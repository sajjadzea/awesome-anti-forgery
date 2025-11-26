<!--lint disable awesome-github-->
# لیست پروژه‌های اوپن‌سورس ضدجعل و ضدفرا‌د (Awesome Anti-Forgery & Anti-Fraud) 🔍 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/sajjadzea/awesome-anti-forgery/blob/main/CONTRIBUTING.md)

[English version](README.en.md)

&#x202b; راهنمای جامع پروژه‌های اوپن‌سورس برای جلوگیری از جعل سند، جعل هویت، تقلب در زنجیره تأمین و تشخیص رسانه‌ی دستکاری‌شده.

## Contents
- [Certificates & Documents](#certificates--documents)
- [Identity & Authentication](#identity--authentication)
- [Supply Chain & Anti-Counterfeiting](#supply-chain--anti-counterfeiting)
- [Media & Deepfake Detection](#media--deepfake-detection)
- [Crypto Libraries & Tools](#crypto-libraries--tools)
- [Use Cases](#use-cases)
- [Usage](#usage)

---

## Certificates & Documents
اسناد و گواهی‌ها: پروژه‌هایی برای صدور و اعتبارسنجی مدارک دیجیتال.
- [Blockcerts (cert-issuer)](https://github.com/blockchain-certificates/cert-issuer) - استاندارد Blockcerts و ابزار صدور گواهی روی بلاک‌چین برای امضا و راستی‌آزمایی.
- [OpenAttestation (OpenCerts)](https://github.com/Open-Attestation/open-attestation) - استاندارد OpenAttestation که مبنای OpenCerts برای صدور و اعتبارسنجی گواهی‌های آموزشی است.
- [Automated Document Verification](https://github.com/Karan-07E/Automated-Document-Verification) - پلتفرم وب برای تأیید اسناد رسمی با بلاک‌چین و رابط کاربری مدرن.
- [BlockChain-Based Document Verification with IPFS](https://github.com/DevAloshe/BlockChain-Based-Document-Verfication-With-IPFS) - ذخیره هش سند روی بلاک‌چین و خود سند روی IPFS برای جلوگیری از دستکاری.
- [EtherDocs](https://github.com/DevelopersLeague/EtherDocs) - مدیریت و تأیید اسناد دانشگاهی با بلاک‌چین، IPFS و توابع هش.
- [Online Document Verification using Blockchain](https://github.com/SomSingh23/Online-document-verification-using-Blockchain) - سامانه وب برای تأیید و احراز اصالت اسناد با استفاده از بلاک‌چین.

---

## Identity & Authentication
هویت دیجیتال و احراز هویت: سامانه‌های SSO، IAM و DID.
- [Authelia](https://github.com/authelia/authelia) - پورتال SSO و MFA به‌صورت reverse-proxy برای حفاظت از برنامه‌های وب.
- [Keycloak](https://github.com/keycloak/keycloak) - مدیریت هویت و دسترسی (SSO، احراز چندعاملی، مدیریت کاربر) برای وب‌اپ و API.
- [Ory Hydra](https://github.com/ory/hydra) - سرور OAuth2/OIDC متن‌باز برای صدور توکن و جلوگیری از جعل هویت.
- [Blockchain-based Identity Verification](https://github.com/Kayleexx/Blockchain-based-identity-verification) - سامانه احراز هویت غیرمتمرکز روی بلاک‌چین اتریوم با Solidity.
- [Decentralized Identity Verification (DID)](https://github.com/codewithsheikh/Decentralized-Identity-Verification-System-DID-on-Ethereum-Blockchain) - پیاده‌سازی سیستم DID برای مدیریت هویت غیرمتمرکز روی اتریوم.
- [Identity.com](https://github.com/identity-com) - مجموعه سرویس‌های احراز هویت غیرمتمرکز و KYC روی بلاک‌چین.

---

## Supply Chain & Anti-Counterfeiting
زنجیره تأمین و اصالت کالا: ردیابی منشاء و جلوگیری از تقلب.
- [OriginTrail Node (OT Node)](https://github.com/OriginTrail/ot-node) - نود شبکه OriginTrail برای ساخت «گراف دانش غیرمتمرکز» و داده‌های قابل‌اعتماد.
- [OriginTrail DKG Client](https://github.com/OriginTrail/dkg-client) - کتابخانه برای تعامل با Decentralized Knowledge Graph و مدیریت دارایی‌های دانشی.
- [Hyperledger Food Supply Chain](https://github.com/AleRapchan/hyperledger-supply-chain) - راهکار زنجیره تأمین مواد غذایی روی Hyperledger Fabric برای ردیابی منشأ محصول.
- [Pharma Supply Chain (Fabric)](https://github.com/spike-spiegel-21/blockchain-supply-chain) - پیاده‌سازی زنجیره تأمین دارو با Hyperledger Fabric برای ردیابی و جلوگیری از تقلب.
- [Supply Chain using Hyperledger Fabric & React](https://github.com/kuldeep23907/Supply-Chain-using-Hyperledger-Fabric-and-React) - سیستم زنجیره تأمین با تمرکز بر ردیابی و احراز اصالت و رابط React.
- [Hyperledger Grid](https://github.com/hyperledger/grid) - پلتفرم ماژولار برای مدیریت زنجیره تأمین و اصالت دارایی‌ها روی Hyperledger Sawtooth.

---

## Media & Deepfake Detection
رسانه و دیپ‌فیک: ابزارها و مدل‌های تشخیص دستکاری.
- [Deepfake Detection using Deep Learning](https://github.com/abhijithjadhav/Deepfake_detection_using_deep_learning) - تشخیص دیپ‌فیک ویدئو با ترکیب ResNext و LSTM (ویژگی + توالی زمانی).
- [DeepfakeDetector](https://github.com/TRahulsingh/DeepfakeDetector) - سامانه تشخیص دیپ‌فیک با EfficientNet-B0 و رابط وب کاربرپسند.
- [DeepSafe](https://github.com/siddharthksah/DeepSafe) - پلتفرم وب Streamlit برای تشخیص دیپ‌فیک روی تصویر و ویدئو.
- [Awesome Deepfakes Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) - فهرست مرجع مقالات و ابزارهای تشخیص دیپ‌فیک (منبع پژوهشی).
- [FaceForensics++](https://github.com/ondyari/FaceForensics) - دیتاست و کد تشخیص چهره دستکاری‌شده برای سنجش سامانه‌های ضد دیپ‌فیک.

---

## Crypto Libraries & Tools
ابزارها و کتابخانه‌های رمزنگاری پایه.
- [libsodium](https://github.com/jedisct1/libsodium) - کتابخانه‌ی مدرن و ساده برای رمزنگاری، امضا، هش و مدیریت کلید.
- [OpenSSL](https://github.com/openssl/openssl) - تولکیت کامل SSL/TLS و رمزنگاری، زیرساخت اکثر ارتباطات امن وب (HTTPS).
- [Tink](https://github.com/google/tink) - کتابخانه چندزبانه گوگل برای رمزنگاری متقارن/نامتقارن و امضای دیجیتال با API امن.

---

## Use Cases
### صدور گواهی دانشگاهی مقاوم در برابر جعل
Blockcerts (cert-issuer) یا OpenAttestation/OpenCerts را برای صدور گواهی استفاده کنید و EtherDocs را برای مدیریت مدارک به کار بگیرید.

### احراز هویت امن در وب و API
Keycloak یا Authelia را برای SSO و MFA به‌کار ببرید؛ برای شناسه‌های غیرمتمرکز، پروژه‌های DID مانند Decentralized Identity Verification مناسب‌اند.

### رهگیری اصالت دارو و کالا
نمونه‌های Hyperledger Fabric مانند Hyperledger Food Supply Chain، به‌همراه OriginTrail Node و Hyperledger Grid برای ردیابی و اثبات منشاء استفاده کنید.

### تشخیص ویدئوهای دستکاری‌شده
DeepfakeDetector یا DeepSafe را برای پیاده‌سازی سرویس تشخیص، و FaceForensics++ را برای داده آموزشی به‌کار گیرید.

### لایه رمزنگاری استاندارد
Tink، OpenSSL یا libsodium را به‌عنوان هسته امضا، هش و TLS در سرویس‌های ضدجعل به کار ببرید.

---

## Usage
- از بخش مرتبط با مسئله‌ی خود شروع کنید و پروژه‌های متناظر را بررسی کنید.
- لینک‌ها مستقیم به ریپوهای اوپن‌سورس هستند؛ قبل از استفاده، README و لایسنس هر ریپو را بخوانید.
- اگر URLی در دسترس نبود، در Issueها گزارش دهید تا به‌روز شود.

---

## Contributing
- برای افزودن پروژه جدید، نام و لینک را به بخش مرتبط اضافه کنید و یک ورودی کامل در `projects.json` (شامل `github`، `license` و `tags`) بسازید.
- قوانین دقیق فرمت و دسته‌بندی در [CONTRIBUTING.md](CONTRIBUTING.md) و [docs/SCHEMA.md](docs/SCHEMA.md) آمده است.
- برای گزارش لینک خراب یا داده نادرست، از قالب Issue آماده در مخزن استفاده کنید.

