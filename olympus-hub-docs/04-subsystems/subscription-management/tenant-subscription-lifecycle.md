# Tenant Subscription Lifecycle

> **Status:** 🔴 Stub — Placeholder for expansion

Defines the lifecycle states and transitions for tenant subscriptions in Olympus Hub.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Manage tenant subscription from provisioning to termination |
| **States** | Provisioned, Active, Suspended, Terminated |
| **Triggers** | Signup, payment, admin actions, policy violations |

---

## Subscription States

```
[Provisioned] → [Active] → [Suspended] → [Terminated]
                    │            │
                    │            └─→ [Active] (reactivation)
                    │
                    ├─→ [Upgraded]
                    │
                    └─→ [Downgraded]
```

---

## State Definitions

| State | Description |
|-------|-------------|
| **Provisioned** | Subscription created, resources being allocated |
| **Active** | Subscription active, tenant fully operational |
| **Suspended** | Temporarily suspended (payment, policy, or admin action) |
| **Terminated** | Subscription ended, data retention period active |
| **Upgraded** | Tier upgrade in progress |
| **Downgraded** | Tier downgrade in progress |

---

## State Transitions

| From | To | Trigger | Approval |
|------|----|---------|----------|
| — | Provisioned | Signup/contract | Automated |
| Provisioned | Active | Resources ready | Automated |
| Active | Suspended | Payment failure, policy violation | Automated/Admin |
| Active | Upgraded | Upgrade request | Admin/Payment |
| Active | Downgraded | Downgrade request | Admin |
| Suspended | Active | Payment received, issue resolved | Automated/Admin |
| Suspended | Terminated | Grace period expired, termination request | Admin |
| Active | Terminated | Contract end, termination request | Admin |

---

## Provisioning Process

```
1. Signup/contract received
2. Create tenant record
3. Allocate resources based on tier:
   - Data stores
   - Memory stores
   - Knowledge stores
   - Compute quotas
4. Configure default I/O Gateways
5. Provision administrator accounts
6. Apply default branding
7. Transition to Active
```

---

## Suspension Policies

| Reason | Grace Period | Auto-Terminate |
|--------|--------------|----------------|
| Payment failure | 15 days | After 30 days |
| Policy violation | Immediate | Admin decision |
| Admin request | Immediate | N/A |

---

## Termination Process

```
1. Transition to Terminated state
2. Disable all access
3. Stop all processing
4. Begin data retention period (per policy)
5. Export data if requested
6. After retention period: purge data
```

---

## Related Documentation

- [Subscription Management Overview](./README.md)
- [Resource Management](./resource-management.md)
- [Administrators Management](./administrators-management.md)

---

*TODO: Detailed design — notification workflows, data export, retention policies*

