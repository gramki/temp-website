# Quality Compliance Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/quality-compliance`

**Group:** Governance

**Purpose:** Required quality thresholds, audit evidence, and compliance sign-offs.

---

## Page Sections

### 1. Compliance Summary

| Metric | Description |
|--------|-------------|
| **Overall compliance** | % of thresholds met |
| **Compliant PIs** | PIs meeting all requirements |
| **Non-compliant PIs** | PIs with unmet requirements |
| **Pending sign-offs** | Awaiting approval |

### 2. Quality Thresholds

| Threshold | Required | Current | Status |
|-----------|----------|---------|--------|
| Test coverage | ≥80% | 78% | ⚠️ Below |
| Test pass rate | ≥95% | 97% | ✓ Met |
| Critical bugs | 0 | 0 | ✓ Met |
| Security scan | Pass | Pass | ✓ Met |
| Performance test | Pass | Pending | ⏳ Pending |

### 3. Compliance by PI

| PI | Coverage | Pass Rate | Bugs | Security | Overall |
|----|----------|-----------|------|----------|---------|
| PI-039 | ✓ | ✓ | ✓ | ✓ | ✓ Compliant |
| PI-041 | ⚠️ | ✓ | ✓ | ✓ | ⚠️ Partial |
| PI-042 | ✓ | ✓ | ⚠️ | ⏳ | ⚠️ Partial |

### 4. Audit Evidence

| Element | Description |
|---------|-------------|
| **Test results** | Links to test runs |
| **Coverage reports** | Code coverage data |
| **Security scans** | Vulnerability scan results |
| **Performance tests** | Load/stress test results |
| **Sign-off records** | Who approved what |

### 5. Sign-off Workflow

| Element | Description |
|---------|-------------|
| **Pending sign-offs** | Items awaiting approval |
| **Sign-off history** | Past approvals |
| **Approvers** | Who can sign off |
| **Delegation** | Backup approvers |

### 6. Threshold Configuration

| Element | Description |
|---------|-------------|
| **Current thresholds** | Active requirements |
| **Threshold history** | Changes over time |
| **Exceptions / Waivers** | Approved non-applicability, alternate controls, or bounded bypasses |
| **Debt + Catch-Up** | Temporary deviations with remediation plan, Debt Owner, due date, and repayment evidence |

### 7. Role Legend

| Role | Console meaning |
|------|-----------------|
| **Governance Admin** | Configures thresholds, control objectives, and policy bindings where permitted |
| **Control Owner** | Accountable party shown on each threshold/control row |
| **Approver** | Decision authority for sign-off, exception/waiver, or Debt + Catch-Up |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Sign off | Approver | Approve compliance |
| Request exception / waiver | Manager | Ask for approved non-applicability, alternate control, or bounded bypass |
| Approve exception / waiver | Approver | Grant waiver with rationale, scope, and expiry |
| Request Debt + Catch-Up | Manager | Request temporary deviation with remediation plan |
| Approve Debt + Catch-Up | Approver | Approve debt, Debt Owner, due date, and repayment evidence |
| Update threshold | Governance Admin | Change Control Objective Thresholds where permitted |
| Close debt | Control Owner | Mark catch-up complete after evidence re-check |
| View evidence | All | Access supporting data |

---

## Filters

- By PI
- By threshold type
- By compliance status
- By date range

---

## Notifications

- Threshold breach → immediate alert
- Pending sign-off → reminder to approvers
- Exception expiring → advance notice

---

## Related Consoles

- **Quality Status** — Current test results
- **Risk Console** — Quality-related risks
- **Reports Console** — Compliance reports
- **Release Console** — Quality gates for release
