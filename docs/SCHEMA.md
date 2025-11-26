# طرح داده `projects.json`

این سند ساختار و قوانین داده‌های فهرست پروژه‌ها را شرح می‌دهد تا اسکریپت اعتبارسنجی و CI بدون خطا اجرا شوند.

## فیلدهای اجباری برای هر پروژه
| فیلد | نوع | توضیح |
| --- | --- | --- |
| `name` | string | نام پروژه (منحصر‌به‌فرد و غیرخالی). |
| `github` | string | مسیر `owner/repo` در GitHub یا در صورت نبود، یک شناسه غیرخالی. |
| `url` | string | لینک HTTP/HTTPS معتبر به صفحه اصلی پروژه. |
| `category` | enum | یکی از مقادیر در [دسته‌بندی‌ها](#دسته‌بندیها). |
| `description` | string | توضیح کوتاه فارسی درباره نقش ضدجعل/ضدفرا‌د. |
| `tags` | array[string] | برچسب‌های کلیدی؛ آرایه اجباری است. |
| `license` | string | SPDX ID مجوز پروژه (مثلاً `MIT`، `Apache-2.0`) یا در صورت شک `UNKNOWN`. |

> فیلد `tech` اختیاری است ولی توصیه می‌شود (آرایه‌ای از فناوری‌ها/زبان‌ها).

## دسته‌بندی‌ها
مقدار `category` باید یکی از این گزینه‌ها باشد:

- `certificates`
- `identity`
- `supply_chain`
- `media_forensics`
- `library`

## مثال حداقلی
```json
{
  "name": "Blockcerts",
  "github": "blockchain-certificates/blockcerts",
  "url": "https://github.com/blockchain-certificates/blockcerts",
  "category": "certificates",
  "description": "استاندارد و ابزار صدور و اعتبارسنجی گواهی‌های مبتنی بر بلاک‌چین.",
  "tags": ["certificate", "verification", "education"],
  "license": "UNKNOWN",
  "tech": ["blockchain", "json-ld"]
}
```

## سیاست نام‌گذاری و تکرار
- `name` باید یکتا باشد؛ از نام‌های تکراری یا مترادف پرهیز کنید.
- `github` در صورت وجود باید دقیقاً `owner/repo` باشد تا لینک و لایسنس به‌راحتی بررسی شود.

## توصیه درباره `license`
- اگر SPDX ID را نمی‌دانید، موقتاً `UNKNOWN` بنویسید و Issue باز کنید.
- از مقادیر غیررسمی مثل "free" یا "open" استفاده نکنید.

## اعتبارسنجی خودکار
- CI با `scripts/validate_projects.py` ساختار و لینک‌ها را بررسی می‌کند.
- اجرای محلی:
  ```bash
  python scripts/validate_projects.py --check-urls --timeout 5.0
  ```
- خطاهای رایج شامل نبود فیلد `github`، تکرار `name` یا `category` نامعتبر است.
