---
layout: post
title: "Do Audio-Visual Large Language Models Really See and Hear?"
date: 2026-03-21 09:00:00 -0400
permalink: /blog/2026/audio-visual-interpretability/
tags: interpretability multimodal audio-visual LLMs mechanistic CVPR research
image: https://kaousheik-26.github.io/assets/avllm_blog_teaser.png
---

We present the first mechanistic interpretability study of Audio-Visual Large Language Models (AVLLMs), investigating how audio and visual features evolve and fuse through different layers to produce text. Our findings reveal a fundamental modality bias — AVLLMs encode rich audio semantics internally but fail to surface them in generation when audio conflicts with vision.

**Paper**: [Do Audio-Visual Large Language Models Really See and Hear?](https://drive.google.com/file/d/1tZT3rtrjQoTdRRwAwFsTVYlweaXaTKO4/view?usp=sharing)

**Authors**: Ramaneswaran Selvakumar\*, Kaousheik Jayakumar\*, S Sakshi, Sreyan Ghosh, Ruohan Gao, Dinesh Manocha (\*equal contribution)

**Affiliation**: University of Maryland, College Park

---

## tl;dr

Audio-Visual LLMs (AVLLMs) like Qwen2.5-Omni and Qwen3-Omni can process both audio and video inputs. But **do they *really* hear?** We perform a systematic mechanistic interpretability analysis and find:

1. AVLLMs **encode rich audio semantics** in their intermediate layers — audio tokens decode into meaningful onomatopoeic descriptions of sound events.
2. Despite this, **deeper layers disproportionately privilege vision**, actively suppressing audio cues during generation.
3. Audio performance **drops by up to 56%** when audio and visual content conflict (counterfactual samples).
4. The AVLLM's output distribution **strongly mirrors its base vision-language model**, suggesting that the visual bias stems from training rather than architectural limitations.

The takeaway: current AVLLMs *can* hear, but they choose not to when the eyes disagree.

---

## Motivation: Why Does This Matter?

AVLLMs are emerging as unified interfaces for multimodal perception — from video understanding to embodied agents. But what happens when audio and visual cues *conflict*?

Consider a safety-critical scenario: a self-driving car sees a blue car and a woman walking a dog, but the actual audible sound is an **off-screen ambulance siren**. When asked to describe the scene, existing AVLLMs consistently hallucinate sounds from the *visible* objects (car engine, dog barking) while completely missing the real siren.

This isn't just a quirky failure — it reveals that these models fundamentally **don't integrate audio properly**. They see, and then they guess what they should be hearing based on what they see.

To understand *why* and *where* this happens, we open the black box.

---

## Approach: A Four-Stage Mechanistic Analysis

We design a systematic pipeline to trace how audio and visual information flows through the transformer layers of an AVLLM:

### 1. Attention Pattern Analysis
We track the average attention that generated tokens allocate to audio, video, and text input tokens across all transformer layers. This tells us *where* the model is looking (and listening).

### 2. Probing Audio Representations
Using the **logit lens** technique, we decode intermediate-layer audio token representations through the LLM's unembedding matrix. This reveals *what information* is encoded in audio representations at each layer.

### 3. Attention Knockout Experiments
We perform **causal mediation analysis** by selectively blocking (knocking out) attention to audio or visual tokens at specific layers. This establishes *causal relationships* — does blocking vision actually help audio surface?

### 4. Comparing with Base Vision-Language Models
We compare the AVLLM's output token distributions against its base LVLM (e.g., Qwen2.5-Omni vs. Qwen2.5-VL) to test whether the visual bias is inherited from pre-training.

---

## Key Findings

### Audio Gets Attention Early — Then Gets Ignored

Generated tokens allocate **40–50% attention to audio in early layers (0–5)**, but this drops to **near-zero** afterward. In contrast, video attention steadily increases through deeper layers (15–30), reaching 20–40%. This creates a striking asymmetry: by the time the model generates text, it's almost exclusively looking at vision.

### Audio Representations Are Surprisingly Rich

Here's the twist: when we probe the audio token representations in intermediate layers using the logit lens, they **decode into meaningful concepts** describing sound events — in multiple languages! For example, audio tokens for keyboard sounds decode into tokens like "键盘" (keyboard) and "typing". The model *knows* what it hears; it just doesn't *use* that information.

### Blocking Vision Restores Audio Understanding

Our attention knockout experiments provide the smoking gun. When we **block visual attention in deeper layers** (layers 15–35), audio captioning performance **dramatically improves** — demonstrating that vision doesn't just dominate, it actively *suppresses* audio information. Conversely, blocking audio in early layers has little to no effect, confirming that audio's early-layer representations don't contribute meaningfully to the final output.

### The Bias Comes from Training, Not Architecture

By comparing AVLLM outputs with their base LVLMs, we find that the output token distributions are **remarkably similar**. The tokens that describe genuinely audio-only events (like an off-screen sound) show the highest distributional shift, while visually-grounded tokens remain almost identical between the two models. This strongly suggests that the modality bias **originates from the vision-language pre-training and alignment** — the model inherits its vision-first behavior rather than developing it from architectural constraints.

---

## Implications and Future Directions

Our findings point to a clear path forward:

- **Balanced training data**: Future AVLLM training must address modality imbalance through either balanced data mixtures or introducing **counterfactual samples** to penalize visual shortcuts.
- **Architectural interventions**: Understanding that deeper layers actively suppress audio opens the door to regularization strategies that preserve audio information through the full forward pass.
- **Better evaluation**: Standard benchmarks with naturally aligned audio-visual content mask these failures. Counterfactual evaluation protocols are essential for measuring genuine multimodal reasoning.

We believe these mechanistic insights provide a foundation for building AVLLMs that truly *see and hear*.

---

## Citation

```
@article{selvakumar2026avllm,
  title={Do Audio-Visual Large Language Models Really See and Hear?},
  author={Selvakumar, Ramaneswaran and Jayakumar, Kaousheik and Sakshi, S and Ghosh, Sreyan and Gao, Ruohan and Manocha, Dinesh},
  year={2026}
}
```
