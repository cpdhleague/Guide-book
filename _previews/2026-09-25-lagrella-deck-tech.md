---
# ===========================================================================
# CPDH.GUIDE — ARTICLE TEMPLATE
# ===========================================================================

title: "Lagrella, the Magpie - Flicker Control Deck Tech"

# DATE: Must be today or earlier while in _previews/ — Jekyll will not build
# future-dated documents, and the preview will 404. Set the real publish date
# when you move this file into _posts/.
date: 2026-09-10

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

image: /assets/images/lagrella-deck-tech.jpg

header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  teaser: /assets/images/lagrella-deck-tech.jpg

# ===========================================================================
# SECTION 4: EXCERPT
# ===========================================================================

excerpt: ""  # Required for GNews — fill this in before publishing to Google News

# ===========================================================================
# SECTION 5: REDDIT POSTING
# ===========================================================================
# reddit_text: ""  # Uncomment and fill in to enable Reddit posting

---

Control decks generally have a difficult time in PDH. Compared to 1v1 formats, commander requires you to answer three times the threats and stop three opponents instead of one., where you can trade a resource, like a counterspell or kill spell, for one of your opponent's resources, like a [[Colossal Dreadmaw]]. Add a few tools to stay ahead on card count and you can keep your opponent's board clear while you beat them down. It's almost always a better use of your time to focus on winning the game than to stop three other people from winning.

Today we're going to look at one of only a few exceptions. We're exploring [Lagrella, the Magpie](https://moxfield.com/decks/XHU6WSse-UCE30Qh8Z4gYQ). Lagrella doesn't negate the problems of multiplayer control, but she does offer something powerful: she interacts with all three of your opponents at once, furthering your own gameplan while doing so.

{% include card-grid.html cards="Lagrella the Magpie;" %}

This is a flicker combo-control deck. Flicker is one of the most versatile mechanics in PDH, and it's the bread and butter of this list. We run 21 flicker spells (counting [[Icewind Stalwart]]). We can flicker Lagrella to put her exile trigger on the stack when we want it; some cards can exile her until the end of turn to dodge an edict effect; or we can flicker her in response to targeted removal to protect her. The deck builds on the flexibility of the flicker spells at our disposal to abuse our commander's ability, extending the reach of each flicker effect to each player's board.

## How Does Lagrella Win?

Flicker combo. We have the well-known [[Archaeomancer]] + [[Ghostly Flicker]] + [[Peregrine Drake]] line as well as its close cousins (substituting Prergrine drake for [[High Tide]] + [[Cloud of Faeries]] for example). This line generates infinite mana, and from there flickering any single creature that draws, plus Archaeomancer, draws your entire deck, finds your payoff, and closes out the game. Casting [[Capsize]] on all of your opponents' permanents to bounce them back to hand is a decisive, if slow, way to lock up the game as well. A faster closer is flickering [[Avenging Hunter]], draining each opponent for five life as many times as you have cards left in your deck.

{% include card-grid.html cards="Archaeomancer; Ghostly Flicker; Peregrine Drake" %}

Lagrella also has a number of commander-unique lines, many of which revolve around [[Icewind Stalwart]] and Lagrella flickering each other infinitely, with a requirement to have a payoff for all those ETB and LTB triggers. [[Suture Priest]] wins the game if your opponents have non-commander, non-token creatures in play; a [[Candlekeep Sage]] draws your whole deck to get to a definitive win condition; or a [[Soul Warden]] gains you infinite life, which makes you very difficult to kill, except to commander damage.

{% include card-grid.html cards="Icewind Stalwart; Suture Priest; Candlekeep Sage; Soul Warden" %}

## Buying Time: The Control Engine

Lagrella can win definitively, and she has the ramp and draw to get there, but assembling the combo pieces takes time. There's no fast tutor for what you need — the transmute cards help, but nothing in Bant transmutes into [[Peregrine Drake]]. So we spend much of the early and mid game buying time.

I've found this deck functions best when it only controls creatures. We could try to control the stack with counterspells, answer artifacts and enchantments, and answer creatures all at once — but our card pool would grow diluted the more elements we tried to police. So we focus on snatching creatures off the battlefield with our commander instead of attempting to control everything.

That sounds restrictive, but controlling creatures is one of the most meaningful forms of control in PDH: attackers deal most of the combat damage, pingers deal most of the non-combat damage, others provide incremental value, and most engines and combos in the format relies on a creature being in play. There are almost no win attempts that can be made without funneling through at least one creature.

Second, there's a wonderful control engine here that's easy to assemble and needs only three cards: Lagrella herself, any one of your 20-plus flicker spells, and a "wizard" (any card that returns an instant from your graveyard — most of which happen to be wizards, including [[Archaeomancer]]). When Lagrella enters, you put the wizard in exile underneath her. Now, each time you flicker Lagrella, you get a wizard trigger returning your used flicker spell back to hand, plus a Lagrella trigger to exile up to four creatures, one from each player's board, including your own wizard, which you tuck back under Lagrella again.

By repeating this, you interact with your opponents' creatures as many times as you have mana to recast the flicker spell. It's a strong loop — clearing a wave of attackers in one swoop, or disrupting engines and combos at will.

With our win conditions and our time-buying engine established, let's talk about the cards that bridge the gap between them.

## Miscellaneous Threats & Tools

Here are the final odds and ends in the deck. Let's run through them.

**[[Unexpected Assistance]], [[Frantic Search]], and [[Meeting of the Minds]]** let us draw cards for free. Convoke costs are not a problem in such a creature-focused deck, and Frantic Search can act as a ritual when it untaps a bounceland or [[High Tide]] island on top of its looting ability.

**[[Candlekeep Sage]]** — we want to flicker our commander anyway, so why not draw two cards every time we do?

**[[Avenging Hunter]]** is a flicker payoff that drains each opponent for five life each time we run through the Undercity. I could run the cheaper [[Aarakocra Sneak]], but this deck lacks the damage to grind late-game scrappy brawls, so I prefer the bigger trampling body. He's also great at reclaiming the initiative with two +1/+1 counters from Lagrella on him.

**[[Capsize]]** is an infinite-mana payoff, bouncing everything we don't own back to our opponents' hands. The game isn't won at that point, but it's over from there 99% of the time.

**[[Prismatic Strands]]** is a wonderful piece of protection, made more wonderful by how we can cast it twice, the second time for free.

## Cards to Consider

[[Evolution Witness]] might have combo potential, since you can get free triggers by flickering it with Lagrella. If you can figure out how to make it sing, you're a better brewer than me, and I applaud you.

[[Stonehorn Dignitary]] can skip your opponents' combat phases. It's a cool effect, but since it only helps you survive rather than win, I've cut it for now.

[[Ray of Command]] has a neat interaction trick. Steal an opponent's creature, then flicker it onto your own board with Lagrella, and it stays yours. Why? The "until end of turn" clause applies to the original instance of the creature, not the new one that enters under your control. The creature never returns back to the owner, it stays with the new controller. The exception is commanders: a savvy pilot can send their commander back to the command zone when it gets flickered.

## An Alternate Gameplan

I've seen attempts to run Lagrella as a beatdown midrange deck full of big creatures, effects that give trample to creatures with +1/+1 counters, and similar synergies. In fact, the physical cards I own were bought from someone who ran that style of list, found it both unsatisfying and unsuccessful, and wanted to be rid of the deck.

I haven't seen this version function well, and I don't care to explore it myself, but I do think a list using Lagrella to buff your creatures and beat down your opponents' life totals while controlling the board could find some play. It's not for me, but it's out there, and you can build it if the concept makes you happy.

## Playing Against the Deck

Some anecdotal evidence first: it is rare that the opponent who dedicates their resources to killing Lagrella or her owner ends up winning the game. Killing them can take a lot of resources, given how many flicker effects and triggers the Lagrella player has to keep themselves alive. Far more often, someone decides they want her gone, commits everything to making it happen — and then loses to a different player at the table.

There are a couple of reasons for this. First, Lagrella is hindering the other players too, not just you. The Lagrella pilot often exiles combo and value pieces off of everyone's boards. Take them out, and you may have just handed two other players the room they needed to win — all while dwindling your own resources. Remember: control doesn't win games, it prevents you from losing. If your Lagrella opponent is only controlling the board and not comboing off, they're helping you to not lose as well. She can hold on to one of your creatures at a time, so if you've got other productive lines of play in the meanwhile, leave her be.

If you're a combo player, remember that you'll get your commander back when Lagrella flickers it. I've seen many a [[Malcolm, Keen-Eyed Navigator]] player send their commander back to the command zone to recast it for five mana next turn, just to have Lagrella snatch it right back up. Don't put it back in the command zone. A far better answer is to hold up a [[Dive Down]] or similar protection spell that recovers your key piece for a single mana the next time it's flickered to your board, without driving up your commander tax.

Be savvy and check what removing Lagrella or her owner will do for your opponents, not just for you. Kill her when it makes sense, but otherwise don't throw away your chance to win because you were impatient.

<img src="/assets/images/lagrella-deck.png" alt="Lagrella full decklist" style="width:100%; display:block; margin:2em auto;">

<a href="https://manapool.com/add-deck?deck=MSBBY3JvYmF0aWMgTWFuZXV2ZXIKMSBBaXJiZW5kaW5nIExlc3NvbgoxIEFyY2FuZSBTaWduZXQKMSBBcmNoYWVvbWFuY2VyCjEgQXVndXIgb2YgQm9sYXMKMSBBdmVuZ2luZyBIdW50ZXIKMSBBem9yaXVzIENoYW5jZXJ5CjEgQmx1cgoxIENhbmRsZWtlZXAgU2FnZQoxIENhcHNpemUKMSBDbG91ZCBvZiBGYWVyaWVzCjEgQ2xvdWRzaGlmdAoxIENvaWxpbmcgT3JhY2xlCjEgQ29tbWFuZCBQZXJmb3JtYW5jZQoxIENvbW1hbmQgVG93ZXIKMSBEaXNwbGFjZQoxIERpenp5IFNwZWxsCjEgRHJpZnQgb2YgUGhhbnRhc21zCjEgRWx2aXNoIFZpc2lvbmFyeQoxIEVwaGVtZXJhdGUKMSBFc3NlbmNlIEZsdXgKMSBFc3NlbmNlIFdhcmRlbgoxIEZhcmhhdmVuIEVsZgoxIEZlbGx3YXIgU3RvbmUKMSBGbGlja2VyIG9mIEZhdGUKNSBGb3Jlc3QKMSBGcmFudGljIFNlYXJjaAoxIEdhbGxhbnQgQ2l0aXplbgoxIEdob3N0bHkgRmxpY2tlcgoxIEhlbHBmdWwgSHVudGVyCjEgSGlnaCBUaWRlCjEgSG9sZG91dCBTZXR0bGVtZW50CjEgSWNld2luZCBTdGFsd2FydAoxMCBJc2xhbmQKMSBKdXN0aWNpYXIncyBQb3J0YWwKMSBLaW5kbHkgQ3VzdG9tZXIKMSBMw7NyaWVuIFJldmVhbGVkCjEgTWVldGluZyBvZiBNaW5kcwoxIE1uZW1vbmljIFdhbGwKMSBNb21lbnRhcnkgQmxpbmsKMSBNdWRkbGUgdGhlIE1peHR1cmUKMSBNdWxsZHJpZnRlcgoxIE90aGVyd29ybGRseSBKb3VybmV5CjEgUGVnYXN1cyBHdWFyZGlhbgoxIFBlcmVncmluZSBEcmFrZQo3IFBsYWlucwoxIFBsYW5hciBJbmNpc2lvbgoxIFBvbmQgUHJvcGhldAoxIFByaXNtYXRpYyBTdHJhbmRzCjEgUmFkaWFudCBHcm92ZQoxIFNhbHZhZ2VyIG9mIFNlY3JldHMKMSBTY3JpdmVuZXIKMSBTY3JvbGxzaGlmdAoxIFNlYSBHYXRlIE9yYWNsZQoxIFNlbGVzbnlhIFNhbmN0dWFyeQoxIFNlcnVtIFZpc2lvbmFyeQoxIFNoaXB3cmVjayBEb3dzZXIKMSBTaGlyZSBUZXJyYWNlCjEgU2lic2lnIEFwcHJhaXNlcgoxIFNpbWljIEdyb3d0aCBDaGFtYmVyCjEgU2lyZW4ncyBSdXNlCjEgU2xpcCBPbiB0aGUgUmluZwoxIFNvdWwgV2FyZGVuCjEgU3Bpcml0ZWQgQ29tcGFuaW9uCjEgU3ByaW5nYmxvb20gRHJ1aWQKMSBTcHJpbmdsZWFmIERydW0KMSBTdGVwIFRocm91Z2gKMSBTdW5zY2FwZSBGYW1pbGlhcgoxIFN1cnZpdm9ycycgRW5jYW1wbWVudAoxIFN1dHVyZSBQcmllc3QKMSBUYW5nbGVkIElzbGV0CjEgVGVmZXJpJ3MgVGltZSBUd2lzdAoxIFRyYW5xdWlsIExhbmRzY2FwZQoxIFR1cm4gdG8gTWlzdAoxIFVuZXhwZWN0ZWQgQXNzaXN0YW5jZQoxIFV0b3BpYSBTcHJhd2wKMSBWZWRhbGtlbiBBZXRoZXJtYWdlCjEgV2lsZCBHcm93dGgKMSBXb29kIEVsdmVzCjEgU3BpZGVyLU1hbiwgQnJvb2tseW4gVmlzaW9uYXJ5CgoxIEJlbmRlcidzIFdhdGVyc2tpbgoxIEdlbmVyb3VzIEVudAoxIEdleXNlciBEcmFrZQoxIEguRS5SLkIuSS5FLiBTY291dCBVbml0CjEgTmFpYWQgb2YgSGlkZGVuIENvdmVzCjEgUmVhbGl0eSBSaXBwbGUKMSBTcGFjZXNoaWZ0CgoxIENvb2wgRmx1ZmZ5IExveG9kb24KMSBFdGVybmFsIEFjcm9iYXQgVG9hc3QKMSBGYW1pbGlhciBCZWVibGUgTWFzY290CjEgR2lhbnQgTWFuYSBDYWtlCjEgSGFwcHkgRGVhZCBTcXVpcnJlbAoxIFNhc3N5IEdyZW1saW4gQmxvb2QKMSBTbGlteSBCdXJyaXRvIElsbHVzaW9uCjEgU3F1aXNoeSBTcGhpbnggTmluamEKMSBUcmFpbmVkIEJsZXNzZWQgTWluZAoxIFlhd2dtb3RoIE1lcmZvbGsgU291bAoKMSBMYWdyZWxsYSwgdGhlIE1hZ3BpZQ&ref=cpdhguide" class="btn btn--primary btn--large" target="_blank" rel="noopener">Purchase on Manapool</a>

{% include deck-tech-cta.html %}
{% include author-card.html %}
{% include article-nav.html %}
