# Semantic Enrichment of Historic Documents: Tools and Resources for Document Annotation

## Language Identification

This notebook demonstrates how to run our language identification method for any input document, returning a main language, or a mix of different languages.

#### [Language identification](language-identification_ImpressoHF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/flipz357/impresso-datalab-notebooks/blob/main/annotate/language-identification_ImpressoHF.ipynb)

## Named Entity Recognition and Linking

This repository contains Jupyter notebooks and utilities for performing named entity recognition (NER) and linking (NEL) using models from the HIPE-2022 project. The focus is on detecting named entities such as organizations, locations, persons, and temporal expressions in historical and contemporary texts, and linking them to external knowledge bases like Wikidata and Wikipedia.

### Notebooks

#### [Named Entity Recognition and Linking](NE-processing_ImpressoHF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/annotate/NE-processing_ImpressoHF.ipynb?copy=true)

This notebook identifies named entities and links them to Wikidata and Wikipedia. 

#### [Named Entity Recognition and Linking with Impresso Annotation Services](NE-processing_ImpressoAPI.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/annotate/NE-processing_ImpressoAPI.ipynb?copy=true)

This notebook demonstrates how to use the Impresso Annotation Services to perform named entity recognition and linking on a collection of newspaper articles. It shows how to extract named entities from the Impresso Annotation Services and link them to Wikidata and Wikipedia.

#### [News Agency Entity Recognition](newsagency-processing_ImpressoHF.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-notebooks/blob/main/annotate/newsagency-processing_ImpressoHF.ipynb?copy=true)

This notebook is tailored towards identifying news agencies within historical newspaper articles.

### Requirements

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

## Topic Modeling

Topic modeling annotates your document with topics. Topics are word-clusters that are semantically coherent. It is an unsupervised method for exploration and high-level search of large data.

#### [Todo]
