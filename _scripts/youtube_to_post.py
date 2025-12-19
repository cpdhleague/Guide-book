import os
import sys
import requests
import re
from datetime import datetime
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

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
    except Exception as e:
        print(f"⚠️ oEmbed failed: {e}")

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
    except:
        pass

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

# --- 3. GET TRANSCRIPT ---
transcript_text = ""
has_transcript = False

try:
    if hasattr(YouTubeTranscriptApi, 'list_transcripts'):
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            transcript = transcript_list.find_transcript(['en'])
        except:
            transcript = transcript_list.find_generated_transcript(['en'])
        fetched = transcript.fetch()
        transcript_text = " ".join([t['text'] for t in fetched])
    else:
        fetched = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([t['text'] for t in fetched])
    
    if len(transcript_text) > 50:
        has_transcript = True
        print("✅ Transcript retrieved.")
except Exception as e:
    print(f"⚠️ Transcript failed: {e}")

# --- 4. PREPARE AI SOURCES (Hybrid Approach) ---
source_prompt_data = ""

if len(video_description) > 50:
    source_prompt_data += f"PRIMARY SOURCE (Use for accurate card names/context):\nVIDEO DESCRIPTION:\n{video_description}\n\n"

if has_transcript:
    source_prompt_data += f"SECONDARY SOURCE (Use for narrative flow):\nTRANSCRIPT:\n{transcript_text[:15000]}"

if not source_prompt_data:
    source_prompt_data = "No text available. Please write a general summary based on the Title."

# --- 5. GENERATE CONTENT ---
base_prompt = f"""
You are a writer for a competitive Pauper Commander (cPDH) website.
Write a blog post about this video by {channel_name}.

TITLE: {final_title}

{source_prompt_data}

INSTRUCTIONS:
1. First, write a 1-sentence "teaser" starting with the word "EXCERPT:".
   - Example: "EXCERPT: {channel_name} discusses the top 5 blue commons..."
2. Then, write the full article (300-500 words).
   - Use the DESCRIPTION for accurate card names and deck archetypes.
   - Use the TRANSCRIPT to summarize the discussion or gameplay.
   - Tone: Enthusiastic, knowledgeable, community-focused.
   - Do NOT use a H1 header (# Title) at the start.
"""

article_body = ""
excerpt_text = f"Check out this new video from {channel_name}!"
source_type = "Hybrid (Description + Transcript)" if (len(video_description) > 50 and has_transcript) else "Single Source"

try:
    genai.configure(api_key=GEMINI_API_KEY)
    
    # UPDATED: Using the powerful 2.5-pro model
    print("🤖 Attempting generation with gemini-2.5-pro...")
    model = genai.GenerativeModel('gemini-2.5-pro')
    
    response = model.generate_content(base_prompt)
    response_text = response.text

    if "EXCERPT:" in response_text:
        parts = response_text.split("EXCERPT:", 1)[1].split("\n", 1)
        excerpt_text = parts[0].strip()
        article_body = parts[1].strip()
    else:
        article_body = response_text

except Exception as e:
    print(f"❌ AI Generation Failed: {e}")
    # FALLBACK
    article_body = f"**{channel_name}** has released a new video! Check out the details below:\n\n"
    if video_description:
        article_body += "> " + video_description.replace("\n", "\n> ")
    else:
        article_body += "Watch the video below to learn more."
    
    source_type = "Fallback (AI Failed)"

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
