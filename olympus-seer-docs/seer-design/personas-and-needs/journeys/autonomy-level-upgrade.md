# Journey: Autonomy Level Upgrade

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Priority:** High  
> **Frequency:** Medium  
> **Personas Involved:** APO, ARAO, ARE, COS

---

## Overview

This journey covers the process of upgrading an agent's autonomy level from a lower tier (e.g., L2 Supervised) to a higher tier (e.g., L3 Bounded Autonomous). It requires evidence gathering, risk assessment, and formal approval.

---

## Journey Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       AUTONOMY LEVEL UPGRADE JOURNEY                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   ASSESS    │───▶│   GATHER    │───▶│   PROPOSE   │───▶│   REVIEW    │  │
│  │ READINESS   │    │  EVIDENCE   │    │  UPGRADE    │    │  REQUEST    │  │
│  │   (APO)     │    │ (APO/COS)   │    │   (APO)     │    │   (ARAO)    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                 │                  │                  │          │
│         │ Eligibility     │ Performance      │ Formal           │ Risk     │
│         │ Check           │ Data             │ Submission       │ Analysis │
│         ▼                 ▼                  ▼                  ▼          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │  DECISION   │───▶│  IMPLEMENT  │───▶│  MONITOR    │───▶│   REVIEW    │  │
│  │   (ARAO)    │    │(APO/ARE/AE) │    │(ARE/COS)    │    │  PERIOD     │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Assess Readiness (APO)

**Desk:** [Agent Portfolio Desk](../../ux-architecture/desks/agent-portfolio-desk/README.md)  
**Console:** [Autonomy Console](../../ux-architecture/desks/agent-portfolio-desk/autonomy-console.md)

### Eligibility Criteria

| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| Time at current level | ≥ 90 days | Sufficient observation period |
| Accuracy rate | ≥ 99% | High decision quality |
| AHS score | ≥ 0.90 for 90 days | Operational stability |
| Incident count | 0 critical, ≤ 2 minor | No major issues |
| Human concordance | ≥ 98% | Decisions match human judgment |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 1.1 | Check eligibility criteria | Eligibility Report |
| 1.2 | Review business case | Business Justification |
| 1.3 | Assess organizational readiness | Readiness Assessment |
| 1.4 | Decide to proceed | Decision Record |

---

## Phase 2: Gather Evidence (APO, COS)

**Desks:** [Agent Portfolio Desk](../../ux-architecture/desks/agent-portfolio-desk/README.md), [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)

### Evidence Types

| Evidence | Source | Purpose |
|----------|--------|---------|
| Performance metrics | ARE Health Console | Operational track record |
| Quality metrics | COS Behavior Console | Reasoning quality |
| Human review concordance | APO Outcomes | Decision alignment |
| Incident history | ARE Incident Console | Issue frequency |
| Escalation patterns | COS Patterns Console | Appropriate escalations |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 2.1 | Export performance data | Performance Report |
| 2.2 | Export quality metrics | Quality Report |
| 2.3 | Calculate concordance rate | Concordance Analysis |
| 2.4 | Compile incident history | Incident Summary |
| 2.5 | Assemble evidence package | Evidence Bundle |

---

## Phase 3: Propose Upgrade (APO)

**Desk:** [Agent Portfolio Desk](../../ux-architecture/desks/agent-portfolio-desk/README.md)  
**Console:** [Autonomy Console](../../ux-architecture/desks/agent-portfolio-desk/autonomy-console.md)

### Proposal Contents

```
## Autonomy Upgrade Proposal

### Agent Information
- Agent: [name]
- Class: [class]
- Current Level: [L2 Supervised]
- Requested Level: [L3 Bounded Autonomous]

### Business Justification
[Why upgrade is needed]

### Evidence Summary
- Accuracy: [X]%
- AHS: [X] (90-day avg)
- Concordance: [X]%
- Incidents: [X] total

### Risk Mitigation
- Escalation rules: [rules]
- Monitoring plan: [plan]
- Rollback trigger: [triggers]
```

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 3.1 | Draft proposal | Proposal Document |
| 3.2 | Define updated escalation rules | Escalation Config |
| 3.3 | Define rollback triggers | Rollback Plan |
| 3.4 | Submit to ARAO | Submission Record |

---

## Phase 4: Review Request (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Autonomy Console](../../ux-architecture/desks/agent-compliance-desk/autonomy-console.md)

### Review Checklist

- [ ] Evidence meets minimum thresholds
- [ ] Business justification is valid
- [ ] Escalation rules are appropriate
- [ ] Rollback plan is actionable
- [ ] No outstanding compliance concerns
- [ ] Risk level acceptable

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 4.1 | Review evidence package | Review Notes |
| 4.2 | Assess risk level | Risk Assessment |
| 4.3 | Verify escalation rules | Rule Validation |
| 4.4 | Consult with ARE if needed | Consultation |
| 4.5 | Prepare decision | Decision Draft |

---

## Phase 5: Decision (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Autonomy Console](../../ux-architecture/desks/agent-compliance-desk/autonomy-console.md)

### Decision Options

| Decision | Meaning | Next Steps |
|----------|---------|------------|
| **Approve** | Upgrade approved as requested | Proceed to implementation |
| **Approve with Conditions** | Approved with additional requirements | APO addresses conditions, then implement |
| **Defer** | Not yet ready, gather more evidence | Return to Phase 2 |
| **Deny** | Upgrade not appropriate | Document rationale |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 5.1 | Make decision | Decision Record |
| 5.2 | Document rationale | Rationale Document |
| 5.3 | Define conditions (if any) | Conditions List |
| 5.4 | Notify APO | Notification |

---

## Phase 6: Implement (APO, ARE, AE)

**Desks:** Multiple

### Activities

| Step | Action | Responsible | Console |
|------|--------|-------------|---------|
| 6.1 | Update autonomy configuration | AE | Development Console |
| 6.2 | Update escalation rules | AE | Development Console |
| 6.3 | Update authority boundaries | ARAO | Security Console |
| 6.4 | Deploy configuration | AE | Release Console |
| 6.5 | Verify deployment | ARE | Health Console |

---

## Phase 7: Monitor (ARE, COS)

**Desks:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md), [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)

### Monitoring Focus

| Aspect | Metric | Threshold |
|--------|--------|-----------|
| Error rate | Errors / Total | < 2% |
| Escalation rate | Appropriate escalations | Within expected |
| Authority violations | Blocked attempts | 0 |
| Decision quality | Accuracy | ≥ 99% |

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 7.1 | Enhanced monitoring period (30 days) | ARE, COS |
| 7.2 | Daily health checks | ARE |
| 7.3 | Weekly quality reviews | COS |
| 7.4 | Report any concerns | ARE/COS → APO |

---

## Phase 8: Review Period

### 30-Day Review

At the end of the monitoring period:

| Step | Action | Responsible |
|------|--------|-------------|
| 8.1 | Compile monitoring report | ARE |
| 8.2 | Assess against expectations | APO, ARAO |
| 8.3 | Decide: Continue or Rollback | ARAO |

### Rollback Triggers

- Error rate exceeds 2%
- Critical incident occurs
- Authority violation detected
- Significant behavioral drift

---

## OPDA Alignment

| Property | Journey Relevance |
|----------|-------------------|
| **Observable** | Evidence gathering requires observability |
| **Predictable** | Upgrade maintains predictability through rules |
| **Directable** | Escalation rules enable direction |
| **Authority** | Core journey for authority management |

---

## Success Criteria

- [ ] Eligibility criteria met
- [ ] Evidence package complete
- [ ] ARAO approval obtained
- [ ] Configuration deployed
- [ ] 30-day monitoring period successful
- [ ] No rollback required

---

*Autonomy upgrades represent increased trust in AI agents and must be earned through demonstrated performance.*
