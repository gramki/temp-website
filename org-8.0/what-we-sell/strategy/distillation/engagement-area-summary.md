# Engagement Area Portfolio Summary

*Prepared for strategic deliberation. March 2026.*

---

## 1. Purpose and Limitations

This document places all eleven engagement areas on a common decision surface — Right to Play, Right to Win by customer segment, opportunity size, product alignment, and production evidence — organized by strategic posture.

**What this document does:** synthesizes the R2P/R2W assessments, market sizing, competitive positioning, and production evidence from each engagement area analysis into a single view that supports portfolio-level deliberation.

**What this document does not do:** recommend a portfolio. Portfolio decisions require judgment on deal velocity, engagement economics, sales capacity, competitive dynamics in live deals, and internal engineering allocation — inputs this analysis cannot provide.

**Framework reference:** `how-to.md` defines the Right to Play / Right to Win framework used throughout. R2P assesses market attractiveness and structural demand. R2W assesses Zeta's competitive advantage in each segment.

**Pillar structure:** Engagement areas are organized by strategic posture, not market taxonomy:

- **Pillar 1 — Product-Led Expansion.** Areas where Zeta has production-validated products and can expand from demonstrated capability.
- **Pillar 2 — Category Creation.** Areas where no established vendor category exists and Zeta's fabric architecture addresses a structural gap, but zero production evidence exists.
- **Pillar 3 — Enabling Infrastructure.** Areas that may function as standalone engagement areas or as capabilities that enlarge and deepen Pillar 1 and 2 engagements.

**A note on Tier 1 banks:** R2W is Weak or Very Weak across nearly all engagement areas for Tier 1 US banks (JPMorgan, Bank of America, Wells Fargo, Citi). These institutions build internally, have deep incumbent vendor relationships, and present prohibitive sales cycles. Tier 1 is excluded from the overview table. Individual engagement area documents address Tier 1 positioning where relevant.

---

## 2. Portfolio-at-a-Glance

| Pillar | Engagement Area             | TAM (2025)   | CAGR       | Primary Product         | Production Evidence                                                                | Primary Buyer            | R2P (Tier 2 US) | R2W (Tier 2 US)                 | R2W (India)                      | Preliminary Verdict                          |
|--------|----------------------------|--------------|------------|------------------------|------------------------------------------------------------------------------------|--------------------------|-----------------|-------------------------------|-----------------------------------|----------------------------------------------|
| 1      | Payments                   | $60–85B      | 12–15%     | Photon                 | **Yes.** 3 credit card programs, multiple DDA programs in US production            | CTO                      | Strong          | Medium-Strong                 | Strong                            | **Pursue**                                    |
| 1      | Account Products           | $25–40B      | 9–14%      | Tachyon                | **Yes.** 3 credit card programs, multiple DDA programs (Optum, loyalty) in US      | CTO                      | Strong          | Medium-Strong                 | Medium                            | **Pursue**                                    |
| 1      | Commercial Cards           | $28–30B      | 15–20%     | Electron               | **Partial.** Benefits proven at scale (Pluxee India, 11K+ corporates). Expense/Purchase unvalidated | Corporate Banking        | Strong          | Partial                       | Strong                            | **Pursue with investment**                    |
| 1      | Lending and Credit         | $25–30B      | 14–18%     | Tachyon Loans + CAF    | **No.** Tachyon Loans = "To be expanded." AI governance (CAF) is architecturally ready | CRO / CCO                | Strong          | Weak (platform) / Unique (governance) | Medium                       | **Pursue governance; delay platform**         |
| 2      | Banking Operations         | $19–27B      | 12–15%     | Evolution Fabric       | **No.** Architecture maps; no external deployment                                  | COO                      | Strong          | Medium (category creation)      | Medium                            | **Build-then-pursue**                         |
| 2      | Compliance Operations      | $11–15B      | 16–19%     | Evolution Fabric + CAF | **No.** Greenfield. Zero compliance domain presence                                | CCO / BSA Officer        | Strong          | Medium (no incumbent in orchestration) | Weak                        | **Build-then-pursue**                         |
| 2      | Agentic Banking            | $5–6B (2030) | 25–45%     | Evolution Fabric (Hub + Seer) | **No.** No reference deployments. No conversational AI capability             | CTO / Head of Digital    | Strong          | Medium (operational model gap is real) | Medium                      | **Build-then-pursue**                         |
| 3      | Cloud and Platform Ops     | $8–10B       | 12–15%     | Cloud Fabric           | **Internal only.** Runs Zeta's own banking estate                                  | CIO                      | Strong          | Medium                         | Medium (managed services barrier) | **Requires deliberation**                     |
| 3      | Digital Identity and Trust | $30B+        | 14–15%     | Trust Fabric           | **No.** Architectural alignment only                                               | CISO                     | Strong          | Medium                         | Weak (Aadhaar integration needed)  | **Requires deliberation**                     |
| 3      | Customer Lifecycle         | $26–33B      | 13–17%     | Quark CLM              | **No.** Quark hubs = "to be expanded"                                              | CMO / CX Head            | Strong          | Medium                         | Medium                            | **Requires deliberation**                     |
| 3      | BaaS and Embeddable Banking| $27–30B      | 13–18%     | Multi-product platform | **Indirect.** Tachyon + Photon production-proven; no BaaS-specific deployment      | Digital Banking          | Strong          | Medium                         | Strong                            | **Pursue (India); build-then-pursue (US)**    |

**Reading the table:** R2P is Strong across the board — every area addresses a real, growing, evidence-backed market need. The differentiation lies in R2W, which separates areas where Zeta has earned competitive advantage (Pillar 1) from areas where competitive advantage is architectural but unproven (Pillars 2 and 3).

---

## 3. Pillar 1 — Product-Led Expansion

*Strategy: Expand from production evidence. Increase the engagement surface for Tachyon and Photon. Create visibility.*

| Area             | Product                       | Production Status                                                                                           |
|------------------|------------------------------|-------------------------------------------------------------------------------------------------------------|
| Payments         | Photon                       | In production (US) – card payment processing for 3 credit card programs and multiple DDA programs           |
| Account Products | Tachyon (Credit Cards + DDA) | In production (US) – 3 credit card programs, DDA programs (Optum health benefits, loyalty/rewards)          |
| Commercial Cards | Electron (on Tachyon)         | Benefits: proven at scale (Pluxee India, 11K+ corporates, 3.5M+ consumers). Expense/Purchase: unvalidated   |
| Lending and Credit | Tachyon Loans + CAF         | Governance: architecturally ready. Lending products: early-stage ("To be expanded")                        |

### Payments

**Opportunity.** $60–85B payments technology infrastructure market, 12–15% CAGR, projected to exceed $130B by 2030. Eight structural shifts — real-time payments as default rail, tokenization mandated, acquiring diversification, AI in payments operations. The most underserved segment is Tier 2–3 banks: legacy incumbents over-engineered, modern challengers designed for fintechs.

| Segment                               | R2P    | R2W           | Key Evidence                                                   | Key Gap                                  |
|----------------------------------------|--------|---------------|----------------------------------------------------------------|-------------------------------------------|
| Card issuance + tokenization (Tier 2 US)| Strong | Medium-Strong | Photon in US production; network tokenization mandates create urgency | Brand recognition absent; no analyst coverage |
| India card issuance + tokenization     | Strong | Strong        | Existing relationships; RBI tokenization mandate                | –                                         |
| Acquiring (Tier 2 US)                  | Medium | Weak          | $25–28B market                                                | No acquiring references; no merchant onboarding |
| Payment hub orchestration (Tier 1)     | Strong | Weak          | 87% of FIs plan modernization                                 | Volante is Gartner Leader; ACI has incumbency   |
| Embedded payments / BaaS (Tier 2 US)   | Strong | Medium        | 80%+ of TAM unpenetrated                                      | No BaaS-specific packaging                   |

**Production evidence.** Photon processes authorization, clearing, and settlement for three credit card programs and multiple DDA programs in the US (health benefits via Optum, loyalty/rewards).

**Highest-risk competitor.** Marqeta — modern card issuing platform with Tier 2 bank relationships, analyst recognition, and public company visibility.

**Verdict: Pursue.** Lead with card issuance + tokenization at Tier 2 US banks and India. Defer acquiring and payment hub orchestration. The production evidence is real; the gap is visibility, not capability.

### Account Products and Core Banking

**Opportunity.** $25–40B market, 9–14% CAGR. Progressive core replacement displacing big-bang migration. Cloud-native infrastructure becoming default. 53% bank dissatisfaction with core providers. Mid-market banks ($10–100B) most underserved.

| Segment                               | R2P    | R2W           | Key Evidence                                                         | Key Gap                                                |
|----------------------------------------|--------|---------------|----------------------------------------------------------------------|--------------------------------------------------------|
| Progressive core migration (Tier 2 US) | Strong | Medium-Strong | Tachyon in US production; market fragmented (top 3 hold 30.1%)       | Purpose-specific programs, not full-service core; no analyst coverage |
| India retail/business banking          | Strong | Medium        | Existing banking relationships                                       | Must demonstrate beyond credit cards and purpose-specific DDA         |
| Digital account platform (Tier 2 US)   | Strong | Weak          | $37–46B digital banking market                                       | Alkami ($444M rev), Q2 ($795M rev), Backbase dominate                |
| BaaS enablement (Tier 2)               | Strong | Medium        | Post-Synapse demand; Tachyon validates multi-tenant architecture     | BaaS-specific packaging not yet developed                            |

**Production evidence.** Tachyon Credit Cards powers three credit card programs in the US. Tachyon DDA powers multiple demand deposit account programs (health benefits, loyalty/rewards). All use Photon for payment rail processing.

**Highest-risk competitor.** Thought Machine — cloud-native core platform with Tier 1 references (Lloyds, Standard Chartered, JPMorgan partnership) and growing mid-market presence.

**Verdict: Pursue.** Target Tier 2 US banks ($10–100B) with Tachyon + Photon + Evolution Fabric. Convert existing deployments into referenceable case studies as the immediate priority. The gap is market visibility, not product readiness.

### Commercial Cards

**Opportunity.** $28–30B technology TAM growing to $75–90B by early 2030s. Commercial card spend crossed $4T globally but represents only 4% of $80T B2B payments. Virtual cards displacing checks. Card issuance and spend management converging through M&A (Capital One–Brex $5.15B, Amex–Center, Paylocity–Airbase $325M).

| Segment                                    | R2P    | R2W     | Key Evidence                                                    | Key Gap                             |
|---------------------------------------------|--------|---------|-----------------------------------------------------------------|--------------------------------------|
| India benefits cards (Tier 2–3)             | Strong | Strong  | Pluxee: 11K+ corporates, 3.5M+ consumers. IDFC FIRST, RBL partnerships | Zaggle is primary competitor         |
| Multi-program commercial card (India + US Tier 2) | Strong | Partial | Electron Benefits proven; Tachyon Credit in US production        | Expense/Purchase unvalidated         |
| US enterprise T&E                           | Strong | Weak    | Large market                                                    | SAP Concur and Ramp entrenched       |
| Fleet cards                                 | Weak   | Weak    | Vertically integrated                                            | Poor fit                            |

**Production evidence.** Electron Benefits is production-proven at scale — Pluxee India (11,000+ corporates, 3.5M+ consumers) and direct bank partnerships (IDFC FIRST, RBL). India meal card tax exemption proposed 4x increase would expand addressable market.

**Highest-risk competitor.** Zaggle — direct-to-corporate model in India benefits; Brex (now Capital One) — integrated issuance + expense management in US.

**Verdict: Pursue with investment.** Expand India benefits card partnerships (3–5 new banks). Validate Electron Expense Cards through pilot before positioning multi-program commercial card platform. Defer US enterprise T&E.

### Lending and Credit

**Opportunity.** $25–30B vendor-addressable lending technology market, projected $60–80B by 2030–2033. Lending generates 50–70% of bank revenue but has received less modernization investment than payments or core banking. AI/ML decisioning crossing from optional to regulated (EU AI Act August 2026, Colorado AI law June 2026). No vendor covers the full lending lifecycle with integrated AI governance.

| Segment                        | R2P    | R2W     | Key Evidence                                                   | Key Gap                                         |
|---------------------------------|--------|---------|----------------------------------------------------------------|--------------------------------------------------|
| AI governance in lending (all tiers) | Strong | Unique  | Evolution Fabric + CAF = only integrated AI governance platform for lending | Not a lending product sale – governance overlay on existing infrastructure |
| Consumer origination (India)    | Strong | Medium  | Active banking relationships; 31.5% CAGR                       | Tachyon Loans = "To be expanded"                 |
| Consumer origination (US)       | Strong | Weak    | $18–22B market                                                | No US lending references; no demonstrated capability |
| Commercial lending              | Strong | Weak    | 41% of banks use spreadsheets                                  | nCino has 2,700+ customers                       |
| Mortgage                        | Strong | Very Weak | ICE ~50% LOS share                                             | Permanent exclusion                              |

**Production evidence.** None for lending products. Tachyon Loans and Quark Lending are declared but not deployed. The AI governance position (Evolution Fabric + CAF) is architecturally ready and unique in the market — but governance without a lending platform is a consulting sale, not a product sale.

**Highest-risk competitor.** nCino — 2,700+ customers including recent enterprise wins, expanding from commercial into consumer lending with AI.

**Verdict: Pursue governance immediately; delay platform.** Ship AI governance for lending by Q2 2026 to capture EU AI Act and Colorado compliance waves. Mature Tachyon Loans through India deployments (2–3 consumer lending deployments within 18 months). Enter US with governance-first positioning, expand to platform once India references exist.

### Pillar 1 Deliberation Questions

1. **Which adjacency first — Commercial Cards or Lending?** Commercial Cards has India production evidence; Lending has a regulatory urgency window (EU AI Act August 2026). These compete for product and sales attention.
2. **Can Pillar 1 areas generate $2M+ engagements, or are they bundled into platform deals?** Credit card and DDA program implementations at mid-market banks may generate $2–5M engagements individually; the more common model may be multi-product platform deals that bundle several Pillar 1 areas.
3. **How many Pillar 1 buying events exist per year?** The core banking replacement cycle at Tier 2 US banks generates an estimated 15–25 evaluations per year. Card issuance evaluations may be somewhat more frequent. These numbers cannot be verified through analysis — they require sales intelligence.
4. **What is the conversion rate from "production evidence exists" to "referenceable case study"?** Current US deployments are not publicly referenceable. Converting them is the single highest-leverage near-term action.

---

## 4. Pillar 2 — Category Creation

*Strategy: Identify high-traction potential areas with a differentiable positioning. Build product and double down to create category leadership.*

| Area               | Primary Fabric                                         | Category Status                  |
|--------------------|-------------------------------------------------------|----------------------------------|
| Banking Operations | Evolution Fabric (Hub + Seer), CAF, Truth Fabric      | No established vendor category   |
| Compliance Operations | Evolution Fabric + CAF + Trust Fabric + Truth Fabric | No established vendor category   |
| Agentic Banking    | Evolution Fabric (Hub + Seer), CAF, Trust Fabric      | Nascent, pre-category            |

### Banking Operations

**Opportunity.** $19–27B across six sub-domains (reconciliation, compliance ops, fraud ops, collections, credit ops, regulatory reporting), 12–15% CAGR. Compliance operations growing fastest at 16–19%. Operations volumes outstripping staff capacity. Regulatory enforcement at record intensity (TD Bank $3.09B penalty). AI entering operations but only 17% of institutions have governance frameworks.

**Category thesis.** The "unified banking operations model" — an explicit, governed model for operations work that spans multiple sub-domains with decision auditability. No vendor occupies this intersection.

| Segment                                    | R2P    | R2W       | Recommendation                                 |
|---------------------------------------------|--------|-----------|------------------------------------------------|
| Compliance operations workflow (Tier 2 US)  | Strong | Medium    | Pursue near-term                               |
| Reconciliation (Tier 2 US/India)            | Strong | Medium    | Pursue near-term (Truth Fabric)                |
| India (Tier 1–2, RBI enforcement)           | Strong | Medium    | Pursue near-term                               |
| Operations model modernization (all tiers)  | Strong | Medium    | Pursue medium-term                             |
| Regulatory reporting (G-SIBs)               | Strong | Very Weak | Do not pursue (AxiomSL: 90% G-SIB penetration) |
| Pure-play AML detection                     | Strong | Weak      | Do not pursue (NICE Actimize, SAS entrenched)  |

**Category creation investment.** Quark Operations hub must be built from scratch (compliance, fraud, collections, reconciliation, regulatory reporting sub-domains). No pre-built domain hubs exist. Requires deep domain expertise hire — compliance, reconciliation, collections operations practitioners.

**Verdict: Build-then-pursue.** Start with compliance operations workflow and reconciliation at Tier 2 US banks. Secure one India production reference (RBI enforcement creates receptive conditions). Position CAF as a standalone compliance audit layer alongside existing detection engines (NICE, SAS) as the market entry wedge.

### Compliance Operations

**Opportunity.** $11–15B vendor-addressable compliance technology market, 16–19% CAGR. $206B annual global financial crime compliance spending, 57–79% is labor cost. 2024 was a record year at $10.4B in global AML fines. 80% of compliance leaders plan AI adoption within 18 months but only 17% have governance frameworks.

**Category thesis.** The "Compliance Operations Center" — an orchestration and governance layer above existing compliance point solutions that provides cross-domain workflow, unified decision auditability, and continuous examination readiness. No vendor fills this structural gap.

| Segment                                    | R2P    | R2W            | Recommendation                              |
|---------------------------------------------|--------|----------------|---------------------------------------------|
| Compliance ops orchestration (Tier 2 US)    | Strong | Medium         | **Pursue as primary**                       |
| KYC/CDD workflow orchestration (Tier 2 US)  | Strong | Medium         | **Pursue as secondary** (Trust Fabric alignment) |
| Compliance AI governance (EU AI Act)        | Strong | Medium-Strong  | **Pursue as differentiator** (CAF advantage)|
| AML transaction monitoring                  | Strong | Weak           | Do not pursue (32+ established vendors)     |
| Regulatory reporting                        | Strong | Very Weak      | Do not pursue (AxiomSL dominance)           |
| G-SIB compliance                            | Strong | Very Weak      | Do not pursue                               |

**Category creation investment.** Compliance domain leader hire (former BSA Officer / CCO). Compliance Operations Hub prototype. Compliance tool integrations (NICE Actimize, Alloy, AxiomSL). Market education and analyst engagement (Celent, ACAMS). Entirely new buyer community (CCO/BSA Officer) distinct from existing CTO relationships.

**Verdict: Build-then-pursue.** Highest-urgency buyer segment is US banks under or emerging from consent orders ($2B+ combined remediation investment). EU AI Act deadline (August 2026) creates compliance AI governance buying event. The fabric architecture is genuinely differentiated for the orchestration gap — but everything else (domain expertise, integrations, buyer relationships, analyst coverage) must be built from zero.

### Agentic Banking

**Opportunity.** $5–6B by 2030, 25–45% CAGR from nascent base. New category forming at the intersection of AI agent platforms, banking domains, and customer relationships. Current vendor landscape frames the opportunity through the contact center; the broader surface — advisory, product optimization, credit management, life event orchestration, SME operational banking — is unaddressed.

**Category thesis.** AI agents as governed participants in the banking relationship, operating across the full customer-facing surface. The binding constraint is the operational model, not AI capability. Hub provides the only platform-level answer to this constraint.

| Domain                                  | Timing                | Rationale                                             |
|------------------------------------------|-----------------------|-------------------------------------------------------|
| Consumer servicing / dispute resolution  | Entry (0–12 months)   | Highest volume, structured patterns, regulatory forcing|
| Proactive advisory / product optimization| Second-move (12–24 months) | Same platform, new domain Scenarios               |
| Credit management / life events          | Third-move (24–36 months)  | Cross-Hub composition                             |
| SOHO/SME operational banking             | India expansion (18–36 months) | $335–360B MSME credit gap                     |

**Category creation investment.** Conversational AI partnership (Personetics, Kasisto, or Yellow.ai). 30+ production-grade Quark Customer Servicing Scenarios. Domain models for advisory, product optimization, credit management. Analyst relations to position the operational model approach.

**Verdict: Build-then-pursue.** Lead with consumer dispute resolution at Tier 2 US banks. Design platform engagement from day one to span the broader surface. Secure conversational AI partnership. The window is 2026–2028 before a convergence event (Salesforce acquiring a banking domain specialist, Personetics building execution capability) closes the operational model gap.

### Pillar 2 Deliberation Questions

1. **Which category bet first — Banking Operations, Compliance Operations, or Agentic Banking?** All three depend on Evolution Fabric. Compliance Operations has the most time-bounded forcing function (EU AI Act August 2026, enforcement wave). Agentic Banking has the largest long-term market. Banking Operations has the broadest surface. They compete for the same platform engineering investment.
2. **Is Agentic Banking standalone or a capability that strengthens Pillar 1 and other Pillar 2 areas?** If agentic capabilities are embedded within Payments and Account Products engagements, the $5–6B market may be captured without a standalone go-to-market.
3. **Category creation requires different buyers.** Banking Operations sells to COO. Compliance Operations sells to CCO/BSA Officer. Agentic Banking sells to CTO/Head of Digital. Pursuing all three simultaneously requires three distinct go-to-market motions beyond Zeta's existing buyer relationships.
4. **What is the realistic timeline from "fabric exists" to "first referenceable deployment"?** Each Pillar 2 area requires domain expertise hire, domain model build, and buyer relationship development. Realistic estimate: 12–18 months from investment decision to first deployable offering. This cannot be compressed significantly.

---

## 5. Pillar 3 — Enabling Infrastructure

*Question: Are these standalone engagement areas or capabilities that make Pillar 1 and Pillar 2 engagements larger and stickier?*

| Area                        | Primary Fabric              | Enabling Role                                                     |
|-----------------------------|----------------------------|-------------------------------------------------------------------|
| Cloud and Platform Ops      | Cloud Fabric               | Deployment infrastructure for all Zeta products                   |
| Digital Identity and Trust  | Trust Fabric               | KYC/authentication layer – serves Payments, Account Products, Compliance         |
| Customer Lifecycle          | Quark CLM + Evolution Fabric | Spans onboarding, servicing, cross-sell across product areas      |
| BaaS and Embeddable Banking | Multi-product, multi-fabric | Platform architecture for bank-as-a-service delivery              |

### Cloud and Platform Operations

**Opportunity.** $8–10B banking cloud operations market across observability, AIOps, incident management, Kubernetes governance, and cloud management. DORA, PRA, OCC mandates create non-discretionary compliance spending. No vendor covers all five operational domains with banking-grade tenant isolation, data sovereignty, and regulatory-grade operational records.

**Standalone vs. enabler.** Cloud Fabric operates in production on Zeta's own banking estate — the strongest internal validation of any fabric. The strategic question is whether banks will procure Cloud Fabric as a standalone platform (competing with Datadog, ServiceNow, Grafana) or whether it functions as the deployment substrate that makes Pillar 1 and 2 engagements operationally excellent. The compliance governance surface positioning — reducing the cost of maintaining seven separate compliance evidence chains — favors standalone. But no external bank deployment exists.

**Verdict: Requires deliberation.** Pursue Tier 2 banks (US, UK/EU) if standalone positioning is validated. If not, fold Cloud Fabric into the delivery architecture for all engagements and remove from the standalone engagement area list.

### Digital Identity and Trust

**Opportunity.** $30B+ market at 14–15% CAGR across CIAM, identity verification, authentication, consent management, fraud analytics, and non-human identity. PE has deployed $13B+ assembling identity portfolios (Thoma Bravo, Permira). Convergence is inevitable but not yet achieved. AI agent identity is an emerging sub-segment no vendor addresses.

**Standalone vs. enabler.** Trust Fabric's AI agent identity governance (Trust Fabric + Seer) is the wedge capability no competitor offers — directly relevant to EU AI Act compliance. Consent-as-infrastructure addresses the 20-state US privacy patchwork. These capabilities are also enabling layers for Compliance Operations (KYC lifecycle), Agentic Banking (agent identity), and Payments (authentication). Can Trust Fabric generate $2M+ standalone identity engagements, or is it most valuable as a component of larger platform deals?

**Verdict: Requires deliberation.** AI agent identity governance has a time-bounded window (EU AI Act August 2026) that argues for near-term standalone pursuit. Broader identity capabilities may be better positioned as components within Pillar 1 and 2 engagements.

### Customer Lifecycle and Engagement

**Opportunity.** $26–33B market projected to reach $75–95B by 2030 across CRM, CDP, engagement/decisioning, contact center, and origination. Only 8% of FS leaders confident in unified customer view. 70% of banks lose clients during onboarding. 56-point gap between bank-perceived and customer-rated experience.

**Standalone vs. enabler.** Quark CLM and Quark Customer Lifecycle address the operational-model gap across the customer lifecycle — but all Quark hubs are marked "to be expanded." The lifecycle engagement capability is also an enabling layer for Account Products (origination-to-relationship), Payments (customer-centric servicing), and Agentic Banking (relationship context for AI agents). The standalone engagement area competes against Salesforce, Pega, NICE, and Alkami — entrenched incumbents with massive installed bases.

**Verdict: Requires deliberation.** May generate standalone $2M+ engagements if Quark hubs reach production readiness. More likely delivers value as the lifecycle layer within Pillar 1 platform deals. Consider retiring as a standalone engagement area and embedding lifecycle capability into Account Products and Agentic Banking narratives.

### BaaS and Embeddable Banking

**Opportunity.** $27–30B vendor revenue, 13–18% CAGR. Embedded finance beyond payments projected to grow 5.5x ($2B to $11B by 2026). $185B broader embedded finance TAM at only 17% penetration. Post-Synapse regulatory enforcement reshaping the market toward bank-owned infrastructure.

**Standalone vs. enabler.** BaaS is architecturally a multi-product platform play — Tachyon (accounts) + Photon (payments) + Electron (cards) + Trust Fabric (identity) + CAF (compliance). Tachyon and Photon are production-proven in the US, giving BaaS a stronger R2W foundation than other Pillar 3 areas. India BaaS (Federal Bank, Yes Bank, SBM Bank India) has the strongest combined R2P + R2W of any Pillar 3 segment. US BaaS faces a cold-start problem (no reference deployment).

| Segment                         | R2P    | R2W     | Recommendation                       |
|----------------------------------|--------|---------|--------------------------------------|
| Multi-product BaaS (India Tier 1–2) | Strong | Strong  | Pursue aggressively                  |
| Multi-product BaaS (US Tier 2–3)   | Strong | Medium  | Pursue (first deployment critical)   |
| Post-enforcement infrastructure (US)| Strong | Medium  | Pursue selectively                   |
| Embedded lending BaaS              | Strong | Weak    | Defer (Tachyon Loans not ready)      |
| UK BaaS                            | Medium | Weak    | Do not pursue                        |

**Verdict: Pursue India aggressively; build-then-pursue US.** BaaS has the strongest case for reclassification from Pillar 3 to Pillar 1 — it leverages production-proven products and has clear standalone $2M+ engagement potential. The deliberation question is whether to treat BaaS as a distinct go-to-market or as a delivery mode for Pillar 1 products.

### Pillar 3 Deliberation Questions

1. **Should BaaS be reclassified as Pillar 1?** It leverages production-proven products (Tachyon + Photon) and can generate standalone $2M+ engagements in India. The India BaaS opportunity may be the highest-probability near-term revenue path outside existing Pillar 1 areas.
2. **Should Customer Lifecycle be retired as a standalone engagement area?** If Quark hubs remain at "to be expanded" status, the standalone proposition is not viable. Lifecycle capabilities may be better embedded within Account Products and Agentic Banking narratives.
3. **Is Cloud and Platform Ops an engagement area or a delivery requirement?** If Cloud Fabric is positioned as the operational substrate for all Zeta deployments (which it already is internally), it may not need a standalone go-to-market.
4. **Can Digital Identity generate standalone $2M+ deals?** AI agent identity governance has a time-bounded opportunity (EU AI Act). If this window is pursued, it requires dedicated sales motion to CISOs and identity architects — a buyer community Zeta does not currently reach.

---

## 6. Cross-Cutting Observations

### Product line leverage

Evolution Fabric appears across all of Pillar 2, most of Pillar 3, and portions of Pillar 1. Investment in Evolution Fabric pays dividends across 6–8 engagement areas simultaneously. Tachyon spans all of Pillar 1 and BaaS. Photon spans Payments, Account Products, and BaaS. CAF appears in 7 of 11 areas. This concentration implies that platform investment priority should weight fabrics by cross-area leverage, not by individual engagement area attractiveness.

| Product/Fabric    | Pillar 1 Areas                                | Pillar 2 Areas     | Pillar 3 Areas             | Total |
|-------------------|-----------------------------------------------|--------------------|----------------------------|-------|
| Evolution Fabric  | 1 (Lending governance)                        | 3 (all)            | 2 (Customer Lifecycle, BaaS) | 6     |
| Tachyon           | 3 (Payments, Account Products, Commercial Cards) | 0                  | 1 (BaaS)                  | 4     |
| Photon            | 1 (Payments)                                  | 0                  | 1 (BaaS)                  | 2     |
| CAF               | 1 (Lending governance)                        | 3 (all)            | 3 (Cloud, Identity, Customer Lifecycle) | 7     |
| Trust Fabric      | 0                                             | 2 (Compliance, Agentic) | 2 (Identity, BaaS)      | 4     |

### Buyer concentration

Pillar 1 sells to CTO / Head of Products — one buyer community where Zeta has existing relationships. Pillar 2 sells to COO (Banking Ops), CCO/BSA Officer (Compliance), and CTO/Head of Digital (Agentic) — 2–3 new buyer communities. Pillar 3 is mixed: CIO (Cloud), CISO (Identity), CMO (Lifecycle), Digital Banking (BaaS). Pursuing all three pillars simultaneously requires at least four distinct go-to-market motions.

### The production evidence cliff

Pillar 1 has production evidence (Photon, Tachyon, Electron Benefits). Pillars 2 and 3 have zero external production deployments. This is the sharpest divide in the portfolio. It is the strongest argument for sequencing Pillar 1 expansion before Pillar 2 investment, and the strongest argument against diluting Pillar 1 resources to fund Pillar 2 prematurely.

### The $2M+ engagement filter

The stated goal is $2M+ engagements. Based on the analysis:

- **Pillar 1 areas can plausibly generate $2M+ engagements.** Core banking modernization, payment infrastructure, and multi-program card platforms at Tier 2 banks are $2–10M engagements.
- **Pillar 2 areas can generate $2M+ engagements if the category is established.** Banking operations transformation and compliance operations modernization are executive-sponsored programs at Tier 2 banks. But category creation extends the timeline.
- **Some Pillar 3 areas may not independently generate $2M+ engagements.** Cloud operations, identity, and customer lifecycle capabilities may be features within larger platform deals rather than standalone $2M+ line items. BaaS is the exception — multi-product BaaS platform deals at Tier 2 banks are $2M+ engagements.

### Geographic concentration

Across all 11 areas, the two geographies with the most consistent R2P + R2W combination are:

1. **Tier 2 US banks ($10–100B assets):** Primary target in 10 of 11 areas. Approximately 200 institutions in the target range. Regulatory enforcement creates urgency across payments, lending, compliance, and operations.
2. **India (Tier 1–2 banks):** Secondary target in 9 of 11 areas. Existing market presence, regulatory familiarity, and banking relationships reduce entry cost. Strongest R2W for Commercial Cards (benefits) and BaaS.

UK/Europe is tertiary: relevant primarily where regulatory forcing functions (DORA, PRA, EU AI Act, eIDAS 2.0) create time-bounded buying events.

---

## 7. The Deliberation Agenda

The following questions cannot be answered through analysis. They require judgment from specific leadership functions before portfolio decisions can be made.

### Questions only sales leadership can answer

- How many buying events per engagement area occur annually at Tier 2 US banks?
- What are realistic deal sizes and engagement economics for each area?
- What are win rates against named competitors in live evaluations?
- What is Zeta's current sales capacity, and how many simultaneous go-to-market motions can it support?
- Can existing US production deployments be converted to referenceable case studies? What is blocking this?

### Questions only product/engineering leadership can answer

- What is the realistic timeline to production readiness for each Quark hub currently at "to be expanded" status?
- How much engineering capacity can be allocated to Pillar 2 domain model development without degrading Pillar 1 product delivery?
- What is the build cost for compliance, banking operations, and agentic banking domain-specific Scenarios?
- Can conversational AI capability be acquired through partnership, or does it require internal build or acquisition?

### Questions only executive leadership can answer

- How many pillars to pursue simultaneously? Pillar 1 alone requires sustained investment; adding Pillar 2 doubles the engineering and go-to-market surface.
- What is the sequencing across and within pillars? The EU AI Act deadline (August 2026) creates a time-bounded opportunity for compliance AI governance and identity governance — but pursuing both simultaneously competes for the same fabric engineering resources.
- How to allocate between "expand from strength" (Pillar 1) and "create new category" (Pillar 2)? The production evidence cliff argues for Pillar 1 first. The category creation window argues for parallel investment.
- Should Pillar 3 areas remain standalone engagement areas, be reclassified, or be folded into Pillar 1/2 delivery narratives?
- Is India a primary revenue market or a reference-building market? The answer changes investment allocation for Commercial Cards, BaaS, and Lending.

---

*Source documents: eleven engagement area analyses in `engagement-areas/`, research files in `_research/`, framework definition in `distillation/how-to.md`.*
