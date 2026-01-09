# Process Architect Operator

> **Status:** 🟡 Draft — Under active development

The Process Architect Operator manages **Normative Specifications** for Workbenches and Scenarios. These specifications define *"what ought to be done"* — the roles, goals, standard operating procedures, and compliance requirements that govern operations.

---

## Overview

| Operator | Specifications Managed |
|----------|------------------------|
| **workbench-architect-operator** | Workbench Normative Spec, Scenario Normative Spec, SOP Document Spec, Notification Template Spec |

---

## Normative Layer Context

The Normative Specifications align with the **Normative Layer** of the Hub Ontology:

```
┌─────────────────────────────────────────────────────────────────────┐
│                      NORMATIVE LAYER                                 │
│                                                                      │
│   "What ought to be done?" — Goals, Roles, Rules, Decision Criteria │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Workbench Normative Specification                           │   │
│   │  • Purpose and scope                                         │   │
│   │  • Roles and responsibilities                                │   │
│   │  • Compliance frameworks                                     │   │
│   │  • Cross-scenario policies                                   │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              │                                       │
│                              ▼                                       │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  Scenario Normative Specification                            │   │
│   │  • Goals and success criteria                                │   │
│   │  • Agent roles                                               │   │
│   │  • Standard Operating Procedures (SOPs)                      │   │
│   │  • Decision criteria                                         │   │
│   │  • Evidence requirements                                     │   │
│   │  • Escalation rules                                          │   │
│   └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Workbench Architect Operator

The `workbench-architect-operator` reconciles Normative Specifications that establish the rules and standards for a Workbench and its Scenarios.

### Purpose

- Define the normative foundation for workbench operations
- Establish roles, responsibilities, and governance
- Specify compliance requirements and audit controls
- Configure scenario-level operating procedures and decision frameworks

---

## Specifications

### Workbench Normative Specification

Defines the overall normative foundation for a workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchNormativeSpec
metadata:
  name: dispute-operations-normative
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  workbench:
    name: dispute-operations
    display_name: "Dispute Operations"
    version: "1.0.0"

  # Purpose and Scope
  purpose:
    description: |
      This workbench handles customer disputes for credit and debit card 
      transactions, ensuring timely resolution in compliance with Regulation E 
      and card network rules.
    
    in_scope:
      - Credit card transaction disputes
      - Debit card transaction disputes
      - Provisional credit decisions
      - Merchant communication
      - Network chargebacks
    
    out_of_scope:
      - Fraud investigations (handled by Fraud Workbench)
      - Account closures
      - Collections

  # Compliance Framework
  compliance:
    frameworks:
      - name: regulation-e
        description: "Electronic Fund Transfer Act"
        requirements:
          - id: reg-e-11
            description: "Error resolution within 10 business days"
          - id: reg-e-provisional
            description: "Provisional credit within 10 days if investigation extended"
      
      - name: visa-core-rules
        description: "Visa Core Rules for Disputes"
        requirements:
          - id: visa-120
            description: "Chargeback within 120 days of transaction"
      
      - name: mastercard-chargeback-guide
        description: "Mastercard Chargeback Guide"
    
    audit_controls:
      - id: ctrl-001
        name: "Decision Documentation"
        description: "All dispute decisions must be documented with rationale"
        frequency: per_decision
      
      - id: ctrl-002
        name: "Evidence Retention"
        description: "All evidence must be retained for 7 years"
        frequency: continuous

  # Roles and Responsibilities
  roles:
    - id: dispute-analyst
      name: "Dispute Analyst"
      description: "Reviews disputes and makes initial decisions"
      responsibilities:
        - Review incoming disputes
        - Gather evidence
        - Make provisional credit decisions
        - Communicate with merchants
      required_skills:
        - dispute-resolution
        - card-network-rules
        - customer-communication

    - id: senior-analyst
      name: "Senior Dispute Analyst"
      description: "Handles complex disputes and escalations"
      responsibilities:
        - Handle escalated disputes
        - Review analyst decisions
        - Manage merchant relationships
        - Mentor junior analysts
      required_skills:
        - dispute-resolution
        - card-network-rules
        - escalation-management

    - id: supervisor
      name: "Dispute Supervisor"
      description: "Manages team and ensures SLA compliance"
      responsibilities:
        - Monitor workload distribution
        - Ensure SLA compliance
        - Handle customer escalations
        - Approve high-value decisions
      required_skills:
        - team-management
        - sla-monitoring
        - escalation-handling

  # Cross-Scenario Policies
  policies:
    - id: four-eyes-principle
      name: "Four Eyes Principle"
      description: "Disputes over $10,000 require two approvers"
      applies_to:
        scenarios:
          - high-value-dispute
        conditions:
          - dispute_amount > 10000

    - id: conflict-of-interest
      name: "Conflict of Interest Check"
      description: "Agents cannot process disputes for accounts they own"
      applies_to:
        scenarios:
          - all

    - id: sla-priority
      name: "SLA-Based Priority"
      description: "Tasks are prioritized based on SLA urgency"
      configuration:
        priority_factors:
          - sla_remaining_time
          - customer_tier
          - dispute_amount

  # Supervision Configuration
  supervision:
    escalation_contacts:
      - level: 1
        role: senior-analyst
        notification: immediate
      - level: 2
        role: supervisor
        notification: immediate
      - level: 3
        role: department-manager
        notification: within_1_hour

    review_requirements:
      - scenario: high-value-dispute
        review_percentage: 100
      - scenario: standard-dispute
        review_percentage: 10

  # Knowledge References
  knowledge_references:
    - name: "Dispute Resolution Handbook"
      type: sop_document
      location: "knowledge://dispute-ops/handbook"
    - name: "Regulation E Guide"
      type: compliance_document
      location: "knowledge://compliance/reg-e"
    - name: "Card Network Rules"
      type: reference_document
      location: "knowledge://compliance/card-networks"
```

### Scenario Normative Specification

Defines the normative requirements for a specific scenario within a workbench.

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioNormativeSpec
metadata:
  name: standard-dispute-normative
  namespace: acme-bank
  labels:
    workbench: dispute-operations
    scenario: standard-dispute
spec:
  # Identity
  scenario:
    name: standard-dispute
    display_name: "Standard Dispute Resolution"
    version: "1.2.0"
    workbench_ref: dispute-operations

  # Goals and Success Criteria
  goals:
    primary:
      description: "Resolve customer disputes fairly and within regulatory timeframes"
      success_criteria:
        - metric: resolution_time
          target: "< 10 business days"
          threshold: 95  # 95% of disputes
        - metric: customer_satisfaction
          target: ">= 4.0"
          scale: "1-5"
        - metric: regulatory_compliance
          target: "100%"
    
    secondary:
      - description: "Minimize provisional credit losses"
        success_criteria:
          - metric: provisional_credit_recovery
            target: ">= 80%"
      - description: "First contact resolution when possible"
        success_criteria:
          - metric: first_contact_resolution
            target: ">= 30%"

  # Agent Roles (scenario-specific)
  agent_roles:
    - id: intake-agent
      name: "Intake Agent"
      description: "Reviews and categorizes incoming disputes"
      tasks:
        - initial-review
        - categorization
        - evidence-request
      decision_authority:
        - approve_disputes_under: 100
        - request_additional_info: true
        - reject_clearly_invalid: true

    - id: resolution-agent
      name: "Resolution Agent"
      description: "Investigates and resolves disputes"
      tasks:
        - investigation
        - merchant-contact
        - resolution-decision
      decision_authority:
        - approve_disputes_under: 5000
        - issue_provisional_credit: true
        - initiate_chargeback: true

    - id: approval-agent
      name: "Approval Agent"
      description: "Approves high-value or complex disputes"
      tasks:
        - high-value-review
        - exception-handling
      decision_authority:
        - approve_disputes_under: 50000
        - override_merchant_response: true

  # Standard Operating Procedures (References to SOPDocumentSpec)
  sops:
    - ref: dispute-handling-sop            # Reference to SOPDocumentSpec
      sections:                             # Which sections apply to this scenario
        - initial-review
        - evidence-collection
        - decision-making
        - resolution
    
    - ref: regulation-e-compliance-sop     # Reference to SOPDocumentSpec
      sections:
        - provisional-credit-rules
        - timeline-requirements
    
    # Inline SOP summaries for quick reference (full detail in SOPDocumentSpec)
    sop_summaries:
      - id: sop-intake
        name: "Dispute Intake Procedure"
        description: "Steps for processing new dispute submissions"
        key_steps:
          - "Verify customer identity and account ownership"
          - "Confirm transaction exists in system"
          - "Categorize dispute type"
          - "Determine provisional credit eligibility"
          - "Request additional documentation if needed"
        full_document_ref: dispute-handling-sop

      - id: sop-investigation
        name: "Dispute Investigation Procedure"
        key_steps:
          - "Review all submitted evidence"
          - "Contact merchant for response (SLA: 3 business days)"
          - "Analyze merchant response"
          - "Make resolution decision with documented rationale"
        full_document_ref: dispute-handling-sop

  # Decision Criteria
  decision_criteria:
    - id: provisional-credit
      name: "Provisional Credit Decision"
      description: "Criteria for issuing provisional credit"
      rules:
        - condition: "customer_history == 'good' AND amount <= 500"
          decision: "approve_immediately"
          rationale: "Low risk, good customer"
        - condition: "amount > 500 AND amount <= 5000"
          decision: "approve_with_evidence"
          rationale: "Moderate amount requires documentation"
        - condition: "amount > 5000"
          decision: "escalate_to_senior"
          rationale: "High value requires senior review"
        - condition: "customer_history == 'poor'"
          decision: "require_full_investigation"
          rationale: "History indicates risk"

    - id: resolution-decision
      name: "Final Resolution Decision"
      description: "Criteria for resolving the dispute"
      rules:
        - condition: "evidence_supports_customer"
          decision: "find_for_customer"
        - condition: "evidence_supports_merchant"
          decision: "find_for_merchant"
        - condition: "insufficient_evidence"
          decision: "find_for_customer"
          rationale: "Regulation E default favors consumer"

  # Evidence Requirements
  evidence_requirements:
    intake:
      required:
        - name: "customer_statement"
          type: document
          description: "Written statement from customer"
        - name: "transaction_record"
          type: system_data
          description: "Transaction from core banking system"
      optional:
        - name: "supporting_documents"
          type: document
          description: "Receipts, communications, etc."

    resolution:
      required:
        - name: "investigation_notes"
          type: memo
          description: "Agent investigation notes"
        - name: "decision_rationale"
          type: decision_record
          description: "Documented reason for decision"
        - name: "evidence_summary"
          type: evidence_bundle
          description: "All evidence considered"
      conditional:
        - name: "merchant_response"
          type: document
          condition: "merchant_contacted"

  # Escalation Rules
  escalation:
    sla_based:
      - name: "Approaching Reg E Deadline"
        trigger:
          type: sla_threshold
          threshold_hours: 48
          sla_metric: regulation_e_deadline
        action:
          escalate_to: senior-analyst
          priority: high
          notification: immediate

    value_based:
      - name: "High Value Dispute"
        trigger:
          type: attribute
          condition: "dispute_amount >= 10000"
        action:
          escalate_to: approval-agent
          notification: immediate

    exception_based:
      - name: "Customer VIP"
        trigger:
          type: attribute
          condition: "customer_tier == 'platinum'"
        action:
          escalate_to: senior-analyst
          priority: high

  # Task Definitions (normative view)
  task_types:
    - id: initial-review
      name: "Initial Dispute Review"
      description: "Review and categorize new dispute"
      expected_duration_minutes: 15
      sla_minutes: 120
      skills_required:
        - dispute-resolution

    - id: investigation
      name: "Dispute Investigation"
      description: "Investigate dispute and gather evidence"
      expected_duration_minutes: 45
      sla_minutes: 2880  # 2 business days
      skills_required:
        - dispute-resolution
        - evidence-analysis

    - id: resolution-decision
      name: "Resolution Decision"
      description: "Make final resolution decision"
      expected_duration_minutes: 20
      sla_minutes: 480
      skills_required:
        - dispute-resolution
        - decision-making

  # Notification Requirements
  notifications:
    - event: dispute_received
      recipients:
        - role: intake-agent
      channels:
        - desk
        - email
      template: "dispute_received_notification"

    - event: provisional_credit_issued
      recipients:
        - role: subject  # Customer
      channels:
        - email
        - sms
      template: "provisional_credit_issued_customer"

    - event: resolution_complete
      recipients:
        - role: subject
      channels:
        - email
      template: "dispute_resolution_notification"

    - event: sla_warning
      recipients:
        - role: assignee
        - role: supervisor
      channels:
        - desk
        - email
      template: "sla_warning_notification"

  # Audit Configuration
  audit:
    decision_logging:
      enabled: true
      details: full  # full | summary
      retention_days: 2555  # 7 years
    
    evidence_retention:
      enabled: true
      retention_days: 2555
      
    access_logging:
      enabled: true
      events:
        - case_viewed
        - decision_made
        - evidence_added

  # Knowledge Bindings (scenario-specific)
  knowledge:
    required:
      - ref: "knowledge://dispute-ops/handbook"
        sections:
          - standard-dispute-process
      - ref: "knowledge://compliance/reg-e"
        sections:
          - error-resolution
          - provisional-credit

    suggested:
      - ref: "knowledge://dispute-ops/merchant-contacts"
      - ref: "knowledge://dispute-ops/common-scenarios"
```

---

### SOP Document Specification

Defines Standard Operating Procedure documents with versioning and governance. Referenced by Scenario Normative Specifications.

```yaml
apiVersion: hub.olympus.io/v1
kind: SOPDocumentSpec
metadata:
  name: dispute-handling-sop
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  document:
    id: sop-dispute-handling
    name: "Dispute Handling Procedure"
    display_name: "Standard Dispute Handling Procedure"
    version: "2.1.0"
    workbench_ref: dispute-operations

  # Classification
  classification:
    category: operational  # operational | compliance | safety | reference
    sensitivity: internal  # public | internal | confidential | restricted
    regulatory_refs:
      - regulation-e
      - visa-core-rules

  # Content
  content:
    format: markdown  # markdown | html | pdf
    
    # Inline content or reference
    source:
      type: inline  # inline | git | sharepoint | url
      content: |
        # Dispute Handling Procedure
        
        ## 1. Purpose
        This procedure defines the standard steps for handling customer disputes 
        in compliance with Regulation E and card network rules.
        
        ## 2. Scope
        Applies to all dispute types: chargebacks, fraud claims, and service disputes.
        
        ## 3. Procedure Steps
        
        ### 3.1 Initial Review
        1. Verify customer identity and account ownership
        2. Confirm transaction exists in core banking system
        3. Categorize dispute by type
        4. Check for duplicate submissions
        
        ### 3.2 Evidence Collection
        1. Request documentation from customer if needed
        2. Retrieve transaction details from core banking
        3. Check for prior disputes on same transaction
        4. Document all evidence gathered
        
        ### 3.3 Decision Making
        1. Apply decision criteria from scenario specification
        2. Document rationale for decision
        3. Obtain approval if amount exceeds threshold
        4. Record decision in Enterprise Memory
        
        ### 3.4 Resolution
        1. Execute resolution action (credit, reject, partial)
        2. Notify customer of outcome
        3. Initiate chargeback with network if applicable
        4. Close dispute with full documentation
        
        ## 4. Escalation
        Escalate to supervisor when:
        - Amount exceeds $10,000
        - Customer is VIP tier
        - Prior dispute history indicates fraud risk
        - Evidence is ambiguous
        
        ## 5. Compliance Notes
        - Regulation E requires resolution within 10 business days
        - Provisional credit must be issued if investigation extended
        - All decisions must be documented with rationale

    # Or external source
    # source:
    #   type: git
    #   repository: "https://github.com/acme-bank/sops"
    #   path: "dispute-ops/handling-procedure.md"
    #   branch: main

  # Approval Workflow
  approval:
    required: true
    approvers:
      - role: compliance-officer
      - role: process-owner
    min_approvals: 2

  # Review Schedule
  review:
    frequency: quarterly  # monthly | quarterly | annually
    next_review_date: "2026-04-01"
    reviewers:
      - role: process-architect
      - role: compliance-officer

  # Effective Dates
  effective:
    from: "2026-01-01"
    to: null  # null = no end date
    supersedes:
      - sop-dispute-handling-v2.0.0

  # Access Control
  access:
    visibility: workbench  # workbench | tenant | public
    allowed_roles:
      - dispute-analyst
      - senior-analyst
      - supervisor
```

#### SOP Document Examples

**Compliance SOP:**

```yaml
apiVersion: hub.olympus.io/v1
kind: SOPDocumentSpec
metadata:
  name: regulation-e-compliance-sop
spec:
  document:
    id: sop-reg-e-compliance
    name: "Regulation E Compliance Procedure"
    version: "1.0.0"
    workbench_ref: dispute-operations

  classification:
    category: compliance
    sensitivity: confidential
    regulatory_refs:
      - regulation-e

  content:
    source:
      type: sharepoint
      location: "https://acme.sharepoint.com/sites/compliance/reg-e-sop.docx"
      sync_schedule: "0 0 * * *"  # Daily sync

  approval:
    required: true
    approvers:
      - role: chief-compliance-officer
    min_approvals: 1

  review:
    frequency: annually
    next_review_date: "2027-01-01"
```

---

### Notification Template Specification

Defines notification templates for scenario events. Referenced by Scenario Automation Specifications.

```yaml
apiVersion: hub.olympus.io/v1
kind: NotificationTemplateSpec
metadata:
  name: dispute-notification-templates
  namespace: acme-bank
  labels:
    workbench: dispute-operations
spec:
  # Identity
  template_set:
    name: dispute-notification-templates
    display_name: "Dispute Notification Templates"
    version: "1.0.0"
    workbench_ref: dispute-operations

  # Templates by Event and Mechanism
  templates:
    # Task Assignment Notifications
    - id: task_assigned_email
      event: task_assigned
      mechanism: email
      
      subject: "[{{priority | uppercase}}] New Task: {{task.display_name}}"
      
      body: |
        Hi {{recipient.name}},
        
        You have been assigned a new task in the Dispute Operations workbench.
        
        **Task Details:**
        - **Task:** {{task.display_name}}
        - **Request:** {{request.id}}
        - **Customer:** {{request.subject.name}}
        - **Amount:** {{request.context.amount | currency}}
        - **Priority:** {{task.priority | capitalize}}
        - **Due:** {{task.sla_deadline | date:"MMMM d, yyyy h:mm a"}}
        
        **Description:**
        {{task.description}}
        
        {{#cta}}
        [View Task]({{cta.view_task_url}})
        [Start Working]({{cta.start_task_url}})
        {{/cta}}
        
        ---
        This is an automated notification from Dispute Operations.
      
      # Template variables documentation
      variables:
        - name: recipient
          type: object
          description: "Notification recipient"
        - name: task
          type: object
          description: "Task entity"
        - name: request
          type: object
          description: "Request entity"
        - name: cta
          type: object
          description: "Call-to-action URLs"

    - id: task_assigned_sms
      event: task_assigned
      mechanism: sms
      
      body: |
        New task assigned: {{task.display_name}} ({{request.id}}). Due: {{task.sla_deadline | date:"MMM d"}}. View in Agent Desk.

    - id: task_assigned_push
      event: task_assigned
      mechanism: push
      
      title: "New Task Assigned"
      body: "{{task.display_name}} - Due {{task.sla_deadline | relative}}"
      
      data:
        task_id: "{{task.id}}"
        request_id: "{{request.id}}"
        deep_link: "hub://tasks/{{task.id}}"

    # SLA Warning Notifications
    - id: sla_warning_email
      event: sla_warning
      mechanism: email
      
      subject: "⚠️ SLA Warning: {{task.display_name}} due in {{task.sla_remaining | duration}}"
      
      body: |
        Hi {{recipient.name}},
        
        **SLA Warning:** Your assigned task is approaching its deadline.
        
        **Task:** {{task.display_name}}
        **Request:** {{request.id}}
        **Time Remaining:** {{task.sla_remaining | duration}}
        **Deadline:** {{task.sla_deadline | date:"MMMM d, yyyy h:mm a"}}
        
        Please complete or escalate this task before the deadline.
        
        {{#cta}}
        [View Task]({{cta.view_task_url}})
        [Escalate]({{cta.escalate_url}})
        {{/cta}}

    - id: sla_warning_teams
      event: sla_warning
      mechanism: teams_adaptive_card
      
      card_template: |
        {
          "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
          "type": "AdaptiveCard",
          "version": "1.4",
          "body": [
            {
              "type": "TextBlock",
              "text": "⚠️ SLA Warning",
              "weight": "Bolder",
              "size": "Large",
              "color": "Warning"
            },
            {
              "type": "FactSet",
              "facts": [
                {"title": "Task", "value": "{{task.display_name}}"},
                {"title": "Request", "value": "{{request.id}}"},
                {"title": "Time Left", "value": "{{task.sla_remaining | duration}}"}
              ]
            }
          ],
          "actions": [
            {
              "type": "Action.OpenUrl",
              "title": "View Task",
              "url": "{{cta.view_task_url}}"
            }
          ]
        }

    # Customer Notifications
    - id: dispute_received_email
      event: request_created
      mechanism: email
      recipient_type: subject  # subject = customer
      
      subject: "Your Dispute Has Been Received - Reference #{{request.id}}"
      
      body: |
        Dear {{request.subject.name}},
        
        We have received your dispute for the following transaction:
        
        **Transaction Details:**
        - **Date:** {{request.context.transaction_date | date:"MMMM d, yyyy"}}
        - **Amount:** {{request.context.amount | currency}}
        - **Merchant:** {{request.context.merchant_name}}
        - **Reference:** {{request.id}}
        
        **What Happens Next:**
        1. Our team will review your dispute within 2 business days
        2. We may contact you if additional information is needed
        3. You will receive updates on the progress of your dispute
        
        **Expected Resolution:** Within 10 business days
        
        If you have questions, please contact us at disputes@acme-bank.com 
        or call 1-800-ACME-BANK.
        
        Thank you for your patience.
        
        ACME Bank Dispute Resolution Team

    - id: resolution_complete_email
      event: request_completed
      mechanism: email
      recipient_type: subject
      
      subject: "Dispute Resolved - Reference #{{request.id}}"
      
      body: |
        Dear {{request.subject.name}},
        
        Your dispute has been resolved.
        
        **Resolution Details:**
        - **Reference:** {{request.id}}
        - **Transaction Amount:** {{request.context.amount | currency}}
        - **Resolution:** {{request.outcome.decision | capitalize}}
        {{#if request.outcome.credit_amount}}
        - **Credit Amount:** {{request.outcome.credit_amount | currency}}
        {{/if}}
        
        **Resolution Reason:**
        {{request.outcome.rationale}}
        
        {{#if request.outcome.decision == 'approved'}}
        The credit has been applied to your account and will appear 
        within 1-2 business days.
        {{/if}}
        
        If you have questions about this resolution, please contact us.
        
        Thank you for banking with ACME Bank.

  # Template Filters (custom Mustache helpers)
  filters:
    - name: currency
      description: "Format as currency"
      example: "{{amount | currency}} → $1,234.56"
    
    - name: date
      description: "Format date"
      example: "{{timestamp | date:'MMM d, yyyy'}} → Jan 5, 2026"
    
    - name: duration
      description: "Format duration"
      example: "{{minutes | duration}} → 2h 30m"
    
    - name: relative
      description: "Relative time"
      example: "{{timestamp | relative}} → in 2 hours"
    
    - name: uppercase
      description: "Convert to uppercase"
    
    - name: capitalize
      description: "Capitalize first letter"
```

---

## Specification Relationships

```
WorkbenchNormativeSpec
        │
        │ references
        ▼
┌───────────────────────────────────────────┐
│          ScenarioNormativeSpec            │
│  ┌─────────────────────────────────────┐  │
│  │  Goals ──► SOPs ──► Decision Criteria│  │
│  │     │                    │           │  │
│  │     ▼                    ▼           │  │
│  │  Roles ◄── Escalation ──► Evidence   │  │
│  │     │                    │           │  │
│  │     ▼                    ▼           │  │
│  │  Tasks ◄────────── Notifications     │  │
│  └─────────────────────────────────────┘  │
└───────────────────────────────────────────┘
```

---

## Reconciliation Behavior

| Specification | Create | Update | Delete |
|---------------|--------|--------|--------|
| WorkbenchNormativeSpec | Create normative record, validate roles | Validate no active scenario conflicts | Check no active scenarios depend on it |
| ScenarioNormativeSpec | Validate against workbench normative, register | Version bump, validate compatibility | Archive, check no active requests |

### Validation Rules

1. **Role Consistency**: Scenario roles must align with Workbench roles
2. **Compliance Mapping**: Scenario SOPs must address Workbench compliance requirements
3. **SLA Feasibility**: Task SLAs must be achievable given expected workload
4. **Evidence Completeness**: Required evidence must be producible by defined tasks

---

## Versioning

Normative Specifications follow semantic versioning:

| Version Change | When to Bump |
|----------------|--------------|
| **Major** | Breaking changes to roles, goals, or compliance requirements |
| **Minor** | New SOPs, decision criteria, or optional features |
| **Patch** | Clarifications, typos, non-behavioral changes |

---

## Process Architect Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│                    Process Architect Workflow                         │
│                                                                       │
│  1. Define Workbench Normative Specification                          │
│     └── Purpose, Compliance, Roles, Policies                          │
│                              │                                        │
│                              ▼                                        │
│  2. Define Scenario Normative Specifications                          │
│     └── Goals, SOPs, Decision Criteria, Evidence, Escalation          │
│                              │                                        │
│                              ▼                                        │
│  3. Commit to Git                                                     │
│     └── Version controlled, reviewed, approved                        │
│                              │                                        │
│                              ▼                                        │
│  4. Operator Reconciles                                               │
│     └── Validates, registers in Hub                                   │
│                              │                                        │
│                              ▼                                        │
│  5. Handoff to Developer                                              │
│     └── Normative specs guide automation development                  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Operators Overview](./README.md)
- [Developer Operators](./developer-operators.md) — Automation and Deployment specs
- [Supervisor Operators](./supervisor-operators.md) — Operational configuration
- [Ontology - Normative Layer](../../01-concepts/ontology-2-normative-layer.md)
- [Scenario Development Journey](../../08-personas-and-journeys/journeys/scenario-development.md)

---

*The Process Architect Operator enables declarative definition of operational standards, ensuring consistent governance across Hub deployments.*

