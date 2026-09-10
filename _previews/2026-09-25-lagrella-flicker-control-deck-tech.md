---
# ===========================================================================
# CPDH.GUIDE — ARTICLE TEMPLATE
# ===========================================================================

title: "Lagrella, the Magpie cPDH Deck Tech: Flicker Control"

# DATE: Update to actual publish date
date: 2026-09-25

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

image: /assets/images/lagrella-decktech.png

header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  teaser: /assets/images/lagrella-decktech.png

# ===========================================================================
# SECTION 4: EXCERPT
# ===========================================================================

excerpt: ""  # Required for GNews — fill this in before publishing to Google News

# ===========================================================================
# SECTION 5: REDDIT POSTING
# ===========================================================================
# reddit_text: ""  # Uncomment and fill in to enable Reddit posting

---

Generally speaking, control decks have an easier time in 1v1 settings, where you can trade a resource, like a counterspell or kill spell, for one of your opponent's resources, like a [[Colossal Dreadmaw]]. Add a few tools to stay ahead on card count and you can keep your opponent's board clear while you slowly beat them down.

That concept falls apart in most of cPDH. The format simply doesn't have the tools to facilitate a traditional control gameplan. Boardwipes are few in the format, most of them dealing a limited amount of damage. Edicts are effective, but are also limited in their reach — opponents with extra creatures can choose which ones they want to keep most. Staying ahead is brutal when, in the theoretical environment where you're answering everyone's resources, you have three times as many opponents and threats to deal with as you would in a 1v1 environment. It's almost always a better use of your time to focus on winning the game than to stop three other people from winning simultaneously.

So why go to all this trouble explaining why control is a pretty bad option in cPDH? Because today we're going to look at an exception. We're exploring [Lagrella, the Magpie](https://moxfield.com/decks/XHU6WSse-UCE30Qh8Z4gYQ). Lagrella doesn't exactly turn the problems of multiplayer control on their head, but she does offer something genuinely powerful: she interacts with all three of your opponents at once, while simultaneously offering additional value to you as she does.

{% include card-grid.html cards="Lagrella the Magpie;" %}

This is a flicker combo-control deck. Flicker — blinking a permanent into exile and back onto the battlefield — is one of the most versatile mechanics in PDH, and it's the bread and butter of this list. We run 21 flicker spells (counting [[Icewind Stalwart]]). We can flicker Lagrella instantly to put her exile trigger on the stack when we want it; some cards can exile her until the end of turn to dodge an edict effect; or we can flicker her in response to targeted removal to protect her. The deck builds on the flexibility of the flicker spells at our disposal to repeatedly abuse our commander's ability, extending the reach of each flicker effect to each player's board.

## How Does Lagrella Win?

Because the whole deck is built around flickering, we can win through two primary combo lines.

The first is the well-known [[Archaeomancer]] + [[Ghostly Flicker]] + [[Peregrine Drake]] line. This line generates infinite mana, and from there flickering any single creature that draws, plus Archaeomancer, draws your entire deck, finds your payoff, and closes out the game. Casting [[Capsize]] on all of your opponents' permanents to bounce them back to hand is a decisive, if slow, way to lock up the game as well. A faster closer is flickering [[Avenging Hunter]] repeatedly, draining each opponent for five life as many times as you have cards left in your deck.

{% include card-grid.html cards="Archaeomancer; Ghostly Flicker; Peregrine Drake" %}

The second line has [[Icewind Stalwart]] and Lagrella flickering each other infinitely, with a requirement to have a payoff for all those ETB and LTB triggers. [[Suture Priest]] wins the game if your opponents have non-commander, non-token creatures in play; a [[Candlekeep Sage]] draws your whole deck to get to a more effective win condition; or a [[Soul Warden]] gains you infinite life, which makes you very difficult to kill, except to commander damage.

{% include card-grid.html cards="Icewind Stalwart; Suture Priest; Candlekeep Sage; Soul Warden" %}

## Buying Time: The Control Engine

Lagrella can win definitively, and she has the ramp and draw to get there, but assembling the pieces takes time. There's no fast tutor for exactly what you need — the transmute cards help, but nothing in Bant transmutes into [[Peregrine Drake]]. So we spend much of the early and mid game buying time.

I've found this deck functions best when it only controls creatures. We could try to control the stack with counterspells, answer artifacts and enchantments, and answer creatures all at once — but our card pool would grow hopelessly diluted the more elements we tried to police. So we focus on snatching creatures off the battlefield with our commander instead of attempting to control everything.

That sounds restrictive, but controlling creatures is one of the most meaningful forms of control in PDH: attackers deal most of the combat damage, pingers deal most of the non-combat damage, others provide incremental value, and nearly every engine and combo in the format relies on one creature or another. There are hardly any win attempts that won't funnel through at least one creature.

Second, there's a wonderful control engine here that's easy to assemble and needs only three cards: Lagrella herself, any one of your 20-plus flicker spells, and a "wizard" (any card that returns an instant from your graveyard — most of which happen to be wizards, including [[Archaeomancer]]). When Lagrella enters, you put the wizard in exile underneath her. Now, each time you flicker Lagrella, you get a wizard trigger returning your used flicker spell back to hand, plus a Lagrella trigger to exile up to four creatures, one from each player's board, including your own wizard, which you simply tuck back under Lagrella again.

By repeating this, you interact with your opponents' creatures as many times as you have mana to recast the flicker spell. It's a remarkably strong loop — clearing a wave of attackers in one swoop, or disrupting engines and combos at will.

With our win conditions and our time-buying engine established, let's talk about the cards that bridge the gap between them.

## Mana Base

The mana base is a fun and tricky puzzle, because we have three colors to fix. I've heard players fret about how hard that is to pull off, but with our toes dipped in green and some wise selections, getting our colors is easy and rarely disrupts the rest of the gameplan.

### Lands

I hate tapped lands. I want my lands to make mana and I want them to do it now, not later. In the words of Dr. Seuss:

> I do not like those enter-tapped lands,
> I do not like them, Sam-I-am.

Everyone hates them. But we're in three colors and we do need some of them. These are the ones that matter most, and they're the only ones I currently run.

**Dual-typed lands** let us fetch any color whenever we islandcycle, forestcycle, or play a [[Wood Elves]] — and in all of those cases we can instead grab the untapped basic land for faster mana. The flexibility offered by having these in our deck lets us keep a much wider range of opening hands, confident we'll find the colors we need.

{% include card-grid.html cards="Idyllic Beachfront; Radiant Grove; Tangled Islet" %}

**Bouncelands** earn their slot through sheer card efficiency: each one represents two land drops as they return another land back to our hand. Better still, we run [[Cloud of Faeries]], [[Peregrine Drake]], and [[Frantic Search]], all of which untap these lands — turning mana-neutral cards into mana-positive "rituals."

{% include card-grid.html cards="Azorius Chancery; Simic Growth Chamber; Selesnya Sanctuary" %}

**Fast fetchlands** — lands that enter untapped, tap for colorless right away, and can sacrifice to fetch any of our three colors. That makes them great early-game for color fixing and great late-game when we just need mana and the color doesn't matter.

{% include card-grid.html cards="Tranquil Landscape; Shire Terrace" %}

**Tap-a-creature-for-any-color lands** are exceptional here too: in a deck this creature-heavy, cards like [[Holdout Settlement]] and [[Survivors' Encampment]] are extra copies of [[Command Tower]]. What's more, if you're about to flicker a creature anyway, tap it for mana first — you're not costing yourself a blocker.

And of course we run [[Lórien Revealed]] and [[Generous Ent]], because they're just so gosh darn good.

### Ramp

Wherever possible, we want our ramp to fix colors in addition to adding to our mana count — we have three colors we want access to. Our rocks — [[Springleaf Drum]], [[Arcane Signet]], and [[Fellwar Stone]] — do exactly that. [[Bender's Waterskin]] recently made the cut, feeding the deck's desire to tap for instant-speed interaction as often as possible. [[Farhaven Elf]], [[Wood Elves]], [[Springbloom Druid]], and [[Utopia Sprawl]] all do the same job: more mana, more colors, more of the good life.

There are a number of effective cost reducers that feel right at home in the deck, reducing the costs of our prominent flicker spells: [[Sunscape Familiar]], [[Naiad of Hidden Coves]], and [[Geyser Drake]]. I don't run [[Mocking Sprite]] — it dies too easily at one toughness.

## Card Draw & Selection

We run all of the two-mana "draw a card" creature spells. They're cheap, they're effective, and if more get printed, they'll make the cut too. If I'm going to pay more than two for a drawing creature, it had better dig deeper than just the top card of the deck. So I choose to skip the [[Inspiring Overseer]]s and [[Generous Stray]]s in favor of [[Sea Gate Oracle]], [[Sibsig Appraiser]], [[Serum Visionary]], [[Mulldrifter]], and [[Augur of Bolas]].

Alongside that selection, we run all three of the available transmute cards: [[Drift of Phantasms]], [[Dizzy Spell]], and [[Muddle the Mixture]].

## Wizards

We covered why these are so valuable to the gameplan above. Five creatures fit the bill — four wizards and one wall — each able to return an instant from the graveyard to keep our hand full of flicker spells.

On top of those, we get to run two of the best tutors in the format: wizardcyclers. [[Step Through]] and [[Vedalken Aethermage]] put a wizard directly into our hand at instant speed and remain nearly uncounterable (no one runs [[Mirrorshell Crab]], right?).

## Miscellaneous Threats & Tools

Here are the final odds and ends in the deck. Let's run through them.

**[[Unexpected Assistance]], [[Frantic Search]], and [[Meeting of the Minds]]** let us draw cards for free. Convoke costs are rarely a problem, and Frantic Search can act as a ritual when it untaps an enchanted land, bounceland, or [[High Tide]] island, on top of its draw.

**[[Peregrine Drake]] and [[Cloud of Faeries]]** come down as rituals, or at least for free. Even if you only want a free blocker, savvy opponents know how dangerous these two are and may treat you as a real threat for deploying them — and they're right, since both are pieces of our winning lines.

**[[Candlekeep Sage]]** — we want to flicker our commander anyway, so why not draw two cards every time we do?

**[[Avenging Hunter]]** is a flicker payoff that drains each opponent for five life each time we run through the Undercity. I could run the cheaper [[Aarakocra Sneak]], but this deck lacks the damage to grind late-game scrappy brawls, so I prefer the bigger trampling body. He's also great at reclaiming the initiative, especially with two +1/+1 counters from Lagrella on him.

**[[Capsize]]** is an infinite-mana payoff, bouncing everything we don't own back to our opponents' hands. The game isn't technically won at that point, but it's basically over from there.

**[[Prismatic Strands]]** is a wonderful piece of protection, made more wonderful by how easily we can cast it twice, the second time for free.

**[[High Tide]]** is mostly a combo piece, letting [[Cloud of Faeries]] generate infinite mana in a flicker loop by untapping our islands for two mana each. When we're not comboing, it's a fine tempo boost to push through a mana-hungry turn. We can always get it back with a wizard if we need it again later.

## Cards to Consider

[[Evolution Witness]] might have combo potential, especially since you can get free triggers by flickering it with Lagrella. If you can figure out how to make it sing, you're a better brewer than me, and I applaud you.

[[Stonehorn Dignitary]] can skip your opponents' combat phases entirely. It's a cool effect, but since it only helps you survive rather than win, I've cut it for now.

[[Ray of Command]] has a neat interaction trick. Steal an opponent's creature, then flicker it onto your own board with Lagrella, and it stays yours. Why? The "until end of turn" clause applies to the original instance of the creature, not the new one that enters under your control. The creature never returns back to the owner, it stays with the new controller. The exception is commanders: a savvy pilot can send their commander back to the command zone when it gets flickered.

## An Alternate Gameplan

I've seen attempts to run Lagrella as a beatdown midrange deck full of big creatures, effects that give trample to creatures with +1/+1 counters, and similar synergies. In fact, the physical cards I own were bought from someone who ran exactly that style of list, found it both unsatisfying and unsuccessful, and wanted to be rid of the deck.

I haven't seen this version function well, and I don't care to explore it myself, but I do think a list using Lagrella to buff your creatures and beat down your opponents' life totals while controlling the board could find some play. It's not for me, but it's out there, and you can build it if the concept makes you happy.

## Playing Against the Deck

Some anecdotal evidence first: it is rare that the opponent who dedicates their resources to killing Lagrella or her owner ends up winning the game. Killing them can take a lot of resources, given how many flicker effects and triggers the Lagrella player has to keep her alive. Far more often, someone decides they want her gone, commits everything to making it happen — and then loses to a different player at the table.

There are a couple of reasons for this. First, Lagrella is usually hindering the other players too, not just you. When I pilot the deck, I'm often exiling combo and value pieces off everyone's boards. Take me out, and you may have just handed two other players the room they needed to win — all while dwindling your own resources. Remember: control doesn't win games, it only prevents you from losing. If your Lagrella opponent is only controlling the board and not comboing off, they're probably helping you to not lose as well. She can only hold on to one of your creatures at a time, so if you've got other productive lines of play in the meanwhile, leave her be.

If you're a combo player, remember that you'll get your commander back when Lagrella flickers it. I've seen many a [[Malcolm, Keen-Eyed Navigator]] player send their commander back to the command zone to recast it for five mana next turn, only to have Lagrella snatch it right back up. Don't put it back in the command zone. A far better answer is to hold up a [[Dive Down]] or similar protection spell that recovers your key piece for a single mana the next time it's flickered to your board, without driving up your commander tax.

Be savvy and check what removing Lagrella or her owner will do for your opponents, not just for you. Kill her when it makes sense, but otherwise don't throw away your chance to win because you were impatient.

<!-- TODO: export the decklist image to /assets/images/cpdh-lagrella-list.png -->
<img src="/assets/images/lagrella-deck.png" alt="Lagrella full decklist" style="width:100%; display:block; margin:2em auto;">

<a href="https://manapool.com/add-deck?deck=MSBBY3JvYmF0aWMgTWFuZXV2ZXIKMSBBaXJiZW5kaW5nIExlc3NvbgoxIEFyY2FuZSBTaWduZXQKMSBBcmNoYWVvbWFuY2VyCjEgQXVndXIgb2YgQm9sYXMKMSBBdmVuZ2luZyBIdW50ZXIKMSBBem9yaXVzIENoYW5jZXJ5CjEgQmx1cgoxIENhbmRsZWtlZXAgU2FnZQoxIENhcHNpemUKMSBDbG91ZCBvZiBGYWVyaWVzCjEgQ2xvdWRzaGlmdAoxIENvaWxpbmcgT3JhY2xlCjEgQ29tbWFuZCBQZXJmb3JtYW5jZQoxIENvbW1hbmQgVG93ZXIKMSBEaXNwbGFjZQoxIERpenp5IFNwZWxsCjEgRHJpZnQgb2YgUGhhbnRhc21zCjEgRWx2aXNoIFZpc2lvbmFyeQoxIEVwaGVtZXJhdGUKMSBFc3NlbmNlIEZsdXgKMSBFc3NlbmNlIFdhcmRlbgoxIEZhcmhhdmVuIEVsZgoxIEZlbGx3YXIgU3RvbmUKMSBGbGlja2VyIG9mIEZhdGUKNSBGb3Jlc3QKMSBGcmFudGljIFNlYXJjaAoxIEdhbGxhbnQgQ2l0aXplbgoxIEdob3N0bHkgRmxpY2tlcgoxIEhlbHBmdWwgSHVudGVyCjEgSGlnaCBUaWRlCjEgSG9sZG91dCBTZXR0bGVtZW50CjEgSWNld2luZCBTdGFsd2FydAoxMCBJc2xhbmQKMSBKdXN0aWNpYXIncyBQb3J0YWwKMSBLaW5kbHkgQ3VzdG9tZXIKMSBMw7NyaWVuIFJldmVhbGVkCjEgTWVldGluZyBvZiBNaW5kcwoxIE1uZW1vbmljIFdhbGwKMSBNb21lbnRhcnkgQmxpbmsKMSBNdWRkbGUgdGhlIE1peHR1cmUKMSBNdWxsZHJpZnRlcgoxIE90aGVyd29ybGRseSBKb3VybmV5CjEgUGVnYXN1cyBHdWFyZGlhbgoxIFBlcmVncmluZSBEcmFrZQo3IFBsYWlucwoxIFBsYW5hciBJbmNpc2lvbgoxIFBvbmQgUHJvcGhldAoxIFByaXNtYXRpYyBTdHJhbmRzCjEgUmFkaWFudCBHcm92ZQoxIFNhbHZhZ2VyIG9mIFNlY3JldHMKMSBTY3JpdmVuZXIKMSBTY3JvbGxzaGlmdAoxIFNlYSBHYXRlIE9yYWNsZQoxIFNlbGVzbnlhIFNhbmN0dWFyeQoxIFNlcnVtIFZpc2lvbmFyeQoxIFNoaXB3cmVjayBEb3dzZXIKMSBTaGlyZSBUZXJyYWNlCjEgU2lic2lnIEFwcHJhaXNlcgoxIFNpbWljIEdyb3d0aCBDaGFtYmVyCjEgU2lyZW4ncyBSdXNlCjEgU2xpcCBPbiB0aGUgUmluZwoxIFNvdWwgV2FyZGVuCjEgU3Bpcml0ZWQgQ29tcGFuaW9uCjEgU3ByaW5nYmxvb20gRHJ1aWQKMSBTcHJpbmdsZWFmIERydW0KMSBTdGVwIFRocm91Z2gKMSBTdW5zY2FwZSBGYW1pbGlhcgoxIFN1cnZpdm9ycycgRW5jYW1wbWVudAoxIFN1dHVyZSBQcmllc3QKMSBUYW5nbGVkIElzbGV0CjEgVGVmZXJpJ3MgVGltZSBUd2lzdAoxIFRyYW5xdWlsIExhbmRzY2FwZQoxIFR1cm4gdG8gTWlzdAoxIFVuZXhwZWN0ZWQgQXNzaXN0YW5jZQoxIFV0b3BpYSBTcHJhd2wKMSBWZWRhbGtlbiBBZXRoZXJtYWdlCjEgV2lsZCBHcm93dGgKMSBXb29kIEVsdmVzCjEgU3BpZGVyLU1hbiwgQnJvb2tseW4gVmlzaW9uYXJ5CgoxIEJlbmRlcidzIFdhdGVyc2tpbgoxIEdlbmVyb3VzIEVudAoxIEdleXNlciBEcmFrZQoxIEguRS5SLkIuSS5FLiBTY291dCBVbml0CjEgTmFpYWQgb2YgSGlkZGVuIENvdmVzCjEgUmVhbGl0eSBSaXBwbGUKMSBTcGFjZXNoaWZ0CgoxIENvb2wgRmx1ZmZ5IExveG9kb24KMSBFdGVybmFsIEFjcm9iYXQgVG9hc3QKMSBGYW1pbGlhciBCZWVibGUgTWFzY290CjEgR2lhbnQgTWFuYSBDYWtlCjEgSGFwcHkgRGVhZCBTcXVpcnJlbAoxIFNhc3N5IEdyZW1saW4gQmxvb2QKMSBTbGlteSBCdXJyaXRvIElsbHVzaW9uCjEgU3F1aXNoeSBTcGhpbnggTmluamEKMSBUcmFpbmVkIEJsZXNzZWQgTWluZAoxIFlhd2dtb3RoIE1lcmZvbGsgU291bAoKMSBMYWdyZWxsYSwgdGhlIE1hZ3BpZQ&ref=cpdhguide" class="btn btn--primary btn--large" target="_blank" rel="noopener">Purchase on Manapool</a>

{% include deck-tech-cta.html %}
{% include author-card.html %}
{% include article-nav.html %}
