---
title: "Link Usage"
layout: splash
permalink: /link-usage-8c2f/
classes: short-header wide
hidden: true
sitemap: false
noindex: true
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.6
---

<div style="max-width: 900px; margin: 0 auto;">

<div class="home-welcome" style="margin-top: 0;">
  <h2>Link Usage</h2>
  <p style="color: var(--dim); margin-bottom: 0;">
    Click counts for the footer social icons and the masthead logo. Collected
    so we can decide at the end of the year whether Font Awesome &mdash; about
    344KB of CSS and webfonts on every page &mdash; is worth keeping for five
    icons. Nothing here identifies a visitor: each row is a label, a page path
    and a timestamp.
  </p>
</div>

<div id="lu-state" style="color: var(--dim); font-style: italic; margin: 2em 0;">
  Loading counts&hellip;
</div>

<div id="lu-body" hidden>
  <h3 class="archive__subtitle">Total clicks per link</h3>
  <table>
    <thead>
      <tr><th>Link</th><th style="text-align:right">Clicks</th><th>First seen</th><th>Last seen</th></tr>
    </thead>
    <tbody id="lu-rows"></tbody>
  </table>

  <h3 class="archive__subtitle" style="margin-top:2.5em;">By month</h3>
  <div style="overflow-x:auto;">
    <table>
      <thead><tr id="lu-mhead"><th>Link</th></tr></thead>
      <tbody id="lu-mrows"></tbody>
    </table>
  </div>

  <p style="color: var(--dim); font-size: 0.85em; margin-top: 2em;" id="lu-foot"></p>
</div>

</div>

<script>
(function () {
  'use strict';

  var NAMES = {
    'footer-youtube':  'Footer — YouTube',
    'footer-discord':  'Footer — Discord',
    'footer-reddit':   'Footer — Reddit',
    'footer-moxfield': 'Footer — Moxfield',
    'footer-rss':       'Footer — RSS feed',
    'masthead-logo':    'Masthead — logo image',
    'masthead-wordmark':'Masthead — CPDH.guide wordmark'
  };
  var ALL = Object.keys(NAMES);

  function fmt(ms) {
    if (!ms) return '—';
    return new Date(ms).toLocaleDateString('en-US',
      { year: 'numeric', month: 'short', day: 'numeric' });
  }

  function render(data) {
    var byLabel = {};
    (data.labels || []).forEach(function (r) { byLabel[r.label] = r; });

    // Show every tracked link, including ones with zero clicks. A link nobody
    // has ever used is exactly the finding we are looking for, and it would be
    // invisible if we only listed rows the database returned.
    var rows = ALL.map(function (l) {
      var r = byLabel[l] || { label: l, count: 0, first: null, last: null };
      return r;
    }).sort(function (a, b) { return b.count - a.count; });

    var total = rows.reduce(function (s, r) { return s + r.count; }, 0);

    document.getElementById('lu-rows').innerHTML = rows.map(function (r) {
      var zero = r.count === 0;
      return '<tr' + (zero ? ' style="opacity:.55"' : '') + '>' +
        '<td>' + (NAMES[r.label] || r.label) + '</td>' +
        '<td style="text-align:right;font-variant-numeric:tabular-nums">' +
          r.count + (zero ? ' <span style="color:var(--warning)">never used</span>' : '') +
        '</td>' +
        '<td>' + fmt(r.first) + '</td>' +
        '<td>' + fmt(r.last) + '</td>' +
      '</tr>';
    }).join('');

    // Monthly grid
    var months = [];
    (data.monthly || []).forEach(function (m) {
      if (months.indexOf(m.month) === -1) months.push(m.month);
    });
    months.sort();

    var head = document.getElementById('lu-mhead');
    head.innerHTML = '<th>Link</th>' + months.map(function (m) {
      return '<th style="text-align:right">' + m + '</th>';
    }).join('');

    var grid = {};
    (data.monthly || []).forEach(function (m) {
      grid[m.label + '|' + m.month] = m.count;
    });

    document.getElementById('lu-mrows').innerHTML = rows.map(function (r) {
      return '<tr><td>' + (NAMES[r.label] || r.label) + '</td>' +
        months.map(function (m) {
          var v = grid[r.label + '|' + m] || 0;
          return '<td style="text-align:right;font-variant-numeric:tabular-nums' +
                 (v ? '' : ';opacity:.4') + '">' + v + '</td>';
        }).join('') + '</tr>';
    }).join('');

    document.getElementById('lu-foot').textContent =
      total + ' clicks recorded in total. Counts update within five minutes.';

    document.getElementById('lu-state').hidden = true;
    document.getElementById('lu-body').hidden = false;
  }

  fetch('https://cards.cpdh.guide/click/stats')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(render)
    .catch(function (err) {
      document.getElementById('lu-state').innerHTML =
        'Could not load counts (' + err.message + '). ' +
        'If this is the first run, check that the <code>/click/stats</code> route ' +
        'and the <code>CLICKS</code> D1 binding are both live on the Worker.';
    });
})();
</script>
