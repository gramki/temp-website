# Cognitive Audit Fabric (CAF)

> **Status:** 🔴 Stub — Placeholder for expansion

The Cognitive Audit Fabric (CAF) is the **Enterprise Memory Control Plane**—the connecting tissue that governs how memory is captured, linked, explained, and audited. CAF provides catalogs, policies, and services but does **not** store the memory itself.

---

## Overview

From the conceptual foundation:

> *"CAF emerges as the connecting tissue: It does not replace knowledge systems. It does not store raw agent memory. It governs how memory is captured, linked, explained, and audited. CAF makes enterprise memory legible and defensible."*

---

## CAF is a Control Plane, Not Storage

| CAF Provides | CAF Does NOT Provide |
|--------------|---------------------|
| **Catalog** of decision records | Storage for decision records |
| **Catalog** of evidence bundles | Storage for evidence bundles |
| **Explanation Service** | Raw data storage |
| Memory capture **policies** | Memory storage itself |
| Linking and indexing **rules** | Operational storage |
| Schema **definitions** | — |

**Where is the actual storage?**
- Decision records and evidence bundles are stored in **Enterprise Memory** (via Memory Services)
- CAF maintains a catalog (metadata, references, indexes) pointing to these records
- CAF enforces policies on how records are structured, linked, and accessed

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Decision Records](./decision-records.md) | Catalog and schema for decision journaling | 🔴 Stub |
| [Explanation Service](./explanation-service.md) | Explanation generation and narrative assembly | 🔴 Stub |
| [Evidence Bundles](./evidence-bundles.md) | Catalog and schema for evidence packaging | 🔴 Stub |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                 COGNITIVE AUDIT FABRIC                           │
│                     (Control Plane)                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                     POLICIES                             │    │
│  │                                                          │    │
│  │  • Memory capture policies (what to capture, when)       │    │
│  │  • Schema definitions (structure of records)             │    │
│  │  • Linking rules (how records relate)                    │    │
│  │  • Retention policies (how long to keep)                 │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                     CATALOGS                             │    │
│  │                                                          │    │
│  │  ┌───────────────────┐  ┌───────────────────┐           │    │
│  │  │ Decision Record   │  │ Evidence Bundle   │           │    │
│  │  │ Catalog           │  │ Catalog           │           │    │
│  │  │ (metadata, refs)  │  │ (metadata, refs)  │           │    │
│  │  └───────────────────┘  └───────────────────┘           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    SERVICES                              │    │
│  │                                                          │    │
│  │  ┌───────────────────────────────────────────────────┐  │    │
│  │  │              Explanation Service                   │  │    │
│  │  │  • Narrative assembly from records                 │  │    │
│  │  │  • Counterfactual generation                       │  │    │
│  │  │  • Multi-audience formatting                       │  │    │
│  │  └───────────────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            │                                     │
│                            │ references                          │
│                            ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │         ENTERPRISE MEMORY (via Memory Services)          │    │
│  │                                                          │    │
│  │  Actual storage of decision records, evidence bundles   │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Core Capabilities

### Decision Journaling
Capture rationale at decision time:
- What was decided
- What alternatives existed
- What evidence was considered
- What reasoning was applied
- Who is accountable

### Evidence Bundles
Package context for reproducibility:
- State of information at decision time
- Documents and data referenced
- Model inputs and outputs
- Retrieval results

### Explanation Generation
Produce human-readable explanations:
- Narrative assembly from records
- Counterfactual generation
- Compliance-appropriate summaries
- Multi-audience formats

### Replay Capability
Reconstruct decisions with original context:
- Time-travel to decision point
- Same inputs produce same explanation
- Audit and investigation support

---

## The CAF Questions

CAF enables answering the critical questions:

| Question | CAF Component |
|----------|---------------|
| *"What was decided?"* | Decision Records |
| *"Why was it decided?"* | Decision Records + Explanation Service |
| *"What was known at the time?"* | Evidence Bundles |
| *"What would have happened otherwise?"* | Counterfactual Generator |
| *"Can we prove this was reasonable?"* | Explanation Service + Evidence Bundles |

---

## Compliance Use Cases

| Requirement | CAF Support |
|-------------|-------------|
| **Model Explainability** | Explain AI decisions in human terms |
| **Fair Lending** | Document decision factors and outcomes |
| **Right to Explanation** | Generate customer-facing explanations |
| **Audit Response** | Produce evidence packages on demand |
| **Dispute Resolution** | Reconstruct decision context |

---

## Seer Integration

| Integration Point | Description |
|-------------------|-------------|
| **Agent Observability** | Decision traces feed CAF |
| **Context Assembly** | CAF receives context snapshots |
| **Runtime Enforcement** | Policy violations logged |
| **Workbench Integration** | CAF accessed through Hub Workbench |

---

## Workbench as CAF Memory Provider

From the Todo notes:
- Workbench with Enterprise Memory Storage Services
- Enterprise Memory Storage Services as part of Seer
- Workbench Enterprise Memory Stores to CAF Memory mapping
- Workbench serving as CAF Memory Provider

---

## Related Documentation

- [Memory Services](../memory-services/README.md) — Enterprise Memory storage
- [Hub Enterprise Memory](../memory-services/hub-enterprise-memory.md) — Memory layer
- [Seer Agent Observability](../../../olympus-seer-docs/seer-design/subsystems/agent-observability.md)

---

*TODO: Detailed design — CAF schema, explanation templates, linking semantics, compliance mappings*

