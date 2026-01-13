# COS REST Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Seer-Native  
> **Base Path:** `/api/seer/cos/v1`

---

## Overview

The COS Channel provides APIs for the **Cognitive Operations Specialist (COS)** ([role definition](../../../personas-and-needs/roles.md#6-cognitive-operations-specialist-cos)) to monitor reasoning quality, analyze behavioral patterns, and manage cognitive issues.

This is a **Seer-native channel** with no Hub equivalent.

---

## Endpoint Groups

### Reasoning Quality

```
# Get quality metrics
GET /quality/metrics
Query: agent_class, period, granularity

# Get agent quality
GET /agents/{agent_id}/quality
Query: period

# Get confidence distribution
GET /agents/{agent_id}/confidence
Query: period

# List low-confidence decisions
GET /agents/{agent_id}/confidence/low
Query: threshold, limit, cursor
```

### Traces

```
# Search traces
GET /traces
Query: agent_id, request_id, status, time_from, time_to, limit, cursor

# Get trace detail
GET /traces/{trace_id}

# Get trace steps
GET /traces/{trace_id}/steps

# Flag trace for review
POST /traces/{trace_id}/flag
Body: { reason, priority }
```

### Behavioral Analysis

```
# Get behavioral trends
GET /behavior/trends
Query: agent_class, metric, period, granularity

# Detect drift
GET /behavior/drift
Query: agent_id, baseline_period, comparison_period

# Get anti-patterns
GET /behavior/anti-patterns
Query: agent_id, period, severity

# Get anti-pattern detail
GET /behavior/anti-patterns/{pattern_id}
```

### Hallucination Detection

```
# Get hallucination indicators
GET /hallucinations
Query: agent_id, severity, period, limit, cursor

# Get hallucination detail
GET /hallucinations/{detection_id}

# Mark as false positive
POST /hallucinations/{detection_id}/false-positive
Body: { reason }
```

### Cognitive Issues

```
# List issues
GET /issues
Query: status, priority, agent_id, type, sort, limit, cursor

# Get issue detail
GET /issues/{issue_id}

# Create issue
POST /issues
Body: { title, type, agent_id, description, evidence }

# Update issue
PATCH /issues/{issue_id}
Body: { status, priority, assignee }

# Route issue
POST /issues/{issue_id}/route
Body: { target_role, notes }

# Add evidence
POST /issues/{issue_id}/evidence
Body: { type, content, trace_ids }

# Resolve issue
POST /issues/{issue_id}/resolve
Body: { resolution_notes }
```

---

## Sample Requests

### Get Trace Detail

```http
GET /api/seer/cos/v1/traces/trace-2026-0113-abc
Authorization: Bearer <token>
```

Response:
```json
{
  "trace_id": "trace-2026-0113-abc",
  "request_id": "req-2026-0113-abc123",
  "agent_id": "expense-approver-02",
  "started_at": "2026-01-13T15:30:00Z",
  "completed_at": "2026-01-13T15:30:02.3Z",
  "duration_ms": 2300,
  "status": "completed",
  "result": "approved",
  "confidence": 0.91,
  "step_count": 4,
  "steps": [
    {
      "step": 1,
      "type": "parse",
      "name": "Parse Request",
      "duration_ms": 150,
      "confidence": 0.95,
      "input_summary": "Expense claim for team lunch - $450",
      "output_summary": "{type: meals, amount: 450}"
    }
    // ... more steps
  ]
}
```

### Detect Drift

```http
GET /api/seer/cos/v1/behavior/drift?agent_id=expense-approver&baseline_period=30d&comparison_period=7d
Authorization: Bearer <token>
```

Response:
```json
{
  "agent_id": "expense-approver",
  "baseline_period": "2025-12-14 to 2026-01-06",
  "comparison_period": "2026-01-06 to 2026-01-13",
  "drift_detected": true,
  "metrics": [
    {
      "metric": "approval_rate",
      "baseline": 0.75,
      "current": 0.72,
      "drift_percentage": -4.0,
      "significance": "low"
    },
    {
      "metric": "escalation_rate",
      "baseline": 0.12,
      "current": 0.18,
      "drift_percentage": 50.0,
      "significance": "high"
    }
  ],
  "possible_causes": [
    "Prompt update on Jan 10",
    "Knowledge source refresh on Jan 8"
  ]
}
```

---

## MCP Tools

| REST Endpoint | MCP Tool |
|--------------|----------|
| `GET /quality/metrics` | `seer_cos_get_quality_metrics` |
| `GET /traces/{id}` | `seer_cos_get_trace` |
| `GET /behavior/drift` | `seer_cos_detect_drift` |
| `GET /behavior/anti-patterns` | `seer_cos_get_anti_patterns` |

---

*Status: 🟡 Draft — Endpoint structure defined, OpenAPI spec TBD*
