# DR-013: Dimension 1 Comprehensiveness Refinements

**Status:** Accepted
**Date:** 2026-02-15

## Context

A critical review of Dimension 1 (The Strategy Dimension) identified several gaps:

1. **Signal statuses undefined.** All three Signal entities had `_To be refined._` for statuses — no lifecycle, no way to track Signal progression.
2. **Idea and PDR fields empty.** Both entities were shells — statuses and fields marked `_To be refined._`.
3. **No common Signal fields.** Problem, Need, and Opportunity had different specialized fields but no shared structure (title, source, date, related signals).
4. **Stale Work Model references.** Signal entities still referenced Research Task as the primary investigator after DR-010 split it into Signal Exploration Task and Research Task.
5. **PDR didn't reference Deliberation.** After DR-011 introduced Deliberation, PDR's evidence sources were stale.
6. **PSD Section 3 stale.** Referenced "Buyer Persona" (pre-rename) and "ROI Metric" (pre-restructure).
7. **No external constraint capture.** Regulatory deadlines, partnership timelines, and competitive threats that constrain Objectives and Initiatives had no structured representation.
8. **No strategic continuity across horizons.** Objectives are time-bound; the persistent strategic direction across horizons was implicit.
9. **No portfolio context.** Products exist within portfolios, but the UPIM had no way to express this relationship.

## Decisions

### 1. Common Signal lifecycle (applies to Problem, Need, Opportunity)

`New → Triaged → Exploring / Associated / Parked → Addressed / Dismissed`

With explicit transition triggers documented in state diagrams.

### 2. Idea fields populated

Hypothesis Statement, Source Signal(s), Target Customer Segment(s), Expected Impact, Confidence Level (L/M/H), Effort Estimate (XS–XL).

### 3. PDR fields and statuses populated

Decision Type (Go/Kill/Pivot), Decision Date, Decision Makers, Evidence References (including Deliberation), Rationale, Trade-offs, Confidence Level, Triggers. PDR may correspond to multiple Ideas and may exist without a specific Idea (from strategic Deliberation). Status lifecycle: Draft → Final → Superseded.

### 4. Common Signal fields added

Title, Description, Source, Source Type (Customer/Prospect/Internal-Engineering/Internal-Operations/Internal-Strategy/Internal-Support/Data-Analytics), Date Captured, Related Signals (for pre-Initiative correlation).

### 5. Signal entities updated to reference Signal Exploration Task

Primary work model reference is now Signal Exploration Task, with Research Task and Deliberation as secondary references.

### 6. PDR updated to reference Deliberation

Deliberation added as an evidence/decision source.

### 7. PSD Section 3 updated

Renamed to "Customer Value Impact (Dimension 3)." Now references Buying Persona (with role types), Pain implications, Customer Promise implications, Customer Value Metric (Target + SLA Threshold), and Adoption Barrier impact.

### 8. External Constraints field added to Objective and Initiative

Structured list field for regulatory deadlines, partnership timelines, competitive threats, and contractual obligations. No new entity — keeps the model lean.

### 9. Strategic Theme entity introduced

Persistent, cross-cutting strategic direction across planning horizons. Scope: Portfolio (shared across products) or Product (local). Pursued through Objectives. Influences Customer Segments (Dim 3) and Capabilities/Value Streams (Dim 8). Status: Proposed → Active → Dormant → Retired. Optional on Objectives.

### 10. Portfolio thin entity introduced

Local reference entity — not owned by the UPIM. Provides traceable origin for portfolio-scoped Themes and documents the product's place within its portfolio.

## Rationale

- Signal lifecycle enables operational visibility ("how many Signals are we exploring?")
- Idea fields enable structured prioritization and comparison
- PDR fields create complete decision traceability (evidence → reasoning → action)
- Common Signal fields + Related Signals enable pre-Initiative correlation
- Updated references ensure consistency with DR-010 (Signal Exploration) and DR-011 (Deliberation)
- External Constraints as structured fields (not a new entity) keeps the model lean
- Strategic Theme provides cross-horizon continuity without duplicating Objectives
- Portfolio as thin reference acknowledges organizational context without overstepping UPIM scope

## Consequences

### Positive
- Dim 1 entities are now fully specified — no remaining `_To be refined._` placeholders for core fields/statuses
- Complete traceability: Theme → Objective → Initiative → Signal → Idea → PDR → PSD
- Signal progression is visible and queryable
- PDR is a comprehensive knowledge artifact with full evidence chain
- Portfolio-level strategic coordination is expressible without a separate portfolio model

### Negative
- Dim 1 now has 11 entities (up from 9): +Portfolio, +Strategic Theme
- Signal lifecycle has 7 statuses — teams need to maintain status transitions
- PDR's expanded scope (multi-Idea, Idea-free) requires clear guidance on when to create a PDR vs. when it's overkill
