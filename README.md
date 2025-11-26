<!--lint disable awesome-github-->
# لیست پروژه‌های اوپن‌سورس ضدجعل و ضدفرا‌د (Awesome Anti-Forgery & Anti-Fraud) 🔍 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/sajjadzea/awesome-anti-forgery/blob/main/CONTRIBUTING.md)

[English version](README.en.md)

A curated, Persian-first index of open-source anti-forgery and anti-fraud projects covering document integrity, digital identity, supply-chain traceability, media forensics, and foundational crypto tooling.

<div dir="rtl">

## فهرست مطالب
- [کاربردها](#کاربردها)
- [نحوه-استفاده](#نحوه-استفاده)
- [موج-پنج](#موج-پنج)
- [دسته‌بندی‌ها](#دسته‌بندی‌ها)
- [پروژه‌ها-به-تفکیک-دسته](#پروژه‌ها-به-تفکیک-دسته)
- [راهنمای-مشارکت](#راهنمای-مشارکت)
- [related-awesome-lists](#related-awesome-lists)

## کاربردها
- جلوگیری از جعل گواهی دانشگاهی و اسناد رسمی با صدور دیجیتال و راستی‌آزمایی روی بلاک‌چین.
- احراز هویت مطمئن برای وب‌اپ و API با SSO، MFA و DID.
- رهگیری منشأ کالا، دارو و تجهیزات در زنجیره تأمین برای کاهش تقلب.
- تشخیص رسانه دستکاری‌شده و دیپ‌فیک برای حفظ اعتماد مخاطب و مراجع قانونی.
- پیاده‌سازی لایه رمزنگاری استاندارد برای امضا، هش و مدیریت کلید.

## نحوه استفاده
- از دسته‌ای که به مسئله شما نزدیک‌تر است شروع کنید و چند پروژه را مقایسه کنید.
- README و لایسنس هر ریپو را قبل از استفاده دقیق بخوانید و الزامات فنی را بسنجید.
- اگر لینکی از دسترس خارج بود یا دسته‌بندی اشتباه بود، در Issueها گزارش دهید.
- برای اتوماسیون، از اسکریپت `scripts/generate_readme.py` جهت بازتولید جداول استفاده کنید.

## موج پنج
این فهرست موج پنجم ابزارهای ضدجعل را پوشش می‌دهد: ترکیب بلاک‌چین، هویت غیرمتمرکز، زنجیره تأمین قابل‌ردگیری، مدل‌های تشخیص دیپ‌فیک و کتابخانه‌های رمزنگاری که به‌صورت یکپارچه برای کاهش تقلب و جعل به کار می‌روند.

## دسته‌بندی‌ها
- **گواهی‌نامه و اسناد** (`certificates`): صدور، ذخیره و اعتبارسنجی مدارک دیجیتال.
- **هویت و احراز هویت** (`identity`): مدیریت هویت، SSO، MFA و DID.
- **زنجیره تأمین و ضدتقلب** (`supply_chain`): ردیابی منشأ دارایی‌ها و جلوگیری از جعل کالا.
- **رسانه و تشخیص دستکاری** (`media_forensics`): شناسایی رسانه و ویدئوهای دستکاری‌شده.
- **کتابخانه‌ها و ابزارهای رمزنگاری** (`library`): زیرساخت رمزنگاری پایه برای سایر سامانه‌ها.

## پروژه‌ها به تفکیک دسته
جداول زیر به‌صورت خودکار از `projects.json` ساخته می‌شوند. برای به‌روزرسانی، اسکریپت تولید README را اجرا کنید.

<!-- AUTO-GENERATED: PROJECT TABLES START -->
<div dir="rtl">
### گواهی‌نامه و اسناد
پروژه‌های صدور، ذخیره و اعتبارسنجی مدارک دیجیتال.

| پروژه | توضیح کوتاه | لایسنس | برچسب‌ها |
| --- | --- | --- | --- |
| [Automated Document Verification](https://github.com/Karan-07E/Automated-Document-Verification) | پلتفرم وب برای تأیید اسناد رسمی با بلاک‌چین و رابط کاربری مدرن. | UNKNOWN | document، verification، webapp |
| [Blockcerts (cert-issuer)](https://github.com/blockchain-certificates/cert-issuer) | استاندارد Blockcerts و ابزار صدور گواهی روی بلاک‌چین برای امضا و راستی‌آزمایی. | MIT | certificate، verification، education |
| [BlockChain-Based Document Verification with IPFS](https://github.com/DevAloshe/BlockChain-Based-Document-Verfication-With-IPFS) | ذخیره هش سند روی بلاک‌چین و سند در IPFS برای جلوگیری از دستکاری. | UNKNOWN | document، verification، integrity |
| [EtherDocs](https://github.com/DevelopersLeague/EtherDocs) | مدیریت و تأیید اسناد دانشگاهی با بلاک‌چین، IPFS و توابع هش. | UNKNOWN | education، document، verification |
| [Online Document Verification using Blockchain](https://github.com/SomSingh23/Online-document-verification-using-Blockchain) | سامانه وب برای تأیید و احراز اصالت اسناد با استفاده از بلاک‌چین. | UNKNOWN | document، verification، webapp |
| [OpenAttestation (OpenCerts)](https://github.com/Open-Attestation/open-attestation) | استاندارد OpenAttestation که زیرساخت OpenCerts سنگاپور برای صدور و اعتبارسنجی گواهی‌های آموزشی است. | Apache-2.0 | certificate، verification، education |

### هویت و احراز هویت
زیرساخت هویت، SSO، MFA و شناسه‌های غیرمتمرکز.

| پروژه | توضیح کوتاه | لایسنس | برچسب‌ها |
| --- | --- | --- | --- |
| [Authelia](https://github.com/authelia/authelia) | پورتال SSO و MFA به‌صورت reverse-proxy برای حفاظت برنامه‌های وب. | Apache-2.0 | identity، authentication، reverse-proxy |
| [Blockchain-based Identity Verification](https://github.com/Kayleexx/Blockchain-based-identity-verification) | سامانه احراز هویت غیرمتمرکز روی بلاک‌چین اتریوم با Solidity. | UNKNOWN | identity، blockchain، verification |
| [Decentralized Identity Verification (DID)](https://github.com/codewithsheikh/Decentralized-Identity-Verification-System-DID-on-Ethereum-Blockchain) | پیاده‌سازی سیستم DID برای مدیریت هویت غیرمتمرکز روی اتریوم. | UNKNOWN | identity، decentralized، blockchain |
| [Identity.com](https://github.com/identity-com) | مجموعه سرویس‌های احراز هویت غیرمتمرکز و KYC روی بلاک‌چین. | UNKNOWN | kyc، identity، verification |
| [Keycloak](https://github.com/keycloak/keycloak) | مدیریت هویت و دسترسی (SSO، احراز چندعاملی، مدیریت کاربر) برای وب‌اپ و API. | Apache-2.0 | identity، sso، authentication |
| [Ory Hydra](https://github.com/ory/hydra) | سرور OAuth2/OIDC متن‌باز برای صدور توکن و جلوگیری از جعل هویت. | Apache-2.0 | identity، authorization، tokens |

### زنجیره تأمین و ضدتقلب
ردیابی منشأ دارایی‌ها و جلوگیری از جعل کالا در زنجیره تأمین.

| پروژه | توضیح کوتاه | لایسنس | برچسب‌ها |
| --- | --- | --- | --- |
| [Hyperledger Food Supply Chain](https://github.com/AleRapchan/hyperledger-supply-chain) | راهکار زنجیره تأمین مواد غذایی روی Hyperledger Fabric برای ردیابی منشأ محصول. | UNKNOWN | food، supply-chain، traceability |
| [Hyperledger Grid](https://github.com/hyperledger/grid) | پلتفرم ماژولار برای مدیریت زنجیره تأمین و اصالت دارایی‌ها روی بلاک‌چین. | Apache-2.0 | supply-chain، provenance، modular |
| [OriginTrail DKG Client](https://github.com/OriginTrail/dkg-client) | کتابخانه برای تعامل با Decentralized Knowledge Graph و مدیریت دارایی‌های دانشی. | UNKNOWN | knowledge-graph، client، sdk |
| [OriginTrail Node (OT Node)](https://github.com/OriginTrail/ot-node) | نود شبکه OriginTrail برای ساخت گراف دانش غیرمتمرکز و داده‌های قابل‌اعتماد. | UNKNOWN | supply-chain، provenance، knowledge-graph |
| [Pharma Supply Chain (Fabric)](https://github.com/spike-spiegel-21/blockchain-supply-chain) | پیاده‌سازی زنجیره تأمین دارو با Hyperledger Fabric برای ردیابی و جلوگیری از تقلب. | UNKNOWN | pharma، supply-chain، traceability |
| [Supply Chain using Hyperledger Fabric & React](https://github.com/kuldeep23907/Supply-Chain-using-Hyperledger-Fabric-and-React) | نمونه سیستم زنجیره تأمین با تمرکز بر ردیابی و احراز اصالت و رابط React. | UNKNOWN | supply-chain، frontend، blockchain |

### رسانه و تشخیص دستکاری
مدل‌ها و ابزارهای تشخیص دیپ‌فیک و رسانه دستکاری‌شده.

| پروژه | توضیح کوتاه | لایسنس | برچسب‌ها |
| --- | --- | --- | --- |
| [Awesome Deepfakes Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) | فهرست مرجع مقالات و ابزارهای تشخیص دیپ‌فیک و فورنزیک رسانه. | UNKNOWN | deepfake، research، detection |
| [Deepfake Detection using Deep Learning](https://github.com/abhijithjadhav/Deepfake_detection_using_deep_learning) | تشخیص دیپ‌فیک ویدئو با ترکیب ResNext و LSTM (استخراج ویژگی + توالی زمانی). | UNKNOWN | deepfake، video، detection |
| [DeepfakeDetector](https://github.com/TRahulsingh/DeepfakeDetector) | سامانه تشخیص دیپ‌فیک با EfficientNet-B0 و رابط وب کاربرپسند. | UNKNOWN | deepfake، webapp، detection |
| [DeepSafe](https://github.com/siddharthksah/DeepSafe) | پلتفرم وب Streamlit برای تشخیص دیپ‌فیک روی تصویر و ویدئو. | UNKNOWN | deepfake، image، video |
| [FaceForensics++](https://github.com/ondyari/FaceForensics) | دیتاست و کد تشخیص چهره دستکاری‌شده برای سنجش سامانه‌های ضد دیپ‌فیک. | UNKNOWN | deepfake، dataset، benchmark |

### کتابخانه‌ها و ابزارهای رمزنگاری
لایه رمزنگاری پایه برای امضا، هش و مدیریت کلید.

| پروژه | توضیح کوتاه | لایسنس | برچسب‌ها |
| --- | --- | --- | --- |
| [libsodium](https://github.com/jedisct1/libsodium) | کتابخانه مدرن و ساده برای رمزنگاری، امضا، هش و مدیریت کلید. | ISC | encryption، hashing، signing |
| [OpenSSL](https://github.com/openssl/openssl) | تولکیت کامل SSL/TLS و رمزنگاری برای ارتباطات امن. | Apache-2.0 | encryption، tls، certificates |
| [Tink](https://github.com/google/tink) | کتابخانه چندزبانه گوگل برای رمزنگاری متقارن/نامتقارن و امضای دیجیتال با API امن. | Apache-2.0 | encryption، signing، key-management |

</div>
<!-- AUTO-GENERATED: PROJECT TABLES END -->

## راهنمای مشارکت
- برای افزودن پروژه جدید، یک ورودی کامل در `projects.json` با `github`، `license` و `tags` ثبت کنید.
- قوانین دقیق فرمت و دسته‌بندی در [CONTRIBUTING.md](CONTRIBUTING.md) و [docs/SCHEMA.md](docs/SCHEMA.md) ذکر شده‌اند.
- پیشنهادها، دسته‌بندی جدید یا لینک‌های مشکل‌دار را از طریق Issue یا Pull Request مطرح کنید.

## Related Awesome Lists
| List | Description |
| --- | --- |
| [Awesome Cryptography](https://github.com/sobolevn/awesome-cryptography) | فهرست کتابخانه‌ها و منابع رمزنگاری برای ساخت لایه‌های امن. |
| [Awesome Security](https://github.com/sbilly/awesome-security) | مجموعه ابزارها و منابع امنیتی عمومی که به سخت‌سازی سامانه‌های ضدتقلب کمک می‌کند. |
| [Awesome Identity](https://github.com/kdeldycke/awesome-iam) | فهرست IAM و SSO که برای کنترل دسترسی و احراز هویت قابل استفاده است. |

</div>
