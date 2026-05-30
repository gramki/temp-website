# Technical Debt Item

**Model:** Work Model
**Track:** Build — Artifact
**Owner:** Tech Lead, Developers

## Definition

A documented instance of accumulated technical debt — a conscious or discovered shortcoming in the codebase, architecture, or infrastructure that increases future cost of change. Technical Debt Items are *artifacts* (things produced by work), not work entities themselves. When a Technical Debt Item is prioritized for resolution, it is addressed via an **Epic** (if significant) or a **Story** (if contained).

Technical Debt Items are produced during any Build Track activity — Stories, Technical Tasks, code reviews, Design Deliberations, or retrospectives. They may also be identified during Run Track Incidents (production issues revealing architectural debt) or Discovery Track analysis.

## Purpose

Makes technical debt visible and manageable. Without Technical Debt Items:
- Debt accumulates silently — developers know about it, but it's not tracked in the model
- Prioritization is impossible — if debt is invisible, it cannot compete with features for sprint capacity
- Debt resolution is untraceable — fixing debt has no structured work entity to track
- The cost of delay is unknown — debt items need context (impact, risk, effort to resolve)

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Brief description (e.g., "payments-service: synchronous bank calls should be async") |
| System | Reference (Technical) | Which System contains this debt |
| Component | Reference (Technical) | Which Component (optional, if debt is localized) |
| Debt Category | Enum | `Code Quality` / `Architecture` / `Infrastructure` / `Testing` / `Documentation` / `Dependency` |
| Description | Text | What the debt is — current state vs. desired state |
| Impact | Text | What problems this debt causes or risks it introduces |
| Effort to Resolve | String | Estimated effort to address (e.g., "2-3 sprints", "1 story") |
| Discovery Source | Text | How this debt was identified (Story, Task, code review, Incident, Design Deliberation) |
| Resolution Epic | Reference (Build) | Epic created to resolve this debt (when prioritized) |
| Resolution Story | Reference (Build) | Story created to resolve this debt (if contained) |

## Statuses

| Status | Description |
|---|---|
| Identified | Debt is documented but not yet prioritized |
| Accepted | Debt is acknowledged; resolution is deferred intentionally |
| Prioritized | Debt has been prioritized; Epic or Story created for resolution |
| Resolving | Resolution work is in progress |
| Resolved | Debt has been addressed |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Located in | System (Technical) | Debt exists within a System |
| Located in | Component (Technical) | Debt may be localized to a Component |
| Discovered during | Story (Build) | Debt may be discovered during Story implementation |
| Discovered during | Technical Task (Build) | Debt may be discovered during Task implementation |
| Discovered during | Incident (Run) | Production incident may reveal architectural debt |
| Discovered during | Design Deliberation (Build) | Deliberation may identify debt as a side finding |
| Resolved via | Epic (Build) | Significant debt is resolved via an Epic |
| Resolved via | Story (Build) | Contained debt may be resolved via a Story |

## Examples

| Technical Debt | Category | System | Impact | Status |
|---|---|---|---|---|
| "Synchronous bank API calls should be async" | Architecture | payments-service | Timeout risk under high load; blocks thread pool | Prioritized → Epic "Async Bank Integration" |
| "Test coverage for compliance screening < 70%" | Testing | compliance-service | Risk of undetected regressions in OFAC screening | Accepted |
| "Deprecated Kafka client library (v2.x → v3.x)" | Dependency | payments-service, fx-service | Security vulnerability warnings; missing new features | Identified |
| "Settlement file generator lacks idempotency" | Code Quality | bank-adapter | Duplicate settlement files on retry | Prioritized → Story in Settlement Epic |
| "Missing circuit breaker on fx-service → rate provider" | Infrastructure | fx-service | Cascading failures when rate provider is down | Resolving |

---
