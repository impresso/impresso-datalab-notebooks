# Impresso Starter Pack

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/impresso/impresso-datalab-starter-pack/HEAD?labpath=main.ipynb)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/impresso/impresso-datalab-starter-pack/blob/main/main.ipynb)

This repository contains the code and data for the [Impresso](https://impresso-project.ch) project's starter pack. The starter pack is a collection of tools and resources to help you get started with the Impresso data. It includes a set of Jupyter notebooks that demonstrate how to access and analyze the data, as well as a set of Python scripts that can be used to download the data and prepare it for analysis.

The repo Dockerfile has been created following the guidelines in https://mybinder.readthedocs.io/en/latest/tutorials/dockerfile.html

## Getting Started on your local machine, using pipenv

With `pipenv` installed, you can install the dependencies by running:

```bash
pipenv install
```

Then, you can start the Jupyter notebook server by running:

```bash
pipenv run jupyter lab
```

Note: remeember to `pipenv requirements > requirements.txt` to keep the requirements file updated and in sync with the Pipfile, and `pipenv run black .` to format the code.

## Getting Started on your local machine, using conda

With `conda` installed, you can install the dependencies by running:

```bash
conda env create -f environment.yml
conda activate impresso
```

Then, you can start the Jupyter notebook server by running:

```bash
jupyter lab
```

## Getting Started on your local machine, using Docker

With `Docker` installed, you can run the image with docker compose:

```bash
docker compose up
```

Then, you can access the Jupyter notebook server at `http://localhost:8888`.

## Project

The 'impresso - Media Monitoring of the Past' project is funded by the Swiss National Science Foundation (SNSF) under grant number CRSII5_173719 (Sinergia program). The project aims at developing tools to process and explore large-scale collections of historical newspapers, and at studying the impact of this new tooling on historical research practices. More information at https://impresso-project.ch.

## License

Copyright (C) 2024 The impresso team. Contributors to this program include: Daniele Guido, Roman Kalyakin. This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU Affero General Public License for more details.
