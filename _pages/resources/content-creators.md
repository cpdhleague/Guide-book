---
# --- 1. YAML FRONT MATTER (THE DATA) ---
title: "Content Creator Directory"
layout: splash
permalink: /resources/content-creators/

# Optional: Add a big header image, just like your index page
header:
  overlay_image: /assets/images/Gemini_Generated_Image_bpu1z6bpu1z6bpu1.png
  overlay_filter: 0.0
#  title: "Content Creator Directory"
#  excerpt: "Discover the amazing creators building the PDH community."

# ---
# We define FOUR separate feature row data blocks here.
# You can add as many or as few creators as you want to each row.
# ---

# Data for the first row
creators_row_1:
  - image_path: /assets/images/pdhpod.png
    title: "PDH Pod"
    url: "https://open.spotify.com/show/55DyhZMhnn7z4SivHPiFVC?si=gzHUt6RKTnmAbtkdYDv0Ow&nd=1&dlsi=9a5666161b4b4e07"
  - image_path: /assets/images/jajepenos.png
    title: "Jalapeño Paupers"
    url: "https://www.youtube.com/@JalapenoPaupersMTG/videos"
  - image_path: /assets/images/pdhpod.png
    title: "PDH Pod Stream"
    url: "https://www.twitch.tv/thepdhpod"

# Data for the second row
creators_row_2:
  - image_path: /assets/images/creator-4.jpg
    title: "Creator Four's Channel"
    url: "https://www.youtube.com/watch?v=..."
  - image_path: /assets/images/creator-5.jpg
    title: "Creator Five's Stream"
    url: "https://www.twitch.tv/..."

# Data for the third row
creators_row_3:
  - image_path: /assets/images/creator-6.jpg
    title: "Creator Six's YouTube"
    url: "https://www.youtube.com/watch?v=..."
    excerpt: "New to the scene, but putting out great content!"

# Data for the fourth row
creators_row_4:
  - image_path: /assets/images/creator-7.jpg
    title: "Creator Seven's Site"
    url: "https://www.creator7.com/..."
  - image_path: /assets/images/creator-8.jpg
    title: "Creator Eight's Stream"
    url: "https://www.twitch.tv/..."
  - image_path: /assets/images/creator-9.jpg
    title: "Creator Nine's Channel"
    url: "https://www.youtube.com/watch?v=..."
---

## Featured Creators

{% include feature_row id="creators_row_1" %}

<div style="clear: both;"></div>

## Up & Coming Channels

{% include feature_row id="creators_row_2" %}

<div style="clear: both;"></div>

## Community Streamers

{% include feature_row id="creators_row_3" %}

<div style="clear: both;"></div>

## PDH Blogs and Articles

{% include feature_row id="creators_row_4" %}
