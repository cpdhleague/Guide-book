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

<div class="feature__row--images">
  {% for post in site.posts %}
    
    {% if post.header.teaser %}
      {% assign post_image = post.header.teaser %}
    {% else %}
      {% assign post_image = "/assets/images/cpdh.png" %}
    {% endif %}

    <div class="feature__item">
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
              {% if post.title and post.title != "" %}
                {{ post.title }}
              {% else %}
                Untitled Article
              {% endif %}
            </a>
          </h3>
        </div>
        
      </div>
    </div>
    
  {% endfor %}
</div>

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
              <strong>{{ category[0] }}</strong> <span class="taxonomy__count">{{ category[1].size }}</span>
            </a>
          </li>
        {% endfor %}
      </ul>
    </div>
  </div>

  <div style="flex: 1; min-width: 250px; text-align: center;">
    <h3 class="archive__subtitle">Contribute</h3>
    <p style="color: var(--text-secondary, #9a9caa);">Have a deck tech, guide, or opinion piece? We'd love to feature your work.</p>
    <a href="/articles/submit-guide/" class="btn btn--success btn--large">Submit Your Guide</a>
  </div>

</div>

</div>
