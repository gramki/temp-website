# Findings Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/findings`

**Group:** Build

**Type:** Queue + Analytics

**Purpose:** Centralized view of all automated scan findings that can gate builds and releases — security vulnerabilities, license violations, code quality issues, and policy violations.

---

## Audience

- Security Engineers
- Compliance Analysts
- Engineering Leads
- Release Managers

---

## Page Sections

### 1. Findings Overview

Summary metrics:

| Metric | Description |
|--------|-------------|
| **Critical/High open** | Findings requiring immediate attention |
| **By type** | Breakdown: Security, License, Quality, Policy |
| **By status** | Open, In Progress, Suppressed, Resolved |
| **Trend** | New vs resolved over time |
| **SLA breaches** | Findings past remediation deadline |

### 2. Findings Queue

Filterable list of findings:

| Column | Description |
|--------|-------------|
| **Severity** | Critical, High, Medium, Low, Info |
| **Type** | Security, License, Quality, Policy |
| **Title** | Finding description |
| **Component** | Affected system/component |
| **Source** | Scanner that detected it (e.g., Snyk, SonarQube, Trivy) |
| **Detected** | When first found |
| **Status** | Open, In Progress, Suppressed, Resolved |
| **Assignee** | Owner for remediation |

### 3. Finding Types

#### Security Vulnerabilities

| Source | Examples |
|--------|----------|
| **Dependency CVEs** | Known vulnerabilities in dependencies (from SBOM analysis) |
| **SAST** | Static application security testing findings |
| **DAST** | Dynamic application security testing findings |
| **Container scans** | Image vulnerabilities |
| **Secrets detection** | Exposed credentials, API keys |

#### License Violations

| Source | Examples |
|--------|----------|
| **License compliance** | Incompatible licenses (e.g., GPL in proprietary code) |
| **Attribution missing** | Required notices not included |
| **Unapproved licenses** | License not on approved list |

#### Code Quality Findings

| Source | Examples |
|--------|----------|
| **Static analysis** | Code smells, complexity, maintainability |
| **Linting** | Style violations, potential bugs |
| **Duplication** | Copy-paste code detection |

#### Policy Violations

| Source | Examples |
|--------|----------|
| **Dependency policy** | Unapproved or deprecated dependencies |
| **Build policy** | Missing required checks, unsigned artifacts |
| **Approval policy** | Required approvals not obtained |

### 4. Finding Detail View

Clicking a finding shows:

| Section | Content |
|---------|---------|
| **Summary** | Title, severity, type, status, detected date |
| **Description** | Full finding description |
| **Affected** | Component, file, line (if applicable) |
| **Remediation** | Recommended fix, upgrade path |
| **References** | CVE links, documentation |
| **History** | Status changes, comments |
| **Related** | Other findings in same component |

### 5. Trend Analytics

| Chart | Purpose |
|-------|---------|
| **Open findings over time** | Are we getting better or worse? |
| **Mean time to remediate** | By severity, by type |
| **Top affected components** | Where to focus hardening |
| **Top finding types** | Recurring patterns |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| **Triage** | Security/Lead | Assign severity, owner |
| **Assign** | Lead | Set remediation owner |
| **Suppress** | Security | Mark as false positive or accepted risk (requires justification) |
| **Create exception** | Security | Request formal exception (creates Governance Register entry) |
| **Link to Work Order** | Engineer | Associate with remediation work |
| **Resolve** | Engineer | Mark as fixed (verified by re-scan) |
| **Escalate** | Any | Create Risk Register entry in Governance |

---

## Filters

- By severity (Critical, High, Medium, Low, Info)
- By type (Security, License, Quality, Policy)
- By status (Open, In Progress, Suppressed, Resolved)
- By component
- By source scanner
- By date range
- By assignee

---

## Gatekeeping Integration

Findings can block CI/CD pipelines:

| Gate | Rule example |
|------|--------------|
| **Build gate** | Fail build if Critical findings exist |
| **PR gate** | Block merge if new High+ findings introduced |
| **Release gate** | Block release if open Critical/High findings |

Gate policies are configured in Governance Admin.

---

## Integrations

| System | Integration |
|--------|-------------|
| **CI Console** | Scan results flow in; findings linked to builds |
| **Components Console** | Affected components; Supply Chain tab shows dependencies |
| **Governance Registers** | Escalate to Risk/Debt register; create exceptions |
| **Quality Controls** | Threshold evaluation for release gates |
| **Release Artifacts** | Findings block release if gates fail |

---

## Related Consoles

- **CI Console** — Builds that produce findings
- **Components Console** — What's affected; Supply Chain for dependency view
- **Quality Status** — Test results (distinct from quality findings)
- **Governance Registers** — Escalated risks, accepted exceptions
- **Quality Controls** — Gate policies and thresholds
