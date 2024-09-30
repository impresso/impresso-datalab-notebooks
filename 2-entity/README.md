# Named Entity Recognition and Linking

This repository contains Jupyter notebooks and utilities for performing named entity recognition (NER) and linking (NEL) using models from the HIPE-2022 project. The focus is on detecting named entities such as organizations, locations, persons, and temporal expressions in historical and contemporary texts, and linking them to external knowledge bases like Wikidata and Wikipedia.

## Notebooks

### 1. [Generic Entity Recognition](NE_01_ner.ipynb)
This notebook demonstrates how to set up a workflow for identifying generic named entities within your text. It uses a pre-trained NER model to detect mentions of people, places, organizations, and temporal expressions.
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/2-entity/NE_01_ner.ipynb?copy=true)

### 2. [Generic Entity Recognition and Linking](NE_01_ner_nel.ipynb)
Building on the `NE_01_ner.ipynb` notebook, this notebook not only identifies generic named entities but also focuses on generating Wikidata and Wikipedia links for these entities. This adds valuable metadata to your text, providing deeper insights and connections to structured knowledge bases.
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/2-entity/NE_02_ner_nel.ipynb?copy=true)

### 3. [News Agency Entity Recognition](NE_03_newsagencies.ipynb)
This notebook is tailored towards identifying news agencies within historical newspaper articles. Using a pre-trained NER model, it highlights the role and mentions of news agencies in your text.
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/2-entity/NE_03_newsagencies.ipynb?copy=true)

### 4. [Generic Named Entity Recognition and Linking with _Impresso_ API](NE_04_ner_nel_API.ipynb)
This notebook demonstrates how to use the _Impresso_ API to perform named entity recognition and linking on a collection of newspaper articles. It shows how to extract named entities from the _Impresso_ API and link them to Wikidata and Wikipedia.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/2-entity/NE_04_ner_nel_API.ipynb?copy=true)

## Utilities

### utils.py
This Python script contains utility functions used across the notebooks. It includes functions for retrieving Wikipedia page properties and linking entities to Wikidata.

## Setup

To use these notebooks, you might need to set the `HF_TOKEN` environment variable. You can get your token by signing up on the [Hugging Face website](https://huggingface.co/join) and read more in the [official documentation](https://huggingface.co/docs/huggingface_hub/v0.20.2/en/quick-start#environment-variable).

## Requirements

To run the notebooks, ensure you have the following Python packages installed:

- transformers
- torch
- pandas
- requests
- nltk

You can install these packages using pip:

```bash
pip install transformers torch pandas requests nltk
```

Also, be sure to also have the `nltk` data downloaded:

```bash
python -m nltk.downloader averaged_perceptron_tagger
```