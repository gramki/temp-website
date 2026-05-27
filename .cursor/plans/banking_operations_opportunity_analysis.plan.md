---
name: Banking Operations Opportunity Analysis
overview: "McKinsey-grade two-part opportunity analysis (Part I: independent analyst assessment, Part II: Zeta strategic advisory) for the Banking Operations engagement area. Creates a deeply researched document on the run-the-bank business operations market — reconciliation, compliance operations, fraud operations, collections, credit operations, and regulatory reporting."
todos:
  - id: p1b1
    content: "Phase 1 Batch 1: Launch 4 parallel research sub-agents (S1 market sizing, S2 regulatory, S3 competitive landscape, S4 structural shifts). Save to _research/banking-operations/s1-s4."
    status: pending
  - id: p1b2
    content: "Phase 1 Batch 2: Launch 2-3 parallel research sub-agents (S5 reconciliation & exception platforms, S6 compliance & regulatory reporting tech, S7 operations cost & headcount evidence). Save to _research/banking-operations/s5-s7."
    status: pending
  - id: p2-synthesis
    content: "Phase 2 Synthesis: cross-reference streams, evidence quality ratings, URL verification, target universe assembly, R2P/R2W mapping. Save synthesis-notes.md and unverified-claims.md."
    status: pending
  - id: p2-gapfill
    content: "Phase 2 Gap-fill: targeted research for thin evidence areas (bank operations spend by sub-domain, named bank modernization signals)."
    status: pending
  - id: p3-partI
    content: "Phase 3 Part I: Write Market, How We Got Here, Structural Shifts, Engagement Landscape, Competitive Landscape, Target Universe. Analyst voice, no Zeta references."
    status: pending
  - id: p3-partII
    content: "Phase 3 Part II: Write Zeta's Position, Where to Play, Risks and Gaps, Recommended Actions. Advisor voice, honest gaps."
    status: pending
  - id: p3-execsummary
    content: "Phase 3 Executive Summary: covers both parts, written last."
    status: pending
  - id: p4-review
    content: "Phase 4 Review: citation verification, voice discipline, editorial rigor (8 tests on Part I), product reference accuracy (Part II)."
    status: pending
isProject: true
---

# Banking Operations — Opportunity Analysis & Strategic Advisory Plan

**Engagement Area:** Banking Operations  
**Output:** `org-8.0/what-we-sell/strategy/engagement-areas/banking-operations.md`  
**Target length:** 5,000–8,000 words (two-part structure)  
**Current state:** No existing engagement-area file under this name. The document will be created. The scope is the **run-the-bank business operations** market — reconciliation and settlement, compliance operations, fraud investigation, collections, credit operations, and regulatory reporting — as a vendor-addressable opportunity. This is distinct from Cloud and Platform Operations (IT/infrastructure) and positions Agentic Operations as the AI-agent deployment layer within this domain.

---

## 1. Model Recommendation

**Orchestration:** Default model. The orchestrator must manage 6–7 parallel research streams, synthesize fragmented market data (operations technology is split across reconciliation, AML/compliance, fraud, collections, regulatory reporting), enforce the analyst/advisor voice boundary, and apply the eight editorial rigor tests. Banking Operations spans multiple sub-categories with no single published "banking operations TAM" — requiring sustained reasoning to construct a coherent opportunity thesis.

**Research sub-agents:** Default model for all streams. Rationale:

- **Streams 1–4** (market sizing, regulatory, competitive, structural shifts) face **fragmented analyst coverage**. There is no single "banking operations" market report. Vendor-addressable spend must be constructed from: reconciliation and exception management (often bundled with treasury or payments), AML/compliance technology (Chartis, Aite-Novarica, Celent), fraud operations (Javelin, Aite), collections and recovery (Debt Buyer/Servicer reports, Celent), and regulatory reporting (RegTech). The default model is needed to aggregate and reconcile sub-segment estimates and avoid double-counting.
- **Stream 5** (reconciliation and exception platforms) has **moderate coverage** — treasury and reconciliation software (Gartner, Celent), bank operations surveys (Cornerstone Advisors, Celent). Primary evidence (vendor 10-Ks, bank earnings mentions of reconciliation modernization) will supplement.
- **Stream 6** (compliance and regulatory reporting) has **strong regulatory and moderate vendor coverage** — AML/sanctions (FinCEN, FATF, RBI), regulatory reporting (BCBS, EBA, SEC, RBI), RegTech sizing (Chartis, CB Insights). Regulatory citations are abundant; vendor-addressable TAM for "compliance operations platforms" (vs. point solutions) is thinner.
- **Stream 7** (operations cost and headcount) has **partial coverage** — McKinsey/BCG cite operations as 60–70% of bank cost base; headcount and FTE data by operations domain is scarcer. Research should emphasize primary sources (bank 10-K disclosures on operations headcount, analyst reports with cited figures).

**Impact of coverage gaps:** Banking Operations is a **constructed category** — the opportunity must be derived by aggregating sub-domains (reconciliation, compliance ops, fraud ops, collections, credit ops, regulatory reporting) rather than read from a single analyst product. Where analyst coverage is thin, research streams must emphasize primary evidence: regulatory texts, SEC/earnings disclosures, vendor product launches, and industry body publications. Market sizing methodology must be transparent and conservative.

---

## 2. Phase 1: Parallel Research (6–7 Streams)

### Stream 1: Market Sizing and Revenue Pools

**What to gather:**

- Vendor-addressable TAM for each sub-segment of **banking business operations** (run-the-bank, not IT operations):
  - **Reconciliation and exception management** — ledger vs. clearing, inter-system reconciliation, exception handling platforms, settlement reconciliation.
  - **Compliance operations** — AML transaction monitoring, sanctions screening, KYC/onboarding operations, compliance workflow and case management.
  - **Fraud operations** — fraud case management, investigation workflows, alert triage and resolution (distinct from fraud detection engines).
  - **Collections and recovery** — collections platforms, workout and forbearance workflows, recovery and cure management.
  - **Credit operations** — covenant monitoring, portfolio surveillance, credit review and underwriting support workflows (operations, not origination LOS).
  - **Regulatory reporting and filing** — regulatory report assembly, regulatory data management, submission workflows (distinct from data warehouse/reporting).
- Revenue breakdown by geography (USA, India, and at most one additional jurisdiction if evidence supports — e.g. UK/EU for regulatory reporting).
- Revenue breakdown by bank tier where available (Tier 1 / $100B+ assets, Tier 2 / $10B–$100B, Tier 3 / $1B–$10B).
- Growth rates (CAGR) by sub-segment.
- Operations spend as a percentage of bank cost base or non-interest expense — with cited source.
- Build vs. buy patterns by bank tier for operations technology.

**Sources to target:**

- Celent (bank operations technology, reconciliation, AML/fraud, collections reports)
- Chartis Research (AML, compliance, risk technology)
- Aite-Novarica (financial crime, compliance, operations)
- Gartner (Market Guide for Financial Crime, reconciliation/treasury where applicable)
- Grand View Research, Mordor Intelligence, MarketsandMarkets (reconciliation software, AML solutions, RegTech — with BFSI segmentation)
- Cornerstone Advisors ("What's Going On in Banking" — operations and technology adoption)
- SEC filings for public vendors: FIS, Fiserv, NICE, SAS (segments touching operations/compliance/fraud)
- McKinsey/BCG banking operations cost and productivity reports (with exact publication, date, title, URL or full bibliographic detail)
- RBI, OCC, Fed, EBA publications on operational risk and compliance spend

**Geographic scope:** USA (primary), India (accessible), and at most one additional jurisdiction (e.g. UK/EU) only if the evidence shows meaningful concentration for this area.

**How data will be used:** Part I, Section 1 (Market). Establishes the prize. Sub-segment breakdowns must be transparent about derivation; where a single "banking operations" TAM does not exist, the methodology for aggregating sub-segments must be documented.

**Citation requirement:** Every data point must include a navigable URL or full bibliographic detail per the Citation Standard. Flag as `[unverified — needs manual confirmation]` if the source cannot be linked or fully attributed.

---

### Stream 2: Regulatory Landscape and Operations Mandates

**What to gather:**

- Regulations that **force or strongly incentivize** banks to invest in operations infrastructure — with compliance deadlines, penalty regimes, and operational capability implications.
- For each regulation: what operational capability it demands, compliance status/deadlines, and what infrastructure or process investment it forces.

**Regulations to cover by geography:**

**USA:**

- BSA/AML and FinCEN rules — AML program requirements, transaction monitoring, suspicious activity reporting, beneficial ownership. Implications for compliance operations platforms and staffing.
- OFAC and sanctions screening — real-time and batch screening requirements; impact on sanctions operations and exception handling.
- OCC/Fed/FDIC operational risk and third-party risk management guidance — as they affect operations outsourcing and control evidence.
- SEC/FINRA regulatory reporting and recordkeeping — implications for regulatory report assembly and audit trails.
- CFPB supervision and enforcement — fair lending, servicing, collections — impact on collections operations and compliance documentation.
- Dodd-Frank 1033 (data access) — any implications for operations data and reporting.

**India:**

- RBI Master Direction on KYC — AML/KYC operations implications.
- RBI guidelines on fraud management and reporting — fraud operations and regulatory reporting.
- RBI regulatory reporting (statutory returns) — report assembly and submission infrastructure.
- PMLA and FIU-IND requirements — AML operations and STR filing.
- Data localization and DPDP — impact on operations data and vendor solutions.

**UK/EU (only if included as third geography):**

- AML Directives (AMLD5/6) and national transposition — compliance operations and reporting.
- DORA — operational resilience; impact on critical operations and incident management (cross-reference with cloud-and-platform-operations research; avoid re-researching).
- EBA regulatory reporting and COREP/FINREP — report production and submission.

**Sources to target:**

- Official regulatory texts (FinCEN, OCC, Fed, RBI, FCA, EBA)
- Law firm and Big Four regulatory summaries (with links to specific documents)
- Cross-reference `org-8.0/what-we-sell/strategy/_research/cloud-and-platform-operations/s2-regulatory-landscape.md` for DORA/operational resilience overlap; note cross-reference in synthesis-notes.md

**Geographic scope:** USA, India, and if justified, UK/EU.

**How data will be used:** Part I, Sections 2 (How We Got Here) and 3 (Structural Shifts). Regulatory pressure on AML, sanctions, fraud reporting, and regulatory filing is a primary forcing function for operations investment.

**Citation requirement:** Every regulation cited must link to official text or a specific guidance document. Secondary summaries must be traceable.

---

### Stream 3: Competitive Landscape

**What to gather:**

For each competitor category: key players; for each player — positioning, target market (bank tier, geography), revenue model, product scope (which operations domains covered), strengths, weaknesses, and vulnerabilities. Focus on **operations** (run-the-bank) not core banking or payments engines.

**Categories and players to map:**


| Category                                                   | Players to Research                                                                                                                                                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Reconciliation and exception management**                | SmartStream, Fiserv (reconciliation modules), FIS (reconciliation), SAP (treasury/reconciliation), Oracle (reconciliation), specialist vendors (e.g. Duco, AutoRek, Adenza — where relevant to banking operations) |
| **AML / compliance operations**                            | NICE Actimize, SAS (AML), FIS (AML), Fiserv (compliance), Oracle (AML), SAS, Verafin (Mastercard), Feedzai, ComplyAdvantage, Chainalysis (crypto-adjacent)                                                         |
| **Fraud operations and case management**                   | NICE, SAS, FIS, Fiserv, Featurespace, BioCatch (behavioral), Deduce (identity) — focus on case management and investigation workflow, not only detection                                                           |
| **Collections and recovery**                               | FIS (Debt Manager), Fiserv (collections), Pegasystems, Experian (collections), FICO (Debt Manager), specialist collections platforms                                                                               |
| **Regulatory reporting and RegTech**                       | AxiomSL, Wolters Kluwer, OneSumX, Oracle (regulatory reporting), SAP (GRC), Moody's Analytics, specialist RegTech (as relevant to report assembly and submission)                                                  |
| **Horizontal workflow/case management used in operations** | ServiceNow (GRC, case management), Pegasystems (decisioning and workflow), Appian (operations workflows)                                                                                                           |
| **India operations technology**                            | TCS, Infosys, Wipro (operations services and platforms), Newgen, Perfios (where relevant to operations), bank-specific builds                                                                                      |


**For each player, capture:**

- Annual revenue or ARR (where public or estimable) for the operations-relevant segment.
- Banking/financial services customer count or logos where disclosed.
- Whether they offer banking-specific operations (reconciliation, compliance ops, fraud ops, collections, regulatory reporting) as a platform vs. point solutions.
- Gaps: which operations domains they do NOT cover; where architecture is legacy vs. modern; where AI/automation is bolt-on vs. structural.
- Recent M&A or partnership signals relevant to banking operations.

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled **banking operations** modernization (reconciliation, compliance operations, fraud operations, collections, regulatory reporting) — through earnings calls, press releases, RFP announcements, vendor partnership disclosures, or analyst commentary. For each: bank name, tier, geography, the signal (which operations domain), the source, and a navigable URL. Do not include banks solely for IT/cloud operations (those belong in Cloud and Platform Operations target universe).

**Sources to target:**

- SEC filings (10-K/10-Q) for FIS, Fiserv, NICE, SAS, Pegasystems
- Celent, Aite-Novarica, Chartis reports on AML, fraud, reconciliation, collections
- Gartner Market Guide for Financial Crime, reconciliation/treasury
- Earnings call transcripts (Seeking Alpha) — search for "reconciliation," "compliance operations," "fraud operations," "collections," "regulatory reporting"
- Vendor press releases (bank partnerships)
- American Banker, Finextra (operations technology deals)

**Geographic scope:** Global with emphasis on USA, India, UK/EU.

**How data will be used:** Part I, Section 5 (Competitive Landscape) and Part II, Section 7 (Zeta's Position).

**Citation requirement:** Revenue and product scope from SEC filings or vendor documentation. Every competitive claim sourced.

---

### Stream 4: Structural Shifts and Bank Operations Modernization Activity

**What to gather:**

Evidence for **6–8 structural shifts** reshaping the banking operations (run-the-bank) market. Each shift must be evidenced with data, regulatory citations, competitive activity, and bank-tier analysis.

**Candidate structural shifts to investigate:**

1. **Operations cost and volume outstripping headcount.** Operations represent 60–70% of bank cost base (McKinsey/BCG — require cited source). Transaction and case volumes grow; experienced operations staff are scarce. Evidence: operations cost as % of bank expense, FTE trends in compliance/fraud/collections, wage and attrition data.
2. **Regulatory intensity forcing operations investment.** AML, sanctions, fraud reporting, and regulatory filing requirements compound. Penalties for control failures are severe. Evidence: enforcement actions, penalty amounts, regulatory deadlines (e.g. beneficial ownership, real-time payments reporting), bank disclosures on compliance spend.
3. **Reconciliation and exception handling at scale.** Real-time payments and multi-system landscapes increase reconciliation and exception volume. Legacy batch reconciliation and manual exception handling do not scale. Evidence: reconciliation platform adoption, exception volume trends, bank or vendor case studies with URLs.
4. **Concentration and fragility of operational knowledge.** How exceptions are resolved, how fraud cases are investigated, how compliance checks are sequenced — knowledge lives in experienced staff. Turnover and retirement create operational risk. Evidence: industry surveys on knowledge retention, operational risk events linked to key-person dependency.
5. **Shift from periodic to continuous operations.** Regulatory and business pressure for continuous compliance monitoring, real-time reconciliation, and always-on operations rather than batch and period-end. Evidence: regulatory guidance (e.g. continuous monitoring expectations), vendor and bank commentary.
6. **AI and automation in operations — from tools to agents.** Banks are deploying AI for alert triage, exception classification, and case assembly. The structural shift from "AI as tool" to "AI as participant" in operations (agentic) is emerging. Evidence: vendor product launches, bank pilots, analyst coverage; distinguish marketing from production deployment (cross-reference cloud-and-platform-operations gap-fill on agentic ops where relevant).
7. **Legacy operations platforms constraining change.** Core operations run on legacy reconciliation, compliance, and collections platforms that are hard to change. Replacement is risky; wrapping adds complexity. Evidence: vendor legacy vs. modern positioning, bank modernization program disclosures.
8. **(Candidate)** **Convergence of operations data and auditability.** Regulators and auditors expect traceable decision trails for operational decisions (reconciliation resolutions, compliance determinations, fraud dispositions). Operations platforms that cannot produce compliance-grade audit trails face replacement pressure. Evidence: regulatory guidance, audit firm expectations, vendor capabilities.

**For each shift, gather:**

- At least 3 data points with sources and URLs (or full bibliographic detail).
- Regulatory citations that create or accelerate the shift.
- Competitive activity (vendors capitalizing on the shift).
- Analysis by bank tier (Tier 1 vs. Tier 2 vs. Tier 3).
- Geographic variation (USA, India, and any additional jurisdiction).

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled **business operations** modernization (reconciliation, compliance, fraud ops, collections, credit operations, regulatory reporting) — through earnings calls, press releases, technology or operations leadership presentations, vendor partnership disclosures. For each: bank name, tier, geography, signal, source, navigable URL.

**Sources to target:**

- McKinsey, BCG, Deloitte banking operations and cost reports (with exact title, date, URL or bibliographic detail)
- Celent, Aite-Novarica operations and compliance surveys
- Bank 10-K/10-Q — risk factors and MD&A for operational risk, compliance, headcount
- Earnings call transcripts — search for operations, reconciliation, compliance, fraud, collections
- Regulatory enforcement actions (FinCEN, OCC, CFPB, RBI) — penalty amounts and required remediation
- Cross-reference `org-8.0/what-we-sell/strategy/_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md` for agentic operations evidence in banking; cite rather than duplicate

**Geographic scope:** USA, India, and if included, UK/EU.

**How data will be used:** Part I, Sections 2–4 and 6 (How We Got Here, Structural Shifts, Engagement Landscape, Target Universe).

**Citation requirement:** Every structural shift claim grounded in at least three independent data points with navigable URLs or full bibliographic detail. Assertions without evidence flagged or dropped.

---

### Stream 5: Reconciliation and Exception Management Platforms

**Why a separate stream:** Reconciliation and exception handling are a major operations sub-domain with distinct vendors, regulatory drivers (settlement, nostro, regulatory reporting accuracy), and structural pressure (real-time payments, multi-system landscapes). Evidence is often bundled with treasury or payments; this stream isolates it.

**What to gather:**

- Market size for reconciliation and exception management software (banking/financial services segment) — with source and URL.
- Key vendors: positioning, product scope (ledger vs. clearing, inter-system, settlement, nostro), deployment model (on-prem vs. cloud), banking-specific capabilities.
- Regulatory and business drivers: settlement finality, real-time reconciliation expectations, regulatory reporting accuracy requirements.
- Evidence of banks modernizing reconciliation (earnings, vendor announcements, case studies) — with navigable URLs.
- Gaps: where do banks still rely on spreadsheets, legacy batch tools, or manual exception handling? Surveys or primary evidence.

**Sources to target:**

- Gartner, Celent (treasury and reconciliation reports)
- SmartStream, Duco, AutoRek, Adenza (or equivalent) — product and client disclosures where available
- FIS, Fiserv, SAP, Oracle — reconciliation module documentation and revenue segmentation
- Real-time payments and settlement literature (BIS, Fed, RBI) — implications for reconciliation
- Bank technology or operations leadership presentations (search for "reconciliation," "exception")

**Geographic scope:** USA, India; UK/EU if evidence supports.

**How data will be used:** Part I, Sections 1 (Market — sub-segment), 3 (Structural Shifts — reconciliation at scale), 5 (Competitive Landscape). Part II — Zeta's position in operations (Quark/Evolution Fabric for reconciliation Loops).

**Citation requirement:** Every claim with navigable URL or full bibliographic detail.

---

### Stream 6: Compliance Operations and Regulatory Reporting Technology

**Why a separate stream:** Compliance operations (AML, sanctions, KYC workflows, case management) and regulatory reporting (report assembly, submission, audit trails) are heavily regulated and have distinct vendor landscapes. This stream provides the evidence base for structural shifts tied to regulation and for competitive mapping.

**What to gather:**

- Vendor-addressable TAM for AML/compliance operations technology and for regulatory reporting/RegTech — with geography and bank-tier breakdown where available.
- Key regulations that mandate or shape compliance operations and reporting (USA, India, and if applicable UK/EU) — with deadlines and penalty regimes; link to official or authoritative source.
- Competitive landscape: NICE, SAS, FIS, Fiserv, Verafin, AxiomSL, Wolters Kluwer, etc. — product scope, banking focus, strengths and vulnerabilities.
- Evidence of banks investing in compliance operations or regulatory reporting modernization — with named banks and URLs.
- Trends: continuous monitoring, automated report assembly, audit trails and evidence management — with evidence.

**Sources to target:**

- Chartis, Aite-Novarica, Celent (AML, compliance, RegTech)
- FinCEN, OCC, RBI, EBA (regulatory texts and guidance)
- SEC filings for NICE, SAS, FIS, Fiserv (compliance/risk segments)
- Vendor press releases and bank case studies with links

**Geographic scope:** USA, India, and if justified UK/EU.

**How data will be used:** Part I, Market (sub-segment), Structural Shifts (regulatory intensity, continuous operations, auditability), Competitive Landscape, Target Universe.

**Citation requirement:** Regulatory citations to official texts. Vendor and market data with navigable URLs or full bibliographic detail.

---

### Stream 7: Operations Cost, Headcount, and Capacity Evidence

**Why a separate stream:** The thesis that "operations are 60–70% of bank cost base" and that "volume exceeds headcount capacity" is central to the opportunity. This stream gathers citable evidence for cost structure, FTE trends, and capacity constraints — so the document does not rely on unattributed claims.

**What to gather:**

- Operations (run-the-bank) as a share of bank cost base or non-interest expense — with exact source (McKinsey, BCG, or other — publication name, date, title, URL or full bibliographic detail).
- FTE or headcount data for compliance, fraud, collections, reconciliation (where publicly disclosed or in analyst reports with citation).
- Wage and attrition data for operations roles (where available with source).
- Evidence that banks are seeking to extend capacity without proportional headcount (automation, AI, platform consolidation) — earnings calls, surveys, vendor outcomes with URLs.
- Any data on exception volume, case volume, or reconciliation volume growth — with source.

**Sources to target:**

- McKinsey, BCG, Deloitte banking cost and operations reports (exact titles and links)
- Bank 10-K — non-interest expense breakdown, risk factors (operational risk, talent)
- Celent, Cornerstone Advisors surveys (operations staffing, technology adoption)
- Industry bodies (ABA, BAI, RBI reports) — operations and technology spend

**Geographic scope:** USA primary; India and UK/EU where data exists.

**How data will be used:** Part I, Market (framing) and Structural Shifts (operations cost and volume vs. headcount). Ensures the central "capacity problem" is evidenced, not asserted.

**Citation requirement:** No "according to McKinsey" without traceable reference. Paywalled reports: full bibliographic detail so the reader can locate independently.

---

## 3. Phase 2: Synthesis and Gap-Fill

### Cross-referencing

- **Market sizing:** Combine Stream 1 with Streams 5 and 6 sub-segment data. Reconcile overlapping categories (e.g. AML platform vs. compliance operations platform) to avoid double-counting. Document derivation methodology in synthesis-notes.md.
- **Regulatory–competitive alignment:** Map regulations (Stream 2) to required capabilities and to vendor coverage (Stream 3). Identify gaps where regulations demand capabilities that incumbents do not fully provide.
- **Structural shifts–evidence quality:** For each shift (Stream 4), confirm at least three independent data points. Cross-reference Stream 7 for cost/headcount shifts. Where agentic/AI in operations is a shift, reference cloud-and-platform-operations agentic gap-fill; do not duplicate.
- **Bank signal aggregation:** Consolidate bank modernization signals from Streams 3 and 4 (and 5–6 where applicable) into a single target universe. De-duplicate. Verify tier and geography. Confirm every source URL resolves.

### Evidence quality assessment

For each structural shift, rate evidence quality:

- **Strong:** 3+ independent data points with navigable URLs or full bibliographic detail; confirmed by analyst and primary sources.
- **Moderate:** 2 data points or analyst-only without primary confirmation.
- **Thin:** Single source or vendor-only.
- **Hypothesis:** No external evidence — flag as hypothesis and state explicitly in the document.

### URL and citation verification

- Verify every URL resolves to the cited content (not homepage, not 404, not login wall with no preview).
- For paywalled sources, confirm full bibliographic detail (publication, author, date, title, issue).
- Flag unverifiable claims in `unverified-claims.md`.

### Targeted gap-fill research

- Any structural shift with fewer than 3 data points.
- Banking operations spend by sub-domain if Stream 1 and 7 leave gaps.
- Named bank targets where initial signals lack a verifiable URL.
- India-specific operations mandates and vendor landscape if thin.

### Right to Play / Right to Win mapping

Map findings to the distillation framework (how-to.md):

**Right to Play:** Is the banking operations (run-the-bank) market large and real enough? Are banks actively commissioning operations modernization (reconciliation, compliance, fraud, collections, reporting)? Is entry feasible given Zeta's assets (Evolution Fabric, Quark, CAF, Trust, Truth)?

**Right to Win:** Does Zeta's operational model (Hub, Streams, Loops, Scenarios, Seer) represent a genuine advantage over assembling horizontal workflow + point solutions? Where are Zeta's gaps (production references, coverage of all operations domains, competitive vs. FIS/Fiserv/NICE/ServiceNow)?

### Assembling the target universe

From bank signals across streams:

- Organize by geography (USA, India, and any additional jurisdiction).
- Classify by tier (Tier 1 / $100B+ assets, Tier 2 / $10B–$100B, Tier 3 / $1B–$10B).
- Classify by horizon (Near-term 0–2 years: active operations modernization signals; Medium-term 2–5 years: structural pressure).
- For each bank: name, tier, geography, signal type, source, URL.
- Minimum 12–15 named institutions across tiers and geographies.
- Every entry must have a citable evidence basis with navigable source link.

### Grounding the Zeta advisory

Cross-reference competitive landscape with Zeta product-line files:

- **Evolution Fabric (Hub, Seer):** Operational substrate for domains; AI agent control plane. Map to operations domains (reconciliation, compliance, fraud, collections, credit ops).
- **Quark:** Pre-built domain hubs — which hubs exist or are planned for reconciliation, compliance, fraud, collections, credit operations. Map to competitive positioning.
- **Cognitive Audit Fabric:** Auditability for operational decisions — reconciliation resolutions, compliance determinations, fraud dispositions. Map to regulatory and audit expectations.
- **Trust Fabric, Truth Fabric:** Identity and semantic grounding for operations. Relevance to compliance and audit trails.

Identify gaps honestly: production references for Zeta in banking operations (vs. agentic-operations capability catalogue); coverage of all sub-domains; competition from horizontal (ServiceNow, Pegasystems) and vertical (FIS, Fiserv, NICE) incumbents.

---

## 4. Phase 3: Document Writing

Section-by-section writing order. Target word counts are guidelines.

### PART I — THE OPPORTUNITY (Analyst voice, no Zeta references)

1. **Market (~600 words)** — Vendor-addressable TAM for banking operations sub-segments (reconciliation, compliance ops, fraud ops, collections, credit ops, regulatory reporting). Geography (USA, India, +1 if justified). Bank-tier breakdown where available. Growth rates. Operations as share of bank cost base (with citation). Derivation methodology transparent where TAM is constructed from sub-segments.
2. **How We Got Here (~400 words)** — Brief historical framing: evolution from manual operations and batch reconciliation to multi-system, high-volume operations; regulatory expansion; legacy platforms and operational debt. Only what is needed to set up structural shifts.
3. **Structural Shifts (6–8 shifts, ~2,200 words)** — The core. Each shift: evidence (data + citations), opportunity by segment (Tier 1/2/3), geographic nuance. Final list determined by evidence quality in Phase 2. No assertion without evidence.
4. **The Engagement Landscape (~450 words)** — Concrete engagement types banks commission: reconciliation and exception platform modernization, compliance operations transformation, fraud operations and case management, collections platform and strategy, regulatory reporting and RegTech, operations model and AI/automation. Map to bank tier and structural shifts.
5. **Competitive Landscape (~550 words)** — By category (reconciliation, AML/compliance, fraud ops, collections, regulatory reporting, horizontal workflow). Strengths and vulnerabilities. Gaps: where no vendor covers the full operations surface or banking-grade auditability.
6. **Target Universe (~500 words)** — Named institutions with observable modernization signals. By geography, tier, horizon. For each: evidence and navigable URL. Framed as analytical observation, not sales targeting.

### PART II — THE ADVISORY (Advisor voice, Zeta-specific)

1. **Zeta's Position (~500 words)** — Evolution Fabric (Hub, Seer), Quark (operations-relevant hubs), Cognitive Audit Fabric, Trust Fabric, Truth Fabric mapped to the opportunity. What is production-ready, what is partial, what is missing. Honest gap assessment vs. incumbents and horizontal workflow vendors.
2. **Where to Play (~450 words)** — Which segments to pursue (e.g. reconciliation-led, compliance-led, agentic operations-led), which to defer, which geographies and bank tiers to prioritize. Explicit "do not pursue" or "delay" where evidence or position is weak.
3. **Risks and Gaps (~400 words)** — What must be true for the opportunity to materialize; what could close the window (incumbent expansion, regulatory change); capability and GTM gaps; where speed matters.
4. **Recommended Actions (~400 words)** — Prioritized, time-bound. Near-term (0–2 years) and medium-term (2–5 years). Which banks to approach first and why (from Target Universe). Capability and partnership priorities.
5. **Executive Summary (~400 words)** — Written last. Covers both Part I and Part II. A board member who reads only this understands the opportunity, Zeta's position, and recommended action.

---

## 5. Phase 4: Review

### Part I checks

- Every data point has a source citation with a navigable, verified URL — or full bibliographic detail for paywalled sources.
- No broken links — every URL resolves to the cited content.
- No "according to [authority]" without a traceable reference.
- All unverifiable claims flagged as `[unverified — needs manual confirmation]`.
- No structural shift relies on assertion without evidence.
- Segment analysis (Tier 1/2/3) grounded in research.
- Geographic analysis specific to selected markets (USA, India, +1 if any).
- No Zeta references, product names, or commercial voice in Part I.
- Every bank in the Target Universe has a citable evidence basis with navigable source link.
- Document reads as external strategic analysis.

### Part II checks

- Every recommendation traces back to evidence in Part I.
- Gaps and weaknesses stated honestly.
- Recommendations specific and prioritized; "do not pursue" / "delay" included where warranted.
- Product and fabric references accurate against repo product-line files (Evolution Fabric, Quark, CAF, Trust, Truth).

### Editorial rigor (Part I only)

Apply all eight tests from `.cursor/skills/editorial-rigor-review/SKILL.md`: sentence economy, tonal consistency, no commercial voice, no meta-narration, vocabulary discipline, shelf life, specificity vs. thesis level, audience neutrality.

---

## 6. Key Differences from Other Engagement Areas


| Dimension                      | Payments                                                       | Cloud & Platform Operations                                             | Agentic Operations (current doc)                                            | Banking Operations (this plan)                                                                                                                                                                                                           |
| ------------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Market structure**           | Single banking category; analyst-sized.                        | Horizontal tech market; banking segment derived.                        | Capability catalogue; no standalone TAM.                                    | **Constructed category** — reconciliation, compliance, fraud, collections, credit ops, regulatory reporting aggregated. No single "banking operations" TAM.                                                                              |
| **Competitive landscape**      | Banking-focused incumbents (FIS, Fiserv) + modern challengers. | Horizontal giants (Datadog, ServiceNow) + cloud native.                 | Not yet analyzed as competitive landscape.                                  | **Fragmented** — reconciliation (SmartStream, Duco, FIS, Fiserv), AML/compliance (NICE, SAS, Verafin), fraud (NICE, SAS), collections (FIS, Fiserv, FICO), RegTech (AxiomSL, Wolters Kluwer); plus horizontal (ServiceNow, Pegasystems). |
| **Primary driver**             | Real-time payments + technology debt.                          | Operational complexity + resilience regulation (DORA, OCC).             | AI agents in middle/back office; substrate (model, governance).             | **Operations cost and volume vs. headcount** + regulatory intensity (AML, sanctions, reporting) + knowledge concentration + shift to continuous operations and auditability.                                                             |
| **Geographic concentration**   | USA, India, UK/EU, Brazil.                                     | USA, EU (DORA), India.                                                  | Not specified.                                                              | **USA primary, India accessible,** at most 1 additional (e.g. UK/EU for regulatory reporting).                                                                                                                                           |
| **Central strategic argument** | Banks must replace aging payment infrastructure.               | Horizontal cloud ops tools insufficient for banking-grade requirements. | Banks need operational model and governance to deploy agents in operations. | **Operations cost and regulatory pressure force investment in operations infrastructure and process platforms;** knowledge concentration and continuous operations create demand for explicit, auditable, AI-ready operational models.   |
| **Zeta's position**            | Strong — Photon and payments product lines.                    | Platform-dependent — Cloud Fabric.                                      | Evolution Fabric, Quark, CAF, Trust, Truth.                                 | **Same fabrics and Quark** — but sold as operations infrastructure and agentic-operations substrate; competition from FIS/Fiserv/NICE/ServiceNow in operations domains.                                                                  |
| **Analyst coverage**           | Strong.                                                        | Strong for horizontal; none for "banking cloud ops."                    | Thin — emerging.                                                            | **Fragmented** — AML/compliance (Chartis, Aite), reconciliation (Celent, Gartner), fraud (Javelin, Aite); no single "banking operations" report.                                                                                         |
| **Key risk**                   | Legacy entrenchment.                                           | Horizontal vendors add banking features.                                | Category and substrate not yet proven at scale.                             | **Incumbents own operations budgets;** "operations platform" may be sold as modules (reconciliation, AML, collections) rather than unified category.                                                                                     |


---

## 7. Execution Approach

### Sub-agent batching strategy

Six to seven research streams; max 4 concurrent sub-agents.

**Batch 1 (4 concurrent):**

- Stream 1: Market sizing and revenue pools  
- Stream 2: Regulatory landscape and operations mandates  
- Stream 3: Competitive landscape  
- Stream 4: Structural shifts and bank operations modernization activity

**Batch 2 (2–3 concurrent):**

- Stream 5: Reconciliation and exception platforms  
- Stream 6: Compliance operations and regulatory reporting technology  
- Stream 7: Operations cost, headcount, and capacity evidence

### Estimated turns


| Phase                               | Estimated turns   |
| ----------------------------------- | ----------------- |
| Phase 1, Batch 1 (Streams 1–4)      | 1 turn (parallel) |
| Phase 1, Batch 2 (Streams 5–7)      | 1 turn (parallel) |
| Phase 2: Synthesis and gap-fill     | 2 turns           |
| Phase 3: Part I writing             | 2–3 turns         |
| Phase 3: Part II writing            | 1–2 turns         |
| Phase 4: Review and editorial rigor | 1–2 turns         |
| **Total**                           | **8–12 turns**    |


### Output file path

`org-8.0/what-we-sell/strategy/engagement-areas/banking-operations.md`

---

## 8. Output Files

### Primary document

`org-8.0/what-we-sell/strategy/engagement-areas/banking-operations.md` — **creates** the two-part opportunity analysis and advisory (no existing file under this name).

### Research retention

**Location:** `org-8.0/what-we-sell/strategy/_research/banking-operations/`

**Files to create:**


| File                                       | Contents                                                                                                                                                                                  |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `s1-market-sizing.md`                      | TAM by sub-segment (reconciliation, compliance, fraud, collections, credit ops, regulatory reporting). Geography and tier. Derivation methodology. Claim/Value/Source/URL/Verified table. |
| `s2-regulatory-landscape.md`               | USA, India, (UK/EU if applicable) regulations on AML, sanctions, fraud reporting, regulatory reporting, operational risk. Deadlines, penalties, infrastructure implications.              |
| `s3-competitive-landscape.md`              | By-category competitor profiles. Revenue, positioning, banking operations scope, strengths, weaknesses, vulnerabilities. Bank modernization signals with URLs.                            |
| `s4-structural-shifts.md`                  | Evidence for each structural shift. Data points, regulatory citations, bank-tier and geographic analysis. Bank signals with URLs.                                                         |
| `s5-reconciliation-exception-platforms.md` | Reconciliation and exception management market and vendors. Bank modernization evidence.                                                                                                  |
| `s6-compliance-regulatory-reporting.md`    | Compliance operations and regulatory reporting TAM and vendors. Regulatory and competitive evidence.                                                                                      |
| `s7-operations-cost-headcount.md`          | Operations cost share, FTE/capacity evidence, wage/attrition, automation/AI adoption evidence.                                                                                            |
| `synthesis-notes.md`                       | Cross-references, contradictions, evidence quality ratings, R2P/R2W mapping, target universe assembly, editorial decisions.                                                               |
| `unverified-claims.md`                     | Every claim flagged as `[unverified — needs manual confirmation]` with context.                                                                                                           |


**Format for stream files:**

- Research date and engagement area  
- Data table: Claim | Value | Source | URL | Verified (Yes/No)  
- Key findings as structured bullets  
- Gaps and unresolved questions  
- Raw notes and excerpts for future use

**Cross-referencing:**

- `org-8.0/what-we-sell/strategy/_research/cloud-and-platform-operations/` — DORA/operational resilience (s2), agentic operations evidence (gap-fill). Reference in synthesis-notes.md; do not re-research.  
- `org-8.0/what-we-sell/strategy/engagement-areas/agentic-operations.md` — current capability catalogue; Part II will map Zeta's assets (Evolution Fabric, Quark, CAF) to the Banking Operations opportunity and distinguish this analysis from the agentic-operations catalogue.

---

## 9. What This Plan Does NOT Do

- Does not write the opportunity analysis itself; it only defines the research and writing plan.  
- Does not produce a generic plan; streams, shifts, competitors, and regulations are specific to Banking Operations (run-the-bank).  
- Does not include more than 4 geographic markets (USA, India, and at most 1–2 additional with justification).  
- Does not plan for a document shorter than 4,000 or longer than 8,000 words.  
- Does not blend analyst and advisor voices; Part I and Part II are structurally separated.  
- Does not include banks in the Target Universe without specifying evidence sources and requiring navigable URLs.  
- Does not cite any source without a navigable URL or full bibliographic detail; does not fabricate URLs.  
- Does not discard research output; every stream's raw findings are saved to `_research/banking-operations/`.

