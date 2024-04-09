FROM quay.io/jupyter/scipy-notebook:python-3.11

USER root

ARG NB_UID=1000
ENV USER impresso
ENV NB_UID ${NB_UID}
ENV HOME /home/impresso

RUN useradd -o \
    --uid ${NB_UID} \
    impresso

COPY notebooks ${HOME}

RUN chown -R ${NB_UID} ${HOME}
USER impresso

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR ${HOME}

RUN python --version