# Named Entity Recognition and Linking

This repository contains Jupyter notebooks and utilities for performing named entity recognition (NER) and linking (NEL) using models from the HIPE-2022 project. The focus is on detecting named entities such as organizations, locations, persons, and temporal expressions in historical and contemporary texts, and linking them to external knowledge bases like Wikidata and Wikipedia.

## Notebooks

### 1. [generic-entity.ipynb](generic-entity.ipynb)
This notebook demonstrates how to set up a workflow for identifying generic named entities within your text. It uses a pre-trained NER model to detect mentions of people, places, organizations, and temporal expressions.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/ner-nel-project/blob/main/generic-entity.ipynb)

### 2. [generic-linked-entity.ipynb](generic-linked-entity.ipynb)
Building on the `generic-entity.ipynb` notebook, this notebook not only identifies generic named entities but also focuses on generating Wikidata and Wikipedia links for these entities. This adds valuable metadata to your text, providing deeper insights and connections to structured knowledge bases.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/ner-nel-project/blob/main/generic-linked-entity.ipynb)

### 3. [news-agency-entity.ipynb](news-agency-entity.ipynb)
This notebook is tailored towards identifying news agencies within historical newspaper articles. Using a pre-trained NER model, it highlights the role and mentions of news agencies in your text.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/ner-nel-project/blob/main/news-agency-entity.ipynb)

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