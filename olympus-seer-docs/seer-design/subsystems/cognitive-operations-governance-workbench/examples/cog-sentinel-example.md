# COG Sentinel Example: Token Usage Governance

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14

---

## Overview

This example demonstrates a complete COG Sentinel configuration for Token Usage Governance, including all three SentinelScenarioSpec types, cogSpec patterns, and TrainingSpec with context compilation.

---

## Use Case

**Token Usage Governance** monitors and enforces token budgets across all workbenches in a subscription. The COG Sentinel:

- Observes token usage metrics from all requests
- Flags requests exceeding budget thresholds
- Creates governance tickets for budget violations
- Provides aggregated token usage analytics

---

## COGW Workbench

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: acme-cogw
  namespace: acme-subscription
  labels:
    hub.olympus.io/workbench-type: cogw
spec:
  domain: cognitive-governance
  description: "ACME Cognitive Operations Governance Workbench"
  
  workbench_type: cogw
  dev_lifecycle_stage: PROD
  
  scenarios:
    - id: token-usage-governance
      name: "Token Usage Governance"
      application_id: token-governance-app
```

---

## SentinelSpec

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: token-governance-sentinel
  namespace: acme-cogw
  labels:
    sentinel.olympus.io/cog-sentinel: "true"
    workbench: acme-cogw
spec:
  type: request
  
  target:
    workbench_ids: ["acme-cogw"]
  
  sentinel_scenario_specs:
    normative_ref:
      name: token-governance-normative
      version: "1.0.0"
    automation_ref:
      name: token-governance-automation
      version: "1.0.0"
    deployment_ref:
      name: token-governance-deployment
      version: "1.0.0"
```

---

## SentinelScenarioNormativeSpec

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioNormativeSpec
metadata:
  name: token-governance-normative
  namespace: acme-cogw
  labels:
    workbench: acme-cogw
    scenario: token-usage-governance
spec:
  scenario:
    name: token-usage-governance
    display_name: "Token Usage Governance"
    version: "1.0.0"
    workbench_ref: acme-cogw
  
  goals:
    primary:
      description: "Ensure token usage across all agents adheres to budget limits"
      success_criteria:
        - metric: budget_adherence_rate
          target: ">= 95%"
        - metric: violation_detection_latency
          target: "< 5 minutes"
    secondary:
      - description: "Identify agents with consistently high token usage"
        success_criteria:
          - metric: anomaly_detection_accuracy
            target: ">= 90%"
  
  agent_roles:
    - id: token-governance-agent
      name: "Token Governance Agent"
      description: "Monitors and governs token usage across workbenches"
      tasks:
        - monitor-token-metrics
        - evaluate-budget-compliance
        - flag-violations
        - create-governance-tickets
      decision_authority:
        - flag_requests_over: 100  # tokens
        - escalate_requests_over: 500
  
  standard_operating_procedures:
    - id: token-monitoring
      name: "Monitor Token Usage"
      description: "Continuously monitor token consumption"
      steps:
        - "Subscribe to request updates with token metrics"
        - "Compare against workbench and scenario budgets"
        - "Track cumulative usage per agent/scenario"
    
    - id: violation-handling
      name: "Handle Budget Violations"
      description: "Process and escalate budget violations"
      steps:
        - "Classify violation severity (warning, critical)"
        - "Create governance ticket with evidence"
        - "Notify workbench admin if critical"
  
  decision_criteria:
    - id: budget-warning
      name: "Budget Warning Threshold"
      description: "Flag when token usage exceeds 80% of budget"
      condition: "request.metrics.token_usage > budget * 0.8"
      action: "create_warning_ticket"
    
    - id: budget-violation
      name: "Budget Violation"
      description: "Escalate when token usage exceeds budget"
      condition: "request.metrics.token_usage > budget"
      action: "escalate_to_admin"
  
  evidence_requirements:
    - id: token-usage-log
      description: "Detailed token usage breakdown by model call"
      required_for:
        - budget-warning
        - budget-violation
  
  status: active
```

---

## SentinelScenarioAutomationSpec

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioAutomationSpec
metadata:
  name: token-governance-automation
  namespace: acme-cogw
  labels:
    workbench: acme-cogw
    scenario: token-usage-governance
spec:
  normative_ref:
    name: token-governance-normative
    version: "1.0.0"
  
  application:
    ref: token-governance-app
    version: "1.0.0"
    runtime: seer
  
  triggers:
    - ref: request-update-trigger
      required: true
  
  ai_agent:
    model:
      provider: bedrock
      model_id: anthropic.claude-3-sonnet
    system_prompt_ref: "prompts://governance/token-usage-agent"
  
  # Sentinel-specific configuration
  sentinel:
    participation:
      mode: observe_and_participate
      
      filters:
        # Monitor all scenarios
        scenario_whitelist:
          - "*"
        
        # Exclude internal testing scenarios
        scenario_blacklist:
          - "internal-testing"
          - "development-*"
          - "sandbox-*"
        
        # OPA policy for fine-grained filtering
        on_request_update:
          enabled: true
          update_filter_policy: |
            package seer.sentinel.token_governance_filter
            
            default allow = false
            
            # Allow if token usage metrics are reported
            allow {
              input.payload.metrics.token_usage != null
            }
            
            # Allow if token cost is reported
            allow {
              input.payload.metrics.token_cost != null
            }
            
            # Allow if request is completed (for final tallying)
            allow {
              input.payload.status == "completed"
            }
            
            # Allow if token cost exceeds threshold (immediate attention)
            allow {
              input.payload.metrics.token_cost > 50
            }
```

---

## SentinelScenarioDeploymentSpec

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
metadata:
  name: token-governance-deployment
  namespace: acme-cogw
  labels:
    workbench: acme-cogw
    scenario: token-usage-governance
spec:
  automation_ref:
    name: token-governance-automation
    version: "1.0.0"
  
  activation:
    status: active
    effective_from: "2026-01-01T00:00:00Z"
  
  agent_enrollment:
    auto_enroll:
      - role: token-governance-agent
        task_types:
          - sentinel-observation
          - governance-action
    enrollment_mode: automatic
  
  capacity:
    expected_daily_volume: 10000  # Expected token events per day
    peak_multiplier: 2.0
    scaling:
      auto_scale_ai_agents: true
      min_ai_agents: 1
      max_ai_agents: 5
  
  # Sentinel-specific deployment configuration
  sentinel_deployment:
    auto_activate: true
    
    enrollment_limits:
      max_concurrent_requests: 500
      cooldown_after_enrollment_ms: 500
      max_child_requests_per_parent: 1
    
    notification_delivery:
      method: webhook
      retry_policy:
        max_attempts: 3
        initial_delay_ms: 1000
        max_delay_ms: 30000
        backoff_multiplier: 2.0
      timeout_ms: 5000
    
    child_request:
      scenario_ref: token-usage-governance
      inherit_context: true
      cascade_completion: true
      cascade_cancellation: true
    
    resource_limits:
      token_budget:
        per_request: 2000
        per_day: 50000
      execution_time:
        per_observation_seconds: 15
        per_request_seconds: 120
  
  # ═══════════════════════════════════════════════════════════════════════════
  # COG SENTINEL TARGETING CONFIGURATION
  # ═══════════════════════════════════════════════════════════════════════════
  cogSpec:
    workbench_patterns:
      # Exclude non-production workbenches
      - pattern: "dev-*"
        action: disallow
      - pattern: "test-*"
        action: disallow
      - pattern: "sandbox-*"
        action: disallow
      
      # Exclude other COGW workbenches
      - pattern: "*-cogw"
        action: disallow
      
      # Allow all production workbenches
      - pattern: "production-*"
        action: allow
      
      # Allow specific named workbenches
      - pattern: "acme-loans"
        action: allow
      - pattern: "acme-payments"
        action: allow
      - pattern: "acme-disputes"
        action: allow
```

---

## HubApplicationSpec

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: token-governance-app
  namespace: acme-cogw
spec:
  display_name: "Token Governance Agent"
  description: "AI agent for monitoring and governing token usage"
  version: "1.0.0"
  runtime: seer
  
  seerTrainingRef:
    name: token-governance-trained-agent
    version: "1.0.0"
  
  capabilities:
    - observe-requests
    - participate-in-requests
    - create-child-requests
    - create-governance-tickets
  
  endpoints:
    webhook:
      path: "/seer/sentinel/token-governance/webhook"
      method: POST
      security:
        hmac_secret_ref:
          name: token-governance-webhook-secret
          key: webhook-secret
```

---

## TrainingSpec

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: token-governance-trained-agent
  namespace: acme-cogw
spec:
  rawAgent:
    name: governance-base
    version: "^1.0.0"
  
  context:
    identity:
      displayName: "Token Governance Agent"
      role: governance-sentinel
      domain: cognitive-governance
  
  behavioral:
    systemPrompt: |
      You are a Token Governance Agent responsible for monitoring and 
      enforcing token usage budgets across all workbenches in the organization.
      
      Your responsibilities:
      1. Monitor token usage metrics from incoming request updates
      2. Compare usage against configured budgets
      3. Flag violations and create governance tickets
      4. Provide insights on token consumption patterns
      
      You have access to:
      - Parent request context (from the workbench being monitored)
      - Historical token usage data
      - Budget configurations per workbench/scenario
      
      When you detect a violation:
      1. Classify severity (warning, critical)
      2. Document the evidence
      3. Create an appropriate governance ticket
      4. For critical violations, flag for immediate attention
    
    skillPrompts:
      - name: analyze-token-usage
        prompt: |
          Analyze the token usage metrics from the request update.
          Compare against the budget for this workbench and scenario.
          Determine if any thresholds are exceeded.
      
      - name: create-governance-ticket
        prompt: |
          Create a governance ticket for the detected violation.
          Include: workbench, scenario, agent, usage details, budget, overage.
  
  # Context compilation configuration
  contextCompilation:
    retrieverConfigs:
      # When task is created (initial enrollment)
      - selector:
          updateType: "task_created"
        retrievers:
          - type: hub_request_context
            purpose: "parent request context"
            include:
              - request_id
              - scenario
              - workbench_id
              - context_records
              - metrics
          - type: enterprise_memory
            purpose: "budget configurations"
            query: "token budgets workbench scenario"
            limit: 5
          - type: knowledge_base
            ref: "token-governance-policies"
            purpose: "governance policies"
        tokenBudget:
          total: 6000
          allocation:
            parent_context: 3000
            budgets: 1500
            policies: 1000
            reserve: 500
      
      # On token metrics update
      - selector:
          updateType: "context_update"
          contextKeys: ["token_metrics", "token_usage"]
        retrievers:
          - type: hub_request_context
            purpose: "token metrics"
            include:
              - metrics.token_usage
              - metrics.token_cost
              - metrics.model_calls
          - type: enterprise_memory
            purpose: "recent violations"
            query: "token violations this workbench"
            limit: 10
        tokenBudget:
          total: 4000
          allocation:
            metrics: 1500
            violations: 2000
            reserve: 500
      
      # Default fallback
      - selector: {}
        retrievers:
          - type: hub_request_context
            include:
              - request_id
              - scenario
              - workbench_id
        tokenBudget:
          total: 2000
  
  guardrails:
    refs:
      - name: pii-protection
        version: "^1.0.0"
    inline:
      - name: governance-action-limits
        type: decision-boundary
        config:
          maxTicketsPerHour: 100
          maxEscalationsPerHour: 10
```

---

## Result: Target Workbench View

When this COG Sentinel is deployed, the `production-loans` workbench will see:

```yaml
# Read-only copy in production-loans workbench
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: token-governance-sentinel
  namespace: production-loans
  labels:
    sentinel.olympus.io/cog-sentinel: "true"
  annotations:
    sentinel.olympus.io/read-only: "true"
    sentinel.olympus.io/cog-sentinel-source: "acme-cogw/token-governance-sentinel"
    sentinel.olympus.io/sync-timestamp: "2026-01-14T10:30:00Z"
spec:
  # ... full spec (read-only copy) ...
```

**Sentinel Directory Entry:**
```
Name: token-governance-sentinel
Type: Request Sentinel (COG)
Source: acme-cogw
Global Status: ● Active
Local Status: ● Active
Effective: ● Active
Actions: [Disable]
```

---

## Related Documentation

- [COG Sentinel Specification](../cog-sentinel-specification.md) — Specification details
- [COGW Operator](../cogw-operator.md) — Sync mechanism
- [Signal Forwarding](../signal-forwarding.md) — Signal flow
- [Administrative Controls](../administrative-controls.md) — Control model

---

*This example demonstrates a complete Token Usage Governance COG Sentinel with cross-workbench targeting and context-aware monitoring.*
