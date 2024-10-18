# Named Entity Recognition and Linking

This repository contains Jupyter notebooks and utilities for performing named entity recognition (NER) and linking (NEL) using models from the HIPE-2022 project. The focus is on detecting named entities such as organizations, locations, persons, and temporal expressions in historical and contemporary texts, and linking them to external knowledge bases like Wikidata and Wikipedia.

## Notebooks

### [Named Entity Recognition and Linking](annotation_NERC_EL_HF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_NERC_EL_HF.ipynb?copy=true)

This notebook identifies named entities and links them to Wikidata and Wikipedia. 

### [News Agency Entity Recognition](annotation_newsagencies.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_newsagencies.ipynb?copy=true)

This notebook is tailored towards identifying news agencies within historical newspaper articles.

### [Named Entity Recognition and Linking with Impresso Annotation Services](annotation_NERC_EL_impresso_services.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/annotation_NERC_EL_impresso_services.ipynb?copy=true)

This notebook demonstrates how to use the Impresso Annotation Services to perform named entity recognition and linking on a collection of newspaper articles. It shows how to extract named entities from the Impresso Annotation Services and link them to Wikidata and Wikipedia.


## Requirements

To run the notebooks, ensure you have the following Python packages installed:

- transformers
- torch


You can install these packages using pip:

```bash
pip install transformers torch 
```
