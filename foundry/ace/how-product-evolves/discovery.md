# Discovery Track

Discovery is the cross-functional learning and decision track. It organizes product-relevant questions until they are dismissed, parked, decided, or routed into Product Intent or another track.

## What Discovery is for

Discovery is for:

- framing uncertainty before product evolution is committed;
- investigating Signals, technical ideas, operational insights, customer commitments, and strategic bets;
- producing evidence through Research, Experiments, Prototypes, Spikes, and Deliberations;
- recording product decisions through PDRs;
- creating Product Intent when a Go or Pivot decision commits the product to evolution;
- requesting Build evidence through Discovery Support Product Intent when learning requires real build work.

## What Discovery is not for

Discovery is not:

- Product Manager-only work;
- only customer-Signal processing;
- backlog grooming;
- a guarantee that every case produces Product Intent;
- a replacement for Build, Run, Win, Evolve, or Governance execution;
- only upstream of customer-shipping work.

## Who participates

Any authorized function may originate or participate in a Discovery Case:

- Product Management
- UX / Research
- Engineering
- Architecture
- QA
- Run / SRE
- Win / Sales / CS / Support / Product Marketing
- Governance / Compliance / Security
- Executive leadership
- authorized agents or monitors

Product Management alignment is required for PDRs that materially change product direction.

## Primary orchestration item: Discovery Case

**Discovery Case** is the Discovery Track orchestration item. It does not require a Signal.

Common origins:

- Signal or Signal cluster
- Product Manager judgment
- Strategic Theme, Objective, KRA, SLA, or customer commitment
- Initiative or Customer Release Intent
- Customer Promise gap
- Technical idea or architecture concern
- QA / testability concern
- Operational insight or incident pattern
- Release learning
- Governance or compliance concern
- Executive direction
- agent / monitoring observation

## Sub-work

A Discovery Case may create or coordinate:

- Signal Exploration Tasks
- Research Tasks
- Experiments
- Prototypes / Spikes
- Deliberations
- Modeling Tasks
- Discovery Support Product Intents

## Outcomes

| Outcome | Meaning |
|---------|---------|
| Dismissed | Not worth pursuing. |
| Parked | Valid but deferred. |
| Kill PDR | Explicit decision not to pursue. |
| Go / Pivot PDR | Product decision recorded. |
| Product Intent | Evolution intent created. |
| Multiple Product Intents | One decision decomposes into several evolution threads. |
| Discovery Support Product Intent | Build evidence requested before a final decision. |
| Modeling Task | Definition Model update needed. |
| Run Case / Win Case / Evolve Case / Governance Ritual or Enforcement | Routed to another track. |

## Discovery can request Build evidence

Sometimes Discovery needs real build work to learn:

```text
Discovery Case
  -> Discovery Support Product Intent
  -> Build Spike / PoC / Technical Validation
  -> Evidence
  -> PDR
  -> Evolution Product Intent, maybe
```

Discovery Support Product Intent is not a customer-delivery commitment. It exists to produce evidence.

## Examples

### Architecture-originated case

An architect raises: "Current module boundaries block partner API extensibility."

```text
Discovery Case
  -> Deliberation + technical spike
  -> PDR
  -> Product Intent: Partner-grade API modularity
```

### PM judgment case

A PM believes the pricing model needs re-evaluation before LATAM launch.

```text
Discovery Case
  -> Research + Modeling Task
  -> PDR
  -> Product Intent or model update
```

### Customer commitment case

Sales commits to API v2 readiness for a customer, but feasibility is unknown.

```text
Discovery Case
  -> Discovery Support Product Intent
  -> Build feasibility spike
  -> Evidence
  -> PDR
```
