# Journey: Agent Incident Response

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Priority:** Critical  
> **Frequency:** Medium  
> **Personas Involved:** ARE, COS, AE, APO

---

## Overview

This journey covers the end-to-end incident response process when an agent experiences operational or cognitive issues. It emphasizes rapid containment, root cause identification, and coordinated resolution across personas.

---

## Journey Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       AGENT INCIDENT RESPONSE JOURNEY                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   DETECT    │───▶│   CONTAIN   │───▶│ INVESTIGATE │───▶│   RESOLVE   │  │
│  │ (ARE/COS)   │    │   (ARE)     │    │(COS/AE/CSA) │    │   (AE)      │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                 │                  │                  │          │
│         │ Alert           │ Containment      │ Root Cause       │ Fix      │
│         │ Triggered       │ Action           │ Analysis         │ Deploy   │
│         ▼                 ▼                  ▼                  ▼          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   VERIFY    │───▶│   NOTIFY    │───▶│    PIR      │───▶│  IMPROVE    │  │
│  │   (ARE)     │    │   (APO)     │    │(ARE/AE/COS) │    │ (All)       │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Detect

**Desks:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md), [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)

### Trigger Types

| Type | Source | Example |
|------|--------|---------|
| **Health Alert** | ARE Health Console | AHS drops below 0.75 |
| **SLA Breach** | ARE Health Console | P95 latency exceeds target |
| **Cognitive Anomaly** | COS Behavior Console | Hallucination detected |
| **Drift Alert** | COS Patterns Console | Approval rate drift >10% |
| **Error Spike** | ARE Health Console | Error rate exceeds 2% |

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 1.1 | Alert triggered | System |
| 1.2 | Acknowledge alert | ARE or COS |
| 1.3 | Assess severity | ARE |
| 1.4 | Create incident | ARE |

---

## Phase 2: Contain

**Desk:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md)  
**Console:** [Control Console](../../ux-architecture/desks/agent-operations-desk/control-console.md)

### Containment Actions

| Severity | Action | Impact |
|----------|--------|--------|
| **Critical** | Kill agent | Full stop |
| **High** | Pause + throttle | No new tasks |
| **Medium** | Throttle to 25% | Reduced capacity |
| **Low** | Monitor closely | No immediate action |

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 2.1 | Select containment action | Action Log |
| 2.2 | Execute containment | Control Record |
| 2.3 | Verify containment effective | Status Check |
| 2.4 | Consider rollback if needed | Rollback (optional) |

---

## Phase 3: Investigate

**Desks:** [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md), [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)

### Activities

| Step | Action | Responsible | Console |
|------|--------|-------------|---------|
| 3.1 | Analyze traces | COS | Behavior Console |
| 3.2 | Check for drift | COS | Patterns Console |
| 3.3 | Identify root cause category | COS | Issues Console |
| 3.4 | Route to appropriate team | COS | Issues Console |
| 3.5 | Deep technical investigation | AE/CSA | Dev Console / Design Console |
| 3.6 | Scenario replay | AE | Test Console |

### Root Cause Categories

| Category | Route To | Example |
|----------|----------|---------|
| **Prompt Issue** | AE | Ambiguous instructions |
| **Tool Failure** | AE | API timeout |
| **Design Flaw** | CSA | Pattern mismatch |
| **Knowledge Gap** | KMO | Stale information |
| **Infrastructure** | Hub ARE | Compute issues |
| **Authority Violation** | ARAO | Exceeded bounds |

---

## Phase 4: Resolve

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)  
**Console:** [Development Console](../../ux-architecture/desks/agent-development-desk/development-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 4.1 | Develop fix | Code/Prompt Change |
| 4.2 | Test fix | Test Results |
| 4.3 | Create hotfix version | Version |
| 4.4 | Deploy fix | Deployment |
| 4.5 | Verify resolution | Health Check |

### OR: Rollback

| Step | Action | Console |
|------|--------|---------|
| 4.1 | Select rollback target | Release Console |
| 4.2 | Execute rollback | Control Console |
| 4.3 | Verify rollback | Health Console |

---

## Phase 5: Verify & Notify

**Desks:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md), [Agent Portfolio Desk](../../ux-architecture/desks/agent-portfolio-desk/README.md)

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 5.1 | Verify agent health restored | ARE |
| 5.2 | Resume normal operations | ARE |
| 5.3 | Notify stakeholders | ARE/APO |
| 5.4 | Update incident status | ARE |

---

## Phase 6: Post-Incident Review (PIR)

**Desk:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md)  
**Console:** [Incident Console](../../ux-architecture/desks/agent-operations-desk/incident-console.md)

### Activities

| Step | Action | Participants |
|------|--------|-------------|
| 6.1 | Schedule PIR meeting | ARE |
| 6.2 | Document timeline | ARE |
| 6.3 | Identify root cause | AE, COS, CSA |
| 6.4 | Identify contributing factors | All |
| 6.5 | Define action items | All |
| 6.6 | Publish PIR | ARE |

### PIR Template

```
## Incident Summary
- ID: INC-YYYY-NNN
- Duration: X hours Y minutes
- Severity: P1/P2/P3
- Impact: [description]

## Timeline
[chronological events]

## Root Cause
[detailed root cause]

## Contributing Factors
- [factor 1]
- [factor 2]

## Action Items
- [ ] [action] - [owner] - [due date]
```

---

## Phase 7: Improve

**All Desks**

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 7.1 | Implement preventive actions | Various |
| 7.2 | Update runbooks | ARE |
| 7.3 | Update tests | AE |
| 7.4 | Update baselines | COS |
| 7.5 | Consider design improvements | CSA |

---

## Timing Expectations

| Phase | Target Duration | Critical Incidents |
|-------|-----------------|-------------------|
| Detect | < 5 minutes | Automated |
| Contain | < 15 minutes | < 5 minutes |
| Investigate | < 2 hours | < 30 minutes |
| Resolve | < 4 hours | < 1 hour |
| PIR | < 5 business days | < 48 hours |

---

## OPDA During Incidents

| Property | Incident Relevance |
|----------|-------------------|
| **Observable** | Trace analysis critical for investigation |
| **Predictable** | Baseline comparison reveals drift |
| **Directable** | Kill switch, throttle, rollback enable containment |
| **Authority** | Incident may reveal authority violations |

---

## Success Criteria

- [ ] Alert acknowledged within SLA
- [ ] Containment action executed appropriately
- [ ] Root cause identified
- [ ] Resolution deployed or rollback completed
- [ ] Agent health restored
- [ ] PIR completed with action items
- [ ] Preventive measures implemented

---

*Incident response is the critical path to maintaining trust in AI agents.*
