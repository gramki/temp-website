# ADR-0125: Hub Composite Applications

## Status

**Accepted**

## Date

2026-01-15

## Context

Hub Applications support single-app-per-scenario patterns where one application handles all request processing. However, many multi-agent collaboration patterns require multiple agents to participate in the same request without explicit orchestration:

- **Blackboard Pattern**: Multiple specialists contribute independently to shared state
- **Planner-Executor-Critic (PEC Loop)**: Agents coordinate through update types, not task assignment
- **Market-Based**: Agents bid/react to broadcasts without central scheduler
- **Role-Specialized Committees**: Multiple perspectives on high-stakes decisions

The existing task-assignment model supports Manager-Worker and Hierarchical patterns but doesn't support event-driven, blackboard-style coordination.

### Requirements

1. Multiple Hub Applications must participate in the same Request
2. Applications coordinate through shared Request state (blackboard), not task assignment
3. Each application operates independently with its own session
4. Support for OPA filters to route updates selectively to applications
5. Support for cross-runtime composites (Seer + Rhea + Atlantis)
6. Support for nested composites
7. No changes to existing Hub Application specs

## Decision

**Introduce Hub Composite Applications** - a new CRD type that groups multiple Hub Applications to participate in the same Request.

### Key Design Decisions

1. **Deployment-Time Resolution**: Composites are resolved at deployment time by operators. Signal Exchange sees only a flattened list of apps, not composites.

2. **Independent Sessions**: Each constituent app gets its own independent session. No shared session state.

3. **OPA Filter-Based Routing**: Each app can have an OPA filter to selectively receive updates based on `update_type` and request state.

4. **All-or-Nothing Deployment**: If any app in composite fails to deploy, entire composite deployment fails and rolls back.

5. **Cross-Runtime Support**: Composites can include apps from different runtimes (Seer, Rhea, Atlantis, etc.).

6. **Nested Composites**: Composites can reference other composites, resolved recursively to union of all apps.

### CRD Structure

**HubCompositeApplicationSpec**:
- Lists constituent applications (HubApplicationSpec refs or nested composite refs)
- Optional OPA filter per app for update routing
- Metadata including topology pattern

**HubCompositeApplicationDeployment**:
- References HubCompositeApplicationSpec
- Owns child HubApplicationDeployment resources
- Aggregates child status to composite status

**ScenarioAutomationSpec Update**:
- `application.ref` for single app (existing)
- `application.composite_ref` for composite (new, mutually exclusive)

### Architecture

```
ScenarioAutomationSpec
  └── application.composite_ref → HubCompositeApplicationSpec
        └── applications: [App1, App2, Composite2]
              └── Composite2 → [App3, App4]
        
At deployment:
  HubCompositeApplicationDeployment
    └── HubApplicationDeployment: App1
    └── HubApplicationDeployment: App2
    └── HubApplicationDeployment: App3
    └── HubApplicationDeployment: App4
    
Routing Table (populated by operator):
  scenario_id → [App1 (+ filter), App2 (+ filter), App3 (+ filter), App4 (+ filter)]
  
Signal Exchange (runtime):
  Request Update → Application Router → [App1, App2, App3, App4] (after OPA filter evaluation)
```

## Consequences

### Positive

- **Enables multi-agent topologies**: Blackboard, PEC Loop, Market-Based, Committees
- **No changes to existing apps**: Existing HubApplicationSpecs work unchanged
- **Lightweight**: No special composite runtime, uses existing Signal Exchange
- **Flexible filtering**: OPA filters enable sophisticated update routing
- **Cross-runtime**: Mix Seer, Rhea, Atlantis in one composite
- **Observable**: Each app's contributions tracked with source_app in request history

### Negative

- **Deployment complexity**: All-or-nothing deployment can be restrictive
- **Update conflicts**: Multiple apps can update same request concurrently (resolved by latest-wins)
- **No dynamic composition**: Composite changes require redeployment

### Neutral

- **Signal Exchange unchanged**: Still operates at Request level only
- **Routing table schema change**: Supports list of apps per scenario (backward compatible)

## Related

- [Hub Composite Application](../02-system-design/implementation-concepts/hub-composite-application.md)
- [ADR-0126: Composite Routing Table Schema](./0126-composite-routing-table-schema.md)
- [ADR-0007: Composite Pattern Technology Agnostic](./0007-composite-pattern-technology-agnostic.md)
- [Multi-Agent Topologies](../../olympus-seer-docs/agentic-ai-concepts/multi-agent-topologies.md)

---

*This ADR enables sophisticated multi-agent collaboration patterns while maintaining Hub's request-level governance and observability.*
