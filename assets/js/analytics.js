/* ===================================================================
   CPDH.guide — Custom Analytics Layer
   Works WITH GoatCounter to add link-click and time-on-page tracking.
   
   HOW IT WORKS:
   GoatCounter handles the basics (page views, visitors, referrers,
   browsers, screen sizes, countries) automatically via its own script.
   
   This file adds TWO extra tracking features on top:
   
   1. LINK CLICK TRACKING
      Every time a user clicks a link (<a> tag), we send a custom
      "event" to GoatCounter. The event path looks like:
        click!{page-path}→{link-destination}
      For example, clicking the Moxfield link on the resources page:
        click!/resources/→https://moxfield.com
      
      GoatCounter shows these in its dashboard under "Events".
   
   2. TIME ON PAGE
      When the user leaves a page (navigates away or closes the tab),
      we calculate how many seconds they spent and send it as an event:
        time!{page-path}!{seconds}s
      For example:
        time!/articles/early_game/!47s
      
      This lets you see which articles keep readers engaged longest.

   IMPORTANT: Both features depend on GoatCounter being loaded first.
   The `window.goatcounter` object is created by GoatCounter's own
   script. We check for it before sending events to avoid errors.
   =================================================================== */

(function () {
  'use strict';

  // --- SETUP ---
  // Record the exact time this page loaded.
  // Date.now() returns milliseconds since Jan 1, 1970 (a "timestamp").
  var pageLoadTime = Date.now();

  // Get the current page path, e.g. "/articles/" or "/meta/"
  // window.location.pathname gives us just the path part of the URL.
  var currentPath = window.location.pathname;


  // --- 1. LINK CLICK TRACKING ---
  // We use "event delegation" here. Instead of attaching a listener
  // to every single <a> tag (which could be hundreds), we attach ONE
  // listener to the entire document. When any click happens, we check
  // if the clicked element was inside an <a> tag.
  //
  // WHY? Because:
  // a) It's more efficient (1 listener vs. hundreds)
  // b) It works for links added to the page AFTER this script runs
  //    (like links loaded dynamically via JavaScript)

  document.addEventListener('click', function (event) {
    // event.target = the exact element that was clicked (could be an
    // <img> inside an <a>, or a <span> inside an <a>, etc.)
    // .closest('a') walks UP the DOM tree to find the nearest <a> tag.
    // If the click wasn't inside any <a> tag, this returns null.
    var link = event.target.closest('a');

    // If no link was found, or if GoatCounter isn't loaded, bail out.
    if (!link) return;
    if (typeof window.goatcounter === 'undefined') return;
    if (typeof window.goatcounter.count !== 'function') return;

    // Get the link's destination URL.
    // link.href gives us the full resolved URL (even if the HTML
    // only had a relative path like "/articles/").
    var destination = link.href;
    if (!destination) return;

    // For readability in the dashboard, shorten internal links.
    // Instead of "https://cpdh.guide/articles/", just show "/articles/"
    try {
      var url = new URL(destination);
      // Check if this link points to our own site
      if (url.hostname === window.location.hostname) {
        destination = url.pathname; // Just the path
      } else {
        // External link: show the full domain + path
        destination = url.hostname + url.pathname;
      }
    } catch (e) {
      // If URL parsing fails (malformed href), just use whatever we got
    }

    // Send the event to GoatCounter.
    // The "path" field is what shows up in the GoatCounter dashboard.
    // Setting event:true tells GoatCounter this is a custom event,
    // not a regular page view.
    window.goatcounter.count({
      path: 'click!' + currentPath + '→' + destination,
      title: 'Link Click',
      event: true
    });
  });


  // --- 2. TIME ON PAGE TRACKING ---
  // We want to know: how many seconds did the user spend on this page?
  //
  // We use the "visibilitychange" event, which fires when the user
  // switches tabs or navigates away. This is MORE RELIABLE than
  // "beforeunload" (which browsers increasingly block/ignore).
  //
  // We also use "pagehide" as a backup for Safari/iOS.

  function sendTimeOnPage() {
    // Calculate seconds spent. Math.round() removes decimal places.
    var seconds = Math.round((Date.now() - pageLoadTime) / 1000);

    // Only send if they spent more than 2 seconds (filters out
    // accidental clicks / immediate bounces) and less than 30 minutes
    // (filters out abandoned tabs left open overnight).
    if (seconds < 3 || seconds > 1800) return;

    // Check GoatCounter is available
    if (typeof window.goatcounter === 'undefined') return;
    if (typeof window.goatcounter.count !== 'function') return;

    // Bucket the time into ranges for cleaner dashboard grouping.
    // Instead of "47s" and "48s" being separate entries, we group them.
    var bucket;
    if (seconds < 10) bucket = '0-10s';
    else if (seconds < 30) bucket = '10-30s';
    else if (seconds < 60) bucket = '30-60s';
    else if (seconds < 180) bucket = '1-3min';
    else if (seconds < 300) bucket = '3-5min';
    else if (seconds < 600) bucket = '5-10min';
    else bucket = '10min+';

    // Send the time event.
    window.goatcounter.count({
      path: 'time!' + currentPath + '!' + bucket,
      title: 'Time on Page',
      event: true
    });
  }

  // visibilitychange fires when the tab becomes hidden (user switches
  // tabs or navigates to a new page within the same tab).
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden') {
      sendTimeOnPage();
    }
  });

  // pagehide is the backup. On iOS Safari, visibilitychange doesn't
  // always fire reliably when the user closes a tab or switches apps.
  window.addEventListener('pagehide', sendTimeOnPage);

})();
// The (function(){ ... })() wrapper is called an IIFE — 
// "Immediately Invoked Function Expression". It runs the code inside
// right away, but keeps all our variables (pageLoadTime, currentPath, etc.)
// PRIVATE so they don't clash with other scripts on the page.
