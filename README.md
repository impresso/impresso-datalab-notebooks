# Impresso Named Entity Recognition Notebooks

Welcome to the impresso Named Entity Recognition (NER) Notebook Series!

In this series of notebooks, we delve into the fascinating world of Named Entity Recognition (NER) within the context of the impresso project. Named Entity Recognition involves identifying and classifying named entities, such as locations, persons, organizations, and more, within a body of text.

## Detect random First steps into NER with _impresso_ model and HugginFace

By [emanuelaboros](https://huggingface.co/emanuelaboros)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/impresso/impresso-datalab-ner-notebooks/HEAD?labpath=main.ipynb)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-ner-notebooks/blob/main/main.ipynb)

In this notebook, we introduce the Named Entity Recognition (NER) task and show how to use the HuggingFace Transformers library with our [Bert NER model for French](https://huggingface.co/impresso-project/bert-newsagency-ner-fr) to perform NER on impresso newspaper articles. We use the `transformers` library to load our pre-trained NER model and apply it to a sample text.

To simply test the transformer with a random text, just go to the related [hugging space](https://huggingface.co/spaces/impresso-project/news-agency-recognition-in-french)

## Project

The 'impresso - Media Monitoring of the Past' project is funded by the Swiss National Science Foundation (SNSF) under grant number CRSII5_173719 (Sinergia program). The project aims at developing tools to process and explore large-scale collections of historical newspapers, and at studying the impact of this new tooling on historical research practices. More information at https://impresso-project.ch.

## License

Copyright (C) 2024 The impresso team. Contributors to this program include: Daniele Guido, Roman Kalyakin. This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU Affero General Public License for more details.
