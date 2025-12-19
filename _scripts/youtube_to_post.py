import os
import sys
import requests
import re
from datetime import datetime
import json

# --- IMPORTS WITH SAFETY CHECKS ---
try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("⚠️ YouTube Transcript Library missing.")
    YouTubeTranscriptApi = None

try:
    # Try new library first
    from google import genai
    USE_NEW_LIB = True
except ImportError:
    # Fallback to old library
    import google.generativeai as genai_old
    USE_NEW_LIB = False

# --- CONFIGURATION ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# --- HELPER: FIND URL ---
def find_youtube_url(text):
    match = re.search(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+))', text)
    if match:
        return match.group(1), match.group(2)
    return None, None

# --- HELPER: CLEAN TEXT ---
def clean_text(text):
    if not text: return ""
    # Remove HTML tags and weird whitespace
    text = re.sub(r'<[^>]+>', '', text)
    return " ".join(text.split())

# --- MAIN START ---
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

# --- 1. GET METADATA (Title & Description) ---
title = f"Video {video_id}"
description = ""

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(VIDEO_URL, headers=headers)
    html = response.text
    
    # 1. Try finding Title
    title_match = re.search(r'<title>(.*?)</title>', html)
    if title_match:
        title = title_match.group(1).replace(" - YouTube", "")
    
    # 2. Try finding Description (Meta tag)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', html)
    if desc_match:
        description = desc_match.group(1)
    else:
        # Fallback: Try JSONLD in script tag (common in YT)
        try:
            json_match = re.search(r'"shortDescription":"(.*?)"', html)
            if json_match:
                description = json_match.group(1).replace('\\n', ' ')
        except:
            pass

except Exception as e:
    print(f"⚠️ Warning: Could not scrape metadata ({e}). Using defaults.")

# --- 2. GET TRANSCRIPT (With Fallback) ---
transcript_text = ""

if YouTubeTranscriptApi:
    print("Attempting to fetch transcript...")
    try:
        # METHOD A: The Modern Way (list_transcripts)
        if hasattr(YouTubeTranscriptApi, 'list_transcripts'):
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            try:
                transcript = transcript_list.find_transcript(['en'])
            except:
                transcript = transcript_list.find_generated_transcript(['en'])
            fetched = transcript.fetch()
            transcript_text = " ".join([t['text'] for t in fetched])
        
        # METHOD B: The Old Way (get_transcript) - Fallback for old libraries
        else:
            print("⚠️ Using legacy transcript method...")
            fetched = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = " ".join([t['text'] for t in fetched])
            
        print("✅ Transcript retrieved successfully.")
        
    except Exception as e:
        print(f"⚠️ Transcript failed: {e}")

# --- 3. PREPARE CONTENT SOURCE ---
# If transcript failed, use Description. If that fails, abort.
if len(transcript_text) > 50:
    source_text = f"TRANSCRIPT:\n{transcript_text[:12000]}"
    print("Using Transcript for generation.")
elif len(description) > 50:
    source_text = f"VIDEO DESCRIPTION:\n{description}"
    print("⚠️ Using Video Description for generation (Transcript missing).")
else:
    source_text = "No transcript or description available. Please write a general post about this video."
    print("⚠️ Using Title only for generation.")

# --- 4. GENERATE CONTENT (With Model Fallback) ---
base_prompt = f"""
You are an expert content writer for a competitive Pauper Commander (cPDH) website.
Write a blog post based on this YouTube video content.

VIDEO TITLE: {title}
{source_text}

INSTRUCTIONS:
1. Write a catchy, professional article summarizing the key points.
2. If it's a gameplay video, highlight the key plays. If it's a deck tech, highlight the key cards.
3. Keep it brief (approx 300-500 words).
4. Tone: Enthusiastic, knowledgeable, community-focused.
5. DO NOT include the Front Matter (YAML). Start directly with the content.
6. Acknowledge the creator of the video.
"""

article_content = ""

try:
    if USE_NEW_LIB:
        client = genai.Client(api_key=GEMINI_API_KEY)
        # Attempt 1: Flash (Newest)
        try:
            print("🤖 Attempting generation with gemini-1.5-flash...")
            response = client.models.generate_content(model='gemini-1.5-flash', contents=base_prompt)
            article_content = response.text
        except Exception as e:
            print(f"⚠️ Flash failed ({e})... trying gemini-pro...")
            # Attempt 2: Pro (Reliable)
            response = client.models.generate_content(model='gemini-pro', contents=base_prompt)
            article_content = response.text
            
    else: # Old Library Fallback
        genai_old.configure(api_key=GEMINI_API_KEY)
        try:
            model = genai_old.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(base_prompt)
            article_content = response.text
        except:
            model = genai_old.GenerativeModel('gemini-pro')
            response = model.generate_content(base_prompt)
            article_content = response.text

except Exception as e:
    print(f"❌ Gemini Generation Failed: {e}")
    # Last resort fallback text so the script doesn't crash the workflow
    article_content = f"Check out this new video: **{title}**!\n\n(Automated summary could not be generated. Please watch the video above.)"

# --- 5. DOWNLOAD THUMBNAIL ---
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

# --- 6. CREATE POST FILE ---
date_str = datetime.now().strftime("%Y-%m-%d")
safe_title = re.sub(r'[^a-zA-Z0-9\s-_]', '', title).strip().replace(" ", "-").lower()
filename = f"_posts/{date_str}-{safe_title}.md"

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
