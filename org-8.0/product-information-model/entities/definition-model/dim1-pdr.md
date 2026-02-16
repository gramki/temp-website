# Product Decision Record (PDR)

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management

## Definition

A formal, referenceable record of a significant product decision — including the reasoning, evidence, and trade-offs. A PDR captures Go, Kill, and Pivot decisions alike. It may validate one or more Ideas, or it may record a strategic decision that doesn't trace to a specific Idea (e.g., a product council Deliberation on market strategy that triggers Modeling Tasks rather than PSDs).

## Purpose

The PDR fills the traceability gap between discovery work and committed action. Without it, the model has no artifact that formally records *why* a decision was made or *what evidence* supports it. The PDR is a knowledge artifact (not a process artifact), persisting as a referenceable record long after the discovery work is complete. It differs from the rejected Discovery Decision Record (DDR) concept, which was a workflow-transition artifact — see FAQ Q6.

Key design choices:
- Captures **any significant decision** — Go, Kill, and Pivot. A "Kill" PDR is just as valuable for institutional memory as a "Go" PDR.
- **May correspond to multiple Ideas** — a single Deliberation may evaluate several related Ideas and produce one PDR covering all of them.
- **May exist without a specific Idea** — a strategic Deliberation (e.g., "enter LATAM market") may produce a PDR that triggers Modeling Tasks and Initiatives without a formal Idea entity preceding it.
- **References Work Model artifacts** — creating cross-model traceability from evidence to decision.
- **Referenced by PSD(s)** — one PDR can justify multiple PSDs across different modules.
- **May trigger Modeling Tasks** — a PDR decision may require Definition Model updates (Dims 2–9) in addition to or instead of engineering changes.

## Fields

| Field | Type | Description |
|---|---|---|
| PDR ID | String | Unique identifier (e.g., PDR-017) |
| Title | String | Short description of the decision |
| Decision Type | Enum | `Go` / `Kill` / `Pivot` |
| Idea(s) | List of References (Dim 1) | Which Idea(s) this decision addresses (may be empty for strategic decisions) |
| Decision Date | Date | When the decision was made |
| Decision Makers | List | Who participated in the decision (roles or names) |
| Evidence References | List of References (Track 1) | Research Tasks, Experiments, Prototypes, Deliberations that produced evidence |
| Rationale | Text | Why this decision was made — the reasoning |
| Trade-offs | Text | What was considered and rejected — alternatives and their downsides |
| Confidence Level | Enum | `Low` / `Medium` / `High` |
| Triggers | Text | What this decision triggers — PSD(s), Modeling Task(s), Initiative(s), or combination |
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
| Upstream | Idea (Dim 1) | PDR validates/kills Idea(s) — may correspond to multiple Ideas |
| Downstream | PSD (Dim 1) | PDR justifies PSD(s) — a single PDR may justify multiple PSDs across different modules |
| Downstream | Modeling Task (Track 1) | PDR may trigger Modeling Tasks for Definition Model updates |
| Downstream | Initiative (Dim 1) | PDR may trigger or refine Initiatives |
| Evidence | Research Task (Track 1) | PDR references Research Tasks as evidence |
| Evidence | Experiment (Track 1) | PDR references Experiments as evidence |
| Evidence | Prototype / Spike (Track 1) | PDR references Prototypes/Spikes as evidence |
| Evidence | Deliberation (Track 1) | PDR references Deliberations as evidence/decision source |
| Supersedes | PDR (Dim 1) | A newer PDR may supersede this one |

## Example

"PDR-017: Go — Real-time FX rate locking. Based on: 23 user interviews confirming margin pain, fake-door test (14% click-through), provider feasibility spike (<200ms quotes), and product council deliberation (2026-02-10). Trade-off: adds FX provider dependency. Triggers: PSD-042 (Invoice & Payout Module), PSD-043 (FX Microservice Module), Modeling Task (update Value Stream 'Cross-Border Payout Processing')."
