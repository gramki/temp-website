# Section 4: Audit Requirements for Enterprise Agents — Overview

*What regulatory-grade audit requires and how it differs from operational logging.*

---

## Purpose of This Section

This section addresses one of the most consequential differences between enterprise agents and consumer or business agents: the requirement for regulatory-grade audit. When an enterprise agent makes a decision that affects a customer, an employee, or a business outcome, the organization must be able to explain and defend that decision—potentially years later, to regulators, courts, or customers.

This is not a "nice to have" feature. In regulated industries such as banking, insurance, and healthcare, the inability to explain AI-assisted decisions creates unacceptable legal and regulatory exposure. The EU AI Act explicitly requires high-risk AI systems to provide traceability and human-understandable explanations. OCC SR 11-7 requires documented decision processes for model-assisted decisions. Fair lending laws require adverse action explanations that can be produced on demand.

Yet many organizations approach this requirement by extending their existing logging infrastructure—adding more logs, increasing retention periods, building dashboards. This approach fundamentally misunderstands what audit requires. Audit is not logging with longer retention. It is a distinct discipline with different artifacts, different guarantees, and different consumers.

This section establishes what regulatory-grade audit actually requires: the regulatory context that drives these requirements, why audit is not logging, what the Cognitive Audit Fabric provides as a conceptual framework, how immutability and tamper evidence work, and why explanations must be tailored to multiple audiences.

---

## Subsections

### 4.1 The Regulatory Reality

This subsection establishes the regulatory context that makes audit a non-optional requirement for enterprise agents. It covers OCC SR 11-7 (model risk management), the EU AI Act (high-risk AI systems), fair lending requirements (adverse action explanations), and the fundamental question regulators are asking.

- [4.1 The Regulatory Reality](./04-1-regulatory-reality.md)

### 4.2 Audit Is Not Logging

This subsection distinguishes between operational logging (debugging aid, mutable, rotated) and enterprise audit (evidentiary record, immutable, retained). It explains why extending logging infrastructure does not satisfy audit requirements and what the differences are in purpose, consumers, guarantees, and lifecycle.

- [4.2 Audit Is Not Logging](./04-2-audit-vs-logging.md)

### 4.3 The Cognitive Audit Fabric

This subsection introduces the Cognitive Audit Fabric (CAF) as the enterprise memory control plane—a federated auditability layer for cognitive systems. It describes the core record types (decision records, evidence bundles, context snapshots, outcome records, override records) and the services CAF provides.

- [4.3 The Cognitive Audit Fabric](./04-3-cognitive-audit-fabric.md)

### 4.4 Immutability and Tamper Evidence

This subsection explains the technical mechanisms that make audit records trustworthy: append-only storage, cryptographic content hashing, chain linking, and correction via new records. It establishes why these mechanisms are essential for regulatory defensibility.

- [4.4 Immutability and Tamper Evidence](./04-4-immutability-tamper-evidence.md)

### 4.5 Multi-Audience Explanations

This subsection addresses the requirement to explain the same decision differently to different audiences: customers (plain language, empathetic), operators (technical, actionable), and regulators (complete, defensible). It describes how the Explanation Service generates audience-appropriate explanations from the same underlying records.

- [4.5 Multi-Audience Explanations](./04-5-multi-audience-explanations.md)

---

## Key Concepts Introduced

| Concept | Definition |
|---------|------------|
| **Audit** | Evidentiary records that can be used to reconstruct and defend decisions, as opposed to operational logs for debugging |
| **Decision Record** | Structured documentation of a decision including what was decided, what alternatives existed, what evidence was considered, and what reasoning was applied |
| **Evidence Bundle** | Package of context that was available at decision time, enabling reconstruction of what the agent knew |
| **Cognitive Audit Fabric (CAF)** | Enterprise memory control plane that governs how memory is captured, linked, explained, and audited |
| **Immutability** | Property of records that prevents modification after creation; corrections made via new records |
| **Tamper Evidence** | Cryptographic mechanisms (hashing, chain linking) that reveal any unauthorized modification |
| **Multi-Audience Explanation** | Capability to generate appropriate explanations for different consumers (customer, operator, regulator) |

---

## Prerequisites

This section assumes familiarity with:

- The accountability gap in enterprise agents (Section 2.2)
- The memory taxonomy and governance imperatives (Section 3)
- Why enterprise agents face different requirements than consumer agents (Section 2.1)

---

## Relationship to Other Sections

**Section 3 (Memory Requirements)** provides the foundation for this section. The ESPP memory taxonomy, particularly episodic memory, is the substrate on which audit is built. CAF is the control plane for enterprise memory.

**Section 5 (Building an Enterprise Agent)** references audit requirements when discussing context compilation, the four sources of agent knowledge, and CI/CD for enterprise agents.

**Part 2, Section 4 (Memory, Knowledge & Audit in Seer)** demonstrates how Seer and Hub implement the audit requirements established here, including the specific record types and the Explanation Service.

---

## Cross-References

For detailed implementation specifications, see:

- `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md` — CAF architecture
- `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/explanation-service.md` — Explanation generation
- `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/episodic-memory-store/` — Record schemas
- `caf-requirement-and-approach/caf-requirement.md` — CAF requirement basis
- `olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md` — Implementation concept

---

*Audit is the mechanism by which enterprises answer the question: "Can you prove this decision was reasonable?" This section establishes what that requires.*
