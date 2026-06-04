---
# ===========================================================================
# CPDH.GUIDE — ARTICLE TEMPLATE
# ===========================================================================
# HOW TO USE THIS FILE:
#   1. Copy this file into the _posts/ folder
#   2. Rename it: YYYY-MM-DD-short-title-slug.md
#      Example: 2026-06-10-deckbuilding-fundamentals.md
#   3. Fill in every field below (read the notes carefully)
#   4. Write your article content below the closing ---
#   5. Push to GitHub — the site rebuilds in 1-3 minutes
#
# YAML RULES (important):
#   - true/false values must NOT be in quotes
#   - Text values SHOULD be in quotes
#   - Indentation uses SPACES not tabs
#   - Lines starting with # are comments — Jekyll ignores them
# ===========================================================================


# ---------------------------------------------------------------------------
# TITLE
# ---------------------------------------------------------------------------
# The article headline. Make it specific, descriptive, and clickable.
# Appears on: the article page, homepage cards, /articles/ listings,
#             social sharing previews, and RSS feeds.
# Tips:
#   - Use Title Case
#   - Avoid ALL CAPS or clickbait
#   - Keep it under 70 characters where possible
#   - Do NOT use double quotes inside the title (use single quotes if needed)
# ---------------------------------------------------------------------------
title: "YOUR CLICKABLE TITLE HERE"


# ---------------------------------------------------------------------------
# DATE
# ---------------------------------------------------------------------------
# Publication date in YYYY-MM-DD format. Must be today or in the past
# (Jekyll will not publish future-dated posts on GitHub Pages).
# This date appears on the article and controls sort order everywhere.
# ---------------------------------------------------------------------------
date: 2026-06-03


# ---------------------------------------------------------------------------
# LAYOUT & CLASSES — DO NOT CHANGE THESE
# ---------------------------------------------------------------------------
layout: splash
classes: wide


# ===========================================================================
# SECTION 1: WHO & WHAT
# ===========================================================================

# ---------------------------------------------------------------------------
# CREATOR
# ---------------------------------------------------------------------------
# Which content stream produced this article. Used by:
#   - The homepage (limits PDHpod and Jalapenos to 1 slot each)
#   - The "More from..." filter on /articles/?creator=X
# Choose EXACTLY ONE of these values (no quotes needed):
#   guide      — written by the CPDH.guide team
#   pdhpod     — produced by The PDH Pod
#   jalapenos  — produced by the Jalapeno Paupers
# ---------------------------------------------------------------------------
creator: guide


# ---------------------------------------------------------------------------
# AUTHOR
# ---------------------------------------------------------------------------
# Who wrote or produced this specific piece. Controls the author card
# displayed at the bottom of the article.
#
# Two options:
#   Option A — Known author (has a profile in _data/authors.yml):
#              author: gingerpersolus
#              Use the exact key from authors.yml (lowercase, no spaces)
#              This shows the full card: photo + bio + links + "More from" button
#
#   Option B — Guest author (no profile in authors.yml):
#              author: "First Last"
#              Put their name in quotes with a capital letter and a space
#              This shows a name-only card: "Content by First Last"
#
# Leave this field out entirely to show NO author card.
#
# Current authors in _data/authors.yml:
#   ginger, beachbodgod69, pdhpod, jalapenos
#   (Add new authors to that file before using their key here)
# ---------------------------------------------------------------------------
author: gingerpersolus


# ---------------------------------------------------------------------------
# CATEGORIES
# ---------------------------------------------------------------------------
# The topic category for this article. Used on the /articles/ page topic list.
# Choose EXACTLY ONE from this approved list:
#   - Game Guides          (strategy, mechanics, how-to)
#   - Deck Tech            (commander spotlight, decklist deep dives)
#   - Videos               (YouTube embeds, video content)
#   - Podcast              (PDHpod episodes — set automatically by the form)
#   - Community            (interviews, community highlights)
#   - Tournament Reports   (event recaps, standings, winner interviews)
#   - Events               (upcoming events, announcements)
# ---------------------------------------------------------------------------
categories:
  - Game Guides


# ===========================================================================
# SECTION 2: DISPLAY CONTROLS
# ===========================================================================
# These fields control WHERE this article appears across the site.
# All four should be present on every article.

# ---------------------------------------------------------------------------
# FRONT PAGE
# ---------------------------------------------------------------------------
# Should this article appear on the homepage?
#   true  — eligible for one of the 6 homepage slots
#   false — appears on /articles/ only, never on homepage
# Note: even with true, the homepage only shows the most recent PDHpod
# and Jalapenos article (1 each), so older ones won't show if newer exist.
# ---------------------------------------------------------------------------
front_page: true


# ---------------------------------------------------------------------------
# HIDDEN
# ---------------------------------------------------------------------------
# Hide this article from ALL listings (homepage, /articles/, RSS feeds).
# The article still exists and is accessible by direct URL.
#   false — normal, visible article (use this almost always)
#   true  — invisible in listings (use for drafts or unlisted content)
# ---------------------------------------------------------------------------
hidden: false


# ---------------------------------------------------------------------------
# ARCHIVE ONLY
# ---------------------------------------------------------------------------
# Show this article ONLY in its category archive, not on /articles/ or homepage.
# Use for older content, event recaps, or anything you want archived but
# not prominently featured in the main article feed.
#   false — appears everywhere normally (use this almost always)
#   true  — category archive only
# ---------------------------------------------------------------------------
archive_only: false


# ---------------------------------------------------------------------------
# GNEWS
# ---------------------------------------------------------------------------
# Include this article in the Google News RSS feed (/gnews.xml)?
# This feed is also watched by Reddit and Discord auto-posting.
#   false — site only, no external distribution
#   true  — included in RSS feed → Google News, Reddit, Discord
#
# IMPORTANT: If setting to true, you MUST fill in:
#   1. excerpt (required — feeds look broken without it)
#   2. A real image in both image: and header.teaser:
#   3. reddit_text (required if you want Reddit posting — see below)
#
# For PDHpod/Jalapenos submissions: this is set by the submission form.
# For guide articles: Patrik sets this manually after review.
# ---------------------------------------------------------------------------
gnews: false


# ===========================================================================
# SECTION 3: IMAGES
# ===========================================================================
# Three image fields serve different purposes. Ideally all three use the
# same well-composed 16:9 image. Use /assets/images/ for local files.
# File naming: lowercase, hyphens not spaces (my-image.jpg not My Image.jpg)

# IMAGE (top-level)
# Controls: Discord link previews, Reddit thumbnails, social sharing cards,
#           and the <og:image> meta tag that all social platforms read.
# This is the image people see when a link to this article is shared.
image: /assets/images/YOUR-IMAGE.jpg

header:
  # OVERLAY IMAGE
  # The large banner displayed at the top of the article page itself.
  # Should be wide and high resolution (1200px+ wide recommended).
  # For most guide articles use the standard banner: header2025-1.png
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5    # Darkness of the overlay (0.0 = none, 1.0 = black)

  # TEASER
  # The thumbnail shown on the homepage cards and /articles/ listing grid.
  # Should be 16:9 ratio. Usually the same as the top-level image: above.
  teaser: /assets/images/YOUR-IMAGE.jpg

# NOTE: For PDHpod articles, the image is always pdhpod.png (set automatically).
# For Jalapenos articles, the YouTube thumbnail is downloaded automatically.
# For guide articles, upload your image to assets/images/ and reference it here.


# ===========================================================================
# SECTION 4: EXCERPT
# ===========================================================================
# A short 1-2 sentence summary of the article.
# Appears on: homepage cards, /articles/ listing, RSS feeds, social previews,
#             Google News description field, Discord embeds.
#
# Rules:
#   - No markdown formatting (no **bold**, no [links], no #headers)
#   - No double quotes inside the excerpt (use single quotes if needed)
#   - Keep it under 160 characters for best results in feeds
#   - Write it as a standalone sentence — it appears without context
#
# REQUIRED if gnews: true — Google News and RSS feeds look broken without it.
# REQUIRED if front_page: true — homepage cards show this text.
# ---------------------------------------------------------------------------
excerpt: ""  # Required for GNews — fill this in before publishing to Google News


# ===========================================================================
# SECTION 5: REDDIT POSTING
# ===========================================================================
# Controls whether and how this article is posted to Reddit.
# Reddit posting only happens for articles where gnews: true AND
# reddit_text is present and non-empty.
#
# HOW IT WORKS:
#   - reddit_text present and filled → posts to r/pauperEDH and
#     r/competitivepauperedh as a link post, then adds this text as
#     a comment on that post to start discussion
#   - reddit_text absent OR empty → article is NOT posted to Reddit
#
# This is the complete on/off switch for Reddit. Remove the field entirely
# or leave it blank to prevent Reddit posting, no other changes needed.
#
# TEMPLATES by creator (copy and customise):
#
#   PDHpod episodes:
#     "\U0001F3A7 New episode of the PDH Pod is live! Drop your thoughts
#      below — questions for the hosts? Tag u/alkadron!"
#
#   Jalapenos videos:
#     "\U0001F336\uFE0F The Jalapenos dropped a new video! What do you think?
#      Any questions for the crew? Tag u/JalapenoPaupersMTG!"
#
#   Guide articles — write something specific to THIS article:
#     "We've been thinking about X a lot lately. What's your take?"
#     "This challenges the conventional wisdom on Y — agree or disagree?"
#     "Would love to hear what commanders you think belong in this tier."
#
# Note: For PDHpod and Jalapenos, the template text is applied automatically
# by the GitHub Action. You only need to fill this in for guide articles.
# ---------------------------------------------------------------------------
# reddit_text: ""  # Uncomment and fill in to enable Reddit posting

---

Write your article content here. Use ## for section headings and ### for sub-sections.

Add images inline with:
<img src="/assets/images/your-image.jpg" alt="Description" style="width:100%; display:block; margin:0 auto;">

Embed YouTube videos with:
<div style="text-align:center; margin:2em 0;">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
</div>

Delete these example lines before publishing.

{% include author-card.html %}
{% include article-nav.html %}
