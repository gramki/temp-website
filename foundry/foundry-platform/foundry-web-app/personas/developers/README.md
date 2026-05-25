# Developers — Jobs to be Done

**Primary Workspace:** Development

**Role:** Build the specified solution — implement features, fix defects, write code.

---

## Primary Jobs

### J1. View my Work Orders and Human Tasks queue
**When** I start my work session  
**I want to** see all Work Orders assigned to me and the Human Tasks waiting on me  
**So that** I can prioritize what to work on

**Acceptance Criteria:**
- List of Work Orders with status, priority, due date
- Filter by Track, status, age
- Sort by priority, date, or custom
- Badge count of pending Human Tasks

---

### J2. Understand context for the work
**When** I pick up a Work Order  
**I want to** see the full context — Product Intent, specifications, design decisions, prior work  
**So that** I don't have to ask others or search for information

**Acceptance Criteria:**
- Parent orchestration-item graph visualization (Product Intent for Build work)
- Link to originating spec (PSD)
- Link to related design artifacts
- Prior Work Orders on this Product Intent
- Agent-provided context summary

---

### J3. Complete assigned Human Tasks
**When** I have a Human Task to do  
**I want to** mark it complete, add notes, attach artifacts  
**So that** the Work Order can progress

**Acceptance Criteria:**
- Task details with acceptance criteria
- Complete/reject actions
- Notes/comments field
- Artifact attachment
- Transition to next task or agent

---

### J4. Monitor agent progress on Agent Tasks
**When** an agent is working on Tasks in my Work Order  
**I want to** see its progress, outputs, and any blockers  
**So that** I can intervene if needed

**Acceptance Criteria:**
- Real-time progress indicator
- Agent output stream (code, decisions, artifacts)
- Blocker alerts
- Ability to pause/resume agent
- Human takeover option

---

### J5. Add or refine context in Work Orders
**When** I discover missing or incorrect context  
**I want to** update the Work Order's context  
**So that** agents and other humans have accurate information

**Acceptance Criteria:**
- Edit context fields
- Add notes/comments
- Attach files or links
- Context change audit trail

---

### J6. Review and act on agent-generated code/artifacts
**When** an agent produces code or artifacts  
**I want to** review, approve, request changes, or reject  
**So that** quality is maintained

**Acceptance Criteria:**
- Diff view for code changes
- Approve/reject/request-changes actions
- Inline comments
- Link to CI results

---

### J7. Navigate to related Work Orders
**When** I need to understand upstream or downstream work  
**I want to** navigate to related Work Orders in other Workspaces  
**So that** I can see the full picture

**Acceptance Criteria:**
- Links to spec Work Order (Product Specification)
- Links to design Work Order (UX Design)
- Links to QA Work Orders
- Links to Release Work Orders
- Parent orchestration-item graph navigation

---

## Supporting Jobs

### J8. Access code repositories
**When** I need to view or work with code  
**I want to** navigate to the relevant repository  
**So that** I can see the codebase context

---

### J9. View build/test status
**When** I've made changes  
**I want to** see CI status  
**So that** I know if my work is ready

---

### J10. See history of Work Orders I've worked on
**When** I need to recall past work  
**I want to** search my Work Order history  
**So that** I can reference or learn from it

---

### J11. Understand why a Work Order is blocked
**When** a Work Order isn't progressing  
**I want to** see the blocker reason  
**So that** I can unblock it or escalate

---

### J12. Escalate or reassign tasks
**When** I can't complete a task  
**I want to** escalate or reassign it  
**So that** work continues

---

### J13. Search past Work Orders and decisions
**When** I need to find prior art  
**I want to** search across Work Orders, specs, code, decisions  
**So that** I can reuse or learn

---

## Open Questions

- How does the web app integrate with the Foundry IDE? (context sync, deep links)
- What's the relationship between web app task completion and IDE-based work?
- How are code reviews surfaced — web app, IDE, or both?
