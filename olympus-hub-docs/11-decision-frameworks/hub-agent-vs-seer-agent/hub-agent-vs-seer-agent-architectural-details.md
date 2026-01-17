# Hub Agent vs Seer Agent: Architectural Details

> **Status**: 🟢 Design Complete  
> **Target Audience**: Developers, Agent Engineers  
> **Purpose**: C2-level architectural details and references to implementation documentation

---

## Overview

This document provides architectural-level details about Hub Agent and Seer Agent implementation, focusing on container-level (C2) interactions and relationships. For implementation details (C4 level), see the referenced documentation.

---

## ScenarioAsAgent CRD Architectural Role

### Relationship to Hub Agent Creation

The ScenarioAsAgent CRD is the mechanism that registers a Scenario as a Hub Agent. It does not create the Scenario or Hub Application; it configures the Scenario to participate as an agent.

**Architectural Flow**:
1. Scenario exists (with Hub Application)
2. ScenarioAsAgent CRD references the Scenario
3. CRD registers Agent Persona in Cipher IAM
4. Supervisor enrolls agent in task queue(s)
5. Scenario becomes a Hub Agent

### Key Architectural Points

- **ScenarioAsAgent CRD is the only way to create Hub Agents** — there is no other mechanism
- **Hub Agent is a configuration of Scenario**, not a property of Hub Application
- **The CRD bridges Scenario (automation) and Agent (participation)** — it doesn't change the automation itself
- **Agent Persona registration happens automatically** when the CRD is applied

### CRD Structure (Architectural Overview)

The CRD contains:
- `scenario_ref`: Reference to the source Scenario
- `agent`: Agent Persona configuration (name, display name, capabilities)
- `enrollment`: Task queue enrollment configuration (managed by Supervisor)

For complete CRD schema and YAML examples, see [`Scenario as Agent`](../../02-system-design/implementation-concepts/scenario-as-agent.md#scenarioasagent-crd).

> **Reference**: [`Scenario as Agent`](../../02-system-design/implementation-concepts/scenario-as-agent.md) provides the complete pattern definition and CRD structure. [`Developer Operators`](../../04-subsystems/operators/developer-operators.md#scenario-as-an-agent-operator) describes operator support.

---

## Agent Persona Registration (Architectural Process)

### What Happens (C2 Level)

When a ScenarioAsAgent CRD is applied:

1. **Agent Persona Creation**: Scenario's Agent Persona is registered in Cipher IAM
   - Persona name derived from CRD `agent.name`
   - Persona type: Agent
   - Persona bound to Scenario

2. **IAM Registration**: Cipher IAM creates the Agent Persona profile
   - Profile tagged as `agent` type
   - Profile linked to Scenario
   - Profile available for delegation and audit

3. **Enrollment Ready**: Agent Persona is ready for task queue enrollment
   - Supervisor can enroll in task queues
   - Agent can receive task assignments
   - Agent can produce Request Updates

### Identity Flow

```
Scenario → ScenarioAsAgent CRD → Cipher IAM → Agent Persona Registered → Enrollment Ready
```

For implementation details on Cipher IAM registration, see [`Cipher IAM Infrastructure`](../../05-infrastructure/cipher-iam-infrastructure.md).

> **Reference**: [`ADR-0129: Agent Identity Model`](../../decision-logs/0129-agent-identity-model.md) explains the Agent Persona identity layer. [`Cipher IAM Infrastructure`](../../05-infrastructure/cipher-iam-infrastructure.md) describes IAM integration.

---

## Task Queue Enrollment (Architectural Process)

### Enrollment Mechanism (C2 Level)

Task queue enrollment is a Supervisor operation that adds an Agent Persona to a task queue:

1. **Supervisor Action**: Supervisor enrolls agent via Supervisor Desk or API
2. **Queue Configuration**: Agent added to queue with allocation weight and priority
3. **Task Assignment**: Queue can now assign tasks to the agent
4. **Signal Routing**: Signal Exchange routes task assignments to the Scenario

### Enrollment Relationship

- **Enrollment is separate from CRD** — CRD registers the agent, Supervisor enrolls it
- **One agent can be enrolled in multiple queues** — same Agent Persona, different queues
- **Enrollment can be adjusted dynamically** — allocation weights, priorities, active/inactive

For task queue management details, see [`Task Management`](../../04-subsystems/task-management/README.md).

> **Reference**: [`Task Allocation`](../../02-system-design/implementation-concepts/task-allocation.md) describes work distribution. [`Task Management`](../../04-subsystems/task-management/README.md) explains queue operations.

---

## Identity Management (Architectural Overview)

### Token Structure (What Identities Are Included)

Delegation Access Tokens include both identity layers for Seer Agents:

```json
{
  "sub": "dispute-resolution-agent@acme.hub.io",  // Agent Persona (business identity)
  "iss": "cipher.hub.olympus.io",
  "client_id": "spiffe://acme.hub.io/seer/agent/acme/fraud-analyst-pod-001",  // Deployment Identity (SPIFFE)
  "delegated_by": "dispute-scenario-profile",  // Authority source
  "certificate_id": "cert-abc123",
  "template": "analyze-disputes",
  "scopes": ["disputes:read", "disputes:analyze"],
  "exp": "2026-01-17T22:00:00Z"
}
```

**Key Points**:
- `sub`: Agent Persona (business identity) — always present
- `client_id`: SPIFFE ID (deployment identity) — present for Seer Agents, may be absent for non-Seer Hub Agents
- `delegated_by`: Authority source (Scenario Identity Profile or Business User)

For token structure details and parsing, see [`Cipher IAM Extensions: Authority Delegation`](../../../olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/authority-delegation.md).

### Using Agent Persona vs SPIFFE ID

- **Agent Persona**: Used for business authorization, audit logs, delegation chains
- **SPIFFE ID**: Used for infrastructure authentication (mTLS, service mesh)

For implementation details on token usage, see [`Agent Identity and Credentials`](../../../olympus-seer-docs/seer-design/implementation-concepts/agent-identity-credentials.md).

> **Reference**: [`ADR-0129: Agent Identity Model`](../../decision-logs/0129-agent-identity-model.md) provides the complete two-layer identity model. [`Cipher IAM Extensions: Authority Delegation`](../../../olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/authority-delegation.md) describes token issuance.

---

## Protocol Interfaces (Architectural Overview)

### Available Protocols

Hub provides these protocol interfaces to ALL Hub Agents (regardless of runtime):

| Protocol | Use Case | When Used |
|----------|----------|-----------|
| **HTTP/REST** | Standard request/response | Task APIs, Request Updates, synchronous operations |
| **MCP** | Multi-turn, tool-based interaction | AI assistant integration, conversational interfaces |
| **A2A** | Agent-to-agent communication | Cross-agent collaboration, delegation |

### Protocol Selection (C2 Level)

- **HTTP/REST**: Default protocol for most Hub Agents, supports standard task operations
- **MCP**: Used when Hub Agent needs to integrate with AI assistants or conversational UIs
- **A2A**: Used for direct agent-to-agent communication without human intermediaries

Protocol selection is configured in ScenarioAsAgent CRD or Employment Spec, depending on agent type.

For protocol implementation details, see [`Channel`](../../02-system-design/implementation-concepts/channel.md) and [`Headless Access Service`](../../02-system-design/implementation-concepts/headless-access-service.md).

> **Reference**: [`Channel`](../../02-system-design/implementation-concepts/channel.md) describes protocol interfaces. [`Agent Model`](../../02-system-design/agent-model.md) explains agent interaction channels.

---

## Hub Application vs Hub Agent Relationship

### Architectural Distinction

- **Hub Application**: The automation artifact (code, configuration, runtime)
- **Hub Agent**: The participation pattern (how the application participates in task queues)

**Key Point**: A Hub Application becomes a Hub Agent when configured via ScenarioAsAgent CRD. The application code doesn't change; only the participation model changes.

### Relationship Diagram

```
Hub Application (automation artifact)
    │
    │ configured via
    ▼
ScenarioAsAgent CRD
    │
    │ registers
    ▼
Agent Persona (in Cipher IAM)
    │
    │ enrolled in
    ▼
Task Queue
    │
    │ becomes
    ▼
Hub Agent (participation pattern)
```

For Hub Application details, see [`Hub Application`](../../02-system-design/implementation-concepts/hub-application.md).

> **Reference**: [`Hub Application`](../../02-system-design/implementation-concepts/hub-application.md) describes the automation artifact. [`Scenario as Agent`](../../02-system-design/implementation-concepts/scenario-as-agent.md) explains the participation pattern.

---

## Seer Agent to Hub Agent Relationship

### Architectural Flow

A Seer Agent becomes a Hub Agent through:

1. **Employment Spec binds to Scenario** — Scenario provides Agent Persona
2. **Seer Agent deployed as Hub Application** — Employed Agent is a Hub Application
3. **ScenarioAsAgent CRD registers Scenario** — Scenario becomes a Hub Agent
4. **Seer Agent participates as Hub Agent** — Same Agent Persona, Hub Agent participation

**Key Point**: Seer Agent deployment automatically creates a Hub Application. The ScenarioAsAgent CRD then enables Hub Agent participation.

For Seer Agent deployment details, see [`Employed Agent as Hub Application`](../../../olympus-seer-docs/seer-design/hub-integration/employed-agent.md).

> **Reference**: [`Employed Agent as Hub Application`](../../../olympus-seer-docs/seer-design/hub-integration/employed-agent.md) explains Hub integration. [`Agent Lifecycle`](../../../olympus-seer-docs/seer-design/implementation-concepts/agent-lifecycle.md) describes the Raw → Trained → Employed progression.

---

## References to Implementation Documentation

### Testing

For testing Hub Agent behavior:
- [`Testing Hub Applications`](../../04-subsystems/testing/README.md) — General testing guidance
- [`Scenario Testing`](../../02-system-design/implementation-concepts/scenario-testing.md) — Scenario-level testing

### Troubleshooting

For operational troubleshooting:
- [`Operational Runbooks`](../../06-operations/runbooks/README.md) — Common operational issues
- [`Observability`](../../06-operations/observability/README.md) — Monitoring and debugging

### Code Examples

For runtime-specific code examples:
- [`Rhea Workflow Engine`](../../04-subsystems/automation-runtimes/rhea-workflow-engine.md) — Rhea examples
- [`Seer Agent SDK`](../../../olympus-seer-docs/seer-design/subsystems/seer-agent-sdk/README.md) — Seer Agent examples
- [`Hub Application Development`](../../02-system-design/implementation-concepts/hub-application-development.md) — General development patterns

### Operational Concerns

For operational considerations:
- [`Deployment`](../../05-infrastructure/deployment/README.md) — Deployment patterns
- [`Scaling`](../../06-operations/scaling/README.md) — Scaling considerations
- [`Security`](../../06-operations/security/README.md) — Security practices

---

## Related Documentation

### This Documentation Suite
- [`Hub Agent vs Seer Agent`](./hub-agent-vs-seer-agent.md) — Entry point and overview
- [`Core Concepts`](./hub-agent-vs-seer-agent-core.md) — Understanding and decision framework
- [`Examples`](./hub-agent-vs-seer-agent-examples.md) — Concrete use cases
- [`Anti-patterns`](./hub-agent-vs-seer-agent-anti-patterns.md) — When NOT to use Hub Agent pattern
- [`Customer Guide`](./hub-agent-vs-seer-agent-customer-guide.md) — Customer-facing explanations
