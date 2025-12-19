import os
import sys
import requests
import re
from datetime import datetime
import google.generativeai as genai
import time

# --- CONFIGURATION ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# --- HELPER: FIND URL ---
def find_youtube_url(text):
    match = re.search(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+))', text)
    if match:
        return match.group(1), match.group(2)
    return None, None

# --- HELPER: SCRAPE METADATA (Author & Description) ---
def scrape_video_data(url):
    author = "The Creator"
    description = ""
    
    # 1. Try oEmbed (Official YouTube API)
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
        data = requests.get(oembed_url).json()
        author = data.get("author_name", author)
    except: pass

    # 2. Try HTML Scraping for Description
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        html = response.text
        
        desc_match = re.search(r'"shortDescription":"(.*?)"', html)
        if desc_match:
            description = desc_match.group(1).replace('\\n', '\n')
        else:
            meta_desc = re.search(r'<meta name="description" content="(.*?)">', html)
            if meta_desc:
                description = meta_desc.group(1)
        
        if "Enjoy the videos and music" in description:
            description = ""     
    except: pass

    return author, description

# --- MAIN START ---
try:
    issue_body = sys.argv[1]
    raw_issue_title = sys.argv[2] if len(sys.argv) > 2 else ""
except IndexError:
    print("❌ Error: Missing arguments.")
    sys.exit(1)

VIDEO_URL, video_id = find_youtube_url(issue_body)

if not video_id:
    print(f"❌ Error: No valid YouTube URL found.")
    sys.exit(1)

print(f"Processing Video ID: {video_id}")

# --- 1. DETERMINE TITLE ---
if "Video:" in raw_issue_title:
    final_title = raw_issue_title.replace("Video:", "").strip()
else:
    final_title = raw_issue_title.strip() or f"Video Breakdown: {video_id}"

# --- 2. GET METADATA ---
channel_name, video_description = scrape_video_data(VIDEO_URL)
print(f"Detected Channel: {channel_name}")

# --- 3. PREPARE AI SOURCE (Description Only) ---
source_prompt_data = ""

if len(video_description) > 20:
    source_prompt_data = f"VIDEO DESCRIPTION:\n{video_description}"
    print("✅ Using Video Description.")
else:
    source_prompt_data = "No description available. Please write a general summary based on the Title."
    print("⚠️ No Description found. Using Title only.")

# --- 4. GENERATE CONTENT (5-Layer Cascade) ---
base_prompt = f"""
You are a writer for a Pauper Commander (PDH) community website.
Write a blog post about this video by {channel_name}.

TITLE: {final_title}

{source_prompt_data}

INSTRUCTIONS:
1. First, write a VERY SHORT "teaser" (Max 12 words) starting with "EXCERPT:".
   - Example: "EXCERPT: {channel_name} breaks down the new ban list."
2. Then, write the full article (150-300 words).
   - Keep it short and to the point.
   - Only mention "cPDH" (Competitive) if it is explicitly in the Title or Description. Otherwise, just refer to it as PDH or Pauper Commander.
   - Tone: Excited, community-focused, and encouraging. Focus on the joy of seeing people play the format. Avoid sounding like an expert analyzing the gameplay.
   - Do NOT use a H1 header (# Title) at the start.
"""

article_body = ""
excerpt_text = f"Check out this new video from {channel_name}!"
source_type = "Fallback"
ai_success = False

# THE LIST: Ranked by Quality (Best -> Worst)
models_to_try = [
    'gemini-2.5-pro',                    # 1. The Ferrari
    'gemini-2.0-flash',                  # 2. The Modern Standard
    'gemini-flash-latest',               # 3. The Workhorse (1.5 Flash)
    'gemini-2.0-flash-lite-preview-02-05', # 4. The Backup
    'gemini-2.0-flash-lite'              # 5. The Safety Net
]

try:
    genai.configure(api_key=GEMINI_API_KEY)
    
    for model_name in models_to_try:
        try:
            print(f"🤖 Attempting generation with {model_name}...")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(base_prompt)
            response_text = response.text
            
            # If we get here, it worked!
            source_type = f"AI Success ({model_name})"
            ai_success = True
            
            # Parse response
            if "EXCERPT:" in response_text:
                parts = response_text.split("EXCERPT:", 1)[1].split("\n", 1)
                excerpt_text = parts[0].strip()
                article_body = parts[1].strip()
            else:
                article_body = response_text
            
            # Break the loop since we succeeded
            break 
            
        except Exception as e:
            print(f"⚠️ {model_name} failed ({e}). Trying next...")
            time.sleep(1) # Tiny pause before retry

except Exception as e:
    print(f"❌ Critical Error in AI loop: {e}")

# --- 5. FALLBACK CONTENT (If all 5 failed) ---
if not ai_success:
    print("❌ All AI models failed. Using generic fallback.")
    article_body = f"**{channel_name}** has released a new video! Check out the details below:\n\n"
    if video_description:
        article_body += "> " + video_description.replace("\n", "\n> ")
    else:
        article_body += "Watch the video below to learn more."
    source_type = "Generic Text (All Models Failed)"

# --- 6. DOWNLOAD THUMBNAIL ---
image_filename = f"{video_id}.jpg"
image_path = f"assets/images/{image_filename}"
thumb_urls = [f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg", f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"]

downloaded = False
for url in thumb_urls:
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            with open(image_path, 'wb') as h: h.write(resp.content)
            downloaded = True; break
    except: continue

# --- 7. CREATE POST FILE ---
date_str = datetime.now().strftime("%Y-%m-%d")
safe_title = re.sub(r'[^a-zA-Z0-9\s_-]', '', final_title).strip().replace(" ", "-").lower()
filename = f"_posts/{date_str}-{safe_title}.md"
yaml_title = final_title.replace('"', '\\"')
yaml_excerpt = excerpt_text.replace('"', '\\"')

file_content = f"""---
title: "{yaml_title}"
date: {date_str}
layout: splash
classes: wide
categories:
  - Videos
tags:
  - Community
header:
  overlay_image: /assets/images/{image_filename}
  overlay_filter: 0.5
  teaser: /assets/images/{image_filename}
excerpt: "{yaml_excerpt}"
---

{article_body}

<div style="text-align: center; margin-top: 40px; margin-bottom: 40px;">
  <h3>Watch the Video</h3>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
</div>

"""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(file_content)

print(f"Successfully created post: {filename}")
