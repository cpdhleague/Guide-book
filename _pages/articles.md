---
title: "Articles & Guides"
layout: splash
permalink: /articles/
classes: short-header wide
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  title: "Articles & Guides"
  excerpt: "Deep dives, deck techs, and tournament reports from the cPDH community."
---

<div style="max-width: 1200px; margin: 0 auto;">

<h3 class="archive__subtitle" style="margin-top: 0;">All Articles</h3>

<div class="feature__row--images" id="articles-grid">
  {% assign visible_count = 0 %}
  {% for post in site.posts %}

    {% comment %} Skip hidden and archive-only articles {% endcomment %}
    {% if post.hidden == true or post.archive_only == true %}{% continue %}{% endif %}

    {% if post.header.teaser %}
      {% assign post_image = post.header.teaser %}
    {% else %}
      {% assign post_image = "/assets/images/cpdh.png" %}
    {% endif %}

    {% assign visible_count = visible_count | plus: 1 %}

    <div class="feature__item article-card"
      {% if visible_count > 9 %}style="display:none;"{% endif %}
      data-index="{{ visible_count }}">
      <div class="feature__item__content-wrapper">
        <div class="feature__item-image">
          <a href="{{ post.url | relative_url }}" class="feature__item-image-link">
            <img
              src="{{ post_image | relative_url }}"
              alt="{{ post.title | escape }}"
              class="feature__item-image"
              style="aspect-ratio: 16/9; object-fit: cover;"
            >
          </a>
        </div>
        <div class="feature__item-content">
          <h3 class="feature__item-title">
            <a href="{{ post.url | relative_url }}">
              {% if post.title and post.title != "" %}{{ post.title }}{% else %}Untitled Article{% endif %}
            </a>
          </h3>
        </div>
      </div>
    </div>

  {% endfor %}
</div>

<div id="load-more-wrap" style="text-align: center; margin: 2em 0 3em;">
  <button id="load-more-btn" class="btn btn--inverse btn--large" onclick="loadMoreArticles()">
    Load More Articles
  </button>
</div>

<script>
  var shown = 9;
  var batchSize = 9;

  function loadMoreArticles() {
    var cards = document.querySelectorAll('.article-card');
    var loadedCount = 0;

    for (var i = 0; i < cards.length; i++) {
      if (cards[i].style.display === 'none') {
        cards[i].style.display = '';
        loadedCount++;
        if (loadedCount >= batchSize) break;
      }
    }

    shown += loadedCount;

    if (shown >= cards.length) {
      document.getElementById('load-more-wrap').style.display = 'none';
    }
  }
</script>

<div style="clear: both;"></div>
<hr style="margin: 3em 0;">

<div style="display: flex; flex-wrap: wrap; gap: 40px; align-items: flex-start; margin-bottom: 3em;">

  <div style="flex: 1; min-width: 250px;">
    <h3 class="archive__subtitle">Topics</h3>
    <div class="archive-taxonomy-list">
      <ul class="taxonomy__index">
        {% for category in site.categories %}
          <li>
            <a href="{{ category[0] | slugify | prepend: '/categories/#' | relative_url }}">
              <strong>{{ category[0] }}</strong>
              <span class="taxonomy__count">{{ category[1].size }}</span>
            </a>
          </li>
        {% endfor %}
      </ul>
    </div>
  </div>

  <div style="flex: 1; min-width: 250px; text-align: center;">
    <h3 class="archive__subtitle">Contribute</h3>
    <p style="color: #9ca3af;">Have a deck tech, guide, or opinion piece? We'd love to feature your work.</p>
    <a href="/articles/submit-guide/" class="btn btn--success btn--large">Submit Your Guide</a>
  </div>

</div>

</div>
