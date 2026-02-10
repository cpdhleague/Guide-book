---
title: "Decklist Library"
layout: splash
permalink: /library/
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
---

<style>
    /* --- 1. CENTERED LAYOUT --- */
    .library-centered-wrapper {
        width: 100%;
        max-width: 1200px; /* Stops it from getting too wide on huge monitors */
        margin: 0 auto;    /* This centers the wrapper */
        padding: 0 10px;   /* Small safety padding for mobile edges */
    }

    /* --- 2. CLEAN TABLE STYLING (No Outer Box) --- */
    .centered-deck-table {
        width: 100%;
        border-collapse: collapse; 
        color: #e0e0e0;
        font-size: 0.95em;
        /* No background color on the table itself to blend in */
    }

    /* Header: Clean line at the bottom */
    .centered-deck-table thead th {
        text-align: left;
        padding: 12px 15px;
        border-bottom: 2px solid #7c3aed; /* Using your 'primary' purple for flair */
        color: #fff;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        font-size: 0.85em;
    }

    /* Rows: Minimalist */
    .centered-deck-table tbody tr {
        border-bottom: 1px solid #333; /* Subtle divider */
        transition: background 0.2s;
    }

    /* Hover: Highlight the row slightly */
    .centered-deck-table tbody tr:hover {
        background-color: rgba(255, 255, 255, 0.05); 
    }

    .centered-deck-table tbody td {
        padding: 12px 15px;
        vertical-align: middle;
    }

    /* --- 3. MOBILE SCROLLING --- */
    /* If the screen is smaller than the table, allow scrolling */
    .scroll-container {
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }

    /* --- 4. BUTTON --- */
    .btn-view {
        display: inline-block;
        padding: 4px 12px;
        background-color: transparent;
        border: 1px solid #555;
        color: #ddd !important;
        text-decoration: none;
        border-radius: 4px;
        font-size: 0.8em;
        transition: all 0.2s;
    }
    .btn-view:hover {
        border-color: #7c3aed; /* Purple hover */
        color: #fff !important;
        background-color: rgba(124, 58, 237, 0.1);
    }
</style>

<div class="library-centered-wrapper">
    
    <div class="scroll-container">
        <table class="centered-deck-table">
            <thead>
                <tr>
                    <th>Link</th>
                    <th>Commander</th>
                    <th>Event</th>
                    <th>Player</th>
                    <th>Identity</th>
                    <th>Strategy</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><a href="https://moxfield.com/decks/WFOkQ_uhmkOsNCKO4mUDTw" target="_blank" class="btn-view">VIEW</a></td>
                    <td>Arabella, Abandoned Doll</td>
                    <td>Common Cause X</td>
                    <td>Clay</td>
                    <td>Boros</td>
                    <td>Aggro</td>
                    <td>2026-02-07</td>
                </tr>
                <tr>
                    <td><a href="https://www.moxfield.com/decks/8Y8epCv_fk2Xd4ddYIdANw" target="_blank" class="btn-view">VIEW</a></td>
                    <td>Juri, Master of the Revue</td>
                    <td>Riches to Rags I</td>
                    <td>Jacob Paris</td>
                    <td>Rakdos</td>
                    <td>Midrange</td>
                    <td>2022-10-31</td>
                </tr>
                <tr>
                    <td><a href="#" class="btn-view">VIEW</a></td>
                    <td>Tivit, Seller of Secrets</td>
                    <td>The 3rd Event</td>
                    <td>Michael</td>
                    <td>Esper</td>
                    <td>Control</td>
                    <td>2025-01-15</td>
                </tr>
            </tbody>
        </table>
    </div>
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