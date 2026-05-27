# Product Managers — Jobs to be Done

**Primary Workspace:** Product Specification

**Role:** Define what to build — translate Signals and Discovery Cases into Product Decisions (PDRs), authorize evolution as typed Product Intent, refine specifications (PSDs) under that intent, prioritize work, and track product evolution.

---

## Primary Jobs

### J1. Create Product Intent from a Product Decision (PDR)
**When** a Go or Pivot PDR is finalized
**I want to** create a Product Intent anchored to that decision and its evidence
**So that** it enters the ACE Product Evolution Cycle

**Acceptance Criteria:**
- Create Product Intent from linked PDR
- Set Product Intent purpose (Evolution / Delivery, Discovery Support, Technical Validation, Internal / Enabling, Operational Enablement, Release Renewal)
- Link Customer Release Intent when purpose is Delivery or Release Renewal
- Surface "not customer-committed delivery" when purpose is not Delivery or Release Renewal
- Preserve traceability to source Signals and Ideas
- Capture decision rationale and evidence references
- Assign to Workbench
- Initial prioritization against Objective, Initiative, KRA, SLA, or Customer Promise context
- Route to Product Specification Workspace for PSD refinement scenarios

---

### J2. Refine Product Intent into specifications (PSDs)
**When** a Product Intent has entered the Product Specification Workspace
**I want to** write or refine PSDs under that intent
**So that** UX and Development can act on an approved specification contract

**Acceptance Criteria:**
- PSD editor with templates
- Agent-assisted drafting
- Link to Product Intent
- Reference the authorizing PDR
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

### J7. Manage Strategy Frame
**When** strategic direction or commitments change
**I want to** update Objectives, KRAs, SLAs, Initiatives, Customer Release Intents, and strategic constraints
**So that** Product Intent formation is grounded in decision-grade strategy

**Acceptance Criteria:**
- Clearly distinguish strategy from raw Signals, tasks, bugs, incidents, and PSD body content
- Link strategy items to Product Decisions and Product Intents
- Capture customer-committed deadlines as strategic constraints when they shape product evolution

---

### J8. Monitor Product Intent funnel
**When** Product Intent is forming across many sources
**I want to** see the funnel from Strategy / Signals / Commitments / Release Learnings through Discovery Case, PDR, typed Product Intent, PSD refinement when required, and execution
**So that** I can see where product evolution is forming, blocked, or stale

---

### J9. Use Traceability Maps for stakeholder questions
**When** I need to explain why intent exists or what it affects
**I want to** select the appropriate Traceability Map
**So that** I can answer executive, delivery, governance, customer-value, or vendor-value questions without arbitrary graph exploration

---

### J10. Manage Discovery Cases
**When** a product-relevant question needs grouped investigation
**I want to** open and track a Discovery Case through evidence to PDR or routing outcome
**So that** discovery progress is visible before Product Intent is formed

**Acceptance Criteria:**
- Create Discovery Case without requiring a Signal
- Capture origin type and originating function
- Track participating functions and accountable PM
- Link evidence, PDR, Product Intent, Modeling Task, or cross-track routing outcome

---

### J11. View Workbench-level KPIs
**When** I need to assess product health  
**I want to** see velocity, say/do, quality, and cycle time metrics  
**So that** I can identify improvement areas

**Acceptance Criteria:**
- Dashboard with key metrics
- Trend charts
- Comparison to targets
- Drill-down to contributing Work Orders

---

### J12. Track Product evolution over time
**When** I need to understand product history  
**I want to** see the evolution of Product Intents and their outcomes  
**So that** I can make informed decisions

---

### J13. Access feedback repository (FIRs, customer signals)
**When** I need raw customer input  
**I want to** browse and search the Feedback repository  
**So that** I can ground Product Intent in real signals

---

### J14. Compare planned vs actual delivery
**When** assessing predictability  
**I want to** see what was planned vs what was delivered  
**So that** I can improve estimation

---

### J15. Manage dependencies between Work Orders
**When** Work Orders depend on each other  
**I want to** visualize and manage dependencies  
**So that** sequencing is correct

---

### J16. Search and filter Work Orders
**When** I need to find specific work  
**I want to** search by status, track, workspace, date, assignee  
**So that** I can locate it quickly

---

## Open Questions

- How do Product Managers interact with the Foundry IDE vs. web app?
- What's the handoff between Product Specification and UX Design Workspaces?
- How are agent-generated spec drafts reviewed and approved?
