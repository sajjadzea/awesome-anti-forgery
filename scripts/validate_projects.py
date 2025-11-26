#!/usr/bin/env python3
"""Validate projects.json formatting and optional link health."""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
except Exception:  # pragma: no cover - optional dependency
    requests = None

ALLOWED_CATEGORIES = {
    "certificates",
    "identity",
    "supply_chain",
    "media_forensics",
    "library",
}

REQUIRED_FIELDS = ["name", "github", "url", "category", "description", "tags", "license"]


def load_projects(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_structure(projects):
    if not isinstance(projects, list):
        raise ValueError("projects.json must contain a list")

    names = set()
    for entry in projects:
        if not isinstance(entry, dict):
            raise ValueError("Each project entry must be an object")

        for field in REQUIRED_FIELDS:
            if field not in entry:
                raise ValueError(
                    f"Missing required field '{field}' in entry: {entry}. "
                    f"Required fields: {', '.join(REQUIRED_FIELDS)}"
                )

        name = entry["name"].strip()
        if not name:
            raise ValueError("Project name cannot be empty")
        if name in names:
            raise ValueError(f"Duplicate project name detected: {name}")
        names.add(name)

        category = entry["category"]
        if category not in ALLOWED_CATEGORIES:
            allowed = ", ".join(sorted(ALLOWED_CATEGORIES))
            raise ValueError(
                f"Invalid category '{category}' for project {name}. Allowed: {allowed}"
            )

        url = entry["url"]
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            raise ValueError(f"Invalid URL '{url}' for project {name}")

        tags = entry.get("tags", [])
        if not isinstance(tags, list):
            raise ValueError(f"Tags must be a list for project {name}")


def check_urls(projects, timeout):
    if requests is None:
        print("requests not available; skipping URL checks", file=sys.stderr)
        return

    for entry in projects:
        url = entry["url"]
        try:
            response = requests.head(url, allow_redirects=True, timeout=timeout)
            if response.status_code >= 400:
                raise ValueError(
                    f"URL check failed for {entry['name']} ({url}): status {response.status_code}"
                )
        except Exception as exc:  # pragma: no cover - network variability
            raise ValueError(
                f"URL check failed for {entry['name']} ({url}): {exc}"
            )


def main():
    parser = argparse.ArgumentParser(description="Validate projects.json")
    parser.add_argument("--check-urls", action="store_true", help="Perform HTTP HEAD requests for each project URL")
    parser.add_argument("--path", default="projects.json", help="Path to projects.json")
    parser.add_argument("--timeout", type=float, default=5.0, help="Timeout for URL checks in seconds")
    args = parser.parse_args()

    path = Path(args.path)
    try:
        projects = load_projects(path)
        validate_structure(projects)
        if args.check_urls:
            check_urls(projects, args.timeout)
    except Exception as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1

    print("projects.json validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
