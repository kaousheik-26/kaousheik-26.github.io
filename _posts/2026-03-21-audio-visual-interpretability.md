---
layout: post
title: "Do Audio-Visual Large Language Models Really See and Hear?"
date: 2026-03-21 09:00:00 -0400
tags: avllm interpretability audio visual multimodal research
image: https://kaousheik-26.github.io/assets/cvpr/blog_teaser.png
permalink: /blog/2026/audio-visual-interpretability/
---

# Do Audio-Visual Large Language Models Really See and Hear?

**March 21, 2026**

*AVLLMs encode rich audio semantics internally—but systematically suppress them in favor of vision during generation.*

**Authors:** Ramaneswaran Selvakumar, Kaousheik Jayakumar, S Sakshi, Sreyan Ghosh, Ruohan Gao, Dinesh Manocha  
**Affiliation:** University of Maryland, College Park  
[Paper](#) · [Code](#)

---

AVLLMs have made remarkable progress in jointly processing video and audio. But how do they actually integrate these modalities internally? That mechanism has remained a black box.

When we stress-test them, something is clearly wrong. A scene shows a car and a woman walking a dog, but the only sound is an off-screen ambulance siren. AVLLMs **hallucinate sounds from visible objects**—and miss the actual siren. They see, then *guess* what they should be hearing.

![Visual bias in action. Visible objects are silent; the only real sound is an off-screen siren. The AVLLM hallucinates audio from what it sees.]({{ site.url }}/assets/cvpr/blog_teaser.png)

On counterfactual samples where audio and visual content conflict, audio captioning drops by **up to 56%**. We set out to understand why.

> **tl;dr** — Audio tokens encode **rich semantics** internally. Both modalities transfer to generated text in **deeper layers**. But vision gets systematic preference—blocking it *recovers* audio understanding. The bias stems from training, not architecture.

---

## How We Study This

In natural videos, audio and visual content are correlated. To isolate each modality, we construct **counterfactual samples** by swapping a video's audio with an unrelated track. We curate 500 samples from AudioCaps (equal factual/counterfactual split), primarily testing Qwen2.5-Omni (3B) with validation across four additional models.

`[Video: Counterfactual sample — mismatched audio and visual content]`

We evaluate using an **LLM-as-judge** (Qwen3-32B) that scores audio and video caption fidelity separately (0–1), with strong human correlation (ρ = 0.816 audio, ρ = 0.732 video).

<details>
<summary>More on evaluation methodology</summary>

We prompt models with *"describe what you see and hear"* for joint captioning, and modality-specific prompts to isolate each channel. Traditional metrics (BLEU, CIDEr) fail to capture semantic variability. The LLM judge reasons over objects, actions, temporal ordering, and audio events before scoring, calibrated with few-shot examples.

</details>

---

## Findings

### Does the model pay attention to audio?

We've seen that audio captioning collapses when audio and visual content conflict. But this raises a more basic question: does the model even *attend* to audio tokens during generation, or is it effectively ignoring them from the start? If the model never looks at audio, the hallucinations would be unsurprising—it would simply be guessing from vision alone.

To test this, we track the **mean attention** that generated tokens allocate to each input modality—video tokens, audio tokens, and query text tokens—across every transformer layer of the model.

![Mean attention from generated to input tokens. Audio gets 40–50% attention in layers 0–5, then drops to near-zero. Video climbs to 20–40% in layers 15–30.]({{ site.url }}/assets/cvpr/alt_attention_fraction.png)

> **Finding:** The model *does* attend to audio—but only briefly. Audio tokens receive 40–50% of attention in early layers (0–5), which then drops to near-zero. Video attention, by contrast, steadily increases through deeper layers (15–30), reaching 20–40%. Audio is attended to early and then abandoned; vision dominates the layers that matter most for generation.

### Are audio representations meaningful?

Knowing the model looks at audio early on still doesn't tell us whether it *extracts* anything useful. It's possible that attention to audio tokens is superficial—the model might attend without encoding meaningful content. If audio representations are empty, the visual bias would simply reflect a lack of audio understanding.

To find out, we probe audio representations using the **logit lens**. This technique decodes hidden states at each audio token position using the model's unembedding matrix, projecting them into probability distributions over the vocabulary. If the representations are meaningful, they should decode into tokens that describe the actual audio content.

![Probing audio representations. Audio tokens decode into meaningful sound concepts—including multilingual tokens like 键盘 (keyboard).]({{ site.url }}/assets/cvpr/logit_lens_diagram.png)

> **Finding:** Audio representations decode into interpretable tokens that capture sound sources (*drill*, *engine*, *keyboard*) and actions (*typing*, *neighing*)—even in multiple languages (键盘/keyboard, 马/horse). Measuring this systematically, the model achieves **61.4% latent audio understanding** from its internal representations—yet generated captions hit only **23% audio fidelity** on counterfactual samples. The model *hears* and encodes what it hears. It just doesn't use it.

### How does cross-modal information flow?

So the model attends to audio early, and encodes meaningful audio semantics internally. But somewhere between those internal representations and the final generated text, audio gets lost. Where exactly does this happen? And critically—is vision merely *preferred* over audio, or does it actively *suppress* it?

To trace the flow, we use **attention knockout**—a causal intervention that selectively blocks attention from generated tokens to either audio (G↛A) or video (G↛V) at specific layers, then measures the impact on caption quality. If blocking a modality at a given layer degrades the output, that modality was contributing there. If blocking it *improves* the output, it was actively interfering.

![Attention knockout. Blocking video in deeper layers improves audio understanding by ~50%—vision actively suppresses audio.]({{ site.url }}/assets/avllm_fig_knockout.png)

> **Finding:** Both modalities integrate into generated text in the **deeper layers** of the network. Blocking audio in these layers degrades audio captioning as expected. But the striking result: blocking *video* in deeper layers **improves audio understanding by ~50%**, recovering it to near factual-setting levels. Vision doesn't just win over audio—it actively suppresses it during cross-modal integration.

### Where does the vision bias originate?

We now know that vision dominates audio in the final layers. But *why*? Is this an inherent architectural limitation—something about how transformers fuse modalities—or is it a learned behavior that comes from training? Most AVLLMs initialize from pretrained vision-language models (LVLMs) and add audio adapters, or train on datasets heavily skewed toward vision-language examples. The model may simply inherit strong visual priors that audio training never overcomes.

To test this, we compare the **output token distributions** of Qwen2.5-Omni (the AVLLM, with audio input) against Qwen2.5-VL (its base vision-only model, no audio). For each generated token, we measure whether the AVLLM's prediction shifts away from what the vision-only model would predict. If audio meaningfully influences generation, we should see significant distributional shifts.

![Token distribution analysis. Hallucinated audio tokens match the vision-only model's predictions. Genuinely audio-derived tokens shift away.]({{ site.url }}/assets/avllm_fig_distribution.png)

> **Finding:** The KL divergence between the AVLLM and its base LVLM is just 0.4—remarkably similar. Of tokens describing audio events, 66% are *unshifted* (identical top prediction as the vision-only model), and **85% fall within the vision-only model's top 3 predictions**. When the model does correctly identify audio-only content (e.g., "child speaking"), those tokens shift away from the LVLM distribution—confirming that genuine audio processing produces distributional shifts, but it rarely happens. The visual bias stems from training—LVLM initialization and vision-heavy data—not architecture.

---

## Audio Fidelity Across Models

| Model | Factual | Counterfactual | Drop |
|---|---|---|---|
| Qwen2.5-Omni (3B) | 53.58 | 23.10 | −57% |
| Qwen2.5-Omni (7B) | 57.36 | 25.94 | −55% |
| Qwen3-Omni | 58.27 | 36.72 | −37% |
| VideoLLaMA 2.1 | 53.02 | 22.61 | −57% |
| MiniCPM-o 2.6 | 47.46 | 20.74 | −56% |

---

## Implications

**Better evaluation.** Aligned benchmarks mask visual bias. Counterfactual protocols are essential.

**Balanced training.** AVLLMs need balanced data and counterfactual samples to penalize visual shortcuts.

**Architectural interventions.** Deeper layers suppress audio—regularization can preserve it through the forward pass.

> *Current AVLLMs can see and hear—but they choose vision, even for audio tasks. The audio understanding is already there. The challenge is getting models to actually use it.*

---

## Citation

```
@article{selvakumar2026avllm,
  title={Do Audio-Visual Large Language Models Really See and Hear?},
  author={Selvakumar, Ramaneswaran and Jayakumar, Kaousheik and
          Sakshi, S and Ghosh, Sreyan and Gao, Ruohan and Manocha, Dinesh},
  year={2026}
}
```

---

