---
title: "Decklist Library"
layout: splash
permalink: /library/
classes: wide
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
---

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.css">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css">

<style>

  /* In your <style> block */
.page__content, .wrapper {
    max-width: 100% !important;
    padding-right: 2em; /* Add breathing room */
    padding-left: 2em;
}
    /* --- 1. LAYOUT & WIDTH FIXES --- */
    
    /* Force the main content area to be full width if the theme restricts it */
    .page__content {
        max-width: 100% !important;
        width: 100% !important;
        padding-right: 0 !important;
        padding-left: 0 !important;
    }

    .library-container {
        width: 100%;
        margin: 0 auto;
        display: block;
    }

    /* Ensure DataTables Wrapper fills the container */
    .dataTables_wrapper {
        width: 100% !important;
        margin: 0 auto;
    }

    /* --- 2. TABLE STYLING (Dark Mode) --- */
    #libraryTable {
        width: 100% !important;
        background-color: #2d2d2d;
        color: #e0e0e0;
        border-collapse: collapse;
        font-size: 0.95em;
        border-radius: 8px; /* Rounded corners for the table itself */
        overflow: hidden;
    }

    /* Header Styling */
    #libraryTable thead th {
        background-color: #1a1a1a;
        color: #ffffff;
        border-bottom: 2px solid #555;
        text-align: left;
        padding: 12px 10px;
    }

    /* Filter Row Styling (The inputs/dropdowns) */
    .filter-row th {
        background-color: #252525 !important;
        padding: 5px !important;
    }
    
    /* Styling the Dropdowns and Search Boxes */
    .column-search-select, .column-search-input {
        width: 100%;
        padding: 4px;
        background-color: #444;
        border: 1px solid #666;
        color: #fff;
        border-radius: 4px;
        font-size: 0.85em;
    }

    /* Row Styling */
    #libraryTable tbody tr {
        background-color: #2d2d2d !important;
        border-bottom: 1px solid #444;
    }
    #libraryTable tbody tr:hover {
        background-color: #383838 !important;
    }
    #libraryTable tbody td {
        padding: 10px;
        vertical-align: middle;
    }

    /* --- 3. BUTTONS & CONTROLS --- */
    .btn-decklist {
        display: inline-block;
        padding: 5px 12px;
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

    /* DataTables Interface Coloring */
    .dataTables_wrapper .dataTables_length, 
    .dataTables_wrapper .dataTables_filter, 
    .dataTables_wrapper .dataTables_info, 
    .dataTables_wrapper .dataTables_paginate {
        color: #e0e0e0 !important;
        margin-bottom: 10px;
        margin-top: 10px;
    }
    
    /* Search Box Input Field */
    .dataTables_filter input {
        background-color: #444;
        border: 1px solid #666;
        color: #fff;
        border-radius: 4px;
        padding: 5px;
    }

    /* Pagination Buttons */
    .dataTables_wrapper .dataTables_paginate .paginate_button {
        color: #e0e0e0 !important;
    }
    .dataTables_wrapper .dataTables_paginate .paginate_button.current {
        background: #555 !important;
        border-color: #777 !important;
        color: #fff !important;
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
                <th data-priority="5">Identity</th> <th data-priority="4">Strategy</th> <th data-priority="6">Date</th>
            </tr>
            </thead>
        <tbody>
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
        <td><a href="https://topdeck.gg/deck/cpdh-commander-clash-2025/xA5c35JHdoefe1dH5RRJMPIerCG2" target="_blank" class="btn-decklist">View</a></td>
        <td>The Emperor of Palamecia // The Lord Master of Hell</td>
        <td>Commander Clash 2025</td>
        <td>Russell  Harder</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20251213">2025-12-13</td>
    </tr>
    <tr>
        <td><a href="https://topdeck.gg/deck/cpdh-commander-clash-2025/RF01KBbpm5h2JMkwqdzbDuLWKo12" target="_blank" class="btn-decklist">View</a></td>
        <td>Veteran Beastrider</td>
        <td>Commander Clash 2025</td>
        <td>Scarecrow1779</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20251213">2025-12-13</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/CR0NHcwhUESrTax5qO2sJA" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Keskit, the Flesh Sculptor</td>
        <td>AllThatGames I</td>
        <td>Nathan Haiser</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20251019">2025-10-19</td>
    </tr>
    <tr>
        <td><a href="https://topdeck.gg/deck/free-pauper-commander-tournament/UY3rayeh6UhzYDlIPUr0F1FVwyc2" target="_blank" class="btn-decklist">View</a></td>
        <td>Honest Rutstein</td>
        <td>AllThatGames I</td>
        <td>Brandon White</td>
        <td>Golgari</td>
        <td>Midrange</td>
        <td data-sort="20251019">2025-10-19</td>
    </tr>
    <tr>
        <td><a href="https://topdeck.gg/deck/free-pauper-commander-tournament/kB0YyPVCo8XWy4sVeZ3m3Wje98k1" target="_blank" class="btn-decklist">View</a></td>
        <td>Lagrella, the Magpie</td>
        <td>AllThatGames I</td>
        <td>Robby Hatmaker</td>
        <td>Bant</td>
        <td>Combo</td>
        <td data-sort="20251019">2025-10-19</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/9NynA609AkWFdJim94kKNg" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>Cloudy Commons II</td>
        <td>Josh Mattson</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20251004">2025-10-04</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/a6QRhLaha0-ZipO9E-ZBEQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Kediss, Emberclaw Familiar + Malcolm, Keen-Eyed Navigator</td>
        <td>Cloudy Commons II</td>
        <td>Justin McNamara</td>
        <td>Izzet</td>
        <td>Combo</td>
        <td data-sort="20251004">2025-10-04</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/abaRtSFfKEyuX5POke7MRA" target="_blank" class="btn-decklist">View</a></td>
        <td>Shao Jun</td>
        <td>Cloudy Commons II</td>
        <td>Patrick Kramper</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20251004">2025-10-04</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/M3p9X9kVNUy7ZGhfQmeyQg" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>Cloudy Commons II</td>
        <td>Jaeden Woltjer</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20251004">2025-10-04</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/NnC5pANZI0SnuysrAvyOuw" target="_blank" class="btn-decklist">View</a></td>
        <td>Disciple of Deceit</td>
        <td>Common Cause IX</td>
        <td>Dukeslayer</td>
        <td>Dimir</td>
        <td>Combo</td>
        <td data-sort="20250816">2025-08-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/2--Ih4wTPkKJ8nxPnNSEnQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Imoen, Mystic Trickster + Criminal Past</td>
        <td>Common Cause IX</td>
        <td>southlakesvibes</td>
        <td>Dimir</td>
        <td>Midrange</td>
        <td data-sort="20250816">2025-08-16</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/rXJ5AkJA8EeDC6MLE6vwiw" target="_blank" class="btn-decklist">View</a></td>
        <td>Mystic Enforcer</td>
        <td>Common Cause IX</td>
        <td>BeachBodGod69</td>
        <td>Selesnya</td>
        <td>Voltron</td>
        <td data-sort="20250816">2025-08-16</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/EQeyjAlsNESZzB6rboqgDg" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Common Cause IX</td>
        <td>PapaPauper</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20250816">2025-08-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/xvyNpNC6A0aPNqMRGTLK9w" target="_blank" class="btn-decklist">View</a></td>
        <td>Lazav, Familiar Stranger</td>
        <td>Cloudy Commons I</td>
        <td>Joshua Mattson</td>
        <td>Dimir</td>
        <td>Voltron</td>
        <td data-sort="20250517">2025-05-17</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/mWP7zKIjXEOeylb-X-0jJg" target="_blank" class="btn-decklist">View</a></td>
        <td>Young Pyromancer</td>
        <td>Cloudy Commons I</td>
        <td>Peter Young</td>
        <td>Red</td>
        <td>Aggro</td>
        <td data-sort="20250517">2025-05-17</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/aUJ-X8ltOkmbEdZSmKQ3zQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Ley Weaver + Lore Weaver</td>
        <td>Common Cause VIII</td>
        <td>Clay</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20250322">2025-03-22</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/8JCLvQyWSEmV6wtnaA4qrQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Ley Weaver + Lore Weaver</td>
        <td>Common Cause VIII</td>
        <td>Bfine</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20250322">2025-03-22</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/YPbNuTKcLU24gZ7Z-uhzvA" target="_blank" class="btn-decklist">View</a></td>
        <td>Shao Jun</td>
        <td>Common Cause VIII</td>
        <td>Alkadron</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20250322">2025-03-22</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/BW8_OJXw70KLvJstGhfTDQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Skirmish Rhino</td>
        <td>Common Cause VIII</td>
        <td>DrSefLeaf</td>
        <td>Abzan</td>
        <td>Combo</td>
        <td data-sort="20250322">2025-03-22</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/hAo1bvF2LUaGP1j0hyHzHg" target="_blank" class="btn-decklist">View</a></td>
        <td>Disciple of Deceit</td>
        <td>Riches to Rags V</td>
        <td>Alex Tong</td>
        <td>Dimir</td>
        <td>Combo</td>
        <td data-sort="20250316">2025-03-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/wpRRrpJJdEWczwF6S_PlUA" target="_blank" class="btn-decklist">View</a></td>
        <td>Knotvine Mystic</td>
        <td>Riches to Rags V</td>
        <td>Scot Wiley</td>
        <td>Naya</td>
        <td>Midrange</td>
        <td data-sort="20250316">2025-03-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/XF_kbWFhXEC_u6i5p8spWA" target="_blank" class="btn-decklist">View</a></td>
        <td>Oji, the Exquisite Blade</td>
        <td>Riches to Rags V</td>
        <td>Stephanie Snow Da Cruz</td>
        <td>Azorius</td>
        <td>Midrange</td>
        <td data-sort="20250316">2025-03-16</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/H5YMtjnOPEGW6AcxlO_TIQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Third Path Iconoclast</td>
        <td>Riches to Rags V</td>
        <td>Ross Berkowitz</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20250316">2025-03-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/hSNg0sbuS0mlxLfeE8bUlA" target="_blank" class="btn-decklist">View</a></td>
        <td>Bilbo, Retired Burglar</td>
        <td>Sanctuary PDH VIII</td>
        <td>Ginger Persolus</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20250215">2025-02-15</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/ldWBKTilHEStYfnztmdI_Q" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Keskit, the Flesh Sculptor</td>
        <td>Sanctuary PDH VIII</td>
        <td>Xrlylyl</td>
        <td>Rakdos</td>
        <td>Combo</td>
        <td data-sort="20250215">2025-02-15</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/EBN9baXZ1E64jJWf05OvQw" target="_blank" class="btn-decklist">View</a></td>
        <td>Gut, True Soul Zealot + Inspiring Leader</td>
        <td>Sanctuary PDH VIII</td>
        <td>Aaron</td>
        <td>Boros</td>
        <td>Aggro</td>
        <td data-sort="20250215">2025-02-15</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/1LCewKgqSEyu1INcOGAA0A" target="_blank" class="btn-decklist">View</a></td>
        <td>Heartfire Hero</td>
        <td>Common Cause VII</td>
        <td>PurplePenguinJo</td>
        <td>Red</td>
        <td>Aggro</td>
        <td data-sort="20250125">2025-01-25</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/1CGT-HOhdEymjFyFGAcOeg" target="_blank" class="btn-decklist">View</a></td>
        <td>Horrid Shadowspinner</td>
        <td>Common Cause VII</td>
        <td>GatorbaitTV</td>
        <td>Dimir</td>
        <td>Combo</td>
        <td data-sort="20250125">2025-01-25</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/jWnufsB3SEuXFXfUjszZ3g" target="_blank" class="btn-decklist">View</a></td>
        <td>Zada, Hedron Grinder</td>
        <td>Common Cause VII</td>
        <td>Stein</td>
        <td>Red</td>
        <td>Aggro</td>
        <td data-sort="20250125">2025-01-25</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/-67pN4-VfUyLlyVEAF8Hag" target="_blank" class="btn-decklist">View</a></td>
        <td>Trygon Prime</td>
        <td>Dragon Master Games I</td>
        <td>William Harder</td>
        <td>Simic</td>
        <td>Midrange</td>
        <td data-sort="20241123">2024-11-23</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/Yr_wtHangUq7Lmhlli4fMw" target="_blank" class="btn-decklist">View</a></td>
        <td>Abdel Adrian, Gorion’s Ward + Agent of the Iron Throne</td>
        <td>Common Cause VI</td>
        <td>uyokonoyami</td>
        <td>Orzhov</td>
        <td>Combo</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/bl8xsbwTsU-J0s1UZULYiQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Abdel Adrian, Gorion’s Ward + Sword Coast Sailor</td>
        <td>Common Cause VI</td>
        <td>PurplePenguinJo</td>
        <td>Azorius</td>
        <td>Combo</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/NtDtHwhfF0WqVqEuaZ7EfA" target="_blank" class="btn-decklist">View</a></td>
        <td>Diviner Spirit</td>
        <td>Common Cause VI</td>
        <td>Brewbear</td>
        <td>Blue</td>
        <td>Voltron</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/eYZSyMKhK0u5XlNsbnanug" target="_blank" class="btn-decklist">View</a></td>
        <td>Hollow Marauder</td>
        <td>Common Cause VI</td>
        <td>PapaPauper</td>
        <td>Black</td>
        <td>Control</td>
        <td data-sort="20241109">2024-11-09</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/ZUMlxGM5EEWu4gFtX-TzGg" target="_blank" class="btn-decklist">View</a></td>
        <td>Abdel Adrian, Gorion’s Ward + Agent of the Iron Throne</td>
        <td>The Pauper Pit I</td>
        <td>Heartless</td>
        <td>Orzhov</td>
        <td>Combo</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/PZI5L9zmCEuOBznPDzrqJQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Arabella, Abandoned Doll</td>
        <td>The Pauper Pit I</td>
        <td>Shakur W</td>
        <td>Boros</td>
        <td>Aggro</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/UAIeiIOWok--5rpoi7kCrA" target="_blank" class="btn-decklist">View</a></td>
        <td>Glaring Fleshraker</td>
        <td>The Pauper Pit I</td>
        <td>Kevin R</td>
        <td>Colorless</td>
        <td>Combo</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/7Jzp4PEWdU6iYRpDi9_GDQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Tatyova, Benthic Druid</td>
        <td>The Pauper Pit I</td>
        <td>Roman N</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240928">2024-09-28</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/ROR3Ll-bVU6L06KlOwZc2g" target="_blank" class="btn-decklist">View</a></td>
        <td>Breeches, Brazen Plunderer + Malcolm, Keen-Eyed Navigator</td>
        <td>Common Cause V</td>
        <td>Kunx</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20240831">2024-08-31</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/Sv5hMA-I806ArpyKom7AAg" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Kediss, Emberclaw Familiar</td>
        <td>Common Cause V</td>
        <td>Aaron</td>
        <td>Red</td>
        <td>Aggro</td>
        <td data-sort="20240831">2024-08-31</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/1sDi-9JZoEq9A7HFL4XegA" target="_blank" class="btn-decklist">View</a></td>
        <td>Risen Reef</td>
        <td>RIW II</td>
        <td>Alex MM</td>
        <td>Simic</td>
        <td>Midrange</td>
        <td data-sort="20240727">2024-07-27</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/gt_j26k5Q0CDujwAIi92_A" target="_blank" class="btn-decklist">View</a></td>
        <td>Vhal, Candlekeep Researcher + Agent of the Shadow Thieves</td>
        <td>RIW II</td>
        <td>TonisBolognis</td>
        <td>Dimir</td>
        <td>Combo</td>
        <td data-sort="20240727">2024-07-27</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/tVgoCMX4C0yfHxDL7RpNAw" target="_blank" class="btn-decklist">View</a></td>
        <td>Wilson, Refined Grizzly + Far Traveler</td>
        <td>RIW II</td>
        <td>HiveCryptid</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20240727">2024-07-27</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/Pu_fVLvYLUOxUfM6srUkow" target="_blank" class="btn-decklist">View</a></td>
        <td>Breeches, Brazen Plunderer + Malcolm, Keen-Eyed Navigator</td>
        <td>Sanctuary PDH VI</td>
        <td>Nolan S</td>
        <td>Izzet</td>
        <td>Midrange</td>
        <td data-sort="20240720">2024-07-20</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/9tGroGXxD0Gy0WDQ6mTLxA" target="_blank" class="btn-decklist">View</a></td>
        <td>Kutzil, Malamet Exemplar</td>
        <td>Sanctuary PDH VI</td>
        <td>Seraphiel</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20240720">2024-07-20</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/n04JVHmojkKKJTU85rjwwQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Ley Weaver + Lore Weaver</td>
        <td>Sanctuary PDH VI</td>
        <td>GatorbaitTV</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240720">2024-07-20</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/ptDs_HP6mEyOJENDj2mE_A" target="_blank" class="btn-decklist">View</a></td>
        <td>Rilsa Rael, Kingpin</td>
        <td>Sanctuary PDH VI</td>
        <td>budyfish</td>
        <td>Dimir</td>
        <td>Midrange</td>
        <td data-sort="20240720">2024-07-20</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/IaiX4ShuMUydmcxniMzCUg" target="_blank" class="btn-decklist">View</a></td>
        <td>Gilanra, Caller of Wirewood + Numa, Joraga Chieftain</td>
        <td>Common Cause IV</td>
        <td>southlakesvibes</td>
        <td>Green</td>
        <td>Midrange</td>
        <td data-sort="20240622">2024-06-22</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/hyOgwcLUbE6OX8VRYkhttg" target="_blank" class="btn-decklist">View</a></td>
        <td>Lumberknot</td>
        <td>Common Cause IV</td>
        <td>Brewbear</td>
        <td>Green</td>
        <td>Midrange</td>
        <td data-sort="20240622">2024-06-22</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/fYZKUOMj_EqeNMCvH5leww" target="_blank" class="btn-decklist">View</a></td>
        <td>Sphinx Summoner</td>
        <td>Common Cause IV</td>
        <td>Lobbert</td>
        <td>Dimir</td>
        <td>Combo</td>
        <td data-sort="20240622">2024-06-22</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/C2SPUw5rCEGYqyJnQ6nnqw?ut" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>Sanctuary PDH V</td>
        <td>karnatheon</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240518">2024-05-18</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/sxzp3LVZT0mKm_WLaykXuQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>Sanctuary PDH V</td>
        <td>Xrlylyl</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240518">2024-05-18</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/MY6Wv-mWnUmFwDSoAiv13Q" target="_blank" class="btn-decklist">View</a></td>
        <td>Lorehold Apprentice</td>
        <td>Common Cause III</td>
        <td>Ankylosaur</td>
        <td>Boros</td>
        <td>Midrange</td>
        <td data-sort="20240427">2024-04-27</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/LC5EhCv4W0-l34IyF8oxzg" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>Riches to Rags IV</td>
        <td>William S</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240407">2024-04-07</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/8XK59D5RmUKlgrK_H4EkcA" target="_blank" class="btn-decklist">View</a></td>
        <td>Patchwork Automaton</td>
        <td>Riches to Rags IV</td>
        <td>Kevin R</td>
        <td>Colorless</td>
        <td>Voltron</td>
        <td data-sort="20240407">2024-04-07</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/HMve6vBIIk-QyT7_D_vxbA" target="_blank" class="btn-decklist">View</a></td>
        <td>Fynn, the Fangbearer</td>
        <td>PDH Tourney - Mainberg I</td>
        <td>Timo</td>
        <td>Green</td>
        <td>Aggro</td>
        <td data-sort="20240323">2024-03-23</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/kPEgKbFNe0yZPXp5D0sB_A" target="_blank" class="btn-decklist">View</a></td>
        <td>Ghost of Ramirez DePietro + Tormod, the Desecrator</td>
        <td>PDH Tourney - Mainberg I</td>
        <td>Chris S</td>
        <td>Dimir</td>
        <td>Control</td>
        <td data-sort="20240323">2024-03-23</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/S134dNSTy0SiFND5610K2Q" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>Sanctuary PDH IV</td>
        <td>BrayBu</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20240316">2024-03-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/j1S3GhgWPkixFyvOXYYBVA" target="_blank" class="btn-decklist">View</a></td>
        <td>Kediss, Emberclaw Familiar + Malcolm, Keen-Eyed Navigator</td>
        <td>Sanctuary PDH IV</td>
        <td>Ankylosaur</td>
        <td>Izzet</td>
        <td>Combo</td>
        <td data-sort="20240316">2024-03-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/wIJvB0XAfUeRsyK_DRVqoA" target="_blank" class="btn-decklist">View</a></td>
        <td>Syr Konrad, the Grim</td>
        <td>Sanctuary PDH IV</td>
        <td>Aaron</td>
        <td>Black</td>
        <td>Control</td>
        <td data-sort="20240316">2024-03-16</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/tmMplRiiQU6p6DzssHzy2g" target="_blank" class="btn-decklist">View</a></td>
        <td>Scholar of the Ages</td>
        <td>Common Cause II</td>
        <td>MizuSun</td>
        <td>Blue</td>
        <td>Combo</td>
        <td data-sort="20240210">2024-02-10</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/AIn0u7bqc06raB-75tkLCg" target="_blank" class="btn-decklist">View</a></td>
        <td>Sivriss, Nightmare Speaker + Cloakwood Hermit</td>
        <td>Goblin's Heist I</td>
        <td>Slyns</td>
        <td>Golgari</td>
        <td>Midrange</td>
        <td data-sort="20231221">2023-12-21</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/ypO7zk3rckmOdaMUppAN-A" target="_blank" class="btn-decklist">View</a></td>
        <td>Terravore</td>
        <td>Goblin's Heist I</td>
        <td>Tim U</td>
        <td>Green</td>
        <td>Midrange</td>
        <td data-sort="20231221">2023-12-21</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/an986JYA4ESWsy5iCtty1Q" target="_blank" class="btn-decklist">View</a></td>
        <td>Cadira, Caller of the Small</td>
        <td>Common Cause I</td>
        <td>Raevimati</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20231111">2023-11-11</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/f2Pyemv2zk-uGi5atTXG4w" target="_blank" class="btn-decklist">View</a></td>
        <td>Cyberman Patrol</td>
        <td>Common Cause I</td>
        <td>KatieCombat</td>
        <td>Colorless</td>
        <td>Midrange</td>
        <td data-sort="20231111">2023-11-11</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/ufYjl-QfH0uvY-EugYNhAg" target="_blank" class="btn-decklist">View</a></td>
        <td>Loyal Apprentice</td>
        <td>Common Cause I</td>
        <td>Obstinate</td>
        <td>Red</td>
        <td>Aggro</td>
        <td data-sort="20231111">2023-11-11</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/ADy_WV-dlE2BVObDpDZBOQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Teshar, Ancestor’s Apostle</td>
        <td>Common Cause I</td>
        <td>Jorbilicious</td>
        <td>White</td>
        <td>Combo</td>
        <td data-sort="20231111">2023-11-11</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/gobW0aiqQUGidavyGyw7_Q" target="_blank" class="btn-decklist">View</a></td>
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
        <td><a href="https://moxfield.com/decks/oXbkSrbw1kKMnHJDnhNF3g" target="_blank" class="btn-decklist">View</a></td>
        <td>Kediss, Emberclaw Familiar + Malcolm, Keen-Eyed Navigator</td>
        <td>Sanctuary PDH III</td>
        <td>GatorbaitTV</td>
        <td>Izzet</td>
        <td>Combo</td>
        <td data-sort="20231104">2023-11-04</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/SaKWDQYvmE6iEsHJ_WJzpg" target="_blank" class="btn-decklist">View</a></td>
        <td>Satyr Enchanter</td>
        <td>Sanctuary PDH III</td>
        <td>Ankylosaur</td>
        <td>Selesnya</td>
        <td>Midrange</td>
        <td data-sort="20231104">2023-11-04</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/ONYzU8zGnE-vGql05-3KqQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Erinis, Gloom Stalker + Street Urchin</td>
        <td>RIW I</td>
        <td>Ankylosaur</td>
        <td>Gruul</td>
        <td>Control</td>
        <td data-sort="20230624">2023-06-24</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/mkvjgoEQwEanpo6EdAwuqQ" target="_blank" class="btn-decklist">View</a></td>
        <td>Sprite Dragon</td>
        <td>RIW I</td>
        <td>Jackson S</td>
        <td>Izzet</td>
        <td>Voltron</td>
        <td data-sort="20230624">2023-06-24</td>
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
        <td><a href="https://www.moxfield.com/decks/VXn-nHJHCki5mCQHIX32Xg" target="_blank" class="btn-decklist">View</a></td>
        <td>Dargo, the Shipwrecker + Malcolm, Keen-Eyed Navigator</td>
        <td>Sanctuary PDH I</td>
        <td>Clay</td>
        <td>Izzet</td>
        <td>Combo</td>
        <td data-sort="20230513">2023-05-13</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/BB45YbVrg06lj3Fc9C4C-w" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>Sanctuary PDH I</td>
        <td>rusty_fuchs</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20230513">2023-05-13</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/qp8i-fp01EOlRfSc4qXH0Q" target="_blank" class="btn-decklist">View</a></td>
        <td>Gretchen Titchwillow</td>
        <td>Riches to Rags II</td>
        <td>Bfine</td>
        <td>Simic</td>
        <td>Combo</td>
        <td data-sort="20230312">2023-03-12</td>
    </tr>
    <tr>
        <td><a href="https://moxfield.com/decks/GMJDy-NfwUOyVfXqLCxtnw" target="_blank" class="btn-decklist">View</a></td>
        <td>Vizkopa Guildmage</td>
        <td>Riches to Rags II</td>
        <td>Dylan A</td>
        <td>Orzhov</td>
        <td>Combo</td>
        <td data-sort="20230312">2023-03-12</td>
    </tr>
    <tr>
        <td><a href="https://www.moxfield.com/decks/8Y8epCv_fk2Xd4ddYIdANw" target="_blank" class="btn-decklist">View</a></td>
        <td>Juri, Master of the Revue</td>
        <td>Riches to Rags I</td>
        <td>Jacob Paris</td>
        <td>Rakdos</td>
        <td>Midrange</td>
        <td data-sort="20221031">2022-10-31</td>
    </tr>
</tbody>
    </table>
</div>

<script src="https://code.jquery.com/jquery-3.7.0.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.js"></script>
<script src="https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js"></script>

<script>
    $(document).ready(function() {
        // Clone the header row to create the input row
        $('#libraryTable thead tr')
            .clone(true)
            .addClass('filter-row')
            .appendTo('#libraryTable thead');

        $('#libraryTable').DataTable({
            responsive: true,
            pageLength: 25,
            order: [[ 6, "desc" ]], // Default Sort: Date
            columnDefs: [
                { type: 'date', targets: 6 },
                { orderable: false, targets: 0 } // Disable sorting on the "Link" column
            ],
            language: {
                search: "_INPUT_",
                searchPlaceholder: "Search all columns..."
            },
            
            // Logic to create Dropdowns for specific columns
            initComplete: function () {
                var api = this.api();

                // For each column in the second header row
                api.columns().every(function (colIdx) {
                    var column = this;
                    var headerCell = $('.filter-row th').eq(column.index());
                    var title = $(headerCell).text();

                    // CLEAR existing text in the filter row
                    headerCell.empty();

                    // 1. If it's the Identity (4) or Strategy (5) column -> Create Dropdown
                    if (colIdx === 4 || colIdx === 5) {
                        var select = $('<select class="column-search-select"><option value="">All ' + title + '</option></select>')
                            .appendTo(headerCell)
                            .on('change', function () {
                                var val = $.fn.dataTable.util.escapeRegex($(this).val());
                                column.search(val ? '^' + val + '$' : '', true, false).draw();
                            });

                        // Populate the dropdown with unique values from the column data
                        column.data().unique().sort().each(function (d, j) {
                            // Strip HTML tags if necessary, though simpler is better
                            var textContent = $('<div>').html(d).text(); 
                            select.append('<option value="' + textContent + '">' + textContent + '</option>');
                        });
                    } 
                    // 2. If it's Date, Link, or others -> Leave empty or add text input?
                    // Let's leave Link (0) and Date (6) empty to keep it clean.
                    // Let's add text search for Commander (1), Event (2), Player (3)
                    else if (colIdx === 1 || colIdx === 2 || colIdx === 3) {
                         var input = $('<input type="text" placeholder="Filter..." class="column-search-input" />')
                            .appendTo(headerCell)
                            .on('keyup change clear', function () {
                                if (column.search() !== this.value) {
                                    column.search(this.value).draw();
                                }
                            });
                    }
                });
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