# AE REST Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Seer-Native  
> **Base Path:** `/api/seer/ae/v1`

---

## Overview

The AE Channel provides APIs for the **Agent Engineer (AE)** ([role definition](../../../personas-and-needs/roles.md#3-agent-engineer-ae)) to develop, test, and release agents throughout their full lifecycle.

This is a **Seer-native channel** with no Hub equivalent.

---

## Endpoint Groups

### Agent Development

```
# List agent configs
GET /agents
Query: status, class, sort, limit, cursor

# Get agent config
GET /agents/{agent_id}

# Update agent config
PUT /agents/{agent_id}
Body: { prompts, tools, telemetry, workflow }

# Get agent prompts
GET /agents/{agent_id}/prompts

# Update agent prompts
PUT /agents/{agent_id}/prompts
Body: { system_prompt, task_prompts, tool_prompts }

# Compare prompt versions
GET /agents/{agent_id}/prompts/diff
Query: version_a, version_b
```

### Tool Bindings

```
# List tool bindings
GET /agents/{agent_id}/tools
Query: status

# Add tool binding
POST /agents/{agent_id}/tools
Body: { tool_id, protocol, config, permissions }

# Update tool binding
PUT /agents/{agent_id}/tools/{binding_id}
Body: { config, permissions }

# Remove tool binding
DELETE /agents/{agent_id}/tools/{binding_id}

# Test tool binding
POST /agents/{agent_id}/tools/{binding_id}/test
Body: { test_input }
```

### Telemetry

```
# Get telemetry config
GET /agents/{agent_id}/telemetry

# Update telemetry config
PUT /agents/{agent_id}/telemetry
Body: { required_events, custom_events }

# Validate telemetry contract
POST /agents/{agent_id}/telemetry/validate
```

### Testing

```
# List test suites
GET /agents/{agent_id}/tests
Query: type

# Get test suite
GET /agents/{agent_id}/tests/{suite_id}

# Create test suite
POST /agents/{agent_id}/tests
Body: { name, type, test_cases }

# Run test suite
POST /agents/{agent_id}/tests/{suite_id}/run
Response: { run_id }

# Get test run results
GET /agents/{agent_id}/tests/runs/{run_id}

# Replay scenario
POST /agents/{agent_id}/replay
Body: { request_id }
```

### Versioning & Release

```
# List versions
GET /agents/{agent_id}/versions
Query: status, sort

# Create version
POST /agents/{agent_id}/versions
Body: { version, changelog }

# Get version detail
GET /agents/{agent_id}/versions/{version}

# Deploy version
POST /agents/{agent_id}/versions/{version}/deploy
Body: { environment, canary_percentage }

# Get deployment status
GET /agents/{agent_id}/deployments/{deployment_id}

# Rollback
POST /agents/{agent_id}/rollback
Body: { target_version, reason }
```

### Feedback Inbox

```
# List feedback items
GET /agents/{agent_id}/feedback
Query: source, status, priority

# Get feedback detail
GET /agents/{agent_id}/feedback/{feedback_id}

# Update feedback status
PATCH /agents/{agent_id}/feedback/{feedback_id}
Body: { status, resolution_notes }
```

---

## Sample Requests

### Run Test Suite

```http
POST /api/seer/ae/v1/agents/expense-approver/tests/behavioral/run
Authorization: Bearer <token>
```

Response:
```json
{
  "run_id": "run-2026-0113-001",
  "status": "running",
  "started_at": "2026-01-13T15:30:00Z",
  "estimated_duration_seconds": 120
}
```

### Deploy Version

```http
POST /api/seer/ae/v1/agents/expense-approver/versions/v2.4.0/deploy
Authorization: Bearer <token>
Content-Type: application/json

{
  "environment": "production",
  "canary_percentage": 10,
  "promotion_criteria": {
    "min_duration_minutes": 30,
    "max_error_rate": 0.02,
    "min_ahs": 0.85
  }
}
```

---

## MCP Tools

| REST Endpoint | MCP Tool |
|--------------|----------|
| `GET /agents/{id}/prompts` | `seer_ae_get_prompts` |
| `POST /agents/{id}/tests/{suite}/run` | `seer_ae_run_tests` |
| `POST /agents/{id}/versions/{v}/deploy` | `seer_ae_deploy_version` |
| `POST /agents/{id}/rollback` | `seer_ae_rollback` |

---

*Status: 🟡 Draft — Endpoint structure defined, OpenAPI spec TBD*
