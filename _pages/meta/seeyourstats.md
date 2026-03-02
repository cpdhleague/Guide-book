---
title: "Player Data"
layout: splash
permalink: /meta/seeyourstats/
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
  <a href="{{ '/meta/top10timeline/' | relative_url }}">📈 Timelines</a>
  <a href="{{ '/meta/seeyourstats/' | relative_url }}" class="active">🔎 Player Data</a>
</nav>

<div style="width: 100%; max-width: 1200px; margin: 0 auto; padding: 20px 0;">
  <div class="flourish-embed flourish-chart" data-src="visualisation/26897507">
    <script src="https://public.flourish.studio/resources/embed.js"></script>
      <noscript>
        <img src="https://public.flourish.studio/visualisation/26897507/thumbnail" width="100%" alt="chart visualization" />
      </noscript>
  </div>
</div>

<div style="text-align: center; max-width: 800px; margin: 0 auto 2em auto; padding: 0 20px;">
  <p style="font-size: 1.1em; opacity: 0.9;">
    <strong>Find Your Data:</strong> Use the dropdown filters at the top of the chart below to search by <strong>Player Name</strong> or <strong>Commander</strong>.
    You can select multiple options to compare specific pilots or see how you perform across different decks.
  </p>
</div>

<div style="width: 100%; max-width: 1200px; margin: 0 auto; padding: 20px 0;">
  <div class="flourish-embed flourish-chart" data-src="visualisation/26909540">
    <script src="https://public.flourish.studio/resources/embed.js"></script>
    <noscript>
      <img src="https://public.flourish.studio/visualisation/26909540/thumbnail" width="100%" alt="chart visualization" />
    </noscript>
  </div>
</div>
