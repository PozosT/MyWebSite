---
title: "Students"
layout: gridlay
sitemap: false
permalink: /students/
---

# Student Supervision

{% assign total_master_advisor = site.data.theses_advisor | size %}
{% assign total_jury = site.data.theses_jury | size %}
{% assign total_undergrad = site.data.theses_undergrad | size %}
{% assign total_students_master = 0 %}
{% for t in site.data.theses_advisor %}
  {% assign total_students_master = total_students_master | plus: t.students.size %}
{% endfor %}
{% assign total_students_undergrad = 0 %}
{% for t in site.data.theses_undergrad %}
  {% assign total_students_undergrad = total_students_undergrad | plus: t.students.size %}
{% endfor %}
{% assign total_all = total_students_master | plus: total_students_undergrad %}

<div class="row g-3 mb-5">
  <div class="col-sm-3">
    <div class="text-center p-3 rounded" style="background:#eaf0fb;">
      <div style="font-size:2rem;font-weight:700;color:#2c3e50;">{{ total_all }}</div>
      <div class="text-muted small">Total students</div>
    </div>
  </div>
  <div class="col-sm-3">
    <div class="text-center p-3 rounded" style="background:#eafaf1;">
      <div style="font-size:2rem;font-weight:700;color:#27ae60;">{{ total_students_master }}</div>
      <div class="text-muted small">Master's students</div>
    </div>
  </div>
  <div class="col-sm-3">
    <div class="text-center p-3 rounded" style="background:#f3e8ff;">
      <div style="font-size:2rem;font-weight:700;color:#7c3aed;">{{ total_students_undergrad }}</div>
      <div class="text-muted small">Undergraduate students</div>
    </div>
  </div>
  <div class="col-sm-3">
    <div class="text-center p-3 rounded" style="background:#fef9e7;">
      <div style="font-size:2rem;font-weight:700;color:#f39c12;">{{ total_jury }}</div>
      <div class="text-muted small">Thesis committees</div>
    </div>
  </div>
</div>

---

## Master's Supervised Theses

<p class="text-muted mb-4">Master's theses directed at <strong>Universidad de los Andes</strong>.<br>
<span class="badge-prog badge-miind">MIIND</span> Maestría en Ingeniería Industrial &nbsp;
<span class="badge-prog badge-miia">MIIA</span> Maestría en Inteligencia Artificial</p>

{% assign advisor_years = "" %}
{% for t in site.data.theses_advisor %}
  {% assign yr = t.period | split: "-" | first %}
  {% unless advisor_years contains yr %}
    {% assign advisor_years = advisor_years | append: yr | append: "," %}
  {% endunless %}
{% endfor %}
{% assign advisor_year_list = advisor_years | split: "," | sort | reverse %}

{% for yr in advisor_year_list %}
{% if yr == "" %}{% continue %}{% endif %}

<h3 class="thesis-year-heading">{{ yr }}</h3>

{% for t in site.data.theses_advisor %}
{% assign t_year = t.period | split: "-" | first %}
{% if t_year == yr %}
<div class="thesis-card {% if t.status %}thesis-inprogress{% endif %}">
  <div class="thesis-header">
    <span class="badge-prog {% if t.program == 'MIIND' %}badge-miind{% else %}badge-miia{% endif %}">{{ t.program }}</span>
    <span class="thesis-period">Semester {{ t.period }}</span>
    {% if t.status %}<span class="thesis-status">{{ t.status }}</span>{% endif %}
  </div>
  <div class="thesis-title">{{ t.title }}</div>
  <div class="thesis-students">
    <i class="fas fa-user-graduate me-1" style="color:#6c757d;font-size:0.85rem;"></i>
    {{ t.students | size }} student{% if t.students.size > 1 %}s{% endif %}
  </div>
</div>
{% endif %}
{% endfor %}

{% endfor %}

---

## Undergraduate Thesis Projects (PG2)

<p class="text-muted mb-4">Bachelor's degree final projects (PG2) directed at <strong>Departamento de Ingeniería Industrial, Universidad de los Andes</strong>.</p>

{% assign undergrad_years = "" %}
{% for t in site.data.theses_undergrad %}
  {% assign yr = t.period | split: "-" | first %}
  {% unless undergrad_years contains yr %}
    {% assign undergrad_years = undergrad_years | append: yr | append: "," %}
  {% endunless %}
{% endfor %}
{% assign undergrad_year_list = undergrad_years | split: "," | sort | reverse %}

{% for yr in undergrad_year_list %}
{% if yr == "" %}{% continue %}{% endif %}

<h3 class="thesis-year-heading" style="background:linear-gradient(135deg,#5b21b6,#7c3aed);">{{ yr }}</h3>

{% for t in site.data.theses_undergrad %}
{% assign t_year = t.period | split: "-" | first %}
{% if t_year == yr %}
<div class="thesis-card thesis-undergrad">
  <div class="thesis-header">
    <span class="badge-prog badge-pregrado">Pregrado</span>
    <span class="thesis-period">Semester {{ t.period }}</span>
  </div>
  <div class="thesis-title">{{ t.title }}</div>
  <div class="thesis-students">
    <i class="fas fa-user-graduate me-1" style="color:#6c757d;font-size:0.85rem;"></i>
    {{ t.students | size }} student{% if t.students.size > 1 %}s{% endif %}
  </div>
</div>
{% endif %}
{% endfor %}

{% endfor %}

---

## Thesis Committee Memberships

<p class="text-muted mb-4">Master's thesis defenses where I served as examiner/jury member.</p>

{% assign jury_years = "" %}
{% for t in site.data.theses_jury %}
  {% assign yr = t.period | split: "-" | first %}
  {% unless jury_years contains yr %}
    {% assign jury_years = jury_years | append: yr | append: "," %}
  {% endunless %}
{% endfor %}
{% assign jury_year_list = jury_years | split: "," | sort | reverse %}

{% for yr in jury_year_list %}
{% if yr == "" %}{% continue %}{% endif %}

<h3 class="thesis-year-heading">{{ yr }}</h3>

{% for t in site.data.theses_jury %}
{% assign t_year = t.period | split: "-" | first %}
{% if t_year == yr %}
<div class="thesis-card thesis-jury {% if t.status %}thesis-inprogress{% endif %}">
  <div class="thesis-header">
    <span class="badge-prog {% if t.program == 'MIIND' %}badge-miind{% else %}badge-miia{% endif %}">{{ t.program }}</span>
    <span class="thesis-period">Semester {{ t.period }}</span>
    {% if t.status %}<span class="thesis-status">{{ t.status }}</span>{% endif %}
  </div>
  <div class="thesis-title">{{ t.title }}</div>
  <div class="thesis-students">
    <i class="fas fa-user me-1" style="color:#6c757d;font-size:0.85rem;"></i>
    {{ t.students | size }} student{% if t.students.size > 1 %}s{% endif %}
  </div>
</div>
{% endif %}
{% endfor %}

{% endfor %}

<style>
.thesis-year-heading {
  font-size: 1.2rem;
  font-weight: 700;
  color: #fff;
  background: linear-gradient(135deg, #2c3e50, #34495e);
  padding: 0.3rem 0.9rem;
  border-radius: 6px;
  margin: 1.8rem 0 0.8rem;
  display: inline-block;
}
.thesis-card {
  background: #fff;
  border: 1px solid #e9ecef;
  border-left: 4px solid #3498db;
  border-radius: 8px;
  padding: 0.9rem 1.2rem;
  margin-bottom: 0.7rem;
  transition: box-shadow 0.2s ease;
}
.thesis-card:hover { box-shadow: 0 3px 12px rgba(0,0,0,0.09); }
.thesis-jury      { border-left-color: #27ae60; }
.thesis-undergrad { border-left-color: #7c3aed; }
.thesis-inprogress { border-left-color: #f39c12; background: #fffdf5; }
.thesis-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.4rem;
  flex-wrap: wrap;
}
.badge-prog {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.badge-miind    { background: #dbeafe; color: #1e40af; }
.badge-miia     { background: #dcfce7; color: #166534; }
.badge-pregrado { background: #ede9fe; color: #5b21b6; }
.thesis-period { font-size: 0.8rem; color: #6c757d; }
.thesis-status {
  font-size: 0.75rem;
  font-weight: 600;
  background: #fef3c7;
  color: #92400e;
  padding: 1px 7px;
  border-radius: 4px;
}
.thesis-title {
  font-weight: 600;
  color: #2c3e50;
  font-size: 0.95rem;
  margin-bottom: 0.3rem;
  line-height: 1.4;
}
.thesis-students {
  font-size: 0.85rem;
  color: #6c757d;
}
.thesis-coadvisor {
  font-size: 0.8rem;
  color: #9ca3af;
  margin-top: 0.2rem;
}
</style>
