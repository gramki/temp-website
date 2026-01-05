# Steward Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Steward Desk** is the runtime operations console for Process Architects and Developers to monitor Workbenches and Hub Applications in production, triage issues, and respond to incidents.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Personas** | [Process Architect](../08-personas-and-journeys/personas/process-architect.md), [Developer](../08-personas-and-journeys/personas/developer.md) |
| **Scope** | Workbenches and Hub Applications they create/maintain |
| **Purpose** | Runtime monitoring, incident triage, production issue resolution |
| **Access** | Web, MCP (Creator Channel) |

---

## Design-time / Runtime Separation

| Phase | Application | Purpose |
|-------|-------------|---------|
| **Design-time** | Workbench Studio | Build scenarios, applications, configure triggers |
| **Runtime** | Steward Desk | Monitor health, triage issues, resolve incidents |

The same personas (Process Architect, Developer) use both applications, but with different objectives.

---

## Console Types

### Health Monitoring Consoles

| Console | Purpose |
|---------|---------|
| **Workbench Health Console** | Overall workbench status, throughput, error rates |
| **Application Health Console** | Per-application metrics, latency, failures |
| **Trigger Health Console** | Trigger evaluation rates, misses, errors |
| **Queue Health Console** | Task queue depths, processing times |
| **Reports Console** | Operational reports for workbench/application health (via [Hub Analytics](../../04-subsystems/hub-analytics/README.md)) |

### Incident Response Consoles

| Console | Purpose |
|---------|---------|
| **Incident Console** | Active incidents, triage queue, resolution tracking |
| **Error Log Console** | Application errors, stack traces, correlations |
| **Signal Trace Console** | Trace signals through trigger → request → application flow |
| **Request Forensics Console** | Deep-dive into specific request lifecycle |

### Production Support Consoles

| Console | Purpose |
|---------|---------|
| **Production SOPs Console** | Issue resolution runbooks and procedures |
| **Remediation Tools Console** | Tools for common fixes (retry, requeue, cancel) |
| **Configuration Drift Console** | Detect drift from expected configuration |
| **Deployment History Console** | Recent deployments, rollback options |

---

## Workbench Health Console

Real-time view of workbench operational health.

### Sample Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     WORKBENCH HEALTH - Dispute Operations                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐  │
│  │  REQUEST VOLUME      │  │  ERROR RATE          │  │  AVG LATENCY     │  │
│  │     1,247 / hr       │  │      0.3%            │  │      2.4s        │  │
│  │  ▲ 12% vs yesterday  │  │  🟢 within SLO       │  │  🟢 within SLO   │  │
│  └──────────────────────┘  └──────────────────────┘  └──────────────────┘  │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  APPLICATION STATUS                                                 │    │
│  │                                                                     │    │
│  │  Application           │ Status │ Requests │ Errors │ P95 Latency  │    │
│  │  ────────────────────────────────────────────────────────────────── │    │
│  │  Dispute Filing Agent  │  🟢    │   423    │   1    │    1.8s      │    │
│  │  Document Processor    │  🟢    │   312    │   0    │    3.2s      │    │
│  │  Merchant Contact WF   │  🟡    │   156    │   5    │    8.1s      │    │
│  │  Final Decision Agent  │  🟢    │    89    │   0    │    2.1s      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  RECENT INCIDENTS                                          [View All]│    │
│  │  ─────────────────────────────────────────────────────────────────  │    │
│  │  🔴 INC-2024-0312 | Merchant Contact timeout spike | 15m ago        │    │
│  │  🟢 INC-2024-0311 | Document upload failures | Resolved 2h ago      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Incident Console

Triage and track production incidents.

### Capabilities

| Capability | Description |
|------------|-------------|
| **Incident Queue** | Prioritized list of active incidents |
| **Auto-Detection** | Automatic incident creation from anomaly detection |
| **Impact Assessment** | Affected requests, users, scenarios |
| **Root Cause Tools** | Linked traces, logs, related changes |
| **Resolution Tracking** | Status updates, resolution notes, post-mortem |

### Incident Lifecycle

```
[Detected] → [Triaged] → [Investigating] → [Mitigating] → [Resolved] → [Post-Mortem]
```

---

## Production SOPs Console

Access runbooks and resolution procedures for known issues.

### SOP Categories

| Category | Examples |
|----------|----------|
| **Application Issues** | Restart procedures, cache flush, config reload |
| **Integration Issues** | External service degradation, fallback activation |
| **Data Issues** | Stuck requests, orphaned tasks, data repair |
| **Performance Issues** | Scaling triggers, throttling adjustments |
| **Security Issues** | Token refresh, access revocation, audit triggers |

### SOP Structure

```yaml
sop:
  id: "SOP-MERCHANT-TIMEOUT"
  title: "Merchant API Timeout Resolution"
  symptoms:
    - "Merchant Contact workflow latency > 10s"
    - "Error rate spike in Merchant Contact App"
  diagnosis:
    steps:
      - "Check Merchant API health dashboard"
      - "Review recent deployment changes"
      - "Check rate limit status"
  resolution:
    steps:
      - "If API degraded: Enable fallback mode"
      - "If rate limited: Increase throttle backoff"
      - "If deployment issue: Initiate rollback"
  tools:
    - tool: "enable_fallback_mode"
      params: { app: "merchant-contact-wf" }
    - tool: "rollback_deployment"
      params: { app: "merchant-contact-wf", version: "previous" }
```

---

## Remediation Tools Console

Quick-access tools for common production fixes.

| Tool | Purpose |
|------|---------|
| **Retry Request** | Resubmit a failed request |
| **Requeue Task** | Move task back to queue |
| **Cancel Request** | Gracefully terminate stuck request |
| **Flush Cache** | Clear application cache |
| **Enable Fallback** | Activate fallback mode for integration |
| **Scale Application** | Adjust replica count |
| **Rollback Deployment** | Revert to previous version |

---

## Screen Structure

```
Steward Desk
├── Home (Workbench health overview)
│
├── Health Monitoring
│   ├── Workbench Health
│   ├── Application Health
│   ├── Trigger Health
│   ├── Queue Health
│   └── Reports
│
├── Incident Response
│   ├── Incident Console
│   ├── Error Logs
│   ├── Signal Trace
│   └── Request Forensics
│
├── Production Support
│   ├── SOPs
│   ├── Remediation Tools
│   ├── Configuration Drift
│   └── Deployment History
│
└── Alerts & Notifications
    └── (Configured alerting rules and channels)
```

---

## Integration with Olympus Watch

Steward Desk integrates with **Olympus Watch** for:
- Metrics visualization
- Log aggregation and search
- Distributed tracing
- Anomaly detection alerts

See [Olympus Watch](../05-infrastructure/olympus-watch.md) for observability infrastructure.

---

## Related Documentation

- [Process Architect Persona](../../08-personas-and-journeys/personas/process-architect.md)
- [Developer Persona](../../08-personas-and-journeys/personas/developer.md)
- [Workbench Studio](./workbench-studio.md) — Design-time counterpart
- [Hub Application APM](../../04-subsystems/supporting-systems/hub-application-apm.md)
- [Olympus Watch](../../05-infrastructure/olympus-watch.md)
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Powers Reports Console

---

## Appendix: Naming Rationale

### Why "Steward Desk"?

The name "Steward" was chosen to convey:

| Aspect | Rationale |
|--------|-----------|
| **Ownership with care** | Not just fixing, but overseeing health |
| **Proactive governance** | Monitoring, not just reacting |
| **Alignment with industry** | "Data steward", "product steward" are established concepts |
| **Process Architect fit** | Governance-minded personas resonate with stewardship |

### Alternative Considered: Maintainer Desk

"Maintainer Desk" was a strong alternative with different connotations:

| Aspect | Maintainer Desk |
|--------|-----------------|
| **Clarity** | Immediately understood ("I maintain this") |
| **Developer familiarity** | Strong in open source culture |
| **Action-oriented** | Implies hands-on fixing |

### Recommendation

If feedback indicates that "Steward" feels unfamiliar or passive, consider switching to "Maintainer Desk" as it offers:
- Stronger developer resonance
- Clearer action-oriented connotation
- Well-established in engineering culture

---

*TODO: Detailed console specifications, SOP templates, integration with alerting systems*
