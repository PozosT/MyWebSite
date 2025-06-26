---
title: "About"
layout: gridlay
sitemap: false
permalink: /about/
---

## About 


{% for member in site.data.pi %}

<div class="row">
  <img src="{{ site.baseurl }}/images/team/{{ member.photo-large }}" class="img-responsive avatar-about" />
  <h3>{{ member.name }}</h3>
  <i style="font-size:20px">{{ member.info }}</i><br>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-3x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-3x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-3x"></i></a> {% endif %}
  {% if member.orcid %} <a href="{{ member.orcid }}" target="_blank"><i class="ai ai-orcid-square ai-3x"></i></a> {% endif %}
  {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-3x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-3x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-3x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-3x"></i></a> {% endif %}
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  {% if member.number_educ == 6 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  <li> {{ member.education6 }} </li>
  {% endif %}

  </ul>
</div>

{% endfor %}

## Short biography

<div class="short-bio">
Dr. Alejandra Tabares Pozos is an Assistant Professor in the Department of Industrial Engineering at the Universidad de los Andes in Bogotá, Colombia. She is an Industrial Engineer with a Ph.D. in Electrical Engineering, specializing in the application of advanced mathematical models to solve critical challenges in modern energy systems.


Her research is centered on leveraging stochastic optimization, artificial intelligence, and reinforcement learning to address the complexities of the energy transition in Colombia and Latin America. Dr. Tabares is driven by a clear vision: to develop computational tools that not only represent a scientific breakthrough but also deliver a tangible impact. Her goal is to ensure more reliable, sustainable, and equitable access to energy for all communities, transforming the technical complexity of microgrids into practical solutions that foster social development and environmental protection.


Dr. Tabares earned her Ph.D. and M.Sc. in Electrical Engineering from São Paulo State University (UNESP), Brazil. She completed her undergraduate studies in Industrial Engineering with honors at the Universidad Tecnológica de Pereira (UTP) in Colombia. Her postdoctoral work was conducted as a Research Assistant with the São Paulo Research Foundation (FAPESP). During her doctoral studies, she was a visiting research scholar at the University of Castilla-La Mancha in Spain.



A leader in her field, Dr. Tabares heads the Renewable Energy Living Lab at Universidad de los Andes, an initiative that provides a real-world microgrid environment for validating innovative algorithms and technologies. She has also led industry-focused projects, including the co-direction of a project with the major energy company ENEL to develop a predictive and optimization algorithm for the El Paso solar plant, demonstrating the direct industrial application of her research.


Mentorship is a cornerstone of her academic career. Dr. Tabares is committed to training the next generation of scientists, currently supervising Ph.D. students whose research is crucial for advancing microgrid management, from local energy markets to hybrid AI operational models. Her teaching portfolio includes graduate and undergraduate courses such as Optimization under Uncertainty, Probabilistic Models, Optimization in networks, Metahaueristics and Smart Microgrids.

</div>

{% if site.data.awards %}
## Awards
<div class="rowl1" style="padding-top: 10px;">

{% for award in site.data.awards %}
{{ forloop.index }}. {% if award.name_url %}<a href="{{ award.name_url }}" target="_blank">{% endif %}<strong>{{ award.name }}</strong>{% if award.name_url %}</a>{% endif %} {% if award.organisation %} from {% if award.organisation_url %}<a href="{{ award.organisation_url }}" target="_blank">{% endif %} {{ award.organisation }}{% if award.organisation_url %}</a>{% endif %}{% endif %}{% if award.subtitle %}: {{ award.subtitle }}{% endif %} ({{ award.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.grants %}
## Grants
<div class="rowl1" style="padding-top: 10px;">

{% for grant in site.data.grants %}
{{ forloop.index }}. {% if grant.name_url %}<a href="{{ grant.name_url }}" target="_blank">{% endif %}<strong>{{ grant.name }}</strong>{% if grant.name_url %}</a>{% endif %} {% if grant.organisation %} from {% if grant.organisation_url %}<a href="{{ grant.organisation_url }}" target="_blank">{% endif %} {{ grant.organisation }}{% if grant.organisation_url %}</a>{% endif %}{% endif %}{% if grant.subtitle %}: {{ grant.subtitle }}{% endif %} ({{ grant.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.collaborators %}
## Collaborations
<div class="rowl1" style="padding-top: 10px;">

{% for collaborator in site.data.collaborators %}
{{ forloop.index }}. {% if collaborator.name_url %}<a href="{{ collaborator.name_url }}" target="_blank">{% endif %}<strong>{{ collaborator.name }}</strong>{% if collaborator.name_url %}</a>{% endif %} ({{ collaborator.field }}, {% if collaborator.institution_url %}<a href="{{ collaborator.institution_url }}" target="_blank">{% endif %}{{ collaborator.institution }}{% if collaborator.institution_url %}</a>{% endif %}).
{% endfor %}
</div>
{% endif %}


{% if site.data.research_visits %}
## Research visits
<div class="rowl1" style="padding-top: 10px;">

{% for research_visit in site.data.research_visits %}
{{ forloop.index }}. {% if research_visit.institution_url %}<a href="{{ research_visit.institution_url }}" target="_blank">{% endif %}<strong>{{ research_visit.institution }}</strong>{% if research_visit.institution_url %}</a>{% endif %}{% if research_visit.location %} ({{ research_visit.location }}){% endif %}{% if research_visit.period %}, {{ research_visit.period }}{% endif %}.
{% endfor %}
</div>
{% endif %}

{% if site.data.invited_speakers %}
## Invited speakers at my group
<div class="rowl1" style="padding-top: 10px;">

{% for invited_speaker in site.data.invited_speakers %}
{{ forloop.index }}. {% if invited_speaker.name_url %}<a href="{{ invited_speaker.name_url }}" target="_blank">{% endif %}<strong>{{ invited_speaker.name }}</strong>{% if invited_speaker.name_url %}</a>{% endif %} ({{ invited_speaker.field }}, {% if invited_speaker.institution_url %}<a href="{{ invited_speaker.institution_url }}" target="_blank">{% endif %}{{ invited_speaker.institution }}{% if invited_speaker.institution_url %}</a>{% endif %}){% if invited_speaker.venue %}  at {{ invited_speaker.venue }}{% endif %}{% if invited_speaker.date %}, {{ invited_speaker.date }}{% endif %}.
{% endfor %}
</div>
{% endif %} 