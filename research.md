---
layout: default
title: (Selected) research & publications
---

I just list publications if I can be bothered to update the website and only list ones where I played a big role. Full list at [Google Scholar](https://scholar.google.com/citations?hl=en&user=FPfGzxoAAAAJ&view_op=list_works&sortby=pubdate).

<div class="pubs-list">
  {% assign current_year = "" %}
  {% for pub in site.data.publications %}
    {% if pub.year != current_year %}
      {% assign current_year = pub.year %}
      <h3 style="margin-top: 3rem; margin-bottom: 1.5rem; font-size: 1.1rem; font-weight: bold; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">{{ current_year }}</h3>
    {% endif %}
    
  <div class="pub-item" style="margin-bottom: 2rem;">
    <div style="font-size: 1rem;">
      <a href="{{ pub.url }}" target="_blank" style="font-weight: 500;">{{ pub.title }}</a>
    </div>
    <div style="font-size: 0.9rem; font-style: italic; color: #555; margin-bottom: 0.2rem;">{{ pub.venue }}</div>
    {% if pub.description %}
    <p style="margin: 0; font-size: 0.9rem; color: #444; line-height: 1.4;">{{ pub.description }}</p>
    {% endif %}
  </div>
  {% endfor %}
</div>

