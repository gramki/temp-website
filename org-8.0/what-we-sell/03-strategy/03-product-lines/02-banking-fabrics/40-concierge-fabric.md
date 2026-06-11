# Chapter 03.02.40: Concierge Fabric — Product Note

**The relationship manager (RM) CRM and task ledger infrastructure — owning RM-to-customer assignments, immutable interaction logs, and operational task tracking for high-touch servicing.**

---

## The Architectural Problem

Traditional Customer Relationship Management (CRM) systems are completely disconnected from the bank's core transactional systems. Relationship Managers (RMs) and customer support agents must navigate a dozen different screens across multiple platforms to view account balances, transaction histories, pending holds, or active loan applications. 

Furthermore, traditional CRMs operate as passive databases rather than active operational systems. They rely on agents to manually log interactions, leading to incomplete records, lost context, and a lack of accountability. There is no secure, audit-compliant way to track RM-assigned tasks, follow-ups, or customer requests directly linked to transactional states. This separation leads to slow resolution times, missed follow-ups, and an inability to enforce Service Level Agreements (SLAs) for high-net-worth or commercial clients who expect seamless, high-touch servicing.

---

## What It Governs

Concierge Fabric is the authoritative domain-specific Banking Fabric for relationship manager assignment, interaction logging, and high-touch servicing task management. It provides the active operational ledger that coordinates how bank staff and AI agents interact with and service customers.

In scope: RM-to-customer assignment records, immutable interaction logging, concierge task ledger management, and servicing SLA tracking. Out of scope: customer-facing messaging channels (Engagement Fabric), core customer identity data (Customer Record Fabric), general ledger accounting (Accounting Fabric), and visual agent workspace layouts (Neutrino Agent Experiences).

---

## Source of Truth

- **Entities owned:** RM-to-customer assignment records, RM interaction logs, RM task ledger, customer servicing preferences, concierge service level agreements (SLAs), operational case links, servicing notes.
- **Key invariants:**
  - Every customer interaction must be immutably logged with timestamp, channel, and agent/RM details.
  - RM tasks must have defined owners, priorities, and deadlines, and be bound to a specific customer profile (Party_ID).
  - Concierge SLAs must be tracked and monitored for breach conditions in real-time.
  - Sensitive servicing notes and interaction logs must be encrypted and access-controlled based on employee roles.
- **Configurable vs. compliance floor:** RM assignment rules, task categories, SLA thresholds, and interaction logging templates are fully configurable. Compliance floor: Immutable logging of customer interactions, secure storage of sensitive servicing notes, and compliance with consumer privacy regulations (e.g., GLBA, GDPR, CCPA).

---

## Scope Highlights

- **RM-Customer Assignment:** Manages the mapping of customers to dedicated relationship managers or specialized servicing teams based on segment, geography, or asset tier.
- **Interaction Logging & History:** Immutably logs all visual, conversational, and agent-led customer interactions to provide a single, continuous history of engagement.
- **Concierge Task Ledger:** Manages RM-assigned tasks, follow-ups, and customer requests, ensuring clear ownership and tracking.
- **SLA Tracking & Escalation:** Monitors servicing response times against defined SLAs and automatically escalates overdue tasks to supervisors.

---

## Capability Domains

### 1. RM-Customer Assignment

The authoritative system for managing the mapping of customers to dedicated relationship managers or servicing teams.

| Capability | What It Delivers |
|---|---|
| Assignment manager | Establishes and maintains the mappings between customers (Party_ID) and their assigned relationship managers (RM_ID) or servicing teams. |
| Segment router | Automatically assigns RMs to customers based on segment rules (e.g., wealth tier, commercial industry, geographic location). |
| Capacity balancer | Monitors RM workloads and balances customer assignments to ensure optimal servicing capacity. |

### 2. Interaction Logging & History

Immutably logs all visual, conversational, and agent-led customer interactions.

| Capability | What It Delivers |
|---|---|
| Interaction logger | Captures and immutably logs details of every customer interaction (timestamp, duration, channel, agent, summary). |
| Servicing notes ledger | Stores encrypted, role-access-controlled servicing notes and customer preferences (e.g., preferred contact times, communication style). |
| Interaction timeline resolver | Exposes high-performance APIs to reconstruct a unified, chronological timeline of all customer interactions across all channels. |

### 3. Concierge Task Ledger

Manages RM-assigned tasks, follow-ups, and customer requests.

| Capability | What It Delivers |
|---|---|
| Task manager | Creates, updates, and tracks the lifecycle (pending, in-progress, completed, overdue) of servicing tasks and customer requests. |
| Task-to-transaction linker | Links servicing tasks directly to transactional entities (e.g., linking a dispute task to a specific transaction in Card Issuer Txn Processing). |
| Follow-up scheduler | Schedules automated follow-up reminders for RMs and coordinates with Engagement Fabric to send automated status updates to customers. |

### 4. SLA Tracking & Escalation

Monitors servicing response times and escalation paths.

| Capability | What It Delivers |
|---|---|
| SLA monitor | Tracks active tasks against defined service level agreements (e.g., resolve wealth tier requests within 2 hours). |
| Escalation engine | Automatically escalates tasks to supervisors or alternative queues when SLA breach thresholds are crossed. |
| Servicing performance analytics | Aggregates SLA performance metrics across RMs and servicing teams to identify operational bottlenecks. |

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| **Customer Record Fabric** | Customer Record owns the core customer identity (Party_ID) and contact details; Concierge Fabric links RMs and tasks to the Party_ID. |
| **Cognitive Audit Fabric** | Cognitive Audit Fabric provides the tamper-proof audit trail for sensitive servicing actions and note access. |
| **Engagement Fabric** | Concierge Fabric coordinates with Engagement Fabric to deliver notifications, follow-up messages, and task status updates to customers. |
| **Branch and Institution Fabric** | Branch and Institution Fabric logs in-branch interactions and handoffs to RMs, which are captured in the Concierge interaction log. |
| **Influence Fabric** | Concierge Fabric queries Influence Fabric for active customer benefits and rewards to assist RMs in relationship-building. |

---

## References

- [Customer Record Fabric](02-customer-record-fabric.md) — Customer master data and identity
- [Branch and Institution Fabric](33-branch-and-institution-fabric.md) — Branch operations and teller functions
- [Engagement Fabric](../../01-infra-fabrics/09-engagement-fabric.md) — Multi-channel interaction infrastructure
- [Cognitive Audit Fabric](../../01-infra-fabrics/08-cognition-fabric.md) — Tamper-proof interaction audit trail
