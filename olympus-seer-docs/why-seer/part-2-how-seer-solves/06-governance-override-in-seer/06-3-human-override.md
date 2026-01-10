# 6.3 Human Override

Human override is the mechanism by which humans can intervene in agent operations—approving, rejecting, modifying, or taking over agent decisions. This is fundamental to Human-AI Teaming and ensures humans remain in control of consequential outcomes.

## Types of Human Override

| Override Type | When It Occurs | Who Initiates |
|---------------|----------------|---------------|
| **Approval required** | Policy mandates human sign-off | System (escalation) |
| **Rejection** | Human rejects agent proposal | Human |
| **Correction** | Human modifies agent output | Human |
| **Takeover** | Human assumes control entirely | Human |
| **Emergency stop** | Critical situation | Human or system |

## Override Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   HUMAN OVERRIDE FLOW                        │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │              AGENT OPERATION                       │    │
│   │                                                    │    │
│   │   Reasoning → Proposal → [Approval Gate?]          │    │
│   │                              │                     │    │
│   │                              ▼                     │    │
│   │                     ┌───────────────┐              │    │
│   │                     │ Requires      │              │    │
│   │                     │ Approval?     │              │    │
│   │                     └───────┬───────┘              │    │
│   │                             │                      │    │
│   │              No ──┘         │                      │    │
│   │                             ▼ Yes                  │    │
│   └─────────────────────────────┼──────────────────────┘    │
│                                 │                           │
│   ┌─────────────────────────────▼──────────────────────┐    │
│   │              HUMAN REVIEW INTERFACE                │    │
│   │                                                    │    │
│   │   • Present proposal with context                  │    │
│   │   • Show agent rationale                           │    │
│   │   • Provide approval/rejection options             │    │
│   │   • Allow modification                             │    │
│   │   • Allow takeover                                 │    │
│   └─────────────────────────────┬──────────────────────┘    │
│                                 │                           │
│   ┌─────────────────────────────▼──────────────────────┐    │
│   │              HUMAN DECISION                         │    │
│   │                                                    │    │
│   │   Approve → Execute with audit                     │    │
│   │   Reject  → Return to agent or terminate           │    │
│   │   Modify  → Execute modified with audit            │    │
│   │   Takeover → Human assumes control                 │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Escalation Triggers

Situations that trigger human review:

### Policy-Mandated Escalation

```yaml
escalation_policy:
  triggers:
    - condition: action.amount > 500
      escalate_to: manager
      reason: "Exceeds agent authority ceiling"
      
    - condition: case.complexity == "high"
      escalate_to: senior_analyst
      reason: "High complexity case"
      
    - condition: customer.tier == "vip"
      escalate_to: relationship_manager
      reason: "VIP customer handling"
```

### Agent-Initiated Escalation

Agents can request human help:

```python
if confidence < 0.7:
    return await seer.escalate(
        reason="Low confidence in decision",
        proposal=my_proposal,
        context=current_context
    )
```

### System-Detected Escalation

System detects need for human:

```yaml
auto_escalation:
  - trigger: loop_detected
    escalate_to: agent_operator
    
  - trigger: repeated_failures
    escalate_to: agent_operator
    
  - trigger: customer_frustration_detected
    escalate_to: human_support
```

## Human Review Interface

What humans see when reviewing:

```yaml
review_request:
  case_id: case-12345
  agent: dispute-analyst-tier1
  
  proposal:
    action: approve_refund
    amount: 750
    
  rationale:
    summary: "Merchant error confirmed, customer in good standing"
    factors:
      - merchant_error_confirmed: 0.95
      - customer_history: positive
      - policy_compliance: within_guidelines
      
  escalation_reason: "Amount exceeds agent authority ($500)"
  
  context:
    transaction: $750 charge at ACME Store
    evidence: [transaction_record, merchant_response]
    precedents: [case-11234 (approved), case-11189 (approved)]
    
  options:
    - approve: "Approve as proposed"
    - modify: "Approve different amount"
    - reject: "Deny refund"
    - takeover: "Handle manually"
```

## Override Recording

All overrides are recorded in CAF:

```yaml
override_record:
  record_id: "or-abc123"
  case_id: case-12345
  timestamp: 2026-01-10T15:00:00Z
  
  original_proposal:
    action: approve_refund
    amount: 750
    
  override:
    type: modification
    new_action: approve_refund
    new_amount: 500
    
  overrider:
    principal: manager@acme.com
    role: dispute_manager
    
  justification: "Reduce to agent authority ceiling; escalation unnecessary"
  
  agent:
    employment_spec: dispute-analyst-acme-production
```

## Learning from Overrides

Overrides provide feedback for improvement:

### Override Patterns

```yaml
override_analytics:
  period: last_30_days
  agent: dispute-analyst-tier1
  
  patterns:
    - type: rejection
      count: 12
      common_reasons:
        - "Policy interpretation error" (5)
        - "Missing information" (4)
        - "Customer context not considered" (3)
        
    - type: modification
      count: 28
      common_modifications:
        - "Reduced amount" (15)
        - "Added disclosure" (8)
        - "Changed tone" (5)
```

### Feedback Loop

```
Override Recorded
    │
    ▼
Pattern Analysis
    │
    ▼
Identify Improvement Opportunities
    │
    ▼
Training Spec Update (governed)
    │
    ▼
Reduced Override Rate
```

## Takeover Protocol

When human takes over completely:

```yaml
takeover:
  timestamp: 2026-01-10T15:00:00Z
  case_id: case-12345
  
  handoff_context:
    - conversation_history: full
    - agent_reasoning: full
    - tool_results: full
    - current_step: verify_eligibility
    
  agent_status: suspended_for_case
  
  human:
    principal: manager@acme.com
    role: dispute_manager
    
  reason: "Customer request for human handling"
```

---

**References:**
*   `aosm-meta-model/human-ai-team.md`
*   `olympus-seer-docs/seer-design/subsystems/intervention-solver.md`
