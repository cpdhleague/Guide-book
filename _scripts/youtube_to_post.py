"""
youtube_to_post.py - Convert content submissions into Jekyll blog posts
=======================================================================
Called by the GitHub Actions workflow when someone opens an issue with
a title like "PDHpod: Ep 222 - Simic Combo Deep Dive".

AI processing is intentionally disabled. Text is published as-written.
See youtube_to_post_WITH_AI.py if you ever want to restore AI support.

SUPPORTED TITLE PREFIXES:
  YouTube:   → Embeds a YouTube video, downloads thumbnail (creator: guide)
  Spotify:   → Embeds a Spotify player (creator: guide)
  Article:   → Plain text article with optional link buttons (creator: guide)
  PDHpod:    → Spotify embed with PDHpod author card (creator: pdhpod)
  Jalapenos: → YouTube embed + thumbnail, Jalapenos card (creator: jalapenos)

ISSUE BODY FORMAT (for YouTube/Spotify/PDHpod/Jalapenos):
  Line 1:  The media link (YouTube or Spotify URL)
  Line 2+: Article body / show notes — published exactly as written

LEARNING NOTE ON ENVIRONMENT VARIABLES:
  We read ISSUE_BODY and ISSUE_TITLE from env vars, not command-line
  args, to avoid shell injection bugs with special characters in URLs.
"""

import os
import sys
import re
import requests
from datetime import datetime

# =============================================================
# INPUTS
# =============================================================

issue_body      = os.environ.get("ISSUE_BODY", "")
raw_issue_title = os.environ.get("ISSUE_TITLE", "")

# Allow local testing via command line
if not issue_body and len(sys.argv) > 1:
    issue_body = sys.argv[1]
if not raw_issue_title and len(sys.argv) > 2:
    raw_issue_title = sys.argv[2]

if not issue_body:
    print("Error: No issue body provided (check ISSUE_BODY env var).")
    sys.exit(1)
if not raw_issue_title:
    print("Error: No issue title provided (check ISSUE_TITLE env var).")
    sys.exit(1)


# =============================================================
# CREATOR / CATEGORY MAPPINGS
# =============================================================
# Add new creator types here. Each prefix produces different
# front matter tags on the generated post.

PREFIX_MAP = {
    "youtube:":   {"media": "youtube",  "creator": "guide",     "author": None,        "category": "Videos"},
    "spotify:":   {"media": "spotify",  "creator": "guide",     "author": None,        "category": "Videos"},
    "article:":   {"media": "article",  "creator": "guide",     "author": None,        "category": "Game Guides"},
    "pdhpod:":    {"media": "spotify",  "creator": "pdhpod",    "author": "pdhpod",    "category": "Podcast"},
    "jalapenos:": {"media": "youtube",  "creator": "jalapenos", "author": "jalapenos", "category": "Videos"},
}


# =============================================================
# HELPERS
# =============================================================

def find_youtube_url(text):
    match = re.search(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+))', text)
    if match:
        return match.group(1), match.group(2)
    return None, None


def make_excerpt(text):
    """Pull the first sentence or ~12 words as an excerpt."""
    clean = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE).strip()
    sentence = re.split(r'[.!?]', clean)[0].strip()
    if len(sentence) > 15:
        return sentence.replace('"', "'")
    words = clean.split()
    if len(words) > 12:
        return " ".join(words[:12]).replace('"', "'") + "..."
    return clean.replace('"', "'") or "New content from the cPDH community."


# =============================================================
# ROUTING
# =============================================================

matched_config = None
final_title    = raw_issue_title

for prefix, config in PREFIX_MAP.items():
    if raw_issue_title.lower().startswith(prefix):
        matched_config = config
        final_title = raw_issue_title[len(prefix):].strip()
        break

if not matched_config:
    print(f"Error: Unrecognised prefix in: {raw_issue_title}")
    print(f"Supported prefixes: {', '.join(PREFIX_MAP.keys())}")
    sys.exit(1)

media_type    = matched_config["media"]
post_creator  = matched_config["creator"]
post_author   = matched_config["author"]
post_category = matched_config["category"]

print(f"Media type : {media_type}")
print(f"Creator    : {post_creator}")
print(f"Title      : {final_title}")


# =============================================================
# PARSE ISSUE BODY
# =============================================================

if media_type in ["youtube", "spotify"]:
    body_lines     = issue_body.strip().split('\n')
    first_line     = body_lines[0].strip()
    article_body   = '\n'.join(body_lines[1:]).strip()
else:
    first_line     = ""
    article_body   = issue_body.strip()

# Check for an optional EXCERPT: line in the body
# (the submission form can inject one)
custom_excerpt = None
excerpt_match = re.search(r'^EXCERPT:\s*(.+)$', article_body, re.MULTILINE | re.IGNORECASE)
if excerpt_match:
    custom_excerpt = excerpt_match.group(1).strip()
    article_body = re.sub(r'^EXCERPT:.*\n?', '', article_body, flags=re.MULTILINE | re.IGNORECASE).strip()

excerpt_text = custom_excerpt if custom_excerpt else make_excerpt(article_body)

print(f"Excerpt    : {excerpt_text}")


# =============================================================
# BUILD EMBED CODE
# =============================================================

image_filename = "cpdh.png"
embed_code     = ""
video_id       = None

if media_type == "youtube":
    video_url, video_id = find_youtube_url(first_line)
    if not video_id:
        print(f"Error: No YouTube URL found in: {first_line}")
        sys.exit(1)
    print(f"YouTube ID : {video_id}")
    embed_code = (
        '\n<div style="text-align:center;margin:40px 0;">\n'
        '  <h3>Watch the Video</h3>\n'
        f'  <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" '
        'frameborder="0" allowfullscreen></iframe>\n'
        '</div>\n'
    )

elif media_type == "spotify":
    m = re.search(r'spotify\.com/(episode|show)/([a-zA-Z0-9]+)', first_line)
    if not m:
        print(f"Error: No Spotify URL found in: {first_line}")
        sys.exit(1)
    spot_type, spot_id = m.group(1), m.group(2)
    print(f"Spotify    : {spot_type}/{spot_id}")
    embed_code = (
        '\n<div style="margin:40px 0;">\n'
        f'  <iframe style="border-radius:12px" '
        f'src="https://open.spotify.com/embed/{spot_type}/{spot_id}?utm_source=generator" '
        'width="100%" height="352" frameBorder="0" allowfullscreen="" '
        'allow="autoplay;clipboard-write;encrypted-media;fullscreen;picture-in-picture" '
        'loading="lazy"></iframe>\n'
        '</div>\n'
    )

elif media_type == "article":
    links = list(set([
        re.sub(r'[.,;!?]$', '', l)
        for l in re.findall(r'(https?://[^\s\)]+)', issue_body)
    ]))
    if links:
        embed_code = '\n\n<div style="margin-top:40px;text-align:center;">\n  <hr>\n  <h3>Helpful Links</h3>\n'
        for i, link in enumerate(links):
            embed_code += f'  <a href="{link}" class="btn btn--primary" target="_blank" style="margin:5px;">Reference Link {i+1}</a>\n'
        embed_code += '</div>\n'


# =============================================================
# DOWNLOAD THUMBNAIL (YouTube only)
# =============================================================

if media_type == "youtube" and video_id:
    image_filename = f"{video_id}.jpg"
    os.makedirs("assets/images", exist_ok=True)
    downloaded = False
    for url in [
        f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
        f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
    ]:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200 and len(resp.content) > 10_000:
                with open(f"assets/images/{image_filename}", 'wb') as f:
                    f.write(resp.content)
                downloaded = True
                print(f"Thumbnail  : assets/images/{image_filename} ({len(resp.content)} bytes)")
                break
        except Exception as e:
            print(f"Thumbnail failed for {url}: {e}")
    if not downloaded:
        print("Thumbnail download failed — using default image.")
        image_filename = "cpdh.png"


# =============================================================
# GENERATE JEKYLL POST FILE
# =============================================================

date_str   = datetime.now().strftime("%Y-%m-%d")
safe_title = re.sub(r'\s+', '-', re.sub(r'[^a-zA-Z0-9\s_-]', '', final_title).strip()).lower()
safe_title = safe_title or "untitled-post"
filename   = f"_posts/{date_str}-{safe_title}.md"

os.makedirs("_posts", exist_ok=True)

author_line  = f"author: {post_author}\n" if post_author else ""
include_card = "{% include author-card.html %}\n" if post_author else ""

post_content = f"""---
title: "{final_title.replace('"', '\\"')}"
date: {date_str}
layout: splash
classes: wide
creator: {post_creator}
{author_line}front_page: true
hidden: false
archive_only: false
gnews: false
categories:
  - {post_category}
image: /assets/images/{image_filename}
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  teaser: /assets/images/{image_filename}
excerpt: "{excerpt_text.replace('"', "'")}"
---

{article_body}

{embed_code}
{include_card}
{{% include article-nav.html %}}
"""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(post_content)

print(f"Created    : {filename}")
