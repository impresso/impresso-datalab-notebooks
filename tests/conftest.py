"""Shared notebook discovery and fixtures for pytest."""

from pathlib import Path
import subprocess

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


def repository_paths(pattern):
    """Include tracked and new files matching a Git path pattern."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", pattern],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    # Git still lists unstaged deletions; only check files present on disk.
    return sorted(
        {
            REPO_ROOT / name
            for name in result.stdout.split("\0")
            if name and (REPO_ROOT / name).is_file()
        }
    )


NOTEBOOK_PATHS = repository_paths("*.ipynb")
if not NOTEBOOK_PATHS:
    raise RuntimeError("No notebooks found; check notebook discovery.")


@pytest.fixture(params=NOTEBOOK_PATHS, ids=lambda path: str(path.relative_to(REPO_ROOT)))
def notebook_path(request):
    return request.param


@pytest.fixture(scope="session")
def repo_root():
    return REPO_ROOT


@pytest.fixture
def repo_files():
    return repository_paths
