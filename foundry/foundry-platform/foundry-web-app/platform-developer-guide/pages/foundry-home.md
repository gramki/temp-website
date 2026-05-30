# Foundry Home Page

**URL pattern:** `/`

**Purpose:** Entry point for all Foundry users; dashboard view of the entire Foundry.

---

## Target Users

- Foundry Admins
- Workshop leads
- Anyone with Foundry-level visibility

---

## Page Sections

### 1. Foundry Overview

| Element | Description |
|---------|-------------|
| Foundry name | Display name of this Foundry instance |
| Tenant info | Organization/tenant identifier |
| Quick stats | Workshops count, Workbenches count, active Work Orders |

### 2. Workshops List

| Element | Description |
|---------|-------------|
| Workshop cards | Grid/list of all Workshops in the Foundry |
| Per-card info | Name, Workbench count, recent activity |
| Quick actions | Navigate to Workshop Home |
| Search/filter | Filter by name, status |

### 3. Recent Activity (Foundry-wide)

| Element | Description |
|---------|-------------|
| Activity feed | Recent Work Orders, deployments, governance events |
| Scope | Aggregated across all Workshops |
| Time range | Configurable (today, week, month) |

### 4. Foundry Health

| Element | Description |
|---------|-------------|
| Agent utilization | Active agents, queue depth |
| Integration status | GitHub, Jira, TestRail, Figma, Weave connection health |
| Alerts | Any system-level warnings |

### 5. Quick Actions (Admin)

| Action | Description |
|--------|-------------|
| Create Workshop | Launch Workshop creation wizard |
| Manage Teams | Navigate to team management |
| Platform Settings | Navigate to Foundry-level settings |

---

## Navigation

| Target | Path |
|--------|------|
| Workshop Home | Click Workshop card → `/workshops/{workshopId}` |
| Workbench Home | Via Workshop → Workbench card |
| Settings | Header nav → `/settings` |

---

## Access Control

| Role | Access |
|------|--------|
| Foundry Admin | Full access, all actions |
| Workshop Manager | View only (own Workshops highlighted) |
| Workbench Member | View only (limited to assigned Workshops) |

---

## Open Questions

- Should Foundry Home show cross-Workshop analytics?
- How deep should the activity feed go (Work Orders vs Tasks)?
- Notification center at Foundry level?
