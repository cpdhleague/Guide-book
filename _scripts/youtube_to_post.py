import os
import sys
import requests
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import re

# --- CONFIGURATION ---
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# --- HELPER: FIND URL ---
def find_youtube_url(text):
    match = re.search(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+))', text)
    if match:
        return match.group(1), match.group(2)
    return None, None

# Get arguments
try:
    issue_body = sys.argv[1]
except IndexError:
    print("❌ Error: No issue body provided.")
    sys.exit(1)

VIDEO_URL, video_id = find_youtube_url(issue_body)

if not video_id:
    print(f"❌ Error: No valid YouTube URL found in issue body.")
    sys.exit(1)

print(f"Processing Video ID: {video_id}")

# --- 1. GET METADATA ---
try:
    response = requests.get(VIDEO_URL)
    html = response.text
    title_match = re.search(r'<title>(.*?)</title>', html)
    if title_match:
        title = title_match.group(1).replace(" - YouTube", "")
    else:
        title = f"Video {video_id}"
except Exception as e:
    print(f"Warning: Could not scrape title ({e}). Using ID.")
    title = f"Video {video_id}"

# --- 2. GET TRANSCRIPT (Robust Method) ---
transcript_text = "No transcript available. Summary will be based on title only."
try:
    # Use list_transcripts which is more robust than get_transcript
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    
    # Try to find an English transcript (manual or generated)
    try:
        transcript = transcript_list.find_transcript(['en'])
    except:
        # Fallback to any available transcript
        transcript = transcript_list.find_generated_transcript(['en'])
    
    fetched_transcript = transcript.fetch()
    transcript_text = " ".join([t['text'] for t in fetched_transcript])
    print("✅ Transcript retrieved successfully.")

except Exception as e:
    print(f"⚠️ Could not retrieve transcript: {e}")

# --- 3. GENERATE CONTENT WITH GEMINI (With Fallback) ---
try:
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Define the prompt outside so we can reuse it
    base_prompt = f"""
    You are an expert content writer for a competitive Pauper Commander (cPDH) website.
    Write a blog post based on this YouTube video transcript.

    VIDEO TITLE: {title}
    TRANSCRIPT: {transcript_text[:12000]} (truncated)

    INSTRUCTIONS:
    1. Write a catchy, professional article summarizing the key points.
    2. If it's a gameplay video, highlight the key plays. If it's a deck tech, highlight the key cards.
    3. Keep it brief (approx 300-500 words).
    4. Tone: Enthusiastic, knowledgeable, community-focused.
    5. DO NOT include the Front Matter (YAML). Start directly with the content.
    6. Acknowledge the creator of the video.
    """

    try:
        # Attempt 1: Try the Flash model (Fast & Cheap)
        print("🤖 Attempting generation with gemini-1.5-flash...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(base_prompt)
        article_content = response.text
    except Exception as e:
        print(f"⚠️ Flash model failed ({e}). Switching to gemini-pro...")
        # Attempt 2: Fallback to Pro (Standard)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(base_prompt)
        article_content = response.text

except Exception as e:
    print(f"❌ Critical Gemini Error: {e}")
    sys.exit(1)

# --- 4. DOWNLOAD THUMBNAIL ---
image_filename = f"{video_id}.jpg"
image_path = f"assets/images/{image_filename}"

thumb_urls = [
    f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
    f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
]

downloaded = False
for url in thumb_urls:
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            with open(image_path, 'wb') as handler:
                handler.write(resp.content)
            print(f"✅ Downloaded thumbnail from: {url}")
            downloaded = True
            break
    except:
        continue

if not downloaded:
    print("⚠️ Warning: Could not download thumbnail.")

# --- 5. CREATE POST FILE ---
date_str = datetime.now().strftime("%Y-%m-%d")
safe_title = re.sub(r'[^a-zA-Z0-9\s-_]', '', title).strip().replace(" ", "-").lower()
filename = f"_posts/{date_str}-{safe_title}.md"

# Safe title for YAML
yaml_safe_title = title.replace('"', '\\"')

front_matter = f"""---
title: "{yaml_safe_title}"
date: {date_str}
layout: single
classes: 
  - wide
  - short-header
categories:
  - Videos
tags:
  - Community
header:
  overlay_image: /assets/images/{image_filename}
  overlay_filter: 0.5
  teaser: /assets/images/{image_filename}
excerpt: "New video content! Check out this breakdown of {title}."
---

<div style="text-align: center; margin-bottom: 20px;">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
</div>

{article_content}
"""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(front_matter)

print(f"Successfully created post: {filename}")
