---
title: " "
layout: splash
permalink: /
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.0
  title: " "
  excerpt: " "
---

<div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">

<h3 class="archive__subtitle" style="margin-top: 2em;">Latest Articles</h3>

<div class="feature__row--images">
  {% assign count = 0 %}
  {% for post in site.posts %}
    {% if post.header.teaser %}
      {% assign count = count | plus: 1 %}
      <div class="feature__item">
        <div class="feature__item__content-wrapper">
          <div class="feature__item-image">
            <a href="{{ post.url | relative_url }}" class="feature__item-image-link">
              <img 
                src="{{ post.header.teaser | relative_url }}" 
                alt="{{ post.title | escape }}" 
                class="feature__item-image"
              >
            </a>
          </div>
          <div class="feature__item-content">
            <h3 class="feature__item-title">
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
          </div>
        </div>
      </div>
    {% endif %}
    {% if count == 6 %}{% break %}{% endif %}
  {% endfor %}
</div>

<div style="text-align: center; margin: 1.5em 0 3em;">
  <a href="/articles/" class="btn btn--inverse btn--large">View All Articles →</a>
</div>

</div>

<div class="home-welcome">

<h2>Welcome to CPDH.guide</h2>

Compete in the ultimate Pauper Commander experience. Our year-long, ELO-based league is designed for agility—dynamic ranking means new challengers can storm the leaderboard at any time. Leverage our live metagame data to master the format, refine your deck, and prove your skill.

<div style="display: flex; gap: 12px; flex-wrap: wrap; margin-top: 1.5em;">
  <a href="https://app.cpdh.guide" class="btn btn--primary">Join the League</a>
  <a href="/meta/" class="btn btn--inverse">Explore the Meta</a>
  <a href="/articles/" class="btn btn--inverse">Read Articles</a>
  <a href="/resources/" class="btn btn--inverse">Resources</a>
</div>

</div>
