#!/usr/bin/env python3
"""اعتبارسنجی فایل projects.json و بررسی اختیاری لینک‌ها."""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
except Exception:  # pragma: no cover - dependency اختیاری است
    requests = None

ALLOWED_CATEGORIES = {
    "certificates",  # اسناد و گواهی‌ها
    "identity",  # هویت دیجیتال و احراز هویت
    "supply_chain",  # زنجیره تأمین نرم‌افزار/سخت‌افزار
    "media_forensics",  # تشخیص دستکاری و دیپ‌فیک
    "library",  # کتابخانه‌های رمزنگاری و امنیتی
}

REQUIRED_FIELDS = ["name", "github", "url", "category", "description", "license"]


def load_projects(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _validate_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_structure(projects):
    errors = []

    if not isinstance(projects, list):
        raise ValueError("projects.json باید یک لیست از پروژه‌ها باشد.")

    names = set()
    github_ids = set()

    for idx, entry in enumerate(projects, start=1):
        if not isinstance(entry, dict):
            errors.append(f"ردیف {idx}: هر پروژه باید یک شیء JSON باشد.")
            continue

        for field in REQUIRED_FIELDS:
            if field not in entry:
                errors.append(
                    f"ردیف {idx} ({entry.get('name', 'بدون‌نام')}): فیلد الزامی '{field}' وجود ندارد."
                )

        name = (entry.get("name") or "").strip()
        if not name:
            errors.append(f"ردیف {idx}: مقدار 'name' خالی است یا فقط فاصله دارد.")
        elif name in names:
            errors.append(f"ردیف {idx}: نام پروژه تکراری است: {name}.")
        names.add(name)

        github_path = (entry.get("github") or "").strip()
        if not github_path:
            errors.append(f"ردیف {idx} ({name}): مقدار 'github' خالی است.")
        elif github_path in github_ids:
            errors.append(f"ردیف {idx} ({name}): مقدار 'github' تکراری است: {github_path}.")
        github_ids.add(github_path)

        category = entry.get("category")
        if category not in ALLOWED_CATEGORIES:
            allowed = ", ".join(sorted(ALLOWED_CATEGORIES))
            errors.append(
                f"ردیف {idx} ({name}): مقدار 'category' نامعتبر است ({category}). مقادیر مجاز: {allowed}."
            )

        url = entry.get("url", "")
        if not _validate_url(url):
            errors.append(f"ردیف {idx} ({name}): URL نامعتبر است ({url}).")

        tags = entry.get("tags")
        if tags is not None and not isinstance(tags, list):
            errors.append(f"ردیف {idx} ({name}): فیلد 'tags' باید آرایه باشد.")

        tech = entry.get("tech")
        if tech is not None and not isinstance(tech, list):
            errors.append(f"ردیف {idx} ({name}): فیلد اختیاری 'tech' باید آرایه باشد.")

    if errors:
        raise ValueError("\n".join(errors))


def check_urls(projects, timeout):
    if requests is None:
        print("کتابخانه requests نصب نیست؛ بررسی لینک‌ها رد شد.", file=sys.stderr)
        return

    for entry in projects:
        for key in ("url", "github"):
            target = entry.get(key)
            if not target:
                continue
            if key == "github" and not target.startswith("http"):
                target = f"https://github.com/{target}"
            try:
                response = requests.head(target, allow_redirects=True, timeout=timeout)
                if response.status_code >= 400:
                    raise ValueError(
                        f"وضعیت HTTP {response.status_code} برای {key} پروژه {entry.get('name')} ({target})."
                    )
            except Exception as exc:  # pragma: no cover - وابسته به شبکه
                raise ValueError(
                    f"بررسی لینک {key} برای {entry.get('name')} ناموفق بود: {exc}"
                )


def main():
    parser = argparse.ArgumentParser(description="Validate projects.json")
    parser.add_argument("--check-urls", action="store_true", help="Perform HTTP HEAD requests for each project URL and GitHub path")
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
        print(f"اعتبارسنجی ناموفق بود:\n{exc}", file=sys.stderr)
        return 1

    print("projects.json بدون خطا اعتبارسنجی شد.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
