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

# --- ROUTING BASED ON TITLE PREFIX ---
content_type = "article" # Default fallback
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

# --- ISOLATE TEXT BODY AND CHECK FOR QUOTES ---
# Articles don't require a link on line 1, so we handle them differently
if content_type in ["youtube", "spotify"]:
    body_lines = issue_body.strip().split('\n')
    first_line = body_lines[0].strip()
    text_to_process = '\n'.join(body_lines[1:]).strip()
else:
    first_line = ""
    text_to_process = issue_body.strip()

# Check if the user wrapped their text entirely in double or single quotes
skip_ai = False
if len(text_to_process) >= 2 and (
    (text_to_process.startswith('"') and text_to_process.endswith('"')) or 
    (text_to_process.startswith("'") and text_to_process.endswith("'"))
):
    skip_ai = True
    # Remove the outer quotes so they don't appear in the final article
    text_to_process = text_to_process[1:-1].strip()
    print("✅ User requested text to remain untouched (found quotes).")
else:
    print("🤖 User provided unquoted text. AI will expand to ~500 words or spellcheck.")

# --- AI GENERATION FUNCTION ---
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-pro')

def process_content_with_ai(user_text, content_category):
    if not user_text.strip():
        return "Check out this new release!", ""
        
    prompt = f"""
    You are an expert writer and editor for a Pauper Commander (PDH) community website. 
    A creator submitted notes/text for a new post. 
    
    YOUR TASK:
    1. First, write a VERY SHORT "teaser" (Max 12 words) starting with "EXCERPT:".
    2. Then, write a full, engaging article of approximately 500 words based on their submission. 
       Correct any bad spelling or grammar natively.
       Keep the tone excited, community-focused, and encouraging. Focus on the joy of the format.
       Do not use an H1 header (# Title) at the start.
    
    CREATOR'S SUBMISSION:
    {user_text}
    """
    try:
        response = model.generate_content(prompt)
        resp_text = response.text
        
        # Parse Excerpt vs Body
        if "EXCERPT:" in resp_text:
            parts = resp_text.split("EXCERPT:", 1)[1].split("\n", 1)
            out_excerpt = parts[0].strip().replace('"', '')
            out_body = parts[1].strip() if len(parts) > 1 else ""
            return out_excerpt, out_body
        return "Check out our latest content!", resp_text.replace('"', '')
    except Exception as e:
        print(f"❌ AI Generation failed: {e}")
        return "Check out our latest content!", user_text

def get_fallback_excerpt(text):
    words = text.split()
    return " ".join(words[:12]).replace('"', '') + "..." if len(words) > 12 else text.replace('"', '')

# --- ROUTING, EMBEDS & CONTENT ASSEMBLY ---
article_body = ""
excerpt_text = "Check out our latest content!"
image_filename = "cpdh.png" # Safe default from your repo for Spotify/Articles
embed_code = ""
video_id = None

if content_type == "youtube":
    video_url, video_id = find_youtube_url(first_line)
    if not video_id:
        print("❌ Error: The first line is not a valid YouTube URL.")
        sys.exit(1)
        
    channel_name, video_description = scrape_video_data(video_url)
    
    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        # If they gave no text at all, fall back to scraped YouTube description
        source_text = text_to_process if text_to_process.strip() else f"Video by {channel_name}. YouTube Description: {video_description}"
        excerpt_text, article_body = process_content_with_ai(source_text, content_type)

    embed_code = f"""
<div style="text-align: center; margin-top: 40px; margin-bottom: 40px;">
  <h3>Watch the Video</h3>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
</div>
"""

elif content_type == "spotify":
    spotify_match = re.search(r'spotify\.com/(episode|show)/([a-zA-Z0-9]+)', first_line)
    if not spotify_match:
        print("❌ Error: The first line is not a valid Spotify URL.")
        sys.exit(1)
    
    spot_type = spotify_match.group(1)
    spot_id = spotify_match.group(2)
    
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

elif content_type == "article":
    if skip_ai:
        article_body = text_to_process
        excerpt_text = get_fallback_excerpt(text_to_process)
    else:
        excerpt_text, article_body = process_content_with_ai(text_to_process, content_type)

    # Extract links to create buttons at the bottom
    links = re.findall(r'(https?://[^\s\)]+)', issue_body)
    links = list(set([re.sub(r'[.,;!?]$', '', l) for l in links]))
    
    if links:
        button_html = '\n\n<div style="margin-top: 40px; text-align: center;">\n  <hr>\n  <h3>Helpful Links</h3>\n'
        for i, link in enumerate(links):
            button_html += f'  <a href="{link}" class="btn btn--primary" target="_blank" style="margin: 5px;">Reference Link {i+1}</a>\n'
        button_html += '</div>\n'
        embed_code = button_html

# --- 6. DOWNLOAD THUMBNAIL (YouTube Only) ---
if content_type == "youtube" and video_id:
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

print(f"Successfully created post: {filename}")
