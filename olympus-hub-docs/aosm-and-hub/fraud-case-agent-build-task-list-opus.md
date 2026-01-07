# Fraud Case Resolution Agent — Build Task List

> **Author:** Engineer's Perspective  
> **Status:** Planning  
> **Created:** 2026-01-07  
> **Objective:** Detailed task breakdown for building the fraud-case-resolution-agent, with approach, confidence levels, and identified gaps.

---

## Executive Summary

This document provides a structured task breakdown for building an enterprise-grade Fraud Case Resolution Agent using the Olympus Hub and Seer platforms. Each task includes:

- **Approach:** How to address the task based on Hub/Seer documentation
- **Confidence:** HIGH / MEDIUM / LOW
- **Gaps:** What needs clarification before implementation

---

## Context: What We're Building

**Job:** Given an existing (or newly opened) fraud case, the agent helps drive it to resolution:
- Collect/validate evidence
- Propose actions (freeze, step-up auth, reimburse/deny, file SAR referral, escalate)
- Execute *allowed* steps via tools
- Document the outcome with audit-grade rationale

**Key Constraint:** This is not fraud scoring — it's **case resolution**: decisions + actions + documentation under governance.

---

## Phase 1: Foundation & Governance Setup

### Task 1.1: Define Agent Governance Model

**Description:** Establish the governance framework including human accountability, authority ceilings, and escalation rules.

**Approach:**
1. Following the Raw → Trained → Employed model from Seer's Agent Lifecycle Service:
   - Define the **Trained Agent** with guardrails (immutable safety constraints)
   - Define the **Employment Spec** with authority delegation and scope limiting
2. Establish RASCI matrix:
   - Agents can be **Responsible** for investigation and recommendation
   - Humans must remain **Accountable** for final decisions above threshold
3. Define authority ceilings aligned with fraud policy:
   - Auto-approve/deny thresholds
   - Mandatory human review triggers
   - SAR referral always requires human sign-off

**Confidence:** HIGH

The documentation is explicit that "Humans are always Accountable; agents can be Responsible" (RASCI principle). The guardrail immutability constraint is well-documented.

**Gaps:** None — governance model is well-defined.

---

### Task 1.2: Define Memory Artifact Schemas (CAF Integration)

**Description:** Design the concrete schemas for memory artifacts that will support auditability and learning.

**Approach:**
Based on the CAF and Enterprise Memory documentation, define these artifacts:

1. **DecisionRecord**
   ```yaml
   decision_id: uuid
   timestamp: datetime
   actor: {type: agent|human, id: string}
   case_id: string
   decision: {action: approve|deny|freeze|step_up|escalate|sar_referral, outcome: string}
   policy_references: [policy_id]
   evidence_bundle_id: uuid
   confidence: float  # 0-1
   uncertainty_flags: [string]
   alternatives_considered: [{action, reason_rejected}]
   ```

2. **OverrideRecord**
   ```yaml
   override_id: uuid
   original_decision_id: uuid
   overriding_actor: {type: human, id: string}
   override_action: string
   rationale: string
   outcome: string  # to be updated after resolution
   ```

3. **IncidentTimeline**
   ```yaml
   timeline_id: uuid
   case_id: string
   events: [{timestamp, event_type, actor, description, evidence_refs}]
   ```

4. **HypothesisRecord** (for semantic enterprise memory)
   ```yaml
   hypothesis_id: uuid
   statement: string  # "Merchant X shows elevated chargeback pattern"
   scope: {segment, time_range}
   confidence: float
   supporting_evidence: [evidence_id]
   counter_evidence: [evidence_id]
   review_cadence: duration
   status: draft|active|promoted|rejected
   ```

**Confidence:** HIGH

CAF documentation explicitly lists DecisionRecords, Evidence Bundles, and Explanation Service. The schema structure follows the fraud-case-resolution-agent.md guidance.

**Gaps:**
- ⚠️ **Gap 1.2.1:** Exact CAF schema specification is marked as "TODO" in Hub docs. Need to confirm final schema formats with the CAF team.
- ⚠️ **Gap 1.2.2:** Retention and deletion semantics (PII, legal hold) need legal/compliance input.

---

### Task 1.3: Establish Policy-of-Record Location

**Description:** Set up the governed knowledge layer where fraud policies live.

**Approach:**
1. Use Hub **Knowledge Services** as the authoritative source for:
   - Fraud policy thresholds
   - Regulatory obligations (timelines, disclosures, reporting triggers)
   - Reason-code taxonomy
   - Approved SOPs/runbooks

2. Structure in Knowledge Bank:
   ```
   knowledge-bank/
   ├── policies/
   │   ├── fraud-policy-v2.3.yaml
   │   ├── sla-requirements.yaml
   │   └── regulatory-compliance/
   │       ├── reg-e-requirements.yaml
   │       └── sar-filing-rules.yaml
   ├── reference-data/
   │   ├── reason-code-taxonomy.yaml
   │   └── risk-score-definitions.yaml
   └── runbooks/
       ├── account-takeover-sop.md
       ├── unauthorized-transaction-sop.md
       └── friendly-fraud-sop.md
   ```

3. Version all policies with semantic versioning
4. Establish approval workflow via Hub's artifact governance

**Confidence:** MEDIUM

Knowledge Services architecture is documented but marked as "🔴 Stub". The conceptual model is clear (normative layer, governed knowledge), but implementation details are incomplete.

**Gaps:**
- ⚠️ **Gap 1.3.1:** Knowledge Bank ingress pipelines, chunking strategies, and retrieval algorithms are listed as "TODO" in Hub docs.
- ⚠️ **Gap 1.3.2:** Policy versioning and approval workflow integration needs specification.

---

## Phase 2: Agent Development (Raw Agent)

### Task 2.1: Create Raw Agent Application

**Description:** Build the deployable artifact (container) that implements the agent orchestration.

**Approach:**
Using the Strands Agents framework (as shown in the example-agent), create:

```python
from strands_agents import Agent, BedrockProvider
from strands_agents.tools import Tool

# Initialize with Bedrock (or other Seer Model Gateway)
provider = BedrockProvider(
    region=config.region,
    model_id=config.model_id
)

# Create the fraud case resolution agent
agent = Agent(
    provider=provider,
    system_prompt=FRAUD_CASE_SYSTEM_PROMPT,
    tools=[
        # Tool definitions (see Task 2.3)
    ]
)
```

Key components:
1. **Agent loop** — Strands handles the reasoning loop
2. **Context management** — Integrate with Seer Context Assembly Engine
3. **Memory integration** — Connect to Hub Memory Services
4. **Multi-modal support** — Text-based for this agent (extendable)

**Confidence:** HIGH

The example-agent demonstrates the pattern clearly. Strands Agents provides the orchestration framework.

**Gaps:**
- ⚠️ **Gap 2.1.1:** Need to confirm Model Gateway integration (model routing, failover) — documented but incomplete.
- ⚠️ **Gap 2.1.2:** Container deployment specification for Seer runtime needs clarification.

---

### Task 2.2: Design System Prompt (Behavioral Configuration)

**Description:** Create the system prompt that defines agent behavior, aligned with fraud case resolution requirements.

**Approach:**
```
You are a Fraud Case Resolution Agent operating under strict governance.

## Your Role
You help drive fraud cases to resolution by:
1. Collecting and validating evidence
2. Analyzing transaction patterns and account state
3. Proposing actions based on policy
4. Executing allowed steps via approved tools
5. Documenting decisions with audit-grade rationale

## Constraints
- You MUST NOT approve/deny cases above $[THRESHOLD] without human review
- You MUST escalate any case involving SAR-reportable conditions
- You MUST cite policy references for every decision recommendation
- You MUST document uncertainty when confidence < 0.8

## Decision Framework
For each case, you will:
1. Compile context (enterprise knowledge + memory + operational state)
2. Apply the appropriate SOP for the fraud category
3. Gather required evidence per policy
4. Propose action with rationale
5. If authorized, execute; otherwise escalate

## Available Tools
[Tool catalog populated at runtime]

## Output Requirements
Every recommendation must include:
- Proposed action
- Policy references
- Evidence summary with provenance
- Confidence level
- Risk flags or uncertainty markers
```

**Confidence:** HIGH

The fraud-case-resolution-agent.md provides clear guidance on agent contract and context frame structure.

**Gaps:** None for prompt design; implementation testing will refine.

---

### Task 2.3: Define Tool Catalog

**Description:** Define the tools the agent can invoke, with schemas, preconditions, and authorization.

**Approach:**
Based on the fraud-case-resolution-agent requirements and Hub's Direct Tool Dispatcher:

| Tool | Purpose | Preconditions | Authorization |
|------|---------|---------------|---------------|
| `get_case_state` | Fetch current case from CMS | case_id required | Read access to CMS |
| `get_transaction_history` | Fetch transactions from ledger | customer_id or account_id | Read access to core banking |
| `get_account_status` | Current account flags and state | account_id | Read access to core banking |
| `get_device_fingerprint` | Device/session telemetry | session_id or device_id | Read access to fraud vendor |
| `query_vendor_signals` | Risk signals, watchlist hits | customer_id | Read access to fraud vendor |
| `freeze_account` | Freeze account (high-risk) | account_id, rationale | **Human approval** or auto if < threshold |
| `apply_step_up_auth` | Trigger step-up authentication | customer_id, session_id | Automatic for policy-defined conditions |
| `record_decision` | Write DecisionRecord to CAF | decision_payload | Agent identity |
| `escalate_case` | Escalate to human analyst | case_id, reason | Automatic |
| `retrieve_precedent` | Query enterprise memory for similar cases | query, filters | Read access to enterprise memory |
| `retrieve_policy` | Query knowledge bank for applicable policy | policy_type, context | Read access to knowledge bank |

Tool definition example:
```yaml
tool_id: freeze_account
display_name: "Freeze Account"
description: "Apply account freeze for suspected fraud"
input_schema:
  type: object
  properties:
    account_id: {type: string, required: true}
    freeze_type: {enum: [full, partial_debit, partial_credit]}
    rationale: {type: string, required: true}
    case_id: {type: string, required: true}
output_schema:
  type: object
  properties:
    success: {type: boolean}
    freeze_id: {type: string}
    effective_time: {type: datetime}
preconditions:
  - case_status in [open, under_review]
  - evidence_bundle_attached: true
authorization:
  auto_approve_threshold: 1000  # USD
  above_threshold: requires_human_approval
idempotency_key: "{case_id}-{freeze_type}"
```

**Confidence:** HIGH

Hub's Direct Tool Dispatcher and Tool Registry patterns are well-documented. The tool schema structure follows MCP and Hub conventions.

**Gaps:**
- ⚠️ **Gap 2.3.1:** Specific fraud vendor API schemas need to be defined (external dependency).
- ⚠️ **Gap 2.3.2:** Human-in-the-loop checkpoint implementation for high-impact actions (freeze, SAR) needs design.

---

### Task 2.4: Integrate with Case Management System

**Description:** Connect agent to the operational case management system (OLTP).

**Approach:**
1. Define **Machine** in Hub for the case management system:
   ```yaml
   apiVersion: hub.olympus.io/v1
   kind: Machine
   metadata:
     name: fraud-case-cms
   spec:
     type: external
     connection:
       protocol: rest
       base_url: ${CMS_BASE_URL}
       auth:
         type: oauth2_client_credentials
     tools:
       - get_case_state
       - update_case_status
       - add_case_memo
       - get_case_history
   ```

2. Use Direct Tool Dispatcher for synchronous calls:
   ```python
   result = await tools.invoke(
       tool_id="fraud-case-cms/get_case_state",
       params={"case_id": case_id}
   )
   ```

3. Implement state machine validation — ensure case transitions are valid

**Confidence:** HIGH

Hub Machine and Tool abstraction is well-documented. The pattern is consistent with Hub's framework-agnostic approach.

**Gaps:**
- ⚠️ **Gap 2.4.1:** CMS API contract and state machine definition (allowed transitions) — depends on existing system.
- ⚠️ **Gap 2.4.2:** Race condition handling for concurrent case updates needs design.

---

## Phase 3: Training Specification

### Task 3.1: Create Training Spec

**Description:** Define the Training Spec that transforms the Raw Agent into a Trained Agent.

**Approach:**
Following Seer's Agent Lifecycle Service:

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: fraud-case-resolution
  namespace: acme-bank
  version: "1.0.0"
spec:
  # Reference to Raw Agent
  raw_agent_ref:
    name: fraud-case-agent
    version: "^2.0.0"
  
  # Context Definitions
  context:
    tenant_id: acme-bank
    domain: fraud-operations
    role: fraud-case-resolver
    pida:
      perceive:
        - case_state_changes
        - evidence_availability
        - policy_updates
      interpret:
        - transaction_pattern_analysis
        - risk_signal_correlation
        - precedent_matching
      decide:
        - action_recommendation
        - escalation_determination
        - confidence_assessment
      act:
        - tool_invocation
        - record_writing
        - notification_sending
  
  # Behavioral Configuration
  behavior:
    system_prompt_ref: fraud-case-system-prompt-v1
    style_guidelines:
      - formal_professional
      - evidence_based
      - policy_citing
    procedures:
      - fraud-investigation-workflow-v2
      - sar-evaluation-checklist
  
  # Guardrails (IMMUTABLE after publish)
  guardrails:
    ref: fraud-case-guardrails-v1
    constraints:
      - no_sar_filing_without_human_approval
      - no_account_freeze_above_threshold_without_approval
      - no_pii_logging
      - mandatory_rationale_for_denial
  
  # Tool Specifications
  tools:
    allowed:
      - get_case_state
      - get_transaction_history
      - get_account_status
      - freeze_account  # with preconditions
      - escalate_case
      - record_decision
    denied:
      - transfer_funds  # Never allowed
      - delete_evidence  # Never allowed
  
  # Knowledge Bases
  knowledge_bases:
    - ref: fraud-policy-kb
      retrieval_strategy: hybrid
    - ref: regulatory-compliance-kb
      retrieval_strategy: semantic
    - ref: reason-code-taxonomy
      retrieval_strategy: exact
  
  # Memory Training
  memory:
    procedural:
      - fraud-investigation-workflow
      - evidence-collection-checklist
    semantic:
      - fraud-pattern-definitions
    episodic:
      retention_policy: 90d
      summarization: enabled
```

**Confidence:** MEDIUM

The three-layer agent model is well-documented, but Training Spec is marked as "TODO: Detailed design" in Seer docs. The structure above is derived from documented concepts.

**Gaps:**
- ⚠️ **Gap 3.1.1:** Training Spec CRD schema not finalized — need Seer team confirmation.
- ⚠️ **Gap 3.1.2:** Guardrail definition format and enforcement mechanism needs specification.
- ⚠️ **Gap 3.1.3:** Knowledge base reference integration with Hub Knowledge Services needs clarification.

---

### Task 3.2: Define Guardrails

**Description:** Create the immutable safety constraints for the Trained Agent.

**Approach:**
```yaml
apiVersion: seer.olympus.io/v1
kind: Guardrails
metadata:
  name: fraud-case-guardrails
  version: "1.0.0"
spec:
  # Input guardrails
  input:
    - name: pii_sanitization
      type: redaction
      patterns: [ssn, credit_card, dob]
    - name: prompt_injection_detection
      type: filter
      action: reject_and_log
  
  # Output guardrails
  output:
    - name: no_raw_pii
      type: filter
      patterns: [ssn, credit_card]
      action: redact
    - name: mandatory_citation
      type: validation
      rule: decision_must_cite_policy
  
  # Action guardrails
  actions:
    - name: freeze_threshold
      tool: freeze_account
      condition: "amount > 10000"
      action: require_human_approval
    
    - name: sar_mandatory_review
      tool: file_sar_referral
      action: always_require_human_approval
    
    - name: denial_requires_rationale
      tool: deny_claim
      validation: rationale_field_not_empty
  
  # Kill switch conditions
  kill_switch:
    - condition: confidence_consistently_below_0.3
      action: suspend_and_alert
    - condition: error_rate_above_threshold
      action: suspend_and_alert
```

**Confidence:** MEDIUM

Guardrail concepts are documented, but implementation details are sparse. The structure follows standard AI safety patterns.

**Gaps:**
- ⚠️ **Gap 3.2.1:** Guardrail enforcement runtime integration with Seer needs specification.
- ⚠️ **Gap 3.2.2:** PII patterns and redaction rules need compliance team input.

---

## Phase 4: Context Assembly Integration

### Task 4.1: Implement Context Compiler

**Description:** Build the context assembly logic that compiles the agent's working context for each step.

**Approach:**
Following Seer's Context Assembly Engine design:

```python
class FraudCaseContextCompiler:
    """Compiles context from Enterprise Knowledge, Enterprise Memory, and Agent Memory."""
    
    async def compile_context(
        self,
        case_id: str,
        goal: str,
        token_budget: int = 8000
    ) -> ContextFrame:
        # 1. Clarify goal
        decision_type = self._classify_decision(goal)
        
        # 2. Retrieve from multiple sources (parallel)
        knowledge_task = self._retrieve_knowledge(decision_type, case_id)
        enterprise_memory_task = self._retrieve_enterprise_memory(case_id)
        agent_memory_task = self._retrieve_agent_memory(case_id)
        operational_state_task = self._retrieve_operational_state(case_id)
        
        knowledge, ent_memory, agent_memory, op_state = await asyncio.gather(
            knowledge_task, enterprise_memory_task, 
            agent_memory_task, operational_state_task
        )
        
        # 3. Filter and dedupe
        filtered = self._filter_and_dedupe(knowledge, ent_memory, agent_memory, op_state)
        
        # 4. Resolve conflicts (precedence order)
        resolved = self._resolve_conflicts(
            filtered,
            precedence=[
                "system_policy",
                "procedural_allowlist",
                "enterprise_knowledge",
                "operational_state",
                "enterprise_memory",
                "agent_memory"
            ]
        )
        
        # 5. Token budget allocation
        allocated = self._allocate_tokens(resolved, token_budget)
        
        # 6. Assemble structured frame
        frame = ContextFrame(
            constraints=allocated["constraints"],
            goal=goal,
            ground_truth_facts=allocated["facts"],
            relevant_precedent=allocated["precedent"],
            applicable_procedures=allocated["procedures"],
            working_state=allocated["working_state"]
        )
        
        # 7. Log provenance
        self._log_provenance(frame)
        
        return frame
```

Context frame structure:
```
┌─────────────────────────────────────────────────────┐
│ CONTEXT FRAME                                        │
├─────────────────────────────────────────────────────┤
│ 1. CONSTRAINTS                                       │
│    - Tool allowlists                                 │
│    - Safety rules (guardrails)                       │
│    - Escalation rules                                │
├─────────────────────────────────────────────────────┤
│ 2. GOAL                                              │
│    - Current objective                               │
│    - Definition of done                              │
├─────────────────────────────────────────────────────┤
│ 3. GROUND TRUTH FACTS (from OLTP + verified)        │
│    - Case state (from CMS)                           │
│    - Transaction facts (from ledger)                 │
│    - Account flags (from core banking)               │
│    - Vendor results (from fraud vendor)              │
│    [Each with source citation]                       │
├─────────────────────────────────────────────────────┤
│ 4. RELEVANT PRECEDENT (from Enterprise Memory)      │
│    - Similar override outcomes                       │
│    - Prior dispute patterns for segment              │
│    - Incident notes if relevant                      │
│    [Summarized + pointers to full records]           │
├─────────────────────────────────────────────────────┤
│ 5. APPLICABLE PROCEDURES (from Knowledge + Agent)   │
│    - Approved SOP for this fraud category            │
│    - Agent procedure (tool chain)                    │
├─────────────────────────────────────────────────────┤
│ 6. WORKING STATE (from Agent Memory)                │
│    - Tool outputs from previous steps                │
│    - Pending calls                                   │
│    - Partial progress                                │
└─────────────────────────────────────────────────────┘
```

**Confidence:** HIGH

Context Assembly Engine documentation is conceptually complete. The compiler pattern follows the documented precedence model.

**Gaps:**
- ⚠️ **Gap 4.1.1:** SDK/API for retrieving from Hub Memory Services needs confirmation.
- ⚠️ **Gap 4.1.2:** Token budgeting algorithms for large context windows need design.

---

### Task 4.2: Integrate Enterprise Memory Retrieval

**Description:** Implement retrieval from Enterprise Memory for precedent and institutional learning.

**Approach:**
Query Enterprise Memory for:

1. **Prior Override Records** (similar cases):
   ```python
   overrides = await enterprise_memory.query(
       type="OverrideRecord",
       filters={
           "fraud_category": case.fraud_category,
           "amount_range": (case.amount * 0.5, case.amount * 2.0),
           "outcome": ["approved", "denied"]  # both for learning
       },
       limit=5,
       recency_weight=0.3  # Some preference for recent
   )
   ```

2. **Prior Dispute Patterns** (customer/merchant):
   ```python
   patterns = await enterprise_memory.query(
       type="EpisodicMemory",
       entity_type="customer",
       entity_id=case.customer_id,
       event_types=["dispute", "chargeback", "fraud_claim"],
       time_range="2y"
   )
   ```

3. **Incident Notes** (relevant degradations):
   ```python
   incidents = await enterprise_memory.query(
       type="IncidentTimeline",
       filters={
           "affected_systems": ["fraud_model", "vendor_x"],
           "time_range": "7d"
       }
   )
   ```

**Confidence:** MEDIUM

The conceptual model is clear, but Memory Services API is marked as "🔴 Stub" in Hub docs.

**Gaps:**
- ⚠️ **Gap 4.2.1:** Memory Services query API specification needs finalization.
- ⚠️ **Gap 4.2.2:** Memory indexing and search (semantic + filter) implementation details missing.

---

### Task 4.3: Integrate Knowledge Retrieval (RAG)

**Description:** Implement RAG from Hub Knowledge Services for policy and reference data.

**Approach:**
```python
class FraudKnowledgeRetriever:
    def __init__(self, knowledge_client):
        self.client = knowledge_client
    
    async def get_applicable_policy(
        self,
        fraud_category: str,
        jurisdiction: str,
        amount: float
    ) -> PolicyBundle:
        # Retrieve fraud policy
        fraud_policy = await self.client.retrieve(
            knowledge_base="fraud-policy-kb",
            query=f"policy for {fraud_category} fraud in {jurisdiction}",
            filters={"status": "active", "version": "latest"},
            strategy="hybrid"  # semantic + keyword
        )
        
        # Retrieve regulatory requirements
        regulatory = await self.client.retrieve(
            knowledge_base="regulatory-compliance-kb",
            query=f"requirements for fraud case resolution {jurisdiction}",
            filters={"regulation_type": ["reg_e", "aml", "sar"]}
        )
        
        # Retrieve reason code definitions
        reason_codes = await self.client.exact_lookup(
            knowledge_base="reason-code-taxonomy",
            category=fraud_category
        )
        
        return PolicyBundle(
            fraud_policy=fraud_policy,
            regulatory=regulatory,
            reason_codes=reason_codes,
            provenance=self._capture_provenance()
        )
```

**Confidence:** MEDIUM

Knowledge Services conceptual model is clear, but RAG implementation details are "TODO".

**Gaps:**
- ⚠️ **Gap 4.3.1:** Knowledge Bank retrieval API specification needs finalization.
- ⚠️ **Gap 4.3.2:** Chunking and embedding strategies for policy documents need design.
- ⚠️ **Gap 4.3.3:** Provenance tracking for retrieved chunks needs specification.

---

## Phase 5: Hub Scenario Configuration

### Task 5.1: Create Scenario Normative Spec

**Description:** Define the business requirements for the fraud case resolution scenario (Process Architect ownership).

**Approach:**
Following Hub's Scenario Specification Types:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioNormativeSpec
metadata:
  name: fraud-case-resolution
  namespace: acme-bank
spec:
  display_name: "Fraud Case Resolution"
  version: "1.0.0"
  
  description: |
    Automated fraud case resolution with human oversight.
    Handles investigation, evidence collection, action recommendation,
    and resolution documentation with audit-grade rationale.
  
  # Roles involved
  roles:
    - name: fraud-case-agent
      type: ai_agent
      goals:
        - "Investigate case within 24 hours"
        - "Collect required evidence per policy"
        - "Recommend action with policy-backed rationale"
        - "Document decision with audit trail"
      responsibilities:
        - "Query operational systems for case state"
        - "Retrieve and apply applicable policy"
        - "Analyze transaction patterns"
        - "Generate evidence bundle"
        - "Write DecisionRecord"
        
    - name: fraud-analyst
      type: human_agent
      goals:
        - "Review agent recommendations for high-value cases"
        - "Override when warranted with documented rationale"
        - "Approve SAR referrals"
      responsibilities:
        - "Validate agent analysis"
        - "Make final decision on cases above threshold"
        - "Sign off on regulatory filings"
        
    - name: fraud-supervisor
      type: supervisor
      goals:
        - "Ensure SLA compliance"
        - "Handle escalations"
        - "Review override patterns"
  
  # SOPs
  sops:
    - ref: sop-fraud-investigation
    - ref: sop-evidence-collection
    - ref: sop-sar-evaluation
    - ref: sop-customer-communication
  
  # Decision criteria
  decision_criteria:
    - name: liability-determination
      description: "Criteria for determining transaction liability"
      document_ref: fraud-liability-matrix
    - name: refund-eligibility
      description: "Criteria for refund approval"
      document_ref: refund-policy
  
  # Evidence requirements
  evidence_requirements:
    - type: transaction-history
      mandatory: true
      retention: 7y
    - type: device-fingerprint
      mandatory: true
      retention: 90d
    - type: customer-statement
      mandatory: false
      retention: 7y
    - type: vendor-risk-signals
      mandatory: true
      retention: 90d
  
  # Escalation rules
  escalation_rules:
    - condition: "amount > 10000"
      escalate_to: fraud-analyst
    - condition: "sar_indicators_present"
      escalate_to: fraud-analyst
    - condition: "confidence < 0.7"
      escalate_to: fraud-analyst
    - condition: "multiple_prior_disputes > 3"
      escalate_to: fraud-supervisor
  
  # Compliance
  compliance:
    - regulation: "Reg E"
      requirements:
        - "10-day provisional credit for claims > $500"
        - "45-day resolution deadline"
    - regulation: "BSA/AML"
      requirements:
        - "SAR filing within 30 days of detection"
```

**Confidence:** HIGH

Scenario Specification Types are well-documented with examples. This follows the standard pattern.

**Gaps:** None for normative spec — pattern is clear.

---

### Task 5.2: Create Scenario Automation Spec

**Description:** Define the technical implementation for the scenario (Developer ownership).

**Approach:**
```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: fraud-case-resolution
  namespace: acme-bank
spec:
  normative_ref: fraud-case-resolution
  version: "1.0.0"
  
  # Hub Application
  application:
    ref: fraud-case-resolution-app
    version: "1.0.0"
    runtime: seer  # Runs on Seer runtime
  
  # Triggers
  triggers:
    - ref: fraud-case-created-trigger
      signal_type: event
      source: fraud-case-cms
      filter: "event.type == 'case_created' && event.category == 'fraud'"
    
    - ref: fraud-case-updated-trigger
      signal_type: event
      source: fraud-case-cms
      filter: "event.type == 'case_updated'"
    
    - ref: evidence-received-trigger
      signal_type: event
      source: fraud-case-cms
      filter: "event.type == 'evidence_attached'"
  
  # Tool bindings
  tools:
    - name: case-management
      machine_ref: fraud-case-cms
      tools:
        - get_case_state
        - update_case_status
        - add_case_memo
    
    - name: transaction-lookup
      machine_ref: core-banking
      tools:
        - get_transaction_history
        - get_account_status
    
    - name: fraud-signals
      machine_ref: fraud-vendor
      tools:
        - get_device_fingerprint
        - query_risk_signals
    
    - name: actions
      machine_ref: core-banking
      tools:
        - freeze_account
        - apply_step_up_auth
    
    - name: memory
      machine_ref: hub-memory-services
      tools:
        - write_decision_record
        - query_precedent
  
  # Seer agent binding
  seer_agent:
    training_spec_ref: fraud-case-resolution
    employment_spec_ref: fraud-case-resolution-employed
  
  # Notifications
  notifications:
    - event: escalation_required
      template_ref: analyst-escalation-notification
      channels: [teams, email]
    - event: case_resolved
      template_ref: case-resolution-notification
      channels: [email]
```

**Confidence:** MEDIUM

The automation spec pattern is documented, but Seer agent binding integration needs confirmation.

**Gaps:**
- ⚠️ **Gap 5.2.1:** Seer agent binding in Hub Automation Spec needs specification — how does Hub invoke Seer agents?
- ⚠️ **Gap 5.2.2:** Runtime selection (Seer vs other Hub runtimes) needs clarification.

---

### Task 5.3: Create Scenario Deployment Spec

**Description:** Define the deployment configuration for the scenario (Supervisor ownership).

**Approach:**
```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioDeploymentSpec
metadata:
  name: fraud-case-resolution
  namespace: acme-bank
spec:
  automation_ref: fraud-case-resolution
  version: "1.0.0"
  
  # Task queues
  task_queues:
    - task_type: ai_investigation
      queue_ref: fraud-ai-queue
      assignment: ai_delegation
      
    - task_type: human_review
      queue_ref: fraud-analyst-queue
      assignment: skills_based
      required_skills: [fraud_analyst_l2]
      
    - task_type: supervisor_escalation
      queue_ref: fraud-supervisor-queue
      assignment: direct
  
  # Agent enrollment
  agents:
    ai_pool:
      ref: fraud-case-resolution-agent
      concurrency: 50
      auto_scale: true
    human_pool:
      ref: fraud-analysts
      fallback: fraud-supervisor
  
  # SLA parameters
  sla:
    target_completion_hours: 24
    warning_threshold_hours: 16
    critical_threshold_hours: 22
    regulatory_deadline_hours: 240  # 10 days for Reg E
  
  # Activation
  activation:
    enabled: true
    start_date: "2026-02-01"
    gradual_rollout:
      enabled: true
      initial_percentage: 10
      ramp_schedule:
        - day: 7
          percentage: 25
        - day: 14
          percentage: 50
        - day: 21
          percentage: 100
  
  # Environment
  environment:
    variables:
      FREEZE_THRESHOLD: "10000"
      CONFIDENCE_THRESHOLD: "0.7"
```

**Confidence:** HIGH

Deployment spec pattern is well-documented with clear examples.

**Gaps:**
- ⚠️ **Gap 5.3.1:** AI delegation to Seer agents — task handoff mechanism needs specification.

---

## Phase 6: Employment & Deployment

### Task 6.1: Create Employment Spec

**Description:** Define how the Trained Agent is granted authority to act.

**Approach:**
Following Seer's Employed Agent model:

```yaml
apiVersion: seer.olympus.io/v1
kind: EmploymentSpec
metadata:
  name: fraud-case-resolution-employed
  namespace: acme-bank
  version: "1.0.0"
spec:
  # Reference to Training Spec
  training_spec_ref:
    name: fraud-case-resolution
    version: "~1.0.0"
  
  # Work scope
  work_scope:
    workbenches:
      - fraud-operations
    functional_scope:
      - fraud_case_resolution
    temporal_scope: permanent  # or time-bounded
  
  # Authority delegation
  authority:
    delegation_model: role_delegation
    role: fraud-case-resolver
    manager: fraud-ops-manager  # Accountable human
    
    # What the agent CAN do
    permissions:
      - read_case_state
      - read_transaction_history
      - read_account_status
      - read_vendor_signals
      - write_decision_record
      - write_memo
      - invoke_freeze_below_threshold
      - invoke_step_up_auth
      - escalate_case
    
    # What the agent CANNOT do (restrictions from training)
    restrictions:
      - approve_above_threshold_without_human
      - file_sar_directly
      - delete_evidence
  
  # Operational environment
  environment:
    connections:
      - ref: fraud-case-cms
        credential_type: service_account
      - ref: core-banking
        credential_type: service_account
      - ref: fraud-vendor
        credential_type: api_key
    
    secrets:
      - CMS_SERVICE_ACCOUNT
      - CORE_BANKING_SA
      - FRAUD_VENDOR_API_KEY
  
  # Capacity & resources
  capacity:
    concurrent_cases: 50
    token_budget_per_case: 50000
    api_rate_limits:
      core_banking: 100/min
      fraud_vendor: 200/min
  
  # Constraints & policies
  constraints:
    action_limits:
      freeze_account: 100/day  # Circuit breaker
      escalate: unlimited
    approval_requirements:
      - action: freeze_account
        condition: "amount > ${FREEZE_THRESHOLD}"
        requires: human_approval
```

**Confidence:** MEDIUM

Employment model concepts are well-documented, but spec schema is "TODO".

**Gaps:**
- ⚠️ **Gap 6.1.1:** Employment Spec CRD schema needs finalization.
- ⚠️ **Gap 6.1.2:** Credential injection mechanism for secrets needs specification.
- ⚠️ **Gap 6.1.3:** Authority enforcement at runtime — how does Seer enforce delegation limits?

---

### Task 6.2: Deploy to Seer Runtime

**Description:** Deploy the agent to Seer's runtime infrastructure.

**Approach:**
1. Build Raw Agent container:
   ```bash
   docker build -t fraud-case-agent:1.0.0 .
   docker push ${REGISTRY}/fraud-case-agent:1.0.0
   ```

2. Register Raw Agent with Seer:
   ```yaml
   apiVersion: seer.olympus.io/v1
   kind: RawAgent
   metadata:
     name: fraud-case-agent
     version: "1.0.0"
   spec:
     container:
       image: ${REGISTRY}/fraud-case-agent:1.0.0
     identity:
       type: spiffe
       trust_domain: seer.acme-bank
     capabilities:
       - text_reasoning
       - tool_use
       - memory_integration
     health_check:
       endpoint: /health
       interval: 30s
   ```

3. Apply Training Spec (validated → published)
4. Apply Employment Spec (approved → active)
5. Register with Hub Scenario Automation

**Confidence:** LOW

Runtime deployment mechanics are "TODO: Detailed design" in Seer docs.

**Gaps:**
- ⚠️ **Gap 6.2.1:** Raw Agent deployment model (containers, serverless) needs specification.
- ⚠️ **Gap 6.2.2:** Seer runtime infrastructure details incomplete.
- ⚠️ **Gap 6.2.3:** Agent registration and lifecycle API needs specification.

---

## Phase 7: Observability & Audit

### Task 7.1: Implement Decision Logging

**Description:** Ensure all decisions are captured with full provenance.

**Approach:**
Integrate with CAF for every decision:

```python
async def log_decision(
    self,
    case_id: str,
    decision: Decision,
    evidence_bundle: EvidenceBundle,
    context_snapshot: ContextFrame
) -> DecisionRecord:
    record = DecisionRecord(
        decision_id=uuid.uuid4(),
        timestamp=datetime.utcnow(),
        actor=AgentActor(
            type="agent",
            id=self.agent_id,
            version=self.version
        ),
        case_id=case_id,
        decision=decision,
        policy_references=context_snapshot.constraints.policy_refs,
        evidence_bundle_id=evidence_bundle.id,
        confidence=decision.confidence,
        uncertainty_flags=decision.uncertainty_flags,
        alternatives_considered=decision.alternatives,
        context_hash=context_snapshot.hash(),  # For replay
        provenance={
            "knowledge_sources": context_snapshot.knowledge_provenance,
            "memory_sources": context_snapshot.memory_provenance,
            "operational_sources": context_snapshot.operational_provenance
        }
    )
    
    # Write to Enterprise Memory via CAF
    await self.caf_client.write_decision_record(record)
    
    return record
```

**Confidence:** HIGH

CAF decision journaling is conceptually well-documented. The pattern is clear.

**Gaps:**
- ⚠️ **Gap 7.1.1:** CAF write API specification needs finalization.
- ⚠️ **Gap 7.1.2:** Context hashing for replay needs design.

---

### Task 7.2: Implement Agent Observability

**Description:** Integrate with Seer Agent Observability for runtime monitoring.

**Approach:**
```python
# Integrate with Seer observability
from seer.observability import trace, metrics

class FraudCaseAgent:
    @trace("fraud_case_investigation")
    async def investigate_case(self, case_id: str):
        with metrics.timer("case_investigation_duration"):
            # ... investigation logic
            
        metrics.counter("cases_investigated").inc()
        metrics.gauge("agent_confidence").set(decision.confidence)
```

Metrics to track:
- Case throughput (cases/hour)
- Average resolution time
- Confidence distribution
- Escalation rate
- Tool call latency
- Error rate by tool

**Confidence:** MEDIUM

Observability concepts documented, but SDK integration details are sparse.

**Gaps:**
- ⚠️ **Gap 7.2.1:** Seer observability SDK specification incomplete.
- ⚠️ **Gap 7.2.2:** Integration with Olympus Watch needs clarification.

---

### Task 7.3: Implement Explanation Generation

**Description:** Enable on-demand explanation generation for decisions.

**Approach:**
Integrate with CAF Explanation Service:

```python
async def generate_explanation(
    self,
    decision_record_id: str,
    audience: str = "analyst"  # analyst | customer | regulator
) -> Explanation:
    # Retrieve decision record
    record = await self.caf_client.get_decision_record(decision_record_id)
    
    # Retrieve evidence bundle
    evidence = await self.caf_client.get_evidence_bundle(record.evidence_bundle_id)
    
    # Generate explanation using CAF Explanation Service
    explanation = await self.caf_client.generate_explanation(
        decision_record=record,
        evidence_bundle=evidence,
        audience=audience,
        format="narrative"  # narrative | structured | counterfactual
    )
    
    return explanation
```

**Confidence:** MEDIUM

CAF Explanation Service is documented conceptually, but implementation is "TODO".

**Gaps:**
- ⚠️ **Gap 7.3.1:** Explanation Service API specification needs finalization.
- ⚠️ **Gap 7.3.2:** Audience-specific formatting rules need definition.

---

## Phase 8: Testing & Evaluation

### Task 8.1: Create Evaluation Suite

**Description:** Build test fixtures and benchmarks for agent evaluation.

**Approach:**
Following Seer's Agent Evaluation Service:

1. **Policy test fixtures:**
   ```yaml
   # test-fixtures/policy-tests.yaml
   tests:
     - name: high_value_requires_escalation
       input:
         case:
           amount: 15000
           fraud_category: unauthorized_transaction
       expected:
         decision: escalate
         escalate_to: fraud-analyst
     
     - name: clear_fraud_below_threshold
       input:
         case:
           amount: 500
           fraud_category: account_takeover
           evidence:
             device_mismatch: true
             velocity_anomaly: true
       expected:
         decision: deny
         confidence: "> 0.85"
   ```

2. **Benchmark from Enterprise Memory:**
   - Extract real decisions with known outcomes
   - Create regression test suite
   - Measure accuracy on historical cases

3. **CI/CD quality gates:**
   ```yaml
   quality_gates:
     - metric: accuracy
       threshold: 0.92
       dataset: historical_cases
     - metric: false_positive_rate
       threshold: "< 0.05"
     - metric: escalation_appropriateness
       threshold: 0.95
   ```

**Confidence:** MEDIUM

Evaluation concepts are documented, but implementation details are sparse.

**Gaps:**
- ⚠️ **Gap 8.1.1:** Agent Evaluation Service API specification incomplete.
- ⚠️ **Gap 8.1.2:** Benchmark creation from Enterprise Memory needs design.
- ⚠️ **Gap 8.1.3:** CI/CD integration for agent testing needs specification.

---

### Task 8.2: Implement Sandbox Testing

**Description:** Test agent behavior in isolated sandbox before production.

**Approach:**
1. Create sandbox workbench with mock data
2. Deploy Training Spec in "validated" state (not published)
3. Run test scenarios
4. Validate against expected outcomes
5. Review guardrail effectiveness

**Confidence:** MEDIUM

**Gaps:**
- ⚠️ **Gap 8.2.1:** Sandbox environment provisioning needs specification.
- ⚠️ **Gap 8.2.2:** Mock data generation for fraud scenarios needs design.

---

## Gap Summary

### High-Priority Gaps (Blocking)

| ID | Gap | Impact | Owner to Clarify |
|----|-----|--------|------------------|
| Gap 6.2.1 | Raw Agent deployment model | Cannot deploy agent | Seer Team |
| Gap 6.2.2 | Seer runtime infrastructure | Cannot deploy agent | Seer Team |
| Gap 5.2.1 | Seer agent binding in Hub | Cannot integrate Hub + Seer | Hub + Seer Teams |
| Gap 3.1.1 | Training Spec CRD schema | Cannot create Training Spec | Seer Team |

### Medium-Priority Gaps (Design Needed)

| ID | Gap | Impact | Owner to Clarify |
|----|-----|--------|------------------|
| Gap 1.2.1 | CAF schema specification | Memory artifact format unclear | Hub/CAF Team |
| Gap 1.3.1 | Knowledge Bank implementation | RAG setup unclear | Hub Team |
| Gap 4.2.1 | Memory Services query API | Cannot retrieve precedent | Hub Team |
| Gap 4.3.1 | Knowledge Bank retrieval API | Cannot retrieve policy | Hub Team |
| Gap 6.1.3 | Authority enforcement | Security model unclear | Seer Team |
| Gap 2.3.2 | Human-in-the-loop checkpoints | Approval flow unclear | Hub Team |

### Lower-Priority Gaps (Refinement)

| ID | Gap | Impact | Owner to Clarify |
|----|-----|--------|------------------|
| Gap 1.2.2 | Retention semantics | Compliance risk | Legal/Compliance |
| Gap 2.4.1 | CMS API contract | External dependency | CMS Team |
| Gap 7.2.1 | Observability SDK | Monitoring incomplete | Seer Team |

---

## Recommended Next Steps

1. **Immediate:** Schedule gap resolution meetings with Hub and Seer teams for high-priority gaps
2. **Week 1:** Define CAF schemas and Memory/Knowledge APIs (collaboration with Hub team)
3. **Week 2:** Finalize Training Spec and Employment Spec schemas (Seer team)
4. **Week 3:** Build Raw Agent with mock integrations for local testing
5. **Week 4:** Integrate with Hub sandbox environment
6. **Week 5-6:** End-to-end testing with real case data (anonymized)
7. **Week 7-8:** Production deployment with gradual rollout

---

## References

- [Fraud Case Resolution Agent Story](./fraud-case-resolution-agent.md)
- [Enterprise Knowledge vs Memory vs Agent Memory](../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge-memory-other-data.md)
- [Designing an Agent](../../olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md)
- [Hub Architecture](../../olympus-hub-docs/02-system-design/hub-architecture.md)
- [Seer Introduction](../../olympus-seer-docs/seer-design/introduction.md)
- [Agent Lifecycle Service](../../olympus-seer-docs/seer-design/subsystems/agent-lifecycle-service.md)
- [Context Assembly Engine](../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)
- [Memory Services](../../olympus-hub-docs/04-subsystems/memory-services/README.md)
- [Knowledge Services](../../olympus-hub-docs/04-subsystems/knowledge-services/README.md)
- [Cognitive Audit Fabric](../../olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md)

