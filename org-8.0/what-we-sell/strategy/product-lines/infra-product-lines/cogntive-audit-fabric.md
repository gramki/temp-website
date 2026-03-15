# Cognitive Audit Fabric — Product Note

**A federated governance layer that makes enterprise cognitive systems — ML models, GenAI workflows, and AI agents — auditable, reconstructable, and accountable without centralizing them.**

---

## The Architectural Problem

Banks have always had systems that make decisions. What has changed is the nature, scale, and opacity of those decisions — and the audit infrastructure has not kept pace.

The consequences compound:

- **Cognitive systems exercise judgment at scale, with no audit infrastructure.** Banks operate hundreds of systems that decide, recommend, or exercise discretion — credit approvals, fraud escalation, collections strategies, compliance screening, customer routing. Each produces outcomes that may need to be explained, defended, or reconstructed. There is no consistent way to answer: what was decided, on what basis, and who was accountable.
- **Memory is scattered and unowned.** Decision rationale lives in logs, emails, tickets, model outputs, investigator notes, and spreadsheets — across different systems, different formats, different retention policies. Transactional data is owned by IT. Documents by knowledge management. Logs by platform teams. Rationale by individuals. Context by no one. No function owns the reconstructability of decisions end-to-end.
- **Traditional audit doesn't work for adaptive systems.** SOPs, sampling audits, and static documentation were designed for deterministic processes that behave the same way every time. ML models drift. Agents adapt. GenAI responses vary. The assumption of consistent behavior — the foundation of traditional audit — no longer holds.
- **Regulators are asking different questions.** The shift from "was the process followed?" to "was the decision reasonable given what was known?" demands decision rationale, alternatives considered, evidence used, and override justification. Auditors now expect counterfactual explanations, reasoning traces, and confidence bounds. Most banks cannot produce these for their existing decision systems, let alone for AI.
- **AI agents compound the problem.** Agents acting at scale — resolving disputes, processing applications, executing compliance steps — produce thousands of judgment calls per day. Each call involves evidence evaluation, tool usage, and reasoning that is neither fully deterministic nor easily inspectable. Without a fabric to capture what each agent decided, why, and with whose authority, enterprise AI deployment is either ungovernable or blocked by compliance.

The result: every cognitive system deployed without audit infrastructure creates a growing liability — discoverable in litigation, unexplainable to regulators, unreconstructable in incident response.

---

## What CAF Is

CAF is a **fabric**, not a platform or repository. It coordinates and governs memory and auditability without centralizing domain systems.

The governing principle:

> **Memory lives close to action. Governance lives centrally.**

CAF does not move data. It makes data discoverable, interpretable, and auditable across heterogeneous systems. Specifically, CAF provides:

- A **control plane** for cognitive audit requirements — what must be captured, how long it must be retained, who can access it.
- **Standards and interfaces** for decision and action records — a common envelope that wraps domain-specific content.
- **Discovery and replay orchestration** across federated domains — find relevant records regardless of which system produced them, and reconstruct what happened on demand.
- **Explanation generation** for multiple audiences — regulators, auditors, customers, operations — from the same underlying records.
- A common language for regulators, auditors, and risk owners to reason about cognitive systems.

CAF exists to answer one question:

> *"If this system exercised judgment at scale, can we later reconstruct what happened, under what policy, with whose authority, and whether it remained controlled over time?"*

The bar is **reasonable reconstruction**, not omniscience. Regulators do not expect total recall. Auditors expect defensible evidence. Courts expect good faith. CAF is designed to that standard.

---

## Capability Domains

### 1. Cognitive System Registry

An enterprise-wide inventory of every system that exercises judgment — not just AI, but any system that decides, recommends, classifies, or exercises discretion.

| Capability | What It Delivers |
|---|---|
| System inventory | Catalog of all cognitive systems — ML models, rule engines, GenAI workflows, agentic systems, human-machine decision chains — with their purpose, scope, and operational status |
| Risk classification | Each system classified by risk level (high / medium / low) based on regulatory exposure, decision impact, and autonomy level — driving retention, audit, and governance requirements |
| Ownership and accountability | Named business owner and named technical owner for every cognitive system, with escalation authority and intervention rights |
| Change and version traceability | Model versions, rule set versions, prompt template versions, configuration versions, and deployment metadata — what was running, when, and what changed |

Without a registry, the enterprise cannot answer "what cognitive systems do we have?" — the prerequisite for governing any of them.

### 2. Decision and Action Memory

Standardized capture of what cognitive systems decide and do — structured for reconstruction, not just logging.

| Capability | What It Delivers |
|---|---|
| Decision records | What was decided, what alternatives existed, what reasoning was applied, what confidence level, and who is accountable — captured at decision time, not reconstructed after the fact |
| Evidence bundles | The state of information at the moment of decision — data inputs, model outputs, retrieval results, documents referenced — packaged for reproducibility |
| Action records | What was executed as a result of the decision — the operational consequence, linked back to the decision that triggered it |
| Outcome records | What happened after the decision — did the outcome match the intent? Enables feedback loops and post-decision analysis |
| Context snapshots | Compiled state per decision point — what the agent or system knew, what tools it had access to, what constraints applied |

Decision records are not logs. Logs capture events. Decision records capture judgment — the reasoning, evidence, and accountability that make a decision defensible.

### 3. Override and Intervention Governance

When a human overrides, redirects, or intervenes in a cognitive outcome, that act must be captured with the same rigor as the original decision.

| Capability | What It Delivers |
|---|---|
| Override records | What was overridden, by whom, with what authority, and with what justification — linked to the original decision record |
| Directive resolution tracking | Full lifecycle of human interventions — from the directive issued, through agent response, to resolution and outcome |
| Authority chain capture | The approval matrix or role reference that authorized the override — proving the overrider had the authority to act |
| Handoff context | When work transfers between agents, or between an agent and a human, the context that transfers with it — what was known, what was decided, what remains open |

Overrides are among the highest-risk audit events in cognitive systems. An unexplained override of an AI decision is a regulatory finding waiting to happen. CAF makes every override auditable without requiring free-text justification that may itself become a liability.

### 4. Explanation Generation

Producing human-readable explanations from structured decision records — for regulators, auditors, customers, and operations — without requiring the cognitive system to explain itself.

| Capability | What It Delivers |
|---|---|
| Narrative assembly | Constructing coherent explanations from decision records, evidence bundles, and outcome records — turning structured data into defensible narrative |
| Counterfactual generation | Answering "what would have happened otherwise?" — what the decision would have been with different inputs, different thresholds, or different policies |
| Multi-audience formatting | The same decision explained differently for a regulator (compliance language), an auditor (evidence focus), a customer (plain language), and operations (technical detail) |
| Compliance-specific explanations | Adverse action notices, fair lending documentation, right-to-explanation responses — generated from decision records rather than hardcoded templates |

Explanation is separated from decision by design. The cognitive system decides. CAF explains. This avoids the problem of systems that can act but cannot account for their actions.

### 5. Audit Discovery and Replay

Finding relevant records across domains and reconstructing what happened — on demand, without heroic forensics.

| Capability | What It Delivers |
|---|---|
| Cross-domain artifact discovery | Locate relevant decision records, evidence bundles, overrides, and outcomes regardless of which domain system produced them — fraud, credit, collections, servicing — from a single query surface |
| Decision replay | Reconstruct a decision with its original context — the same evidence, the same policy version, the same model version — to verify that the outcome was consistent with what was known |
| Reconstruction bundles | Assembled packages of all artifacts related to a case, incident, or regulatory inquiry — ready for review without requiring investigators to query each domain separately |
| Integrity attestation | Cryptographic proof that records have not been altered since capture — content hashing, append-only guarantees, tamper-evident chains |

Replay is what turns decision memory from a compliance exercise into an operational capability. Incident response, dispute resolution, and regulatory examination all require reconstruction — CAF makes it a standard operation, not an emergency project.

### 6. Federated Memory Architecture

Memory stays in the domain that produced it. CAF provides the governance, discovery, and orchestration layer — not the storage.

| Capability | What It Delivers |
|---|---|
| Domain-owned memory stores | Each domain — fraud, credit, collections, servicing, compliance — owns and operates its own memory store. Domain systems capture their own decisions, evidence, and outcomes in their own infrastructure |
| Standardized artifact envelope | A common wrapper for every memory artifact — artifact type, actor identity, timestamp, policy references, integrity hash, retention class — while domain-specific content remains domain-defined |
| Central metadata index | CAF maintains a catalog of what exists, where it lives, who can access it, and how long it must be retained — metadata and pointers, not the records themselves |
| Domain memory contracts | Each domain publishes what it captures, at what fidelity, what artifact types it produces, what replay guarantees it offers, and what redaction profiles it supports — making federation predictable |

Centralization fails for structural reasons: ownership ambiguity, liability gravity, cost explosion, and semantic mismatch across domains. Federation works because it respects domain ownership while providing the cross-cutting governance that no single domain can provide alone.

### 7. Memory Lifecycle and Integrity

Governing how long memory lives, who can see it, and proving it hasn't been tampered with.

| Capability | What It Delivers |
|---|---|
| Retention and redaction policies | Risk-weighted retention requirements — full retention for high-risk decisions, summarized retention for low-risk, sampling where regulatorily permitted — applied consistently across domains |
| PII separation | No personally identifiable information in cognitive records. Entity references (opaque tokens) replace personal identifiers. PII is resolved at runtime through separate, access-controlled channels — simplifying GDPR/CCPA compliance for immutable records |
| Cryptographic integrity | Content hashing of every record at write time. Append-only storage. Tamper-evident design — any modification changes the hash, revealing alteration |
| Purpose-limited access | Different views for different consumers — operations see full records, auditors see scoped views, regulators see compliance-formatted summaries, dispute resolution sees redacted customer-safe versions — enforced by policy at the domain provider |
| Tiered storage | Full fidelity for high-risk artifacts, summarized or hashed retention for low-risk, configurable by domain and risk classification — controlling cost without sacrificing auditability for material decisions |

Immutable records with no PII is a deliberate design choice. It eliminates the tension between "records cannot be changed" (audit requirement) and "records must be deletable" (privacy requirement) — because there is nothing to delete.

---

## Regulatory Alignment

CAF is designed to meet the requirements of converging regulatory frameworks from a single governance layer, rather than implementing each regulation as a separate audit project.

| Regulation | Relevant Capabilities |
|---|---|
| EU AI Act | Cognitive system registry, risk classification, decision records, explanation generation, human accountability |
| SR 11-7 / Model Risk Management | System registry, model versioning, decision replay, outcome tracking, change traceability |
| GDPR Art. 22 (automated decisions) | Right to explanation, counterfactual generation, override records, multi-audience explanations |
| GDPR / CCPA (data rights) | PII separation, purpose-limited access, retention policies, entity-reference-only design |
| SEC / FINRA record-keeping | Decision retention, tamper-evident records, integrity attestation, replay capability |
| Fair Lending (ECOA / HMDA) | Decision factor documentation, adverse action explanations, outcome records |
| FCA / PRA (UK accountability) | Named ownership, override governance, escalation authority, intervention tracking |
| Basel / operational resilience | Incident timelines, cross-domain reconstruction, integrity attestation, replay bundles |

Each new regulatory requirement maps to capabilities already present in the fabric. Compliance becomes configuration, not construction.

---

## Architectural Position

CAF spans three foundational systems in the enterprise architecture:

| System | CAF Role |
|---|---|
| **System of Intelligence** | Decision memory, evidence capture, context snapshots, explanation generation, replay |
| **System of Enforcement** | Override governance, policy-version tracing, compliance attestation, intervention tracking |
| **System of Record** | CAF does not replace — it references. Domain records stay domain-owned; CAF provides the index, governance, and reconstruction orchestration |

CAF is the governance layer between cognitive systems and the enterprise's accountability obligations. Every cognitive system — whether ML model, rule engine, GenAI workflow, or AI agent — produces auditable memory through CAF rather than implementing its own audit approach. The result: one governance model for cognitive accountability, federated by design, defensible by construction.

> **CAF turns audit from a brake on AI adoption into an enabler of safe scale.**

---

## References

| Document | Contents |
|---|---|
| [Cognitive Audit Fabric — Concept](../../../../caf-requirement-and-approach/cognitive-audit-fabric.md) | Purpose, definition, core capabilities, architectural principle |
| [CAF Requirement Basis](../../../../caf-requirement-and-approach/caf-requirement.md) | Background analysis, enterprise shifts, memory infrastructure problem, federation architecture, domain memory blueprint |
| [CAF Hub Subsystem](../../../../olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md) | System design — memory stores, record schemas, APIs, typed content conventions, Seer integration |
