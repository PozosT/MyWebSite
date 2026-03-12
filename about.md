---
title: "About"
layout: gridlay
sitemap: false
permalink: /about/
---

## About

{% for member in site.data.pi %}
<div class="about-profile-card">
  <div class="about-photo-wrap">
    <img src="{{ site.baseurl }}/images/team/{{ member.photo-large | default: member.photo-small }}" alt="{{ member.name }}" class="about-photo" />
  </div>
  <div class="about-info">
    <h3 class="about-name">{{ member.name }}</h3>
    <p class="about-role">{{ member.info }}</p>
    <div class="about-links">
      {% if member.email %}<a href="mailto:{{ member.email }}" title="Email"><i class="fas fa-envelope fa-lg"></i></a>{% endif %}
      {% if member.scholar %}<a href="{{ member.scholar }}" target="_blank" title="Google Scholar"><i class="ai ai-google-scholar-square ai-lg"></i></a>{% endif %}
      {% if member.orcid %}<a href="{{ member.orcid }}" target="_blank" title="ORCID"><i class="ai ai-orcid-square ai-lg"></i></a>{% endif %}
      {% if member.linkedin %}<a href="{{ member.linkedin }}" target="_blank" title="LinkedIn"><i class="fab fa-linkedin fa-lg"></i></a>{% endif %}
      {% if member.github %}<a href="{{ member.github }}" target="_blank" title="GitHub"><i class="fab fa-github fa-lg"></i></a>{% endif %}
      {% if member.researchgate %}<a href="{{ member.researchgate }}" target="_blank" title="ResearchGate"><i class="ai ai-researchgate-square ai-lg"></i></a>{% endif %}
      {% if member.cv %}<a href="{{ member.cv }}" target="_blank" title="CV"><i class="ai ai-cv-square ai-lg"></i></a>{% endif %}
    </div>
    <ul class="about-edu">
      {% if member.education1 %}<li>{{ member.education1 }}</li>{% endif %}
      {% if member.education2 %}<li>{{ member.education2 }}</li>{% endif %}
      {% if member.education3 %}<li>{{ member.education3 }}</li>{% endif %}
      {% if member.education4 %}<li>{{ member.education4 }}</li>{% endif %}
      {% if member.education5 %}<li>{{ member.education5 }}</li>{% endif %}
      {% if member.education6 %}<li>{{ member.education6 }}</li>{% endif %}
    </ul>
  </div>
</div>
{% endfor %}

## Short Biography

<div class="about-bio">
Dr. Alejandra Tabares Pozos is an Assistant Professor in the Department of Industrial Engineering at the Universidad de los Andes in Bogotá, Colombia. She is an Industrial Engineer with a Ph.D. in Electrical Engineering, specializing in the application of advanced mathematical models to solve critical challenges in modern energy systems.

Her research is centered on leveraging stochastic optimization, artificial intelligence, and reinforcement learning to address the complexities of the energy transition in Colombia and Latin America. Dr. Tabares is driven by a clear vision: to develop computational tools that not only represent a scientific breakthrough but also deliver a tangible impact — ensuring more reliable, sustainable, and equitable access to energy for all communities, transforming the technical complexity of microgrids into practical solutions that foster social development and environmental protection.

Dr. Tabares earned her Ph.D. and M.Sc. in Electrical Engineering from São Paulo State University (UNESP), Brazil. She completed her undergraduate studies in Industrial Engineering with honors at the Universidad Tecnológica de Pereira (UTP) in Colombia. Her postdoctoral work was conducted as a Research Assistant with the São Paulo Research Foundation (FAPESP). During her doctoral studies, she was a visiting research scholar at the University of Castilla-La Mancha in Spain.

A leader in her field, Dr. Tabares heads the Renewable Energy Living Lab at Universidad de los Andes, an initiative that provides a real-world microgrid environment for validating innovative algorithms and technologies. She has also led industry-focused projects, including the co-direction of a project with ENEL to develop a predictive and optimization algorithm for the El Paso solar plant.

Mentorship is a cornerstone of her academic career. Dr. Tabares is committed to training the next generation of scientists, supervising graduate students whose research advances microgrid management, from local energy markets to hybrid AI operational models. Her teaching portfolio includes graduate and undergraduate courses such as Optimization under Uncertainty, Probabilistic Models, Network Flow Optimization, Metaheuristics, and Smart Microgrids.
</div>

{% if site.data.awards %}
<div class="about-section-label" style="margin-top:2rem"><i class="fas fa-trophy me-2"></i>Awards</div>
<ol class="about-list">
{% for award in site.data.awards %}
  <li class="about-list-item">
    <span class="about-item-name">{% if award.name_url %}<a href="{{ award.name_url }}" target="_blank">{{ award.name }}</a>{% else %}{{ award.name }}{% endif %}</span>
    {% if award.organisation %}<span class="about-item-org"> — {% if award.organisation_url %}<a href="{{ award.organisation_url }}" target="_blank">{{ award.organisation }}</a>{% else %}{{ award.organisation }}{% endif %}</span>{% endif %}
    {% if award.subtitle %}<span class="about-item-sub">: {{ award.subtitle }}</span>{% endif %}
    <span class="about-item-year">({{ award.year }})</span>
  </li>
{% endfor %}
</ol>
{% endif %}

{% if site.data.grants %}
<div class="about-section-label" style="margin-top:2rem"><i class="fas fa-file-invoice-dollar me-2"></i>Grants & Funding</div>
<ol class="about-list">
{% for grant in site.data.grants %}
  <li class="about-list-item">
    <span class="about-item-name">{% if grant.name_url %}<a href="{{ grant.name_url }}" target="_blank">{{ grant.name }}</a>{% else %}{{ grant.name }}{% endif %}</span>
    {% if grant.organisation %}<span class="about-item-org"> — {% if grant.organisation_url %}<a href="{{ grant.organisation_url }}" target="_blank">{{ grant.organisation }}</a>{% else %}{{ grant.organisation }}{% endif %}</span>{% endif %}
    {% if grant.subtitle %}<span class="about-item-sub">: {{ grant.subtitle }}</span>{% endif %}
    <span class="about-item-year">({{ grant.year }})</span>
  </li>
{% endfor %}
</ol>
{% endif %}

{% if site.data.research_visits %}
<div class="about-section-label" style="margin-top:2rem"><i class="fas fa-plane me-2"></i>Research Visits</div>
<ol class="about-list">
{% for rv in site.data.research_visits %}
  <li class="about-list-item">
    <span class="about-item-name">{% if rv.institution_url %}<a href="{{ rv.institution_url }}" target="_blank">{{ rv.institution }}</a>{% else %}{{ rv.institution }}{% endif %}</span>
    {% if rv.location %}<span class="about-item-org"> — {{ rv.location }}</span>{% endif %}
    {% if rv.period %}<span class="about-item-year">, {{ rv.period }}</span>{% endif %}
  </li>
{% endfor %}
</ol>
{% endif %}

{% if site.data.collaborators %}
<div class="about-section-label" style="margin-top:2rem"><i class="fas fa-handshake me-2"></i>Collaborations</div>
<ol class="about-list">
{% for c in site.data.collaborators %}
  <li class="about-list-item">
    <span class="about-item-name">{% if c.name_url %}<a href="{{ c.name_url }}" target="_blank">{{ c.name }}</a>{% else %}{{ c.name }}{% endif %}</span>
    <span class="about-item-org"> — {{ c.field }}, {% if c.institution_url %}<a href="{{ c.institution_url }}" target="_blank">{{ c.institution }}</a>{% else %}{{ c.institution }}{% endif %}</span>
  </li>
{% endfor %}
</ol>
{% endif %}

<style>
/* Profile card */
.about-profile-card {
  display: flex;
  gap: 2rem;
  background: #fff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 12px rgba(0,0,0,0.05);
}
.about-photo-wrap { flex-shrink: 0; }
.about-photo {
  width: 160px;
  height: 160px;
  object-fit: cover;
  border-radius: 10px;
  border: 3px solid #eaf0fb;
}
.about-info { flex: 1; min-width: 0; }
.about-name {
  font-size: 1.4rem;
  font-weight: 800;
  color: #2c3e50;
  margin: 0 0 0.2rem 0;
}
.about-role {
  font-size: 0.95rem;
  color: #6c757d;
  font-style: italic;
  margin-bottom: 0.9rem;
}
.about-links {
  display: flex;
  gap: 0.65rem;
  margin-bottom: 1.1rem;
  flex-wrap: wrap;
}
.about-links a {
  color: #2c3e50;
  font-size: 1.35rem;
  transition: color 0.2s;
}
.about-links a:hover { color: #3498db; }
.about-edu {
  list-style: none;
  padding: 0;
  margin: 0;
}
.about-edu li {
  font-size: 0.87rem;
  color: #495057;
  padding: 0.3rem 0;
  border-bottom: 1px solid #f8f9fa;
  line-height: 1.5;
}
.about-edu li:last-child { border-bottom: none; }

/* Biography */
.about-bio {
  background: #f8f9fa;
  border-left: 4px solid #3498db;
  border-radius: 0 10px 10px 0;
  padding: 1.4rem 1.6rem;
  margin-bottom: 0.5rem;
  font-size: 0.92rem;
  color: #495057;
  line-height: 1.75;
}
.about-bio p, .about-bio + p {
  margin-bottom: 1rem;
}

/* Lists */
.about-section-label {
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #6c757d;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #e9ecef;
}
.about-list {
  list-style: none;
  counter-reset: about-counter;
  padding: 0;
  margin: 0;
  background: #fff;
  border: 1px solid #e9ecef;
  border-radius: 10px;
  overflow: hidden;
}
.about-list-item {
  counter-increment: about-counter;
  padding: 0.8rem 1rem 0.8rem 3.1rem;
  position: relative;
  border-bottom: 1px solid #f1f3f5;
  font-size: 0.88rem;
  line-height: 1.5;
}
.about-list-item:last-child { border-bottom: none; }
.about-list-item::before {
  content: counter(about-counter);
  position: absolute;
  left: 0.6rem;
  top: 0.8rem;
  width: 1.5rem;
  height: 1.5rem;
  background: #eaf0fb;
  color: #2c3e50;
  border-radius: 50%;
  font-size: 0.7rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}
.about-item-name { font-weight: 600; color: #2c3e50; }
.about-item-name a { color: #2c3e50; text-decoration: none; }
.about-item-name a:hover { color: #3498db; text-decoration: underline; }
.about-item-org { color: #6c757d; }
.about-item-org a { color: #6c757d; }
.about-item-org a:hover { color: #3498db; }
.about-item-sub { color: #9ca3af; font-style: italic; }
.about-item-year { font-size: 0.78rem; color: #9ca3af; }

@media (max-width: 640px) {
  .about-profile-card { flex-direction: column; gap: 1.25rem; }
  .about-photo { width: 120px; height: 120px; }
}
</style>
