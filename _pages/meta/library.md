---
title: "Decklist Library"
layout: splash
permalink: /library/
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
---

<style>
    /* --- 1. The Container "Breakout" --- */
    /* This wrapper ensures the table can scroll on mobile */
    .table-wrapper {
        width: 100%;
        overflow-x: auto; /* Adds scrollbar ONLY if needed (mobile) */
        margin-bottom: 2em;
        -webkit-overflow-scrolling: touch; /* Smooth scrolling on iOS */
    }

    /* --- 2. The Table Styling --- */
    .simple-deck-table {
        width: 100%;          /* Force full width */
        min-width: 600px;     /* Minimum width to prevent crushing content */
        border-collapse: collapse; /* Removes gaps between cells */
        background-color: #2d2d2d;
        color: #e0e0e0;
        font-size: 0.95em;
        border-radius: 8px;   /* Rounded corners if the container allows */
        overflow: hidden;
    }

    /* Header Styling */
    .simple-deck-table thead th {
        background-color: #1a1a1a;
        color: #ffffff;
        text-align: left;
        padding: 14px 12px;
        border-bottom: 2px solid #555;
        white-space: nowrap; /* Keeps headers on one line */
    }

    /* Row Styling */
    .simple-deck-table tbody td {
        padding: 12px;
        border-bottom: 1px solid #444;
        vertical-align: middle;
    }

    /* Alternating Row Colors (Optional, good for readability) */
    .simple-deck-table tbody tr:nth-of-type(even) {
        background-color: #333;
    }

    /* Hover Effect */
    .simple-deck-table tbody tr:hover {
        background-color: #444;
    }

    /* --- 3. The Button --- */
    .btn-view {
        display: inline-block;
        padding: 6px 14px;
        background-color: #555;
        color: #fff !important;
        text-decoration: none;
        border-radius: 4px;
        font-size: 0.85em;
        transition: background 0.2s;
    }
    .btn-view:hover {
        background-color: #777;
    }
    
    /* --- 4. THE "GAP" FIXER --- */
    /* If your theme adds padding, use negative margins to pull the table to the edge */
    @media (min-width: 800px) {
        .full-width-breakout {
            margin-left: -20px;  /* Adjust these numbers if there is still a gap */
            margin-right: -20px;
            width: calc(100% + 40px);
        }
    }
</style>

<div class="table-wrapper full-width-breakout">
    <table class="simple-deck-table">
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
                <td><a href="https://moxfield.com/decks/WFOkQ_uhmkOsNCKO4mUDTw" target="_blank" class="btn-view">View</a></td>
                <td>Arabella, Abandoned Doll</td>
                <td>Common Cause X</td>
                <td>Clay</td>
                <td>Boros</td>
                <td>Aggro</td>
                <td>2026-02-07</td>
            </tr>
            <tr>
                <td><a href="https://www.moxfield.com/decks/8Y8epCv_fk2Xd4ddYIdANw" target="_blank" class="btn-view">View</a></td>
                <td>Juri, Master of the Revue</td>
                <td>Riches to Rags I</td>
                <td>Jacob Paris</td>
                <td>Rakdos</td>
                <td>Midrange</td>
                <td>2022-10-31</td>
            </tr>
             <tr>
                <td><a href="#" class="btn-view">View</a></td>
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

<hr style="margin: 3em 0;">

<div style="text-align: center; margin-bottom: 4em;">
  <h3>Explore Deeper</h3>
  <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px;">
    <a href="{{ '/meta/top10timeline/' | relative_url }}" class="btn btn--primary btn--large">📈 Historical Top 10</a>
    <a href="{{ '/meta/seeyourstats/' | relative_url }}" class="btn btn--primary btn--large">🔎 See Your Stats</a>
    <a href="{{ '/meta/' | relative_url }}" class="btn btn--inverse btn--large">↩ Back to Meta</a>
  </div>
</div>