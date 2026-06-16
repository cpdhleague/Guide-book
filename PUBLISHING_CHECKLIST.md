# CPDH.guide — Publishing Checklist

Copy this checklist for every article. Work top to bottom.
Delete sections that don't apply (e.g. skip the GNews section if gnews: false).

---

## BEFORE YOU START

- [ ] Copy `template.md` into `_posts/`
- [ ] Rename it: `YYYY-MM-DD-short-title-slug.md`
  - Use today's date (or your scheduled future date — see Scheduled Publishing below)
  - All lowercase, hyphens not spaces, no special characters
  - Example: `2026-06-10-deckbuilding-fundamentals.md`
  - The filename date controls the URL — it does not need to match `date:` in the front matter, but keeping them consistent avoids confusion

---

## FRONT MATTER FIELDS

### title
- [ ] Compelling, specific, and clickable
- [ ] Use Title Case
- [ ] No ALL CAPS, no clickbait, no double quotes inside the title
- [ ] Keep under 70 characters where possible

### date
- [ ] Format: `YYYY-MM-DD`
- [ ] Use today's date for immediate publishing
- [ ] Use a future date for scheduled publishing (see Scheduled Publishing section below)
- [ ] Controls article sort order across the entire site

### creator
- [ ] Set to exactly ONE of:
  - `guide` — written by the CPDH.guide team
  - `pdhpod` — produced by The PDH Pod (set automatically by submission form)
  - `jalapenos` — produced by the Jalapeno Paupers (set automatically by submission form)

### author
- [ ] Set to exactly ONE of:
  - A key from `_data/authors.yml` — shows full author card (photo + bio + links)
    Current valid keys: `ginger` | `beachbodgod69` | `pdhpod` | `jalapenos`
  - `"First Last"` in quotes (with a space) — shows name-only guest card
  - Omit the field entirely — shows no author card at all
- [ ] If using a new author, add their profile to `_data/authors.yml` first

### categories
- [ ] Set to exactly ONE of:
  - `Game Guides` — strategy, mechanics, format education
  - `Deck Tech` — commander spotlight, decklist deep dives
  - `cPDH Deck Techs` — legacy value, treated the same as Deck Tech
  - `PDH Deck Techs` — legacy value, treated the same as Deck Tech
  - `Videos` — YouTube embeds, video content
  - `Podcast` — PDHpod episodes (set automatically by submission form)
  - `Community` — interviews, player spotlights, community highlights
  - `Tournament Reports` — event recaps, standings, winner interviews
  - `Events` — upcoming events, announcements
- [ ] Note: articles categorised as `Deck Tech`, `cPDH Deck Techs`, or `PDH Deck Techs`
      automatically show a "Submit Your Deck Tech" call-to-action banner at the
      bottom of the article. No extra steps needed — it's driven by the category.

### image (top-level)
- [ ] Full path to the article's main image: `/assets/images/your-image.jpg`
- [ ] This is what appears in Discord link previews, Reddit thumbnails,
      and all social sharing cards (the og:image meta tag)
- [ ] Should be 16:9 ratio, 1200px+ wide
- [ ] For PDHpod: set automatically to `/assets/images/pdhpod.png`
- [ ] For Jalapenos: set automatically to the downloaded YouTube thumbnail

### header.overlay_image
- [ ] The large banner at the top of the article page
- [ ] For most guide articles use the standard banner: `/assets/images/header2025-1.png`
- [ ] Should be wide (1200px+) and high resolution

### header.overlay_filter
- [ ] Controls the darkness of the overlay on the banner image
- [ ] `0.0` = no darkening (full image), `1.0` = completely black
- [ ] `0.5` is the standard — adjust if text is hard to read over the image

### header.teaser
- [ ] The thumbnail shown on homepage cards and the /articles/ listing grid
- [ ] Should be 16:9 ratio — use the same image as the top-level `image:` field
- [ ] For PDHpod: set automatically to `/assets/images/pdhpod.png`
- [ ] For Jalapenos: set automatically to the downloaded YouTube thumbnail

### front_page
- [ ] `true` — eligible for one of the 6 homepage slots
- [ ] `false` — appears on /articles/ only, never on homepage
- [ ] Note: PDHpod and Jalapenos are each capped at 1 slot on the homepage
      (the most recent of each). Older ones won't show if newer ones exist.

### hidden
- [ ] `false` — normal visible article (use this almost always)
- [ ] `true` — invisible in ALL listings but accessible by direct URL
      Use for drafts, unlisted content, or submission/utility pages

### archive_only
- [ ] `false` — appears everywhere normally (use this almost always)
- [ ] `true` — appears only in the category archive, not on /articles/ or homepage
      Use for older event recaps or content you want archived but not featured

### gnews
- [ ] `false` — site only, no external distribution
- [ ] `true` — article appears in /gnews.xml RSS feed, which feeds:
      Google News, Reddit auto-posting (if reddit_text is set), Discord
- [ ] REQUIRES: `excerpt:` to be filled in (feeds look broken without it)
- [ ] REQUIRES: a real image in both `image:` and `header.teaser:`
- [ ] REQUIRES: `reddit_text:` if you want Reddit posting

### excerpt
- [ ] 1–2 plain sentences summarising the article
- [ ] No markdown formatting (no **bold**, no [links], no #headers)
- [ ] No double quotes inside — use single quotes if needed
- [ ] Keep under 160 characters for best feed display
- [ ] Write it as a standalone sentence — it appears without surrounding context
- [ ] REQUIRED if `gnews: true`
- [ ] REQUIRED if `front_page: true` — homepage cards show this text

### reddit_text
- [ ] This field is the COMPLETE on/off switch for Reddit posting
- [ ] Present and filled → posts to r/pauperEDH and r/competitivepauperedh
      as a link post, with this text added as a comment to start discussion
- [ ] Absent or empty → article is NOT posted to Reddit (no other changes needed)
- [ ] For PDHpod and Jalapenos: templates are applied automatically by the
      GitHub Action — only needed here for guide articles
- [ ] Template for guide articles (write something specific to THIS article):
      "We've been thinking about X a lot lately. What's your take?"
      "This challenges the conventional wisdom on Y — agree or disagree?"

---

## IMAGES

- [ ] All images uploaded to `assets/images/`
- [ ] File names: lowercase, hyphens not spaces (`my-image.jpg` not `My Image.jpg`)
- [ ] Reference with a leading slash: `/assets/images/my-image.jpg`
- [ ] Inline body images:
  ```html
  <img src="/assets/images/name.jpg" alt="Description" style="width:100%; display:block; margin:0 auto;">
  ```

---

## MANA SYMBOLS

Mana costs and symbols are automatic — just write them in standard Magic bracket
notation anywhere in your article body. The page converts them to real icons.

| Type | Notation | Notes |
|------|----------|-------|
| Basic mana | `{W}` `{U}` `{B}` `{R}` `{G}` | White Blue Black Red Green |
| Colourless | `{C}` | |
| Generic | `{0}` `{1}` `{2}` ... `{10}` ... `{20}` | |
| Variable | `{X}` | |
| Tap / Untap | `{T}` `{Q}` | |
| Snow | `{S}` | |
| Hybrid | `{W/U}` `{U/B}` `{B/R}` `{R/G}` `{G/W}` | Allied pairs |
| Hybrid | `{W/B}` `{U/R}` `{B/G}` `{R/W}` `{G/U}` | Enemy pairs |
| 2-hybrid | `{2/W}` `{2/U}` `{2/B}` `{2/R}` `{2/G}` | |
| Phyrexian | `{W/P}` `{U/P}` `{B/P}` `{R/P}` `{G/P}` | |

**Examples in prose:**
- `Ayli, Eternal Pilgrim costs {W}{B}` → renders with real white and black mana symbols
- `This commander costs {4}{W}{U}` → renders with a 4 and white/blue symbols
- `{T}: Add {G}` → renders tap symbol and green mana

**Note:** `{B}` in plain prose can look like a variable name out of context.
Where clarity matters, write it as `black mana ({B})` so readers understand before the symbol renders.

**Inside code blocks** (`\`like this\``), symbols are intentionally left as raw text
and not converted — safe to use for code examples in technical articles.

---

## CARD HOVER TOOLTIPS

Wrap any Magic card name in `[[double brackets]]` to make it interactive.
On desktop, hovering shows the card image floating near your cursor.
On mobile, tapping toggles the image; tapping anywhere else closes it.

**Syntax:** `[[Card Name]]`

**Examples in prose:**
```
...the power of [[Ayli, Eternal Pilgrim]] in this shell...
...pairing [[Mystic Remora]] with [[Rhystic Study]] is redundant...
...[[Jeska's Will]] generates absurd value here...
```

**Notes:**
- Spelling just needs to be close — Scryfall's fuzzy search finds the card
  (`[[ayli pilgrim]]` finds Ayli, Eternal Pilgrim correctly)
- Double-faced cards automatically show the front face
- If a card name isn't found, it displays as plain highlighted text (no crash)
- Inside \`code blocks\`, double brackets render as raw text — safe for technical writing
- No setup needed — just write the syntax and it works

---

## ARTICLE BODY

- [ ] Opening paragraph hooks the reader — no "In this article we will..."
- [ ] Section headings use `##` (H2), sub-sections use `###` (H3)
- [ ] YouTube embeds use the iframe from YouTube's Share → Embed button
- [ ] Blockquotes use `>` for pull quotes
- [ ] Section dividers use `{% include divider.html %}` — renders a short purple accent line
- [ ] `{% include deck-tech-cta.html %}` is present before the author card
      (outputs nothing on non-deck-tech articles — safe to include on every article)
- [ ] `{% include author-card.html %}` is after the deck-tech-cta
- [ ] `{% include article-nav.html %}` is the very last line

Correct order for the bottom of every article:
```
{% include deck-tech-cta.html %}
{% include author-card.html %}
{% include article-nav.html %}
```

---

## FINAL CHECKS

- [ ] Spell check the title and excerpt
- [ ] Read the excerpt aloud — does it make sense on its own?
- [ ] Teaser image looks good at 16:9 (not awkwardly cropped)
- [ ] If `gnews: true`: excerpt is filled in, image is real (not a placeholder)
- [ ] If `reddit_text:` is set: the text reads well as a standalone Reddit comment

---

## PUBLISHING (immediate)

```bash
git add .
git commit -m "Add: [article title here]"
git push
```

- [ ] Wait 1–3 minutes for GitHub Pages to rebuild
- [ ] Visit cpdh.guide — confirm the article is live
- [ ] If `front_page: true` — check homepage, confirm it appears correctly
- [ ] If `gnews: true` — check https://cpdh.guide/gnews.xml, confirm it appears
- [ ] If `reddit_text:` is set — check r/pauperEDH and r/competitivepauperedh

---

## SCHEDULED PUBLISHING (future date)

To schedule an article to go live on a specific future date:

1. Set `date:` in the front matter to the target date (e.g. `date: 2026-07-04`)
2. Name the file with the same target date (e.g. `2026-07-04-my-article.md`)
3. Push to GitHub as normal — the article is silently held back
4. A GitHub Action rebuilds the site automatically every day at 6 AM UTC
5. On the morning of the target date, the rebuild will include the article
   and it will go live without any further action from you

- [ ] `date:` in front matter set to the target date
- [ ] Filename also uses the target date
- [ ] Article pushed to GitHub before the target date
- [ ] No further action needed — the daily rebuild handles it

Note: if you need the article live at a precise time (not just "sometime on that day"),
push a manual commit after 6 AM UTC on the target date instead of relying on the schedule.

---

## FOR SUBMITTED CONTENT (PDHpod / Jalapenos via GitHub Issues)

PDHpod and Jalapenos submit content via the submission forms at /pdhpodsub/ and /jalapenosub/.
The GitHub Action processes these automatically. Patrik's role depends on the submission type:

### Standard submissions (gnews: false)
- Article is generated and published automatically — no action needed
- [ ] Spot-check the live article looks correct
- [ ] If anything needs fixing, edit the generated file in `_posts/` and push

### GNews submissions (gnews: true — submitter ticked the GNews checkbox)
- A Pull Request is created for review instead of auto-publishing
- [ ] Go to github.com/cpdhleague/Guide-book/pulls
- [ ] Review the generated article (check formatting, excerpt, image)
- [ ] Fill in `reddit_text:` in the front matter if Reddit posting is wanted
- [ ] Merge the PR to publish
- [ ] Confirm article appears in https://cpdh.guide/gnews.xml after rebuild
