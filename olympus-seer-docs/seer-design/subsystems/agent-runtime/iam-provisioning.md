# IAM Profile Provisioning

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-12

---

## Overview

IAM Profile Provisioning is the process by which the **Seer Operator** creates, updates, and manages identity profiles for Employed Agents in **Cipher IAM Extensions**. Each Employed Agent receives a unique IAM profile that encapsulates its identity, authority delegation, group memberships, and OPA policies.

---

## IAM Profile Creation Flow

### 1. EmploymentSpec Contains Agent Identity

Each Employed Agent has a **unique code** within the tenant subscription, defined in the EmploymentSpec:

```yaml
apiVersion: seer.olympus.io/v1
kind: EmploymentSpec
metadata:
  name: fraud-analyst-acme-retail
  namespace: acme-disputes
spec:
  agentCode: "fraud-analyst-acme-retail"  # Unique within tenant subscription
  trainingSpecRef:
    name: fraud-analyst-v2
  delegation:
    type: user  # or "role"
    delegator: "user:john.smith@acme.com"
    accountable: "user:jane.manager@acme.com"
    roles: "*"  # or CSV: "fraud-reviewer,dispute-handler"
    groups: "disputes-team,fraud-analysts"
    policies:
      - pep: "tool-gateway"
        policyRef: "policies/tool-gateway-restrictions.rego"
      - pep: "signal-exchange"
        policyRef: "policies/signal-exchange-restrictions.rego"
  # ... other spec fields
```

### 2. Seer Operator Watches EmploymentSpec CRD

The Seer Operator watches for EmploymentSpec CRD creation and changes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       IAM PROFILE CREATION FLOW                              │
│                                                                              │
│   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐ │
│   │  EmploymentSpec │───▶│  Seer Operator  │───▶│  Cipher IAM Extensions  │ │
│   │     (CRD)       │    │   (watches)     │    │      (API calls)        │ │
│   └─────────────────┘    └─────────────────┘    └─────────────────────────┘ │
│                                  │                                           │
│                                  ▼                                           │
│                          ┌─────────────────┐                                │
│                          │ Hub Environment │                                │
│                          │  (endpoints)    │                                │
│                          └─────────────────┘                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. Operator Contacts Cipher IAM

The operator obtains IAM endpoints from the **Hub Environment** associated with the Workbench instance:

1. **Retrieve Hub Environment** — Get IAM endpoints from workbench configuration
2. **Call Cipher IAM Extensions API** — Create agent profile with delegation information
3. **Await Confirmation** — Wait for profile creation before proceeding with deployment

```
Seer Operator → Hub Environment → Cipher IAM Endpoints
                                        ↓
                               Create Agent Profile
                                        ↓
                               Configure Delegation
                                        ↓
                               Assign Roles/Groups
                                        ↓
                               Apply OPA Policies
```

---

## EmploymentSpec Profile Information

The EmploymentSpec contains all relevant profile information for the agent:

### 1. Authority Delegation Information

From `spec.delegation`:

| Field | Description | Example |
|-------|-------------|---------|
| `type` | Delegation type | `user` or `role` |
| `delegator` | Identity delegating authority | `user:john.smith@acme.com` |

### 2. Manager of the Employed Agent

From `spec.delegation.accountable`:

- The **accountable human** for the agent's actions
- Required for all Employed Agents
- Must be a valid user identity in Cipher IAM

### 3. User-Groups

From `spec.delegation.groups`:

- Groups the agent will be a member of
- Supports wildcard (`*`) or CSV list

### 4. OPA Policies per PEP

From `spec.delegation.policies`:

```yaml
policies:
  - pep: "tool-gateway"
    policyRef: "policies/tool-gateway-restrictions.rego"
  - pep: "signal-exchange"
    policyRef: "policies/signal-exchange-restrictions.rego"
  - pep: "model-gateway"
    policyRef: "policies/model-access.rego"
```

**Policy Configuration**:
- Policies can be **referenced files** (not inline) — `policyRef` points to policy files
- Unknown PEP policies are **ignored** — only PEPs registered with Cipher are processed
- Policy is specified **per PEP** that Cipher recognizes

---

## IAM Profile Lifecycle

### Profile Creation (During Deployment)

1. **Before Pod Creation** — IAM profile must exist before agent pods are created
2. **Failure Handling** — If Cipher cannot provision IAM profile, employment operation fails
3. **No Partial Deployment** — Agent is not deployed if IAM provisioning fails

```
EmploymentSpec Created
        │
        ▼
┌───────────────────┐
│ Seer Operator     │
│ Detects CRD       │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Create IAM Profile│──────▶ FAIL? ──▶ Employment Fails
│ via Cipher IAM    │
└─────────┬─────────┘
          │ SUCCESS
          ▼
┌───────────────────┐
│ Create K8s        │
│ Deployment        │
└───────────────────┘
```

### Profile Updates

The operator **always updates the profile** to keep in sync with the EmploymentSpec:

| Trigger | Action |
|---------|--------|
| EmploymentSpec changes | Operator updates profile immediately |
| Authority changes | Triggered by Delegation Chain Sync Service (see `authority-change-respawning.md`) |

### Profile Revocation (Kill Switch)

When a kill switch is activated:

1. **Immediate IAM Revocation** — Profile is revoked in Cipher IAM
2. **Pod Termination** — Agent pods are scaled to 0 or isolated
3. **Authority Revoked** — Agent can no longer authenticate

### Profile Cleanup (Agent Retirement)

On agent retirement:

1. **Graceful Shutdown** — Agent pods are terminated gracefully
2. **Profile Deletion** — IAM profile is removed from Cipher
3. **Group Cleanup** — Agent is removed from all groups

---

## Roles and Groups Inheritance Logic

### Wildcard Inheritance (`*`)

If EmploymentSpec uses `*` for roles or groups:

```yaml
spec:
  delegation:
    roles: "*"
    groups: "*"
```

**Behavior**:
- All delegator's roles are copied to agent at profile creation/update
- All delegator's groups are copied to agent at profile creation/update

### CSV Subset Inheritance

If EmploymentSpec uses CSV values:

```yaml
spec:
  delegation:
    roles: "fraud-reviewer,dispute-handler,case-closer"
    groups: "disputes-team,fraud-analysts"
```

**Behavior**:
1. Only roles/groups that the **delegator also has** will be retained
2. Requested roles/groups that the delegator **lacks** will be rejected
3. Deployment continues with **warning** status
4. Resource will be in **out-of-sync status** until unavailable roles/groups are removed

```
Requested: [fraud-reviewer, dispute-handler, case-closer]
Delegator Has: [fraud-reviewer, dispute-handler]

Result: [fraud-reviewer, dispute-handler]
        ⚠️ Warning: "case-closer" not available from delegator
        📌 Status: out-of-sync
```

---

## Bot Mode (No Delegator)

When there is **no delegator** specified:

```yaml
spec:
  delegation:
    type: bot
    accountable: "user:jane.manager@acme.com"
    roles: "automated-processor"
    groups: "bots"
```

**Bot Mode Behavior**:

| Aspect | Behavior |
|--------|----------|
| **Identity** | Base identity only |
| **Accountable Human** | The manager (required) |
| **Role Inheritance** | NOT inherited from any profile |
| **Group Inheritance** | NOT inherited from any profile |
| **Policy Inheritance** | NOT inherited from any profile |

Bot mode is used for fully automated agents that don't act on behalf of a specific user.

---

## IAM Profile Configuration

### EmploymentSpec to IAM Mapping

| EmploymentSpec Field | IAM Profile Field |
|---------------------|-------------------|
| `spec.agentCode` | Profile ID |
| `spec.delegation.delegator` | Delegation chain parent |
| `spec.delegation.accountable` | Accountable user |
| `spec.delegation.roles` | Role assignments |
| `spec.delegation.groups` | Group memberships |
| `spec.delegation.policies` | Policy attachments |

### Integration with Cipher IAM Policy Enforcement Points

Cipher IAM recognizes multiple Policy Enforcement Points (PEPs):

| PEP | Purpose |
|-----|---------|
| `tool-gateway` | Tool invocation authorization |
| `signal-exchange` | Request/response access control |
| `model-gateway` | LLM access control |
| `memory-service` | Agent memory access control |
| `knowledge-service` | Knowledge base access control |

### Credential Injection via zone-vault

Agent credentials are injected from zone-vault:

```yaml
spec:
  containers:
    - name: agent
      env:
        - name: AGENT_TOKEN
          valueFrom:
            secretKeyRef:
              name: fraud-analyst-secrets
              key: agent-token
```

---

## Schema Evolution

### EmploymentSpec Schema

The EmploymentSpec schema will evolve. Current delegation-related fields:

```yaml
spec:
  delegation:
    type: string        # "user" | "role" | "bot"
    delegator: string   # Identity URI
    accountable: string # Manager identity URI
    roles: string       # "*" or CSV
    groups: string      # "*" or CSV
    policies:
      - pep: string
        policyRef: string
```

**Schema Location**: `agent-lifecycle-manager/employment-spec-manager.md`

### TrainingSpec Schema

The TrainingSpec schema defines base authority constraints:

```yaml
spec:
  authority:
    ceilings:
      maxConcurrentRequests: number
      maxTokensPerRequest: number
    requiredCapabilities:
      - capability: string
```

**Schema Location**: `trained-agent-lifecycle-manager/` (to be detailed)

---

## Integration Points and References

### Related Documents

- `cipher-iam-extensions/README.md` - IAM API details
- `implementation-concepts/agent-lifecycle.md` - Delegation models
- `aosm-meta-model/raw-trained-employed-agents.md` - Delegation model details
- `why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-2-delegation-chains.md` - Delegation chains
- `hub-integration/employment-spec-crd.md` - EmploymentSpec schema

### Related Subsystems

- **Cipher IAM Extensions** - Provides IAM profile API
- **Agent Lifecycle Manager** - Manages EmploymentSpec, triggers authority updates
- **Agent Runtime** - Consumes IAM profiles for deployment

---

*IAM Profile Provisioning ensures every Employed Agent has a properly configured identity and authority profile before deployment.*
