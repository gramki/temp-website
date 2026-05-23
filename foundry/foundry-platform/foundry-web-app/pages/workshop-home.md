# Workshop Home Page

**URL pattern:** `/workshops/{workshopId}`

**Purpose:** Dashboard for a single Workshop (division/unit); shows all Workbenches and Workshop-level resources.

---

## Target Users

- Workshop Managers
- Workbench Managers within the Workshop
- Team members assigned to Workbenches in this Workshop

---

## Page Sections

### 1. Workshop Header

| Element | Description |
|---------|-------------|
| Workshop name | Display name |
| Description | Brief description of the division/unit |
| Owner | Workshop lead/manager |
| Quick stats | Workbench count, active Work Orders, team size |

### 2. Workbenches List

| Element | Description |
|---------|-------------|
| Workbench cards | Grid/list of all Workbenches in this Workshop |
| Per-card info | Product name, Product Code, recent activity, health status |
| Deployment status | Latest version deployed (from Weave) |
| Quick actions | Navigate to Workbench Home |
| Search/filter | Filter by name, status, activity |

### 3. Shared Repositories

Workshop-level shared repositories:

| Repository | Actions |
|------------|---------|
| **Domain** | Browse, search domain knowledge |
| **Practices** | Browse standards, templates |
| **Stakeholders** | View stakeholder registry |

### 4. Workshop Activity

| Element | Description |
|---------|-------------|
| Activity feed | Recent Work Orders, deployments across all Workbenches |
| Governance events | Gate approvals, rejections |
| Time range | Configurable |

### 5. Workshop Health

| Element | Description |
|---------|-------------|
| Workbench health | Per-Workbench status indicators |
| Deployment overview | Version distribution across Workbenches |
| EoS/Deprecation alerts | Flagged from Weave |

### 6. Quick Actions (Manager)

| Action | Description |
|--------|-------------|
| Create Workbench | Launch Workbench creation wizard |
| Manage Domain | Navigate to Domain repository |
| Manage Practices | Navigate to Practices repository |
| Workshop Settings | Navigate to Workshop settings |

---

## Navigation

| Target | Path |
|--------|------|
| Foundry Home | Breadcrumb → `/` |
| Workbench Home | Click Workbench card → `/workbenches/{workbenchId}` |
| Shared Repository | Click repository link → `/workshops/{workshopId}/repos/{repoType}` |

---

## Access Control

| Role | Access |
|------|--------|
| Foundry Admin | Full access |
| Workshop Manager | Full access to this Workshop |
| Workbench Manager | View Workshop, full access to own Workbenches |
| Workbench Member | View Workshop, view assigned Workbenches |

---

## Open Questions

- Should Workshop Home show cross-Workbench dependency graphs?
- How to surface EoS/deprecation alerts prominently?
- Workshop-level reporting/analytics?
