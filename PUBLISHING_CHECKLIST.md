# CPDH.guide — Publishing Checklist

Copy this checklist for every article. Work top to bottom.

---

## BEFORE YOU START

- [ ] Copy `template.md` into `_posts/`
- [ ] Name the file: `YYYY-MM-DD-short-title-slug.md`
  - Example: `2026-05-26-deckbuilding-fundamentals.md`
  - Use today's date, all lowercase, hyphens not spaces, no special characters

---

## FRONT MATTER

- [ ] `title:` — compelling, specific, clickable. No clickbait, no ALL CAPS.
- [ ] `date:` — today's date in YYYY-MM-DD format
- [ ] `creator:` — one of: `guide` | `pdhpod` | `jalapenos`
- [ ] `author:` — key from `_data/authors.yml`, or `"First Last"` for guest authors
- [ ] `categories:` — exactly ONE from:
  - `Game Guides`
  - `Deck Tech`
  - `Videos`
  - `Community`
  - `Tournament Reports`
  - `Events`
- [ ] `front_page:` — `true` or `false`
  - `true` = eligible for homepage (reserve for strong, original content)
  - `false` = articles page only
- [ ] `hidden:` — `false` (only set `true` for drafts not ready to publish)
- [ ] `archive_only:` — `false` (set `true` for things like event recaps you want archived but not in the main feed)
- [ ] `gnews:` — `true` or `false`
  - `true` = will auto-post to Reddit, Discord, and Google News via RSS
  - `false` = site only
- [ ] `header.overlay_image:` — wide banner image (1200×630px or larger)
- [ ] `header.teaser:` — 16:9 thumbnail image (same image is fine)
- [ ] `excerpt:` — 1–2 plain sentences. No markdown, no quotes. Shows on homepage and in feeds.

---

## IMAGES

- [ ] All images uploaded to `assets/images/`
- [ ] File names: lowercase, no spaces (use hyphens): `my-image.jpg` not `My Image.jpg`
- [ ] Referenced with a leading slash: `/assets/images/my-image.jpg`
- [ ] Images in the article body sized appropriately:
  ```html
  <img src="/assets/images/name.jpg" alt="Description" style="width: 50%; display: block; margin: 0 auto;">
  ```

---

## ARTICLE BODY

- [ ] Opening paragraph is strong — hooks the reader immediately
- [ ] No "In this article, we will..." openers
- [ ] Section headings use `##` (H2)
- [ ] YouTube embeds use the iframe from YouTube's Share → Embed button
- [ ] Blockquotes use `>` for pull quotes
- [ ] `{% include author-card.html %}` is at the bottom of the content
- [ ] `{% include article-nav.html %}` is the very last line

---

## FINAL CHECKS

- [ ] Spell check the title and excerpt
- [ ] Read the excerpt aloud — does it make sense on its own?
- [ ] Check that the teaser image looks good at 16:9 (not weirdly cropped)

---

## PUBLISHING

```bash
git add .
git commit -m "Add: [article title here]"
git push
```

- [ ] Wait 1–3 minutes for GitHub Pages to rebuild
- [ ] Visit cpdh.guide and confirm the article is live
- [ ] Check the homepage if `front_page: true` — confirm it appears correctly
- [ ] If `gnews: true` — confirm it appears in https://cpdh.guide/gnews.xml

---

## FOR SUBMITTED CONTENT (PDHpod / Jalapenos)

When you receive a Formspree submission email:

- [ ] Create a new file in `_posts/` using `template.md`
- [ ] Fill in front matter from the email fields
- [ ] Paste the article body
- [ ] Set `creator:` to `pdhpod` or `jalapenos` as appropriate
- [ ] Add `{% include author-card.html %}` and `{% include article-nav.html %}` at the bottom
- [ ] Review for quality and formatting
- [ ] Publish using the steps above
