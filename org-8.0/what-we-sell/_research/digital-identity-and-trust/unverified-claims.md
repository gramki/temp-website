# Digital Identity and Trust — Unverified Claims Register
**Date:** March 2026  
**Engagement Area:** Digital Identity and Trust

Items flagged as `[unverified — needs manual confirmation]` or equivalent across all six research streams. For each: claim, stream, attempted source, verification gap, and whether needed for final document.

---

## Stream 1: Market Sizing and Structure

### 1. Build-vs-buy ratios by bank tier

| Field | Value |
|---|---|
| **Claim** | Tier 1: 70:30 → 40:60 (build:buy); Tier 2: 85%+ buy; Tier 3: almost exclusively buy |
| **Stream** | s1-market-sizing.md |
| **Attempted source** | Analyst commentary, industry interviews |
| **Why unverified** | No single published source provides these breakdowns by bank tier |
| **Needed for final doc?** | **Can drop.** Directional context only; TAM and spending data do not depend on it. |

---

### 2. Bank tier revenue pools (identity/security spend by asset tier)

| Field | Value |
|---|---|
| **Claim** | Tier 1: $15–350M identity spend; Tier 2: $600K–12M; Tier 3: $30K–750K |
| **Stream** | s1-market-sizing.md |
| **Attempted source** | Deloitte cybersecurity benchmarks, Celent IT spending data, public bank filings |
| **Why unverified** | No single source provides identity/security vendor spend broken down by bank asset tier |
| **Needed for final doc?** | **Can drop.** Aggregated TAM ($29.7–34.8B) is sufficient; tier-level precision is nice-to-have. |

---

### 3. India CIAM-specific market data

| Field | Value |
|---|---|
| **Claim** | India CIAM platform market for banks specifically — not broken out in available research |
| **Stream** | s1-market-sizing.md |
| **Attempted source** | IMARC (India eKYC, India IDV), Mordor Intelligence |
| **Why unverified** | eKYC/IDV data exists (Aadhaar-driven); CIAM platform market for Indian banks is not isolated |
| **Needed for final doc?** | **Can drop.** India eKYC and IDV data ($494M→$1.7B) is sufficient for India narrative. |

---

### 4. BFSI share of consent management market

| Field | Value |
|---|---|
| **Claim** | BFSI share estimated at 15–20% of ~$1.1B consent management market; banking CMP TAM ~$150–250M |
| **Stream** | s1-market-sizing.md |
| **Attempted source** | TechSci Research, Business Research Insights (market totals) |
| **Why unverified** | No published report isolates BFSI share of consent management platform market |
| **Needed for final doc?** | **Can drop.** Consent is smallest sub-segment; total market size is sufficient. |

---

## Stream 2: Regulatory Landscape

### 5. FinCEN BOI reporting status

| Field | Value |
|---|---|
| **Claim** | Corporate Transparency Act BOI reporting requirements face court injunctions (2024–2025); status in flux as of March 2026 |
| **Stream** | s2-regulatory-landscape.md |
| **Attempted source** | FinCEN CDD Final Rule, Federal Register |
| **Why unverified** | Multiple court injunctions; current enforcement status requires manual confirmation from FinCEN or legal counsel |
| **Needed for final doc?** | **Optional.** CDD Rule and KYC obligations remain; BOI status affects beneficial ownership workflows. Include with "status in flux" caveat if retained. |

---

### 6. GLBA Safeguards Rule MFA technical specification

| Field | Value |
|---|---|
| **Claim** | 2021 amendments mandate MFA; exact technical specification (FIDO2, SMS OTP, etc.) and scope for banks vs. non-bank FIs unclear |
| **Stream** | s2-regulatory-landscape.md |
| **Attempted source** | FTC Safeguards Rule, 16 CFR Part 314 |
| **Why unverified** | Rule mandates MFA but does not prescribe technology; banks covered by OCC/FDIC/Fed Interagency Guidelines, not FTC — scope overlap needs verification |
| **Needed for final doc?** | **Can drop.** FFIEC guidance and NIST 800-63-4 provide sufficient MFA/passwordless narrative. |

---

## Stream 3: Competitive Landscape

### 7. Au10tix revenue

| Field | Value |
|---|---|
| **Claim** | Revenue not publicly disclosed |
| **Stream** | s3-competitive-landscape.md |
| **Attempted source** | None — private company |
| **Why unverified** | No public financials; would require analyst briefings or confidential disclosure |
| **Needed for final doc?** | **Can drop.** Au10tix is a point solution; competitive analysis does not depend on its revenue. |

---

### 8. Sumsub revenue

| Field | Value |
|---|---|
| **Claim** | Revenue not publicly disclosed |
| **Stream** | s3-competitive-landscape.md |
| **Attempted source** | None — private company |
| **Why unverified** | No public financials |
| **Needed for final doc?** | **Can drop.** Sumsub is one of many IDV vendors; revenue opacity noted in gaps. |

---

### 9. IDnow revenue

| Field | Value |
|---|---|
| **Claim** | Revenue not publicly disclosed |
| **Stream** | s3-competitive-landscape.md |
| **Attempted source** | None — private company |
| **Why unverified** | No public financials |
| **Needed for final doc?** | **Can drop.** EU IDV specialist; EU narrative does not depend on IDnow revenue. |

---

### 10. Transmit Security revenue

| Field | Value |
|---|---|
| **Claim** | Revenue not disclosed despite $543M funding |
| **Stream** | s3-competitive-landscape.md |
| **Attempted source** | Case studies, Gartner MQ |
| **Why unverified** | Private company; no public financials |
| **Needed for final doc?** | **Can drop.** Case studies (200M customers passwordless, Wells Fargo, TIAA) provide sufficient evidence. |

---

### 11. TransUnion identity segment revenue

| Field | Value |
|---|---|
| **Claim** | $4.2B total revenue (est. 2024); identity + fraud segment not separately disclosed |
| **Stream** | s3-competitive-landscape.md |
| **Attempted source** | TransUnion investor relations, annual reports |
| **Why unverified** | Identity/fraud revenue not broken out; TruValidate banking penetration vs. bureau services unclear |
| **Needed for final doc?** | **Can drop.** TransUnion's bureau presence and TruValidate platform are documented; revenue split is not critical. |

---

### 12. Temenos revenue

| Field | Value |
|---|---|
| **Claim** | ~$1B estimated annual revenue; identity is a module |
| **Stream** | s3-competitive-landscape.md |
| **Attempted source** | None cited |
| **Why unverified** | Temenos does not separately disclose identity module revenue; estimate is industry convention |
| **Needed for final doc?** | **Can drop.** Banking platform vendors (Temenos, FIS, Fiserv) are noted as bundled identity; precise revenue not required. |

---

### 13. FIS / Fiserv identity module details

| Field | Value |
|---|---|
| **Claim** | FIS ~$9.5B; Fiserv ~$19.5B total revenue; identity/CIAM portion not separately disclosed; identity is commodity module |
| **Stream** | s3-competitive-landscape.md |
| **Attempted source** | None cited for identity-specific capabilities |
| **Why unverified** | Core banking revenue is public; identity module capabilities and differentiation are poorly documented |
| **Needed for final doc?** | **Can drop.** "Identity as commodity module" is sufficient; product-level comparison would require vendor briefings. |

---

## Stream 4: Structural Shifts

### 14. Unified vs. per-regulation compliance cost differential

| Field | Value |
|---|---|
| **Claim** | No analyst has published rigorous comparison of per-regulation compliance project cost vs. unified infrastructure |
| **Stream** | s4-structural-shifts.md |
| **Attempted source** | None found |
| **Why unverified** | Would be a powerful data point but does not exist in published form |
| **Needed for final doc?** | **Can drop.** Regulatory convergence and budget growth (40%, 75% C-Suite time) provide sufficient evidence. |

---

### 15. DSAR volume and cost per institution (banking-specific)

| Field | Value |
|---|---|
| **Claim** | GDPR breach notifications 443/day; DSAR volumes and processing costs ($1,500–$5,000/request in some industries) not sourced for banking |
| **Stream** | s4-structural-shifts.md |
| **Attempted source** | DLA Piper (breach notifications); industry estimates for DSAR cost |
| **Why unverified** | Banking-specific DSAR volume and cost not independently sourced |
| **Needed for final doc?** | **Can drop.** GDPR fines and breach notification volume are sufficient for privacy-by-design narrative. |

---

### 16. Password reset helpdesk cost (banking-specific)

| Field | Value |
|---|---|
| **Claim** | Industry estimates $25–$70 per password reset (Forrester); banking-specific figure not sourced |
| **Stream** | s4-structural-shifts.md |
| **Attempted source** | Forrester (widely cited) |
| **Why unverified** | Banking-specific figure not independently sourced |
| **Needed for final doc?** | **Can drop.** FIDO Alliance 81% helpdesk reduction with passkeys is sufficient. |

---

### 17. EU bank branch closure data

| Field | Value |
|---|---|
| **Claim** | ECB/EBA-level data on EU bank branch closures not independently sourced |
| **Stream** | s4-structural-shifts.md |
| **Attempted source** | US data from NCRC/S&P Global; EU equivalent not found |
| **Why unverified** | EU branch data not located in this research |
| **Needed for final doc?** | **Can drop.** US branch contraction and India/mobile banking data support digital-first shift. |

---

### 18. US banking-specific CCPA/CPRA enforcement actions

| Field | Value |
|---|---|
| **Claim** | No specific CCPA/CPRA enforcement actions targeting banks identified |
| **Stream** | s4-structural-shifts.md |
| **Attempted source** | CPPA, CA AG enforcement database |
| **Why unverified** | Banks may be subject to CCPA but no bank-specific enforcement action was found |
| **Needed for final doc?** | **Can drop.** Disney, PlayOn Sports, data broker enforcement establish consent enforcement trend; bank-specific actions not required. |

---

## Stream 5: AI Agent Identity

### 19. Microsoft Entra Agent ID banking adoption

| Field | Value |
|---|---|
| **Claim** | Banking adoption of Agent ID not specifically documented; Azure is major banking cloud |
| **Stream** | s5-ai-agent-identity.md |
| **Attempted source** | Microsoft documentation, case studies |
| **Why unverified** | Agent ID is in preview; no banking-specific deployment data published |
| **Needed for final doc?** | **Can drop.** "First hyperscaler to offer agent identity construct" and preview status are sufficient. |

---

### 20. Strata Identity shipping product details

| Field | Value |
|---|---|
| **Claim** | Strata positions in "agentic identity"; co-published CSA survey; shipping product details need confirmation |
| **Stream** | s5-ai-agent-identity.md |
| **Attempted source** | Strata website, CSA survey |
| **Why unverified** | Product capabilities and deployment status not verified |
| **Needed for final doc?** | **Can drop.** CSA survey data (18% confident, etc.) is the key input; vendor product details are secondary. |

---

### 21. ConductorOne banking-specific capabilities

| Field | Value |
|---|---|
| **Claim** | ConductorOne published "Future of Identity Security" survey; banking-specific capabilities need confirmation |
| **Stream** | s5-ai-agent-identity.md |
| **Attempted source** | ConductorOne press release |
| **Why unverified** | Survey is enterprise-wide; banking breakdown not confirmed |
| **Needed for final doc?** | **Can drop.** 95% run agents autonomously is the key statistic; banking-specific slice is optional. |

---

### 22. Gravitee agent identity capabilities

| Field | Value |
|---|---|
| **Claim** | Gravitee "State of AI Agent Security 2026" report; primary focus API management/gateway; agent identity capabilities need confirmation |
| **Stream** | s5-ai-agent-identity.md |
| **Attempted source** | Gravitee report |
| **Why unverified** | Report focus is API/gateway security; identity governance scope unclear |
| **Needed for final doc?** | **Can drop.** Report is one of several survey sources; not central to narrative. |

---

### 23. DIF agent identity work stream

| Field | Value |
|---|---|
| **Claim** | DIF (Decentralized Identity Foundation) may have unpublished working group activity on agent identity |
| **Stream** | s5-ai-agent-identity.md |
| **Attempted source** | DIF website, work items |
| **Why unverified** | No visible work stream on agent identity; may exist but not published |
| **Needed for final doc?** | **Can drop.** OpenID Foundation and IETF are the primary standards references. |

---

## Stream 6: Fraud and Identity Convergence

### 24. Synthetic identity fraud $35B — official Fed figure

| Field | Value |
|---|---|
| **Claim** | $35B synthetic identity fraud (FiVerity estimate cited by Federal Reserve Bank of Boston); Fed has not published official loss estimate |
| **Stream** | s6-fraud-identity-convergence.md |
| **Attempted source** | Fed Reserve Boston, FiVerity, FedPayments Improvement |
| **Why unverified** | FiVerity estimate widely cited; synthetic identity often misclassified as credit loss; no official Fed figure |
| **Needed for final doc?** | **Needed.** Use with explicit caveat: "FiVerity estimate cited by Federal Reserve; Fed has not published official loss figure." |

---

### 25. BioCatch "32 of top 100 global banks" — current status

| Field | Value |
|---|---|
| **Claim** | BioCatch "32 of top 100 global banks" (earlier messaging) vs. "340 global clients" and "3 of 4 largest U.S. banks" (2025) |
| **Stream** | s6-fraud-identity-convergence.md |
| **Attempted source** | BioCatch press releases (2024, 2025) |
| **Why unverified** | "32 of 100" not repeated in 2025 materials; current top-100 bank count unclear |
| **Needed for final doc?** | **Can drop.** "3 of 4 largest U.S. banks" and >$185M ARR are sufficient and more current. |

---

## Summary: Needed vs. Can Drop

| Needed for final doc | Can drop |
|---|---|
| Synthetic identity $35B (with caveat) | All others (24 items) |

**Recommendation:** Proceed with final document using verified data. For synthetic identity, include: "Synthetic identity fraud losses are estimated at $35B+ (FiVerity, cited by Federal Reserve Bank of Boston); the Federal Reserve has not published an official loss figure, and synthetic identity is often misclassified as credit loss."
