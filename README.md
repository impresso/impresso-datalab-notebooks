# Impresso Datalab Notebooks

![License: AGPLV3+](https://img.shields.io/badge/License-AGPLV3+-brightgreen.svg) ![Python](https://img.shields.io/badge/Python->=3.10-blue.svg) [![Generic badge](https://img.shields.io/badge/Status-WIP!-red.svg)](https://shields.io/)

## About

The Impresso project develops application interfaces to facilate historical transmedia research through:

- the **[Impresso Web App](https://impresso-project.ch/app)**, a user interface for content exploration and visualisation.
- the **[Impresso Datalab]()**, a suite of tools for data exploration and analysis.

Specifically, the Impresso Datalab enables custom analyses of the Impresso corpus, and the semantic indexation of external document collections also with Impresso models. We offer access to the Impresso corpus, data and models via the Impresso Public API, a dedicated Python library, and HuggingFace. For more information, be sure to visit the [Datalab website](https://dev.impresso-project.ch/datalab/about/).

## Contents

This repository contains notebooks that illustrate how to use the **[Impresso Public API](#)** (coming soon!) and **Impresso Models**, allowing you to search through Impresso data and use Impresso annotation models.    
 
  
- **Impresso Public API**: The software component that provides third-party access to the Impresso backend.    
- **Impresso Python Library**: The preferred method for users to interact with the Impresso Public API.    
- **Impresso Models**: A collection of models trained to annotate the Impresso Corpus, made publicly available to facilitate the annotation of external documents, enabling comparison and analysis of semantic enrichments. Impresso models can be accessed through the [Impresso Hugging Face organisation](https://huggingface.co/impresso-project) and via annotation services offered through the API.    

Before getting started, check out how to create an account and obtain an API token on the [Impresso Datalab website]().     


## Notebooks

### Getting Started

The notebooks in the [`starter`](https://github.com/impresso/impresso-datalab-notebooks/tree/main/starter) folder will help you get started with the Impresso Public API and Python library:

- [basics_ImpressoAPI](https://github.com/impresso/impresso-datalab-notebooks/blob/main/starter/basics_ImpressoAPI.ipynb)
- [search]()
- [collection]()


### Explore and Visualise your Impresso data

The notebooks in the [`explore-vis`](https://github.com/impresso/impresso-datalab-notebooks/tree/main/explore-vis) folder help you build complementary views on your Impresso data:

- [entity_network](https://github.com/impresso/impresso-datalab-notebooks/blob/main/explore-vis/entity_network.ipynb)
- [place-entities_map](https://github.com/impresso/impresso-datalab-notebooks/blob/main/explore-vis/place-entities_map.ipynb)

### Annotate your Documents with Impresso Models

The notebooks in the [`annotate`](https://github.com/impresso/impresso-datalab-notebooks/tree/main/annotate) folder demonstrate how to use Impresso models, either from the [Hugging Face hub](https://huggingface.co/impresso-project) or through the Impresso API. These notebooks guide you in annotating your documents to produce annotations that are compatible with those in the Impresso corpus.

- [Language identification](https://github.com/impresso/impresso-datalab-notebooks/blob/main/annotate/language-identification_ImpressoHF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/annotate/language-identification_ImpressoHF.ipynb)

- [NE-processing_ImpressoHF](https://github.com/impresso/impresso-datalab-notebooks/blob/main/annotate/NE-processing_ImpressoHF.ipynb) to use NER and EL Impresso model from Hugging Face (HF). [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/annotate/NE-processing_ImpressoHF.ipynb)

- [NE-processing_ImpressoAPI](https://github.com/impresso/impresso-datalab-notebooks/blob/main/annotate/NE-processing_ImpressoAPI.ipynb) to use NER and EL Impresso model via the Impresso API. [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/annotate/NE-processing_ImpressoAPI.ipynb?copy=true)

- [newsagency-processing_ImpressoHF](https://github.com/impresso/impresso-datalab-notebooks/blob/main/annotate/newsagency-processing_ImpressoHF.ipynb)  to use the Impresso newsagency recognition model from Hugging Face [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/impresso/impresso-datalab-notebooks/blob/main/annotate/newsagency-processing_ImpressoHF.ipynb).

- [language-identification_ImpressoHF.ipynb](https://github.com/impresso/impresso-datalab-notebooks/blob/main/annotate/language-identification_with_ImpressoHF.ipynb)


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
