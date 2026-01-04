# Business Domain Actor: Business Employee

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Business Employee** is an internal employee of the tenant organization whose business activities trigger **Service Requests** (when assisting customers) or **Business Requests** (for internal operations) in Hub. They may or may not also be Hub Agents.

| Attribute | Value |
|-----------|-------|
| **Category** | Business Domain Actor |
| **Request Type** | Business Request |
| **Interaction** | Via internal systems, Hub interfaces, or integrated applications |

---

## Who Are Business Employees?

Business Employees perform internal operations that may trigger Hub requests:

| Role | Examples of Triggering Actions |
|------|-------------------------------|
| **Relationship Manager** | Initiates customer onboarding, requests account review |
| **Compliance Officer** | Triggers regulatory review, requests audit |
| **Operations Manager** | Initiates process improvement, requests report |
| **Risk Analyst** | Escalates risk finding, requests investigation |
| **Finance Controller** | Initiates reconciliation, requests exception handling |

---

## Hub Capabilities Consumed

Business Employees may use Hub directly (if also an Agent) or through integrated applications.

### When Also an Agent (Ops Center Access)

| Capability | What It Provides |
|------------|------------------|
| **Request Initiation** | Start Service or Business Requests |
| **Entity Views** | View business entity details |
| **Task Processing** | Work assigned tasks (as Agent) |
| **Knowledge Access** | Query SOPs, policies |

### When Using Integrated Applications

| Capability | What It Provides |
|------------|------------------|
| **Request Initiation** | Start requests via integrated systems |
| **Status Tracking** | View request status in source system |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Heracles** | API for request initiation |
| **Request Management** | Create requests, view status |
| **Atropos** | Event-driven request initiation |
| **Dia** | Document-based request initiation |
| **Memory Services** | User Memory for preferences |

## How They Generate Requests

Business Employees trigger requests through:

| Channel | Example | Signal Provider |
|---------|---------|-----------------|
| **Hub Ops Center** | Manually initiate a request | Heracles |
| **Internal Portal** | Submit business request form | Heracles |
| **Email** | Forward document for processing | Dia |
| **Integrated Application** | Trigger from CRM/ERP | Atropos |

---

## Request Flow

```
Employee Action ──→ Signal ──→ Trigger ──→ Business Request ──→ Processing
       │                                          │
       │                                          ▼
       │                                   [Tasks Created]
       │                                          │
       └──── May also work tasks ─────────────────┘
            (if also an Agent)
```

---

## Dual Role: Business Employee + Agent

Many Business Employees are **also** Hub Agents:

| As Business Employee | As Agent |
|---------------------|----------|
| Triggers requests based on business judgment | Processes tasks in their queue |
| Decides *when* something needs to happen | Executes *how* it gets done |
| Owns the business outcome | Completes assigned work |

### Example: Relationship Manager

```
┌──────────────────────────────────────────────────────────────┐
│                     Relationship Manager                      │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  As Business Employee:                                        │
│  • Meets with customer, identifies need                       │
│  • Decides to initiate onboarding                             │
│  • Triggers "Customer Onboarding" request                     │
│                                                               │
│  As Agent:                                                    │
│  • Receives "Collect Documents" task                          │
│  • Completes KYC verification task                            │
│  • Reviews and approves application                           │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## Request Types Originated

Business Employees can originate **Service Requests** and **Business Requests**:

| Request Type | When Used | Examples |
|--------------|-----------|----------|
| **Service Request** | Assisting a customer (assisted channel) | Filing dispute on behalf of customer, processing customer call |
| **Business Request** | Internal business operations | Onboarding initiation, compliance review, exception handling |

### Common Scenarios

| Category | Request Type | Examples |
|----------|--------------|----------|
| **Customer-Assisted** | Service Request | Dispute filed via phone, account change via branch |
| **Customer-Related Ops** | Business Request | Relationship review, account health check |
| **Operational** | Business Request | Exception handling, reconciliation, corrections |
| **Compliance** | Business Request | Regulatory filings, audit requests, investigations |
| **Administrative** | Business Request | Report requests, approvals, escalations |

---

### What They Produce

| Output | Stored In |
|--------|-----------|
| Service/Business Requests | Operations Data |
| Documents | Application Data / Knowledge Bank |
| User Preferences | User Memory |

---

## Relationship to Hub Personas

| Relationship | Description |
|--------------|-------------|
| **Agent** | May also be an Agent (dual role) |
| **Supervisor** | May be supervised as Agent, or be a Supervisor themselves |
| **Process Architect** | Follows Scenarios designed by Process Architects |

---

## Key Journeys

- [Request Lifecycle](../../journeys/request-lifecycle.md) — As request originator

---

## Related Documentation

- [Request Types](../../../01-concepts/ontology-1-perception-layer.md)
- [Agent Persona](../agent.md) — When also operating as Agent
- [Manual Task Application](../../../04-subsystems/hub-native-utilities/manual-task-application.md)

---

*TODO: Common patterns, integration scenarios, dual-role workflows*

