# Promotion Destination

> **Category:** DevOps and Lifecycle

---

## Overview

A **Promotion Destination** defines a target for artifact promotion, including the target subscription/workbench, approval workflow, and notification settings. Promotion Destinations are configured per subscription and establish the allowed paths for moving artifacts from development to production.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address deployment paths. Promotion Destination is an implementation concept for controlling artifact movement.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| (not covered) | Promotion Destination | Target for artifact movement |
| (not covered) | Approval workflow | Control over promotions |

### Gap This Fills

The ontology focuses on runtime. Promotion Destination addresses:
1. **Target specification**: Where can artifacts go?
2. **Approval control**: Who authorizes movement?
3. **Notification**: Who is informed of promotions?

---

## Definition

**Promotion Destination** is a configuration that:
- Defines a valid target for artifact promotion
- Specifies approval workflow requirements
- Configures notification recipients
- Controls who can request promotion

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Subscription-level or workbench-level |
| **Lifecycle** | Created by Admin; used by Developers |
| **Ownership** | Admin owns; Developer uses |
| **Multiplicity** | Multiple destinations per subscription |

---

## Structure

### Promotion Destination CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionDestination
metadata:
  name: dev-to-staging
  namespace: acme-bank
spec:
  # Source subscription
  source_subscription: acme-dev
  
  # Target
  target:
    type: workbench           # subscription | workbench
    subscription_id: acme-dev
    workbench_id: dispute-ops-staging
    
  # Approval configuration
  approval:
    required: true
    approver_roles:
      - supervisor
      - tenant-admin
    min_approvers: 1
    auto_approve_conditions:
      - type: test_passed
        suite: integration-tests
        
  # Request permissions
  requesters:
    roles:
      - developer
    users: []
    
  # Notifications
  notifications:
    on_request:
      - requester
      - admin-group
    on_approval:
      - requester
      - admin-group
      - ops-team
    on_completion:
      - requester
      - ops-team
    on_failure:
      - requester
      - admin-group
```

### Destination Types

| Type | Target | Use Case |
|------|--------|----------|
| **subscription** | Entire subscription | Clone full workbenches |
| **workbench** | Specific workbench | Scenario-level promotion |

---

## Behavior

### Promotion Flow with Destination

```
1. Developer requests promotion
   ├── Specifies destination reference
   └── Includes artifacts and reason

2. System validates destination
   ├── Check requester is authorized
   └── Validate target exists and is compatible

3. Approval workflow (if required)
   ├── Notify approvers
   ├── Wait for required approvals
   └── Check auto-approve conditions

4. Execute promotion
   ├── Copy artifacts per destination config
   └── Apply at target

5. Notify stakeholders
   └── Per notification configuration
```

### Sensible Defaults for Small Teams

```yaml
# Minimal configuration for small teams
spec:
  target:
    type: workbench
    workbench_id: dispute-ops-prod
    
  approval:
    required: true
    approver_roles: [tenant-admin]
    
  notifications:
    on_completion: [requester, admin]
```

### Cross-Subscription Promotion

```
When target is different subscription:

1. Credentials for target stored in destination
2. Physical copy of artifacts
3. CRDs copied to target Git repo
4. Target operators reconcile

Security: Only admins can create cross-subscription destinations
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Promotion System | ← used by | Promotion references destination |
| Admin | ← created by | Admin configures destinations |
| Developer | ← used by | Developers request to destination |
| Notification Services | → triggers | Stakeholder notifications |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Valid target** | Target must exist and be accessible |
| **Authorization stored** | Credentials for cross-sub stored |
| **Version compatibility** | Target must accept source version |
| **Admin only cross-sub** | Cross-subscription requires admin |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Controlled paths** | Only approved destinations |
| ✅ **Audit** | Clear promotion path record |
| ✅ **Flexibility** | Configure per org needs |
| ✅ **Notification** | Stakeholders informed |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Configuration required** | Templates; sensible defaults |
| ⚠️ **Approval delays** | Auto-approve conditions |

---

## Examples

### Example 1: Dev to Prod Destination

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionDestination
metadata:
  name: dev-to-prod
spec:
  source_subscription: acme-dev
  
  target:
    type: subscription
    subscription_id: acme-prod
    
  approval:
    required: true
    approver_roles: [tenant-admin]
    min_approvers: 2
```

### Example 2: Auto-Approve for Staging

```yaml
spec:
  target:
    workbench_id: dispute-ops-staging
    
  approval:
    required: true
    auto_approve_conditions:
      - type: test_passed
        suite: integration-tests
      - type: static_analysis_passed
```

---

## Implementation Notes

### For Developers

- Know which destinations you can use
- Include required information in requests
- Respond to feedback from approvers

### For Admins

- Create destinations during subscription setup
- Review approval patterns regularly
- Manage cross-subscription credentials securely

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Promotion](./promotion.md) | Uses Promotion Destination |
| [Subscription](./subscription.md) | Destinations defined per subscription |
| [Artifact Registry](./artifact-registry.md) | Artifacts copied via destinations |

---

## References

- [Promotion Model](../../04-subsystems/artifact-registry/promotion-model.md)

