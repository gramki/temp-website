# Workbench Setup Guide

> **Audience:** Process Architects  
> **Prerequisites:** Tenant subscription configured, Process Architect role assigned

This guide walks through creating and configuring a Workbench for a business domain in Olympus Hub.

---

## Overview

A **Workbench** is the core abstraction for a business domain. Setting up a workbench involves:

1. [Planning Your Workbench](#1-planning-your-workbench)
2. [Creating the Workbench](#2-creating-the-workbench)
3. [Defining Scenarios](#3-defining-scenarios)
4. [Configuring Triggers](#4-configuring-triggers)
5. [Setting Up Knowledge Base](#5-setting-up-knowledge-base)
6. [Configuring Memory Stores](#6-configuring-memory-stores)
7. [Provisioning Application Data Stores](#7-provisioning-application-data-stores)
8. [Enrolling Agent Groups](#8-enrolling-agent-groups)
9. [Setting Up Task Queues](#9-setting-up-task-queues)
10. [Defining Request Policies](#10-defining-request-policies)
11. [Publishing the Workbench](#11-publishing-the-workbench)

---

## 1. Planning Your Workbench

Before creating a workbench, answer these questions:

### Domain Scope

| Question | Example Answer |
|----------|----------------|
| What business domain does this cover? | Dispute Resolution |
| What operations will be managed here? | Chargebacks, Fraud cases, Customer complaints |
| Who are the stakeholders? | Dispute agents, Supervisors, Compliance team |

### Scenario Identification

List the scenarios (situational contexts) this workbench will handle:

| Scenario | Trigger Source | Automation Type |
|----------|----------------|-----------------|
| Chargeback Resolution | Event: `payment.disputed` | Seer Case Agent |
| Fraud Investigation | API: POST `/fraud-reports` | Durable Workflow |
| Customer Complaint | Event: `customer.complaint` | Workflow |
| Daily Reconciliation | Schedule: Daily 2 AM | Batch Processing |

### Integration Mapping

Identify external systems and data sources:

| System | Purpose | Integration Type |
|--------|---------|------------------|
| Core Banking | Transaction lookup | REST API |
| Card Network | Dispute filing | SOAP API |
| CRM | Customer info | REST API |
| Document Store | Evidence files | Dia (Files) |

---

## 2. Creating the Workbench

### Access Workbench Studio

```
Hub Console → Workbench Studio → Create Workbench
```

### Basic Configuration

```yaml
Workbench:
  Name: Dispute Operations
  ID: dispute-ops  # Auto-generated or custom
  Domain: dispute-resolution
  Description: >
    Manages all dispute-related operations including chargebacks,
    fraud investigations, and customer complaints.
  
  Owner: [Process Architect email]
  Environment: Development  # Start in dev
```

### Environment Assignment

| Environment | Purpose |
|-------------|---------|
| **Development** | Building and testing |
| **Staging** | Pre-production validation |
| **Production** | Live operations |

```
Workbench Studio → [Workbench] → Environments
├── Development: Enabled (default)
├── Staging: Enabled
└── Production: Enabled (requires approval)
```

---

## 3. Defining Scenarios

### Create Scenarios

For each identified scenario:

```
Workbench Studio → [Workbench] → Scenarios → Create
```

#### Example: Chargeback Resolution

```yaml
Scenario:
  ID: chargeback-resolution
  Name: Chargeback Resolution
  Description: Handle disputed transactions from card networks
  
  # Automation
  Automation Runtime: Olympus Seer
  Application Type: Seer Case Orchestration Agent
  Application ID: [Created by Developer]
  
  # Request Type
  Request Type: Business Request
  Subject Type: Customer
  Object Type: Transaction
  
  # SOP Links
  SOPs:
    - chargeback-handling-sop
    - evidence-collection-sop
    - escalation-procedures
  
  # Roles Involved
  Roles:
    - Dispute Agent
    - Senior Agent
    - Compliance Officer
```

#### Example: Daily Reconciliation

```yaml
Scenario:
  ID: daily-reconciliation
  Name: Daily Reconciliation
  Description: Reconcile dispute status with card networks
  
  # Automation
  Automation Runtime: Perseus
  Application Type: Batch Application
  Application ID: [Created by Developer]
  
  # Request Type
  Request Type: System Request
  
  # No subject/object for system requests
```

### Scenario to Automation Runtime Mapping

| Scenario Type | Recommended Runtime | Application Type |
|--------------|---------------------|------------------|
| Complex cases requiring judgment | Olympus Seer | Seer Case Agent |
| Long-running with human tasks | ChronoShift | Durable Workflow |
| Structured process flows | Rhea | Workflow Application |
| Batch/file processing | Perseus | Batch Application |
| Stateless decisions | Atlantis | Procedure Application |

---

## 4. Configuring Triggers

### Create Triggers

For each scenario, define how signals activate it:

```
Workbench Studio → [Workbench] → Triggers → Create
```

#### Event Trigger Example

```yaml
Trigger:
  ID: payment-disputed-trigger
  Name: Payment Disputed Event
  
  # Signal Source
  Source: Atropos
  Topic: payment.events
  
  # Conditions
  Conditions:
    - field: event_type
      operator: equals
      value: "DISPUTED"
    - field: amount
      operator: greater_than
      value: 0
  
  # Transformation
  Transform:
    request.subject_id: "$.customer_id"
    request.object_id: "$.transaction_id"
    request.payload.amount: "$.disputed_amount"
    request.payload.reason: "$.dispute_reason"
  
  # Target
  Scenario: chargeback-resolution
  
  # Correlation (for updates to existing requests)
  Correlation:
    field: "$.transaction_id"
    strategy: UPDATE_OR_CREATE
```

#### API Trigger Example

```yaml
Trigger:
  ID: fraud-report-api-trigger
  Name: Fraud Report API
  
  # Signal Source
  Source: Heracles
  Endpoint: POST /api/v1/fraud-reports
  
  # Validation
  Schema: fraud-report-schema.json
  
  # Transform
  Transform:
    request.subject_id: "$.reporter_id"
    request.object_id: "$.transaction_id"
    request.payload: "$"
  
  # Target
  Scenario: fraud-investigation
```

#### Schedule Trigger Example

```yaml
Trigger:
  ID: daily-recon-schedule
  Name: Daily Reconciliation Schedule
  
  # Signal Source
  Source: Kale
  Schedule: "0 2 * * *"  # Daily at 2 AM
  Timezone: UTC
  
  # Payload
  Payload:
    type: "DAILY_RECONCILIATION"
    date: "${yesterday}"
  
  # Target
  Scenario: daily-reconciliation
```

---

## 5. Setting Up Knowledge Base

### Create Knowledge Collections

```
Workbench Studio → [Workbench] → Knowledge → Create Collection
```

#### Policy Documents

```yaml
Collection:
  Name: Dispute Policies
  Type: Policy Documents
  
  Sources:
    - Type: Document Upload
      Path: /policies/dispute/*.pdf
    - Type: URL Crawl
      URL: https://docs.company.com/dispute-policies/
  
  Ingestion:
    Schedule: Weekly
    Chunking: Semantic
    Embedding: OpenAI Ada
```

#### SOPs

```yaml
Collection:
  Name: Standard Operating Procedures
  Type: SOP Documents
  
  Sources:
    - Type: Document Upload
      Path: /sops/dispute/*.md
  
  Ingestion:
    Schedule: On Change
    Chunking: Section-based
    Embedding: OpenAI Ada
```

#### Reference Materials

```yaml
Collection:
  Name: Card Network Regulations
  Type: Reference
  
  Sources:
    - Type: External API
      Endpoint: https://regulations.visa.com/api/
    - Type: Document Upload
      Path: /regulations/*.pdf
  
  Ingestion:
    Schedule: Monthly
    Chunking: Semantic
    Embedding: OpenAI Ada
```

### Configure Access

```
Workbench Studio → [Workbench] → Knowledge → Access
├── This Workbench: Full Access
├── Other Workbenches: [Select which can read]
└── Cross-Tenant: Disabled (default)
```

---

## 6. Configuring Memory Stores

### Enterprise Memory

```
Workbench Studio → [Workbench] → Memory → Enterprise Memory
```

```yaml
Enterprise Memory:
  Enabled: true
  
  Categories:
    - Name: Decisions
      Retention: 7 years
      CAF Governed: true
    
    - Name: Exceptions
      Retention: 3 years
      CAF Governed: true
    
    - Name: Procedural Updates
      Retention: 5 years
      CAF Governed: false
  
  Visibility:
    - Workbench: Payment Operations  # Can access our memories
```

### User Memory

```yaml
User Memory:
  Enabled: true
  
  Categories:
    - Name: Preferences
      Retention: Active + 1 year
    
    - Name: Interaction History
      Retention: 90 days
  
  Visibility:
    - Workbench: Customer Service  # Can access our user memories
```

### Agent Memory

```yaml
Agent Memory:
  Enabled: true  # Automatic per-session
  
  Session Scope: Request
  Private Memory: Enabled  # Per-agent within session
```

---

## 7. Provisioning Application Data Stores

> **Note:** Application Data Stores are for Hub Application-specific business entities, not operational data.

### When to Use Which Store

| Data Type | Recommended Store |
|-----------|-------------------|
| Business entities with relationships | Ganymede (Relational) |
| Entity state cache, session data | Callisto (Key-Value) |
| Full-text search, analytics | Europa (OpenSearch) |

### Provision Ganymede (if needed)

```
Workbench Studio → [Workbench] → Data Stores → Ganymede → Enable
```

```yaml
Ganymede:
  Enabled: true
  
  DDL:
    Version: 1
    Script: |
      CREATE TABLE transaction_disputes (
        dispute_id UUID PRIMARY KEY,
        transaction_id UUID NOT NULL,
        customer_id UUID NOT NULL,
        status VARCHAR(50) NOT NULL,
        amount DECIMAL(15,2),
        reason VARCHAR(100),
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW()
      );
      
      CREATE INDEX idx_disputes_customer ON transaction_disputes(customer_id);
      CREATE INDEX idx_disputes_status ON transaction_disputes(status);
```

### Provision Callisto (if needed)

```yaml
Callisto:
  Enabled: true
  
  Namespaces:
    - dispute-state-cache
    - session-context
```

### Provision Europa (if needed)

```yaml
Europa:
  Enabled: true
  
  Indices:
    - Name: dispute-search
      Mappings:
        dispute_id: keyword
        customer_name: text
        description: text
        status: keyword
        amount: float
        created_at: date
```

---

## 8. Enrolling Agent Groups

### Create Agent Groups in Cipher

First, create groups in Cipher IAM:

```
Cipher IAM → Groups → Create
├── dispute-agents
├── dispute-supervisors
├── dispute-senior-agents
└── dispute-compliance
```

### Enroll Groups in Workbench

```
Workbench Studio → [Workbench] → Access → Agent Groups → Enroll
```

```yaml
Agent Groups:
  - Group: dispute-agents
    Role: Agent
    Queues: [tier-1-queue, general-queue]
  
  - Group: dispute-senior-agents
    Role: Agent
    Queues: [tier-2-queue, escalation-queue]
  
  - Group: dispute-supervisors
    Role: Supervisor
    Queues: [All]
  
  - Group: dispute-compliance
    Role: Auditor
    Queues: [Read-only access]
```

---

## 9. Setting Up Task Queues

### Create Queues

```
Workbench Studio → [Workbench] → Task Queues → Create
```

```yaml
Queues:
  - Name: Tier 1 Queue
    ID: tier-1-queue
    Description: Standard dispute tasks
    Assignment: Round Robin
    SLA: 4 hours
    Escalation:
      After: 3 hours
      To: tier-2-queue
  
  - Name: Tier 2 Queue
    ID: tier-2-queue
    Description: Complex or escalated disputes
    Assignment: Skill-based
    SLA: 8 hours
    Escalation:
      After: 6 hours
      To: escalation-queue
  
  - Name: Escalation Queue
    ID: escalation-queue
    Description: Supervisor attention required
    Assignment: Manual
    SLA: 24 hours
    Notification: Immediate to supervisors
  
  - Name: Expert Queue
    ID: expert-queue
    Description: Compliance review required
    Assignment: Manual
    SLA: 48 hours
    Access: dispute-compliance group only
```

### Configure Escalation Matrix

```yaml
Escalation Matrix:
  - Condition: SLA breach
    Action: Move to next tier queue
    Notify: Current assignee, Supervisor
  
  - Condition: Customer VIP
    Action: Direct to Tier 2
    Notify: Supervisor
  
  - Condition: Amount > $10,000
    Action: Copy to Expert Queue
    Notify: Compliance team
  
  - Condition: Regulatory flag
    Action: Immediate to Compliance
    Notify: Compliance team, Legal
```

---

## 10. Defining Request Policies

### Lifecycle Policies

```
Workbench Studio → [Workbench] → Policies → Request Lifecycle
```

```yaml
Request Lifecycle:
  States:
    - ACTIVE    # Being processed
    - PENDING   # Waiting for external input
    - COMPLETED # Successfully resolved
    - CANCELLED # Terminated without resolution
  
  Timeouts:
    PENDING: 72 hours  # Auto-cancel if no response
    ACTIVE: 30 days    # Escalate if still active
  
  Completion:
    Require Resolution Code: true
    Require Summary: true
```

### Storage Policies

```yaml
Storage Policy:
  Request Data:
    Retention: 7 years
    Archive After: 1 year
  
  Task Data:
    Retention: 7 years
    Archive After: 6 months
  
  Session Data:
    Retention: 90 days
    Archive After: 30 days
```

### Self-Serve Policy (Optional)

If customers can initiate requests:

```yaml
Self-Serve:
  Enabled: true
  
  Scenarios:
    - chargeback-resolution:
        Allowed: true
        Customer Groups: [all-customers]
        Subject Assignment: true  # Tasks can be assigned to customer
    
    - fraud-investigation:
        Allowed: false  # Internal only
```

---

## 11. Publishing the Workbench

### Validation

Before publishing, validate the workbench:

```
Workbench Studio → [Workbench] → Validate
```

Validation checks:
- ✅ All scenarios have applications assigned
- ✅ All triggers are valid
- ✅ Knowledge base is indexed
- ✅ Agent groups are enrolled
- ✅ Task queues are configured
- ✅ Policies are complete

### Publish to Environment

```
Workbench Studio → [Workbench] → Publish
├── Target Environment: Staging
├── Approval: [Required approvers]
└── Notes: [Release notes]
```

### Workbench States

| State | Description |
|-------|-------------|
| **Draft** | Under development |
| **Validated** | Passed validation |
| **Published** | Approved, ready for deployment |
| **Active** | Live in environment |
| **Archived** | Decommissioned |

### Promote to Production

After staging validation:

```
Workbench Studio → [Workbench] → Promote
├── From: Staging
├── To: Production
├── Approval: [Production approvers]
└── Rollback Plan: [Document]
```

---

## Setup Checklist

```
□ Planning
  □ Domain scope defined
  □ Scenarios identified
  □ Integrations mapped

□ Workbench Creation
  □ Workbench created
  □ Environments assigned

□ Scenarios
  □ All scenarios defined
  □ Automation types selected
  □ SOPs linked

□ Triggers
  □ Event triggers configured
  □ API triggers configured
  □ Schedule triggers configured (if needed)
  □ Correlation rules set

□ Knowledge
  □ Policy documents ingested
  □ SOPs ingested
  □ Reference materials ingested
  □ Access configured

□ Memory
  □ Enterprise Memory configured
  □ User Memory configured (if needed)
  □ Visibility rules set

□ Data Stores (if needed)
  □ Ganymede provisioned with DDL
  □ Callisto namespaces created
  □ Europa indices created

□ Agents
  □ Groups created in Cipher
  □ Groups enrolled in Workbench
  □ Roles assigned

□ Task Queues
  □ Queues created
  □ SLAs configured
  □ Escalation matrix defined

□ Policies
  □ Lifecycle policies set
  □ Storage policies set
  □ Self-serve configured (if applicable)

□ Publishing
  □ Validation passed
  □ Published to Staging
  □ Staging tested
  □ Promoted to Production
```

---

## Next Steps

After workbench setup:

1. **Developer Handoff** — Developers build Hub Applications for each scenario
2. **Supervisor Onboarding** — Supervisors configure queue assignments
3. **Agent Training** — Train agents on the new workbench
4. **Go-Live** — Activate the workbench in production

---

## Troubleshooting

### Common Issues

| Issue | Resolution |
|-------|------------|
| Trigger not firing | Check conditions, verify signal source is connected |
| Knowledge not retrieving | Verify ingestion completed, check embeddings |
| Agents can't see tasks | Check group enrollment, verify queue access |
| Request stuck in PENDING | Check timeout policies, verify external dependencies |

### Getting Help

- **Technical Support:** Contact Zeta support portal
- **Documentation:** Refer to [Workbench Management](../04-subsystems/workbench-management/README.md)

---

## Related Documentation

- [Workbench Management](../04-subsystems/workbench-management/README.md) — Technical reference
- [Signal Exchange](../04-subsystems/signal-exchange/README.md) — Trigger processing
- [Automation Runtimes](../04-subsystems/automation-runtimes/README.md) — Application hosts
- [Tenant Setup Guide](./tenant-setup-guide.md) — Prerequisites

