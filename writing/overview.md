---
slug: github-freight-jnapolitano-io-writing-overview
id: github-freight-jnapolitano-io-writing-overview
title: Analyzing Freight Networks in the U.S. with freight.jnapolitano.io
repo: justin-napolitano/freight.jnapolitano.io
githubUrl: https://github.com/justin-napolitano/freight.jnapolitano.io
generatedAt: '2025-11-24T17:24:28.387Z'
source: github-auto
summary: >-
  I started the freight.jnapolitano.io project to dive into the intricacies of
  the United States' freight networks. This includes all the heavy hitters like
  rail, shipping, and intermodal transport. The goal is to analyze and visualize
  this complex web of logistics. Let's get into what the project is, why it
  exists, some key decisions I made, the tech stack I'm using, trade-offs I've
  run into, and my future plans for improvement.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I started the freight.jnapolitano.io project to dive into the intricacies of the United States' freight networks. This includes all the heavy hitters like rail, shipping, and intermodal transport. The goal is to analyze and visualize this complex web of logistics. Let's get into what the project is, why it exists, some key decisions I made, the tech stack I'm using, trade-offs I've run into, and my future plans for improvement.

## What the Repo Is

At its core, freight.jnapolitano.io is a data-driven exploration of freight networks. It houses Jupyter notebooks, scripts, and comprehensive documentation for visualizing and analyzing freight infrastructure. There's a lot of rich data out there, so I wanted to create a means to make sense of it all.

## Why It Exists

Freight transport is the backbone of our economy. But honestly, how many of us really grasp how intricate these networks are? I wanted to provide a resource to unearth insights into these systems. By making the data easily accessible and visualized, I hope to contribute to better understanding and decision-making around freight logistics. Plus, I've always had an interest in data visualization and geographic information systems (GIS) — so it was a natural project for me.

## Key Design Decisions

### Data-Driven Focus

I chose to center the project around data analysis because that's where most insights live. By using packages like `pandas` and `geopandas`, I'm able to manipulate and visualize geographic data effectively.

### Comprehensive Visualization

Building a clear interface for visualizing freight routes was non-negotiable. I’m using libraries like `folium` and `matplotlib` to create maps and charts that actual users can work with—not just other devs or data scientists.

### Automation

I automated a lot of the processes (like backup and deployment) mainly to minimize manual steps. It's all scripted out with Bash scripts and a Makefile, which saves me time in the long run.

## Tech Stack

Here’s a peek under the hood of what I’m using for this project:

- **Python 3.5+**: This is the backbone of my project.
- **Libraries**: 
  - `pandas` and `geopandas` for data manipulation.
  - `matplotlib` for plotting.
  - `folium` for interactive maps.
  - `contextily` for adding background maps to visualizations.
- **Jupyter Notebooks**: With MyST markdown support for rich documentation.
- **Sphinx**: I’m using this for the project documentation, with extensions like `ablog` and `myst_nb` to enhance functionality.
- **Bash Scripts and Makefile**: These facilitate deployment and backup processes.

## Trade-offs

With any project, there are trade-offs. Here are a few I’ve encountered:

- **Complexity vs. Usability**: I had to balance advanced analysis capabilities while ensuring that the interface remains user-friendly. Too much complexity might scare off users, but too little limits functionality.
- **Real-time Data vs. Static Analysis**: I initially wanted real-time data updates, but the infrastructure for that can be both expensive and complicated. I've opted for periodic updates instead — it’s simpler for now.
- **Deployment Dilemma**: Automating deployment via GitHub Pages is cool, but it creates a delicate dependency on GitHub’s ecosystem. I can't ignore the potential impact if GitHub makes changes to how Pages works.

## Future Work / Roadmap

I’ve got plenty of ideas swirling in my head for future development. Here’s what’s on the slate:

- **Expanded Analysis**: I want to dig deeper into volumetric analysis and broaden the scope to incorporate more freight modalities like trucking and air freight.
- **Automation of Data Updates**: I’m working towards auto-refreshing my datasets to keep everything up to date and relevant without manual intervention.
- **Documentation Improvements**: While I’ve got good coverage at the moment, I’m looking to add more examples and clarify existing documentation for better user experience.
- **Robust Deployment Scripts**: I want to refine my deployment and backup scripts to handle edge cases and errors more gracefully.

## Keeping Up with Updates

If you’re interested in freight analysis, data visualization, or even just following along with my progress, I share updates on [Mastodon](https://mastodon.social/@yourhandle), [Bluesky](https://bsky.app/profile/yourhandle.bsky.social), and [Twitter/X](https://twitter.com/yourhandle). I’d love to connect with anyone who's exploring similar topics!

---

In conclusion, freight.jnapolitano.io is about making visible the often-invisible world of U.S. freight networks. I’m excited about where this project is headed and welcome any collaboration or feedback. Check it out on [GitHub](https://github.com/justin-napolitano/freight.jnapolitano.io) and join me in this journey of exploration!
