---
title: "Data Engineering"
author: Blake Vente
toc: true
type: pages
layout: posts
#theme: metropolis
links-as-notes: true
header-includes:
  - "\\usetheme{metropolis}"
#pandoc site.md -t beamer -i -o slides.pdf  
---

# Constraints

* free hosting

* no fine print

* familiar

* easy to maintain

* mobile friendly

* Screen-Reader Friendly (accessibility)

# Solutions

## Github-centered Workflow

* GitHub Pages

* GitHub Markdown

* Open Source

## GitHub Markdown

* superset of HTML

* reduces our maintenence complexity

# Inter-Op

* Losslessly convert between HTML and Markdown
  using Pandoc

# Maintenence

* `_posts/labs/` stores the labs

* `_posts/readings/` stores the readings

* `etc`...

* Push to `master`...

* Everything autopopulates in 5 minutes or less.

# Im2Latex Model

## Upgrading

* [Ported model to Python 3](https://github.com/untrix/im2latex)
* Future plans to upgrade Tensorflow to v2
* Deal with deprecated dependencies 

# Progress so far 

## Training model

* Model has been deployed on a Google-Cloud GPU learner and locally for consistency
* Trains without problems - all log files show promising results
* Currently has problems restoring from checkpoint

## Following Upgrades to Model

* Be able to tweak the attention model and customizable hyperparameters of the model
* Upgrade preproccessing scripts to work on Blake's generated data for consistency
* Experiment with running the  model on various data categories (i.e Matrices, Equations, Piecewise Functions)


# Additional Documentation

 - [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
