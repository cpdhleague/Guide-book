---
# ===========================================================================
# CPDH.GUIDE — ARTICLE TEMPLATE
# ===========================================================================

title: "Sailors' Bane - cPDH Deck Tech"

# DATE: Must be today or earlier while in _previews/ — Jekyll will not build
# future-dated documents, and the preview will 404.
# REAL PUBLISH DATE IS 2026-11-20 (two Fridays out). Set date back to
# 2026-11-20 when you move this file into _posts/. The filename already
# carries 11-20, so the post URL will not shift.
date: 2026-11-10

layout: splash
classes: wide

# ===========================================================================
# SECTION 1: WHO & WHAT
# ===========================================================================

creator: guide
author: ginger

categories:
  - cPDH Deck Techs

# ===========================================================================
# SECTION 2: DISPLAY CONTROLS
# ===========================================================================

front_page: true
hidden: false
archive_only: false
gnews: false

# ===========================================================================
# SECTION 3: IMAGES
# ===========================================================================
# TODO: Replace placeholder with a real image once available.

image: /assets/images/sailors-bane-deck-tech.png

header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  teaser: /assets/images/sailors-bane-deck-tech.png

# ===========================================================================
# SECTION 4: EXCERPT
# ===========================================================================

excerpt: ""  # Required for GNews — fill this in before publishing to Google News

# ===========================================================================
# SECTION 5: REDDIT POSTING
# ===========================================================================
# reddit_text: ""  # Uncomment and fill in to enable Reddit posting

---

Shout out to [PapaPauper](https://moxfield.com/decks/kDiWDYZDrEu4zQ99L4G8pA) for pioneering this deck first. My version is about 20 cards off from his, and I want to recognize that all I did was refine his heavy lifting.

{% include card-grid.html cards="Sailors' Bane" %}

## Abstract

[[Sailors' Bane]] is a voltron-control deck that has spent time in the top 10 ranked pauper commanders on our [meta page](/meta/). It is fast, well protected, and resilient. The commander has even been banned in PDC (Pauper Duel Commander).

Because the commander needs so few cards to get set up, we can dedicate a huge proportion of the deck to countermagic and removal. Of the 99, I run 16 counterspells and 12 bounce spells. That is 28 cards of interaction in a deck whose win condition is one card in the command zone.

It is simple to pilot with no reduction in efficacy.

## What the Commander Does for Us

Sailors' Bane costs {7}{U}{U}, and it costs {1} less for each card you own in exile and in your graveyard that is an instant, a sorcery, or a card with an Adventure. The floor is {U}{U}. Three things fall out of that:

**The cost reduction counts exile as well as the graveyard.** 64 of my 99 cards are instants, sorceries, or Adventure cards, so the fuel is most of the deck. It also means graveyard hate does not shut us off the way it shuts off [[Cryptic Serpent]]. An opponent who exiles our yard has moved our fuel from one half of the counter to the other.

**Ward {4} is a lot of protection for a commander this cheap.** We do not need to spend slots on protection spells, and we do not need to play around removal the way a fragile voltron deck does. A player holding [[Snuff Out]] cannot touch the turtle and pay the ward before turn four.

**7 power is a real clock.** 7/7 means three connections per opponent, and a handful of our buffs cut that to two. The body also dodges most red removal.

Losing the turtle is low consequence. We cast it, we lose it, we cast it again. [[Opal Palace]] turns a recast into growth.

## Deck Composition

### 1. Mill

A fair number of cards in the deck are dedicated to self-mill up front, for the sake of casting the turtle on turn three. 14 cards fill the yard. Turn two is possible, but turn three is more common.

[[Foresight]] is one of my favorite cards to cast on turn two. It replaces itself, and it exiles three cards from our library at once — three fuel for the cost reduction in a single spell, while taking out mill cards we would not want to see from our deck. [[Tolarian Winds]] dumps our hand to reduce the cost. Some of the cards draw and discard instead of milling direct, which suits us the same.

{% include card-grid.html cards="Foresight; Tolarian Winds; Tome Scour; Stream of Thought; Careful Study; Shriekhorn" %}

### 2. Evasion & Buff

Once the turtle is on the board, we need small buffs on it to make it a two-turn kill and to get it through any blockers our opponents have started putting in our way. I run 13 of these.

The buffs matter more than they look. 7 power is three connections. Add 4 power and it becomes two, which is where the deck wants to be — [[Spectral Flight]] plus [[Cartouche of Knowledge]] gets there, and so does stacking a smaller buff onto an aura. [[Slip Through Space]] and [[Distortion Strike]] handle the blockers instead of the math.

{% include card-grid.html cards="Spectral Flight; Cartouche of Knowledge; One With the Wind; Distortion Strike; Maximize Altitude; Security Bypass" %}

### 3. Counterspells & Removal

We counter spells and we remove permanents that pose us problems or death. 16 counterspells and 12 bounce spells.

[[Logic Knot]] and [[Treasure Cruise]] both have delve, which turns the yard we built for the commander into mana. The cost reduction counts cards in exile too, so delving does not set our commander back a single turn — the cards move to exile and keep counting. That interaction is the reason both cards are in the deck.

{% include card-grid.html cards="Counterspell; Logic Knot; Memory Lapse; Muddle the Mixture; Echoing Truth; Snap" %}

## Opening Hands

Our number one priority is to get the commander out as soon as we can. Keep a hand with a clear path to casting Sailors' Bane on turn three, or, if you draw a hand with [[Gitaxian Probe]] or [[Snapback]], the enviable turn two cast.

The arithmetic behind that: a turn three cast with three lands wants six instants, sorceries, or Adventure cards between the yard and exile. Turn two with two lands wants seven. Probe and Snapback both cost no mana, so they move that counter without costing us a land drop.

The deck runs 26 lands — 24 Island plus [[Mystic Sanctuary]] and Opal Palace — against a curve of 25 one-drops and 32 two-drops, for an average mana value of 2.26. One-land hands are keepable when the card selection is there.

## Strategies

- Delve is good. Use the graveyard without fear of stranding the commander.
- We can lose the turtle and we can recast the turtle. The deck is resilient to graveyard hate.
- It protects itself, so we do not need to invest in protection.
- Kill your opponents one at a time. It may feel heartless, but it stops them developing resources to use against you later. Kill whoever poses the biggest threat to your eventual win.
- It takes about six landed attacks to win the table, so you have to think through how the game is going to unfold.
- A lot of your evaluation happens during the mulligan, before any player takes a turn — whether you hold more countermagic or more removal, and which of those gives you the advantage in controlling this table.

The deck can be easy to pilot, but at high levels it asks for forethought and an understanding of not just your own deck but the decks of your opponents. Which is how it goes with any control deck.

<a href="https://moxfield.com/decks/Hi-te6G4bkSFgr7dBicWEA" class="btn btn--primary btn--large" target="_blank" rel="noopener">View Moxfield List</a>

{% include deck-tech-cta.html %}
{% include author-card.html %}
{% include article-nav.html %}
