---
title: "Jalapeno Paupers Content Submission"
layout: splash
permalink: /jalapenosub/
classes: wide
hidden: true
---

<div style="max-width: 800px; margin: 2em auto; padding: 0 20px;">

<div class="home-welcome" style="margin-top: 0;">
  <h2>Jalapeno Paupers Submission Form</h2>
  <p style="color: var(--dim);">
    Use this form to submit your content for review. Patrik will receive it by email,
    then review, format, and publish it. You'll hear back within a few days.
  </p>
</div>

<form id="submission-form" action="YOUR_FORMSPREE_ENDPOINT_HERE" method="POST" style="margin-top: 2em;">

  <input type="text" name="_gotcha" style="display:none">
  <input type="hidden" name="creator" value="jalapenos">

  <div class="submit-field">
    <label class="submit-label">Episode / Content Title *</label>
    <input type="text" name="title" class="submit-input" required
      placeholder="e.g. Jalapenos Rate Top 10 Avatar Commanders">
  </div>

  <div class="submit-field">
    <label class="submit-label">Your Name / Handle *</label>
    <input type="text" name="author" class="submit-input" required placeholder="e.g. Jalapeno Paupers">
  </div>

  <div class="submit-field">
    <label class="submit-label">YouTube / Video Link (if applicable)</label>
    <input type="url" name="video_link" class="submit-input"
      placeholder="https://youtube.com/watch?v=...">
  </div>

  <div class="submit-field">
    <label class="submit-label">Thumbnail Image URL</label>
    <input type="url" name="thumbnail" class="submit-input"
      placeholder="https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg">
    <p class="submit-hint">
      For YouTube thumbnails: https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg
    </p>
  </div>

  <div class="submit-field">
    <label class="submit-label">Short Excerpt (1–2 sentences) *</label>
    <textarea name="excerpt" class="submit-input submit-textarea" required rows="3"
      placeholder="A short summary that appears on the homepage and article listings."></textarea>
  </div>

  <div class="submit-field">
    <label class="submit-label">Article Body</label>
    <textarea name="body" class="submit-input submit-textarea" rows="12"
      placeholder="Write your article content here. Use ## for section headings. Leave blank if this is a video-only post."></textarea>
  </div>

  <div class="submit-field">
    <label class="submit-label">Category</label>
    <select name="category" class="submit-input">
      <option value="Videos">Videos</option>
      <option value="Community">Community</option>
      <option value="Game Guides">Game Guides</option>
      <option value="Deck Tech">Deck Tech</option>
      <option value="Tournament Reports">Tournament Reports</option>
    </select>
  </div>

  <div class="submit-field">
    <label class="submit-label">Request Homepage Feature?</label>
    <select name="front_page" class="submit-input">
      <option value="true">Yes — please feature on homepage</option>
      <option value="false">No — articles page only</option>
    </select>
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
  ✅ <strong>Submitted!</strong> Patrik has been notified and will review your content shortly.
</div>

</div>

<script>
  // Change this password whenever you want. Keep it simple — it's just to keep the URL semi-private.
  var SUBMIT_PASSWORD = "jalapenos2026";

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
select.submit-input { cursor: pointer; }
</style>
