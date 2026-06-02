"""
youtube_to_post.py - Convert content submissions into Jekyll blog posts
=======================================================================
Called by the GitHub Actions workflow when someone opens an issue with
a title like "PDHpod: Ep 222 - Simic Combo Deep Dive".

AI processing is intentionally disabled. Text is published as-written.
See youtube_to_post_WITH_AI.py if you ever want to restore AI support.

SUPPORTED TITLE PREFIXES:
  YouTube:   -> Embeds a YouTube video, downloads thumbnail (creator: guide)
  Spotify:   -> Embeds a Spotify player (creator: guide)
  Article:   -> Plain text article with optional link buttons (creator: guide)
  PDHpod:    -> Spotify embed with PDHpod author card (creator: pdhpod)
  Jalapenos: -> YouTube embed + thumbnail, Jalapenos card (creator: jalapenos)

ISSUE BODY FORMAT:
  The media URL can appear anywhere in the first 10 lines -- the script
  searches for it rather than requiring it to be exactly on line 1.

  Special metadata lines (KEY: value) are parsed from anywhere in the body:
    EXCERPT: Custom excerpt text
    IMAGE:   /assets/images/custom-image.jpg  (or full URL)
    GNEWS:   true   (if present, article requires Patrik review before going live)

  Everything else (non-URL, non-metadata lines) becomes the article body.

OUTPUTS (written to $GITHUB_OUTPUT for the workflow to read):
  gnews=true|false   -- whether GNews review was requested
  filename=...       -- the generated post filename
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

PREFIX_MAP = {
    "youtube:":   {"media": "youtube",  "creator": "guide",     "author": None,        "category": "Videos"},
    "spotify:":   {"media": "spotify",  "creator": "guide",     "author": None,        "category": "Videos"},
    "article:":   {"media": "article",  "creator": "guide",     "author": None,        "category": "Game Guides"},
    "pdhpod:":    {"media": "spotify",  "creator": "pdhpod",    "author": "pdhpod",    "category": "Podcast"},
    "jalapenos:": {"media": "youtube",  "creator": "jalapenos", "author": "jalapenos", "category": "Videos"},
}

# Default images per creator (used when no IMAGE: metadata is provided)
DEFAULT_IMAGES = {
    "pdhpod":    "pdhpod.png",
    "jalapenos": "cpdh.png",
    "guide":     "cpdh.png",
}


# =============================================================
# HELPERS
# =============================================================

def find_youtube_url(text):
    match = re.search(
        r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+))', text
    )
    if match:
        return match.group(1), match.group(2)
    return None, None


def find_spotify_url(text):
    match = re.search(r'https?://[^\s]*spotify\.com/(episode|show)/([a-zA-Z0-9]+)', text)
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
# ROBUST BODY PARSING
# =============================================================
# We search ALL lines for the media URL and KEY: value metadata,
# rather than assuming a fixed line ordering. This makes the script
# resilient to blank leading lines, CRLF endings, and other
# formatting quirks from GitHub or the submission form.

lines = issue_body.strip().splitlines()

media_url_line = None   # the raw line containing the media URL
metadata       = {}     # KEY -> value for any KEY: value lines
body_lines     = []     # everything else becomes the article body

METADATA_KEYS = {'EXCERPT', 'IMAGE', 'GNEWS'}
MEDIA_PATTERNS = ['spotify.com', 'youtube.com', 'youtu.be']

for line in lines:
    stripped = line.strip()
    if not stripped:
        body_lines.append(line)
        continue

    # Check for media URL (only capture the first one found)
    if media_url_line is None and any(p in stripped for p in MEDIA_PATTERNS):
        media_url_line = stripped
        continue

    # Check for KEY: value metadata lines
    meta_match = re.match(r'^([A-Z_]+):\s*(.+)$', stripped)
    if meta_match and meta_match.group(1) in METADATA_KEYS:
        metadata[meta_match.group(1)] = meta_match.group(2).strip()
        continue

    body_lines.append(line)

article_body   = '\n'.join(body_lines).strip()
custom_excerpt = metadata.get('EXCERPT', '')
custom_image   = metadata.get('IMAGE', '')
gnews_flag     = metadata.get('GNEWS', 'false').lower() == 'true'

print(f"Media URL  : {media_url_line}")
print(f"GNews      : {gnews_flag}")
print(f"Custom img : {custom_image or '(using default)'}")


# =============================================================
# BUILD EMBED CODE
# =============================================================

image_filename = custom_image if custom_image else DEFAULT_IMAGES.get(post_creator, "cpdh.png")
embed_code     = ""
video_id       = None

if media_type == "youtube":
    if not media_url_line:
        print("Error: No YouTube URL found in issue body.")
        sys.exit(1)
    video_url, video_id = find_youtube_url(media_url_line)
    if not video_id:
        print(f"Error: Could not parse YouTube video ID from: {media_url_line}")
        sys.exit(1)
    print(f"YouTube ID : {video_id}")
    embed_code = (
        '\n<div style="text-align:center;margin:40px 0;">\n'
        '  <h3>Watch the Video</h3>\n'
        f'  <iframe width="560" height="315"'
        f' src="https://www.youtube.com/embed/{video_id}"'
        ' frameborder="0" allowfullscreen></iframe>\n'
        '</div>\n'
    )

elif media_type == "spotify":
    if not media_url_line:
        print("Error: No Spotify URL found in issue body.")
        sys.exit(1)
    spot_type, spot_id = find_spotify_url(media_url_line)
    if not spot_id:
        print(f"Error: Could not parse Spotify ID from: {media_url_line}")
        sys.exit(1)
    print(f"Spotify    : {spot_type}/{spot_id}")
    embed_code = (
        '\n<div style="margin:40px 0;">\n'
        f'  <iframe style="border-radius:12px"'
        f' src="https://open.spotify.com/embed/{spot_type}/{spot_id}?utm_source=generator"'
        ' width="100%" height="352" frameBorder="0" allowfullscreen=""'
        ' allow="autoplay;clipboard-write;encrypted-media;fullscreen;picture-in-picture"'
        ' loading="lazy"></iframe>\n'
        '</div>\n'
    )

elif media_type == "article":
    links = list(set([
        re.sub(r'[.,;!?]$', '', lnk)
        for lnk in re.findall(r'(https?://[^\s\)]+)', issue_body)
    ]))
    if links:
        embed_code = (
            '\n\n<div style="margin-top:40px;text-align:center;">\n'
            '  <hr>\n  <h3>Helpful Links</h3>\n'
        )
        for i, lnk in enumerate(links):
            embed_code += f'  <a href="{lnk}" class="btn btn--primary" target="_blank" style="margin:5px;">Reference Link {i+1}</a>\n'
        embed_code += '</div>\n'


# =============================================================
# DOWNLOAD THUMBNAIL (YouTube only)
# =============================================================

if media_type == "youtube" and video_id and not custom_image:
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
                print(f"Thumbnail  : assets/images/{image_filename}")
                break
        except Exception as e:
            print(f"Thumbnail failed for {url}: {e}")
    if not downloaded:
        print("Thumbnail download failed — using default image.")
        image_filename = DEFAULT_IMAGES.get(post_creator, "cpdh.png")


# =============================================================
# GENERATE JEKYLL POST FILE
# =============================================================

date_str   = datetime.now().strftime("%Y-%m-%d")
safe_title = re.sub(r'\s+', '-', re.sub(r'[^a-zA-Z0-9\s_-]', '', final_title).strip()).lower()
safe_title = safe_title or "untitled-post"
filename   = f"_posts/{date_str}-{safe_title}.md"

os.makedirs("_posts", exist_ok=True)

excerpt_text = custom_excerpt if custom_excerpt else make_excerpt(article_body)
author_line  = f"author: {post_author}\n" if post_author else ""
include_card = "{% include author-card.html %}\n" if post_author else ""

# Strip leading slash for the image path if it's a local path
image_path = image_filename if image_filename.startswith('http') else f"/assets/images/{image_filename.lstrip('/')}"

post_content = f"""---
title: "{final_title.replace('"', '\\"')}"
date: {date_str}
layout: splash
classes: wide
creator: {post_creator}
{author_line}front_page: true
hidden: false
archive_only: false
gnews: {str(gnews_flag).lower()}
categories:
  - {post_category}
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  teaser: {image_path}
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

# Write outputs for the workflow to read
github_output = os.environ.get('GITHUB_OUTPUT', '')
if github_output:
    with open(github_output, 'a') as f:
        f.write(f"gnews={str(gnews_flag).lower()}\n")
        f.write(f"filename={filename}\n")
