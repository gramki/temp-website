# Semantic Memory Store

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Cognitive Audit Fabric](../README.md)

---

## Overview

This folder contains the contracts, schemas, and APIs for **Semantic Memory Stores** — the storage layer for learned beliefs and patterns derived from experience.

### What is Semantic Memory?

**Semantic Memory** captures **learned beliefs from experience** — probabilistic patterns that inform (but do not constrain) future decisions.

| Characteristic | Description |
|----------------|-------------|
| **Probabilistic** | Confidence-scored, not asserted |
| **Revisable** | Challengeable, can be deprecated |
| **Scoped** | Domain/workbench-bound, context-dependent |
| **Evidence-grounded** | Traceable to supporting episodes |
| **Informative** | Informs action, does not constrain it |

### Semantic Memory vs Enterprise Knowledge (Critical Distinction)

```
Knowledge = Truth × Semantics (asserted + meaningful = binding)
Semantic Memory = Learned beliefs (probabilistic, informative, not normative)
```

| Aspect | Enterprise Knowledge | Semantic Memory |
|--------|---------------------|-----------------|
| **Source** | Assertion | Experience |
| **Confidence** | Declared | Probabilistic |
| **Governance** | Formal | Analytical + review |
| **Role** | **Constrain** action | **Inform** action |
| **Examples** | Policies, rules, definitions | Patterns, hypotheses, learned constraints |

### Promotion Path

Semantic Memory may be **promoted** to Enterprise Knowledge through governance:

```
Episode → Pattern → Hypothesis → Candidate → Knowledge
(Episodic)  (Semantic Memory)              (Asserted Truth)
```

Promotion requires:
- Strong, replicated evidence
- Clear, stable scope
- Governance acceptance (policy/standard update)

---

## Domain Binding

All Semantic Memory records are **domain-bound**. In Hub parlance, a domain maps to a **Workbench**.

### Hub Metadata (Domain Scope)

```yaml
hub_metadata:
  tenant_id: uuid           # Tenant boundary
  subscription_id: uuid     # Subscription within tenant
  workbench_id: uuid        # Domain = Workbench
```

Unlike Episodic Memory (which includes `scenario_id`, `request_id`, `case_id`), Semantic Memory is:
- **Not case-bound** — patterns span many cases
- **Not request-bound** — beliefs persist across requests
- **Workbench-scoped** — learned within a domain context

---

## Documents

### Contracts & APIs

| Document | Description |
|----------|-------------|
| [Memory Store Contract](./memory-store-contract.md) | CRD registration, protocols, capabilities |
| [Record Relationships](./record-relationships.md) | How records link and traversal patterns |

### Record Schemas (6 types)

| Document | Description |
|----------|-------------|
| [Hypothesis Records](./hypothesis-records.md) | Learned patterns pending promotion |
| [Pattern Summary](./pattern-summary.md) | Recurring patterns with conditions |
| [Learned Constraints](./learned-constraints.md) | "Avoid X when Y" with scope |
| [Evaluation Findings](./evaluation-findings.md) | Benchmark/test results |
| [Entity Beliefs](./entity-beliefs.md) | Learned entity attributes (probabilistic) |
| [Relationship Beliefs](./relationship-beliefs.md) | Learned entity connections |

---

## Record Summary

| # | Record Type | Purpose | Key Fields |
|---|-------------|---------|------------|
| 1 | **HypothesisRecord** | Pattern pending promotion | `hypothesis_id`, `confidence`, `evidence_links`, `status` |
| 2 | **PatternSummary** | Recurring pattern | `pattern_id`, `conditions`, `outcomes`, `frequency` |
| 3 | **LearnedConstraint** | Advisory constraint | `constraint_id`, `statement`, `scope`, `risk_if_violated` |
| 4 | **EvaluationFinding** | Benchmark result | `finding_id`, `metric`, `result`, `significance` |
| 5 | **EntityBelief** | Learned entity attribute | `belief_id`, `subject`, `attribute`, `confidence` |
| 6 | **RelationshipBelief** | Learned connection | `belief_id`, `from_entity`, `to_entity`, `confidence` |

---

## What Belongs in Semantic Memory

Semantic Memory arises from **patterns across episodes**, not single events.

### Common Sources

- Recurring incident clusters with common precursors
- Repeated override rationales ("we keep accepting this under these conditions")
- Consistent failure modes in workflow/tool chains
- Anomaly analysis and investigations
- Model evaluation results ("strategy A outperforms B under condition C")

### Capture Requirements

All Semantic Memory records must include:

| Field | Purpose |
|-------|---------|
| `confidence` | How certain (0-1) and how computed |
| `evidence_links` | Traceable to supporting episodes |
| `scope` | Where applies, explicit exclusions |
| `freshness` | Last corroborated, decay model |
| `review_owner` | Who can promote/retire |

---

## What Does NOT Belong Here

| Concept | Where It Belongs | Why |
|---------|------------------|-----|
| Entity master data | Enterprise Knowledge (MDM) | Asserted, not learned |
| Business rules | Enterprise Knowledge (Policy) | Normative, constrains behavior |
| Definitions | Enterprise Knowledge (Glossary) | Asserted meaning |
| Taxonomies | Enterprise Knowledge (Ontology) | Asserted structure |
| Case-bound events | Episodic Memory | Event-based, time-ordered |

---

## Retention & Forgetting

Semantic Memory should **weaken before it disappears**:

| Mechanism | Description |
|-----------|-------------|
| **Confidence decay** | Without reinforcement, confidence decreases |
| **Replacement** | Stronger, newer patterns supersede older ones |
| **Explicit invalidation** | Disproven beliefs are retired |
| **Scheduled review** | High-impact hypotheses require periodic review |

---

## CAF's Role

CAF is a **control plane** that federates Semantic Memory stores created elsewhere:

| CAF Does | CAF Does NOT |
|----------|--------------|
| Register/catalog stores | Own any store |
| Define schemas | Store data |
| Govern retention | Create stores |
| Enable discovery | Replace existing systems |

---

## Related Documents

- [CAF README](../README.md) — Cognitive Audit Fabric overview
- [Episodic Memory Store](../episodic-memory-store/README.md) — Event-based records
- [Enterprise Knowledge](../../../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/README.md) — Asserted truths
- [Enterprise Semantic Memory (Conceptual)](../../../../olympus-seer-docs/agentic-ai-concepts/enterprise-memory/semantic-memory.md) — Conceptual foundation

