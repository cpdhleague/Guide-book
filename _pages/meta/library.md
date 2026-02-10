---
title: "Decklist Library"
layout: splash
permalink: /library/
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
---

<style>
    /* --- 1. THE LAYOUT FIX --- */
    /* This wrapper grabs the table and forces it to the center */
    .decklist-center-driver {
        display: flex;
        justify-content: center; /* Perfect centering */
        width: 100%;
        margin: 2em 0;
    }

    /* This wrapper handles the scrolling and width */
    .decklist-scroll-frame {
        /* "fit-content" is the magic. It tells the box:
           "Don't stretch to the edge. Just wrap around the text." */
        width: fit-content; 
        max-width: 100%; /* Prevent it from breaking mobile screens */
        overflow-x: auto; 
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5); /* Deep shadow for depth */
        background: #252532; /* 'Stone' color from your theme */
    }

    /* --- 2. TABLE STYLING --- */
    .decklist-table {
        /* We force 'max-content' so columns never squish. 
           The scrollbar will appear if this gets too wide. */
        width: max-content !important; 
        border-collapse: collapse;
        font-family: 'Outfit', sans-serif; /* Your theme font */
        color: #e5e5e7; /* Your 'pale' color */
    }

    /* Header */
    .decklist-table thead th {
        background-color: #1a1a24; /* 'Slate' */
        color: #a78bfa; /* 'Primary Glow' (Purple) */
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 700;
        padding: 16px 24px; /* Generous padding for a premium look */
        border-bottom: 2px solid rgba(124, 58, 237, 0.3);
        white-space: nowrap;
        text-align: left;
    }

    /* Rows */
    .decklist-table tbody tr {
        border-bottom: 1px solid rgba(58, 58, 74, 0.5);
        transition: background 0.2s;
    }
    .decklist-table tbody tr:last-child {
        border-bottom: none;
    }
    .decklist-table tbody tr:hover {
        background-color: #3a3a4a; /* 'Mist' - Highlight on hover */
    }
    .decklist-table tbody td {
        padding: 14px 24px;
        vertical-align: middle;
        white-space: nowrap; /* Keeps rows clean and straight */
    }

    /* --- 3. BUTTON STYLING --- */
    .btn-deck-link {
        display: inline-block;
        padding: 6px 16px;
        background-color: #7c3aed; /* Your 'Primary' Purple */
        color: #fff !important;
        text-decoration: none;
        border-radius: 4px;
        font-size: 0.85em;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: transform 0.2s, background 0.2s;
        box-shadow: 0 4px 10px rgba(124, 58, 237, 0.2);
    }
    .btn-deck-link:hover {
        background-color: #a78bfa; /* Glow on hover */
        transform: translateY(-2px);
        text-decoration: none;
    }
</style>

<div class="decklist-center-driver">
    <div class="decklist-scroll-frame">
        <table class="decklist-table">
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
                    <td><a href="https://moxfield.com/decks/WFOkQ_uhmkOsNCKO4mUDTw" target="_blank" class="btn-deck-link">View</a></td>
                    <td>Arabella, Abandoned Doll</td>
                    <td>Common Cause X</td>
                    <td>Clay</td>
                    <td>Boros</td>
                    <td>Aggro</td>
                    <td>2026-02-07</td>
                </tr>
                <tr>
                    <td><a href="https://www.moxfield.com/decks/8Y8epCv_fk2Xd4ddYIdANw" target="_blank" class="btn-deck-link">View</a></td>
                    <td>Juri, Master of the Revue</td>
                    <td>Riches to Rags I</td>
                    <td>Jacob Paris</td>
                    <td>Rakdos</td>
                    <td>Midrange</td>
                    <td>2022-10-31</td>
                </tr>
                <tr>
                    <td><a href="#" class="btn-deck-link">View</a></td>
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