# موارد استفاده پیشنهادی

در این سند، چند سناریوی متداول ضدجعل/ضدفرا‌د معرفی می‌شود و برای هر کدام پروژه‌های پیشنهادی از فهرست اصلی ارائه می‌گردد.

## 1. صدور گواهی دانشگاهی مقاوم در برابر جعل
- **پروژه‌های پیشنهادی:** [Blockcerts](https://github.com/blockchain-certificates/blockcerts)، [OpenCerts](https://github.com/OpenCerts/opencerts)، [EtherDocs](https://github.com/DevelopersLeague/EtherDocs)
- **راهنما:** از استاندارد Blockcerts برای قالب و امضای گواهی استفاده کنید، سپس با OpenCerts/ EtherDocs ذخیره و اعتبارسنجی کنید.

## 2. احراز هویت امن و جلوگیری از جعل هویت کاربران
- **پروژه‌های پیشنهادی:** [Keycloak](https://github.com/keycloak/keycloak)، [Authelia](https://github.com/authelia/authelia)، [Ory Hydra](https://github.com/ory/hydra)، پروژه‌های DID برای هویت غیرمتمرکز.
- **راهنما:** Keycloak یا Authelia را به‌عنوان دروازه SSO/MFA مستقر کنید؛ برای صدور توکن‌های امن OAuth2/OIDC از Ory Hydra استفاده کنید و در صورت نیاز به on-chain identity از پیاده‌سازی‌های DID بهره ببرید.

## 3. رهگیری اصالت دارو و کالا در زنجیره تأمین
- **پروژه‌های پیشنهادی:** [Hyperledger Food Supply Chain](https://github.com/AleRapchan/hyperledger-supply-chain)، [Hyperledger Grid](https://github.com/hyperledger/grid)، [OriginTrail Node](https://github.com/OriginTrail/ot-node)
- **راهنما:** داده‌های منبع و حمل را در Fabric/ Grid ثبت کنید و برای شفافیت و اشتراک‌گذاری بین ذی‌نفعان از OriginTrail DKG استفاده کنید.

## 4. تشخیص ویدئوهای دیپ‌فیک و رسانه دستکاری‌شده
- **پروژه‌های پیشنهادی:** [DeepfakeDetector](https://github.com/TRahulsingh/DeepfakeDetector)، [DeepSafe](https://github.com/siddharthksah/DeepSafe)، [FaceForensics++](https://github.com/ondyari/FaceForensics)
- **راهنما:** از FaceForensics++ برای داده آموزشی، DeepfakeDetector یا DeepSafe برای استقرار مدل و API تشخیص استفاده کنید و نتایج را در زنجیره گزارش کنید.

## 5. لایه رمزنگاری و امضای دیجیتال قابل اعتماد
- **پروژه‌های پیشنهادی:** [OpenSSL](https://github.com/openssl/openssl)، [libsodium](https://github.com/jedisct1/libsodium)، [Tink](https://github.com/google/tink)
- **راهنما:** بسته به زبان و پشته، یکی از این کتابخانه‌ها را برای امضا، رمزنگاری و مدیریت کلید به‌عنوان پایه امنیتی سایر راهکارها به‌کار ببرید.
