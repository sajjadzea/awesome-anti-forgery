#!/usr/bin/env python3
"""Generate the categorized project tables inside README.md."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_PATH = ROOT / "projects.json"
README_PATH = ROOT / "README.md"

CATEGORY_METADATA = {
    "certificates": {
        "title": "گواهی‌نامه و اسناد",
        "description": "پروژه‌های صدور، ذخیره و اعتبارسنجی مدارک دیجیتال.",
    },
    "identity": {
        "title": "هویت و احراز هویت",
        "description": "زیرساخت هویت، SSO، MFA و شناسه‌های غیرمتمرکز.",
    },
    "supply_chain": {
        "title": "زنجیره تأمین و ضدتقلب",
        "description": "ردیابی منشأ دارایی‌ها و جلوگیری از جعل کالا در زنجیره تأمین.",
    },
    "media_forensics": {
        "title": "رسانه و تشخیص دستکاری",
        "description": "مدل‌ها و ابزارهای تشخیص دیپ‌فیک و رسانه دستکاری‌شده.",
    },
    "library": {
        "title": "کتابخانه‌ها و ابزارهای رمزنگاری",
        "description": "لایه رمزنگاری پایه برای امضا، هش و مدیریت کلید.",
    },
}

CATEGORY_ORDER = [
    "certificates",
    "identity",
    "supply_chain",
    "media_forensics",
    "library",
]

START_MARKER = "<!-- AUTO-GENERATED: PROJECT TABLES START -->"
END_MARKER = "<!-- AUTO-GENERATED: PROJECT TABLES END -->"


def load_projects(path: Path) -> List[Dict]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def group_projects(projects: List[Dict]) -> Dict[str, List[Dict]]:
    grouped: Dict[str, List[Dict]] = {category: [] for category in CATEGORY_ORDER}
    for project in projects:
        category = project.get("category")
        if category not in grouped:
            grouped.setdefault(category, []).append(project)
        else:
            grouped[category].append(project)

    for entries in grouped.values():
        entries.sort(key=lambda item: item.get("name", "").lower())
    return grouped


def render_tables(grouped: Dict[str, List[Dict]]) -> str:
    sections: List[str] = []
    sections.append('<div dir="rtl">')
    for category in CATEGORY_ORDER:
        projects = grouped.get(category, [])
        if not projects:
            continue

        metadata = CATEGORY_METADATA.get(category, {})
        title = metadata.get("title", category)
        description = metadata.get("description", "")

        sections.append(f"### {title}")
        if description:
            sections.append(description)
        sections.append("")
        sections.append("| پروژه | توضیح کوتاه | لایسنس | برچسب‌ها |")
        sections.append("| --- | --- | --- | --- |")

        for project in projects:
            name = escape_cell(project.get("name", ""))
            url = project.get("url") or project.get("github")
            link = f"[{name}]({url})" if url else name
            description_cell = escape_cell(project.get("description", ""))
            license_cell = escape_cell(project.get("license", ""))
            tags = project.get("tags", []) or []
            tags_cell = escape_cell("، ".join(tags))
            row = f"| {link} | {description_cell} | {license_cell} | {tags_cell} |"
            sections.append(row)

        sections.append("")

    sections.append("</div>")
    return "\n".join(sections).strip() + "\n"


def replace_block(content: str, new_block: str) -> str:
    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        flags=re.DOTALL,
    )
    if not pattern.search(content):
        raise RuntimeError("Unable to find auto-generated block markers in README.md")
    return pattern.sub(f"{START_MARKER}\n{new_block}{END_MARKER}", content)


def main() -> None:
    projects = load_projects(PROJECTS_PATH)
    grouped = group_projects(projects)
    tables_markdown = render_tables(grouped)

    readme_text = README_PATH.read_text(encoding="utf-8")
    updated = replace_block(readme_text, tables_markdown)
    README_PATH.write_text(updated, encoding="utf-8")
    print("README.md updated with generated project tables.")


if __name__ == "__main__":
    main()
