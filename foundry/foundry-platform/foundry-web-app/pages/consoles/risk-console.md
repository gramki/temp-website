# Risk Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/risk`

**Group:** Governance

**Purpose:** Governance risk flags — view, manage, and respond to risks.

---

## Page Sections

### 1. Risk Summary

| Metric | Description |
|--------|-------------|
| **Active risks** | Total open risk flags |
| **By severity** | Critical, High, Medium, Low |
| **PIs at risk** | Product Intents with flags |
| **New this week** | Recently raised risks |

### 2. Risk List

| Column | Description |
|--------|-------------|
| Risk ID | Identifier |
| PI | Affected Product Intent |
| Type | Risk category |
| Severity | Critical / High / Medium / Low |
| Raised | When flagged |
| Raised by | Who/what raised it |
| Status | Open, mitigating, resolved |

### 3. Risk Types

| Type | Description |
|------|-------------|
| **Schedule** | Deadline at risk |
| **Quality** | Quality thresholds not met |
| **Dependency** | Blocked by external factor |
| **Resource** | Team/agent capacity issue |
| **Technical** | Technical blocker |
| **Compliance** | Governance requirement unmet |

### 4. Risk Detail View

| Element | Description |
|---------|-------------|
| **Risk info** | ID, type, severity, description |
| **Affected PI** | Product Intent impacted |
| **Impact** | What's at stake |
| **Root cause** | Why this risk exists |
| **Mitigation** | Actions being taken |
| **History** | Status changes, comments |
| **Evidence** | Supporting data |

### 5. PI Risk Badges

Shows how risks affect PI badges on Workbench Home:

| PI | Risks | Badge Color |
|----|-------|-------------|
| PI-039 | 1 Critical | Red |
| PI-041 | 2 Medium | Yellow |
| PI-042 | None | Green |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Raise risk | Manager, Governance | Flag a new risk |
| Update status | Manager, Governance | Change risk status |
| Add mitigation | Manager | Document mitigation actions |
| Resolve risk | Manager, Governance | Close the risk |
| Escalate | Governance | Raise to Workshop/Foundry level |

---

## Filters

- By PI
- By severity
- By type
- By status (open, mitigating, resolved)
- By date range

---

## Notifications

- New Critical/High risk → immediate notification
- Risk status change → notify stakeholders
- Risk approaching deadline → reminder

---

## Related Consoles

- **PI Console** — See PI details
- **Reports Console** — Risk reports
- **Quality Compliance** — Quality-related risks
- **Progress Console** — Schedule-related risks
