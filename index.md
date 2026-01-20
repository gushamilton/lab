---
layout: default
title: Fergus Hamilton
subtitle: NIHR Clinical Lecturer in Aetiological Epidemiology
---
## About

I am a clinical academic working at the intersection of infectious disease medicine, statistical genetics, and clinical
epidemiology. My research focuses on understanding why some individuals develop severe outcomes from infection while
others do not.

I approach this problem by combining large-scale human genomic data with pragmatic clinical trials. My goal is to
develop and apply rigorous statistical methodologies to identify causal drivers of sepsis and infection susceptibility.

## Research Focus

### Trials
My clinical research focuses on the design and delivery of pragmatic trials to improve outcomes in severe infection. <span class="marginnote-left"><strong>Why trials?</strong><br> Trials are such a pain. I hate them, but they are the best. Why do I hate them? They are incredibly time consuming. They are totally overregulated in many ways and in some ways remarkably underregulated. They are unbelivably costly for what they should be. However, they are the only compelling way to generate evidence in a large number of questions, so we are stuck with them.</span> I
co-lead the [DEXACELL trial](https://www.isrctn.com/ISRCTN76873478), which evaluates the use of dexamethasone as an
adjunctive therapy in cellulitis.

I also am very interested in developing and testing novel trial methodologies, such as adaptive designs, and methods to improve inference around specific populations. 


### Statistical genetics (and other stats stuff)
I focus on the development of new statistical methodologies to analyze high-dimensional genetic data. My work utilizes
novel methods in Mendelian randomization and genetic epidemiology to investigate causal drivers of disease. <span class="marginnote"><strong>Why genetic epi of infection?</strong><br>Infection is highly heritable - in that historically it has been a major driver of selection, and most modern data (notably from malaria and COVID-19) have found that people who have certain genetic variants are more likely to have worse outcomes. This is remarkably understudied in most infections compared to other traits.<br><br>Remarkably, we also know that these genetic variants can predict clinical trial success - that is, we can use the information we gain from genetic studies to identify the apppropriate drug targets.</span>


I am particularly interested in integrating new methods to analyse infection data at scale. This data is a complete mess, 
as anyone who has tried to use it will know. There is so much more to do.

On the side I think a bit about general observational epi and statistics and comment a bit on that occasionally.

### Clinical Microbiology

I have a strong interest in the optimization of clinical microbiology pathways. I was a lead investigator on the
[AERATOR
study](https://www.nbt.nhs.uk/research-development/our-research/current-research/covid-19-research/covid-19-aerator-study),
which quantified aerosol generation during medical procedures.

I have worked widely on trying to improve blood culture diagnostics, including thinking about pre-analytical pathways. It's kind remarkable how little we've changed blood culture diagnostics in the last 50 years...


### Respiratory infection

I have a real interest in respiratory infection, and have been working on an idea for a trial of aspirin for pneumonia since 2012, and eventually David Arnold led this to fruition with the ASPECT trial, due to complete 2026.

I also work on RCTs and other studies in respiratory infection, including in pharmacokinetics of antibiotics in the pleural space. I am a quasi-official member of the [Academic Respiratory Unit](https://www.bristol.ac.uk/medicine/medicine/academic-respiratory-unit/), (I get invited to the Christmas drinks and lurk on the WhatsApp group). 


### Pharmacokinetics of antimicrobials

I work clinically at North Bristol, which houses both the national antimicrobial reference laboratory [ARL](https://www.nbt.nhs.uk/severn-pathology/pathology-services/antimicrobial-reference-laboratory/bristol-centre-antimicrobial-research-evaluation/bcare-research) and [BCARE](https://www.nbt.nhs.uk/severn-pathology/pathology-services/antimicrobial-reference-laboratory/bristol-centre-antimicrobial-research-evaluation/bcare-research), which performs a number of in-vitro studies relating to pharmacodynamics and pharmacokinetics of infection. I am broadly interested in these studies, as in infection, pK strongly predicts future success (not like cancer, or other fields).

### Other stuff

I find I spend a sort of depressingly large amount of time thinking about other things, quasi-unrelated to my research. THese usually involve computaitonal methods but could be economics, geography, AI, or whatever. 

## Recent News

{% for post in site.posts limit:3 %}
* **{{ post.date | date: "%b %Y" }}**: [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

[Read all news →]({{ '/blog/' | relative_url }})