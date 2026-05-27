---
name: "Engagement Area Opportunity Analysis (Template)"
overview: "Template for creating a detailed research and writing plan for a McKinsey-grade two-part opportunity analysis on any engagement area. Run this plan with a specific [ENGAGEMENT AREA] to generate the area-specific .plan.md and follow the two-part document structure, citation standard, and research retention rules."
todos:
  - id: resolve-area
    content: "Resolve [ENGAGEMENT AREA], engagement area filename ([FILENAME].md), slug for _research/, and output paths. Confirm current engagement area file exists or note 'creates'."
    status: pending
  - id: read-inputs
    content: "Read all inputs: current EA file, distillation/how-to.md, thesis.md, relevant product-lines, archetype (if any), S.TODO, editorial-rigor-review skill, _research/ and market-study/ overlap, one reference plan (e.g. lending or cloud-ops)."
    status: pending
  - id: draft-phase1
    content: "Draft Phase 1 — 5-7 parallel research streams (market sizing, regulatory, competitive, structural shifts, + 1-3 area-specific). Include bank-signal sub-task and citation requirement per stream."
    status: pending
  - id: draft-phase2
    content: "Draft Phase 2 — Synthesis and gap-fill: cross-reference, evidence quality, URL verification, R2P/R2W mapping, target universe assembly, Zeta advisory grounding."
    status: pending
  - id: draft-phase3-4
    content: "Draft Phase 3 (section-by-section writing order for Part I and Part II) and Phase 4 (review checklist, editorial rigor)."
    status: pending
  - id: draft-diffs-exec-output
    content: "Draft Key Differences table, Execution Approach (batching, turns, output path), and Output Files (primary doc, _research/ stream files, synthesis-notes, unverified-claims)."
    status: pending
  - id: write-model-recommendation
    content: "Write Model Recommendation (orchestration vs research sub-agents, analyst coverage impact)."
    status: pending
  - id: write-save-plan
    content: "Assemble full plan and save as .cursor/plans/[engagement_area_slug]_opportunity_analysis.plan.md."
    status: pending
isProject: true
---

# Engagement Area Opportunity Analysis — Template

**Purpose:** Use this template to create a detailed research and writing plan for a **McKinsey-grade opportunity analysis and strategic advisory** on a specific engagement area. Substitute **[ENGAGEMENT AREA]** and **[ENGAGEMENT AREA FILENAME]** (and slug) throughout.

---

## Task

Create a detailed research and writing plan for a **McKinsey-grade opportunity analysis and strategic advisory** on the **[ENGAGEMENT AREA]** engagement area, then save it as a `.plan.md` file in `.cursor/plans/`.

## Context

The repo (`org-8.0/what-we-sell/strategy/engagement-areas/`) contains engagement area documents. The current `[ENGAGEMENT AREA FILENAME].md` is a shallow CIO-facing capability catalogue. It needs to be replaced with a deeply researched, two-part document:

- **Part I** is an independent opportunity analysis — the kind a senior McKinsey or Bain consultant would deliver to any technology company evaluating this space.
- **Part II** is a strategic advisory specific to Zeta — opinionated, prescriptive, and honest about where Zeta should play, where it should not, and what's missing.

Neither part should dilute the other. The analyst never sells. The advisor never hedges what the analysis has already established.

---

## Document Structure: Two Distinct Roles

### PART I — THE OPPORTUNITY (Analyst voice)

- **Evidence-first.** Every structural shift, market claim, or segment assertion is grounded in data from credible sources. Every citation must include a navigable URL or full bibliographic detail. No "according to McKinsey" without a traceable reference.
- **Segment-specific.** Bank tiers (regional, mid-size, large) and specific geographies. USA primary, India accessible, at most 1–2 additional jurisdictions with justification.
- **Forward-looking with structural grounding.** "Structural Shifts Creating Opportunity" — 2–10 year horizon.
- **Board-grade prose.** No Zeta references. No commercial voice. No meta-narration. No time-fragile language.

### PART II — THE ADVISORY (Advisor voice)

- **Zeta-specific.** Names assets and maps to the opportunity. Honest gaps. Prescriptive (Pursue X, Delay Y). Risk-aware. Named bank targets with citable basis.

**Boundary:** Clear heading between Part I and Part II. No blending.

---

## Citation Standard

- **Acceptable:** Direct navigable URL; regulatory/government source; SEC filing; earnings transcript; paywalled report with full bibliographic detail (publication, author, date, title, issue).
- **Not acceptable:** Unattributed "according to [authority]"; generic homepage/404/login wall; fabricated URL; "industry analysts" without naming source.
- **Unverifiable:** Flag as `[unverified — needs manual confirmation]`. Verify URLs resolve before including.

---

## Reference Plan

Use `.cursor/plans/` plans (e.g. `lending_credit_opportunity_analysis.plan.md`, `cloud_platform_ops_opportunity_analysis.plan.md`) as structural templates. Same architecture: parallel research streams → synthesis → section-by-section writing → review. Tune to [ENGAGEMENT AREA] dynamics.

---

## Inputs to Study Before Planning

1. **Current engagement area file** — `org-8.0/what-we-sell/strategy/engagement-areas/[ENGAGEMENT AREA FILENAME].md`
2. **Distillation framework** — `org-8.0/what-we-sell/strategy/distillation/how-to.md` (Right to Play / Right to Win)
3. **Thesis** — `org-8.0/what-we-sell/the-thesis/thesis.md`
4. **Related product-line files** — `org-8.0/what-we-sell/strategy/product-lines/`
5. **Product-line-engineering archetype** — `org-8.0/product-line-engineering/archetypes/` (if exists)
6. **S.TODO** — `org-8.0/what-we-sell/strategy/S.TODO`
7. **Editorial rigor skill** — `.cursor/skills/editorial-rigor-review/SKILL.md` (eight tests for Part I)
8. **Existing research** — `org-8.0/what-we-sell/strategy/_research/`, `market-study/` (cross-reference, do not re-research)
9. **Other opportunity analyses** — for depth and style calibration

---

## Plan Structure Requirements

The generated plan must include:

### 1. Model Recommendation

Orchestration vs research sub-agents; reasoning specific to this area. If analyst coverage is thin, note impact on research approach (e.g. primary evidence over analyst sizing).

### 2. Phase 1: Parallel Research (5–7 streams)

Each stream: what to gather; sources to target; geographic scope; how data is used; **citation requirement (URL or full bibliographic detail)**. Typical streams:

- Market sizing and revenue pools (vendor-addressable TAM by sub-segment and geography)
- Regulatory landscape and mandates (regulations that force infrastructure investment)
- Competitive landscape (incumbents, challengers, specialists; positioning, revenue, strengths, weaknesses, vulnerabilities)
- Structural shifts / modernization activity (evidence of banks modernizing)

**Every competitive landscape and structural shifts stream must include:**

> Identify specific banks that have publicly signaled modernization in this area — earnings calls, press releases, RFP announcements, analyst commentary, vendor partnership disclosures. Capture bank name, tier, geography, signal, source, and navigable URL.

Plus 1–3 streams specific to [ENGAGEMENT AREA]. If analyst coverage is thin, emphasize primary evidence (regulatory proposals, vendor launches, patent activity, standards bodies).

### 3. Phase 2: Synthesis and Gap-Fill

- Cross-reference streams; evidence strong vs thin
- **Verify all URLs resolve; citations complete;** flag manual confirmation
- Targeted follow-up for gaps
- Map to Right to Play / Right to Win
- Assemble named bank target universe from streams
- Ground Zeta advisory against competitive landscape

### 4. Phase 3: Document Writing (section order)

**PART I:** (1) Market (2) How We Got Here (3) Structural Shifts 6–8 (4) Engagement Landscape (5) Competitive Landscape (6) Target Universe (geography, tier, horizon; each bank with cited evidence and URL; analytical observation not sales).

**PART II:** (7) Zeta's Position (8) Where to Play (9) Risks and Gaps (10) Recommended Actions (11) Executive Summary (written last, covers both parts).

### 5. Phase 4: Review

**Part I:** Citations with URL or full bibliographic detail; no broken links; no unattributed authority; unverifiable flagged; evidence under every shift; segment/geography grounded; no Zeta/commercial voice; every Target Universe bank with citable evidence; reads as external analysis.

**Part II:** Recommendations trace to Part I; gaps honest; specific and prioritized; "do not pursue"/"delay" where warranted; product references accurate vs repo.

**Editorial rigor (Part I only):** All eight tests from `.cursor/skills/editorial-rigor-review/SKILL.md`.

### 6. Key Differences from Other Engagement Areas

Brief table: market structure, competitive landscape, regulatory drivers, geographic concentration, central strategic argument (and optionally vs payments as reference).

### 7. Execution Approach

Sub-agent batching (max 4 concurrent); estimated turns; output file path.

### 8. Output Files

- **Primary document:** `org-8.0/what-we-sell/strategy/engagement-areas/[ENGAGEMENT AREA FILENAME].md` — replaces (or creates) the two-part opportunity analysis and advisory.
- **Research retention:** `org-8.0/what-we-sell/strategy/_research/[ENGAGEMENT AREA SLUG]/`
  - One file per stream: `s1-[stream-name].md`, …
  - `synthesis-notes.md` — cross-references, evidence quality, R2P/R2W, target universe, editorial decisions.
  - `unverified-claims.md` — every claim flagged with context.
- **Stream file format:** Research date and engagement area; data table Claim | Value | Source | URL | Verified (Yes/No); key findings; gaps; raw notes.
- **Cross-referencing:** If overlap with another area’s research, reference existing file in synthesis-notes; do not re-research.

---

## What NOT to Do

- Do not write the opportunity analysis itself; write only the research and writing plan.
- Do not produce a generic plan; streams, shifts, competitors, regulations must be specific to [ENGAGEMENT AREA].
- Do not include more than 4 geographic markets (USA and India defaults; add only with justification).
- Do not plan for a document shorter than 4,000 or longer than 8,000 words.
- Do not blend analyst and advisor voices.
- Do not include banks in Target Universe without evidence sources and URLs.
- Do not cite without navigable URL or full bibliographic detail; do not fabricate URLs.
- Do not discard research output; all stream findings saved under _research/[slug]/.

---

## How to Use This Template

1. **Choose the engagement area** (e.g. Banking Operations, Payments, Lending and Credit).
2. **Derive:** engagement area filename (e.g. `banking-operations.md`), slug (e.g. `banking-operations`), output plan name (e.g. `banking_operations_opportunity_analysis.plan.md`).
3. **Execute the todos** in order: resolve paths, read all inputs, draft Phase 1–4 and diffs/exec/output, write model recommendation, assemble and save the full area-specific plan to `.cursor/plans/[slug]_opportunity_analysis.plan.md`.

The resulting plan is then run separately to execute the research and write the two-part document.
