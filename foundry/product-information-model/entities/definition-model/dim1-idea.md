# Idea (Hypothesis)

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management

## Definition

The proposed solution bet for a given Signal (Problem, Need, or Opportunity). An Idea states what will be built, the expected metric impact, and the reasoning behind the bet. It is a hypothesis that must be validated through Discovery Track work before any commitment to build. An Idea is always spawned by one or more Signals.

## Purpose

The Idea bridges Signals (Problems, Needs, Opportunities) to a potential solution direction. It enters the Discovery Track where Signal Exploration Tasks, Research Tasks, Experiments, Prototypes, and Deliberations validate or invalidate it. A validated Idea produces a Product Decision Record (PDR); a killed Idea is archived with its evidence trail. The Idea is a Definition Model entity — the Discovery Track works *on* Ideas but does not *own* them as work items (see FAQ Q2).

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Short hypothesis name |
| Hypothesis Statement | Text | Structured hypothesis: "If we build X, we expect Y because Z" |
| Source Signal(s) | List of References (Dim 1) | Which Signals spawned this Idea |
| Target Customer Segment(s) | List of References (Dim 3) | Which segments benefit |
| Expected Impact | Text | What metric moves and by how much (e.g., "reduce FX transaction cost by 60%") |
| Confidence Level | Enum | `Low` / `Medium` / `High` (pre-validation estimate; may change during validation) |
| Effort Estimate | Enum | `XS` / `S` / `M` / `L` / `XL` (rough T-shirt size, pre-PSD) |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Proposed | Idea has been formulated but not yet under active investigation |
| Investigating | Discovery Track work is actively validating this Idea |
| Validated | Evidence supports the hypothesis — triggers PDR creation |
| Killed | Evidence does not support the hypothesis — archived with rationale |

**State Diagram:**

```
Proposed ──[Discovery work begins               Proposed ──[Deliberation or evidence
             (Research, Experiment,                          immediately invalidates]──► Killed
              Prototype, Deliberation)]
             │
             ▼
        Investigating
             │
             ├──[evidence supports hypothesis;
             │   PDR (Go) created]──────────────► Validated
             │
             └──[evidence contradicts hypothesis;
                  PDR (Kill) created]────────────► Killed
```

**Key transitions:**
- `Proposed → Investigating`: Discovery work begins — Research Tasks, Experiments, Prototypes, or Deliberations are created to test this Idea
- `Proposed → Killed`: Idea is invalidated before formal investigation (e.g., a Deliberation quickly determines infeasibility)
- `Investigating → Validated`: Sufficient evidence supports the hypothesis; a PDR (Go) is created
- `Investigating → Killed`: Evidence contradicts the hypothesis; a PDR (Kill) is created, preserving the rationale

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Problem (Dim 1) | Problem spawns this Idea |
| Upstream | Need (Dim 1) | Need spawns this Idea |
| Upstream | Opportunity (Dim 1) | Opportunity spawns this Idea |
| Downstream | Product Decision Record (Dim 1) | Idea is validated/killed by PDR |
| Work Model | Signal Exploration Task (Track 1) | Signal Exploration may produce this Idea |
| Work Model | Research Task (Track 1) | Research Tasks validate this Idea |
| Work Model | Experiment (Track 1) | Experiments test this Idea's hypothesis |
| Work Model | Prototype / Spike (Track 1) | Prototypes explore this Idea's feasibility or desirability |
| Work Model | Deliberation (Track 1) | Deliberations may evaluate this Idea |

## Example

"Build real-time FX rate locking in the invoice flow to reduce cart abandonment."
- Hypothesis: "If we add one-click FX rate locking, we expect a 60% reduction in per-transaction cost because manual hedging and multi-step confirmation are the primary cost drivers."
- Source Signals: Problem "6-click FX confirmation flow", Need "Batch payout with locked rates"
- Target Segment: LATAM Enterprise
- Confidence: Medium
- Effort: L
