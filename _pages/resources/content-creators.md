---
# --- 1. YAML FRONT MATTER (THE DATA) ---
title: " "
layout: splash
permalink: /resources/content-creators/

# Optional: Add a big header image, just like your index page
# header:
#   overlay_image: /assets/images/Gemini_Generated_Image_bpu1z6bpu1z6bpu1.png
#   overlay_filter: 0.0
#   title: " "

# ---
# We define FOUR separate feature row data blocks here.
# You can add as many or as few creators as you want to each row.
# ---

# Data for the first row
creators_row_1:
  - image_path: /assets/images/tpp-sq.jfif
    title: "PDH Pod"
    url: "https://open.spotify.com/show/55DyhZMhnn7z4SivHPiFVC?si=gzHUt6RKTnmAbtkdYDv0Ow&nd=1&dlsi=9a5666161b4b4e07"
  - image_path: /assets/images/jala-sq.jpg
    title: "Jalapeño Paupers"
    url: "https://www.youtube.com/@JalapenoPaupersMTG/videos"
  - image_path: /assets/images/tpp-sq.jfif
    title: "PDH Pod Stream"
    url: "https://www.twitch.tv/thepdhpod"

# Data for the second row
creators_row_2:
  - image_path: /assets/images/lobbert.png
    title: "Lobbert"
    url: "https://www.youtube.com/@lobbert8"
  - image_path: /assets/images/comcon.jpg
    title: "Common Connoisseurs"
    url: "https://www.youtube.com/@CommonConnoisseurs"
  - image_path: /assets/images/sanctuary.png
    title: "Sanctuary PDH"
    url: "https://www.youtube.com/@SanctuaryPDH/videos"

# Data for the third row
creators_row_3:
  - image_path: /assets/images/omg.jpg
    title: "One More Game"
    url: "https://www.youtube.com/@Omgmtg"
  - image_path: /assets/images/pstorm.jpg
    title: "Possibility Storm"
    url: "https://www.youtube.com/@thepossibilitystorm"
  - image_path: /assets/images/twitch.jpg
    title: "PDH Pals Stream"
    url: "https://www.twitch.tv/pdhpals?sr=a"

---

<style>
  /* 1. The Grid Layout */
  .creator-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
    padding: 0 1rem;
  }

  /* 2. The Card Container */
  .creator-card {
    background: #12121a; /* Abyss theme */
    border: 1px solid #3a3a4a; /* Mist border */
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.2s ease;
    text-decoration: none !important;
    display: block;
    height: 100%;
  }

  .creator-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
    border-color: #7c3aed; /* Arcane purple hover */
  }

  /* 3. The Image Area */
  .creator-image-box {
    position: relative;
    height: 200px; /* Fixed height for uniformity */
    width: 100%;
    overflow: hidden;
    background: #0a0a0f; /* Void background */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* 4. The Blurred Background */
  .creator-bg-blur {
    position: absolute;
    inset: -20px;
    background-size: cover;
    background-position: center;
    filter: blur(12px) brightness(0.4);
    z-index: 1;
    transform: scale(1.2);
  }

  /* 5. The Sharp Foreground Image */
  .creator-img-front {
    position: relative;
    z-index: 2;
    max-height: 85%;
    max-width: 85%;
    width: auto;
    height: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));
  }

  /* 6. The Text Area */
  .creator-info {
    padding: 1.25rem;
    text-align: center;
    border-top: 1px solid #3a3a4a;
  }

  .creator-title {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 1.25rem;
    color: #e5e5e7;
    margin: 0;
  }
  
  .section-title {
    text-align: center;
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.5rem;
    margin-bottom: 2rem;
    margin-top: 2rem;
  }
</style>

<h2 class="section-title">Featured Creators</h2>

<div class="creator-grid">
  {% for creator in page.creators_row_1 %}
    <a href="{{ creator.url }}" target="_blank" rel="noopener noreferrer" class="creator-card">
      <div class="creator-image-box">
        <div class="creator-bg-blur" style="background-image: url('{{ creator.image_path | relative_url }}');"></div>
        <img src="{{ creator.image_path | relative_url }}" alt="{{ creator.title }}" class="creator-img-front">
      </div>
      <div class="creator-info">
        <h3 class="creator-title">{{ creator.title }}</h3>
      </div>
    </a>
  {% endfor %}

  {% for creator in page.creators_row_2 %}
    <a href="{{ creator.url }}" target="_blank" rel="noopener noreferrer" class="creator-card">
      <div class="creator-image-box">
        <div class="creator-bg-blur" style="background-image: url('{{ creator.image_path | relative_url }}');"></div>
        <img src="{{ creator.image_path | relative_url }}" alt="{{ creator.title }}" class="creator-img-front">
      </div>
      <div class="creator-info">
        <h3 class="creator-title">{{ creator.title }}</h3>
      </div>
    </a>
  {% endfor %}

  {% for creator in page.creators_row_3 %}
    <a href="{{ creator.url }}" target="_blank" rel="noopener noreferrer" class="creator-card">
      <div class="creator-image-box">
        <div class="creator-bg-blur" style="background-image: url('{{ creator.image_path | relative_url }}');"></div>
        <img src="{{ creator.image_path | relative_url }}" alt="{{ creator.title }}" class="creator-img-front">
      </div>
      <div class="creator-info">
        <h3 class="creator-title">{{ creator.title }}</h3>
      </div>
    </a>
  {% endfor %}
  
  {% if page.creators_row_4 %}
    {% for creator in page.creators_row_4 %}
      <a href="{{ creator.url }}" target="_blank" rel="noopener noreferrer" class="creator-card">
        <div class="creator-image-box">
          <div class="creator-bg-blur" style="background-image: url('{{ creator.image_path | relative_url }}');"></div>
          <img src="{{ creator.image_path | relative_url }}" alt="{{ creator.title }}" class="creator-img-front">
        </div>
        <div class="creator-info">
          <h3 class="creator-title">{{ creator.title }}</h3>
        </div>
      </a>
    {% endfor %}
  {% endif %}
</div>