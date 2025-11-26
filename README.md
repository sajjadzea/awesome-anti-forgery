# Awesome Anti-Forgery & Anti-Fraud

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A curated list of open-source projects that fight forgery, fraud, and counterfeiting across documents, identities, supply chains, and media. These tools cover verifiable credentials, identity and access management, provenance for physical and digital goods, and media authenticity checks. The focus is on actionable software—frameworks, SDKs, and reference implementations—not generic articles.

## Table of Contents
- [Certificates & Documents](#certificates--documents)
- [Identity & Authentication](#identity--authentication)
- [Supply Chain & Anti-Counterfeiting](#supply-chain--anti-counterfeiting)
- [Deepfake & Media Forensics](#deepfake--media-forensics)
- [Supporting Libraries & Tools](#supporting-libraries--tools)
- [How to Use This List](#how-to-use-this-list)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Certificates & Documents
- **Blockcerts** – Open standard and tools for blockchain-based certificates and credentials. [GitHub](https://github.com/blockchain-certificates/blockcerts)
- **Credential Handler Polyfill** – Polyfill for W3C Verifiable Credential wallets to issue and verify digital credentials. [GitHub](https://github.com/digitalbazaar/credential-handler-polyfill)
- **Open Badges Validator Core** – Validator for IMS Open Badges to check badge authenticity and structure. [GitHub](https://github.com/IMSGlobal/openbadges-validator-core)

## Identity & Authentication
- **Authelia** – SSO portal and 2FA-capable reverse proxy to protect web applications. [GitHub](https://github.com/authelia/authelia)
- **Keycloak** – Identity and access management with SSO, brokering, and fine-grained authorization. [GitHub](https://github.com/keycloak/keycloak)
- **privacyIDEA** – Multi-factor authentication and policy engine for diverse tokens and workflows. [GitHub](https://github.com/privacyidea/privacyidea)

## Supply Chain & Anti-Counterfeiting
- **Hyperledger Grid** – Framework for supply-chain data models, product catalogs, and provenance. [GitHub](https://github.com/hyperledger/grid)
- **in-toto** – Framework to secure software supply chains with signed step metadata and layout verification. [GitHub](https://github.com/in-toto/in-toto)
- **OriginTrail** – Decentralized knowledge graph for product traceability and authenticity proofs. [GitHub](https://github.com/OriginTrail/ot-node)
- **Sigstore Cosign** – Container signing and verification to prove software origin and integrity. [GitHub](https://github.com/sigstore/cosign)

## Deepfake & Media Forensics
- **DFDC Deepfake Challenge** – Training and inference pipeline for the Facebook Deepfake Detection Challenge dataset. [GitHub](https://github.com/selimsef/dfdc_deepfake_challenge)
- **FaceForensics** – Dataset and benchmark code for detecting manipulated face videos and images. [GitHub](https://github.com/ondyari/FaceForensics)

## Supporting Libraries & Tools
- **Google Tink** – Multi-language cryptography SDK with safe defaults for signing and encryption. [GitHub](https://github.com/google/tink)
- **libsodium** – Modern, easy-to-use cryptographic library for signatures, encryption, and hashing. [GitHub](https://github.com/jedisct1/libsodium)
- **OpenSSL** – TLS/SSL toolkit and general-purpose cryptography library. [GitHub](https://github.com/openssl/openssl)
- **Python TUF** – Reference implementation of The Update Framework for secure software updates. [GitHub](https://github.com/theupdateframework/python-tuf)
- **YubiKey libfido2** – FIDO2/WebAuthn library for authenticators and security keys. [GitHub](https://github.com/Yubico/libfido2)

## How to Use This List
- Browse by category to discover projects that match your use case—documents, identity, supply chains, or media forensics.
- Combine categories to build layered defenses (e.g., identity verification + document signing + supply-chain provenance).
- Use these repos as starting points for prototypes, integrations, or audits when designing anti-fraud and authenticity workflows.

## Roadmap
- Expand coverage to sector-specific solutions (e.g., healthcare credentials, digital ticketing).
- Add language and license badges for quick filtering.
- Automate link health checks and metadata synchronization with `projects.json`.

## Contributing
Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md) and keep entries concise, factual, and in alphabetical order. Update both `README.md` and `projects.json` when adding projects.

## License
This project is licensed under the [MIT License](LICENSE).
