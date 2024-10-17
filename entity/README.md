# Named Entity Recognition and Linking

This repository contains Jupyter notebooks and utilities for performing named entity recognition (NER) and linking (NEL) using models from the HIPE-2022 project. The focus is on detecting named entities such as organizations, locations, persons, and temporal expressions in historical and contemporary texts, and linking them to external knowledge bases like Wikidata and Wikipedia.

## Notebooks

### [Named Entity Recognition and Linking](annotation_NERC_EL_HF.ipynb)
Building on the `NE_01_ner.ipynb` notebook, this notebook not only identifies generic named entities but also focuses on generating Wikidata and Wikipedia links for these entities. This adds valuable metadata to your text, providing deeper insights and connections to structured knowledge bases.
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/2-entity/annotation_NERC_EL_HF.ipynb?copy=true)

### [News Agency Entity Recognition](annotation_newsagencies.ipynb)
This notebook is tailored towards identifying news agencies within historical newspaper articles. Using a pre-trained NER model, it highlights the role and mentions of news agencies in your text.
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_newsagencies.ipynb?copy=true)

### [Named Entity Recognition and Linking with _Impresso_ API](annotation_NERC_EL_impresso_services.ipynb)
This notebook demonstrates how to use the _Impresso_ API to perform named entity recognition and linking on a collection of newspaper articles. It shows how to extract named entities from the _Impresso_ API and link them to Wikidata and Wikipedia.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/2-entity/annotation_NERC_EL_impresso_services.ipynb?copy=true)


## Requirements

To run the notebooks, ensure you have the following Python packages installed:

- transformers
- torch


You can install these packages using pip:

```bash
pip install transformers torch 
```
