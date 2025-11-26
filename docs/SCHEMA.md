# ساختار داده `projects.json`

> JSON schema for the curated list — توضیحات فارسی به‌همراه توضیح کوتاه انگلیسی.

## فیلدها (Fields)
```jsonc
{
  "name": "Blockcerts",                  // نام پروژه - Project name (unique, non-empty)
  "github": "blockchain-certificates/cert-issuer", // GitHub owner/repo یا org
  "url": "https://github.com/blockchain-certificates/cert-issuer", // لینک مرجع https
  "category": "certificates",           // یکی از enum های تعریف‌شده
  "description": "توضیح کوتاه فارسی درباره نقش ضدجعل/ضدفرا‌د.",
  "license": "Apache-2.0",              // SPDX ID یا UNKNOWN
  "tech": ["blockchain", "json-ld"],    // (اختیاری) فناوری‌ها/زبان‌ها
  "tags": ["certificate", "verification"] // (اختیاری) تگ‌های کوتاه، حروف کوچک
}
```

### فیلدهای الزامی / Required
- `name`, `github`, `url`, `category`, `description`, `license`

### فیلدهای پیشنهادی / Recommended
- `tech` (array of strings)
- `tags` (array of lowercase, hyphen-separated keywords)

## دسته‌بندی‌های مجاز (Allowed categories)
- `certificates` — اسناد، گواهی‌ها، OpenBadges، Blockcerts.
- `identity` — IAM, SSO, OAuth2/OIDC, MFA, DID, verifiable credentials.
- `supply_chain` — زنجیره تأمین نرم‌افزار و کالا، provenance، SBOM، DKG.
- `media_forensics` — تشخیص دیپ‌فیک، فورنزیک رسانه، دیتاست و بنچمارک.
- `library` — کتابخانه‌های رمزنگاری/امنیتی برای اصالت و تمامیت داده.

## مثال‌ها (Samples by category)

### certificates
```jsonc
[
  {
    "name": "OpenAttestation", // استاندارد گواهی‌های آموزشی
    "github": "Open-Attestation/open-attestation",
    "url": "https://github.com/Open-Attestation/open-attestation",
    "category": "certificates",
    "description": "استاندارد OpenAttestation برای صدور و اعتبارسنجی گواهی‌ها.",
    "license": "Apache-2.0",
    "tech": ["merkle", "ethereum"],
    "tags": ["certificate", "education"]
  },
  {
    "name": "Automated Document Verification", // نمونه وب‌اپ احراز سند
    "github": "Karan-07E/Automated-Document-Verification",
    "url": "https://github.com/Karan-07E/Automated-Document-Verification",
    "category": "certificates",
    "description": "تأیید اسناد رسمی با بلاک‌چین و رابط کاربری مدرن.",
    "license": "UNKNOWN",
    "tech": ["react", "node"],
    "tags": ["document", "verification"]
  }
]
```

### identity
```jsonc
[
  {
    "name": "Authelia", // SSO + MFA reverse-proxy
    "github": "authelia/authelia",
    "url": "https://github.com/authelia/authelia",
    "category": "identity",
    "description": "پورتال SSO و MFA به‌صورت reverse-proxy.",
    "license": "Apache-2.0",
    "tech": ["go", "sso", "mfa"],
    "tags": ["authentication", "identity"]
  },
  {
    "name": "Ory Hydra", // OAuth2/OIDC server
    "github": "ory/hydra",
    "url": "https://github.com/ory/hydra",
    "category": "identity",
    "description": "سرور OAuth2/OIDC برای صدور توکن و جلوگیری از جعل هویت.",
    "license": "Apache-2.0",
    "tech": ["go", "oauth2"],
    "tags": ["tokens", "authorization"]
  }
]
```

### supply_chain
```jsonc
[
  {
    "name": "OriginTrail Node", // گراف دانش غیرمتمرکز
    "github": "OriginTrail/ot-node",
    "url": "https://github.com/OriginTrail/ot-node",
    "category": "supply_chain",
    "description": "نود DKG برای داده‌های قابل‌اعتماد در زنجیره تأمین.",
    "license": "UNKNOWN",
    "tech": ["nodejs", "web3"],
    "tags": ["provenance", "supply-chain"]
  },
  {
    "name": "Hyperledger Grid", // ماژولار و Sawtooth-based
    "github": "hyperledger/grid",
    "url": "https://github.com/hyperledger/grid",
    "category": "supply_chain",
    "description": "مدیریت دارایی و اصالت روی Hyperledger Sawtooth.",
    "license": "Apache-2.0",
    "tech": ["hyperledger", "rust"],
    "tags": ["traceability", "supply-chain"]
  }
]
```

### media_forensics
```jsonc
[
  {
    "name": "DeepfakeDetector", // EfficientNet-B0
    "github": "TRahulsingh/DeepfakeDetector",
    "url": "https://github.com/TRahulsingh/DeepfakeDetector",
    "category": "media_forensics",
    "description": "تشخیص دیپ‌فیک با رابط وب کاربرپسند.",
    "license": "UNKNOWN",
    "tech": ["pytorch", "web"],
    "tags": ["deepfake", "detection"]
  },
  {
    "name": "FaceForensics++", // دیتاست مرجع
    "github": "ondyari/FaceForensics",
    "url": "https://github.com/ondyari/FaceForensics",
    "category": "media_forensics",
    "description": "دیتاست و کد سنجش سامانه‌های ضد دیپ‌فیک.",
    "license": "UNKNOWN",
    "tech": ["dataset", "forensics"],
    "tags": ["benchmark", "deepfake"]
  }
]
```

### library
```jsonc
[
  {
    "name": "Tink", // Google multi-language crypto
    "github": "google/tink",
    "url": "https://github.com/google/tink",
    "category": "library",
    "description": "رمزنگاری متقارن/نامتقارن و امضا با API امن.",
    "license": "Apache-2.0",
    "tech": ["go", "java", "python"],
    "tags": ["encryption", "signing"]
  },
  {
    "name": "libsodium", // مدرن و ساده
    "github": "jedisct1/libsodium",
    "url": "https://github.com/jedisct1/libsodium",
    "category": "library",
    "description": "کتابخانه مدرن برای رمزنگاری، امضا و هش.",
    "license": "ISC",
    "tech": ["c", "signature"],
    "tags": ["crypto", "integrity"]
  }
]
```

## خط‌مشی داده و کیفیت (Data Quality)
- توضیح پروژه حداکثر ۱–۲ خط و فارسی باشد.
- `tags` بهتر است حروف کوچک و بدون فاصله (hyphen-separated در صورت نیاز) باشند.
- `github` می‌تواند فقط نام سازمان باشد؛ در صورت وجود مخزن، فرمت `owner/repo` ترجیح داده می‌شود.
- قبل از ارسال PR، اسکریپت‌های زیر را اجرا کنید:
  ```bash
  python -m json.tool projects.json
  python scripts/validate_projects.py
  python scripts/generate_readme.py
  ```
