# Observability Extensions to Watch

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-09

---

## Overview

This document specifies **Seer-specific extensions to Olympus Watch** that serve the operational needs of AI platform engineering and SRE teams. These extensions provide specialized metrics, dashboards, alerts, and operational tools for managing agentic systems at scale.

While [Agent Observability](./agent-observability.md) documents the SDK and agent-level instrumentation, this document focuses on **platform-level observability** consumed by Seer SRE personas.

---

## Seer SRE Personas

| Persona | Focus Area | Primary Concerns |
|---------|------------|------------------|
| **AI Platform Engineer** | Platform infrastructure | Runtime health, tool registry, policy engine |
| **LLMOps Engineer** | Model lifecycle | Prompt versions, model performance, rollbacks |
| **SRE for Agentic Systems** | Reliability & cost | Latency, hallucinations, retries, cascading failures |
| **Security Architect (AI-focused)** | AI security | Tool access, prompt injection, data exfiltration |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  SEER OBSERVABILITY EXTENSIONS TO WATCH                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SEER RUNTIME COMPONENTS (Metric Sources)                                   │
│   ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐    │
│   │  Model    │ │   Tool    │ │  Policy   │ │  Agent    │ │ Guardrail │    │
│   │  Gateway  │ │  Gateway  │ │  Engine   │ │ Lifecycle │ │  Sidecar  │    │
│   └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘    │
│         │             │             │             │             │          │
│         └─────────────┴─────────────┴─────────────┴─────────────┘          │
│                                     │                                       │
│                                     ▼                                       │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                         OLYMPUS WATCH                                │  │
│   │                                                                      │  │
│   │   ┌─────────────────────────────────────────────────────────────┐   │  │
│   │   │                 SEER EXTENSION LAYER                         │   │  │
│   │   │                                                              │   │  │
│   │   │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │  │
│   │   │   │  AI Platform │  │   LLMOps     │  │  Agentic SRE │      │   │  │
│   │   │   │  Dashboards  │  │  Dashboards  │  │  Dashboards  │      │   │  │
│   │   │   └──────────────┘  └──────────────┘  └──────────────┘      │   │  │
│   │   │                                                              │   │  │
│   │   │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │  │
│   │   │   │  AI Security │  │   Alert      │  │  Operational │      │   │  │
│   │   │   │  Dashboards  │  │  Templates   │  │  Runbooks    │      │   │  │
│   │   │   └──────────────┘  └──────────────┘  └──────────────┘      │   │  │
│   │   │                                                              │   │  │
│   │   └──────────────────────────────────────────────────────────────┘   │  │
│   │                                                                      │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

# Persona 1: AI Platform Engineer

> *Builds the internal agent platform: runtimes, tool registries, policy engines.*

## Responsibilities

- Maintain Seer runtime infrastructure
- Manage tool registry availability and versioning
- Operate policy engine (OPA) for agent governance
- Ensure platform component health and performance

---

## Metrics

### Runtime Health Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_runtime_pods_total` | Total agent pods by state | `state={running,pending,failed}` |
| `seer_runtime_pod_restarts_total` | Pod restart count | `agent_id`, `reason` |
| `seer_runtime_scaling_events_total` | HPA scaling events | `direction={up,down}`, `agent_id` |
| `seer_runtime_resource_usage_ratio` | CPU/Memory usage vs limit | `resource={cpu,memory}`, `agent_id` |
| `seer_runtime_node_pressure` | Node resource pressure | `node`, `pressure_type` |

### Tool Registry Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_tool_registry_tools_total` | Total registered tools | `workbench`, `status={active,deprecated}` |
| `seer_tool_registry_versions_total` | Tool versions available | `tool_id` |
| `seer_tool_registry_lookup_latency_seconds` | Tool lookup latency | `quantile` |
| `seer_tool_registry_sync_errors_total` | Registry sync failures | `source` |
| `seer_tool_gateway_availability_ratio` | Tool endpoint availability | `tool_id` |

### Policy Engine Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_policy_evaluations_total` | OPA policy evaluations | `policy`, `result={allow,deny}` |
| `seer_policy_evaluation_latency_seconds` | Policy evaluation time | `policy`, `quantile` |
| `seer_policy_bundle_sync_timestamp` | Last policy bundle sync | `bundle` |
| `seer_policy_bundle_size_bytes` | Policy bundle size | `bundle` |
| `seer_policy_compile_errors_total` | Policy compilation failures | `policy` |

---

## Dashboards

### Platform Health Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SEER PLATFORM HEALTH                                     Refresh: 30s      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  RUNTIME STATUS                                                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │  Agents     │ │  Pods       │ │  Pod        │ │  Scaling    │           │
│  │  Deployed   │ │  Healthy    │ │  Restarts   │ │  Events     │           │
│  │    127      │ │   98.4%     │ │    12/24h   │ │    8/24h    │           │
│  │  ▲ +3 today │ │  ▼ -0.2%    │ │  ▼ -5       │ │  ◄► stable  │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                              │
│  RESOURCE UTILIZATION (All Agents)                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ CPU ████████████████░░░░░░░░░░░░  62%   avg across 127 agents       │   │
│  │ Memory ████████████████████░░░░░  78%   avg across 127 agents       │   │
│  │ GPU ████████░░░░░░░░░░░░░░░░░░░░  31%   16 agents with GPU          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  TOOL REGISTRY                                                               │
│  ┌─────────────────────────────┐  ┌────────────────────────────────────┐   │
│  │  Total Tools: 342           │  │  Tool Lookup Latency (P99)         │   │
│  │  Active: 298                │  │  ████▌ 12ms (target: <50ms)        │   │
│  │  Deprecated: 44             │  │                                    │   │
│  │  Sync Errors (24h): 0       │  │  Availability: 99.97%              │   │
│  └─────────────────────────────┘  └────────────────────────────────────┘   │
│                                                                              │
│  POLICY ENGINE                                                               │
│  ┌─────────────────────────────┐  ┌────────────────────────────────────┐   │
│  │  Policies Loaded: 89        │  │  Evaluations (1h)                  │   │
│  │  Bundle Version: v2.14.3    │  │  ███████████████ 45,231            │   │
│  │  Last Sync: 2 min ago       │  │  Allow: 98.7%  Deny: 1.3%          │   │
│  │  Compile Errors: 0          │  │  Latency P99: 2.3ms                │   │
│  └─────────────────────────────┘  └────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Tool Registry Dashboard

- Tool registration timeline
- Version distribution by tool
- Deprecation countdown (tools approaching EOL)
- Usage heatmap (which tools are most invoked)
- Availability by tool endpoint

### Policy Engine Dashboard

- Policy evaluation rate over time
- Allow/Deny ratio by policy category
- Slow policies (evaluation latency > threshold)
- Bundle sync status across regions
- Policy coverage (agents with no policy bindings)

---

## Alerts

| Alert | Condition | Severity | Response |
|-------|-----------|----------|----------|
| **RuntimeNodePressure** | Node CPU/Memory > 85% for 10m | Warning | Scale nodes or redistribute agents |
| **HighPodRestartRate** | > 5 restarts in 30m for any agent | Warning | Investigate crash loops |
| **ToolRegistryUnavailable** | Registry sync failed for > 5m | Critical | Check registry backend, failover |
| **ToolEndpointDown** | Tool availability < 95% for 5m | Warning | Check tool backend, circuit breaker |
| **PolicySyncStale** | Bundle not synced for > 15m | Warning | Check OPA connectivity |
| **PolicyEvaluationSlow** | P99 > 100ms for 5m | Warning | Optimize policy, scale OPA |

---

## Operational Tools

| Tool | Purpose | Access |
|------|---------|--------|
| **Agent Scaler** | Manually scale agent replicas | Watch Console + kubectl |
| **Tool Registry Admin** | Deprecate, activate, version tools | Workbench Studio |
| **Policy Simulator** | Test policy changes before deployment | Watch Console (Rego Playground) |
| **Runtime Debugger** | Pod exec, log streaming, resource inspection | Watch Console + kubectl |

---

# Persona 2: LLMOps Engineer

> *Handles model lifecycle, prompt versions, rollbacks, observability.*

## Responsibilities

- Manage LLM model versions and deployments
- Version and deploy prompt templates
- Monitor model performance and cost
- Execute rollbacks when models underperform

---

## Metrics

### Model Performance Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_llm_requests_total` | LLM API calls | `model`, `provider`, `status` |
| `seer_llm_latency_seconds` | Time to first token / total | `model`, `phase={ttft,total}` |
| `seer_llm_tokens_total` | Token consumption | `model`, `direction={input,output}` |
| `seer_llm_cost_dollars` | Cost incurred | `model`, `workbench`, `agent_id` |
| `seer_llm_errors_total` | LLM errors by type | `model`, `error_type` |
| `seer_llm_fallback_activations_total` | Fallback model activations | `primary_model`, `fallback_model` |

### Prompt Versioning Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_prompt_version_active` | Currently active prompt version | `prompt_id`, `version` |
| `seer_prompt_deployments_total` | Prompt version deployments | `prompt_id`, `version`, `status` |
| `seer_prompt_rollbacks_total` | Prompt rollbacks | `prompt_id`, `from_version`, `to_version` |
| `seer_prompt_a_b_split_ratio` | A/B test traffic split | `prompt_id`, `variant` |

### Model Quality Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_llm_confidence_score` | Average confidence of LLM outputs | `model`, `agent_id` |
| `seer_llm_hallucination_detections_total` | Hallucinations detected | `model`, `detection_method` |
| `seer_llm_grounding_failures_total` | RAG grounding failures | `model`, `agent_id` |
| `seer_llm_refusal_rate` | Rate of model refusals | `model`, `refusal_type` |

---

## Dashboards

### LLM Operations Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  LLM OPERATIONS                                           Refresh: 1m       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  MODEL USAGE (Last 24h)                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Model          │ Requests │ Tokens (M) │  Cost ($) │ Latency P50  │   │
│  ├─────────────────┼──────────┼────────────┼───────────┼──────────────┤   │
│  │  gpt-4o         │  45,231  │    12.4    │   $847    │   1.2s       │   │
│  │  gpt-4o-mini    │ 128,456  │    28.7    │   $143    │   0.4s       │   │
│  │  claude-3-opus  │   8,921  │     4.1    │   $369    │   2.1s       │   │
│  │  claude-3-sonnet│  67,234  │    15.3    │   $230    │   0.9s       │   │
│  │  llama-3-70b    │  23,001  │     8.2    │    $41    │   0.6s       │   │
│  └─────────────────┴──────────┴────────────┴───────────┴──────────────┘   │
│                                                                              │
│  COST TRACKING                           LATENCY TRENDS                      │
│  ┌─────────────────────────┐            ┌──────────────────────────────┐   │
│  │  Today:     $1,630      │            │  P50  ────────────────────   │   │
│  │  Budget:    $2,000/day  │            │  P95  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │   │
│  │  Remaining: $370        │            │  P99  ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈  │   │
│  │  Projection: $1,890     │            │                              │   │
│  │  ████████████████░░░░░  │            │  [Time series graph]         │   │
│  │       81.5%             │            │                              │   │
│  └─────────────────────────┘            └──────────────────────────────┘   │
│                                                                              │
│  PROMPT VERSIONS                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Prompt                  │ Version │ Traffic │ Deployed │ Status   │   │
│  ├──────────────────────────┼─────────┼─────────┼──────────┼──────────┤   │
│  │  fraud-analysis-v2       │  2.4.1  │  100%   │  Jan 05  │ ✓ Active │   │
│  │  dispute-resolution      │  1.8.0  │   90%   │  Jan 07  │ ✓ Active │   │
│  │  dispute-resolution      │  1.9.0  │   10%   │  Jan 08  │ ◉ A/B    │   │
│  │  customer-intent         │  3.1.2  │  100%   │  Dec 28  │ ✓ Active │   │
│  └──────────────────────────┴─────────┴─────────┴──────────┴──────────┘   │
│                                                                              │
│  MODEL QUALITY                                                               │
│  ┌─────────────────────────┐ ┌─────────────────────────┐                   │
│  │  Hallucination Rate     │ │  Grounding Success      │                   │
│  │  ▼ 0.23% (target <1%)   │ │  ▲ 97.8% (target >95%) │                   │
│  │  Trend: improving       │ │  Trend: stable          │                   │
│  └─────────────────────────┘ └─────────────────────────┘                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Model Comparison Dashboard

- Side-by-side latency comparison across models
- Cost efficiency (output quality per dollar)
- Error rate comparison
- Token efficiency (output/input ratio)

### Prompt A/B Testing Dashboard

- Variant performance comparison
- Statistical significance indicators
- Confidence intervals
- Recommended winner

---

## Alerts

| Alert | Condition | Severity | Response |
|-------|-----------|----------|----------|
| **ModelLatencyDegraded** | P99 > 2x baseline for 10m | Warning | Check provider status, consider fallback |
| **BudgetThresholdReached** | Daily spend > 75% / 90% | Info/Warning | Review high-cost agents |
| **FallbackModelActive** | Primary model unavailable | Warning | Check provider, plan recovery |
| **HighHallucinationRate** | Rate > 2% for 30m | Warning | Review prompts, add grounding |
| **PromptDeploymentFailed** | Version deployment failed | Critical | Rollback, investigate |
| **ModelRefusalSpike** | Refusal rate > 5% | Warning | Review prompt, check for policy changes |

---

## Operational Tools

| Tool | Purpose | Access |
|------|---------|--------|
| **Prompt Version Manager** | Deploy, rollback, A/B test prompts | Workbench Studio |
| **Model Fallback Config** | Configure model fallback chains | Watch Console |
| **Cost Analyzer** | Drill-down cost by agent, prompt, model | Watch Console |
| **Prompt Playground** | Test prompts before deployment | Workbench Studio |
| **Rollback Trigger** | Instant rollback to previous prompt version | Watch Console (one-click) |

---

# Persona 3: SRE for Agentic Systems

> *Manages latency, hallucination rates, retries, cost blowups, cascading failures.*

## Responsibilities

- Ensure agent reliability and SLA compliance
- Manage retry storms and circuit breakers
- Prevent cost runaway scenarios
- Handle cascading failures in multi-agent systems

---

## Metrics

### Reliability Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_requests_total` | Agent request count | `agent_id`, `status={success,error}` |
| `seer_agent_latency_seconds` | End-to-end agent latency | `agent_id`, `quantile` |
| `seer_agent_sla_compliance_ratio` | SLA target achievement | `agent_id`, `sla_tier` |
| `seer_agent_timeout_total` | Request timeouts | `agent_id`, `phase` |
| `seer_agent_availability_ratio` | Uptime ratio | `agent_id` |

### Retry & Circuit Breaker Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_retries_total` | Retry attempts | `agent_id`, `retry_reason` |
| `seer_agent_retry_exhausted_total` | Retries exhausted (final failure) | `agent_id` |
| `seer_circuit_breaker_state` | CB state (0=closed, 1=open, 2=half-open) | `agent_id`, `dependency` |
| `seer_circuit_breaker_trips_total` | CB trip events | `agent_id`, `dependency` |
| `seer_backpressure_rejections_total` | Requests rejected due to load | `agent_id` |

### Multi-Agent Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_delegation_total` | Agent-to-agent delegations | `from_agent`, `to_agent`, `status` |
| `seer_agent_delegation_latency_seconds` | Delegation round-trip time | `from_agent`, `to_agent` |
| `seer_cascade_depth` | Delegation chain depth | `root_agent` |
| `seer_cascade_failures_total` | Failures cascading from dependencies | `root_agent`, `failed_agent` |

### Cost Control Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_agent_cost_dollars` | Cost per agent | `agent_id` |
| `seer_agent_cost_per_request_dollars` | Cost efficiency | `agent_id` |
| `seer_budget_utilization_ratio` | Spend vs budget | `workbench`, `budget_type` |
| `seer_cost_anomaly_score` | Cost anomaly detection | `agent_id` |

---

## Dashboards

### Agentic Reliability Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENTIC SYSTEM RELIABILITY                               Refresh: 30s      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SYSTEM HEALTH                                                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │  Success    │ │  P99        │ │  Circuit    │ │  Cost       │           │
│  │  Rate       │ │  Latency    │ │  Breakers   │ │  Anomalies  │           │
│  │   98.7%     │ │   2.3s      │ │   2 open    │ │   0         │           │
│  │  target >99%│ │  target <3s │ │  ⚠ warning  │ │   ✓ normal  │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                              │
│  AGENT RELIABILITY (Bottom 10)                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Agent                    │ Success │ P99 Lat │ Retries │ CB State │   │
│  ├───────────────────────────┼─────────┼─────────┼─────────┼──────────┤   │
│  │  ⚠ payment-validator      │  94.2%  │  4.5s   │  12%    │  OPEN    │   │
│  │  ⚠ document-analyzer      │  96.1%  │  3.8s   │   8%    │  HALF    │   │
│  │  ● fraud-detector-v2      │  97.3%  │  2.9s   │   5%    │  CLOSED  │   │
│  │  ● customer-intent        │  98.1%  │  2.1s   │   3%    │  CLOSED  │   │
│  └───────────────────────────┴─────────┴─────────┴─────────┴──────────┘   │
│                                                                              │
│  RETRY ANALYSIS (Last 1h)                                                    │
│  ┌─────────────────────────────┐  ┌────────────────────────────────────┐   │
│  │  Retry Reasons              │  │  Retry Storm Detection             │   │
│  │  ████████ LLM Timeout  45%  │  │                                    │   │
│  │  █████ Tool Error      28%  │  │  Current: 234 retries/min          │   │
│  │  ███ Rate Limit        17%  │  │  Baseline: 180 retries/min         │   │
│  │  ██ Network Error      10%  │  │  Status: ⚠ Elevated (+30%)        │   │
│  └─────────────────────────────┘  └────────────────────────────────────┘   │
│                                                                              │
│  MULTI-AGENT TOPOLOGY                                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                       │   │
│  │    [orchestrator] ──► [analyzer] ──► [validator] ──► [notifier]      │   │
│  │          │                 │              ⚠                          │   │
│  │          └──► [enricher] ──┘          CB OPEN                        │   │
│  │                                                                       │   │
│  │    Max Cascade Depth: 4    Cascade Failures (1h): 12                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  COST CONTROL                                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Workbench: dispute-ops    Budget: $5,000/day    Spent: $3,421      │   │
│  │  ██████████████████████████████████░░░░░░░░░░░░░░  68.4%            │   │
│  │  Projection: $4,891 (within budget)                                  │   │
│  │                                                                       │   │
│  │  ⚠ High-cost agents:                                                 │   │
│  │    • fraud-case-resolution: $892 (18% of budget, 5% of requests)    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Cascade Failure Dashboard

- Multi-agent dependency graph (live)
- Failure propagation visualization
- Circuit breaker status by dependency
- Isolation boundary indicators

### Cost Runaway Dashboard

- Real-time spend rate
- Budget burn-down projection
- Per-agent cost breakdown
- Anomaly detection highlights

---

## Alerts

| Alert | Condition | Severity | Response |
|-------|-----------|----------|----------|
| **AgentSLABreach** | Success rate < 99% for 15m | Critical | Investigate failures, scale resources |
| **HighLatency** | P99 > 2x baseline for 10m | Warning | Check dependencies, LLM latency |
| **CircuitBreakerOpen** | CB open for > 5m | Warning | Investigate dependency, failover |
| **RetryStormDetected** | Retry rate > 2x baseline | Warning | Check root cause, enable backpressure |
| **CascadeFailure** | > 3 agents failing in chain | Critical | Isolate failure, break cascade |
| **CostAnomalyDetected** | Cost > 3σ from baseline | Warning | Investigate high-cost agent |
| **BudgetExhausted** | Spend > 100% of budget | Critical | Throttle agents, emergency budget |

---

## Operational Tools

| Tool | Purpose | Access |
|------|---------|--------|
| **Circuit Breaker Control** | Force open/close CBs | Watch Console |
| **Load Shedder** | Enable/configure backpressure | Watch Console |
| **Agent Throttle** | Limit request rate per agent | Watch Console |
| **Cascade Isolator** | Disable delegation to failing agent | Watch Console |
| **Budget Override** | Emergency budget increase | Watch Console (requires approval) |
| **Cost Kill-Switch** | Immediately halt high-cost agent | Watch Console (requires approval) |

---

# Persona 4: Security Architect (AI-focused)

> *Tool access control, prompt injection defense, data exfiltration prevention.*

## Responsibilities

- Monitor and prevent prompt injection attacks
- Ensure tool access control compliance
- Detect data exfiltration attempts
- Audit sensitive operations

---

## Metrics

### Tool Access Control Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_tool_access_denied_total` | Tool access denials | `agent_id`, `tool_id`, `reason` |
| `seer_tool_access_granted_total` | Tool access grants | `agent_id`, `tool_id` |
| `seer_tool_sensitive_invocations_total` | Sensitive tool usage | `agent_id`, `tool_id`, `sensitivity_level` |
| `seer_authority_escalation_attempts_total` | Escalation attempts | `agent_id`, `requested_scope` |
| `seer_credential_usage_total` | Credential access | `agent_id`, `credential_type` |

### Prompt Security Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_prompt_injection_detections_total` | Injection attempts detected | `agent_id`, `detection_type` |
| `seer_prompt_injection_blocked_total` | Injections blocked | `agent_id`, `block_reason` |
| `seer_jailbreak_attempts_total` | Jailbreak attempts | `agent_id`, `method` |
| `seer_prompt_validation_failures_total` | Prompt validation failures | `agent_id`, `validation_rule` |

### Data Security Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_pii_access_total` | PII data access | `agent_id`, `pii_type` |
| `seer_data_exfiltration_blocked_total` | Exfiltration attempts blocked | `agent_id`, `destination` |
| `seer_output_sanitization_applied_total` | Output sanitization events | `agent_id`, `sanitization_type` |
| `seer_guardrail_blocks_total` | Guardrail-blocked operations | `agent_id`, `guardrail_id`, `reason` |

### Audit Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_sensitive_decision_total` | High-impact decisions | `agent_id`, `decision_type` |
| `seer_human_override_total` | Human overrides of AI decisions | `agent_id`, `override_type` |
| `seer_audit_log_writes_total` | Audit log entries created | `agent_id`, `log_category` |

---

## Dashboards

### AI Security Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AI SECURITY OPERATIONS                                   Refresh: 1m       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SECURITY STATUS                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │  Injection  │ │  Access     │ │  Data       │ │  Guardrail  │           │
│  │  Attempts   │ │  Denials    │ │  Exfil      │ │  Blocks     │           │
│  │    23/24h   │ │   156/24h   │ │    0/24h    │ │   89/24h    │           │
│  │  ▲ +5       │ │  ◄► normal  │ │   ✓ clear   │ │  ▼ -12      │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                              │
│  PROMPT INJECTION ANALYSIS                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Detection Type              │ Count │ Blocked │ Escalated         │   │
│  ├──────────────────────────────┼───────┼─────────┼───────────────────┤   │
│  │  Direct injection            │   12  │   12    │   3               │   │
│  │  Indirect injection (RAG)    │    5  │    5    │   2               │   │
│  │  Jailbreak attempt           │    4  │    4    │   4               │   │
│  │  Prompt leakage attempt      │    2  │    2    │   1               │   │
│  └──────────────────────────────┴───────┴─────────┴───────────────────┘   │
│                                                                              │
│  TOOL ACCESS PATTERNS                                                        │
│  ┌─────────────────────────────┐  ┌────────────────────────────────────┐   │
│  │  Sensitive Tools Used       │  │  Access Denials by Reason          │   │
│  │                             │  │                                    │   │
│  │  • payment.transfer: 234    │  │  ███████ Scope exceeded    45%     │   │
│  │  • pii.retrieve: 156        │  │  █████ Not authorized      32%     │   │
│  │  • admin.config: 12         │  │  ███ Rate limited          18%     │   │
│  │  • external.api: 89         │  │  █ Revoked                  5%     │   │
│  └─────────────────────────────┘  └────────────────────────────────────┘   │
│                                                                              │
│  DATA PROTECTION                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                       │   │
│  │  PII Access (by type, 24h):                                          │   │
│  │  • SSN: 45 (all authorized) ✓                                        │   │
│  │  • Credit Card: 234 (all masked in logs) ✓                           │   │
│  │  • Email: 1,234 (12 access to external tools - reviewed) ⚠           │   │
│  │                                                                       │   │
│  │  Output Sanitization:                                                 │   │
│  │  • PII redacted from responses: 89 instances                         │   │
│  │  • Confidential data blocked: 3 instances                            │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  RECENT SECURITY EVENTS                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Time     │ Agent              │ Event                   │ Status   │   │
│  ├───────────┼────────────────────┼─────────────────────────┼──────────┤   │
│  │  14:23:01 │ customer-support   │ Injection blocked       │ Blocked  │   │
│  │  14:15:45 │ fraud-analyzer     │ Sensitive tool access   │ Allowed  │   │
│  │  14:12:33 │ unknown-agent      │ Auth escalation attempt │ Denied   │   │
│  │  14:08:12 │ data-enricher      │ External API (unusual)  │ Flagged  │   │
│  └───────────┴────────────────────┴─────────────────────────┴──────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Tool Access Audit Dashboard

- Tool access patterns over time
- Unusual access pattern detection
- Cross-agent tool access comparison
- Privilege escalation timeline

### Prompt Security Dashboard

- Injection attempt timeline
- Attack vector breakdown
- Agent vulnerability scores
- Mitigation effectiveness

---

## Alerts

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

## Operational Tools

| Tool | Purpose | Access |
|------|---------|--------|
| **Agent Isolator** | Immediately isolate agent from network | Watch Console (emergency) |
| **Credential Revoker** | Revoke agent credentials | Watch Console |
| **Guardrail Configurator** | Update guardrail rules | Workbench Studio |
| **Audit Log Viewer** | Deep-dive audit trail analysis | Watch Console |
| **Injection Pattern Analyzer** | Analyze injection attempt patterns | Watch Console |
| **Tool Access Reviewer** | Review and approve tool access requests | Watch Console |

---

# Cross-Persona: Unified Operations View

## Seer Platform Operations Dashboard

A unified view for on-call engineers combining all personas:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SEER PLATFORM OPERATIONS CENTER                          On-call: @alice   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  ACTIVE ALERTS                                                        │   │
│  │  🔴 CRITICAL: CircuitBreakerOpen - payment-validator (5m ago)        │   │
│  │  🟡 WARNING:  HighLatency - fraud-analyzer P99 > 4s (12m ago)        │   │
│  │  🟡 WARNING:  BudgetThreshold - dispute-ops at 75% (1h ago)          │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  PLATFORM    │  LLMOPS      │  RELIABILITY  │  SECURITY                     │
│  ──────────  │  ──────────  │  ──────────── │  ──────────                    │
│  Agents: 127 │  Cost: $1.6k │  Success: 98% │  Inj Blocks: 23               │
│  Healthy: 98%│  Tokens: 28M │  P99 Lat: 2.3s│  Tool Denials: 156            │
│  Tools: 342  │  Fallbacks: 2│  CBs Open: 2  │  Exfil: 0                     │
│                                                                              │
│  [Platform] [LLMOps] [Reliability] [Security] [All Dashboards ▼]            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Implementation Notes

### Watch Extension Deployment

Extensions are deployed as:
1. **Grafana Dashboard JSONs** — Pre-built dashboards
2. **Prometheus Recording Rules** — Derived metrics
3. **Alertmanager Configurations** — Alert routing
4. **Custom Watch Plugins** — Operational tools UI

### Metric Collection Architecture

```yaml
# Seer components expose Prometheus metrics
# Collected by Watch's Prometheus instances
# Recording rules compute derived metrics
# Dashboards query Prometheus
# Alerts evaluated by Alertmanager
```

---

## Related Documentation

- [Agent Observability](./agent-observability.md) — SDK and agent-level instrumentation
- [Model Gateway](./model-gateway.md) — LLM routing and metrics source
- [Guardrails](./guardrails.md) — Security guardrail implementation
- [Authority Enforcement](./authority-enforcement.md) — OPA policy enforcement
- [Runtime Deployment](../agent-runtime/runtime-deployment.md) — Atlantis infrastructure
- [ADR-0076: Observability via Watch](../../../olympus-hub-docs/decision-logs/0076-seer-observability-watch-based.md)

---

*Seer Observability Extensions to Watch provide comprehensive platform-level monitoring for AI Platform Engineers, LLMOps Engineers, Agentic System SREs, and AI Security Architects.*

