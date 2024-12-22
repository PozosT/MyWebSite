---
title: "Home"
layout: homelay
sitemap: false
permalink: /
---

<style>
code {padding: 6px 8px; font-size: 90%;}
</style>

Welcome to my personal homepage! I am currently an assistant professor in the Department of Production Engineering at [Universidad de los Andes](https://www.uniandes.edu.co). My research focuses on the development of AI-driven models for solar energy prediction using satellite and sky images, the creation of digital twins for renewable energy plants, and the application of reinforcement learning for microgrid operation and optimization systems. I also integrate deep learning techniques with optimization methods to address complex energy challenges.

From 2019 to 2021, I was a postdoctoral researcher in the Department of Electrical Engineering at [Universidade Estadual Paulista (UNESP)](https://www.unesp.br), where I contributed to the development of convex and stochastic mathematical models for the planning and operation of electrical distribution networks, focusing on the integration of renewable energy and reliability analysis. I received a postdoctoral research fellowship from FAPESP for this work. 

During my doctoral studies (2015–2019) at UNESP, I explored advanced optimization methods to plan electric power distribution systems, incorporating traditional and non-traditional assets. My dissertation focused on integrating service reliability into expansion planning. I also collaborated with the [University of Castilla-La Mancha](https://www.uclm.es) during my doctoral internship, addressing challenges in reliability assessment for distribution networks.

Prior to my Ph.D., I completed a master's degree in Electrical Engineering at UNESP (2013–2015), where I pioneered the inclusion of distributed generation and storage assets into long-term network planning models. My undergraduate studies in Industrial Engineering were at the [Universidad Tecnológica de Pereira](https://www.utp.edu.co), where I graduated with honors in 2012. My thesis explored heuristic methods for improving logistics efficiency in distribution companies.

My passion for education has led me to design and teach courses on optimization, stochastic processes and power energy systems. I am passionate about education and design my courses to provide students with both theoretical foundations and practical experiences that prepare them for real-world challenges. Currently, I coordinate undergraduate courses on probabilistic models, focusing on topics such as Markov chains, where students build foundational skills in probabilistic thinking and uncertainty management. Given that many undergraduate students are still developing strong study habits, these courses follow a highly structured format with weekly activities, frequent quizzes to track progress, and individual midterm exams that hold significant weight in the overall evaluation. This ensures a solid understanding of core topics in probability and stochastic processes.

At the graduate level, I teach courses on network flow optimization, metaheuristics, linear statistical models, and data mining. These courses are designed to encourage students to take on integrative and challenging projects that involve real-world datasets or scenarios. The goal is to expose students to practical situations they might encounter in professional or research environments. I value flexibility in graduate courses and often adapt deadlines based on the commitment and progress demonstrated by the group, fostering a collaborative and engaging learning environment.

I am an advocate for interdisciplinary collaboration and have worked with researchers in Portugal, the UK, and Spain to tackle energy systems challenges. My academic contributions include publications in high-impact journals such as *IEEE Transactions on Power Systems* and *Energy*. I have also received awards for my work, including the Best Paper Award at the IEEE PES Innovative Smart Grid Technologies Conference in 2019.

Feel free to explore my [Google Scholar](https://scholar.google.com/citations?user=C9PY5CwAAAAJ&hl=en) profile to learn more about my publications and ongoing projects. 


### Free time
* ⚽ Play soccer (I bet that I am better than you! hahahaha).
* 📖 Reading mostly non-fiction books.
* 🗺️ Travelling, especially to see old cities.

<br/>

<div class="well-md">
  <h3>Funding</h3>
  <div style='display:block; text-align:center; margin-left:auto; margin-right:auto;'>
   {% for funder in site.data.funders %}{% if funder.url %}<a href="{{funder.url}}" target="_blank"><img src='/images/logos/{{ funder.image }}' style='max-height: 70px; max-width: 170px;'/></a>{% else %}<img src='/images/logos/{{ funder.image }}' class='mycenter' style='max-height: 70px; max-width: 170px;'/>{% endif %}   {% endfor %}
  </div>
</div>
