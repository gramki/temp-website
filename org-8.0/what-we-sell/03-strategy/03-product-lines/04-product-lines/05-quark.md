# Chapter 03.04.05: Quark — Domain Hubs for Banking

**Zeta's pre-built commercial delivery of domain-specific Hub classes, packaging complete Bounded Work Architectures with out-of-the-box Agent Swarms to operate natively on Evolution Fabric and orchestrate core banking systems as Machines.**

---

## 1. The Core Shift: From Software Capabilities to Bounded Work Architectures

Historically, banks have purchased systems — core ledgers, payment processors, card platforms, customer relationship managers (CRMs). Each of these systems provides a discrete *software capability*, but none provides the *operational model* that binds them together. 

The result is an ad-hoc assembly of manual procedures, custom integration code, and tribal knowledge. The intelligence of how systems interact to fulfill customer commitments or enforce internal disciplines is never modeled; it lives in integration plumbing and the heads of tenured staff.

**Quark** represents a fundamental paradigm shift. Rather than selling raw software capabilities, Quark delivers **pre-packaged Bounded Work Architectures (Work Models)**. A Quark domain package provides an explicit, model-driven operational structure that organizes the bank's people, automated systems, AI agents, and communication channels into a unified domain boundary.

Each Quark package delivers a fully configured Work Model composed of six architectural primitives:

```
                  ┌─────────────────────────────────────────┐
                  │                 CHANNELS                │
                  │ (Unified SRE Workspaces, Conversational)│
                  └────────────────────┬────────────────────┘
                                       │
                  ┌────────────────────▼────────────────────┐
                  │                SCENARIOS                │
                  │      (Goal-Directed Execution Unit)     │
                  └──────────┬───────────────────┬──────────┘
                             │                   │
              ┌──────────────▼──────┐     ┌──────▼──────────────┐
              │       STREAMS       │     │        LOOPS        │
              │(External Commitments)│     │(Internal Discipline)│
              └──────────────┬──────┘     └──────┬──────────────┘
                             │                   │
              ┌──────────────▼──────┐     ┌──────▼──────────────┐
              │        TEAMS        │     │       MACHINES      │
              │  (Human-AI Swarms)  │     │   (Tool Contracts)  │
              └─────────────────────┘     └─────────────────────┘
```

1. **Pre-Modeled Streams (External Commitments)**: Episodic workflows triggered by external actions crossing the domain boundary. They progress through structured stages to meet concrete outer-world commitments.
2. **Pre-Modeled Loops (Internal Discipline)**: Schedule-triggered or pattern-triggered cycles of continuous feedback that maintain the domain's risk posture and operational hygiene (e.g., daily ledger reconciliation, fraud transaction sweeps, portfolio utilization reviews).
3. **Adaptive Scenarios (Atomic Execution)**: Goal-oriented declarations of *what* must be achieved. Because they focus on goals rather than hard-coded paths, Scenarios dynamically adapt to exceptions, allowing human operators and AI agents to collaborate in real-time.
4. **Pre-Configured Teams (The Unified Workforce)**: Templates that organize human specialized operators and AI Agent Swarms into collaborative, permissioned groups.
5. **Pre-Integrated Machines (System Capabilities)**: Physical and logical systems (such as Tachyon, Photon, or legacy systems) that are registered via stable **Tool Contracts** (using the Model Context Protocol, or MCP).
6. **Built-in Channels (Interaction Surfaces)**: Pre-packaged user interfaces (like human SRE Workbenches, client messaging surfaces, and voice portals) tailored to the domain's roles.

---

## 2. Domain-Level Hub Scoping (The Quark-Neutrino Boundary)

Quark Domain Packages partition operational boundaries cleanly based on the bank's two core domain archetypes:

### I. Product Domains (Deposits, Credit Cards, Lending, Commercial Cards)
For any product-focused domain, Quark delivers the commercial back-office brain — the **Product Hub**:
- **Role:** Governs product blueprinting, interest rates, fee matrices, dynamic bundling, and marketing campaigns. PMs use it to declare rates and budget limits.
- **The Quark-Neutrino Boundary:** While Quark delivers the back-office Product Hub, the corresponding consumer-facing and RM-facing experience layers (**Distribution Hub** and **Relationship Hub**) for these product domains are delivered and run under the **Neutrino** Product Line Experience, not Quark.

### II. Service Domains (Payments, Disputes, Clearing, Compliance, Sourcing)
For transactional or back-office service domains, Quark delivers the operational and technical back-office engines — the **Operations Hub** and **Systems Hub**:
- **Operations Hub (per Service Domain):** Governs back-office exception workflows, clearing file reconciliation loops, manual dispute casework, and compliance cases. These utilize Zeta's highly modular, pre-packaged banking fabric components (like *Transfers Fabric*, *Disputes Fabric*, *Card Issuer Txn Processing Fabric*) as their System Capabilities (Machines), invoking them via secure MCP Tool Contracts.
- **Systems Hub (per Service Domain):** Monitors runtime metrics, USE signals, tool contract audit logs, and agent token quotas for that service domain.

---

## 3. Core Native Assets (The Quark Baselines)

Quark is built upon a baseline of native operational assets that provide the foundational party and product truths of the bank. These core assets are **native to Quark** and cannot be divorced from its runtime:

- **Customer Record Fabric:** Quark's native System of Record for master party data, customer lifecycle states, and core KYC profiles.
- **Product Fabric:** Quark's native System of Record for active product blueprints, commercial metadata structures, interest matrices, and fee tables.
- **Customer Hub:** Quark's native party-governance Hub. It orchestrates party onboarding, identity verification transitions, and KYC refresh loops.

### The Structural Invariant
The native hubs require relevant native fabrics of the Hub to ensure core operational integrity. This creates two un-breakable binding invariants:
- **Product Hub** natively binds to and requires the **Product Fabric**.
- **Customer Hub** natively binds to and requires the **Customer Record Fabric**.

These baseline pairs act as the bedrock upon which all other downstream experience or processing layers operate.

---

## 4. Fabric Substitution & Customization Policies

Quark acts as the orchestrator over Zeta's core system capabilities, enforcing strict boundaries regarding what can be substituted by custom bank code:

### I. Infrastructure Fabrics are Non-Substitutable
Quark runs natively on and is deeply coupled with **all of Zeta's Infra Fabrics** (Trust, Truth, Cloud, Evolution, Agent, Memory, Cognition, Engagement, Intelligence, Experimentation, Foundry). These form the secure, unalterable technical substrate, and **cannot** be substituted with customer-authored fabrics. They represent the non-negotiable core capability layer of the bank.

### II. Banking Fabrics are Substitutable & Integratable
Unlike Infra Fabrics, the underlying core transactional or banking fabrics (such as custom general ledgers, core credit databases, card processors, or third-party CRM fabrics) **are substitutable**. Banks can easily integrate, swap, or extend these systems, exposing them to Quark Hubs as **Machines** via secure MCP Tool Contracts without disrupting the Hub's Work Model.

---

## 5. Architectural Topology

By establishing this clear boundary, a bank's operational topology splits cleanly between administrative backend operations (Quark) and front-end experience channels (Neutrino):

```
           ┌──────────────────────────────────────────────────┐
           │              THE BANK'S ENTERPRISE               │
           └────────────────────────┬─────────────────────────┘
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         │                                                     │
┌────────▼───────────────────────────┐               ┌────────▼───────────────────────────┐
│     QUARK (CORE BACK-OFFICE)       │               │     NEUTRINO (FRONT-EXPERIENCE)    │
├────────────────────────────────────┤               ├────────────────────────────────────┤
│ - Customer Hub (Native Party SOR)  │               │ - Distribution Hubs                │
│ - Product Hubs (Product Blueprints)│               │   (Onboarding, Funnel Management)  │
│ - Operations Hubs (Service Exceptions)             │ - Relationship Hubs                │
│ - Systems Hubs (SRE Observability) │               │   (Client-facing Servicing, RMs)   │
└────────┬───────────────────────────┘               └────────┬───────────────────────────┘
         │                                                    │
         └──────────────────────────┬─────────────────────────┘
                                    │
     ┌──────────────────────────────▼──────────────────────────────┐
     │                       EVOLUTION FABRIC                      │
     │            (Domain Runtime & Agentic Orchestration)         │
     └──────────────────────────────┬──────────────────────────────┘
                                    │ (MCP Tool Contracts)
     ┌──────────────────────────────▼──────────────────────────────┐
     │                      THE MACHINE LAYER                      │
     │      (Tachyon Ledgers, Photon Money, Electron Cards)        │
     └─────────────────────────────────────────────────────────────┘
```

---

## 6. Quark Domain Catalog

Quark offers a suite of pre-packaged baseline and service-domain packages, each delivering complete Work Models and native Agent Swarms:

| Quark Package | Target Domain | Constituent Hubs | Shipped Agent Swarms | Native & Consumed Fabrics |
|:---|:---|:---|:---|:---|
| **Quark Customer Identity** | Baseline Party Domain | Customer Hub | - KYC Progression Swarm<br>- Profile Verification Swarm | **Customer Record Fabric** (Native SOR)<br>**Trust Fabric** |
| **Quark Deposits** | Deposits Product Domain | Product Hub | - Pricing Elasticity Swarm<br>- Fee & Benefit Modeling Swarm | **Product Fabric** (Native SOR)<br>**Deposit Relationship Fabric** |
| **Quark Credit Card** | Credit Card Product Domain | Product Hub | - Campaign Optimizer Swarm<br>- Pricing Elasticity Swarm | **Product Fabric** (Native SOR)<br>**Card Relationship Fabric** |
| **Quark Lending** | Lending Product Domain | Product Hub | - Pricing Elasticity Swarm<br>- Benefit Modeling Swarm | **Product Fabric** (Native SOR)<br>**Credit Relationship Fabric** |
| **Quark Payments** | Money Movement Service Domain | - Payments Operations Hub<br>- Payments Systems Hub | - Payment Reconciliation Swarm<br>- Incident Response Swarm | **Transfers Fabric** (Zeta Component)<br>**Accounting Fabric** |
| **Quark Disputes** | Dispute Resolution Service Domain | - Disputes Operations Hub<br>- Disputes Systems Hub | - Dispute Investigation Swarm<br>- Tool Contract Auditor Swarm | **Disputes Fabric** (Zeta Component)<br>**Accounting Fabric** |

---

## 7. The Quark Differentiator

The other product families (Tachyon, Photon, Electron, Neutrino) deliver **what the bank can do** — process ledgers, move money, authorize card transactions, and host client interfaces. 

**Quark delivers how the bank operates.** 

This is the distinction between software capability and operational excellence. A bank with Tachyon has a fast credit card ledger. A bank with Quark Credit Card has an **active credit card commercial operation** — packaged with a model-driven Work Architecture, native Product Hubs, and a digital workforce of Agent Swarms ready to collaborate with human operators from day one.
