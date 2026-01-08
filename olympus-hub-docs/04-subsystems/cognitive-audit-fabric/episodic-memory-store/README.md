# Episodic Memory Store

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Cognitive Audit Fabric](../README.md)

---

## Overview

This folder contains the contracts, schemas, and APIs for **Episodic Memory Stores** — the storage layer for event-based, time-ordered, case-bound cognitive records.

### What is Episodic Memory?

In cognitive science, **episodic memory** stores autobiographical events — experiences that occurred at a particular time and place. In the CAF context:

| Characteristic | Description |
|----------------|-------------|
| **Event-based** | Each record captures a specific event (decision, handoff, outcome) |
| **Time-ordered** | Records have timestamps and form chronological sequences |
| **Case-bound** | All records belong to a case (via `case_id`) |
| **Immutable** | Records are append-only; history is preserved |

### Memory Class Taxonomy

| Memory Class | Purpose | Store Contract |
|--------------|---------|----------------|
| **Episodic** | Events, decisions, outcomes | ✅ This folder |
| Semantic | Facts, entities, relationships | 🔴 Future |
| Procedural | Skills, patterns, procedures | 🔴 Future |
| Preference | User/agent preferences | 🔴 Future |

---

## Documents

### Contracts & APIs

| Document | Description |
|----------|-------------|
| [Memory Store Contract](./memory-store-contract.md) | CRD registration, protocols, capabilities |
| [CAF Store REST API](./caf-store-rest-api.md) | Default write API (order-tolerant, idempotent) |
| [Record Relationships](./record-relationships.md) | How records link and traversal patterns |

### Record Schemas

#### Anchor Record
| Document | Description |
|----------|-------------|
| [Case Records](./case-records.md) | Case anchor, lifecycle, and resolution |

#### Core Records (Audit Foundation)
| Document | Description |
|----------|-------------|
| [Decision Records](./decision-records.md) | Decision with rationale |
| [Evidence Bundles](./evidence-bundles.md) | Context at decision time |
| [Context Snapshots](./context-snapshots.md) | Compiled context per agent turn |

#### Lifecycle & Feedback Records
| Document | Description |
|----------|-------------|
| [Outcome Records](./outcome-records.md) | Post-decision outcomes |
| [Override Records](./override-records.md) | Manual override documentation |
| [Directive Resolution Records](./directive-resolution-records.md) | Intervention lifecycle tracking |
| [Handoff Context](./handoff-context.md) | State transfer between agents |

#### Learning & Investigation Records
| Document | Description |
|----------|-------------|
| [Hypothesis Records](./hypothesis-records.md) | Learned patterns (bridge to Semantic) |
| [Incident Timelines](./incident-timelines.md) | Chronological event sequences |

---

## Record Summary

| # | Record Type | Purpose | Key Fields |
|---|-------------|---------|------------|
| 1 | **CaseRecord** | Root anchor | `case_id`, `status`, `actors`, `resolution` |
| 2 | DecisionRecord | Decision with rationale | `decision_id`, `action`, `confidence`, `evidence_bundle_id` |
| 3 | EvidenceBundle | Context at decision | `bundle_id`, `decision_id`, `context_snapshot_id` |
| 4 | ContextSnapshot | Compiled context | `snapshot_id`, `session_id`, `turn_number`, `context_frame` |
| 5 | OutcomeRecord | Post-decision outcome | `outcome_id`, `decision_id`, `actual_outcome`, `variance` |
| 6 | OverrideRecord | Manual override | `override_id`, `original_decision_id`, `justification` |
| 7 | DirectiveResolution | Intervention lifecycle | `resolution_id`, `intervention_ref`, `subtype`, `outcome` |
| 8 | HandoffContext | State transfer | `handoff_id`, `from_actor`, `to_actor`, `open_items` |
| 9 | HypothesisRecord | Learned pattern | `hypothesis_id`, `pattern`, `confidence`, `supporting_evidence` |
| 10 | IncidentTimeline | Event sequence | `timeline_id`, `events[]`, `analysis` |

---

## Store Requirements

Episodic Memory Stores must implement:

| Requirement | Description |
|-------------|-------------|
| **CAF Store REST API** | Default read/write protocol (required) |
| **Order-Tolerant Writes** | Accept records before their case exists |
| **Idempotent Writes** | De-duplicate by `(record_type, record_id)` |
| **Schema Validation** | Validate against CAF schemas |
| **JWS Verification** | Verify CAF-signed requests |
| **Hypermedia Links** | Include `self` and relationship URLs |

See [Memory Store Contract](./memory-store-contract.md) for full specification.

---

## Related Documents

- [CAF README](../README.md) — Cognitive Audit Fabric overview
- [Explanation Service](../explanation-service.md) — Narrative generation from records

