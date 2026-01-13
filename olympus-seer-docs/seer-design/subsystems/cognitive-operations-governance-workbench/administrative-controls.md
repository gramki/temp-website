# Administrative Controls

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14  
> **Design Level**: C2 (Container)

---

## Overview

Administrative Controls define how COG Sentinels are managed in both COGW workbenches (full control) and target workbenches (limited control). Target workbench admins can enable/disable COG Sentinels but cannot modify specifications.

---

## Control Model

### Two-Level Control

| Level | Location | Capabilities |
|-------|----------|--------------|
| **COGW Control** | COGW workbench | Full control (create, update, delete, enable/disable) |
| **Local Control** | Target workbenches | Limited control (enable/disable only) |

### Control Summary

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COG SENTINEL CONTROL MODEL                                │
│                                                                              │
│   COGW WORKBENCH (Full Control)         TARGET WORKBENCH (Limited Control)  │
│   ──────────────────────────────         ─────────────────────────────────  │
│                                                                              │
│   ┌─────────────────────────────┐        ┌─────────────────────────────┐   │
│   │ COG Sentinel                 │        │ Read-only Sentinel Specs    │   │
│   │                              │        │                              │   │
│   │ ✅ Create                    │        │ ❌ Create (managed by COGW)  │   │
│   │ ✅ Update specs              │        │ ❌ Update (read-only)        │   │
│   │ ✅ Delete                    │        │ ❌ Delete (managed by COGW)  │   │
│   │ ✅ Enable/Disable globally   │        │ ✅ Enable/Disable locally    │   │
│   │ ✅ Modify cogSpec patterns   │        │ ❌ Modify patterns           │   │
│   │ ✅ View status               │        │ ✅ View status               │   │
│   │                              │        │                              │   │
│   └─────────────────────────────┘        └─────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## COGW Controls

### Full Control in COGW Workbench

COGW admins (with appropriate roles) have full control over COG Sentinels:

| Action | Description | Effect |
|--------|-------------|--------|
| **Create** | Create new COG Sentinel | Synced to matching target workbenches |
| **Update Specs** | Modify SentinelScenarioSpecs | Changes synced to all targets |
| **Delete** | Delete COG Sentinel | Removed from all target workbenches |
| **Enable Globally** | Activate COG Sentinel | Active in all matching targets |
| **Disable Globally** | Deactivate COG Sentinel | Inactive in all targets |
| **Modify cogSpec** | Change target patterns | Re-evaluated, workbenches added/removed |

### Global Enable/Disable

When COGW admin disables a COG Sentinel globally:

1. **Sentinel marked inactive** in COGW
2. **Sync to targets** — All target workbenches receive disabled status
3. **Signal Exchange** — Auto-enrollment deregistered
4. **Existing child requests** — Continue to completion, no new enrollments

```yaml
# COGW control via Sentinel Levers
apiVersion: seer.olympus.io/v1
kind: SentinelLeverAction
metadata:
  name: disable-token-governance
  namespace: acme-cogw
spec:
  sentinel_ref:
    name: token-governance-sentinel
  action: disable
  scope: global  # Affects all target workbenches
  reason: "Maintenance window"
```

---

## Local Controls (Target Workbenches)

### Limited Control in Target Workbenches

Target workbench admins have limited control:

| Action | Allowed | Description |
|--------|---------|-------------|
| **View** | ✅ | See COG Sentinel status and configuration |
| **Enable** | ✅ | Enable COG Sentinel in this workbench |
| **Disable** | ✅ | Disable COG Sentinel in this workbench |
| **Modify Specs** | ❌ | Specs are read-only |
| **Delete** | ❌ | Managed by COGW Operator |
| **Modify Patterns** | ❌ | cogSpec is read-only |

### Local Enable/Disable

When target workbench admin disables a COG Sentinel locally:

1. **Local status set to disabled** — Only in this workbench
2. **Signal Exchange** — Auto-enrollment deregistered for this workbench only
3. **Other workbenches** — Unaffected
4. **COGW status** — Still shows as active (global status unchanged)

```yaml
# Local control via Sentinel Levers
apiVersion: seer.olympus.io/v1
kind: SentinelLeverAction
metadata:
  name: disable-token-governance-local
  namespace: production-loans
spec:
  sentinel_ref:
    name: token-governance-sentinel
    source_workbench: acme-cogw  # Identifies as COG Sentinel
  action: disable
  scope: local  # Only this workbench
  reason: "Testing new deployment"
```

---

## Visibility in Target Workbenches

### Sentinel Directory Display

COG Sentinels appear in target workbench Sentinel Directory:

| Field | Value | Notes |
|-------|-------|-------|
| **Name** | Original COG Sentinel name | Same as in COGW |
| **Type** | `request` | Standard sentinel type |
| **Source** | `COG: <cogw-workbench>/<sentinel-name>` | Identifies as COG Sentinel |
| **Global Status** | Active/Disabled | Set by COGW admin |
| **Local Status** | Active/Disabled | Set by local admin |
| **Effective Status** | Active only if both global AND local are active | |
| **Read-only** | Yes | Cannot modify specs |

### Example Directory Entry

```yaml
sentinel_directory_entry:
  name: token-governance-sentinel
  type: request
  source:
    type: cog_sentinel
    cogw_workbench: acme-cogw
    source_sentinel: token-governance-sentinel
  
  status:
    global: active      # Set by COGW admin
    local: active       # Set by local admin
    effective: active   # Both must be active
  
  read_only: true
  
  last_sync: "2026-01-14T10:30:00Z"
  
  actions_available:
    - enable
    - disable
  
  actions_blocked:
    - update
    - delete
```

---

## Read-only Enforcement

### Annotation-based Enforcement

Read-only status is enforced via annotations:

```yaml
metadata:
  annotations:
    sentinel.olympus.io/read-only: "true"
    sentinel.olympus.io/cog-sentinel-source: "acme-cogw/token-governance-sentinel"
```

### Validation Webhook

The Sentinel Spec Manager validation webhook enforces read-only status:

```python
def validate_sentinel_spec_update(old_spec, new_spec):
    # Check if read-only
    if old_spec.metadata.annotations.get("sentinel.olympus.io/read-only") == "true":
        # Only allow status changes via Sentinel Levers
        if specs_differ(old_spec.spec, new_spec.spec):
            return ValidationError(
                "Cannot modify read-only COG Sentinel spec. "
                "Modifications must be made in source COGW workbench."
            )
    return ValidationSuccess()
```

### Allowed Changes

Even with read-only annotation, these changes are allowed:

| Change | Allowed By | Mechanism |
|--------|------------|-----------|
| **Local status** | Local admin | Sentinel Levers |
| **Sync updates** | COGW Operator | Special service account |
| **Deletion** | COGW Operator | Special service account |

---

## Status Hierarchy

### Effective Status Calculation

```
Effective Status = Global Status AND Local Status

┌─────────────────────────────────────────────────────────────────────────────┐
│                    EFFECTIVE STATUS CALCULATION                              │
│                                                                              │
│   Global Status    Local Status     Effective Status                        │
│   ─────────────    ────────────     ─────────────────                       │
│                                                                              │
│   Active      +    Active       =   Active (enrolled, receiving signals)    │
│   Active      +    Disabled     =   Disabled (not enrolled)                 │
│   Disabled    +    Active       =   Disabled (not enrolled)                 │
│   Disabled    +    Disabled     =   Disabled (not enrolled)                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Status Display in UI

```
Token Governance Sentinel
├── Type: Request Sentinel (COG)
├── Source: acme-cogw
├── Global Status: ● Active
├── Local Status: ○ Disabled
├── Effective: ○ Disabled
└── Actions: [Enable] [View Details]
```

---

## Audit Trail

### Actions Logged

All control actions are logged for audit:

| Action | Logged Data |
|--------|-------------|
| **COGW Create** | Who, when, spec content |
| **COGW Update** | Who, when, changes made |
| **COGW Delete** | Who, when, reason |
| **COGW Enable/Disable** | Who, when, reason, scope |
| **Local Enable/Disable** | Who, when, reason, workbench |

### Audit Log Entry

```yaml
audit_entry:
  timestamp: "2026-01-14T10:30:00Z"
  action: local_disable
  actor:
    user_id: admin@acme.com
    role: workbench_admin
  target:
    sentinel_name: token-governance-sentinel
    workbench: production-loans
    type: cog_sentinel
    source_workbench: acme-cogw
  details:
    previous_local_status: active
    new_local_status: disabled
    reason: "Testing new deployment"
```

---

## Related Documentation

- [COGW Operator](./cogw-operator.md) — Read-only sync mechanism
- [COG Sentinel Specification](./cog-sentinel-specification.md) — COG Sentinel definition
- [Sentinel Levers](../seer-sentinels/sentinel-levers.md) — Enable/disable controls
- [Sentinel Directory](../seer-sentinels/sentinel-directory.md) — Sentinel visibility

---

*Administrative Controls enable centralized governance from COGW while allowing target workbench autonomy through local enable/disable controls and clear visibility of COG Sentinel status.*
