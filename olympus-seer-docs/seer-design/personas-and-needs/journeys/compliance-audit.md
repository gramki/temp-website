# Journey: Agent Compliance Audit

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Priority:** High  
> **Frequency:** Low (scheduled)  
> **Personas Involved:** ARAO, APO, ARE, COS, AE

---

## Overview

This journey covers the process of conducting a compliance audit of AI agents — ensuring they operate within approved autonomy levels, follow policies, and maintain audit-ready evidence. Audits may be scheduled (periodic) or triggered (event-based).

---

## Journey Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        COMPLIANCE AUDIT JOURNEY                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   PLAN      │───▶│   GATHER    │───▶│   ASSESS    │───▶│   REPORT    │  │
│  │   (ARAO)    │    │  (ARAO)     │    │   (ARAO)    │    │   (ARAO)    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                 │                  │                  │          │
│         │ Scope &         │ Evidence         │ Compliance       │ Findings │
│         │ Schedule        │ Collection       │ Assessment       │ & Recs   │
│         ▼                 ▼                  ▼                  ▼          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │  REMEDIATE  │───▶│   VERIFY    │───▶│   CLOSE     │───▶│   ARCHIVE   │  │
│  │(APO/AE/ARE) │    │   (ARAO)    │    │   (ARAO)    │    │   (ARAO)    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Audit Types

| Type | Frequency | Trigger |
|------|-----------|---------|
| **Periodic** | Quarterly/Annual | Schedule |
| **Pre-Release** | Per major release | Release gate |
| **Incident** | As needed | Significant incident |
| **External** | Annual | Regulatory requirement |
| **Autonomy Change** | Per request | Autonomy upgrade |

---

## Phase 1: Plan (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Compliance Console](../../ux-architecture/desks/agent-compliance-desk/compliance-console.md)

### Audit Planning

| Element | Description |
|---------|-------------|
| Scope | Which agents/domains |
| Period | Time range under review |
| Focus Areas | Specific compliance domains |
| Evidence Requirements | What evidence needed |
| Timeline | Audit schedule |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 1.1 | Define audit scope | Scope Document |
| 1.2 | Identify focus areas | Focus Areas List |
| 1.3 | Define evidence requirements | Evidence Checklist |
| 1.4 | Schedule activities | Audit Calendar |
| 1.5 | Notify stakeholders | Notification |

### Sample Audit Scope

```
COMPLIANCE AUDIT PLAN

Audit ID: AUD-2026-Q1-001
Type: Quarterly Periodic
Period: Oct 1, 2025 - Dec 31, 2025

Scope:
- All production agents (45)
- All autonomy levels

Focus Areas:
- Authority boundary compliance
- Escalation rule adherence
- Decision audit trail completeness
- OPDA property verification

Timeline:
- Evidence gathering: Jan 6-10
- Assessment: Jan 13-17
- Report: Jan 20
- Remediation: Jan 20 - Feb 7
```

---

## Phase 2: Gather Evidence (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Compliance Console](../../ux-architecture/desks/agent-compliance-desk/compliance-console.md)

### Evidence Sources

| Evidence Type | Source | Console |
|---------------|--------|---------|
| Agent inventory | APO | Portfolio Console |
| Autonomy levels | ARAO | Autonomy Console |
| Authority violations | ARAO | Security Console |
| Decision audit trails | ARAO | Compliance Console |
| Health metrics | ARE | Health Console |
| Cognitive quality | COS | Behavior Console |
| Incident history | ARE | Incident Console |
| Change history | AE | Release Console |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 2.1 | Export agent inventory | Inventory Report |
| 2.2 | Export autonomy assignments | Autonomy Report |
| 2.3 | Export violation log | Violation Report |
| 2.4 | Sample decision audit trails | Decision Samples |
| 2.5 | Export incident history | Incident Report |
| 2.6 | Generate compliance report | Compliance Data |

### Evidence Package

```yaml
evidence_package:
  audit_id: AUD-2026-Q1-001
  generated: 2026-01-10T15:00:00Z
  contents:
    - agent_inventory.xlsx
    - autonomy_assignments.xlsx
    - violation_log.xlsx
    - decision_samples/  # 100 sampled decisions
    - incident_history.xlsx
    - compliance_metrics.xlsx
    - change_log.xlsx
```

---

## Phase 3: Assess (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Compliance Console](../../ux-architecture/desks/agent-compliance-desk/compliance-console.md)

### Assessment Areas

| Area | Criteria | Weight |
|------|----------|--------|
| **Authority Compliance** | No violations, appropriate boundaries | 25% |
| **Escalation Adherence** | Escalations triggered correctly | 20% |
| **Audit Trail Completeness** | All decisions have trails | 20% |
| **OPDA Verification** | All properties maintained | 15% |
| **Policy Compliance** | No policy violations | 15% |
| **Incident Response** | Incidents handled properly | 5% |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 3.1 | Review authority compliance | Assessment Notes |
| 3.2 | Verify escalation adherence | Assessment Notes |
| 3.3 | Check audit trail completeness | Completeness Score |
| 3.4 | Verify OPDA properties | OPDA Checklist |
| 3.5 | Check policy compliance | Policy Check |
| 3.6 | Review incident handling | Incident Review |
| 3.7 | Calculate overall score | Compliance Score |

### Compliance Scoring

| Score | Rating | Status |
|-------|--------|--------|
| 95-100% | Excellent | Full compliance |
| 85-94% | Good | Minor issues |
| 70-84% | Needs Improvement | Significant issues |
| < 70% | Unsatisfactory | Critical issues |

---

## Phase 4: Report (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Compliance Console](../../ux-architecture/desks/agent-compliance-desk/compliance-console.md)

### Report Structure

```
COMPLIANCE AUDIT REPORT

1. Executive Summary
   - Scope and period
   - Overall rating
   - Key findings

2. Compliance Assessment
   - Authority compliance
   - Escalation adherence
   - Audit trail completeness
   - OPDA verification
   - Policy compliance

3. Findings
   - Finding 1: [description, severity, agent(s)]
   - Finding 2: ...

4. Recommendations
   - Recommendation 1: [description, owner, deadline]
   - Recommendation 2: ...

5. Evidence Index
   - List of supporting evidence

6. Appendices
   - Detailed data tables
```

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 4.1 | Draft report | Report Draft |
| 4.2 | Review with stakeholders | Reviewed Report |
| 4.3 | Finalize report | Final Report |
| 4.4 | Distribute to stakeholders | Distribution Record |

---

## Phase 5: Remediate (APO, AE, ARE)

### Finding Severity Levels

| Severity | SLA | Example |
|----------|-----|---------|
| Critical | 7 days | Authority violation detected |
| High | 14 days | Incomplete audit trails |
| Medium | 30 days | Escalation timing issue |
| Low | 60 days | Documentation gaps |

### Remediation Ownership

| Finding Category | Owner |
|-----------------|-------|
| Authority boundary | ARAO + AE |
| Escalation rules | AE + APO |
| Audit trail | AE |
| OPDA properties | AE + CSA |
| Policy configuration | ARAO |
| Operational | ARE |

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 5.1 | Create remediation tickets | ARAO |
| 5.2 | Assign owners | ARAO |
| 5.3 | Execute remediation | Various |
| 5.4 | Document completion | Owner |

---

## Phase 6: Verify (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Compliance Console](../../ux-architecture/desks/agent-compliance-desk/compliance-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 6.1 | Verify each remediation | Verification Record |
| 6.2 | Re-assess if needed | Re-assessment |
| 6.3 | Confirm closure criteria | Closure Check |
| 6.4 | Document verification | Verification Log |

---

## Phase 7: Close & Archive (ARAO)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 7.1 | Confirm all findings addressed | Closure Confirmation |
| 7.2 | Update compliance status | Status Update |
| 7.3 | Archive audit package | Archive Record |
| 7.4 | Schedule next audit | Next Audit Plan |

### Archive Contents

```
audit-2026-q1-001/
├── plan.md
├── evidence/
│   ├── agent_inventory.xlsx
│   ├── autonomy_assignments.xlsx
│   └── ...
├── assessment/
│   ├── assessment_notes.md
│   └── scoring.xlsx
├── report/
│   └── final_report.pdf
├── remediation/
│   ├── tickets.xlsx
│   └── verification.xlsx
└── closure.md
```

---

## OPDA in Audits

| Property | Audit Verification |
|----------|-------------------|
| **Observable** | Trace availability, audit trail completeness |
| **Predictable** | Behavior within baselines, constraint adherence |
| **Directable** | Kill switch tested, controls documented |
| **Authority** | No violations, appropriate escalations |

---

## Success Criteria

- [ ] Audit plan approved
- [ ] Evidence collected completely
- [ ] Assessment completed
- [ ] Report published
- [ ] Findings assigned
- [ ] Remediations completed
- [ ] Verifications passed
- [ ] Audit archived

---

*Compliance audits ensure that AI agents operate within governance frameworks and maintain organizational trust.*
