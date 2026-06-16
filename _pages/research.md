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

/* card styles (shared look with the publications page) */
.research-card {
  display: flex;
  align-items: flex-start;
  gap: 1.25rem;
  padding: 1.5rem 0;
  border-bottom: 1px solid #e6e6e6;
  color: inherit;
}

.research-card-body {
  flex: 1;
  min-width: 0;
}

.research-card-meta {
  font-size: 0.75rem;
  color: #757575;
  margin-bottom: 0.3rem;
}

.research-card-title {
  font-size: 1rem;
  font-weight: 700;
  line-height: 1.3;
  margin: 0 0 0.35rem 0;
  color: #111;
}

.research-card-title a {
  color: inherit;
  text-decoration: none;
}

.research-card-title a:hover {
  text-decoration: underline;
}

.research-card-footer {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  font-size: 0.72rem;
  color: #757575;
  flex-wrap: wrap;
}

.research-card-venue {
  background: #f2f2f2;
  padding: 0.12rem 0.45rem;
  border-radius: 100px;
  font-weight: 500;
  color: #444;
}

.research-card-links {
  display: flex;
  gap: 0.4rem;
  align-items: center;
  flex-wrap: wrap;
}

.research-card-links a {
  font-size: 0.72rem;
  background: white;
  border: 1px solid #d0d0d0;
  padding: 0.12rem 0.45rem;
  border-radius: 4px;
  color: #333;
  text-decoration: none;
  transition: background 0.15s;
}

.research-card-links a:hover {
  background: #f5f5f5;
  text-decoration: none;
}

.research-card-thumbnail {
  width: 140px;
  flex-shrink: 0;
  border-radius: 4px;
  overflow: hidden;
}

.research-card-thumbnail img {
  width: 100%;
  height: auto;
  display: block;
}

@media screen and (max-width: 600px) {
  .research-card {
    flex-direction: column-reverse;
    gap: 0.75rem;
  }
  .research-card-thumbnail {
    width: 100%;
  }
}

/* blog-post cards (moved over from the old blog page) */
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

<p>My research centers on building <strong>multimodal intelligence</strong> — machines that can perceive, reason over, and ground language in what they hear and see. Most of my recent work focuses on <strong>Large Audio(-Visual)-Language Models</strong>: how they fuse audio, vision, and text, where that fusion fails (temporal grounding, modality bias), and how to post-train them for stronger reasoning over long and complex real-world videos.</p>

<p>Alongside this, I study <strong>reasoning and reinforcement learning in language agents</strong> — what cooperative and strategic capabilities emerge in LLMs, and what actually transfers when RL trains an agent. My earlier work at IIT Madras and on the Govt. of India Bhashini project built robust multilingual speech systems for low-resource Indian languages.</p>

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
<p class="research-section-blurb">Large audio-language and audio-visual models, temporal grounding and modality bias, omni understanding of long videos, and multilingual speech recognition.</p>

<!-- Do AV LLMs See and Hear? (CVPR Findings) -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Ramaneswaran Selvakumar*, <strong>Kaousheik Jayakumar</strong>*, S Sakshi, Sreyan Ghosh, Ruohan Gao, Dinesh Manocha</div>
    <h3 class="research-card-title">
      <a href="https://arxiv.org/abs/2604.02605">Do Audio-Visual Large Language Models Really See and Hear?</a>
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">CVPR Findings · Denver, 2026</span>
      <span class="research-card-links">
        <a href="https://arxiv.org/abs/2604.02605">📄 arXiv</a>
        <a href="https://ramaneswaran.github.io/avllm_interpretability/">🌐 Project Page</a>
      </span>
    </div>
  </div>
  <div class="research-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/cvpr.png" alt="Do AV LLMs See and Hear">
  </div>
</div>

<!-- A Closer Look at Failure Modes in Temporal Understanding (Interspeech 2026) -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Apoorva Kulkarni, <strong>Kaousheik Jayakumar</strong>, Sreyan Ghosh, Sarah Wiegreffe, Dinesh Manocha, Ramani Duraiswami</div>
    <h3 class="research-card-title">
      <a href="{{ site.url }}/temporal-reasoning-lalms/">A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models</a>
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">Interspeech · Sydney, 2026</span>
      <span class="research-card-links">
        <a href="{{ site.url }}/temporal-reasoning-lalms/">🌐 Project Page</a>
      </span>
    </div>
  </div>
</div>

<!-- TEMPO (Under Review) -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Apoorva Kulkarni*, <strong>Kaousheik Jayakumar</strong>*, Sreyan Ghosh, Utathya Aich, Ramani Duraiswami, Dinesh Manocha</div>
    <h3 class="research-card-title">
      TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">Under Review · 2026</span>
    </div>
  </div>
</div>

<!-- Audio-Visual Flamingo -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Sreyan Ghosh*, Arushi Goel*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h3 class="research-card-title">
      <a href="https://drive.google.com/file/d/1s8loNX_FHOkbM83ws4agPgMEJFzMAY5e/view?usp=sharing">Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos</a>
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">Under Review · 2026</span>
      <span class="research-card-venue" style="background:#fff3cd; color:#856404;">Coming Soon</span>
      <span class="research-card-links">
        <a href="https://drive.google.com/file/d/1s8loNX_FHOkbM83ws4agPgMEJFzMAY5e/view?usp=sharing">📄 Paper</a>
      </span>
    </div>
  </div>
  <div class="research-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/AVF.png" alt="Audio-Visual Flamingo">
  </div>
</div>

<!-- Audio Flamingo Next -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Sreyan Ghosh*, Arushi Goel*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h3 class="research-card-title">
      <a href="https://arxiv.org/abs/2604.10905">Audio Flamingo Next: Next-Generation Open Audio-Language Models for Speech, Sound, and Music</a>
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">arXiv preprint · 2026</span>
      <span class="research-card-links">
        <a href="https://arxiv.org/abs/2604.10905">📄 arXiv</a>
        <a href="https://afnext-umd-nvidia.github.io/">🌐 Project Page</a>
        <a href="https://huggingface.co/nvidia/audio-flamingo-next-hf">🤗 HuggingFace</a>
      </span>
    </div>
  </div>
  <div class="research-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/af-next.png" alt="Audio Flamingo Next">
  </div>
</div>

<!-- MMOU -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Arushi Goel*, Sreyan Ghosh*, Vatsal Agarwal*, Nishit Anand*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h3 class="research-card-title">
      <a href="https://arxiv.org/abs/2603.14145">Massive Multi-Task Omni Understanding and Reasoning Benchmark for Long Real-World Videos</a>
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">arXiv preprint · 2026</span>
      <span class="research-card-links">
        <a href="https://arxiv.org/abs/2603.14145">📄 arXiv</a>
        <a href="https://mmou-bench.github.io/">🌐 Project Page</a>
        <a href="https://huggingface.co/datasets/nvidia/MMOU">🤗 HuggingFace</a>
      </span>
    </div>
  </div>
  <div class="research-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/MMOU.png" alt="MMOU">
  </div>
</div>

<!-- Tag-Team (Interspeech 2023) -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta"><strong>Kaousheik Jayakumar</strong>, Vrunda N. Sukhadia, A Arunkumar, S Umesh</div>
    <h3 class="research-card-title">
      <a href="https://arxiv.org/abs/2305.19584">The Tag-Team Approach: Leveraging CLS and Language Tagging for Enhancing Multilingual ASR</a>
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">Interspeech · Dublin, 2023</span>
      <span class="research-card-links">
        <a href="https://arxiv.org/abs/2305.19584">📄 arXiv</a>
      </span>
    </div>
  </div>
  <div class="research-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/tag-team.png" alt="Tag-Team Multilingual ASR">
  </div>
</div>

<!-- Building Robust and Scalable Multilingual ASR -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Arjun Gangwar, <strong>Kaousheik Jayakumar</strong>, S Umesh</div>
    <h3 class="research-card-title">
      Building Robust and Scalable Multilingual ASR for Indian Languages
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">arXiv preprint · 2024</span>
    </div>
  </div>
</div>

<!-- ============================================================= -->
<!-- SECTION 2: Natural Language Processing -->
<!-- ============================================================= -->
<h2 class="research-section-title">Natural Language Processing</h2>
<p class="research-section-blurb">Reasoning and reinforcement learning in language agents — emergent cooperative and strategic behavior, multi-turn analysis, and what transfers when RL trains an LLM.</p>

<!-- Sparks of Cooperative Reasoning (ICML 2026) -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Mahesh Ramesh, <strong>Kaousheik Jayakumar</strong>, Aswinkumar Ramkumar, Pavan Thodima, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis</div>
    <h3 class="research-card-title">
      <a href="https://www.arxiv.org/abs/2601.18077">Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents</a>
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">ICML · Seoul, 2026</span>
      <span class="research-card-links">
        <a href="https://www.arxiv.org/abs/2601.18077">📄 arXiv</a>
        <a href="{{ site.url }}/llms-hanabi-cooperative-reasoning/">🌐 Project Page</a>
        <a href="https://app.primeintellect.ai/dashboard/environments/mahesh-ramesh/hanabi">🧪 Environment</a>
        <a href="https://huggingface.co/datasets/Mahesh111000/Hanabi_data">🤗 Dataset</a>
      </span>
    </div>
  </div>
  <div class="research-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/hanabi.png" alt="Hanabi Cooperative Reasoning">
  </div>
</div>

<!-- Playing with Fire (Under Review) -->
<div class="research-card">
  <div class="research-card-body">
    <div class="research-card-meta">Mahesh Ramesh*, <strong>Kaousheik Jayakumar</strong>*, Hemanth Ram, Pavan Thodima, Ramani Duraiswami, Dinesh Manocha, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis</div>
    <h3 class="research-card-title">
      Playing with Fire: What Transfers When RL Trains a Language Agent?
    </h3>
    <div class="research-card-footer">
      <span class="research-card-venue">Under Review · 2026</span>
      <span class="research-card-venue">ICML Workshop on RL from World Feedback</span>
    </div>
  </div>
</div>

<!-- ============================================================= -->
<!-- SECTION 3: Blog Posts -->
<!-- ============================================================= -->
<h2 class="research-section-title">Blog Posts</h2>
<p class="research-section-blurb">Longer-form write-ups and project pages for selected papers.</p>

<a class="blog-card" href="{{ '/temporal-reasoning-lalms' | relative_url }}">
  <div class="blog-card-body">
    <div class="blog-card-meta">Kaousheik Jayakumar</div>
    <h3 class="blog-card-title">A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models</h3>
    <p class="blog-card-subtitle">LALMs consistently fail at foundational temporal tasks — identifying which sound started first, ended last, or lasted longest. We introduce a 1,657-question benchmark for mechanistic diagnosis and find that the problem isn't just modality imbalance: redistributing attention across audio tokens (scaling) outperforms simply increasing audio attention (upweighting). Layer-targeted scaling improves accuracy by 3.2% with no fine-tuning.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Interspeech 2026</span>
      <span>·</span>
      <span>Jun 7, 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/interspeech/task_examples.png" alt="Temporal reasoning task examples">
  </div>
</a>

<a class="blog-card" href="{{ '/llms-hanabi-cooperative-reasoning' | relative_url }}">
  <div class="blog-card-body">
    <div class="blog-card-meta">Kaousheik Jayakumar</div>
    <h3 class="blog-card-title">Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents</h3>
    <p class="blog-card-subtitle">We benchmark 17 LLMs as strategic agents in Hanabi across 2–5 player settings and three scaffolds: Watson, Sherlock, and Mycroft. Our main scaffold, Mycroft, tests whether LLMs can maintain their own evolving belief state across turns without engine-provided deductions. Recent reasoning models show promising cooperative behavior, but still lag behind strong human and specialized Hanabi agents. We also release Hanabi trajectories and move-level judge data for training, and show that a post-trained Qwen3-4B model can substantially close the gap while transferring to other tasks.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">ICML 2026</span>
      <span>·</span>
      <span>Apr 30, 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/icml/firework.png" alt="Hanabi firework teaser">
  </div>
</a>

<a class="blog-card" href="https://ramaneswaran.github.io/avllm_interpretability/">
  <div class="blog-card-body">
    <div class="blog-card-meta">Kaousheik Jayakumar</div>
    <h3 class="blog-card-title">Do Audio-Visual Large Language Models Really See and Hear?</h3>
    <p class="blog-card-subtitle">AVLLMs exhibit a strong vision bias in audio understanding, hallucinating sounds from what they see rather than what they hear. We conduct mechanistic interpretability experiments showing that rich audio semantics exist internally, cross-modal transfer occurs in mid-to-deep layers where vision dominates, and this bias likely stems from vision-centric training.</p>
    <div class="blog-card-footer">
      <span class="blog-card-venue">CVPR Findings 2026</span>
      <span>·</span>
      <span>Apr 6, 2026</span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/cvpr/teaser.png" alt="Audio-Visual Interpretability teaser">
  </div>
</a>

</div>
