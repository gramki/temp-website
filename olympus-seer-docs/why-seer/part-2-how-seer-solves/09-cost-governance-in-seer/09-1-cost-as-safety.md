# 9.1 Cost as Safety Signal

In enterprise AI agents, cost is more than a financial metric—it's a critical operational health and safety signal. A sudden spike in cost often indicates something has gone wrong.

## Why Cost Signals Problems

| Cost Pattern | Potential Problem |
|--------------|-------------------|
| **Sudden spike** | Reasoning loop, retry storm |
| **Steady increase** | Prompt drift, inefficiency |
| **High variance** | Unpredictable behavior |
| **Exceeds budget** | Unauthorized activity, attack |

## How Agents Spend Money

Unlike traditional software with predictable compute costs, agents have unbounded spending potential:

```
Each Reasoning Turn:
├── Model call: $0.01 - $0.10
├── × Turns per request: 1-20+
├── × Retries on failure: 1-5
├── + Tool calls: $0.001 - $1.00 each
├── + Embedding lookups: $0.0001 per
└── = Highly variable total
```

A simple request might cost $0.05. A complex one might cost $5.00. An agent stuck in a loop might cost $500+ before anyone notices.

## Cost Anomalies

### Reasoning Loops

Agent gets stuck thinking:

```yaml
loop_cost_pattern:
  normal_turns: 3-5
  loop_detected: 15+ turns
  normal_cost: $0.10
  loop_cost: $2.00+
  
  detection:
    - same_tool_repeated
    - no_progress
    - escalating_token_count
    
  action: terminate_and_alert
```

### Retry Storms

Failed tool calls trigger retries:

```yaml
retry_storm_pattern:
  normal_retries: 1-2
  storm_detected: 10+ retries
  
  cause:
    - external_api_down
    - bad_credentials
    - incorrect_parameters
    
  cost_impact: 10x-100x normal
  action: circuit_breaker
```

### Prompt Injection/Jailbreak

Malicious input causes expensive behavior:

```yaml
attack_pattern:
  indicators:
    - unusual_tool_calls
    - high_token_output
    - repeated_attempts
    
  cost_impact: variable, potentially extreme
  action: block_and_investigate
```

## Cost Monitoring for Safety

### Real-Time Alerts

```yaml
cost_alerts:
  - name: cost_spike
    condition: cost_per_minute > 5x baseline
    action: alert + investigate
    
  - name: budget_warning
    condition: budget_utilization > 80%
    action: alert
    
  - name: budget_critical
    condition: budget_utilization > 100%
    action: throttle + alert
    
  - name: anomaly
    condition: cost_pattern_unusual
    action: alert + possible_kill_switch
```

### Automatic Actions

```yaml
automatic_actions:
  on_cost_spike:
    - log_event
    - alert_operators
    - if: spike > 10x
      then: throttle_agent
    - if: spike > 50x
      then: kill_switch
      
  on_budget_exceeded:
    - block_new_requests
    - complete_in_flight
    - alert_operators
```

## The Safety Principle

> **If an agent can spend unlimited money without triggering an alert or intervention, it is not production-ready.**

This principle drives Seer's cost governance:

1. All costs are tracked in real-time
2. Anomalies trigger alerts
3. Hard ceilings enforce limits
4. Kill switches provide emergency stop

---

**References:**
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-11-cost-requirements.md`
*   `olympus-seer-docs/seer-design/personas-and-needs/are.md`

