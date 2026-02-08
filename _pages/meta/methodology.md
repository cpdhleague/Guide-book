---
title: "Methodology & Data"
layout: splash
permalink: /meta/methodology/
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
excerpt: "Understanding how we calculate ratings and access to our raw data."
---

# Methodology for cPDH Ratings

For our rating system, we use an Elo variant adapted for multiplayer. It has three key differences from standard Elo.

## What is Elo?
Elo is a rating system where, after every game, the winning player takes points from the losing player. If the winner has a higher rating, they will take fewer points. If the winner has a lower rating, they will take more points. Against an equally rated opponent, you will both remain at the same Elo if you each win 50% of the time.

## Our Multiplayer Variant
In a **4-player game**, the winner takes points from each loser, scored as three simultaneous wins. The rating of the winner is compared to the rating of each loser to determine how many points are taken. Against 3 equally rated opponents, you will all remain at the same Elo rating if you each win 25% of the time.

In a **3-player game** (which happens in some tournament settings), the winner takes points from only two losers and thus gains fewer points.

## Reduced Volatility at High Ratings
In our system, you do not lose more points when losing against a lower-rated opponent; to compensate, you take fewer points when winning against a lower-rated opponent. In Elo terms, the *k-value* is modified by the ratings difference. This makes the climb to the top a bit slower, but in return, a high rating won't be lost as quickly.

## Inactive Rating Adjustments
If a deck isn’t played for 4 calendar quarters, the Elo rating of that deck is adjusted to be 10% closer to the base Elo of 1,000 each calendar quarter. This ensures that ratings are fresh—a deck that was top-rated 2 years ago but has seen no play since then will no longer be considered a top deck.

## Bigger Numbers!
You start with 1,000 points. A win against equal or higher-rated opponents gains you 100 points, and a loss against equal or lower-rated opponents decreases your points by 33⅓. 

Regular Elo is not designed for such large gains, so on the backend, you actually start with 300 Elo; you gain 30 points from an equal win and lose 10 points from an equal loss. In Elo terms, the *k-value* is 20, which creates a balanced level of volatility. That backend Elo number is then multiplied by 3⅓ so that the displayed rating is more stretched out to avoid rating ties.

## Win Rates and Ratings
The table below shows what your rating would be based on your win rate against specific opponents.

| Win Rate | Rating (vs 1,000 Rated Opponents) | Rating (vs 1,200 Rated Opponents) |
| :--- | :--- | :--- |
| **25%** | 1,000 | 1,200 |
| **33%** | 1,235 | 1,435 |
| **40%** | 1,401 | 1,601 |
| **50%** | 1,636 | 1,836 |

---

# Data Access

We believe in transparency. You can view the raw data we use on our backend at the link below.

<div style="text-align: center; margin: 2em 0;">
  <a href="https://docs.google.com/spreadsheets/d/1URtAdCkQXfT7Jk_YEVtPLY3n11ciBCLhKu_7x-9VNu4/edit?usp=sharing" class="btn btn--primary btn--large" target="_blank">📂 Access Raw Data Sheet</a>
</div>

---

# Historical Data Archive

<div class="notice--warning">
  <strong>Note:</strong> The charts below display historical data from the previous version of our site. This data is <strong>no longer being updated as of late 2025</strong> and is preserved here for reference purposes only.
</div>

### Commander Stats (Archive)
<div style="width: 100%; overflow: auto; margin-bottom: 2em;">
<iframe width="1200" height="860" src="https://lookerstudio.google.com/embed/reporting/14d15235-575f-4dca-8751-b7797598765e/page/JaCSD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>
</div>

### Player Stats (Archive)
<div style="width: 100%; overflow: auto; margin-bottom: 2em;">
<iframe width="1200" height="860" src="https://lookerstudio.google.com/embed/reporting/c9c425f6-2c3d-4542-8b73-0adfac98fdc9/page/JaCSD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>
</div>

### Metagame Stats (Archive)
<div style="width: 100%; overflow: auto; margin-bottom: 2em;">
<iframe width="1200" height="1000" src="https://lookerstudio.google.com/embed/reporting/e6465966-c3f7-442c-9fb5-1a2f616882a0/page/p_de5p8rjwcd" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>
</div>
