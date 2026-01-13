# APO REST Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Hub-Extended  
> **Base Path:** `/api/seer/apo/v1`

---

## Overview

The APO Channel provides APIs for the **Automation Product Owner (APO)** ([role definition](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)) to manage agent portfolios, track business outcomes, and govern autonomy levels.

This channel **extends Hub's APO channel** with Seer-specific capabilities for AI agent management.

---

## Endpoint Groups

### Agent Portfolio

```
# List agents in portfolio
GET /agents
Query: status, class, autonomy_level, sort, limit, cursor

# Get agent details
GET /agents/{agent_id}

# Create agent (initiate)
POST /agents
Body: { name, class, description, design_id, autonomy_ceiling }

# Update agent
PATCH /agents/{agent_id}
Body: { name, description, status }

# Retire agent
POST /agents/{agent_id}/retire
Body: { reason, transition_plan }
```

### Business Outcomes

```
# List outcome metrics
GET /outcomes
Query: agent_id, period, metric_type

# Get outcome detail
GET /outcomes/{outcome_id}

# Create outcome definition
POST /outcomes
Body: { agent_id, metric_name, target, measurement_method }

# Update outcome target
PATCH /outcomes/{outcome_id}
Body: { target, threshold }

# Get outcome history
GET /outcomes/{outcome_id}/history
Query: start_date, end_date, granularity
```

### Autonomy Management

```
# Get agent autonomy
GET /agents/{agent_id}/autonomy

# Request autonomy change
POST /agents/{agent_id}/autonomy/requests
Body: { requested_level, justification, evidence }

# List autonomy requests
GET /autonomy/requests
Query: status, agent_id, sort

# Get request status
GET /autonomy/requests/{request_id}
```

### Portfolio Analytics

```
# Get portfolio summary
GET /portfolio/summary
Query: period

# Get performance trends
GET /portfolio/trends
Query: metric, period, granularity

# Get agent comparison
GET /portfolio/comparison
Query: agent_ids, metric
```

---

## Sample Requests

### List Active Agents

```http
GET /api/seer/apo/v1/agents?status=active&limit=20
Authorization: Bearer <token>
```

Response:
```json
{
  "items": [
    {
      "id": "agent-001",
      "name": "expense-approver",
      "class": "expense-approver",
      "status": "active",
      "autonomy_level": "L3",
      "autonomy_ceiling": "L3",
      "created_at": "2025-06-15T10:00:00Z",
      "health_score": 0.91
    }
  ],
  "next_cursor": "...",
  "has_more": true
}
```

### Request Autonomy Upgrade

```http
POST /api/seer/apo/v1/agents/agent-001/autonomy/requests
Authorization: Bearer <token>
Content-Type: application/json

{
  "requested_level": "L3",
  "justification": "Agent has demonstrated 99.2% accuracy over 6 months",
  "evidence": {
    "months_at_current_level": 6,
    "accuracy_rate": 0.992,
    "human_concordance": 0.98,
    "incident_count": 0
  }
}
```

---

## Hub Extension Points

This channel extends Hub's APO channel:

| Hub Endpoint | Seer Extension |
|-------------|----------------|
| `/hub/apo/v1/scenarios` | Proxied as-is |
| `/hub/apo/v1/applications` | Proxied as-is |
| N/A | `/seer/apo/v1/agents` (new) |
| N/A | `/seer/apo/v1/autonomy` (new) |
| N/A | `/seer/apo/v1/outcomes` (new) |

---

## MCP Tools

| REST Endpoint | MCP Tool |
|--------------|----------|
| `GET /agents` | `seer_apo_list_agents` |
| `GET /agents/{id}` | `seer_apo_get_agent` |
| `GET /outcomes` | `seer_apo_list_outcomes` |
| `POST /autonomy/requests` | `seer_apo_request_autonomy` |

---

*Status: 🟡 Draft — Endpoint structure defined, OpenAPI spec TBD*
