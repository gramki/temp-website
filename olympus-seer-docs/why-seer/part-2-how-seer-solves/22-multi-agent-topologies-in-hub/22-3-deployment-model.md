# 22.3 Deployment Model

Hub Composite Applications are resolved at deployment time by the Composite Deployment Operator, which flattens nested composites to a union of all apps, creates child deployments, and populates routing tables. Signal Exchange doesn't know about composites—it just sees flattened app lists with OPA filters, ensuring that composite applications work seamlessly with existing Hub infrastructure.

This subsection describes how composite applications are deployed, how deployment-time resolution works, how routing tables are populated, and how update conflicts are resolved. It explains how this deployment model enables sophisticated multi-agent collaboration while maintaining compatibility with existing Hub infrastructure.

## Purpose of this Subsection

This subsection describes the deployment model for Hub Composite Applications. It explains deployment-time resolution, routing table population, and update conflict resolution. It also explains how this model enables sophisticated multi-agent collaboration while maintaining compatibility with existing Hub infrastructure.

## Core Concepts & Definitions

### Deployment-Time Resolution

**Deployment-time resolution** is the process by which the Composite Deployment Operator resolves composite applications at deployment time:
1. **Recursive Resolution**: Flattens nested composites to union of all apps
2. **Child Deployment Creation**: Creates `HubApplicationDeployment` for each app
3. **Routing Table Population**: Populates routing table with flattened app list + OPA filters

Deployment-time resolution ensures that Signal Exchange doesn't need to understand composites—it just sees flattened app lists with OPA filters, maintaining compatibility with existing infrastructure.

### Routing Table Population

**Routing table population** is the process by which the Composite Deployment Operator populates Signal Exchange routing tables with flattened app lists and OPA filters. The routing table contains:
*   **Scenario ID**: The composite scenario identifier
*   **App List**: Flattened list of all apps in the composite
*   **OPA Filters**: OPA filter for each app

Signal Exchange uses this routing table to route updates to appropriate apps based on OPA filter evaluation.

### Routing Table Schema

The routing table schema supports both single-app and multi-app scenarios with backward compatibility:

**Single-App Schema** (existing, backward compatible):
```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  application:
    deployment_id: "dispute-handler-sandbox"
    endpoint: "http://..."
```

**Multi-App Schema** (new, for composites):
```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  applications:
    - deployment_id: "risk-agent-deployment-sandbox"
      endpoint: "http://..."
      opa_filter: "<compiled Rego policy>"
    - deployment_id: "compliance-agent-deployment-sandbox"
      endpoint: "http://..."
      opa_filter: "<compiled Rego policy>"
```

**Routing Logic**:
1. If `applications` field exists: route to all apps (after OPA filter evaluation)
2. If only `application` field exists: existing behavior (direct dispatch)

This schema ensures backward compatibility while enabling multi-app routing for composite applications.

### OPA Filter Compilation and Caching

OPA filters are compiled and cached for performance:

*   **Compilation**: Filters are compiled from Rego policies at deployment time by the Composite Deployment Operator
*   **Storage**: Compiled filters are stored in the routing table as compiled Rego policies
*   **Caching**: Compiled filters are cached for performance during routing
*   **Evaluation**: Application Router evaluates compiled filters for each update

OPA filter compilation and caching ensure that update routing is performant even with complex filter policies.

### Backward Compatibility Guarantee

The routing table schema maintains backward compatibility:

*   **Single-app scenarios unchanged**: Existing single-app scenarios continue to work without modification
*   **Schema validation**: System ensures exactly one of `application` or `applications` is set
*   **Signal Exchange unchanged**: Signal Exchange routing logic is backward compatible

Backward compatibility ensures that existing deployments continue to work while new composite applications can be deployed alongside them.

### Update Conflict Resolution

**Update conflict resolution** handles concurrent updates from multiple apps to the same request:
*   **Latest wins**: Timestamp-based resolution (later update wins)
*   **Illegal updates rejected**: OPA policy determines legality of updates
*   **Rejected updates recorded**: Request history includes rejection reason and source app

Update conflict resolution ensures that composite applications maintain request state consistency while allowing parallel updates.

### Nested Composite Resolution

**Nested composite resolution** handles composites that contain other composites:
*   **Recursive flattening**: Nested composites are recursively flattened to union of all apps
*   **Filter inheritance**: OPA filters from nested composites are preserved
*   **Deployment hierarchy**: Child deployments maintain hierarchy for management

Nested composite resolution enables composite reuse and composition while maintaining deployment simplicity.

## Conceptual Models / Frameworks

### The Deployment Resolution Model

Deployment-time resolution flattens composites:

```
Composite Application Specification
    ├── Risk Agent
    ├── Compliance Agent
    └── Customer Service Composite (nested)
        ├── Customer Service Agent
        └── Document Analyzer
            ↓
Deployment-Time Resolution
    ↓
Flattened App List
    ├── Risk Agent (OPA filter F1)
    ├── Compliance Agent (OPA filter F2)
    ├── Customer Service Agent (OPA filter F3)
    └── Document Analyzer (OPA filter F4)
            ↓
Routing Table Population
    └── Signal Exchange sees: Scenario X → [A, B, C, D] with [F1, F2, F3, F4]
```

This model ensures that Signal Exchange works with flattened app lists, not composite structures.

### The Update Routing Model

Update routing uses OPA filters:

```
Request Update Arrives
    ↓
Application Router (Signal Exchange)
    ├── Looks up scenario in routing table
    ├── Finds app list [A, B, C, D] with filters [F1, F2, F3, F4]
    ├── Evaluates OPA filter F1 for app A
    ├── Evaluates OPA filter F2 for app B
    ├── Evaluates OPA filter F3 for app C
    └── Evaluates OPA filter F4 for app D
            ↓
    Routes update to apps where filter allows
```

This model enables pattern-specific routing while maintaining flexibility.

## Systemic and Enterprise Considerations

### Deployment Consistency

Composite deployments must be consistent:
*   **All-or-nothing deployment**: All apps in composite deploy together or not at all
*   **Version consistency**: All apps must be compatible versions
*   **State consistency**: Deployment must maintain request state consistency
*   **Rollback support**: Rollback must roll back entire composite

Deployment consistency ensures that composite applications deploy reliably and can be rolled back safely.

### Routing Performance

Update routing must be performant:
*   **Fast filter evaluation**: OPA filter evaluation must be fast (milliseconds)
*   **Efficient routing**: Routing must be efficient for many apps
*   **Scalability**: Routing must scale to many composites and apps
*   **Caching**: Filter evaluation results should be cached when appropriate

Routing performance directly impacts agent responsiveness and system scalability.

### Conflict Resolution Performance

Update conflict resolution must be performant:
*   **Fast conflict detection**: Conflict detection must be fast
*   **Efficient resolution**: Conflict resolution must be efficient
*   **Minimal overhead**: Conflict resolution should add minimal overhead
*   **Scalability**: Conflict resolution must scale to many concurrent updates

Conflict resolution performance directly impacts agent responsiveness and system scalability.

## Common Misconceptions & Failure Modes

### Misconception: Signal Exchange Understands Composites

Some organizations assume that Signal Exchange understands composite structures. However, Signal Exchange sees only flattened app lists with OPA filters, not composite structures.

**Failure mode**: Organizations expect Signal Exchange to understand composite structures, leading to confusion about routing behavior.

### Misconception: Deployment Is Complex

Some organizations assume that composite deployment is complex. However, deployment-time resolution simplifies deployment by flattening composites to standard app deployments.

**Failure mode**: Organizations avoid composites due to perceived complexity, missing opportunities for sophisticated coordination.

### Misconception: Conflicts Are Rare

Some organizations assume that update conflicts are rare. However, multiple apps updating the same request concurrently can create conflicts that must be resolved.

**Failure mode**: Organizations don't plan for conflict resolution, resulting in inconsistent request state or rejected updates.

## Practical Implications

### Deployment Strategy

Organizations should develop a deployment strategy that:
*   **Plans composite structure**: Plan composite structure and nesting
*   **Designs OPA filters**: Design OPA filters for update routing
*   **Tests deployment**: Test composite deployment in non-production environments
*   **Monitors deployment**: Monitor composite deployment for issues

Deployment strategy directly impacts deployment reliability and system stability.

### Conflict Resolution Strategy

Organizations should develop a conflict resolution strategy that:
*   **Defines conflict policies**: Define OPA policies for conflict resolution
*   **Plans conflict handling**: Plan how to handle rejected updates
*   **Monitors conflicts**: Monitor conflicts to identify patterns
*   **Optimizes routing**: Optimize update routing to minimize conflicts

Conflict resolution strategy directly impacts request state consistency and agent coordination effectiveness.

## Cross-References

*   **Section 22.1 (Hub Composite Applications)**: Describes the composite application architecture
*   **Section 22.2 (Supported Topologies)**: Describes the topology patterns that composites support

---

**References:**

*   `olympus-hub-docs/02-system-design/implementation-concepts/hub-composite-application.md` — Hub Composite Application design
