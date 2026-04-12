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
---

## Overview

Most benchmarks for large language models reward solitary brilliance — solve the math problem, win the chess game, finish the code. But many of the situations we actually want AI to handle are *cooperative* under *incomplete information*: coordinating with a teammate, inferring what someone else knows, deciding when to speak and when to stay quiet. None of that shows up cleanly on a leaderboard for IMO problems.

We use **Hanabi** as a testbed for exactly these capabilities. Hanabi is a cooperative card game where every player can see everyone's hand *except their own*. You succeed by giving sparse, expensive hints and inferring teammates' intent from their actions — a near-perfect probe of theory-of-mind and strategic coordination under uncertainty.

This work makes four contributions: a large-scale, reproducible benchmark of 17 frontier LLMs across 2–5 player Hanabi games; a context-engineering study via three prompting scaffolds of increasing difficulty; two new public datasets for post-training cooperative agents; and a 4B open-weights model that, after RL fine-tuning on our data, closes most of the gap to frontier reasoning models — with surprising out-of-domain transfer.

## Qualitative examples

Hanabi looks simple from the outside, but every turn involves layered reasoning about what *you* know, what *others* know, and what others believe *you* know. Here's the kind of thing we mean: imagine the Yellow firework is at 4 and you hold a card you've been told is "rank 5." Should you play it? Yes — but only if you can also rule out it being a Red 5 or Blue 5 from the public history. That deduction is trivial for a human player who's been tracking the game; it turns out to be genuinely hard for LLMs across long horizons.

The full paper has detailed transcripts showing how, given identical context, o3 and Grok-3-mini diverge into entirely different play styles, and how non-reasoning models silently corrupt their own context by mis-rating moves.

## How we study this

We designed three prompting scaffolds, each named after a Holmes brother of escalating reasoning power, to isolate *where* LLMs struggle:

**Watson** is the minimal-context baseline. The agent receives only the raw game state and must reason from scratch. This gives us a lower bound and probes the model's prior knowledge of Hanabi.

**Sherlock** adds programmatic deductions from the game engine — explicit "this card could be red, yellow, or green; it cannot be 4 or 5" belief states — plus a Bayesian-style step-by-step reasoning workflow. This is meant as an upper bound: the model gets the deductions handed to it.

**Mycroft** is the hardest setting and our novel contribution. Instead of receiving engine-computed belief states, the agent has to maintain them *itself* across turns, writing out a "working memory" scratchpad of what every player knows about every card. This is much closer to how humans actually play, and it's where multi-turn state tracking really gets stress-tested.

Across 17 LLMs ranging from 4B to 600B+ parameters, we ran 2-, 3-, 4-, and 5-player games on fixed seeds — what we believe is the largest reproducible evaluation of LLMs as Hanabi agents to date.

## Findings

### Does the model pay attention to audio

The first headline: **reasoning models are meaningfully better than non-reasoning ones**. Across the board, models with test-time reasoning (o3, o4-mini, Gemini 2.5 Pro, Grok-3-mini, DeepSeek-R1) scored above 13/25, while non-reasoning models clustered below 10/25. The best performers landed around 15–18 points, putting them at roughly the lower quartile of human players from BoardGameGeek logs — competent, but well behind the median (≈20+) and far behind specialized self-play RL agents that score above 23.

### Are audio representations meaningful

**Context engineering matters more than you'd expect.** Different models react very differently to richer prompts. Gemini 2.5 Pro gained nearly 3 points on average moving from Watson to Sherlock; o4-mini barely budged. Some non-reasoning models actually got *worse* with the more elaborate Sherlock prompt because they couldn't juggle the probability calculations alongside the format requirements. Even frontier reasoning models remain surprisingly sensitive to how a task is framed — the intuition that "stronger model = robust to prompting" doesn't hold up.

### How does cross-modal information flow

**State tracking is the real bottleneck.** When we forced models to maintain their own belief states in the Mycroft setting, performance dropped across the board — by roughly 3.7 points for o4-mini and Gemini 2.5 Pro, and 1.2 points even for o3, the strongest implicit-state-tracker we tested. An LLM-as-judge evaluation gave both o4-mini and Grok-3-mini overall state-tracking scores well below 0.5. Keeping a coherent picture of the world over many turns is still genuinely hard.

We also moved beyond self-play to **cross-play**, where mixed teams play together. Traditional self-play RL agents fall apart when paired with strangers. We tested mixed teams with one Grok-3-mini and several o4-minis, and found team performance lands cleanly *between* the two self-play scores. That's a small but meaningful sign that LLMs carry more generalizable cooperative priors than specialized RL agents.

### Where does the vision bias originate

Because there are essentially no public Hanabi datasets designed for post-training LLMs, we built two: **HanabiLogs** (1,520 annotated game trajectories with full prompts and reasoning traces) and **HanabiRewards** (560 games with dense, move-level utility annotations from an LLM judge).

We then took **Qwen3-4B-Instruct-2507**, a small open-weights model, and trained it on HanabiRewards using GRPO-style RLVR. The result: a **156% improvement in the Sherlock setting and 138% in Mycroft**, landing within ~3 points of o4-mini and beating GPT-4.1 — the strongest non-reasoning baseline — by 88%. A 4B model, trained on a few thousand cooperative-reasoning trajectories, closes most of the gap to a frontier reasoning model.

The more interesting result is what happens *outside* Hanabi. The same RL-trained model improves on the Group Guessing Game (a different cooperative benchmark) by **11%**, on EventQA temporal reasoning by up to **6.4 points** at long context lengths, and on IFBench instruction-following by **1.7 Pass@10** — all while *maintaining* AIME 2025 math performance. Training on cooperative-reasoning data didn't just teach the model Hanabi; it transferred to temporal reasoning, instruction following, and out-of-domain coordination, without degrading general capability.

Two takeaways stand out. First, the gap between LLMs and humans on Hanabi isn't really about raw intelligence — frontier models clearly have the strategic vocabulary. The gap is about **persistent state tracking** and **theory of mind** under genuine information asymmetry, which are exactly the capabilities you need for AI systems that work alongside humans on long-horizon tasks. Second, **cooperative reasoning seems to be a generalizable training target**: a small model trained on a few thousand annotated game trajectories transferred its gains broadly, suggesting untapped value in benchmarking and training on theory-of-mind-heavy environments.

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