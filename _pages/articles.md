---
title: "Articles & Guides"
layout: splash
permalink: /articles/
classes: short-header
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  title: "Community Articles"
  excerpt: "Deep dives, deck techs, and tournament reports from the cPDH League."
---

## Latest Articles

<div class="feature__row--images">
  {% for post in site.posts limit:12 %}
    
    {% comment %} --- 1. Set Image (Use Teaser OR Fallback) --- {% endcomment %}
    {% if post.header.teaser %}
      {% assign post_image = post.header.teaser %}
    {% else %}
      {% assign post_image = "/assets/images/cpdh.png" %}
    {% endif %}

    <div class="feature__item" style="flex-basis: 33.33333%; margin-bottom: 30px;">
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
          <h3 class="feature__item-title" style="margin-top: 0.5rem; margin-bottom: 0;">
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

## Topics

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
