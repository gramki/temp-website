# 5. Managing Requirements & Their Evolution

## The Foundation of Everything

Requirements are the foundation of delivery success. Get them wrong, and everything else becomes harder: cost overruns, scope creep, quality issues, and stakeholder conflicts.

This section converts abstract notions of "vague requirements" and "requirement drift" into practical governance, tooling, and behavior strategies. It bridges business intent → delivery units (Feature, Epic, Story) → testability → change control.

> **VP Insight**: "In one program, we built a dashboard showing 30% of backlog lacked AC. The client's PMO complained about overhead until we showed how that correlated with 40% rework cost. Suddenly, the dashboard became their best friend."

## 5.1 Requirement Taxonomy & Ownership

### The Hierarchy

**Requirement** → **Feature** → **Epic** → **Story**

Each level has different owners and purposes:

| Level | Owner | Purpose | Example |
|-------|-------|---------|---------|
| **Requirement** | Customer Team | Business intent | "Enable real-time fraud detection" |
| **Feature** | Customer Team | Solution design | "ML-based transaction scoring API" |
| **Epic** | Delivery Team | Implementation scope | "Real-time scoring engine" |
| **Story** | Delivery Team | Development work | "Implement scoring algorithm" |

### Ownership Rules

- **Customer Team owns Requirements**: They define what business problem to solve
- **Customer Team owns Features**: They design how to solve it and are accountable for ensuring requirements are met
- **Customer Team is accountable for Feature Acceptance Criteria**: Regardless of who does the requirement decomposition
- **Delivery Team is consulted for converting Requirements to Features**: They provide technical input and feasibility guidance
- **Delivery Team owns Epics & Stories**: They break down features into implementation work
- **Delivery Team may perform requirement decomposition**: But Customer Team remains accountable for feature acceptance criteria
- **Requirement decomposition is billable work**: Involves solutioning, deliberation, stakeholder interviews, and technical analysis

### Two Distinct Decomposition Steps

**Step 1: Requirement Decomposition** (Requirement → Features)
- Converts business requirements into solution features
- Involves stakeholder interviews, technical analysis, solution design
- Customer Team accountable for feature acceptance criteria
- Billable work for Delivery Team if they perform it

**Step 2: Feature Decomposition** (Feature → Epics → Stories)
- Converts approved features into implementation work
- Requires design documentation and impact assessment sign-off
- Delivery Team owns the decomposition process
- Part of development planning

### Scope Boundaries

- **Requirements**: Can span multiple modules/subsystems (business capability level)
- **Features**: Must be scoped to a single subsystem boundary (implementation level)

> **Note**: A subsystem is a cohesive slice of the larger system (e.g., Payments Authorization, Settlement, Ledger, Fraud, Notifications). It may contain multiple services and data stores. Features should target a subsystem boundary, not an individual microservice.

> **Why This Matters**: Mixing these terms is one of the biggest early confusion sources. When a client says "we need a feature for fraud detection," they mean a requirement. When you say "we'll build a feature," you mean a solution.

### Real Example

**Step 1: Requirement Decomposition**
**Client says**: "We need fraud detection" (Requirement - spans payment, user, and notification modules)
**Studio consults**: Technical analysis, stakeholder interviews, solution options
**Client designs**: "We'll build an ML-based scoring API" (Feature - scoped to payment module)
**Client signs off**: Feature acceptance criteria and design approach

**Step 2: Feature Decomposition**
**Studio breaks down**: "Real-time scoring engine" (Epic)
**Studio implements**: "Implement scoring algorithm" (Story)

The client owns the problem and solution design. The Studio owns the implementation breakdown.

## 5.2 Minimally Acceptable Requirements (MAR)

### What MAR Means

A requirement is "minimally acceptable" when it has just enough information to:
- Estimate effort and risk
- Design a solution
- Write acceptance criteria
- Identify dependencies

### MAR Checklist

A requirement must have:

✅ **Intent**: What business problem does it solve?
✅ **Boundaries**: What's in scope, what's out?
✅ **Dependencies**: What does it depend on?
✅ **Constraints**: What are the limits?
✅ **Initial Acceptance Criteria**: How do we know it's done?

### Real Example

**Bad Requirement**: "Make the app faster"

**MAR Requirement**: 
- **Intent**: Reduce mobile app load time to improve user experience
- **Boundaries**: Home screen and login flow only
- **Dependencies**: CDN implementation, image optimization
- **Constraints**: Must work on iOS 12+, Android 8+
- **Initial AC**: Home screen loads in <3 seconds on 3G

> **Pro Tip**: If you can't write a test for it, it isn't minimally acceptable.

## 5.3 Ready-for-Planning (RfP) Gate

### The Gate

Before a requirement enters sprint planning, it must pass the RfP gate. This prevents planning with incomplete information.

### RfP Criteria

A requirement is Ready-for-Planning when:

✅ **MAR Complete**: All MAR elements present
✅ **Decomposed to Features**: Requirement broken down into specific features
✅ **AC Written**: All acceptance criteria defined
✅ **Dependencies Mapped**: All dependencies identified
✅ **Impacts Assessed**: All system impacts understood
✅ **Stakeholders Aligned**: All stakeholders agree on scope

### Requirement State Progression

**MAR** → **Decomposed** → **RfP**

### Decomposition Flow (At a glance)
Use this quick map to orient new readers. It shows the requirement flow and the implementation flow with their gating checks.

```mermaid
flowchart TB
  subgraph Requirement Flow
    R[Requirement] --> MAR[MAR]
    MAR --> DEC[Decomposed]
    DEC --> RFP[RfP (signed Features)]
    RFP --> PLAN[Planned]
    PLAN --> DEV[In Development]
  end

  subgraph Implementation Flow
    F[Feature] --> E[Epic]
    E --> S[Story]
  end

  %% Gates
  G1[Design/Impact sign-off]:::gate
  G2[AC/NFR sign-off]:::gate

  F -. requires .- G1
  F -. requires .- G2

  classDef gate fill:#fff7e6,stroke:#f0a202,color:#333;
```

See 5.8 for Feature Decomposition Gates (Design/Impact, AC/NFR, Risk Registry) and 5.10 for Integration Readiness before planning.

- **MAR**: Minimally acceptable for initial analysis
- **Decomposed**: Broken down into specific features
- **RfP**: Feature definitions signed off by Customer Team

### Transition from Decomposed to RfP

A requirement moves from **Decomposed** to **RfP** when:

✅ **Feature Definitions Complete**: All features identified and documented
✅ **Customer Team Sign-off**: Customer Team approves feature definitions and acceptance criteria
✅ **Design Documentation**: Each feature has appropriate design documentation
✅ **Impact Assessment**: Technical, business, and operational impacts assessed
✅ **Risk Registry**: All identified risks documented and assessed

**Real Example**: 
- **Decomposed**: "Fraud detection" broken into 3 features: "ML scoring API", "Real-time alerts", "Audit logging"
- **RfP**: Customer Team signs off on all 3 feature definitions, acceptance criteria, and design approaches

### Examples: Requirement → Multiple Features

**Example A: PSD2 SCA Compliance (EU Card‑Not‑Present)**
- **Requirement (MAR excerpt)**: Enforce Strong Customer Authentication for EU CNP payments; scope web + mobile checkout; exemptions per RTS; <2% auth failure increase.
- **Feature 1 (Payments Authorization subsystem)**: SCA challenge orchestration with 3DS 2.x
  - Measurable: SCA success ≥97% sandbox parity; auth failure delta <2%
  - Testable: 3DS challenge/frictionless flows, fallback to 3DS 1
- **Feature 2 (Checkout UX subsystem: Web & Mobile)**: SCA UX surfaces challenge, handles timeouts and retries
  - Measurable: checkout abandonment ≤+1% vs baseline during SCA
  - Testable: device/browser matrix, timeout/retry edge cases
- **Feature 3 (Notifications subsystem)**: OTP/SMS/email fallback and customer comms for step‑up
  - Measurable: message delivery ≥99%; retry ≤3; link expiry honored
  - Testable: deliverability tests, link/OTP expiry, locale variants
- **Feature 4 (Fraud/Risk subsystem)**: Risk‑based exemptions policy engine (TRA, low‑value)
  - Measurable: exemption utilization reported; false‑decline rate unchanged
  - Testable: policy evaluation tests, audit log of exemptions

**Example B: Card Dispute/Chargeback Handling**
- **Requirement (MAR excerpt)**: Provide end‑to‑end dispute handling for card transactions; SLA: evidence within 10 days; regulator access to audit trail.
- **Feature 1 (Customer Portal subsystem)**: Dispute intake + status tracking
  - Measurable: create case ≤2s; upload ≤100MB evidence; P95 read <300ms
  - Testable: file types, size limits, status transitions
- **Feature 2 (Case Management subsystem)**: Dispute workflow + SLA timers and roles
  - Measurable: SLA breach alerts <1 min; assign/reassign <1s
  - Testable: workflow paths, escalation rules, audit of actions
- **Feature 3 (Network Integration subsystem)**: Card network chargeback API integration
  - Measurable: API success ≥99.5%; retries with backoff; idempotency keys
  - Testable: happy/error paths, retry/idempotency, schema conformance
- **Feature 4 (Ledger/Settlement subsystem)**: Financial adjustments and reversals
  - Measurable: double‑entry integrity; cutoff posting rules; P95 post <150ms
  - Testable: accounting invariants, reversal flows, report parity

### Additional Single-Feature Examples

- **Performance Enhancement (Payments Authorization subsystem)**
  - Feature: Caching layer to reduce `/authorize` P95 from 2s → 200ms at 1k RPS
  - Testable AC: Load tests meet target; cache hit ≥85%; correctness on invalidation

- **Apple Pay Acceptance (iOS Checkout subsystem)**
  - Feature: Support PKPaymentAuthorizationController with 3DS step-up
  - Testable AC: Device matrix passes; tokenization error <1%; challenge/decline paths covered

### Feature Decomposition Gates

Before a Feature can be decomposed into Epics and Stories, it must have:

✅ **Design Documentation**: Design note (simple) or design document (complex)
✅ **Impact Assessment**: Technical, business, and operational impact analysis
✅ **Design Sign-off**: Customer Team approval of design approach
✅ **Risk Registry Entries**: All identified risks documented and assessed

### Real Example

**Not RfP**: "Add payment method validation" (no AC, no dependencies)
**RfP**: "Add payment method validation that checks card number format, expiry date, and CVV before allowing payment submission, with error messages for each validation failure, integrated with existing payment form"

> **VP Insight**: The number of "incomplete" RfP items is a leading indicator of planning risk.

## 5.4 Acceptance Criteria: Smells & Maturity

### Good Acceptance Criteria

✅ **Testable**: Can be verified with tests
✅ **Observable**: Can be seen or measured
✅ **Data Thresholds**: Specific numbers or values
✅ **Deterministic**: Same input = same output

### Bad Acceptance Criteria (Smells)

❌ **Vague**: "Works as expected"
❌ **Ambiguous**: "User-friendly interface"
❌ **UI Only**: "Button should be blue"
❌ **Subjective**: "Looks professional"

### Real Example

**Bad AC**: "User can login successfully"

**Good AC**: 
- User can login with valid email/password
- Login fails with invalid credentials
- Login shows error message after 3 failed attempts
- Login redirects to dashboard on success
- Login logs all attempts for security

> **From the Field**: "We once accepted a story because user said 'works as expected' — months later we discovered 3 scenarios that failed."

## 5.5 Navigating Requirement Decomposition

### The Challenge of Unknowns

Requirement decomposition is the most uncertain phase in enterprise delivery. Unlike development work, you can't estimate decomposition effort accurately because:

- **Stakeholder availability** is unpredictable
- **Business context** emerges during interviews
- **Technical complexity** reveals itself during analysis
- **Integration points** are often discovered late
- **Compliance requirements** surface during deep dives

### Experience-Informed Approach

**1. Start with Time-Boxed Discovery**
- Allocate 1-2 weeks for initial discovery
- Use this to understand scope and complexity
- Don't commit to full decomposition timeline upfront

**Real Example**: "We need 2 weeks to understand your fraud detection requirement. After that, we'll give you a realistic timeline for full decomposition."

**2. Progressive Decomposition**
- Break down requirements in waves, not all at once
- Start with highest-priority or highest-risk requirements
- Use learnings from early waves to improve later ones

**Real Example**: "Let's decompose your payment processing requirement first. We'll learn about your systems and processes, then apply that knowledge to fraud detection."

**3. Parallel Discovery Tracks**
- Technical analysis (architecture, integration points)
- Business analysis (processes, stakeholders, constraints)
- Compliance analysis (regulations, audit requirements)
- Run these in parallel to maximize learning

### Communication & Visibility

**Weekly Discovery Reports**
- What we learned this week
- What questions we answered
- What new questions emerged
- What risks we identified
- Next week's focus areas

**Real Example**:
```
Week 1 Discovery Report:
✅ Learned: Payment system uses 15-year-old COBOL mainframe
✅ Answered: Integration requires message queue, not direct API
❓ New Question: How do you handle transaction reversals?
⚠️ Risk: Mainframe team availability unknown
📋 Next Week: Interview mainframe team, map data flows
```

**Stakeholder Checkpoints**
- Weekly 30-minute sync with key stakeholders
- Show progress, not just status
- Surface decisions needed, not just information gathered
- Use visual aids (diagrams, flowcharts) to show understanding

**Real Example**: "Here's what we understand about your payment flow. Does this look right? What are we missing?"

**Risk-First Approach**
- Identify the biggest unknowns first
- Tackle high-risk, high-impact questions early
- Don't save the hard questions for last

**Real Example**: "The biggest unknown is your mainframe integration. Let's solve that first before we design the API."

### Managing Client Expectations

**Set Realistic Expectations**
- "We can't estimate decomposition effort accurately because we don't know what we don't know"
- "We'll give you weekly updates and adjust timeline as we learn"
- "Some requirements will be easy to decompose, others will surprise us"

**Use Discovery Phases**
- Phase 1: High-level understanding (1-2 weeks)
- Phase 2: Detailed decomposition (2-4 weeks per requirement)
- Phase 3: Validation and refinement (1 week)

**Real Example**: "Phase 1 will cost $25K and tell us if this is a 3-month or 6-month project. Phase 2 will give you the detailed features and estimates."

### Progress Tracking

**Discovery Metrics**
- Number of stakeholders interviewed
- Number of questions answered vs. total questions
- Number of features identified
- Number of risks identified
- Number of dependencies mapped

**Visual Progress Indicators**
- Progress bars for each discovery track
- Risk heat maps
- Stakeholder interview completion
- Feature identification timeline

**Real Example**:
```
Discovery Progress:
Technical Analysis: ████████░░ 80%
Business Analysis: ██████░░░░ 60%
Compliance Analysis: ████░░░░░░ 40%
Stakeholder Interviews: 8/12 completed
Features Identified: 3/8 estimated
```

> **VP Insight**: "I've seen teams spend 6 months 'analyzing' requirements without decomposing anything. Time-box discovery, show progress weekly, and decompose in waves."

## 5.6 Requirement Evolution

### Three Types of Change

**Discovery**: We learn something new about the existing requirement
**Clarification**: We understand the requirement better
**Emergence**: A new requirement appears

### How to Handle Each

**Discovery**: Update the requirement, log the change, re-estimate if needed
**Clarification**: Refine the requirement, update AC, no re-estimation
**Emergence**: New requirement, new estimation, new funding discussion

### Real Example

**Original**: "Build payment processing"
**Discovery**: "Payment must support 15 currencies" (update existing)
**Clarification**: "Payment means credit card only" (refine existing)
**Emergence**: "Add mobile wallet support" (new requirement)

> **Caution**: Lumping all changes into "scope creep" kills judgment. Some changes are legitimate discoveries.

## 5.7 Jira Practices for Requirement Control

### Labels for Risk Management

**Decomposition Labels:**
- **decomposed**: Requirement broken down into features
- **decomposition-in-progress**: Currently being decomposed
- **decomposition-blocked**: Blocked by missing information
- **features-pending-signoff**: Features defined, awaiting Customer Team approval
- **rfp-yes**: Ready for planning (Customer Team signed off)

**Risk Management Labels:**
- **ac-missing**: Missing acceptance criteria
- **integration-risk**: High integration complexity
- **dependency-blocked**: Blocked by external dependency
- **estimate-tbd**: Estimation pending

### Why Labels Instead of Fields?

**Labels are better for decomposition tracking because:**

1. **Multiple States**: A requirement can have multiple labels simultaneously (e.g., "decomposed" + "ac-missing" + "integration-risk")

2. **Flexible Filtering**: Easy to filter by any combination of labels in Jira queries and dashboards

3. **Visual Clarity**: Labels show up as colored tags, making status immediately visible

4. **Agile-Friendly**: Labels align with agile practices and are familiar to development teams

5. **Searchable**: Can search across all issues with specific label combinations

**Fields would be limiting because:**
- Single-select fields force one state at a time
- Multi-select fields are harder to filter and visualize
- Custom fields require more setup and maintenance
- Less intuitive for team members

**Real Example**: A requirement with labels "decomposed", "features-pending-signoff", "integration-risk" immediately shows it's been decomposed but needs Customer sign-off and has integration complexity.

### Status Workflow

**Requirement** → **In Progress** → **RfP** → **Planned** → **In Development** → **Done**

### Workflow Stage Definitions

**Requirement**
- **Definition**: Initial requirement captured, not yet started
- **Criteria**: MAR complete, stakeholder identified, scope defined
- **Labels**: None (or "new-requirement")

**In Progress**
- **Definition**: Requirement decomposition has started
- **Criteria**: Decomposition work initiated, stakeholders being interviewed
- **Labels**: "decomposition-in-progress"
- **Transition Trigger**: Studio begins decomposition work

**RfP (Ready for Planning)**
- **Definition**: Requirement decomposed into features, Customer Team signed off
- **Criteria**: Features defined, AC written, dependencies mapped, Customer Team approval
- **Labels**: "decomposed", "rfp-yes"
- **Transition Trigger**: Customer Team signs off on feature definitions and acceptance criteria

**Planned**
- **Definition**: Features broken down into epics/stories, assigned to sprints
- **Criteria**: Design documentation complete, impact assessment done, sprint allocation
- **Labels**: "planned", "design-complete"
- **Transition Trigger**: Features decomposed into epics/stories and assigned to development sprints

**In Development**
- **Definition**: Development work has started
- **Criteria**: Stories in active development, code being written
- **Labels**: "in-development"
- **Transition Trigger**: First story enters development status

**Done**
- **Definition**: All features delivered and accepted
- **Criteria**: All stories completed, features tested, Customer Team acceptance
- **Labels**: "done", "delivered"
- **Transition Trigger**: Customer Team accepts all features as meeting requirements

### Tracking Partial Delivery

**The Challenge**: Requirements often span multiple sprints. Features can be delivered incrementally while the requirement remains "In Development."

**Solution**: Track both requirement-level and feature-level completion:

**Requirement-Level Tracking**:
- **Status**: Remains "In Development" until all features are delivered
- **Progress**: Track percentage of features completed
- **Labels**: Add "partially-delivered" when some features are accepted

**Feature-Level Tracking**:
- **Individual Feature Status**: Each feature has its own lifecycle
- **Feature Acceptance**: Customer Team accepts individual features
- **Feature Labels**: "feature-accepted", "feature-in-development", "feature-done"

**Real Example**:
```
Requirement: "Real-time fraud detection"
Status: In Development
Progress: 2/3 features completed (67%)

Features:
✅ ML scoring API (accepted by Customer Team)
✅ Real-time alerts (accepted by Customer Team)  
🔄 Audit logging (in development)

Labels: "in-development", "partially-delivered"
```

### Delivery Tracking Metrics

**Requirement Completion Percentage**:
- **Feature Count Method**: (Accepted Features / Total Features) × 100
- **Story Points Method**: (Completed Story Points / Total Story Points) × 100
- **Effort Hours Method**: (Completed Effort Hours / Total Effort Hours) × 100
- **Recommended**: Use Story Points for more accurate progress tracking

**Feature Delivery Timeline**:
- Track when each feature was accepted
- Identify delivery patterns and bottlenecks
- Plan remaining feature delivery

**Customer Value Delivered**:
- Track business value of accepted features
- Show incremental value delivery
- Justify continued investment

**Real Example**:
```
Week 1: ML scoring API accepted (33% complete)
Week 3: Real-time alerts accepted (67% complete)  
Week 5: Audit logging accepted (100% complete)
Requirement Status: Done
```

### Jira Implementation for Effort-Based Progress

**Custom Fields for Progress Tracking**:

**Requirement-Level Fields**:
- **Total Story Points**: Sum of all story points for the requirement
- **Completed Story Points**: Sum of completed story points
- **Progress Percentage**: (Completed Story Points / Total Story Points) × 100
- **Estimated Completion**: Calculated based on velocity and remaining points

**Feature-Level Fields**:
- **Feature Story Points**: Story points for this specific feature
- **Feature Status**: "Not Started", "In Progress", "Completed", "Accepted"
- **Feature Completion Date**: When Customer Team accepted the feature

**Jira Configuration**:

**1. Custom Fields Setup**:
```
Field Name: Total Story Points
Type: Number
Scope: Requirement issues

Field Name: Completed Story Points  
Type: Number
Scope: Requirement issues

Field Name: Progress Percentage
Type: Number (calculated field)
Formula: (Completed Story Points / Total Story Points) × 100
Scope: Requirement issues
```

**2. Automation Rules**:
```
When: Story status changes to "Done"
Action: Add story points to "Completed Story Points" field
Update: Progress Percentage field

When: Feature status changes to "Accepted"
Action: Add feature story points to "Completed Story Points" field
Update: Progress Percentage field
```

**3. Dashboard Widgets**:
- **Progress Bar**: Shows completion percentage for each requirement
- **Burndown Chart**: Story points completed over time
- **Feature Status Board**: Visual status of all features
- **Velocity Tracking**: Average story points completed per sprint

**Real Example in Jira**:
```
Requirement: "Real-time fraud detection"
Total Story Points: 100
Completed Story Points: 67
Progress Percentage: 67%

Features:
✅ ML scoring API (40 story points, accepted)
✅ Real-time alerts (27 story points, accepted)  
🔄 Audit logging (33 story points, in progress)

Labels: "in-development", "partially-delivered"
```

**4. Reporting Queries**:
```
JQL for Requirements in Progress:
project = "PROJ" AND status = "In Development" AND "Progress Percentage" < 100

JQL for Requirements with Partial Delivery:
project = "PROJ" AND labels in ("partially-delivered")

JQL for Features Pending Acceptance:
project = "PROJ" AND "Feature Status" = "Completed" AND status != "Done"
```

**5. Progress Visualization**:
- **Requirement Progress Board**: Shows all requirements with progress bars
- **Feature Delivery Timeline**: Gantt chart showing feature delivery schedule
- **Velocity Burndown**: Story points completed vs. planned over time
- **Risk Dashboard**: Requirements with low progress or blocked features

> **VP Insight**: "I've seen requirements show 80% complete by feature count but only 40% complete by story points. Always use effort-based metrics for accurate progress tracking."

### Managing Partial Delivery

**Weekly Progress Reports**:
- Show which features are accepted
- Highlight which features are in progress
- Identify any blocked features
- Update requirement completion percentage

**Customer Communication**:
- "We've delivered 2 of 3 features for fraud detection"
- "The remaining feature will be ready next sprint"
- "You can start using the accepted features immediately"

**Risk Management**:
- Monitor features that are taking longer than expected
- Identify dependencies between features
- Plan for potential scope changes

> **VP Insight**: "I've seen requirements stuck at 80% completion for months because the last feature was complex. Track feature-level progress to identify and address these bottlenecks early."

### Transition Rules

**Forward Transitions** (normal flow):
- **Requirement → In Progress**: Studio starts decomposition work
- **In Progress → RfP**: Customer Team signs off on feature definitions
- **RfP → Planned**: Features decomposed and assigned to sprints
- **Planned → In Development**: First story enters development
- **In Development → Done**: All features delivered and accepted

**Backward Transitions** (when issues arise):
- **RfP → In Progress**: Customer Team requests changes to feature definitions
- **Planned → RfP**: Design issues discovered, need to rework features
- **In Development → Planned**: Major scope changes require replanning

**Blocked States** (temporary):
- **In Progress + decomposition-blocked**: Missing stakeholder information
- **RfP + features-pending-signoff**: Waiting for Customer Team approval
- **Planned + dependency-blocked**: Blocked by external dependencies

> **VP Insight**: "I've seen requirements stuck in 'In Progress' for months because teams didn't know when to move to RfP. The key is Customer Team sign-off on feature definitions."

### Custom Fields

- **MAR Score**: 1-5 maturity rating
- **RfP Date**: When it became ready
- **AC Count**: Number of acceptance criteria
- **Dependency Count**: Number of dependencies

> **Pro Tip**: Use rfp-yes label, ac-missing, integration-risk flags to surface risk trends.

## 5.8 Feature Decomposition Gates

### Design Documentation Requirements

Before a feature can be decomposed into epics and stories, it must have appropriate design documentation:

**Simple Features**: Design note (1-2 pages)
- High-level approach
- Key technical decisions
- Integration points
- Risk summary

**Complex Features**: Design document (5-10 pages)
- Detailed architecture
- Technical specifications
- Data flow diagrams
- Security considerations
- Performance requirements
- Integration contracts

### Impact Assessment

Every feature must have a comprehensive impact assessment covering:

**Technical Impact**:
- System architecture changes
- Database modifications
- API changes
- Performance implications
- Security considerations

**Business Impact**:
- User experience changes
- Process modifications
- Compliance requirements
- Training needs

**Operational Impact**:
- Deployment requirements
- Monitoring needs
- Support implications
- Rollback procedures

### Real Example

**Feature**: "ML-based transaction scoring API"

**Design Document** (8 pages):
- Architecture: Microservice with Redis cache
- Integration: REST API with Bank Core System
- Security: OAuth 2.0, data encryption
- Performance: <100ms response time
- Monitoring: Prometheus metrics

**Impact Assessment**:
- Technical: New microservice, Redis cluster, ML model deployment
- Business: Real-time fraud detection, reduced false positives
- Operational: 24/7 monitoring, model retraining process

**Risk Registry**:
- High: ML model accuracy degradation
- Medium: Redis cluster failure
- Low: API version compatibility

> **VP Insight**: Features without proper design documentation often lead to significant project delays and cost overruns. I've seen teams spend months reworking features because they didn't understand the full scope and dependencies upfront.

## 5.9 Feature Decomposition Process

### Decomposition Rules

**Feature**: High-level solution (typically 1-6 months in enterprise contexts)
**Epic**: Implementation scope (typically 2-8 weeks depending on complexity)
**Story**: Development work (typically 1-5 days, but can vary significantly)

> **Note**: These timelines are general guidelines. Enterprise delivery often involves longer timelines due to compliance requirements, integration complexity, and stakeholder coordination. Adjust based on your specific context and team velocity.

### Why Enterprise Features Take 4-6 Weeks or More

**What Developers Often Miss in Estimates**:

**1. Enterprise Integration Complexity** (1-2 weeks)
- Legacy system integration requires data mapping, protocol translation
- API versioning and backward compatibility concerns
- Authentication and authorization across multiple systems
- Error handling and retry logic for external dependencies

**2. Compliance & Security Requirements** (1-2 weeks)
- Security review and penetration testing
- Compliance audit preparation (PCI DSS, SOX, GDPR)
- Data privacy impact assessments
- Regulatory approval processes

**3. Quality Assurance & Testing** (1-2 weeks)
- Integration testing with multiple systems
- Performance testing under enterprise load
- User acceptance testing with business stakeholders
- Security testing and vulnerability scanning

**4. Deployment & Operations** (1 week)
- Production environment provisioning
- Database migration scripts and rollback procedures
- Monitoring and alerting setup
- Documentation for operations team

**5. Stakeholder Coordination** (1-2 weeks)
- Business user training and change management
- IT operations handoff and knowledge transfer
- Legal and compliance sign-offs
- Executive approval for go-live

**6. Enterprise Process Overhead** (1 week)
- Change management board approvals
- Architecture review board sign-offs
- Security architecture review
- Capacity planning and resource allocation

**Real Example**: A "simple" user authentication feature took 12 weeks:
- Weeks 1-3: Integration with 3 legacy systems (each system took 1 week due to different protocols, data formats, and authentication methods)
- Weeks 4-5: Security review and compliance testing (penetration testing alone took 2 weeks)
- Weeks 6-7: Performance testing with 10,000 concurrent users (load testing and optimization)
- Weeks 8-9: User acceptance testing with 5 different business units (coordination and feedback cycles)
- Weeks 10-11: Production deployment and monitoring setup (environment provisioning and rollback procedures)
- Week 12: User training and change management (training sessions and documentation)

**The Hidden Time Sinks**:
- Waiting for security team availability (3 days)
- Database migration approval process (2 days)
- Business user testing feedback cycles (5 days)
- Production environment access delays (2 days)
- Compliance documentation review (3 days)

> **VP Insight**: "I've seen developers estimate 2 weeks for a feature that took 8 weeks. The code was done in 2 weeks, but the enterprise processes, integrations, and approvals took 6 weeks. Always factor in the full enterprise delivery cycle, not just development time."

### Traceability

Every story must trace back to an epic, every epic to a feature, every feature to a requirement.

### Re-estimation Control

When decomposition changes estimates:
1. Log the variance
2. Update the feature estimate
3. Escalate if >20% variance
4. Get approval for additional funding

> **Why This Matters**: Estimating at Feature level gives negotiation anchor; re-estimation during decomposition must be controlled.

## 5.10 External Integrations & Dependencies

### Why Integration Requirements Are Hard (And Often Missed)

Enterprise integrations are not “just connect the API.” They are moving contracts between organizations with different priorities, SLAs, data semantics, and release cadences. The difficulty rarely lives in a single call; it lives in the edges:

- Data that looks valid but means something different (BIN ranges, MCCs, time zones, currency rounding)
- AuthN/Z policies that change by environment (IP allowlists in UAT, mTLS in prod, SSO flows for admin portals)
- Partial failures and backpressure (rate-limits, intermittent 5xx, long-tail latency, duplicate webhooks)
- Version drift and undocumented behavior (v2.1 in docs, v2.2 in sandbox; optional fields that are actually mandatory)
- Legal/compliance constraints on test data (you can’t create the scenario you need, and masked data breaks referential integrity)

> VP Insight: “Integrations fail in the seams—where timeouts, retries, idempotency, and semantics meet organizational boundaries. Treat the seams as first‑class design problems.”

### Common Hidden Complications (Field Notes)

- Idempotency Isn’t Optional: Providers may retry your requests or deliver duplicate webhooks. Require idempotency keys and store replay protection for at least the provider’s documented (and undocumented) window.
- Time Is Political: Cutoff windows, settlement days, daylight‑saving shifts, and provider time zones create silent reconciliation gaps. Normalize timestamps and store both provider and system time.
- Errors Lie: A 200 may mean “accepted for processing” not “done.” A 400 may hide multiple validation failures. Design explicit state machines, not boolean flags.
- Sandboxes Aren’t Prod: Throttling, auth, and SLAs often differ. Assume optimistic sandbox results will degrade in production; budget for live‑traffic hardening.
- Schemas Drift: Providers add “optional” fields that become de‑facto required. Version your contracts and validate payloads at boundaries.
- Security Surprises: mTLS, key rotation, JWK freshness, and per‑environment certificates create fragile deployments. Automate rotation and fail closed with clear runbooks.

### Testing Integrations in Enterprises (What Works)

- Contract Tests at the Boundary: Define request/response schemas, error maps, and idempotency rules. Validate every change (your side and theirs) before promotion.
- Golden Datasets and Replayable Scenarios: Curate masked test data with end‑to‑end referential integrity. Build replay harnesses to reproduce edge cases (chargebacks, reversals, partial approvals).
- Latency/Chaos Injection: Inject 429, 5xx, slow responses, and dropped callbacks. Verify circuit breakers, retries with jittered backoff, and DLQ paths.
- Walking Skeletons First: Ship the simplest end‑to‑end path with deep observability (correlation IDs, structured logs, trace spans). Then widen scenarios.
- Environment Parity Plan: Document where sandbox differs from prod (auth, rate limits, data). Compensate with simulation and traffic‑shadowing where permissible.

### Operational Prerequisites (Before You Go Live)

- SLAs/SLOs: Document upstream SLAs and your SLOs; define error budgets and escalation paths.
- Rate Limits: Enforce client‑side budgets; detect and adapt (leaky bucket, token bucket). Negotiate increased quotas before traffic ramps.
- Idempotency & Ordering: Store idempotency keys; design for at‑least‑once delivery and out‑of‑order events.
- Observability: Correlation IDs across hops, business‑level metrics (auth approvals, settlement deltas), targeted alerts (not just CPU).
- Runbooks: Clear remediation steps for auth failures, schema changes, provider outages, and throttling.

### Readiness Checklist (RfP Gate for Integration Features)

A feature that integrates with an external system is RfP only when:

- Contract Defined: Endpoint list, methods, auth scheme, required/optional fields, error taxonomy, idempotency rules
- Non‑Functionals Agreed: SLAs, rate limits, payload sizes, max concurrency, maintenance windows
- Testability Secured: Sandbox access, test accounts/keys, seed data strategy, callback endpoints, replay harness
- Security Cleared: mTLS/keys/certs rotation, IP allowlists, secrets management, audit requirements
- Observability Ready: Correlation strategy, logs/metrics/traces, dashboards, alert thresholds
- Change Control: Versioning policy, deprecation timelines, contact/escalation info, provider status page

### Integration Readiness Visual Checklist (At‑a‑glance)

Use this quick checklist to decide if an integration Feature can move beyond RfP/Planned. Mark Yes/No with links to evidence.

- [ ] Contract defined (endpoints, auth, required/optional fields, error taxonomy, idempotency rules)
- [ ] Testability secured (sandbox access, keys/accounts, seed data, callback endpoints, replay harness)
- [ ] Non‑functionals agreed (SLAs, rate‑limits/quotas, payload sizes, concurrency, maintenance windows)
- [ ] Security cleared (mTLS/keys/certs rotation, IP allowlists, secrets management, audit requirements)
- [ ] Observability ready (correlation strategy, structured logs/metrics/traces, dashboards and alert thresholds)
- [ ] Change control in place (versioning/deprecation policy, provider status page, escalation contacts)
- [ ] Failure modes exercised (429/5xx/latency/dropped callbacks; retries with jitter; DLQ paths)
- [ ] Idempotency & ordering validated (keys stored; at‑least‑once + out‑of‑order handling)

Green to proceed: All mandatory checks above are Yes. Any No blocks transition to Planned/In Dev. Proceed only via recorded exception (Appendix M) with dated reversion and owner. See Appendix A/B for widgets/alerts to surface readiness.

> VP Insight: “If you can’t test it independently, you can’t own it in production. Make testability a contractual requirement.”

### Example: Card Network Settlement Integration (What We Actually Faced)

- Hidden Spec: Cutoff at 21:00 CET, but file timestamps in UTC with DST anomalies. Fix: store provider and normalized times; reconcile by provider clock.
- Throttling Reality: 429 limits undocumented in sandbox; production enforced 200 req/min bursts. Fix: client‑side token bucket and adaptive backoff.
- Idempotency Gap: Re‑posts after network brownouts created duplicate settlements. Fix: checksum + idempotency keys, reconciliation ledger, replay‑safe consumers.
- Schema Drift: “optional” surcharge field became required in prod for EU merchants. Fix: strict contract validation and dark‑launch schema flags.
- Testing Barrier: No real multi‑currency data in sandbox. Fix: provider‑approved simulators + golden test fixtures verified end‑to‑end formatting and rounding.

### Jira Instrumentation (Make the Risk Visible)

Labels:
- `integration-risk`, `contract-missing`, `sandbox-unstable`, `rate-limit`, `idempotency-gap`, `version-drift`

Custom Fields:
- Upstream SLA (ms/%), Rate Limit (req/min), Auth Method (mTLS/OAuth), Contract Version, Idempotency Policy

Definition of Done (integration stories):
- Contract tests pass; chaos/latency scenarios verified; runbooks published; dashboards/alerts live; rollback and feature‑flag strategy validated.

## 5.11 Commercial Implications

### Requirement Decomposition Costs

When the Delivery Team performs requirement decomposition, this is significant billable work that includes:

- **Solution Architecture**: Technical design and feasibility analysis
- **Stakeholder Interviews**: Understanding business context and constraints
- **Technical Analysis**: Integration points, dependencies, and complexity assessment
- **Feature Definition**: Breaking down requirements into implementable features
- **Acceptance Criteria Development**: Working with Customer Team to define testable criteria

**Real Example**: A requirement for "real-time fraud detection" required 3 weeks of decomposition work:
- Week 1: Stakeholder interviews with risk team, compliance team, and operations
- Week 2: Technical analysis of ML algorithms, data sources, and integration points
- Week 3: Feature definition and acceptance criteria development

This was billed as a separate phase before development began.

### Change Impact

Every requirement change has cost implications:
- **Discovery**: Usually no additional cost
- **Clarification**: Usually no additional cost
- **Emergence**: Usually additional cost

### Funding Responsibility

- **Client owns**: New requirements, scope changes, requirement decomposition
- **Studio owns**: Discovery, clarification, technical debt

### Real Example

**Client says**: "Add mobile wallet support" (Emergence)
**Studio says**: "That's a new requirement. Here's the estimate: 3 weeks, $50K"
**Client says**: "Can you absorb it?"
**Studio says**: "No, that's outside our scope. We need a change request."

> **From the Field**: "We delivered the change gratis once — next time the client assumed we'd always absorb."

## 5.12 Dashboards & Alerts

### Audience Views

- Steering (Executive): Flow health, risk exposure, delivery confidence
- Program (DM/Studio Owner): Maturity, bottlenecks, blockers, variance
- Team (Squads): Today’s risks, readiness gaps, testability status

### Core Flow Metrics (Requirements → Features)

- % MAR: Requirements meeting minimal acceptance (intent, boundaries, AC seed)
- % Decomposed: Requirements broken into subsystem‑scoped features
- % RfP: Requirements with Customer sign‑off on features and AC
- Time in State: Median/95th time in In Progress, Decomposed, RfP
- Features Pending Sign‑off: Count and aging (label: `features-pending-signoff`)
- Decomposition Blocked: Count and median days blocked (label: `decomposition-blocked`)
- AC Coverage: % of features with complete, testable AC (for RfP items)

### Effort‑Based Delivery Progress

- Requirement Progress %: (Completed Story Points / Total Story Points)
- Feature Acceptance Rate: Features accepted per week (trend)
- Stagnation Detector: No progress change in ≥2 sprints (flag)
- Estimate Variance: Features with >20% re‑estimation (count, list)

### Integration Readiness & Risk

- Contract Completeness: Missing items (labels: `contract-missing`, `version-drift`)
- Testability Readiness: Sandbox accounts/keys/callbacks present (Yes/No)
- Rate‑Limit Incidents: 429s per day (thresholded)
- Idempotency Gaps: Flags present (label: `idempotency-gap`) – block go‑live
- Sandbox Stability: Incidents/week (label: `sandbox-unstable`)
- Upstream SLA vs SLO: P95 latency/availability deltas
- Chaos/Latency Coverage: Scenarios verified (429, 5xx, slow, dropped callbacks)

### Dependency & Volatility

- Dependency Risk: High‑risk dependencies per requirement (count, aging)
- Volatility: Weekly requirement/feature churn rate (% change in AC/scope)
- Blocker Aging: Median/95th age of blockers on critical path

### Readiness Flags (Definition of Done – Integration Features)

- Observability Ready: Correlation IDs, dashboards, alerts (Yes/No)
- Runbooks Published: Auth failures, schema changes, throttling, outage (Yes/No)
- Rollback/FF Strategy Validated: Dark launch/feature flags tested (Yes/No)

### Alerts (Good Defaults)

- RfP < 70% for target increment window → Planning risk (Program/Steering)
- `features-pending-signoff` aging > 5 days on any critical requirement → Escalate
- `decomposition-blocked` > 3 days median → Remove blocker or re‑scope
- AC Coverage < 90% on RfP set → Gate planning
- Requirement Progress % unchanged across 2 sprints → Review plan/risks
- Estimate Variance > 30% on ≥3 features in a requirement → Re‑baseline
- Any `contract-missing`, `idempotency-gap`, or `sandbox-unstable` on items moving to Planned → Block transition
- Rate‑limit incidents > 50/day or SLA breach > 1 hour → Incident + provider escalation

### Example Boards

- Steering: %RfP, Delivery Confidence (progress % distribution), Integration Risk Heatmap (labels), Top 10 Aging Blockers
- Program: Time‑in‑State trends, Sign‑off aging, Variance table, Volatility trend, Readiness flags
- Team: Today’s blockers, AC coverage by feature, Testability checklist, Chaos coverage, DoD flags

### Sample Queries (Jira)

- Requirements in Progress > 14 days:
  - project = PROJ AND type = Requirement AND status = "In Progress" AND updated < -14d
- Pending Customer sign‑off:
  - project = PROJ AND labels = "features-pending-signoff"
- Integration readiness blockers:
  - project = PROJ AND labels in ("contract-missing","idempotency-gap","sandbox-unstable")
- Stalled progress (no story points change in 2 sprints):
  - project = PROJ AND type = Requirement AND "Progress Percentage" <= previousSprint()

> Caution: Pick 8–12 signals per audience. Too many widgets dilute attention and mask risk.

## How to Live These Practices

### 1. Don't Ask for Perfect Requirements — Ask for the Minimal

Recognize that waiting for complete clarity is often a trap. Push for minimally enough to move forward, with guards for change.

**Example**: "We don't need every detail, but we need enough to estimate and design. We can refine as we learn."

### 2. Refine AC with the Customer — Not Impose Them

Use collaborative questions rather than dictating. Share the cost/risk perspective.

**Example**: "How would we test that case?" instead of "You must write better AC."

### 3. Expect Estimates to Be Revisable — But Manage Variance

When decomposition changes estimates, trigger a variance review. Don't let silent overrun creep through.

**Example**: "Our initial estimate was 2 weeks, but decomposition shows 3 weeks. Here's the variance analysis."

### 4. Treat Integrations as First-Class Risks

Don't let "just an interface" slip through; always consider auth, data, error modes, SLA, versioning.

**Example**: "This isn't just an API call. We need to handle authentication, data mapping, error handling, and SLA monitoring."

### 5. Evolve Documentation, Don't Replace It

Requirements will change. Use living artifacts rather than static docs.

**Example**: Use wiki pages with version history instead of Word documents.

### 6. Link Everything to Tests & Traceability

If a requirement, feature, or story lacks trace to a test case, surface that as a gap.

**Example**: "This story has no test case. How will we know it's done?"

### 7. Expose Maturity Trends, Not Instantaneous Snapshots

Use trend charts rather than just static counts. That gives early warning.

**Example**: Show RfP percentage over time, not just current count.

### 8. Push Back Politely, But Firmly, When Changes Arise Late

Ask "Was this known at RfP?" Link to governance. Log change, show delta, escalate if needed.

**Example**: "This change wasn't in the original requirement. Here's the impact analysis and cost estimate."

### 10. Distinguish Between the Two Decomposition Steps

**Requirement Decomposition** (Requirement → Features) is different from **Feature Decomposition** (Feature → Epics → Stories).

**Example**: "We need to decompose your requirement into features first (2 weeks, $25K), then we can decompose those features into epics and stories for development planning."

### 11. Bill for Requirement Decomposition Work

When the Studio performs requirement decomposition, this is significant billable work. Don't absorb it as "pre-work."

**Example**: "We need 2 weeks to decompose this requirement into features. This involves stakeholder interviews, technical analysis, and solution design. Here's the estimate: $25K."

### 12. Require Design Sign-off Before Feature Decomposition

Never decompose features into epics/stories without design documentation and impact assessment sign-off.

**Example**: "Before we can break this feature into epics, we need your sign-off on the design document and impact assessment. This ensures we're building what you actually need."

### 13. Get Customer Sign-off to Move from Decomposed to RfP

A requirement only becomes RfP when the Customer Team signs off on all feature definitions and acceptance criteria.

**Example**: "We've decomposed your requirement into 3 features. We need your sign-off on each feature's definition and acceptance criteria before we can move to development planning."

### 14. Track Partial Delivery Progress

Monitor both requirement-level and feature-level completion to show incremental value delivery.

**Example**: "We've delivered 2 of 3 features for fraud detection (67% complete). The ML scoring API and real-time alerts are ready for use. The audit logging feature will be ready next sprint."

### 15. Use Effort-Based Progress Tracking

Don't rely on feature count alone. Use story points or effort hours for accurate progress tracking.

**Example**: "We've completed 67 story points out of 100 (67% complete). The ML scoring API (40 points) and real-time alerts (27 points) are accepted. The audit logging feature (33 points) is in progress."

### 9. Use Dashboards as Conversational Anchors, Not Power Plays

When showing backlog risk or AC gaps, frame it as shared visibility. Don't weaponize metrics.

**Example**: "Let's look at this together" instead of "You're not meeting our standards."

## The Bottom Line

Requirements are the foundation of everything. Master them, and many other problems become smaller. Get them wrong, and everything else becomes harder.

Use these practices to build a shared understanding with your client, manage change effectively, and deliver what they actually need.

> **VP Insight**: "I've seen teams without requirement discipline get pushed around by every stakeholder request. I've seen teams with requirement discipline stand firm and deliver better results. Requirements discipline is your armor and your compass."