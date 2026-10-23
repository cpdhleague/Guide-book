---
title: "Events"
layout: splash
permalink: /events/
classes: short-header wide
hidden: true
header:
  overlay_image: /assets/images/header2025-1.png
  overlay_filter: 0.5
  title: "Events"
  excerpt: "Upcoming cPDH events, tournaments, and community gatherings."
---

<div style="max-width: 1200px; margin: 0 auto;">

{% assign all_events = site.data.events | sort: "date" %}
{% assign today = "now" | date: "%Y-%m-%d" %}
{% assign future_events = "" | split: "" %}
{% assign past_events   = "" | split: "" %}

{% for event in all_events %}
  {% assign event_date_str = event.date | date: "%Y-%m-%d" %}
  {% if event_date_str >= today %}
    {% assign future_events = future_events | push: event %}
  {% else %}
    {% assign past_events = past_events | push: event %}
  {% endif %}
{% endfor %}

{% if future_events.size > 0 %}
<h3 class="archive__subtitle" style="margin-top: 0;">Upcoming Events</h3>
<div class="events-grid">
  {% for event in future_events %}
  <div class="event-card">
    <div class="event-card__date">
      <span class="event-card__month">{{ event.date | date: "%b" | upcase }}</span>
      <span class="event-card__day">{{ event.date | date: "%-d" }}</span>
    </div>
    <div class="event-card__body">
      <h3 class="event-card__title">{{ event.title }}</h3>
      <div class="event-card__location">
        {% if event.online %}
          <span class="event-badge event-badge--online"><span class="ico">{% include icons/online.svg %}</span>Online</span>
          {{ event.location }}
        {% else %}
          <span class="event-badge event-badge--local"><span class="ico" style="margin-right:0">{% include icons/location.svg %}</span></span>
          {{ event.location }}
        {% endif %}
      </div>
      {% if event.description %}
        <p class="event-card__desc">{{ event.description }}</p>
      {% endif %}
      {% comment %} Empty strings are truthy in Liquid, so a placeholder link: ""
         would render a button pointing at nothing. Test for both. {% endcomment %}
      {% if event.link and event.link != "" %}
        <a href="{{ event.link }}" class="btn btn--primary" target="_blank" rel="noopener">Details / Info</a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>
{% else %}
<p style="color: var(--dim); font-style: italic; margin-top: 1em;">
  No upcoming events scheduled. Check back soon or join the
  <a href="https://discord.com/invite/UtgN272kpq">Discord</a> for announcements.
</p>
{% endif %}

{% if past_events.size > 0 %}
<hr style="margin: 3em 0;">
<h3 class="archive__subtitle">Past Events</h3>
<div class="events-grid">
  {% assign past_reversed = past_events | reverse %}
  {% for event in past_reversed %}
  <div class="event-card event-card--past">
    <div class="event-card__date">
      <span class="event-card__month">{{ event.date | date: "%b" | upcase }}</span>
      <span class="event-card__day">{{ event.date | date: "%-d" }}</span>
    </div>
    <div class="event-card__body">
      <h3 class="event-card__title">{{ event.title }}</h3>
      <div class="event-card__location">
        {% if event.online %}
          <span class="ico">{% include icons/online.svg %}</span>Online &mdash; {{ event.location }}
        {% else %}
          <span class="ico">{% include icons/location.svg %}</span>{{ event.location }}
        {% endif %}
      </div>
      {% if event.link and event.link != "" %}
        <a href="{{ event.link }}" class="btn btn--inverse" target="_blank" rel="noopener">View Details</a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>
{% endif %}

</div>
