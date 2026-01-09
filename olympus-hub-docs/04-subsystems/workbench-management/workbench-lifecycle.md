# Workbench Lifecycle

> **Status:** 🔴 Stub — Placeholder for expansion

Defines the lifecycle states and transitions for Workbenches.

---

## Lifecycle States

```
[Draft] → [Validated] → [Published] → [Active] → [Archived]
              │                           │
              └─→ [Rejected] → [Draft]    └─→ [Suspended] → [Active]
```

---

## State Definitions

| State | Description |
|-------|-------------|
| **Draft** | Workbench under development, not deployed |
| **Validated** | Tested in sandbox, ready for review |
| **Rejected** | Failed review, returned to draft |
| **Published** | Approved, ready for activation |
| **Active** | Live, processing signals |
| **Suspended** | Temporarily paused |
| **Archived** | Permanently deactivated |

---

## State Transitions

| From | To | Trigger | Approval |
|------|-----|---------|----------|
| Draft | Validated | Submit for validation | Automated tests |
| Validated | Published | Approval workflow | Workbench owner |
| Validated | Rejected | Review rejection | Reviewer |
| Rejected | Draft | Reopen | None |
| Published | Active | Deployment | Ops approval |
| Active | Suspended | Suspend command | Ops/Emergency |
| Suspended | Active | Resume command | Ops |
| Active | Archived | Archive command | Owner + Ops |

---

## Related Documentation

- [Workbench Management Overview](./README.md)
- [Scenario Definitions](./scenario-definitions.md)

---

*TODO: Detailed design — state machine, approval workflows, rollback*

