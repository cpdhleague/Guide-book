"""
resolve_cards.py — Pre-resolve MTG card image URLs at build time
================================================================
Scans _posts/ and _previews/ for card references and resolves each one to a
direct Scryfall CDN image URL. Writes the results to two files:

  _data/cards.json          -> Jekyll reads this at build time (site.data.cards)
                               so card-grid.html can emit direct <img> URLs
  assets/data/cards.json    -> fetched once per page by the hover-tooltip JS

WHY THIS EXISTS:
Previously every card image and every hover tooltip made a live call to the
Scryfall API when the page loaded. An article with 15 cards fired 15 calls at
once, Scryfall rate-limited the burst, and images silently failed to load.
Resolving at build time means the browser makes ZERO API calls — the image URL
is already in the HTML, exactly like any other image on the site.

WHAT IT SCANS FOR:
  [[Card Name]]              -> article hover tooltips
  [[Card Name|back]]         -> back face of a double-faced card
  [[Card Name|token]]        -> token version
  {% include card-grid.html cards="A; B; C" %}
  The Commander column of _pages/meta/library.md

RATE LIMITING:
Scryfall asks for 50-100ms between requests. We use 120ms to be polite.
Only cards NOT already in _data/cards.json are looked up, so normal builds
resolve just the handful of new cards rather than the whole back catalogue.
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

SCRYFALL_NAMED = "https://api.scryfall.com/cards/named?fuzzy="
SCRYFALL_SEARCH = "https://api.scryfall.com/cards/search?q="
USER_AGENT = "cpdh-guide-build/1.0"
DELAY_SECONDS = 0.12

SCAN_DIRS = ["_posts", "_previews"]
EXTRA_FILES = ["_pages/meta/library.md"]

DATA_OUT = "_data/cards.json"
ASSET_OUT = "assets/data/cards.json"


# =============================================================
# EXTRACTION
# =============================================================

# [[Card Name]] or [[Card Name|back]] or [[Card Name|token]]
BRACKET_RE = re.compile(r"\[\[([^\]\|]+?)(?:\|(back|token))?\]\]")

# {% include card-grid.html cards="A; B; C" %}
GRID_RE = re.compile(r"card-grid\.html\s+cards=[\"']([^\"']+)[\"']")


def parse_grid_list(raw):
    """Split a card-grid cards="..." string the same way the Liquid include does."""
    parts = raw.split(";") if ";" in raw else raw.split(", ")
    out = []
    for part in parts:
        entry = part.strip()
        if not entry:
            continue
        if "|" in entry:
            name, _, opt = entry.partition("|")
            out.append((name.strip(), opt.strip().lower()))
        else:
            out.append((entry, ""))
    return out


def extract_from_text(text):
    """Return a set of (card_name, variant) tuples found in one file."""
    found = set()

    for match in BRACKET_RE.finditer(text):
        name = match.group(1).strip()
        variant = (match.group(2) or "").lower()
        if name:
            found.add((name, variant))

    for match in GRID_RE.finditer(text):
        for name, variant in parse_grid_list(match.group(1)):
            # Skip placeholder text left in draft articles
            if name.upper().startswith("CARD NAME"):
                continue
            found.add((name, variant))

    return found


def extract_library_commanders(text):
    """
    The library table lists commanders as plain text in the second <td> of each
    row. Split partner pairs and double-faced names on ' // ' and ' + '.
    """
    found = set()
    rows = re.findall(r"<tr>(.*?)</tr>", text, re.DOTALL | re.IGNORECASE)
    for row in rows:
        cells = re.findall(r"<td>(.*?)</td>", row, re.DOTALL | re.IGNORECASE)
        if len(cells) < 2:
            continue
        raw = re.sub(r"<[^>]+>", "", cells[1])           # strip any tags
        raw = raw.replace("[[", "").replace("]]", "").strip()
        if not raw:
            continue
        for piece in re.split(r" // | \+ ", raw):
            name = piece.strip()
            if name:
                found.add((name, ""))
    return found


def collect_all_cards():
    wanted = set()

    for directory in SCAN_DIRS:
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not filename.endswith((".md", ".markdown", ".html")):
                continue
            path = os.path.join(directory, filename)
            with open(path, "r", encoding="utf-8") as handle:
                wanted |= extract_from_text(handle.read())

    for path in EXTRA_FILES:
        if not os.path.isfile(path):
            continue
        with open(path, "r", encoding="utf-8") as handle:
            content = handle.read()
        wanted |= extract_from_text(content)
        if path.endswith("library.md"):
            wanted |= extract_library_commanders(content)

    return wanted


# =============================================================
# SCRYFALL LOOKUP
# =============================================================

def cache_key(name, variant):
    return f"{name.lower()}|{variant}" if variant else name.lower()


def fetch_json(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def pick_image(card_data, variant):
    """Choose the right image URL from a Scryfall card object."""
    faces = card_data.get("card_faces")
    if faces and len(faces) > 1:
        index = 1 if variant == "back" else 0
        face = faces[index]
        if face.get("image_uris"):
            return face["image_uris"].get("normal")
    if card_data.get("image_uris"):
        return card_data["image_uris"].get("normal")
    if faces and faces[0].get("image_uris"):
        return faces[0]["image_uris"].get("normal")
    return None


def resolve(name, variant):
    """Return {'name':..., 'image':...} or None if Scryfall can't find it."""
    try:
        if variant == "token":
            query = urllib.parse.quote(f'!"{name}" t:token')
            results = fetch_json(SCRYFALL_SEARCH + query)
            data_list = results.get("data") or []
            if not data_list:
                return None
            card_data = data_list[0]
        else:
            card_data = fetch_json(SCRYFALL_NAMED + urllib.parse.quote(name))
    except Exception as error:
        print(f"  MISS  {name} ({variant or 'front'}) -> {error}")
        return None

    image = pick_image(card_data, variant)
    if not image:
        print(f"  MISS  {name} ({variant or 'front'}) -> no image on card object")
        return None

    return {"name": card_data.get("name", name), "image": image}


# =============================================================
# MAIN
# =============================================================

def main():
    # Load the existing cache so we only look up genuinely new cards
    cache = {}
    if os.path.isfile(DATA_OUT):
        try:
            with open(DATA_OUT, "r", encoding="utf-8") as handle:
                cache = json.load(handle)
        except Exception:
            cache = {}

    wanted = collect_all_cards()
    print(f"Found {len(wanted)} card references across the site.")

    missing = [(n, v) for (n, v) in sorted(wanted) if cache_key(n, v) not in cache]
    print(f"{len(missing)} not yet cached. Resolving...")

    resolved_count = 0
    failed = []

    for name, variant in missing:
        entry = resolve(name, variant)
        if entry:
            cache[cache_key(name, variant)] = entry
            resolved_count += 1
            print(f"  OK    {name} ({variant or 'front'}) -> {entry['name']}")
        else:
            failed.append(f"{name} ({variant or 'front'})")
        time.sleep(DELAY_SECONDS)

    os.makedirs(os.path.dirname(DATA_OUT), exist_ok=True)
    os.makedirs(os.path.dirname(ASSET_OUT), exist_ok=True)

    payload = json.dumps(cache, indent=2, sort_keys=True, ensure_ascii=False)
    with open(DATA_OUT, "w", encoding="utf-8") as handle:
        handle.write(payload)
    with open(ASSET_OUT, "w", encoding="utf-8") as handle:
        handle.write(payload)

    print(f"\nResolved {resolved_count} new cards. Cache now holds {len(cache)}.")

    if failed:
        print("\nCards Scryfall could not find — check these names:")
        for item in failed:
            print(f"  - {item}")

    # Surface the unresolved list to the workflow so it can comment or warn
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as handle:
            handle.write(f"resolved={resolved_count}\n")
            handle.write(f"failed_count={len(failed)}\n")
            handle.write(f"failed_list={'; '.join(failed)}\n")

    # Never fail the build over an unresolvable card name
    return 0


if __name__ == "__main__":
    sys.exit(main())
