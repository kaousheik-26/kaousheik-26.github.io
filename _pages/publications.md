---
layout: default
title: Publications
permalink: /publications/
order: 2
---

<style>
.blog-list {
  max-width: 720px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.blog-list h1 {
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
  color: #111;
}

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

.blog-card:hover .blog-card-title a {
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

.blog-card-title a {
  color: inherit;
  text-decoration: none;
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
  flex-wrap: wrap; /* required for publications with lots of links */
}

.blog-card-venue {
  background: #f2f2f2;
  padding: 0.12rem 0.45rem;
  border-radius: 100px;
  font-weight: 500;
  color: #444;
}

/* extra classes exclusively for multiple nested links mapping */
.blog-card-links {
  display: flex;
  gap: 0.4rem;
  align-items: center;
}

.blog-card-links a {
  font-size: 0.72rem;
  background: white;
  border: 1px solid #d0d0d0;
  padding: 0.12rem 0.45rem;
  border-radius: 4px;
  color: #333;
  text-decoration: none;
  transition: background 0.15s;
}

.blog-card-links a:hover {
  background: #f5f5f5;
  text-decoration: none;
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

<div class="blog-list">
<br/>
<h1>Selected publications and preprints.</h1>

<!-- 1. AVF -->
<div class="blog-card">
  <div class="blog-card-body">
    <div class="blog-card-meta">Sreyan Ghosh, Arushi Goel, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h2 class="blog-card-title">
      <a href="https://drive.google.com/file/d/1s8loNX_FHOkbM83ws4agPgMEJFzMAY5e/view?usp=sharing">Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos</a>
    </h2>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Preprint · 2026</span>
      <span class="blog-card-venue" style="background:#fff3cd; color:#856404;">Coming Soon</span>
      <span class="blog-card-links">
        <a href="https://drive.google.com/file/d/1s8loNX_FHOkbM83ws4agPgMEJFzMAY5e/view?usp=sharing">📄 Paper</a>
      </span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/AVF.png" alt="Audio-Visual Flamingo Logo" style="transform: scale(1.4);">
  </div>
</div>

<!-- 2. AF Next -->
<div class="blog-card">
  <div class="blog-card-body">
    <div class="blog-card-meta">Sreyan Ghosh, Arushi Goel, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h2 class="blog-card-title">
      <a href="https://arxiv.org/abs/2604.10905">Audio Flamingo Next: Next-Generation Open Audio-Language Models for Speech, Sound, and Music</a>
    </h2>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Preprint · 2026</span>
      <span class="blog-card-links">
        <a href="https://arxiv.org/abs/2604.10905">📄 arXiv</a>
        <a href="https://afnext-umd-nvidia.github.io/">🌐 Project Page</a>
        <a href="https://huggingface.co/nvidia/audio-flamingo-next-hf">🤗 HuggingFace</a>
      </span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/af-next.png" alt="Audio Flamingo Next Logo">
  </div>
</div>

<!-- 3. MMOU -->
<div class="blog-card">
  <div class="blog-card-body">
    <div class="blog-card-meta">Arushi Goel, Sreyan Ghosh, Vatsal Agarwal, Nishit Anand, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</div>
    <h2 class="blog-card-title">
      <a href="https://arxiv.org/abs/2603.14145">MMOU - Massive Multi-Task Omni Understanding and Reasoning Benchmark for Long and Complex Real-World Videos</a>
    </h2>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Preprint · 2026</span>
      <span class="blog-card-links">
        <a href="https://arxiv.org/abs/2603.14145">📄 arXiv</a>
        <a href="https://mmou-bench.github.io/">🌐 Project Page</a>
        <a href="https://huggingface.co/datasets/nvidia/MMOU">🤗 HuggingFace</a>
      </span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/MMOU.png" alt="MMOU Logo">
  </div>
</div>

<!-- 4. CVPR Paper -->
<div class="blog-card">
  <div class="blog-card-body">
    <div class="blog-card-meta">Ramaneswaran Selvakumar*, <strong>Kaousheik Jayakumar</strong>* et al.</div>
    <h2 class="blog-card-title">
      <a href="https://arxiv.org/abs/2604.02605">Do Audio-Visual Large Language Models Really See and Hear?</a>
    </h2>
    <div class="blog-card-footer">
      <span class="blog-card-venue">CVPR Findings · 2026</span>
      <span class="blog-card-links">
        <a href="https://arxiv.org/abs/2604.02605">📄 arXiv</a>
        <a href="https://ramaneswaran.github.io/avllm_interpretability/">🌐 Project Page</a>
      </span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/cvpr.png" alt="CVPR Paper Logo">
  </div>
</div>

<!-- 5. Sparks of Cooperative Reasoning -->
<div class="blog-card">
  <div class="blog-card-body">
    <div class="blog-card-meta">Mahesh Ramesh, <strong>Kaousheik Jayakumar</strong>, et al.</div>
    <h2 class="blog-card-title">
      <a href="https://www.arxiv.org/abs/2601.18077">Sparks of Cooperative Reasoning: Multi-turn LLM Analysis through Hanabi</a>
    </h2>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Preprint · 2026</span>
      <span class="blog-card-links">
        <a href="https://www.arxiv.org/abs/2601.18077">📄 arXiv</a>
        <a href="https://app.primeintellect.ai/dashboard/environments/mahesh-ramesh/hanabi">🌐 Project Page</a>
      </span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/hanabi.png" alt="Hanabi Logo">
  </div>
</div>

<!-- 6. Interspeech Multilingual ASR -->
<div class="blog-card">
  <div class="blog-card-body">
    <div class="blog-card-meta"><strong>Kaousheik Jayakumar</strong>, et al.</div>
    <h2 class="blog-card-title">
      <a href="https://arxiv.org/abs/2305.19584">Multilingual ASR Systems for Indian Languages</a>
    </h2>
    <div class="blog-card-footer">
      <span class="blog-card-venue">Interspeech · 2023</span>
      <span class="blog-card-links">
        <a href="https://arxiv.org/abs/2305.19584">📄 arXiv</a>
      </span>
    </div>
  </div>
  <div class="blog-card-thumbnail">
    <img src="{{ site.url }}/assets/logos/tag-team.png" alt="Tag Team Logo">
  </div>
</div>

</div>
