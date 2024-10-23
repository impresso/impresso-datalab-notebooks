# Named Entity Recognition and Linking

This repository contains Jupyter notebooks and utilities for performing named entity recognition (NER) and linking (NEL) using models from the HIPE-2022 project. The focus is on detecting named entities such as organizations, locations, persons, and temporal expressions in historical and contemporary texts, and linking them to external knowledge bases like Wikidata and Wikipedia.

## Notebooks

### [Named Entity Recognition and Linking](NE-processing_with_ImpressoHF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/NE-processing_with_ImpressoHF.ipynb?copy=true)

This notebook identifies named entities and links them to Wikidata and Wikipedia. 

### [Named Entity Recognition and Linking with Impresso Annotation Services](NE-processing_with_ImpressoAPI.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/NE-processing_with_ImpressoAPI.ipynb?copy=true)

This notebook demonstrates how to use the Impresso Annotation Services to perform named entity recognition and linking on a collection of newspaper articles. It shows how to extract named entities from the Impresso Annotation Services and link them to Wikidata and Wikipedia.

### [News Agency Entity Recognition](newsagency-processing_with_ImpressoHF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/entity/newsagency-processing_with_ImpressoHF.ipynb?copy=true)

This notebook is tailored towards identifying news agencies within historical newspaper articles.


## Requirements

To run the notebooks, ensure you have the following Python packages installed. Otherwise, you can install them directly in the notebooks.

- transformers
- torch
- nltk
- sentencepiece
- protobuf


You can install these packages using pip:

```bash
pip install transformers torch nltk sentencepiece protobuf
```
