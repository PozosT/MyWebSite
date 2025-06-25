---
title: "All News"
layout: gridlay
sitemap: false
permalink: /allnews/
---

# All News

<ul>
{% for news in site.data.news %}
  <li>
    <a href="{{ site.baseurl }}/news/{{ news.slug }}">{{ news.title }}</a> - {{ news.date }}
  </li>
{% endfor %}
</ul>
