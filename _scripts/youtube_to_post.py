import os
import sys
import requests
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import re

# --- CONFIGURATION ---
# Get arguments from the command line (passed by GitHub Action)
VIDEO_URL = sys.argv[1]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# Extract Video ID
video_id = VIDEO_URL.split("v=")[-1].split("&")[0]
if "youtu.be" in VIDEO_URL:
    video_id = VIDEO_URL.split("/")[-1].split("?")[0]

# --- 1. GET METADATA (Simple Scraping) ---
# We use simple scraping to avoid heavy dependencies like yt-dlp for just a title
response = requests.get(VIDEO_URL)
html = response.text
try:
    title = re.search(r'<title>(.*?)</title>', html).group(1).replace(" - YouTube", "")
except:
    title = "New Video Post"

# --- 2. GET TRANSCRIPT ---
try:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join([t['text'] for t in transcript_list])
except Exception as e:
    print(f"Could not retrieve transcript: {e}")
    transcript_text = "No transcript available. Please summarize based on the video title."

# --- 3. GENERATE CONTENT WITH GEMINI ---
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = f"""
You are an expert content writer for a competitive Pauper Commander (cPDH) website.
Write a blog post based on this YouTube video transcript.

VIDEO TITLE: {title}
TRANSCRIPT: {transcript_text[:10000]} (truncated if too long)

INSTRUCTIONS:
1. Write a catchy, professional article summarizing the key points.
2. If it's a gameplay video, highlight the key plays. If it's a deck tech, highlight the key cards.
3. Keep it brief (approx 300-500 words).
4. Tone: Enthusiastic, knowledgeable, community-focused.
5. DO NOT include the Front Matter (YAML). Start directly with the content.
6. Acknowledge the creator of the video.
"""

response = model.generate_content(prompt)
article_content = response.text

# --- 4. DOWNLOAD THUMBNAIL ---
image_filename = f"{video_id}.jpg"
image_path = f"assets/images/{image_filename}"
thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

img_data = requests.get(thumbnail_url).content
with open(image_path, 'wb') as handler:
    handler.write(img_data)

# --- 5. CREATE POST FILE ---
date_str = datetime.now().strftime("%Y-%m-%d")
safe_title = "".join([c for c in title if c.isalnum() or c in " -_"]).replace(" ", "-").lower()
filename = f"_posts/{date_str}-{safe_title}.md"

front_matter = f"""---
title: "{title}"
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

with open(filename, 'w') as f:
    f.write(front_matter)

print(f"Successfully created post: {filename}")
