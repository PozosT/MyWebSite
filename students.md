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
{% for t in site.data.theses_advisor %}{% assign total_students_master = total_students_master | plus: t.students.size %}{% endfor %}
{% assign total_students_undergrad = 0 %}
{% for t in site.data.theses_undergrad %}{% assign total_students_undergrad = total_students_undergrad | plus: t.students.size %}{% endfor %}
{% assign total_all = total_students_master | plus: total_students_undergrad %}

<!-- Hero stats -->
<div class="sup-hero">
  <div class="sup-stat">
    <div class="sup-stat-number">{{ total_all }}</div>
    <div class="sup-stat-label"><i class="fas fa-users me-1"></i>Students supervised</div>
  </div>
  <div class="sup-divider"></div>
  <div class="sup-stat">
    <div class="sup-stat-number">{{ total_students_master }}</div>
    <div class="sup-stat-label"><i class="fas fa-user-graduate me-1"></i>Master's students</div>
  </div>
  <div class="sup-divider"></div>
  <div class="sup-stat">
    <div class="sup-stat-number">{{ total_students_undergrad }}</div>
    <div class="sup-stat-label"><i class="fas fa-graduation-cap me-1"></i>Undergraduate students</div>
  </div>
  <div class="sup-divider"></div>
  <div class="sup-stat">
    <div class="sup-stat-number">{{ total_jury }}</div>
    <div class="sup-stat-label"><i class="fas fa-clipboard-check me-1"></i>Thesis committees</div>
  </div>
</div>

<!-- Tabs -->
<ul class="nav nav-tabs sup-tabs mt-4 mb-0" id="supTabs" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="master-tab" data-bs-toggle="tab" data-bs-target="#master" type="button" role="tab">
      <i class="fas fa-user-graduate me-2"></i>Master's <span class="tab-count">{{ total_master_advisor }}</span>
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="undergrad-tab" data-bs-toggle="tab" data-bs-target="#undergrad" type="button" role="tab">
      <i class="fas fa-graduation-cap me-2"></i>Undergraduate <span class="tab-count">{{ total_undergrad }}</span>
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="jury-tab" data-bs-toggle="tab" data-bs-target="#jury" type="button" role="tab">
      <i class="fas fa-clipboard-check me-2"></i>Jury <span class="tab-count">{{ total_jury }}</span>
    </button>
  </li>
</ul>

<div class="tab-content sup-tab-content">

  <!-- MASTER'S TAB -->
  <div class="tab-pane fade show active" id="master" role="tabpanel">
    <p class="sup-desc">Master's theses directed at <strong>Universidad de los Andes</strong>.
    <span class="badge-prog badge-miind">MIIND</span> Ingeniería Industrial &nbsp;
    <span class="badge-prog badge-miia">MIIA</span> Inteligencia Artificial</p>
    <ol class="sup-list">
    {% assign sorted_master = site.data.theses_advisor | sort: "period" | reverse %}
    {% for t in sorted_master %}
      <li class="sup-item {% if t.status %}sup-inprogress{% endif %}">
        <div class="sup-item-main">{{ t.title }}</div>
        <div class="sup-item-meta">
          <span class="badge-prog {% if t.program == 'MIIND' %}badge-miind{% else %}badge-miia{% endif %}">{{ t.program }}</span>
          <span class="sup-period"><i class="fas fa-calendar-alt me-1"></i>{{ t.period }}</span>
          <span class="sup-nstudents"><i class="fas fa-users me-1"></i>{{ t.students | size }} student{% if t.students.size > 1 %}s{% endif %}</span>
          {% if t.status %}<span class="sup-status-badge">{{ t.status }}</span>{% endif %}
        </div>
      </li>
    {% endfor %}
    </ol>
  </div>

  <!-- UNDERGRAD TAB -->
  <div class="tab-pane fade" id="undergrad" role="tabpanel">
    <p class="sup-desc">Bachelor's final projects (PG2) directed at the <strong>Departamento de Ingeniería Industrial, Universidad de los Andes</strong>.</p>
    <ol class="sup-list">
    {% assign sorted_undergrad = site.data.theses_undergrad | sort: "period" | reverse %}
    {% for t in sorted_undergrad %}
      <li class="sup-item">
        <div class="sup-item-main">{{ t.title }}</div>
        <div class="sup-item-meta">
          <span class="badge-prog badge-pregrado">Pregrado</span>
          <span class="sup-period"><i class="fas fa-calendar-alt me-1"></i>{{ t.period }}</span>
          <span class="sup-nstudents"><i class="fas fa-users me-1"></i>{{ t.students | size }} student{% if t.students.size > 1 %}s{% endif %}</span>
        </div>
      </li>
    {% endfor %}
    </ol>
  </div>

  <!-- JURY TAB -->
  <div class="tab-pane fade" id="jury" role="tabpanel">
    <p class="sup-desc">Master's thesis defenses where I served as examiner/jury member.</p>
    <ol class="sup-list">
    {% assign sorted_jury = site.data.theses_jury | sort: "period" | reverse %}
    {% for t in sorted_jury %}
      <li class="sup-item {% if t.status %}sup-inprogress{% endif %}">
        <div class="sup-item-main">{{ t.title }}</div>
        <div class="sup-item-meta">
          <span class="badge-prog {% if t.program == 'MIIND' %}badge-miind{% else %}badge-miia{% endif %}">{{ t.program }}</span>
          <span class="sup-period"><i class="fas fa-calendar-alt me-1"></i>{{ t.period }}</span>
          {% if t.status %}<span class="sup-status-badge">{{ t.status }}</span>{% endif %}
        </div>
      </li>
    {% endfor %}
    </ol>
  </div>

</div>

<style>
/* Hero stats banner */
.sup-hero {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
  border-radius: 12px;
  padding: 1.8rem 2rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 1rem;
}
.sup-stat {
  text-align: center;
  flex: 1;
  min-width: 120px;
}
.sup-stat-number {
  font-size: 2.8rem;
  font-weight: 800;
  color: #fff;
  line-height: 1;
  margin-bottom: 0.3rem;
}
.sup-stat-label {
  font-size: 0.82rem;
  color: rgba(255,255,255,0.75);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.sup-divider {
  width: 1px;
  height: 50px;
  background: rgba(255,255,255,0.2);
  flex-shrink: 0;
}
@media (max-width: 576px) {
  .sup-divider { display: none; }
  .sup-stat { min-width: 45%; }
}

/* Tabs */
.sup-tabs {
  border-bottom: 2px solid #e9ecef;
}
.sup-tabs .nav-link {
  color: #6c757d;
  border: none;
  border-bottom: 3px solid transparent;
  border-radius: 0;
  padding: 0.75rem 1.25rem;
  font-weight: 600;
  font-size: 0.92rem;
  transition: all 0.2s;
  margin-bottom: -2px;
}
.sup-tabs .nav-link:hover { color: #2c3e50; }
.sup-tabs .nav-link.active {
  color: #3498db;
  border-bottom-color: #3498db;
  background: transparent;
}
.tab-count {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #e9ecef;
  color: #495057;
  font-size: 0.72rem;
  font-weight: 700;
  min-width: 20px;
  height: 20px;
  border-radius: 10px;
  padding: 0 5px;
  margin-left: 4px;
}
.sup-tabs .nav-link.active .tab-count {
  background: #dbeafe;
  color: #1e40af;
}

/* Tab content */
.sup-tab-content {
  border: 1px solid #e9ecef;
  border-top: none;
  border-radius: 0 0 10px 10px;
  padding: 1.5rem 1.75rem;
  background: #fff;
}
.sup-desc {
  color: #6c757d;
  font-size: 0.9rem;
  margin-bottom: 1.2rem;
}

/* Numbered list */
.sup-list {
  list-style: none;
  counter-reset: sup-counter;
  padding: 0;
  margin: 0;
}
.sup-item {
  counter-increment: sup-counter;
  display: flex;
  flex-direction: column;
  padding: 0.85rem 0.85rem 0.85rem 3rem;
  position: relative;
  border-bottom: 1px solid #f1f3f5;
  transition: background 0.15s;
}
.sup-item:last-child { border-bottom: none; }
.sup-item:hover { background: #f8f9fa; border-radius: 6px; }
.sup-item::before {
  content: counter(sup-counter);
  position: absolute;
  left: 0.5rem;
  top: 0.85rem;
  width: 1.6rem;
  height: 1.6rem;
  background: #eaf0fb;
  color: #2c3e50;
  border-radius: 50%;
  font-size: 0.72rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}
.sup-inprogress { background: #fffdf5 !important; }
.sup-inprogress::before { background: #fef3c7; color: #92400e; }

.sup-item-main {
  font-weight: 600;
  color: #2c3e50;
  font-size: 0.93rem;
  line-height: 1.45;
  margin-bottom: 0.4rem;
}
.sup-item-meta {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.badge-prog {
  font-size: 0.7rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.badge-miind    { background: #dbeafe; color: #1e40af; }
.badge-miia     { background: #dcfce7; color: #166534; }
.badge-pregrado { background: #ede9fe; color: #5b21b6; }
.sup-period, .sup-nstudents {
  font-size: 0.78rem;
  color: #9ca3af;
}
.sup-status-badge {
  font-size: 0.7rem;
  font-weight: 600;
  background: #fef3c7;
  color: #92400e;
  padding: 1px 7px;
  border-radius: 4px;
}
</style>
