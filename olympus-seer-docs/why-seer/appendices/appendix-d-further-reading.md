# Appendix D: Further Reading

This appendix provides links to additional documentation for readers who want to explore specific topics in greater depth.

---

## Conceptual Foundations

### Agent Concepts

| Document | Description |
|----------|-------------|
| `olympus-seer-docs/agentic-ai-concepts/enterprise-agent-platform.md` | What an enterprise agent platform provides |
| `olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md` | Practical guide to agent design |
| `olympus-seer-docs/agentic-ai-concepts/agent-memory/` | Memory concepts and management |
| `olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/` | Knowledge services concepts |

### AOSM Meta-Model

| Document | Description |
|----------|-------------|
| `aosm-meta-model/agent-oriented-system.md` | Core AOSM concepts |
| `aosm-meta-model/raw-trained-employed-agents.md` | Three-layer agent lifecycle |
| `aosm-meta-model/controlled-autonomy.md` | Autonomy governance model |

---

## Seer Design Documentation

### Overview

| Document | Description |
|----------|-------------|
| `olympus-seer-docs/seer-design/introduction.md` | Seer introduction and overview |
| `olympus-seer-docs/seer-design/premise.md` | Design premise and philosophy |

### Subsystems

| Document | Description |
|----------|-------------|
| `olympus-seer-docs/seer-design/subsystems/agent-lifecycle/` | Agent lifecycle management |
| `olympus-seer-docs/seer-design/subsystems/model-gateway.md` | Bifrost model gateway |
| `olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md` | Context compilation |
| `olympus-seer-docs/seer-design/subsystems/guardrails.md` | Guardrail implementation |
| `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md` | Authority and ceilings |
| `olympus-seer-docs/seer-design/subsystems/agent-identity-authority.md` | Identity model |
| `olympus-seer-docs/seer-design/subsystems/agent-observability.md` | Observability and health |
| `olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md` | Request-Scoped Authority Delegation |
| `olympus-seer-docs/seer-design/implementation-concepts/persona-twin-blueprint.md` | Persona Twin Blueprint |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/README.md` | Seer Sentinels |
| `olympus-seer-docs/seer-design/subsystems/cognitive-operations-governance-workbench/README.md` | COGW design |

### Hub Integration

| Document | Description |
|----------|-------------|
| `olympus-seer-docs/seer-design/hub-integration/README.md` | Integration overview |

### Personas

| Document | Description |
|----------|-------------|
| `olympus-seer-docs/seer-design/personas-and-needs/` | Enterprise personas and their needs |
| `olympus-seer-docs/seer-design/ux-architecture/` | UX architecture and Desks |

---

## Hub Documentation

### System Design

| Document | Description |
|----------|-------------|
| `olympus-hub-docs/README.md` | Hub overview |
| `olympus-hub-docs/02-system-design/` | System architecture |
| `olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md` | CAF design |
| `olympus-hub-docs/02-system-design/implementation-concepts/agent-directability.md` | Directability model |

### Subsystems

| Document | Description |
|----------|-------------|
| `olympus-hub-docs/04-subsystems/memory-services/README.md` | Memory services overview |
| `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md` | CAF subsystem |
| `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md` | Learning promotion |
| `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/explanation-service.md` | Explanation generation |
| `olympus-hub-docs/04-subsystems/registry-services/tool-registry.md` | Tool registry |
| `olympus-hub-docs/04-subsystems/task-management/README.md` | Task management |
| `olympus-hub-docs/04-subsystems/signal-exchange/README.md` | Signal routing |
| `olympus-hub-docs/04-subsystems/signal-exchange/application-router.md` | Application Router (composite routing) |
| `olympus-hub-docs/04-subsystems/mcp-channel/mcp-server-crd.md` | MCP Server CRD |
| `olympus-hub-docs/04-subsystems/mcp-channel/directory-service.md` | MCP Directory Service |
| `olympus-hub-docs/04-subsystems/feedback-services/README.md` | Feedback capture |

### Composite Patterns

| Document | Description |
|----------|-------------|
| `olympus-hub-docs/02-system-design/implementation-concepts/hub-composite-application.md` | Hub Composite Applications design |
| `olympus-hub-docs/09-composite-systems-and-patterns/scenario-as-a-tool.md` | Scenario-as-Tool pattern |
| `olympus-hub-docs/09-composite-systems-and-patterns/scenario-as-an-agent.md` | Scenario-as-Agent pattern |
| `olympus-hub-docs/09-composite-systems-and-patterns/workbench-as-a-machine.md` | Workbench-as-Machine pattern |
| `olympus-hub-docs/09-composite-systems-and-patterns/devops-workbench/README.md` | DevOps Workbench |

---

## Requirements Documentation

| Document | Description |
|----------|-------------|
| `olympus-seer-docs/requirements-enterprise-agentic-platform/08-platform-components.md` | Platform component requirements |
| `olympus-seer-docs/requirements-enterprise-agentic-platform/09-platform-services-table.md` | Service requirements matrix |

---

## Decision Records

### Seer Decisions

| ADR | Title |
|-----|-------|
| `olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md` | Guardrails architecture |
| `olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md` | Authority enforcement |

### Identity & Authority Decisions

| ADR | Title |
|-----|-------|
| `olympus-hub-docs/decision-logs/0127-request-scoped-authority-delegation.md` | Request-Scoped Authority Delegation |
| `olympus-hub-docs/decision-logs/0129-agent-identity-model.md` | Agent Identity Model (Deployment vs Persona) |
| `olympus-hub-docs/decision-logs/0130-unified-delegation-model.md` | Unified Delegation Model |

### Collaboration Channels Decisions

| ADR | Title |
|-----|-------|
| `olympus-hub-docs/decision-logs/0131-mcp-server-crd-design.md` | MCP Server CRD Design |
| `olympus-hub-docs/decision-logs/0132-mcp-template-kinds.md` | MCP Template Kinds |
| `olympus-hub-docs/decision-logs/0134-mcp-directory-service.md` | MCP Directory Service |

### Composite Patterns Decisions

| ADR | Title |
|-----|-------|
| `olympus-hub-docs/decision-logs/0125-hub-composite-applications.md` | Hub Composite Applications |
| `olympus-hub-docs/decision-logs/0126-composite-routing-table-schema.md` | Composite Routing Table Schema |

### Memory Decisions

| ADR | Title |
|-----|-------|
| `olympus-hub-docs/decision-logs/0061-no-pii-in-episodic-memory.md` | No PII in Episodic Memory |
| `olympus-hub-docs/decision-logs/0062-memory-writes-via-signal-exchange.md` | Memory write routing |
| `olympus-hub-docs/decision-logs/0067-agent-memory-session-scope.md` | Agent Memory scope |

---

## External References

### Standards and Frameworks

- **SPIFFE:** Secure Production Identity Framework for Everyone
- **OPA:** Open Policy Agent for policy enforcement
- **OpenTelemetry:** Observability framework
- **MCP:** Model Context Protocol

### Regulatory Context

- **OCC SR 11-7:** Model Risk Management guidance
- **EU AI Act:** European AI regulation
- **Fair Lending Laws:** ECOA, Fair Housing Act

---

*Note: All paths are relative to the workspace root. Use your IDE's navigation or search to locate specific documents.*
