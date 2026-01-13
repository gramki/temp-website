# Request Sentinel Example: Token Usage Governance

> **Status**: 🟢 Complete  
> **Last Updated**: 2026-01-14

This example demonstrates a complete Request Sentinel configuration for token usage governance. The sentinel monitors AI agent token consumption across requests and intervenes when budgets are exceeded.

---

## Use Case

**Problem**: AI agents in the Dispute Operations workbench consume tokens unpredictably. The organization needs to:
- Monitor token usage in real-time
- Flag when budgets are approached (80% threshold)
- Escalate when budgets are exceeded (100% threshold)
- Create governance records for audit

**Solution**: Deploy a Request Sentinel that:
- Auto-enrolls in all requests in the workbench
- Monitors REQUEST_UPDATE events for token metrics
- Takes action when thresholds are breached

---

## Complete Specification Set

### 1. SentinelSpec

The top-level specification that defines the sentinel type and references the three SentinelScenarioSpec CRDs:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: token-usage-governance-sentinel
  namespace: acme-disputes
  labels:
    workbench: acme-disputes
    sentinel-type: request
    category: governance
spec:
  # Sentinel Type
  type: request  # realtime | analytical | request
  
  # Target Scope
  target:
    workbench_ids: ["acme-disputes"]
  
  # Reference to Sentinel Scenario Specs
  sentinel_scenario_specs:
    normative_ref:
      name: token-usage-governance-normative
      version: "1.0.0"
    automation_ref:
      name: token-usage-governance-automation
      version: "1.0.0"
    deployment_ref:
      name: token-usage-governance-deployment
      version: "1.0.0"
```

---

### 2. SentinelScenarioNormativeSpec

Defines the goals, roles, SOPs, and decision criteria for the sentinel:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioNormativeSpec
metadata:
  name: token-usage-governance-normative
  namespace: acme-disputes
  labels:
    workbench: acme-disputes
    sentinel: token-usage-governance
spec:
  # Identity
  scenario:
    name: token-usage-governance
    display_name: "Token Usage Governance"
    version: "1.0.0"
    workbench_ref: acme-disputes

  # Goals and Success Criteria
  goals:
    primary:
      description: "Monitor and govern AI agent token usage to ensure cost compliance"
      success_criteria:
        - metric: budget_violations_detected
          target: "100%"
          description: "All budget violations detected in real-time"
        - metric: false_positive_rate
          target: "< 5%"
          description: "Minimize false positive alerts"
        - metric: intervention_latency_ms
          target: "< 5000"
          description: "Detect and act within 5 seconds"
    
    secondary:
      - description: "Provide actionable cost optimization insights"
        success_criteria:
          - metric: recommendation_acceptance_rate
            target: ">= 60%"

  # Agent Roles
  agent_roles:
    - id: token-monitor
      name: "Token Usage Monitor"
      description: "Monitors token consumption and enforces budgets"
      tasks:
        - observe-token-metrics
        - evaluate-thresholds
        - generate-alerts
        - escalate-violations
      decision_authority:
        - flag_approaching_budget: true
        - flag_exceeded_budget: true
        - escalate_to_supervisor: true
        - recommend_throttling: true

  # Standard Operating Procedures
  sops:
    - id: token-monitoring-sop
      name: "Token Usage Monitoring Procedure"
      description: "Standard procedure for monitoring and governing token usage"
      steps:
        - id: receive-update
          action: "Receive REQUEST_UPDATE notification"
          expected_outcome: "Token usage metrics extracted from update payload"
        
        - id: calculate-usage
          action: "Calculate cumulative token usage for request"
          expected_outcome: "Current usage percentage against budget determined"
        
        - id: evaluate-threshold
          action: "Compare usage against configured thresholds"
          expected_outcome: "Classification: normal | approaching | exceeded"
        
        - id: take-action
          action: "Execute appropriate action based on classification"
          expected_outcome: |
            - Normal: Log and continue monitoring
            - Approaching (>80%): Add memo with warning
            - Exceeded (>=100%): Escalate to supervisor
      
      references:
        - "knowledge://seer/token-governance-policy"
        - "knowledge://seer/cost-management-guidelines"

  # Decision Criteria
  decision_criteria:
    - id: approaching-threshold
      name: "Approaching Budget Threshold"
      description: "Token usage approaching but not exceeding budget"
      rules:
        - condition: "usage_percentage >= 80 AND usage_percentage < 100"
          action: "Add warning memo to request"
          severity: "warning"
    
    - id: exceeded-threshold
      name: "Exceeded Budget Threshold"
      description: "Token usage has exceeded budget"
      rules:
        - condition: "usage_percentage >= 100"
          action: "Escalate to supervisor"
          severity: "critical"

  # Evidence Requirements
  evidence_requirements:
    - type: token_metrics
      description: "Token consumption data from each monitored update"
      retention_days: 90
    
    - type: threshold_evaluation
      description: "Record of threshold evaluation and classification"
      retention_days: 90
    
    - type: governance_action
      description: "Record of actions taken (memos, escalations)"
      retention_days: 365

  # Escalation Rules
  escalation_rules:
    - id: budget-exceeded
      trigger: "Token budget exceeded (>=100%)"
      escalate_to: supervisor
      notification: immediate
      priority: high
      evidence_required:
        - token_metrics
        - budget_configuration
```

---

### 3. SentinelScenarioAutomationSpec

Defines the automation, tools, and enrollment filters:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioAutomationSpec
metadata:
  name: token-usage-governance-automation
  namespace: acme-disputes
  labels:
    workbench: acme-disputes
    sentinel: token-usage-governance
spec:
  # Reference to Normative Spec
  normative_ref:
    name: token-usage-governance-normative
    version: "1.0.0"

  # Hub Application Binding
  application:
    ref: token-usage-governance-agent
    version: "1.0.0"
    runtime: seer

  # Triggers (empty for Request Sentinels - enrollment-based)
  triggers: []

  # Tool Bindings
  tools:
    # Analytics access
    - id: get-token-metrics
      tool_ref: hub://agent-analytics/token-metrics
      description: "Retrieve detailed token metrics for request/session"
      permissions:
        - read
    
    # Request context access
    - id: get-request-context
      tool_ref: hub://request-management/get-context
      description: "Retrieve request context and metadata"
      permissions:
        - read
    
    # Action tools
    - id: add-memo
      tool_ref: hub://request-management/add-memo
      description: "Add governance memo to request"
      permissions:
        - write
    
    - id: create-observation
      tool_ref: hub://cronus/add-observation
      description: "Create governance observation in Cronus"
      permissions:
        - write
    
    - id: escalate
      tool_ref: hub://task-management/escalate
      description: "Escalate to supervisor"
      permissions:
        - write

  # AI Agent Configuration
  ai_agent:
    model:
      provider: bedrock
      model_id: anthropic.claude-3-haiku  # Lightweight model for governance
    
    system_prompt_ref: "prompts://seer/token-governance-sentinel"
    
    guardrails:
      - id: read-mostly
        enabled: true
        config:
          allow_writes_for:
            - add-memo
            - create-observation
            - escalate
    
    memory:
      conversation_memory: false  # Stateless monitoring
      working_memory: true        # Track within session
      entity_memory: false

  # ═══════════════════════════════════════════════════════════════════════════
  # SENTINEL-SPECIFIC SECTION
  # ═══════════════════════════════════════════════════════════════════════════
  sentinel:
    participation:
      # Participation Mode
      mode: observe_and_participate  # observe | participate | observe_and_participate

      # Enrollment Filters
      filters:
        # Monitor all scenarios except test scenarios
        scenario_whitelist: []  # Empty = all scenarios
        
        scenario_blacklist:
          - internal-test
          - sandbox-scenario
          - load-test
        
        # Enroll on updates that contain token metrics
        on_request_update:
          enabled: true
          
          # OPA Policy for filtering updates
          update_filter_policy: |
            package seer.sentinel.token_governance.enrollment
            
            default allow = false
            
            # Enroll when a Seer agent is first assigned
            allow {
              input.update_type == "TASK_LIFECYCLE"
              input.payload.task.agent_type == "seer"
              input.payload.task.lifecycle_event == "ASSIGNED"
            }
            
            # Enroll when token usage metrics are reported
            allow {
              input.update_type == "PROGRESS"
              input.payload.metrics.token_usage != null
            }
            
            # Enroll on any model invocation completion
            allow {
              input.update_type == "PROGRESS"
              input.payload.event_type == "MODEL_RESPONSE"
            }
```

---

### 4. SentinelScenarioDeploymentSpec

Defines deployment configuration, limits, and notification settings:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
metadata:
  name: token-usage-governance-deployment
  namespace: acme-disputes
  labels:
    workbench: acme-disputes
    sentinel: token-usage-governance
spec:
  # Reference to Automation Spec
  automation_ref:
    name: token-usage-governance-automation
    version: "1.0.0"

  # Activation Settings
  activation:
    status: active
    effective_from: "2026-01-01T00:00:00Z"
    effective_to: null  # No end date

  # Task Queues (internal for sentinel processing)
  task_queues:
    - task_type: sentinel-governance
      queue_ref: governance-internal-queue
      priority_override: low  # Don't compete with production work

  # SLA Parameters
  sla:
    per_task:
      - task_type: sentinel-governance
        target_hours: 0.05  # 3 minutes max for sentinel to process

  # Agent Enrollment
  agent_enrollment:
    auto_enroll:
      - role: token-monitor
        task_types:
          - sentinel-governance
    enrollment_mode: automatic

  # Capacity Planning
  capacity:
    expected_daily_volume: 5000  # Expected monitored requests
    peak_multiplier: 3.0

    scaling:
      auto_scale_ai_agents: true
      min_ai_agents: 1
      max_ai_agents: 3

  # ═══════════════════════════════════════════════════════════════════════════
  # SENTINEL-SPECIFIC DEPLOYMENT SECTION
  # ═══════════════════════════════════════════════════════════════════════════
  sentinel_deployment:
    # Auto-Activation
    auto_activate: true

    # Enrollment Limits
    enrollment_limits:
      max_concurrent_requests: 200
      cooldown_after_enrollment_ms: 500
      max_child_requests_per_parent: 1

    # Notification Delivery
    notification_delivery:
      method: webhook
      
      retry_policy:
        max_attempts: 3
        initial_delay_ms: 500
        max_delay_ms: 10000
        backoff_multiplier: 2.0
      
      timeout_ms: 3000

    # Child Request Configuration
    child_request:
      scenario_ref: token-usage-governance
      inherit_context: true
      cascade_completion: true
      cascade_cancellation: true

    # Resource Limits for Sentinel
    resource_limits:
      token_budget:
        per_request: 2000    # Sentinel shouldn't use many tokens
        per_day: 50000       # Daily cap across all monitored requests
      
      execution_time:
        per_observation_seconds: 15
        per_request_seconds: 120
```

---

### 5. HubApplicationSpec

The Hub Application that references the Trained Agent:

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: token-usage-governance-agent
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench: acme-disputes
    hub.olympus.io/runtime: seer
    seer.olympus.io/resource-type: trained-agent
    seer.olympus.io/agent-type: specialist
spec:
  application:
    name: token-usage-governance-agent
    display_name: "Token Usage Governance Agent"
    version: "1.0.0"
    description: "AI sentinel for monitoring and governing token usage across requests"

  runtime:
    type: seer
    version: "1.0.0"

  # Reference to Seer TrainingSpec
  seerTrainingRef:
    name: token-usage-governance-training-v1
    namespace: acme-disputes
    version: "1.0.0"

  dependencies:
    tools:
      - protocol: agent-analytics/token-metrics
      - protocol: request-management/get-context
      - protocol: request-management/add-memo
      - protocol: cronus/add-observation
      - protocol: task-management/escalate
```

---

## Enrollment Flow Example

When a dispute request is created and processed:

```
1. Signal arrives: New dispute submitted
2. Request Factory creates: req-dispute-001 (standard-dispute scenario)
3. Signal Exchange queries: Active Request Sentinels for acme-disputes
4. Sentinel matches:
   - Scenario "standard-dispute" not in blacklist ✓
   - Scenario whitelist empty (all scenarios) ✓
5. Child request created: req-sentinel-001 (token-usage-governance scenario)
6. Sentinel notified via webhook

Later, as the dispute agent works:

7. Dispute agent invokes model → REQUEST_UPDATE with token metrics
8. Signal Exchange evaluates update_filter_policy:
   - input.update_type == "PROGRESS" ✓
   - input.payload.metrics.token_usage != null ✓
   - Policy returns: allow = true
9. (Sentinel already enrolled → just notify)
10. Sentinel receives update:
    - Extracts token_usage: 3500 tokens
    - Compares to budget: 4000 tokens (87.5%)
    - Classification: APPROACHING
    - Action: Add warning memo

11. Dispute agent invokes model again → REQUEST_UPDATE
12. Sentinel receives update:
    - Cumulative usage: 4200 tokens (105%)
    - Classification: EXCEEDED
    - Action: Escalate to supervisor
```

---

## Webhook Notification Example

The notification delivered to the sentinel for each REQUEST_UPDATE:

```json
{
  "notification_id": "notif-abc123",
  "sentinel_id": "token-usage-governance-sentinel",
  "child_request_id": "req-sentinel-001",
  "parent_request_id": "req-dispute-001",
  
  "enrollment_context": {
    "trigger": "on_request_update",
    "scenario_id": "standard-dispute",
    "workbench_id": "acme-disputes",
    "enrolled_at": "2026-01-14T10:30:00Z"
  },
  
  "update": {
    "update_id": "upd-xyz789",
    "update_type": "PROGRESS",
    "timestamp": "2026-01-14T10:35:00Z",
    
    "payload": {
      "event_type": "MODEL_RESPONSE",
      "metrics": {
        "token_usage": {
          "prompt_tokens": 1800,
          "completion_tokens": 700,
          "total_tokens": 2500
        }
      },
      "session_id": "sess-456",
      "model_id": "anthropic.claude-3-sonnet"
    }
  },
  
  "cumulative_metrics": {
    "total_tokens_this_request": 3500,
    "budget_remaining": 500,
    "budget_percentage_used": 87.5
  }
}
```

---

## Related Documentation

- [Sentinel Spec Manager](../sentinel-spec-manager.md) — SentinelSpec structure and validation
- [Sentinel Scenario Normative Spec](../sentinel-scenario-normative-spec.md) — Normative specification pattern
- [Sentinel Scenario Automation Spec](../sentinel-scenario-automation-spec.md) — Automation with sentinel filters
- [Sentinel Scenario Deployment Spec](../sentinel-scenario-deployment-spec.md) — Deployment configuration
- [ADR-0116: Request Sentinel Type](../../../../olympus-hub-docs/decision-logs/0116-request-sentinel-type.md) — Design decision

---

*This example demonstrates a complete Token Usage Governance Request Sentinel with all required specifications.*
