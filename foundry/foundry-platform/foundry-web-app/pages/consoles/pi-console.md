# PI Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/pi`

**Group:** Work

**Purpose:** View and manage all Product Intents — active and archived.

---

## Page Sections

### 1. PI List

| Element | Description |
|---------|-------------|
| **Active PIs** | Currently in-progress Intents |
| **Archived PIs** | Completed/shipped Intents |
| **View toggle** | Switch between Active / Archived / All |
| **Sort options** | By start date, due date, health, name |
| **Search** | Find PI by ID or title |

### 2. PI Card (List Item)

| Element | Description |
|---------|-------------|
| PI ID + Title | Identity |
| Start → Due dates | Time orientation |
| Health badge | Color from Governance risk flags |
| Track progress | [Spec✓][UX●][Dev○][QA○][Rel○][Gov○] |
| Active Work Orders | Count of in-progress WOs |
| Last activity | Most recent update |

### 3. PI Detail View (Drill-down)

| Element | Description |
|---------|-------------|
| **Overview** | Title, description, dates, owner |
| **Intent content** | PRD, PSD links (GitHub) |
| **Track timeline** | Visual flow through Tracks |
| **Work Orders** | All WOs for this PI |
| **Artifacts** | Design docs, code repos, test suites |
| **History** | Audit trail of changes |
| **Risk flags** | Active Governance concerns |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Create Intent | Manager, Member | Start new PI (calls Metadata Service for ID) |
| Edit Intent | Manager, Member | Update title, description, dates |
| Archive Intent | Manager | Move to archived (after Release complete) |
| Create Work Order | Manager, Member | Initiate work for this PI |
| View in Wall | All | Filter Workbench Wall to this PI |

---

## Filters

- By health (Green, Yellow, Red)
- By current Track/Workspace
- By date range (start, due)
- By owner/assignee

---

## Related Consoles

- **Workspaces Console** — See WOs by Workspace
- **Progress Console** — PI completion metrics
- **Risk Console** — Risk flags affecting PIs
