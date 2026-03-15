# Quark — Domain Hubs for Banking

**Pre-built domain hubs for banking — each delivering work models, pre-integrated Machines, Streams, and Loops for a specific banking domain, ready to operate on Evolution Fabric.**

---

## The Problem Quark Solves

Banks buy systems — account platforms, payment engines, card management, fraud engines, CRM. Each system delivers capability. None delivers the operational model that connects them.

The result is predictable: every banking domain — payments, credit cards, lending, servicing — runs on its own ad-hoc assembly of systems, manual procedures, spreadsheet bridges, and tribal knowledge. The operational intelligence of how these systems work together to fulfill a customer commitment or maintain internal discipline is never modeled. It lives in bespoke integration code, in the heads of tenured staff, and in undocumented routines that nobody owns.

This creates three compounding problems:

- **Every new system makes operations harder, not easier.** A bank adds a better fraud engine — and then spends months re-wiring the manual handoffs, escalation paths, and exception-handling routines that connected the old one to everything else. The system is new; the integration burden is larger.
- **AI has no operational context to participate in.** When a bank wants AI to help resolve disputes, process applications, or detect anomalies, there is no explicit model of how that work currently happens — no declared scenarios, no structured context, no governed delegation. Every AI project starts by reverse-engineering the operational reality from scratch.
- **Domain knowledge walks out the door.** When key people leave, the operational knowledge they carried — how exceptions are handled, which workarounds keep things running, what the actual escalation paths are — leaves with them. The systems remain; the operational intelligence disappears.

Quark solves this by delivering **pre-built operational domains** — not just systems, but the explicit, governed work model that makes systems function as a coherent banking operation.

## Product Family

Each Quark hub is a bounded business domain — pre-modeled with the Streams (external commitments), Loops (internal discipline), Machines (pre-integrated system capabilities), Teams (collaboration models), and Channels (interaction surfaces) that the domain requires. Each Quark hub runs on Evolution Fabric (Hub + Seer) and consumes the capabilities of other product families (Tachyon, Photon, Electron, Neutrino) as Machines.

### How Quark Hubs Work

A Quark hub for a banking domain comes with:

- **Pre-modeled Streams** — the external commitments the domain fulfills (e.g., credit card application, dispute resolution, payment processing)
- **Pre-modeled Loops** — the internal discipline the domain maintains (e.g., reconciliation, fraud detection, compliance verification, portfolio analytics)
- **Pre-integrated Machines** — Tachyon, Photon, Electron, and third-party systems registered with declared tool contracts, ready to be invoked by Scenarios
- **Scenario definitions** — goal-oriented work models for each Stream and Loop, with work patterns (queue-based, case-based, event-driven, etc.) and resolution models (automation through human collaboration) pre-configured
- **Team templates** — human-AI collaboration models appropriate to the domain's work

A bank adopting a Quark hub gets an operational domain — not just software capabilities, but the **work model** that makes those capabilities function as a coherent banking operation.

### Domain Hubs

| Quark Hub | Banking Domain | Description |
|---|---|---|
| **Quark Origination** | Prospecting, sourcing, and application processing | Prospecting, lead sourcing, application intake, application assessment, cross-sell, and up-sell capabilities — the full origination lifecycle across products. *(To be expanded)* |
| **Quark Payments** | Payments and money movement | *(To be expanded)* |
| **Quark Credit Card** | Credit card issuance and servicing | *(To be expanded)* |
| **Quark Customer Servicing** | Customer servicing and digital journeys | *(To be expanded)* |
| **Quark CLM** | Customer lifecycle management — offers, rewards, engagement | *(To be expanded)* |
| **Quark Commercial Cards** | Commercial cards, benefits, expense management | *(To be expanded)* |
| **Quark Lending** | Lending products and loan servicing | *(To be expanded)* |
| **Quark Customer Lifecycle** | Customer identity, lifecycle, and behavioral intelligence | Customer IAM (identity, SSO, authentication), identity risk, behavioral risk, and full customer lifecycle governance — from onboarding through active relationship to dormancy and exit. *(To be expanded)* |
| **Quark Merchant** | Acquiring, payment facilitation, payment aggregation | *(To be expanded)* |

---

## Relationship to Fabrics

| Fabric | How Quark Uses It |
|---|---|
| **Evolution Fabric** | Every Quark hub runs on Evolution Fabric. Hub provides the operational substrate (Workbenches, Scenarios, Signals, Requests); Seer provides the AI agent runtime. Quark hubs are the **domain instantiation** of Evolution Fabric's infrastructure |
| **Trust Fabric** | Identity, authentication, and authorization for all participants in a Quark hub — customers, bank staff, AI agents — including delegated authority for agent operations |
| **Truth Fabric** | Semantic grounding for domain-specific terms — ensuring that every Scenario in the hub operates on shared, authority-aware definitions |
| **Cognitive Audit Fabric** | Decision auditability for every judgment call within the hub — whether made by a human, an AI agent, or an automated rule |
| **Cloud Fabric** | Infrastructure management and observability for the hub's deployment — customer-centric health monitoring for the hub's Streams and Loops |

---

## Relationship to Other Product Families

| Family | Relationship |
|---|---|
| **Tachyon** | Tachyon product lines register as Machines in Quark hubs — providing account capabilities (create, modify, close, assess) as declared Tools that Scenarios invoke |
| **Photon** | Photon product lines register as Machines in Quark hubs — providing payment capabilities (authorize, settle, reverse, route) as declared Tools |
| **Electron** | Electron product lines register as Machines in Quark hubs — providing commercial card capabilities (issue, load, authorize, reconcile) as declared Tools |
| **Neutrino** | Neutrino channels are configured per Quark hub — each hub determines which interaction surfaces are available for its Scenarios, and Channel Products compose cross-hub experiences |

---

## The Quark Differentiator

The other product families deliver **what the bank can do** — process accounts, move payments, manage cards, serve customers through channels. Quark delivers **how the bank operates** — the explicit, governed, evolvable model of domain operations.

This is the difference between having capabilities and having an operational domain. A bank with Tachyon and Photon has account and payment systems. A bank with Tachyon, Photon, and a Quark Payments hub has a **payments operation** — with modeled commitments, internal discipline, human-AI collaboration, and the ability to evolve without re-engineering.

---

*This is a placeholder brief. Individual domain hub details to be expanded in subsequent sessions.*
