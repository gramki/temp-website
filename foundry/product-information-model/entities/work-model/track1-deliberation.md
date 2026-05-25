# Deliberation

**Model:** Work Model
**Track:** Track 1: The Discovery Track (Learning)
**Owner:** Product Manager (facilitates); participants include any authorized stakeholders — product council, architecture review board, customer advisory board, cross-functional teams, executive leadership.

## Definition

A collaborative, group-based activity where authorized stakeholders convene to discuss, evaluate, and decide. Deliberation produces outcomes through collective judgment — the combined expertise, experience, and perspective of the group — rather than through empirical evidence (which is the domain of Research Tasks, Experiments, and Prototypes).

## Purpose

Many significant product decisions are not made through formal experiments or research. They emerge from structured group discussions — brainstorming sessions, product council reviews, architecture boards, customer advisory meetings. Before Deliberation, this entire class of decision-making work was invisible in the model, creating a false impression that all product decisions must be empirically validated.

Deliberation spans both discovery phases:

- **Signal Exploration (divergent):** A cross-functional brainstorm generating candidate Ideas from Signals. The group's diverse expertise produces hypotheses that no single investigator would arrive at alone.
- **Idea Validation (evaluative):** A product council evaluating an Idea's strategic fit, feasibility, and priority, and deciding Go/Kill/Pivot. The group's authority makes this a legitimate decision path.

Deliberation may directly produce a PDR — "the product council deliberated and decided X, for these reasons." This is a first-class decision path alongside empirical validation (Research → Experiment → PDR).

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | What is being deliberated |
| Originating Discovery Case | Reference (Track 1) | Discovery Case this deliberation belongs to, if any |
| Purpose | Enum | `Exploration` (generate Ideas) / `Evaluation` (decide on Ideas) / `Both` |
| Participants | List | Who participated (roles or names) |
| Authority | Text | What this group is authorized to decide |
| Input | List of References | Signals, Ideas, Research findings, or other context informing the deliberation |
| Outcome | Text | What was decided, generated, or concluded |
| Ideas Generated | List of References (Dim 1) | Ideas produced (if Exploration) |
| PDR Produced | Reference (Dim 1) | PDR produced (if Evaluation) |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Scheduled | Deliberation is planned |
| In Progress | Deliberation is underway (multi-session or async) |
| Concluded | Deliberation is complete, outcome documented |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Originates from | Discovery Case (Track 1) | Sub-item of a Discovery Case; carries bidirectional reference |
| Consumes | Signal (Dim 1) | May deliberate on Signals (exploration mode) |
| Consumes | Idea (Dim 1) | May deliberate on Ideas (evaluation mode) |
| Consumes | Research Task / Experiment / Prototype (Track 1) | May consume evidence from prior validation work |
| Produces | Idea (Dim 1) | May generate Ideas (exploration mode) |
| Produces | PDR (Dim 1) | May produce a PDR (evaluation mode — Go/Kill/Pivot) |
| Sibling | Signal Exploration Task (Track 1) | Both can generate Ideas from Signals |
| May trigger | Modeling Task (Track 1) | Deliberation outcomes may require Definition Model updates |

## Examples

| Deliberation | Mode | Participants | Outcome |
|---|---|---|---|
| "Product council: LATAM expansion strategy" | Evaluation | CPO, VP Eng, VP Sales, PM | PDR: Go with currency-first approach (Option B), LATAM pricing tier scoped |
| "Cross-functional brainstorm: batch payout automation" | Exploration | PM, 3 Engineers, UX, CSM | 4 candidate Ideas generated, 2 selected for validation |
| "Architecture review: unified adapter framework" | Evaluation | CTO, 2 Staff Engineers, PM | PDR: Approve unified adapter approach, timeline constraints noted |
| "Customer advisory board: H2 roadmap input" | Both | 5 Enterprise customers, PM, VP Product | 3 new Signals captured, 2 existing Ideas validated by customer demand |
| "Channel strategy: mobile app investment" | Evaluation | CPO, VP Eng, UX Lead, PM | PDR: Approve Mobile + Self-serve channel for approvals; UX Channel and HI Module scoped |
| "API strategy: external Payments API investment" | Evaluation | CPO, VP Eng, API Platform PM, Solutions Arch | PDR: Approve Cross-Border Payments API Module; scope operations, SLO targets, versioning strategy |
| "SDK investment: which languages and generation strategy?" | Evaluation | API Platform PM, DevRel, 2 Staff Engineers | PDR: Approve Python and Java SDKs, hand-crafted; defer Go and auto-gen approach to next cycle |

## Notes

- Deliberation is the only Discovery Track entity that is inherently *collaborative*. All other entities (Signal Exploration, Research, Experiment, Prototype) can be performed by individuals or small teams. Deliberation requires a group by definition.
- A Deliberation may consume the output of other discovery work — reviewing Research Task findings, Experiment results, or Prototype demos as input to the group discussion.
- Not every meeting is a Deliberation. Deliberation is tracked when the group activity produces a consequential outcome — Ideas, PDRs, or significant strategic direction. Status syncs, sprint ceremonies, and routine check-ins are not Deliberations.
