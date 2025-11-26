#!/usr/bin/env python3
"""تولید جدول‌های README از روی projects.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
PROJECTS_PATH = ROOT / "projects.json"

START_MARKER = "@-- AUTO-GENERATED: PROJECT TABLES START --"
END_MARKER = "@-- AUTO-GENERATED: PROJECT TABLES END --"

CATEGORY_ORDER = [
    "certificates",
    "identity",
    "supply_chain",
    "media_forensics",
    "library",
]

CATEGORY_HEADERS = {
    "certificates": "## ۱) پروژه‌های ضدجعل اسناد و گواهی‌ها",
    "identity": "## ۲) هویت دیجیتال و Authentication",
    "supply_chain": "## ۳) زنجیره تأمین و ردیابی اصالت کالا",
    "media_forensics": "## ۴) تشخیص رسانه جعلی (Deepfake & Forensics)",
    "library": "## ۵) کتابخانه‌ها و ابزارهای امنیتی",
}

CATEGORY_DESCRIPTIONS = {
    "certificates": "راهکارهای اعتبارسنجی اسناد، گواهی‌ها و مدارک آموزشی/حرفه‌ای.",
    "identity": "IAM، احراز هویت چندعاملی، DID و صدور توکن برای جلوگیری از جعل هویت.",
    "supply_chain": "ردیابی منشأ در زنجیره تأمین نرم‌افزار و کالا برای جلوگیری از تقلب.",
    "media_forensics": "ابزارها و دیتاست‌های کشف دیپ‌فیک و دستکاری رسانه.",
    "library": "کتابخانه‌های رمزنگاری و امنیتی برای امضا، هش و حفظ اصالت داده.",
}


def load_projects() -> list[dict]:
    data = json.loads(PROJECTS_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("projects.json باید شامل یک لیست باشد.")
    return data


def format_table(rows: list[dict]) -> str:
    tech_overrides = {
        "blockchain": "Blockchain",
        "ethereum": "Ethereum",
        "solidity": "Solidity",
        "docker": "Docker",
        "pytorch": "PyTorch",
        "javascript": "JavaScript",
        "nodejs": "Node.js",
        "web3": "Web3",
        "hyperledger": "Hyperledger",
        "hyperledger-fabric": "Hyperledger Fabric",
        "ipfs": "IPFS",
        "json-ld": "JSON-LD",
        "oauth2": "OAuth2",
        "openid-connect": "OpenID Connect",
        "mfa": "MFA",
        "sso": "SSO",
        "dkg": "DKG",
        "cnn": "CNN",
        "lstm": "LSTM",
        "ssl": "SSL",
        "tls": "TLS",
        "go": "Go",
        "rust": "Rust",
        "java": "Java",
        "python": "Python",
        "react": "React",
        "node": "Node",
        "streamlit": "Streamlit",
        "survey": "Survey",
        "credentials": "Credentials",
        "merkle": "Merkle",
        "identity": "Identity",
        "awesome-list": "Awesome List",
        "hashing": "Hashing",
        "signature": "Signature",
        "forensics": "Forensics",
        "dataset": "Dataset",
        "efficientnet": "EfficientNet",
    }

    def display_tech(values: list[str] | None) -> str:
        if not values:
            return "—"
        formatted = []
        for item in values:
            key = item.strip().lower()
            formatted.append(tech_overrides.get(key, item))
        return ", ".join(formatted)

    headers = ["نام پروژه", "توضیح کوتاه", "تکنولوژی", "لینک"]
    rows_matrix: list[list[str]] = []
    for entry in rows:
        tech = display_tech(entry.get("tech"))
        link = f"[GitHub]({entry['url']})"
        rows_matrix.append([
            entry["name"],
            entry["description"],
            tech,
            link,
        ])

    all_rows = [headers, *rows_matrix]
    col_widths = [max(len(row[idx]) for row in all_rows) for idx in range(len(headers))]

    def render_row(cells: list[str]) -> str:
        padded = [f" {cell.ljust(col_widths[idx])} " for idx, cell in enumerate(cells)]
        return "|" + "|".join(padded) + "|"

    separator = "|" + "|".join(["-" * (w + 2) for w in col_widths]) + "|"
    lines = [render_row(headers), separator]
    for data_row in rows_matrix:
        lines.append(render_row(data_row))

    table = "\n".join(lines)
    return "\n".join([
        '<div dir="rtl">',
        "",
        table,
        "",
        "</div>",
    ])


def render_sections(projects: list[dict]) -> str:
    by_category: dict[str, list[dict]] = {cat: [] for cat in CATEGORY_ORDER}
    for entry in projects:
        cat = entry.get("category")
        if cat in by_category:
            by_category[cat].append(entry)

    sections: list[str] = []
    for cat in CATEGORY_ORDER:
        rows = sorted(by_category.get(cat, []), key=lambda e: e.get("name", ""))
        heading = CATEGORY_HEADERS[cat]
        description = CATEGORY_DESCRIPTIONS.get(cat, "")
        table_block = format_table(rows) if rows else "_هیچ ورودی ثبت نشده است._"
        sections.append("\n".join([heading, description, "", table_block, ""]))

    return "\n".join(sections).rstrip() + "\n"


def replace_between_markers(readme_text: str, new_block: str) -> str:
    if START_MARKER not in readme_text or END_MARKER not in readme_text:
        raise SystemExit("نشان‌گرهای تولید خودکار در README.md یافت نشد.")

    before, _sep, remainder = readme_text.partition(START_MARKER)
    _mid, _sep, after = remainder.partition(END_MARKER)
    return f"{before}{START_MARKER}\n\n{new_block}\n{END_MARKER}{after}"


def main():
    projects = load_projects()
    block = render_sections(projects)
    readme_text = README_PATH.read_text(encoding="utf-8")
    updated = replace_between_markers(readme_text, block)
    README_PATH.write_text(updated, encoding="utf-8")
    print("README.md با موفقیت به‌روزرسانی شد.")


if __name__ == "__main__":
    main()
