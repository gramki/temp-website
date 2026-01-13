# CSA REST Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Seer-Native  
> **Base Path:** `/api/seer/csa/v1`

---

## Overview

The CSA Channel provides APIs for the **Cognitive Systems Architect (CSA)** ([role definition](../../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)) to manage cognitive patterns, agent designs, and validation workflows.

This is a **Seer-native channel** with no Hub equivalent.

---

## Endpoint Groups

### Patterns

```
# List patterns
GET /patterns
Query: status, type, sort, limit, cursor

# Get pattern detail
GET /patterns/{pattern_id}

# Create pattern
POST /patterns
Body: { name, type, structure, constraints, when_to_use }

# Update pattern
PUT /patterns/{pattern_id}
Body: { structure, constraints, when_to_use }

# Deprecate pattern
POST /patterns/{pattern_id}/deprecate
Body: { reason, replacement_pattern_id }

# Get pattern usage
GET /patterns/{pattern_id}/usage
Query: period
```

### Designs

```
# List designs
GET /designs
Query: status, pattern_id, agent_class, sort, limit, cursor

# Get design detail
GET /designs/{design_id}

# Create design
POST /designs
Body: { name, agent_class, pattern_id, structure, constraints }

# Update design
PUT /designs/{design_id}
Body: { structure, constraints }

# Validate design
POST /designs/{design_id}/validate
Response: { valid, violations, warnings }

# Clone design
POST /designs/{design_id}/clone
Body: { name }
```

### Topologies

```
# List topologies
GET /topologies
Query: status, sort, limit, cursor

# Get topology detail
GET /topologies/{topology_id}

# Create topology
POST /topologies
Body: { name, agents, interactions, coordination_pattern }

# Update topology
PUT /topologies/{topology_id}
Body: { agents, interactions }

# Analyze blast radius
POST /topologies/{topology_id}/blast-radius
Body: { failure_agent_id }
```

### Failure Modes

```
# List failure modes
GET /failure-modes
Query: pattern_id, agent_class, severity

# Get failure mode detail
GET /failure-modes/{mode_id}

# Create failure mode
POST /failure-modes
Body: { pattern_id, name, detection, response, escalation }

# Update failure mode
PUT /failure-modes/{mode_id}
Body: { detection, response, escalation }
```

### Validation Reviews

```
# List pending reviews
GET /reviews
Query: status, agent_class, sort

# Get review detail
GET /reviews/{review_id}

# Submit review decision
POST /reviews/{review_id}/decision
Body: { decision, notes, required_changes }
```

---

## Sample Requests

### Create Pattern

```http
POST /api/seer/csa/v1/patterns
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "ReAct",
  "type": "reasoning",
  "structure": {
    "steps": ["reason", "act", "observe"],
    "loop": true,
    "termination": "goal_achieved OR max_iterations"
  },
  "constraints": {
    "max_iterations": 10,
    "max_time_per_iteration_ms": 30000,
    "required_traces": ["reasoning.step", "tool.invoked", "observation.recorded"]
  },
  "when_to_use": [
    "General-purpose tasks requiring tool use",
    "Tasks with clear action-observation cycles"
  ]
}
```

### Validate Design

```http
POST /api/seer/csa/v1/designs/design-001/validate
Authorization: Bearer <token>
```

Response:
```json
{
  "valid": false,
  "violations": [
    {
      "rule": "escalation_required",
      "message": "DECIDE nodes must have escalation paths defined",
      "location": "nodes.decision_1"
    }
  ],
  "warnings": [
    {
      "rule": "timeout_recommended",
      "message": "No timeout specified for tool call",
      "location": "nodes.tool_call_1"
    }
  ]
}
```

---

## MCP Tools

| REST Endpoint | MCP Tool |
|--------------|----------|
| `GET /patterns` | `seer_csa_list_patterns` |
| `POST /designs/{id}/validate` | `seer_csa_validate_design` |
| `POST /topologies/{id}/blast-radius` | `seer_csa_analyze_blast_radius` |

---

*Status: 🟡 Draft — Endpoint structure defined, OpenAPI spec TBD*
