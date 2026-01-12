# Authority Change Respawning

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-12

---

## Overview

Authority Change Respawning is the process by which Employed Agents are redeployed when their authority profiles change. This ensures that agents always operate with current, valid authority and that authority changes are enforced promptly.

---

## Authority Change Detection Architecture

### Separation of Concerns

The authority change detection system has two distinct components:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     AUTHORITY CHANGE DETECTION                               │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                AGENT LIFECYCLE MANAGER                               │   │
│   │                                                                       │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │          Agent Ecosystem Integration Services                │   │   │
│   │   │          (operates with tenant-admin authority)              │   │   │
│   │   │                                                               │   │   │
│   │   │   ┌───────────────┐                                          │   │   │
│   │   │   │ IAM Observer  │───▶ Listens to Cipher IAM changes       │   │   │
│   │   │   │   Service     │───▶ Tracks delegator role/group changes │   │   │
│   │   │   │               │───▶ Edits EmploymentSpec CRDs           │   │   │
│   │   │   └───────────────┘                                          │   │   │
│   │   │                                                               │   │   │
│   │   └───────────────────────────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                  │                                           │
│                                  │ Publishes CRD changes                     │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                SEER OPERATOR                                         │   │
│   │                                                                       │   │
│   │   • ONLY watches for CRD changes (EmploymentSpec, TrainingSpec)     │   │
│   │   • Does NOT listen to IAM directly                                  │   │
│   │   • Triggers respawning when CRD changes                             │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| **Seer Operator** | Only watches for changes to CRDs (EmploymentSpec, TrainingSpec) |
| **IAM Observer Service** | Listens to IAM changes, tracks delegator role/group changes |
| **Agent Ecosystem Integration Services** | Suite of services operating with tenant-admin authority |

---

## Authority Change Flow

### Step-by-Step Flow

```
1. IAM Change Occurs (delegator roles/groups changed)
            │
            ▼
2. IAM Observer Service Detects IAM Changes
   (listens to Cipher IAM events)
            │
            ▼
3. IAM Observer Service Edits EmploymentSpec CRD
   (propagates authority changes to agent specs)
            │
            ▼
4. Seer Operator Watches CRD and Detects Change
   (only monitors CRD, not IAM directly)
            │
            ▼
5. Seer Operator Triggers Respawning Process
```

### Sequence Diagram

```
┌─────────┐    ┌─────────────┐    ┌────────────────┐    ┌──────────────┐
│Cipher   │    │IAM Observer │    │EmploymentSpec  │    │Seer Operator │
│IAM      │    │Service      │    │CRD             │    │              │
└────┬────┘    └──────┬──────┘    └───────┬────────┘    └──────┬───────┘
     │                │                    │                    │
     │ Role/Group     │                    │                    │
     │ Change Event   │                    │                    │
     │───────────────▶│                    │                    │
     │                │                    │                    │
     │                │ Edit CRD           │                    │
     │                │ (update authority) │                    │
     │                │───────────────────▶│                    │
     │                │                    │                    │
     │                │                    │ Watch detects      │
     │                │                    │ CRD change         │
     │                │                    │───────────────────▶│
     │                │                    │                    │
     │                │                    │           Trigger  │
     │                │                    │          Respawn   │
     │                │                    │                    │
```

---

## Authority Change Sources

### 1. Training Spec CRD Updates

Agent class authority changes:

| Change Type | Example |
|-------------|---------|
| Authority ceilings | `maxConcurrentRequests` changed |
| Required capabilities | New capability added/removed |
| Base permissions | Fundamental permissions changed |

### 2. Employment Spec CRD Updates

Agent instance authority changes:

| Trigger Source | Description |
|----------------|-------------|
| **IAM Observer Service** | Delegator roles/groups change |
| **Other Agent Ecosystem Services** | Direct employment config changes |
| **Manual Updates** | Admin-initiated changes |

---

## Respawning Triggers

The following changes trigger agent respawning:

### 1. Authority Ceilings Change

Must respawn to apply new limits:

```yaml
# Before
spec:
  authority:
    maxConcurrentRequests: 10

# After
spec:
  authority:
    maxConcurrentRequests: 5
```

**Reason**: Authority ceilings are enforced at pod initialization.

### 2. Delegation Chain Changes

Detected via IAM Observer Service when delegator's authority shrinks:

```
Delegator: john.smith@acme.com
Original Roles: [admin, reviewer, processor]
New Roles: [reviewer]  ← "admin" and "processor" removed

Agent must respawn with reduced authority
```

### 3. OPA Policy Updates

Affect runtime enforcement:

```yaml
# New policy restricts tool access
policies:
  - pep: "tool-gateway"
    policyRef: "policies/restricted-tools.rego"  # Updated policy
```

**Reason**: OPA policies are loaded at sidecar initialization.

### 4. Kill Switch Deactivation

Resume with new authority after kill switch is lifted:

```
Agent Status: KILLED → ACTIVE (with authority review)
```

---

## Respawning Process

### Process Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         RESPAWNING PROCESS                                   │
│                                                                              │
│   1. Seer Operator detects EmploymentSpec CRD change                        │
│                          │                                                   │
│                          ▼                                                   │
│   2. Graceful Shutdown ──────────────────────────────────────────────────▶  │
│      • Drain existing connections                                            │
│      • Complete in-flight requests (with timeout)                           │
│      • Signal pods for termination                                           │
│                          │                                                   │
│                          ▼                                                   │
│   3. Update IAM Profiles ────────────────────────────────────────────────▶  │
│      • Update Cipher IAM Extensions (if authority changed)                  │
│      • Sync roles/groups from delegator                                     │
│      • Apply new OPA policies                                               │
│                          │                                                   │
│                          ▼                                                   │
│   4. Redeploy with Updated EmploymentSpec ───────────────────────────────▶  │
│      • Create new pods with updated configuration                           │
│      • Inject new credentials from zone-vault                               │
│      • Initialize with updated authority                                    │
│                          │                                                   │
│                          ▼                                                   │
│   5. Zero-Downtime Respawning ───────────────────────────────────────────▶  │
│      • Rolling update via Argo Rollouts                                     │
│      • Progressive traffic shift                                            │
│      • Automatic rollback on failure                                        │
│                          │                                                   │
│                          ▼                                                   │
│   6. Verification ───────────────────────────────────────────────────────▶  │
│      • Health checks pass                                                   │
│      • Policy validation confirms new authority                             │
│      • Agent operational with updated profile                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Argo Rollouts Strategy

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: fraud-analyst-acme-retail
spec:
  strategy:
    canary:
      steps:
        - setWeight: 20
        - pause: { duration: 2m }
        - setWeight: 50
        - pause: { duration: 5m }
        - setWeight: 100
      analysis:
        templates:
          - templateName: authority-verification
```

---

## Integration Points

### Agent Lifecycle Manager

- **Agent Ecosystem Integration Services** - Contains IAM Observer Service
- **Delegation Chain Sync Service** - Monitors and syncs delegation chains

See: `agent-lifecycle-manager/agent-ecosystem-integration-services.md`

### Cipher IAM Extensions

- Authority changes detected by IAM Observer
- Profile updates via Cipher IAM API

See: `cipher-iam-extensions/README.md`

### Seer Sidecar

- Policy enforcement updates
- OPA policy reloading

See: `seer-sidecar/README.md`

---

## Related Documentation

- `agent-lifecycle-manager/agent-ecosystem-integration-services.md` - IAM Observer Service
- `agent-lifecycle-manager/README.md` - Agent Ecosystem Integration Services overview
- `cipher-iam-extensions/README.md` - Cipher IAM integration
- `iam-provisioning.md` - IAM profile creation and lifecycle
- `implementation-concepts/authority-enforcement.md` - Authority enforcement concepts

---

*Authority Change Respawning ensures that Employed Agents always operate with current, valid authority profiles.*
