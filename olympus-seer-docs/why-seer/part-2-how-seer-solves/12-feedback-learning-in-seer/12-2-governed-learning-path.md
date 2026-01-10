# 12.2 Governed Learning Path

The governed learning path ensures that agent learnings move from operational observation to authoritative knowledge through controlled promotion with human approval gates.

## The Learning Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                  OPERATIONAL FEEDBACK                        │
│     (Explicit, implicit, outcome signals)                    │
└──────────────────────────┬──────────────────────────────────┘
                           │ Captured
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    AGENT MEMORY                              │
│     Session-scoped observations, transient hypotheses        │
│     • Not authoritative                                      │
│     • Ephemeral                                              │
└──────────────────────────┬──────────────────────────────────┘
                           │ Pattern detection
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               ENTERPRISE MEMORY - EPISODIC                   │
│     Decision records, outcomes, overrides                    │
│     • Immutable                                              │
│     • Long-retained                                          │
└──────────────────────────┬──────────────────────────────────┘
                           │ Pattern aggregation
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               ENTERPRISE MEMORY - SEMANTIC                   │
│     Patterns, hypotheses, beliefs                            │
│     • Validated observations                                 │
│     • Not yet authoritative                                  │
└──────────────────────────┬──────────────────────────────────┘
                           │ HUMAN APPROVAL GATE
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  ENTERPRISE KNOWLEDGE                        │
│     Authoritative policy, facts, procedures                  │
│     • Normative                                              │
│     • Versioned                                              │
│     • Governs agent behavior                                 │
└─────────────────────────────────────────────────────────────┘
```

## Learning Stages

### Stage 1: Feedback Capture

Raw feedback is captured in context:

```yaml
feedback_capture:
  source: explicit_correction
  
  observation:
    agent_proposed: approve_full_refund
    human_corrected: approve_partial_refund
    reason: "Policy section 4.3 applies"
    
  context:
    case_type: merchant_dispute
    customer_tier: standard
    dispute_amount: 450
```

### Stage 2: Pattern Detection

Patterns emerge from aggregated feedback:

```yaml
pattern_detection:
  algorithm: statistical_aggregation
  
  observation:
    - 15 corrections in last 30 days
    - common_pattern: partial_refund_correction
    - conditions: [dispute_amount > 300, merchant_responded]
    
  hypothesis:
    statement: "When dispute amount > $300 and merchant has responded, partial refund is often appropriate"
    confidence: 0.78
    evidence_count: 15
```

### Stage 3: Hypothesis Formation

Pattern becomes semantic memory:

```yaml
hypothesis_record:
  hypothesis_id: hyp-partial-refund-001
  
  statement: "Partial refunds should be considered when dispute amount exceeds $300 and merchant has provided a response"
  
  evidence:
    supporting_cases: 15
    contradicting_cases: 3
    
  confidence: 0.78
  
  status: pending_validation
```

### Stage 4: Human Validation

Human reviews and approves:

```yaml
validation_request:
  hypothesis: hyp-partial-refund-001
  
  evidence_package:
    - supporting_cases: [case-111, case-222, ...]
    - contradiction_analysis
    - policy_alignment_check
    
  submitted_to:
    role: knowledge_management_owner
    
  decision: approve
  
  notes: "Aligns with policy 4.3 interpretation. Recommend adding to agent guidance."
```

### Stage 5: Knowledge Promotion

Approved hypothesis becomes knowledge:

```yaml
knowledge_promotion:
  source: hyp-partial-refund-001
  
  target:
    type: procedural_guidance
    location: dispute-handling-procedures
    
  content:
    statement: "When dispute amount exceeds $300 and merchant has provided a documented response, consider partial refund based on evidence strength."
    
  effective_from: 2026-02-01
  approved_by: kmo@acme.com
  approval_date: 2026-01-15
```

## Promotion Criteria

Promotion requires meeting thresholds:

```yaml
promotion_criteria:
  to_semantic:
    min_observations: 5
    min_consistency: 0.80
    min_timespan: 14_days
    
  to_knowledge:
    min_confidence: 0.85
    min_evidence: 20
    min_stability: 30_days
    contradiction_ratio_max: 0.10
    human_approval: required
```

## Learning Controls

Safeguards prevent problematic learning:

```yaml
learning_controls:
  prohibited:
    - silent_policy_change
    - bypass_approval
    - PII_in_knowledge
    
  monitored:
    - rapid_hypothesis_changes
    - high_contradiction_rates
    - conflict_with_existing_knowledge
    
  required:
    - audit_trail
    - human_gate_for_authority
    - version_control
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md`
*   `olympus-seer-docs/why-seer/part-1-background/03-memory-requirements/03-5-learning-imperative.md`

