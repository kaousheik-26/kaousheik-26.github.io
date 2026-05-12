---
layout: hanabi-post
permalink: /llms-hanabi-cooperative-reasoning/
title: "Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents"
subtitle: "Even frontier reasoning models are sparks — not flames — of cooperative reasoning. We benchmark 17 LLMs on Hanabi across 2–5 players, introduce three prompting scaffolds and two new datasets, and show a 4B model finetuned on our data closes most of the gap to o4-mini while transferring to temporal reasoning, instruction following, and other cooperative tasks."
authors: "Mahesh Ramesh¹, <span class='me'>Kaousheik Jayakumar²</span>, Aswinkumar Ramkumar¹, Pavan Thodima¹, Aniket Rege¹†, Emmanouil V. Vlatakis-Gkaragkounis¹†"
affiliation: "<span class='star'>★</span> ¹University of Wisconsin–Madison &nbsp;·&nbsp; ²University of Maryland, College Park &nbsp;·&nbsp; †Equal advising"
venue: "ICML 2026"
paper_url: "https://arxiv.org/abs/2601.18077"
code_url: "https://app.primeintellect.ai/dashboard/environments/mahesh-ramesh/hanabi"
dataset_url: "https://huggingface.co/"
date: 2026-03-21

nav_sections:
  - title: "Why Hanabi"
    id: "why-hanabi"
  - title: "Three Scaffolds"
    id: "three-scaffolds"
    children:
      - title: "Watson & Sherlock"
        id: "watson-sherlock"
      - title: "Mycroft"
        id: "mycroft"
  - title: "Benchmark Results"
    id: "benchmark-results"
  - title: "Ablations"
    id: "ablations"
    children:
      - title: "Cross-Play"
        id: "cross-play"
      - title: "Best-of-K"
        id: "best-of-k"
      - title: "Mixture of Agents"
        id: "moa"
  - title: "Post-Training"
    id: "post-training"
    children:
      - title: "Generalization"
        id: "generalization"
  - title: "Takeaways"
    id: "takeaways"
  - title: "Citation"
    id: "citation"
---

## Why Hanabi {#why-hanabi}

Cooperative coordination under partial information is the part of intelligence that single-agent benchmarks miss. **Hanabi** is the canonical testbed: 2–5 players hold cards facing outward — visible to everyone but themselves — and must build five color-ordered "fireworks" using only color or rank hints from a finite pool of information tokens. Success demands theory-of-mind, convention building, and inference under sparse signals.

Specialized RL agents reach ~24/25 in 2-player self-play but degrade sharply with more players or unfamiliar partners. We ask a different question: **how good are general-purpose LLMs as cooperative agents, and what limits them?**

## Three scaffolds {#three-scaffolds}

We progressively scale the context an agent receives, from minimal state to engine-provided deductions to fully implicit multi-turn state tracking. Each scaffold isolates a different capability.

<div class="settings-grid">
  <div class="setting-card">
    <div class="ord">01 · BASELINE</div>
    <h4>Watson</h4>
    <p>Minimal context. Game state, visible hands, explicit knowledge from clues — and nothing else. Establishes a lower bound on what LLMs can do without scaffolding.</p>
  </div>
  <div class="setting-card">
    <div class="ord">02 · SCAFFOLDED</div>
    <h4>Sherlock</h4>
    <p>Adds engine-computed deductive context (per-card "could be" possibilities), Hanabi strategy notes, and a Bayesian step-by-step prompt. Establishes an upper bound with rich prefill.</p>
  </div>
  <div class="setting-card">
    <div class="ord">03 · IMPLICIT</div>
    <h4>Mycroft</h4>
    <p>No engine deductions. The agent must implicitly track its own and teammates' beliefs across turns via a structured "scratch pad" — closer to how humans actually play.</p>
  </div>
</div>

### Watson & Sherlock {#watson-sherlock}

Watson and Sherlock differ in one thing: whether the agent receives a programmatic belief state. Sherlock's deductive context lists, for every card in every hand, the colors and ranks still consistent with the clue history. The agent is then prompted to do Bayesian-style probability reasoning over those candidates before acting.

<figure>
  <img src="{{ site.url }}/assets/icml/sherlock_watson_teaser.png" alt="Watson vs Sherlock prompt comparison">
  <figcaption><strong>Figure 1.</strong> Watson provides only explicit knowledge (clues received). Sherlock additionally provides a Deductive Context block — the per-card belief state — and enforces Bayesian-style step-by-step reasoning.</figcaption>
</figure>

### Mycroft {#mycroft}

Mycroft removes the engine crutch. Each turn the agent receives the previous turn's game state, its own deductions for every player, move ratings, chosen action, and reasoning — then must produce updated deductions, ratings, and an action. This forces the model to be its own Hanabi Learning Environment, tracking belief shifts and card position changes (cards slide left after a play or discard) across 60+ turns.

<figure>
  <img src="{{ site.url }}/assets/icml/mycroft_teaser.png" alt="Mycroft scratch pad example">
  <figcaption><strong>Figure 2.</strong> A Mycroft turn from Player 1's perspective. The agent maintains an independent deduction block for every other player and must update card positions implicitly after plays and discards.</figcaption>
</figure>

## Benchmark results {#benchmark-results}

We evaluate **17 LLMs** (4B–600B+, both reasoning and non-reasoning) across 2–5 player self-play, with 10 fixed seeds per configuration. Reasoning models clear ~13/25 in Watson; non-reasoning models mostly stall below 10/25.


<div class="results-tabbed" id="results-table">

  <!-- Left-side tabs -->
  <div class="results-tabs">
    <button class="results-tab active" data-panel="panel-watson">
      <span class="tab-ord">01 · Baseline</span> Watson
    </button>
    <button class="results-tab" data-panel="panel-sherlock">
      <span class="tab-ord">02 · Scaffolded</span> Sherlock
    </button>
    <button class="results-tab" data-panel="panel-mycroft">
      <span class="tab-ord">03 · Implicit</span> Mycroft
    </button>
  </div>

  <!-- Panels -->
  <div class="results-panels">

    <!-- ─── Watson ─── -->
    <div class="results-panel active" id="panel-watson">
      <div class="results-legend">
        <div class="legend-item"><span class="swatch non-reasoning"></span> Non-reasoning</div>
        <div class="legend-item"><span class="swatch reasoning"></span> Reasoning</div>
      </div>
      <table>
        <thead>
          <tr><th>Model</th><th>2-Player</th><th>3-Player</th><th>4-Player</th><th>5-Player</th></tr>
        </thead>
        <tbody>
          <tr class="non-reasoning"><td>Mistral Medium 3</td><td>2.2</td><td>1.9</td><td>1.7</td><td>1.2</td></tr>
          <tr class="non-reasoning"><td>Gemini 2.0 Flash</td><td>4.5</td><td>3.7</td><td>3.3</td><td>3.6</td></tr>
          <tr class="non-reasoning"><td>Llama-4 Maverick</td><td>3.8</td><td>4.4</td><td>5.9</td><td>4.8</td></tr>
          <tr class="non-reasoning"><td>GPT-4o</td><td>5.3</td><td>4.6</td><td>5.3</td><td>4.9</td></tr>
          <tr class="non-reasoning"><td>DeepSeek-V3</td><td>5.9</td><td>6.3</td><td>4.3</td><td>5.0</td></tr>
          <tr class="non-reasoning"><td>GPT-4.1 mini</td><td>10.8</td><td>8.3</td><td>8.2</td><td>7.2</td></tr>
          <tr class="non-reasoning"><td>Claude Sonnet 3.7</td><td>10.7</td><td>9.2</td><td>8.5</td><td>6.9</td></tr>
          <tr class="non-reasoning"><td>Qwen-32B</td><td>9.9</td><td>9.0</td><td>8.8</td><td>9.2</td></tr>
          <tr class="non-reasoning"><td>Grok-3</td><td>9.9</td><td>10.6</td><td>9.3</td><td>8.0</td></tr>
          <tr class="reasoning"><td>GPT-4.1</td><td>12.1</td><td>11.8</td><td>10.0</td><td>8.2</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Flash</td><td>12.8</td><td>13.8</td><td>13.0</td><td>12.7</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Pro</td><td>13.2</td><td>13.9</td><td>12.9</td><td>12.9</td></tr>
          <tr class="reasoning"><td>Qwen-235B-A22B</td><td>15.0</td><td>14.6</td><td>13.0</td><td>12.9</td></tr>
          <tr class="reasoning"><td>Grok-3 Mini</td><td>14.2</td><td>13.9</td><td>14.5</td><td>14.8</td></tr>
          <tr class="reasoning"><td>DeepSeek-R1</td><td>14.2</td><td>15.3</td><td>14.1</td><td>13.4</td></tr>
          <tr class="reasoning"><td>o4-mini</td><td>15.0</td><td>15.5</td><td>14.5</td><td>13.9</td></tr>
          <tr class="reasoning"><td>o3</td><td>15.9</td><td>15.3</td><td>16.4</td><td>13.9</td></tr>
        </tbody>
      </table>
      <div class="panel-note">Average scores over 10 seeds per configuration.</div>
    </div>

    <!-- ─── Sherlock ─── -->
    <div class="results-panel" id="panel-sherlock">
      <div class="results-legend">
        <div class="legend-item"><span class="swatch non-reasoning"></span> Non-reasoning</div>
        <div class="legend-item"><span class="swatch reasoning"></span> Reasoning</div>
      </div>
      <table>
        <thead>
          <tr><th>Model</th><th>2-Player</th><th>3-Player</th><th>4-Player</th><th>5-Player</th></tr>
        </thead>
        <tbody>
          <tr class="non-reasoning"><td>Mistral Medium 3</td><td>4.1</td><td>4.8</td><td>5.3</td><td>5.4</td></tr>
          <tr class="non-reasoning"><td>Gemini 2.0 Flash</td><td>4.2</td><td>3.3</td><td>4.0</td><td>4.3</td></tr>
          <tr class="non-reasoning"><td>Llama-4 Maverick</td><td>4.9</td><td>5.2</td><td>5.4</td><td>5.6</td></tr>
          <tr class="non-reasoning"><td>GPT-4o</td><td>4.4</td><td>4.1</td><td>4.5</td><td>4.6</td></tr>
          <tr class="non-reasoning"><td>DeepSeek-V3</td><td>3.9</td><td>4.2</td><td>5.4</td><td>5.8</td></tr>
          <tr class="non-reasoning"><td>GPT-4.1 mini</td><td>6.5</td><td>6.1</td><td>5.1</td><td>5.8</td></tr>
          <tr class="non-reasoning"><td>Claude Sonnet 3.7</td><td>5.4</td><td>5.4</td><td>5.4</td><td>5.6</td></tr>
          <tr class="non-reasoning"><td>Qwen-32B</td><td>5.6</td><td>13.1</td><td>5.4</td><td>12.1</td></tr>
          <tr class="non-reasoning"><td>Grok-3</td><td>12.8</td><td>8.0</td><td>13.3</td><td>5.6</td></tr>
          <tr class="reasoning"><td>GPT-4.1</td><td>14.8</td><td>16.4</td><td>15.5</td><td>14.4</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Flash</td><td>8.4</td><td>6.6</td><td>7.7</td><td>5.6</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Pro</td><td>12.8</td><td>16.2</td><td>16.9</td><td>14.4</td></tr>
          <tr class="reasoning"><td>Qwen-235B-A22B</td><td>14.6</td><td>16.6</td><td>16.7</td><td>13.3</td></tr>
          <tr class="reasoning"><td>Grok-3 Mini</td><td>14.4</td><td>16.6</td><td>17.4</td><td>15.5</td></tr>
          <tr class="reasoning"><td>DeepSeek-R1</td><td>17.5</td><td>16.6</td><td>15.6</td><td>15.1</td></tr>
          <tr class="reasoning"><td>o4-mini</td><td>14.6</td><td>18.0</td><td>14.1</td><td>13.0</td></tr>
          <tr class="reasoning"><td>o3</td><td>17.6</td><td>17.6</td><td>16.8</td><td>15.7</td></tr>
        </tbody>
      </table>
      <div class="panel-note">Average scores over 10 seeds per configuration.</div>
    </div>

    <!-- ─── Mycroft ─── -->
    <div class="results-panel" id="panel-mycroft">
      <div class="results-legend">
        <div class="legend-item"><span class="swatch reasoning"></span> Reasoning (only)</div>
      </div>
      <table>
        <thead>
          <tr><th>Model</th><th>2-Player</th><th>3-Player</th><th>4-Player</th><th>5-Player</th></tr>
        </thead>
        <tbody>
          <tr class="reasoning"><td>o4-mini</td><td>10.8</td><td>12.4</td><td>11.3</td><td>10.9</td></tr>
          <tr class="reasoning"><td>Grok-3 Mini</td><td>14.2</td><td>16.5</td><td>14.5</td><td>14.4</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Pro</td><td>10.2</td><td>13.4</td><td>14.1</td><td>11.6</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Flash</td><td>11.8</td><td>13.2</td><td>12.3</td><td>9.8</td></tr>
          <tr class="reasoning"><td>o3</td><td>16.3</td><td>16.4</td><td>15.5</td><td>14.7</td></tr>
        </tbody>
      </table>
      <div class="panel-note">Mycroft evaluated on the top 5 reasoning models only. Average scores over 10 seeds.</div>
    </div>

  </div>
</div>

<figcaption style="margin-top: -0.5rem; font-size: 0.8rem; color: var(--text3); line-height: 1.5;"><strong style="color: var(--text2);">Table 2.</strong> Average scores (out of 25) across all three scaffolds. Watson provides minimal context; Sherlock adds deductive beliefs; Mycroft requires fully implicit state tracking. Best in each column is highlighted.</figcaption>



## Ablations {#ablations}

### Cross-play {#cross-play}

Self-play is generous; real cooperation is ad hoc. We compose teams with one Grok-3-mini agent and the rest o4-mini (the weaker model in Mycroft, 14.9 vs 11.3). Across all 2–5 player settings, **adding one stronger agent lifts team scores by ~1.7 points** — performance smoothly interpolates between the weak and strong self-play baselines, unlike specialized RL agents which collapse with unfamiliar partners.

<figure>
  <img src="{{ site.url }}/assets/icml/cross_play.png" alt="Cross-play interpolation">
  <figcaption><strong>Figure 8.</strong> Mixed teams score between weak (all o4-mini) and strong (all Grok-3-mini) self-play, demonstrating that LLM agents cooperate gracefully with unfamiliar partners — a meaningful contrast with traditional self-play RL.</figcaption>
</figure>

### Best-of-K {#best-of-k}

Sample the agent K times per turn and ask it to pick its best candidate. With Watson, performance climbs through K=5 (+1.5 on average) then plateaus. With Sherlock, gains are negligible (+0.1) — a well-engineered prompt mostly converges to the same action across samples, so naive scaling does not help. **Better context beats more samples.**

### Mixture of agents {#moa}

To break sample homogeneity, we run five role-specialized agents in parallel — Baseline, Rank-Focused, Analyst, Discard Strategist, History Analyst — and aggregate their proposals via a sixth "finalizer" agent. MoA modestly improves the 5-player setting (+1.1 with Watson, +0.8 with Sherlock over Best-of-5) but introduces high variance: speculative agents (especially the History Analyst) occasionally mislead the aggregator and tank a run. Diversity helps when it lands; reliability remains the open problem.

## Post-training: closing the gap with a 4B model {#post-training}

To validate our datasets, we post-train **Qwen3-4B-Instruct-2507** — a small, non-reasoning model — on data collected from o3 and Grok-3-mini.

- **HanabiLogs** (1,520+ trajectories) — for supervised finetuning.
- **HanabiRewards** (560+ games with dense move-level utility annotations) — for RLVR via GRPO.

The base model scores 1.7 in Mycroft. After RL on HanabiRewards: **8.3** — a +388% jump that lands within ~3 points of o4-mini (11.3) and surpasses GPT-4.1 (the best non-reasoning baseline) by +88%. In Sherlock, the same model jumps from 4.8 to 12.3 (+156%), comparable to Grok-3 and beating GPT-4o.

<figure>
  <div class="img-row" style="margin: 0;">
    <img src="{{ site.url }}/assets/icml/Sherlock_finetune.png" alt="Sherlock post-training results">
    <img src="{{ site.url }}/assets/icml/mycroft_finetuned.png" alt="Mycroft post-training results">
  </div>
  <figcaption><strong>Figure 9.</strong> Qwen3-4B before and after instruction tuning (Ours-SFT) and RLVR (Ours-RL), versus larger proprietary models. Evaluated on held-out seeds to avoid leakage.</figcaption>
</figure>

### Generalization beyond Hanabi {#generalization}

The interesting result isn't just "we got better at Hanabi." Training on HanabiRewards transfers to four out-of-domain benchmarks, with no degradation on math.

<div class="table-wrap">
  <table>
    <caption>Table 1 — Qwen3-4B base vs. our RL-finetuned model. Group Guessing is wins/200 games (cooperative); EventQA is 6-way MCQ accuracy at increasing context lengths (temporal reasoning); IFBench is strict instruction-following; AIME 2025 measures math reasoning.</caption>
    <thead>
      <tr>
        <th>Model</th>
        <th>Group Guess<br><span style="font-weight:400;font-size:0.7rem;">(1st / 2nd run)</span></th>
        <th>EventQA<br><span style="font-weight:400;font-size:0.7rem;">(64K / 128K / 800K)</span></th>
        <th>IFBench<br><span style="font-weight:400;font-size:0.7rem;">(Avg / Pass@10)</span></th>
        <th>AIME 2025<br><span style="font-weight:400;font-size:0.7rem;">(Avg / Pass@10)</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Base</td>
        <td class="num">61.0 / 60.5</td>
        <td class="num">84.0 / 62.6 / 37.2</td>
        <td class="num">30.9 / 42.9</td>
        <td class="num">48.7 / 73.3</td>
      </tr>
      <tr>
        <td><strong>Ours-RL</strong></td>
        <td class="num delta-pos">73.0 / 71.5</td>
        <td class="num delta-pos">85.6 / 66.8 / 43.6</td>
        <td class="num delta-pos">31.5 / 44.6</td>
        <td class="num">50.0 / 73.3</td>
      </tr>
      <tr>
        <td>Δ</td>
        <td class="num delta-pos">+12.0 / +11.0</td>
        <td class="num delta-pos">+1.6 / +4.2 / +6.4</td>
        <td class="num delta-pos">+0.6 / +1.7</td>
        <td class="num delta-neutral">+1.3 / +0.0</td>
      </tr>
    </tbody>
  </table>
</div>

The temporal-reasoning lift on EventQA grows with context length (+1.6 → +4.2 → +6.4 from 64K to 800K), which we read as evidence that learning to implicitly track Hanabi state generalizes to long-horizon belief tracking elsewhere. AIME stays flat — no catastrophic forgetting on math.

## Takeaways {#takeaways}

1. **Modern reasoning LLMs are sparks of cooperative reasoning, not flames.** The best score ~15–18/25 in self-play, comfortably below specialized agents (>23) and the median human Hanabi player (~18–21).
2. **Scaffold design matters more than model scale.** Watson → Sherlock improves reasoning models by +2.0 on average; the same scaffold *hurts* most non-reasoning models. Different families respond differently to identical context.
3. **Implicit state tracking is the open problem.** Even o3 drops 1.2 points moving from engine-provided deductions to self-tracking; Gemini 2.5 Pro drops 3.7. Multi-turn belief maintenance is where current models break.
4. **Cross-play is graceful.** Unlike specialized RL agents, LLMs interpolate smoothly between weak and strong teammates — a small but real "spark" of cooperative generalization.
5. **A 4B model can carry surprising weight.** Post-training on our datasets closes most of the gap to frontier reasoning models on Hanabi *and* transfers to temporal reasoning, instruction following, and out-of-domain cooperation.

## Citation {#citation}

<div class="citation-block">
  <div class="citation-header">
    <span class="lbl">BibTeX</span>
    <button><span>Copy</span></button>
  </div>
<pre>@misc{ramesh2026sparkscooperativereasoningllms,
      title={Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents}, 
      author={Mahesh Ramesh and Kaousheik Jayakumar and Aswinkumar Ramkumar and Pavan Thodima and Aniket Rege and Emmanouil-Vasileios Vlatakis-Gkaragkounis},
      year={2026},
      eprint={2601.18077},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2601.18077}, 
}</pre>
</div>