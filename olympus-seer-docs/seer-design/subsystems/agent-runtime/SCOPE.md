# Agent Runtime Subsystem - Scope and Detailed Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Scope

The **Agent Runtime** subsystem provides the runtime environment for deployed Employed Agents. It is responsible for:

1. **Deployment Operations** - Deploying Employed Agents to Kubernetes (Atlantis)
2. **Scaling Operations** - Horizontal and vertical scaling of agent pods
3. **Lifecycle Management** - Rolling updates, respawning, kill switches
4. **Infrastructure Provisioning** - IAM profiles, ingress paths, networking
5. **Signal Exchange Integration** - Receiving request updates via sx-observer
6. **Agent Ingress Gateway Integration** - Routing requests to deployed agents

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| `runtime-deployment.md` | Core runtime architecture, deployment, scaling, security | ✅ Complete |
| `iam-provisioning.md` | IAM profile creation, lifecycle, delegation, bot mode | ✅ Complete |
| `authority-change-respawning.md` | Authority change detection and respawning process | ✅ Complete |
| `signal-exchange-integration.md` | sx-observer service, store-and-forward, scale-to-zero | ✅ Complete |
| `agent-ingress-gateway-integration.md` | Request routing, response handling, data store integration | ✅ Complete |

---

## Coverage Summary

### ✅ Architecture & Infrastructure (runtime-deployment.md)
- **Architecture Overview** - Atlantis (EKS), Heracles (API Gateway), Istio (Service Mesh)
- **Deployment Flow** - Hub Operator → EmploymentSpec CRD → Seer Operator → K8s Deployment
- **Pod Architecture** - Container composition (main agent, Istio sidecar, guardrail sidecars)
- **Resource Specification** - Training Spec requirements vs Employment Spec allocation

### ✅ Request Dispatch (runtime-deployment.md)
- **Traffic Path** - Signal Exchange → Heracles → K8s Service → Istio → Guardrails → Agent
- **Session Affinity** - Opportunistic routing based on request_id
- **Networking** - Service-to-service communication via Istio, egress control

### ✅ Configuration & Secrets (runtime-deployment.md)
- **Credential Injection** - Environment variables from zone-vault
- **Configuration Updates** - Rolling updates via Argo Rollouts

### ✅ Lifecycle Operations (runtime-deployment.md)
- **Rolling Updates** - Progressive delivery when Training/Employment Specs change
- **Kill Switch** - Scale to 0 or Network Policy isolation

### ✅ Raw Agent Contract (runtime-deployment.md)
- **Required Endpoints** - `/dispatch`, `/health`, `/metrics`
- **Request/Response Formats** - Standardized dispatch protocol

### ✅ Autoscaling (runtime-deployment.md)
- **Horizontal Pod Autoscaler** - CPU, memory, custom metrics (agent_active_requests)

### ✅ Observability (runtime-deployment.md)
- **Tracing** - Jaeger integration via Istio
- **Metrics** - Prometheus endpoints
- **Logging** - Stdout/stderr → Watch

### ✅ Security (runtime-deployment.md)
- **Zero-Trust Model** - mTLS, Network Policies, Pod Security Policies, RBAC
- **Workload Segregation** - Namespace-per-workbench, resource quotas

### ✅ Ingress Path Provisioning (runtime-deployment.md)
- **Path Pattern** - `/seer/subscription/{subscription_id}/data-plane/workbench/{workbench_id}/agents/{agent_id}/dispatch`
- **Cluster-ingress** - Internal only, not publicly accessible
- **Authentication** - zone-auth verification of sx-observer credentials
- **Lifecycle** - Creation after IAM profile, updates on config changes, cleanup on retirement

### ✅ IAM Profile Provisioning (iam-provisioning.md)
- **IAM Profile Creation Flow** - EmploymentSpec → Seer Operator → Cipher IAM Extensions
- **EmploymentSpec Profile Information** - Delegation, manager, groups, OPA policies per PEP
- **IAM Profile Lifecycle** - Creation, updates, revocation, cleanup
- **Roles/Groups Inheritance Logic** - Wildcard vs CSV subset
- **Bot Mode** - No delegator, base identity only
- **Schema Evolution** - EmploymentSpec and TrainingSpec schemas

### ✅ Authority Change Respawning (authority-change-respawning.md)
- **Architecture** - Seer Operator watches CRDs only; IAM Observer Service watches IAM
- **Authority Change Flow** - IAM change → IAM Observer → CRD update → Seer Operator → Respawn
- **Authority Change Sources** - TrainingSpec, EmploymentSpec, IAM Observer Service
- **Respawning Triggers** - Authority ceilings, delegation chain, OPA policies, kill switch
- **Respawning Process** - Graceful shutdown, IAM update, zero-downtime rolling update

### ✅ Signal Exchange Integration (signal-exchange-integration.md)
- **sx-observer Architecture** - Workbench-level observer for Signal Exchange
- **Architecture Separation** - Signal Exchange unaware of Agent Ingress Gateway
- **Store and Forward** - Durable message queue for reliable delivery
- **Back-Pressure Handling** - Flow control to prevent overwhelming agents
- **Scale-to-Zero** - Requests stored; sx-observer triggers scale-up
- **Message Transport** - All routing via Atropos (event bus)
- **Request Update Flow** - SX → Atropos → sx-observer → Atropos → Agent Ingress Gateway → Agents
- **Filtering Logic** - Based on scenarios and agent subscriptions

### ✅ Agent Ingress Gateway Integration (agent-ingress-gateway-integration.md)
- **Request Update Dispatch** - sx-observer → Atropos → Agent Ingress Gateway → Agent pods
- **Response Path** - Agents update requests directly via Hub APIs (not via sx-observer)
- **External Resource References** - URIs to Workbench Data Store for large outputs
- **Workbench Data Store** - Hub-provided Object and Stream store
- **Error Handling** - DLQ in Atropos, configurable retries, Cronus Exceptions
- **sx-observer Lifecycle** - Registration, updates, cleanup

---

## Design Gaps Summary

| Area | Status | Document |
|------|--------|----------|
| IAM Profile Provisioning | ✅ Complete | `iam-provisioning.md` |
| Respawning After Authority Changes | ✅ Complete | `authority-change-respawning.md` |
| Signal Exchange Integration | ✅ Complete | `signal-exchange-integration.md` |
| Agent Ingress Gateway Integration | ✅ Complete | `agent-ingress-gateway-integration.md` |
| Ingress Path Configuration | ✅ Complete | `runtime-deployment.md` |

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **sx-observer** | Storage backend, queue type, retention policies |
| **Back-Pressure Handling** | Thresholds, throttling algorithms, configuration |
| **Scale-Up** | Scaling mechanisms, warm-up times, HPA configuration |
| **Load Balancing** | Specific algorithms, session affinity |
| **Observability** | Specific metrics, dashboard layouts |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

- **`cipher-iam-extensions/`** - IAM profile provisioning, authority delegation
- **`agent-lifecycle-manager/`** - Employment spec management, delegation chain sync, IAM Observer Service
- **`agent-ingress-gateway/`** - Subscription lifecycle, request routing
- **`seer-sidecar/`** - Policy enforcement, authority enforcement
- **`seer-agent-sdk/`** - SDK for agent response handling, data store access

---

## Related Documentation

- `implementation-concepts/agent-lifecycle.md` - Agent lifecycle model
- `implementation-concepts/authority-enforcement.md` - Authority enforcement concepts
- `olympus-hub-docs/04-subsystems/signal-exchange/README.md` - Signal Exchange
- `olympus-hub-docs/05-infrastructure/atropos.md` - Atropos event bus
- `olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md` - ADR: Runtime on Atlantis

---

*This scope document reflects the completed detailed design of the Agent Runtime subsystem.*
