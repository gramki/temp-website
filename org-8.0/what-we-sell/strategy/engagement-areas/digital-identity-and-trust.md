# Digital Identity and Trust

## Executive Summary

The vendor-addressable market for banking identity and trust infrastructure exceeds USD 30 billion and is growing at approximately 14–15 percent annually, driven by regulatory compounding across jurisdictions, digital-first channel dominance, and the emergence of AI agents as a new identity category. Eight structural shifts are reshaping the market over a two-to-ten-year horizon, creating opportunity concentration in three areas: unified trust infrastructure for multi-jurisdictional compliance, passwordless and biometric authentication, and identity governance for AI agents.

The market remains fragmented across six sub-segments — CIAM, identity verification, authentication, consent management, fraud analytics, and non-human identity — with no single vendor spanning all six in a banking-grade platform. Private equity has deployed over USD 13 billion assembling identity portfolios (Thoma Bravo, Permira), signaling that convergence is inevitable but not yet achieved. This fragmentation creates a structural opening for a platform vendor that treats identity, authentication, consent, privacy, and AI agent governance as a single architectural surface.

Zeta's position is distinctive but incomplete. Trust Fabric's architecture directly addresses the convergence gap — identity, authentication, consent, and privacy as a unified layer, with first-class AI agent identity via Seer. Quark Customer Lifecycle provides the domain model for customer identity lifecycle governance. These capabilities are architecturally differentiated and, in the case of AI agent identity, ahead of all surveyed competitors. The principal gaps are in identity verification depth (document verification, biometric liveness, deepfake detection), behavioral biometrics, and geographic regulatory specificity — particularly for India's Aadhaar-based infrastructure and the EU's eIDAS 2.0 wallet mandate.

The recommended strategy is to pursue Tier 2 US banks as the beachhead segment (highest buy propensity, lowest competitive entrenchment), lead with AI agent identity governance as the wedge capability no incumbent offers, and defer direct competition in mature identity verification and behavioral biometrics sub-segments where entrenched specialists dominate.

---

# Part I — The Opportunity

## 1. The Market

Banks spend more on identity-related infrastructure than most technology categories outside core processing. Across six sub-segments, the vendor-addressable market for banking identity and trust infrastructure reaches USD 29.7–34.8 billion in 2025, projected to reach USD 57.3–68.6 billion by 2030 — a compound annual growth rate of approximately 14–15 percent.

| Sub-Segment | Banking TAM 2025 (est.) | Banking TAM 2030 (est.) | CAGR |
|---|---|---|---|
| Customer Identity and Access Management (CIAM) | USD 4.0–4.5 B | USD 6.4–7.5 B | 10–18% |
| Identity Verification / eKYC | USD 4.0–5.0 B | USD 8.5–10.0 B | 15% |
| Consent and Privacy Management | USD 0.15–0.25 B | USD 0.4–0.6 B | 18% |
| Fraud / Identity Analytics | USD 8.0–10.0 B | USD 17.0–22.0 B | 16–23% |
| Enterprise IAM (internal) | USD 9.0–9.5 B | USD 15.0–15.5 B | 10% |
| Authentication Infrastructure | USD 4.5–5.5 B | USD 10.0–13.0 B | 18–27% |
| **Total** | **USD 29.7–34.8 B** | **USD 57.3–68.6 B** | **~14–15%** |

Sources: [MarketsandMarkets IAM Market Report 2025–2030](https://www.marketsandmarkets.com/Market-Reports/identity-access-management-iam-market-1168.html); [MarketsandMarkets Identity Verification Market 2025–2030](https://www.marketsandmarkets.com/Market-Reports/identity-verification-market-178660742.html); [Mordor Intelligence Passwordless Authentication Market](https://www.mordorintelligence.com/industry-reports/passwordless-authentication-market); [MarketsandMarkets Fraud Detection Market 2025–2030](https://www.prnewswire.com/news-releases/fraud-detection-and-prevention-market-worth-65-68-billion-by-2030--marketsandmarkets-302514788.html)

Banking and financial services is the largest single vertical in every identity sub-segment, accounting for 28–36 percent of spend depending on category ([Mordor Intelligence CIAM Market](https://www.mordorintelligence.com/industry-reports/global-consumer-identity-and-access-management-market); [Fundamental Business Insights IAM Market](https://www.fundamentalbusinessinsights.com/industry-report/identity-and-access-management-market-7307)). Identity ranks as the second-highest IT investment priority for North American corporate banks — behind only AI — with 37 percent ranking it in their top three ([Celent Dimensions: Corporate Banking IT Pressures & Priorities NA 2025](https://celent.com/en/insights/insight-4)). Ninety percent of banking and financial services respondents consider identity critical to their security goals, and 42 percent now view customer identity management as a revenue center rather than a cost center ([Thales BFSI 2025 Survey](https://cpl.thalesgroup.com/blog/access-management/identity-access-bfsi-2025-survey)).

The geographic distribution is uneven. North America accounts for approximately 40 percent of CIAM demand. The EU is the fastest-growing regulatory-driven market, with GDPR enforcement, eIDAS 2.0 wallet mandates, and the EU AI Act compounding compliance investment. India is structurally distinct — Aadhaar-based eKYC processes over 27 billion authentication transactions annually ([UIDAI FY24-25 Data](https://www.uidai.gov.in/en/media-resources/media/press-releases/18883-aadhaar-authentication-surges-past-2-707-cr-in-2024-25-aadhaar-e-kyc-transactions-close-to-45-cr-in-march.html)), creating a public-infrastructure identity layer that shapes vendor opportunity differently from Western markets.

## 2. How We Got Here

Banking identity infrastructure has passed through three eras, each leaving architectural sediment that the next must absorb.

**The directory era** treated identity as an IT administration function. Active Directory, LDAP, and mainframe-era access control systems managed who could log in and what they could reach. Identity was an internal concern — customers proved themselves at the branch counter with a signature, a passbook, and a personal relationship with their banker.

**The point-solution era** followed digitization. As banks opened web and mobile channels, each new surface — online banking, mobile apps, call centers, open banking APIs — acquired its own identity and authentication stack. CIAM platforms handled customer login. KYC systems handled onboarding. Consent tools handled open banking permissions. Fraud engines monitored transactions. Privacy teams managed GDPR workflows. Each system worked in isolation. Each regulatory mandate — PSD2 Strong Customer Authentication, GDPR consent, FinCEN CDD, RBI KYC — triggered a separate compliance project layered onto the existing stack.

**The convergence era** is now beginning. Three forces are compressing the point-solution architecture. First, regulatory convergence across jurisdictions is making per-regulation compliance projects unsustainable — a bank operating in the USA and EU must comply with 18–22 distinct identity, privacy, and authentication regulations simultaneously. Second, fraud has become an identity problem: synthetic identity losses exceed USD 35 billion annually ([Federal Reserve Bank of Boston](https://www.bostonfed.org/news-and-events/news/2025/04/synthetic-identity-fraud-financial-fraud-expanding-because-of-generative-artificial-intelligence.aspx)), and deepfake attacks grew 704 percent in the second half of 2023 alone ([iProov Threat Intelligence Report 2024](https://www.iproov.com/press/annual-identity-verification-threat-intelligence-report)). Third, AI agents are entering banking workflows without an identity model — 95 percent of enterprises now run agents autonomously, but only 18 percent of security leaders are confident their identity infrastructure can manage them ([ConductorOne 2026 Survey](https://www.conductorone.com/news/press-release/future-of-identity-security-2026/); [CSA/Strata Identity Survey 2026](https://www.strata.io/resources/whitepapers/securing-autonomous-ai-agents-csa-survey-report-2026-strata-identity/)).

## 3. Structural Shifts Creating Opportunity

### Shift 1: Regulatory convergence forcing unified trust infrastructure

A bank operating across the USA and EU now navigates 18–22 distinct regulations with identity, authentication, consent, or privacy obligations — from GDPR and PSD2 SCA to CCPA/CPRA, the 20-state US privacy patchwork, FinCEN CDD, FFIEC authentication guidance, eIDAS 2.0, and the EU AI Act. Each regulation independently requires a subset of the same underlying capabilities: consent management, identity proofing, multi-factor authentication, breach notification.

The compliance burden is growing faster than the resources to manage it. A [Bank Policy Institute survey](https://bpi.com/survey-finds-compliance-is-growing-demand-on-bank-resources/) of 20 major US banks found that IT budget allocation to compliance grew 40 percent between 2016 and 2023 (from 9.6 percent to 13.4 percent), C-Suite time on compliance increased 75 percent, and employee compliance hours rose 61 percent — despite only 20 percent workforce growth. In Europe, 51 percent of financial services professionals cite keeping up with regulatory change as their top challenge ([Sumsub 2025 European Report](https://financialit.net/news/compliance/compliance-fatigue-emerges-leading-challenge-europes-financial-services-new-sumsub)). In the US, 54 percent of financial services firms still rely on spreadsheets to track security controls ([Omega Systems, November 2025](https://omegasystemscorp.com/insights/blog/omega-systems-report-exposes-growing-compliance-fatigue-in-financial-services/)).

The compounding effect is structural: building separate compliance projects for GDPR consent, CCPA opt-out, DPDP consent managers, PSD3 consent dashboards, and open banking permissions — each requiring the same foundational consent architecture — is multiplicatively more expensive than building unified consent infrastructure configurable per regulatory regime.

### Shift 2: Digital-first identity replacing branch-based verification

The US bank branch network has contracted 14.8 percent since 2017 — from 86,469 to 73,649 branches ([NCRC / S&P Global](https://ncrc.org/bank-branch-closures-slow-but-shifting-demographics-cloud-the-picture/)). Globally, 2.17 billion people use mobile banking, with penetration reaching 76 percent in Europe and 61 percent in the USA ([ABSRBD / Statista](https://www.absrbd.com/post/mobile-banking-statistics)). India's Aadhaar infrastructure processed 27.07 billion authentication transactions in FY24-25 ([UIDAI](https://www.uidai.gov.in/en/media-resources/media/press-releases/18883)), with face authentication emerging as the fastest-growing modality at over 150 million monthly transactions.

Branch closure does not merely shift where identity verification happens — it eliminates the channel where identity assurance was highest and replaces it with channels where fraud risk is greatest. Digital account opening abandonment rates exceed 68 percent, and 8.3 percent of digital account creations are flagged as potentially fraudulent ([BIIA.com / FiVerity](https://www.biia.com/synthetic-identity-fraud-statistics-2026-hard-numbers-big-threats/)). The infrastructure that replaces the branch counter must deliver equivalent assurance at digital scale.

### Shift 3: Passwordless authentication becoming the security baseline

Passkey adoption has reached inflection. Ninety-three percent of accounts at leading providers are eligible for passkeys, 36 percent have enrolled, and 26 percent of sign-ins now use passkeys — with a 93 percent success rate compared to 63 percent for legacy methods, 73 percent faster sign-in times, and an 81 percent reduction in help-desk incidents ([FIDO Alliance Passkey Index 2025](https://fidoalliance.org/fido-alliance-launches-passkey-index-revealing-significant-passkey-uptake-and-business-benefits/)). Enterprise deployment has reached 87 percent in the US and UK ([FIDO Alliance Enterprise Report](https://fidoalliance.org/new-fido-alliance-report-87-of-enterprises-in-the-u-s-and-uk-are-deploying-passkeys)). Three countries — UAE, India, and the Philippines — have mandated SMS OTP elimination for financial services in 2026 ([Security Boulevard](https://securityboulevard.com/2026/03/passkeys-at-scale-the-complete-enterprise-deployment-playbook-2026/)).

Compromised credentials remain the most common breach vector — 22 percent of all breaches according to the [Verizon 2025 DBIR](https://www.verizon.com/business/resources/articles/credential-stuffing-attacks-2025-dbir-research/) — and 16 billion unique credentials have been leaked cumulatively ([Cybernews / RockYou2025](https://passwordsleaked.com/blog/2025-06-20-16-billion-credentials-leak-vs-rockyou-2024-why-its-an-even-bigger-deal)). Passwordless is no longer a differentiation play. It is the security baseline that every banking identity platform must deliver.

### Shift 4: Synthetic identity fraud forcing identity infrastructure investment

Total identity fraud and scam losses reached USD 47 billion in 2024 — USD 27 billion in identity fraud across 18 million victims and USD 20 billion in scams across 22 million victims ([Javelin 2025 Identity Fraud Study](https://javelinstrategy.com/research/2025-identity-fraud-study-breaking-barriers-innovation)). Account takeover losses grew 23 percent year-over-year to USD 15.6 billion ([Federal Reserve Financial Services](https://www.frbservices.org/news/fed360/issues/021726/fraud-mitigation-account-takeover)). The FBI's Internet Crime Complaint Center reported USD 16.6 billion in losses — a 33 percent increase ([FBI IC3 2024](https://www.fbi.gov/news/press-releases/fbi-releases-annual-internet-crime-report)).

Synthetic identity fraud — the fastest-growing category — uses combinations of fabricated and real information to create identities that pass traditional verification. Losses are estimated to exceed USD 35 billion annually ([Federal Reserve Bank of Boston / FiVerity](https://www.bostonfed.org/news-and-events/news/2025/04/synthetic-identity-fraud-financial-fraud-expanding-because-of-generative-artificial-intelligence.aspx)). Deepfake-enabled fraud compounds the problem: face swap attacks grew 704 percent in the second half of 2023 ([iProov](https://www.iproov.com/press/annual-identity-verification-threat-intelligence-report)), and the cost of producing a convincing deepfake has collapsed from hundreds of dollars to USD 30–50 ([Kaspersky 2025](https://me-en.kaspersky.com/about/press-releases/kaspersky-warns-deepfake-services-are-now-400-times-cheaper-and-more-accessible)). Standalone fraud engines that operate without real-time identity signals are structurally disadvantaged against these attack vectors.

### Shift 5: Privacy as architecture, not compliance project

GDPR enforcement has reached EUR 7.1 billion in cumulative fines, with 443 breach notifications filed daily — a 22 percent year-over-year increase ([DLA Piper GDPR Fines Survey January 2026](https://www.dlapiper.com/en-gb/insights/publications/2026/01/dla-piper-gdpr-fines-and-data-breach-survey-january-2026)). Twenty US states now have comprehensive privacy laws, covering over 184 million residents — more than half the population — with no federal standard in sight ([MultiState Tracker 2026](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026)). India's Digital Personal Data Protection Act reaches full compliance by May 2027, with penalties up to INR 250 crore ([CADP DPDP Implementation Tracker](https://cadp.in/resources/guides/dpdp-implementation-tracker/)). India's Account Aggregator framework has scaled to 580 Financial Information Users and 173 Financial Information Providers, processing 11.58 crore consent-based transactions in FY25 ([Business Standard / Sahamati](https://www.business-standard.com/finance/news/aa-ecosystem-consent-processing-up-78-in-fy25-shows-sahamati-data-125031301053_1.html)).

The structural implication: consent, data minimization, and erasure obligations are no longer compliance features bolted onto existing systems. They must be foundational to how data flows through the enterprise — embedded in architecture, not applied after the fact.

### Shift 6: Identity convergence — from point solutions to trust platforms

The boundaries between identity sub-segments are dissolving through M&A. Since 2021, over USD 17.5 billion in identity-adjacent deals have completed: Thoma Bravo's acquisition and merger of Ping Identity (USD 2.8 billion) and ForgeRock (USD 2.3 billion), CyberArk's acquisition of Venafi (USD 1.54 billion), IBM's acquisition of HashiCorp (USD 6.4 billion), Entrust's acquisition of Onfido (~USD 650 million), Permira's acquisition of BioCatch (USD 1.3 billion valuation), SailPoint's re-IPO (USD 1.32 billion raised), and LexisNexis's acquisition of IDVerse. Fraud analytics vendors are acquiring identity verification. PKI vendors are acquiring biometric verification. CIAM vendors are merging with governance platforms.

Eighty-nine percent of banking and financial services respondents report an urgent or moderate desire to consolidate identity vendors ([Thales 2025 BFSI Survey](https://cpl.thalesgroup.com/blog/access-management/identity-access-bfsi-2025-survey)). The demand for convergence is clear. The supply is not: no single vendor spans all six identity sub-domains — CIAM, identity verification, authentication, consent, fraud analytics, and non-human identity — in a banking-grade platform.

### Shift 7: AI agents creating a new identity category

Ninety-five percent of enterprises now run AI agents autonomously, yet only 18 percent of security leaders are confident their identity infrastructure can manage agent identities ([ConductorOne 2026](https://www.conductorone.com/news/press-release/future-of-identity-security-2026/); [CSA/Strata Identity 2026](https://www.strata.io/resources/whitepapers/securing-autonomous-ai-agents-csa-survey-report-2026-strata-identity/)). Only 23 percent of organizations have a formal agent identity strategy. Only 28 percent can trace agent actions to a human sponsor. Eighty-four percent doubt they could pass an audit on agent access controls.

The EU AI Act classifies credit scoring and creditworthiness assessment AI as high-risk under Annex III, with compliance required by August 2026 — penalties reach 7 percent of global turnover ([EU AI Act Implementation Timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline)). The Act establishes deployer obligations (Article 26) that cannot be contractually transferred to providers: banks must assign trained human overseers, maintain event logs for six months minimum, and report serious incidents regardless of what vendor contracts state.

Machine identities already outnumber humans 82–87:1 in financial services ([CyberArk 2025](https://www.cyberark.com/press/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security/)). But machine identity — certificates, secrets, API keys — is not agent identity. AI agents require delegation chains, authority boundaries, context-specific permissions, and human accountability linkage. No product or standard delivers this comprehensively. The [IETF Transaction Tokens for Agents draft](https://datatracker.ietf.org/doc/draft-oauth-transaction-tokens-for-agents/) (February 2026) and the [OpenID Foundation agentic AI whitepaper](https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/) (October 2025) are the closest protocol-level specifications, both in early stages.

### Shift 8: Banks as identity providers — monetizing trust

Banks hold a unique position in the identity ecosystem: they have already verified their customers' identities to regulatory standards. Several jurisdictions are formalizing frameworks that allow banks to extend this verified identity to third parties. Australia's ConnectID covers over 10 million customers through the Big Four banks ([ConnectID](https://connectid.com.au/big-four-banks-join-connectid-so-customers-can-share-less-online/)). Canada's Interac Verified processed 141 million interactions for 14 million Canadians ([Interac](https://interac.ca/en/consumers/products/interac-verification-solutions/sign-in-service/)). The EU's eIDAS 2.0 regulation mandates that banks accept EU Digital Identity Wallets by December 2027 ([eIDAS 2.0 Timeline](https://eidasreadiness.com/eidas-2-timeline)) — and positions banks as relying parties in a pan-European identity layer.

The Identity-as-a-Service market is forecast at USD 10.8 billion in 2025, growing to USD 99 billion by 2035 at 24.8 percent CAGR, with banking and financial services accounting for 31.2 percent ([Fundamental Business Insights](https://www.fundamentalbusinessinsights.com/industry-report/identity-as-a-service-market-4805)). Banks that invest in identity infrastructure today are not just meeting compliance obligations — they are building a monetizable trust asset.

## 4. The Engagement Landscape

Banks are not buying "identity platforms" as a single procurement. Engagement activity clusters around specific program types, each tied to a structural shift and varying by bank tier:

| Program Type | Bank Tier | Structural Shift | Engagement Evidence |
|---|---|---|---|
| CIAM modernization / passwordless | Tier 1–2 | Shifts 3, 6 | Wells Fargo passkey rollout; JPMorgan anti-deepfake authentication; Bank of America QR sign-in; DBS/OCBC/UOB Singpass integration |
| KYC/eKYC transformation | Tier 1–3 | Shifts 2, 4 | BNP Paribas "One KYC" global platform; Standard Chartered centralized identity; Boost Bank facial recognition onboarding |
| Consent and privacy compliance | Tier 1–2 | Shifts 1, 5 | Driven by GDPR, CCPA patchwork, DPDP Act; engagement via OneTrust/TrustArc procurement |
| Fraud-identity convergence | Tier 1 | Shift 4 | BioCatch deployment at 32 of top 100 banks; LexisNexis IDVerse acquisition for front-end IDV |
| AI agent governance | Early adopters | Shift 7 | No public bank program yet — gap between AI deployment (92 percent of EU banks) and agent identity governance (23 percent with strategy) |
| Digital identity-as-a-service | Consortia | Shift 8 | ConnectID (Australia Big Four), Interac Verified (Canada Big Six), eIDAS 2.0 wallet integration |

The most significant near-term opportunity concentration is at the intersection of Tier 2 US banks and shifts 1, 3, and 6: banks with USD 10–100 billion in assets that cannot afford per-regulation compliance engineering, are under pressure to deploy passwordless authentication, and want to consolidate identity vendors — but lack the internal engineering capacity of Tier 1 institutions. These banks predominantly buy rather than build.

## 5. The Competitive Landscape

The competitive landscape for banking identity infrastructure divides into six categories. No vendor spans all six.

**Enterprise IAM / CIAM.** Ping Identity (post-ForgeRock merger, ~USD 800 million ARR, [9 of 9 largest US banks](https://www.prnewswire.com/news-releases/ping-identity-surpasses-30-annual-growth-in-saas-revenue-and-approaches-800m-arr-302305376.html)) is the banking incumbent. Okta (USD 2.92 billion revenue, [SEC filing](https://investor.okta.com/financials/quarterly-results/default.aspx)) leads in cloud CIAM broadly but has limited banking-specific depth. Microsoft Entra ID dominates workforce identity through M365 bundling but is not purpose-built for banking CIAM. Transmit Security ([Gartner MQ Leader 2025](https://transmitsecurity.com/content-hub/global-bank-takes-200-million-customers-passwordless-with-transmit-security)) focuses on passwordless banking. None offers native identity verification, fraud analytics, or consent management.

**Identity Verification / eKYC.** Socure ([18 of top 20 US banks](https://www.socure.com/company/), USD 4.5 billion valuation) leads US banking penetration. LexisNexis Risk Solutions (~GBP 3.2 billion Risk division revenue, [RELX 2024 Results](https://www.relx.com/~/media/Files/R/RELX-Group/documents/press-releases/2025/results-2024-pressrelease.pdf)) dominates fraud-adjacent IDV. Onfido (acquired by Entrust for ~USD 650 million) and Jumio serve global verification needs. These vendors do not offer CIAM, consent, or AI agent identity.

**Consent and Privacy.** OneTrust (USD 500 million ARR, [OneTrust Press](https://www.onetrust.com/news/onetrust-trustweek-2024-momentum/)) defines the category but is a privacy/GRC company, not an identity company. No consent vendor offers identity verification or authentication.

**Fraud / Identity Analytics.** BioCatch ([32 of top 100 banks](https://www.permira.com/news-and-insights/announcements/permira-completes-acquisition-of-majority-position-in-biocatch-at-13-billion-valuation), behavioral biometrics), NICE Actimize (largest enterprise fraud platform in banking), and the credit bureaus (Experian, TransUnion, LexisNexis) dominate fraud analytics. Each focuses on detection, not on managing the identity lifecycle.

**Non-Human / AI Agent Identity.** CyberArk (USD 1.34 billion ARR, [Venafi acquisition](https://www.cyberark.com/press/cyberark-announces-strong-third-quarter-2025-results/)) leads machine identity. Microsoft Entra Workload ID (0.7 percent IDaaS mindshare) and Astrix Security (USD 85 million funded) are nascent. All address infrastructure identity — certificates, secrets, API keys — not AI agent delegation, authority, and human accountability.

**The convergence gap.** The market's defining feature is that no vendor has assembled a banking-grade platform spanning CIAM, identity verification, authentication, consent, fraud analytics, and AI agent identity. Thoma Bravo has deployed USD 13 billion+ in identity-adjacent acquisitions (Ping, ForgeRock, SailPoint, Venafi), but PE-assembled portfolios do not guarantee architectural integration. The demand is clear — 89 percent of banking respondents want vendor consolidation — but the supply does not exist.

## 6. Target Universe

The following institutions have publicly signaled identity modernization activity, organized by geography, tier, and evidence basis.

**USA — Tier 1**

| Institution | Signal | Source |
|---|---|---|
| JPMorgan Chase | Passkey deployment; anti-deepfake facial authentication; patent filed for liveness detection | [MobileIDWorld 2025](https://mobileidworld.com/jpmorgan-chase-enhances-mobile-banking-security-with-anti-deepfake-measures-and-passkeys/) |
| Wells Fargo | Passkeys for all customers; biometric authentication; Transmit Security partnership | [Wells Fargo Passkey FAQ](https://wellsfargo.com/help/security-and-fraud/passkey-faqs) |
| Bank of America | QR sign-in on CashPro surged 60% YoY; Push Authentication; eliminating physical tokens | [BofA Newsroom May 2025](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/05/qr-sign-ins-surge-60--on-bofa-s-cashpro--platform.html) |
| TD Bank | CIAM modernization with Deloitte; identity-proofing and real-time fraud alerts | [Fintech Futures](https://www.fintechfutures.com/bankingtech/td-bank-upgrades-retail-card-business-with-backbase-engagement-banking-platform) |

**EU/UK — Tier 1**

| Institution | Signal | Source |
|---|---|---|
| BNP Paribas | "One KYC" global platform using AI/automation; Encompass corporate digital identity | [BNP Paribas CIB](https://cib.bnpparibas/one-kyc-an-innovative-tech-solution-to-improve-customer-experience/) |
| NatWest | First UK bank to integrate OneID bank-verified digital identity; BioCatch behavioral biometrics since 2016 | [NatWest Group July 2024](https://www.natwestgroup.com/news-and-insights/news-room/press-releases/data-and-technology/2024/jul/natwest-leads-in-bank-verified-digital-identity-by-integrating-o.html) |
| Deutsche Bank | Digital identity white paper exploring zero-knowledge identity with Polygon Labs | [Deutsche Bank Flow May 2024](https://flow.db.com/publications/flow-white-papers-and-guides/digital-identity?language_id=1) |
| Standard Chartered | Centralized identity platform via Ping Identity across 30 retail markets | [Ping Identity Case Study](https://www.pingidentity.com/en/customer-stories/3987-standard-chartered.html) |

**Asia-Pacific — Tier 1**

| Institution | Signal | Source |
|---|---|---|
| DBS Bank | Singpass Face Verification; phasing out OTPs; money lock anti-scam feature | [The Paypers](https://thepaypers.com/fraud-and-fincrime/news/dbs-and-ocbc-to-implement-biometric-authentication) |
| OCBC | Singpass Face Verification; OneTouch/OneLook biometric login; voice biometrics | [OCBC Security](https://www.ocbc.com/personal-banking/security/secure-banking-ways/ocbc-onetouch-onelook.page) |

**USA — Tier 2–3 (near-term opportunity)**

| Institution | Signal | Source |
|---|---|---|
| IncredibleBank | Alloy identity + fraud platform; 90% automated account opening | [Alloy Case Study](https://alloy.com/case-studies/incrediblebank) |
| Heritage Bank | Persona for streamlined KYC/AML; 2.4x faster application time | [Persona Case Study](https://withpersona.com/customers/heritage-bank) |
| WyHy Federal CU | Illuma Shield voice authentication; 83% faster verification | [Illuma Case Study](https://illuma.cx/article/wyhy-credit-union-illuma-case-study/) |

These Tier 2–3 institutions are predominantly buying, not building — deploying vendor platforms to solve identity challenges that their internal engineering teams cannot address. Their vendor consolidation appetite and limited internal engineering capacity make them the most receptive segment for any platform vendor offering architectural convergence across identity sub-domains.

---

# Part II — The Advisory

## 7. Zeta's Position

Zeta's product architecture maps to the digital identity and trust opportunity through four assets:

**Trust Fabric** is the primary platform. Its architecture directly addresses the convergence gap identified in Part I — identity, authentication, consent, and privacy as a single layer, with AI agent identity as a first-class concern. Trust Fabric's capability domains align to the six identity sub-segments: Identity Foundation (CIAM), Verification and Onboarding (eKYC), Authentication (passwordless/adaptive), Consent and Data Governance (privacy/consent), Trust Intelligence (fraud/identity analytics), and AI Agent Identity and Delegation (non-human identity). No surveyed competitor mirrors this architectural scope.

**Quark Customer Lifecycle** provides the domain-specific work model for customer identity — onboarding through active relationship to dormancy and exit — operating on Evolution Fabric's infrastructure. It instantiates the operational patterns (identity risk workflows, behavioral risk loops, lifecycle governance) that Trust Fabric's infrastructure layer enables.

**Evolution Fabric / Seer** governs AI agent participation in identity workflows. Seer provides agent lifecycle management, identity and authority, context assembly, and guardrails. When an AI agent resolves a dispute, processes an application, or executes a compliance check, Seer governs its identity — who authorized it, what it may access, which human is accountable. This directly addresses Shift 7's governance gap, and no surveyed competitor — including CyberArk, Microsoft Entra Workload ID, and Astrix — offers equivalent agent-level accountability infrastructure for banking workflows.

**Cognitive Audit Fabric** provides decision auditability for identity decisions, particularly for AI agents — reconstructable audit trails that satisfy the EU AI Act's deployer obligations under Article 26.

**Honest assessment of gaps:**

- **Identity verification depth.** Trust Fabric defines document verification, biometric liveness, and deepfake detection as capabilities but does not possess the trained models, document libraries, or biometric matching algorithms that specialists (Socure, iProov, Jumio) have built over years. This capability likely requires a build-or-partner decision.
- **Behavioral biometrics.** BioCatch serves 32 of the top 100 banks with behavioral models trained on 11.6 billion monthly sessions. Replicating this data advantage is not feasible. Partnership or integration is the realistic path.
- **Geographic regulatory specificity.** India's Aadhaar integration (UIDAI-certified biometric infrastructure, V-CIP, CKYCR) and the EU's eIDAS 2.0 wallet mandate each require jurisdiction-specific implementation depth that is not yet demonstrated.
- **Go-to-market in identity buying centers.** Identity infrastructure is purchased by CISOs, identity architects, and fraud leadership — a buying center distinct from the CIO/CTO audiences that banking platform vendors typically address.

## 8. Where to Play

**Pursue — Near-term (0–2 years):**

- **Tier 2 US banks (USD 10–100 billion in assets).** Highest buy propensity, lowest competitive entrenchment. Ping Identity dominates Tier 1; Tier 2 banks are assembling multi-vendor identity stacks with active vendor consolidation appetite. Lead with unified trust layer positioning.
- **AI agent identity governance — all tiers.** No competitor has a production-grade offering. The EU AI Act's August 2026 deadline creates urgency for EU-operating banks. Trust Fabric + Seer's agent identity and delegation model is architecturally differentiated. This is the wedge capability.
- **Consent and privacy as infrastructure — Tier 2 US and EU banks.** The 20-state US privacy patchwork and GDPR/DPDP convergence create demand for consent-as-architecture. Trust Fabric's consent domain addresses a capability that CIAM vendors (Okta, Ping) do not offer and privacy vendors (OneTrust) deliver without identity context.

**Pursue — Medium-term (2–5 years):**

- **Tier 1 US and EU banks.** After proving at Tier 2, expand to Tier 1 where identity budgets are largest (USD 15–350 million per institution) but vendor entrenchment and switching costs are highest.
- **India — upon Aadhaar/RBI integration.** India's identity market is structurally distinct. Entry requires UIDAI-certified biometric integration, V-CIP capability, Account Aggregator connectivity, and DPDP consent manager compliance. Pursue after building this regulatory-specific layer.
- **eIDAS 2.0 wallet integration — EU.** Banks must accept EU Digital Identity Wallets by December 2027. Trust Fabric's federation and credential verification capabilities position it as the integration layer, but implementation requires participation in EU Digital Identity Wallet large-scale pilots.

**Defer:**

- **Direct competition in identity verification.** Socure, LexisNexis, and the credit bureaus have data moats and banking relationships in IDV that are not replicable. Integrate with IDV specialists rather than competing. Trust Fabric should be the orchestration layer that consumes IDV signals, not the IDV engine itself.
- **Behavioral biometrics.** BioCatch's 32-of-top-100-banks position and proprietary behavioral models represent a data-driven moat. Partner rather than build.
- **Tier 3 banks (under USD 1 billion in assets).** Identity budgets are too small (USD 30–750K) for platform-level engagement. These institutions buy bundled identity from their core banking vendor. Address through partner/channel strategy only.

## 9. Risks and Gaps

**What must be true for the opportunity to materialize:**

- Banks must continue prioritizing vendor consolidation in identity. If procurement stays siloed (CISO buys authentication, compliance buys consent, fraud team buys analytics), the converged platform value proposition weakens.
- The EU AI Act high-risk obligations must take effect as scheduled (August 2026). Delays reduce the urgency for agent identity governance.
- Trust Fabric's architectural scope must translate to production-ready capabilities in each domain. An architecture document is not a shipping product.

**Window risks:**

- **PE-assembled convergence.** Thoma Bravo (Ping + ForgeRock), or a similar PE play, could achieve genuine integration and close the convergence gap before Zeta establishes a beachhead. The distinction between "loosely bundled" and "architecturally converged" must be demonstrable, not claimed.
- **Microsoft Entra expansion.** If Microsoft invests seriously in Entra External ID (CIAM) and Entra Workload ID (agent identity), bundled pricing and M365 distribution could suppress the addressable market for standalone trust platforms.
- **LexisNexis + IDV + CIAM.** LexisNexis's IDVerse acquisition signals upstream expansion. If LexisNexis adds CIAM and consent, its data moat and banking relationships make it formidable.

**Capability gaps requiring investment:**

- Identity verification: build minimum viable document verification or formalize integration partnerships with Socure, iProov, or Jumio.
- eIDAS 2.0 wallet: begin EU Digital Identity Wallet pilot participation to demonstrate credential verification capability before the December 2027 mandate.
- Aadhaar integration: invest in UIDAI certification and V-CIP infrastructure for India market entry.
- Go-to-market: build a sales motion that reaches CISOs and identity architects, not only CIOs and platform buyers.

## 10. Recommended Actions

**Near-term (0–2 years):**

1. **Ship AI agent identity governance as the first general-availability capability.** The EU AI Act August 2026 deadline creates a hard buying window. No competitor has production-grade agent identity for banking. Trust Fabric + Seer's delegation model, human accountability chain, and Cognitive Audit Fabric's decision auditability directly address Articles 16/26. Target: EU-operating Tier 1–2 banks preparing for high-risk AI compliance.

2. **Establish 2–3 Tier 2 US bank deployments** of Trust Fabric's unified CIAM + consent + authentication layer. Focus on banks actively consolidating identity vendors (89 percent desire consolidation). Demonstrate measurable vendor count reduction and compliance cost reduction. Named targets: banks in the USD 10–100 billion range that have recently adopted point solutions (similar profiles to IncredibleBank, Heritage Bank) and face the 20-state privacy patchwork compliance burden.

3. **Formalize IDV integration partnerships.** Sign integration agreements with Socure (US banking IDV leader) and iProov (biometric liveness specialist) so that Trust Fabric orchestrates identity verification signals without competing in a sub-segment where data moats are unassailable.

**Medium-term (2–5 years):**

4. **Expand to Tier 1 US and EU banks** on the basis of proven Tier 2 deployments. Lead with the AI agent identity governance capability — Tier 1 banks deploying hundreds of AI agents across credit, compliance, and servicing domains will need agent identity infrastructure at scale.

5. **Build India market readiness** — UIDAI certification, V-CIP integration, Account Aggregator connectivity, and DPDP consent manager compliance. India's identity infrastructure is publicly operated (Aadhaar), which means the entry barrier is regulatory certification, not market competition.

6. **Participate in EU Digital Identity Wallet pilots** to establish credential verification and wallet-based authentication capability before the December 2027 bank acceptance mandate.
