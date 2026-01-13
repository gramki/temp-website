# Cognitive Health Desk

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Primary Persona:** [Cognitive Operations Steward (COS)](../../../personas-and-needs/roles.md#6-cognitive-operations-steward-cos)  
> **Related:** [COS Reference](../../../personas-and-needs/cos.md) | [COS Needs](../../../personas-and-needs/needs/cos-behavioral-monitoring.md)

---

## Purpose

The Cognitive Health Desk is the primary workspace for the **Cognitive Operations Steward (COS)** ([role definition](../../../personas-and-needs/roles.md#6-cognitive-operations-steward-cos)). It provides capabilities to:

- Monitor cognitive quality across agents
- Detect drift, anomalies, and confusion
- Route issues to appropriate owners
- Flag patterns for enterprise learning

---

## Consoles

| Console | Purpose | Documentation |
|---------|---------|---------------|
| **Behavior Console** | Quality signals, consistency, confidence | [behavior-console.md](./behavior-console.md) |
| **Patterns Console** | Drift, anomalies, learning candidates | [patterns-console.md](./patterns-console.md) |
| **Issues Console** | Issue triage and handoff | [issues-console.md](./issues-console.md) |

---

## Key Journeys

| Journey | Description | Consoles Used |
|---------|-------------|---------------|
| **Drift Investigation** | Investigate detected drift, determine cause | Patterns Console, Behavior Console |
| **Pattern Flagging** | Flag pattern to KMO for promotion review | Patterns Console |
| **Issue Routing** | Triage issue, route to appropriate owner | Issues Console |
| **Behavioral Baseline** | Establish and update behavior baselines | Behavior Console, Patterns Console |
| **User Signal Analysis** | Analyze user feedback and override patterns | Behavior Console |

---

## OPDA Integration

The Cognitive Health Desk demonstrates OPDA capabilities for COS:

| OPDA | Capability | Console |
|------|------------|---------|
| **Observable** | Behavior quality metrics, user signals | Behavior Console |
| **Predictable** | Drift detection, baseline comparison | Patterns Console |
| **Directable** | Issue routing, intervention triggers | Issues Console |
| **Authority Enforceable** | Policy adherence monitoring, baseline updates | Behavior Console |

### How COS Actions, Assesses, and Evidences OPDA

| OPDA | COS Actions | COS Assesses | COS Evidences |
|------|-------------|--------------|---------------|
| **Observable** | Configure quality metrics | Review decision quality | Quality dashboards |
| **Predictable** | Set baselines | Compare to baselines | Drift reports |
| **Directable** | Route issues | Track resolution | Routing records |
| **Authority Enforceable** | Monitor policy adherence | Flag violations | Violation reports |

---

## Channel Access

| Channel | Capabilities |
|---------|--------------|
| **Web UI** | Full desk access via Seer Portal |
| **REST API** | `/api/seer/cos/v1` — [API Documentation](../../rest-channels/cos-rest-channel.md) |
| **MCP** | `seer-cos-mcp` server for AI assistant integration |
| **Slack/Teams** | Issue notifications |

---

## Integration Points

### Receives From

| Source | Data |
|--------|------|
| **Platform** | Agent behavior traces, decisions |
| **Users** | Overrides, feedback, escalations |
| **ARE** | System health data for correlation |

### Sends To

| Destination | Data |
|-------------|------|
| **APO** | Intent misalignment issues |
| **CSA** | Design flaw issues |
| **AE** | Implementation bug issues |
| **KMO** | Pattern candidates for promotion |
| **ARE** | System reliability issues |
| **ARAO** | Compliance concern issues |

---

## Indicative Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  COGNITIVE HEALTH DESK                                      COS: Morgan L.  │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Behavior] [Patterns] [Issues]                                 🔔 🔍 ⚙️    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ COGNITIVE QUALITY OVERVIEW                       Last Updated: 5m    │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │                                                                       │   │
│  │   Consistency    │  Confidence     │   User Trust    │   Coherence   │   │
│  │   █████████░     │  ████████░░     │   ███████░░░    │   ████████░░  │   │
│  │      94%         │      87%        │      78%        │      89%      │   │
│  │   [Healthy]      │   [Good]        │   [Attention]   │   [Good]      │   │
│  │                                                                       │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────┐  ┌──────────────────────────────┐  │
│  │ DRIFT ALERTS                  [2]   │  │ USER SIGNALS (7d)            │  │
│  │                                     │  │                              │  │
│  │ ⚠️ customer-service: Intent drift  │  │ Overrides: 23 (↑5%)          │  │
│  │    Confidence: 87% → 71% (7d)      │  │ Escalations: 8 (↓12%)        │  │
│  │    [Investigate]                    │  │ Positive: 156 (↑8%)          │  │
│  │                                     │  │ Negative: 12 (↓3%)           │  │
│  │ ⚠️ order-validator: Behavior drift │  │                              │  │
│  │    Approval rate: 85% → 68% (3d)   │  │ [View Details →]             │  │
│  │    [Investigate]                    │  │                              │  │
│  └─────────────────────────────────────┘  └──────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ ISSUE QUEUE                                                  [8]     │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │ Status │ Agent            │ Type        │ Suggested Route │ Age      │   │
│  │ ────────────────────────────────────────────────────────────────────  │   │
│  │ 🔴 NEW │ customer-service │ Intent      │ APO             │ 2h       │   │
│  │ 🟡 TRI │ order-validator  │ Design      │ CSA             │ 4h       │   │
│  │ 🟢 ROU │ expense-approver │ Bug         │ AE              │ 1d       │   │
│  │                                                                       │   │
│  │ [Route Selected] [Bulk Actions]                                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Console Summaries

### Behavior Console

Monitor cognitive quality across agents.

**Sections:**
- **Quality Dashboard** — Consistency, confidence, coherence metrics
- **User Signals** — Overrides, escalations, feedback sentiment
- **Baseline Comparisons** — Current vs. baseline behavior
- **Agent Deep Dive** — Per-agent behavioral analysis

**Key Features:**
- Quality trend analysis
- User trust indicators
- Anomaly highlighting
- Drill-down to specific decisions

[Full specification →](./behavior-console.md)

---

### Patterns Console

Detect drift, anomalies, and learning candidates.

**Sections:**
- **Drift Alerts** — Active drift detections
- **Anomaly Feed** — Unusual behaviors flagged
- **Pattern Candidates** — Recurring patterns for learning review
- **Baseline Manager** — View and update behavioral baselines

**Key Features:**
- Automated drift detection
- Pattern recognition algorithms
- Threshold configuration
- Evidence collection for KMO

[Full specification →](./patterns-console.md)

---

### Issues Console

Triage issues and route to appropriate owners.

**Sections:**
- **Issue Queue** — All detected issues awaiting triage
- **Classification** — Categorize: Intent, Design, Implementation, etc.
- **Routing Actions** — Route to APO, CSA, AE, KMO, ARE, ARAO
- **Resolution Tracker** — Track issues through resolution

**Key Features:**
- Smart routing suggestions
- One-click routing
- SLA tracking for issue resolution
- Closed-loop feedback

[Full specification →](./issues-console.md)

---

## REST API Overview

The COS REST channel provides programmatic access:

```
Base: /api/seer/cos/v1

Behavior:
  GET    /quality                  - Quality summary
  GET    /quality/agents/{id}      - Agent quality details
  GET    /user-signals             - User signal summary
  GET    /user-signals/agents/{id} - Agent user signals
  GET    /baselines                - List baselines
  PUT    /baselines/{id}           - Update baseline

Patterns:
  GET    /drift                    - List drift alerts
  GET    /drift/{id}               - Drift alert details
  GET    /anomalies                - List anomalies
  GET    /patterns                 - List pattern candidates
  POST   /patterns/{id}/flag       - Flag pattern for KMO

Issues:
  GET    /issues                   - List issues
  GET    /issues/{id}              - Issue details
  POST   /issues                   - Create issue
  PUT    /issues/{id}/classify     - Classify issue
  POST   /issues/{id}/route        - Route issue
  PUT    /issues/{id}/resolve      - Mark resolved
```

[Full API documentation →](../../rest-channels/cos-rest-channel.md)

---

*Status: 🟡 Draft — Overview and console specifications complete*
