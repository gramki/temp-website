# Chapter 03.04.04: Neutrino — Retail Transformation Substrate

**The experience, relationship, and distribution substrate for retail banking innovation — providing the interaction surfaces, relationship models, and distribution networks through which customers, agents, and banks collaborate.**

---

## Product Family

Neutrino is Zeta's retail transformation substrate. Rather than serving as a passive set of front-end channels, Neutrino is the active experience, relationship, and distribution engine for retail banking innovation. It provides the infrastructure for building, composing, and operating the interaction surfaces and relationship boundaries through which banking work is accessed — by customers, bank staff, and AI agents.

In Hub Way terms, Neutrino delivers **Channels** — the collaboration surfaces through which humans and agents participate in a Hub's Scenarios — and **Channel Products** — organization-scoped experiences that recompose components from multiple Hubs into cohesive customer journeys.

### Product Lines

| Product Line | Domain | Description |
|---|---|---|
| **Neutrino Consumer Experiences** | Customer-facing channels | High-fidelity interfaces for retail, commercial, and wealth clients. This encompasses traditional visual channels (web portals, mobile apps) and **Agent-Native Channel Products** (such as bank-provided proactive conversational copilots and **Bring-Your-Own-Agent (BYOA)** integration plugins for external agents like Apple Intelligence, ChatGPT, or corporate treasury LLMs). |
| **Neutrino Agent Experiences** | Bank staff and operational channels | Specialized consoles and workspaces for bank operations, support representatives, relationship managers, risk analysts, and supervisors (such as the Agent Desk, Concierge CRM, and Supervisor Console). |

---

## Operational Reliance on Infrastructure Fabrics

Neutrino has a deep, heavy operational reliance on two domain-neutral **Infra Fabrics** to power closed-loop experiences, continuous optimization, and attribution:

| Infra Fabric | Operational Role and Reliance |
|---|---|
| **Engagement Fabric** | Neutrino relies on Engagement Fabric to deliver **Interaction Units (IUs)** — the atomic, stateful UI components rendered across channels. It provides real-time delivery telemetry, read receipts, and closed-loop **AppsFlyer** action/attribution tracking to measure engagement and attribute acquisition channels. |
| **Experimentation Fabric** | Neutrino uses Experimentation Fabric to run multivariate **A/B testing**, manage feature flags, and perform metric-driven hypothesis validation. This allows banks to test new channel layouts, onboarding flows, and relationship nudges in real-time with zero-downtime rollbacks. |

---

## Native Experience & Distribution Fabrics

Neutrino orchestrates and is natively aligned with **eight experience and distribution fabrics** (Banking Fabrics) that manage the customer relationship, household structures, and distribution channels:

| Fabric | Role in the Substrate |
|---|---|
| **Deposit Relationship Fabric** | Governs the deposit relationship context, interest-bearing relationship tiers, and deposit-specific servicing rules. |
| **Credit Relationship Fabric** | Governs the credit relationship context, consolidated credit exposure views, and repayment relationship parameters. |
| **Card Relationship Fabric** | Governs the card relationship context, cardholder preferences, and consolidated multi-card relationship views. |
| **Concierge Fabric** | Governs the relationship manager (RM) CRM, task ledger, and operational interaction logs. |
| **Family Fabric (FFOS)** | Governs the Family Financial Operating System (FFOS), family graph, shared wallets, and delegated permissions. |
| **Sourcing Fabric** | Governs lead management, prospecting, partner integrations, and top-of-funnel origination channels. |
| **Influence Fabric** | Governs the campaign, incentives, and loyalty ledger, tracking reward points, cashbacks, and voucher lifecycles. |
| **BaaS Fabric** | Governs embedded distribution, exposing banking capabilities to third-party platforms and fintech partners. |

---

## Specialized Hubs Orchestrated under Neutrino

Neutrino manages and orchestrates several specialized, bounded operational domains (Hubs) that coordinate people, AI agents, technical systems, and communication channels:

### 1. Channel Product Hub
Orchestrates the delivery, composition, and lifecycle of channel products. It defines how visual components and Interaction Units (IUs) are assembled into unified applications (e.g., mobile banking, web portals, and agent consoles) and manages channel-specific configurations.

### 2. Relationship Hub (per product domain)
Coordinates active relationship contexts, servicing, and lifecycle engagement. It acts as the servicing engine that draws on the respective Relationship Fabrics (Deposit, Credit, Cards) to provide context-aware servicing, relationship-tier benefits, and proactive customer engagement.

### 3. Family Hub (FFOS)
Governs household-level banking operations. Natively powered by the Family Fabric, it manages the family graph, shared financial goals, pocket-money delegation, and parental controls, enabling a comprehensive Family Financial Operating System (FFOS).

### 4. Distribution Hub (per product domain)
Manages customer acquisition, prospecting, and onboarding journeys. Native to Neutrino's acquisition framework, it coordinates lead ingestion, referral campaigns, and application processing, drawing on the Sourcing Fabric to convert prospects into active customers.

---

## Relationship to Other Product Families

| Family | Relationship |
|---|---|
| **Tachyon** | Neutrino provides customer-facing experiences for account products — account opening, balance inquiries, statement access, limit management. |
| **Photon** | Neutrino provides payment initiation and tracking surfaces — mobile payments, transfer interfaces, payment status. |
| **Electron** | Neutrino provides cardholder and administrator experiences for commercial card programs — expense submission, approval workflows, reporting. |
| **Quark** | Neutrino channels are configured per Quark domain Hub — each Hub determines which channels are available for its Scenarios, and Neutrino Channel Products compose cross-hub experiences. |

---

## References

- [Engagement Fabric](../../01-infra-fabrics/09-engagement-fabric.md) — Multi-channel interaction infrastructure
- [Experimentation Fabric](../../01-infra-fabrics/11-experimentation-fabric.md) — Multivariate testing and feature flagging
- [Deposit Relationship Fabric](../02-banking-fabrics/37-deposit-relationship-fabric.md) — Deposit relationship context and servicing
- [Credit Relationship Fabric](../02-banking-fabrics/38-credit-relationship-fabric.md) — Credit relationship context and exposure
- [Card Relationship Fabric](../02-banking-fabrics/39-card-relationship-fabric.md) — Card relationship context and cardholder preferences
- [Concierge Fabric](../02-banking-fabrics/40-concierge-fabric.md) — RM CRM and task ledger
- [Family Fabric](../02-banking-fabrics/41-family-fabric.md) — Family Financial Operating System (FFOS)
- [Sourcing Fabric](../02-banking-fabrics/35-sourcing-fabric.md) — Lead management and origination
- [Influence Fabric](../02-banking-fabrics/36-influence-fabric.md) — Loyalty and incentivization SOR
- [BaaS Fabric](../02-banking-fabrics/34-baas-fabric.md) — Embedded banking and distribution
