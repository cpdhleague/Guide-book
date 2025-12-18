---
title: " "
baseurl: "/Guide-book"
layout: splash
permalink: /
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.0
  title: " "
  excerpt: " "

---

<div>
<h3 class="archive__subtitle">Latest Articles</h3>

<div class="entries-grid">
  {% assign count = 0 %}
  {% for post in site.posts %}
    {% comment %} Check if the post has a teaser image defined {% endcomment %}
    {% if post.header.teaser %}
      {% include archive-single.html type="grid" %}
      {% assign count = count | plus: 1 %}
    {% endif %}
    
    {% comment %} Stop once we reach 3 posts {% endcomment %}
    {% if count == 3 %}
      {% break %}
    {% endif %}
  {% endfor %}
</div>
</div>

<div style="clear: both;"></div>

## Welcome to CPDH.guide

Our primary mission is to provide the clear, actionable [**Metagame Data**](/Guide-book/meta/) you need to build better decks and understand the format. Our dynamic data displays give you a flowable view of what's winning right now.

But data is only half the story. CPDH.guide is also a [**Library**](/Guide-book/articles/). We're building a platform to celebrate the players and creators who make this format thrive. Check out our latest community-driven articles and PDH videos.

In our [**Resources**](/Guide-book/resources/) section, you'll find everything you need to get started or get ahead, including:
* The official PDH rules
* Links to essential tools like PDHREC
* A growing Decklist Library
* A directory of PDH content creators

Whether you're here to tune into our community or tune your latest deck, we're glad you're here. 
