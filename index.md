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

Our primary mission is to provide the clear, actionable [**Metagame Data**](/meta/) you need to build better decks and understand the format. Our dynamic data displays give you a flowable view of what's winning right now.

But data is only half the story. We're building a platform to celebrate the players and creators who make this format thrive. Check out our latest community-driven [**articles and PDH videos**](/articles/).

In our [**Resources**](/resources/) section, you'll find everything you need to get started or get ahead — the official [PDH rules](/resources/rules/), links to essential tools like PDHREC, a growing [Decklist Library](/library), and a directory of [PDH content creators](/resources/content-creators/).

Whether you're here to tune into our community or tune your latest deck, we're glad you're here.

<div style="display: flex; gap: 12px; flex-wrap: wrap; margin-top: 1.5em;">
  <a href="/meta/" class="btn btn--primary">Explore the Meta</a>
  <a href="/articles/" class="btn btn--inverse">Read Articles</a>
  <a href="/resources/" class="btn btn--inverse">Resources</a>
</div>

</div>
