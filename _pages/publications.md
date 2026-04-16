---
layout: default
title: Publications
permalink: /publications/
order: 2
---

<style>
.papers-container {
  max-width: 780px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.papers-container h1 {
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
  color: #111;
}

.papers-subtitle {
  font-size: 0.88rem;
  color: #757575;
  margin-bottom: 2rem;
}

.paper-card {
  display: flex;
  align-items: flex-start;
  gap: 1.5rem;
  padding: 1.4rem 0;
  border-bottom: 1px solid #e6e6e6;
}

.paper-card:first-of-type {
  padding-top: 0;
}

.paper-content {
  flex: 1;
  min-width: 0;
}

.paper-thumbnail {
  width: 180px;
  flex-shrink: 0;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid #eaeaea; /* subtle border */
}

.paper-thumbnail img {
  width: 100%;
  height: auto;
  display: block;
}

@media screen and (max-width: 600px) {
  .paper-card {
    flex-direction: column-reverse;
    gap: 1rem;
  }
  .paper-thumbnail {
    width: 60%;
    margin: 0 auto;
  }
}

.paper-venue {
  display: inline-block;
  background: #f2f2f2;
  padding: 0.12rem 0.5rem;
  border-radius: 100px;
  font-size: 0.72rem;
  font-weight: 600;
  color: #444;
  margin-bottom: 0.45rem;
  letter-spacing: 0.01em;
}

.paper-title {
  font-size: 1.05rem;
  font-weight: 700;
  line-height: 1.35;
  margin: 0 0 0.35rem 0;
  color: #111;
}

.paper-title a {
  color: inherit;
  text-decoration: none;
}

.paper-title a:hover {
  text-decoration: underline;
}

.paper-authors {
  font-size: 0.82rem;
  color: #555;
  line-height: 1.5;
  margin: 0 0 0.45rem 0;
}

.paper-authors strong {
  color: #111;
}

.paper-links {
  display: flex;
  gap: 0.6rem;
  flex-wrap: wrap;
  margin-top: 0.4rem;
}

.paper-links a {
  font-size: 0.75rem;
  padding: 0.2rem 0.55rem;
  border: 1px solid #d0d0d0;
  border-radius: 4px;
  color: #333;
  text-decoration: none;
  transition: background 0.15s, border-color 0.15s;
}

.paper-links a:hover {
  background: #f5f5f5;
  border-color: #aaa;
  text-decoration: none;
}
</style>

<div class="papers-container">

<h1>Selected publications and preprints.</h1>

<!-- 1. AVF -->
<div class="paper-card">
  <div class="paper-content">
    <span class="paper-venue">Preprint · 2026</span>
    <span class="paper-venue" style="background:#fff3cd; color:#856404;">Coming Soon</span>
    <h2 class="paper-title">
      <a href="https://drive.google.com/file/d/1s8loNX_FHOkbM83ws4agPgMEJFzMAY5e/view?usp=sharing">Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos</a>
    </h2>
    <p class="paper-authors">
      <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)
    </p>
    <div class="paper-links">
      <a href="https://drive.google.com/file/d/1s8loNX_FHOkbM83ws4agPgMEJFzMAY5e/view?usp=sharing">📄 Paper</a>
    </div>
  </div>
  <div class="paper-thumbnail">
    <img src="{{ site.url }}/assets/logos/AVF.png" alt="Audio-Visual Flamingo Logo">
  </div>
</div>

<!-- 2. AF Next -->
<div class="paper-card">
  <div class="paper-content">
    <span class="paper-venue">Preprint · 2026</span>
    <h2 class="paper-title">
      <a href="https://arxiv.org/abs/2604.10905">Audio Flamingo Next: Next-Generation Open Audio-Language Models for Speech, Sound, and Music</a>
    </h2>
    <p class="paper-authors">
      <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)
    </p>
    <div class="paper-links">
      <a href="https://arxiv.org/abs/2604.10905">📄 arXiv</a>
      <a href="https://afnext-umd-nvidia.github.io/">🌐 Project Page</a>
      <a href="https://huggingface.co/nvidia/audio-flamingo-next-hf">🤗 HuggingFace</a>
    </div>
  </div>
  <div class="paper-thumbnail">
    <img src="{{ site.url }}/assets/logos/af-next.png" alt="Audio Flamingo Next Logo">
  </div>
</div>

<!-- 3. MMOU -->
<div class="paper-card">
  <div class="paper-content">
    <span class="paper-venue">Preprint · 2026</span>
    <h2 class="paper-title">
      <a href="https://arxiv.org/abs/2603.14145">MMOU: Massive Multitask Omni Understanding Benchmark</a>
    </h2>
    <p class="paper-authors">
      <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)
    </p>
    <div class="paper-links">
      <a href="https://arxiv.org/abs/2603.14145">📄 arXiv</a>
      <a href="https://mmou-bench.github.io/">🌐 Project Page</a>
      <a href="https://huggingface.co/datasets/nvidia/MMOU">🤗 HuggingFace</a>
    </div>
  </div>
  <div class="paper-thumbnail">
    <img src="{{ site.url }}/assets/logos/MMOU.png" alt="MMOU Logo">
  </div>
</div>

<!-- 4. CVPR Paper -->
<div class="paper-card">
  <div class="paper-content">
    <span class="paper-venue">CVPR Findings · 2026</span>
    <h2 class="paper-title">
      <a href="https://arxiv.org/abs/2604.02605">Do Audio-Visual Large Language Models Really See and Hear?</a>
    </h2>
    <p class="paper-authors">
      <strong>Kaousheik Jayakumar</strong>, et al.
    </p>
    <div class="paper-links">
      <a href="https://arxiv.org/abs/2604.02605">📄 arXiv</a>
      <a href="https://ramaneswaran.github.io/avllm_interpretability/">🌐 Project Page</a>
    </div>
  </div>
  <div class="paper-thumbnail">
    <img src="{{ site.url }}/assets/logos/cvpr.png" alt="CVPR Paper Logo">
  </div>
</div>

<!-- 5. Sparks of Cooperative Reasoning -->
<div class="paper-card">
  <div class="paper-content">
    <span class="paper-venue">Preprint · 2026</span>
    <h2 class="paper-title">
      <a href="https://www.arxiv.org/abs/2601.18077">Sparks of Cooperative Reasoning: Multi-turn LLM Analysis through Hanabi</a>
    </h2>
    <p class="paper-authors">
      <strong>Kaousheik Jayakumar</strong>, et al.
    </p>
    <div class="paper-links">
      <a href="https://www.arxiv.org/abs/2601.18077">📄 arXiv</a>
      <a href="https://app.primeintellect.ai/dashboard/environments/mahesh-ramesh/hanabi">🌐 Project Page</a>
    </div>
  </div>
  <div class="paper-thumbnail">
    <img src="{{ site.url }}/assets/logos/hanabi.png" alt="Hanabi Logo">
  </div>
</div>

<!-- 6. Interspeech Multilingual ASR -->
<div class="paper-card">
  <div class="paper-content">
    <span class="paper-venue">Interspeech · 2023</span>
    <h2 class="paper-title">
      <a href="https://arxiv.org/abs/2305.19584">Multilingual ASR Systems for Indian Languages</a>
    </h2>
    <p class="paper-authors">
      <strong>Kaousheik Jayakumar</strong>, et al.
    </p>
    <div class="paper-links">
      <a href="https://arxiv.org/abs/2305.19584">📄 arXiv</a>
    </div>
  </div>
  <div class="paper-thumbnail">
    <img src="{{ site.url }}/assets/logos/tag-team.png" alt="Tag Team Logo">
  </div>
</div>

</div>
