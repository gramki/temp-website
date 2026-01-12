

## Clarifying Questions

### 1. Agent Analytics

**Content Migration:**
- The README mentions `agent-observability.md` has parts to migrate. Which parts should move to Agent Analytics?
  - Platform-level dashboards → already in `observability-extensions-to-watch.md`?
  - Cognitive observability enhancements (AHS, reasoning metrics) → new component?
  - Or is Agent Analytics only the cognitive enhancements, with platform dashboards staying separate?

> Agent analytics houses a data mart of the agent operational data. It is not observability into agent runtime status.
> This answer questions based on historic health, cost, effectiveness, feedback, behavior of the agents.
> This is analogous hub-analytics subsystem and is similarly designed. refer to that for context. 

**Component Structure:**
- Should Agent Analytics have sub-components like:
  - Cognitive Observability Service (AHS, reasoning metrics, decision confidence)
  - Platform Dashboards Service (or keep `observability-extensions-to-watch.md` as-is)?
  - Or is it a single service with multiple capabilities?

> All runtime observability concerns addressing AREs, Cogntive Operations Stewards come from observability-extensions-to-watch.
> Make watch-extensions can be an indepdendent subsystem like cipher-iam-extensions subsytem in seer. 

### 2. Agent Session Supervisor

**Supervisory Policies:**
- What are supervisory policies? How do they differ from:
  - Guardrails (safety constraints)
  - Authority policies (OPA policies)
  - Employment Spec policies
- Are they runtime monitoring rules (e.g., "if agent stuck > 5 min, escalate")?
> Yes
> The Supervisory policies observe Agent Session and run rules on them. Based on the result they generate Cronus Observations or Exceptions in the respective Workbenches.
> Two type of Supervisors and each of them have a service running them.
> Realtime Supervisor Service -> Observer for SX events. Invokes interested Supervisor policies written in OPA. Based on the result generates Observartions or Exceptions. 
> Analytical Supervisor Service -> Runs on the agent-analytics data mart periodically. The Spec is written as a templated SQL, with results emiting a table of exceptions or observations (with columns mapping to the exception/observation JSON objects).
> Supervisors are employed with Deployment CRDs. The Deployment CRD corresponds to Spec CRD where a templatized definition of the Supervisor is defined. 

**Observations:**
- What triggers a supervisory observation?
  - Agent stuck (no progress)
  - Agent failed (error state)
  - Guardrail violations
  - Cost anomalies
  - All of the above?

> All of the above
> Health deviations


**Escalation Model:**
- How does escalation work?
  - Escalate to human supervisor?
  - Escalate to Agent Health Monitor?
  - Create intervention tasks?
  - All of the above?

> Hub has a model for Observations and Exceptions. refer to that. Nothing specific or new required for these Observations and Exceptions.

**Component Structure:**
- Should this have sub-components like:
  - Supervisory Policy Manager
  - Observation Service
  - Escalation Service
  - Or is it a single service?

> Should have oeprators
> Should have above named services.
> Should have levers to control supervisors in runtime
> Should have lifetime management and spec validation service (just like we have for trained/employed agents)

### 3. Agent Health Monitor

**SLO Types:**
- Cost SLOs: budget thresholds, cost per request limits?
- Behavior SLOs: AHS thresholds, error rates, latency?
- Feedback SLOs: user satisfaction, override rates?
- Are these defined per agent, per workbench, or both?

> Check ARE role and expectations - Cost SLOs address ARE needs
> Check COS role and expectations - Behavior SLOs address COS Needs
> Feedback SLOs address the needs of a Process Architect (Cogntive Solution Architect) and that of APO.
> Metrics are at per Agent and can be rolled upto Workbench as well.

**SLO Enforcement:**
- How are SLOs enforced?
  - Alerting only?
  - Automatic actions (throttle, suspend)?
  - Integration with Agent Session Supervisor for escalation?

**Human Feedback Service:**
- What does this service do?
  - Collect feedback from users?
  - Route feedback to Training Feedback Services?
  - Calculate feedback-based metrics?
  - All of the above?

> all of the above

**Component Structure:**
- Should this have sub-components like:
  - SLO Manager (definition, tracking)
  - SLO Enforcement Service
  - Human Feedback Service
  - Or is it a single service?

> There are no enforcements services requried. 
> Managing SLO definitions (thresholds) and tracking deviations is the scope
> You can follow structure similar to Supervisors for SLOs/Health subsystem

### 4. Relationships Between Subsystems

**Agent Analytics ↔ Agent Health Monitor:**
- Does Agent Health Monitor use Agent Analytics metrics for SLO evaluation?
- Or are they independent?

> Yes

**Agent Session Supervisor ↔ Agent Health Monitor:**
- Does Session Supervisor trigger on SLO violations?
- Or do they operate independently?

> If a supervisor is defined for SLO deviations, yes

**Agent Analytics ↔ Agent Session Supervisor:**
- Does Session Supervisor use Agent Analytics observations?
- Or does it have its own observation mechanisms?

> Yes

### 5. General

**Design Pattern:**
- Should these follow the same sub-component pattern as Trained Agent Lifecycle Manager (Manager → Directory → Operators → Levers)?
- Or are they single services with multiple capabilities?

> Yes

**Content to Migrate:**
- Are there existing documents (like `agent-observability.md`) that should have content migrated to these subsystems?
> Explained earlier

Once you answer these, I'll create a plan following the same pattern as the previous designs.