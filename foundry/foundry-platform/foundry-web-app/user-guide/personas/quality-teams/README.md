# Quality Teams — Jobs to be Done

**Primary Workspace:** QA

**Role:** Verify and validate what is built — ensure quality through testing, defect reporting, and evidence generation.

## Prerequisites

- Access to a Workbench with QA Workspace membership
- Familiarity with test management tools (TestRail integration if configured)
- Understanding of [Work Order lifecycle](../../../../work-order-runtime/user-guide/work-order-lifecycle.md)

---

## Primary Jobs

### J1. View QA-related Work Orders and Human Tasks
**When** I start my work session  
**I want to** see all QA Work Orders and Human Tasks assigned to me  
**So that** I can prioritize testing work

**Acceptance Criteria:**
- List of QA Work Orders with status, priority
- Filter by Workbench, Track, status
- Human Tasks queue with due dates
- Badge count of pending tasks

---

### J2. Execute verification scenarios (manual test tasks)
**When** a Human Task requires manual testing  
**I want to** execute the test, record results, and mark complete  
**So that** verification evidence is captured

**Acceptance Criteria:**
- Test steps display
- Pass/fail/blocked recording per step
- Notes/observations field
- Screenshot/evidence attachment
- Link to test case in Quality repository

---

### J3. Review agent-generated test results
**When** an agent executes automated tests  
**I want to** review the results, failures, and coverage  
**So that** I can validate quality and investigate failures

**Acceptance Criteria:**
- Test run summary (pass/fail/skip counts)
- Failure details with logs
- Coverage metrics
- Comparison to previous runs
- Approve/flag-for-review actions

---

### J4. Report defects
**When** I find a defect  
**I want to** create a defect Work Order routed to Development  
**So that** it gets fixed

**Acceptance Criteria:**
- Defect creation form
- Severity/priority classification
- Steps to reproduce
- Expected vs actual
- Attach screenshots/logs
- Link to originating Work Order
- Auto-route to Development Workspace

---

### J5. Validate quality evidence before release gates
**When** a release gate requires quality sign-off  
**I want to** review all quality evidence and approve/reject  
**So that** only quality-verified work proceeds

**Acceptance Criteria:**
- Quality evidence checklist
- Test coverage summary
- Defect status (open/closed)
- BQI (Build Quality Indicator) display
- Approve/reject actions
- Comments field

---

### J6. Track test coverage by feature/Workbench
**When** I need to assess coverage gaps  
**I want to** see test coverage mapped to features and Workbenches  
**So that** I can identify untested areas

**Acceptance Criteria:**
- Coverage dashboard by Workbench
- Feature-to-test mapping
- Coverage trends over time
- Gap identification

---

## Supporting Jobs

### J7. Access Quality repository
**When** I need test cases, verification results, or test plans  
**I want to** browse and search the Quality repository  
**So that** I can find relevant artifacts

---

### J8. View historical defect trends
**When** assessing quality trajectory  
**I want to** see defect trends over time  
**So that** I can identify patterns

---

### J9. Monitor build quality indicators (BQI)
**When** reviewing build readiness  
**I want to** see BQI metrics  
**So that** I know if quality gates will pass

---

### J10. Review acceptance criteria traceability
**When** validating completeness  
**I want to** see acceptance criteria mapped to test cases  
**So that** I know everything is covered

---

### J11. Search Work Orders by test status
**When** looking for specific test work  
**I want to** filter Work Orders by test status  
**So that** I can find them quickly

---

### J12. Collaborate with Development on defect resolution
**When** a defect needs clarification  
**I want to** comment on the defect Work Order  
**So that** developers have the information they need

---

## Open Questions

- How are agent-generated tests reviewed for quality?
- What's the workflow for test case authoring (manual vs agent-assisted)?
- How does QA interact with Release for pre-release verification?
