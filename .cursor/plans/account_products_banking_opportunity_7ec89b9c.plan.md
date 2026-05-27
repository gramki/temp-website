---
name: Account Products Banking Opportunity
overview: "McKinsey-grade two-part opportunity analysis (Part I: independent analyst assessment, Part II: Zeta strategic advisory) for the Account Products and Core Banking engagement area. Replaces the current CIO-facing capability catalogue at account-products-and-banking.md."
todos:
  - id: p1b1
    content: Phase 1 Batch 1 — Research Streams 1–4 (market sizing, regulatory landscape, competitive landscape, structural shifts). 4 parallel sub-agents. Raw output to _research/account-products-and-banking/s1–s4.
    status: pending
  - id: p1b2
    content: Phase 1 Batch 2 — Research Streams 5–6 (business banking/cash management, deposit innovation/open banking). 2 parallel sub-agents. Raw output to _research/account-products-and-banking/s5–s6.
    status: pending
  - id: p2-synthesis
    content: "Phase 2 — Synthesis: cross-reference streams, rate evidence quality for each shift (Strong/Moderate/Thin/Hypothesis), verify URLs, assemble target universe (15+ named banks), map R2P/R2W. Save synthesis-notes.md and unverified-claims.md."
    status: pending
  - id: p2-gapfill
    content: Phase 2 — Targeted gap-fill for shifts with <3 data points, unclear competitive positioning, or thin progressive-migration evidence.
    status: pending
  - id: p3-market
    content: Phase 3 Part I §1 — Market (~600w). Vendor-addressable TAM by sub-domain, geography, bank tier.
    status: pending
  - id: p3-history
    content: "Phase 3 Part I §2 — How We Got Here (~400w). Three eras: monolithic core, channel overlay, composable platform pressure."
    status: pending
  - id: p3-shifts
    content: Phase 3 Part I §3 — Structural Shifts (~2,500w). 6–8 shifts with evidence, bank-tier analysis, geographic variation. The core of the document.
    status: pending
  - id: p3-engagements
    content: Phase 3 Part I §4 — Engagement Landscape (~500w). 6 engagement types mapped to bank tier and structural shift.
    status: pending
  - id: p3-competitive
    content: Phase 3 Part I §5 — Competitive Landscape (~600w). Incumbents, challengers, specialists. Replace-vs-augment question.
    status: pending
  - id: p3-targets
    content: Phase 3 Part I §6 — Target Universe (~500w). Named institutions across USA, India, UK with cited modernization evidence.
    status: pending
  - id: p3-position
    content: Phase 3 Part II §7 — Zeta's Position (~500w). Tachyon, Quark, Evolution Fabric mapped. Product maturity assessed honestly.
    status: pending
  - id: p3-wheretoplay
    content: "Phase 3 Part II §8 — Where to Play (~500w). R2P/R2W table. Pursue/defer/avoid. Sequencing: lead with payments then expand?"
    status: pending
  - id: p3-risks
    content: Phase 3 Part II §9 — Risks and Gaps (~400w). Tachyon readiness, Thought Machine window, sales cycle, cannibalization.
    status: pending
  - id: p3-actions
    content: Phase 3 Part II §10 — Recommended Actions (~400w). Near-term and medium-term, conditioned on product readiness.
    status: pending
  - id: p3-execsummary
    content: Phase 3 §11 — Executive Summary (~400w). Written last. Board member reads only this and understands opportunity + position + action.
    status: pending
  - id: p4-partI
    content: "Phase 4 — Part I review: citations verified, no commercial voice, no Zeta refs, composable banking thesis grounded in empirical evidence."
    status: pending
  - id: p4-partII
    content: "Phase 4 — Part II review: recommendations trace to Part I, gaps honest, product refs verified, conditional recs where Tachyon readiness uncertain."
    status: pending
  - id: p4-editorial
    content: "Phase 4 — Editorial rigor (Part I only): all 8 tests from editorial-rigor-review skill."
    status: pending
isProject: true
---

# Account Products and Core Banking — Opportunity Analysis & Strategic Advisory

**Full plan detail:** [.cursor/plans/account_products_banking_opportunity_analysis.plan.md](.cursor/plans/account_products_banking_opportunity_analysis.plan.md)
**Output file:** [org-8.0/what-we-sell/strategy/engagement-areas/account-products-and-banking.md](org-8.0/what-we-sell/strategy/engagement-areas/account-products-and-banking.md)
**Research output:** `org-8.0/what-we-sell/strategy/_research/account-products-and-banking/`
**Target length:** 5,500–7,500 words (two-part structure)

---

## What This Area Is About

Core banking modernization — the most consequential and slowest-moving technology decision a bank makes. Replacement cycles are 15–25 years, sales cycles are 2–5 years, and implementations span 3–7 years. The current file is a 109-line CIO-facing capability catalogue with an explicit placeholder note. It must be replaced with a deeply researched two-part document.

**Key Zeta assets for Part II:** Tachyon (Kernel, DDA, Credit Cards, CLM, Loans), Quark domain hubs, Evolution Fabric, Trust Fabric, Neutrino, Photon. Critical internal question: Tachyon product-line docs are placeholder ("to be expanded") — is this a documentation gap or a product maturity gap?

---

## Phase 1: Parallel Research (6 Streams)

### Batch 1 (4 concurrent sub-agents)

- **S1 — Market Sizing:** Vendor-addressable TAM for core banking technology (core platforms, digital banking, business banking/cash management, origination, BaaS-enabling). By geography (USA, India, UK/Europe), by bank tier, by build-vs-buy pattern. Sources: Gartner MQ, Celent Dimensions, IDC, IBS Intelligence, vendor SEC filings (Temenos, FIS, Fiserv, Jack Henry, Alkami, Q2).
- **S2 — Regulatory Landscape:** Regulations forcing account infrastructure investment. USA: CFPB Section 1033, FDIC Part 370, FinCEN CDD/KYC, CRA modernization. India: RBI Account Aggregator, RBI Current Account Direction, DPDP Act. UK/EU: PSD2/PSD3, UK Open Banking/CASS, FCA Consumer Duty, DORA, Basel III/IV. Cross-ref existing `_research/payments/s2-regulatory-landscape.md` and `_research/digital-identity-and-trust/s2-regulatory-landscape.md`.
- **S3 — Competitive Landscape:** Legacy (FIS, Fiserv, Jack Henry, Temenos, Finacle, BaNCS, FLEXCUBE, Finastra), modern challengers (Thought Machine, Mambu, 10x, Finxact/FIS, Pismo/Visa), digital banking platforms (Backbase, Alkami, Q2), business banking specialists (Finastra Fusion, Bottomline, Kyriba, Intellect iGTB), product/pricing engines (Zafin, SunTec). For each: revenue, bank tier focus, architecture, wins/losses, vulnerabilities. Include bank modernization signals sub-task.
- **S4 — Structural Shifts:** 8 candidate shifts — progressive core replacement, composable banking, cloud-native core, business banking digitization, open banking mandates, deposit competition, embedded banking/BaaS, AI in account operations. Each needs 3+ independent data points. Include bank modernization signals sub-task.

### Batch 2 (2 concurrent sub-agents)

- **S5 — Business Banking & Cash Management:** Separate sub-market with different dynamics. Virtual accounts, cash pooling, multi-entity structures, treasury, SME digital banking challengers (Tide, Mercury, Relay, Novo). McKinsey/BCG commercial banking data.
- **S6 — Deposit Innovation & Open Banking:** Neobank deposit capture data (Chime, SoFi, Revolut, Monzo, Starling), high-yield savings competition, time-to-market evidence, open banking adoption (OBIE UK stats, Section 1033 timeline, Account Aggregator India), stablecoin/tokenized deposit competition.

---

## Phase 2: Synthesis and Gap-Fill

- Cross-reference market sizing definitions across sources (core banking TAM is inconsistently defined)
- Assess evidence for "composable banking" and "progressive core replacement" — well-articulated by analysts but how many established banks (not neobanks) have completed it?
- Distinguish regulations that force core replacement vs. those satisfiable by wrapping the legacy core
- Rate each structural shift: Strong / Moderate / Thin / Hypothesis
- Consolidate bank signals into target universe (min 15 named institutions)
- Map Right to Play / Right to Win — critically: can Zeta enter given Tachyon's uncertain product maturity?
- Verify all URLs, flag unverified claims
- Assess Middle East/Gulf as potential 4th geography (only if evidence warrants)

---

## Phase 3: Document Writing

### Part I — The Opportunity (analyst voice, zero Zeta references)

1. **Market** (~600w) — vendor-addressable TAM, geography/tier breakdowns, fastest-growing segments
2. **How We Got Here** (~400w) — three eras: monolithic core, channel overlay, composable platform pressure
3. **Structural Shifts** (~2,500w) — 6–8 shifts evidenced with data, by bank tier and geography
4. **Engagement Landscape** (~500w) — progressive core migration, digital account platform, business banking build, BaaS enablement, deposit innovation platform, open banking compliance
5. **Competitive Landscape** (~600w) — incumbents, challengers, specialists, the "replace vs. augment" question
6. **Target Universe** (~500w) — named banks by geography, tier, horizon, with cited evidence

### Part II — The Advisory (advisor voice, Zeta-specific)

1. **Zeta's Position** (~500w) — Tachyon, Quark, Evolution Fabric mapped honestly; product maturity assessed
2. **Where to Play** (~500w) — R2P/R2W assessment; explicit pursue/defer/avoid calls; sequencing question (lead with payments then expand to accounts?)
3. **Risks and Gaps** (~400w) — Tachyon readiness prerequisite, Thought Machine window risk, sales cycle reality, cannibalization risk
4. **Recommended Actions** (~400w) — near-term and medium-term, conditioned on product readiness
5. **Executive Summary** (~400w) — written last, covers both parts

---

## Phase 4: Review

- Part I: citation verification, no commercial voice, no Zeta refs, evidence-grounded tier/geo analysis, "composable banking" thesis grounded in empirical data not just analyst advocacy
- Part II: recommendations trace to Part I evidence, gaps stated honestly, product refs verified against repo files, conditional recommendations where Tachyon readiness is uncertain
- Editorial rigor (Part I only): all 8 tests from [.cursor/skills/editorial-rigor-review/SKILL.md](.cursor/skills/editorial-rigor-review/SKILL.md)

---

## Key Differences from Payments

- **Replacement cycle:** 15–25 years (vs. 5–10 for payments) — most consequential tech decision
- **Sales cycle:** 2–5 years (vs. 6–18 months) — fundamentally different GTM economics
- **Zeta position:** Uncertain (Tachyon docs are placeholder) vs. strong for payments (Photon production-deployed)
- **Regulatory forcing:** Moderate — fewer hard deadlines than payments; driven more by competitive pressure and tech debt
- **UK as 3rd market:** Stronger than for payments — open banking leadership, CASS, challenger bank proof points
- **Central argument:** The core is the most consequential constraint on a bank's ability to evolve. Progressive product-by-product replacement is becoming viable.

---

## Output Files

- **Primary:** `org-8.0/what-we-sell/strategy/engagement-areas/account-products-and-banking.md`
- **Research retention:** `org-8.0/what-we-sell/strategy/_research/account-products-and-banking/` — s1 through s6 stream files, synthesis-notes.md, unverified-claims.md
- **Cross-refs:** Existing research in payments, digital identity, commercial cards streams for overlapping regulatory and competitive data

