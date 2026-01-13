# ADR-0126: Composite Routing Table Schema

## Status

**Accepted**

## Date

2026-01-15

## Context

With the introduction of Hub Composite Applications (ADR-0125), Signal Exchange's Application Router needs to route Request Updates to multiple applications per scenario. The routing table currently supports one application per scenario.

### Requirements

1. Support multiple applications per scenario (for composites)
2. Support OPA filters per application for selective update routing
3. Maintain backward compatibility with single-app scenarios
4. Keep Signal Exchange unaware of composite concept (deployment-time resolution)

## Decision

**Extend routing table schema** to support both single-app and multi-app scenarios, with backward compatibility.

### Schema Change

**Current Schema** (single app):
```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  application:
    deployment_id: "dispute-handler-sandbox"
    endpoint: "http://..."
```

**New Schema** (backward compatible):
```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  
  # Single app (existing - for backward compatibility)
  application:
    deployment_id: "dispute-handler-sandbox"
    endpoint: "http://..."
  
  # OR multiple apps (new - for composites)
  applications:
    - deployment_id: "risk-agent-deployment-sandbox"
      endpoint: "http://..."
      opa_filter: "<compiled Rego policy>"
    - deployment_id: "compliance-agent-deployment-sandbox"
      endpoint: "http://..."
      opa_filter: "<compiled Rego policy>"
```

### Routing Logic

Application Router behavior:

1. If `applications` field exists: route to all apps (after OPA filter evaluation)
2. If only `application` field exists: existing behavior (direct dispatch)

### OPA Filter Storage

- Filters stored as compiled Rego policies in routing table
- Compiled at deployment time by Composite Deployment Operator
- Cached for performance during routing

### Population

Composite Deployment Operator populates routing table:
1. Resolves composite recursively (flattens nested composites)
2. Compiles OPA filters for each app
3. Populates `applications` array with deployment IDs, endpoints, and compiled filters

## Consequences

### Positive

- **Backward compatible**: Existing single-app scenarios unchanged
- **Simple routing logic**: Application Router just checks which field exists
- **Performance**: Compiled filters cached in routing table
- **Signal Exchange unchanged**: Still Request-level only, no composite awareness

### Negative

- **Schema complexity**: Two fields for same concept (single vs multi)
- **Validation needed**: Ensure exactly one of `application` or `applications` is set

### Neutral

- **Routing table is internal**: Schema change doesn't affect external APIs

## Related

- [ADR-0125: Hub Composite Applications](./0125-hub-composite-applications.md)
- [Application Router](../04-subsystems/signal-exchange/application-router.md)
- [Composite Deployment Operator](../04-subsystems/operators/developer-operators.md)

---

*This ADR enables multi-app routing while maintaining backward compatibility and keeping Signal Exchange simple.*
