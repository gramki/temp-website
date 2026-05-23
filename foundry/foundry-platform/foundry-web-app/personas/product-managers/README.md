# Product Managers — Jobs to be Done

**Primary Workspace:** Product Specification

**Role:** Define what to build — translate signals into Product Intent and specifications, prioritize work, track product evolution.

---

## Primary Jobs

### J1. Create new Product Intent from signals/feedback
**When** a signal arrives (customer feedback, market insight, strategic directive)  
**I want to** create a new Product Intent and capture its context  
**So that** it enters the product evolution flow

**Acceptance Criteria:**
- Create Product Intent form
- Link to source signal (FIR, feedback, request)
- Assign to Workbench
- Initial prioritization
- Route to specification scenario

---

### J2. Translate Product Intent into specifications (PSDs)
**When** a Product Intent needs elaboration  
**I want to** write or refine the Product Specification Document  
**So that** UX and Development can act on it

**Acceptance Criteria:**
- PSD editor with templates
- Agent-assisted drafting
- Link to Product Intent
- Acceptance criteria definition
- Ready-for-design transition

---

### J3. Prioritize and sequence Work Orders in the backlog
**When** multiple Work Orders compete for resources  
**I want to** set priorities and sequence  
**So that** teams work on the right things

**Acceptance Criteria:**
- Backlog view with drag-drop ordering
- Priority levels (critical, high, medium, low)
- Dependency visualization
- Capacity awareness
- Bulk update capabilities

---

### J4. Review Work Order progress across all Workspaces
**When** I need to know delivery status  
**I want to** see all Work Orders for my Product Intent across Workspaces  
**So that** I can identify blockers and risks

**Acceptance Criteria:**
- Cross-workspace view filtered by Product Intent
- Status by Workspace (spec, design, dev, QA, release)
- Time in each stage
- Blocker indicators
- Drill-down to Work Order details

---

### J5. Approve/reject spec transitions (governance triggers)
**When** a spec is ready to move to design or development  
**I want to** review and approve the transition  
**So that** only ready work moves forward

**Acceptance Criteria:**
- Transition request notification
- Spec review with checklist
- Approve/reject/request-changes actions
- Comments/feedback field
- Audit trail

---

### J6. Refine specifications based on feedback
**When** UX, Dev, or QA raises questions or issues  
**I want to** update the specification  
**So that** the work proceeds with clarity

**Acceptance Criteria:**
- Feedback notifications
- Edit spec in context
- Version history
- Link changes to feedback source

---

## Supporting Jobs

### J7. View Workbench-level KPIs
**When** I need to assess product health  
**I want to** see velocity, say/do, quality, and cycle time metrics  
**So that** I can identify improvement areas

**Acceptance Criteria:**
- Dashboard with key metrics
- Trend charts
- Comparison to targets
- Drill-down to contributing Work Orders

---

### J8. Track Product evolution over time
**When** I need to understand product history  
**I want to** see the evolution of Product Intents and their outcomes  
**So that** I can make informed decisions

---

### J9. Access feedback repository (FIRs, customer signals)
**When** I need raw customer input  
**I want to** browse and search the Feedback repository  
**So that** I can ground Product Intent in real signals

---

### J10. Compare planned vs actual delivery
**When** assessing predictability  
**I want to** see what was planned vs what was delivered  
**So that** I can improve estimation

---

### J11. Manage dependencies between Work Orders
**When** Work Orders depend on each other  
**I want to** visualize and manage dependencies  
**So that** sequencing is correct

---

### J12. Search and filter Work Orders
**When** I need to find specific work  
**I want to** search by status, track, workspace, date, assignee  
**So that** I can locate it quickly

---

## Open Questions

- How do Product Managers interact with the Foundry IDE vs. web app?
- What's the handoff between Product Specification and UX Design Workspaces?
- How are agent-generated spec drafts reviewed and approved?
