# Chapter 03.02.00: What Is a Fabric?

**A fabric is a single-concern system of record and/or processing, woven horizontally across the enterprise, that exposes its capabilities through contracts for any product, channel, or Hub to draw on — without embedding the workflow that orchestrates them.**

---

## The Metaphor, Made Precise

"Fabric" connotes a pervasive, horizontal weave — the same framing used for data fabric, service fabric, network fabric. The word signals something that underlies and supports, something woven throughout rather than stacked on top.

In banking software, the opposite of fabric is monolith. Traditional core banking systems package everything together: accounts, payments, cards, loans, ledger, compliance — all in one tightly-coupled system where changing one capability risks breaking others, where the customer record is inseparable from the transaction engine, where regulatory reporting is entangled with product logic.

The fabric framing decomposes the monolith. Instead of one system that does everything, the enterprise is woven from many fabrics — each owning a single concern, each independently deployable, each exposing its capabilities through contracts that any product or channel can draw on.

---

## Seven Defining Properties

A system qualifies as a fabric when it exhibits all seven of these properties:

| Property | What It Means |
|---|---|
| **Single concern** | The fabric owns one coherent domain — not a grab-bag of related functions. Accounting Fabric owns the ledger. Customer Record Fabric owns identity and relationships. A fabric that tries to own too much becomes a monolith by another name. |
| **Horizontal / pervasive** | The fabric is drawn on across the enterprise — by multiple products, multiple channels, multiple Hubs. A fabric that serves only one product line is a component, not a fabric. |
| **Contract-exposed** | Capabilities are accessed through stable, versioned contracts — APIs, events, schemas. The fabric's internals are hidden; consumers depend on the contract surface, not on implementation details. |
| **Orchestration-free** | The fabric does not embed workflow logic. It provides capabilities that workflows assemble. A Hub orchestrates; a fabric contributes. When a fabric starts embedding "when this happens, do that" logic, it has crossed into orchestration territory. |
| **Independently deployable and replaceable** | The fabric can be deployed, upgraded, or replaced without re-engineering its neighbors. This is the practical test of loose coupling. If changing the fabric requires coordinated releases across other systems, the boundary is leaking. |
| **Authoritative (source of truth)** | The fabric is the system of record for its domain entities. Other systems may cache, replicate, or derive — but when the question is "what is the authoritative state?", the answer points to the fabric. |
| **Integrity- and compliance-enforcing** | The fabric upholds invariants regardless of what consumers request. It enforces a compliance floor that cannot be configured away. The fabric refuses requests that would violate its integrity guarantees. |

These seven properties are not aspirational. They are definitional. A system that lacks any of them is something else — a service, a module, a component — but not a fabric.

---

## Fabric as Authoritative Domain System

The source-of-truth and integrity emphasis distinguishes a fabric from a mere service.

A service provides functionality. A fabric provides functionality **and** is the authoritative custodian of domain truth. The difference matters:

- **The fabric owns its domain entities.** Customer Record Fabric owns customer identity, relationships, and lifecycle state. Accounting Fabric owns the ledger and all accounting entries. These are not caches of data held elsewhere; they are the authoritative records.

- **The fabric enforces invariants always.** Invariants are the business rules that must never be violated — debits must equal credits, a customer's identity must be verified before account opening, a credit limit cannot be exceeded without explicit override. The fabric does not rely on consumers to enforce these; it enforces them itself, rejecting requests that would create invalid state.

- **The fabric upholds a compliance floor.** Some things are configurable — interest rates, fee structures, workflow timing. Other things are non-negotiable — regulatory requirements, audit trail completeness, data integrity. The compliance floor is what the fabric guarantees regardless of configuration.

This is why fabrics are described as systems of record and/or processing. Some fabrics are primarily about owning data (Customer Record Fabric). Some are primarily about processing (Card Issuer Transaction Processing Fabric). Many are both. All are authoritative for their domain.

---

## Fabric Responsibilities, Drawn from DDD

The fabric concept draws heavily from Domain-Driven Design. The mapping is not cosmetic — it explains why fabrics work the way they do:

| DDD Construct | Fabric Responsibility |
|---|---|
| **Bounded Context** | Each fabric owns a ubiquitous language for its domain. "Account" means one thing in Accounting Fabric, potentially something related but distinct in Demand Deposit Fabric. The boundary prevents semantic pollution. |
| **Aggregate + Aggregate Root** | Changes to fabric state go through defined entry points (aggregate roots) that enforce consistency. You don't update a ledger entry directly; you post to an account, and the account maintains consistency. |
| **Invariants** | The fabric's invariants are the business rules that are always upheld. These are not validation hints — they are structural guarantees. Invalid states are unreachable because the fabric refuses transitions that would create them. |
| **Entities & Value Objects** | The fabric is the system of record for entities with identity and lifecycle (customers, accounts, transactions) and value objects that describe them (addresses, monetary amounts, dates). |
| **Repository** | The fabric owns the authoritative persistence boundary. External systems don't reach into the fabric's database; they go through the contract surface. |
| **Domain Events** | When fabric state changes, the fabric emits authoritative state-change signals. These are the events that Cognition Fabric consumes and routes. The fabric is the source of domain events, not a relay for events generated elsewhere. |
| **Anti-Corruption Layer** | The fabric validates inputs at its boundary. Requests that would violate invariants are refused at the edge — the corruption does not leak in. This is boundary integrity, not input validation as a courtesy. |

Understanding the DDD foundation explains why fabrics are strict about boundaries, why they refuse invalid requests, and why they emit authoritative events. These are not arbitrary design choices; they are the architectural discipline that makes decomposition possible without chaos.

---

## Configurability Without Surrendering Integrity

Fabrics must be configurable — different banks, different jurisdictions, different products require different policies. But configurability has limits.

The principle: **configurable invariants (policy surface) over a non-negotiable integrity floor.**

| Layer | What It Means |
|---|---|
| **Policy surface** | What flexes for bank policy and jurisdiction. Interest calculation methods. Fee schedules. Grace periods. Notification timing. These are configured per deployment, per product, per jurisdiction. |
| **Integrity floor** | What is guaranteed regardless of configuration. Double-entry balance. Audit completeness. Data integrity. Regulatory minimums. These cannot be configured away — they are the fabric's non-negotiable guarantees. |

When a bank deploys a fabric, it configures the policy surface for its context. The integrity floor travels with every configuration. A misconfigured policy might produce a suboptimal customer experience; it cannot produce an integrity violation.

This is why the fabric test (below) asks: "What is configurable vs. its compliance floor?" Every fabric must answer this clearly. If everything is configurable, there is no integrity guarantee. If nothing is configurable, the fabric cannot adapt to real-world variation.

---

## What a Fabric Is NOT

Clarity about what a fabric is requires clarity about what it is not:

| Not a Fabric | Why |
|---|---|
| **Monolithic core system** | A core banking system packages many concerns together, tightly coupled. A fabric owns one concern and is loosely coupled. The point of fabric architecture is to decompose the monolith. |
| **Hub / orchestration layer** | Hubs assemble Machines from fabric capabilities and orchestrate workflow. Fabrics provide capabilities; Hubs compose them. A fabric that starts orchestrating workflow is stepping out of its role. |
| **Product line / offering** | A product line (Tachyon, Photon) is a market-facing offering that bundles value. A fabric is an architectural component. Product lines draw on fabrics; they are not fabrics themselves. |
| **Point integration / microservice** | A microservice might provide a single capability without being authoritative for domain truth. A fabric is both capability provider and system of record. The authority and integrity commitments distinguish it. |
| **Utility function** | A logging service, a notification gateway, a file converter — these provide utility without owning domain truth. Fabrics are not utilities; they are authoritative domain systems. |

If you're unsure whether something is a fabric, apply the seven properties. Missing any one disqualifies it.

---

## The Two Species: Infra Fabric vs. Banking Fabric

All fabrics share the same definition. Two species emerge based on domain specificity:

| Species | Scope | Examples |
|---|---|---|
| **Infra Fabric** | Domain-neutral enterprise systems. These are not banking-specific; they would exist in any large enterprise running at scale with AI. | Trust Fabric, Truth Fabric, Cloud Fabric, Agent Fabric, Memory Fabric, Cognition Fabric |
| **Banking Fabric** | Banking-specific systems of record and processing. These are the fabrics that embody banking domain knowledge. | Accounting Fabric, Customer Record Fabric, Demand Deposit Fabric, Revolving Credit Fabric, Underwriting Fabric |

The distinction matters for two reasons:

1. **Infra Fabrics are prerequisites.** A bank can operate Banking Fabrics without having formalized its Infra Fabrics — but not well. Trust Fabric (identity, consent, agent accountability) and Truth Fabric (semantic agreement, authority) are foundational. Building Banking Fabrics without them creates the same integration debt that plagued monolithic cores.

2. **Both are drawn on by Hubs.** When a Hub assembles a Machine for loan origination, it draws on Infra Fabrics (Trust for identity, Agent for AI workforce, Memory for context) and Banking Fabrics (Customer Record, Product, Underwriting, Term Loans). The Hub does not distinguish species; it composes capabilities from both.

---

## Adjacency: Fabric Authority vs. Truth Fabric

Each fabric is locally authoritative for its own entities. Customer Record Fabric is the source of truth for customer identity. Accounting Fabric is the source of truth for the ledger. This local authority is what makes fabrics systems of record.

But enterprises also need **cross-fabric semantic agreement**: when Accounting Fabric refers to a "customer" and Customer Record Fabric refers to a "customer," do they mean the same thing? When Demand Deposit Fabric calculates "available balance" and Revolving Credit Fabric calculates "available credit," are the calculations consistent?

This is where Truth Fabric enters:

| Concern | Where It Sits |
|---|---|
| **Entity authority** | Local — each fabric is authoritative for its own entities and their invariants |
| **Semantic agreement** | Truth Fabric — governs cross-fabric vocabulary, meaning, and reconciliation |
| **Authority arbitration** | Truth Fabric — when multiple fabrics might claim authority over a shared concept, Truth Fabric models the authority explicitly |
| **Reconciliation** | Truth Fabric — when fabrics assert different values for related facts, Truth Fabric governs how the conflict is resolved |

The relationship is complementary: Banking Fabrics own their domains; Truth Fabric ensures the domains speak a coherent language. A bank can operate Banking Fabrics without Truth Fabric — but cross-domain analytics, AI, and regulatory reporting will require the same semantic reconciliation that created integration debt before fabrics existed.

---

## The Fabric Test

Three questions applied to every fabric — if any answer is unclear, the fabric definition is incomplete:

| Question | What a Good Answer Looks Like |
|---|---|
| **What entities is this fabric the source of truth for?** | Specific entities with identity and lifecycle: accounts, customers, transactions, loans, cards. Not "data" in general — specific domain entities. |
| **What invariants does it enforce?** | Specific business rules that are always upheld: debits equal credits, credit limits are not exceeded without override, customer identity is verified before account opening. These are not configurable; they are guaranteed. |
| **What is configurable vs. its compliance floor?** | Clear separation: interest rates and fee schedules are configurable; double-entry integrity and audit completeness are not. The compliance floor is explicit. |

A fourth question applies to the composition test — verifying that the fabric participates in the architecture as intended:

| Question | What a Good Answer Looks Like |
|---|---|
| **Is this fabric drawn on by more than one product/Hub, and replaceable without re-engineering neighbors?** | Yes — if the fabric serves only one product, it's a component of that product, not a fabric. If replacing it requires coordinated releases across many systems, the boundary is leaking. |

Every Banking Fabric note in this series answers these questions in its "Source of Truth" section. The test operationalizes the fabric definition — it is not a philosophical exercise but a practical verification that the fabric meets its architectural commitments.

---

## References

| Document | Contents |
|---|---|
| [Infra Fabrics](../01-infra-fabrics/) | The 12 domain-neutral enterprise fabrics: Trust, Truth, Cloud, Evolution, Agent, Memory, Cognition, Engagement, Influence, Intelligence, Experimentation |
| [Truth Fabric](../01-infra-fabrics/02-truth-fabric.md) | Enterprise semantic layer — cross-fabric truth, authority modeling, reconciliation |
| [Trust Fabric](../01-infra-fabrics/01-trust-fabric.md) | Identity, authentication, consent, privacy, agent accountability |
| [Agent Fabric](../01-infra-fabrics/06-agent-fabric.md) | AI workforce infrastructure — agent lifecycle, deployment, capability routing |
