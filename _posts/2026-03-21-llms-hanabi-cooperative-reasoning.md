---
layout: research-post
title: "Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents"
subtitle: "Frontier LLMs show real but uneven cooperative reasoning on Hanabi — and a 4B model trained on our new datasets closes most of the gap to o4-mini while transferring to temporal reasoning, instruction following, and out-of-domain coordination."
authors: "Mahesh Ramesh¹, Kaousheik Jayakumar², Aswinkumar Ramkumar¹, Pavan Thodima¹, Aniket Rege¹, Emmanouil V. Vlatakis-Gkaragkounis¹"
author_note: "¹University of Wisconsin–Madison ²University of Maryland, College Park"
venue: "Preprint, 2026"
paper_url: "https://arxiv.org/abs/2601.18077"
code_url: "https://github.com/"
date: 2026-03-21

nav_sections:
  - title: "Why Hanabi"
    id: "why-hanabi"
  - title: "How We Study This"
    id: "how-we-study-this"
    children:
      - title: "Watson → Sherlock → Mycroft"
        id: "watson-sherlock-mycroft"
  - title: "Findings"
    id: "findings"
    children:
      - title: "Reasoning Models Lead"
        id: "reasoning-vs-non-reasoning"
      - title: "Context Engineering"
        id: "context-engineering-matters"
      - title: "State Tracking"
        id: "state-tracking-bottleneck"
      - title: "Cross-Play"
        id: "cross-play-interpolates"
      - title: "Statistical Robustness (IQM)"
        id: "statistical-robustness-iqm"
  - title: "Datasets & Fine-Tuning"
    id: "datasets-and-finetuning"
    children:
      - title: "Out-of-Domain Transfer"
        id: "out-of-domain-transfer"
  - title: "Takeaways"
    id: "takeaways"
  - title: "Citation"
    id: "citation"
---

## Why Hanabi

Most benchmarks for large language models reward solitary brilliance — solve the math problem, win the chess game, finish the code. But many situations we actually want AI to handle are *cooperative* under *incomplete information*: coordinating with a teammate, inferring what someone else knows, deciding when to speak and when to stay quiet. None of that shows up cleanly on a leaderboard for IMO problems.

We use **Hanabi** as a testbed for exactly these capabilities. Hanabi is a cooperative card game where every player can see everyone's hand *except their own*. You succeed by giving sparse, expensive hints and inferring teammates' intent from their actions — a near-perfect probe of theory-of-mind and strategic coordination under uncertainty. It has been a standard challenge problem for multi-agent AI since the Bayesian Action Decoder days, and despite being a card game, the skills it demands transfer directly to the asymmetric, long-horizon coordination problems that show up in real human-AI deployments.

This work makes four contributions: a large-scale, reproducible benchmark of 17 frontier LLMs across 2–5 player games; a context-engineering study via three prompting scaffolds of increasing difficulty; two new public datasets for post-training cooperative agents; and a 4B open-weights model that, after RL fine-tuning on our data, closes most of the gap to frontier reasoning models — with surprising out-of-domain transfer.

## How we study this

### Watson Sherlock Mycroft

We designed three prompting scaffolds, each named after a Holmes brother of escalating reasoning power, to isolate *where* LLMs struggle.

**Watson** is the minimal-context baseline. The agent receives only the raw game state and must reason from scratch. This gives us a lower bound and probes the model's prior knowledge of Hanabi.

**Sherlock** adds programmatic deductions from the game engine — explicit "this card could be red, yellow, or green; it cannot be 4 or 5" belief states — plus a Bayesian-style step-by-step reasoning workflow. This is meant as an upper bound: the model gets the deductions handed to it, so any failure here is a failure of strategic reasoning rather than bookkeeping.

<figure>
  <img src="{{ '/assets/images/hanabi/fig1-watson-sherlock.png' | relative_url }}" alt="Watson vs Sherlock prompting scaffolds">
  <figcaption><strong>Figure 1.</strong> The <em>Watson</em> setting (left) provides only the basic game state with explicit knowledge. The <em>Sherlock</em> setting (right) adds a "Deductive Context" block listing all valid color/rank possibilities for every card and enforces a step-by-step Bayesian reasoning workflow.</figcaption>
</figure>

**Mycroft** is the hardest setting and our novel contribution. Instead of receiving engine-computed belief states, the agent has to maintain them *itself* across turns, writing out a "working memory" scratchpad of what every player knows about every card. This is much closer to how humans actually play, and it's where multi-turn state tracking really gets stress-tested.

<figure>
  <img src="{{ '/assets/images/hanabi/fig20-mycroft-turn.png' | relative_url }}" alt="Mycroft turn from player 1's perspective">
  <figcaption><strong>Figure 20.</strong> An example game state as viewed by Player 1 in the <em>Mycroft</em> setting. Each player maintains independent deduction blocks for every other player's hand, updated turn by turn from the agent's own scratchpad rather than from the game engine.</figcaption>
</figure>

Across 17 LLMs ranging from 4B to 600B+ parameters, we ran 2-, 3-, 4-, and 5-player games on fixed seeds — what we believe is the largest reproducible evaluation of LLMs as Hanabi agents to date.

## Findings

### Reasoning vs non reasoning

Across the board, models with test-time reasoning (o3, o4-mini, Gemini 2.5 Pro, Grok-3-mini, DeepSeek-R1) scored above 13/25, while non-reasoning models clustered below 10/25. The best performers landed around 15–18 points, putting them at roughly the **lower quartile of human players** from BoardGameGeek logs — competent, but well behind the median (≈20+) and far behind specialized self-play RL agents that score above 23. Frontier LLMs are real Hanabi players, but they're not yet good ones.

### Context engineering matters

Different models react very differently to richer prompts. Gemini 2.5 Pro gained nearly 3 points on average moving from Watson to Sherlock; o4-mini barely budged. Some non-reasoning models actually got *worse* with the more elaborate Sherlock prompt because they couldn't juggle the probability calculations alongside the format requirements. Even frontier reasoning models remain surprisingly sensitive to how a task is framed — the intuition that "stronger model = robust to prompting" doesn't hold up. Models given identical context often adopt entirely different play styles: o4-mini becomes more discard-happy under Sherlock, Gemini 2.5 Pro plays aggressively until it loses two life tokens then snaps to conservative, and Grok-3-mini grinds out steady, low-variance scores.

### State tracking bottleneck

When we forced models to maintain their own belief states in the Mycroft setting, performance dropped across the board — by roughly 3.7 points for o4-mini and Gemini 2.5 Pro, and 1.2 points even for o3, the strongest implicit-state-tracker we tested. An LLM-as-judge evaluation gave both o4-mini and Grok-3-mini overall state-tracking scores well below 0.5. Keeping a coherent picture of the world over many turns — remembering that Player 3's card 0 became their card 1 after a discard, and that the new draw is unknown, and that the rank-2 hint from three turns ago still constrains card 2 — is still genuinely hard for frontier models.

### Cross play interpolates

We also moved beyond self-play to **cross-play**, where mixed teams play together. Traditional self-play RL agents fall apart when paired with strangers. We tested mixed teams with one Grok-3-mini and several o4-minis, and team performance lands cleanly *between* the two self-play scores — adding a single stronger agent to a team of weaker ones lifted average scores by ≈1.7 points. To probe diversity-driven gains, we also built a Mixture-of-Agents system where five specialist agents (baseline, rank-focused, analyst, discard strategist, history analyst) feed into an aggregator that picks the final move.

<div class="figure-row">
<figure>
  <img src="{{ '/assets/images/hanabi/fig19a-moa-architecture.png' | relative_url }}" alt="Mixture-of-Agents architecture">
  <figcaption><strong>Figure 19a.</strong> The Mixture-of-Agents system: five parallel specialist agents generate diverse outputs that an Aggregator Agent synthesizes into a final move.</figcaption>
</figure>
<figure>
  <img src="{{ '/assets/images/hanabi/fig19b-moa-scores.png' | relative_url }}" alt="Mixture-of-Agents scores across player counts">
  <figcaption><strong>Figure 19b.</strong> Mixture-of-Agents average scores under Watson and Sherlock prompting strategies across 2–5 player settings.</figcaption>
</figure>
</div>

The cross-play and MoA results together are a small but meaningful sign that LLMs carry more generalizable cooperative priors than specialized RL agents — exactly the property you want for ad-hoc human-AI teamwork.

### Statistical robustness IQM

Mean scores can be misleading on a benchmark with this much per-game variance, so we also report interquartile mean (IQM) scores with 95% confidence intervals across all 17 models and player counts. The IQM analysis confirms every trend in the main paper: reasoning models dominate, the Sherlock scaffold beats Watson and SPIN-Bench variants, and the cross-play interpolation effect holds up under the more conservative statistic.

<div class="figure-row">
<figure>
  <img src="{{ '/assets/images/hanabi/fig9-iqm-watson-sherlock.png' | relative_url }}" alt="IQM scores across all 17 models">
  <figcaption><strong>Figure 9.</strong> Interquartile mean (IQM) scores of all 17 LLM Hanabi agents across 2–5 player settings, with 95% confidence intervals.</figcaption>
</figure>
<figure>
  <img src="{{ '/assets/images/hanabi/fig10-iqm-reasoning-models.png' | relative_url }}" alt="IQM scores for top reasoning models">
  <figcaption><strong>Figure 10.</strong> IQM scores for the top reasoning LLMs broken down by player count (2P–5P) under both Watson and Sherlock settings.</figcaption>
</figure>
</div>

## Datasets and finetuning

Because there are essentially no public Hanabi datasets designed for post-training LLMs, we built two: **HanabiLogs** (1,520 annotated game trajectories with full prompts and reasoning traces from o3, Grok-3-mini, and others) and **HanabiRewards** (560 games with dense, move-level utility annotations from an LLM judge).

We then took **Qwen3-4B-Instruct-2507**, a small open-weights model, and trained it on HanabiRewards using GRPO-style RLVR. The result: a **156% improvement in the Sherlock setting and 138% in Mycroft**, landing within ~3 points of o4-mini and beating GPT-4.1 — the strongest non-reasoning baseline — by 88%. A 4B model, trained on a few thousand cooperative-reasoning trajectories, closes most of the gap to a frontier reasoning model with vastly more parameters and test-time compute.

### Out of domain transfer

The more interesting result is what happens *outside* Hanabi. The same RL-trained model improves on the Group Guessing Game (a different cooperative benchmark) by **11%**, on EventQA temporal reasoning by up to **6.4 points** at long context lengths, and on IFBench instruction-following by **1.7 Pass@10** — all while *maintaining* AIME 2025 math performance. Training on cooperative-reasoning data didn't just teach the model Hanabi. It transferred to temporal reasoning, instruction following, and out-of-domain coordination, without degrading general capability. That's a meaningful signal that cooperative-reasoning data is doing real work on the model's underlying representations, not just teaching it the game.

## Takeaways

Two things stand out from this work. First, the gap between LLMs and humans on Hanabi isn't really about raw intelligence — frontier models clearly have the strategic vocabulary. The gap is about **persistent state tracking** and **theory of mind** under genuine information asymmetry. Those are exactly the capabilities you need for AI systems that work alongside humans on long-horizon tasks, and they're surprisingly hard to get right even with frontier reasoning models.

Second, **cooperative reasoning seems to be a generalizable training target**. A small model trained on a few thousand annotated game trajectories transferred its gains to temporal reasoning and instruction following, suggesting there's untapped value in benchmarking and training on theory-of-mind-heavy environments — not just as a curiosity, but as a way to build more robust general-purpose reasoners. The sparks are visible. The path forward feels concrete.

## Citation

<div class="citation-block">
<span class="cite-label">BibTeX</span>
<pre>@article{ramesh2026sparks,
  title={Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents},
  author={Ramesh, Mahesh and Jayakumar, Kaousheik and Ramkumar, Aswinkumar and
          Thodima, Pavan and Rege, Aniket and Vlatakis-Gkaragkounis, Emmanouil V.},
  journal={arXiv preprint arXiv:2601.18077},
  year={2026}
}</pre>
</div>