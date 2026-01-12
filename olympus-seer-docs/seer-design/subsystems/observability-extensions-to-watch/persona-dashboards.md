# Persona Dashboards

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13  
> **Design Level**: C2 (Container)

---

## Overview

Persona Dashboards provides pre-built Grafana dashboards for four SRE personas: AI Platform Engineer, LLMOps Engineer, SRE for Agentic Systems, and Security Architect. Each dashboard is tailored to the specific needs and responsibilities of that persona.

**Key Principle**: Dashboards are organized by persona to provide focused, relevant observability for each role's responsibilities.

---

## Persona 1: AI Platform Engineer

> *Builds the internal agent platform: runtimes, tool registries, policy engines.*

### Responsibilities

- Maintain Seer runtime infrastructure
- Manage tool registry availability and versioning
- Operate policy engine (OPA) for agent governance
- Ensure platform component health and performance

### Metrics

#### Runtime Health Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_runtime_pods_total` | Total agent pods by state | `state={running,pending,failed}` |
| `seer_runtime_pod_restarts_total` | Pod restart count | `agent_id`, `reason` |
| `seer_runtime_scaling_events_total` | HPA scaling events | `direction={up,down}`, `agent_id` |
| `seer_runtime_resource_usage_ratio` | CPU/Memory usage vs limit | `resource={cpu,memory}`, `agent_id` |
| `seer_runtime_node_pressure` | Node resource pressure | `node`, `pressure_type` |

#### Tool Registry Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_tool_registry_tools_total` | Total registered tools | `workbench`, `status={active,deprecated}` |
| `seer_tool_registry_versions_total` | Tool versions available | `tool_id` |
| `seer_tool_registry_lookup_latency_seconds` | Tool lookup latency | `quantile` |
| `seer_tool_registry_sync_errors_total` | Registry sync failures | `source` |
| `seer_tool_gateway_availability_ratio` | Tool endpoint availability | `tool_id` |

#### Policy Engine Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_policy_evaluations_total` | OPA policy evaluations | `policy`, `result={allow,deny}` |
| `seer_policy_evaluation_latency_seconds` | Policy evaluation time | `policy`, `quantile` |
| `seer_policy_bundle_sync_timestamp` | Last policy bundle sync | `bundle` |
| `seer_policy_bundle_size_bytes` | Policy bundle size | `bundle` |
| `seer_policy_compile_errors_total` | Policy compilation failures | `policy` |

### Dashboards

#### Platform Health Dashboard

- Runtime status (agents deployed, pods healthy, restarts, scaling events)
- Resource utilization (CPU, memory, GPU across all agents)
- Tool registry status (total tools, active/deprecated, lookup latency, availability)
- Policy engine status (policies loaded, bundle version, sync status, evaluation metrics)

#### Tool Registry Dashboard

- Tool registration timeline
- Version distribution by tool
- Deprecation countdown (tools approaching EOL)
- Usage heatmap (which tools are most invoked)
- Availability by tool endpoint

#### Policy Engine Dashboard

- Policy evaluation rate over time
- Allow/Deny ratio by policy category
- Slow policies (evaluation latency > threshold)
- Bundle sync status across regions
- Policy coverage (agents with no policy bindings)

---

## Persona 2: LLMOps Engineer

> *Handles model lifecycle, prompt versions, rollbacks, observability.*

### Responsibilities

- Manage LLM model versions and deployments
- Version and deploy prompt templates
- Monitor model performance and cost
- Execute rollbacks when models underperform

### Metrics

#### Model Performance Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_llm_requests_total` | LLM API calls | `model`, `provider`, `status` |
| `seer_llm_latency_seconds` | Time to first token / total | `model`, `phase={ttft,total}` |
| `seer_llm_tokens_total` | Token consumption | `model`, `direction={input,output}` |
| `seer_llm_cost_dollars` | Cost incurred | `model`, `workbench`, `agent_id` |
| `seer_llm_errors_total` | LLM errors by type | `model`, `error_type` |
| `seer_llm_fallback_activations_total` | Fallback model activations | `primary_model`, `fallback_model` |

#### Prompt Versioning Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_prompt_version_active` | Currently active prompt version | `prompt_id`, `version` |
| `seer_prompt_deployments_total` | Prompt version deployments | `prompt_id`, `version`, `status` |
| `seer_prompt_rollbacks_total` | Prompt rollbacks | `prompt_id`, `from_version`, `to_version` |
| `seer_prompt_a_b_split_ratio` | A/B test traffic split | `prompt_id`, `variant` |

#### Model Quality Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_llm_confidence_score` | Average confidence of LLM outputs | `model`, `agent_id` |
| `seer_llm_hallucination_detections_total` | Hallucinations detected | `model`, `detection_method` |
| `seer_llm_grounding_failures_total` | RAG grounding failures | `model`, `agent_id` |
| `seer_llm_refusal_rate` | Rate of model refusals | `model`, `refusal_type` |

### Dashboards

#### LLM Operations Dashboard

- Model usage (requests, tokens, cost, latency by model)
- Cost tracking (daily spend, budget, projection)
- Latency trends (P50, P95, P99 over time)
- Prompt versions (active versions, traffic split, deployment status, A/B testing)
- Model quality (hallucination rate, grounding success)

#### Model Comparison Dashboard

- Side-by-side latency comparison across models
- Cost efficiency (output quality per dollar)
- Error rate comparison
- Token efficiency (output/input ratio)

#### Prompt A/B Testing Dashboard

- Variant performance comparison
- Statistical significance indicators
- Confidence intervals
- Recommended winner

---

## Persona 3: SRE for Agentic Systems

> *Manages latency, hallucination rates, retries, cost blowups, cascading failures.*

### Responsibilities

- Ensure agent reliability and SLA compliance
- Manage retry storms and circuit breakers
- Prevent cost runaway scenarios
- Handle cascading failures in multi-agent systems

### Metrics

#### Reliability Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_requests_total` | Agent request count | `agent_id`, `status={success,error}` |
| `seer_agent_latency_seconds` | End-to-end agent latency | `agent_id`, `quantile` |
| `seer_agent_sla_compliance_ratio` | SLA target achievement | `agent_id`, `sla_tier` |
| `seer_agent_timeout_total` | Request timeouts | `agent_id`, `phase` |
| `seer_agent_availability_ratio` | Uptime ratio | `agent_id` |

#### Retry & Circuit Breaker Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_retries_total` | Retry attempts | `agent_id`, `retry_reason` |
| `seer_agent_retry_exhausted_total` | Retries exhausted (final failure) | `agent_id` |
| `seer_circuit_breaker_state` | CB state (0=closed, 1=open, 2=half-open) | `agent_id`, `dependency` |
| `seer_circuit_breaker_trips_total` | CB trip events | `agent_id`, `dependency` |
| `seer_backpressure_rejections_total` | Requests rejected due to load | `agent_id` |

#### Multi-Agent Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_delegation_total` | Agent-to-agent delegations | `from_agent`, `to_agent`, `status` |
| `seer_agent_delegation_latency_seconds` | Delegation round-trip time | `from_agent`, `to_agent` |
| `seer_cascade_depth` | Delegation chain depth | `root_agent` |
| `seer_cascade_failures_total` | Failures cascading from dependencies | `root_agent`, `failed_agent` |

#### Cost Control Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_cost_dollars` | Cost per agent | `agent_id` |
| `seer_agent_cost_per_request_dollars` | Cost efficiency | `agent_id` |
| `seer_budget_utilization_ratio` | Spend vs budget | `workbench`, `budget_type` |
| `seer_cost_anomaly_score` | Cost anomaly detection | `agent_id` |

### Dashboards

#### Agentic Reliability Dashboard

- System health (success rate, P99 latency, circuit breakers, cost anomalies)
- Agent reliability (bottom 10 agents by success rate, latency, retries, CB state)
- Retry analysis (retry rate, retry reasons, exhausted retries)
- Circuit breaker status (open/closed/half-open by agent and dependency)
- Cascade analysis (delegation chains, cascade failures, depth analysis)

#### Cost Control Dashboard

- Cost by agent (total cost, cost per request, budget utilization)
- Cost anomalies (anomaly detection, cost spikes, unusual patterns)
- Budget tracking (daily/weekly/monthly budgets, utilization, projections)

---

## Persona 4: Security Architect (AI-focused)

> *Monitors tool access, prompt injection, data exfiltration, AI security.*

### Responsibilities

- Monitor tool access patterns and privilege escalation
- Detect prompt injection and jailbreak attempts
- Prevent data exfiltration
- Ensure guardrail enforcement

### Metrics

#### Security Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_guardrail_executions_total` | Guardrail executions | `guardrail`, `phase`, `response` |
| `seer_guardrail_violations_total` | Guardrail violations | `guardrail`, `violation_type` |
| `seer_prompt_injection_detections_total` | Prompt injection attempts | `agent_id`, `injection_type` |
| `seer_jailbreak_attempts_total` | Jailbreak attempts | `agent_id`, `method` |
| `seer_tool_access_denied_total` | Tool access denials | `agent_id`, `tool_id`, `reason` |
| `seer_data_exfiltration_attempts_total` | Data exfiltration attempts | `agent_id`, `method` |

### Dashboards

#### Security Operations Dashboard

- Guardrail enforcement (executions, violations, response rates)
- Prompt injection timeline (injection attempts, blocked attempts, attack vectors)
- Tool access audit (access patterns, denials, privilege escalations)
- Data exfiltration monitoring (attempts, blocked attempts, methods)

---

## Dashboard Deployment

Dashboards are deployed via Watch Extension Layer:

```yaml
dashboard_deployment:
  persona: "ai-platform-engineer"
  dashboards:
    - id: "platform-health"
      title: "Platform Health Dashboard"
      folder: "Seer/AI Platform Engineer"
    - id: "tool-registry"
      title: "Tool Registry Dashboard"
      folder: "Seer/AI Platform Engineer"
    - id: "policy-engine"
      title: "Policy Engine Dashboard"
      folder: "Seer/AI Platform Engineer"
```

---

## Related Documentation

- [Watch Extension Layer](./watch-extension-layer.md) — Extension infrastructure and deployment
- [Alert Templates](./alert-templates.md) — Pre-built alerts for each persona
- [Operational Tools](./operational-tools.md) — Tools for each persona
- [Agent Observability](../agent-observability.md) — SDK and agent-level instrumentation

---

*Persona Dashboards provide focused, role-specific observability for AI Platform Engineers, LLMOps Engineers, SREs for Agentic Systems, and Security Architects.*
