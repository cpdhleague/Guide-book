---
# ===========================================================================
# CPDH.GUIDE — ARTICLE TEMPLATE
# ===========================================================================
# HOW TO USE THIS FILE:
#   1. Copy this file into the _posts/ folder
#   2. Rename it: YYYY-MM-DD-short-title-slug.md
#      Example: 2026-06-10-deckbuilding-fundamentals.md
#   3. Fill in every field below (read the notes carefully)
#   4. Write your article content below the closing ---
#   5. Push to GitHub — the site rebuilds in 1-3 minutes
#
# YAML RULES (important):
#   - true/false values must NOT be in quotes
#   - Text values SHOULD be in quotes
#   - Indentation uses SPACES not tabs
#   - Lines starting with # are comments — Jekyll ignores them
# ===========================================================================


# ---------------------------------------------------------------------------
# TITLE
# ---------------------------------------------------------------------------
# The article headline. Make it specific, descriptive, and clickable.
# Appears on: the article page, homepage cards, /articles/ listings,
#             social sharing previews, and RSS feeds.
# Tips:
#   - Use Title Case
#   - Avoid ALL CAPS or clickbait
#   - Keep it under 70 characters where possible
#   - Do NOT use double quotes inside the title (use single quotes if needed)
# ---------------------------------------------------------------------------
title: "Brewing With JANK"


# ---------------------------------------------------------------------------
# DATE
# ---------------------------------------------------------------------------
# Publication date in YYYY-MM-DD format.
#
# PAST OR TODAY: Article publishes on next push to GitHub.
#
# FUTURE DATE — SCHEDULED PUBLISHING:
#   Set a future date to hold the article until that date.
#   A scheduled GitHub Action rebuilds the site daily at 6 AM UTC.
#   The article will appear automatically on (or just after) that date
#   without any further action from you.
#   Example: set date: 2026-07-04 today, push it, and it goes live
#   on the morning of July 4th with no further action needed.
#   Note: the article file must be in _posts/ and pushed to GitHub
#   before the target date — it won't publish from your local machine.
# ---------------------------------------------------------------------------
date: 2026-07-31


# ---------------------------------------------------------------------------
# LAYOUT & CLASSES — DO NOT CHANGE THESE
# ---------------------------------------------------------------------------
layout: splash
classes: wide


# ===========================================================================
# SECTION 1: WHO & WHAT
# ===========================================================================

# ---------------------------------------------------------------------------
# CREATOR
# ---------------------------------------------------------------------------
# Which content stream produced this article. Used by:
#   - The homepage (limits PDHpod and Jalapenos to 1 slot each)
#   - The "More from..." filter on /articles/?creator=X
# Choose EXACTLY ONE of these values (no quotes needed):
#   guide      — written by the CPDH.guide team
#   pdhpod     — produced by The PDH Pod
#   jalapenos  — produced by the Jalapeno Paupers
# ---------------------------------------------------------------------------
creator: guide


# ---------------------------------------------------------------------------
# AUTHOR
# ---------------------------------------------------------------------------
# Who wrote or produced this specific piece. Controls the author card
# displayed at the bottom of the article.
#
# Two options:
#   Option A — Known author (has a profile in _data/authors.yml):
#              author: gingerpersolus
#              Use the exact key from authors.yml (lowercase, no spaces)
#              This shows the full card: photo + bio + links + "More from" button
#
#   Option B — Guest author (no profile in authors.yml):
#              author: "First Last"
#              Put their name in quotes with a capital letter and a space
#              This shows a name-only card: "Content by First Last"
#
# Leave this field out entirely to show NO author card.
#
# Current authors in _data/authors.yml:
#   ginger, beachbodgod69, pdhpod, jalapenos
#   (Add new authors to that file before using their key here)
# ---------------------------------------------------------------------------
author: magusofthejank


# ---------------------------------------------------------------------------
# CATEGORIES
# ---------------------------------------------------------------------------
# The topic category for this article. Used on the /articles/ page topic list.
# Choose EXACTLY ONE from this approved list:
#   - Game Guides          (strategy, mechanics, how-to)
#   - Deck Tech            (commander spotlight, decklist deep dives)
#   - Videos               (YouTube embeds, video content)
#   - Podcast              (PDHpod episodes — set automatically by the form)
#   - Community            (interviews, community highlights)
#   - Tournament Reports   (event recaps, standings, winner interviews)
#   - Events               (upcoming events, announcements)
# ---------------------------------------------------------------------------
categories:
  - Game Guides


# ===========================================================================
# SECTION 2: DISPLAY CONTROLS
# ===========================================================================
# These fields control WHERE this article appears across the site.
# All four should be present on every article.

# ---------------------------------------------------------------------------
# FRONT PAGE
# ---------------------------------------------------------------------------
# Should this article appear on the homepage?
#   true  — eligible for one of the 6 homepage slots
#   false — appears on /articles/ only, never on homepage
# Note: even with true, the homepage only shows the most recent PDHpod
# and Jalapenos article (1 each), so older ones won't show if newer exist.
# ---------------------------------------------------------------------------
front_page: true


# ---------------------------------------------------------------------------
# HIDDEN
# ---------------------------------------------------------------------------
# Hide this article from ALL listings (homepage, /articles/, RSS feeds).
# The article still exists and is accessible by direct URL.
#   false — normal, visible article (use this almost always)
#   true  — invisible in listings (use for drafts or unlisted content)
# ---------------------------------------------------------------------------
hidden: false


# ---------------------------------------------------------------------------
# ARCHIVE ONLY
# ---------------------------------------------------------------------------
# Show this article ONLY in its category archive, not on /articles/ or homepage.
# Use for older content, event recaps, or anything you want archived but
# not prominently featured in the main article feed.
#   false — appears everywhere normally (use this almost always)
#   true  — category archive only
# ---------------------------------------------------------------------------
archive_only: false


# ---------------------------------------------------------------------------
# GNEWS
# ---------------------------------------------------------------------------
# Include this article in the Google News RSS feed (/gnews.xml)?
# This feed is also watched by Reddit and Discord auto-posting.
#   false — site only, no external distribution
#   true  — included in RSS feed → Google News, Reddit, Discord
#
# IMPORTANT: If setting to true, you MUST fill in:
#   1. excerpt (required — feeds look broken without it)
#   2. A real image in both image: and header.teaser:
#   3. reddit_text (required if you want Reddit posting — see below)
#
# For PDHpod/Jalapenos submissions: this is set by the submission form.
# For guide articles: Patrik sets this manually after review.
# ---------------------------------------------------------------------------
gnews: false


# ===========================================================================
# SECTION 3: IMAGES
# ===========================================================================
# Three image fields serve different purposes. Ideally all three use the
# same well-composed 16:9 image. Use /assets/images/ for local files.
# File naming: lowercase, hyphens not spaces (my-image.jpg not My Image.jpg)

# IMAGE (top-level)
# Controls: Discord link previews, Reddit thumbnails, social sharing cards,
#           and the <og:image> meta tag that all social platforms read.
# This is the image people see when a link to this article is shared.
image: /assets/images/bwj-thumbnail.png

header:
  # OVERLAY IMAGE
  # The large banner displayed at the top of the article page itself.
  # Should be wide and high resolution (1200px+ wide recommended).
  # For most guide articles use the standard banner: header2025-1.png
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5    # Darkness of the overlay (0.0 = none, 1.0 = black)

  # TEASER
  # The thumbnail shown on the homepage cards and /articles/ listing grid.
  # Should be 16:9 ratio. Usually the same as the top-level image: above.
  teaser: /assets/images/bwj-thumbnail.png

# NOTE: For PDHpod articles, the image is always pdhpod.png (set automatically).
# For Jalapenos articles, the YouTube thumbnail is downloaded automatically.
# For guide articles, upload your image to assets/images/ and reference it here.


# ===========================================================================
# SECTION 4: EXCERPT
# ===========================================================================
# A short 1-2 sentence summary of the article.
# Appears on: homepage cards, /articles/ listing, RSS feeds, social previews,
#             Google News description field, Discord embeds.
#
# Rules:
#   - No markdown formatting (no **bold**, no [links], no #headers)
#   - No double quotes inside the excerpt (use single quotes if needed)
#   - Keep it under 160 characters for best results in feeds
#   - Write it as a standalone sentence — it appears without context
#
# REQUIRED if gnews: true — Google News and RSS feeds look broken without it.
# REQUIRED if front_page: true — homepage cards show this text.
# ---------------------------------------------------------------------------
excerpt: ""  # Required for GNews — fill this in before publishing to Google News


# ===========================================================================
# SECTION 5: REDDIT POSTING
# ===========================================================================
# Controls whether and how this article is posted to Reddit.
# Reddit posting only happens for articles where gnews: true AND
# reddit_text is present and non-empty.
#
# HOW IT WORKS:
#   - reddit_text present and filled → posts to r/pauperEDH and
#     r/competitivepauperedh as a link post, then adds this text as
#     a comment on that post to start discussion
#   - reddit_text absent OR empty → article is NOT posted to Reddit
#
# This is the complete on/off switch for Reddit. Remove the field entirely
# or leave it blank to prevent Reddit posting, no other changes needed.
#
# TEMPLATES by creator (copy and customise):
#
#   PDHpod episodes:
#     "🎧 New episode of the PDH Pod is live! Drop your thoughts
#      below — questions for the hosts? Tag u/alkadron!"
#
#   Jalapenos videos:
#     "🌶️ The Jalapenos dropped a new video! What do you think?
#      Any questions for the crew? Tag u/JalapenoPaupersMTG!"
#
#   Guide articles — write something specific to THIS article:
#     "We've been thinking about X a lot lately. What's your take?"
#     "This challenges the conventional wisdom on Y — agree or disagree?"
#     "Would love to hear what commanders you think belong in this tier."
#
# Note: For PDHpod and Jalapenos, the template text is applied automatically
# by the GitHub Action. You only need to fill this in for guide articles.
# ---------------------------------------------------------------------------
# reddit_text: ""  # Uncomment and fill in to enable Reddit posting

---
## Brewing With JANK
Hey, it's Ethan aka MagusoftheJank, Host of the Cloudy Commons Cup tournament series and prolific cPDH brewer. Today I'd like to talk to you a little bit about how I think about brewing a competitive deck, and introduce you to a method that you can hopefully also use to improve your own decks!

When you hear the word "Jank," it probably conjures images of fragile five card combos or unplayable bulk cards cobbled into an unsleeved pile that wins one in ten games. But what if "Jank" wasn't a descriptor for a bad deck? What if it was an acronym for an iterative deck engineering cycle designed to focus and optimize your list?

The JANK brewing method is a four-stage, continuous cycle designed to iteratively tune your deck towards peak performance. It guides you through answering critical questions about your list, backed by a competitive philosophy that you constantly refine with real world data and deep reflection.
Like I said before, JANK is an acronym. It stands for:

Justify 

Analyze 

Neuralize 

Kaizen

Let's dive in and talk about what each step of this cycle means, and how you can apply them to your own deckbuilding!

<img src="/assets/images/bwj-jank-cycle.png" alt="The JANK cycle" style="display:block; margin:2em auto;">


### JUSTIFY
Every single card swap should have a clear purpose. Justifying a change can take many forms: maybe you want to lower the curve of your ramp to cast your commander a turn earlier, or perhaps you need more answers for a specific threat that keeps losing you games. Whatever problem you are trying to solve, this step is where you define the parameters of your solution.

"Justifying" also means aligning something to a margin or standard. You can create a clear standard for your deck, and establish the margins it must operate within, by developing its Core Thesis. A deck's Core Thesis is a detailed set of guidelines and rules that contain the answers to questions like:

"What is the deck's main win condition, and what turn can it consistently achieve that wincon?"

And

"What does this deck's ideal first few turns look like, and how consistently can the deck mulligan to those hands?"

Notice that both of those examples mention consistency. In a competitive setting, consistency is the key to brewing a successful deck.

Being able to really define what your deck wants to do in order to consistently achieve its goals will help you justify any change that you may want to make to the deck. It also ensures that it's a change that improves the deck's performance overall.

<img src="/assets/images/bwj-actually.gif" alt="Actually" style="display:block; margin:2em auto;">


### ANALYZE
So you have a reason you want to make a change to your deck, and the parameters of how to achieve that change in a way that best supports your deck's Core Thesis. Now what?
You Analyze.

Analysis is the detailed examination of a complex system, breaking it down into smaller parts so you can understand its essential features and relationships. In deckbuilding, this means using the tools at your disposal to research the absolute best way to implement your justified change.

<img src="/assets/images/bwj-deep-analysis-1.jpg" alt="Deep Analysis" style="display:block; margin:2em auto;"> <img src="/assets/images/bwj-deep-analysis-2.jpg" alt="Deep Analysis" style="display:block; margin:2em auto;">


There are countless ways to do this. Often, this step looks like doom-scrolling advanced Scryfall searches, hunting for specific Oracle text or mechanics that solve your exact problem. Another way to find groups of cards is to manually type out criteria using the Scryfall Syntax directly into the search bar, or by using otags. [A guide to all that can be found here](https://scryfall.com/docs/syntax).

The more you practice navigating Scryfall's syntax to narrow your search down to the perfect cards, the easier this becomes. It also helps you to pay closer attention to the specific, precise language that Magic uses to interact with the state of the game.

This knowledge of game mechanics is invaluable to the analysis of a problem, and the more you engage in the JANK method of brewing, the more insight into the mechanics of Magic you will gain.

You can also borrow methods of analysis from other subjects like Root Cause Analysis. The Five Whys and Fishbone Diagrams are great tools to visualize issues and work towards a solution to any problem. Adapting these concepts to card analysis with the parameters that you set in the justification phase can really help to get to cards that most affect the changes you want in the deck.

Let’s explore adapting the Five Whys to analyzing your changes. The Five Whys is a process where you repeatedly ask "why" in response to each successive answer, much like a curious child seeking the root of all knowledge (parents, you know exactly what I'm talking about 🤣). By repeatedly drilling down on a subject, you gain a much better understanding of its root cause or potential effects. When evaluating a group of cards on Scryfall, we can systematically earmark or eliminate candidates by repeatedly checking them against our deck's Core Thesis and the margins set during the justification phase. It’s like playing a game of Guess Who!

Once you have analyzed your options and found a few viable cards, plus that perfect jank from Fallen Empires, you are ready for step three.


### NEURALIZE
Neuralizing is the act of implementing your changes with the least amount of disruption to the deck's core structure. This is the delicate stage where you make cuts, carefully weighing the impact those losses will have on your deck's "neural infrastructure".

This process is essentially the analysis step in reverse. You are weighing every logical cut you could make, and choosing the path of least resistance to maintain the deck's consistent performance.

I like to visualize a deck as a neural network. Every card connects back to the core pillars of the deck: things like the commander, the primary win conditions, and the overarching strategy (whether that's aggro, control, midrange, etc.). These connections form a complex lattice of cards branching out like neurons, all firing in patterns and sequences aimed at a single end state: winning the game.

Removing a card means removing a neuron. Any winning pathway that relied on that card being in the deck must now be reworked, or abandoned. To minimize friction, look to cut cards that sit on the outer fringes of this network, or the ones that are infrequently utilized or highly situational.

This might look like cutting narrow or inefficient interaction in favor of something more effective against the threats of your meta, or swapping out a high mana value beater for a more efficient, scaling threat. The goal is to eliminate the dead ends in your network, replacing them with cards that connect to as many pathways as possible. The tighter and more interconnected your network becomes, the faster and more consistently your deck will perform.

If you've made it this far, congratulations! You have successfully used JANK to optimize your deck. But the loop isn't finished yet. We must now move on to the last, and most important step.

<img src="/assets/images/bwj-neural-network.jpg" alt="Neural Network" style="display:block; margin:2em auto;">


### KAIZEN

<div class="wrapper">
  <article class="aside aside-1">Kaizen is a Japanese philosophy and business methodology that translates to "change for the better" or "continuous improvement". It focuses on making small, incremental, and sustainable changes to processes to boost efficiency, eliminate waste, and improve overall quality.
  Adopting this mindset of Always Improving (shoutout to the Constructed Criticism podcast) fundamentally changes how you look at Magic, and life. There are tons of ways to implement Kaizen, like reading articles or books, listening to podcasts, playing games with the intent of learning or gathering data, or even just talking about ideas with your friends. All of that insight that you gain can be applied back into the JANK cycle, further improving the process each time.However you choose to practice Kaizen, it is a way of thinking that leaves you grounded in a core set of principles, that while always changing and improving, will constantly drive you down a path of improvement that is ultimately rewarding, whether that reward be winning more games, or just being a better person than you were the day before.</aside>
  <article class="aside aside-2"><img src="/assets/images/bwj-kaizen.jpg" alt="Kaizen"></aside>
 </div>


### CONCLUSION
I hope this framework gives you a new lens for your next brewing session, and I highly encourage you to give the JANK method a try! If you want to dive deeper, share your builds, or just talk shop, you can always find me on the cpdh.guide Discord server.

But to close in the immortal stylings of Brad DracV:

"Go brew a deck, and get JANKy with it!"
✌️



{% include deck-tech-cta.html %}
{% include author-card.html %}
{% include article-nav.html %}
