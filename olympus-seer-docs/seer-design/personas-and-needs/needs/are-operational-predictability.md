# ARE: Operational Predictability & Production Readiness

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Persona:** [Agent Reliability Engineer (ARE)](../roles.md#5-agent-reliability-engineer-are)  
> **Related:** [Production Readiness](./production-readiness.md) | [AE Deliverables to ARE](./ae-deliverables-to-are.md)

---

## Overview

This page details the operational needs of the **Agent Reliability Engineer (ARE)** regarding predictability, safety, and production readiness of AI agents. These needs inform the capabilities of the [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md).

---

## Need 1: Operational Predictability

### Description

ARE requires assurance that agents behave predictably within defined bounds. Unpredictable agent behavior undermines operational confidence and makes incident response difficult.

### Requirements

| Requirement | Rationale |
|-------------|-----------|
| **Bounded execution** | Agents must have defined maximum iterations, timeouts, and token limits |
| **Consistent behavior** | Given similar inputs, agents should produce similar outputs |
| **Baseline comparison** | Ability to compare current behavior against established baselines |
| **Drift detection** | Automatic alerting when behavior deviates from baseline |
| **SLA enforcement** | Agents must meet defined latency, availability, and error rate targets |

### Success Criteria

- [ ] All agents have defined execution bounds
- [ ] Baselines established for all production agents
- [ ] Drift detection alerts configured
- [ ] SLA targets defined and monitored

---

## Need 2: Production Readiness Gates

### Description

Before an agent can run in production, ARE must verify that it meets operational requirements. This includes safety controls, observability, and rollback capability.

### Production Readiness Checklist

See [Production Readiness Checklist](./production-readiness-checklist.md) for the complete checklist.

Core requirements:

| Category | Requirement |
|----------|-------------|
| **Safety** | Kill switch implemented and tested |
| **Safety** | Execution bounds defined |
| **Safety** | Cost ceiling configured |
| **Observability** | Telemetry contract fulfilled |
| **Observability** | Required trace events implemented |
| **Rollback** | Previous version available |
| **Rollback** | One-click rollback tested |

---

## Need 3: Intervention Capability

### Description

ARE must be able to intervene in agent operations at any time. This includes stopping, pausing, throttling, and rolling back agents.

### Required Controls

| Control | Description | SLA |
|---------|-------------|-----|
| **Kill Switch** | Immediately stop all agent execution | < 30 seconds |
| **Pause** | Stop accepting new tasks | < 1 minute |
| **Throttle** | Reduce execution rate | < 1 minute |
| **Rollback** | Revert to previous version | < 5 minutes |
| **Circuit Breaker** | Automatic fault isolation | Automatic |

### Success Criteria

- [ ] All controls accessible from Health Console
- [ ] Controls tested in staging before production
- [ ] Audit trail for all control actions

---

## Need 4: Health Visibility

### Description

ARE requires comprehensive visibility into agent health across the fleet. This includes individual agent health, fleet-wide metrics, and resource utilization.

### Key Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Agent Health Score (AHS)** | Composite health metric | > 0.85 |
| **Availability** | Uptime percentage | Per SLA tier |
| **Error Rate** | Errors / Total requests | < 2% |
| **Latency (P95)** | 95th percentile response time | Per SLA tier |
| **Cost-to-Health Ratio (CHR)** | Cost efficiency metric | Monitored |

### Dashboard Requirements

- Fleet-wide summary view
- Drill-down to individual agents
- Historical trend analysis
- Alerting based on thresholds

---

## Need 5: Incident Response Capability

### Description

When incidents occur, ARE must be able to quickly detect, contain, investigate, and resolve issues. This requires integrated tooling and clear workflows.

### Incident Management Requirements

| Phase | Capability |
|-------|------------|
| **Detect** | Automated alerting on anomalies |
| **Contain** | Quick access to kill switch and throttle |
| **Investigate** | Access to traces and logs |
| **Resolve** | Rollback capability |
| **Review** | PIR templates and tracking |

---

## Need 6: SLA Management

### Description

Different agents have different SLA requirements based on business criticality. ARE must be able to define, monitor, and enforce SLAs by tier.

### SLA Tiers

| Tier | Availability | P95 Latency | Error Rate |
|------|-------------|-------------|------------|
| **Critical** | 99.9% | 1s | 0.1% |
| **High** | 99.5% | 5s | 0.5% |
| **Standard** | 99.0% | 30s | 2% |
| **Background** | 95.0% | 5m | 5% |

---

## Desk Integration

These needs are addressed through the [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md):

| Need | Console | Key Features |
|------|---------|--------------|
| Operational Predictability | Health Console | AHS, baselines, drift alerts |
| Production Readiness | Control Console | Gate review, checklist verification |
| Intervention Capability | Control Console | Kill switch, throttle, rollback |
| Health Visibility | Health Console | Fleet dashboard, drill-down |
| Incident Response | Incident Console | Timeline, containment, PIR |
| SLA Management | Health Console | SLA tracking, breach alerts |

---

## OPDA Alignment

| Property | ARE Role |
|----------|----------|
| **Observable** | Fleet health visibility, trace access |
| **Predictable** | SLA enforcement, baseline comparison |
| **Directable** | Kill switch, throttle, rollback |
| **Authority Enforceable** | Production gates |

---

*These needs ensure ARE can maintain safe, predictable, and controllable agent operations.*
