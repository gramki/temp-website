# Request Sentinels
Ref: .cursor/plans/request_sentinel_implementation_2f91051c.plan.md

Sentinels as Employed Agents in a Workbench  
- Employed for Observing and/or Participating in every request of the Workbench
-- Participation Filters 
--- whitelist/blacklist Scenarios (enrolled into every request as an assignee)
--- On Request Updates (enrolled into a request as an assignee when such update is posted to the request)

Sentinel Scenarios Specs and deployment specs are distinctly called SentinelScenarioSpecs and SentinelScenarioDeploymentSpec. They extend the default Scenario specs of Trained Agents with Sentinel-specific configuration. Deploying SentinelScenarioDeploymentSpec creates Employed Agent as with regular ScenarioSpec assocaited with Trained Agents.

For avoidance of doubt, all request udpates of request that a Sentinel is an assignee of are delivered as notifications via Webhook to the SentinelScenario. This is same as how any assignee of a request can receive notifications for updates in a request. The request created for the SentinelScenario will be a child request to the parent request from which the notification was received, thereby allowsing the Employed Agent to see the context of the parent request. 


# X-Worbench (X-Domain) Scenarios and Request Context Sharing
Ref: .cursor/plans/cross-workbench_request_hierarchy_7918f472.plan.md

As of now, when a Scenario (B) is invoked from a request (R-A) of another Scenario (A), then the request (R-B) created will become child request of R-A if and only if A and B belong to the same workbench.

We now intend to extend the capability for cross-workench request hierarchies to enable cross-domain agent collaboration. 

If Scenario A from Workbench W1 marks a Workbench W2 or a Scenario B from W2 as a child-context AND if W2 marks W1 or Scenario A of W1 as parent-context, then calls from A to B will lead to parent-child relationship between requests of A and B. Both W1 and W2 should be part of same subscription.

To facilitate this we could introduce a new WorkbenchContextSharingSpec that specifies the acceptable parent and child context for a Workbench. A ScenarioAutomationSpecification can have contextSharing section that hold information of what the scenario recognizes as parent or child over and above what the WorkbenchContextSharingSpec recognizes. The ScenarioAutomationSpecification's inclusions are union of WorkbenchContextSharingSpec when assessed at a Scenario level.

All children of a reuqest will access ancestors irrespective of which workbench any ancestor belongs to. To complie the request context of all ancestors the APIs need to make cross-workbench calls. The information passed in the invocation of a Scenario from a different WB with child-context relationship will include the SX and Request Lifecycle Manager endpoint and the request specific access token using which the request context can be fetched by the child workbench applications/services.   

This is an addition to Hub request hierarchy and request dispatch model. Assess the changes required to incorporate this into current hub systems.

Ask me any questions you may have.


# Cognitive Operations Governance Workbench
----
Cognitive Operations Governance Workbench is a new subsystem of Seer. The objective is not enable organizations to automate cognitive operations of the organization using Hub Workbenches and Seer Agents themselves, to the extent the organization chooses to.

Purpose of COGWs is to handle subscription-wide cognitive operations - multi-domain governance, supervision, and learning. They can be used to inject cross-domain or org-wide-knowledge and resources into the agent collaboration context.


Every Subscription of Seer comes with a default COGW. There can be any number of COGW workbenches in a Subscription. Any Workbench can be defined as a COGW in its specification. All the instances of that Workbench will be COGW instances. The Subscription comes with COGW Blueprint to facilitate creation of COGW Specification and from there instances.

Refer to Hub's Cross-Workbench Context Sharing capabilities.
Refer to the Request Sentinels.

Based on these capabilities, the CSAs and Agent Engineers can develop Sentinels that can be employed across all workbenches under a Subscription. However, this workbench comes with an operator to make Sentinels labelled as COG-Sentinels to be auto setup for request assignment with the specified workbenches (allow, disallow list with wildcard support) in the cogSpec part of the SentinelScenarioDeploymentSpec. A COG Sentinel is not permitted to exist in non COG workbenches.

Sentinels defined here can be assigned to all or multiple workbenches.

*enterprise agentic systems** — coordinated, self-optimizing, policy-governed ecosystems where agents reason globally, adapt collectively, and operate under unified semantics across domains.


COG Sentinels are auto enrolled as a Sentinel in every Workbench that is specified in the cogSpec. The sentinel will be enrolled as assignee based on the sentinel section filters in the AutomationSpec. COGW operator ensures all the desired setup and synchronization is done after every change to the Sentinel and to the workbenches under the subscription.

COG Sentinel appear as Sentinel with workbench local Sentinel Scenario Specs in all workbenches. However, all signals to this scenario are forwarded to the COGW instance where the Sentinel is defined. This is to ensure that the COG Sentinel is visible for administrative control and operability controls in each Workbench. COG Sentinels are distinctly recognizable.


=====
9. Key Design Questions
9.1 Participation Model
Q1: When mode: observe, does the Sentinel still create child requests, or only receive notifications?
> Create  child requests always
Q2: Can a Request Sentinel participate in multiple scenarios simultaneously?
> As an employed agent, it is part of only one scenario. However, it can be assigned to any number of scenarios as a collaborator. Therefore, its requests will be child requests to all of those scenario requests. Thus, this sentinel agent becomes part of multiple scenarios.

Q3: What happens if a Request Sentinel is enrolled in a request but the parent request completes before the child request?
> The child request is also deemed as completed. See hub documentation.
> Any updates to request are recorded as stale updates and ignored.
> Ofcourse, the sentinel agent is notified about the closure/completion of the parent request. 

9.2 Enrollment Timing
Q4: For on_request_update: true, which update types trigger enrollment? (All updates, or specific types like STATUS_CHANGE, TASK_LIFECYCLE?)
> This can be specified with a rego expression (OPA policy)

Q5: Can a Request Sentinel be enrolled retroactively in an existing request?
> Yes, it may be manually assigned. If so assigned, it gets to see request updates starting from the update of its assignment to the request. 

9.3 Child Request Behavior
Q6: Does the child request have its own scenario, or does it use the SentinelScenario?
> Sentinel Scenario

Q7: Can the child request create its own child requests (grandchild)?
> Yes, if a agent invokes other scenarios in the workbench as tools or in other hub supported model, the requests of those scenarios become children of this sentinel agent's request. Request hierarchy, ancestory explained in detail in hub docs. Make relevant references.

Q8: What happens to the child request if the parent request is cancelled?
> answered above for completion

9.4 Workbench Scope
Q9: Can a Request Sentinel observe/participate across multiple Workbenches?
> Yes, but I will introduce that concept later.

Q10: How does this relate to the COGW (Cognitive Operations Governance Workbench) concept mentioned in the scratchpad?
> I will explain it after we conclude this part

9.5 Notification Delivery
Q11: Are webhook notifications delivered synchronously or asynchronously?
> Asynchronously

Q12: What happens if the webhook delivery fails? Retry logic?
> Notification service has retry mechanisms and certain level of guarantees. after which the update will be lost until further deliverable update is received by agent. Agent can see if it missed any udpate upon receive this update.

Q13: Does the SentinelScenario need to acknowledge receipt?
> no
----
Clarifying Questions

WorkbenchContextSharingSpec Structure
Should it specify:
a) Workbench-level (W1 can accept W2 as parent/child)
b) Scenario-level (W1 can accept Scenario B from W2 as parent/child)
c) Both (workbench and scenario granularity)

> Both

Bidirectional Configuration
If W1 marks W2 as child-context and W2 marks W1 as parent-context, is that sufficient?
Or must both sides explicitly mark each other (W1→W2 and W2→W1)?
> Context sharing is uni-directional and should be mutually acknowledged by parent and child.

Access Token Scope
Should the request-specific access token:
a) Only allow reading the specific parent request's context
b) Allow reading the entire ancestor chain (all ancestors)
c) Allow reading any request in the parent workbench (broader scope)

> b
> Each workbench in the ancestor chain will have a unique token to allow access to all requests in the ancestor hierarchy from that workbench. 

Context Compilation Performance
When compiling context across workbenches, should:
a) Each ancestor be fetched individually (N calls for N ancestors)
b) A single call fetch the entire ancestor chain
c) Caching be used to reduce cross-workbench calls

> Request lifecycle manager that provides the context of request is unique per workbench.
> The context need to be compiled from all workbenches (so if m unique workbenches in ancestor chain, at least m requests need to be made)


Lifecycle Cascade Across Workbenches
Should parent completion/cancellation cascade to child requests in different workbenches?
Or should cross-workbench relationships only support context sharing, not lifecycle cascade?
> The event will be propagated to all children
> There are no hard guarantees for cascading but there will be best effort cascading

Depth Limits
Should depth limits apply across workbenches (e.g., max depth 5 total, regardless of workbench boundaries)?
Or should each workbench have its own depth limit?
> each workbench

Subscription Validation
Should subscription membership be validated:
a) At request creation time (when creating child request)
b) At configuration time (when setting up WorkbenchContextSharingSpec)
c) Both
> configuration time
=====
4. Clarifying questions
4.1 COGW workbench type
Q1: Should COGW be a distinct workbench_type: "cogw", or a marker/annotation on a regular workbench?
Option A: workbench_type: "cogw" (like devops)
Option B: Annotation/label (e.g., cogw.enabled: true)

> A

4.2 Default COGW creation
Q2: When is the default COGW created?
At subscription creation?
On first COG Sentinel creation?
Manually by admin?
> Subscriotion creation

Q3: Can the default COGW be deleted or only disabled?
> can be deleted

4.3 COG Sentinel labeling
Q4: How is a Sentinel labeled as "COG-Sentinel"?
Label in SentinelSpec metadata?
Presence of cogSpec in SentinelScenarioDeploymentSpec?
Explicit field in SentinelSpec?
> label in metadata and cogSpec presence

4.4 cogSpec structure
Q5: What is the exact structure of cogSpec in SentinelScenarioDeploymentSpec?
cogSpec:  workbenches:    allow: ["workbench-*", "acme-*"]    disallow: ["workbench-dev", "acme-test"]  # Or:  workbench_patterns:    - pattern: "workbench-*"      action: allow    - pattern: "workbench-dev"      action: disallow

>   workbench_patterns:
    - pattern: "workbench-*"
      action: allow
    - pattern: "workbench-dev"
      action: disallow
> we should support a sequence of allow, disallows interspersed 

Q6: Does cogSpec support:
Wildcards in allow/disallow lists?
Regex patterns?
Workbench tags/labels?

> wildcards

4.5 Local SentinelScenarioSpecs
Q7: When COG Sentinel appears in target workbenches:
Are full SentinelScenarioSpec CRDs created locally?
Are they read-only references?
Can local admins override any settings?

> read-only; local-admins are not authorized changes specs, however they can disable the Sentinel

Q8: How are updates to COG Sentinel handled?
Automatic sync to all target workbenches?
Manual sync trigger?
Versioning per workbench?
> Automatic sync

4.6 Signal forwarding
Q9: When a COG Sentinel is enrolled in a target workbench request:
Are all request updates forwarded to COGW?
Only updates matching the sentinel's filters?
How is the forwarding implemented (Signal Exchange, Notification Service)?

> Filtered locally before forwarded COGW


Q10: Does the child request in COGW have access to:
Full parent request context?
Filtered context?
Only specific fields?
> Upto Context Compiler of the Sentinel

4.7 Administrative controls
Q11: In target workbenches, can local admins:
See COG Sentinel status?
Enable/disable COG Sentinel?
Override enrollment filters?
Or is control only in COGW?
> Enable/Disble
> No other changes

4.8 COGW operator scope
Q12: Does the COGW operator:
Run only in COGW workbench instances?
Run at subscription level?
Need access to all workbenches in subscription?
> Yes to all

4.9 Multiple COGW workbenches
Q13: If multiple COGW workbenches exist in a subscription:
Can a COG Sentinel be defined in any COGW?
Can workbenches be targeted by multiple COGWs?
How are conflicts resolved?
> There no conflicts. All COGWs sentinels are unique and they all can particpate in all workbenches.

4.10 Blueprint structure
Q14: What should the COGW Blueprint include?
Default COG Sentinels?
Standard governance scenarios?
Configuration templates?

> Standard governance scenarios