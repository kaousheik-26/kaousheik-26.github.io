---
layout: hanabi-post
permalink: /llms-hanabi-cooperative-reasoning/
title: "Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents"
subtitle: "We introduce a reproducible Hanabi benchmark for cooperative LLM reasoning across 17 models, 2–5 players, and three Holmesian scaffolds that vary the amount of information agents can query from the environment and their deductive reasoning capabilities (Watson, Sherlock, Mycroft). Our key insight is that performance depends strongly on modeling belief-state, with Mycroft isolating true multi-turn implicit state tracking. We release Hanabi trajectories and move-level judge data to support SFT/RL post-training. We show that posttraining Qwen3-4B on our new dataset can substantially close the gap to frontier LLMs on Hanabi (+21% with SFT and +156% with RL) while transferring to out-of-domain tasks (AIME 2025, EventQA, IFBench)."
teaser_img: "/assets/icml/project_pg_teaser.jpg"
authors: "<a href='https://maheshram1.github.io/'>Mahesh Ramesh</a>¹, <span class='me'><a href='https://kaousheik-26.github.io/'>Kaousheik Jayakumar</a>²</span>, <a href='https://aswinkumar.me/'>Aswinkumar Ramkumar</a>¹, <a href='https://pthodima.github.io/'>Pavan Thodima</a>¹, <a href='https://aniketrege.github.io/'>Aniket Rege</a>¹†, <a href='https://pages.cs.wisc.edu/~vlatakis/'>Manolis Vlatakis</a>¹†<br><span style='font-size: 0.85em; font-weight: normal; color: var(--text2);'>†Equal advising</span>"
affiliation: "<span class='star'>★</span> ¹University of Wisconsin–Madison &nbsp;·&nbsp; ²University of Maryland, College Park"
venue: "ICML 2026"
paper_url: "https://arxiv.org/abs/2601.18077"
env_url: "https://app.primeintellect.ai/dashboard/environments/mahesh-ramesh/hanabi"
dataset_url: "https://huggingface.co/datasets/Mahesh111000/Hanabi_data"
date: 2026-03-21

blog_sidebar_authors:
  - name: Kaousheik Jayakumar
    url: https://kaousheik-26.github.io/
    avatar: https://github.com/kaousheik-26.png?size=80
  - name: Aniket Rege
    url: https://aniketrege.github.io/
    avatar: https://aniketrege.github.io/assets/img/prof_pic.png?size=80

nav_sections:
  - title: "Why Hanabi"
    id: "why-hanabi"
  - title: "Our Holmesian Scaffolds"
    id: "holmesian-scaffolds"
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

<div class="contributions-box" style="background: var(--bg-elevated); border-left: 3px solid var(--accent); padding: 1.25rem 1.5rem; border-radius: 6px; margin-bottom: 2rem; box-shadow: var(--shadow-sm); border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border);">
  <h4 style="margin-top: 0; color: var(--accent); font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem;">Contributions</h4>
  <ol style="margin-bottom: 0; padding-left: 1.25rem;">
    <li style="margin-bottom: 0.4rem;"><strong>Benchmark protocol:</strong> a reproducible evaluation suite for cooperative LLM play in Hanabi (17 open weight and proprietary models, 2–5 players, fixed-seed settings, self-play + cross-play).</li>
    <li style="margin-bottom: 0.4rem;"><strong>Scaffolded diagnosis:</strong> Our Holmesian scaffolds (Watson/Sherlock/Mycroft) distinguish between LLMs that reason with provided deductions and those that can maintain implicit beliefs over long horizons.</li>
    <li style="margin-bottom: 0.4rem;"><strong>🗂️ New training data release:</strong> HanabiLogs (LLM game playing trajectories for SFT) and HanabiRewards (move-level utility annotations as rewards for RL).</li>
    <li style="margin-bottom: 0.4rem;"><strong>Actionable post-training baseline:</strong> Qwen3-4B improvements quantify what small open models gain from cooperative trajectory and reward supervision.</li>
    <li><strong>Transfer signal:</strong> cooperative-reasoning post-training improves multiple out-of-domain tasks, supporting Hanabi as a practical post-training substrate.</li>
  </ol>
</div>

## Why Hanabi? {#why-hanabi}

Popular single-agent benchmarks currently do not evaluate a specific but important type of intelligence: multiple LLM agents cooperating to solve a single task with partial or incomplete information about their environment and other agents. **Hanabi** is extremely well suited to this task: between 2 and 5 players hold cards facing outward, visible to everyone but themselves, and must build five color-ordered "fireworks" using only color or rank hints from a finite pool of information tokens. Success requires tracking hidden information, inferring teammate intent, and coordinating through sparse signals.

Specialized RL agents reach ~24/25 in 2-player self-play[^selfplay] but degrade sharply with more players or unfamiliar partners. In this work, we focus on the question: **how good are general-purpose LLMs as cooperative agents, and what limits them?**

[^selfplay]: Self-Play refers to a Hanabi game where all players/agents have the same LLM backbone (e.g. GPT-4o).

## Holmesian Scaffolds {#holmesian-scaffolds}

We progressively scale the context an agent receives, from minimal state to engine-provided deductions to fully implicit multi-turn state tracking. Each scaffold isolates a different capability.

<div class="settings-grid">
  <div class="setting-card">
    <div class="ord">01 · BASELINE</div>
    <h4>Watson</h4>
    <p>Minimal context: game state, visible hands, and explicit knowledge from clues. Nothing else. This establishes a lower bound on what LLMs can do without scaffolding.</p>
  </div>
  <div class="setting-card">
    <div class="ord">02 · SCAFFOLDED</div>
    <h4>Sherlock</h4>
    <p>Adds engine-computed deductions (per-card "could be" possibilities), Hanabi strategies, and a Bayesian step-by-step prompt. This establishes an upper bound with rich prefill.</p>
  </div>
  <div class="setting-card">
    <div class="ord">03 · IMPLICIT</div>
    <h4>Mycroft</h4>
    <p>No engine deductions. The agent must implicitly track its own and teammates' beliefs across turns via a structured "scratch pad," closer to how humans actually play Hanabi.</p>
  </div>
</div>

### Watson & Sherlock {#watson-sherlock}

Watson and Sherlock differ in one key way, i.e., whether the agent receives a programmatic belief state. Sherlock is provided, for every card in every hand, the colors and ranks still consistent with the clue history.[^hle] The agent is then prompted to do Bayesian-style probabilistic reasoning over these candidates before acting.

<figure>
  <img src="{{ site.url }}/assets/icml/sherlock_watson_teaser.png" alt="Watson vs Sherlock prompt comparison">
  <figcaption><strong>Figure 1.</strong> Watson provides only explicit knowledge (clues received). Sherlock additionally provides a Deductive Context block (the per-card belief state) and enforces Bayesian-style step-by-step reasoning.</figcaption>
</figure>

[^hle]: Sherlock's programmatic candidate sets are computed with [Google DeepMind's Hanabi Learning Environment](https://github.com/google-deepmind/hanabi-learning-environment).

### Mycroft {#mycroft}

Mycroft removes Sherlock's dependency on deductions from an external game engine[^hle]. Each turn, the agent receives the previous turn's game state, its own deductions for every player, move ratings, its chosen action, and the reasoning for its choice. It must then produce updated deductions, ratings, and an action for that turn. This forces the LLM to be its own deductive game engine, tracking belief shifts and card position changes (cards slide left after a play or discard) across 60+ turns.

<figure>
  <img src="{{ site.url }}/assets/icml/mycroft_teaser.png" alt="Mycroft scratch pad example">
  <figcaption><strong>Figure 2.</strong> A Mycroft turn from Player 1's perspective. The agent maintains an independent deduction block for every other player and must update card positions implicitly after plays and discards.</figcaption>
</figure>

## Benchmark results {#benchmark-results}

We evaluate **17 LLMs** (open-weights and proprietary, 4B to 600B+, both reasoning and non-reasoning) across 2 to 5 player self-play, with 10 fixed seeds per configuration. Reasoning models clear ~13/25 in Watson; non-reasoning models generally stall below 10/25. Performance tends to drop as the number of players increase (tracking information is harder!), though there are exceptions (e.g. Grok 3 Mini).


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
          <tr class="non-reasoning"><td>Grok 3</td><td>9.9</td><td>10.6</td><td>9.3</td><td>8.0</td></tr>
          <tr class="reasoning"><td>GPT-4.1</td><td>12.1</td><td>11.8</td><td>10.0</td><td>8.2</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Flash</td><td>12.8</td><td>13.8</td><td>13.0</td><td>12.7</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Pro</td><td>13.2</td><td>13.9</td><td>12.9</td><td>12.9</td></tr>
          <tr class="reasoning"><td>Qwen-235B-A22B</td><td>15.0</td><td>14.6</td><td>13.0</td><td>12.9</td></tr>
          <tr class="reasoning"><td>Grok 3 Mini</td><td>14.2</td><td>13.9</td><td>14.5</td><td>14.8</td></tr>
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
          <tr class="non-reasoning"><td>Grok 3</td><td>12.8</td><td>8.0</td><td>13.3</td><td>5.6</td></tr>
          <tr class="reasoning"><td>GPT-4.1</td><td>14.8</td><td>16.4</td><td>15.5</td><td>14.4</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Flash</td><td>8.4</td><td>6.6</td><td>7.7</td><td>5.6</td></tr>
          <tr class="reasoning"><td>Gemini 2.5 Pro</td><td>12.8</td><td>16.2</td><td>16.9</td><td>14.4</td></tr>
          <tr class="reasoning"><td>Qwen-235B-A22B</td><td>14.6</td><td>16.6</td><td>16.7</td><td>13.3</td></tr>
          <tr class="reasoning"><td>Grok 3 Mini</td><td>14.4</td><td>16.6</td><td>17.4</td><td>15.5</td></tr>
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
          <tr class="reasoning"><td>Grok 3 Mini</td><td>14.2</td><td>16.5</td><td>14.5</td><td>14.4</td></tr>
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

The self-play assumption that all players are essentially identical (the same LLM) is strong and does not hold in real-world ad hoc cooperative settings (no humans are identical!). We thus extend our evaluation to "cross-play", i.e., teams with LLMs of disparate Hanabi playing competence. Specifically, we compose 2-5 player teams of one strong LLM (Grok 3 Mini) and the rest, a weaker LLM (o4-mini). Across all player counts, **adding one stronger agent improves a team's score by 1.7 points on average** (see Fig. 8 below). Performance smoothly interpolates between the weak and strong self-play baselines (o4-mini and Grok 3 Mini respectively), unlike specialized RL agents which collapse with unfamiliar partners.

<figure>
  <img src="{{ site.url }}/assets/icml/cross_play.png" alt="Cross-play interpolation">
  <figcaption><strong>Figure 8.</strong> Mixed teams score between weak (all o4-mini) and strong (all Grok 3 Mini) self-play, demonstrating that LLM agents cooperate gracefully with unfamiliar partners, in meaningful contrast with traditional self-play RL.</figcaption>
</figure>

### Best-of-K {#best-of-k}

Can we get better performance by majority voting over K move candidates by sampling the agent k times? We provide these K chosen moves and reasoning to the agent and ask it to pick the optimal move with the best strategic thinking. With Watson, performance climbs through K=5 (+1.5 on average) and then plateaus. With Sherlock, gains are negligible (+0.1) because a well-designed scaffold with verifiable deductive reasoning tends to converge to the same chosen action regardless of how many times we sample the LLM. **Better context beats best-of-k sampling!**

### Mixture of Agents {#moa}

<div class="text-img-row">
  <div class="text-side">
    <p>Inspired by <a href='https://arxiv.org/abs/2406.04692'>Mixture of Agents</a>, we assign five specialized roles to sub-agents that execute in parallel (Baseline, Rank-Focused, Analyst, Discard Strategist, History Analyst) and aggregate their proposals via a sixth "Aggregator" agent.</p>
    <p>MoA modestly improves the 5-player setting (+1.1 with Watson, +0.8 with Sherlock over Best-of-5) but introduces high variance: speculative high-risk sub-agents (especially the History Analyst) occasionally mislead the aggregator and tank a run.</p>
  </div>
  <div class="img-side">
    <img src="{{ site.url }}/assets/icml/moa.png" alt="Mixture of Agents architecture">
  </div>
</div>
**Encouraging agent move selection diversity can sometimes help, but there is a fine line between diversity and unreliability.**

## Post-training on a 4B LLM closes the gap to Frontier models {#post-training}

To validate our datasets, we post-train **Qwen3-4B-Instruct-2507**, a small non-reasoning model, on data we collect from o3 and Grok 3 Mini:

- **HanabiLogs** (1,520+ game trajectories): used for supervised finetuning (SFT).
- **HanabiRewards** (560+ games with dense move-level utility annotations): used for Reinforcement Learning with Verifiable Rewards via GRPO.

The Mycroft base model scores a very low 1.7/25, indicating low base Hanabi competence. After RL on HanabiRewards it reaches **8.3/25**, a +388% jump that lands within ~3 points of o4-mini (11.3) and surpasses GPT-4.1 (the best non-reasoning baseline) by +88%. In Sherlock, the same model jumps from 4.8 to 12.3 (+156%), comparable to Grok 3 and beating GPT-4o.

<figure>
  <div class="img-row" style="margin: 0;">
    <img src="{{ site.url }}/assets/icml/Sherlock_finetune.png" alt="Sherlock post-training results">
    <img src="{{ site.url }}/assets/icml/mycroft_finetuned.png" alt="Mycroft post-training results">
  </div>
  <figcaption><strong>Figure 9.</strong> Qwen3-4B before and after instruction tuning (Ours-SFT) and RLVR (Ours-RL), versus larger proprietary models. Evaluated on held-out seeds to avoid leakage.</figcaption>
</figure>

### Generalizing Beyond Hanabi {#generalization}

Now for the big (and fun) question: what else does getting really good at Hanabi teach the LLM? As it turns out, training on our new HanabiRewards data improves scores on four out-of-domain benchmarks:

<div class="table-wrap table-align-col-headers">
  <table>
    <caption>Table 1. Qwen3-4B base vs. our RL-finetuned model. Group Guessing is wins/200 games (cooperative); EventQA is 6-way MCQ accuracy at increasing context lengths (temporal reasoning); IFBench is strict instruction-following; AIME 2025 measures math reasoning.</caption>
    <thead>
      <tr>
        <th style="vertical-align: middle;">Model</th>
        <th style="vertical-align: middle;"><a href="https://arxiv.org/abs/2510.05174">Group Guess</a><br><span style="font-weight:400;font-size:0.7rem;">(1st / 2nd run)</span></th>
        <th style="vertical-align: middle;"><a href="https://arxiv.org/abs/2507.05257">EventQA</a><br><span style="font-weight:400;font-size:0.7rem;">(64K / 128K / 800K)</span></th>
        <th style="vertical-align: middle;"><a href="https://arxiv.org/abs/2507.02833">IFBench</a><br><span style="font-weight:400;font-size:0.7rem;">(Avg / Pass@10)</span></th>
        <th style="vertical-align: middle;"><a href="https://huggingface.co/datasets/opencompass/AIME2025">AIME 2025</a><br><span style="font-weight:400;font-size:0.7rem;">(Avg / Pass@10)</span></th>
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
        <td class="num">73.0 / 71.5</td>
        <td class="num">85.6 / 66.8 / 43.6</td>
        <td class="num">31.5 / 44.6</td>
        <td class="num">50.0 / 73.3</td>
      </tr>
      <tr>
        <td>Δ</td>
        <td class="num delta-pos">+12.0 / +11.0</td>
        <td class="num delta-pos">+1.6 / +4.2 / +6.4</td>
        <td class="num delta-pos">+0.6 / +1.7</td>
        <td class="num"><span class="delta-pos">+1.3 / </span><span class="delta-neutral">+0.0</span></td>
      </tr>
    </tbody>
  </table>
</div>

Our post-trained model's temporal-reasoning ability (EventQA) grows with context length (+1.6 &rarr; +4.2 &rarr; +6.4 from 64K &rarr; 128K &rarr; 800K), providing evidence that encouraging the LLM to implicitly track Hanabi state over long games (60+ turns) generalizes to long-horizon belief tracking in other tasks. Our post-trained model also shows strong gains on a held-out cooperative task (Group Guessing game) and general instruction-following capabilities (IFBench), with small mathematical reasoning improvements (AIME 2025).

## Takeaways {#takeaways}

1. **Modern reasoning LLMs show sparks of cooperative reasoning, but reliable multi-agent coordination remains unsolved.** The best LLMs score between 15 and 18 out of 25 in self-play, comfortably below specialized RL agents (>23) and the median human Hanabi player (~18 to 21).
2. **Scaffold design matters more than model scale.** Moving from Watson to Sherlock improves reasoning models by +2.0 on average; the same scaffold *hurts* most non-reasoning models. Different families respond differently to identical context.
3. **Implicit state and belief tracking is an open and important problem, especially over many turns.** Even a strong reasoning model like o3 drops 1.2 points when moving from engine-provided deductions to self-tracking and Gemini 2.5 Pro drops 3.7 points. Multi-turn belief maintenance is where current models break.
4. **Cross-play interpolates gracefully.** Unlike specialized RL agents, LLMs interpolate smoothly between weak and strong teammates, showing a small but real "spark" of cooperative generalization.
5. **A 4B model can carry surprising weight.** Post-training on our new datasets closes most of the gap to frontier reasoning models on Hanabi *and* transfers to general-purpose temporal reasoning, instruction following and mathematical reasoning, as well as out-of-domain cooperative tasks.

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
