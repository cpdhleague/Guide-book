"""
youtube_to_post_WITH_AI.py — ARCHIVED VERSION with Gemini AI support
=====================================================================
This is the AI-enabled version of the submission script, saved for
reference. It is NOT used by the GitHub Actions workflow.

To re-enable AI processing:
  1. Copy this file over youtube_to_post.py
  2. Ensure GEMINI_API_KEY is set in your GitHub repo Secrets
     (Settings → Secrets and variables → Actions → New secret)
  3. Push — the workflow will pick it up automatically

See youtube_to_post.py for the current active (no-AI) version.
"""

import os
import sys
import requests
import re
from datetime import datetime

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

issue_body = os.environ.get("ISSUE_BODY", "")
raw_issue_title = os.environ.get("ISSUE_TITLE", "")

if not issue_body and len(sys.argv) > 1:
    issue_body = sys.argv[1]
if not raw_issue_title and len(sys.argv) > 2:
    raw_issue_title = sys.argv[2]

if not issue_body:
    print("Error: No issue body provided.")
    sys.exit(1)
if not raw_issue_title:
    print("Error: No issue title provided.")
    sys.exit(1)

PREFIX_MAP = {
    "youtube:":   {"media": "youtube",  "creator": "guide",     "author": None,        "category": "Videos"},
    "spotify:":   {"media": "spotify",  "creator": "guide",     "author": None,        "category": "Videos"},
    "article:":   {"media": "article",  "creator": "guide",     "author": None,        "category": "Game Guides"},
    "pdhpod:":    {"media": "spotify",  "creator": "pdhpod",    "author": "pdhpod",    "category": "Podcast"},
    "jalapenos:": {"media": "youtube",  "creator": "jalapenos", "author": "jalapenos", "category": "Videos"},
}

def find_youtube_url(text):
    match = re.search(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+))', text)
    if match:
        return match.group(1), match.group(2)
    return None, None

def scrape_video_data(url):
    author, description = "The Creator", ""
    try:
        data = requests.get(f"https://www.youtube.com/oembed?url={url}&format=json", timeout=10).json()
        author = data.get("author_name", author)
    except Exception:
        pass
    try:
        html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10).text
        m = re.search(r'"shortDescription":"(.*?)"', html)
        if m:
            description = m.group(1).replace('\\n', '\n')
        if "Enjoy the videos and music" in description:
            description = ""
    except Exception:
        pass
    return author, description

def get_fallback_excerpt(text):
    words = text.split()
    if len(words) > 12:
        return " ".join(words[:12]).replace('"', '') + "..."
    return text.replace('"', '')

def process_content_with_ai(user_text, content_category):
    if not GEMINI_API_KEY:
        print("GEMINI_API_KEY not set — using raw text.")
        return get_fallback_excerpt(user_text), user_text
    if not user_text.strip():
        return "Check out this new release!", ""
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-pro')
        prompt = f"""You are an expert writer for a Pauper Commander (PDH) community website.
A creator submitted notes for a new post.

YOUR TASK:
1. Write a VERY SHORT teaser (max 12 words) on its own line starting with "EXCERPT:".
2. Write a full ~500 word article based on their submission.
   Correct spelling/grammar. Keep the tone excited and community-focused.
   Do not use an H1 header. Do not include the EXCERPT in the body.

SUBMISSION:
{user_text}"""
        resp_text = model.generate_content(prompt).text
        if "EXCERPT:" in resp_text:
            parts = resp_text.split("EXCERPT:", 1)[1].split("\n", 1)
            return parts[0].strip().replace('"', ''), (parts[1].strip() if len(parts) > 1 else "")
        return "Check out our latest content!", resp_text.replace('"', '')
    except Exception as e:
        print(f"AI generation failed: {e}")
        return "Check out our latest content!", user_text

matched_config = None
final_title = raw_issue_title
for prefix, config in PREFIX_MAP.items():
    if raw_issue_title.lower().startswith(prefix):
        matched_config = config
        final_title = raw_issue_title[len(prefix):].strip()
        break

if not matched_config:
    print(f"Error: Unrecognised prefix in: {raw_issue_title}")
    sys.exit(1)

media_type, post_creator, post_author, post_category = (
    matched_config["media"], matched_config["creator"],
    matched_config["author"], matched_config["category"]
)

if media_type in ["youtube", "spotify"]:
    body_lines = issue_body.strip().split('\n')
    first_line = body_lines[0].strip()
    text_to_process = '\n'.join(body_lines[1:]).strip()
else:
    first_line = ""
    text_to_process = issue_body.strip()

skip_ai = False
if len(text_to_process) >= 2 and (
    (text_to_process.startswith('"') and text_to_process.endswith('"')) or
    (text_to_process.startswith("'") and text_to_process.endswith("'"))
):
    skip_ai = True
    text_to_process = text_to_process[1:-1].strip()

article_body = ""
excerpt_text = "Check out our latest content!"
image_filename = "cpdh.png"
embed_code = ""
video_id = None

if media_type == "youtube":
    video_url, video_id = find_youtube_url(first_line)
    if not video_id:
        print(f"Error: No YouTube URL in: {first_line}")
        sys.exit(1)
    channel_name, video_description = scrape_video_data(video_url)
    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        source = text_to_process or f"Video by {channel_name}. {video_description}"
        excerpt_text, article_body = process_content_with_ai(source, media_type)
    embed_code = f'\n<div style="text-align:center;margin:40px 0;">\n  <h3>Watch the Video</h3>\n  <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>\n</div>\n'

elif media_type == "spotify":
    m = re.search(r'spotify\.com/(episode|show)/([a-zA-Z0-9]+)', first_line)
    if not m:
        print(f"Error: No Spotify URL in: {first_line}")
        sys.exit(1)
    spot_type, spot_id = m.group(1), m.group(2)
    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        excerpt_text, article_body = process_content_with_ai(text_to_process, media_type)
    embed_code = f'\n<div style="margin:40px 0;">\n  <iframe style="border-radius:12px" src="https://open.spotify.com/embed/{spot_type}/{spot_id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay;clipboard-write;encrypted-media;fullscreen;picture-in-picture" loading="lazy"></iframe>\n</div>\n'

elif media_type == "article":
    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        excerpt_text, article_body = process_content_with_ai(text_to_process, media_type)
    links = list(set([re.sub(r'[.,;!?]$', '', l) for l in re.findall(r'(https?://[^\s\)]+)', issue_body)]))
    if links:
        embed_code = '\n\n<div style="margin-top:40px;text-align:center;">\n  <hr>\n  <h3>Helpful Links</h3>\n'
        for i, link in enumerate(links):
            embed_code += f'  <a href="{link}" class="btn btn--primary" target="_blank" style="margin:5px;">Reference Link {i+1}</a>\n'
        embed_code += '</div>\n'

if media_type == "youtube" and video_id:
    image_filename = f"{video_id}.jpg"
    os.makedirs("assets/images", exist_ok=True)
    for url in [f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg", f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"]:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200 and len(resp.content) > 10_000:
                with open(f"assets/images/{image_filename}", 'wb') as f:
                    f.write(resp.content)
                break
        except Exception:
            continue
    else:
        image_filename = "cpdh.png"

date_str = datetime.now().strftime("%Y-%m-%d")
safe_title = re.sub(r'\s+', '-', re.sub(r'[^a-zA-Z0-9\s_-]', '', final_title).strip()).lower() or "untitled-post"
filename = f"_posts/{date_str}-{safe_title}.md"
os.makedirs("_posts", exist_ok=True)

author_line  = f"author: {post_author}\n" if post_author else ""
include_card = "{% include author-card.html %}\n" if post_author else ""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"""---
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
excerpt: "{excerpt_text.replace('"', '\\"')}"
---

{article_body}

{embed_code}
{include_card}
{{% include article-nav.html %}}
""")

print(f"Successfully created post: {filename}")
