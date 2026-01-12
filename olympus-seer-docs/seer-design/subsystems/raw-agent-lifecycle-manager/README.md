# Raw Agent Lifecycle Manager

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Overview

The Raw Agent Lifecycle Manager manages Raw Agent specifications, directory, operators, and levers. **Important**: Raw Agents are NOT deployable on their own; they are containers referenced by Employed Agents through Training Specs and deployed only as part of Employed Agent instances within workbench environments.

**Key Design Point**: Raw Agent Specs include structured/typed capabilities (tool calling, orchestration, archetype roles, prompt tags) that help Agent Engineers evaluate suitability. The spec also includes documentation references for Trained/Employed Agent developers and container image references.

---

## Design Documents

| Document | Status | Description |
|----------|--------|-------------|
| [Raw Agent Spec Manager](raw-agent-spec-manager.md) | 🟢 Complete | Raw Agent CRD structure with structured/typed capabilities, validation rules |
| [Raw Agent Directory](raw-agent-directory.md) | 🟢 Complete | Raw Agent registry, capability discovery, versioning, search |
| [Raw Agent Operators](raw-agent-operators.md) | 🟢 Complete | Raw Agent lifecycle management (registration, validation, versioning, discovery) |
| [Raw Agent Levers](raw-agent-levers.md) | 🟢 Complete | Kill switches, capability toggles, emergency controls |
| [SCOPE](SCOPE.md) | 🟢 Complete | Coverage summary, design status, intended depth, implementation details deferred |

---

## Key Design Decisions

### Raw Agents Are NOT Deployable

**Decision**: Raw Agents are containers referenced by Training Specs; only Employed Agents are deployable.

**Rationale**:
- Raw Agents are foundational artifacts without organizational knowledge
- Training Specs add organizational knowledge and domain skills
- Employment Specs add authority and work context
- Only Employed Agents have complete configuration for deployment

### Structured/Typed Capabilities

**Decision**: Capabilities are structured and typed (not free-form text).

**Rationale**:
- Enables programmatic capability discovery
- Supports automated suitability evaluation
- Ensures consistent capability declarations
- Enables capability-based search and filtering

### Capability Declaration for Agent Engineers

**Decision**: Capabilities are declared for Agent Engineers to evaluate suitability.

**Capability Types**:
- **Tool Calling Capabilities**: Supported tool protocols, tool invocation patterns
- **Orchestration Capabilities**: Multi-agent coordination, workflow orchestration
- **Archetype Roles**: Supported roles (thinker, doer, orchestrator, governor)
- **Prompt Tags**: Tags supported for prompts and their meaning in Authority Enforcement

**Rationale**:
- Agent Engineers need to understand what Raw Agents can do
- Capabilities help match Raw Agents to use cases
- Supports informed selection of Raw Agents for Training Specs

### Documentation References

**Decision**: Raw Agent Specs include documentation references for different developer personas.

**Documentation Types**:
- **Agent Engineer Docs**: Capability documentation for evaluating suitability
- **Trained Agent Developer Docs**: Integration documentation for Training Spec creation
- **Employed Agent Developer Docs**: Deployment documentation for Employment Spec creation

**Rationale**:
- Different personas need different documentation
- Agent Engineers need capability documentation
- Trained Agent developers need integration documentation
- Employed Agent developers need deployment documentation

### Identity for Recognizing Derived Agents

**Decision**: Raw Agent identity is used to recognize derived Trained and Employed Agents.

**Rationale**:
- Enables tracking of agent lineage
- Supports impact analysis when Raw Agents change
- Enables capability-based agent discovery
- Supports agent version management

### Centralized Control via Levers

**Decision**: Levers provide centralized control over all derived Employed Agents.

**Rationale**:
- Enables rapid response to issues
- Single point of control for all deployments
- Reduces operational overhead
- Supports emergency controls and capability toggles

---

## Related Documentation

### Seer Design
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Training/Employment Spec management
- [Agent Runtime](../agent-runtime/README.md) — Employed Agent deployment
- [Agent Archetypes](../../../why-seer/part-2-how-seer-solves/11-multi-agent-patterns-in-seer/11-2-agent-archetypes.md)

### Hub Documentation
- [Container Registry](../../../olympus-hub-docs/05-infrastructure/container-registry.md) — Container image management

---

*Raw Agent Lifecycle Manager manages Raw Agent specifications, directory, operators, and levers, enabling Agent Engineers to discover and evaluate Raw Agents while supporting centralized control through levers.*
