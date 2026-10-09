"""Shared notebook discovery and fixtures for pytest."""

from pathlib import Path
import subprocess

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


def notebook_paths():
    """Include tracked and new notebooks, excluding Git-ignored files."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", "*.ipynb"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted({REPO_ROOT / name for name in result.stdout.split("\0") if name})


NOTEBOOK_PATHS = notebook_paths()
if not NOTEBOOK_PATHS:
    raise RuntimeError("No notebooks found; check notebook discovery.")


@pytest.fixture(params=NOTEBOOK_PATHS, ids=lambda path: str(path.relative_to(REPO_ROOT)))
def notebook_path(request):
    return request.param


@pytest.fixture(scope="session")
def repo_root():
    return REPO_ROOT
