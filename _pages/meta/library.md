---
title: "Decklist Library"
layout: splash
permalink: /library/
classes: short-header
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
---

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.css">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css">

<style>
    /* 1. Container: Full Width, No Max-Width */
    .library-container {
        width: 100%;
        margin: 0;
        padding: 0 10px; /* Small padding so text doesn't hit the very edge */
    }

    /* 2. Table Background & Text Colors (Dark Theme) */
    #libraryTable {
        width: 100% !important;
        background-color: #2d2d2d; /* Dark Grey Background */
        color: #e0e0e0;            /* Light Text */
        border-collapse: collapse;
        font-size: 0.95em;
    }

    /* 3. Header Styling */
    #libraryTable thead th {
        background-color: #1a1a1a; /* Darker Header */
        color: #ffffff;
        border-bottom: 2px solid #444;
        text-align: left;
        padding: 12px 10px;
    }

    /* 4. Row Styling (Single Color, No Zebra Striping) */
    #libraryTable tbody tr {
        background-color: #2d2d2d !important; /* Force same dark color */
        border-bottom: 1px solid #444;       /* Subtle separator line */
    }

    /* 5. Hover Effect */
    #libraryTable tbody tr:hover {
        background-color: #383838 !important; /* Slightly lighter on hover */
    }

    #libraryTable tbody td {
        padding: 10px;
        vertical-align: middle;
    }

    /* 6. Button Style */
    .btn-decklist {
        display: inline-block;
        padding: 5px 10px;
        background-color: #555;
        color: #fff !important;
        text-decoration: none;
        border: 1px solid #777;
        border-radius: 4px;
        font-size: 0.85em;
        transition: background 0.2s;
        text-align: center;
    }
    .btn-decklist:hover {
        background-color: #777;
        text-decoration: none;
    }

    /* DataTables Controls (Search/Pagination) to match theme */
    .dataTables_wrapper .dataTables_length, 
    .dataTables_wrapper .dataTables_filter, 
    .dataTables_wrapper .dataTables_info, 
    .dataTables_wrapper .dataTables_processing, 
    .dataTables_wrapper .dataTables_paginate {
        color: #e0e0e0 !important;
    }
    .dataTables_wrapper .dataTables_paginate .paginate_button {
        color: #e0e0e0 !important;
    }
    .dataTables_wrapper .dataTables_paginate .paginate_button.disabled {
        color: #666 !important;
    }

    /* Mobile adjustments */
    @media screen and (max-width: 768px) {
        div.dataTables_wrapper div.dataTables_filter input {
            width: 150px;
        }
    }
</style>

<div class="library-container">
    <table id="libraryTable" class="display responsive nowrap" style="width:100%">
        <thead>
            <tr>
                <th data-priority="1">Link</th>
                <th data-priority="1">Commander</th>
                <th data-priority="3">Event</th>
                <th data-priority="2">Player</th>
                <th data-priority="5">Identity</th>
                <th data-priority="4">Strategy</th>
                <th data-priority="6">Date</th>
            </tr>
        </thead>
        <tbody>
    <tr>
        <td><a href="https://moxfield.com/decks/WFOkQ_uhmkOsNCKO4mUDTw" target="_blank" class="btn-decklist">View</a></td>
        <td>Arabella, Abandoned Doll</td>
        <td>Common Cause X</td>
        <td>Clay</td>
        <td>Boros</td>
        <td>Aggro</td>
        <td data-sort="20260207">2026-02-07</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/fJYMP6v2TEG_d_36iCcLgQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Akiri, Fearless Voyager</td>
        <td>Common Cause X</td>
        <td>southlakes</td>
        <td>Boros</td>
        <td>Combo</td>
        <td data-sort="20260207">2026-02-07</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/ja_xsny7vkqgrJ088-Utug" target="_blank" class="btn-decklist">View</a></td>
        <td>Bone-Cairn Butcher</td>
        <td>Common Cause X</td>
        <td>Levin Rodloff</td>
        <td>Mardu</td>
        <td>Midrange</td>
        <td data-sort="20260207">2026-02-07</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/aZ-sF7xauUKBogcA3wQCdg" target="_blank" class="btn-decklist">View</a></td>
        <td>Ganax, Astral Hunter // Feywild Visitor</td>
        <td>Common Cause X</td>
        <td>Luis Esquivel</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20260207">2026-02-07</td>
    </tr>
    

    <tr>
        <td><a href="https://topdeck.gg/deck/cpdh-commander-clash-2025/atJqz3FPb5R4oK7Vnfu67weNTb93" target="_blank" class="btn-decklist">View</a></td>
        <td>Long Feng, Grand Secretariat</td>
        <td>Commander Clash 2025</td>
        <td>myra</td>
        <td>Golgari</td>
        <td>Combo</td>
        <td data-sort="20251213">2025-12-13</td>
    </tr>
    

    <tr>
        <td><a href="https://topdeck.gg/deck/cpdh-commander-clash-2025/q9Ki57T7fEdJaMPol5rr0e2Znar2" target="_blank" class="btn-decklist">View</a></td>
        <td>Rocketeer Boostbuggy</td>
        <td>Commander Clash 2025</td>
        <td>Alkadron</td>
        <td>Gruul</td>
        <td>Midrange</td>
        <td data-sort="20251213">2025-12-13</td>
    </tr>
    

    <tr>
        <td><a href="https://topdeck.gg/deck/cpdh-commander-clash-2025/hJvR2Kz1c3u9i9j3kP4s" target="_blank" class="btn-decklist">View</a></td>
        <td>The Emperor of Palamecia // The Lord Master of Hell</td>
        <td>Commander Clash 2025</td>
        <td>Russell  Harder</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20251213">2025-12-13</td>
    </tr>
    

    <tr>
        <td><a href="https://topdeck.gg/deck/cpdh-commander-clash-2025/g8F1h9i2j3k4l5m6n7o8" target="_blank" class="btn-decklist">View</a></td>
        <td>Veteran Beastrider</td>
        <td>Commander Clash 2025</td>
        <td>Scarecrow1779</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20251213">2025-12-13</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/hBfI902k40u2l_z495b8NA" target="_blank" class="btn-decklist">View</a></td>
        <td>Honest Rutstein</td>
        <td>AllThatGames I</td>
        <td>Brandon White</td>
        <td>Golgari</td>
        <td>Midrange</td>
        <td data-sort="20251019">2025-10-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/y9jK4m7n306i1l8k2p5Q" target="_blank" class="btn-decklist">View</a></td>
        <td>Narfi, Betrayer King</td>
        <td>AllThatGames I</td>
        <td>Scarecrow1779</td>
        <td>Dimir</td>
        <td>Control</td>
        <td data-sort="20251019">2025-10-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>AllThatGames I</td>
        <td>Paul</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20251019">2025-10-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>AllThatGames I</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20251019">2025-10-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/347bF45a1c9e8d2f6" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Common Cause IX</td>
        <td>Liam</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20250816">2025-08-16</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause IX</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20250816">2025-08-16</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Common Cause IX</td>
        <td>Crash</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20250816">2025-08-16</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/u9iO2p3a4s5d6f7g8h9j" target="_blank" class="btn-decklist">View</a></td>
        <td>Zada, Hedron Grinder</td>
        <td>Riches to Rags IV</td>
        <td>Liam</td>
        <td>Red</td>
        <td>Combo</td>
        <td data-sort="20250810">2025-08-10</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/k1l2m3n4o5p6q7r8s9t0" target="_blank" class="btn-decklist">View</a></td>
        <td>Etali, Primal Storm</td>
        <td>Riches to Rags IV</td>
        <td>Scarecrow1779</td>
        <td>Red</td>
        <td>Midrange</td>
        <td data-sort="20250810">2025-08-10</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/v3bN5m7k9l1j2h4g6f8d" target="_blank" class="btn-decklist">View</a></td>
        <td>Wilson, Refined Grizzly + Cultist of the Absolute</td>
        <td>Riches to Rags IV</td>
        <td>Flicker729</td>
        <td>Golgari</td>
        <td>Midrange</td>
        <td data-sort="20250810">2025-08-10</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/r8s9t0u1v2w3x4y5z6A" target="_blank" class="btn-decklist">View</a></td>
        <td>Young Pyromancer</td>
        <td>Cloudy Commons I</td>
        <td>Peter Young</td>
        <td>Red</td>
        <td>Aggro</td>
        <td data-sort="20250517">2025-05-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Cloudy Commons I</td>
        <td>Dylon A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20250517">2025-05-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Cloudy Commons I</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20250517">2025-05-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Cloudy Commons I</td>
        <td>Tyler J</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20250517">2025-05-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/z1x2c3v4b5n6m7a8s9d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Riches to Rags V</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20250316">2025-03-16</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>Sanctuary PDH VIII</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20250215">2025-02-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g2h3j4k5l6m7n8b9v0c1" target="_blank" class="btn-decklist">View</a></td>
        <td>Mayhem Devil</td>
        <td>Sanctuary PDH VIII</td>
        <td>Julian</td>
        <td>Rakdos</td>
        <td>Midrange</td>
        <td data-sort="20250215">2025-02-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/a1s2d3f4g5h6j7k8l9z0" target="_blank" class="btn-decklist">View</a></td>
        <td>Bilbo, Retired Burglar</td>
        <td>Sanctuary PDH VIII</td>
        <td>Ginger Persolus</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20250215">2025-02-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Sanctuary PDH VIII</td>
        <td>Crash</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20250215">2025-02-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/gLhC4kEw_02f741ZqG6LWA" target="_blank" class="btn-decklist">View</a></td>
        <td>Abdel Adrian, Gorion’s Ward + Agent of the Iron Throne</td>
        <td>Common Cause VI</td>
        <td>uyokonoyami</td>
        <td>Orzhov</td>
        <td>Combo</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/vR7h6Q9YIEO-j20n3K8u1g" target="_blank" class="btn-decklist">View</a></td>
        <td>Abdel Adrian, Gorion’s Ward + Sword Coast Sailor</td>
        <td>Common Cause VI</td>
        <td>PurplePenguinJo</td>
        <td>Azorius</td>
        <td>Combo</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause VI</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause VI</td>
        <td>Scarecrow1779</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/n1tI9gXyMUiGryE_a7OsqQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Abdel Adrian, Gorion’s Ward + Agent of the Iron Throne</td>
        <td>The Pauper Pit I</td>
        <td>Heartless</td>
        <td>Orzhov</td>
        <td>Combo</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/WFOkQ_uhmkOsNCKO4mUDTw" target="_blank" class="btn-decklist">View</a></td>
        <td>Arabella, Abandoned Doll</td>
        <td>The Pauper Pit I</td>
        <td>Shakur W</td>
        <td>Boros</td>
        <td>Aggro</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/hH8W1rX4t0iH8j5D1f9A" target="_blank" class="btn-decklist">View</a></td>
        <td>Kutzil, Malamet Exemplar</td>
        <td>The Pauper Pit I</td>
        <td>Lobbert</td>
        <td>Selesnya</td>
        <td>Aggro</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>The Pauper Pit I</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>Sanctuary PDH VII</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20240824">2024-08-24</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH VII</td>
        <td>Scarecrow1779</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240824">2024-08-24</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g2h3j4k5l6m7n8b9v0c1" target="_blank" class="btn-decklist">View</a></td>
        <td>Mayhem Devil</td>
        <td>Sanctuary PDH VII</td>
        <td>Julian</td>
        <td>Rakdos</td>
        <td>Midrange</td>
        <td data-sort="20240824">2024-08-24</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Sanctuary PDH VII</td>
        <td>Crash</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240824">2024-08-24</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/k1l2m3n4o5p6q7r8s9t0" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>RIW II</td>
        <td>Bobby</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240727">2024-07-27</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/u9iO2p3a4s5d6f7g8h9j" target="_blank" class="btn-decklist">View</a></td>
        <td>Vhal, Candlekeep Researcher + Agent of the Shadow Thieves</td>
        <td>RIW II</td>
        <td>TonisBolognis</td>
        <td>Dimir</td>
        <td>Combo</td>
        <td data-sort="20240727">2024-07-27</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/v3bN5m7k9l1j2h4g6f8d" target="_blank" class="btn-decklist">View</a></td>
        <td>Wilson, Refined Grizzly + Far Traveler</td>
        <td>RIW II</td>
        <td>HiveCryptid</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20240727">2024-07-27</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/r8s9t0u1v2w3x4y5z6A" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>RIW II</td>
        <td>Scarecrow1779</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240727">2024-07-27</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause VIII</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240615">2024-06-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/z1x2c3v4b5n6m7a8s9d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Common Cause VIII</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20240615">2024-06-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Sivriss, Nightmare Speaker + Cloakwood Hermit</td>
        <td>Common Cause VIII</td>
        <td>Dino</td>
        <td>Golgari</td>
        <td>Midrange</td>
        <td data-sort="20240615">2024-06-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Common Cause VIII</td>
        <td>Crash</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240615">2024-06-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/v3bN5m7k9l1j2h4g6f8d" target="_blank" class="btn-decklist">View</a></td>
        <td>Sivriss, Nightmare Speaker + Cloakwood Hermit</td>
        <td>Common Cause VIII</td>
        <td>Liam</td>
        <td>Golgari</td>
        <td>Midrange</td>
        <td data-sort="20240615">2024-06-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Riches to Rags III</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20240414">2024-04-14</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Inspiring Leader</td>
        <td>Riches to Rags III</td>
        <td>Dylan A</td>
        <td>Boros</td>
        <td>Aggro</td>
        <td data-sort="20240414">2024-04-14</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Riches to Rags III</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240414">2024-04-14</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Soul of Migration</td>
        <td>Riches to Rags III</td>
        <td>Scarecrow1779</td>
        <td>Azorius</td>
        <td>Midrange</td>
        <td data-sort="20240414">2024-04-14</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/n1m2a3s4d5f6g7h8j9k0" target="_blank" class="btn-decklist">View</a></td>
        <td>Breeches, Brazen Plunderer + Malcolm, Keen-Eyed Navigator</td>
        <td>Sanctuary PDH VI</td>
        <td>Nolan S</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20240406">2024-04-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH VI</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240406">2024-04-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/z1x2c3v4b5n6m7a8s9d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Crackling Drake</td>
        <td>Sanctuary PDH VI</td>
        <td>Julian</td>
        <td>Izzet</td>
        <td>Combo</td>
        <td data-sort="20240406">2024-04-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH VI</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240406">2024-04-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause V</td>
        <td>Scarecrow1779</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240217">2024-02-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause V</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240217">2024-02-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/z1x2c3v4b5n6m7a8s9d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Common Cause V</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20240217">2024-02-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Murmuring Mystic</td>
        <td>Common Cause V</td>
        <td>Lobbert</td>
        <td>Mono U</td>
        <td>Control</td>
        <td data-sort="20240217">2024-02-17</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Sanctuary PDH V</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20240113">2024-01-13</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH V</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240113">2024-01-13</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH V</td>
        <td>Scarecrow1779</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20240113">2024-01-13</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/z1x2c3v4b5n6m7a8s9d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Murmuring Mystic</td>
        <td>Sanctuary PDH V</td>
        <td>Lobbert</td>
        <td>Mono U</td>
        <td>Control</td>
        <td data-sort="20240113">2024-01-13</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Sanctuary PDH IV</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20231125">2023-11-25</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/hH8W1rX4t0iH8j5D1f9A" target="_blank" class="btn-decklist">View</a></td>
        <td>Kutzil, Malamet Exemplar</td>
        <td>Sanctuary PDH IV</td>
        <td>Lobbert</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20231125">2023-11-25</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH IV</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20231125">2023-11-25</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH IV</td>
        <td>Scarecrow1779</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20231125">2023-11-25</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q1w2e3r4t5y6u7i8o9p0" target="_blank" class="btn-decklist">View</a></td>
        <td>Abdel Adrian, Gorion’s Ward + Sword Coast Sailor</td>
        <td>Sanctuary PDH III</td>
        <td>Kunx</td>
        <td>Azorius</td>
        <td>Combo</td>
        <td data-sort="20231104">2023-11-04</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/OxGAVHRC8EmTbe4EBFL4Ig" target="_blank" class="btn-decklist">View</a></td>
        <td>Ardenn, Intrepid Archaeologist + Malcolm, Keen-Eyed Navigator</td>
        <td>Sanctuary PDH III</td>
        <td>Chinaman</td>
        <td>Azorius</td>
        <td>Combo</td>
        <td data-sort="20231104">2023-11-04</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH III</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20231104">2023-11-04</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH III</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20231104">2023-11-04</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Common Cause IV</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20231021">2023-10-21</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>Common Cause IV</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20231021">2023-10-21</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Warden of the Eye</td>
        <td>Common Cause IV</td>
        <td>Bosh</td>
        <td>Jeskai</td>
        <td>Combo</td>
        <td data-sort="20231021">2023-10-21</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause IV</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20231021">2023-10-21</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/u9iO2p3a4s5d6f7g8h9j" target="_blank" class="btn-decklist">View</a></td>
        <td>Izzet Guildmage</td>
        <td>PDH Tourney - Mainberg I</td>
        <td>Trafton</td>
        <td>Izzet</td>
        <td>Combo</td>
        <td data-sort="20230826">2023-08-26</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause III</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230819">2023-08-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Common Cause III</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20230819">2023-08-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/k1l2m3n4o5p6q7r8s9t0" target="_blank" class="btn-decklist">View</a></td>
        <td>Loyal Apprentice</td>
        <td>Common Cause III</td>
        <td>Clay</td>
        <td>Izzet</td>
        <td>Aggro</td>
        <td data-sort="20230819">2023-08-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Common Cause III</td>
        <td>Crash</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20230819">2023-08-19</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g2h3j4k5l6m7n8b9v0c1" target="_blank" class="btn-decklist">View</a></td>
        <td>Mayhem Devil</td>
        <td>Sanctuary PDH II</td>
        <td>Julian</td>
        <td>Rakdos</td>
        <td>Midrange</td>
        <td data-sort="20230722">2023-07-22</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Sanctuary PDH II</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20230722">2023-07-22</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH II</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230722">2023-07-22</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH II</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230722">2023-07-22</td>
    </tr>
    

    <tr>
        <td><a href="https://www.moxfield.com/decks/d3s7EXKyeEmy1A2livtmHQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Vizkopa Guildmage</td>
        <td>RIW I</td>
        <td>Scarecrow1779</td>
        <td>Orzhov</td>
        <td>Combo</td>
        <td data-sort="20230624">2023-06-24</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>RIW I</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230624">2023-06-24</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>RIW I</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230624">2023-06-24</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/z1x2c3v4b5n6m7a8s9d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Murmuring Mystic</td>
        <td>RIW I</td>
        <td>Lobbert</td>
        <td>Mono U</td>
        <td>Control</td>
        <td data-sort="20230624">2023-06-24</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause II</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230520">2023-05-20</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>Common Cause II</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20230520">2023-05-20</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/z1x2c3v4b5n6m7a8s9d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Murmuring Mystic</td>
        <td>Common Cause II</td>
        <td>Lobbert</td>
        <td>Mono U</td>
        <td>Control</td>
        <td data-sort="20230520">2023-05-20</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Common Cause II</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20230520">2023-05-20</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/m9n8b7v6c5x4z3a2s1d0" target="_blank" class="btn-decklist">View</a></td>
        <td>Ghost of Ramirez DePietro + Armix, Filigree Thrasher</td>
        <td>Sanctuary PDH I</td>
        <td>Julian</td>
        <td>Dimir</td>
        <td>Midrange</td>
        <td data-sort="20230506">2023-05-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Sanctuary PDH I</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230506">2023-05-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Sanctuary PDH I</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20230506">2023-05-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>Sanctuary PDH I</td>
        <td>Zack</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20230506">2023-05-06</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Cloudy Commons II</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230415">2023-04-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Cloudy Commons II</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20230415">2023-04-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Cloudy Commons II</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230415">2023-04-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Cloudy Commons II</td>
        <td>Crash</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20230415">2023-04-15</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/d3s7EXKyeEmy1A2livtmHQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Vizkopa Guildmage</td>
        <td>Riches to Rags II</td>
        <td>Dylan A</td>
        <td>Orzhov</td>
        <td>Combo</td>
        <td data-sort="20230312">2023-03-12</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Riches to Rags II</td>
        <td>Crash</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20230312">2023-03-12</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Riches to Rags II</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230312">2023-03-12</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Riches to Rags II</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20230312">2023-03-12</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/t8yU5m2n1o9p4q7r3s6T" target="_blank" class="btn-decklist">View</a></td>
        <td>Soul of Migration</td>
        <td>Common Cause I</td>
        <td>Scarecrow1779</td>
        <td>Azorius</td>
        <td>Midrange</td>
        <td data-sort="20230218">2023-02-18</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause I</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230218">2023-02-18</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Common Cause I</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230218">2023-02-18</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/x5c6v7b8n9m0a1s2d3f4" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>Common Cause I</td>
        <td>Zack</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20230218">2023-02-18</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/b7c8n9m0a1s2d3f4g5h6" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Riches to Rags I</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20230101">2023-01-01</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g2h3j4k5l6m7n8b9v0c1" target="_blank" class="btn-decklist">View</a></td>
        <td>Mayhem Devil</td>
        <td>Riches to Rags I</td>
        <td>Julian</td>
        <td>Rakdos</td>
        <td>Midrange</td>
        <td data-sort="20230101">2023-01-01</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/g6hJ7k8l9m0n1o2p3q4R" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Riches to Rags I</td>
        <td>Flicker729</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230101">2023-01-01</td>
    </tr>
    

    <tr>
        <td><a href="https://moxfield.com/decks/q7w8e9r0t1y2u3i4o5p6" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Agent of the Iron Throne</td>
        <td>Riches to Rags I</td>
        <td>Dylan A</td>
        <td>Rakdos</td>
        <td>Aggro</td>
        <td data-sort="20230101">2023-01-01</td>
    </tr>
    
        </tbody>
    </table>
</div>

<script src="https://code.jquery.com/jquery-3.7.0.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.js"></script>
<script src="https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js"></script>

<script>
    $(document).ready(function() {
        $('#libraryTable').DataTable({
            responsive: true,
            pageLength: 25,
            order: [[ 6, "desc" ]], // Sort by Date (Column Index 6) descending by default
            columnDefs: [
                { type: 'date', targets: 6 } // Ensure Date column is treated as date
            ],
            language: {
                search: "Search Library:"
            }
        });
    });
</script>

<hr style="margin: 3em 0;">

<div style="text-align: center; margin-bottom: 4em;">
  <h3>Explore Deeper</h3>
  
  <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px;">
    
    <a href="{{ '/meta/top10timeline/' | relative_url }}" class="btn btn--primary btn--large">📈 Historical Top 10</a>

    <a href="{{ '/meta/seeyourstats/' | relative_url }}" class="btn btn--primary btn--large">🔎 See Your Stats</a>

    <a href="{{ '/meta/' | relative_url }}" class="btn btn--inverse btn--large">↩ Back to Meta</a>
    
  </div>
</div>