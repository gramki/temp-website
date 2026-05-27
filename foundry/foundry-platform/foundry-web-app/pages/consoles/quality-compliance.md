# Quality Controls Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/quality-compliance`

**Group:** Governance

**Purpose:** Specialized Controls & Enforcement view for build and release quality: Control Objectives, Control Objective Indicators, thresholds, evidence, Debt + Catch-Up, and Exception / Waiver status.

> **Position:** Quality Controls covers the Build Quality Readiness family. It is one part of Release Readiness, alongside documentation, SRE/operational, security, evidence, customer, GTM, data/migration, and dependency readiness.

---

## Page Sections

### 1. Compliance Summary

| Metric | Description |
|--------|-------------|
| **Overall compliance** | % of thresholds met |
| **Compliant PIs** | PIs meeting all requirements |
| **Non-compliant PIs** | PIs with unmet requirements |
| **Pending sign-offs** | Awaiting approval |

### 2. Quality Control Objectives

| Control Objective | Indicator | Required / threshold | Current | Result |
|-------------------|-----------|----------------------|---------|--------|
| Unit test coverage healthy | Coverage % | ≥80% target | 78% | Debt required |
| Test pass rate healthy | Pass rate % | ≥95% | 97% | Pass |
| No critical bugs | Critical bug count | 0 | 0 | Pass |
| Security scan passed | Scan verdict | Pass | Pass | Pass |
| Performance tested | Performance verdict | Pass | Pending | Awaiting evidence |

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
| **Current thresholds** | Active Control Objective Thresholds |
| **Threshold history** | Changes over time |
| **Exceptions / Waivers** | Approved non-applicability, alternate controls, or bounded bypasses |
| **Debt + Catch-Up** | Temporary deviations with remediation plan, Debt Owner, due date, and repayment evidence |

### 7. Project Type and Maturity Configuration

| Element | Description |
|---------|-------------|
| **Project type** | Microservice, library, ClusterSpec artifact, or other configured type |
| **Maturity profile** | Alpha, Beta, Gamma, Theta, or configured maturity model |
| **Effective thresholds** | Thresholds after type and maturity resolution |
| **Maturity change request** | Request and approval status for maturity profile changes |

### 8. Role Legend

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
| Request maturity change | Manager | Request project maturity profile change |
| Close debt | Control Owner | Mark catch-up complete after evidence re-check |
| View evidence | All | Access supporting data |

---

## Filters

- By PI
- By Control Objective
- By Control Objective Indicator
- By project type
- By maturity profile
- By compliance status
- By date range

---

## Notifications

- Hard fail → immediate alert
- Debt required → prompt for Catch-Up Plan
- Pending sign-off → reminder to approvers
- Exception expiring → advance notice

---

## Related Consoles

- **Quality Status** — Current test results
- **Controls & Enforcement** — Generic control/enforcement view
- **Registers** — Debt, exceptions, and risk entries
- **Reports & Dashboards** — Compliance reports and quality dashboards
- **Release Console** — Quality gates for release
