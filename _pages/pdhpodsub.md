---
title: "PDHpod Content Submission"
layout: splash
permalink: /pdhpodsub/
classes: wide
hidden: true
---

<div style="max-width: 800px; margin: 2em auto; padding: 0 20px;">

<div class="home-welcome" style="margin-top: 0;">
  <h2>PDHpod Submission Form</h2>
  <p style="color: var(--dim);">
    Submit a new episode. Patrik will receive a pull request to review —
    once he approves it, the article goes live automatically.
  </p>
</div>

<div id="form-wrap" style="margin-top: 2em;">

  <div class="submit-field">
    <label class="submit-label">Episode Title *</label>
    <input type="text" id="field-title" class="submit-input" required
      placeholder="Ep 222 - Simic Combo Deep Dive">
    <p class="submit-hint">Format: Ep [number] - [Title In Title Case]</p>
  </div>

  <div class="submit-field">
    <label class="submit-label">Spotify Episode Link *</label>
    <input type="url" id="field-spotify" class="submit-input" required
      placeholder="https://open.spotify.com/episode/...">
  </div>

  <div class="submit-field">
    <label class="submit-label">
      Short Excerpt
      <span style="color:var(--dim);font-weight:400;text-transform:none;font-size:0.9em;">(optional)</span>
    </label>
    <textarea id="field-excerpt" class="submit-input submit-textarea" rows="2"
      placeholder="1-2 sentence summary for the homepage and listings."></textarea>
  </div>

  <div class="submit-field">
    <label class="submit-label">Show Notes / Episode Description *</label>
    <textarea id="field-body" class="submit-input submit-textarea" rows="10" required
      placeholder="Paste your show notes here."></textarea>
  </div>

  <hr style="margin: 2em 0; border-color: var(--border-subtle);">

  <div class="submit-field">
    <label class="submit-label">Submission Password *</label>
    <input type="password" id="sub-password" class="submit-input"
      placeholder="Enter submission password" autocomplete="off">
    <p class="submit-hint" id="password-error" style="color:var(--danger);display:none;">
      Incorrect password. Contact Patrik if you have forgotten it.
    </p>
  </div>

  <div style="margin-top:1.5em;">
    <button type="button" onclick="handleSubmit()" id="submit-btn" class="btn btn--primary btn--large">
      Submit for Review
    </button>
  </div>

</div>

<div id="success-message" style="display:none;margin-top:2em;" class="notice--success notice">
  <strong>Submitted!</strong> Patrik has been notified via GitHub and will review shortly.
  Once he approves, the article goes live automatically.
</div>

<div id="error-message" style="display:none;margin-top:2em;" class="notice--danger notice">
  <strong>Something went wrong.</strong> <span id="error-detail"></span>
  <br>Please try again or contact Patrik directly.
</div>

</div>

<script>
  var SUBMIT_PASSWORD = "pdhpod2026";

  // Cloudflare Worker URL — the Worker holds the GitHub token securely server-side.
  // Replace this with your Worker URL once it is set up.
  var WORKER_URL = "https://pdhpodsub.gingerpersolus.workers.dev/";

  function handleSubmit() {
    var title   = document.getElementById('field-title').value.trim();
    var spotify = document.getElementById('field-spotify').value.trim();
    var excerpt = document.getElementById('field-excerpt').value.trim();
    var body    = document.getElementById('field-body').value.trim();
    var pw      = document.getElementById('sub-password').value;

    // Password check
    if (pw !== SUBMIT_PASSWORD) {
      document.getElementById('password-error').style.display = 'block';
      return;
    }
    document.getElementById('password-error').style.display = 'none';

    // Required field check
    if (!title || !spotify || !body) {
      alert('Please fill in all required fields (Title, Spotify Link, Show Notes).');
      return;
    }

    // Build the GitHub issue body.
    // Line 1 = Spotify link (the Python script expects this on line 1).
    // Optional EXCERPT line the script will parse out and use as the post excerpt.
    // Everything else becomes the article body, published exactly as written.
    var issueBody = spotify + '\n\n';
    if (excerpt) {
      issueBody += 'EXCERPT: ' + excerpt + '\n\n';
    }
    issueBody += body;

    var issueTitle = 'PDHpod: ' + title;

    var btn = document.getElementById('submit-btn');
    btn.textContent = 'Submitting...';
    btn.disabled = true;

    // Post to the Cloudflare Worker, which adds the GitHub token and
    // forwards the request to the GitHub Issues API.
    fetch(WORKER_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: issueTitle,
        body: issueBody,
        labels: ['submission', 'pdhpod']
      })
    })
    .then(function(response) {
      if (response.ok) {
        document.getElementById('form-wrap').style.display = 'none';
        document.getElementById('success-message').style.display = 'block';
      } else {
        return response.json().then(function(data) {
          throw new Error(data.message || 'Error ' + response.status);
        });
      }
    })
    .catch(function(err) {
      btn.textContent = 'Submit for Review';
      btn.disabled = false;
      document.getElementById('error-detail').textContent = err.message;
      document.getElementById('error-message').style.display = 'block';
    });
  }
</script>

<style>
.submit-field{margin-bottom:1.5em}
.submit-label{display:block;font-family:var(--font-display);font-size:.9em;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--pale);margin-bottom:.5em}
.submit-input{width:100%;background:var(--slate);border:1px solid var(--border-subtle);border-radius:var(--radius-sm);padding:.7em 1em;color:var(--pale);font-family:var(--font-body);font-size:1em;transition:border-color .2s ease;box-sizing:border-box}
.submit-input:focus{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px var(--primary-dim)}
.submit-textarea{resize:vertical;min-height:100px}
.submit-hint{font-size:.82em;color:var(--dim);margin-top:.4em}
</style>
