# Open Points — Artifact Registry

## Overview

This document tracks unresolved questions and pending decisions for the Artifact Registry subsystem.

**Last Updated:** 2026-01-06

---

## Resolved

*No items resolved yet.*

---

## Under Discussion

### Registry & Artifacts

- [ ] **Retention Policy Defaults**
  - **Context:** What should be the default retention for snapshot registry artifacts?
  - **Current thinking:** 30 days untagged, 90 days tagged
  - **Blocking:** Configuration documentation

### Promotion Model

- [ ] **Approval Workflow Timeout**
  - **Context:** What happens if an approval request times out?
  - **Options:**
    1. Auto-reject after N days
    2. Escalate to higher authority
    3. Remain pending indefinitely
  - **Blocking:** Workflow implementation

- [ ] **Cross-Tenant Credential Management**
  - **Context:** How are credentials for cross-tenant promotion managed securely?
  - **Current thinking:** Stored in PromotionDestination spec with secret references
  - **Blocking:** Security review

### Git Repository

- [ ] **Branch Support Timeline**
  - **Context:** When will feature branch support be added?
  - **Current state:** Main branch only
  - **Blocking:** Developer experience for larger teams

- [ ] **Git Provider Options**
  - **Context:** Will customers be able to use their own Git providers as primary?
  - **Current state:** Platform-managed only, with mirror option
  - **Blocking:** Enterprise requirements

### Migrations

- [ ] **Migration Rollback Strategy**
  - **Context:** Should we provide automated rollback for migrations?
  - **Current state:** Manual only, down scripts for reference
  - **Blocking:** Production resilience

---

## Deferred

### External Tool Integration

- [ ] **Jira Integration for Approvals**
  - **Reason:** Placeholder for future release
  - **Deferred until:** External tool integration phase

- [ ] **ServiceNow Integration**
  - **Reason:** Placeholder for future release
  - **Deferred until:** External tool integration phase

### Advanced Features

- [ ] **Canary Deployments**
  - **Reason:** Out of scope for initial release
  - **Deferred until:** Post-GA feature planning

- [ ] **Blue-Green Deployments**
  - **Reason:** Out of scope for initial release
  - **Deferred until:** Post-GA feature planning

---

## Out of Scope

- **Kubernetes Manifests** — Hub manages only Hub-defined CRDs
- **Helm Charts** — Not exposed to Hub users
- **Infrastructure as Code** — Managed by Olympus Weave, not Hub


