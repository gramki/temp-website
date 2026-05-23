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
| **Exceptions** | Approved deviations |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Sign off | Governance | Approve compliance |
| Request exception | Manager | Ask for threshold waiver |
| Approve exception | Governance | Grant waiver |
| Update threshold | Governance, Admin | Change requirements |
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
