"""Validate all notebooks and check syntax without executing notebook code."""

import ast
import json

from IPython.core.inputtransformer2 import TransformerManager
import nbformat
import pytest


def test_notebook_format(notebook_path):
    notebook = nbformat.from_dict(json.loads(notebook_path.read_text(encoding="utf-8")))
    nbformat.validate(notebook)


def test_code_cell_syntax(notebook_path, repo_root):
    transformer = TransformerManager()
    relative_path = str(notebook_path.relative_to(repo_root))
    notebook = nbformat.read(notebook_path, as_version=4)
    errors = []
    for index, cell in enumerate(notebook.cells, start=1):
        if cell.cell_type != "code":
            continue
        try:
            # Convert IPython commands to Python without executing them.
            source = transformer.transform_cell(cell.source)
            compile(
                source,
                filename=f"{relative_path}:cell {index}",
                mode="exec",
                flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT,
                dont_inherit=True,
            )
        except SyntaxError as error:
            errors.append(f"Cell {index}, line {error.lineno}: {error.msg}\n{error.text or ''}")
    if errors:
        pytest.fail("\n".join(errors), pytrace=False)
