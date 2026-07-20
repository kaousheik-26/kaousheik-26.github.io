---
layout: default
title: Research
permalink: /research/
order: 1
---

<style>
.research-list {
  max-width: 760px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.research-intro h1 {
  font-size: 1.7rem;
  font-weight: 700;
  margin-bottom: 0.6rem;
  color: #111;
}

.research-intro p {
  font-size: 0.92rem;
  line-height: 1.6;
  color: #333;
  margin: 0 0 0.9rem 0;
}

.research-profiles {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0 0.5rem 0;
}

.research-profiles a {
  font-size: 0.8rem;
  background: #f2f2f2;
  border: 1px solid #e0e0e0;
  padding: 0.3rem 0.7rem;
  border-radius: 100px;
  color: #333;
  text-decoration: none;
  transition: background 0.15s;
}

.research-profiles a:hover {
  background: #e8e8e8;
  text-decoration: none;
}

.research-section-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #111;
  margin: 2.4rem 0 0.2rem 0;
  padding-bottom: 0.35rem;
  border-bottom: 2px solid #111;
}

.research-section-blurb {
  font-size: 0.82rem;
  color: #666;
  line-height: 1.5;
  margin: 0.5rem 0 0.4rem 0;
}

/* blog-card template (shared look for every research entry) */
.blog-card {
  display: flex;
  align-items: flex-start;
  gap: 1.25rem;
  padding: 1.5rem 0;
  border-bottom: 1px solid #e6e6e6;
  text-decoration: none;
  color: inherit;
  transition: background 0.15s;
}

.blog-card:hover {
  text-decoration: none;
  color: inherit;
}

.blog-card:hover .blog-card-title {
  text-decoration: underline;
}

.blog-card-body {
  flex: 1;
  min-width: 0;
}

.blog-card-meta {
  font-size: 0.75rem;
  color: #757575;
  margin-bottom: 0.3rem;
}

.blog-card-title {
  font-size: 1rem;
  font-weight: 700;
  line-height: 1.3;
  margin: 0 0 0.35rem 0;
  color: #111;
}

.blog-card-subtitle {
  font-size: 0.82rem;
  color: #555;
  line-height: 1.45;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.blog-card-footer {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  font-size: 0.72rem;
  color: #757575;
  flex-wrap: wrap;
}

.blog-card-venue {
  background: #f2f2f2;
  padding: 0.12rem 0.45rem;
  border-radius: 100px;
  font-weight: 500;
  color: #444;
}

.blog-card-thumbnail {
  width: 140px;
  flex-shrink: 0;
  border-radius: 4px;
  overflow: hidden;
}

.blog-card-thumbnail img {
  width: 100%;
  height: auto;
  display: block;
}

@media screen and (max-width: 600px) {
  .blog-card {
    flex-direction: column-reverse;
    gap: 0.75rem;
  }
  .blog-card-thumbnail {
    width: 100%;
  }
}
</style>

<div class="research-list">
<br/>

<div class="research-intro">
<h1>Research</h1>

<p>My research centers on building <strong>multimodal intelligence</strong>; machines that can perceive, reason over, and ground language in what they hear and see. Most of my recent work focuses on <strong>Large Audio(-Visual)-Language Models</strong>: how they fuse audio, vision, and text, where that fusion fails (temporal grounding, modality bias), and how to post-train them for stronger reasoning over long and complex real-world videos.</p>

<p>Alongside this, I study <strong>reasoning and reinforcement learning in language agents</strong>;  what cooperative and strategic capabilities emerge in LLMs, and what actually transfers when RL trains an agent. My earlier work at IIT Madras and on the Govt. of India Bhashini project built robust multilingual speech systems for low-resource Indian languages.</p>

<div class="research-profiles">
  <a href="https://scholar.google.com/citations?user=Yc8bSDIAAAAJ&hl=en">📚 Google Scholar</a>
  <a href="{{ site.url }}/assets/kaousheik_CV.pdf">📄 CV / Resume</a>
  <a href="mailto:kaousheik@gmail.com">✉️ Email</a>
</div>
</div>

<!-- ============================================================= -->
<!-- SECTION 1: Audio Understanding and Processing -->
<!-- ============================================================= -->
<h2 class="research-section-title">Audio Understanding and Processing</h2>

<!-- Do AV LLMs See and Hear? (CVPR Findings) -->
<a class="blog-card" href="https://ramaneswaran.github.io/avllm_interpretability/">
  <div class="blog-card-body">
    <div class="blog-card-meta">Ramaneswaran Selvakumar*, <strong>Kaousheik Jayakumar</strong>*, S Sakshi, Sreyan Ghosh, Ruohan Gao, Dinesh Manocha</div>
    <h3 class="blog-card-title">Do Audio-Visual Large Language Models Really See and Hear?</h3>
    <p class="blog-card-subtitle">AVLLMs exhibit a strong vision bias in audio understanding, hallucinating sounds from what they see rather than what they hear. We conduct mechanistic interpretability experiments showing that rich audio semantics exist internally, cross-modal transfer occurs in mid-to-deep layers where vision dominates, and this bias likely stems from vision-centric training.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">CVPR Findings · Denver, 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/cvpr.png" alt="Do AV LLMs See and Hear">
  </div>
</a>

<!-- A Closer Look at Failure Modes in Temporal Understanding (Interspeech 2026) -->
<a class="blog-card" href="{{ '/temporal-reasoning-lalms' | relative_url }}">
  <div class="blog-card-body">
    <div class="blog-card-meta">Apoorva Kulkarni, <strong>Kaousheik Jayakumar</strong>, Sreyan Ghosh, Sarah Wiegreffe, Dinesh Manocha, Ramani Duraiswami</div>
    <h3 class="blog-card-title">A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models</h3>
    <p class="blog-card-subtitle">LALMs consistently fail at foundational temporal tasks — identifying which sound started first, ended last, or lasted longest. We introduce a 1,657-question benchmark for mechanistic diagnosis and find that the problem isn't just modality imbalance: redistributing attention across audio tokens (scaling) outperforms simply increasing audio attention (upweighting). Layer-targeted scaling improves accuracy by 3.2% with no fine-tuning.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Interspeech · Sydney, 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/interspeech/task_examples.png" alt="Temporal reasoning task examples">
  </div>
</a>

<!-- Audio-Visual Flamingo -->
<a class="blog-card" href="https://arxiv.org/abs/2607.16107">
  <div class="blog-card-body">
    <div class="blog-card-meta">Sreyan Ghosh*, Arushi Goel*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h3 class="blog-card-title">Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos</h3>
    <p class="blog-card-subtitle">An open audio-visual model built to understand long and complex videos, jointly reasoning over speech, sound, and what's on screen across extended temporal contexts — advancing open audio-visual intelligence beyond short clips.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Under Review · 2026</span>
      <span class="blog-card-venue" style="background:#fff3cd; color:#856404;">Coming Soon</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/AVF.png" alt="Audio-Visual Flamingo">
  </div>
</a>

<!-- Audio Flamingo Next -->
<a class="blog-card" href="https://huggingface.co/nvidia/audio-flamingo-next-hf">
  <div class="blog-card-body">
    <div class="blog-card-meta">Sreyan Ghosh*, Arushi Goel*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h3 class="blog-card-title">Audio Flamingo Next: Next-Generation Open Audio-Language Models for Speech, Sound, and Music</h3>
    <p class="blog-card-subtitle">The next generation of open audio-language models spanning speech, sound, and music — pushing open audio intelligence with stronger reasoning and broader coverage across the full audio spectrum.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">arXiv preprint · 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/af-next.png" alt="Audio Flamingo Next">
  </div>
</a>

<!-- MMOU -->
<a class="blog-card" href="https://mmou.pages.dev/">
  <div class="blog-card-body">
    <div class="blog-card-meta">Arushi Goel*, Sreyan Ghosh*, Vatsal Agarwal*, Nishit Anand*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h3 class="blog-card-title">Massive Multi-Task Omni Understanding and Reasoning Benchmark for Long Real-World Videos</h3>
    <p class="blog-card-subtitle">A massive multi-task benchmark for omni understanding and reasoning over long, real-world videos, stress-testing models across audio, vision, and language jointly rather than in isolation.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">arXiv preprint · 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/MMOU.png" alt="MMOU">
  </div>
</a>

<!-- Tag-Team (Interspeech 2023) -->
<a class="blog-card" href="https://arxiv.org/abs/2305.19584">
  <div class="blog-card-body">
    <div class="blog-card-meta"><strong>Kaousheik Jayakumar</strong>, Vrunda N. Sukhadia, A Arunkumar, S Umesh</div>
    <h3 class="blog-card-title">The Tag-Team Approach: Leveraging CLS and Language Tagging for Enhancing Multilingual ASR</h3>
    <p class="blog-card-subtitle">We leverage CLS tokens and explicit language tagging to improve multilingual ASR across Indian languages, boosting recognition for low-resource languages over the corresponding monolingual baselines.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Interspeech · Dublin, 2023</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/tag-team.png" alt="Tag-Team Multilingual ASR">
  </div>
</a>

<!-- ============================================================= -->
<!-- SECTION 2: Natural Language Processing -->
<!-- ============================================================= -->
<h2 class="research-section-title">Natural Language Processing</h2>

<!-- Sparks of Cooperative Reasoning (ICML 2026) -->
<a class="blog-card" href="{{ '/llms-hanabi-cooperative-reasoning' | relative_url }}">
  <div class="blog-card-body">
    <div class="blog-card-meta">Mahesh Ramesh, <strong>Kaousheik Jayakumar</strong>, Aswinkumar Ramkumar, Pavan Thodima, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis</div>
    <h3 class="blog-card-title">Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents</h3>
    <p class="blog-card-subtitle">We benchmark 17 LLMs as strategic agents in Hanabi across 2–5 player settings and three scaffolds: Watson, Sherlock, and Mycroft. Our main scaffold, Mycroft, tests whether LLMs can maintain their own evolving belief state across turns without engine-provided deductions. Recent reasoning models show promising cooperative behavior, but still lag behind strong human and specialized Hanabi agents. We also release Hanabi trajectories and move-level judge data for training, and show that a post-trained Qwen3-4B model can substantially close the gap while transferring to other tasks.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">ICML · Seoul, 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/hanabi.png" alt="Hanabi Cooperative Reasoning">
  </div>
</a>

<!-- Playing with Fire -->
<a class="blog-card" href="{{ site.url }}/playing-with-fire/">
  <div class="blog-card-body">
    <div class="blog-card-meta">Mahesh Ramesh*, <strong>Kaousheik Jayakumar</strong>*, Hemanth Ram, Pavan Thodima, Ramani Duraiswami, Dinesh Manocha, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis</div>
    <h3 class="blog-card-title">Playing with Fire: What Transfers When RL Trains a Language Agent?</h3>
    <p class="blog-card-subtitle">We study what actually transfers when reinforcement learning trains a language agent — separating the skills that generalize to out-of-domain tasks from those that overfit to the training environment.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">ICML Workshop on RL from World Feedback · 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/neurips_2026/playing_with_fire_teaser.jpeg" alt="Playing with Fire teaser">
  </div>
</a>

</div>
