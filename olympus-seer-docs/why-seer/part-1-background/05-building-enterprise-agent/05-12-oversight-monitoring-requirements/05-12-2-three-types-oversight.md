# 5.12.2 Three Types of Oversight

Enterprise AI agents require oversight mechanisms that operate at different time scales and with different operational models. A single type of oversight is insufficient because different problems manifest differently: some require immediate detection, others require pattern analysis over time, and still others require active agent participation to observe and intervene.

This subsection defines three distinct types of oversight mechanisms—Realtime Sentinels, Analytical Sentinels, and Request Sentinels—and explains when each is appropriate. These three types complement each other, providing comprehensive coverage of the oversight requirements established in Section 5.12.1.

## Purpose of this Subsection

This subsection establishes the three-layer oversight model for enterprise AI agents. It defines each sentinel type, explains their operational models, and describes the problems each type is designed to detect. It also explains how the three types work together to provide comprehensive oversight coverage.

## Core Concepts & Definitions

### Realtime Sentinels

**Realtime Sentinels** are event-based policy evaluation mechanisms that observe Signal Exchange events as they occur and evaluate Open Policy Agent (OPA) policies to generate real-time Observations and Exceptions. Realtime Sentinels operate on event streams, providing immediate detection and alerting for conditions that require sentinel attention.

Realtime Sentinels observe events such as:
*   Agent session state changes (e.g., agent becomes stuck, session times out)
*   Agent request state changes (e.g., request fails, request exceeds timeout)
*   Guardrail violations (e.g., agent attempts to violate guardrail constraints)
*   Policy violations (e.g., agent attempts to violate policy rules)
*   Cost anomalies (e.g., cost accumulation exceeds thresholds)

Realtime Sentinels evaluate OPA policies on these events, generating Observations (warnings) or Exceptions (critical issues) that are routed to appropriate personas via Cronus Gateway (Hub's business exception model).

### Analytical Sentinels

**Analytical Sentinels** are historical pattern analysis mechanisms that run templated SQL queries on analytics data marts periodically (e.g., hourly, daily) to identify trends, drift, and long-term issues. Analytical Sentinels operate on aggregated historical data, providing pattern-based detection that complements real-time detection.

Analytical Sentinels analyze:
*   **Cost trends**: Gradual increases in cost per task, budget utilization trends, cost efficiency degradation
*   **Behavioral patterns**: Changes in agent decision patterns, quality metrics over time, user satisfaction trends
*   **Drift detection**: Comparison of current behavior to historical baselines, identification of gradual behavioral changes
*   **Cross-agent patterns**: Identification of patterns that span multiple agents or workbenches

Analytical Sentinels execute templated SQL queries against Agent Analytics data marts, generating Observations or Exceptions based on query results. Unlike Realtime Sentinels, which operate on event streams, Analytical Sentinels operate on aggregated data, enabling detection of patterns that may not be apparent in individual events.

### Request Sentinels

**Request Sentinels** are active agent participation mechanisms where sentinel agents enroll in other agents' requests to observe and participate in real-time. Request Sentinels operate as Employed Agents in Workbenches, automatically enrolling in requests that match their enrollment filters (specified via OPA policies).

Request Sentinels enable:
*   **Active monitoring**: Sentinel agents observe request processing in real-time, not just after the fact
*   **Intervention capability**: Sentinel agents can create child requests, escalate issues, or take corrective actions
*   **Context-aware oversight**: Sentinel agents have access to the full request context, enabling sophisticated policy evaluation
*   **Multi-agent coordination**: Sentinel agents can coordinate with other agents to resolve issues

Request Sentinels differ from Realtime and Analytical Sentinels in that they operate as agents themselves, participating in the request lifecycle rather than just observing it. This enables active intervention and coordination that passive observation cannot provide.

## Conceptual Models / Frameworks

### The Three-Layer Oversight Architecture

The three sentinel types form a layered architecture:

```
┌─────────────────────────────────────────────────────────┐
│              Request Sentinels (Active Layer)            │
│  Agent participation, intervention, coordination         │
└─────────────────────────────────────────────────────────┘
                        ↑
┌─────────────────────────────────────────────────────────┐
│          Analytical Sentinels (Pattern Layer)            │
│  Historical analysis, trend detection, drift analysis   │
└─────────────────────────────────────────────────────────┘
                        ↑
┌─────────────────────────────────────────────────────────┐
│          Realtime Sentinels (Event Layer)                │
│  Event-based policy evaluation, immediate detection      │
└─────────────────────────────────────────────────────────┘
```

Each layer serves different purposes:
*   **Event Layer (Realtime)**: Catches immediate problems as they occur
*   **Pattern Layer (Analytical)**: Identifies trends and gradual changes over time
*   **Active Layer (Request)**: Enables intervention and coordination for complex issues

### Operational Model Comparison

| Aspect | Realtime Sentinels | Analytical Sentinels | Request Sentinels |
|--------|-------------------|----------------------|-------------------|
| **Operation Model** | Observe SX events | Query analytics data mart | Enroll as agent in requests |
| **Time Scale** | Real-time (seconds) | Periodic (hours/days) | Real-time (during request) |
| **Data Source** | Signal Exchange events | Agent Analytics data mart | Request context |
| **Output** | Cronus Observations/Exceptions | Cronus Observations/Exceptions | Child requests, agent actions |
| **Integration** | Seer internal | Seer internal | Hub Request model |
| **Use Case** | Immediate anomaly detection | Trend and drift detection | Active intervention |

### Policy Evaluation Model

All three sentinel types use OPA (Open Policy Agent) for policy evaluation, but with different input contexts:

*   **Realtime Sentinels**: Evaluate policies on SX event data (event type, agent context, session state, timestamps)
*   **Analytical Sentinels**: Evaluate policies on aggregated analytics data (cost trends, behavioral metrics, historical comparisons)
*   **Request Sentinels**: Evaluate policies on request context (request state, agent actions, tool invocations, decision points)

This unified policy evaluation model enables consistent policy expression across all three sentinel types while allowing each type to operate on the data most relevant to its purpose.

## Systemic and Enterprise Considerations

### Performance and Scalability

Each sentinel type has different performance characteristics:

*   **Realtime Sentinels**: Must handle high event volumes (thousands of events per second) with low latency (milliseconds to seconds)
*   **Analytical Sentinels**: Must efficiently query large data marts (millions of records) with acceptable query latency (seconds to minutes)
*   **Request Sentinels**: Must operate within request processing time constraints, adding minimal overhead to request processing

Oversight mechanisms must be designed to scale without impacting agent performance or request processing latency.

### Integration with Hub Models

All three sentinel types integrate with Hub's existing models:

*   **Realtime and Analytical Sentinels**: Generate Observations and Exceptions via Cronus Gateway, using Hub's existing Observation/Exception model
*   **Request Sentinels**: Operate as Employed Agents, using Hub's Request model and creating child requests for intervention

This integration ensures that oversight mechanisms leverage existing Hub infrastructure rather than creating parallel systems.

### Deployment Model

Sentinels are deployed via Deployment CRDs (Custom Resource Definitions) that reference Spec CRDs (Specification CRDs):

*   **Spec CRDs**: Define the sentinel specification (policy, filters, evaluation criteria) in a templatized, versioned format
*   **Deployment CRDs**: Define the deployment configuration (which workbenches, which agents, enable/disable state)

This separation enables sentinel specifications to be defined once and deployed multiple times with different configurations, supporting reuse and consistency across deployments.

## Common Misconceptions & Failure Modes

### Misconception: One Sentinel Type Is Sufficient

Some organizations assume that one sentinel type (typically Realtime Sentinels) is sufficient for all oversight needs. In reality, each sentinel type detects different classes of problems:

*   Realtime Sentinels miss gradual trends that Analytical Sentinels detect
*   Analytical Sentinels miss immediate crises that Realtime Sentinels detect
*   Both Realtime and Analytical Sentinels are passive observers that cannot actively intervene, which Request Sentinels enable

**Failure mode**: Organizations deploy only one sentinel type, missing problems that require a different detection mechanism.

### Misconception: Request Sentinels Replace Realtime Sentinels

Some organizations assume that Request Sentinels, being more sophisticated, can replace Realtime Sentinels. However, Request Sentinels operate only on requests that match their enrollment filters, while Realtime Sentinels observe all events. Request Sentinels also add overhead to request processing, making them unsuitable for high-volume, low-latency detection.

**Failure mode**: Organizations deploy only Request Sentinels, missing events that don't match enrollment filters or adding excessive overhead to request processing.

### Misconception: Analytical Sentinels Are Just Reports

Some organizations treat Analytical Sentinels as reporting mechanisms rather than oversight mechanisms. While Analytical Sentinels do generate reports, they also generate Observations and Exceptions that trigger alerts and interventions, just like Realtime Sentinels.

**Failure mode**: Organizations deploy Analytical Sentinels for reporting only, missing opportunities for proactive intervention based on trend analysis.

## Practical Implications

### Sentinel Selection Criteria

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

### Cost and Resource Considerations

Each sentinel type has different resource requirements:

*   **Realtime Sentinels**: Require high-throughput event processing infrastructure
*   **Analytical Sentinels**: Require data mart infrastructure and query processing capacity
*   **Request Sentinels**: Require agent runtime capacity and add overhead to request processing

Organizations must provision appropriate infrastructure for each sentinel type they deploy.

## Cross-References

*   **Section 5.12.1 (Why Oversight Is Needed)**: Establishes the fundamental need for oversight that these three types address
*   **Section 19.1 (Seer Sentinels)**: Describes how Seer implements these three sentinel types
*   **Section 19.5 (Cognitive Operations Governance Workbench)**: Describes how COG Sentinels (a type of Request Sentinel) enable subscription-wide governance

---

**References:**

*   `seer-design/subsystems/seer-sentinels/README.md` — Seer Sentinels design
*   `seer-design/subsystems/seer-sentinels/SCOPE.md` — Seer Sentinels scope and key decisions
*   `seer-design/subsystems/seer-sentinels/realtime-sentinel-service.md` — Realtime Sentinel Service design
*   `seer-design/subsystems/seer-sentinels/analytical-sentinel-service.md` — Analytical Sentinel Service design
*   `seer-design/implementation-concepts/sentinels.md` — Sentinel implementation concept
