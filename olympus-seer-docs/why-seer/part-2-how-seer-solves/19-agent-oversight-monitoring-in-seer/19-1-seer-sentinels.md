# 19.1 Seer Sentinels

Seer Sentinels implement the three types of oversight established in Section 5.12: Realtime Sentinels for event-based immediate detection, Analytical Sentinels for historical pattern analysis, and Request Sentinels for active agent participation in other agents' requests. All three sentinel types use Open Policy Agent (OPA) for policy evaluation and integrate with Hub's Cronus Gateway to generate Observations and Exceptions.

Seer Sentinels provide automated oversight that scales to hundreds of agents and thousands of requests, enabling organizations to detect anomalies, prevent policy violations, and maintain operational control without requiring human monitoring of every agent decision.

## Purpose of this Subsection

This subsection describes how Seer implements the three sentinel types established in Section 5.12.2. It explains how Realtime Sentinels observe Signal Exchange events, how Analytical Sentinels query Agent Analytics data marts, and how Request Sentinels operate as Employed Agents. It also describes OPA policy evaluation, Cronus integration, and auto-enrollment mechanisms.

## Core Concepts & Definitions

### Realtime Sentinels

**Realtime Sentinels** observe Signal Exchange (SX) events as they occur and evaluate OPA policies to generate real-time Observations and Exceptions via Cronus Gateway. Realtime Sentinels operate on event streams, providing immediate detection and alerting for conditions that require sentinel attention.

Realtime Sentinels observe events such as:
*   Agent session state changes (agent becomes stuck, session times out)
*   Agent request state changes (request fails, request exceeds timeout)
*   Guardrail violations (agent attempts to violate guardrail constraints)
*   Policy violations (agent attempts to violate policy rules)
*   Cost anomalies (cost accumulation exceeds thresholds)

Realtime Sentinels evaluate OPA policies on these events, generating Observations (warnings) or Exceptions (critical issues) that are routed to appropriate personas via Cronus Gateway using Hub's existing Observation/Exception model.

### Analytical Sentinels

**Analytical Sentinels** run templated SQL queries on Agent Analytics data marts periodically (hourly, daily) to identify trends, drift, and long-term issues. Analytical Sentinels operate on aggregated historical data, providing pattern-based detection that complements real-time detection.

Analytical Sentinels analyze:
*   Cost trends: Gradual increases in cost per task, budget utilization trends, cost efficiency degradation
*   Behavioral patterns: Changes in agent decision patterns, quality metrics over time, user satisfaction trends
*   Drift detection: Comparison of current behavior to historical baselines, identification of gradual behavioral changes
*   Cross-agent patterns: Identification of patterns that span multiple agents or workbenches

Analytical Sentinels execute templated SQL queries against Agent Analytics data marts, generating Observations or Exceptions based on query results. Unlike Realtime Sentinels, which operate on event streams, Analytical Sentinels operate on aggregated data, enabling detection of patterns that may not be apparent in individual events.

### Request Sentinels

**Request Sentinels** operate as Employed Agents in Workbenches, automatically enrolling in requests that match their enrollment filters (specified via OPA policies). Request Sentinels observe and participate in requests in real-time, creating child requests for intervention or coordination.

Request Sentinels enable:
*   Active monitoring: Sentinel agents observe request processing in real-time, not just after the fact
*   Intervention capability: Sentinel agents can create child requests, escalate issues, or take corrective actions
*   Context-aware oversight: Sentinel agents have access to the full request context, enabling sophisticated policy evaluation
*   Multi-agent coordination: Sentinel agents can coordinate with other agents to resolve issues

Request Sentinels differ from Realtime and Analytical Sentinels in that they operate as agents themselves, participating in the request lifecycle rather than just observing it. This enables active intervention and coordination that passive observation cannot provide.

### OPA Policy Evaluation

All three sentinel types use Open Policy Agent (OPA) for policy evaluation, but with different input contexts:

*   **Realtime Sentinels**: Evaluate policies on SX event data (event type, agent context, session state, timestamps)
*   **Analytical Sentinels**: Evaluate policies on aggregated analytics data (cost trends, behavioral metrics, historical comparisons)
*   **Request Sentinels**: Evaluate policies on request context (request state, agent actions, tool invocations, decision points)

This unified policy evaluation model enables consistent policy expression across all three sentinel types while allowing each type to operate on the data most relevant to its purpose.

### Cronus Integration

All sentinel types generate Observations and Exceptions via Hub's Cronus Gateway, using Hub's existing Observation/Exception model. This integration ensures that:
*   No new model is required: Sentinels leverage existing Hub infrastructure
*   Observations route to Ops Center: Observations appear in Hub's Ops Center for human review
*   Workbench routing works: Observations route to appropriate workbenches via Cronus
*   Audit trail is maintained: All Observations and Exceptions are auditable

Cronus integration provides a unified mechanism for sentinel outputs while maintaining consistency with Hub's existing models.

### Auto-Enrollment

Request Sentinels automatically enroll in requests that match their enrollment filters (specified via OPA policies). When a request is created, Signal Exchange evaluates enrollment filters for all Request Sentinels in the workbench, and matching sentinels are automatically enrolled in the request.

Auto-enrollment enables:
*   Automatic participation: Sentinels participate in requests without manual configuration
*   Pattern-based targeting: Sentinels target requests based on patterns (scenario, workbench, agent, etc.)
*   Dynamic enrollment: Sentinels can be added or removed without affecting existing requests
*   Scalability: Auto-enrollment scales to many requests and sentinels

Auto-enrollment ensures that Request Sentinels participate in the right requests without requiring manual configuration for each request.

## Conceptual Models / Frameworks

### The Three-Layer Sentinel Architecture

Sentinels form a three-layer architecture:

```
┌─────────────────────────────────────────────────────────┐
│         Request Sentinels (Active Layer)                │
│  Agent participation, intervention, coordination        │
└─────────────────────────────────────────────────────────┘
                        ↑
┌─────────────────────────────────────────────────────────┐
│      Analytical Sentinels (Pattern Layer)               │
│  Historical analysis, trend detection, drift analysis   │
└─────────────────────────────────────────────────────────┘
                        ↑
┌─────────────────────────────────────────────────────────┐
│        Realtime Sentinels (Event Layer)                  │
│  Event-based policy evaluation, immediate detection     │
└─────────────────────────────────────────────────────────┘
```

Each layer serves different purposes, providing comprehensive oversight coverage.

### The Sentinel Deployment Model

Sentinels are deployed via Deployment CRDs that reference Spec CRDs:

*   **Spec CRDs**: Define sentinel specifications (policy, filters, evaluation criteria) in a templatized, versioned format
*   **Deployment CRDs**: Define deployment configuration (which workbenches, which agents, enable/disable state)

This separation enables sentinel specifications to be defined once and deployed multiple times with different configurations, supporting reuse and consistency across deployments.

## Systemic and Enterprise Considerations

### Performance and Scalability

Sentinels must be performant and scalable:

*   **Realtime Sentinels**: Must handle high event volumes (thousands of events per second) with low latency (milliseconds to seconds)
*   **Analytical Sentinels**: Must efficiently query large data marts (millions of records) with acceptable query latency (seconds to minutes)
*   **Request Sentinels**: Must operate within request processing time constraints, adding minimal overhead to request processing

Sentinels must scale without impacting agent performance or request processing latency.

### Integration with Hub Models

All sentinel types integrate with Hub's existing models:

*   **Realtime and Analytical Sentinels**: Generate Observations and Exceptions via Cronus Gateway, using Hub's existing Observation/Exception model
*   **Request Sentinels**: Operate as Employed Agents, using Hub's Request model and creating child requests for intervention

This integration ensures that sentinels leverage existing Hub infrastructure rather than creating parallel systems.

### Policy Management

Sentinels require policy management:

*   **Policy versioning**: Policies must be versioned and tracked
*   **Policy validation**: Policies must be validated before deployment
*   **Policy testing**: Policies should be tested before production deployment
*   **Policy governance**: Policies must comply with governance requirements

Policy management ensures that sentinels operate correctly and comply with enterprise policies.

## Common Misconceptions & Failure Modes

### Misconception: One Sentinel Type Is Sufficient

Some organizations assume that one sentinel type (typically Realtime Sentinels) is sufficient. However, each sentinel type detects different classes of problems: Realtime Sentinels miss gradual trends, Analytical Sentinels miss immediate crises, and both are passive observers that cannot actively intervene.

**Failure mode**: Organizations deploy only one sentinel type, missing problems that require a different detection mechanism.

### Misconception: Request Sentinels Replace Realtime Sentinels

Some organizations assume that Request Sentinels, being more sophisticated, can replace Realtime Sentinels. However, Request Sentinels operate only on requests that match their enrollment filters, while Realtime Sentinels observe all events. Request Sentinels also add overhead to request processing.

**Failure mode**: Organizations deploy only Request Sentinels, missing events that don't match enrollment filters or adding excessive overhead to request processing.

### Misconception: Sentinels Enforce Policies

Some organizations assume that sentinels automatically enforce policies. However, sentinels generate Observations and Exceptions; enforcement (if required) is handled by other mechanisms (e.g., guardrails, cost ceilings, human intervention).

**Failure mode**: Organizations expect sentinels to automatically halt agent execution when policies are violated, leading to confusion when agents continue operating despite sentinel Observations.

## Practical Implications

### Sentinel Deployment Strategy

Organizations should deploy sentinels based on the problems they need to detect:

*   **Deploy Realtime Sentinels for**: Immediate anomaly detection, policy violation detection, cost anomaly detection, stuck agent detection
*   **Deploy Analytical Sentinels for**: Cost trend analysis, behavioral drift detection, quality degradation detection, cross-agent pattern detection
*   **Deploy Request Sentinels for**: Active intervention, complex policy evaluation requiring request context, coordination with other agents

Most organizations will deploy all three types, with different sentinels addressing different aspects of oversight.

### Policy Design Considerations

Policy design must consider the operational model of each sentinel type:

*   **Realtime Sentinel policies**: Must be fast to evaluate (milliseconds), operate on event data, and avoid complex aggregations
*   **Analytical Sentinel policies**: Can use complex SQL queries and aggregations, operate on historical data, and tolerate longer evaluation times
*   **Request Sentinel policies**: Must operate within request processing time constraints, have access to full request context, and enable agent actions

Policies should be designed to leverage the strengths of each sentinel type while avoiding their limitations.

### Integration with Other Systems

Sentinels integrate with other Seer and Hub systems:

*   **Agent Health Monitor**: Sentinels can be triggered by SLO deviations (if configured)
*   **Agent Analytics**: Analytical Sentinels use Agent Analytics data marts
*   **Signal Exchange**: Realtime Sentinels observe SX events; Request Sentinels auto-enroll via SX
*   **Cronus Gateway**: All sentinels generate Observations/Exceptions via Cronus

Integration ensures that sentinels work seamlessly with other Seer and Hub capabilities.

## Cross-References

*   **Section 5.12.2 (Three Types of Oversight)**: Establishes the three sentinel types that Seer Sentinels implement
*   **Section 19.2 (Agent Health Monitor)**: Describes how SLO tracking can trigger sentinels
*   **Section 19.3 (Agent Analytics)**: Describes the data mart that Analytical Sentinels use
*   **Section 19.5 (COGW)**: Describes how COG Sentinels extend Request Sentinels for subscription-wide governance

---

**References:**

*   `seer-design/subsystems/seer-sentinels/README.md` — Seer Sentinels design
*   `seer-design/subsystems/seer-sentinels/SCOPE.md` — Seer Sentinels scope
*   `seer-design/implementation-concepts/sentinels.md` — Sentinel implementation concept
