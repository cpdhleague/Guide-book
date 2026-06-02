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
    Submit a new episode. Once submitted it goes live on the site automatically.
    If you request Google News distribution, Patrik will review it first.
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
    <p class="submit-hint">The episode will be embedded directly on the page so visitors can listen without leaving the site.</p>
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

  <div class="submit-field">
    <div style="background:rgba(26,26,36,0.5);border:1px solid var(--border-subtle);border-radius:var(--radius-md);padding:1.2em 1.5em;">
      <label style="display:flex;align-items:flex-start;gap:12px;cursor:pointer;">
        <input type="checkbox" id="field-gnews" style="margin-top:3px;flex-shrink:0;width:18px;height:18px;cursor:pointer;">
        <div>
          <span style="font-family:var(--font-display);font-size:0.95em;font-weight:600;color:var(--pale);text-transform:uppercase;letter-spacing:0.05em;">
            Request Google News Distribution
          </span>
          <p style="font-size:0.85em;color:var(--dim);margin:6px 0 0;line-height:1.5;">
            To qualify for Google News, an episode needs a full written article attached — not just show notes.
            If you check this box, Patrik will review and expand the article before it goes out.
            We cannot guarantee all GNews requests will be approved. Contact Patrik directly with any questions.
          </p>
        </div>
      </label>
    </div>
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
      Submit Episode
    </button>
  </div>

</div>

<div id="success-message" style="display:none;margin-top:2em;" class="notice--success notice">
  <strong>Submitted!</strong> Your episode will be live on the site shortly.
  <span id="gnews-note"></span>
</div>

<div id="error-message" style="display:none;margin-top:2em;" class="notice--danger notice">
  <strong>Something went wrong.</strong> <span id="error-detail"></span>
  <br>Please try again or contact Patrik directly.
</div>

</div>

<script>
  var SUBMIT_PASSWORD = "pdhpod2026";
  var WORKER_URL = "YOUR_CLOUDFLARE_WORKER_URL_HERE";

  function handleSubmit() {
    var title   = document.getElementById('field-title').value.trim();
    var spotify = document.getElementById('field-spotify').value.trim();
    var excerpt = document.getElementById('field-excerpt').value.trim();
    var body    = document.getElementById('field-body').value.trim();
    var gnews   = document.getElementById('field-gnews').checked;
    var pw      = document.getElementById('sub-password').value;

    if (pw !== SUBMIT_PASSWORD) {
      document.getElementById('password-error').style.display = 'block';
      return;
    }
    document.getElementById('password-error').style.display = 'none';

    if (!title || !spotify || !body) {
      alert('Please fill in all required fields: Title, Spotify Link, and Show Notes.');
      return;
    }

    // Build the issue body.
    // The Python script searches all lines for the Spotify URL,
    // and parses KEY: value metadata lines from anywhere in the body.
    var issueBody = spotify + '\n';
    if (gnews)   issueBody += 'GNEWS: true\n';
    if (excerpt) issueBody += 'EXCERPT: ' + excerpt + '\n';
    issueBody += '\n' + body;

    var issueTitle = 'PDHpod: ' + title;

    var btn = document.getElementById('submit-btn');
    btn.textContent = 'Submitting...';
    btn.disabled = true;

    fetch(WORKER_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: issueTitle,
        body: issueBody,
        labels: gnews ? ['submission', 'pdhpod', 'gnews'] : ['submission', 'pdhpod']
      })
    })
    .then(function(response) {
      if (response.ok) {
        document.getElementById('form-wrap').style.display = 'none';
        var note = gnews
          ? ' Patrik will review it for Google News distribution before it goes live.'
          : '';
        document.getElementById('gnews-note').textContent = note;
        document.getElementById('success-message').style.display = 'block';
      } else {
        return response.json().then(function(data) {
          throw new Error(data.message || 'Error ' + response.status);
        });
      }
    })
    .catch(function(err) {
      btn.textContent = 'Submit Episode';
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
