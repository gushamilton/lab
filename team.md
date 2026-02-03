---
layout: default
title: Team
description: "Meet the research team at Fergus Hamilton's lab."
---

<div class="grid">
  {% for member in site.data.team %}
  <div class="card">
    {% if member.image %}
    <img src="{{ member.image | relative_url }}" alt="{{ member.name }}">
    {% endif %}
    <div class="card-content">
      <h3>{{ member.name }}</h3>
      <span class="role">{{ member.role }}</span>
      <p>{{ member.bio }}</p>
      {% if member.links %}
        <p>
        {% for link in member.links %}
          <a href="{{ link.url }}">{{ link.title }}</a>{% unless forloop.last %} · {% endunless %}
        {% endfor %}
        </p>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

## Join Us
We are always looking for new PhD students and postdocs. If you are interested in our work, please email [fergus.hamilton@bristol.ac.uk](mailto:fergus.hamilton@bristol.ac.uk).
