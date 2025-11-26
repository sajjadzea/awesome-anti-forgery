<!--lint disable awesome-github-->
# لیست پروژه‌های اوپن‌سورس ضدجعل و ضدفرا‌د (Awesome Anti-Forgery & Anti-Fraud) 🔍 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

An opinionated, Farsi-first awesome list for anti-fraud/anti-forgery, document verification, identity, supply-chain provenance, media forensics, and crypto integrity tooling.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/sajjadzea/awesome-anti-forgery/blob/main/CONTRIBUTING.md)

[English version](README.en.md)

<div dir="rtl">

## این ریپو به چه درد می‌خورد؟
- فهرست سریع ابزارها و فریم‌ورک‌هایی که اصالت اسناد، هویت، زنجیره تأمین و رسانه را تضمین می‌کنند.
- کمک به تیم‌های محصول برای انتخاب استک MVP در برابر جعل، تقلب و دیپ‌فیک.
- الهام برای محققان امنیت، فورنزیک و هوش مصنوعی در موج پنجم تکنولوژی.
- رفرنس برای سیاست‌گذاری امنیتی و انطباق (compliance) در حوزه اصالت‌سنجی.
- نمونه‌های واقعی برای طراحی PoC یا پیاده‌سازی در مقیاس تولید.

## چطور از این ریپو استفاده کنم؟
1. دسته مرتبط با مسئله را در بخش «دسته‌بندی‌ها» پیدا کنید.
2. جدول پروژه‌ها را بر اساس توضیح کوتاه و تکنولوژی مرور کنید و روی لینک GitHub کلیک کنید.
3. برای تست سریع، ریپو را کلون کنید و از دستورهای README همان پروژه استفاده کنید.
4. اگر پروژه‌ای یافتید که نبود، با قالب JSON در `projects.json` اضافه کنید و `scripts/generate_readme.py` را اجرا کنید.
5. برای مرور دسته‌های دیگر یا مقایسه، از جدول‌های خودکار زیر استفاده کنید.

## چرا ضدجعل در موج پنج تکنولوژی مهم است؟
در عصر LLMها، مدل‌های مولد و اتوماسیون، هزینه جعل و تقلب نزدیک به صفر شده است. دیپ‌فیک‌ها، مهندسی اجتماعی خودکار و زنجیره تأمین نرم‌افزار بدون امضای دیجیتال، اعتماد را می‌شکنند. ضدجعل دیگر یک قابلیت فرعی نیست؛ بخشی از معماری کلان اعتماد در محصولات دیجیتال است. این ریپو به تیم‌ها کمک می‌کند سریعاً استک مناسب برای MVP و محصول نهایی را بیابند.

### سناریوهای نمونه
- سامانه صدور و اعتبارسنجی مدارک آموزشی همراه با تشخیص دیپ‌فیک مصاحبه ویدیویی.
- رهگیری اصالت کالا و زنجیره تأمین دارو یا قطعات صنعتی با گراف دانش غیرمتمرکز.
- حفاظت از زنجیره تأمین نرم‌افزار (امضای آرتیفکت، SBOM و اثبات منشاء در CI/CD).

## دسته‌بندی‌ها
<!--lint disable awesome-list-item -->
- `certificates`: اسناد، گواهی‌ها، OpenBadges، Blockcerts و هر چیزی که اصالت مدارک را تضمین کند.
- `identity`: IAM، SSO، OAuth2/OIDC، MFA، DID و Verifiable Credentials.
- `supply_chain`: زنجیره تأمین فیزیکی/نرم‌افزار، Provenance، SBOM و DKG.
- `media_forensics`: تشخیص دیپ‌فیک، فورنزیک و ضد دستکاری رسانه.
- `library`: کتابخانه‌های رمزنگاری و امنیتی مرتبط با امضا و اصالت.
<!--lint enable awesome-list-item -->

<!--lint disable table-cell-padding -->
@-- AUTO-GENERATED: PROJECT TABLES START --

## ۱) پروژه‌های ضدجعل اسناد و گواهی‌ها
راهکارهای اعتبارسنجی اسناد، گواهی‌ها و مدارک آموزشی/حرفه‌ای.

<div dir="rtl">

| نام پروژه                                        | توضیح کوتاه                                                                                         | تکنولوژی                         | لینک                                                                                   |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------|
| Automated Document Verification                  | پلتفرم وب برای تأیید اسناد رسمی با بلاک‌چین و رابط کاربری مدرن.                                     | React, Node, Blockchain          | [GitHub](https://github.com/Karan-07E/Automated-Document-Verification)                 |
| BlockChain-Based Document Verification with IPFS | ذخیره هش سند روی بلاک‌چین و سند در IPFS برای جلوگیری از دستکاری.                                    | Blockchain, IPFS                 | [GitHub](https://github.com/DevAloshe/BlockChain-Based-Document-Verfication-With-IPFS) |
| Blockcerts (cert-issuer)                         | استاندارد Blockcerts و ابزار صدور گواهی روی بلاک‌چین برای امضا و راستی‌آزمایی.                      | Blockchain, Credentials, JSON-LD | [GitHub](https://github.com/blockchain-certificates/cert-issuer)                       |
| EtherDocs                                        | مدیریت و تأیید اسناد دانشگاهی با بلاک‌چین، IPFS و توابع هش.                                         | Blockchain, IPFS, Hashing        | [GitHub](https://github.com/DevelopersLeague/EtherDocs)                                |
| Online Document Verification using Blockchain    | سامانه وب برای تأیید و احراز اصالت اسناد با استفاده از بلاک‌چین.                                    | Ethereum, web                    | [GitHub](https://github.com/SomSingh23/Online-document-verification-using-Blockchain)  |
| OpenAttestation (OpenCerts)                      | استاندارد OpenAttestation که زیرساخت OpenCerts سنگاپور برای صدور و اعتبارسنجی گواهی‌های آموزشی است. | Blockchain, Merkle, Ethereum     | [GitHub](https://github.com/Open-Attestation/open-attestation)                         |

</div>

## ۲) هویت دیجیتال و Authentication
IAM، احراز هویت چندعاملی، DID و صدور توکن برای جلوگیری از جعل هویت.

<div dir="rtl">

| نام پروژه                                 | توضیح کوتاه                                                                | تکنولوژی                     | لینک                                                                                                              |
|-------------------------------------------|----------------------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Authelia                                  | پورتال SSO و MFA به‌صورت reverse-proxy برای حفاظت برنامه‌های وب.           | Go, SSO, MFA                 | [GitHub](https://github.com/authelia/authelia)                                                                    |
| Blockchain-based Identity Verification    | سامانه احراز هویت غیرمتمرکز روی بلاک‌چین اتریوم با Solidity.               | Solidity, Ethereum           | [GitHub](https://github.com/Kayleexx/Blockchain-based-identity-verification)                                      |
| Decentralized Identity Verification (DID) | پیاده‌سازی سیستم DID برای مدیریت هویت غیرمتمرکز روی اتریوم.                | Solidity, Ethereum, did      | [GitHub](https://github.com/codewithsheikh/Decentralized-Identity-Verification-System-DID-on-Ethereum-Blockchain) |
| Identity.com                              | مجموعه سرویس‌های احراز هویت غیرمتمرکز و KYC روی بلاک‌چین.                  | Blockchain, Identity         | [GitHub](https://github.com/identity-com)                                                                         |
| Keycloak                                  | مدیریت هویت و دسترسی (SSO، احراز چندعاملی، مدیریت کاربر) برای وب‌اپ و API. | Java, OAuth2, OpenID Connect | [GitHub](https://github.com/keycloak/keycloak)                                                                    |
| Ory Hydra                                 | سرور OAuth2/OIDC متن‌باز برای صدور توکن و جلوگیری از جعل هویت.             | Go, OAuth2, OpenID Connect   | [GitHub](https://github.com/ory/hydra)                                                                            |

</div>

## ۳) زنجیره تأمین و ردیابی اصالت کالا
ردیابی منشأ در زنجیره تأمین نرم‌افزار و کالا برای جلوگیری از تقلب.

<div dir="rtl">

| نام پروژه                                     | توضیح کوتاه                                                                       | تکنولوژی                  | لینک                                                                                      |
|-----------------------------------------------|-----------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|
| Hyperledger Food Supply Chain                 | راهکار زنجیره تأمین مواد غذایی روی Hyperledger Fabric برای ردیابی منشأ محصول.     | Hyperledger Fabric        | [GitHub](https://github.com/AleRapchan/hyperledger-supply-chain)                          |
| Hyperledger Grid                              | پلتفرم ماژولار برای مدیریت زنجیره تأمین و اصالت دارایی‌ها روی بلاک‌چین.           | Hyperledger, Rust         | [GitHub](https://github.com/hyperledger/grid)                                             |
| OriginTrail DKG Client                        | کتابخانه برای تعامل با Decentralized Knowledge Graph و مدیریت دارایی‌های دانشی.   | JavaScript, DKG           | [GitHub](https://github.com/OriginTrail/dkg-client)                                       |
| OriginTrail Node (OT Node)                    | نود شبکه OriginTrail برای ساخت گراف دانش غیرمتمرکز و داده‌های قابل‌اعتماد.        | Node.js, Web3, DKG        | [GitHub](https://github.com/OriginTrail/ot-node)                                          |
| Pharma Supply Chain (Fabric)                  | پیاده‌سازی زنجیره تأمین دارو با Hyperledger Fabric برای ردیابی و جلوگیری از تقلب. | Hyperledger Fabric        | [GitHub](https://github.com/spike-spiegel-21/blockchain-supply-chain)                     |
| Supply Chain using Hyperledger Fabric & React | نمونه سیستم زنجیره تأمین با تمرکز بر ردیابی و احراز اصالت و رابط React.           | Hyperledger Fabric, React | [GitHub](https://github.com/kuldeep23907/Supply-Chain-using-Hyperledger-Fabric-and-React) |

</div>

## ۴) تشخیص رسانه جعلی (Deepfake & Forensics)
ابزارها و دیتاست‌های کشف دیپ‌فیک و دستکاری رسانه.

<div dir="rtl">

| نام پروژه                              | توضیح کوتاه                                                                | تکنولوژی                   | لینک                                                                               |
|----------------------------------------|----------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------|
| Awesome Deepfakes Detection            | فهرست مرجع مقالات و ابزارهای تشخیص دیپ‌فیک و فورنزیک رسانه.                | Survey, Awesome List       | [GitHub](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection)               |
| DeepSafe                               | پلتفرم وب Streamlit برای تشخیص دیپ‌فیک روی تصویر و ویدئو.                  | Python, Streamlit, Docker  | [GitHub](https://github.com/siddharthksah/DeepSafe)                                |
| Deepfake Detection using Deep Learning | تشخیص دیپ‌فیک ویدئو با ترکیب ResNext و LSTM (استخراج ویژگی + توالی زمانی). | PyTorch, CNN, LSTM         | [GitHub](https://github.com/abhijithjadhav/Deepfake_detection_using_deep_learning) |
| DeepfakeDetector                       | سامانه تشخیص دیپ‌فیک با EfficientNet-B0 و رابط وب کاربرپسند.               | PyTorch, EfficientNet, web | [GitHub](https://github.com/TRahulsingh/DeepfakeDetector)                          |
| FaceForensics++                        | دیتاست و کد تشخیص چهره دستکاری‌شده برای سنجش سامانه‌های ضد دیپ‌فیک.        | Dataset, Forensics         | [GitHub](https://github.com/ondyari/FaceForensics)                                 |

</div>

## ۵) کتابخانه‌ها و ابزارهای امنیتی
کتابخانه‌های رمزنگاری و امنیتی برای امضا، هش و حفظ اصالت داده.

<div dir="rtl">

| نام پروژه | توضیح کوتاه                                                                      | تکنولوژی             | لینک                                            |
|-----------|----------------------------------------------------------------------------------|----------------------|-------------------------------------------------|
| OpenSSL   | تولکیت کامل SSL/TLS و رمزنگاری برای ارتباطات امن.                                | c, TLS, SSL          | [GitHub](https://github.com/openssl/openssl)    |
| Tink      | کتابخانه چندزبانه گوگل برای رمزنگاری متقارن/نامتقارن و امضای دیجیتال با API امن. | Go, Java, Python     | [GitHub](https://github.com/google/tink)        |
| libsodium | کتابخانه مدرن و ساده برای رمزنگاری، امضا، هش و مدیریت کلید.                      | c, crypto, Signature | [GitHub](https://github.com/jedisct1/libsodium) |

</div>

@-- AUTO-GENERATED: PROJECT TABLES END --
<!--lint enable table-cell-padding -->

## راهنمای مشارکت (Contribution Guide)
- پیش از PR، `python -m json.tool projects.json` و سپس `python scripts/validate_projects.py` و `python scripts/generate_readme.py` را اجرا کنید.
- فیلدهای الزامی و مثال‌ها در [docs/SCHEMA.md](docs/SCHEMA.md) آمده است. توضیح کوتاه فارسی و بی‌طرف بنویسید.
- پروژه‌هایی با محتوای غیراخلاقی، دیپ‌فیک غیرمجاز یا ابزارهای misinformation پذیرفته نمی‌شوند. جزئیات بیشتر در [CONTRIBUTING.md](CONTRIBUTING.md).

## ریپوهای مرتبط (Related Awesome Lists)
- [Awesome Security](https://github.com/sbilly/awesome-security) - مرجع کلی امنیت (English).
- [Awesome Software Supply Chain Security](https://github.com/cccs-jc/awesome-software-supply-chain-security) - امنیت زنجیره تأمین نرم‌افزار.
- [Awesome Cryptography](https://github.com/sobolevn/awesome-cryptography) - فهرست ابزارها و منابع رمزنگاری (Awesome Cryptography).

## لایسنس
این فهرست تحت مجوز MIT منتشر می‌شود؛ فایل [LICENSE](LICENSE) را ببینید. برای صفحه ریپوی GitHub توضیح کوتاه انگلیسی/فارسی و تاپیک‌های `security`, `anti-fraud`, `anti-forgery`, `deepfake-detection`, `supply-chain-security`, `identity`, `awesome-list` را در تنظیمات مخزن اضافه کنید.

</div>
