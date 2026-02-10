---
title: "Decklist Library"
layout: splash
permalink: /library/
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
---

<style>
    /* --- 1. THE BREAKOUT CONTAINER --- */
    /* This forces the container to ignore the max-width of the page 
       and stretch to the absolute edges of the browser window (100vw). */
    .decklist-breakout {
        width: 100vw; 
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        background: #1a1a1a; /* Dark background behind table */
        padding: 0;
        overflow: hidden; /* No scrollbars allowed */
    }

    /* --- 2. THE FLUID TABLE (Behaves like an Image) --- */
    .fluid-deck-table {
        width: 100%;           
        table-layout: fixed;   /* CRITICAL: Forces columns to split space evenly/fluidly */
        border-collapse: collapse;
        color: #e0e0e0;
        
        /* THE MAGIC: Font size scales with screen width.
           Min: 10px (so it's readable on phone)
           Ideal: 1.1% of screen width
           Max: 16px (so it's not huge on TV screens) */
        font-size: clamp(10px, 1.1vw, 16px); 
    }

    /* Header Styling */
    .fluid-deck-table thead th {
        background-color: #121212;
        color: #ffffff;
        text-align: left;
        padding: 1em 0.5em; /* Padding scales relative to font size */
        border-bottom: 2px solid #555;
        white-space: nowrap; /* Prevent headers from wrapping awkwardly */
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* Row Styling */
    .fluid-deck-table tbody td {
        padding: 0.8em 0.5em;
        border-bottom: 1px solid #444;
        vertical-align: middle;
        white-space: nowrap; /* Keep data on one line to act like an image */
        overflow: hidden;
        text-overflow: ellipsis; /* Add "..." if screen is WAY too small */
    }

    /* Alternating Colors */
    .fluid-deck-table tbody tr:nth-of-type(even) {
        background-color: #252525;
    }
    .fluid-deck-table tbody tr:hover {
        background-color: #333;
    }

    /* --- 3. COLUMN WIDTH CONTROL --- */
    /* We manually set widths so important columns (Commander) get more space 
       and small columns (Date/Link) get less. Total must = 100% */
    
    .col-link     { width: 8%;  text-align: center; }
    .col-cmdr     { width: 25%; }
    .col-event    { width: 20%; }
    .col-player   { width: 12%; }
    .col-identity { width: 12%; }
    .col-strategy { width: 12%; }
    .col-date     { width: 11%; }

    /* Button Styling */
    .btn-view {
        display: inline-block;
        padding: 0.3em 0.8em;
        background-color: #555;
        color: #fff !important;
        text-decoration: none;
        border-radius: 4px;
        transition: background 0.2s;
    }
    .btn-view:hover {
        background-color: #777;
    }

</style>

<div class="decklist-breakout">
    <table class="fluid-deck-table">
        <thead>
            <tr>
                <th class="col-link">Link</th>
                <th class="col-cmdr">Commander</th>
                <th class="col-event">Event</th>
                <th class="col-player">Player</th>
                <th class="col-identity">Identity</th>
                <th class="col-strategy">Strategy</th>
                <th class="col-date">Date</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="col-link"><a href="https://moxfield.com/decks/WFOkQ_uhmkOsNCKO4mUDTw" target="_blank" class="btn-view">View</a></td>
                <td class="col-cmdr">Arabella, Abandoned Doll</td>
                <td class="col-event">Common Cause X</td>
                <td class="col-player">Clay</td>
                <td class="col-identity">Boros</td>
                <td class="col-strategy">Aggro</td>
                <td class="col-date">2026-02-07</td>
            </tr>
            <tr>
                <td class="col-link"><a href="https://www.moxfield.com/decks/8Y8epCv_fk2Xd4ddYIdANw" target="_blank" class="btn-view">View</a></td>
                <td class="col-cmdr">Juri, Master of the Revue</td>
                <td class="col-event">Riches to Rags I</td>
                <td class="col-player">Jacob Paris</td>
                <td class="col-identity">Rakdos</td>
                <td class="col-strategy">Midrange</td>
                <td class="col-date">2022-10-31</td>
            </tr>
            <tr>
                <td class="col-link"><a href="#" class="btn-view">View</a></td>
                <td class="col-cmdr">Tivit, Seller of Secrets</td>
                <td class="col-event">The 3rd Event</td>
                <td class="col-player">Michael</td>
                <td class="col-identity">Esper</td>
                <td class="col-strategy">Control</td>
                <td class="col-date">2025-01-15</td>
            </tr>
        </tbody>
    </table>
</div>

<hr style="margin: 3em 0;">

<div style="text-align: center; margin-bottom: 4em;">
  <h3>Explore Deeper</h3>
  <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px;">
    <a href="{{ '/meta/top10timeline/' | relative_url }}" class="btn btn--primary btn--large">📈 Historical Top 10</a>
    <a href="{{ '/meta/seeyourstats/' | relative_url }}" class="btn btn--primary btn--large">🔎 See Your Stats</a>
    <a href="{{ '/meta/' | relative_url }}" class="btn btn--inverse btn--large">↩ Back to Meta</a>
  </div>
</div>