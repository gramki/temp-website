# Cronus - Business Exception & Observation Gateway

Cronus is the I/O Gateway for **Business Exceptions and Observations**—higher-order business operation anomalies or concerns that originating systems want to draw attention to. Cronus operates at the business domain level, not system infrastructure level.

> **Key Distinction:** Cronus handles business-level signals (e.g., "Failed clearance record", "Transaction requires manual review"), not system-level monitoring (metrics, logs, traces). Watch may integrate with Cronus to map system operations entities (Alerts, Metrics, Logs) to Business Observations and Exceptions as needed.

## Overview

| Attribute | Value |
|-----------|-------|
| **Signal Type** | Business Exceptions, Business Observations |
| **Protocol** | Publisher API (Push-based) |
| **Direction** | Inbound from Domain Machines |
| **Role** | Receives business anomalies, routes to Workbenches, creates Requests |

## What is a Business Exception?

From the Cronus Architecture specification:

> *"Any business use case that may have been impacted without a recourse to a customer (whether a bank or end user), should be considered as a business exception, that someone needs to pay attention to. If the situation is impacting business and someone has to make a decision to make progress, then the impacted business use case is a business exception."*

**Key Principle:** Exception definition should be based on **consequence to a customer**, not on why or how it originated.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Business Exception** | An anomaly impacting a business use case that requires human attention and decision |
| **Business Observation** | Information that may be of operational interest but doesn't yet require action |
| **Exception Definition** | Registered exception type with schema, SOP, and optional Request Definition |
| **Exception Instance** | A specific occurrence of a registered exception type |
| **Workbench** | Category of exceptions based on special skills required to handle them |
| **SOP** | Standard Operating Procedure for handling an exception type |
| **Request Definition (RD)** | Optional automation to create a Request when exception is published |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    PUBLISHER APPLICATIONS               │
│     (Athens, Aura, Rewards, Acropolis, Emerald, etc.)  │
└────────────────────────┬────────────────────────────────┘
                         │ Business Exception Instances
                         ▼
┌─────────────────────────────────────────────────────────┐
│                       CRONUS                             │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │           EXCEPTION REGISTRY                     │    │
│  │   (Exception Definitions, SOPs, RD mappings)    │    │
│  └─────────────────────────┬───────────────────────┘    │
│                            │                             │
│  ┌─────────────┐  ┌────────┴────────┐  ┌─────────────┐  │
│  │ Exception   │  │ Request Mgmt    │  │ Exception   │  │
│  │ Receiver    │→ │ Service         │→ │ Monitor     │  │
│  └─────────────┘  └─────────────────┘  └─────────────┘  │
│                                                          │
└────────────────────────┬────────────────────────────────┘
                         │ Requests (via RD)
                         ▼
                   OPS CENTER (Workbenches)
```

## Exception Definition Schema

Publishers register exception types in the Exception Registry:

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `name` | Yes | Canonical name | `in.zeta.athena.clearance_exceptions` |
| `display_name` | Yes | Display name in Ops Center | "Failed clearance record" |
| `description` | Yes | Details about the exception | - |
| `exception_publisher` | Yes | Publishing system/app | Athens, Aura, Acropolis |
| `exception_definition_code` | Yes | Unique code (Zeta naming) | `AHXZZZZ1232` |
| `SOP_file_location` | Yes | .md file for resolution process | - |
| `request_definition_code` | Yes | RD code for auto-Request creation | `RD00123123` |
| `workbench_id` | Yes | Target Workbench for viewing | - |
| `criticality` | Yes | Priority tier | Tier-1, Tier-2, Tier-3 |
| `labels` | No | Enhanced filtering | Rewards, Prepaid, Credit |
| `exception_specific_info` | Yes | Mandatory attributes schema | JSON attr list |

### Exception Definition Code Convention

| Code | Meaning |
|------|---------|
| `LDXZZZZ0002` | Ledger Exception (LDX), system-provided (ZZZZ), sequence 0002 |
| `AHXZZZZ0001` | Account Holder Exception |
| `RWXZZZZ0007` | Reward Exception |
| `CDXZZZZ0005` | Card Exception |

## Exception Instance Schema

Published by client applications:

| Field | Type | Description |
|-------|------|-------------|
| `tenant_id` | long | Tenant identifier |
| `exception_definition_code` | string | Registered exception type code |
| `reported_time_in_millis` | long | Epoch time (UTC) |
| `exception_id` | long | Unique instance identifier |
| `exception_specific_info` | JSON | Information required for RD instance |

Enriched by Cronus/Ops Center:

| Field | Type | Description |
|-------|------|-------------|
| `status` | enum | Open, Closed, etc. (starts as Open) |
| `closed_by` | string | Auth profile ID who closed |
| `closed_at_in_millis` | long | Closure timestamp |
| `closure_remarks` | string | Resolution notes |

## Key Functional Requirements

1. **Exception Registration**: Publishers define exception types with SOP and schema
2. **Exception Publishing**: Publishers publish instances of registered types
3. **Workbench Routing**: Each exception belongs to exactly one Workbench
4. **Exception Monitor**: Biz Ops agents view exceptions in Ops Center
5. **Auto-Request Creation**: RD instance created automatically if defined
6. **SOP Access**: Biz Ops users access SOP from within Ops Center
7. **Retrospective Requests**: Create RD instance for exception after the fact
8. **Filtering**: Date range, exception type, criticality, status filters

## Non-Functional Requirements

| Requirement | Target |
|-------------|--------|
| **Visibility Latency** | < 2 minutes from publish to Exception Monitor |
| **API Throughput** | 100 RPS for filtering APIs |
| **API Latency** | 300ms for common filtering queries |
| **Retention (Closed)** | 30 days (configurable per tenant) |
| **Retention (Open)** | Forever until closed |
| **Volume** | ~1 exception per 100 accounts per day |

## Integration with Watch (Optional)

Watch may integrate with Cronus to transform system-level signals into business-level signals:

| Watch Signal | Cronus Signal |
|--------------|---------------|
| System Alert (SLA breach) | Business Exception (Customer SLA impact) |
| Metric threshold crossed | Business Observation (Capacity concern) |
| Error rate spike | Business Exception (Service degradation) |

This mapping is configured in Workbench Triggers, not in Cronus itself. Cronus remains agnostic to signal origin—it processes whatever Business Exceptions and Observations publishers send.

## Early Adopters

| Publisher | Use Case |
|-----------|----------|
| **Aon/Emerald** | Merchant EMI Exceptions |
| **Aura** | Transaction Failures |
| **Athens** | Clearance File Exceptions |

## Data Store

- **Technology**: PostgreSQL
- **Partitioning**: By `workbench_id`
- **Primary Key**: `exception_id`
- **Indexing**: Composite on `reported_time_in_millis`, `status`, `criticality`
- **Schema Isolation**: Separate schema per tenant for auth/access control

## Related Documentation

- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Hub Architecture - Triggers](../../02-system-design/hub-architecture.md#14-triggers)
- [Ontology - Signal](../../01-concepts/ontology-reference.md#signal)
- [Ontology - Exception](../../01-concepts/ontology-reference.md#signal)

---

*Status: 🟡 WIP - Based on Cronus Architecture PRD*
*TBD: Clean up the document to the right level of abstraction for Hub story; Convert any Tachyon-specific references to examples*