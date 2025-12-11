---
title: "Articles & Guides"
layout: splash
permalink: /articles/
header:
  overlay_image: /assets/images/Gemini_Generated_Image_bpu1z6bpu1z6bpu1.png
  overlay_filter: 0.5
  title: "Community Articles"
  excerpt: "Deep dives, deck techs, and tournament reports from the cPDH League."
---

## Latest Articles

<div class="entries-grid">
  {% for post in site.posts limit:6 %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>

## Browse by Topic

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
