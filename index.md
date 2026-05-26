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

{% comment %}
  Homepage sorting logic:
  - Only articles with front_page: true are eligible
  - Pick the most recent from each creator: pdhpod, jalapenos, guide
  - Fill remaining slots (up to 6 total) with next most-recent front_page articles
  - Final list sorted by date, newest first
{% endcomment %}

{% assign front_posts = site.posts | where: "front_page", true %}

{% assign pdhpod_post    = nil %}
{% assign jalapenos_post = nil %}
{% assign guide_post     = nil %}

{% for post in front_posts %}
  {% if pdhpod_post    == nil and post.creator == "pdhpod"    %}{% assign pdhpod_post    = post %}{% endif %}
  {% if jalapenos_post == nil and post.creator == "jalapenos" %}{% assign jalapenos_post = post %}{% endif %}
  {% if guide_post     == nil and post.creator == "guide"     %}{% assign guide_post     = post %}{% endif %}
{% endfor %}

{% assign used_urls = "" | split: "" %}
{% if pdhpod_post    %}{% assign used_urls = used_urls | push: pdhpod_post.url    %}{% endif %}
{% if jalapenos_post %}{% assign used_urls = used_urls | push: jalapenos_post.url %}{% endif %}
{% if guide_post     %}{% assign used_urls = used_urls | push: guide_post.url     %}{% endif %}

{% assign others = "" | split: "" %}
{% for post in front_posts %}
  {% unless used_urls contains post.url %}
    {% if others.size < 3 %}
      {% assign others = others | push: post %}
    {% endif %}
  {% endunless %}
{% endfor %}

{% assign featured = "" | split: "" %}
{% if pdhpod_post    %}{% assign featured = featured | push: pdhpod_post    %}{% endif %}
{% if jalapenos_post %}{% assign featured = featured | push: jalapenos_post %}{% endif %}
{% if guide_post     %}{% assign featured = featured | push: guide_post     %}{% endif %}
{% for post in others %}{% assign featured = featured | push: post %}{% endfor %}

{% assign featured = featured | sort: "date" | reverse %}

<div class="feature__row--images">
  {% for post in featured %}
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
  {% endfor %}
</div>

<div style="text-align: center; margin: 1.5em 0 3em;">
  <a href="/articles/" class="btn btn--inverse btn--large">View All Articles →</a>
</div>

</div>

<div class="home-welcome">

<h2>Welcome to CPDH.guide</h2>

Compete in the ultimate Pauper Commander experience. Our year-long, ELO-based league
is designed for agility — dynamic ranking means new challengers can storm the
leaderboard at any time. Beyond the ladder, level up your game with our expert
articles and live data, or connect with fellow brewers in our Discord. Whether
you're here to study the meta or join the fray, the path to victory is open.

<div style="display: flex; gap: 12px; flex-wrap: wrap; margin-top: 1.5em;">
  <a href="https://app.cpdh.guide" class="btn btn--primary" target="_blank" rel="noopener noreferrer">Join the League</a>
  <a href="/meta/" class="btn btn--inverse">Explore the Meta</a>
  <a href="/articles/" class="btn btn--inverse">Read Articles</a>
  <a href="/resources/" class="btn btn--inverse">Resources</a>
</div>

</div>
