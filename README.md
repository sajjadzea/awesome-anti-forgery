# لیست پروژه‌های اوپن‌سورس ضدجعل و ضدفرا‌د (Anti-Forgery & Anti-Fraud)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

🔗 مناسب برای توسعه سیستم‌های اصالت‌سنجی داده، سند، کالا، هویت و تشخیص جعل رسانه‌ای

- این ریپو مجموعه‌ای از پروژه‌های اوپن‌سورس مربوط به جلوگیری از جعل، احراز اصالت و کشف تقلب است.
- پروژه‌ها در ۵ دسته طبقه‌بندی شده‌اند تا انتخاب و ارزیابی سریع‌تر شود.
- تمام لینک‌ها واقعی و بررسی‌شده هستند تا مستقیماً در PoC یا محصول استفاده شوند.

## 🔷 فهرست بخش‌ها
| بخش | لینک |
|---|---|
| اسناد و گواهی‌ها | [📄 Certificates & Documents](#certificates) |
| هویت و احراز هویت | [🪪 Identity Authentication](#identity) |
| زنجیره تأمین و کالا | [📦 Supply Chain Verification](#supply-chain) |
| تشخیص رسانه و دیپ‌فیک | [🎭 Media Deepfake Detection](#media-forensics) |
| کتابخانه‌ها و ابزارها | [🧰 Libraries & Crypto](#libraries) |

---

<a id="certificates"></a>
## 📄 1) پروژه‌های ضدجعل اسناد و گواهی‌ها

| نام پروژه | توضیح کوتاه | تکنولوژی | لینک |
|---|---|---|---|
| Blockcerts | استاندارد صدور و تأیید گواهی روی بلاک‌چین با ابزار انتشار و اعتبارسنجی | Blockchain + JSON-LD | https://github.com/blockchain-certificates/cert-issuer |
| Credential Handler Polyfill | پیاده‌سازی Polyfill برای کیف‌پول Verifiable Credential جهت صدور و بررسی اعتبار | Verifiable Credentials + Web | https://github.com/digitalbazaar/credential-handler-polyfill |
| Open Badges Validator Core | اعتبارسنجی ساختار و اصالت IMS Open Badges برای گواهی‌های آموزشی | JSON Validation + Open Badges | https://github.com/IMSGlobal/openbadges-validator-core |

---

<a id="identity"></a>
## 🪪 2) هویت دیجیتال و Authentication

| نام پروژه | کاربرد | تکنولوژی | لینک |
|---|---|---|---|
| Authelia | درگاه SSO با پشتیبانی 2FA و سیاست‌های دسترسی معکوس برای اپلیکیشن‌های وب | OAuth2 / OIDC + Reverse Proxy | https://github.com/authelia/authelia |
| Keycloak | مدیریت هویت و دسترسی سازمانی با SSO، فدراسیون و سیاست‌گذاری دقیق | OAuth2 / OIDC + SAML | https://github.com/keycloak/keycloak |
| privacyIDEA | سامانه MFA و موتور سیاست برای توکن‌های متنوع و جریان‌های پیچیده احراز هویت | MFA + Policy Engine | https://github.com/privacyidea/privacyidea |

---

<a id="supply-chain"></a>
## 📦 3) زنجیره تأمین و ردیابی اصالت کالا

| نام | توضیح | فناوری | لینک |
|---|---|---|---|
| Hyperledger Grid | چارچوب مدل‌داده و قرارداد هوشمند برای شفافیت و ضدتقلب زنجیره تأمین | Hyperledger + Smart Contracts | https://github.com/hyperledger/grid |
| in-toto | امنیت زنجیره عرضه نرم‌افزار با امضای مراحل و تأیید طرح اجرایی | Metadata Signing + Supply Chain Layout | https://github.com/in-toto/in-toto |
| OriginTrail | گراف دانش غیرمتمرکز برای رهگیری کالا و اثبات اصالت در Supply Chain | DKG + Blockchain | https://github.com/OriginTrail/ot-node |
| Sigstore Cosign | امضای کانتینر و آرتیفکت برای اثبات منشاء و تمامیت بسته‌های نرم‌افزاری | Sigstore + Container Signing | https://github.com/sigstore/cosign |

---

<a id="media-forensics"></a>
## 🎭 4) تشخیص رسانه جعلی (Deepfake & Forensics)

| نام | کاربرد | مدل پردازش | لینک |
|---|---|---|---|
| DFDC Deepfake Challenge | کد آموزش/استنتاج روی دیتاست Facebook DFDC برای کشف ویدئوهای جعل‌شده | CNN + Video ML | https://github.com/selimsef/dfdc_deepfake_challenge |
| FaceForensics | دیتاست و کد بنچمارک برای تشخیص ویدئو و تصویر دستکاری‌شده صورت | CNN + Forensic Analysis | https://github.com/ondyari/FaceForensics |

---

<a id="libraries"></a>
## 🧰 5) کتابخانه‌ها و ابزار امنیتی

| نام ابزار | کاربرد | زبان/پشته | لینک |
|---|---|---|---|
| Google Tink | SDK چندزبانه رمزنگاری با تنظیمات امن برای امضا و رمزنگاری | C++ / Java / Go / Python | https://github.com/google/tink |
| libsodium | کتابخانه رمزنگاری سطح سیستم برای امضا، رمزنگاری و هش | C | https://github.com/jedisct1/libsodium |
| OpenSSL | مجموعه ابزار TLS/SSL و رمزنگاری عمومی برای شبکه و فایل | C | https://github.com/openssl/openssl |
| Python TUF | مرجع The Update Framework برای به‌روزرسانی امن بسته‌های نرم‌افزاری | Python | https://github.com/theupdateframework/python-tuf |
| YubiKey libfido2 | پیاده‌سازی FIDO2/WebAuthn برای کلیدهای امنیتی سخت‌افزاری | C | https://github.com/Yubico/libfido2 |

---

## نحوه استفاده
- بر اساس دسته‌بندی، پروژه متناسب با نیاز (اسناد، هویت، زنجیره تأمین، رسانه یا کتابخانه) را انتخاب کنید.
- مخازن معرفی‌شده را برای POC یا ادغام مستقیم کلون کرده و به کمک توضیحات فنی سریعاً راه‌اندازی کنید.
- برای هر افزوده جدید، هر دو فایل `README.md` و `projects.json` را همزمان به‌روز کنید تا هم‌راستا بمانند.

## لایسنس
این فهرست تحت مجوز [MIT](LICENSE) منتشر شده است.
