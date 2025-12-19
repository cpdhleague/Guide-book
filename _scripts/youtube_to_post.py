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
    from google import genai
    USE_NEW_LIB = True
except ImportError:
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

# --- HELPER: SCRAPE METADATA (Author & Description) ---
def scrape_video_data(url):
    author = "The Creator"
    description = ""
    
    # 1. Try oEmbed (Official YouTube API - Most Reliable for Author)
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
        data = requests.get(oembed_url).json()
        author = data.get("author_name", author)
    except Exception as e:
        print(f"⚠️ oEmbed failed: {e}")

    # 2. Try HTML Scraping for Description (Backup)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html = response.text
        
        # Scrape description
        desc_match = re.search(r'"shortDescription":"(.*?)"', html)
        if desc_match:
            description = desc_match.group(1).replace('\\n', '\n')
        else:
            meta_desc = re.search(r'<meta name="description" content="(.*?)">', html)
            if meta_desc:
                description = meta_desc.group(1)
        
        # Clean up generic YouTube garbage description
        if "Enjoy the videos and music you love" in description:
            description = ""
            
    except Exception as e:
        print(f"⚠️ Scraping failed: {e}")

    return author, description

# --- MAIN START ---
# Get arguments: URL is #1, Issue Title is #2
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
source_type = "None"

if YouTubeTranscriptApi:
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
            source_type = "Transcript"
            print("✅ Transcript retrieved.")
    except Exception as e:
        print(f"⚠️ Transcript failed: {e}")

# --- 4. PREPARE AI SOURCE ---
if source_type == "Transcript":
    source_text = f"TRANSCRIPT:\n{transcript_text[:12000]}"
elif len(video_description) > 50:
    source_text = f"VIDEO DESCRIPTION:\n{video_description}"
    source_type = "Description"
    print("⚠️ Using Description for AI.")
else:
    source_text = "No text available."
    source_type = "Title Only"

# --- 5. GENERATE CONTENT (Article + Excerpt) ---
base_prompt = f"""
You are a writer for a competitive Pauper Commander (cPDH) website.
Write a blog post about this video by {channel_name}.

TITLE: {final_title}
{source_text}

INSTRUCTIONS:
1. First, write a 1-sentence "teaser" starting with the word "EXCERPT:".
   - Example: "EXCERPT: {channel_name} breaks down the new ban list..."
2. Then, write the full article.
   - Summarize key points/plays.
   - Tone: Enthusiastic and community-focused.
   - Do NOT use a H1 header (# Title) at the start.
   - Length: 300-500 words.
"""

article_body = ""
excerpt_text = f"Check out this new video from {channel_name}!"

try:
    response_text = ""
    if USE_NEW_LIB:
        client = genai.Client(api_key=GEMINI_API_KEY)
        try:
            resp = client.models.generate_content(model='gemini-1.5-flash', contents=base_prompt)
            response_text = resp.text
        except:
            resp = client.models.generate_content(model='gemini-pro', contents=base_prompt)
            response_text = resp.text
    else:
        genai_old.configure(api_key=GEMINI_API_KEY)
        try:
            model = genai_old.GenerativeModel('gemini-1.5-flash-latest')
            response_text = model.generate_content(base_prompt).text
        except:
            model = genai_old.GenerativeModel('gemini-pro')
            response_text = model.generate_content(base_prompt).text

    # Parse Excerpt vs Body
    if "EXCERPT:" in response_text:
        parts = response_text.split("EXCERPT:", 1)[1].split("\n", 1)
        excerpt_text = parts[0].strip()
        article_body = parts[1].strip()
    else:
        article_body = response_text

except Exception as e:
    print(f"❌ AI Generation Failed: {e}")
    # FALLBACK: Use Description if AI dies
    article_body = f"**{channel_name}** has released a new video! Check out the details below:\n\n"
    if video_description:
        article_body += "> " + video_description.replace("\n", "\n> ")
    else:
        article_body += "Watch the video below to learn more."
    
    excerpt_text = f"New cPDH content from {channel_name}. Watch it now!"
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
