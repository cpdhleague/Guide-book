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

<!-- Active filter banner — shown via JS when ?creator= param is present -->
<div id="active-filter" style="display:none; align-items:center; gap:12px;
  background:var(--primary-dim); border:1px solid var(--border-accent);
  border-radius:var(--radius-md); padding:0.75em 1.25em; margin-bottom:1.5em;">
  <span style="color:var(--pale); font-family:var(--font-display); font-size:0.9em; letter-spacing:0.05em; text-transform:uppercase;">
    Showing content from: <strong id="filter-label" style="color:var(--primary-glow);"></strong>
  </span>
  <a href="/articles/" style="margin-left:auto; color:var(--dim); font-size:0.85em;
    border:1px solid var(--border-subtle); padding:0.2em 0.8em;
    border-radius:100px; text-decoration:none;">
    ✕ Clear filter
  </a>
</div>

<h3 class="archive__subtitle" style="margin-top:0;">All Articles</h3>

<div class="feature__row--images" id="articles-grid">
  {% assign visible_count = 0 %}
  {% for post in site.posts %}

    {% if post.hidden == true or post.archive_only == true %}{% continue %}{% endif %}

    {% if post.header.teaser %}
      {% assign post_image = post.header.teaser %}
    {% else %}
      {% assign post_image = "/assets/images/cpdh.png" %}
    {% endif %}

    {% assign visible_count = visible_count | plus: 1 %}

    <div class="feature__item article-card"
      data-author="{{ post.author }}"
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
  var BATCH = 30;
  var shown = 0;

  function initPage() {
    var params = new URLSearchParams(window.location.search);
    var author = params.get('author');
    var cards  = Array.from(document.querySelectorAll('.article-card'));

    if (author) {
      // Filter mode: show all matching, hide everything else, no load-more needed
      cards.forEach(function(card) {
        card.style.display = card.dataset.author === author ? '' : 'none';
      });
      document.getElementById('load-more-wrap').style.display = 'none';

      var knownNames = { pdhpod: 'The PDH Pod', jalapenos: 'Jalapeno Paupers', ginger: 'Ginger Persolus', beachbodgod69: 'BeachBodGod69' };
      document.getElementById('filter-label').textContent = knownNames[author] || author;
      document.getElementById('active-filter').style.display = 'flex';

    } else {
      // Normal mode: show first BATCH, hide the rest
      cards.forEach(function(card, i) {
        card.style.display = i < BATCH ? '' : 'none';
      });
      shown = Math.min(BATCH, cards.length);
      if (shown >= cards.length) {
        document.getElementById('load-more-wrap').style.display = 'none';
      }
    }
  }

  function loadMoreArticles() {
    var cards = Array.from(document.querySelectorAll('.article-card'));
    var loaded = 0;
    for (var i = 0; i < cards.length; i++) {
      if (cards[i].style.display === 'none') {
        cards[i].style.display = '';
        loaded++;
        if (loaded >= BATCH) break;
      }
    }
    shown += loaded;
    if (shown >= cards.length) {
      document.getElementById('load-more-wrap').style.display = 'none';
    }
  }

  initPage();
</script>

<div style="clear: both;"></div>
<hr style="margin: 3em 0;">

<div style="display: flex; flex-wrap: wrap; gap: 40px; align-items: flex-start; margin-bottom: 3em;">
  <div style="flex: 1; min-width: 250px;">
    <h3 class="archive__subtitle">Topics</h3>
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

  <div style="flex: 1; min-width: 250px;">
    <h3 class="archive__subtitle">Submit Your Deck Tech</h3>
    <p style="color: var(--dim); font-size: 0.95em; margin-bottom: 1em;">
      Have a commander you want to break down? We welcome deck techs, guides,
      and opinion pieces from the community.
    </p>
    <a href="/articles/submit-guide/" class="btn btn--primary">See Submission Guidelines →</a>
  </div>
</div>

</div>
