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
    Use this form to submit a new episode for the site. Patrik will receive it
    by email, then review and publish it. You'll hear back within a few days.
  </p>
</div>

<form id="submission-form" action="https://formspree.io/f/mzdwogyv" method="POST" style="margin-top: 2em;">

  <input type="text" name="_gotcha" style="display:none">
  <input type="hidden" name="creator" value="pdhpod">
  <input type="hidden" name="author" value="pdhpod">
  <input type="hidden" name="category" value="Podcast">
  <input type="hidden" name="front_page" value="true">

  <div class="submit-field">
    <label class="submit-label">Episode Title *</label>
    <input type="text" name="title" class="submit-input" required
      placeholder="Ep 222 - Simic Combo Deep Dive">
    <p class="submit-hint">Format: Ep [number] - [Title In Title Case]</p>
  </div>

  <div class="submit-field">
    <label class="submit-label">Spotify Episode Link *</label>
    <input type="url" name="spotify_link" class="submit-input" required
      placeholder="https://open.spotify.com/episode/...">
  </div>

  <div class="submit-field">
    <label class="submit-label">Short Excerpt (1–2 sentences) *</label>
    <textarea name="excerpt" class="submit-input submit-textarea" required rows="3"
      placeholder="A short summary that appears on the homepage and article listings."></textarea>
  </div>

  <div class="submit-field">
    <label class="submit-label">Show Notes / Episode Description</label>
    <textarea name="body" class="submit-input submit-textarea" rows="10"
      placeholder="Paste your show notes or episode description here. Use ## for section headings if needed."></textarea>
  </div>

  <hr style="margin: 2em 0; border-color: var(--border-subtle);">

  <div class="submit-field">
    <label class="submit-label">Submission Password *</label>
    <input type="password" id="sub-password" class="submit-input"
      placeholder="Enter submission password" autocomplete="off">
    <p class="submit-hint" id="password-error" style="color: var(--danger); display: none;">
      ❌ Incorrect password. Contact Patrik if you've forgotten it.
    </p>
  </div>

  <div style="margin-top: 1.5em;">
    <button type="button" onclick="handleSubmit()" class="btn btn--primary btn--large">
      Submit for Review →
    </button>
  </div>

</form>

<div id="success-message" style="display:none; margin-top: 2em;" class="notice--success notice">
  ✅ <strong>Submitted!</strong> Patrik has been notified and will review your episode shortly.
</div>

</div>

<script>
  var SUBMIT_PASSWORD = "NosleevesBestsleeves";

  function handleSubmit() {
    var pw = document.getElementById('sub-password').value;
    var errorEl = document.getElementById('password-error');

    if (pw !== SUBMIT_PASSWORD) {
      errorEl.style.display = 'block';
      return;
    }
    errorEl.style.display = 'none';
    document.getElementById('submission-form').submit();
  }
</script>

<style>
.submit-field { margin-bottom: 1.5em; }
.submit-label {
  display: block;
  font-family: var(--font-display);
  font-size: 0.9em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--pale);
  margin-bottom: 0.5em;
}
.submit-input {
  width: 100%;
  background: var(--slate);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 0.7em 1em;
  color: var(--pale);
  font-family: var(--font-body);
  font-size: 1em;
  transition: border-color 0.2s ease;
  box-sizing: border-box;
}
.submit-input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px var(--primary-dim);
}
.submit-textarea { resize: vertical; min-height: 100px; }
.submit-hint { font-size: 0.82em; color: var(--dim); margin-top: 0.4em; }
</style>
