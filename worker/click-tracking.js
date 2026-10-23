// ===========================================================================
// LINK USAGE TRACKING — Worker routes
// ===========================================================================
// This is a reference copy. The live code lives in the Cloudflare dashboard
// Worker that already serves cards.cpdh.guide (/card and /card-image, plus
// the submission POST handler). Keep this file in sync by hand when you
// change the Worker, so the logic is in version control rather than only in
// a browser tab.
//
// SETUP (once):
//
//   1. Cloudflare dashboard -> Storage & Databases -> D1 -> Create database
//      Name it:  cpdh-clicks
//
//   2. Open its Console tab and run:
//
//        CREATE TABLE clicks (
//          id    INTEGER PRIMARY KEY AUTOINCREMENT,
//          label TEXT    NOT NULL,
//          path  TEXT,
//          ts    INTEGER NOT NULL
//        );
//        CREATE INDEX idx_clicks_label ON clicks(label);
//        CREATE INDEX idx_clicks_ts    ON clicks(ts);
//
//   3. Worker -> Settings -> Bindings -> Add -> D1 database
//      Variable name:  CLICKS
//      Database:       cpdh-clicks
//
//   4. Paste the two route blocks below into the Worker's fetch handler,
//      above the existing /card and /card-image handling.
//
// WHY D1 AND NOT KV:
//   A KV counter needs read-modify-write, so two clicks landing together can
//   lose one. D1 takes an append-only INSERT with no such race, and keeping a
//   timestamp per row means you can ask "was this used more in March than in
//   October" at the end of the year instead of only seeing one running total.
//
// FREE TIER:
//   D1 allows 100,000 writes/day. This site will not come close.
// ===========================================================================

// --- Route 1: record a click -----------------------------------------------
// POST /click   body: {"label":"footer-discord","path":"/articles/"}
//
// The beacon is sent as text/plain so it does not trigger a CORS preflight
// during page unload, so we parse the text ourselves rather than using
// request.json().

if (url.pathname === '/click' && request.method === 'POST') {
  try {
    const body = JSON.parse(await request.text());
    const label = String(body.label || '').slice(0, 64);
    const path = String(body.path || '').slice(0, 200);

    // Only accept labels we expect. Without this, the endpoint is an open
    // write to our database for anyone who finds the URL.
    const ALLOWED = [
      'footer-youtube', 'footer-discord', 'footer-reddit',
      'footer-moxfield', 'footer-rss',
      'masthead-logo', 'masthead-wordmark'
    ];
    if (!ALLOWED.includes(label)) {
      return new Response(null, { status: 204, headers: CORS });
    }

    await env.CLICKS.prepare(
      'INSERT INTO clicks (label, path, ts) VALUES (?, ?, ?)'
    ).bind(label, path, Date.now()).run();
  } catch (err) {
    // Never fail loudly: a tracking error must not surface to the visitor.
  }
  // 204 regardless — sendBeacon ignores the response anyway.
  return new Response(null, { status: 204, headers: CORS });
}

// --- Route 2: read the totals ----------------------------------------------
// GET /click/stats  ->  {"total":123,"since":...,"labels":[{label,count,last}]}

if (url.pathname === '/click/stats' && request.method === 'GET') {
  const rows = await env.CLICKS.prepare(
    `SELECT label,
            COUNT(*)  AS count,
            MIN(ts)   AS first,
            MAX(ts)   AS last
       FROM clicks
      GROUP BY label
      ORDER BY count DESC`
  ).all();

  const monthly = await env.CLICKS.prepare(
    `SELECT label,
            strftime('%Y-%m', ts / 1000, 'unixepoch') AS month,
            COUNT(*) AS count
       FROM clicks
      GROUP BY label, month
      ORDER BY month ASC`
  ).all();

  return new Response(JSON.stringify({
    labels: rows.results,
    monthly: monthly.results,
    generated: Date.now()
  }), {
    headers: { ...CORS, 'Content-Type': 'application/json',
               'Cache-Control': 'max-age=300' }
  });
}

// --- CORS header used by both routes ---------------------------------------
// Defined near the top of the Worker alongside the existing handlers.
//
// const CORS = {
//   'Access-Control-Allow-Origin':  'https://cpdh.guide',
//   'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
//   'Access-Control-Allow-Headers': 'Content-Type'
// };
