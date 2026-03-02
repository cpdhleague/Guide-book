"""
youtube_to_post.py - Convert content submissions into Jekyll blog posts
=======================================================================
This script is called by a GitHub Actions workflow when someone opens
an issue with a title like "YouTube: Cool Video About PDH".

It reads the issue body and title from ENVIRONMENT VARIABLES (not
command line arguments — see the workflow file for why this matters).

WHAT IT DOES:
  1. Determines content type from the issue title prefix
  2. Extracts media links (YouTube/Spotify) from line 1 of the body
  3. Optionally runs Gemini AI to expand short notes into a full article
  4. Downloads thumbnails (YouTube only)
  5. Generates a Jekyll-compatible markdown post file

SKIP-AI MODE:
  If the user wraps their entire text in quotes ("like this"), the AI
  step is skipped and their text is used verbatim. This is useful for
  pre-written articles that just need to be formatted as a post.

LEARNING NOTE ON ENVIRONMENT VARIABLES:
  The old version used sys.argv (command line arguments) which required
  the workflow to paste the issue body into a shell command — breaking
  on any URL with & or ? characters. Environment variables avoid this
  entirely because they're set by the OS, not parsed by the shell.
"""

import os
import sys
import requests
import re
from datetime import datetime

# =============================================================
# CONFIGURATION
# =============================================================

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Read inputs from environment variables (set by GitHub Actions)
# Falls back to sys.argv for local testing
issue_body = os.environ.get("ISSUE_BODY", "")
raw_issue_title = os.environ.get("ISSUE_TITLE", "")

# Allow local testing via command line args
if not issue_body and len(sys.argv) > 1:
    issue_body = sys.argv[1]
if not raw_issue_title and len(sys.argv) > 2:
    raw_issue_title = sys.argv[2]

if not issue_body:
    print("❌ Error: No issue body provided (check ISSUE_BODY env var or pass as argument).")
    sys.exit(1)

if not raw_issue_title:
    print("❌ Error: No issue title provided (check ISSUE_TITLE env var or pass as argument).")
    sys.exit(1)


# =============================================================
# HELPER: FIND YOUTUBE URL
# =============================================================
# Extracts both the full URL and the video ID from a YouTube link.
#
# LEARNING NOTE ON REGEX:
# This pattern handles two YouTube URL formats:
#   - youtube.com/watch?v=VIDEO_ID (standard)
#   - youtu.be/VIDEO_ID (short link)
# The [\w-]+ captures alphanumeric chars and hyphens (video IDs).
# =============================================================

def find_youtube_url(text):
    match = re.search(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+))', text)
    if match:
        return match.group(1), match.group(2)
    return None, None


# =============================================================
# HELPER: SCRAPE VIDEO METADATA
# =============================================================
# Gets the channel name and video description without needing
# a YouTube Data API key. Uses two approaches:
#   1. oEmbed API (official, gives channel name)
#   2. HTML scraping (unofficial, gets description)
#
# LEARNING NOTE: oEmbed is a standard that many sites support.
# You give it a URL, it gives you metadata (title, author, etc.)
# It's lightweight and doesn't require API keys.
# =============================================================

def scrape_video_data(url):
    author = "The Creator"
    description = ""

    # 1. oEmbed for the channel name (official YouTube endpoint)
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
        data = requests.get(oembed_url, timeout=10).json()
        author = data.get("author_name", author)
    except Exception:
        pass

    # 2. HTML scraping for the video description
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        html = response.text

        # YouTube embeds the description in a JSON blob in the page
        desc_match = re.search(r'"shortDescription":"(.*?)"', html)
        if desc_match:
            description = desc_match.group(1).replace('\\n', '\n')
        else:
            # Fallback: meta description tag
            meta_desc = re.search(r'<meta name="description" content="(.*?)">', html)
            if meta_desc:
                description = meta_desc.group(1)

        # YouTube's default description is useless — discard it
        if "Enjoy the videos and music" in description:
            description = ""
    except Exception:
        pass

    return author, description


# =============================================================
# ROUTING: DETERMINE CONTENT TYPE
# =============================================================

content_type = "article"  # Default fallback
final_title = raw_issue_title

if raw_issue_title.lower().startswith("youtube:"):
    content_type = "youtube"
    final_title = raw_issue_title[8:].strip()
elif raw_issue_title.lower().startswith("spotify:"):
    content_type = "spotify"
    final_title = raw_issue_title[8:].strip()
elif raw_issue_title.lower().startswith("article:"):
    content_type = "article"
    final_title = raw_issue_title[8:].strip()

print(f"📋 Content type: {content_type}")
print(f"📋 Title: {final_title}")


# =============================================================
# PARSE ISSUE BODY
# =============================================================
# For YouTube/Spotify: line 1 = media link, rest = article text
# For Articles: entire body = article text (no link required)
#
# SKIP-AI MODE: If the text body is wrapped in quotes, the user
# wants their exact text used — no AI rewriting.
# =============================================================

if content_type in ["youtube", "spotify"]:
    body_lines = issue_body.strip().split('\n')
    first_line = body_lines[0].strip()
    text_to_process = '\n'.join(body_lines[1:]).strip()
else:
    first_line = ""
    text_to_process = issue_body.strip()

# Check for quote-wrapped text (skip AI mode)
skip_ai = False
if len(text_to_process) >= 2 and (
    (text_to_process.startswith('"') and text_to_process.endswith('"')) or
    (text_to_process.startswith("'") and text_to_process.endswith("'"))
):
    skip_ai = True
    text_to_process = text_to_process[1:-1].strip()
    print("✅ User requested text remain untouched (found quotes).")
else:
    print("🤖 User provided unquoted text. AI will expand/spellcheck.")


# =============================================================
# AI GENERATION (GEMINI)
# =============================================================
# Only import and configure Gemini if we actually need it.
#
# LEARNING NOTE: "Lazy imports" — we only load the AI library
# when we know we'll use it. This means submissions using the
# quote-to-skip-AI feature work even if GEMINI_API_KEY isn't set.
# =============================================================

def process_content_with_ai(user_text, content_category):
    """Send text to Gemini for expansion into a ~500 word article."""
    if not GEMINI_API_KEY:
        print("⚠️ GEMINI_API_KEY not set — using raw text as fallback.")
        return get_fallback_excerpt(user_text), user_text

    if not user_text.strip():
        return "Check out this new release!", ""

    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-pro')

        prompt = f"""
You are an expert writer and editor for a Pauper Commander (PDH) community website.
A creator submitted notes/text for a new post.

YOUR TASK:
1. First, write a VERY SHORT "teaser" (Max 12 words) on its own line starting with "EXCERPT:".
2. Then, write a full, engaging article of approximately 500 words based on their submission.
   Correct any bad spelling or grammar natively.
   Keep the tone excited, community-focused, and encouraging. Focus on the joy of the format.
   Do not use an H1 header (# Title) at the start.
   Do not include the EXCERPT line in the article body.

CREATOR'S SUBMISSION:
{user_text}
"""
        response = model.generate_content(prompt)
        resp_text = response.text

        # Parse the EXCERPT line from the rest of the body
        if "EXCERPT:" in resp_text:
            parts = resp_text.split("EXCERPT:", 1)[1].split("\n", 1)
            out_excerpt = parts[0].strip().replace('"', '')
            out_body = parts[1].strip() if len(parts) > 1 else ""
            return out_excerpt, out_body

        return "Check out our latest content!", resp_text.replace('"', '')

    except Exception as e:
        print(f"❌ AI generation failed: {e}")
        return "Check out our latest content!", user_text


def get_fallback_excerpt(text):
    """Create a simple excerpt from the first ~12 words of the text."""
    words = text.split()
    if len(words) > 12:
        return " ".join(words[:12]).replace('"', '') + "..."
    return text.replace('"', '')


# =============================================================
# CONTENT ASSEMBLY (per type)
# =============================================================

article_body = ""
excerpt_text = "Check out our latest content!"
image_filename = "cpdh.png"  # Default image for Spotify/Articles
embed_code = ""
video_id = None

# --- YOUTUBE ---
if content_type == "youtube":
    video_url, video_id = find_youtube_url(first_line)
    if not video_id:
        print(f"❌ Error: Could not find a YouTube URL in: {first_line}")
        sys.exit(1)

    print(f"🎬 Found YouTube video ID: {video_id}")
    channel_name, video_description = scrape_video_data(video_url)
    print(f"🎬 Channel: {channel_name}")

    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        source_text = text_to_process if text_to_process.strip() else \
            f"Video by {channel_name}. YouTube Description: {video_description}"
        excerpt_text, article_body = process_content_with_ai(source_text, content_type)

    embed_code = f"""
<div style="text-align: center; margin-top: 40px; margin-bottom: 40px;">
  <h3>Watch the Video</h3>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
</div>
"""

# --- SPOTIFY ---
elif content_type == "spotify":
    spotify_match = re.search(r'spotify\.com/(episode|show)/([a-zA-Z0-9]+)', first_line)
    if not spotify_match:
        print(f"❌ Error: Could not find a Spotify URL in: {first_line}")
        sys.exit(1)

    spot_type = spotify_match.group(1)
    spot_id = spotify_match.group(2)
    print(f"🎧 Found Spotify {spot_type}: {spot_id}")

    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        excerpt_text, article_body = process_content_with_ai(text_to_process, content_type)

    embed_code = f"""
<div style="margin-top: 40px; margin-bottom: 40px;">
  <iframe style="border-radius:12px" src="https://open.spotify.com/embed/{spot_type}/{spot_id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
</div>
"""

# --- ARTICLE ---
elif content_type == "article":
    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        excerpt_text, article_body = process_content_with_ai(text_to_process, content_type)

    # Extract any URLs from the body to create link buttons
    links = re.findall(r'(https?://[^\s\)]+)', issue_body)
    # Deduplicate and clean trailing punctuation
    links = list(set([re.sub(r'[.,;!?]$', '', l) for l in links]))

    if links:
        button_html = '\n\n<div style="margin-top: 40px; text-align: center;">\n  <hr>\n  <h3>Helpful Links</h3>\n'
        for i, link in enumerate(links):
            button_html += f'  <a href="{link}" class="btn btn--primary" target="_blank" style="margin: 5px;">Reference Link {i+1}</a>\n'
        button_html += '</div>\n'
        embed_code = button_html


# =============================================================
# DOWNLOAD THUMBNAIL (YouTube only)
# =============================================================
# YouTube provides thumbnails at predictable URLs based on video ID.
# We try maxresdefault first (1280x720), then hqdefault (480x360).
#
# LEARNING NOTE: YouTube returns HTTP 200 even for placeholder/
# missing thumbnails, but those are tiny files. We check that the
# downloaded file is at least 10KB to filter out gray placeholders.
# =============================================================

if content_type == "youtube" and video_id:
    image_filename = f"{video_id}.jpg"
    image_dir = "assets/images"
    image_path = f"{image_dir}/{image_filename}"

    # Ensure the directory exists (it should in your repo, but just in case)
    os.makedirs(image_dir, exist_ok=True)

    thumb_urls = [
        f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
        f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
    ]

    downloaded = False
    for url in thumb_urls:
        try:
            resp = requests.get(url, timeout=10)
            # Check status AND file size (YouTube returns 200 for gray placeholders)
            if resp.status_code == 200 and len(resp.content) > 10_000:
                with open(image_path, 'wb') as f:
                    f.write(resp.content)
                downloaded = True
                print(f"✅ Downloaded thumbnail: {image_path} ({len(resp.content)} bytes)")
                break
        except Exception as e:
            print(f"⚠️ Thumbnail download failed for {url}: {e}")
            continue

    if not downloaded:
        print("⚠️ Could not download YouTube thumbnail — using default image.")
        image_filename = "cpdh.png"  # Fall back to default


# =============================================================
# GENERATE THE JEKYLL POST FILE
# =============================================================
# Jekyll post filenames follow a strict format: YYYY-MM-DD-title.md
# The front matter (between --- markers) configures how the page
# looks. We include the `image:` field so the RSS feed (and your
# Discord news bot!) can find the teaser image.
# =============================================================

date_str = datetime.now().strftime("%Y-%m-%d")

# Create a URL-safe filename from the title
safe_title = re.sub(r'[^a-zA-Z0-9\s_-]', '', final_title).strip()
safe_title = re.sub(r'\s+', '-', safe_title).lower()

# Guard against empty title producing a bad filename
if not safe_title:
    safe_title = "untitled-post"

filename = f"_posts/{date_str}-{safe_title}.md"

# Ensure _posts directory exists
os.makedirs("_posts", exist_ok=True)

# Escape quotes in YAML strings to prevent broken front matter
yaml_title = final_title.replace('"', '\\"')
yaml_excerpt = excerpt_text.replace('"', '\\"')

file_content = f"""---
title: "{yaml_title}"
date: {date_str}
layout: splash
classes: wide
categories:
  - {content_type.capitalize()}
image: /assets/images/{image_filename}
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  teaser: /assets/images/{image_filename}
excerpt: "{yaml_excerpt}"
---

{article_body}

{embed_code}
"""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(file_content)

print(f"✅ Successfully created post: {filename}")
