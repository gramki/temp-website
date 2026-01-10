# 6.4 Kill Switches & Dual Control

Kill switches and dual control are emergency governance mechanisms for critical situations. While policy enforcement handles normal operations, these mechanisms provide last-resort controls when agents must be stopped or high-risk actions require multiple approvers.

## Kill Switches

### What Kill Switch Does

A kill switch is an immediate, authoritative mechanism to revoke agent authority:

| Kill Switch Action | Effect |
|--------------------|--------|
| **Credential revocation** | Agent cannot authenticate |
| **Policy enforcement** | All PEPs reject agent immediately |
| **Model gateway block** | LLM access denied |
| **Tool registry block** | All tool calls denied |
| **Memory access** | Read-only or denied |

### Kill Switch Scope

Kill switches can operate at different levels:

```yaml
kill_switch_levels:
  agent_instance:
    scope: "Single deployed agent"
    example: "dispute-analyst-tier1-acme-production"
    
  agent_class:
    scope: "All instances of an agent type"
    example: "dispute-analyst-tier1 (all tenants)"
    
  workbench:
    scope: "All agents in a workbench"
    example: "dispute-ops-prod"
    
  tenant:
    scope: "All agents for a tenant"
    example: "acme-bank"
    
  platform:
    scope: "All agents platform-wide"
    example: "Olympus Seer (emergency only)"
```

### Kill Switch Triggers

```yaml
kill_switch_triggers:
  manual:
    authorized_roles:
      - agent_reliability_engineer
      - security_incident_responder
      - platform_operator
      
  automated:
    - trigger: cost_anomaly_extreme
      threshold: 1000  # 10x normal
      scope: agent_instance
      
    - trigger: security_alert
      source: security_team
      scope: configurable
      
    - trigger: regulatory_order
      source: compliance_team
      scope: tenant
```

### Kill Switch Process

```
Trigger
    │
    ├──→ Authenticate authority
    │
    ├──→ Revoke credentials (Cipher IAM)
    │
    ├──→ Propagate to all PEPs
    │     • Model Gateway
    │     • Tool Registry
    │     • Memory Services
    │
    ├──→ Handle in-flight requests
    │     • Block new actions
    │     • Complete/rollback pending
    │
    ├──→ Create audit record
    │
    └──→ Alert stakeholders
```

### Kill Switch Recovery

Recovery requires explicit action:

```yaml
kill_switch_recovery:
  requirements:
    - investigation_complete: true
    - root_cause_identified: true
    - remediation_applied: true
    - approval:
        required_approvers:
          - agent_reliability_engineer
          - security_team (if security-related)
          - compliance (if regulatory)
        minimum_approvers: 2
        
  process:
    - verify_requirements
    - restore_credentials
    - enable_monitoring (heightened)
    - gradual_traffic_restoration
    - create_recovery_audit_record
```

## Dual Control

### What Dual Control Is

Dual control requires multiple independent approvers for high-risk actions:

```yaml
dual_control:
  principle: "No single person can authorize high-risk agent actions"
  
  applies_to:
    - agent_deployment_to_production
    - authority_ceiling_increase
    - guardrail_modification
    - kill_switch_recovery
    - bulk_agent_operations
```

### Dual Control Configuration

```yaml
dual_control_policy:
  - action: deploy_to_production
    required_approvers: 2
    approver_roles:
      - agent_engineer
      - agent_reliability_engineer
    same_role_allowed: false
    
  - action: modify_guardrails
    required_approvers: 2
    approver_roles:
      - agent_engineer
      - ai_risk_audit_owner
    same_role_allowed: false
    
  - action: increase_authority_ceiling
    required_approvers: 3
    approver_roles:
      - agent_engineer
      - business_owner
      - ai_risk_audit_owner
```

### Dual Control Workflow

```
Request Initiated
    │
    ▼
First Approver Reviews
    │
    ├── Reject → Request Denied
    │
    └── Approve → Pending Second Approval
                    │
                    ▼
              Second Approver Reviews
                    │
                    ├── Reject → Request Denied
                    │
                    └── Approve → Action Executed
                                    │
                                    ▼
                            Audit Record Created
```

### Dual Control Record

```yaml
dual_control_record:
  action_id: "dc-12345"
  action_type: deploy_to_production
  timestamp: 2026-01-10T10:00:00Z
  
  request:
    initiated_by: engineer@acme.com
    subject: dispute-analyst-tier1-v2.1
    target: production
    
  approvals:
    - approver: engineer@acme.com
      role: agent_engineer
      timestamp: 2026-01-10T10:05:00Z
      decision: approve
      
    - approver: are@acme.com
      role: agent_reliability_engineer
      timestamp: 2026-01-10T10:15:00Z
      decision: approve
      
  execution:
    timestamp: 2026-01-10T10:15:30Z
    status: success
```

## Break-Glass Procedures

For genuine emergencies where normal controls are too slow:

```yaml
break_glass:
  definition: "Emergency bypass of normal approval workflows"
  
  requirements:
    - declared_emergency: true
    - authorized_emergency_responder: true
    - immediate_notification: all_stakeholders
    - retrospective_review: mandatory_within_24h
    
  auditing:
    - all_actions_logged
    - full_context_captured
    - automatic_escalation_to_leadership
    
  example:
    action: emergency_kill_switch
    authorized_by: security_incident_responder
    reason: "Active security breach detected"
    normal_approvers_bypassed: true
    retrospective_required: true
```

## Audit Requirements

All emergency controls are heavily audited:

```yaml
emergency_audit:
  kill_switch:
    - who_initiated
    - authority_verified
    - scope_of_impact
    - in_flight_actions_affected
    - time_to_propagation
    - recovery_timeline
    
  dual_control:
    - all_approval_chain
    - timestamps
    - role_verification
    - any_rejections
    
  break_glass:
    - justification_detail
    - emergency_declaration
    - bypassed_controls
    - retrospective_findings
```

---

**References:**
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-4-kill-switch.md`
*   `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md`
