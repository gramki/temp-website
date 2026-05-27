# Governance Teams — Jobs to be Done

**Primary Workspace:** Governance

**Role:** Validate transitions, enforce policies, capture evidence, produce audit trails, and provide management analytics.

---

## Primary Jobs — Governance Execution

### J1. Review Governance Scenarios triggered at gates
**When** a gate is triggered (Work Order transition, release, etc.)  
**I want to** see the Governance Scenario and its inputs  
**So that** I can validate the transition

**Acceptance Criteria:**
- Gate trigger notification
- Governance Scenario details
- Input artifacts/evidence
- Policy checklist
- Historical precedents

---

### J2. Validate transition evidence
**When** reviewing a gate  
**I want to** verify that all required evidence is present and valid  
**So that** compliance is assured

**Acceptance Criteria:**
- Evidence checklist
- Evidence artifact viewer
- Completeness indicators
- Validation actions (verify, flag, reject)
- Governance Evidence Map in PI Console showing PDR → Product Intent → Governance Events → PSD Approval → QA Evidence → Release Evidence
- Distinguish Delivery Product Intents from Discovery Support, Technical Validation, Internal / Enabling, and Operational Enablement intents; Build evidence for non-delivery intents does not substitute for Customer Release Intent fulfillment evidence

---

### J3. Approve/reject gate transitions
**When** evidence is reviewed  
**I want to** approve or reject the transition  
**So that** work proceeds or is blocked appropriately

**Acceptance Criteria:**
- Approve/reject/request-more actions
- Rejection reason field
- Conditional approval option
- Audit trail capture

---

### J4. Investigate blocked Work Orders
**When** a Work Order is stuck at a gate  
**I want to** understand why and what's needed  
**So that** I can help unblock it

**Acceptance Criteria:**
- Blocker details
- Missing evidence list
- Policy failure reasons
- Suggested remediation
- Contact responsible party

---

### J5. Generate compliance and audit reports
**When** reporting is required (audit, management review)  
**I want to** generate compliance reports  
**So that** I can demonstrate adherence

**Acceptance Criteria:**
- Report templates (compliance, audit, management)
- Date range selection
- Workbench/Track filters
- Export formats (PDF, CSV)
- Scheduled report option

---

### J6. Monitor policy adherence across Workbenches
**When** overseeing governance health  
**I want to** see policy adherence metrics across all Workbenches  
**So that** I can identify problem areas

**Acceptance Criteria:**
- Policy adherence dashboard
- Violation trends
- Workbench comparison
- Drill-down to violations

---

## Primary Jobs — Analytics & Reporting

### J7. View work analytics
**When** assessing delivery performance  
**I want to** see throughput, cycle time, WIP, and lead time  
**So that** I can identify bottlenecks

**Acceptance Criteria:**
- Work analytics dashboard
- Throughput by Track/Workspace
- Cycle time trends
- WIP limits and actuals
- Lead time distribution

---

### J8. View human analytics
**When** assessing team performance  
**I want to** see task completion rates, time-to-pickup, capacity  
**So that** I can optimize team allocation

**Acceptance Criteria:**
- Human analytics dashboard
- Task completion by builder
- Time-to-pickup trends
- Capacity utilization
- Skill utilization

---

### J9. View agent analytics
**When** assessing agent performance  
**I want to** see efficiency, effectiveness, and cost metrics  
**So that** I can optimize agent use

**Acceptance Criteria:**
- Agent analytics dashboard
- Tasks per agent
- Time per task
- Quality of outputs (rework rate)
- Cost per Work Order
- Skill coverage gaps

---

### J10. Track say/do metrics
**When** assessing predictability  
**I want to** see planned vs delivered metrics  
**So that** I can improve estimation

**Acceptance Criteria:**
- Say/do dashboard
- Commitment vs delivery by sprint/release
- Trend over time
- Root cause for misses

---

### J11. Monitor quality trends
**When** assessing quality trajectory  
**I want to** see defect trends, BQI, and gate pass rates  
**So that** I can identify quality issues

**Acceptance Criteria:**
- Quality trends dashboard
- Defect open/close rates
- Control Objective Indicator trends (including Build Quality Indicators)
- Gate pass/fail rates
- Severity distribution

---

### J12. Generate management dashboards
**When** leadership needs visibility  
**I want to** provide executive dashboards  
**So that** management is informed

**Acceptance Criteria:**
- Executive summary dashboard
- Key metrics (velocity, quality, cost)
- Risk indicators
- Drill-down capability
- Export/share options

---

## Supporting Jobs

### J13. Configure governance policies
**When** policies need to change  
**I want to** update policy definitions  
**So that** governance evolves

*(Note: May require admin role or Scenario Authoring access)*

---

### J14. Search audit trail
**When** investigating past decisions  
**I want to** search the audit trail by Work Order, time, actor  
**So that** I can trace what happened

---

### J15. Export compliance reports
**When** external reporting is needed  
**I want to** export reports in standard formats  
**So that** I can share with auditors/regulators

---

### J16. Review historical gate decisions
**When** understanding precedent  
**I want to** see past gate decisions for similar Work Orders  
**So that** I can be consistent

---

## Open Questions

- How are Governance Scenarios authored and updated?
- What's the relationship between Governance Workspace and Governance Track?
- How are DORA-style metrics integrated?
- What alerting/notification patterns apply for governance violations?
