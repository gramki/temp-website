# Build Track

Build is the track where Product Intent is refined, implemented, verified, and prepared for release. Build is Product Intent-orchestrated.

## What Build is for

Build is for executing Product Intent through Workspaces:

```text
Product Intent
  -> Product Specification / PSD refinement
  -> UX Design
  -> Development
  -> QA
  -> Release
```

Build may produce:

- customer-facing product capabilities;
- internal or enabling capabilities;
- technical validation evidence;
- PoCs and spikes;
- operational enablement artifacts;
- release-renewal work.

## What Build is not for

Build is not:

- a dumping ground for technical wishes;
- independently orchestrated by Epics, PSDs, ADRs, or refactoring tasks;
- only customer-shipping work;
- a bypass around Discovery decisions.

## Primary orchestration item: Product Intent

The Build Track has one primary orchestration item: **Product Intent**.

Product Intent may have several purposes:

| Product Intent purpose | Meaning |
|------------------------|---------|
| Delivery | Intended to ship or become customer available. |
| Discovery Support | Build work needed to answer a Discovery Case question. |
| Technical Validation | Spike / PoC / architecture feasibility. |
| Internal / Enabling | Internal product or platform capability. |
| Operational Enablement | Build work to satisfy SLA, readiness, reliability, observability, or operational commitments. |
| Release Renewal | Follow-up intent generated from release evidence or learning. |

Product Intent entering Build does **not** necessarily mean customer-committed delivery.

## Architecture and refactoring rule

Architectural refactoring must find its product intent or move tracks.

It may:

1. fit under an existing Product Intent;
2. become Product Intent through a Discovery Case and product decision;
3. route to Run if operational response or readiness is the concern;
4. route to Evolve if standards, practice, guidance, or model structure are changing;
5. remain local engineering hygiene if small and internal.

Build does not independently commission top-level architecture work outside Product Intent.

## Examples

### Refactor under existing Product Intent

```text
Product Intent: Real-time FX quote locking
  -> PSD
  -> ADR: split FX quote service
  -> Epic / Technical Tasks
```

### Refactor becomes Product Intent

```text
Architecture concern: settlement engine cannot scale
  -> Discovery Case
  -> PDR
  -> Product Intent: Settlement throughput scale-up for LATAM volume
```

### Discovery-support Build work

```text
Discovery Case: assess event-sourcing for audit trail
  -> Discovery Support Product Intent
  -> Build spike
  -> Evidence
  -> PDR
```
