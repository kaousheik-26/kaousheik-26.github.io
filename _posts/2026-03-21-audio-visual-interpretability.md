---
layout: research-post
title: "Do Audio-Visual Large Language Models Really See and Hear?"
subtitle: "AVLLMs encode rich audio semantics internally—but systematically suppress them in favor of vision during generation."
date: 2026-03-21 09:00:00 -0400
tags: avllm interpretability audio visual multimodal research
image: https://kaousheik-26.github.io/assets/cvpr/blog_teaser.png
permalink: /blog/2026/audio-visual-interpretability/
venue: "CVPR Findings 2026"
authors: "Ramaneswaran Selvakumar*, Kaousheik Jayakumar*, S Sakshi, Sreyan Ghosh, Ruohan Gao#, Dinesh Manocha#"
author_note: "*Equal contribution &nbsp;&nbsp; #Equal advising"
affiliation: "University of Maryland, College Park"
project_url: https://ramaneswaran.github.io/avllm_interpretability/
paper_url: https://arxiv.org/abs/2604.02605
code_url: https://github.com/ramaneswaran/avllm_interpretability
dataset_url: https://huggingface.co/datasets/gamma-lab-umd/counterfactual-av-eval
---

<div class="text-figure-row">
  <div class="tf-text">

AVLLMs have made remarkable progress in jointly understanding audio and visual inputs. But how they actually process and use these modalities internally remains a black box, and this opacity has real consequences.

To see why this matters, consider the safety-critical setting shown on the right: an autonomous vehicle should respond to an off-screen ambulance siren even when it isn't visible. Current AVLLMs would likely fail here—when we stress-test them on scenarios where audio and visual content conflict, they hallucinate sounds from visible objects and miss the actual audio entirely. They have a bias to see, then *guess* what they should be hearing.

We curate an evaluation set consisting of such counterfactual samples where audio and visual content conflict, and observe that audio captioning performance drops by **up to 56%**. We then conduct a systematic mechanistic analysis to understand why this happens.

  </div>
  <figure class="tf-figure">
    <img src="{{ site.url }}/assets/cvpr/blog_teaser.png" alt="Visual bias in action">
    <figcaption><strong>Figure 1.</strong> Visual bias in action. Visible objects are silent; the only real sound is an off-screen siren. The AVLLM hallucinates audio from what it sees.</figcaption>
  </figure>
</div>

---

## How We Study This

**Task:** We ask AVLLMs to describe what they see and hear—a simple task, but one that directly forces the model to use both modalities. And unlike multiple choice or binary QA, free-form captions are interpretable.

**Dataset:** In natural videos, audio and visual content are correlated, so vision can confound audio understanding—i.e., the model can infer sounds just from what it sees. To prevent this, we construct **counterfactual samples** by swapping a video's audio with a semantically unrelated track. We curate 500 samples from AudioCaps, half factual, half counterfactual.

**Evaluation:** Evaluating free-form captions at scale is hard. We use an **LLM-as-judge** that scores audio and video fidelity separately on a 0–1 scale. It is scalable, and has strong correlation with human judgements (ρ = 0.816 audio, ρ = 0.732 video).

---

## Findings

### Does the model pay attention to audio?

<div class="text-figure-row">
  <div class="tf-text">

Before asking why audio fails, a more basic question: does the model even *attend* to audio tokens during generation, or is it effectively ignoring them from the start? If the model never looks at audio, the hallucinations would be unsurprising—it would simply be guessing from vision alone.

To test this, we track the **mean attention** that generated tokens allocate to each input modality—video tokens, audio tokens, and query text tokens—across every transformer layer of the model.

The result is surprising: the model *does* attend to audio—but only briefly. Audio tokens receive 40–50% of attention in early layers (0–5), then drop to near-zero. Visual attention, by contrast, steadily climbs through deeper layers (15–30), reaching 20–40%. This suggests the model processes audio early on but progressively discards it in favor of visual information as it moves toward generating output tokens.

  </div>
  <figure class="tf-figure">
    <img src="{{ site.url }}/assets/cvpr/alt_attention_fraction.png" alt="Attention fraction across layers">
    <figcaption><strong>Figure 2.</strong> Mean attention from generated to input tokens. Audio gets 40–50% attention in layers 0–5, then drops to near-zero. Video climbs to 20–40% in layers 15–30.</figcaption>
  </figure>
</div>

> **Finding:** The model *does* attend to audio—but only briefly. Audio dominates early layers, then gets suppressed as visual attention takes over in deeper layers.

### Are audio representations meaningful?

We've established that the model does attend to audio tokens, albeit briefly. Next, we ask whether those audio tokens actually encode anything meaningful to begin with. If the representations are not meaningful, the visual bias would simply reflect a lack of useful audio signal, not a failure to use it.

To find out, we probe audio representations using the **logit lens**. This technique decodes hidden states at each audio token position using the model's unembedding matrix, projecting them into probability distributions over the vocabulary. If the representations are meaningful, they should decode into tokens that describe the actual audio content.

<figure>
  <img src="{{ site.url }}/assets/cvpr/logit_lens_diagram.png" alt="Logit lens probing">
  <figcaption><strong>Figure 3.</strong> Probing audio representations. Audio tokens decode into meaningful sound concepts—including multilingual tokens like 键盘 (keyboard).</figcaption>
</figure>

> **Finding:** Audio representations decode into interpretable tokens that capture sound sources (*drill*, *engine*, *keyboard*) and actions (*typing*, *neighing*)—even in multiple languages (键盘/keyboard, 马/horse). Measuring this systematically, the model achieves **61.4% latent audio understanding** from its internal representations—yet generated captions hit only **23% audio fidelity** on counterfactual samples. The audio understanding is there internally—it just isn't making it to the output.

### How does cross-modal information flow?

So the model attends to audio, and encodes meaningful audio semantics internally. But somewhere between those internal representations and the final generated text, audio gets lost. Where exactly does this happen?

To trace this, we use **attention knockout**—a causal intervention that selectively blocks attention from generated tokens to either audio (G↛A) or video (G↛V) at specific layers. The logic is simple: if blocking a modality at a given layer degrades the output, that modality was actively contributing there.

**Factual samples:** When we block either modality, the model compensates using the other—performance recovers either way. This demonstrates audio-visual complementarity, but also reveals why factual samples alone are insufficient for evaluation. The modalities are so correlated that the model can always lean on one to cover for the other—which is exactly why counterfactuals are necessary.

**Counterfactual samples:** Here the modalities conflict, so compensation is impossible. Blocking video causes a clear drop in video understanding, concentrated in mid-to-deep layers—telling us where visual information transfers to generated text. For audio understanding, blocking audio produces a similar drop in the same mid-to-deep layers, confirming audio transfers there too. But the critical finding: **blocking video actually improves audio understanding by ~50%**, recovering it to near factual-setting levels. When both modalities compete in those deeper layers, vision wins—and audio pays the price.

### Where does the vision bias originate?

We know vision dominates in the final layers. But is this because audio training never really changed the model's behavior to begin with—leaving it fundamentally a vision-language model with audio bolted on?

To test this, we compare the **output token distributions** of Qwen2.5-Omni (the AVLLM, with audio input) against Qwen2.5-VL (its base vision-only model, no audio). For each generated token, we measure whether the AVLLM's prediction shifts away from what the vision-only model would predict. If audio meaningfully influences generation, we should see significant distributional shifts.

> **Finding:** The distributions are remarkably similar—KL divergence of just 0.4. Of tokens describing audio events, 66% are *unshifted* (identical top prediction as the vision-only model), and **85% fall within the vision-only model's top 3 predictions**. Notably, when the model does correctly identify audio content, those tokens *do* shift away from the base LVLM distribution, confirming that genuine audio processing produces distributional shifts. But the model still defaults to its visual priors more often than it should, particularly under conflict.

We can see this bias in action by visualizing the **cross-modal attention** during generation. The two examples below are counterfactual samples where the model is instructed to **"Describe what you hear."** In both cases, it ignores the actual audio and instead generates audio descriptions by attending directly to visible objects in the video frames.

<div class="figure-row">
  <figure>
    <img src="{{ site.url }}/assets/cvpr/attention_helicopter.png" alt="Attention heatmap: helicopter example">
    <figcaption><strong>(a)</strong> The actual audio is a young boy talking as a baby yells — but the model generates "I hear <em>the sound of a helicopter</em>," with attention concentrated on the helicopter in the video frames.</figcaption>
  </figure>
  <figure>
    <img src="{{ site.url }}/assets/cvpr/attention_speech.png" alt="Attention heatmap: speech example">
    <figcaption><strong>(b)</strong> The actual audio is several motor vehicles accelerating — but the model generates "I hear <em>a man speaking into a microphone</em>," with attention locked onto the man and microphone in the video.</figcaption>
  </figure>
</div>

The attention heatmaps reveal that when generating audio-describing tokens, the model's attention flows directly to **visually salient objects** — the helicopter, the man with the microphone — rather than to the audio tokens. It is performing visual object recognition and translating the result into plausible sound descriptions, bypassing the audio modality entirely.

---

## Qualitative Examples

Below are two examples that vividly illustrate the visual-to-audio hallucination phenomenon. In each case, we show the **factual** (original matched audio) and **counterfactual** (swapped unrelated audio) conditions side by side. The model produces correct visual descriptions in both—but in the counterfactual setting, it fabricates audio based on what it *sees* rather than reporting what it actually *hears*.

### Example 1: Person Typing on a Keyboard

<div class="example-card">
  <div class="example-header">
    <div class="example-title">ID 151 — Office Keyboard Typing</div>
    <span class="model-badge">Qwen2.5-Omni 7B</span>
  </div>
  <div class="pair-grid">
    <!-- Factual -->
    <div class="pair-cell">
      <div class="condition-badge badge-factual"><span class="dot"></span> Factual</div>
      <div class="video-slot">
        <iframe src="https://www.youtube.com/embed/f0Zhcv4P5Lg" allowfullscreen></iframe>
      </div>
      <div class="info-block">
        <div class="info-label">Video Description</div>
        <div class="info-text">A person typing on a keyboard at a desk in an office cubicle. The view is from the side, focusing on the hands and keyboard.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Audio (Ground Truth)</div>
        <div class="info-text">Typing is occurring on a keyboard in a quiet environment.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Model Output</div>
        <div class="model-output">Well, I see a close-up of a person's hands typing on a black keyboard. There's a computer monitor in the background, and it seems like there's a piece of paper on the desk too. I can hear <span class="correct-audio">the sound of the keys being pressed</span>, which is pretty clear. It gives off the vibe of someone working on a computer, maybe typing an email or writing a document.</div>
      </div>
    </div>
    <!-- Counterfactual -->
    <div class="pair-cell">
      <div class="condition-badge badge-cf"><span class="dot"></span> Counterfactual</div>
      <div class="video-slot">
        <iframe src="https://www.youtube.com/embed/xtlM1ON6q64" allowfullscreen></iframe>
      </div>
      <div class="info-block">
        <div class="info-label">Video Description</div>
        <div class="info-text">Same video — a person typing on a keyboard at a desk in an office cubicle.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Audio (Swapped — Ground Truth)</div>
        <div class="info-text">A train running on railroad tracks, followed by a lawn mower engine, then a steam engine whistle blowing as a crowd of people talk.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Model Output</div>
        <div class="model-output">Well, I see a close-up of a person's hands typing on a black keyboard. There's a computer monitor in the background, and it seems like there's a piece of paper on the desk too. I can hear <span class="hallucinated">the sound of the keyboard keys clicking</span> as the person types. It's a pretty focused scene.</div>
      </div>
    </div>
  </div>
  <div class="analysis-box">
    <div class="info-label">⚠ Analysis — Visual-to-Audio Hallucination</div>
    <div class="analysis-text">The model produces <strong>near-identical outputs</strong> for both conditions. In the factual case, hearing "the sound of the keys being pressed" is correct — the original audio contains keyboard typing. In the counterfactual case, the audio has been replaced with <strong>trains, lawn mowers, and a steam whistle</strong> — yet the model still reports hearing "keyboard keys clicking." The visual content of hands on a keyboard is enough for the model to fabricate matching audio, completely ignoring the actual soundtrack.</div>
  </div>
</div>

### Example 2: Ducklings Swimming in a Pond

<div class="example-card">
  <div class="example-header">
    <div class="example-title">ID 495 — Ducklings Swimming</div>
    <span class="model-badge">Qwen2.5-Omni 3B</span>
  </div>
  <div class="pair-grid">
    <!-- Factual -->
    <div class="pair-cell">
      <div class="condition-badge badge-factual"><span class="dot"></span> Factual</div>
      <div class="video-slot">
        <iframe src="https://www.youtube.com/embed/7EK501R_jbQ" allowfullscreen></iframe>
      </div>
      <div class="info-block">
        <div class="info-label">Video Description</div>
        <div class="info-text">A group of ducklings swimming closely around an adult duck, likely their mother, in water.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Audio (Ground Truth)</div>
        <div class="info-text">Birds are chirping, and ducks are making noises.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Model Output</div>
        <div class="model-output">I see a bunch of ducks in the water. There's a big duck in the middle, and a bunch of smaller ones around it. They're all moving around in the water. I also hear <span class="correct-audio">some quacking and a few other bird sounds</span>. It looks like a peaceful scene.</div>
      </div>
    </div>
    <!-- Counterfactual -->
    <div class="pair-cell">
      <div class="condition-badge badge-cf"><span class="dot"></span> Counterfactual</div>
      <div class="video-slot">
        <iframe src="https://www.youtube.com/embed/4wnLiIxJZzc" allowfullscreen></iframe>
      </div>
      <div class="info-block">
        <div class="info-label">Video Description</div>
        <div class="info-text">Same video — ducklings swimming closely around a mother duck in water.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Audio (Swapped — Ground Truth)</div>
        <div class="info-text">A man speaks followed by a toilet flush.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Model Output</div>
        <div class="model-output">I see ducks floating on the water, with a larger one in the center and smaller ones around it. They move gently, creating a calm scene. I hear <span class="hallucinated">quacking and other bird sounds</span>.</div>
      </div>
    </div>
  </div>
  <div class="analysis-box">
    <div class="info-label">⚠ Analysis — Visual-to-Audio Hallucination</div>
    <div class="analysis-text">The model produces <strong>near-identical outputs</strong> across both conditions. In the factual case, "quacking and a few other bird sounds" is correct — the original audio contains ducks and birds. In the counterfactual case, the audio is <strong>a man speaking followed by a toilet flush</strong> — entirely unrelated to wildlife. Yet the model still confidently reports hearing "quacking and other bird sounds." It sees ducks and fabricates the expected duck audio, completely ignoring the actual soundtrack.</div>
  </div>
</div>

### Example 3: Cooking in a Frying Pan

<div class="example-card">
  <div class="example-header">
    <div class="example-title">ID 437 — Food Sizzling in a Pan</div>
    <span class="model-badge">VideoLLaMA2 7B</span>
  </div>
  <div class="pair-grid">
    <!-- Factual -->
    <div class="pair-cell">
      <div class="condition-badge badge-factual"><span class="dot"></span> Factual</div>
      <div class="video-slot">
        <iframe src="https://www.youtube.com/embed/DV2AYHNCCFk" allowfullscreen></iframe>
      </div>
      <div class="info-block">
        <div class="info-label">Video Description</div>
        <div class="info-text">A frying pan with food in it. The food is being stirred with a spatula on a stove.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Audio (Ground Truth)</div>
        <div class="info-text">A woman talking followed by plastic thumping, then metal clanking as food and oil sizzles.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Model Output</div>
        <div class="model-output">The video shows a person cooking food in a pan on a stove. The main source of sound in the video is <span class="correct-audio">the sizzling and crackling of the food as it cooks</span>.</div>
      </div>
    </div>
    <!-- Counterfactual -->
    <div class="pair-cell">
      <div class="condition-badge badge-cf"><span class="dot"></span> Counterfactual</div>
      <div class="video-slot">
        <iframe src="https://www.youtube.com/embed/K7Fl8E6bxQw" allowfullscreen></iframe>
      </div>
      <div class="info-block">
        <div class="info-label">Video Description</div>
        <div class="info-text">Same video — a frying pan with food being stirred with a spatula on a stove.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Audio (Swapped — Ground Truth)</div>
        <div class="info-text">A series of snores followed by subdued laughter and another snore.</div>
      </div>
      <div class="info-block">
        <div class="info-label">Model Output</div>
        <div class="model-output">The video shows a person cooking food in a pan on a stove. The main source of sound in the video is <span class="hallucinated">the sizzling and crackling of of the food as it cooks</span>.</div>
      </div>
    </div>
  </div>
  <div class="analysis-box">
    <div class="info-label">⚠ Analysis — Visual-to-Audio Hallucination</div>
    <div class="analysis-text">The model produces <strong>virtually identical outputs</strong> for both conditions — the only difference is a stray typo ("of of"). In the factual case, "sizzling and crackling" is correct — the original audio includes food and oil sizzling. In the counterfactual case, the audio has been replaced with <strong>snoring and laughter</strong> — yet the model still reports sizzling cooking sounds. The visual prior of a frying pan is so dominant that it completely overwrites the actual audio signal.</div>
  </div>
</div>

---

## Citation

<div class="citation-block">
  <div class="cite-label">BibTeX</div>
  <pre>@misc{selvakumar2026audiovisuallargelanguagemodels,
      title={Do Audio-Visual Large Language Models Really See and Hear?}, 
      author={Ramaneswaran Selvakumar and Kaousheik Jayakumar and S Sakshi and Sreyan Ghosh and Ruohan Gao and Dinesh Manocha},
      year={2026},
      eprint={2604.02605},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2604.02605}, 
}</pre>
</div>