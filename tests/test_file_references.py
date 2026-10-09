"""Check static local file references without making network requests."""

import json
import re
import shlex
from urllib.parse import unquote, urlsplit

import mistune
import pytest
import yaml


def assert_paths_exist(references):
    missing = [f"{origin}: missing {path}" for origin, path in references if not path.exists()]
    if missing:
        pytest.fail("\n".join(missing), pytrace=False)


def local_link_path(url, document, repo_root):
    parsed = urlsplit(url)
    path = unquote(parsed.path)
    # Treat links to this repository on GitHub/Colab as local references.
    if parsed.netloc in {"github.com", "colab.research.google.com"}:
        path = path.removeprefix("/github")
        match = re.fullmatch(
            r"/impresso/impresso-datalab-notebooks/(?:blob|tree)/(?:main|master)/(.*)", path
        )
        return repo_root / match[1] if match else None
    if parsed.scheme or parsed.netloc or not path:
        return None
    return repo_root / path.lstrip("/") if path.startswith("/") else document.parent / path


def markdown_links(nodes):
    for node in nodes:
        if node["type"] in {"link", "image"}:
            yield node["attrs"]["url"]
        yield from markdown_links(node.get("children", []))


def test_readme_file_links(repo_root, repo_files):
    parser = mistune.create_markdown(renderer="ast")
    references = []
    for document in repo_files("*README.md"):
        for url in markdown_links(parser(document.read_text(encoding="utf-8"))):
            target = local_link_path(url, document, repo_root)
            if target is not None:
                references.append((f"{document.relative_to(repo_root)} link {url}", target))
    assert_paths_exist(references)


def test_docker_copy_sources(repo_root):
    references = []
    text = (repo_root / "Dockerfile").read_text(encoding="utf-8")
    for number, line in enumerate(re.sub(r"\\\n\s*", " ", text).splitlines(), start=1):
        match = re.match(r"\s*(?:COPY|ADD)\s+(.+)", line, re.IGNORECASE)
        if not match:
            continue
        instruction = match[1]
        if re.search(r"--from(?:=|\s)", instruction):
            continue  # These sources live in another build stage/image.
        instruction = re.sub(r"^((?:--\S+\s+)+)", "", instruction)
        parts = json.loads(instruction) if instruction.startswith("[") else shlex.split(instruction)
        for source in parts[:-1]:
            if urlsplit(source).scheme or "$" in source:
                continue
            origin = f"Dockerfile:{number}"
            if any(char in source for char in "*?["):
                if not list(repo_root.glob(source)):
                    pytest.fail(f"{origin}: no files match {source}", pytrace=False)
            else:
                references.append((origin, repo_root / source.lstrip("/")))
    assert_paths_exist(references)


def test_compose_local_paths(repo_root):
    config = yaml.safe_load((repo_root / "docker-compose.yml").read_text(encoding="utf-8"))
    references = []
    for name, service in config["services"].items():
        origin = f"docker-compose.yml service {name}"
        build = service.get("build")
        if build:
            context = build if isinstance(build, str) else build.get("context", ".")
            if not urlsplit(context).scheme and "$" not in context:
                context_path = repo_root / context
                references.append((origin, context_path))
                if isinstance(build, dict):
                    references.append((origin, context_path / build.get("dockerfile", "Dockerfile")))
        for volume in service.get("volumes", []):
            if isinstance(volume, str):
                source = volume.split(":", 1)[0]
                if not source.startswith((".", "/")):
                    continue  # A named Docker volume, not a host folder.
            elif volume.get("type") == "bind":
                source = volume["source"]
            else:
                continue
            if "$" not in source:
                references.append((origin, repo_root / source))
    assert_paths_exist(references)


def test_workflow_file_inputs(repo_root, repo_files):
    references = []
    workflows = repo_files(".github/workflows/*.yml") + repo_files(".github/workflows/*.yaml")
    for workflow in workflows:
        config = yaml.safe_load(workflow.read_text(encoding="utf-8"))
        for job in config.get("jobs", {}).values():
            for step in job.get("steps", []):
                origin = f"{workflow.relative_to(repo_root)} step {step.get('name', 'unnamed')}"
                inputs = step.get("with", {})
                for key in ("notebook", "python-version-file", "cache-dependency-path"):
                    for path in str(inputs.get(key, "")).splitlines():
                        path = path.strip()
                        if not path or "$" in path:
                            continue
                        if any(char in path for char in "*?["):
                            if not list(repo_root.glob(path)):
                                pytest.fail(f"{origin}: no files match {path}", pytrace=False)
                        else:
                            references.append((origin, repo_root / path))
    assert_paths_exist(references)
