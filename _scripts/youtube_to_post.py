import os
import sys
import requests
import re
from datetime import datetime
import google.generativeai as genai
import time

# --- CONFIGURATION ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

try:
    issue_body = sys.argv[1]
    raw_issue_title = sys.argv[2]
except IndexError:
    sys.exit(1)

# --- ROUTING BASED ON TITLE PREFIX ---
content_type = "unknown"
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

# --- CONTENT GENERATION & SPELLCHECK LOGIC ---
article_body = ""
excerpt_text = "Check out our latest content!"
image_filename = "default-thumbnail.jpg" # Make sure you have a default in assets/images/
embed_code = ""

model = genai.GenerativeModel('gemini-2.5-pro')

if content_type == "youtube":
    # (Keep your existing YouTube scraping and Gemini summary code here)
    # embed_code = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" ...></iframe>'
    pass

elif content_type == "spotify":
    # Example logic for Spotify
    # Extract Spotify URL, generate embed code
    pass

elif content_type == "article":
    print("🤖 Running Grammar and Spellcheck Bot...")
    grammar_prompt = f"""
    You are an editor for a Pauper Commander community website. 
    Review the following article submission. Correct bad spelling and grammar without significantly changing the content, wording, or the author's personal voice.
    
    ARTICLE TEXT:
    {issue_body}
    """
    try:
        response = model.generate_content(grammar_prompt)
        article_body = response.text
    except Exception as e:
        article_body = issue_body # Fallback to raw text if AI fails
        print(f"Grammar check failed: {e}")

# --- FRONTMATTER AND FILE CREATION ---
date_str = datetime.now().strftime("%Y-%m-%d")
safe_title = re.sub(r'[^a-zA-Z0-9\s_-]', '', final_title).strip().replace(" ", "-").lower()
filename = f"_posts/{date_str}-{safe_title}.md"
yaml_title = final_title.replace('"', '\\"')
yaml_excerpt = excerpt_text.replace('"', '\\"')

# Added the 'image:' tag for the RSS feed and standardized the header setup
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
