# Lab Website

A simple, data-driven academic website built with Jekyll.

## How to Edit

### 1. Publications (`_data/publications.yml`)
Add new papers to this file. The site automatically groups them by year.
Format:
```yaml
- title: "Paper Title"
  venue: Journal Name
  year: 2026
  url: https://doi.org/...
  description: "One sentence summary."
```

### 2. Team Members (`_data/team.yml`)
Add new team members here. Images should be placed in `assets/`.
Format:
```yaml
- name: Name
  role: Role
  bio: Short bio...
  image: /assets/placeholder.svg
```

### 3. Blog Posts (`_posts/`)
Create a new file named `YYYY-MM-DD-title.md` (e.g., `2026-05-20-new-paper.md`).
Content should start with front matter:
```markdown
---
layout: post
title: "We published a new paper"
date: 2026-05-20
---
Text goes here...
```

### 4. Homepage Content (`index.md`)
Edit this file to change the text in the "About", "Research Focus", or "Trials" sections.
- Use `<span class="marginnote-left">Note text</span>` for side notes.

## Running Locally
To preview changes on your computer:
```bash
bundle exec jekyll serve
```
Open [http://localhost:4000](http://localhost:4000)

## Deployment
Changes pushed to the `main` branch are automatically built and deployed to GitHub Pages.
