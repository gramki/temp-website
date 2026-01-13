# Journey: Behavioral Drift Investigation

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Priority:** High  
> **Frequency:** Medium  
> **Personas Involved:** COS, AE, CSA, KMO

---

## Overview

This journey covers the investigation and resolution of behavioral drift — when an agent's behavior deviates significantly from its established baseline. Drift can indicate prompt degradation, knowledge staleness, or design issues.

---

## Journey Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BEHAVIORAL DRIFT INVESTIGATION JOURNEY                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   DETECT    │───▶│  QUANTIFY   │───▶│   ANALYZE   │───▶│  CLASSIFY   │  │
│  │   (COS)     │    │   (COS)     │    │   (COS)     │    │   (COS)     │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                 │                  │                  │          │
│         │ Drift           │ Impact           │ Root Cause       │ Category │
│         │ Alert           │ Assessment       │ Hypothesis       │ & Route  │
│         ▼                 ▼                  ▼                  ▼          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │ INVESTIGATE │───▶│   RESOLVE   │───▶│   VERIFY    │───▶│  BASELINE   │  │
│  │(AE/CSA/KMO) │    │(AE/CSA/KMO) │    │   (COS)     │    │  UPDATE     │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Detect (COS)

**Desk:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)  
**Console:** [Patterns Console](../../ux-architecture/desks/cognitive-health-desk/patterns-console.md)

### Drift Detection Types

| Metric | Detection Method | Alert Threshold |
|--------|-----------------|-----------------|
| Approval rate | Rolling average | > 10% change |
| Rejection rate | Rolling average | > 10% change |
| Escalation rate | Rolling average | > 15% change |
| Avg confidence | Rolling average | > 5% decrease |
| Processing time | Rolling average | > 25% increase |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 1.1 | Drift alert triggered | Alert Record |
| 1.2 | Acknowledge alert | Acknowledgment |
| 1.3 | Initial assessment | Assessment Notes |

---

## Phase 2: Quantify (COS)

**Desk:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)  
**Console:** [Patterns Console](../../ux-architecture/desks/cognitive-health-desk/patterns-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 2.1 | Compare baseline vs current | Comparison Report |
| 2.2 | Measure drift magnitude | Drift Metrics |
| 2.3 | Identify affected time period | Timeline |
| 2.4 | Assess business impact | Impact Assessment |

### Drift Magnitude Scale

| Level | Magnitude | Urgency |
|-------|-----------|---------|
| Minor | < 10% | Low |
| Moderate | 10-25% | Medium |
| Significant | 25-50% | High |
| Severe | > 50% | Critical |

---

## Phase 3: Analyze (COS)

**Desk:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)  
**Console:** [Behavior Console](../../ux-architecture/desks/cognitive-health-desk/behavior-console.md)

### Analysis Activities

| Step | Action | Artifact |
|------|--------|----------|
| 3.1 | Sample drifted decisions | Sample Set |
| 3.2 | Compare traces before/after | Trace Comparison |
| 3.3 | Identify pattern changes | Pattern Analysis |
| 3.4 | Correlate with events | Correlation Analysis |

### Potential Correlations

| Event Type | Source | Example |
|------------|--------|---------|
| Prompt update | AE Release Console | v2.3.0 deployed Jan 10 |
| Knowledge update | KMO Knowledge Console | Policy docs refreshed Jan 8 |
| Tool change | AE Development Console | New API version Jan 9 |
| External change | Various | Upstream data format changed |

---

## Phase 4: Classify & Route (COS)

**Desk:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)  
**Console:** [Issues Console](../../ux-architecture/desks/cognitive-health-desk/issues-console.md)

### Classification Categories

| Category | Description | Route To |
|----------|-------------|----------|
| **Prompt Drift** | Prompt changes caused issue | AE |
| **Knowledge Drift** | Knowledge staleness or errors | KMO |
| **Design Drift** | Pattern no longer appropriate | CSA |
| **Tool Drift** | Tool behavior changed | AE |
| **External Drift** | External factors changed | AE + APO |
| **Model Drift** | Model behavior changed | AE + CSA |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 4.1 | Classify drift category | Classification |
| 4.2 | Create issue ticket | Issue Record |
| 4.3 | Route to appropriate team | Routing |
| 4.4 | Provide evidence package | Evidence Bundle |

---

## Phase 5: Investigate (AE, CSA, KMO)

Depending on classification:

### Prompt Drift Investigation (AE)

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)

| Step | Action | Console |
|------|--------|---------|
| 5.1a | Compare prompt versions | Development Console |
| 5.1b | Replay scenarios | Test Console |
| 5.1c | Identify problematic change | Development Console |

### Knowledge Drift Investigation (KMO)

**Desk:** [Knowledge Governance Desk](../../ux-architecture/desks/knowledge-governance-desk/README.md)

| Step | Action | Console |
|------|--------|---------|
| 5.2a | Check source freshness | Knowledge Console |
| 5.2b | Verify knowledge accuracy | Knowledge Console |
| 5.2c | Identify stale/incorrect entries | Knowledge Console |

### Design Drift Investigation (CSA)

**Desk:** [Agent Design Desk](../../ux-architecture/desks/agent-design-desk/README.md)

| Step | Action | Console |
|------|--------|---------|
| 5.3a | Review pattern applicability | Design Console |
| 5.3b | Check constraint coverage | Design Console |
| 5.3c | Assess design evolution needs | Validation Console |

---

## Phase 6: Resolve

### Resolution Options

| Category | Resolution | Owner |
|----------|------------|-------|
| Prompt Drift | Prompt fix + test | AE |
| Knowledge Drift | Source refresh/correction | KMO |
| Design Drift | Design update | CSA → AE |
| Tool Drift | Tool binding fix | AE |
| External Drift | Adaptation or escalation | AE + APO |

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 6.1 | Develop fix | AE/KMO/CSA |
| 6.2 | Test fix | AE |
| 6.3 | Deploy fix | AE |
| 6.4 | Notify COS | AE |

---

## Phase 7: Verify (COS)

**Desk:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)  
**Console:** [Behavior Console](../../ux-architecture/desks/cognitive-health-desk/behavior-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 7.1 | Monitor post-fix behavior | Monitoring Report |
| 7.2 | Compare to baseline | Comparison |
| 7.3 | Confirm drift resolved | Resolution Confirmation |
| 7.4 | Close issue | Closure Record |

### Verification Criteria

- Metrics return to baseline ± 5%
- No new anomalies detected
- Sample decisions match expectations

---

## Phase 8: Baseline Update

**Desk:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)  
**Console:** [Patterns Console](../../ux-architecture/desks/cognitive-health-desk/patterns-console.md)

### Decision: Baseline Adjustment

| Scenario | Action |
|----------|--------|
| Drift was bug → fixed | Keep original baseline |
| Drift reflects valid change | Update baseline |
| Mixed scenario | Partial baseline update |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 8.1 | Assess baseline applicability | Assessment |
| 8.2 | Update baseline if needed | Baseline Config |
| 8.3 | Document rationale | Documentation |

---

## OPDA Alignment

| Property | Journey Relevance |
|----------|-------------------|
| **Observable** | Drift detection requires observability |
| **Predictable** | Baseline comparison enables prediction |
| **Directable** | Resolution restores intended behavior |
| **Authority** | N/A (cognitive health focus) |

---

## Success Criteria

- [ ] Drift detected and acknowledged
- [ ] Magnitude quantified
- [ ] Root cause identified
- [ ] Appropriate team engaged
- [ ] Fix developed and tested
- [ ] Drift resolved
- [ ] Baseline updated if appropriate
- [ ] Issue closed

---

*Behavioral drift investigation is essential for maintaining cognitive health and trust in AI agents.*
