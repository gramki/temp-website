# Persona: Auditor

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Auditor** reviews operational compliance across the organization — investigating decisions, verifying evidence, and ensuring adherence to policies and regulations.

| Attribute | Value |
|-----------|-------|
| **Category** | Hub Persona — Tenant Administration |
| **Scope** | Tenant Subscription |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | CAF Investigation Console |

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Review Compliance** | Verify operations meet policy requirements |
| **Investigate Decisions** | Examine decision records and evidence |
| **Identify Patterns** | Detect anomalies and systemic issues |
| **Generate Reports** | Produce compliance and audit reports |

---

## Key Activities

### Investigation

1. **Decision Review**
   - Query decision records via CAF
   - Examine evidence bundles
   - Request explanations

2. **Pattern Analysis**
   - Analyze decision patterns across time
   - Identify anomalies
   - Detect bias or drift

3. **Compliance Verification**
   - Verify SOP adherence
   - Check evidence completeness
   - Validate decision authority

### Reporting

1. **Audit Reports**
   - Compliance status
   - Exception findings
   - Recommendations

2. **Regulatory Response**
   - Evidence extraction
   - Decision lineage
   - Explanation generation

---

## Hub Capabilities Consumed

### CAF Console (Primary Interface)

| Capability | What It Provides |
|------------|------------------|
| **Decision Catalog** | Query decisions by criteria, time, agent, scenario |
| **Evidence Browser** | Access evidence bundles, supporting documents |
| **Explanation Service** | Generate human-readable decision explanations |
| **Lineage Tracking** | Trace decision dependencies, input→output |
| **Compliance Dashboard** | Policy adherence, exception reports |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Cognitive Audit Fabric** | Decision catalog, schemas, policies, explanations |
| **Memory Services** | Access Enterprise Memory (decision records, evidence) |
| **Request Management** | View request history, task records |
| **Operations Data** | Query operational records for investigation |
| **Knowledge Services** | Reference SOPs, policies for compliance check |

### What They Query

| Data | Purpose |
|------|---------|
| **Decision Records** | What was decided, by whom, when |
| **Evidence Bundles** | Supporting context for decisions |
| **Request History** | Full lifecycle of requests |
| **Task Records** | Who did what, when |
| **Memory Context** | What context was available at decision time |

---

## Key Journeys

- [Audit Investigation](../journeys/audit-investigation.md) — Primary journey

---

## Related Documentation

- [Cognitive Audit Fabric](../../04-subsystems/cognitive-audit-fabric/README.md)
- [Memory Services](../../04-subsystems/memory-services/README.md)
- [Enterprise Memory](../../04-subsystems/memory-services/enterprise-memory/README.md)

---

*TODO: Detailed investigation workflows, query patterns, report templates*

