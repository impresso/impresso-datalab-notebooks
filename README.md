# Impresso Datalab Notebooks

![License: AGPLV3+](https://img.shields.io/badge/License-AGPLV3+-brightgreen.svg) ![Python](https://img.shields.io/badge/Python->=3.10-blue.svg) [![Generic badge](https://img.shields.io/badge/Status-WIP!-red.svg)](https://shields.io/)

The Impresso project develops application interfaces to enable historical transmedia research with:

- the **[Impresso web app](https://impresso-project.ch/app)**, a user interface for content exploration and visualisation.
- the **[Impresso Datalab]()**, a suite of tools for data exploration and analysis on the Impresso corpus and enrichments, and with Impresso models.

The two interfaces communicate and one can easily switch from one to the other, e.g. start a search in the web app, and then decide to open the query in the Datalab with a notebook.

This repository contains notebooks that illustrate how to explore

1. the [Impresso Public API]().
2. the [Impresso models](https://huggingface.co/impresso-project) and annotation services.

## Notebooks

### ➤ Getting Started

To get you started with the Impresso Public API, the Starter Pack includes a set of notebooks that illustrate how to access, download, and explore the data.

- [starter_01_environment](): a notebook that explains the basics of Python environment and libraries in [Google Colab](https://colab.google/).
- [starter_02_impresso_api](): a notebook that explains how to use the Impresso API, what data can be retrieved and how to explore it.

### ➤ Explore and Visualise your Impresso data

### ➤ Annotate your Documents with Impresso Models

A series of notebooks that illustrate how to access and explore entities in the impresso corpus, and how to use Impresso entity models. Impresso shares its [models](https://huggingface.co/impresso-project) on Hugging Face. You can use them to annotate your documents, thus obtaining annotations that are compatible with those of the Impresso corpus.

- [annotation_NERC_EL_HF](https://github.com/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_NERC_EL_HF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_NERC_EL_HF.ipynb): a notebook that explains how to use the Impresso NER and EL models to annotate entities in a text.

- [annotation_newsagencies](https://github.com/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_newsagencies.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_newsagencies.ipynb): a notebook that explains how to use the Impresso NER model to annotate news agencies in a text.

- [annotation_NERC_EL_impresso_service](https://github.com/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_NERC_EL_impresso_service.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_NERC_EL_impresso_service.ipynb): a notebook that explains how to use the Impresso NER and EL models to annotate entities in a text using the Impresso Annotation Services.

## About Impresso

### Impresso project

[Impresso - Media Monitoring of the Past](https://impresso-project.ch) is an
interdisciplinary research project that aims to develop and consolidate tools for
processing and exploring large collections of media archives across modalities, time,
languages and national borders. The first project (2017-2021) was funded by the Swiss
National Science Foundation under grant
No. [CRSII5_173719](http://p3.snf.ch/project-173719) and the second project (2023-2027)
by the SNSF under grant No. [CRSII5_213585](https://data.snf.ch/grants/grant/213585)
and the Luxembourg National Research Fund under grant No. 17498891.

### Copyright

Copyright (C) 2024 The Impresso team.

### License

This program is provided as open source under
the [GNU Affero General Public License](https://github.com/impresso/impresso-pyindexation/blob/master/LICENSE)
v3 or later.

---

<p align="center">
  <img src="https://github.com/impresso/impresso.github.io/blob/master/assets/images/3x1--Yellow-Impresso-Black-on-White--transparent.png?raw=true" width="350" alt="Impresso Project Logo"/>
</p>
