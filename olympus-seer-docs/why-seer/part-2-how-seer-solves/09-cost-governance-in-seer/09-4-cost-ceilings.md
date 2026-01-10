# 9.4 Cost Ceilings & Enforcement

Cost ceilings are hard limits that prevent runaway spending. Unlike soft budgets that alert, ceilings enforce—blocking requests that would exceed limits.

## Ceiling Hierarchy

```yaml
cost_ceiling_hierarchy:
  platform:
    daily: 1000000
    description: "Platform-wide emergency limit"
    
  tenant:
    daily: 50000
    monthly: 500000
    description: "Per-tenant allocation"
    
  workbench:
    daily: 5000
    monthly: 50000
    description: "Per-workbench allocation"
    
  agent:
    daily: 500
    per_request: 25
    description: "Per-agent limits"
```

Most restrictive ceiling applies at each level.

## Ceiling Types

### Time-Based Ceilings

```yaml
time_based:
  per_minute:
    enabled: true
    limit: 50
    action: throttle
    
  per_hour:
    enabled: true
    limit: 500
    action: alert_then_throttle
    
  per_day:
    enabled: true
    limit: 5000
    action: block_new_requests
    
  per_month:
    enabled: true
    limit: 100000
    action: block_new_requests
```

### Per-Request Ceilings

```yaml
per_request:
  hard_limit: 25
  action: terminate_request
  
  warning_threshold: 15
  action: log_and_monitor
```

## Enforcement Mechanism

### Pre-Request Check

```python
def check_cost_ceiling(request, agent):
    estimated_cost = estimate_cost(request)
    
    # Check per-request ceiling
    if estimated_cost > agent.per_request_ceiling:
        return CeilingExceeded("Request too expensive")
        
    # Check daily ceiling
    if agent.spent_today + estimated_cost > agent.daily_ceiling:
        return CeilingExceeded("Daily ceiling would be exceeded")
        
    # Check workbench ceiling
    if workbench.spent_today + estimated_cost > workbench.daily_ceiling:
        return CeilingExceeded("Workbench ceiling would be exceeded")
        
    return CeilingOK(remaining=calculate_remaining())
```

### In-Flight Monitoring

```yaml
in_flight_monitoring:
  check_interval: per_model_call
  
  actions:
    - if: cost > 50% of per_request_limit
      then: log_warning
      
    - if: cost > 75% of per_request_limit
      then: simplify_next_turn (use cheaper model)
      
    - if: cost > 100% of per_request_limit
      then: terminate_gracefully
```

## Actions on Ceiling Breach

### Graduated Response

```yaml
ceiling_actions:
  soft_threshold_80:
    actions:
      - alert: operators
      - log: warning
      - continue: yes
      
  soft_threshold_95:
    actions:
      - alert: operators + management
      - throttle: new_requests
      - continue: in_flight
      
  hard_ceiling_100:
    actions:
      - alert: all_stakeholders
      - block: new_requests
      - complete: in_flight (with limit)
      - fallback: cheaper_model (if configured)
      
  emergency_150:
    actions:
      - alert: critical
      - kill_switch: consider
```

### Fallback Strategies

```yaml
fallback_on_ceiling:
  model_downgrade:
    from: claude-3.5-sonnet
    to: gpt-4o-mini
    notify_user: true
    
  capability_reduction:
    disable:
      - complex_reasoning
      - multi_turn_exploration
    enable:
      - simple_responses
      - human_escalation
```

## Ceiling Audit

All ceiling events are logged:

```yaml
ceiling_event:
  timestamp: 2026-01-10T14:30:00Z
  
  ceiling:
    type: daily
    level: agent
    limit: 500
    current: 485
    
  request:
    agent: dispute-analyst-tier1
    estimated_cost: 25
    would_exceed: true
    
  action:
    taken: blocked
    reason: "Would exceed daily agent ceiling"
    notification: sent_to_operators
```

## Budget vs. Ceiling

| Aspect | Budget | Ceiling |
|--------|--------|---------|
| **Purpose** | Planning and tracking | Safety limit |
| **Enforcement** | Alert on exceed | Block on exceed |
| **Flexibility** | Can be increased | Requires approval |
| **Response** | Operational | Emergency |

```yaml
example:
  agent: dispute-analyst-tier1
  
  budget:
    daily: 400
    action_on_exceed: alert
    
  ceiling:
    daily: 500
    action_on_exceed: block
    
  # Agent can exceed budget (alert only)
  # Agent cannot exceed ceiling (blocked)
```

---

**References:**
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-11-cost-requirements.md`
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-3-authority-ceilings.md`

