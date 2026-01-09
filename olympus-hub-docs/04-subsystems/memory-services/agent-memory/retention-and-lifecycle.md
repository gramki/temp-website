# Agent Memory Retention and Lifecycle

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Agent Memory Services](./README.md)

---

## Overview

Agent Memory has a strict lifecycle bound to Request/Session scope. This document describes retention policies, cleanup behavior, and lifecycle management.

---

## Lifecycle Phases

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AGENT MEMORY LIFECYCLE                                │
│                                                                              │
│   Request       Session        Session          Retention       Cleanup     │
│   Created       Active         Completed        Period          Complete    │
│      │            │               │                │               │        │
│      ▼            ▼               ▼                ▼               ▼        │
│   ┌──────┐    ┌───────┐      ┌─────────┐     ┌──────────┐    ┌─────────┐   │
│   │Store │───▶│ Full  │─────▶│Read-only│────▶│ Pending  │───▶│ Deleted │   │
│   │Alloc │    │Access │      │ Access  │     │ Deletion │    │         │   │
│   └──────┘    └───────┘      └─────────┘     └──────────┘    └─────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase Details

### 1. Store Allocation

| Trigger | Request/Session creation |
|---------|-------------------------|
| Action | Storage allocated per agent based on deployment CRD |
| Duration | Immediate |

### 2. Active Session

| Phase | Full Access |
|-------|-------------|
| Capabilities | Read, Write, Delete, Search |
| Duration | Until session completes or is cancelled |
| Encryption | Active — agent+session unique keys |

### 3. Session Completed

| Phase | Read-Only Access |
|-------|------------------|
| Trigger | Request status → COMPLETED or CANCELLED |
| Capabilities | Read-only (for debugging/audit) |
| Duration | Retention period (admin-configured) |
| Access | Original agent identity only |

### 4. Retention Period

| Aspect | Details |
|--------|---------|
| **Configuration** | Per store, by tenant admin |
| **Purpose** | Debugging, audit, support investigation |
| **Access** | Read-only via admin tools |
| **Encryption** | Keys retained during period |

### 5. Cleanup

| Trigger | Retention period expired |
|---------|--------------------------|
| Action | Automatic deletion of all agent memory |
| Key Disposal | Encryption keys securely deleted |
| Audit | Deletion event logged |

---

## Retention Configuration

### Per-Store Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchMemoryConfig
metadata:
  name: fraud-ops-memory
spec:
  agent_memory:
    retention:
      # Per-service retention periods
      log_service:
        after_session_hours: 72
      conversation_service:
        after_session_hours: 48
      kv_service:
        after_session_hours: 24
      document_service:
        after_session_hours: 168  # 7 days
```

### Retention Period Defaults

| Service | Default Retention | Rationale |
|---------|-------------------|-----------|
| Log Service | 72 hours | Audit trail for debugging |
| Conversation | 48 hours | Context for support |
| KV Store | 24 hours | Ephemeral state |
| Documents | 168 hours (7 days) | Document review |

---

## No Early Cleanup

Agents **cannot request early cleanup** of their memory:

| Constraint | Rationale |
|------------|-----------|
| No `delete_all()` API | Prevents accidental data loss |
| No session termination | Session lifecycle controlled by Hub |
| Overwrite allowed | Agents can overwrite values |

### What Agents Can Do

| Action | Allowed |
|--------|---------|
| Overwrite values | ✅ Yes |
| Delete specific keys | ✅ Yes |
| Delete specific documents | ✅ Yes |
| Request session termination | ❌ No |
| Request bulk cleanup | ❌ No |

---

## Cross-Request Memory

Agent Memory is **strictly session-scoped**. For cross-request persistence:

| Requirement | Solution |
|-------------|----------|
| User preferences (cross-session) | Enterprise Memory |
| Business entity data | Operational data stores |
| Learned patterns | Enterprise Memory promotion |
| Agent configuration | Agent specification (immutable) |

### Promotion Path

```
Session-Observed Pattern
        │
        │ Pattern persists across sessions
        ▼
Agent Developer identifies pattern
        │
        │ Explicit promotion
        ▼
Enterprise Memory (via Signal Exchange)
```

---

## Encryption Key Lifecycle

| Phase | Key Status |
|-------|------------|
| Session Active | Keys active, derived from Workbench root |
| Session Completed | Keys retained for retention period |
| Retention Expired | Keys securely deleted |

### Key Hierarchy

```
Workbench Root Key (managed by Olympus KMS)
        │
        ├── Agent A + Session 1 Key
        ├── Agent A + Session 2 Key
        ├── Agent B + Session 1 Key
        └── ...
```

---

## Cleanup Process

### Automatic Cleanup

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CLEANUP PROCESS                                       │
│                                                                              │
│   1. Retention Check                                                         │
│      └── Scheduled job identifies expired sessions                          │
│                                                                              │
│   2. Data Deletion                                                           │
│      ├── Log entries deleted                                                │
│      ├── Conversation history deleted                                       │
│      ├── KV store entries deleted                                           │
│      └── Documents deleted                                                  │
│                                                                              │
│   3. Key Disposal                                                            │
│      └── Encryption keys securely destroyed                                 │
│                                                                              │
│   4. Audit Logging                                                           │
│      └── Cleanup event logged (no content)                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Cleanup Audit Record

```json
{
  "event": "agent_memory_cleanup",
  "timestamp": "2026-01-08T12:00:00Z",
  "tenant": "acme-bank",
  "workbench": "fraud-ops",
  "session_id": "req-12345",
  "agent_id": "support-agent",
  "retention_expired_at": "2026-01-08T12:00:00Z",
  "services_cleaned": ["log", "conversation", "kv", "documents"]
}
```

---

## Quota Management

### Storage Quotas

| Quota | Scope | Configurable |
|-------|-------|--------------|
| Total storage (MB) | Per agent per request | Deployment CRD |
| Document count | Per agent per request | Deployment CRD |
| Document size (MB) | Per document | Workbench config |
| KV entry count | Per agent per request | Deployment CRD |
| Log entries | Per agent per request | Deployment CRD |

### Quota Exceeded Behavior

| Event | Behavior |
|-------|----------|
| Quota exceeded | Write rejected with `QuotaExceededException` |
| Near quota (90%) | Warning logged, metric emitted |
| Agent action | Delete old data or request quota increase |

---

## Related Documents

- [Agent Memory Services](./README.md) — Overview
- [Storage Services](./storage-services.md) — Service details
- [Agent Memory SDK](./sdk.md) — SDK specification
- [Design Rationale](./design-rationale.md) — Design decisions
- [ADR-0067: Agent Memory Session Scope](../../../decision-logs/0067-agent-memory-session-scope.md) — Session scope decision

---

*Agent Memory lifecycle is strictly bound to Request/Session scope with admin-configurable retention periods.*

