# Unverified Claims — Cloud and Platform Operations

**Date:** 2026-03-15
**Engagement area:** Cloud and Platform Operations

Every claim below was flagged as `[unverified — needs manual confirmation]` during research. Organized by stream with context on where the claim is needed and what source was attempted.

---

## Stream 1: Market Sizing

| # | Claim | Context | Source Attempted | Resolution Needed |
|---|---|---|---|---|
| 1 | BFSI-specific AIOps market share (18-22% estimate) | Part I Market section — banking TAM derivation | No analyst publishes BFSI % of AIOps market | Accept derived estimate with transparent methodology |
| 2 | Vendor revenue by industry vertical (Datadog, Dynatrace, PagerDuty) | Competitor financial analysis | 10-K filings do not segment by industry | Cannot resolve — use total revenue as proxy |
| 3 | Grafana Labs revenue (~$400M ARR) | Competitive landscape | Private company; $400M ARR confirmed from press release Sep 2025 | Resolved — verified |
| 4 | Splunk/Cisco observability revenue post-acquisition | Competitive landscape | Not separately disclosed by Cisco | Cannot resolve |
| 5 | India-specific cloud ops market sizing | Geographic analysis for India | No India-specific observability/AIOps market data exists | Use APAC share (42% of global FS IT) with India estimated at 15-20% of APAC |
| 6 | Observability cost as % of cloud spend (FS-specific) | Consolidation pressure argument | 20-30% figure is cross-industry (Honeycomb). No FS-specific measurement. | Present cross-industry figure; note FS likely higher due to compliance requirements |

## Stream 2: Regulatory Landscape

| # | Claim | Context | Resolution Needed |
|---|---|---|---|
| 7 | DORA TLPT scope and timing — which institutions required | Shift 3 (operational resilience) | First notifications expected 2026; await national authority specifications |
| 8 | RBI IT outsourcing — cloud-specific provisions beyond general direction | India cloud governance | Review complete set of RBI circulars |
| 9 | ECB SREP ICT risk capital add-on quantum | ECB capital consequences argument | Methodology not publicly documented in detail |
| 10 | CERT-In 6-hour enforcement data | India incident reporting | No public enforcement data on late reporting penalties |

## Stream 3: Competitive Landscape

| # | Claim | Context | Resolution Needed |
|---|---|---|---|
| 11 | Temenos ARR ($804.2M +12% CC) | Banking technology platform analysis | Source (MarketScreener) partially verified; needs Temenos IR confirmation |
| 12 | Morpheus Data estimated revenue ($5-25M) | Cloud management category | Private company; range from Owler/GrowJo |
| 13 | Wipro FY2025 revenue (~$10.5-11B) | Managed services | Could not retrieve; estimated |
| 14 | New Relic taken private for ~$6.5B | Competitive landscape | Widely reported but SEC confirmation not retrieved |

## Stream 4: Structural Shifts

| # | Claim | Context | Resolution Needed |
|---|---|---|---|
| 15 | Observability cost as 15-30% of cloud spend | Shift 2 core claim | Multiple cross-industry sources; no single authoritative source. Honeycomb states 20-30%. |
| 16 | SRE-to-service ratios in banking | Shift 8 cost argument | No published banking-specific data |
| 17 | Tier 1 bank SRE headcount (estimated 100-500+) | SRE cost scaling argument | Inferred from hiring patterns and estate size; no bank discloses |
| 18 | Multi-cloud governance cost (2-3x single cloud) | Shift 5 cost argument | No published banking data confirms the multiplier |

## Stream 5: AIOps and Agentic Operations

| # | Claim | Context | Resolution Needed |
|---|---|---|---|
| 19 | Banking-specific auto-resolution rates | Agentic operations maturity | No bank has published auto-resolution percentages. ServiceNow's 90% is their own help desk. |
| 20 | MTTR improvement from agentic ops in banking | Agentic operations value | All vendor-stated: PagerDuty 50%, New Relic 25%, Dynatrace 3x. No independent verification. |
| 21 | Regulatory position on autonomous remediation | Banking adoption barrier | No regulator has issued specific guidance on AI agents taking autonomous operational actions. |
| 22 | Dynatrace benchmark (12x more accurate, 3x faster, half cost) | Competitive analysis | Vendor-stated benchmark — architecturally plausible but not independently verified. |

## Stream 6: Banking Cloud Governance

| # | Claim | Context | Resolution Needed |
|---|---|---|---|
| 23 | Quantified banking downtime cost per hour | Availability governance | New Relic: $1.8M/hr for FS high-impact outages. Industry estimates vary. |
| 24 | Datadog/Dynatrace banking-specific compliance modules | Banking-specific gaps | Cannot verify whether vendors offer banking-specific PII pattern libraries beyond generic scanning. |
| 25 | Five nines (99.999%) banking availability commitment | Availability expectations | DORA's 2-hour threshold implies high availability but no source confirms contractual 99.999%. |
| 26 | MAS penalty on DBS (6-month IT pause) | Enforcement evidence | Referenced in DBS 2023 Annual Report; direct MAS enforcement notice not located. |
| 27 | CrowdStrike July 2024 outage — banking-specific impact | Availability risk evidence | Known to have affected financial services but specific banking impact data not retrieved. |

---

## Resolution Strategy

**For Part I writing:**
- Claims 1, 5, 6, 15, 16, 17, 18: Present with transparent methodology and caveats. These are derivations, not fabrications.
- Claims 19, 20, 21: Flag vendor claims as `[vendor-stated]` in the structural shifts section. Present the regulatory grey area honestly.
- Claims 7, 8, 9, 10: Note as evolving regulatory areas. Do not assert specifics that cannot be verified.

**For Part II writing:**
- Claims 22, 24: Relevant to competitive positioning. Present Zeta's capabilities without claiming competitors lack features unless verified.
- Claims 11-14: Revenue figures are contextual. Use verified figures; note approximations.

**Cannot resolve without primary research / analyst engagement:**
- Claims 2, 4, 6, 9, 16, 17, 19, 24 — these require proprietary data (vendor revenue segmentation, analyst reports, or bank internal data) not available through web research.
