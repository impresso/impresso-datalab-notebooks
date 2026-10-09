FROM quay.io/jupyter/scipy-notebook:python-3.12

USER root
RUN usermod --login impresso --home /home/impresso --move-home jovyan
ENV NB_USER=impresso HOME=/home/impresso USER=impresso
USER impresso

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /home/impresso

COPY --chown=impresso:users starter ./starter
COPY --chown=impresso:users explore-vis ./explore-vis
COPY --chown=impresso:users annotate ./annotate
COPY --chown=impresso:users workshop_resources ./workshop_resources
COPY --chown=impresso:users documentation ./documentation
COPY --chown=impresso:users README.md LICENSE reporting-problems.md ./

# The base startup script assumes a user named jovyan exists.
# Start Jupyter directly as impresso, keeping tini for process cleanup.
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.py", "--ServerApp.root_dir=/home/impresso"]
