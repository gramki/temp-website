# Agent Runtime

> **Category:** DevOps and Lifecycle  
> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-15

---

## Overview

Agent Runtime provides the **execution environment for Employed Agents** deployed in Seer. It handles pod-based deployment on Atlantis (EKS), scaling operations, IAM profile provisioning, Signal Exchange integration via sx-observer, and automatic respawning when authority changes occur. Agent Runtime ensures agents run securely, scalably, and with proper observability within the Hub ecosystem.

---

## Ontology Context

### Relationship to Ontology

Agent Runtime implements the **deployment and execution layer** for the Employed Agent layer in the AOSM three-layer model:

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|-------------|
| **Employed Agent** | Pod-based deployment on Atlantis | Runtime provides execution environment |
| **Controlled Autonomy** | Resource limits, network isolation, policy enforcement | Runtime enforces autonomy boundaries |
| **Authority** | IAM profile provisioning, credential injection | Runtime ensures agents operate with correct authority |
| **Observability** | Metrics, traces, health endpoints | Runtime provides visibility into agent execution |
| **Availability** | Scaling, scale-to-zero, respawning | Runtime ensures agent availability |

### Gap This Fills

The AOSM ontology defines the Employed Agent concept but doesn't specify how agents are deployed and executed in practice. Agent Runtime fills this gap by providing:

1. **Container Orchestration**: Pod-based deployment on Kubernetes (Atlantis/EKS)
2. **Scaling Mechanisms**: HPA-based scaling and scale-to-zero support
3. **Signal Exchange Integration**: sx-observer pattern for request routing
4. **Authority Management**: IAM profile provisioning and credential injection
5. **Resilience**: Automatic respawning on authority changes, health monitoring

---

## Definition

**Agent Runtime** is the execution environment that deploys, scales, and manages Employed Agent pods on Atlantis (EKS). It provides pod orchestration, IAM profile provisioning, Signal Exchange integration via sx-observer, ingress path provisioning, and automatic respawning when authority changes occur.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Per Employed Agent deployment (workbench-scoped) |
| **Lifecycle** | Created via EmploymentSpec CRD → IAM profile created → Pods deployed → Scaled → Respawning on authority changes → Terminated on kill switch |
| **Ownership** | Agent Reliability Engineer (ARE) manages runtime operations; Seer Operator reconciles CRDs |
| **Multiplicity** | One runtime deployment per Employed Agent; multiple pods per agent (scaling) |

---

## Rationale

### Why This Design?

**Pod-Based Deployment on Atlantis**:
- Leverages existing Kubernetes infrastructure (Atlantis/EKS)
- Standard container orchestration patterns
- Integration with Istio service mesh for mTLS and observability

**sx-observer Pattern**:
- Signal Exchange remains unaware of individual agents
- Workbench-level observer simplifies routing
- Store-and-forward enables scale-to-zero
- Back-pressure handling prevents overload

**IAM Profile Before Pod Deployment**:
- Agents must have valid identity before execution
- Credentials injected at pod startup
- Authority changes trigger respawning (security requirement)

**Authority Change Respawning**:
- Agents must always operate with current authority
- IAM Observer Service watches IAM changes
- Seer Operator only watches CRDs (separation of concerns)

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Direct Signal Exchange Integration** | Would require Signal Exchange to know about all agents; sx-observer provides abstraction |
| **IAM Profile After Deployment** | Security risk; agents must have valid identity before execution |
| **Manual Respawning** | Authority changes must be enforced automatically; manual process is error-prone |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0074: Runtime on Atlantis](../../../olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md) | Agent Runtime deployed on Atlantis (EKS) |
| [ADR-0104: Agent Runtime Detailed Design](../../../olympus-hub-docs/decision-logs/0104-seer-agent-runtime-detailed-design.md) | Detailed runtime architecture |

---

## Structure

### Key Attributes

```yaml
# Conceptual Agent Runtime deployment structure
agent_runtime:
  employment_spec_ref:
    name: string
    version: string
  
  iam_profile:
    agent_code: string
    delegation:
      type: user | role | bot
      delegator: string
      accountable: string
      roles: string  # "*" or CSV
      groups: string  # CSV
  
  pod_spec:
    image: string
    replicas: integer
    resources:
      requests:
        cpu: string
        memory: string
      limits:
        cpu: string
        memory: string
    env:
      - name: string
        value: string | secretKeyRef
  
  ingress:
    path: string  # /seer/{workbench}/{agent_id}/dispatch
    service: string
  
  scaling:
    min_replicas: integer
    max_replicas: integer
    scale_to_zero: boolean
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **IAM Provisioning** | IAM profile being created | → Pod Deployment |
| **Pod Deployment** | Pods being created | → Running |
| **Running** | Pods active, receiving requests | → Scaling, → Respawning, → Terminated |
| **Scaling** | Replicas being adjusted | → Running |
| **Respawning** | Pods being recreated due to authority change | → Running |
| **Terminated** | Pods terminated (kill switch) | (terminal) |

---

## Behavior

### How It Works

#### Deployment Flow

```
1. EmploymentSpec CRD created/updated
2. Seer Operator watches CRD
3. IAM profile created via Cipher IAM Extensions API
4. Credentials retrieved from zone-vault
5. Kubernetes Deployment created
6. Pods scheduled on Atlantis nodes
7. Istio sidecar injected automatically
8. Seer Sidecar containers added
9. Ingress path provisioned on Heracles
10. sx-observer registers agent for routing
11. Pods ready, receiving requests
```

#### Scaling Flow

```
1. HPA monitors pod metrics (CPU, memory, request queue)
2. If metrics exceed thresholds, scale up
3. If metrics below thresholds and scale-to-zero enabled, scale down
4. sx-observer handles scale-to-zero (store-and-forward)
5. Scale-up triggered when requests arrive at zero replicas
```

#### Authority Change Respawning Flow

```
1. IAM change occurs (delegator roles/groups changed)
2. IAM Observer Service detects change
3. IAM Observer Service edits EmploymentSpec CRD
4. Seer Operator detects CRD change
5. Existing pods terminated
6. New IAM profile created
7. New pods deployed with updated authority
8. Old pods gracefully terminated
```

#### Request Routing Flow

```
1. Signal Exchange publishes request update to Atropos (workbench topic)
2. sx-observer receives update
3. sx-observer filters by scenario and agent subscriptions
4. sx-observer stores update (store-and-forward)
5. sx-observer publishes to Atropos (agent-specific topic)
6. Agent Ingress Gateway receives update
7. Heracles routes to agent pod via ingress path
8. Agent processes request
9. Agent updates request directly via Hub APIs (not via sx-observer)
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| **Seer Operator** | ← | Receives EmploymentSpec CRD updates, reconciles to Kubernetes |
| **Cipher IAM Extensions** | → | Creates/updates IAM profiles, retrieves credentials |
| **Atlantis (EKS)** | → | Deploys pods, manages container lifecycle |
| **Istio Service Mesh** | ↔ | Injects sidecar, provides mTLS, traffic management |
| **Heracles Gateway** | → | Provisions ingress paths, routes requests |
| **Signal Exchange** | ← | Receives request updates via sx-observer |
| **sx-observer** | ↔ | Receives updates, filters, routes to agents |
| **Seer Sidecar** | ↔ | Enforces guardrails, policies, authority checks |
| **Agent Lifecycle Manager** | ← | IAM Observer Service edits CRDs on authority changes |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **IAM Before Pods** | IAM profile must be created before pod deployment |
| **Authority Respawning** | Authority changes always trigger pod respawning (cannot update in-place) |
| **Scale-to-Zero Store** | sx-observer must store requests when agents scale to zero |
| **Direct Hub API Updates** | Agents update requests directly via Hub APIs, not via sx-observer |
| **Signal Exchange Isolation** | Signal Exchange is unaware of Agent Ingress Gateway |
| **One sx-observer Per Workbench** | Each workbench has one sx-observer instance |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Scalable Execution** | HPA-based scaling adapts to load automatically |
| ✅ **Scale-to-Zero** | Agents can scale to zero when idle, reducing costs |
| ✅ **Secure Deployment** | IAM profiles and credential injection ensure secure execution |
| ✅ **Authority Enforcement** | Automatic respawning ensures agents always have current authority |
| ✅ **Resilient Routing** | sx-observer store-and-forward prevents request loss |
| ✅ **Observable** | Integration with Istio and Watch provides full observability |
| ✅ **Standard Infrastructure** | Leverages Kubernetes and Istio (proven patterns) |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Respawning Overhead** | Authority changes are infrequent; respawning ensures security |
| ⚠️ **sx-observer Complexity** | Clear separation of concerns; sx-observer is workbench-scoped |
| ⚠️ **Scale-to-Zero Latency** | Store-and-forward ensures requests are not lost; scale-up is fast |
| ⚠️ **IAM Dependency** | IAM profile creation is fast; deployment waits for completion |

---

## Examples

### Example 1: Basic Agent Deployment

**Use Case**: Deploy a fraud analyst agent with 2 replicas

```yaml
# EmploymentSpec CRD
apiVersion: seer.olympus.io/v1
kind: EmploymentSpec
metadata:
  name: fraud-analyst-acme-retail
  namespace: acme-disputes
spec:
  agentCode: "fraud-analyst-acme-retail"
  trainingSpecRef:
    name: fraud-analyst-v2
  workScope:
    workbench: acme-disputes
    scenarios:
      - retail-fraud-triage
  capacity:
    min_replicas: 2
    max_replicas: 10
    scale_to_zero: false
  delegation:
    type: user
    delegator: "user:john.smith@acme.com"
    accountable: "user:jane.manager@acme.com"
    roles: "*"
    groups: "disputes-team,fraud-analysts"
```

**Runtime Behavior**:
1. Seer Operator creates IAM profile for `fraud-analyst-acme-retail`
2. Kubernetes Deployment created with 2 replicas
3. Pods scheduled on Atlantis nodes
4. Ingress path provisioned: `/seer/acme-disputes/fraud-analyst-acme-retail/dispatch`
5. sx-observer registers agent for routing
6. Agent ready to receive requests

---

### Example 2: Scale-to-Zero Configuration

**Use Case**: Deploy agent that scales to zero when idle

```yaml
spec:
  capacity:
    min_replicas: 0
    max_replicas: 5
    scale_to_zero: true
```

**Runtime Behavior**:
1. Agent scales down to 0 replicas when idle
2. sx-observer stores incoming requests
3. When request arrives, HPA triggers scale-up
4. Pods created, agent processes stored requests
5. After idle period, scales back to zero

---

### Example 3: Authority Change Respawning

**Use Case**: Delegator's roles change, agent must respawn

**Initial State**:
```yaml
delegation:
  delegator: "user:john.smith@acme.com"
  roles: "fraud-reviewer,dispute-handler"
```

**IAM Change**: User `john.smith@acme.com` gains role `senior-fraud-reviewer`

**Runtime Behavior**:
1. IAM Observer Service detects role change
2. IAM Observer Service edits EmploymentSpec CRD (updates `roles` field)
3. Seer Operator detects CRD change
4. Existing pods terminated gracefully
5. New IAM profile created with updated roles
6. New pods deployed with updated authority
7. Agent resumes operation with new authority

---

## Implementation Notes

### For Developers

- **Pod Image**: Must be OCI-compliant container image from Training Spec
- **Health Endpoints**: Pods must expose `/health` endpoint for readiness/liveness probes
- **Metrics Endpoint**: Pods should expose Prometheus metrics on `:9090/metrics`
- **Request Dispatch**: Agents receive requests on `/dispatch` endpoint (HTTP POST)
- **Hub API Integration**: Agents call Hub APIs directly (not via sx-observer)

### For Operators

- **IAM Profile Creation**: Monitor IAM profile creation; deployment waits for completion
- **Scaling Configuration**: Tune HPA thresholds based on workload patterns
- **Scale-to-Zero**: Enable only for non-critical agents; consider latency impact
- **Authority Changes**: Monitor IAM Observer Service logs for authority change detection
- **Respawning**: Respawning is automatic; monitor for successful completion
- **Ingress Paths**: Ingress paths are automatically provisioned; verify in Heracles

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Agent Lifecycle](./agent-lifecycle.md) | Runtime executes Employed Agent layer |
| [Request Routing & Ingress](./request-routing-ingress.md) | Agent Ingress Gateway routes requests to runtime |
| [Seer Sidecar](./seer-sidecar.md) | Sidecar enforces policies at runtime |
| [Agent Identity & Credentials](./agent-identity-credentials.md) | IAM profile provisioning and credential injection |
| [Kill Switch & Emergency Controls](./kill-switch-emergency-controls.md) | Runtime terminates pods on kill switch |
| [Delegation Chains](./delegation-chains.md) | Authority delegation model implemented in runtime |

---

## References

- [Agent Runtime Subsystem](../subsystems/agent-runtime/README.md) — Complete subsystem documentation
- [Runtime Deployment](../subsystems/agent-runtime/runtime-deployment.md) — Pod architecture and deployment flow
- [IAM Provisioning](../subsystems/agent-runtime/iam-provisioning.md) — IAM profile creation and credential injection
- [Signal Exchange Integration](../subsystems/agent-runtime/signal-exchange-integration.md) — sx-observer pattern
- [Authority Change Respawning](../subsystems/agent-runtime/authority-change-respawning.md) — Respawning on authority changes
- [Agent Ingress Gateway Integration](../subsystems/agent-runtime/agent-ingress-gateway-integration.md) — Request dispatch and response handling
- [Atlantis Infrastructure](../../../olympus-hub-docs/05-infrastructure/atlantis.md) — Kubernetes platform
- [Istio Service Mesh](../../../olympus-hub-docs/05-infrastructure/istio.md) — Service mesh integration
- [Heracles Gateway](../../../olympus-hub-docs/05-infrastructure/heracles-gateway.md) — Ingress gateway

---

*Agent Runtime provides secure, scalable, and observable execution for Employed Agents, ensuring they operate with proper authority and resilience within the Hub ecosystem.*
