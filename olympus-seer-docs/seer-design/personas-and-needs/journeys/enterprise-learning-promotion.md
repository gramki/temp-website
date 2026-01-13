# Journey: Enterprise Learning Promotion

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Priority:** High  
> **Frequency:** Medium  
> **Personas Involved:** COS, KMO, APO

---

## Overview

This journey covers the process of promoting learnings from individual agent interactions to higher levels of the memory hierarchy — from agent instance memory to agent class memory, and ultimately to enterprise memory. This enables organizational learning from AI agent operations.

---

## Journey Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE LEARNING PROMOTION JOURNEY                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LEVEL 1 (Agent Instance)                                                   │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                     │
│  │   LEARN     │───▶│   REUSE     │───▶│    FLAG     │                     │
│  │   (Agent)   │    │   (Agent)   │    │   (COS)     │                     │
│  └─────────────┘    └─────────────┘    └─────────────┘                     │
│         │                 │                  │                              │
│         │ Interaction     │ Pattern          │ Promotion                    │
│         │ Memory          │ Emerges          │ Candidate                    │
│         ▼                 ▼                  ▼                              │
│  LEVEL 2 (Agent Class)                                                      │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                     │
│  │   REVIEW    │───▶│   PROMOTE   │───▶│   SHARE     │                     │
│  │   (KMO)     │    │   (KMO)     │    │ (All Class) │                     │
│  └─────────────┘    └─────────────┘    └─────────────┘                     │
│         │                 │                  │                              │
│         │ Validation      │ L1→L2            │ Class                        │
│         │ Review          │ Promotion        │ Distribution                 │
│         ▼                 ▼                  ▼                              │
│  LEVEL 3 (Enterprise)                                                       │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                     │
│  │   REVIEW    │───▶│   PROMOTE   │───▶│   PUBLISH   │                     │
│  │   (KMO)     │    │   (KMO)     │    │(Enterprise) │                     │
│  └─────────────┘    └─────────────┘    └─────────────┘                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Memory Hierarchy Overview

| Level | Name | Scope | Governance |
|-------|------|-------|------------|
| L1 | Agent Instance Memory | Individual agent | Agent |
| L2 | Agent Class Memory | All agents of type | APO + KMO |
| L3 | Enterprise Memory | All agents | KMO |

---

## Phase 1: Learning Emergence (Agent)

### How Agents Learn

| Learning Type | Source | Example |
|---------------|--------|---------|
| Task patterns | Repeated tasks | Invoice validation shortcuts |
| Error recovery | Failed attempts | Retry strategies |
| User preferences | Feedback | Formatting preferences |
| Domain knowledge | Tool responses | Vendor categorizations |

### Automatic Capture

Agents automatically capture learnings when:
- A pattern is reused 3+ times successfully
- Human feedback improves outcomes
- Error recovery succeeds

---

## Phase 2: Pattern Flagging (COS)

**Desk:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)  
**Console:** [Patterns Console](../../ux-architecture/desks/cognitive-health-desk/patterns-console.md)

### Detection Criteria

| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| Reuse count | ≥ 25 | Significant pattern |
| Success rate | ≥ 95% | Reliable pattern |
| Cross-instance validation | ≥ 2 agents | Not agent-specific |
| Age | ≥ 7 days | Stable pattern |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 2.1 | Detect promotion candidate | Detection Record |
| 2.2 | Validate criteria met | Validation Check |
| 2.3 | Flag for KMO review | Flag Record |
| 2.4 | Assemble evidence | Evidence Package |

---

## Phase 3: L1→L2 Review (KMO)

**Desk:** [Knowledge Governance Desk](../../ux-architecture/desks/knowledge-governance-desk/README.md)  
**Console:** [Learning Console](../../ux-architecture/desks/knowledge-governance-desk/learning-console.md)

### Review Checklist

- [ ] Learning is accurate and correct
- [ ] Learning is generalizable to agent class
- [ ] No contradictions with existing class memory
- [ ] No compliance or security concerns
- [ ] Provenance is clear and traceable

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 3.1 | Review learning content | Review Notes |
| 3.2 | Verify accuracy | Accuracy Check |
| 3.3 | Check for contradictions | Contradiction Report |
| 3.4 | Make promotion decision | Decision Record |

### Decision Options

| Decision | Outcome |
|----------|---------|
| **Approve** | Promote to L2 |
| **Edit & Approve** | Modify and promote |
| **Reject** | Document reason, do not promote |
| **Defer** | Request more evidence |

---

## Phase 4: L2 Promotion & Distribution (KMO)

**Desk:** [Knowledge Governance Desk](../../ux-architecture/desks/knowledge-governance-desk/README.md)  
**Console:** [Learning Console](../../ux-architecture/desks/knowledge-governance-desk/learning-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 4.1 | Promote to L2 memory | Promotion Record |
| 4.2 | Configure distribution | Distribution Config |
| 4.3 | Distribute to agent class | Distribution Record |
| 4.4 | Monitor adoption | Adoption Metrics |

### Distribution Configuration

```yaml
learning_id: learn-2026-0113-001
target_level: L2
target_class: expense-approver
distribution:
  mode: immediate  # or staged
  scope: all_instances
notification:
  apo: true
  ae: true
```

---

## Phase 5: L2→L3 Eligibility

A learning becomes eligible for L3 (Enterprise) promotion when:

| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| L2 usage | ≥ 100 uses | Widely applicable |
| Success rate | ≥ 97% | Higher bar for enterprise |
| Cross-class validation | ≥ 2 classes | Not class-specific |
| L2 age | ≥ 30 days | Proven stable |

---

## Phase 6: L2→L3 Review (KMO)

**Desk:** [Knowledge Governance Desk](../../ux-architecture/desks/knowledge-governance-desk/README.md)  
**Console:** [Learning Console](../../ux-architecture/desks/knowledge-governance-desk/learning-console.md)

### Enhanced Review

L3 promotion requires more rigorous review:

- [ ] Cross-class applicability verified
- [ ] No domain-specific dependencies
- [ ] Compliance review (for regulated domains)
- [ ] APO notification (for business impact)
- [ ] Contradiction check against enterprise memory

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 6.1 | Review for enterprise applicability | Review Notes |
| 6.2 | Verify cross-class usage | Usage Report |
| 6.3 | Complete compliance review | Compliance Check |
| 6.4 | Notify APOs of impacted agents | Notification |
| 6.5 | Make promotion decision | Decision Record |

---

## Phase 7: L3 Publication (KMO)

**Desk:** [Knowledge Governance Desk](../../ux-architecture/desks/knowledge-governance-desk/README.md)  
**Console:** [Learning Console](../../ux-architecture/desks/knowledge-governance-desk/learning-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 7.1 | Promote to L3 memory | Promotion Record |
| 7.2 | Publish to all agents | Publication Record |
| 7.3 | Update knowledge graph | Graph Update |
| 7.4 | Notify enterprise | Notification |

### Publication Announcement

```
ENTERPRISE LEARNING PUBLISHED

Learning: Receipt validation pattern for meals
Source: expense-approver class
Promoted: 2026-01-13

Summary: When validating meal receipts, check date 
matches expense date ±1 day, verify vendor is 
food-related, confirm total within $0.10 tolerance.

Applicability: All agents processing expense claims

Provenance: Derived from 45 reuses across 3 expense-
approver instances with 98.2% success rate.
```

---

## Monitoring & Feedback

### Post-Promotion Monitoring

| Metric | Monitor Period | Alert Threshold |
|--------|----------------|-----------------|
| Usage rate | 30 days | < expected adoption |
| Success rate | 30 days | < 95% |
| Contradiction reports | Ongoing | Any |
| Negative feedback | Ongoing | Any |

### Demotion Process

If a promoted learning proves problematic:

| Step | Action | Responsible |
|------|--------|-------------|
| D.1 | Detect issue | COS |
| D.2 | Quarantine learning | KMO |
| D.3 | Investigate | KMO + AE |
| D.4 | Demote or fix | KMO |
| D.5 | Notify affected parties | KMO |

---

## OPDA Alignment

| Property | Journey Relevance |
|----------|-------------------|
| **Observable** | Learning provenance tracked |
| **Predictable** | Promotion criteria are explicit |
| **Directable** | KMO controls promotion |
| **Authority** | Governance at each level |

---

## Success Criteria

- [ ] Learning candidate identified
- [ ] Criteria thresholds met
- [ ] KMO review completed
- [ ] No contradictions detected
- [ ] Promotion executed
- [ ] Distribution confirmed
- [ ] Post-promotion monitoring stable

---

*Enterprise learning promotion enables organizations to capture and share knowledge from AI agent operations.*
