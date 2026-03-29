# Do Audio-Visual Large Language Models Really See and Hear?

**March 21, 2026**

*AVLLMs encode rich audio semantics internally—but systematically suppress them in favor of vision during generation.*

**Authors:** Ramaneswaran Selvakumar, Kaousheik Jayakumar, S Sakshi, Sreyan Ghosh, Ruohan Gao, Dinesh Manocha  
**Affiliation:** University of Maryland, College Park  
[Paper](#) · [Code](#)

---

AVLLMs have made remarkable progress in jointly processing video and audio. But how do they actually integrate these modalities internally? That mechanism has remained a black box.

When we stress-test them, something is clearly wrong. A scene shows a car and a woman walking a dog, but the only sound is an off-screen ambulance siren. AVLLMs **hallucinate sounds from visible objects**—and miss the actual siren. They see, then *guess* what they should be hearing.

![Visual bias in action. Visible objects are silent; the only real sound is an off-screen siren. The AVLLM hallucinates audio from what it sees.](teaser.png)

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

We track **mean attention** from generated tokens to each input modality across all transformer layers.

![Mean attention from generated to input tokens. Audio gets 40–50% attention in layers 0–5, then drops to near-zero. Video climbs to 20–40% in layers 15–30.](attention-1.png)

> **Finding:** AVLLMs attend to audio only in early layers (0–5), then abandon it. Vision dominates the deeper layers that matter most for generation.

### Are audio representations meaningful?

We probe audio representations using the **logit lens**—decoding hidden states at audio token positions into vocabulary tokens via the unembedding matrix.

![Probing audio representations. Audio tokens decode into meaningful sound concepts—including multilingual tokens like 键盘 (keyboard).](logit_lens-1.png)

> **Finding:** Internal representations achieve **61.4% latent audio understanding**—yet generated captions hit only **23% audio fidelity** on counterfactual samples. The model hears but doesn't use what it hears.

### How does cross-modal information flow?

We use **attention knockout**—blocking attention from generated tokens to audio (G↛A) or video (G↛V) at specific layers—and measure the impact on captions.

![Attention knockout. Blocking video in deeper layers improves audio understanding by ~50%—vision actively suppresses audio.](placeholder-fig-knockout.png)

> **Finding:** Both modalities integrate in deeper layers, but **vision actively suppresses audio**. Blocking visual pathways recovers latent audio understanding.

### Where does the vision bias originate?

We compare **output token distributions** of Qwen2.5-Omni against its base vision-only model Qwen2.5-VL.

![Token distribution analysis. Hallucinated audio tokens match the vision-only model's predictions. Genuinely audio-derived tokens shift away.](placeholder-fig-distribution.png)

> **Finding:** **85% of audio-related tokens are predictable from vision alone.** The bias stems from training—LVLM initialization and vision-heavy data—not architecture.

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
