---
slug: "github-freight.jnapolitano.io"
title: "freight.jnapolitano.io"
repo: "justin-napolitano/freight.jnapolitano.io"
githubUrl: "https://github.com/justin-napolitano/freight.jnapolitano.io"
generatedAt: "2025-11-23T08:58:01.888666Z"
source: "github-auto"
---


# freight.jnapolitano.io: Technical Overview and Implementation Notes

## Motivation

This project was initiated to systematically analyze and understand the freight transportation networks across the United States. The focus is on rail, shipping, and intermodal freight systems, aiming to provide insights into infrastructure, logistics, and spatial distribution of freight facilities. The work supports research and policy analysis by mapping and quantifying freight flows and hubs.

## Problem Addressed

Freight transportation is critical to economic activity but complex due to multiple modes and networks. Existing data is fragmented and often lacks integration across rail, shipping, and intermodal modalities. This project addresses the need for a unified analytical framework to visualize, analyze, and interpret freight networks using geospatial data and modern data science tools.

## How It's Built

### Data and Analysis

The core of the project uses geospatial datasets such as navigable waterways, ports, intermodal freight facilities, and rail freight stations. These datasets are processed using Python libraries including geopandas for spatial data manipulation, pandas for tabular data handling, folium for interactive maps, and contextily for basemap tiles.

The project leverages Jupyter notebooks with MyST markdown for literate programming, allowing code, narrative, and visualizations to coexist. This facilitates iterative exploration and documentation.

### Automation and Deployment

A set of shell scripts and Python utilities manage the build, deployment, and backup processes:

- `Makefile` orchestrates build steps such as cleaning and generating HTML documentation via Sphinx.
- `deploy.sh` uses `ghp-import` to publish the built site to GitHub Pages.
- `backup_html.py` uploads the HTML build directory to Dropbox using the Dropbox API, ensuring offsite backups.
- Additional scripts (`install.sh`, `pullit.sh`, `pushit.sh`) assist with environment setup and version control operations.

### Documentation

Sphinx is configured with several extensions to support blogging (`ablog`), notebook integration (`myst_nb`), and enhanced UI features (`sphinx_design`, `sphinx_togglebutton`). The documentation structure is modular, with sections dedicated to freight overview, rail, shipping, intermodal analysis, and bibliographic references.

## Implementation Details

- The `python_build.py` script encapsulates the build pipeline, running dependency installation, cleaning, building, committing, and pushing changes programmatically.
- The `backup_html.py` script requires a Dropbox access token and handles error conditions such as insufficient storage gracefully.
- Geospatial data is converted to EPSG 3857 projection to enable consistent mapping and overlay with basemaps.
- Interactive maps use `geopandas.explore()` for quick visualization during analysis.
- The project includes pickle file readers (`label_list.py`) to extract and inspect serialized Sphinx environment data.

## Practical Notes

- The project assumes familiarity with Python 3.5+, shell scripting, and Git workflows.
- Data paths are currently hardcoded and should be parameterized for portability.
- Some scripts and notebooks reference local file paths and require adjustment before reuse.
- The deployment process assumes GitHub CLI and repository permissions are configured.

## Summary

freight.jnapolitano.io provides a reproducible framework for freight network analysis combining geospatial data processing, automated documentation builds, and deployment pipelines. It serves as a technical foundation for ongoing research into US freight infrastructure and logistics.
