# 4.6 The Learning Path

Enterprise agents must learn from experience—but that learning cannot silently become policy. Seer and Hub implement a governed learning path that moves insights from operational feedback to authoritative enterprise knowledge, with human approval gates at critical transitions.

## The Learning Problem

**Why agents must learn:**
- Business processes evolve
- New patterns emerge in operational data
- Agent behaviors need refinement based on outcomes
- Manual updates don't scale

**Why uncontrolled learning is dangerous:**
- Silent policy drift
- Bias amplification
- Unpredictable behavior
- Compliance risk

The solution is a **governed learning path** with explicit promotion gates.

## The Promotion Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                  OPERATIONAL FEEDBACK                        │
│     (Explicit, implicit, outcome feedback)                   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    AGENT MEMORY                              │
│     Session-scoped hypotheses, transient learnings           │
│     (PII permitted, ephemeral)                               │
└──────────────────────────┬──────────────────────────────────┘
                           │ Explicit write via Signal Exchange
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               ENTERPRISE MEMORY - EPISODIC                   │
│     Decisions, outcomes, overrides, handoffs                 │
│     (Immutable, no PII, 7+ years)                           │
└──────────────────────────┬──────────────────────────────────┘
                           │ Pattern detection + validation
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               ENTERPRISE MEMORY - SEMANTIC                   │
│     Patterns, hypotheses, beliefs, constraints               │
│     (Organizational beliefs, validated)                      │
└──────────────────────────┬──────────────────────────────────┘
                           │ Governance approval (HUMAN GATE)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  ENTERPRISE KNOWLEDGE                        │
│     Authoritative policy, facts, procedures                  │
│     (ETSL: asserted, versioned, time-aware)                 │
└─────────────────────────────────────────────────────────────┘
```

## Promotion Flows

### Flow 1: Episodic → Semantic

Patterns detected across multiple cases become organizational beliefs:

```yaml
# Multiple decisions with similar outcomes
episodic_pattern:
  cases: [case-101, case-102, case-103, ...]
  pattern: "Disputes filed within 24h of transaction have 90% approval rate"
  occurrences: 47
  consistency: 0.91
  
# Promoted to semantic memory
semantic_record:
  type: hypothesis
  hypothesis_id: "hyp-fast-disputes"
  description: "Rapid dispute filing correlates with valid disputes"
  confidence: 0.87
  evidence_count: 47
  status: pending_validation
```

### Flow 2: Episodic → Procedural

Successful action sequences become learned skills:

```yaml
# Repeated successful workflow
action_pattern:
  trigger: "merchant_error_confirmed"
  sequence:
    1. verify_transaction_details
    2. check_customer_history
    3. approve_refund_if_under_ceiling
  success_rate: 0.94
  cases: 156
  
# Promoted to procedural memory
procedural_record:
  type: learned_skill
  skill_id: "skill-merchant-error-handling"
  description: "Efficient merchant error dispute resolution"
  steps: [...]
  applicable_when: "merchant_error_confirmed = true"
```

### Flow 3: Semantic → ETSL (Knowledge Promotion)

High-confidence semantic beliefs become authoritative knowledge:

```yaml
# Semantic hypothesis ready for promotion
semantic_candidate:
  hypothesis_id: "hyp-fast-disputes"
  confidence: 0.92
  evidence_count: 150
  stable_for_days: 45
  contradictions: 3
  
# Submitted for governance review
governance_request:
  candidate: "hyp-fast-disputes"
  evidence_package: "ev-pkg-789"
  recommended_action: "promote to ETSL as business rule"
  reviewer: knowledge-governance-committee
  
# After approval → ETSL assertion
etsl_assertion:
  assertion_id: "ast-dispute-timing"
  statement: "Disputes filed within 24h warrant priority processing"
  authority: "fraud-ops-governance"
  effective_from: "2026-02-01"
  provenance:
    source_type: learned_hypothesis
    source_id: "hyp-fast-disputes"
    approved_by: "policy-committee"
    approval_date: "2026-01-25"
```

## Enterprise Learning Services

Hub's Enterprise Learning Services orchestrates promotions:

```
┌─────────────────────────────────────────────────────────────┐
│            ENTERPRISE LEARNING SERVICES                      │
│                                                              │
│   Pattern Detection                                          │
│   • Identify recurring patterns in episodic memory           │
│   • Calculate confidence scores                              │
│   • Detect when patterns are stable                          │
│                                                              │
│   Evidence Packaging                                         │
│   • Compile supporting cases                                 │
│   • Generate evidence bundles                                │
│   • Prepare governance submission                            │
│                                                              │
│   Governance Checkpoints                                     │
│   • Enforce approval gates                                   │
│   • Route to appropriate reviewers                           │
│   • Track approval status                                    │
│                                                              │
│   Conflict Detection                                         │
│   • Identify contradictions with existing knowledge          │
│   • Flag conflicting patterns                                │
│   • Support rollback when beliefs are disproven              │
└─────────────────────────────────────────────────────────────┘
```

## Human Gates

The critical control: humans must approve promotion to authoritative knowledge.

| Promotion | Gate Type | Approvers |
|-----------|-----------|-----------|
| Agent → Enterprise Memory | Implicit (via Signal Exchange routing) | System |
| Episodic → Semantic | Automatic with criteria | System + monitoring |
| Semantic → ETSL | **Explicit human approval** | Knowledge governance, Policy committee |

### Why Human Gates Matter

- **Accountability:** A human is accountable for policy changes
- **Quality control:** Prevents bias amplification and errors from becoming policy
- **Auditability:** Approval chain is recorded in CAF
- **Reversibility:** Humans can reject, defer, or roll back

## Initial Operating Model

Enterprise Learning Services is designed for phased automation:

**Phase 1 (Initial):**
- Analysts manually identify patterns
- Promotion candidates flagged via reports
- Manual governance review
- Manual ETSL authoring

**Phase 2 (Maturity):**
- System suggests promotion candidates
- Semi-automated evidence packaging
- Integrated governance workflow
- Human confirms suggestions

**Phase 3 (Future):**
- Automated pattern detection with confidence thresholds
- Auto-promotion for low-risk patterns (with oversight)
- Continuous monitoring and anomaly detection

---

**References:**
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md`
*   `olympus-seer-docs/why-seer/part-1-background/03-memory-requirements/03-5-learning-imperative.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-10-feedback-learning-requirements.md`
