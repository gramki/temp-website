# ARAO REST Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Seer-Native  
> **Base Path:** `/api/seer/arao/v1`

---

## Overview

The ARAO Channel provides APIs for the **Agent Risk & Audit Officer (ARAO)** ([role definition](../../../personas-and-needs/roles.md#7-agent-risk--audit-officer-arao)) to manage autonomy governance, compliance policies, and security controls.

This is a **Seer-native channel** with no Hub equivalent.

---

## Endpoint Groups

### Autonomy Management

```
# Get autonomy levels
GET /autonomy/levels

# Get agent autonomy
GET /agents/{agent_id}/autonomy
Response: { current_level, ceiling, history }

# List autonomy requests
GET /autonomy/requests
Query: status, agent_class, sort, limit, cursor

# Get request detail
GET /autonomy/requests/{request_id}

# Process request
POST /autonomy/requests/{request_id}/decision
Body: { decision, conditions, notes }

# Get escalation rules
GET /agents/{agent_id}/escalation-rules

# Update escalation rules
PUT /agents/{agent_id}/escalation-rules
Body: { rules }
```

### Compliance

```
# Get compliance summary
GET /compliance/summary
Query: domain, period

# List policy rules
GET /compliance/policies
Query: domain, status, sort, limit, cursor

# Get policy detail
GET /compliance/policies/{policy_id}

# Create policy
POST /compliance/policies
Body: { name, domain, condition, action, enforcement }

# Update policy
PUT /compliance/policies/{policy_id}
Body: { condition, action, enforcement }

# Enable/disable policy
PATCH /compliance/policies/{policy_id}
Body: { status }

# Test policy
POST /compliance/policies/{policy_id}/test
Body: { test_context }

# List violations
GET /compliance/violations
Query: policy_id, agent_id, severity, period, limit, cursor

# Get violation detail
GET /compliance/violations/{violation_id}
```

### Audit Evidence

```
# Generate audit report
POST /audit/reports
Body: { period, scope, domains, contents, format }

# Get report status
GET /audit/reports/{report_id}

# Download report
GET /audit/reports/{report_id}/download

# Get decision audit trail
GET /audit/decisions
Query: agent_id, time_from, time_to, decision_type, limit, cursor

# Get decision detail
GET /audit/decisions/{decision_id}
```

### Security

```
# List tool permissions
GET /agents/{agent_id}/permissions
Query: status

# Grant permission
POST /agents/{agent_id}/permissions
Body: { tool_id, scope, granted_by }

# Revoke permission
DELETE /agents/{agent_id}/permissions/{permission_id}
Body: { reason }

# Get authority boundaries
GET /agents/{agent_id}/authority

# Update authority boundaries
PUT /agents/{agent_id}/authority
Body: { decision_authority, data_access }

# List authority violations
GET /security/violations
Query: agent_id, period, severity, limit, cursor

# Get violation detail
GET /security/violations/{violation_id}

# Get security events
GET /security/events
Query: type, agent_id, severity, period, limit, cursor
```

---

## Sample Requests

### Process Autonomy Request

```http
POST /api/seer/arao/v1/autonomy/requests/req-001/decision
Authorization: Bearer <token>
Content-Type: application/json

{
  "decision": "approve",
  "conditions": [
    "Maintain escalation rules for amounts > $5000",
    "Review after 30 days of L3 operation"
  ],
  "notes": "Agent has met all criteria for L3. Approval contingent on maintaining escalation rules for high-value transactions."
}
```

### Generate Audit Report

```http
POST /api/seer/arao/v1/audit/reports
Authorization: Bearer <token>
Content-Type: application/json

{
  "period": {
    "start": "2026-01-01",
    "end": "2026-01-31"
  },
  "scope": "all_agents",
  "domains": ["financial_controls", "data_privacy", "operational_risk"],
  "contents": [
    "agent_inventory",
    "autonomy_levels",
    "compliance_status",
    "decision_samples",
    "escalation_stats",
    "incident_history"
  ],
  "format": "xlsx"
}
```

Response:
```json
{
  "report_id": "report-2026-0113-001",
  "status": "generating",
  "estimated_completion": "2026-01-13T16:00:00Z"
}
```

---

## MCP Tools

| REST Endpoint | MCP Tool |
|--------------|----------|
| `GET /compliance/summary` | `seer_arao_get_compliance_summary` |
| `GET /autonomy/requests` | `seer_arao_list_autonomy_requests` |
| `POST /autonomy/requests/{id}/decision` | `seer_arao_process_autonomy_request` |
| `POST /audit/reports` | `seer_arao_generate_audit_report` |

---

*Status: 🟡 Draft — Endpoint structure defined, OpenAPI spec TBD*
