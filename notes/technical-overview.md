---
slug: github-freight-jnapolitano-io-note-technical-overview
id: github-freight-jnapolitano-io-note-technical-overview
title: freight.jnapolitano.io Overview
repo: justin-napolitano/freight.jnapolitano.io
githubUrl: https://github.com/justin-napolitano/freight.jnapolitano.io
generatedAt: '2025-11-24T18:36:27.539Z'
source: github-auto
summary: >-
  freight.jnapolitano.io is a tool for analyzing US freight networks, including
  rail, shipping, and intermodal transport. It provides Jupyter notebooks and
  scripts for data exploration and visualization.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

freight.jnapolitano.io is a tool for analyzing US freight networks, including rail, shipping, and intermodal transport. It provides Jupyter notebooks and scripts for data exploration and visualization.

## Key Features

- Analyze US freight routes and facilities.
- Use **geopandas**, **folium**, and **contextily** for mapping.
- Automated documentation with **Sphinx**.
- Backup to Dropbox and deploy via GitHub Pages.

## Getting Started

### Prerequisites

- Python 3.5+
- Pip
- Dropbox API token
- GitHub CLI

### Installation

Clone the repo:

```bash
git clone https://github.com/justin-napolitano/freight.jnapolitano.io.git
cd freight.jnapolitano.io
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

- Build HTML documentation:

```bash
make html
```

- Deploy to GitHub Pages:

```bash
./deploy.sh
```

- Backup to Dropbox:

```bash
python backup_html.py
```

### Gotchas

Ensure your Dropbox API is set up. Check the **Makefile** for commands and automation support.
