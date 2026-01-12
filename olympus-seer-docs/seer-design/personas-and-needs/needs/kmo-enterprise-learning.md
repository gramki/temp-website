# KMO Need: Enterprise Learning and Memory Promotion

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [KMO Role Definition](../kmo.md) | [Roles Overview](../roles.md#4-knowledge--memory-owner-kmo)

---

## Overview

The **Knowledge & Memory Owner (KMO)** ([role definition](../roles.md#4-knowledge--memory-owner-kmo)) owns what agents know and remember. A critical responsibility is managing **Enterprise Learning** — the process of promoting valuable learnings from individual agent interactions to enterprise-wide knowledge.

This document details the enterprise learning and memory promotion needs for platform developers building KMO capabilities.

---

## What is Enterprise Learning?

### The Learning Hierarchy

Knowledge in an agent-oriented system exists at multiple levels:

```
Individual Agent Observation
       ↓ (automatic, policy-based)
Episodic Memory (CAF)
       ↓ (COS detects patterns → KMO validates)
Semantic Memory
       ↓ (KMO proposes → KMO + ARAO approves)
Enterprise Knowledge
       ↓ (KMO proposes → APO + ARAO approves)
Published SOPs / Policies
```

### Why This Matters

Without governed enterprise learning:
- **Valuable patterns stay siloed** in individual agents
- **Bad patterns propagate** without validation
- **Knowledge conflicts** emerge across agents
- **No organizational memory** of what worked

---

## Memory Promotion Framework

### Promotion Levels

| Level | Scope | Persistence | Approval |
|-------|-------|-------------|----------|
| **Agent Observation** | Single agent, single task | Session | Automatic |
| **Episodic Memory** | Single agent, across tasks | Persistent | Policy-based |
| **Semantic Memory** | Shared across agents | Persistent | KMO approval |
| **Enterprise Knowledge** | Authoritative truth | Persistent | KMO + ARAO |
| **Published SOP** | Business behavior | Permanent | APO + ARAO |

### Promotion Workflow

```
COS detects pattern across agents
       ↓
COS flags pattern to KMO with evidence
       ↓
KMO validates:
├── Is the pattern correct?
├── Is the pattern stable?
├── Is the pattern valuable?
└── What is the risk?
       ↓
KMO proposes promotion level
       ↓
Approval workflow:
├── Semantic: KMO self-approves
├── Knowledge: KMO + ARAO approve
└── SOP: APO + ARAO approve
       ↓
Pattern promoted
       ↓
COS verifies effect
```

---

## Detection: What Patterns to Promote

### Pattern Types

| Pattern Type | Detection Signal | Promotion Target |
|--------------|------------------|------------------|
| **Recurring Decision** | Same conclusion 3+ times | Semantic memory |
| **Stable Correction** | Consistent user overrides | Knowledge update |
| **Emergent Best Practice** | High-quality reasoning pattern | SOP candidate |
| **Cross-Agent Learning** | Pattern helps multiple agents | Shared memory |
| **Knowledge Gap** | Repeated failures in area | Knowledge request |

### Detection Sources

| Source | Pattern Detection | KMO Role |
|--------|-------------------|----------|
| **COS** | Behavioral patterns | Primary source |
| **ARE** | Operational patterns | Secondary source |
| **User Feedback** | Correction patterns | Secondary source |
| **Agent Self-Report** | Learning candidates | Secondary source |

---

## Validation: Is the Pattern Promotable?

### Validation Criteria

Before promoting, KMO validates:

| Criterion | Question | Threshold |
|-----------|----------|-----------|
| **Frequency** | Is this pattern recurring? | 3+ occurrences |
| **Consistency** | Is the pattern stable? | 80%+ same result |
| **Correctness** | Is the pattern accurate? | Validated by expert |
| **Stability** | Is the pattern stable over time? | 7+ days stable |
| **Value** | Does promotion benefit agents? | Measurable improvement |
| **Risk** | Does promotion create risk? | Risk assessment passed |

### Validation Process

```yaml
pattern_validation:
  pattern_id: "pat-2026-01-13-xyz"
  
  detection:
    source: "COS"
    timestamp: "2026-01-13T10:00:00Z"
    occurrences: 15
    agents_involved: ["agent-a", "agent-b", "agent-c"]
  
  pattern_description: |
    When invoice amount exceeds $5000 and vendor is new,
    require manager approval regardless of matching PO.
  
  validation:
    frequency_check: "PASS - 15 occurrences"
    consistency_check: "PASS - 93% consistent"
    correctness_check: "PASS - Finance team validated"
    stability_check: "PASS - Stable for 14 days"
    value_check: "PASS - Reduces fraud risk"
    risk_check: "PASS - No compliance concerns"
  
  recommendation:
    promotion_level: "enterprise_knowledge"
    rationale: "Pattern represents validated business rule"
    requires_approval: ["KMO", "ARAO"]
```

---

## Approval: Who Decides?

### Approval Matrix

| Promotion Type | Approver | Rationale |
|----------------|----------|-----------|
| **Observation → Episodic** | Automatic (policy) | High volume, low risk |
| **Episodic → Semantic** | KMO | Curated sharing |
| **Semantic → Knowledge** | KMO + ARAO | Becomes authoritative |
| **Knowledge → SOP** | APO + ARAO | Changes business behavior |

### Approval Considerations

| Level | KMO Considers | ARAO Considers | APO Considers |
|-------|---------------|----------------|---------------|
| **Semantic** | Accuracy, usefulness | — | — |
| **Knowledge** | Accuracy, usefulness | Compliance impact | — |
| **SOP** | Accuracy, usefulness | Compliance impact | Business impact |

---

## Execution: How Promotion Happens

### Promotion Mechanisms

| From | To | Mechanism |
|------|-----|-----------|
| Observation | Episodic | CAF retention policy |
| Episodic | Semantic | KMO promotion action |
| Semantic | Knowledge | Knowledge base update |
| Knowledge | SOP | Policy system update |

### Promotion Record

Every promotion is recorded:

```yaml
promotion_record:
  id: "prm-2026-01-13-abc123"
  timestamp: "2026-01-13T14:00:00Z"
  
  pattern_id: "pat-2026-01-13-xyz"
  from_level: "semantic"
  to_level: "enterprise_knowledge"
  
  approved_by:
    - user: "kmo-user"
      role: "KMO"
      timestamp: "2026-01-13T12:00:00Z"
    - user: "arao-user"
      role: "ARAO"
      timestamp: "2026-01-13T13:00:00Z"
  
  promotion_details:
    knowledge_entry_id: "kb-2026-01-13-def456"
    scope: "all_invoice_agents"
    effective_date: "2026-01-14T00:00:00Z"
```

---

## Verification: Did It Work?

### Post-Promotion Verification

After promotion, COS verifies:

| Check | Method | Success Criteria |
|-------|--------|------------------|
| **Adoption** | Usage tracking | Agents use new knowledge |
| **Quality** | Decision quality | Quality maintained or improved |
| **No Regression** | Baseline comparison | No negative impact |
| **Conflict Detection** | Conflict analysis | No new conflicts |

### Verification Workflow

```
Pattern promoted
       ↓
Wait stabilization period (7 days)
       ↓
COS runs verification:
├── Is pattern being used?
├── Is decision quality maintained?
├── Any regressions detected?
└── Any new conflicts?
       ↓
Verification result:
├── SUCCESS → Pattern stays
├── PARTIAL → KMO adjusts
└── FAILURE → KMO rolls back
```

---

## Demotion and Correction

### When Demotion is Needed

| Situation | Action |
|-----------|--------|
| Learning found incorrect | Correct and maintain level |
| Learning no longer valid | Demote to lower level |
| Harmful pattern detected | Quarantine immediately |
| Time-based decay | Automatic expiration |

### Demotion Process

```yaml
demotion_record:
  id: "dem-2026-01-13-ghi789"
  timestamp: "2026-01-13T16:00:00Z"
  
  knowledge_entry_id: "kb-2026-01-13-def456"
  from_level: "enterprise_knowledge"
  to_level: "quarantine"
  
  reason: "Pattern found to cause incorrect approvals"
  evidence:
    - "COS report: 5 incorrect approvals in 3 days"
    - "User complaints: 3 customer escalations"
  
  action:
    immediate: "Quarantine knowledge entry"
    investigation: "KMO to investigate root cause"
    notification: "Notify affected agents"
```

---

## Platform Requirements

### Detection Integration

KMO needs:
- **COS Pattern Feed** — Receive flagged patterns from COS
- **Evidence Viewer** — See supporting evidence
- **Pattern Context** — Access to traces and decisions

### Validation Tools

KMO needs:
- **Validation Checklist** — Standard validation criteria
- **Expert Review Workflow** — Request expert validation
- **Risk Assessment Tool** — Evaluate promotion risk
- **Pattern Editor** — Refine patterns before promotion

### Approval Workflow

KMO needs:
- **Approval Queue** — Pending promotions
- **Multi-Approver Workflow** — Route to required approvers
- **Decision Tracking** — Track approval decisions
- **Escalation Path** — Handle approval delays

### Promotion Execution

KMO needs:
- **Promotion Action** — Execute promotion
- **Scope Selector** — Define which agents receive
- **Effective Date** — Schedule promotion
- **Rollback Capability** — Undo promotions

### Verification Integration

KMO needs:
- **Verification Dashboard** — Track post-promotion status
- **COS Verification Feed** — Receive verification results
- **Rollback Trigger** — Initiate rollback if needed

---

## OPDA Requirements Summary

| OPDA Dimension | KMO Need |
|----------------|----------|
| **Observable** | See patterns, promotions, and effects |
| **Predictable** | Promotions have predictable effects |
| **Directable** | KMO can promote, demote, quarantine |
| **Authority Enforceable** | Promotion requires appropriate approval |

---

## Desk Support

These needs are supported through the **Knowledge Governance Desk**:

| Console | Capabilities |
|---------|--------------|
| **Knowledge Console** | Source catalog, quality dashboard |
| **Memory Console** | Policy manager, memory browser, conflict detector |
| **Learning Console** | Promotion queue, promotion decisions, demotion manager |

See [Knowledge Governance Desk](../../ux-architecture/desks/knowledge-governance-desk/README.md) for detailed specifications.

---

## Anti-Patterns

| Pattern | Why It's Problematic |
|---------|---------------------|
| "Let agents learn freely" | Unvalidated learning is dangerous |
| "Promote everything" | Noise overwhelms signal |
| "Promote nothing" | Valuable patterns stay siloed |
| "Skip validation" | Bad patterns propagate |
| "Never demote" | Bad learnings persist |

---

## Success Criteria

KMO enterprise learning needs are met when:

- [ ] Patterns are detected and flagged by COS
- [ ] Validation criteria are applied consistently
- [ ] Approval workflow is followed
- [ ] Promotions are executed correctly
- [ ] Post-promotion verification is performed
- [ ] Demotions and corrections are possible
- [ ] Audit trail is complete

---

*End of document*
