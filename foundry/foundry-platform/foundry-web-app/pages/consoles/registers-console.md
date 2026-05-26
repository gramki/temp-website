# Registers Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/registers`

**Group:** Governance

**Purpose:** Unified view of governance register artifacts: risks, debt, exceptions/waivers, compliance obligations, deferred obligations, and kudos/recognition.

---

## Register Tabs

| Tab | Purpose |
|-----|---------|
| **Risks** | Risk Register entries and mitigation status |
| **Debt + Catch-Up** | Approved temporary deviations and repayment plans |
| **Exceptions / Waivers** | Approved policy deviations, alternate controls, and bounded bypasses |
| **Compliance** | Compliance obligations and audit readiness |
| **Deferred Obligations** | Obligations allowed to proceed with later remediation |
| **Kudos / Recognition** | Positive evidence-backed recognition |

---

## Common Register Entry Fields

| Field | Description |
|-------|-------------|
| Entry ID | Unique register entry |
| Type | Risk, debt, exception, compliance, deferred obligation, recognition |
| Source | Governance Ritual, Governance Enforcement, Work Order, Product Intent, Discovery Case, etc. |
| Linked item | Orchestration item or Work Order affected |
| Owner | Accountable owner for risk/debt/compliance/remediation |
| Approver | Approver for debt, exception, waiver, risk acceptance |
| Severity | Critical, High, Medium, Low where applicable |
| Status | Open, active, mitigating, overdue, closed, expired |
| Due / expiry | Due date or exception expiry |
| Evidence | Evidence bundles or audit links |
| Work links | Remediation Work Orders or Evolve Cases |
| Audit history | Changes, decisions, approvals |

## Register-specific Fields

### Debt + Catch-Up

- Catch-Up Plan
- repayment date
- repayment evidence
- debt age
- overdue status
- related Control Objective / Indicator

### Exceptions / Waivers

- policy/control waived
- rationale
- approver
- expiry
- conditions
- compensating control

### Risks

- probability
- impact
- mitigation
- risk acceptance status

### Compliance

- control obligation
- audit period
- compliance status
- evidence bundle

### Kudos / Recognition

- recognized person/team/agent
- reason
- recognition type
- evidence reference
- reusable practice candidate

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Create entry | Governance / System | Create register entry from ritual or enforcement |
| Update status | Owner / Governance | Update progress |
| Assign owner | Governance / Manager | Set accountable role |
| Approve / reject request | Approver | Decide debt or exception request |
| Attach evidence | Evidence Owner / Participant | Add supporting evidence |
| Close entry | Owner / Approver | Close with evidence or rationale |
| Extend due date / expiry | Approver | Extend debt or exception where policy permits |
| Escalate | Governance | Escalate overdue or severe entry |
| Create Work Order | Governance / Owner | Create remediation work |
| Create Evolve Case | Governance / Evolve | Improve policy, ritual, dashboard, or playbook |

---

## Phase Position

| Maturity | Scope |
|----------|-------|
| Phase 1 | Risk, debt, exception/waiver, and compliance entries required by governance MVP |
| Phase 2 | Deferred obligations and stronger workflows |
| Phase 3 | Kudos dashboard, recognition analytics, reusable practice candidates |

---

## Related Consoles

- **Governance Overview** — summary across registers
- **Controls & Enforcement** — enforcement outcomes that create register entries
- **Rituals** — rituals that produce register entries
- **Reports & Dashboards** — register trends and exports
