# Business Domain Actor: Business System Actor

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

A **Business System Actor** is an automated system, application, or machine in the tenant's ecosystem whose events and integrations trigger Requests in Hub. Business System Actors are a type of **Business Domain Actor** — non-human entities that generate signals leading to Requests.

| Attribute | Value |
|-----------|-------|
| **Category** | Business Domain Actor |
| **Request Type** | System Request |
| **Interaction** | Via events, APIs, file transfers, scheduled jobs |

---

## What Are Business System Actors?

Business System Actors are non-human **Business Domain Actors** that generate signals:

| Category | Examples |
|----------|----------|
| **Core Systems** | Core Banking, Policy Admin, ERP, CRM |
| **Detection Systems** | Fraud Detection, AML Monitoring, Risk Engines |
| **Integration Points** | Payment Networks, Card Networks, Exchanges |
| **Monitoring Systems** | Transaction Monitors, Exception Detectors |
| **Scheduled Jobs** | EOD Processing, Reconciliation, Batch Jobs |

---

## How They Generate Requests

Business System Actors trigger System Requests through various signal providers:

| Signal Provider | Pattern | Examples |
|-----------------|---------|----------|
| **Atropos** | Event-driven | Transaction posted, Alert raised, State changed |
| **Cronus** | Exception/Observation | Threshold breached, Anomaly detected |
| **Dia** | File-based | Batch file received, Report generated |
| **Kale** | Scheduled | Daily reconciliation, Periodic check |
| **Heracles** | API call | External system webhook, Integration request |

---

## Request Flow

```
System Event ──→ Signal Provider ──→ Trigger ──→ System Request ──→ Processing
                                                       │
                                                       ▼
                                                [Automated Processing]
                                                       │
                                                       ▼
                                          [Tasks if human review needed]
```

---

## Common Patterns

### Pattern 1: Detection and Response

```
Fraud System ──→ "Suspicious Transaction" Event ──→ Fraud Review Request
                                                            │
                                                            ▼
                                                   [Seer Case Automation]
                                                            │
                                                            ▼
                                                   [Analyst Task if needed]
```

### Pattern 2: Batch Processing

```
Kale (Scheduler) ──→ "EOD Trigger" ──→ Settlement Processing Request
                                                │
                                                ▼
                                       [Perseus Batch Application]
                                                │
                                                ▼
                                       [Exception Tasks for failures]
```

### Pattern 3: Integration Event

```
Card Network ──→ "Chargeback Received" ──→ Dispute Processing Request
                                                   │
                                                   ▼
                                          [Workflow Application]
                                                   │
                                                   ▼
                                          [Agent Tasks for resolution]
```

---

## Machine Identity

Business System Actors are identified and authenticated via:

| Mechanism | Description |
|-----------|-------------|
| **SPIFFE/SPIRE** | Workload identity for services |
| **API Keys** | For external integrations |
| **Certificates** | mTLS for secure communication |
| **Machine Registry** | Registered machines with defined capabilities |

---

## Hub Capabilities Consumed

Business Systems interact with Hub programmatically through APIs and events — no console access.

### I/O Gateway Access

| Gateway | Usage |
|---------|-------|
| **Atropos** | Publish events that trigger requests |
| **Heracles** | Call APIs to initiate requests, receive callbacks |
| **Dia** | Drop files for batch processing |
| **Cronus** | Publish exceptions and observations |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Signal Exchange** | Send signals, receive responses |
| **Request Management** | Query request status (via API) |
| **Tool Registry** | Registered as machines/tools for invocation |

### What They Produce

| Output | Stored In |
|--------|-----------|
| Signals (Events, Exceptions) | Routed to Signal Exchange |
| Requests (all types) | Operations Data |
| Status Updates | Request updates |

## Relationship to Hub

| Aspect | Description |
|--------|-------------|
| **No UI Interaction** | Systems don't use Hub consoles |
| **Signal Providers** | Interact via I/O Gateways |
| **Tools** | May be invoked as Tools by Hub Applications |
| **Machines** | Registered in Machine Registry |

---

## Request Types Originated

Business Systems can originate **all three request types**:

| Request Type | When Used | Examples |
|--------------|-----------|----------|
| **Service Request** | Acting on behalf of a customer | Customer API submission, automated customer notification |
| **Business Request** | Business operations triggered by system | Automated compliance check, scheduled review |
| **System Request** | System/data integrity issues requiring business resolution | Reconciliation failure, data integrity violation |

### System Requests — Special Characteristics

System Requests are for issues that **require business domain agents to resolve**, not SRE or technical operations:

| Characteristic | Description |
|----------------|-------------|
| **Business Resolution Required** | Cannot be resolved by technical operations alone |
| **Data/Integrity Issues** | Reconciliation failures, consistency violations, out-of-order updates |
| **Entity-Centric** | Often relate to a business entity (transaction, account, record) |
| **Subject Optional** | May or may not have a human subject |

**Examples:**
- Reconciliation mismatch between core banking and card network
- Data integrity failure requiring business decision on which record is authoritative
- Out-of-order updates causing consistency violation that needs business judgment

---

## Key Journeys

- [Request Lifecycle](../../journeys/request-lifecycle.md) — As request originator

---

## Related Documentation

- [Request Types](../../../01-concepts/ontology-1-perception-layer.md)
- [Signal Providers](../../../04-subsystems/signal-providers/README.md)
- [Machine Registry](../../../04-subsystems/registry-services/machine-registry.md)
- [Cipher IAM](../../../04-subsystems/supporting-systems/cipher-iam.md)

---

*TODO: Integration patterns, event schemas, machine registration workflows*

