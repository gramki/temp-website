# KMO REST Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Hub-Extended  
> **Base Path:** `/api/seer/kmo/v1`

---

## Overview

The KMO Channel provides APIs for the **Knowledge & Memory Owner (KMO)** ([role definition](../../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)) to govern knowledge sources, manage memory hierarchies, and oversee enterprise learning.

This channel **extends Hub's KMO channel** with Seer-specific capabilities for AI memory and learning management.

---

## Endpoint Groups

### Knowledge Sources

```
# List knowledge sources
GET /sources
Query: type, status, domain, sort, limit, cursor

# Get source detail
GET /sources/{source_id}

# Register source
POST /sources
Body: { name, type, connection, domain, quality_thresholds }

# Update source config
PUT /sources/{source_id}
Body: { connection, quality_thresholds }

# Trigger sync
POST /sources/{source_id}/sync

# Get sync status
GET /sources/{source_id}/sync/status

# Get quality metrics
GET /sources/{source_id}/quality
Query: period
```

### Knowledge Graphs

```
# List knowledge graphs
GET /graphs
Query: domain, sort, limit, cursor

# Get graph detail
GET /graphs/{graph_id}

# Create graph
POST /graphs
Body: { name, domain, schema }

# Add entity
POST /graphs/{graph_id}/entities
Body: { type, properties, relationships }

# Update entity
PUT /graphs/{graph_id}/entities/{entity_id}
Body: { properties, relationships }

# Query graph
POST /graphs/{graph_id}/query
Body: { query }
```

### Memory Management

```
# Get memory stats
GET /memory/stats
Query: level, agent_class

# Get memory entries
GET /memory/entries
Query: level, agent_id, type, sort, limit, cursor

# Configure retention
PUT /memory/retention
Body: { policies }

# Trigger cleanup
POST /memory/cleanup
Body: { level, dry_run }

# Get cleanup preview
GET /memory/cleanup/preview
Query: level
```

### Enterprise Learning

```
# List promotion candidates
GET /learning/candidates
Query: level, status, min_score, sort, limit, cursor

# Get candidate detail
GET /learning/candidates/{candidate_id}

# Review candidate
POST /learning/candidates/{candidate_id}/review
Body: { decision, notes, edits }

# Configure promotion criteria
PUT /learning/criteria
Body: { l1_to_l2, l2_to_l3 }

# Get learning analytics
GET /learning/analytics
Query: period, granularity
```

---

## Sample Requests

### Review Promotion Candidate

```http
POST /api/seer/kmo/v1/learning/candidates/cand-001/review
Authorization: Bearer <token>
Content-Type: application/json

{
  "decision": "approve",
  "notes": "Pattern is well-validated across 3 agent instances with 98% success rate",
  "edits": null
}
```

### Configure Retention Policy

```http
PUT /api/seer/kmo/v1/memory/retention
Authorization: Bearer <token>
Content-Type: application/json

{
  "policies": {
    "l1": {
      "task_context": { "retention_days": 1, "action": "delete" },
      "session_state": { "retention_days": 7, "action": "delete" },
      "learning_candidates": { "retention_days": 30, "action": "archive" }
    },
    "l2": {
      "promoted_learnings": { "retention_days": 180, "action": "review" },
      "shared_patterns": { "retention_days": 365, "action": "archive" }
    },
    "l3": {
      "enterprise_facts": { "retention": "permanent", "action": "version" },
      "deprecated": { "retention_days": 730, "action": "archive" }
    }
  }
}
```

---

## Hub Extension Points

This channel extends Hub's KMO channel:

| Hub Endpoint | Seer Extension |
|-------------|----------------|
| `/hub/kmo/v1/knowledge-bases` | Proxied as-is |
| N/A | `/seer/kmo/v1/memory` (new) |
| N/A | `/seer/kmo/v1/learning` (new) |
| N/A | `/seer/kmo/v1/graphs` (new) |

---

## MCP Tools

| REST Endpoint | MCP Tool |
|--------------|----------|
| `GET /sources` | `seer_kmo_list_sources` |
| `GET /memory/stats` | `seer_kmo_get_memory_stats` |
| `GET /learning/candidates` | `seer_kmo_list_promotion_candidates` |
| `POST /learning/candidates/{id}/review` | `seer_kmo_review_candidate` |

---

*Status: 🟡 Draft — Endpoint structure defined, OpenAPI spec TBD*
