# Gap-Fill Research: India Cloud Governance for Banking

**Research date:** 2026-03-15
**Gap area:** India-specific cloud operations data — regulatory framework, bank adoption evidence, infrastructure market, operational challenges, market sizing
**Status:** Complete — material improvement over synthesis baseline

---

## Key Findings

### RBI Regulatory Framework

- **RBI has no single "cloud adoption framework" circular for banks.** Cloud governance is governed through a patchwork of directives: ITGRCA (Nov 2023, effective Apr 2024), Master Direction on Outsourcing of IT Services (Apr 2023, effective Oct 2023), data localization circulars (2018), and the updated Operational Resilience Guidance Note (Apr 2024). Banks must synthesize requirements across these instruments.
- **Cloud computing is explicitly recognized as outsourceable IT service** under the 2023 Master Direction, with "material outsourcing" classification triggered if disruption could significantly impact business operations or customer data.
- **Data localization is actively enforced.** RBI restricted American Express and Diners Club from onboarding domestic customers (May 2021–Aug 2022) for violating the 2018 data storage mandate. As of mid-2024, foreign banks were still seeking reprieve for legacy data stored overseas.
- **RBI is building sovereign cloud infrastructure.** The Indian Financial Services (IFS) Cloud, developed by IFTAS (RBI subsidiary), entered pilot in 2025, funded by RBI's $2.72B asset development fund. It is designed for small and mid-sized institutions, using local IT firms rather than hyperscalers.
- **CERT-In imposes a 6-hour incident reporting mandate** — significantly stricter than GDPR's 72 hours. Logs must be retained for 180 days within Indian jurisdiction. Non-compliance is a criminal offense (up to 1 year imprisonment or ₹1 lakh fine per instance).
- **RBI took enforcement action against Kotak Mahindra Bank (Apr 2024)** for IT infrastructure deficiencies — barring new digital customer onboarding and credit card issuance. This is the strongest signal that RBI actively penalizes technology operational failures, not just data residency violations.

### Indian Bank Cloud Adoption — Named Institutions

- **HDFC Bank:** Built multi-cloud active-active architecture in-house after 2019 DC outage. Migrated core banking system to next-gen platform (Jul 2024). 97% digital transaction rate. One of the most advanced cloud architectures among Indian banks.
- **ICICI Bank:** Operates 5,500+ APIs, 3,500+ consumed internally, on microservices-based cloud infrastructure. Zero-trust security from data centres to cloud. Observability platforms deployed across applications, infrastructure, and microservices.
- **SBI:** YONO 2.0 platform re-architecture (Dec 2024) for 200M users. TCS as principal technology partner. Building private cloud. Targeting core banking modernization by 2027 including Unix-to-Linux migration and microservices.
- **Kotak Mahindra Bank:** ₹1,700 Cr tech spend in FY25 (30%+ YoY increase). Cloud-native data platform (DEX). 12 LLM models via "Kotak AI." RBI restrictions forced accelerated clearing of tech debt.
- **Axis Bank:** Partnered with Red Hat OpenShift for cloud-agnostic microservices. 40% reduction in development effort. Plans to migrate 70–75% of customer-facing apps to cloud.
- **YES Bank:** ~₹1,000 Cr annual tech spend. IT budget grew 70.7% over FY22–FY24. Three-pillar cloud strategy (scalability, failure recovery, security standardization). Multi-cloud provider approach.
- **Bandhan Bank:** Core banking transformation on Oracle FLEXCUBE cloud platform (2024). 32M customers across 6,250+ outlets.
- **Jupiter (neobank):** Runs entirely on AWS. Cloud-native from inception, microservices architecture.
- **12 Public Sector Banks (via PSB Alliance):** AWS empanelled (Sep 2024) to provide community cloud services for SBI, PNB, Bank of Baroda, Union Bank, Canara Bank, and 7 others. Initial focus on non-core workloads.

### India Cloud Infrastructure Market

- **India public cloud services market:** $5.2B in H1 2024, projected $25.5B by 2028 (24.3% CAGR) per IDC.
- **BFSI share:** 24.03% of India's cloud market in 2025 — the single largest vertical.
- **AWS India:** Empanelled by PSB Alliance for 12 public sector banks. Delivered via managed service providers (Orient Technologies, Hitachi Systems). Focus on non-core workloads initially.
- **RBI IFS Cloud:** Pilot in 2025, aimed at small/mid-size financial institutions. Uses domestic IT infrastructure. Funded from RBI's $2.72B development fund. Positioned as sovereign alternative to hyperscalers.
- **NPCI/UPI infrastructure:** Currently on-premise with open-source stack (Java, Cassandra). Cloud-first migration being explored to support projected 2B daily transactions by 2030. Innovation cycle bottleneck: 12–18 months from NPCI circular to launch (target: 8–12 weeks with cloud).

### Operational Challenges — India-Specific

- **Regulatory patchwork:** No single cloud framework. Banks must comply with ITGRCA + Outsourcing Directions + data localization + CERT-In directives + operational resilience guidance — each with different scopes and timelines.
- **Enforcement is real:** Kotak Mahindra (IT infrastructure, 2024), American Express (data localization, 2021). RBI has demonstrated willingness to impose business-restricting penalties for technology failures.
- **Domestic IT dominance:** TCS (BaNCS Cloud), Wipro (Core Banking Managed Services, FullStride Cloud), Infosys (Finacle) are the primary cloud operations providers for Indian banks. The managed-services model is deeply entrenched.
- **Talent is abundant but channeled through IT services firms.** India's 170–175 BFSI GCCs employ ~300,000 people, but cloud operations talent flows primarily through TCS/Infosys/Wipro rather than direct bank employment.
- **Private cloud preference:** SBI is building private cloud. HDFC Bank built in-house. Tier 1 Indian banks show preference for controlled infrastructure over full public cloud adoption, partly driven by RBI data localization.

---

## Evidence Table

| # | Claim | Source | URL | Verified |
|---|-------|--------|-----|----------|
| 1 | RBI ITGRCA Master Direction issued Nov 2023, effective Apr 2024 | Mondaq / RBI | https://www.mondaq.com/india/it-and-internet/1445244/rbi-issues-master-directions-on-information-technology-governance-risk-controls-and-assurance-practices | Yes |
| 2 | RBI Master Direction on Outsourcing of IT Services, Apr 2023, effective Oct 2023 | RBI official | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562 | Yes |
| 3 | Cloud computing explicitly listed as outsourceable IT service category | TaxGuru analysis of RBI Direction | https://taxguru.in/rbi/summary-master-direction-outsourcing-information-technology-services.html | Yes |
| 4 | RBI data localization mandate issued Apr 2018 requiring payment data stored in India | RBI circular | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0 | Yes |
| 5 | American Express / Diners Club barred from new customer onboarding May 2021 for data localization violations; lifted Aug 2022 | MyLawRD / Digital Policy Alert | https://www.mylawrd.com/rbi-punishes-american-express-for-violating-data-localisation-guidelines/ | Yes |
| 6 | Foreign banks seeking reprieve on historical data stored overseas as of Aug 2024 | Economic Times | https://economictimes.indiatimes.com/industry/banking/finance/banking/at-rbis-door-for-reprieve-bunch-of-foreign-banks-want-ease-of-storing-data-ask-for-mandate-to-be-applied-prospectively-from-jan-2025/articleshow/112662958.cms | Yes |
| 7 | RBI IFS Cloud entering pilot 2025, developed by IFTAS, funded by $2.72B development fund | Reuters | https://www.reuters.com/business/finance/india-cenbank-plans-2025-launch-cloud-services-countering-dominance-global-firms-2024-11-18/ | Yes |
| 8 | IFS Cloud aims to serve small/mid-size institutions using local IT firms | Mondaq | https://www.mondaq.com/india/data-protection/1663284/building-compliance-in-the-cloud-rbis-ifs-cloud-and-the-future-of-financial-data-localization-under-dpdpa-2023 | Yes |
| 9 | CERT-In 6-hour incident reporting mandate under IT Act Section 70B | CERT-In official | https://cert-in.org.in/Directions70B.jsp | Yes |
| 10 | 180-day log retention within Indian jurisdiction; non-compliance up to 1yr imprisonment / ₹1 lakh fine | AMLegals analysis | https://amlegals.com/cert-in-compliance-guide-2025/ | Yes |
| 11 | RBI barred Kotak Mahindra Bank from digital onboarding + new credit cards, Apr 2024, for IT infrastructure deficiencies | Reuters | https://www.reuters.com/business/finance/indias-cenbank-takes-supervisory-action-against-kotak-mahindra-bank-2024-04-24/ | Yes |
| 12 | Kotak had CBS and digital channel outages over 2 years; assessed deficient in IT Risk & IS Governance for 2 consecutive years | Economic Times | https://m.economictimes.com/wealth/personal-finance-news/kotak-mahindra-bank-penalised-by-rbi-what-happened-on-april-15-that-was-the-final-straw/articleshow/109565395.cms | Yes |
| 13 | Kotak RBI restrictions lifted Feb 2025 after remediation; ₹1,700 Cr tech spend FY25, 30%+ YoY | TechCircle | https://www.techcircle.in/2025/09/11/how-kotak-mahindra-bank-ramped-up-its-digital-tech-adoption-in-fy25 | Yes |
| 14 | HDFC Bank multi-cloud active-active architecture, built in-house post-2019 outage | Aerospike blog | https://aerospike.com/blog/inside-hdfc-multi-cloud-architecture | Yes |
| 15 | HDFC Bank CBS migration to next-gen platform Jul 2024 | HDFC Bank press release | https://www.hdfcbank.com/personal/about-us/news-room/press-release/2024/q2/hdfc-bank-plans-migration-of-core-banking-system-to-new-engineered-platform-to-enhance-robustness-a | Yes |
| 16 | HDFC Bank 97% digital transaction rate | Aerospike blog | https://aerospike.com/blog/inside-hdfc-multi-cloud-architecture | Yes |
| 17 | ICICI Bank 5,500+ APIs, microservices-based cloud infrastructure, zero-trust, observability platforms | QA Financial | https://qa-financial.com/icici-bank-embraces-disciplined-testing-to-reinforce-digital-resilience/ | Yes |
| 18 | SBI YONO 2.0 re-architecture Dec 2024 for 200M users, TCS as partner | CIO Inc | https://www.cio.inc/sbis-big-migration-from-yono-to-yono-20-a-30437 | Yes |
| 19 | SBI targeting core banking modernization by 2027 including private cloud build | Business Standard | https://www.business-standard.com/finance/news/sbi-aiming-to-modernise-its-core-banking-infrastructure-in-next-2-years-125111301692_1.html | Yes |
| 20 | Axis Bank partnered with Red Hat OpenShift, 40% dev effort reduction, 70–75% cloud migration target | Asian Banker | https://www.theasianbanker.com/updates-and-articles/axis-bank-transitions-to-microservices-and-multi-cloud-technology-to-be-future-ready | Yes |
| 21 | YES Bank IT budget grew 70.7% FY22–FY24, ~₹1,000 Cr annual tech spend | TechCircle / MoneyControl | https://www.techcircle.in/2024/09/09/spend-it-yes-bank-s-it-budget-buoyed-70-in-fy24/ | Yes |
| 22 | YES Bank three-pillar cloud strategy: scalability, failure recovery, security | ET CIO | https://cio.economictimes.indiatimes.com/news/cloud-computing/a-look-at-yes-banks-three-pillars-of-cloud-strategy/87597288 | Yes |
| 23 | Bandhan Bank core banking transformation on Oracle FLEXCUBE cloud platform, 32M customers | Silicon India | https://www.siliconindia.com/news/general/bandhan-bank-transforms-its-core-banking-and-expands-digital-services-with-oracle-nid-228037-cid-1.html | Yes |
| 24 | Jupiter neobank runs entirely on AWS, microservices architecture | ET CIO | https://cio.economictimes.indiatimes.com/news/cloud-computing/explained-how-neobank-jupiter-is-using-cloud-tech-to-disrupt-fintech/90353416 | Yes |
| 25 | PSB Alliance (12 public sector banks) empanelled AWS Sep 2024 via MSPs Orient Technologies & Hitachi Systems | Amazon press release | https://press.aboutamazon.com/in/2024/9/psb-alliance-empanels-aws-to-drive-digital-transformation-for-indias-public-sector-banks | Yes |
| 26 | India public cloud services market $5.2B in H1 2024, projected $25.5B by 2028 at 24.3% CAGR | IDC | https://www.idc.com/getdoc.jsp?containerId=prAP52965924 | Yes |
| 27 | BFSI holds 24.03% share of India cloud market in 2025 | IMARC Group | https://www.imarcgroup.com/india-cloud-computing-market | Yes |
| 28 | India IT spending projected at $176.3B in 2026 (10.6% growth) | Business Standard / Gartner | https://www.business-standard.com/industry/news/india-it-spending-gartner-2026-forecast-125111801086_1.html | Yes |
| 29 | IDRBT Centre for Emerging Networks and Cloud Computing established | IDRBT official | https://www.idrbt.ac.in/ | Yes |
| 30 | IDRBT published Cloud Security Framework (2013) and Cloud FAQ for banking | IDRBT Best Practices | https://www.idrbt.ac.in/best-practices/ | Yes |
| 31 | RBI Operational Resilience Guidance Note updated Apr 2024, aligned with BCBS principles | Hindu Business Line | https://www.thehindubusinessline.com/money-and-banking/rbi-releases-updated-guidance-note-on-operational-risk-management-and-operational-resilience-for-lenders/article68125901.ece | Yes |
| 32 | TCS BaNCS Cloud SaaS offering for banking | TCS official | https://www.tcs.com/content/tcs/global/en/what-we-do/products-platforms/tcs-bancs/solution/cloud | Yes |
| 33 | Wipro recognized as Horizon 3 Market Leader by HFS Research for banking services | HFS Research | https://www.hfsresearch.com/research/wipro-service-capabilities-for-commercial-banks-2025/ | Yes |
| 34 | India hosts 170–175 BFSI GCCs employing ~300,000 people | NASSCOM | https://www.nasscom.in/knowledge-center/publications/bfsi-gccs-road-ahead | Yes |
| 35 | NPCI UPI current on-prem infrastructure, 12–18 month innovation cycle | Razorpay blog | https://razorpay.com/blog/powering-the-future-of-upi-with-cloud-first-upi-infrastructure | Yes |
| 36 | Kotak cloud-native data platform DEX, "Kotak AI" with 12 LLMs | TechCircle | https://www.techcircle.in/2025/09/11/how-kotak-mahindra-bank-ramped-up-its-digital-tech-adoption-in-fy25 | Yes |
| 37 | RBI 2024 Master Directions on Cyber Resilience for payment system operators, implementation from Apr 2025 | KPMG analysis | https://assets.kpmg.com/content/dam/kpmgsites/in/pdf/2024/10/securing-non-bank-psos-rbis-guidelines-on-cyber-resilience-and-digital-payment-security-controls.pdf | Yes |

---

## Gaps That Remain Unfilled

| Gap | Notes |
|-----|-------|
| **RBI circular specifically titled "Cloud Computing Framework for Banks"** | No such standalone circular exists. Cloud governance is distributed across ITGRCA, Outsourcing Directions, data localization circulars, and operational resilience guidance. This is itself a finding — the regulatory framework is fragmented. |
| **RBI IFS Cloud post-pilot status (2026)** | Reuters reported pilot planned for 2025. No public reporting on post-pilot status, actual adoption by financial institutions, or service capabilities as of Mar 2026. [unverified — needs manual confirmation] |
| **Azure and GCP India banking deployments** | No specific public disclosures found for Azure or GCP banking customers in India. AWS has the only documented banking-sector partnership (PSB Alliance). Microsoft and Google likely serve Indian banks but deployments are not publicly documented at the customer level. |
| **SEBI Cybersecurity Framework** — cloud-specific provisions | Exists but research did not surface cloud-specific provisions. Applies to market intermediaries, not banks directly. Lower priority for this gap-fill. |
| **Federal Bank, IDFC First Bank** — specific cloud modernization programs | IDFC First Bank references "latest technology stack" as a strength but no specific cloud modernization program disclosed. Federal Bank — no cloud-specific signals found. |
| **Fi, Niyo neobanks** — cloud infrastructure specifics | No public disclosures found on cloud stack. Likely AWS or GCP based on India neobank patterns, but unverifiable. |
| **Cloud operations talent market sizing for India** | NASSCOM reports 300K BFSI GCC employees but does not segment by cloud operations vs. other tech functions. No specific data on SRE/cloud operations headcount in Indian banks. |
| **India banking-specific cloud spending as % of total IT budget** | No disaggregated figure found. BFSI is 24% of India cloud market ($5.2B H1 2024), implying ~$1.25B H1 2024, but this includes insurance, capital markets, NBFCs — not banking alone. |

---

## Assessment: Is India a "Material Accessible Market" for Cloud Operations?

### Verdict: Material market, but primarily a managed-services market with regulatory-driven opportunity for platform vendors.

**Arguments for "material accessible market":**

1. **Scale is real.** India's public cloud market is $10B+ annually (2024 run-rate), with BFSI at ~24% ($2.4B+). Projected to $25.5B by 2028. Even at conservative banking-only estimates (60% of BFSI), this represents $1.4B+ in cloud spending by Indian banks.
2. **Regulatory pressure is escalating.** RBI's 2024 enforcement against Kotak Mahindra Bank demonstrated willingness to impose business-restricting penalties for IT infrastructure failures. ITGRCA + Outsourcing Directions + Operational Resilience Guidance create compliance demand for cloud governance tooling.
3. **Major banks are actively modernizing.** HDFC Bank (multi-cloud active-active), ICICI (microservices + observability platforms), Axis Bank (Red Hat OpenShift, 70–75% cloud target), Kotak (₹1,700 Cr tech spend post-RBI action) — all represent active cloud transformation programs with demonstrated need for operational tooling.
4. **Public sector banks entering cloud.** PSB Alliance's AWS empanelment (Sep 2024) for 12 banks signals that even conservative public sector banks are moving to cloud, creating a new tier of demand.
5. **Data localization creates architectural need.** RBI's strict data residency requirements create genuine need for cloud governance platforms that enforce data sovereignty at the infrastructure level — a capability gap in horizontal tools.

**Arguments for "managed-services market dominated by domestic IT firms":**

1. **TCS, Infosys, Wipro, HCL control the engagement model.** Indian banks overwhelmingly outsource technology operations to domestic IT services firms. Cloud "adoption" in Indian banking is mediated through managed services contracts, not direct platform purchases by bank engineering teams.
2. **SBI's principal tech partner is TCS.** HDFC Bank built in-house. The pattern is either (a) outsource to TCS/Infosys or (b) build internally — neither pattern creates a natural market for third-party platform vendors.
3. **Private cloud preference among Tier 1 banks.** SBI is building private cloud. HDFC Bank built in-house. RBI's IFS Cloud is a sovereign alternative. The market for public cloud platform tooling may be smaller than headline numbers suggest.
4. **RBI's IFS Cloud could disintermediate hyperscalers for smaller institutions.** If successful, the sovereign cloud initiative would channel small/mid-size bank cloud adoption through RBI infrastructure rather than commercial platforms.
5. **PSB Alliance AWS deal is through MSPs (Orient Technologies, Hitachi Systems).** Even public sector cloud adoption is being mediated through managed service providers, not direct platform relationships.

### Net assessment for the opportunity analysis:

India is a **Tier 2 market** for cloud operations platform vendors — significant scale, genuine regulatory drivers, and named bank modernization activity, but the engagement model is primarily managed services. The opportunity for a platform vendor like Zeta is:

- **Strongest** where Zeta already has banking platform deployments in India and Cloud Fabric is used to operate those platforms (operational uplift sale to existing customers).
- **Moderate** for Indian banks seeking multi-cloud governance and data sovereignty tooling to meet RBI requirements — but these banks will likely procure through TCS/Infosys/Wipro intermediation.
- **Weakest** for general cloud operations tooling sold directly to Indian bank IT teams — the managed-services model is too entrenched.

---

## Named Banks with Cloud Modernization Signals — Target Universe Additions

| Bank | Tier | Signal | Source |
|------|------|--------|--------|
| HDFC Bank | Tier 1 | Multi-cloud active-active architecture, CBS migration to next-gen platform (Jul 2024) | [Aerospike](https://aerospike.com/blog/inside-hdfc-multi-cloud-architecture), [HDFC Bank](https://www.hdfcbank.com/personal/about-us/news-room/press-release/2024/q2/hdfc-bank-plans-migration-of-core-banking-system-to-new-engineered-platform-to-enhance-robustness-a) |
| ICICI Bank | Tier 1 | 5,500+ APIs, microservices cloud infrastructure, zero-trust, observability platforms deployed | [QA Financial](https://qa-financial.com/icici-bank-embraces-disciplined-testing-to-reinforce-digital-resilience/) |
| SBI | Tier 1 | YONO 2.0 for 200M users, private cloud build, core modernization by 2027 | [CIO Inc](https://www.cio.inc/sbis-big-migration-from-yono-to-yono-20-a-30437), [Business Standard](https://www.business-standard.com/finance/news/sbi-aiming-to-modernise-its-core-banking-infrastructure-in-next-2-years-125111301692_1.html) |
| Kotak Mahindra Bank | Tier 1 | ₹1,700 Cr tech spend FY25, cloud-native DEX platform, post-RBI-enforcement tech overhaul | [TechCircle](https://www.techcircle.in/2025/09/11/how-kotak-mahindra-bank-ramped-up-its-digital-tech-adoption-in-fy25) |
| Axis Bank | Tier 1 | Red Hat OpenShift, microservices, 70–75% cloud migration target, cloud-agnostic architecture | [Asian Banker](https://www.theasianbanker.com/updates-and-articles/axis-bank-transitions-to-microservices-and-multi-cloud-technology-to-be-future-ready) |
| YES Bank | Tier 2 | ₹1,000 Cr annual tech spend, 70.7% IT budget growth FY22–24, three-pillar cloud strategy | [TechCircle](https://www.techcircle.in/2024/09/09/spend-it-yes-bank-s-it-budget-buoyed-70-in-fy24/), [ET CIO](https://cio.economictimes.indiatimes.com/news/cloud-computing/a-look-at-yes-banks-three-pillars-of-cloud-strategy/87597288) |
| Bandhan Bank | Tier 3 | Core banking transformation on Oracle FLEXCUBE cloud platform (2024) | [Silicon India](https://www.siliconindia.com/news/general/bandhan-bank-transforms-its-core-banking-and-expands-digital-services-with-oracle-nid-228037-cid-1.html) |
| PSB Alliance (12 banks) | Tier 1–2 | AWS empanelment Sep 2024 for community cloud services via MSPs | [Amazon Press](https://press.aboutamazon.com/in/2024/9/psb-alliance-empanels-aws-to-drive-digital-transformation-for-indias-public-sector-banks) |
| Jupiter (neobank) | Neobank | Fully AWS cloud-native, microservices architecture | [ET CIO](https://cio.economictimes.indiatimes.com/news/cloud-computing/explained-how-neobank-jupiter-is-using-cloud-tech-to-disrupt-fintech/90353416) |

---

## Regulatory Framework Summary

| Regulation / Directive | Issuer | Cloud Relevance | Effective Date | Key Requirement |
|------------------------|--------|-----------------|----------------|-----------------|
| ITGRCA Master Direction | RBI | IT governance, risk management, BCP/DR for all regulated entities | Apr 2024 | Board-level IT Strategy Committee, quarterly reviews, IS audit |
| Master Direction on Outsourcing of IT Services | RBI | Cloud explicitly listed as outsourceable service; material outsourcing classification | Oct 2023 | Board oversight, due diligence on providers, RBI supervision not impeded |
| Data Localization Circular | RBI | All payment system data must be stored in India | 2018 | Domestic storage only; Board-approved CERT-In audit required |
| Operational Resilience Guidance Note | RBI | BCP/DR, three lines of defense, impact tolerance metrics (RTO, RPO, SLA) | Apr 2024 | Aligned with BCBS principles; maps critical operations and dependencies |
| Cyber Resilience Master Directions (PSOs) | RBI | Cloud security as baseline IS control for payment operators | Apr 2025 | Cloud-specific security measures for payment system operators |
| CERT-In Directions (Section 70B IT Act) | CERT-In | 6-hour incident reporting, 180-day log retention in India | Apr 2022 | Criminal penalties for non-compliance; cloud platform compromises reportable |
| DPDP Act 2023 | Govt of India | Personal data processing and cross-border transfer provisions | In force | Cross-border data transfer framework intersects with RBI localization |

---

## India-Specific Cloud Governance: Key Structural Differences from USA/EU

| Dimension | USA | EU | India |
|-----------|-----|-----|-------|
| Primary cloud regulation | FFIEC guidance, OCC heightened standards | DORA (Jan 2025) | Patchwork: ITGRCA + Outsourcing Directions + data localization + CERT-In |
| Data localization | No blanket requirement | GDPR restricts cross-border transfers | Strict: all payment data must reside in India |
| Enforcement posture | Examination-driven, consent orders | DORA penalties regime | Active enforcement: Kotak (2024), AmEx (2021) |
| Cloud provider landscape | AWS/Azure/GCP compete directly | AWS/Azure/GCP with EU sovereignty overlays | Hyperscalers + RBI sovereign cloud (IFS Cloud) |
| Bank cloud engagement model | Mix of direct platform + managed services | Mix, with SI intermediation | Overwhelmingly managed services via TCS/Infosys/Wipro |
| Incident reporting | Varies by agency | DORA: within 4 hours (initial) | CERT-In: 6 hours from discovery |
| Sovereign cloud initiative | None | EU: Gaia-X (infrastructure), various national efforts | RBI IFS Cloud (IFTAS) — pilot 2025 |
