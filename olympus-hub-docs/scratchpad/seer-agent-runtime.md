ref: .cursor/plans/agent_runtime_detailed_design_80ece2d7.plan.md

1. Ingress Path Configuration (Remaining Open Item)
a) Heracles Integration
How does Seer Operator configure Heracles ingress paths for agents?

> Yes. As part of deployment it configure cluster-ingress path (not publicly accessible).

Are ingress paths created per agent, per workbench, or per scenario?
> Per Employed Agent.

What is the ingress path pattern structure (e.g., /agents/{agent_id}/dispatch, /workbench/{workbench_id}/agents/{agent_id}/dispatch)?
> /seer/subscription/{subscription_id}/data-plane/workbench/{workbench_id}/agents/{agent_id}/dispatch

b) Ingress Lifecycle
When are ingress paths created (during EmploymentSpec creation, before pod deployment, or after)?

> During deployment after IAM profile creation/updation.

How are ingress paths updated when agent configuration changes?
> Operator updates. As such for a given agent there is only one data plane endpoint.

Who manages ingress path cleanup (Seer Operator, Heracles, or both)?
> Seer Operator

c) Authentication/Authorization
How does zone-auth integrate with Heracles ingress for agent requests?
> Heracles sees the client as sx-observer. 
> zone-auth is used to verify sx-observer credentials.
Are authentication tokens validated at ingress, or passed through to agents?
> Agents would not receive tokens that can be validated at ingress.
> Agent uses its own token, token configured in employment spec and access from Hub Environment, or from Request Context. They don't need tokens in the payload. 
What authorization checks happen at ingress level vs agent level?
> Agent is operating in context of a Scenario. All requests to Scenario or updates to Hub Request objects (authorized by SX) are authorized. Agent need not authorize updates that SX-observer forwards. It just needs to verify that the message is dispatched by SX and the message belongs to the workbench where it is employed.

2. sx-observer Implementation Details
a) Store and Forward
What storage backend does sx-observer use (database, message queue, object store)?
How are requests/updates stored (per-agent queues, per-scenario queues, or single workbench queue)?
What is the retention policy for stored requests?
b) Back-Pressure Detection
How does sx-observer detect back-pressure (queue depth, response times, agent health checks)?
What thresholds trigger throttling or pausing dispatch?
How does sx-observer signal back-pressure to Signal Exchange (if at all)?
c) Scale-Up Triggering
How does sx-observer trigger scale-up (Kubernetes API calls, HPA metrics, custom scaling service)?
What is the scale-up latency target (time from trigger to agent ready)?
How does sx-observer verify agents are ready before dispatching?

> Too much details for this spec scope.
> Keep these a common defaults or TBDs at detailed implementation stage.

3. Workbench Data Store Integration
a) Resource Storage
How do agents write to Workbench Data Store (SDK APIs, direct HTTP calls, sidecar service)?
What are the access patterns (write-once-read-many, streaming, batch uploads)?
How are resource URIs generated and formatted?
> Refer to earlier documentation regarding hub stores and agent memory
> stores can be access as tools, explictly through SDK APIs, or through the store service endpoints
> any further details to be determined during implementation

b) Resource Lifecycle
Who manages resource cleanup (agents, sx-observer, Hub services)?
> Hub services

What are the retention policies (time-based, request-based, manual cleanup)?
How are resource access permissions managed?
> Hub documentation covers this. 
> You can ignore here.

4. Agent Ingress Gateway
a) Request Transformation
What transformations happen between Signal Exchange format and Agent dispatch format?
How are request IDs, context, and metadata mapped?
Are there any format validations or schema checks?

> No transformation by default. The Atropos payload is dispatched as-is to agent addition envelope details of the sx-observer.
> Any transformation is  optional and left to developer's requirements.

b) Load Balancing
How does Agent Ingress Gateway load balance across agent pod replicas (round-robin, least-connections, session affinity)?
How does it handle pod failures or unavailability?
Does it maintain session affinity for long-running requests?
> not required detail at this stage,

5. General Architecture
a) Error Handling
How are errors handled when sx-observer cannot reach agents?
What happens if Agent Ingress Gateway fails?
How are partial failures handled (some agents available, others not)?

> sx-observer maintains DLQ in Atropos after configured retries. DLQ can be replayed.
> the sx-observer retry thresholds can be configured per employed agent, with defaults configured at Workbench Instance level.
> a non-retriable failure is a business error and is logged as a Cronus Exception to the Workbench
> agent can directly update the request through agent APIs
> SX therefore need not forward any response to SX from agent. (update any other previous understanding)

b) Observability
What metrics does sx-observer expose (queue depth, dispatch rate, back-pressure events)?
How are request flows traced across Signal Exchange → sx-observer → Agent Ingress Gateway → Agents?
What logging is needed for debugging request routing issues?

> assume best practices
