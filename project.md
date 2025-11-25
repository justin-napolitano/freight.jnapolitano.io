---
slug: github-freight-jnapolitano-io
id: github-freight-jnapolitano-io
title: Data Analysis of US Freight Networks with Freight.jnapolitano.io
repo: justin-napolitano/freight.jnapolitano.io
githubUrl: https://github.com/justin-napolitano/freight.jnapolitano.io
generatedAt: '2025-11-24T21:34:48.684Z'
source: github-auto
summary: >-
  Explore the freight.jnapolitano.io project for analyzing and visualizing US
  freight networks using Python and Jupyter Notebooks.
tags:
  - python
  - jupyter
  - geopandas
  - folium
  - data visualization
  - GitHub Pages
  - automation
  - GIS
  - gis mapping
  - github pages
  - sphinx
seoPrimaryKeyword: US freight network analysis
seoSecondaryKeywords:
  - freight data visualization
  - geospatial analysis
  - python data processing
  - automated documentation deployment
  - Jupyter Notebook projects
seoOptimized: true
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

freight.jnapolitano.io is a data-driven project focused on analyzing United States freight networks, including rail, shipping, and intermodal freight transport. The repository contains Jupyter notebooks, scripts, and documentation to support the exploration and visualization of freight infrastructure.

---

## Features

- Analysis and visualization of US freight networks, including rail, shipping routes, and intermodal facilities
- Data processing and GIS mapping using geopandas, folium, and contextily
- Automated build and deployment scripts for generating and publishing documentation
- Backup and deployment automation via Dropbox API and GitHub Pages

---

## Tech Stack

- Python 3.5+ with libraries: pandas, geopandas, matplotlib, folium, contextily
- Jupyter Notebooks with MyST markdown support
- Sphinx documentation with extensions including ablog, myst_nb, sphinx_copybutton
- Bash scripts for deployment and backup
- Makefile for build automation

---

## Getting Started

### Prerequisites

- Python 3.5 or higher
- pip package manager
- Dropbox account and API token (for backup script)
- GitHub CLI (for deployment script)

### Installation

Clone the repository:

```bash
git clone https://github.com/justin-napolitano/freight.jnapolitano.io.git
cd freight.jnapolitano.io
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

- To build the HTML documentation:

```bash
make html
```

- To deploy the built documentation to GitHub Pages:

```bash
./deploy.sh
```

- To backup the HTML build folder to Dropbox:

```bash
python backup_html.py
```

---

## Project Structure

```
freight.jnapolitano.io/
├── acp.sh                # Shell scripts for various automation tasks
├── backup_html.py        # Python script to backup build/html to Dropbox
├── deploy.sh             # Script to deploy documentation to GitHub Pages
├── install.sh            # Installation helper script
├── label_list.py         # Script for reading and analyzing pickle files
├── Makefile              # Build automation file
├── pullit.sh             # Git pull helper script
├── pushit.sh             # Git push helper script
├── python_build.py       # Python script managing build pipeline
├── requirements.txt      # Python dependencies
├── requirements_rocky.txt # Alternative dependencies
├── source/               # Source files for Sphinx documentation and notebooks
│   ├── conf.py           # Sphinx configuration
│   ├── index.md          # Documentation homepage
│   └── parts/            # Documentation parts, including freight analyses
├── todo/                 # Notes and TODOs
└── uninstall.sh          # Uninstall helper script
```

---

## Future Work / Roadmap

- Expand volumetric and network analysis of freight data
- Integrate additional freight modalities such as trucking and air freight
- Automate data updates and refresh workflows
- Improve documentation coverage and examples
- Refine deployment and backup scripts for greater robustness

