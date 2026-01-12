# Alert Templates

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13  
> **Design Level**: C2 (Container)

---

## Overview

Alert Templates provides pre-built alert definitions for Seer-specific scenarios. Alerts are organized by persona and severity level, with routing configurations for different notification channels.

**Key Principle**: Alert templates are pre-configured but customizable, providing sensible defaults for common Seer operational scenarios.

---

## Alert Structure

### Alert Rule Format

```yaml
alert_rule:
  name: "SeerAgentHighErrorRate"
  expr: |
    rate(seer_agent_errors_total[10m]) > 0.05
  for: "10m"
  labels:
    severity: "warning"
    subsystem: "seer"
    persona: "sre-agentic-systems"
  annotations:
    summary: "Agent {{ $labels.agent_id }} has high error rate"
    description: |
      Error rate is {{ $value | humanizePercentage }}.
      Agent: {{ $labels.agent_id }}
      Workbench: {{ $labels.workbench_id }}
```

### Alert Routing

```yaml
alert_routing:
  receiver: "seer-alerts"
  group_by: [agent_id, workbench_id]
  group_wait: "30s"
  group_interval: "5m"
  repeat_interval: "12h"
  routes:
    - match:
        severity: critical
      receiver: "seer-critical-alerts"
    - match:
        severity: warning
      receiver: "seer-warning-alerts"
    - match:
        persona: "ai-platform-engineer"
      receiver: "seer-platform-alerts"
```

---

## Persona-Specific Alerts

### AI Platform Engineer Alerts

| Alert | Condition | Severity | Response |
|-------|-----------|----------|----------|
| **RuntimeNodePressure** | Node CPU/Memory > 85% for 10m | Warning | Scale nodes or redistribute agents |
| **HighPodRestartRate** | > 5 restarts in 30m for any agent | Warning | Investigate crash loops |
| **ToolRegistryUnavailable** | Registry sync failed for > 5m | Critical | Check registry backend, failover |
| **ToolEndpointDown** | Tool availability < 95% for 5m | Warning | Check tool backend, circuit breaker |
| **PolicySyncStale** | Bundle not synced for > 15m | Warning | Check OPA connectivity |
| **PolicyEvaluationSlow** | P99 > 100ms for 5m | Warning | Optimize policy, scale OPA |

### LLMOps Engineer Alerts

| Alert | Condition | Severity | Response |
|-------|-----------|----------|----------|
| **ModelLatencyDegraded** | P99 > 2x baseline for 10m | Warning | Check provider status, consider fallback |
| **BudgetThresholdReached** | Daily spend > 75% / 90% | Info/Warning | Review high-cost agents |
| **FallbackModelActive** | Primary model unavailable | Warning | Check provider, plan recovery |
| **HighHallucinationRate** | Rate > 2% for 30m | Warning | Review prompts, add grounding |
| **PromptDeploymentFailed** | Version deployment failed | Critical | Rollback, investigate |
| **ModelRefusalSpike** | Refusal rate > 5% | Warning | Review prompt, check for policy changes |

### SRE for Agentic Systems Alerts

| Alert | Condition | Severity | Response |
|-------|-----------|----------|----------|
| **AgentHighErrorRate** | Error rate > 5% for 10m | Warning | Investigate agent behavior, check dependencies |
| **AgentLatencyDegraded** | P99 > 2x baseline for 15m | Warning | Check agent performance, optimize |
| **CircuitBreakerOpen** | Circuit breaker open for > 5m | Critical | Investigate dependency, plan recovery |
| **RetryStormDetected** | Retry rate > 20% for 10m | Warning | Check dependency health, adjust retry policy |
| **CascadeFailureDetected** | Cascade depth > 5 or cascade failure | Critical | Isolate failing agent, break cascade |
| **CostAnomalyDetected** | Cost anomaly score > threshold | Warning | Review agent behavior, check for loops |
| **SLAViolation** | SLA compliance < target for 15m | Warning | Investigate root cause, optimize |

### Security Architect Alerts

| Alert | Condition | Severity | Response |
|-------|-----------|----------|----------|
| **PromptInjectionDetected** | Any injection attempt | Warning | Review, update guardrails |
| **JailbreakAttemptDetected** | Jailbreak attempt | Critical | Block agent, investigate source |
| **UnauthorizedToolAccess** | Access denied spike > 10/min | Warning | Review agent permissions |
| **SensitiveDataExfiltration** | Any exfiltration attempt | Critical | Isolate agent, forensic review |
| **AnomalousToolAccess** | Tool access pattern anomaly | Warning | Review agent behavior |
| **PrivilegeEscalationAttempt** | Escalation attempt detected | Critical | Block agent, audit credentials |
| **GuardrailBypass** | Guardrail circumvention attempt | Critical | Investigate, strengthen guardrails |

---

## Alert Receivers

### Receiver Configuration

```yaml
receivers:
  - name: "seer-alerts"
    slack_configs:
      - channel: "#seer-alerts"
        api_url: "https://hooks.slack.com/..."
        title: "Seer Alert: {{ .GroupLabels.alertname }}"
        text: "{{ range .Alerts }}{{ .Annotations.description }}{{ end }}"
  
  - name: "seer-critical-alerts"
    slack_configs:
      - channel: "#seer-critical"
        api_url: "https://hooks.slack.com/..."
    email_configs:
      - to: "seer-oncall@company.com"
        subject: "CRITICAL: {{ .GroupLabels.alertname }}"
    pagerduty_configs:
      - service_key: "..."
        description: "{{ .GroupLabels.alertname }}"
  
  - name: "seer-warning-alerts"
    slack_configs:
      - channel: "#seer-warnings"
        api_url: "https://hooks.slack.com/..."
  
  - name: "seer-platform-alerts"
    slack_configs:
      - channel: "#seer-platform"
        api_url: "https://hooks.slack.com/..."
```

---

## Alert Grouping

Alerts are grouped to reduce notification noise:

| Grouping Strategy | Description | Use Case |
|-------------------|-------------|----------|
| **By Agent** | Group alerts by agent_id | Agent-specific issues |
| **By Workbench** | Group alerts by workbench_id | Workbench-wide issues |
| **By Severity** | Group alerts by severity | Critical vs. warning separation |
| **By Persona** | Group alerts by persona | Persona-specific routing |

---

## Alert Suppression

Alerts can be suppressed during maintenance windows:

```yaml
inhibit_rules:
  - source_match:
      severity: "critical"
    target_match:
      severity: "warning"
    equal: [agent_id, workbench_id]
```

---

## Related Documentation

- [Watch Extension Layer](./watch-extension-layer.md) — Alert configuration deployment
- [Persona Dashboards](./persona-dashboards.md) — Dashboards for each persona
- [Operational Tools](./operational-tools.md) — Tools for alert response

---

*Alert Templates provide pre-built alert definitions for Seer-specific operational scenarios.*
