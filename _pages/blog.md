---
layout: default
title: Blog
permalink: /blog/
order: 3
---

<style>
.blog-list {
  max-width: 720px;
  margin: 2rem auto;
  padding: 0 1rem;
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

<div class="blog-list">

<a class="blog-card" href="https://ramaneswaran.github.io/avllm_interpretability/">
  <div class="blog-card-body">
    <div class="blog-card-meta">Kaousheik Jayakumar</div>
    <h2 class="blog-card-title">Do Audio-Visual Large Language Models Really See and Hear?</h2>
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
