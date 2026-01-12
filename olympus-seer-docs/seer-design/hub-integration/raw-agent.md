# Raw Agent in Hub Context

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

A **Raw Agent** is the deployable technical artifact — an OCI container — that implements agent behavior using any agentic framework. Raw Agents are **framework-agnostic** and managed entirely by Seer's CI/CD pipeline.

**Hub does not deploy Raw Agents.** Hub interacts with agents at the Trained and Employed layers.

---

## Definition

| Dimension | Description |
|-----------|-------------|
| **Artifact** | OCI Container image |
| **Runtime** | Olympus Atlantis (serverless container runtime) |
| **Framework** | Any — LangChain, LangGraph, Strands, CrewAI, custom, etc. |
| **CI/CD** | Managed by Seer (not Hub) |
| **Topology** | Can be compound (multi-agent internally) |

---

## Framework Flexibility

Hub and Seer do not prescribe or recommend any specific agentic framework:

| Aspect | Hub/Seer Position |
|--------|-------------------|
| **Framework Choice** | Developer's decision |
| **Internal Topology** | Agent's concern (Hub sees one agent) |
| **Orchestration** | Agent's responsibility |
| **Sub-agents** | Invisible to Hub |

### Compound Agents

A Raw Agent container can host multiple sub-agents internally:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         RAW AGENT CONTAINER                                  │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    Orchestrator Agent                                │   │
│   │                                                                       │   │
│   │   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐    │   │
│   │   │ Sub-Agent │   │ Sub-Agent │   │ Sub-Agent │   │ Sub-Agent │    │   │
│   │   │     A     │   │     B     │   │     C     │   │     D     │    │   │
│   │   └───────────┘   └───────────┘   └───────────┘   └───────────┘    │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   To Hub: This is ONE agent                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

- **Hub perspective**: Single Employed Agent
- **Internal reality**: Complex multi-agent topology
- **Lifecycle/orchestration**: Orchestrator's responsibility
- **Sub-agent memory**: Accessible via parent's Agent Memory scope

---

## Externalized Capabilities

Raw Agents are designed with externalized configuration points:

| Capability | Externalized? | Injected At |
|------------|---------------|-------------|
| **Tools** | ✅ Yes | Training/Employment |
| **Resources** | ✅ Yes | Training/Employment |
| **Skills (Prompts)** | ✅ Yes | Training |
| **Knowledge Bases** | ✅ Yes | Training |
| **Guardrails** | ✅ Yes | Training (immutable) |

### Inbuilt Capabilities

Raw Agents typically include:

| Capability | Description |
|------------|-------------|
| **Context Compilation** | Agent-specific context assembly logic |
| **Conversation Orchestration** | Multi-turn dialog management |
| **Framework Guardrails** | Framework-level safety constraints |
| **Memory Management** | Framework-native memory patterns |

> **Note**: The scope of a Raw Agent is **not bounded** by this definition. Developers are at liberty to define them as they deem appropriate.

---

## Container Requirements

### Image Specification

```yaml
# Example Raw Agent container spec
apiVersion: seer.olympus.io/v1
kind: RawAgentSpec
metadata:
  name: fraud-analyst-base
  version: v2.4.1
spec:
  image:
    registry: registry.olympus.io
    repository: seer/agents/fraud-analyst
    tag: v2.4.1
    digest: sha256:abc123...
  
  runtime:
    platform: atlantis
    resources:
      cpu: "2"
      memory: "4Gi"
      gpu: false
  
  capabilities:
    modalities:
      - text
      - structured-data
    protocols:
      - http
      - grpc
    frameworks:
      - strands  # Informational, not enforced
  
  health:
    liveness: /health/live
    readiness: /health/ready
    startup: /health/startup
```

### Required Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/invoke` | POST | Receive request updates from Seer Runtime |
| `/health/live` | GET | Liveness probe |
| `/health/ready` | GET | Readiness probe |
| `/health/startup` | GET | Startup probe |

### Environment Variables

Injected at runtime by Seer:

| Variable | Source | Description |
|----------|--------|-------------|
| `SEER_AGENT_ID` | EmploymentSpec | Employed Agent identifier |
| `SEER_TENANT_ID` | Deployment | Tenant context |
| `SEER_WORKBENCH_ID` | Deployment | Workbench context |
| `SEER_SCENARIO_ID` | Deployment | Scenario context |
| `HUB_MEMORY_ENDPOINT` | Platform | Agent Memory Services URL |
| `HUB_TOOL_ENDPOINT` | Platform | Direct Tool Dispatcher URL |
| `SEER_CAE_ENDPOINT` | Platform | Context Assembly Engine URL |

---

## Lifecycle

Raw Agent lifecycle is managed by Seer (not Hub):

```
[Developed] → [Built] → [Published] → [Deployed*] → [Retired]
                                          │
                                          └── *Deployed via Training/Employment
```

| State | Description | Owner |
|-------|-------------|-------|
| **Developed** | Source code complete | Agent Developer |
| **Built** | Container image in registry | Seer CI/CD |
| **Published** | Available for Training | Seer |
| **Deployed** | Running as Employed Agent | Seer Operator |
| **Retired** | Decommissioned | Seer |

---

## Versioning

Raw Agents follow semantic versioning:

```
v<major>.<minor>.<patch>
```

- **Major**: Breaking changes to invocation contract
- **Minor**: New capabilities, backward compatible
- **Patch**: Bug fixes, no capability changes

### Compatibility

TrainingSpec declares compatible Raw Agent version range:

```yaml
spec:
  rawAgent:
    name: fraud-analyst-base
    version: "^2.0.0"  # Compatible with 2.x.x
```

---

## Hub Integration Points

Although Hub doesn't directly manage Raw Agents, it indirectly interacts through:

| Integration | Via | Description |
|-------------|-----|-------------|
| **Invocation** | Seer Runtime → Pod | Request updates dispatched to agent |
| **Memory** | Agent Memory SDK | Agent accesses Hub-provided memory stores |
| **Tools** | Direct Tool Dispatcher | Agent invokes Hub-registered tools |
| **Knowledge** | Knowledge Bank API | Agent retrieves policy/procedure documents |
| **Context** | CAE SDK | Agent compiles context from Hub Memory |

---

## Related Documentation

- [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md) — Employment spec management
- [Trained Agent in Hub](./trained-agent.md) — How Raw becomes Trained
- [Request Dispatch](./request-dispatch.md) — How requests reach agents
- [Agent Memory Developer Guide](../../../olympus-hub-docs/10-guides/agent-memory-developer-guide.md) — Memory best practices

---

*Raw Agents are the technical foundation — framework-agnostic containers that Seer configures and Hub utilizes.*

