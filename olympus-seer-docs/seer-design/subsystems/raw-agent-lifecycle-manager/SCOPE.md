# Raw Agent Lifecycle Manager: Scope and Coverage

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Coverage Summary

The Raw Agent Lifecycle Manager subsystem provides comprehensive C2-level design documentation for managing Raw Agent specifications, directory, operators, and levers. Raw Agents are NOT deployable on their own; they are containers referenced by Employed Agents through Training Specs and deployed only as part of Employed Agent instances.

### Design Documents

| Document | Status | Description |
|----------|--------|-------------|
| [Raw Agent Spec Manager](raw-agent-spec-manager.md) | 🟢 Complete | Raw Agent CRD structure with structured/typed capabilities, validation rules |
| [Raw Agent Directory](raw-agent-directory.md) | 🟢 Complete | Raw Agent registry, capability discovery, versioning, search |
| [Raw Agent Operators](raw-agent-operators.md) | 🟢 Complete | Raw Agent lifecycle management (registration, validation, versioning, discovery) |
| [Raw Agent Levers](raw-agent-levers.md) | 🟢 Complete | Kill switches, capability toggles, emergency controls |

---

## Design Status

### Completed

- ✅ **Raw Agent Spec Manager**: Complete C2-level design covering:
  - Raw Agent CRD structure with structured/typed capabilities
  - Tool calling, orchestration, archetype roles, prompt tags
  - Documentation references for different developer personas
  - Container image reference and validation
  - Identity for recognizing derived agents

- ✅ **Raw Agent Directory**: Complete C2-level design covering:
  - Raw Agent registry and automatic registration
  - Capability-based discovery and search
  - Versioning and version tracking
  - Suitability scoring and matching

- ✅ **Raw Agent Operators**: Complete C2-level design covering:
  - Registration, validation, versioning, discovery operators
  - Kubernetes reconciliation patterns
  - Container image validation
  - Directory updates

- ✅ **Raw Agent Levers**: Complete C2-level design covering:
  - Kill switches and capability toggles
  - Emergency controls
  - Lever execution methods
  - Lever rollback

---

## Intended Depth

### C2-Level (Container) Design

All components are designed at the C2 (Container) level, focusing on:
- Functional scope and capabilities
- Integration points with other subsystems
- Conceptual models and data flows
- Operational flows and sequences

### C3-Level (Component) Detail

The following areas include C3-level detail for critical mechanisms:
- **Capability Matching Algorithm**: Detailed matching logic for capability-based discovery
- **Validation Rules**: Detailed validation logic for Raw Agent Specs
- **Lever Execution**: Detailed execution logic for levers
- **Operator Reconciliation**: Detailed reconciliation patterns

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **CRD Schema** | Complete CRD OpenAPI schema definitions |
| **Capability Matching Algorithm** | Specific matching logic, scoring algorithms |
| **Validation Rules** | Complete validation rule implementations |
| **Lever Execution** | Detailed execution logic, propagation mechanisms |
| **Operator Reconciliation** | Detailed reconciliation loop implementations |
| **Directory Indexing** | Search index implementation, indexing strategies |
| **Performance Optimization** | Caching strategies, query optimization |
| **Error Handling** | Specific error codes, retry policies |

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
