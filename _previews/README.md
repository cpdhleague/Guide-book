---
published: false
---

# _previews — draft articles

Put article `.md` files here to preview them before publishing.

**Drafts here are NOT:**
- on the homepage
- in `/articles/`
- in `gnews.xml` or `feed.xml`
- in the sitemap or search engines

**Drafts here ARE:**
- built and viewable at the secret preview URL
- publicly reachable by anyone who has that URL (obscurity, not access control)

## Filenames

No date prefix needed. `bilbo-deck-tech.md` becomes `/preview-92fk3a/bilbo-deck-tech/`.

## Front matter

Same as a normal post. `layout`, `classes`, and `sitemap: false` are applied
automatically by `_config.yml`, so you can omit those.

## Publishing

Move the file to `_posts/` and add a date prefix:

    _previews/bilbo-deck-tech.md  ->  _posts/2026-08-19-bilbo-deck-tech.md

That's the whole publish step. Nothing else to change.

## Rotating the secret URL

Edit the permalink in two places, keeping them identical:
1. `_config.yml` under `collections: previews:`
2. `_pages/preview-index.md` front matter `permalink:`
