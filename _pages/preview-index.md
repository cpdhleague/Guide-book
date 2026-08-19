---
title: "Draft Previews"
layout: splash
permalink: /preview-92fk3a/
classes: short-header wide
sitemap: false
noindex: true
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.6
---

<div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">

<div style="background: rgba(120,60,30,0.25); border: 1px solid rgba(200,120,60,0.5); border-radius: 12px; padding: 1.25em 1.75em; margin-bottom: 2em;">
  <strong style="color: #e5e5e7;">Unlisted drafts.</strong>
  <span style="color: #9ca3af;">
    These articles are not on the homepage, not in /articles/, and not in any RSS feed.
    They are hidden from search engines, but anyone with this URL can view them &mdash;
    treat the link as private.
  </span>
</div>

{% assign drafts = site.previews %}

{% if drafts.size > 0 %}

<h3 class="archive__subtitle" style="margin-top:0;">{{ drafts.size }} draft{% if drafts.size != 1 %}s{% endif %} awaiting review</h3>

<div class="feature__row--images">
  {% for draft in drafts %}
    {% if draft.header.teaser %}
      {% assign draft_image = draft.header.teaser %}
    {% else %}
      {% assign draft_image = "/assets/images/cpdh.png" %}
    {% endif %}
    <div class="feature__item">
      <div class="feature__item__content-wrapper">
        <div class="feature__item-image">
          <a href="{{ draft.url | relative_url }}" class="feature__item-image-link">
            <img src="{{ draft_image | relative_url }}" alt="{{ draft.title | escape }}"
              class="feature__item-image" style="aspect-ratio:16/9;object-fit:cover;">
          </a>
        </div>
        <div class="feature__item-content">
          <p style="font-size:0.8em;color:var(--dim);margin:0 0 0.3em;">
            {% if draft.author %}{{ draft.author }}{% else %}No author set{% endif %}
            {% if draft.categories %} &middot; {{ draft.categories | first }}{% endif %}
          </p>
          <h3 class="feature__item-title">
            <a href="{{ draft.url | relative_url }}">
              {% if draft.title and draft.title != "" %}{{ draft.title }}{% else %}Untitled Draft{% endif %}
            </a>
          </h3>
        </div>
      </div>
    </div>
  {% endfor %}
</div>

{% else %}

<p style="color:var(--dim);font-style:italic;">No drafts in <code>_previews/</code> right now.</p>

{% endif %}

<hr style="margin: 3em 0;">

<div style="background: rgba(26,26,36,0.50); border: 1px solid rgba(58,58,74,0.50); border-radius: 12px; padding: 2em; margin-bottom: 3em;">
  <h3 style="margin-top:0;">How to use this</h3>
  <p style="color:#9ca3af;">
    <strong style="color:#e5e5e7;">To draft an article:</strong>
    put the <code>.md</code> file in <code>_previews/</code> instead of <code>_posts/</code>.
    No date prefix needed on the filename &mdash; <code>bilbo-deck-tech.md</code> is fine.
    Push as normal; it appears here within a couple of minutes.
  </p>
  <p style="color:#9ca3af;">
    <strong style="color:#e5e5e7;">To publish it:</strong>
    move the file from <code>_previews/</code> to <code>_posts/</code> and rename it with a
    date prefix &mdash; <code>2026-08-19-bilbo-deck-tech.md</code>. That single move makes it
    live, listed, and eligible for the feeds.
  </p>
  <p style="color:#9ca3af;margin-bottom:0;">
    <strong style="color:#e5e5e7;">To rotate this secret URL:</strong>
    change the permalink in <code>_config.yml</code> under <code>collections: previews:</code>
    and the <code>permalink</code> at the top of <code>_pages/preview-index.md</code> to match.
  </p>
</div>

</div>
