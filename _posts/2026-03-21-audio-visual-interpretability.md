---
layout: post
title: "Do Audio-Visual Large Language Models Really See and Hear?"
date: 2026-03-21 09:00:00 -0400
permalink: /blog/2026/audio-visual-interpretability/
tags: interpretability multimodal audio-visual LLMs mechanistic CVPR research
image: https://kaousheik-26.github.io/assets/avllm_blog_teaser.png
---

We present the first mechanistic interpretability study of Audio-Visual Large Language Models (AVLLMs), investigating how audio and visual features evolve and fuse through layers to produce text.

**Paper**: [Do Audio-Visual Large Language Models Really See and Hear?](https://drive.google.com/file/d/1tZT3rtrjQoTdRRwAwFsTVYlweaXaTKO4/view?usp=sharing)

**Authors**: Ramaneswaran Selvakumar\*, Kaousheik Jayakumar\*, S Sakshi, Sreyan Ghosh, Ruohan Gao, Dinesh Manocha (\*equal contribution)

**Affiliation**: University of Maryland, College Park

---

## tl;dr

AVLLMs like Qwen2.5-Omni and Qwen3-Omni can process both audio and video — but **do they *really* hear?**

1. AVLLMs **encode rich audio semantics** internally, but **deeper layers disproportionately privilege vision**, suppressing audio cues during generation.
2. Audio performance **drops by up to 56%** when audio and visual content conflict.
3. The AVLLM's output distribution **mirrors its base vision-language model**, suggesting visual bias stems from training.

**The takeaway: current AVLLMs *can* hear, but they choose not to when the eyes disagree.**

---

## The Problem: Vision Dominates Audio

Consider a self-driving car that sees a blue car and a woman walking a dog, but the actual sound is an **off-screen ambulance siren**. Existing AVLLMs consistently hallucinate sounds from *visible* objects while missing the real audio.

![teaser]({{ site.url }}/assets/teaser_cvpr.png)

This isn't a quirky failure — it reveals that these models **don't integrate audio properly**. They see, and then guess what they should be hearing.

---

## Approach: Four-Stage Mechanistic Analysis

We trace how audio and visual information flows through transformer layers:

1. **Attention Pattern Analysis** — Track attention allocated to audio vs. video tokens across layers.
2. **Logit Lens Probing** — Decode intermediate audio representations to reveal encoded semantics.
3. **Attention Knockout** — Causally block attention to audio or video at specific layers.
4. **Base Model Comparison** — Compare AVLLM outputs against their base vision-language models.

---

## Key Findings

### AVLLMs Hallucinate Based on Vision, Not Audio

When asked *"Describe what you hear,"* AVLLMs fabricate audio descriptions matching the **visual content** rather than the actual audio track. Below: the model sees a helicopter and describes helicopter sounds, ignoring the real audio of a boy talking and a baby yelling.

![attention]({{ site.url }}/assets/avllm_fig_attention.png)

Similarly, for a video of a man speaking at a podium, the model describes speech sounds while the actual audio is motor vehicles accelerating — once again relying entirely on visual cues.

![logitlens]({{ site.url }}/assets/avllm_fig_logitlens.png)

### Audio Fidelity Collapses Under Conflict

We measure Audio Caption Fidelity on factual (naturally aligned) vs. counterfactual (mismatched audio-visual) samples. **All models show massive drops** — up to 56% — when audio conflicts with vision.

![knockout]({{ site.url }}/assets/avllm_fig_knockout.png)

### LLM-as-Judge Evaluation

We use an LLM judge to separately score video and audio caption fidelity. Below is an example: the model achieves reasonable video fidelity (0.75) but poor audio fidelity (0.25), hallucinating *meowing* while missing the actual sounds of a man speaking and music.

![distribution]({{ site.url }}/assets/avllm_fig_distribution.png)

---

## Implications

- **Balanced training**: Future AVLLMs need balanced data mixtures and **counterfactual samples** to penalize visual shortcuts.
- **Architectural interventions**: Deeper layers actively suppress audio — regularization strategies can preserve audio through the full forward pass.
- **Better evaluation**: Standard benchmarks with aligned audio-visual content mask these failures. Counterfactual protocols are essential.

---

## Citation

```
@article{selvakumar2026avllm,
  title={Do Audio-Visual Large Language Models Really See and Hear?},
  author={Selvakumar, Ramaneswaran and Jayakumar, Kaousheik and Sakshi, S and Ghosh, Sreyan and Gao, Ruohan and Manocha, Dinesh},
  year={2026}
}
```
