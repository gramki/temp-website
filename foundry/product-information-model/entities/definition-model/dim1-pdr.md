# Product Decision Record (PDR)

**Model:** Definition Model
**Dimension:** Strategy
**Owner:** Product Management

## Definition

A formal, referenceable record of a significant product decision — including the reasoning, evidence, and trade-offs. A PDR captures Go, Kill, and Pivot decisions alike. It may validate one or more Ideas, or it may record a strategic decision that doesn't trace to a specific Idea (e.g., a product council Deliberation on market strategy that triggers Modeling Tasks rather than PSDs).

## Purpose

The PDR fills the traceability gap between discovery work and committed action. Without it, the model has no artifact that formally records *why* a decision was made or *what evidence* supports it. The PDR is a knowledge artifact (not a process artifact), persisting as a referenceable record long after the discovery work is complete. It differs from the rejected Discovery Decision Record (DDR) concept, which was a workflow-transition artifact — see FAQ Q6.

> **PM alignment gate.** PDRs that materially change product direction require explicit Product Management alignment before Final status. Technical ADRs and operational ODRs do not substitute for PM alignment on product-direction decisions. A Discovery Case that produces a direction-changing PDR records PM alignment as part of closure.

Key design choices:
- Captures **any significant decision** — Go, Kill, and Pivot. A "Kill" PDR is just as valuable for institutional memory as a "Go" PDR.
- **May correspond to multiple Ideas** — a single Deliberation may evaluate several related Ideas and produce one PDR covering all of them.
- **May exist without a specific Idea** — a strategic Deliberation (e.g., "enter LATAM market") may produce a PDR that triggers Modeling Tasks and Initiatives without a formal Idea entity preceding it.
- **References Work Model artifacts** — creating cross-model traceability from evidence to decision.
- **Creates or updates Product Intent(s)** — one PDR can justify multiple routable Product Intents.
- **Referenced by PSD(s)** — one PDR can justify multiple PSDs across different modules; PSDs refine Product Intent rather than create it.
- **May trigger Modeling Tasks** — a PDR decision may require Definition Model updates (Dims 2–9) in addition to or instead of engineering changes.

## Fields

| Field | Type | Description |
|---|---|---|
| PDR ID | String | Unique identifier (e.g., PDR-017) |
| Title | String | Short description of the decision |
| Decision Type | Enum | `Go` / `Kill` / `Pivot` |
| Idea(s) | List of References (Strategy) | Which Idea(s) this decision addresses (may be empty for strategic decisions) |
| Decision Date | Date | When the decision was made |
| Decision Makers | List | Who participated in the decision (roles or names) |
| Evidence References | List of References (Discovery) | Research Tasks, Experiments, Prototypes, Deliberations that produced evidence |
| Rationale | Text | Why this decision was made — the reasoning |
| Trade-offs | Text | What was considered and rejected — alternatives and their downsides |
| Confidence Level | Enum | `Low` / `Medium` / `High` |
| Product Direction Change | Boolean | True when the decision materially changes committed product direction, scope, or strategic posture |
| PM Alignment | Reference / Attestation | Required when Product Direction Change = true; records accountable PM attestation |
| Triggers | Text | What this decision triggers — Product Intent(s), PSD(s), Modeling Task(s), Initiative(s), or combination. Product Intent comes first when the decision commits to downstream product evolution. |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Draft | Decision is being documented (evidence being assembled) |
| Final | Decision is recorded and actionable |
| Superseded | Replaced by a newer PDR (e.g., pivot after new evidence) |

**State Diagram:**

```
Draft ──[evidence assembled, decision          Draft ──[abandoned before
          makers approve]──► Final                      finalization]──► (deleted)
                                │
                     [new evidence or
                      changed context;
                      new PDR created]
                                │
                                ▼
                           Superseded
```

**Key transitions:**
- `Draft → Final`: Evidence is assembled, decision makers have reviewed and approved
- `Final → Superseded`: New evidence or changed context warrants a new decision; a new PDR is created that references this one as superseded

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Idea (Strategy) | PDR validates/kills Idea(s) — may correspond to multiple Ideas |
| Context | Discovery Case (Discovery) | PDR may be produced by a Discovery Case |
| Downstream | Product Intent (Strategy) | Go or Pivot PDRs create or update Product Intent(s) |
| Downstream | PSD (Strategy) | PDR justifies PSD(s) that refine Product Intent — a single PDR may justify multiple PSDs across different modules |
| Downstream | ADR(s) (Technical) | PDR may trigger Architecture Decision Records for technical/architectural decisions required to implement the product decision |
| Downstream | ODR(s) (Operational) | PDR may trigger Operations Decision Records for infrastructure/operational decisions required to support the product decision |
| Downstream | Modeling Task (Discovery) | PDR may trigger Modeling Tasks for Definition Model updates |
| Downstream | Initiative (Strategy) | PDR may trigger or refine Initiatives |
| Evidence | Research Task (Discovery) | PDR references Research Tasks as evidence |
| Evidence | Experiment (Discovery) | PDR references Experiments as evidence |
| Evidence | Prototype / Spike (Discovery) | PDR references Prototypes/Spikes as evidence |
| Evidence | Deliberation (Discovery) | PDR references Deliberations as evidence/decision source |
| Supersedes | PDR (Strategy) | A newer PDR may supersede this one |

## Example

"PDR-017: Go — Real-time FX rate locking. Based on: 23 user interviews confirming margin pain, fake-door test (14% click-through), provider feasibility spike (<200ms quotes), and product council deliberation (2026-02-10). Trade-off: adds FX provider dependency. Triggers: PI-042 (Invoice Flow FX Rate Lock), PI-043 (FX Audit Trail), PSD-042 (Invoice & Payout Module), PSD-043 (FX Microservice Module), Modeling Task (update Value Stream 'Cross-Border Payout Processing')."
