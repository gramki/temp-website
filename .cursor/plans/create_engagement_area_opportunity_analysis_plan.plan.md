---
name: Create Engagement Area Opportunity Analysis Plan
overview: "Template plan to create a detailed research and writing plan for a McKinsey-grade two-part opportunity analysis and strategic advisory for any engagement area. Output is a .plan.md file in .cursor/plans/ tuned to that area."
todos:
  - id: inputs
    content: "Read all inputs: current engagement area file, distillation how-to, thesis, product-lines for area, archetype (if any), S.TODO, editorial-rigor-review skill, _research and market-study overlap, reference plan (payments or similar)."
    status: pending
  - id: model
    content: "Write Model Recommendation — orchestration vs research sub-agents, reasoning, impact of thin analyst coverage."
    status: pending
  - id: phase1
    content: "Write Phase 1 — Parallel Research (5–7 streams). Each stream: data to gather, sources, geography, document use, citation requirement; include bank-signals sub-task for competitive and structural-shifts streams."
    status: pending
  - id: phase2
    content: "Write Phase 2 — Synthesis and Gap-Fill (cross-reference, evidence quality, URL verification, gap-fill, RtP/RtW, target universe assembly, Zeta advisory grounding)."
    status: pending
  - id: phase3
    content: "Write Phase 3 — Document Writing: Part I §§1–6 and Part II §§7–11, section-by-section order and word targets."
    status: pending
  - id: phase4
    content: "Write Phase 4 — Review: Part I checks, Part II checks, editorial rigor (Part I only, 8 tests)."
    status: pending
  - id: diff-exec
    content: "Write Key Differences table and Execution Approach (batching, estimated turns, output path)."
    status: pending
  - id: output-files
    content: "Write Output Files — primary document path, research retention path, stream file names and format, synthesis-notes and unverified-claims, cross-referencing rule."
    status: pending
  - id: save
    content: "Save plan as .cursor/plans/[engagement_area_slug]_opportunity_analysis.plan.md (or similar)."
    status: pending
isProject: true
---

# Create Engagement Area Opportunity Analysis Plan (Template)

**Purpose:** Produce a detailed research and writing plan for a **McKinsey-grade opportunity analysis and strategic advisory** on a chosen **[ENGAGEMENT AREA]**, and save it as a `.plan.md` file in `.cursor/plans/`.

**When to use:** For any engagement area in `org-8.0/what-we-sell/strategy/engagement-areas/` whose current doc is a shallow CIO-facing capability catalogue and should be replaced by a two-part (Part I analyst / Part II advisor) document.

---

## Context

- **Part I** — Independent opportunity analysis (evidence-first, segment-specific, no Zeta, no meta-narration, no time-fragile language). If Zeta didn’t exist, Part I would read the same.
- **Part II** — Strategic advisory to Zeta: Zeta-specific, honest about gaps, prescriptive (pursue/defer), risk-aware, named targets with evidence.
- **Boundary** — Explicit heading between Part I and Part II; no blending. Part I shareable externally; Part II internal.

---

## Citation Standard

- Every factual claim traceable: navigable URL preferred, or full bibliographic detail for paywalled sources.
- Not acceptable: “According to [authority]” without traceable reference; generic/homepage/404/login-only URLs; fabricated URLs; “industry analysts” without naming source.
- Unverifiable claims flagged as `[unverified — needs manual confirmation]`. Research sub-agents verify URLs before including.

---

## Reference Plan

Use `.cursor/plans/payments_opportunity_analysis_650b45db.plan.md` if present, else an existing engagement-area plan (e.g. `lending_credit_opportunity_analysis.plan.md`, `account_products_banking_opportunity_analysis.plan.md`, `baas_embeddable_banking_opportunity_analysis.plan.md`) as the structural template. Same architecture: parallel research streams → synthesis → section-by-section writing → review; tuned to [ENGAGEMENT AREA]; include two-part structure, target universe, citation standard, research retention.

---

## Inputs to Study Before Writing the Plan

1. **Current engagement area file** — `org-8.0/what-we-sell/strategy/engagement-areas/[ENGAGEMENT AREA FILENAME].md`
2. **Distillation framework** — `org-8.0/what-we-sell/strategy/distillation/how-to.md` (Right to Play / Right to Win)
3. **Thesis** — `org-8.0/what-we-sell/the-thesis/thesis.md`
4. **Related product-line files** — `org-8.0/what-we-sell/strategy/product-lines/` (relevant to this engagement area)
5. **Product-line-engineering archetype** (if any) — `org-8.0/product-line-engineering/archetypes/`
6. **S.TODO** — `org-8.0/what-we-sell/strategy/S.TODO` (tone and approach)
7. **Editorial rigor skill** — `.cursor/skills/editorial-rigor-review/SKILL.md` (eight tests for Part I)
8. **Existing research** — `org-8.0/what-we-sell/strategy/_research/`, `market-study/` (overlap; cross-reference, don’t re-research)
9. **Other completed opportunity analyses** — for depth and style calibration

---

## Plan Structure Requirements

The generated plan must include:

### 1. Model Recommendation

Orchestration vs. research sub-agents; reasoning specific to this engagement area; impact of thin analyst coverage on research approach.

### 2. Phase 1: Parallel Research (5–7 streams)

Each stream must specify:

- Exactly what data to gather
- Specific sources (analyst firms, regulators, filings, reports)
- Geographic scope
- How data will be used in the final document
- **Citation requirement:** navigable URL or full bibliographic detail per Citation Standard

Typical streams:

- Market sizing and revenue pools (vendor-addressable TAM, sub-segment, geography)
- Regulatory landscape and mandates (geographies that matter; regulations that force infrastructure investment)
- Competitive landscape (incumbents, challengers, specialists; positioning, revenue model, strengths, weaknesses, vulnerabilities)
- Structural shifts / modernization activity (evidence of banks modernizing in this area)
- 1–3 additional streams specific to this engagement area

**Mandatory sub-task** for competitive landscape and structural shifts streams:

> Identify specific banks that have publicly signaled modernization activity — earnings calls, press releases, RFPs, analyst commentary, vendor partnership disclosures. Capture: bank name, tier, geography, signal, source, navigable URL.

If analyst coverage is thin, emphasize primary evidence (regulatory proposals, vendor launches, patent activity, standards) over analyst market sizing.

### 3. Phase 2: Synthesis and Gap-Fill

- Cross-reference data across streams; evidence strength vs. thin
- **Verify all URLs and citations**; flag needs for manual confirmation
- Targeted follow-up for gaps
- Map to Right to Play / Right to Win
- Assemble named bank target universe from streams
- Ground Zeta advisory vs. competitive landscape

### 4. Phase 3: Document Writing

**Part I — The Opportunity (analyst voice, no Zeta):**

1. Market — prize, sub-domain and geography
2. How We Got Here — brief history for structural context
3. Structural Shifts (6–8) — each with data, regulation, competitive activity; by bank tier and geographies
4. Engagement Landscape — engagement types commissioned, mapped to tier and shift
5. Competitive Landscape — incumbents, challengers, specialists; gaps and vulnerabilities
6. Target Universe — named institutions by geography, tier (Tier 1/2/3), horizon (near-term 0–2y, medium-term 2–5y); each with cited evidence and URL; analytical, not sales

**Part II — The Advisory (advisor voice, Zeta-specific):**

7. Zeta's Position — assets mapped; production-ready, partial, missing
8. Where to Play — segments, geographies, program types, tiers; explicit “not yet” and “do not pursue”
9. Risks and Gaps — what must be true; what could close the window; where speed matters; capabilities to build
10. Recommended Actions — prioritized, time-bound; near-term (0–2y), medium-term (2–5y); which banks first and why
11. Executive Summary — written last; Part I + Part II; board-ready

### 5. Phase 4: Review

**Part I:** Citations with URL or full bibliographic detail; no broken links; no unsourced “according to”; unverifiable claims flagged; no assertion-only shifts; segment/geography grounded; no Zeta/commercial voice; every Target Universe bank with citable evidence; reads as external analysis.

**Part II:** Recommendations trace to Part I; gaps honest; recommendations specific and prioritized; “do not pursue”/“delay” where warranted; product/asset refs match repo product-line files.

**Editorial rigor (Part I only):** All eight tests from `.cursor/skills/editorial-rigor-review/SKILL.md`.

### 6. Key Differences from Other Engagement Areas

Brief table: market structure, competitive landscape, regulatory drivers, geographic concentration, central strategic argument vs. other areas (especially payments as reference).

### 7. Execution Approach

- Sub-agent batching (max 4 concurrent; plan batches for 5–7 streams)
- Estimated turns
- Output file path

### 8. Output Files

- **Primary document:** `org-8.0/what-we-sell/strategy/engagement-areas/[ENGAGEMENT AREA FILENAME].md`
- **Research retention:** `org-8.0/what-we-sell/strategy/_research/[ENGAGEMENT AREA SLUG]/`
  - One file per stream: `s1-[stream-name].md`, …
  - `synthesis-notes.md` — cross-refs, evidence quality, RtP/RtW, editorial decisions
  - `unverified-claims.md` — each unverified claim with context and source attempted
- **Stream file format:** Research date, engagement area; table (Claim | Value | Source | URL | Verified); key findings; gaps; raw notes.
- **Cross-referencing:** If overlap with another area’s research, reference existing file; note in `synthesis-notes.md`.

---

## What NOT to Do

- Do not write the opportunity analysis itself; only the research and writing plan.
- Do not produce a generic plan; streams, shifts, competitors, and regulations must be specific to [ENGAGEMENT AREA].
- Do not include more than 4 geographic markets (USA and India defaults; add at most 1–2 with justification).
- Do not plan for a document shorter than 4,000 or longer than 8,000 words.
- Do not blend analyst and advisor voices; enforce Part I / Part II boundary.
- Do not include banks in Target Universe without specifying evidence sources; no speculation.
- Do not cite without navigable URL or full bibliographic detail; do not fabricate URLs.
- Do not discard research; retain all stream output in `_research/`.

---

## Execution

1. **Substitute** [ENGAGEMENT AREA] and [ENGAGEMENT AREA FILENAME] and [ENGAGEMENT AREA SLUG] with the chosen area (e.g. BaaS and Embeddable Banking → `baas-and-embeddable-banking`).
2. **Run** the todos in order: read inputs → write Model Recommendation → Phase 1 (5–7 streams) → Phase 2 → Phase 3 → Phase 4 → Key Differences + Execution → Output Files → save plan.
3. **Save** the plan as `.cursor/plans/[engagement_area_slug]_opportunity_analysis.plan.md` (or equivalent naming used in this repo).
