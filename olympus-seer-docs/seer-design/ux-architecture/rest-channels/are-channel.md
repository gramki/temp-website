# ARE REST Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Hub-Extended  
> **Base Path:** `/api/seer/are/v1`

---

## Overview

The ARE Channel provides APIs for the **Agent Reliability Engineer (ARE)** ([role definition](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)) to monitor agent health, manage operational controls, and respond to incidents.

This channel **extends Hub's ARE channel** with Seer-specific capabilities for AI agent operations.

---

## Endpoint Groups

### Fleet Health

```
# Get fleet status
GET /fleet/status
Response: { healthy, degraded, critical, total }

# Get fleet metrics
GET /fleet/metrics
Query: period, granularity

# List agents by health
GET /fleet/agents
Query: status, class, sort, limit, cursor

# Get agent health detail
GET /agents/{agent_id}/health
Response: { ahs, components, history }

# Get AHS breakdown
GET /agents/{agent_id}/health/components
```

### SLA Management

```
# List SLAs
GET /slas
Query: tier, status

# Get SLA detail
GET /slas/{sla_id}

# Create SLA
POST /slas
Body: { name, tier, targets, agents }

# Update SLA
PUT /slas/{sla_id}
Body: { targets }

# Get SLA performance
GET /slas/{sla_id}/performance
Query: period

# List SLA breaches
GET /slas/breaches
Query: sla_id, period, severity
```

### Control Operations

```
# Kill agent
POST /agents/{agent_id}/kill
Body: { reason }

# Pause agent
POST /agents/{agent_id}/pause
Body: { reason }

# Resume agent
POST /agents/{agent_id}/resume

# Restart agent
POST /agents/{agent_id}/restart
Body: { reason }

# Set throttle
POST /agents/{agent_id}/throttle
Body: { percentage, duration_minutes }

# Clear throttle
DELETE /agents/{agent_id}/throttle
```

### Circuit Breakers

```
# List circuit breakers
GET /circuits
Query: status

# Get circuit detail
GET /circuits/{circuit_id}

# Force close circuit
POST /circuits/{circuit_id}/close
Body: { reason }

# Force open circuit
POST /circuits/{circuit_id}/open
Body: { reason, duration_seconds }

# Configure circuit
PUT /circuits/{circuit_id}
Body: { threshold, reset_timeout }
```

### Rollback

```
# Get rollback options
GET /agents/{agent_id}/rollback/options

# Execute rollback
POST /agents/{agent_id}/rollback
Body: { target_version, reason }

# Get rollback status
GET /agents/{agent_id}/rollback/{rollback_id}
```

### Incidents

```
# List incidents
GET /incidents
Query: status, severity, agent_id, sort, limit, cursor

# Get incident detail
GET /incidents/{incident_id}

# Create incident
POST /incidents
Body: { title, severity, agent_id, description }

# Update incident
PATCH /incidents/{incident_id}
Body: { status, assignee, notes }

# Add incident note
POST /incidents/{incident_id}/notes
Body: { content }

# Resolve incident
POST /incidents/{incident_id}/resolve
Body: { resolution_notes, root_cause }

# Create PIR
POST /incidents/{incident_id}/pir
Body: { summary, root_cause, contributing_factors, action_items }
```

---

## Sample Requests

### Kill Agent

```http
POST /api/seer/are/v1/agents/order-validator-03/kill
Authorization: Bearer <token>
Content-Type: application/json

{
  "reason": "High error rate spike detected - 15% failure rate"
}
```

Response:
```json
{
  "action": "kill",
  "agent_id": "order-validator-03",
  "status": "killed",
  "timestamp": "2026-01-13T14:22:00Z",
  "affected_tasks": 12,
  "tasks_action": "reassigned"
}
```

### Get Fleet Status

```http
GET /api/seer/are/v1/fleet/status
Authorization: Bearer <token>
```

Response:
```json
{
  "summary": {
    "healthy": 38,
    "degraded": 5,
    "critical": 2,
    "total": 45
  },
  "metrics": {
    "fleet_ahs": 0.89,
    "active_tasks": 1247,
    "throughput_per_min": 450,
    "error_rate": 0.008
  },
  "alerts": [
    {
      "agent_id": "order-validator-03",
      "severity": "critical",
      "message": "Error rate 15% exceeds threshold 2%"
    }
  ]
}
```

---

## Hub Extension Points

This channel extends Hub's ARE channel:

| Hub Endpoint | Seer Extension |
|-------------|----------------|
| `/hub/are/v1/applications/{id}/health` | Extended with AHS |
| `/hub/are/v1/incidents` | Extended with PIR |
| N/A | `/seer/are/v1/fleet` (new) |
| N/A | `/seer/are/v1/circuits` (new) |

---

## MCP Tools

| REST Endpoint | MCP Tool |
|--------------|----------|
| `GET /fleet/status` | `seer_are_get_fleet_status` |
| `POST /agents/{id}/kill` | `seer_are_kill_agent` |
| `POST /agents/{id}/pause` | `seer_are_pause_agent` |
| `POST /agents/{id}/rollback` | `seer_are_rollback_agent` |

---

*Status: 🟡 Draft — Endpoint structure defined, OpenAPI spec TBD*
