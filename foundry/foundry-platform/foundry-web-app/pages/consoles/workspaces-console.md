# Workspaces Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/workspaces`

**Group:** Work

**Purpose:** Navigate the 6 Workspace types; view and manage Workspace Sessions and Work Orders.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Workspace** (ACE) | One of 6 types: Product Specification, UX Design, Development, QA, Release, Governance |
| **Workspace Session** | A Coder-based ephemeral dev environment for working in a Workspace |
| **Work Order** | A unit of work that can be attached to a Session |

---

## Page Layout

```
[Product Spec] [UX Design] [Development] [QA] [Release] [Governance]
                              ↓ (selected)
┌─────────────────────────────────────────────────────────────────────┐
│ + Create Session                                                    │
├─────────────────────────────────────────────────────────────────────┤
│ MY SESSIONS:                                                        │
│   ● "Payment Integration" — Active — 3 WOs (12h total) [Open][Stop] │
│   ○ "Legacy Cleanup" — Stopped — 0 WOs                 [Start]      │
├─────────────────────────────────────────────────────────────────────┤
│ TEAM SESSIONS:                                                      │
│   ● @alice — "Checkout Feature" — Active — 2 WOs       [View]       │
│   ● @bob — "Auth Refactor" — Active — 1 WO             [View]       │
│   ○ @carol — "DB Migration" — Stopped — 0 WOs          [View]       │
├─────────────────────────────────────────────────────────────────────┤
│ UNASSIGNED WORK ORDERS:                                             │
│   • WO-126 — Implement caching                         [Assign]     │
│   • WO-127 — Fix memory leak                           [Assign]     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Page Sections

### 1. Workspace Type Tabs

The 6 standard Workspace types as tabs:

| Workspace | Description |
|-----------|-------------|
| **Product Specification** | Translate Intent to specs |
| **UX Design** | Design user experience |
| **Development** | Build the solution |
| **QA** | Verify and validate |
| **Release** | Publish artifacts |
| **Governance** | Validate transitions |

Click a tab → View Sessions and WOs for that Workspace type.

### 2. My Sessions

Current user's Workspace Sessions for the selected Workspace type.

| Element | Description |
|---------|-------------|
| **Session name** | User-provided identifier |
| **Status** | Active (running) / Stopped |
| **WO count** | Number of attached Work Orders |
| **Total time** | Cumulative time spent on WOs in this Session |
| **Actions** | Open (launch IDE), Stop, Start |

### 3. Team Sessions

Other team members' Sessions for the selected Workspace type.

| Element | Description |
|---------|-------------|
| **Owner** | Team member who owns the Session |
| **Session name** | Identifier |
| **Status** | Active / Stopped |
| **WO count** | Number of attached Work Orders |
| **Actions** | View (see details, read-only) |

### 4. Unassigned Work Orders

Work Orders waiting in this Workspace, not attached to any Session.

| Element | Description |
|---------|-------------|
| **WO ID** | Work Order identifier |
| **Title** | Brief description |
| **PI** | Parent Product Intent |
| **Waiting since** | How long in queue |
| **Actions** | Assign (to self or a Session) |

---

## Workspace Session Model

### Definition

A Workspace Session is a Coder-based ephemeral development environment.

| Aspect | Detail |
|--------|--------|
| **Created by** | Work Order Runtime module |
| **Template** | Per (Workspace Type, Workbench) — customized per Workbench |
| **Ownership** | Owned by one person (not shared) |
| **WO relationship** | Multiple WOs can be attached to one Session |
| **Assignment** | Manual now; Orchestrator may automate later |
| **Destruction** | User explicitly closes |

### Session States

| State | Description |
|-------|-------------|
| **Active** | Running, user can work in it |
| **Stopped** | Persisted but not running (can restart) |
| **Archived** | Read-only snapshot (after explicit close) |

### Session Detail View

Clicking a Session (own or team) shows:

| Element | Description |
|---------|-------------|
| **Session info** | Owner, name, status, created date |
| **Attached WOs** | List with time spent per WO |
| **Total time** | Cumulative time in this Session |
| **Activity** | Recent commits, task completions |
| **Open in IDE** | (Only for own Sessions) |

### Attached Work Orders (in Session Detail)

| Column | Description |
|--------|-------------|
| WO ID | Identifier |
| Title | Brief description |
| PI | Product Intent |
| Status | In progress, blocked, complete |
| Time in Session | Time spent on this WO in this Session |
| Actions | Detach, View details |

---

## Work Order Assignment

| Assignment Type | Meaning |
|-----------------|---------|
| **Unassigned** | In pool under Workspace tab, anyone can pick up |
| **Assigned to person** | That person works on it (in any of their Sessions) |
| **Assigned to Session** | Bound to a specific Session (owner works on it there) |

---

## Actions

### Session Actions

| Action | Who | Description |
|--------|-----|-------------|
| Create Session | All | Start a new Session for this Workspace type |
| Open | Owner | Launch IDE for the Session |
| Stop | Owner | Pause the Session (persists state) |
| Start | Owner | Resume a stopped Session |
| Archive | Owner | Close and create read-only snapshot |
| View | All | See Session details (read-only for others) |

### Work Order Actions

| Action | Who | Description |
|--------|-----|-------------|
| Assign to me | All | Pick up unassigned WO |
| Assign to Session | Owner | Attach WO to a specific Session |
| Detach from Session | Owner | Remove WO from Session (back to unassigned or person-assigned) |
| View details | All | Open Work Order detail page |

---

## Filters

- By Session status (Active, Stopped, Archived)
- By owner (My Sessions vs Team)
- By WO status (In progress, Blocked)
- Search by Session name or WO ID

---

## Scenario Catalog Section

Each Workspace type has an associated Scenario Catalog.

| Element | Description |
|---------|-------------|
| **Available Scenarios** | Scenarios added to this Workspace |
| **Scenario card** | Name, description, typical duration |
| **Add Scenario** | Manager action — browse platform catalog |
| **Remove Scenario** | Manager action — remove from Workspace |

---

## Related Consoles

- **PI Console** — See WOs by Product Intent
- **Progress Console** — Workspace completion metrics
- **Track Console** — Track-level view
- **Team Console** — Who's working in which Sessions
