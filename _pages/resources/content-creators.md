---
# --- 1. YAML FRONT MATTER (THE DATA) ---
title: " "
layout: splash
permalink: /resources/content-creators/

# Optional: Add a big header image, just like your index page
# header:
#   overlay_image: /assets/images/Gemini_Generated_Image_bpu1z6bpu1z6bpu1.png
#  overlay_filter: 0.0
#  title: " "

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

## Featured Creators

<div>
{% include_cached feature_row.html id="creators_row_1" %}
</div>

<div style="clear: both;"></div>

<div>
{% include_cached feature_row.html id="creators_row_2" %}
</div>

<div style="clear: both;"></div>

<div>
{% include_cached feature_row.html id="creators_row_3" %}
</div>

<div style="clear: both;"></div>

<div>
{% include_cached feature_row.html id="creators_row_4" %}
</div>
