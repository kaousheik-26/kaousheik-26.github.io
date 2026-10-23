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
  font-size: 1.2rem;
  font-weight: 700;
  color: #111;
  margin: 2.4rem 0 1rem 0;
  padding-bottom: 0.35rem;
  border-bottom: 2px solid #111;
}

/* plain publication list, in the style of a classic academic homepage */
.pub-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.pub-entry {
  padding: 0.95rem 0;
  border-bottom: 1px solid #e6e6e6;
  font-size: 0.92rem;
  line-height: 1.55;
}

.pub-entry:last-child {
  border-bottom: none;
}

.pub-title {
  font-weight: 600;
  color: #111;
  text-decoration: none;
}

.pub-title:hover {
  text-decoration: underline;
}

.pub-authors {
  color: #444;
}

.pub-links a {
  color: #1a56db;
  text-decoration: none;
}

.pub-links a:hover {
  text-decoration: underline;
}

.pub-venue {
  font-weight: 700;
  color: #111;
}

.pub-highlight {
  color: #c0392b;
  font-weight: 700;
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
<!-- SECTION 1: Audio -->
<!-- ============================================================= -->
<h2 class="research-section-title">Audio</h2>

<ul class="pub-list">

  <li class="pub-entry">
    <a class="pub-title" href="{{ site.url }}/tempo/">TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models</a> <br/>
    <span class="pub-authors">Apoorva Kulkarni*, <strong>Kaousheik Jayakumar</strong>*, Sreyan Ghosh, Utathya Aich, Ramani Duraiswami, Dinesh Manocha</span> <br/>
    <span class="pub-links"><a href="{{ site.url }}/tempo/">Project Page</a> / <a href="https://arxiv.org/abs/2608.29999">arXiv</a> / <a href="https://github.com/kaousheik-26/tempo">Code</a> / <a href="https://huggingface.co/datasets/Kaousheik/tempo">Dataset</a> / <a href="https://huggingface.co/collections/Kaousheik/tempo-6a8a96ced2752994aa9034e2">Checkpoints</a></span> <br/>
    <span class="pub-venue">EMNLP 2026 (Main Conference)</span> <span class="pub-highlight">(Oral)</span>
  </li>

  <li class="pub-entry">
    <a class="pub-title" href="https://arxiv.org/abs/2606.17417">A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models</a> <br/>
    <span class="pub-authors">Apoorva Kulkarni, <strong>Kaousheik Jayakumar</strong>, Sreyan Ghosh, Sarah Wiegreffe, Dinesh Manocha, Ramani Duraiswami</span> <br/>
    <span class="pub-links"><a href="https://arxiv.org/abs/2606.17417">arXiv</a> / <a href="{{ '/temporal-reasoning-lalms' | relative_url }}">Project Page</a> / <a href="https://huggingface.co/datasets/gamma-lab-umd/temporal-lalm">Dataset</a></span> <br/>
    <span class="pub-venue">Interspeech 2026</span>
  </li>

  <li class="pub-entry">
    <a class="pub-title" href="https://arxiv.org/abs/2305.19584">The Tag-Team Approach: Leveraging CLS and Language Tagging for Enhancing Multilingual ASR</a> <br/>
    <span class="pub-authors"><strong>Kaousheik Jayakumar</strong>, Vrunda N. Sukhadia, A Arunkumar, S Umesh</span> <br/>
    <span class="pub-links"><a href="https://arxiv.org/abs/2305.19584">arXiv</a></span> <br/>
    <span class="pub-venue">Interspeech 2023</span>
  </li>

</ul>

<!-- ============================================================= -->
<!-- SECTION 2: Audio-Visual -->
<!-- ============================================================= -->
<h2 class="research-section-title">Audio-Visual</h2>

<ul class="pub-list">

  <li class="pub-entry">
    <a class="pub-title" href="https://arxiv.org/abs/2607.16107">Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos</a> <br/>
    <span class="pub-authors">Sreyan Ghosh*, Arushi Goel*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</span> <br/>
    <span class="pub-links"><a href="https://arxiv.org/abs/2607.16107">arXiv</a> / <a href="https://avflamingo.pages.dev/">Project Page</a></span> <br/>
    <span class="pub-venue">NeurIPS 2026</span>
  </li>

  <li class="pub-entry">
    <a class="pub-title" href="https://arxiv.org/abs/2603.14145">MMOU: Massive Multi-Task Omni Understanding and Reasoning Benchmark for Long and Complex Real-World Videos</a> <br/>
    <span class="pub-authors">Arushi Goel*, Sreyan Ghosh*, Vatsal Agarwal*, Nishit Anand*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</span> <br/>
    <span class="pub-links"><a href="https://arxiv.org/abs/2603.14145">arXiv</a> / <a href="https://mmou-bench.github.io/">Project Page</a> / <a href="https://huggingface.co/datasets/nvidia/MMOU">Data</a></span> <br/>
    <span class="pub-venue">NeurIPS 2026 Dataset and Benchmark Track</span>
  </li>

  <li class="pub-entry">
    <a class="pub-title" href="https://arxiv.org/abs/2604.02605">Do Audio-Visual Large Language Models Really See and Hear?</a> <br/>
    <span class="pub-authors">Ramaneswaran Selvakumar*, <strong>Kaousheik Jayakumar</strong>*, S Sakshi, Sreyan Ghosh, Ruohan Gao, Dinesh Manocha</span> <br/>
    <span class="pub-links"><a href="https://arxiv.org/abs/2604.02605">arXiv</a> / <a href="https://ramaneswaran.github.io/avllm_interpretability/">Project Page</a></span> <br/>
    <span class="pub-venue">CVPR 2026 (Findings)</span>
  </li>

</ul>

<!-- ============================================================= -->
<!-- SECTION 3: LLM Post-training -->
<!-- ============================================================= -->
<h2 class="research-section-title">LLM Post-training</h2>

<ul class="pub-list">

  <li class="pub-entry">
    <a class="pub-title" href="https://www.arxiv.org/abs/2601.18077">Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents</a> <br/>
    <span class="pub-authors">Mahesh Ramesh, <strong>Kaousheik Jayakumar</strong>, Aswinkumar Ramkumar, Pavan Thodima, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis</span> <br/>
    <span class="pub-links"><a href="https://www.arxiv.org/abs/2601.18077">arXiv</a> / <a href="{{ '/llms-hanabi-cooperative-reasoning' | relative_url }}">Project Page</a> / <a href="https://app.primeintellect.ai/dashboard/environments/mahesh-ramesh/hanabi">Environment</a></span> <br/>
    <span class="pub-venue">ICML 2026</span>
  </li>

  <li class="pub-entry">
    <a class="pub-title" href="{{ site.url }}/playing-with-fire/">Playing with Fire: What Transfers When RL Trains a Language Agent?</a> <br/>
    <span class="pub-authors">Mahesh Ramesh*, <strong>Kaousheik Jayakumar</strong>*, Hemanth Ram, Pavan Thodima, Ramani Duraiswami, Dinesh Manocha, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis</span> <br/>
    <span class="pub-links"><a href="{{ site.url }}/playing-with-fire/">Project Page</a></span> <br/>
    <span class="pub-venue">ICML Workshop on RL from World Feedback · 2026</span> <br/>
    <span class="pub-venue">COLM Workshop on Efficient Reasoning · 2026</span> <span class="pub-highlight">(Spotlight)</span>
  </li>

</ul>

<!-- ============================================================= -->
<!-- SECTION 4: Preprints -->
<!-- ============================================================= -->
<h2 class="research-section-title">Preprints</h2>

<ul class="pub-list">

  <li class="pub-entry">
    <a class="pub-title" href="https://arxiv.org/abs/2604.10905">Audio Flamingo Next: Next-Generation Open Audio-Language Models for Speech, Sound, and Music</a> <br/>
    <span class="pub-authors">Sreyan Ghosh*, Arushi Goel*, <strong>Kaousheik Jayakumar</strong>, et al. (in collaboration with NVIDIA)</span> <br/>
    <span class="pub-links"><a href="https://arxiv.org/abs/2604.10905">arXiv</a> / <a href="https://afnext-umd-nvidia.github.io/">Project Page</a> / <a href="https://huggingface.co/nvidia/audio-flamingo-next-hf">HuggingFace</a></span> <br/>
    <span class="pub-venue">Preprint · 2026</span>
  </li>

  <li class="pub-entry">
    <a class="pub-title" href="https://arxiv.org/pdf/2511.15418">Building Robust and Scalable Multilingual ASR for Indian Languages</a> <br/>
    <span class="pub-authors">Arjun Gangwar, <strong>Kaousheik Jayakumar</strong>, S. Umesh</span> <br/>
    <span class="pub-links"><a href="https://arxiv.org/pdf/2511.15418">arXiv</a></span> <br/>
    <span class="pub-venue">Preprint · 2026</span>
  </li>

</ul>

</div>
