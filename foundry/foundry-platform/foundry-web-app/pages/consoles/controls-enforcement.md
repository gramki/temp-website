# Controls & Enforcement Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/controls`

**Group:** Governance

**Purpose:** View Governance Policies, Policy Controls, Control Objectives, Control Objective Indicators, thresholds, effective ownership, evidence requirements, and Governance Enforcement outcomes.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Control Objective** | Required governance outcome: what must hold. |
| **Control Objective Indicator** | Metric, evidence artifact, dashboard field, register state, or checklist item used to evaluate the objective. |
| **Control Objective Threshold** | Pass/warn/fail boundary for an indicator at a scope. |
| **Governance Enforcement** | Orchestration item that evaluates controls against an item, transition, artifact, evidence, or state. |
| **Debt + Catch-Up** | Temporary deviation with remediation plan and due date. |
| **Exception / Waiver** | Approved non-applicability, alternate control, or bounded bypass. |

---

## Page Sections

### 1. Control Catalog

| Column | Description |
|--------|-------------|
| **Control ID** | Policy/control identifier |
| **Control Objective** | Required outcome |
| **Indicators** | Indicators used to evaluate the objective |
| **Thresholds** | Effective thresholds after inheritance |
| **Scope** | Foundry / Workspace / Workbench / Track / transition / artifact |
| **Enforcement mode** | Block, warn, allow-with-debt, allow-with-risk, require-exception |
| **Evidence requirement** | Required evidence |
| **Effective Control Owner** | Resolved accountable role |
| **Approvers** | Debt / exception / sign-off approvers |
| **Inheritance source** | Foundry, Workspace, or Workbench definition |

### 2. Enforcement Queue

| Status | Description |
|--------|-------------|
| **Triggered** | Enforcement item created |
| **Evaluating** | Control evaluation in progress |
| **Awaiting evidence** | Required evidence missing |
| **Passed** | Control satisfied |
| **Warning** | Non-blocking concern |
| **Hard fail** | Below minimum / cannot proceed |
| **Debt required** | Debt + Catch-Up needed |
| **Exception required** | Exception / Waiver needed |
| **Routed** | Follow-up register or Work Order created |
| **Closed** | Enforcement complete |

### 3. Enforcement Detail

| Section | Description |
|---------|-------------|
| **Target** | Orchestration item, Work Order, transition, artifact, evidence bundle, or state |
| **Control Objective** | Required outcome |
| **Indicators** | Current values and evidence |
| **Thresholds** | Minimum and target/enforcement boundaries |
| **Evaluation result** | Pass, warning, hard fail, debt required, exception required |
| **Owner / Approver** | Effective Control Owner and Approver |
| **Outcome path** | Block, warn, Debt + Catch-Up, Exception / Waiver |
| **Audit trail** | Events, actors, decisions, evidence |

### 4. Control Objective Examples

| Domain | Control Objective | Indicator |
|--------|-------------------|-----------|
| Build quality | Build evidence supports safe release | coverage %, test pass rate, critical bugs |
| Release readiness | Product Delivery is ready to publish | QA evidence, release approval, open debt |
| Discovery | Product decision is accountable | PDR status, PM alignment, evidence completeness |
| Governance | Ritual was completed | required inputs present, outputs recorded |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Evaluate control | System / Governance | Run enforcement |
| Attach evidence | Evidence Owner / Participant | Add evidence for indicator |
| Request Debt + Catch-Up | Manager / Control Owner | Request temporary deviation with remediation plan |
| Approve Debt + Catch-Up | Approver | Approve debt and repayment plan |
| Request Exception / Waiver | Manager / Control Owner | Request bounded bypass or alternate control |
| Approve Exception / Waiver | Approver | Approve with rationale, scope, expiry |
| Create remediation Work Order | Control Owner / Governance | Create follow-up work |
| Create Evolve Case | Governance / Evolve | Improve policy/control/dashboard/playbook |

---

## Phase Position

| Maturity | Scope |
|----------|-------|
| Phase 1 | Enforcement queue, control detail, debt/exception request and approval references |
| Phase 2 | Control catalog, thresholds, evidence requirements |
| Phase 3 | Full inheritance, effective owner resolution, advanced control analytics |

---

## Related Consoles

- **Governance Overview** — attention queue and health summary
- **Registers** — debt, exceptions, risks, compliance, findings
- **Quality Controls** — build/release quality specialization
- **Governance Admin** — control configuration and inheritance
