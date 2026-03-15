# Digital Identity and Trust — Research Synthesis Notes
**Date:** March 2026  
**Engagement Area:** Digital Identity and Trust

---

## Evidence Quality Summary

| # | Structural Shift | Rating | Key Data Points |
|---|---|---|---|
| 1 | **Regulatory convergence** | Strong | BPI survey (40% IT compliance budget growth, 75% C-Suite time increase); Sumsub (51% cite regulations as top challenge); Omega Systems (54% use spreadsheets); KYC-Chain (15–20 regulations for cross-border bank); AML spending $2.9B (+12% YoY) |
| 2 | **Digital-first identity** | Strong | US branch closure −14.8% (86,469→73,649); Aadhaar 27.07B transactions FY24-25; mobile banking 2.17B users globally; India eKYC 23.56B cumulative |
| 3 | **Passwordless authentication** | Strong | FIDO Alliance: 93% eligible, 36% enrolled, 26% sign-in share; 87% enterprise deployment; 81% helpdesk reduction; 93% success vs 63% legacy |
| 4 | **Synthetic identity fraud** | Strong | Fed Reserve (fastest-growing crime); FTC $12.5B; Javelin $47B ($27B identity + $20B scams); FinCEN advisory; iProov deepfake data (704% face swap growth) |
| 5 | **Privacy-by-design** | Strong | €7.1B GDPR cumulative fines; 443 breach notifications/day (+22% YoY); DPDP Act phased timeline; 20-state US patchwork |
| 6 | **Identity convergence** | Strong | $17.5B+ M&A (Okta/Auth0 $6.5B, Thoma Bravo deals, Entrust/Onfido, Permira/BioCatch); 89% vendor consolidation desire (Thales); PE assembling portfolios |
| 7 | **AI agent identity** | Strong | CSA survey: only 18% confident IAM handles agents; 95% run agents autonomously; EU AI Act Aug 2026 deadline; CyberArk machine identity 82–87:1 ratio |
| 8 | **Bank-as-identity-provider** | Strong | ConnectID 10M+ users (Big Four Australia); Interac 141M interactions (Canada); eIDAS 2.0 Dec 2027 mandate |

---

## Cross-Reference Findings

### Market Sizing Consistency (Stream 1)
- CIAM: MarketsandMarkets $14.12B (2025) vs Mordor $11.3B — definitional scope differs; both converge on 9.7–17.7% CAGR
- Identity verification: MarketsandMarkets $14.34B and Juniper $15.2B (2024) within ~10% — high consistency
- Banking TAM: $29.7–34.8B (2025) → $57.3–68.6B (2030) across six sub-segments; BFSI 28–36% share across categories

### Regulatory-Competitive Alignment (Streams 2 and 3)
- eIDAS 2.0 (Dec 2027) and EU AI Act (Aug 2026) create hard deadlines; competitive landscape shows no vendor spanning all six sub-domains
- NIST 800-63-4 (Jul 2025) deepfake controls align with vendor moves (Onfido/Entrust, iProov, Socure) into liveness and injection-attack detection
- PSD2 SCA and FFIEC MFA guidance drive authentication vendor demand; FIDO Alliance data confirms 87% enterprise passkey deployment

### Fraud-Identity Convergence (Streams 3 and 6)
- Gartner: 50% of large FIs will consolidate fraud/cyber/identity teams by 2031 (from <5% today)
- Vendor M&A: LexisNexis (IDVerse), Socure (Effectiv), Experian (AtData) — all expanding from analytics/IDV into integrated identity+fraud
- BioCatch >$185M ARR, 3 of 4 largest US banks; Socure Sigma v4 positions as first fully integrated IDV + fraud platform
- 76% of fraud occurs after KYC onboarding (Sumsub) — supports continuous identity thesis

### AI Agent Identity Gap (Streams 3 and 5)
- CSA/Strata: 18% confident, 21% real-time agent inventory, 28% can trace to human sponsor
- Microsoft Entra Agent ID only shipping product treating agents as first-class identities; in preview
- CyberArk + Venafi, IBM + HashiCorp address machine identity (certs, secrets) but not agent delegation/accountability
- EU AI Act Articles 12, 14, 26 create implicit identity infrastructure requirements (traceability, human oversight, 6-month logs)

---

## Target Universe Assembly

### USA — Tier 1
| Institution | Evidence | Source |
|---|---|---|
| JPMorgan Chase | Passkeys, anti-deepfake facial auth, Jumio biometric verification, face/palm payments, $18B tech budget, LLM Suite, fraud-proofing kiosks, white paper on repurposable digital identities | MobileIDWorld, American Banker, CNBC, Biometric Update |
| Wells Fargo | Passkeys for consumer/commercial; biometric (Face ID, Touch ID); Transmit Security partner; AI to 180K+ desktops; BioCatch (2025) | Wells Fargo, Transmit Security, AInvest |
| Bank of America | QR sign-in 60% YoY surge on CashPro; Push Authentication; eliminating physical tokens | BofA Newsroom |
| Citi | FIDO Alliance commercial deployment member | FIDO Alliance |

### USA — Tier 2/3
| Institution | Evidence | Source |
|---|---|---|
| TD Bank | CIAM modernization with Deloitte; Backbase for retail card; identity-proofing, real-time fraud alerts | Deloitte, Fintech Futures |
| IncredibleBank | Alloy identity + fraud — 90% account openings automated | Alloy |
| Heritage Bank | Persona KYC/AML — 2.4× faster application | Persona |
| WyHy Federal Credit Union | Illuma Shield voice authentication | Illuma |

### EU/UK — Tier 1
| Institution | Evidence | Source |
|---|---|---|
| BNP Paribas | Encompass financing for corporate digital identity; "One KYC" global platform; passkey login 6× support cost reduction; Ping Identity | Biometric Update, Secfense |
| Standard Chartered | Ping Identity centralized platform; 30 retail markets; Mox Bank launch | Ping Identity |
| NatWest | OneID bank-verified digital identity; BioCatch since 2016; Nordic structured finance | NatWest, BioCatch |
| HSBC | Consents.online for Open Banking; ValidiFI for synthetic identity/mule detection | Finextra |
| Deutsche Bank | Privacy-by-Design Retail Data Platform with Google Cloud; digital identity white paper (Polygon Labs) | Google Cloud, Deutsche Bank Flow |

### Asia-Pacific — Tier 1
| Institution | Evidence | Source |
|---|---|---|
| DBS Bank | SingPass Face Verification; 20-minute SME onboarding; digital token security | DBS Newsroom |
| OCBC | SingPass Face Verification; OneTouch/OneLook biometric; voice biometrics | OCBC, The Paypers |
| UOB | SingPass Face Verification; OTP phase-out | Business Times |
| NAB / Ubank | Passkeys rolled out; plans to phase out passwords in 5 years | NAB News |
| CBA, ANZ, Westpac | ConnectID participants; 10M+ customers | ConnectID |

### Canada — Tier 1
| Institution | Evidence | Source |
|---|---|---|
| BMO, CIBC, Desjardins, RBC, Scotiabank, TD | Interac Verified; 141M interactions/year; reusable credentials (2025) | Interac |

### Other Geographies
| Institution | Evidence | Source |
|---|---|---|
| Chinabank (Philippines) | First PH bank FIDO2 passkeys; mandatory for all users | Chinabank |
| Revolut | Fourthline for multi-market KYC via competitive RFP | Biometric Update |
| UnionDigital Bank (Philippines) | iProov liveness for ATO/mule detection | BusinessWire |
| Raiffeisen Bank (Czech) | iProov biometric for 1.2M+ monthly mobile users | iProov |
| Askari Bank (Pakistan) | IBM Verify — 75% help desk reduction, 100% MFA | IBM |
| CIB Egypt | IBM Identity Governance for zero-trust | IBM |
| Security Bank (Philippines) | Ping Identity for CIAM | Ping Identity |
| Boost Bank (Malaysia) | PingOne AIC; passwordless facial onboarding | Ping Identity |

---

## Right to Play / Right to Win Mapping

### Right to Play

| Question | Answer | Evidence |
|---|---|---|
| **TAM sufficient?** | Yes. $29.7–34.8B (2025), growing 14–15% CAGR to $57.3–68.6B (2030) | s1 aggregated TAM; BFSI 28–36% share across sub-segments |
| **Banks spending?** | Yes. Compliance budgets up 40% (2016–2023); identity #2 IT priority (37% rank top-3 per Celent); 75% increasing fraud prevention budgets | BPI survey, Celent, Cornerstone Advisors |
| **"Converged trust layer" as category?** | Emerging. 89% want consolidation but don't buy as single category yet; ~4 vendors per identity stack; no vendor spans all 6 sub-domains | Thales 2025 BFSI Survey; s3 competitive analysis |
| **Regulatory runway?** | Yes. eIDAS 2.0 Dec 2027; EU AI Act Aug 2026; DPDP May 2027; NIST 800-63-4 Jul 2025; SMS OTP elimination mandates (UAE Mar, India Apr, Philippines Jun 2026) | s2, s4 regulatory timelines |

### Right to Win

| Dimension | Assessment | Evidence |
|---|---|---|
| **Trust Fabric convergence** | Potential architectural advantage. No competitor spans all 6 sub-domains (CIAM, IDV, auth, consent, fraud analytics, NHI). Ping and LexisNexis each cover 2–3. | s3 vendor coverage heat map |
| **AI agent identity** | Emerging category with no dominant player. Microsoft Entra Agent ID in preview; CyberArk/HashiCorp address machine identity, not agent delegation. Zeta's Trust Fabric + Seer combination is differentiated. | s5 vendor landscape |
| **Weaknesses to address** | IDV depth; behavioral biometrics; deepfake detection; identity buying center go-to-market. Banks currently buy from 4+ vendors; convergence thesis requires orchestration or platform narrative. | s3 gaps; s6 fraud-identity bridge |

---

## Editorial Decisions

| Decision | Rationale |
|---|---|
| **All 8 shifts included** | All have Strong evidence quality per s4 Evidence Quality Summary |
| **Geographic scope** | USA, India, EU/UK — EU strongest regulatory driver (eIDAS 2.0, EU AI Act, GDPR) |
| **Part I vocabulary** | Use "trust layer" consistently; avoid alternating with "identity platform" or "CIAM solution" |
| **Part I framing** | Do not reference "converged trust platform" as product — frame as architectural observation (banks face compound regulatory + fraud + identity pressure; no vendor spans the full stack) |
| **Synthetic identity figure** | Use $35B (FiVerity/Fed Reserve Boston) with caveat that it is an estimate; Fed has not published official figure |
| **Bank-as-identity-provider** | Lead with ConnectID and Interac Verified as proven models; eIDAS 2.0 as regulatory mandate |
