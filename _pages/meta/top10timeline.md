---
title: "Timelines"
layout: splash
permalink: /meta/top10timeline/
classes: short-header
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
---

<style>
.cpdh-nav {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0;
  max-width: 900px;
  margin: 0 auto 2.5em auto;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.10);
}
.cpdh-nav a {
  flex: 1 1 150px;
  text-align: center;
  padding: 14px 20px;
  font-size: 0.95em;
  font-weight: 600;
  letter-spacing: 0.03em;
  text-decoration: none !important;
  color: rgba(255,255,255,0.75) !important;
  background: rgba(255,255,255,0.07);
  border-right: 1px solid rgba(255,255,255,0.10);
  transition: background 0.2s, color 0.2s;
}
.cpdh-nav a:last-child {
  border-right: none;
}
.cpdh-nav a:hover {
  background: rgba(255,255,255,0.14);
  color: #fff !important;
}
.cpdh-nav a.active {
  background: rgba(255,255,255,0.20);
  color: #fff !important;
  border-bottom: 3px solid #fff;
  pointer-events: none;
}
</style>

<nav class="cpdh-nav">
  <a href="{{ '/meta/' | relative_url }}">📊 Meta</a>
  <a href="{{ '/library/' | relative_url }}">🏆 Decklist Library</a>
  <a href="{{ '/meta/top10timeline/' | relative_url }}" class="active">📈 Timelines</a>
  <a href="{{ '/meta/seeyourstats/' | relative_url }}">🔎 Player Data</a>
</nav>

<div style="width: 100%; max-width: 1200px; margin: 0 auto; padding: 20px 0;">
  <div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/26896977">
    <script src="https://public.flourish.studio/resources/embed.js"></script>
    <noscript>
      <img src="https://public.flourish.studio/visualisation/26896977/thumbnail" width="100%" alt="bar-chart-race visualization" />
    </noscript>
  </div>
</div>

<div style="text-align: center; max-width: 800px; margin: 0 auto 2em auto; padding: 0 20px;">
  <p style="font-size: 1.1em; opacity: 0.9;">
    <strong>Compare the Legends:</strong> Use the dropdown at the top of the chart below to filter for specific commanders. 
    You can select up to 10 different decks to see how they measure up against each other over time. 
    <br><em>(Scroll or search by commander name to find your favorites!)</em>
  </p>
</div>

<div style="width: 100%; max-width: 1200px; margin: 0 auto; padding: 20px 0;">
  <div class="flourish-embed flourish-chart" data-src="visualisation/26897848">
    <script src="https://public.flourish.studio/resources/embed.js"></script>
    <noscript>
      <img src="https://public.flourish.studio/visualisation/26897848/thumbnail" width="100%" alt="chart visualization" />
    </noscript>
  </div>
</div>
