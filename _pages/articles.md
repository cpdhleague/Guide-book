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

## Latest

<div class="feature__row--images">
  {% assign count = 0 %}
  {% for post in site.posts %}
    
    {% comment %} Only show posts that have a thumbnail {% endcomment %}
    {% if post.header.teaser %}
      {% assign count = count | plus: 1 %}
      
      <div class="feature__item" style="flex-basis: 33.33333%;">
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
    
    {% comment %} Stop after 9 posts to keep the grid even {% endcomment %}
    {% if count == 9 %}
      {% break %}
    {% endif %}
    
  {% endfor %}
</div>

<div style="clear: both;"></div>

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
