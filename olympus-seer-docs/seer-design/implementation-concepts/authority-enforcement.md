# Authority Enforcement

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-11

## Overview

Authority enforcement ensures AI agents operate within their delegated limits. Seer provides **multiple enforcement points** with **OPA-based policies** that validate agent actions against their authorized scope.

**Key Principle**: Enforcement is **layered** — violations are caught at the appropriate point and recorded on the Request for audit and corrective action.

---

## Enforcement Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTHORITY ENFORCEMENT FLOW                                │
│                                                                              │
│                         Agent Action                                         │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                   1. SIDECAR GUARDRAILS                              │   │
│   │                   (Tenant-defined, custom logic)                     │   │
│   │                   → Transform, Reject, or Pass                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                   2. TOOL GATEWAY                                    │   │
│   │                   • OPA policies (Tool Spec + Employment Spec)       │   │
│   │                   • IAM role and scope validation                    │   │
│   │                   → ALLOW / ALERT / REJECT                           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│                      Tool Execution                                          │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                   3. SIGNAL EXCHANGE                                 │   │
│   │                   • OPA policies on REQUEST_UPDATE                   │   │
│   │                   • Any agent update subject to policy               │   │
│   │                   → ALLOW / ALERT / REJECT                           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│                    Request Updated / Violation Recorded                      │
```

---

## Enforcement Points

### 1. Sidecar Guardrails

Tenant-defined guardrails provide **custom enforcement logic**:
- Deployed as Istio sidecars in agent pods
- Execute before/after agent actions
- Can transform, reject, or pass requests

**Use Case**: Domain-specific rules, compliance requirements, custom thresholds.

### 2. Tool Gateway

The Tool Gateway is the **primary enforcement point** for tool invocations:
- OPA policy evaluation (Tool Spec + Training Spec + Employment Spec)
- IAM role and scope validation
- Decision types: ALLOW, ALERT, REJECT

**Policy Sources:**
- Tool Specification policies (per-tool defaults)
- Training Specification policies (per-agent type)
- Employment Specification policies (per-deployment, overrides training)

### 3. Signal Exchange

Signal Exchange enforces policies on all agent updates:
- OPA policies on REQUEST_UPDATE messages
- Any agent update subject to policy evaluation
- Decision types: ALLOW, ALERT, REJECT

---

## OPA Policy Model

Policies are defined in Training and Employment Specs using OPA (Open Policy Agent):

**Policy Definition:**
- Declarative policies with known outcomes
- Employment Spec can override Training Spec policies (narrowing only)
- OPA decision types: ALLOW, ALERT, REJECT

**OPA Context Schema:**
- AgentContext (agent identity, role, authority)
- AccessContext (request context, user context)
- ToolGatewayContext (tool parameters, resource access)
- SignalExchangeContext (update content, request state)

---

## Violation Handling

When a violation is detected:

1. **Recording** — Violation recorded on Request
2. **Notification** — Observers, accountable person, workbench notified
3. **Corrective Actions** — Escalation, reassignment, intervention

---

## Key Principles

- **Layered Enforcement** — Multiple enforcement points catch violations at appropriate layers
- **OPA-Based** — Declarative policies with known outcomes
- **Policy Override** — Employment Spec can narrow (never expand) Training Spec policies
- **Violation Recording** — All violations recorded on Request for audit
- **Compound Agents** — Enforcement scoped to outer agent only

---

## Related

- `subsystems/seer-sidecar/README.md` - Sidecar guardrails execution
- `subsystems/agent-ingress-gateway/README.md` - Tool Gateway enforcement
- `subsystems/agent-lifecycle-manager/README.md` - Policy configuration in Employment Spec
- `implementation-concepts/guardrails.md` - Guardrails (complementary to authority enforcement)
- `olympus-hub-docs/04-subsystems/signal-exchange/README.md` - Signal Exchange enforcement

---

*For detailed implementation, see `subsystems/authority-enforcement.md` (to be migrated to `subsystems/seer-sidecar/` and `subsystems/agent-ingress-gateway/`).*
