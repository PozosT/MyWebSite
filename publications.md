---
title: "Publications"
layout: gridlay
sitemap: false
permalink: /publications/
---

# Publications

{% assign total_pubs = site.publications | size %}

<div class="container-fluid px-0 mb-5">

  <!-- Stats bar -->
  <div class="row g-3 mb-4">
    <div class="col-sm-4">
      <div class="text-center p-3 rounded" style="background:#eaf0fb;">
        <div style="font-size:2rem;font-weight:700;color:#2c3e50;">{{ total_pubs }}</div>
        <div class="text-muted small">Total publications</div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="text-center p-3 rounded" style="background:#eafaf1;">
        {% assign journal_count = 0 %}
        {% for publi in site.publications %}
          {% unless publi.display contains 'Conference' or publi.display contains 'Proc' or publi.display contains 'Workshop' %}
            {% assign journal_count = journal_count | plus: 1 %}
          {% endunless %}
        {% endfor %}
        <div style="font-size:2rem;font-weight:700;color:#27ae60;">{{ journal_count }}</div>
        <div class="text-muted small">Journal articles</div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="text-center p-3 rounded" style="background:#fef9e7;">
        {% assign conf_count = total_pubs | minus: journal_count %}
        <div style="font-size:2rem;font-weight:700;color:#f39c12;">{{ conf_count }}</div>
        <div class="text-muted small">Conference papers</div>
      </div>
    </div>
  </div>

  <!-- Publications per year chart -->
  <div class="card border-0 shadow-sm mb-5">
    <div class="card-body p-4">
      <h5 class="mb-3" style="color:#2c3e50;">Publications per year</h5>
      <canvas id="pubChart" height="90"></canvas>
    </div>
  </div>

</div>

{% for myyear in site.data.years %}
{% assign yeartest = false %}
{% for publi in site.publications %}
  {% if publi.year == myyear.year %}{% assign yeartest = true %}{% endif %}
{% endfor %}

{% if yeartest == true %}
<h2 class="pub-year-heading">{{ myyear.year }}</h2>

{% for publi in site.publications %}
{% if publi.year == myyear.year %}

<div class="pub-card">
  <div class="pub-body">
    <div class="pub-title">
      {% if publi.doi %}<a href="http://doi.org/{{ publi.doi }}" target="_blank">{{ publi.title }}</a>
      {% elsif publi.pdf %}<a href="{{ site.baseurl }}/publications/{{ publi.pdf }}.pdf" target="_blank">{{ publi.title }}</a>
      {% else %}{{ publi.title }}
      {% endif %}
    </div>
    <div class="pub-authors">{{ publi.authors }}</div>
    <div class="pub-venue">
      <i class="fas fa-book-open me-1"></i><em>{{ publi.display }}</em>{% if publi.year %}, {{ publi.year }}{% endif %}
    </div>
    <div class="pub-buttons mt-2">
      {% if publi.abstract %}
      <a class="pub-btn pub-btn-abstract" data-bs-toggle="collapse" href="#abs-{{ forloop.index }}-{{ myyear.year }}" role="button">Abstract</a>
      {% endif %}
      {% if publi.pdf %}
      <a href="{{ site.baseurl }}/publications/{{ publi.pdf }}.pdf" target="_blank" class="pub-btn pub-btn-pdf"><i class="fas fa-file-pdf me-1"></i>PDF</a>
      {% endif %}
      {% if publi.doi %}
      <a href="http://doi.org/{{ publi.doi }}" target="_blank" class="pub-btn pub-btn-doi"><i class="fas fa-external-link-alt me-1"></i>DOI</a>
      {% endif %}
      {% if publi.arxiv %}
      <a href="https://arxiv.org/abs/{{ publi.arxiv }}" target="_blank" class="pub-btn pub-btn-arxiv">arXiv</a>
      {% endif %}
      {% if publi.code %}
      <a href="{{ publi.code }}" target="_blank" class="pub-btn pub-btn-code"><i class="fab fa-github me-1"></i>Code</a>
      {% endif %}
    </div>
    {% if publi.abstract %}
    <div class="collapse mt-2" id="abs-{{ forloop.index }}-{{ myyear.year }}">
      <div class="pub-abstract">{{ publi.abstract }}</div>
    </div>
    {% endif %}
  </div>
</div>

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}

<p class="mt-4 text-muted small">
  <i class="fas fa-download me-1"></i>
  Download full BibTeX file <a href="{{ site.baseurl }}/publications/alejandratp.bib">here</a>.
</p>

<style>
.pub-year-heading {
  font-size: 1.4rem;
  font-weight: 700;
  color: #fff;
  background: linear-gradient(135deg, #2c3e50, #34495e);
  padding: 0.4rem 1rem;
  border-radius: 6px;
  margin: 2rem 0 1rem;
  display: inline-block;
}
.pub-card {
  background: #fff;
  border: 1px solid #e9ecef;
  border-left: 4px solid #3498db;
  border-radius: 8px;
  padding: 1.2rem 1.4rem;
  margin-bottom: 1rem;
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.pub-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
  transform: translateY(-2px);
}
.pub-title { font-weight: 600; color: #2c3e50; margin-bottom: 0.3rem; line-height: 1.4; }
.pub-title a { color: #2c3e50; text-decoration: none; }
.pub-title a:hover { color: #3498db; text-decoration: underline; }
.pub-authors { color: #6c757d; font-size: 0.92rem; margin-bottom: 0.2rem; }
.pub-venue { color: #3498db; font-size: 0.92rem; margin-bottom: 0.3rem; }
.pub-btn {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 2px 10px;
  border-radius: 4px;
  margin-right: 4px;
  margin-bottom: 3px;
  text-decoration: none;
  cursor: pointer;
  transition: opacity 0.2s;
}
.pub-btn:hover { opacity: 0.8; text-decoration: none; }
.pub-btn-abstract { background: #6c757d; color: #fff; }
.pub-btn-pdf      { background: #e74c3c; color: #fff; }
.pub-btn-doi      { background: #2c3e50; color: #fff; }
.pub-btn-arxiv    { background: #b31b1b; color: #fff; }
.pub-btn-code     { background: #333; color: #fff; }
.pub-abstract {
  background: #f8f9fa;
  border-left: 3px solid #3498db;
  padding: 0.75rem 1rem;
  font-size: 0.9rem;
  color: #495057;
  border-radius: 0 4px 4px 0;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
(function() {
  var years = [];
  var counts = [];
  {% for myyear in site.data.years %}
    {% assign n = 0 %}
    {% for publi in site.publications %}
      {% if publi.year == myyear.year %}{% assign n = n | plus: 1 %}{% endif %}
    {% endfor %}
    {% if n > 0 %}
  years.push("{{ myyear.year }}");
  counts.push({{ n }});
    {% endif %}
  {% endfor %}
  years.reverse(); counts.reverse();
  new Chart(document.getElementById('pubChart'), {
    type: 'bar',
    data: {
      labels: years,
      datasets: [{
        label: 'Publications',
        data: counts,
        backgroundColor: 'rgba(52, 152, 219, 0.7)',
        borderColor: 'rgba(52, 152, 219, 1)',
        borderWidth: 1,
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } }
    }
  });
})();
</script>
