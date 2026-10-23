# _includes/icons

Drop downloaded `.svg` files here, one icon per file.

Jekyll inlines them into the page at build time:

    <span class="ico">{% include icons/trophy.svg %}</span>

The `.ico` wrapper (defined in `assets/css/main.scss`) sizes the icon in
`em` so it tracks the text beside it, and the SVG's `fill="currentColor"`
makes it take that text's colour. No extra network request, no icon
webfont, and it re-themes for free when the site's palette changes.

For someone else's brand mark, use `class="ico--brand"` on an `<img>`
instead — a logo should keep its own colours rather than inherit ours.

## In use

| File | Where | Iconify ID |
|---|---|---|
| `rules.svg` | Resources — PDH Rules | `material-symbols:rule-rounded` |
| `trophy.svg` | Resources — Decklist Library | `material-symbols:trophy-rounded` |
| `chart.svg` | Resources — Meta Analysis | `material-symbols:bar-chart-rounded` |
| `movie.svg` | Resources — Content Creators | `material-symbols:movie-outline` |
| `swords.svg` | Resources — Find a Tournament | `material-symbols:swords-rounded` |

Brand marks (not in this folder):

| File | Where |
|---|---|
| `assets/images/pdhrec.png` | Resources — PDHREC |

`movie.svg` is deliberately the outline variant while the rest are
rounded/filled. That mismatch is intentional — leave it.

`movie-filled-unused.svg` is the matching filled version, kept only in
case we ever want it. Safe to delete.

## Adding more

Icons came from [Iconify](https://icon-sets.iconify.design) — search,
pick a set, download SVG. Material Symbols is Apache 2.0.

- **SVG only.** Not PNG, not a webfont, not a React component.
- Name files by what the icon means **on our site**, not what the pack
  called it: `trophy.svg`, not `material-symbols--trophy-rounded.svg`.
  Record the original ID in the table above so future icons can match.
- Iconify exports already use `fill="currentColor"`, which is what we
  want. If an icon comes from elsewhere with a hardcoded `fill="#000"`
  or fixed `width`/`height`, strip those.

## Not icons

The crown in the Decklist Library is still an emoji. It marks the
commander in each row and is doing a real job there.
