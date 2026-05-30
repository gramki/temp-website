# Signal Exploration Task

**Model:** Work Model
**Track:** Discovery
**Owner:** Product Manager, UX Researcher

## Definition

The structured work of investigating a Signal (Problem, Need, or Opportunity) — understanding its context, scope, root causes, affected segments, and adjacent patterns — and synthesizing one or more candidate Ideas (hypotheses) from that understanding. This is the divergent, open-ended work that produces the Signal → Idea transition.

## Purpose

Signal Exploration Task makes the critical Signal → Idea phase transition explicit and trackable. Before this entity, the Discovery Track had no dedicated representation for the substantial work between receiving a Signal and formulating a hypothesis about what to do about it. "Research Task" was conflating two fundamentally different types of work:

- **Exploration** (divergent): "What does this Signal mean? Who's affected? What are the root causes? What could we do?" — open-ended, generative, producing Ideas.
- **Validation** (convergent): "Is this specific Idea viable? What evidence supports or contradicts it?" — targeted, evidence-gathering, producing a Go/Kill/Pivot decision.

These require different mindsets, different skills, and different outputs. Signal Exploration is about *understanding the terrain and forming bets*; Research/Experiment/Prototype are about *testing those bets*.

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | What Signal is being explored |
| Originating Discovery Case | Reference (Discovery) | Discovery Case this task belongs to, when exploration is case-scoped |
| Signal(s) | List of References (Strategy) | Which Signal(s) this exploration investigates |
| Initiative | Reference (Strategy) | Which Initiative this exploration supports (if associated) |
| Exploration Scope | Text | What aspects are being investigated (context, root cause, segment impact, etc.) |
| Findings | Text | What was learned during exploration |
| Ideas Generated | List of References (Strategy) | Which Ideas were synthesized from this exploration |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| To Do | Not yet started |
| In Progress | Actively exploring the Signal |
| Done | Exploration complete, Ideas generated (or Signal dismissed as noise) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Input | Signal — Problem / Need / Opportunity (Strategy) | Explores one or more Signals |
| Originates from | Discovery Case (Discovery) | Sub-item of a Discovery Case; carries bidirectional reference |
| Context | Initiative (Strategy) | May be scoped by an Initiative |
| Output | Idea (Strategy) | Produces one or more Ideas (hypotheses) |
| Sibling | Deliberation (Discovery) | A Deliberation may also generate Ideas from Signals |
| Downstream | Research Task (Discovery) | Research Tasks may be spawned to gather specific evidence during exploration |
| May trigger | Modeling Task (Discovery) | Exploration findings may reveal gaps in Definition Model |

## Examples

| Signal Exploration Task | Signal(s) | Ideas Generated |
|---|---|---|
| "Explore LATAM FX pain points" | Problem: "6-click FX confirmation flow", Need: "Batch payout file upload" | Idea: "One-click FX lock with auto-confirm", Idea: "CSV/SFTP batch payout ingestion" |
| "Explore settlement reporting gaps" | Need: "Multi-currency reporting", Problem: "Manual reconciliation errors" | Idea: "Automated multi-currency settlement dashboard" |
| "Explore infra cost reduction opportunities" | Opportunity: "Consolidate payment adapters for 40% cost savings" | Idea: "Unified adapter framework with provider plugins" |

## Notes

- A single Signal Exploration Task may investigate multiple related Signals that appear to point to the same underlying issue — this is consistent with the Signal concept ("multiple Signals may point to the same underlying issue").
- Signal Exploration may include lightweight investigation (quick interviews, data checks) as part of the exploration, distinct from formal Research Tasks.
- If exploration reveals the Signal is noise (weak, not reproducible, already addressed), the outcome is dismissal — no Ideas generated. This is a valid and valuable outcome.
