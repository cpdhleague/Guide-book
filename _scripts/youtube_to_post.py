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

# --- ISOLATE FIRST LINE AND BODY ---
body_lines = issue_body.strip().split('\n')
first_line = body_lines[0].strip()
remaining_body = '\n'.join(body_lines[1:]).strip()

# --- CONTENT GENERATION, VALIDATION & EMBEDS ---
article_body = ""
excerpt_text = "Check out our latest content!"
image_filename = "default-thumbnail.jpg" 
embed_code = ""

model = genai.GenerativeModel('gemini-2.5-pro')

if content_type == "youtube":
    # 1. Validate YouTube Link
    video_url, video_id = find_youtube_url(first_line)
    if not video_id:
        print("❌ Error: The first line is not a valid YouTube URL.")
        sys.exit(1) # Exits with an error code to fail the GitHub Action
    
    # 2. Scrape and generate content using remaining_body or scraped data
    channel_name, video_description = scrape_video_data(video_url)
    # ... (Include your existing Gemini generation logic here) ...
    
    # 3. Create Embed
    embed_code = f"""
    <div style="text-align: center; margin-top: 40px; margin-bottom: 40px;">
      <h3>Watch the Video</h3>
      <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
    </div>
    """

elif content_type == "spotify":
    # 1. Validate Spotify Link
    spotify_match = re.search(r'spotify\.com/(episode|show)/([a-zA-Z0-9]+)', first_line)
    if not spotify_match:
        print("❌ Error: The first line is not a valid Spotify URL.")
        sys.exit(1) # Fails the GitHub Action
    
    spot_type = spotify_match.group(1) # Will be 'episode' or 'show'
    spot_id = spotify_match.group(2)
    
    # ... (Add Gemini generation logic here if you want it to summarize the podcast description) ...
    article_body = remaining_body # Fallback if no AI is used for Spotify yet
    
    # 2. Create Embed
    embed_code = f"""
    <div style="margin-top: 40px; margin-bottom: 40px;">
      <iframe style="border-radius:12px" src="https://open.spotify.com/embed/{spot_type}/{spot_id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
    """

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
        article_body = issue_body 
        print(f"Grammar check failed: {e}")

    # 1. Extract links to create buttons
    # Finds URLs starting with http:// or https://
    links = re.findall(r'(https?://[^\s\)]+)', issue_body)
    
    # Clean trailing punctuation from regex matches and deduplicate
    links = list(set([re.sub(r'[.,;!?]$', '', l) for l in links]))
    
    # 2. Generate Button HTML
    if links:
        button_html = '\n\n<div style="margin-top: 40px; text-align: center;">\n  <hr>\n  <h3>Helpful Links</h3>\n'
        for i, link in enumerate(links):
            # Using Jekyll's standard 'btn btn--primary' classes for buttons
            button_html += f'  <a href="{link}" class="btn btn--primary" target="_blank" style="margin: 5px;">Reference Link {i+1}</a>\n'
        button_html += '</div>\n'
        
        embed_code = button_html # We append the buttons where the embed code normally goes
