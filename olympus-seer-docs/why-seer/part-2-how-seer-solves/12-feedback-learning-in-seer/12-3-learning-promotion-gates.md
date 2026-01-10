# 12.3 Learning Promotion Gates

Human approval gates are the critical control that prevents agent learnings from silently becoming policy. At each promotion stage, humans validate that learnings are appropriate before they gain authority.

## Gate Locations

```
Agent Memory → Enterprise Memory (Episodic)
    │
    │ Gate 1: Is this worth preserving?
    │         (Usually automatic via Signal Exchange)
    │
    ▼
Enterprise Memory (Episodic) → Enterprise Memory (Semantic)
    │
    │ Gate 2: Is this pattern real?
    │         (Analyst review or automated with threshold)
    │
    ▼
Enterprise Memory (Semantic) → Enterprise Knowledge (ETSL)
    │
    │ Gate 3: Should this become policy?
    │         (MANDATORY HUMAN APPROVAL)
    │
    ▼
Enterprise Knowledge
```

## Gate 1: Preservation Gate

Determines what's worth keeping:

```yaml
preservation_gate:
  type: automatic_with_rules
  
  auto_preserve:
    - decision_records (all)
    - outcome_records (all)
    - override_records (all)
    - high_signal_feedback
    
  do_not_preserve:
    - routine_queries
    - low_value_interactions
    
  review_required:
    - unusual_patterns
    - edge_cases
```

## Gate 2: Pattern Validation Gate

Determines if detected patterns are real:

```yaml
pattern_validation_gate:
  type: threshold_or_review
  
  auto_promote_if:
    - consistency > 0.90
    - evidence_count > 20
    - no_contradictions
    
  require_review_if:
    - consistency < 0.90
    - potential_bias_detected
    - conflicts_with_existing
    
  reviewers:
    - data_analysts
    - domain_experts
```

## Gate 3: Knowledge Authority Gate

**MANDATORY HUMAN APPROVAL** for policy changes:

```yaml
knowledge_authority_gate:
  type: mandatory_human_approval
  
  cannot_bypass: true
  
  reviewers_required:
    minimum: 2
    from_roles:
      - knowledge_management_owner
      - domain_expert
      - compliance (if policy-related)
      
  review_package:
    - hypothesis_statement
    - supporting_evidence
    - contradiction_analysis
    - policy_impact_assessment
    - risk_assessment
    
  approval_options:
    - approve: promotes to knowledge
    - approve_with_modification: promotes with changes
    - defer: more evidence needed
    - reject: hypothesis invalid
```

## Review Workflow

### Submission

```yaml
promotion_request:
  hypothesis_id: hyp-partial-refund-001
  submitted_by: learning_service
  timestamp: 2026-01-10T10:00:00Z
  
  evidence_summary:
    observations: 47
    confidence: 0.87
    contradiction_rate: 0.06
    
  recommended_action: promote_to_knowledge
```

### Review Process

```yaml
review_process:
  assigned_to:
    - reviewer_1: kmo@acme.com
    - reviewer_2: policy@acme.com
    
  deadline: 2026-01-17
  
  review_checklist:
    - evidence_sufficient: [yes/no]
    - pattern_valid: [yes/no]
    - policy_aligned: [yes/no]
    - risk_acceptable: [yes/no]
    - recommendation: [approve/defer/reject]
```

### Decision

```yaml
gate_decision:
  hypothesis_id: hyp-partial-refund-001
  
  reviews:
    - reviewer: kmo@acme.com
      decision: approve
      notes: "Pattern aligns with policy intent"
      
    - reviewer: policy@acme.com
      decision: approve_with_modification
      notes: "Add threshold: only when evidence score > 0.8"
      
  final_decision: approve_with_modification
  
  promotion:
    target: procedural_guidance
    effective_date: 2026-02-01
    version: 1.0
```

## Gate Audit

All gate decisions are recorded:

```yaml
gate_audit_record:
  gate_id: gate-xyz789
  gate_type: knowledge_authority
  timestamp: 2026-01-15T14:00:00Z
  
  subject: hyp-partial-refund-001
  
  reviews:
    - reviewer: kmo@acme.com
      decision: approve
      timestamp: 2026-01-14T10:00:00Z
      
    - reviewer: policy@acme.com
      decision: approve_with_modification
      timestamp: 2026-01-15T09:00:00Z
      
  outcome:
    decision: approved_with_modification
    promoted_to: dispute-handling-procedures-v2.1
    effective: 2026-02-01
    
  accountability:
    accountable_principal: kmo@acme.com
    approval_authority: policy-committee
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-10-feedback-learning-requirements.md`

