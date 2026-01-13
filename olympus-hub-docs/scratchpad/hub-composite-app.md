# Hub Composite Application

## Objective
- Allow multiple Hub Applications to participate in a single Hub Request
- Each application independently evaluates request updates
- Each application can add inputs: create tasks, produce updates, etc.
- Support multi-agent topologies without task-assignment
- Each employed agent is a Hub Application deployment

## Lightweight Approach
- Runtime is Hub (no special composite runtime)
- Individual applications are dispatched all request updates
- No coordination or orchestration between applications
- All applications are equal participants
- No hierarchy or leader-follower pattern

## Design Principles
- **No changes to existing Hub Application specs** from various runtimes
- Add new spec type: `HubCompositeApplicationSpec`
- Composite spec references other Hub Application Specs
- Applications maintain their existing behavior and interfaces

## Composite Specification
- New CRD: `HubCompositeApplicationSpec`
- Contains list of references to other `HubApplicationSpec` resources
- Composite itself is referenced in `AutomationSpec` (like regular apps)
- Operator processes composite and identifies constituent apps to deploy
- Supports nested composites (resolved as union of all referenced apps)
- Supports cross-runtime composites (Seer + Rhea + Atlantis, etc.)

## Deployment Behavior
- When composite is referenced in `AutomationSpec`, operator:
  1. Picks the composite spec
  2. Identifies all referenced Hub Application Specs (recursively if nested)
  3. Deploys all constituent applications (all-or-nothing)
- All deployed applications receive all request updates by default
- Each application operates independently on the same request
- Composite modifications require redeployment (not dynamic)

## Use Cases

### Example 1: Planner-Executor-Critic (PEC Loop)
**Scenario**: High-Value Transaction Approval

**Composite Apps**:
- **Planner Agent** (Seer): Creates approval plan, identifies required checks
- **Executor Agent** (Seer): Performs actual transaction processing, executes checks
- **Critic Agent** (Seer): Evaluates outcomes, validates compliance, provides feedback

**Interaction Pattern**:
- Planner receives `REQUEST_CREATED` → creates plan → updates request with plan
- Executor receives `PLAN_CREATED` update → executes plan → updates with results
- Critic receives `EXECUTION_COMPLETE` update → evaluates → updates with critique
- Loop continues until Critic approves or rejects

**OPA Filters**:
- Planner: `update_type in ["REQUEST_CREATED", "CRITIC_FEEDBACK"]`
- Executor: `update_type in ["PLAN_CREATED", "CRITIC_FEEDBACK"]`
- Critic: `update_type in ["EXECUTION_COMPLETE", "PLAN_CREATED"]`

**Use Case**: Safety-sensitive actions (funds movement, policy changes, production deploys)

---

### Example 2: Blackboard (Shared Memory Coordination)
**Scenario**: Complex Dispute Investigation

**Composite Apps**:
- **Risk Agent** (Seer): Evaluates fraud patterns, transaction anomalies
- **Compliance Agent** (Seer): Checks regulatory requirements, Reg E compliance
- **Customer Service Agent** (Seer): Handles customer communication, satisfaction
- **Document Analyzer** (Atlantis): Extracts and analyzes uploaded documents

**Interaction Pattern**:
- All agents receive all request updates
- Each agent independently evaluates and contributes findings
- Agents read shared request state (blackboard) and write their perspectives
- No explicit coordination - agents react to state changes
- Final decision made by human supervisor based on all contributions

**OPA Filters**:
- Risk Agent: `update_type in ["REQUEST_CREATED", "DOCUMENT_UPLOADED", "TRANSACTION_DATA_ADDED"]`
- Compliance Agent: `update_type in ["REQUEST_CREATED", "DOCUMENT_UPLOADED", "RISK_ASSESSMENT_COMPLETE"]`
- Customer Service Agent: `update_type in ["REQUEST_CREATED", "CUSTOMER_MESSAGE_RECEIVED"]`
- Document Analyzer: `update_type == "DOCUMENT_UPLOADED"`

**Use Case**: Multi-specialist collaboration, knowledge-centric investigations, cases requiring multiple perspectives

---

### Example 3: Market-Based / Auction
**Scenario**: Dynamic Task Routing for Customer Inquiries

**Composite Apps**:
- **Inquiry Router** (Rhea Workflow): Receives customer inquiries, broadcasts to specialists
- **Product Specialist Agent** (Seer): Bids on product-related inquiries
- **Technical Support Agent** (Seer): Bids on technical issues
- **Billing Specialist Agent** (Seer): Bids on billing/payment inquiries
- **Task Assigner** (Atlantis): Evaluates bids, assigns to best match

**Interaction Pattern**:
- Router broadcasts inquiry via request update
- Specialist agents evaluate inquiry and "bid" (create task proposals with confidence scores)
- Task Assigner receives all bids, selects best match, creates final task
- Selected specialist receives assignment and processes

**OPA Filters**:
- Router: `update_type == "REQUEST_CREATED"`
- Product Specialist: `update_type in ["INQUIRY_BROADCAST", "TASK_ASSIGNED"]` + content filter for product keywords
- Technical Support: `update_type in ["INQUIRY_BROADCAST", "TASK_ASSIGNED"]` + content filter for technical keywords
- Billing Specialist: `update_type in ["INQUIRY_BROADCAST", "TASK_ASSIGNED"]` + content filter for billing keywords
- Task Assigner: `update_type == "BID_SUBMITTED"`

**Use Case**: Dynamic resource allocation, load balancing, optimization under uncertainty

---

### Example 4: Role-Specialized Committees (Multi-Perspective Review)
**Scenario**: Credit Committee Decision

**Composite Apps**:
- **Risk Analyst Agent** (Seer): Evaluates credit risk, default probability
- **Compliance Officer Agent** (Seer): Checks regulatory compliance, policy adherence
- **Relationship Manager Agent** (Seer): Evaluates customer relationship value
- **Credit Committee Coordinator** (Rhea Workflow): Aggregates perspectives, manages voting

**Interaction Pattern**:
- All agents receive application details
- Each agent independently evaluates from their perspective
- Agents contribute assessment updates to shared request
- Coordinator aggregates, presents to human committee for final decision

**OPA Filters**:
- Risk Analyst: `update_type in ["APPLICATION_SUBMITTED", "CREDIT_DATA_ADDED"]`
- Compliance Officer: `update_type in ["APPLICATION_SUBMITTED", "RISK_ASSESSMENT_COMPLETE"]`
- Relationship Manager: `update_type in ["APPLICATION_SUBMITTED", "CUSTOMER_HISTORY_ADDED"]`
- Coordinator: `update_type in ["RISK_ASSESSMENT_COMPLETE", "COMPLIANCE_ASSESSMENT_COMPLETE", "RELATIONSHIP_ASSESSMENT_COMPLETE"]`

**Use Case**: High-stakes decisions, regulated approvals, exception handling

---

## Design Decisions

### Conflicting Updates
- Latest update to reach Signal Exchange overrides previous state (if legal to update)
- If update is illegal, latest is recorded as rejected update
- Update legality determined by OPA policy or application logic

### Update Filtering
- Support OPA filter per app referenced in Composite CRD
- Filters based on `update_type` field in request updates
- Allows selective update routing to constituent applications
- Each agent subscribes only to relevant update types for their role

### Task Creation
- Multiple apps can create tasks for same agent
- Duplicate work resolved by agents and supervisors
- No coordination required at composite level

### Failure Handling
- Dispatches are asynchronous
- Signal Exchange manages DLQ for updates that couldn't be dispatched
- Individual app failures don't block other apps in composite
- Each app operates independently

### Deployment Lifecycle
- If one app in composite fails to deploy, entire deployment is deemed failed
- Rollback applies to all constituent applications
- All-or-nothing deployment model
- Composite modifications require redeployment (not dynamic)

### Cross-Runtime Support
- Composites can include apps from different runtimes
- Example: Seer agent + Rhea workflow + Atlantis procedure
- Each app deployed to its respective runtime
- All apps receive same request updates via Signal Exchange

### Nested Composites
- Composites can reference other composites
- Resolved as union of all referenced apps (flattened)
- No special handling needed - just recursive resolution

---

## Notes

- Composite applications enable multi-agent topologies without explicit orchestrators
- Each agent operates independently with its own session
- Coordination happens through shared Request state (blackboard pattern)
- OPA filters enable selective update routing based on update_type
- See [Hub Composite Application](../../02-system-design/implementation-concepts/hub-composite-application.md) for full documentation