# Governance Admin Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/governance-admin`

**Group:** Settings

**Purpose:** Configure governance definitions, authority, inheritance, control objectives, thresholds, rituals, and register definitions for a Workbench, within permissions inherited from Foundry and Workspace configuration.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Governance Admin** | Role authorized to configure governance settings at a scope. |
| **Control Owner** | Role accountable for a control's objective, indicators, and evidence contract. |
| **Approver** | Role authorized to approve debt, exception/waiver, risk acceptance, or transition. |
| **Governance Authority Matrix** | Operating Model mapping from control/action/scope to owners and approvers. |
| **Control inheritance** | Foundry -> Workspace -> Workbench inheritance of controls and thresholds. |

---

## Page Sections

### 1. Governance Authority Matrix

| Field | Description |
|-------|-------------|
| **Action type** | Sign off, approve debt, approve exception, accept risk, override |
| **Control / policy** | Control the authority applies to |
| **Scope** | Foundry, Workspace, Workbench, Track, transition, artifact |
| **Effective Control Owner** | Resolved accountable owner |
| **Approver** | Role authorized to decide |
| **Escalation** | Escalation rule when overdue/unresolved |
| **Delegation** | Backup or delegated approvers |

### 2. Control Inheritance

```text
Foundry controls
  -> Workspace controls
    -> Workbench controls
```

Shows:
- inherited controls;
- local additions;
- permitted overrides;
- blocked overrides;
- effective thresholds;
- effective owners/approvers.

### 3. Control Catalog Configuration

| Element | Description |
|---------|-------------|
| Governance Policies | Policy definitions and scopes |
| Policy Controls | Specific controls under policies |
| Control Objectives | Required outcomes |
| Control Objective Indicators | Metrics/evidence/checks used to evaluate objectives |
| Thresholds | Minimum, warning, target/enforcement thresholds |
| Evidence Requirements | Evidence needed for pass |
| Enforcement Modes | Block, warn, allow-with-debt, allow-with-risk, require-exception |
| Debt Eligibility | Whether Debt + Catch-Up is allowed |
| Exception Eligibility | Whether Exception / Waiver is allowed |

### 4. Ritual Configuration

| Element | Description |
|---------|-------------|
| Ritual Definitions | Purpose, cadence, trigger |
| Participants | Required roles |
| Input dashboards/reports | Required ritual inputs |
| Checklist | Review checklist |
| Decision authority | Approvers for ritual outputs |
| Expected outputs | Decisions, action items, findings, recognitions, register entries |

### 5. Register Configuration

| Register | Configuration |
|----------|---------------|
| Risk | Fields, severity, status lifecycle, escalation |
| Debt | Catch-Up Plan fields, due dates, repayment evidence |
| Exceptions / Waivers | Expiry rules, conditions, renewal |
| Compliance | Control obligations and audit periods |
| Workforce Recognition | Recognition types, visibility, reusable practice candidate flag (stored in WFR) |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Configure control | Governance Admin | Create or edit policy/control |
| Configure threshold | Governance Admin | Update Control Objective Threshold where permitted |
| Configure inheritance | Governance Admin | Set override permissions |
| Assign Control Owner | Governance Admin | Bind accountable role |
| Configure Approver | Governance Admin | Bind decision authority |
| Configure ritual | Governance Admin | Create or edit Ritual Definition |
| Configure register | Governance Admin | Edit register fields/lifecycle |
| Publish configuration | Governance Admin | Publish versioned governance configuration |

---

## Phase Position

| Maturity | Scope |
|----------|-------|
| Phase 1 | Basic governance configuration in Admin Console; read-only effective controls if needed |
| Phase 2 | Control catalog, thresholds, role bindings |
| Phase 3 | Full authority matrix editor, inheritance UI, register/ritual definition management |

---

## Related Consoles

- **Admin Console** — broader Workbench configuration
- **Controls & Enforcement** — runtime evaluation of configured controls
- **Rituals** — runtime execution of configured rituals
- **Registers** — records created by configured governance outcomes
