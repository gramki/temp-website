# 19.2 Agent Health Monitor

Agent Health Monitor implements the SLO tracking requirements established in Section 5.12.3. It tracks Service Level Objectives (SLOs) across three dimensions—Cost SLOs for Agent Reliability Engineers (ARE), Behavior SLOs for Cognitive Operations Stewards (COS), and Feedback SLOs for Process Architects (PA) and Agent Product Owners (APO)—without enforcing thresholds.

Agent Health Monitor provides persona-specific SLO tracking that enables different personas to monitor the aspects of agent health that matter to their roles while maintaining a unified operational health model. SLO tracking identifies deviations from targets, but enforcement (if required) is handled by sentinels or external systems.

## Purpose of this Subsection

This subsection describes how Seer implements SLO tracking through Agent Health Monitor. It explains how SLOs are defined, how they are evaluated using Agent Analytics data marts, and how deviations are tracked and reported. It also describes the Human Feedback Service that collects and routes feedback for Feedback SLO calculation.

## Core Concepts & Definitions

### SLO Tracking Without Enforcement

Agent Health Monitor tracks SLOs but does not enforce them. This separation enables organizations to:
*   Track SLOs without automatically triggering enforcement actions
*   Configure sentinels to trigger on SLO deviations (if desired)
*   Handle SLO deviations through appropriate mechanisms (sentinels, human intervention, external systems)

SLO Manager and SLO Tracking Service only manage and track—no enforcement. Enforcement is handled by sentinels (if configured) or external systems.

### Cost SLOs (ARE)

**Cost SLOs** track cost-related metrics for Agent Reliability Engineers (ARE), enabling AREs to monitor agent cost efficiency, budget utilization, and cost anomalies. Cost SLOs track metrics such as:
*   Cost-to-health ratio: The relationship between cost and agent health/effectiveness
*   Budget utilization: Percentage of allocated budget consumed over time periods
*   Cost anomalies: Unusual cost patterns that deviate from historical baselines
*   Cost per successful task: Average cost per task that completes successfully
*   Cost velocity: Rate of cost accumulation over time

Cost SLOs use Agent Analytics data marts for evaluation, comparing current metrics to SLO targets and historical baselines.

### Behavior SLOs (COS)

**Behavior SLOs** track behavioral metrics for Cognitive Operations Stewards (COS), enabling COSs to monitor agent behavioral patterns, detect drift, and assess quality metrics. Behavior SLOs track metrics such as:
*   Behavioral patterns: Consistency in decision-making, reasoning patterns, tool usage patterns
*   Drift detection: Gradual changes in behavior over time compared to established baselines
*   Quality metrics: Success rates, error rates, user satisfaction indicators
*   Policy compliance: Adherence to policies, guardrail violations, authority ceiling compliance

Behavior SLOs enable COSs to detect behavioral problems that may not manifest as immediate failures but gradually degrade agent performance or violate policies.

### Feedback SLOs (PA/APO)

**Feedback SLOs** track feedback-related metrics for Process Architects (PA) and Agent Product Owners (APO), enabling PAs and APOs to monitor feedback collection, resolution, and promotion effectiveness. Feedback SLOs track metrics such as:
*   Feedback collection rates: Percentage of agent interactions that generate feedback
*   Feedback resolution rates: Percentage of feedback items that are resolved
*   Feedback promotion rates: Percentage of feedback that is promoted to training improvements
*   Feedback quality: Relevance and usefulness of collected feedback

Feedback SLOs use the Human Feedback Service to collect feedback and calculate metrics.

### Human Feedback Service

**Human Feedback Service** collects feedback from various sources, routes feedback to appropriate destinations (Training Feedback Services, agent behavior systems, etc.), and calculates feedback metrics for SLO evaluation. The Human Feedback Service:
*   Collects explicit feedback (user ratings, corrections)
*   Collects implicit feedback (user actions, outcomes)
*   Routes feedback to Training Spec improvements, agent behavior systems, or other destinations
*   Calculates feedback metrics (user satisfaction, override rate, feedback rating, escalation rate)

The Human Feedback Service enables Feedback SLO tracking and supports the feedback and learning requirements established in Section 5.10.

## Conceptual Models / Frameworks

### The SLO Tracking Model

SLO tracking operates on a three-phase model:

1. **SLO Definition**: SLOs are defined with targets, thresholds, and evaluation criteria in Health Specs
2. **SLO Evaluation**: SLOs are evaluated periodically (or continuously) against Agent Analytics data marts
3. **SLO Reporting**: SLO deviations are reported to appropriate personas and may trigger sentinel actions

SLO tracking uses Agent Analytics data marts for historical data, enabling trend analysis and baseline comparison.

### The Persona-Specific SLO Model

Different personas require different SLO views:

| Persona | SLO Type | Primary Metrics | Use Case |
|---------|----------|-----------------|----------|
| **ARE** | Cost SLOs | Cost-to-health ratio, budget utilization, cost anomalies | Monitor cost efficiency and budget compliance |
| **COS** | Behavior SLOs | Behavioral patterns, drift detection, quality metrics | Monitor behavioral consistency and quality |
| **PA/APO** | Feedback SLOs | Feedback collection, resolution, promotion rates | Monitor learning effectiveness and feedback mechanisms |

While personas focus on their specific SLO types, all SLOs contribute to a unified operational health assessment.

## Systemic and Enterprise Considerations

### Data Requirements

SLO tracking requires:
*   **Historical data**: Agent Analytics data marts must maintain sufficient historical data for baseline comparison and trend analysis
*   **Real-time data**: Some SLOs (particularly cost SLOs) may require near-real-time data for timely detection
*   **Aggregated data**: SLO evaluation requires efficient aggregation of operational data across agents, workbenches, and time periods

Agent Analytics data marts must be designed to support efficient SLO evaluation queries while maintaining data freshness appropriate for each SLO type.

### Performance Considerations

SLO evaluation must be efficient:
*   **Incremental evaluation**: SLOs should be evaluated incrementally rather than recalculating from scratch each time
*   **Caching**: SLO evaluation results should be cached to avoid redundant calculations
*   **Parallel evaluation**: Multiple SLOs should be evaluated in parallel to minimize latency

SLO tracking should not impact agent performance or request processing latency.

### Integration with Sentinels

SLO tracking integrates with sentinels:
*   **SLO deviations can trigger sentinels**: If configured, SLO deviations can trigger Realtime or Analytical Sentinels to generate Observations or Exceptions
*   **Sentinels can evaluate SLOs**: Sentinels can use SLO evaluation results in their policy logic
*   **SLO tracking is independent**: SLO tracking operates independently of sentinels, enabling organizations to track SLOs without requiring sentinel deployment

This integration enables organizations to use SLOs as triggers for automated oversight while maintaining flexibility in how SLO deviations are handled.

## Common Misconceptions & Failure Modes

### Misconception: SLOs Are Enforcement Mechanisms

Some organizations assume that SLOs automatically enforce thresholds, similar to cost ceilings or budget limits. However, SLOs are tracking mechanisms that identify deviations; enforcement (if required) is handled by sentinels or external systems.

**Failure mode**: Organizations expect SLOs to automatically halt agent execution when thresholds are breached, leading to confusion when agents continue operating despite SLO breaches.

### Misconception: One SLO Type Is Sufficient

Some organizations assume that one SLO type (typically cost SLOs) is sufficient. However, different personas require different SLO types to monitor the aspects of agent health that matter to their roles.

**Failure mode**: Organizations deploy only cost SLOs, missing behavioral problems and feedback issues that require different monitoring approaches.

### Misconception: SLOs Replace Sentinels

Some organizations assume that SLO tracking can replace sentinel oversight. While SLOs provide structured health monitoring, sentinels provide policy evaluation, anomaly detection, and active intervention capabilities that SLOs do not provide.

**Failure mode**: Organizations deploy SLO tracking without sentinels, missing problems that require policy evaluation or active intervention rather than just metric tracking.

## Practical Implications

### SLO Definition Process

Organizations should define SLOs through a structured process:
1. Identify metrics that matter for each persona and use case
2. Establish baselines by collecting historical data
3. Set targets based on baselines and business requirements
4. Define thresholds (warning, breach, critical) for each SLO
5. Configure evaluation frequency and data sources
6. Integrate with sentinels (if desired) for automated oversight

SLOs should be defined iteratively, starting with critical metrics and expanding based on operational experience.

### SLO Monitoring and Response

Organizations must establish processes for monitoring and responding to SLO deviations:
*   **Monitoring dashboards**: Provide persona-specific dashboards that display SLO status and deviations
*   **Alerting mechanisms**: Configure alerts for SLO breaches that require immediate attention
*   **Response procedures**: Define procedures for responding to SLO deviations, including escalation paths
*   **Review processes**: Establish periodic review processes to assess SLO effectiveness and adjust targets

SLO monitoring should be integrated into operational workflows, not treated as a separate activity.

## Cross-References

*   **Section 5.12.3 (SLO Tracking Requirements)**: Establishes the SLO tracking requirements that Agent Health Monitor implements
*   **Section 19.1 (Seer Sentinels)**: Describes how sentinels can be triggered by SLO deviations
*   **Section 19.3 (Agent Analytics)**: Describes the Agent Analytics data mart that SLO tracking uses
*   **Section 14 (Cost Governance)**: Describes cost governance mechanisms that Cost SLOs track

---

**References:**

*   `seer-design/subsystems/agent-health-monitor/README.md` — Agent Health Monitor design
*   `seer-design/subsystems/agent-health-monitor/SCOPE.md` — Agent Health Monitor scope
*   `seer-design/subsystems/agent-health-monitor/slo-manager.md` — SLO Manager design
*   `seer-design/subsystems/agent-health-monitor/slo-tracking-service.md` — SLO Tracking Service design
*   `seer-design/subsystems/agent-health-monitor/human-feedback-service.md` — Human Feedback Service design
