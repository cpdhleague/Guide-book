---
# ===========================================================================
# CPDH.GUIDE — ARTICLE TEMPLATE
# ===========================================================================
# This file had NO front matter, which is why it never appeared. Jekyll only
# renders a collection file if it opens with a --- block; without one the file
# is treated as a static asset, so it stays out of site.previews and has no URL.

title: "Building a Manabase in cPDH"

# DATE: Must be today or earlier while in _previews/ — Jekyll will not build
# future-dated documents, and the preview will 404. Set the real publish date
# when you move this file into _posts/.
date: 2026-09-09

layout: splash
classes: wide

# ===========================================================================
# SECTION 1: WHO & WHAT
# ===========================================================================

creator: guide
author: ginger

categories:
  - Game Guides

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
# TODO: No artwork for this one yet. With no header.teaser set, the preview
# index falls back to cpdh.png automatically, so this builds fine as-is.

header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5

# ===========================================================================
# SECTION 4: EXCERPT
# ===========================================================================

excerpt: ""  # Required for GNews — fill this in before publishing to Google News

# ===========================================================================
# SECTION 5: REDDIT POSTING
# ===========================================================================
# reddit_text: ""  # Uncomment and fill in to enable Reddit posting

---

Section 1 - TLDR & Widget
Having a solid mana base is one of the most important aspects of deck building and a foundational step toward tournament success in PDH. When choosing lands, it’s important to understand the needs of your deck then build a land base that takes into consideration the spells you want to cast on curve and your commander’s CMC. This article is meant to build upon already popular articles written by MTG Pros and adapt their ideas to a singleton, commons-only manabase.

Before laying out my methodology and assumptions, I’m going to start by presenting a widget with copy-pasteable manabase templates at the beginning of this article. These manabases are meant to be generic starting points to jump-start your deckbuilding. These manabases have no consideration for the exact cards in your deck, nor synergies with your commander. I’ve created this tool for players who enjoy PDH and cPDH, but may not have the time to do the deep analytical dive required to finesse their mana extensively.

[Widget here]

For the deep dive and an itemized analysis of all the lands in PDH, continue on. 

TOC

Section 2 - What are the traits of successful cPDH decks?
Here on cPDH.guide, we maintain a decklist library from tournament finalists at cPDH events. These decklists represent the best-in-class for cPDH, the decks that are winning consistently enough to place in the top 4 and, for a quarter of those decks, also win a tournament. Even though this is only a slice of the meta, most people who are playing cPDH want to win and place in tournaments, so our bias aligns with our goals of succeeding more often.

I’ve analyzed the 116 decks in our library and found four consistent traits that inform how I calculate. We’re going to use the frameworks created by Frank Karsten to analyze the numbers and see where the math leads us. This analysis includes all of the cards of the 99 and does not consider what commander is leading the deck. For example, when we look at how many sources of ramp are in the deck, we don’t consider [[Malcolm]] as a ramp card even though he makes treasure fairly consistently once on the battlefield.

These are the four traits:

cPDH decks have low curves
cPDH decks run at least 10 nonland mana sources
cPDH decks run at least 10 cantrips or card draw spells
cPDH decks have low color-pip density

cPDH decks have low curves
The average cost of nonland cards in our dataset is 2.26, with most decks peaking in the 2-mana slot. The average deck’s curve looks like this:


It’s important to note that the high end of this curve is exaggerated to some extent, as many expensive cards have cost reductions, cycling abilities, or alternative casting costs.

[insert treasure cruise, warped tusker, unexpected assistance, perigee beckoner]

If we split the expensive cards (defined here as being above 3 CMC) into two categories, strict-cost and alt-cost, some trends emerge at the top-end. Only 4 of 116 decks ran more than 10 strictly-costed expensive cards: Vizkopa Guildmage (16), Gilanra + Numa (15), Sphinx of the Guildpact (12), The Emperor of Palamecia (11). 67.2% of decks run four or fewer strictly-costed cards over 3 CMC, even though the average expensive-card count across both categories is 8.15. 

Strict-cost and alt-cost counts correlate weakly (r = 0.33) — decks that run more strict-cost top-end also tend to run more alt-cost top-end, which reads as a commander’s or pilot’s preference for expensive cards rather than a tradeoff between the two.

cPDH decks have at least 10 nonland mana sources
76.7% of decks have 10 or more nonland sources of mana, with a median of 15. These decks are not relying solely on their lands to carry the weight of their gameplan’s mana expenditure.

Nonland mana sources vary in both their cost and function. For simplicity of modeling mana sources later, we're going to assume a cost of {2}, since the actual average cost across every nonland-mana-source card played in the sample is 2.28, and mana rocks — one of the easiest ways to add mana and fix color — are accessible from any color identity. We're also going to use 10 as the floor for what we expect a cPDH deck to run, since it's a conservative baseline even against the higher distribution above.

cPDH decks run at least 10 cantrips or card draw spells
70.7% of decks run 10 or more sources of card draw. Our card draw count includes impulse draw, cantrips, and looting effects. 67.2% run 12+ card draw spells while 29.3% - nearly a third of the sample - run 20 or more. The average is 15.32 card draw spells per deck across our decklist library.

Karsten suggests there are diminishing returns on draw cards, and recommends counting only the first 10. We'll use his recommendation and assume 10 draw spells at a cost of 2.27, the average CMC of card draw spells in our data.

cPDH decks have low color-pip density
Common cards don't ask too much of our mana base. We're not running mana costs like [[Phyrexian Obliterator]]'s {B}{B}{B}{B} in PDH, so we don't need land bases that hit one color 100% of the time. Of the nonland cards in our sample, 90.3% carry one colored pip or none at all. With requirements this light, we can run the optimal number of colored mana sources while also having room for lands with additional value and utility.

The cards that do carry double pips tend to be later-game cards. The biggest culprits are counterspells with {U}{U} — rarely played on curve — followed by loose-costed spells like Lórien Revealed, and closed out by Archaeomancer-style Wizard cards. Because we're looking to cast these cards later in the game, the pressure their mana costs put on the manabase is lower than the pip count suggests.

Frank Karsten has built the table below as a tool for evaluating your deck’s color requirements and determining the correct number of sources for a given color to consistently cast those spells on curve in a 99-card deck. We’re going to revisit this table in-depth later, but I highly recommend reading his article on casting spells consistently to learn and utilize his methods for calculating exactly how you should build out your mana base. Karsten includes methods for calculating spells intended to be cast off-curve and gold cards with multiple pip colors. He walks through a full example for a Rakdos Pioneer deck at the end of that article — it's worth reading end to end if you want to run this math against your own decklist rather than the format-wide averages.



The short version of what the table says: a single-pip card needs far fewer colored sources than a double-pip card to hit the same consistency, and the colored source count increases the earlier you want to cast it. Since 90.3% of our cards are single-pip or colorless, and the double-pip cards we do run tend to be ones we're happy to cast later than turn 2, our decks don't need the color source density a double-pip-heavy deck would require.

Section 3 - How do we define an optimal landbase?
An optimal land base is going to be one that allows us to play on curve and consistently cast our spells. The specifics of how many lands total and how many mana sources per color are questions that each deck will need to answer independently, but we will evaluate the lands available to us in the next section to better understand which of these options are worth putting in our deck and which fall short in their offerings.

These are the considerations I’ve used when analyzing lands, in the order of their weight:

Efficiency
Do our land choices maximize our mana production per turn? Basic lands will be our baseline, offering +1 mana production to our land base per turn, providing a total of 28 mana over the first seven turns (assuming all land drops are made). This is graphed below. We’ll be visiting variations of this graph when analyzing a few of the other land options available to us, so keep it in mind. 



Fixing
Beyond figuring out how many lands are optimal, we want to see how many of them tap for more than one color so we can use those lands to better color-fix our decks. While this is an important criteria, it is secondary to our efficiency criteria on the basis of individual lands. Fixing on a deck level can be accounted for in deckbuilding while calculating the number of mana sources of each color and does not necessarily require less efficient individual lands.

Flexibility
Some lands have additional abilities that can affect mana production, card advantage, or board state. In addition, certain spells can be treated as lands because of their land cycling abilities or abilities to pull lands into our hand. This is our *last* priority and the flexibility of a card should in no way override its efficiency or its fixing, which are our top priorities. 


Section 4 - Evaluating Lands
Establish baseline with basic lands 25 mana efficiency use graph from before
Eval each land based on its math noting which to keep and which to get rid of. add exceptions for when it might be good, descriptions
Untapped - these lands are excellent as they stick to our plan of having our mana available immediately. They completely fill our #1 function. Some of them also fill #2, but not all of them. In order of color ID. These are all good choices, but lets talk about which are best. 
removal lands - excellent
colorless lands, so they don’t help with fixing. These are lands that would be best used in the extra slots after you’ve adjusted your mana base for fixing. 
So good at the extra function, hits boogeymen of the format like weavers, combo pieces, archaeomancers, etc which allows you to shut down wins. Sucks that it costs you a land, but the upside is so good. This is for quicksand
Desert is also very good, no sac needed, repeatable, can slowly eat away at small attackers if you’re not using the mana in other ways. 
surveil/scry lands - good if you can run them
include here the math that Karsten uses to explain that a scry is .2 of a land. By extension, these cards are effectively 1.2 lands in them selves, tho you can also use them to filter for other needs, obv. 
commander x times - situationally excellent
Really good when you have commanders that you either want to cast multiple times or are prepared to cast multiple times. Very few decks. Hollow marauder is an example, but some decks focus on sacing hollow marauder, so only the scry would matter. Not usually ideal or consistent enough.
command tower - good in multi-color. Fixes our mana wonderfully. No extra functions
tap creature for mana - awesome
great for multicolor decks. Must have creatures that are okay to be tapped, but if you have that criteria met, it’s effectively another command tower. 
great synergies where it is needed. Commanders that care about tapping things or untapping thing or for Far Traveler to be able to trigger. 

artifact lands - untapped, on their own are fine. In the context of the meta, more vulnerable to removal, PoP, needs to have a good reason due to additional risks.
eldraine lands
great in mono color, mystic sanctuary belongs in lots of decks because of combos. situationally acceptable in multi color, but sometimes the synergy is relevant. May also be good in decks that are skewed hard into a particular color
tri-color cyclers - these are great in 3- and 5- color decks. Great flexibility. Cycle it, use colorless mana now, sac for colored mana later. If only we had these cards in other colors. 

Tapped - dual lands in general are awful. They stunt our mana production and prevent casting things on time. most aren’t included specifically. The following are cards I’ve commonly seen be asked about. Or they are cards with situational consideration. As much as possible, these lands should not appear in your mana bases. 
sac lands are no good. Most lands with sac effects have been disregarded. The game would have to go on long enough that you run out of spells AND have the excess mana to spend and this is rarely the case. Doesn’t fill our primary function. 
path of ancestry - not good. People are going to run it, but I don’t think it belongs at the table. Argument for decks prepared to cast their commander multiple times, such as Dargo perhaps, but even then I don’t know that Dargo would want to sacrifice the speed of having a tapped land. 
fetch lands - fine. some extra bonuses. Better than tapped lands. avoids PoP. Pay to fetch not great, but offer flexibility. Other bonuses that could be relevant.
cycle lands
bad - explain why
Zendikar ability lands - maybe? usually no
depletion - usually awful. proliferate great. 
damage lands - only good in combo decks. 
duskmorn - running this is optimistic. Doesn’t actually work. 
artifact bridges
acceptable but increasingly less so
can be tutored by trinket mage, so maybe
bouncelands
card efficiency, fixing, great. Counts as 2 lands when in hand as it allows you to complete two land drops. 
also becomes a ritual, empowers a lot of blue decks to do cool things with their spells. 
Dual-typed lands
they are fetchable. They help us fix. We keep these all the time, especially in tandem with LotR cyclers. 

land drops disguised as spells
ltr cyclers - excellent flexibility. The range of flexibility is so great that we often include them. 
2-mana cyclers
fountainport bell
great in almost every deck. Run one! 

Section 5 - Math to support analysis 
Bring in the Karsten math and maximum examination! how to use laid out below

Section 6 - Widget Methodology and Suggestions
Unlike formats with access to all rarities, there is a fairly limited pool of common cards in PDH and cPDH, meaning there are quite clear best practices in comparison to broader flexibility in other formats. 
Explain the thoughts behind the widget and why certain cards were picked. 
Do an example deck. Show how you would make adjustments. 

Section 7 - Additional Considerations
Mulliganing; room for more ability lands?; PoP; math of drawing spells, and , scrying, and other wise and how to calculate their worth toward land count. 

—-----------------------------------------------------------------------------------------------------
Notes and graphs, still in the working: https://docs.google.com/document/d/1T7KPtXSvn5q2Uyilqmy6klHUm63D2OZTp_qJ2Hq9Sqw/edit?tab=t.0