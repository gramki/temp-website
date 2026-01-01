# Ontology: Normative Layer

**Layer Question:** *"What ought to be done?"*

The Normative Layer defines the **standards, rules, and goals** that shape expected behavior in a given scenario. It is *normative* because it encodes what ought to be done, not just what can be done.

Here we find **roles** (who is responsible), **goals** (what outcomes they must achieve), **responsibilities** (duties), **capabilities and capacities** (what they can do and how much), and **SOPs** (codified best practices). This layer also covers **decisions**, where agents—human or AI—choose a course of action, often aided by information, data, and decision-support tools.

It is the legal and procedural backbone: the framework of obligations and standards against which execution is measured.

---

**Navigation:** [← Perception Layer](./ontology-1-perception-layer.md) | [Ontology Reference](./ontology-reference.md) | [Execution Layer →](./ontology-3-execution-layer.md)

---

## Table of Contents

- [Role](#role)
- [Goal](#goal)
- [SOP (Standard Operating Procedure)](#sop-standard-operating-procedure)
- [Responsibility](#responsibility)
- [Capability](#capability)
- [Capacity](#capacity)
- [Decision](#decision)
- [Information Element](#information-element)
- [Data Element](#data-element)
- [Knowledge Base (KB)](#knowledge-base-kb)
- [Runbook](#runbook)
- [Checklist](#checklist)

---

## Role
**Definition:** A functional responsibility played by an [Agent](./ontology-3-execution-layer.md#agent) in a [Scenario](./ontology-1-perception-layer.md#scenario).  
**Role:** Specifies duties and what Procedures are executed.  
**Relationships:** Has [Goals](#goal); executes [Procedures](./ontology-3-execution-layer.md#procedure); is played by [Agents](./ontology-3-execution-layer.md#agent); composed of [Responsibilities](#responsibility).  
**Example:** "Security Analyst," "Controller," "Reviewer."

**See also:** [Goal](#goal), [Procedure](./ontology-3-execution-layer.md#procedure), [Agent](./ontology-3-execution-layer.md#agent), [Responsibility](#responsibility)

---

## Goal
**Definition:** Desired outcomes associated with a [Role](#role); **defined per role**, not per scenario.  
**Role:** Drive [SOP](#sop-standard-operating-procedure) design and [Operation](./ontology-3-execution-layer.md#operation-abstract) selection.  
**Relationships:** Addressed by [SOPs](#sop-standard-operating-procedure); referenced by [Scenarios](./ontology-1-perception-layer.md#scenario); supported by [Decisions](#decision).  
**Example:** "Maintain safe separation of aircraft," "Protect user accounts from takeover."

**See also:** [SOP](#sop-standard-operating-procedure), [Scenario](./ontology-1-perception-layer.md#scenario)

---

## SOP (Standard Operating Procedure)
**Definition:** Codified guidance to meet [Goals](#goal).  
**Role:** **Governs** [Operations](./ontology-3-execution-layer.md#operation-abstract) (Procedures, Workflows, Cases); provides knowledge for OPD Predict/Decide.  
**Relationships:** Address [Goals](#goal); govern [Operations](./ontology-3-execution-layer.md#operation-abstract).  
**Example:** "Lock account after 3 failed attempts; notify user; require step-up auth."

**See also:** [Operation](./ontology-3-execution-layer.md#operation-abstract), [Procedure](./ontology-3-execution-layer.md#procedure), [Workflow](./ontology-3-execution-layer.md#workflow), [Case](./ontology-3-execution-layer.md#case), [Decision](#decision)

---

## Responsibility
**Definition:** A specific accountability or duty assigned to a [Role](#role). Responsibilities define **what** a role is expected to accomplish, without specifying **how** to accomplish it.  
**Role:** Articulates the "what" a role is accountable for; provides the basis for performance measurement and compliance.  
**Relationships:** Contributes to [Role](#role); fulfilled by [Capabilities](#capability); determines [Procedures](./ontology-3-execution-layer.md#procedure).

**Responsibility vs. Procedure:**
- **Responsibility** = What you must achieve (outcome-focused)
- **Procedure** = How you achieve it (process-focused)

**Banking Examples by Role:**

| Role | Responsibilities |
|------|------------------|
| **Dispute Analyst** | Investigate disputed transactions within SLA; Determine liability accurately; Document findings completely |
| **Credit Underwriter** | Assess creditworthiness objectively; Ensure regulatory compliance; Approve within delegated authority |
| **AML Analyst** | Review suspicious activity alerts; File SARs when required; Maintain investigation documentation |
| **Branch Manager** | Ensure branch operational compliance; Resolve escalated customer issues; Manage staff performance |

**Compliance Perspective:**
Responsibilities are often derived from:
- Regulatory requirements (e.g., "Report suspicious transactions within 30 days")
- Internal policies (e.g., "Respond to customer complaints within 48 hours")
- Service level agreements (e.g., "Process wire transfers within 2 hours")

**See also:** [Role](#role), [Capability](#capability), [Procedure](./ontology-3-execution-layer.md#procedure)

---

## Capability
**Definition:** The skills, knowledge, certifications, or functional abilities an [Agent](./ontology-3-execution-layer.md#agent) possesses that enable them to perform work and fulfill [Responsibilities](#responsibility).  
**Role:** Enable [Activities](./ontology-3-execution-layer.md#activity); matched to [Responsibilities](#responsibility) to determine role eligibility.  
**Relationships:** Fulfills [Responsibilities](#responsibility); possessed by [Agents](./ontology-3-execution-layer.md#agent); developed through [Training](./ontology-3-execution-layer.md#training).

**Capability vs. Capacity:**
- **Capability** = "Can they do it?" (qualitative—skills and knowledge)
- **Capacity** = "How much can they do?" (quantitative—workload limits)

**Types of Capabilities:**

| Type | Description | Banking Examples |
|------|-------------|------------------|
| **Domain Knowledge** | Understanding of business rules and regulations | AML regulations, Credit policy, Card network rules |
| **Technical Skills** | Ability to use systems and tools | Core banking navigation, Fraud detection tools |
| **Analytical Skills** | Ability to interpret data and draw conclusions | Transaction pattern analysis, Risk assessment |
| **Communication** | Ability to interact with stakeholders | Customer negotiation, Regulatory correspondence |
| **Certifications** | Formal qualifications | CAMS (AML), CFE (Fraud), Credit analyst certification |

**Human Agent Capabilities (Examples):**
- Fraud investigation expertise
- Regulatory compliance knowledge
- Customer de-escalation skills
- Multi-language proficiency

**AI Agent Capabilities (Examples):**
- Pattern recognition across large datasets
- Natural language processing for document analysis
- Real-time transaction scoring
- Automated data extraction from documents

**Capability Matching:**
When a [Task](./ontology-3-execution-layer.md#task) requires specific capabilities, only [Agents](./ontology-3-execution-layer.md#agent) with matching capabilities can be assigned:

```
Task: "Review SAR Filing"
Required Capabilities: [AML Knowledge, CAMS Certification, SAR Writing]
                              │
                              ▼
               Match against Agent Capability Profile
                              │
                              ▼
               Eligible Agents assigned via Task Queue
```

**See also:** [Capacity](#capacity), [Training](./ontology-3-execution-layer.md#training), [Responsibility](#responsibility), [Task Queue](./ontology-3-execution-layer.md#task-queue)

---

## Capacity
**Definition:** The quantitative limits on how much work an [Agent](./ontology-3-execution-layer.md#agent) can handle—measured in time, throughput, or concurrent task limits.  
**Role:** Constrains [Activities](./ontology-3-execution-layer.md#activity) and informs workload distribution; prevents agent overload.  
**Relationships:** Limits [Agents](./ontology-3-execution-layer.md#agent); considered by [Task Queues](./ontology-3-execution-layer.md#task-queue) for assignment strategies.

**Capacity vs. Capability:**
- **Capability** = "Can they do it?" (qualitative)
- **Capacity** = "How much can they do?" (quantitative)

**Capacity Dimensions:**

| Dimension | Description | Banking Examples |
|-----------|-------------|------------------|
| **Concurrent Tasks** | Maximum tasks in-progress simultaneously | Analyst can work on 5 cases at once |
| **Daily Throughput** | Tasks completable per day | Underwriter processes 25 applications/day |
| **Availability** | Hours available for work | Agent works 8 hours, 5 days/week |
| **Response Time** | Time to first action on new tasks | Must pick up task within 15 minutes |

**Human vs. AI Capacity:**

| Agent Type | Typical Capacity Characteristics |
|------------|----------------------------------|
| **Human** | Limited by working hours, fatigue, context-switching costs; high quality on complex judgment tasks |
| **AI** | Near-unlimited throughput for suitable tasks; 24/7 availability; may need human oversight for edge cases |

**Capacity in Practice:**
```
Agent: Fraud Analyst (Human)
├── Max Concurrent Cases: 8
├── Daily Capacity: 25 cases
├── Working Hours: 09:00-17:00 EST
└── Current Load: 6 cases (75% utilized)

Agent: Document Classifier (AI)
├── Max Concurrent: 1000 documents
├── Daily Capacity: 50,000 documents
├── Availability: 24/7
└── Current Load: 342 documents (0.3% utilized)
```

**See also:** [Capability](#capability), [Agent](./ontology-3-execution-layer.md#agent), [Task Queue](./ontology-3-execution-layer.md#task-queue)

---

## Decision
**Definition:** Act by a human or AI [Agent](./ontology-3-execution-layer.md#agent) to select a course of action.  
**Role:** Supports [Goals](#goal); may be aided by [Decision Applications](./ontology-4-automation-layer.md#decision-application).  
**Relationships:** Informed by [Information Elements](#information-element); realized in OPD **Decide**.  
**Example:** "Block IP," "Escalate incident," "Approve credit."

**See also:** [Decision Application](./ontology-4-automation-layer.md#decision-application), [Goal](#goal)

---

## Information Element
**Definition:** Data that has been analyzed, contextualized, and made meaningful for decision-making. Information Elements transform raw facts into actionable insights.  
**Role:** Bridges raw [Data Elements](#data-element) to decision-ready knowledge; tells the story behind the data.  
**Relationships:** Fed by [Data Elements](#data-element); informs [Decisions](#decision); used by [Agents](./ontology-3-execution-layer.md#agent) during [Activities](./ontology-3-execution-layer.md#activity).

**The Data → Information Transformation:**

| Data Element (Raw) | Information Element (Meaningful) |
|--------------------|----------------------------------|
| `login_attempts: 5, timespan: 120s, device: new` | "5 failed logins from new device within 2 minutes—potential account takeover attempt" |
| `transfer_amount: 50000, dest_country: NG, beneficiary: first_time` | "Large first-time transfer to high-risk jurisdiction—requires enhanced due diligence" |
| `account_balance: -500, overdraft_limit: 0` | "Account is overdrawn with no overdraft protection—potential NSF situation" |

**Banking Examples:**
- **Dispute Context:** "Customer has disputed 3 transactions in the last 90 days, all from the same merchant category"
- **Credit Assessment:** "Applicant's debt-to-income ratio is 45%, above our 40% threshold"
- **Fraud Pattern:** "This card was used in Lagos and London within 30 minutes—physically impossible"

**See also:** [Data Element](#data-element), [Decision](#decision)

---

## Data Element
**Definition:** Raw, unprocessed facts as they are recorded—not yet interpreted or contextualized. Data Elements are the building blocks from which [Information Elements](#information-element) are derived.  
**Role:** Source material for analysis and decision support; the "atoms" of operational knowledge.  
**Relationships:** Feeds [Information Elements](#information-element); stored in systems; referenced by [Operations](./ontology-3-execution-layer.md#operation-abstract).

**Characteristics:**
- Objective and factual (no interpretation)
- Timestamped and attributable to a source
- May be structured (database records) or unstructured (documents, logs)

**Banking Examples:**

| Category | Data Elements |
|----------|---------------|
| **Transaction Data** | Amount, timestamp, merchant ID, MCC code, terminal location |
| **Customer Data** | Account number, name, address, phone, email, date of birth |
| **Authentication Data** | Login timestamp, IP address, device fingerprint, geolocation |
| **Document Data** | PDF content, upload timestamp, file hash, document type |
| **System Data** | API response code, processing time, error message |

**Example Record:**
```json
{
  "transaction_id": "TXN-2024-001234",
  "amount": 5000.00,
  "currency": "USD",
  "timestamp": "2024-01-15T14:32:05Z",
  "merchant_id": "M-9876",
  "mcc_code": "5411",
  "card_present": false,
  "ip_address": "102.89.45.12"
}
```

**See also:** [Information Element](#information-element)

---

## Knowledge Base (KB)
**Definition:** A repository of all information resources required for [Agents](./ontology-3-execution-layer.md#agent) and operations automation engineers to complete various [Requests](./ontology-1-perception-layer.md#request).  
**Role:** Authoritative source of guidance for [Decisions](#decision) and [Actions](./ontology-3-execution-layer.md#action).  
**Relationships:** Contains [SOPs](#sop-standard-operating-procedure), policies, [Runbooks](#runbook), control function [Checklists](#checklist); referenced by [Agents](./ontology-3-execution-layer.md#agent) during [Operations](./ontology-3-execution-layer.md#operation-abstract).

**Characteristics:**
- Written in human-friendly language
- Authoritative and versioned
- Includes: SOPs, policies, procedures, control function checklists, product information

**Scope:**

| Level | Content | Managed By |
|-------|---------|------------|
| **System KB** | Industry knowledge, domain best practices, regulatory guidance | Platform Operators |
| **Tenant KB** | Tenant-specific policies, product information, business rules | Tenant Admins |

**Example:** "Dispute Resolution SOP," "Fraud Detection Policy," "KYC Compliance Checklist."

**See also:** [SOP](#sop-standard-operating-procedure), [Runbook](#runbook), [Checklist](#checklist)

---

## Runbook
**Definition:** A set of steps an [Agent](./ontology-3-execution-layer.md#agent) should perform when handling a specific [Task](./ontology-3-execution-layer.md#task).  
**Role:** Task-level guidance; the SOP of a [Task](./ontology-3-execution-layer.md#task).  
**Relationships:** Referenced by [Tasks](./ontology-3-execution-layer.md#task); may be referenced by [SOPs](#sop-standard-operating-procedure); part of [Knowledge Base](#knowledge-base-kb).

**Hierarchy:**

| Term | Scope | Governs |
|------|-------|---------|
| **SOP** | Operation-level | How an entire [Operation](./ontology-3-execution-layer.md#operation-abstract) should be handled |
| **Runbook** | Task-level | Steps an agent should perform for a specific [Task](./ontology-3-execution-layer.md#task) |

```
SOP (Operation)
  └── may reference multiple Runbooks (for Tasks within that Operation)
```

**Characteristics:**
- Versioned and authoritative
- May be reused across different [Operations](./ontology-3-execution-layer.md#operation-abstract), though reuse value may be limited in practice
- Human-readable with optional structured steps for automation

**Example:** "Verify Transaction Details Runbook," "Escalation Procedure Runbook," "Document Upload Review Runbook."

**See also:** [SOP](#sop-standard-operating-procedure), [Task](./ontology-3-execution-layer.md#task), [Knowledge Base](#knowledge-base-kb)

---

## Checklist
**Definition:** A structured representation of routine reviews or checks that [Agents](./ontology-3-execution-layer.md#agent) are required to perform proactively on a schedule.  
**Role:** Control/governance utility for generating periodic [Signals](./ontology-1-perception-layer.md#signal) and aggregating operation outcomes.  
**Relationships:** Generates Time-Signals (via scheduling); triggers [Requests](./ontology-1-perception-layer.md#request); aggregates [Operation](./ontology-3-execution-layer.md#operation-abstract) outcomes.

**Characteristics:**
- Defined at [Workbench](./ontology-1-perception-layer.md#workbench) level
- Schedule-driven: Hourly, Daily, Weekly, Monthly, etc.
- Quality, governance, or audit related activities
- Access-controlled visibility to checklist and associated [Requests](./ontology-1-perception-layer.md#request)

**How Checklists Work:**

```
Checklist Item + Schedule Config
        │
        ▼
  Time-Signal (via Kale)
        │
        ▼
  Business Request (role-based tasks)
        │
        ▼
  Operation (Procedure/Workflow/Case)
        │
        ▼
  Aggregated Outcomes (visibility in Checklist)
```

**Note:** Checklist is NOT an [Operation](./ontology-3-execution-layer.md#operation-abstract) type like Procedure/Workflow/Case. It is a scheduling and aggregation utility that *uses* Operations.

**Example:** "Daily Cash Position Review," "Weekly Reconciliation Audit," "Monthly Compliance Attestation."

**See also:** [Signal](./ontology-1-perception-layer.md#signal), [Request](./ontology-1-perception-layer.md#request), [Operation](./ontology-3-execution-layer.md#operation-abstract), [Knowledge Base](#knowledge-base-kb)

---

**Navigation:** [← Perception Layer](./ontology-1-perception-layer.md) | [Ontology Reference](./ontology-reference.md) | [Execution Layer →](./ontology-3-execution-layer.md)

