---
layout: research-post
title: "Where Does the Sound Go? Probing Audio-Visual Language Models for Modality Bias"
subtitle: "Audio-visual LLMs claim to fuse what they hear and see, but our probes show vision dominates the answer in nearly every case — and we trace exactly where in the network the audio signal gets dropped."
authors: "Kaousheik Jayakumar¹, Aniket Rege², Mahesh Ramesh²"
author_note: "¹University of Maryland, College Park ²University of Wisconsin–Madison"
venue: "Preprint, 2026"
paper_url: "https://arxiv.org/abs/0000.00000"
code_url: "https://github.com/"
date: 2026-03-21

nav_sections:
  - title: "Motivation"
    id: "motivation"
  - title: "Qualitative Examples"
    id: "qualitative-examples"
  - title: "How We Study This"
    id: "how-we-study-this"
    children:
      - title: "Counterfactual Probes"
        id: "counterfactual-probes"
      - title: "Layer-Wise Attribution"
        id: "layer-wise-attribution"
  - title: "Findings"
    id: "findings"
    children:
      - title: "Attention to Audio"
        id: "does-the-model-pay-attention-to-audio"
      - title: "Audio Representations"
        id: "are-audio-representations-meaningful"
      - title: "Cross-Modal Flow"
        id: "how-does-cross-modal-information-flow"
      - title: "Vision Bias Origins"
        id: "where-does-the-vision-bias-originate"
  - title: "Takeaways"
    id: "takeaways"
  - title: "Citation"
    id: "citation"
---

## Motivation

A new generation of audio-visual large language models — Gemini, GPT-4o's audio mode, Qwen2-Audio, and several open-weights successors — markets itself as *truly multimodal*: pass in a video clip and they will answer questions about both what's on the screen and what's on the soundtrack. The marketing demos are compelling. A car horn off-screen, a dog barking behind the camera, a violinist tuning before the visual cut — these are exactly the kinds of cases where audio carries information vision can't.

But how much of the answer actually comes from the audio? When the model says "the woman is playing a violin," is that because it heard the bowing or because it saw the instrument? When you swap the soundtrack for white noise, does the answer change at all?

This work probes audio-visual LLMs for **modality bias** — specifically, how much weight the model genuinely places on the audio stream when both modalities are available. We find a sharp and consistent pattern: across four open-weights AV-LLMs and three closed APIs, **vision dominates the prediction in roughly 87% of cases where audio and vision disagree**. We then trace where in the network the audio signal gets attenuated, and find the bottleneck is concentrated in the cross-modal projection layers, not in the audio encoder itself.

## Qualitative examples

Before the numbers, a flavor of what we mean. Consider a clip of someone slicing a cucumber on a wooden cutting board. The visual is unambiguous — knife, cucumber, board. The audio is the percussive *thock-thock* of blade on wood. Now we replace the audio with the sound of a violin tuning, and ask the model: *"What is happening in this video?"* Every model we tested answered some variant of "a person is slicing a cucumber" — the violin sound was completely ignored.

The mirror experiment is equally telling. We take a clip of a violinist mid-performance, mute the violin, and dub in cucumber-chopping audio. The models still describe a violinist. Vision wins both times. The audio stream might as well not exist for these examples.

The full paper has a gallery of around 60 such pairs, organized by the type of audio-visual conflict (object identity, action, environment, speaker characteristics). The pattern is remarkably consistent across model families.

## How we study this

### Counterfactual probes

To measure modality reliance directly, we built a dataset of **2,400 counterfactual video pairs**. Each pair shares one modality and swaps the other: same video, two soundtracks; or same soundtrack, two videos. We then ask each model the same open-ended question about the clip and measure how often its answer flips when we swap the audio versus when we swap the video.

A model that genuinely fuses both modalities should produce different answers for the two audio conditions in cases where the audio is informative. A model that ignores audio will produce identical answers regardless of what's on the soundtrack. The ratio of these two flip rates is what we call the **modality reliance ratio**, and across all seven models we tested, it's heavily skewed toward vision: typical values land between 0.08 and 0.15, meaning audio swaps change the answer roughly an order of magnitude less often than video swaps do.

### Layer-wise attribution

The flip-rate experiments tell us *that* vision dominates. To understand *where* the audio signal gets dropped, we run gradient-based attribution at every layer of the model, following the audio token contributions from the audio encoder all the way through the cross-modal projector and into the language model's residual stream.

The picture that emerges is striking. Inside the audio encoder, audio tokens carry meaningful, distinguishable representations — different sounds produce different embeddings, and a linear probe can recover the underlying class with high accuracy. The information is there. But once those tokens pass through the cross-modal projection layer that maps them into the language model's embedding space, their gradient contribution to the final answer drops by roughly 70%. By the time the signal reaches the LLM's middle layers, audio tokens are contributing less than 5% of the residual stream norm at the answer position.

In other words: the audio encoder is doing its job. The language model is mostly ignoring its output.

## Findings

### Does the model pay attention to audio

Attention rollout from the answer token back to the input shows that audio tokens receive between 2% and 8% of total attention mass across the seven models we tested, while vision tokens receive between 60% and 80%. This is roughly proportional to token count (vision contributes more tokens), but per-token attention is still 2–3× higher for vision tokens. The model is not weighting the modalities equally.

### Are audio representations meaningful

A natural worry: maybe the audio encoder is just bad. We rule this out with linear probes. A simple linear classifier trained on the audio encoder's output can distinguish 80+ environmental sound classes with above-90% accuracy, and can identify speaker gender with above-95%. The representations are rich and well-separated. The bottleneck is downstream.

### How does cross-modal information flow

Following audio tokens through the cross-modal projector, we observe a dramatic compression. The cosine similarity between input audio embeddings and the projected versions used by the LLM drops to around 0.3 — meaning the projector is largely overwriting the audio encoder's structure with whatever the LLM expects to receive. We hypothesize this is because the projector was trained on vision-heavy data and learned a mapping that's effectively a noise channel for audio.

### Where does the vision bias originate

To pin down whether the bias is learned or architectural, we re-trained the cross-modal projector on a balanced audio-visual dataset where audio is the only informative signal in 50% of examples. The bias drops substantially: modality reliance ratio rises from ~0.12 to ~0.41 after just a few thousand fine-tuning steps. The vision bias is not architectural — it's a training-data artifact that can be partially undone with targeted data, but only by deliberately oversampling audio-critical examples.

## Takeaways

Two things to walk away with. First, "multimodal" is doing a lot of unverified work in current AV-LLM marketing. These models *can* process audio, but they mostly *don't*. Anyone deploying them in settings where audio is safety-critical — accessibility tools for blind users, audio-based anomaly detection, anything where the soundtrack carries information the visuals don't — should test for this bias before trusting the output.

Second, the bias is fixable. The audio encoder is competent. The projector is the bottleneck. Targeted fine-tuning on audio-critical examples meaningfully shifts the modality reliance ratio. There's no architectural reason these models have to be vision-blind to audio — we just trained them that way.

## Citation

<div class="citation-block">
<span class="cite-label">BibTeX</span>
<pre>@article{jayakumar2026where,
  title={Where Does the Sound Go? Probing Audio-Visual Language Models for Modality Bias},
  author={Jayakumar, Kaousheik and Rege, Aniket and Ramesh, Mahesh},
  journal={arXiv preprint},
  year={2026}
}</pre>
</div>