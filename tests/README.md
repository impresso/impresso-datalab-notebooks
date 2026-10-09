# Notebook checks

`test_notebook_validation_and_syntax.py` contains the notebook format and syntax
checks. Add future checks in separate `test_*.py` files in this folder so pytest
discovers them automatically.

`test_file_references.py` checks README links to local files (including links to
this repository on GitHub and Colab), Docker COPY/ADD sources, Compose build and
bind-mount paths, and workflow file inputs (`notebook`, `python-version-file`, and
`cache-dependency-path`). It does not visit external websites, check link anchors,
or interpret dynamic paths, arbitrary shell commands, or container-only paths.

`conftest.py` provides shared notebook discovery and the `notebook_path` and
`repo_root` fixtures. Pytest makes these available to every test file in this
folder without imports.

GitHub runs all pytest tests automatically on pull requests through
`.github/workflows/pytest.yml`, using the Python version in `.python-version`.
The workflow can also be started manually from GitHub's Actions tab.

From the repository root, with the project Python environment active, install
the test dependencies and run:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests -v
```

Or use Pipenv:

```bash
pipenv run python -m pip install -r requirements-dev.txt
pipenv run python -m pytest tests -v
```

The checks use `nbformat` and `IPython`, already included in the shared
dependencies, plus pytest from `requirements-dev.txt`. They check every tracked or new, non-ignored `.ipynb` file,
including workshop notebooks. Git must be available.

The checks validate notebook structure and compile each code cell after converting
IPython commands such as `%pip` and `!pip` to Python. Notebook code is never run:
no packages are installed, API requests made, or models downloaded. Top-level
`await` is supported, as it is in Jupyter.

Failures identify the notebook and, for syntax errors, the cell number (counting
all cells, starting at 1). These checks do not verify imports, results, or whether
cells work when executed together. Commands inside magics and shell commands are
not syntax-checked as Python.
