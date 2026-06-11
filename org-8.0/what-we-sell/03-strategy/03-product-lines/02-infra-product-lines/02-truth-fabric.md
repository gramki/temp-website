# Chapter 03.02.02: Truth Fabric — Product Note

**An enterprise semantic layer that makes truth explicit, authority-aware, and traceable — so that systems, teams, and AI can build on shared meaning instead of re-arguing it.**

---

## The Architectural Problem

Large enterprises do not suffer from lack of data. They suffer from lack of agreement about what is true.

Over time, banks accumulate many systems of record, many domain teams, many data pipelines, and many definitions of the same thing. At first, the differences feel manageable. Over time, they surface as inconsistent decisions, regulatory friction, repeated reconciliation debates, and loss of trust in data-driven outcomes.

**A familiar scene.** A customer calls their bank. The mobile app shows $8,000 of available credit. The call center agent sees $5,000. The branch manager sees $6,500. Each system is technically correct — given its own data sources and calculation logic. But no one can explain to the customer what their actual available credit is. During the post-mortem, teams discover that "available credit" means different things in different channels: one system includes pending authorizations, another excludes holds, a third applies a temporary limit increase that expired last week. There is no single answer because there is no single definition — and no explicit authority governing which definition applies.

This is not a technology failure. It is a truth failure.

The consequences compound:

- **Truth is implicit, everywhere.** Every day, someone in the bank decides which credit limit to trust, which customer record to believe, which account status governs a transaction. These decisions happen in pipeline code, in spreadsheets, in meeting rooms, in escalation emails. The enterprise is already deciding what is true — it just does so without a shared language, without traceability, and without consistency.
- **Authority is assumed, not modeled.** Who decides what "available credit" means? Credit Risk sets the approved limit. Retail Operations grants temporary increases. Collections imposes restrictions. Fraud places emergency blocks. Compliance applies regulatory holds. Each is a legitimate authority for its scope. None is wrong. But without explicit modeling, the question has no stable answer — because the governing authority varies by context and time.
- **Reconciliation hides in code.** When systems disagree, the resolution logic leaks into pipelines, applications, and spreadsheets — where it becomes invisible, ungoverned, and duplicated. Every team that needs "the right number" builds its own reconciliation. Each drifts independently.
- **Prior approaches plateaued.** Data warehouses centralized views but coupled to physical schemas. MDM focused on identifiers but not semantics. Canonical data models improved integration but broke under change. Data Mesh scaled ownership but pushed reconciliation into downstream products. Each solved part of the problem. None established a truth boundary the enterprise could rely on.
- **AI amplifies ambiguity into systemic risk.** Historically, humans absorbed inconsistencies — an analyst knew which number to trust, a manager knew which system to check. AI removes that safety net. When models auto-approve credit, recommend limit increases, or decline transactions in real time, semantic inconsistency is encoded into model behavior. Two customers with identical profiles may receive different outcomes depending on which data path fed the model — creating explainability and fair-lending risk that is difficult to unwind after the fact.

The result: every initiative that depends on shared meaning — cross-domain analytics, decision automation, AI, regulatory reporting — begins with a reconciliation project. The cost of implicit truth grows with every system added.

---

## What Truth Fabric Is

Truth Fabric treats enterprise truth as a **design decision** — governed, versioned, and auditable — rather than an emergent property of data quality efforts.

The governing principle:

> **ETSL decides what is true. Everything else decides how to use it.**

Rather than centralizing data or forcing a single schema, Truth Fabric provides the enterprise semantic layer where:

- Systems **assert**. No system publishes truth. Every system publishes assertions — claims about facts, relationships, and state at a point in time.
- Authority **decides**. Which assertions are accepted as valid is determined by explicitly modeled authority — not by which system wrote last, not by tribal knowledge, not by pipeline logic.
- Reconciliation is **transparent**. When assertions conflict, resolution follows governed rules — visible, auditable, and consistent — not buried in code that each team implements differently.
- State is **derived**. Enterprise state — what is true right now — is always derived from authority-qualified assertions. State is never asserted directly; it is the output of reconciliation.
- Semantics are **specified once and executed many times**. Entity definitions, relationships, and vocabulary are modeled as explicit artifacts that every downstream consumer references — not redefines.

Truth Fabric does not centralize data ownership. It centralizes **semantic agreement**. Domains retain their systems, their data products, and their roadmaps. Truth Fabric removes the burden of re-arguing meaning in every initiative.

---

## Capability Domains

### 1. Semantic Foundation

Explicit modeling of what things mean — entities, relationships, and vocabulary — as governed artifacts that the enterprise references rather than each team redefining locally.

| Capability | What It Delivers |
|---|---|
| Semantic Artifacts | Formal definitions of entity types, relationships, and vocabulary — specified once, versioned, and consumed by every downstream system and product |
| Enterprise vocabulary governance | Controlled terminology that prevents semantic drift — "delinquency" means the same thing in credit, collections, and compliance, because the definition is explicit and shared |
| Relationship modeling | How entities relate — account-to-customer, product-to-obligation, party-to-role — modeled structurally rather than inferred from join logic in each pipeline |
| Temporal semantics | "What was true at time T?" as a first-class modeling concern — not an afterthought. Point-in-time queries, bi-temporal awareness, and correction semantics built into the semantic layer |

Semantics are the contract between truth and its consumers. When semantics are implicit, every consumer interprets independently. When semantics are explicit, the enterprise agrees once and builds many times.

### 2. Authority and Reconciliation

Who decides what is true, for what scope, at what time — modeled explicitly rather than assumed, and reconciliation governed rather than hidden in code.

| Capability | What It Delivers |
|---|---|
| Authority modeling | Explicit mapping of which function, system, or role has authority over which facts, for what scope and time. Credit Risk governs limits. Fraud governs blocks. Compliance governs holds. Each is modeled, not assumed |
| Authority Registry | A queryable registry answering: who has authority over this fact, under what conditions, for what time period? Replaces tribal knowledge with explicit, auditable rules |
| Reconciliation engine | When multiple systems assert different values for the same fact, reconciliation resolves them using authority, time, and scope — not "latest wins," not "loudest system wins," not "whoever the analyst trusts" |
| Conflict transparency | How a reconciliation was resolved is documented and auditable — which assertions competed, which authority prevailed, why. The resolution logic is governed, not buried in pipeline code |
| Authority boundary evolution | As operating models change, regulations shift, and organizational structures evolve, authority boundaries can be updated explicitly — without silently breaking downstream consumers |

Authority is what separates enterprise truth from enterprise data. Without explicit authority, "truth" is whoever wrote last. With it, truth is a governed decision.

### 3. Enterprise State Derivation

Point-in-time enterprise truth — derived from authority-qualified assertions, never asserted directly — answering "what is true right now?" and "what was true at time T?"

| Capability | What It Delivers |
|---|---|
| State derivation | Enterprise state computed from reconciled assertions — not copied from a single source system. State reflects the current authoritative view, incorporating all relevant assertions and their resolution |
| Point-in-time reconstruction | The ability to answer "what did we believe was true at any given moment?" — essential for audit, regulatory response, model validation, and dispute resolution |
| Correction semantics | When assertions are corrected or superseded, the correction is traceable — the original assertion, the correction, the authority that made the correction, and the effect on derived state |
| Assertion lineage | Every derived state traces back to the assertions that produced it, the authority that qualified them, and the reconciliation logic that resolved them — end-to-end traceability from truth to its sources |

State is never asserted. It is always derived. This is the discipline that prevents "golden records" from becoming opaque — because every value in state can be traced to the assertions and authority that produced it.

### 4. Data Artifact Engineering

Persisted, authority-qualified, time-aware representations of enterprise truth — the output of Truth Fabric that downstream systems and products consume.

| Capability | What It Delivers |
|---|---|
| ETSL Data Artifacts | Materialized representations of enterprise truth — not raw data, not curated marts, but authority-qualified, temporally-aware, semantically-governed artifacts designed for reuse |
| Platform independence | Data Artifacts are defined semantically and can be represented in multiple physical forms — tables, streams, APIs, files — without changing their meaning. Platform choices stay with platform teams |
| Incremental materialization | Artifacts can be built incrementally — start with one cross-domain entity (e.g., credit limits), expand as value is demonstrated. No big-bang transformation required |
| Reuse without re-argument | The second Data Artifact built on Truth Fabric is faster than the first. The tenth is dramatically faster. Each new artifact benefits from the semantic foundation already established |

Data Artifacts are the interface between truth and its consumers. They tell downstream systems "this is what is true" without requiring those systems to understand how truth was derived.

### 5. Data Product Enablement

The boundary between truth and interpretation — Truth Fabric stabilizes meaning so product teams can iterate faster, not slower.

| Capability | What It Delivers |
|---|---|
| Truth-to-product boundary | A clear separation: Truth Fabric provides authority-qualified facts (e.g., credit limit fact with temporal and authority context). Data Products provide consumer-aligned interpretations (e.g., "available credit" for a mobile app). Products interpret truth; they do not redefine it |
| Semantic contracts for consumers | Data Products reference Truth Fabric artifacts through stable contracts — if the underlying truth changes, products are notified rather than silently consuming stale or redefined data |
| Reduced semantic debate | Product teams stop spending sprint time reconciling definitions and start spending it on customer value. The enterprise argument about "what is the right number" happens once in Truth Fabric, not in every product team |
| Cross-domain product acceleration | Products that previously required months of semantic negotiation — because they spanned credit, fraud, collections, and servicing — now take weeks, because the cross-domain truth is already established |

Truth Fabric does not tell teams what products to build. It tells them what they no longer need to argue about.

### 6. AI and Decision Foundation

The semantic infrastructure that AI systems depend on — because AI amplifies ambiguity, and implicit truth becomes systemic risk at machine scale.

| Capability | What It Delivers |
|---|---|
| Authority-qualified training data | ML models trained on Truth Fabric features are grounded in enterprise-accepted truth — not in pipeline-specific interpretations that vary by team and drift silently over time |
| Stable semantic contracts for features | Feature definitions reference Truth Fabric semantics. When a feature means "credit limit as governed by Credit Risk authority, excluding temporary holds," that definition is explicit, versioned, and stable — not implicit in transformation code |
| Explainability grounded in enterprise semantics | Model explanations trace back to semantically defined inputs — not to undocumented pipeline logic. "This decision was based on the customer's credit limit of $X, as determined by Credit Risk authority at time T" — rather than "this decision used feature_47 from pipeline_v3" |
| Feature drift detection | When upstream definitions change — a new authority boundary, a revised reconciliation rule, a corrected assertion — downstream models are aware. Semantic drift is detected and governed rather than silently degrading model performance |
| Bias and fairness analysis on stable ground | Bias investigations require semantic precision: delinquency vs. hardship, point-in-time vs. retrospective views, authority context. Truth Fabric provides the stable definitions that make bias analysis conclusive rather than inconclusive |

AI does not merely consume data. It operationalizes enterprise assumptions at scale. With AI, ambiguity in enterprise truth is no longer a nuisance — it becomes a systemic risk. Truth Fabric addresses this at the root.

### 7. Governance by Design

Semantic governance through explicit artifacts and modeled authority — not through approval committees, process gates, or documentation that drifts from reality.

| Capability | What It Delivers |
|---|---|
| Explicit Semantic Artifacts | Truth definitions are versioned, reviewed, and visible — not hidden in code or tribal knowledge. Governance is embedded in the artifact, not in a process around it |
| Authority Registry as governance | Which function has authority over which facts is queryable and auditable — governance by design, not by committee |
| Semantic drift review | Proposed changes to truth definitions are reviewed for downstream impact before adoption — preventing silent breakage across consuming systems and products |
| Reconciliation transparency | How conflicts are resolved is documented and auditable, not buried in pipeline logic — regulators and auditors can inspect reconciliation rules, not reverse-engineer them from code |
| Lineage for derived decisions | When data products or operational systems consume Truth Fabric, lineage is preserved — from the final decision back through the product, through the Data Artifact, through reconciliation, to the original assertions |

Governance emerges from design, not from process. This makes Truth Fabric durable in large, federated enterprises where committee-based governance creates bottlenecks and documentation-based governance drifts from reality.

---

## Positioning: Truth Fabric and Data Mesh

Truth Fabric and Data Mesh solve different problems and are complementary:

| Concern | Data Mesh | Truth Fabric |
|---|---|---|
| **Ownership** | Domains own their data products, serve consumers, and move fast | Domains retain full ownership. Truth Fabric does not change this |
| **Cross-domain truth** | Pushes reconciliation to downstream consumers | Resolves cross-domain truth centrally, so consumers don't have to |
| **Semantic agreement** | Each domain defines meaning locally | Shared semantic foundation for cross-domain meaning |
| **Adoption** | Domain-first — teams publish independently | Incremental — engage Truth Fabric when cross-domain truth matters |

Three coexistence patterns are common: **domain-first** (no Truth Fabric involvement — domain publishes independently), **truth-first** (cross-domain, truth-sensitive use cases that require semantic agreement), and **hybrid** (domain products for local use, Truth Fabric for shared enterprise truth). Teams engage Truth Fabric when cross-domain truth matters, not for every initiative.

---

## Relationship to Other Fabrics

Truth Fabric provides the semantic foundation that other enterprise fabrics depend on:

| Fabric | Relationship |
|---|---|
| **[Cognitive Audit Fabric](05-cognitive-audit-fabric.md)** | CAF governs *what was decided* — decisions, evidence, outcomes, overrides. Truth Fabric governs *what was true* — the enterprise-accepted facts those decisions were based on. CAF decision records reference Truth Fabric semantics for stable, auditable inputs. Each stands alone; together they close the loop from truth through decision to accountability |
| **[Trust Fabric](01-trust-fabric.md)** | Trust Fabric governs *who is trusted* — identity, authentication, consent, privacy. Truth Fabric governs *what is true* — enterprise semantics and authority. Trust Fabric establishes the identity of actors and agents; Truth Fabric establishes the meaning of the data they act on |

---

## Regulatory Alignment

Truth Fabric addresses the root cause behind many regulatory findings: the inability to explain decisions consistently over time — not because models are weak, but because enterprise truth is implicit.

| Regulation | Relevant Capabilities |
|---|---|
| SR 11-7 / Model Risk Management | Authority-qualified training data, feature lineage, semantic stability, point-in-time reconstruction |
| Fair Lending (ECOA / HMDA) | Semantic precision for bias analysis, consistent definitions across channels, explainability grounded in enterprise semantics |
| GDPR Art. 22 (automated decisions) | Explainability traced to defined inputs, authority-qualified state, correction semantics |
| SEC / FINRA record-keeping | Point-in-time truth reconstruction, assertion lineage, reconciliation transparency |
| Basel / operational resilience | Cross-domain state consistency, governed reconciliation, temporal reconstruction |
| CFPB adverse action | Decision inputs traceable to enterprise-accepted truth, not pipeline-specific interpretations |
| NIST AI RMF | Trustworthy AI grounded in explicit, governed semantics — addressing data quality, bias, and explainability at the source |

Most regulatory findings do not stem from poor models. They stem from inability to explain decisions consistently over time. Truth Fabric addresses this at the root — by making the truth those decisions depend on explicit, governed, and traceable.

---

## Architectural Position

Truth Fabric occupies a distinct layer in the enterprise architecture — between the systems that assert facts and the products that interpret them:

| Layer | Role |
|---|---|
| **Systems of Record** | Emit assertions — claims about facts, relationships, and state. They are assertion sources, not enterprise truth |
| **Truth Fabric** | Receives assertions, applies authority, reconciles conflicts, derives state, and produces authority-qualified Data Artifacts. This is where enterprise truth is decided |
| **Data Products and AI** | Consume Data Artifacts, interpret truth for specific use cases — analytics, decisioning, customer experiences, operational automation |

Truth Fabric does not replace systems of record, and it does not build data products. It occupies the missing layer between them — the layer where the enterprise explicitly decides what it accepts as true, and makes that decision available to everything that depends on it.

> **Truth Fabric makes truth explicit so teams can build faster without re-arguing meaning.**

---

## References

| Document | Contents |
|---|---|
| [ETSL Purpose and Story](../../../../../pontus/etsl/introduction/etsl-purpose-and-story.md) | Full introduction — the enterprise truth problem, ETSL framing, authority, data products, governance, compounding value |
| [ETSL for CIOs: AI at Scale](../../../../../pontus/etsl/introduction/etsl-for-cios-ai-at-scale.md) | Why ETSL matters for AI — banking examples, regulatory reality, where existing approaches fall short |
| [ETSL One-Page Onboarding Primer](../../../../../pontus/etsl/introduction/etsl-one-page-onboarding-primer.md) | Core vocabulary — the 12 Tier-1 terms that govern all ETSL work |
| [ETSL Documentation Index](../../../../../pontus/etsl/README.md) | Complete corpus — terminology, conceptual foundations, building guides, data product guidance |
