# Hub Home

> **Status:** 🔴 Stub — Placeholder for expansion

**Hub Home** is the central landing page for Agents and Supervisors, providing a unified view across all accessible workbenches.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Personas** | Agent, Supervisor |
| **Scope** | User (across workbenches) |
| **Access** | Web, Mobile, MS Teams, AI Assistants |

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Workbench List** | All workbenches the user has access to, with quick stats |
| **My Tasks** | Tasks assigned to the user across all workbenches |
| **Quick Actions** | Shortcuts to common operations |
| **Alerts & Notifications** | Real-time updates requiring attention |
| **Recent Activity** | Recently accessed requests, tasks, entities |
| **Routines Due** | Scheduled routines for today/upcoming |

---

## Screen Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              HUB HOME                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  ALERTS & NOTIFICATIONS                               [View All →]  │    │
│  │  🔴 3 escalated tasks require attention                             │    │
│  │  🟡 5 tasks approaching SLA deadline                                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────┐    │
│  │  MY TASKS                    │  │  QUICK ACTIONS                   │    │
│  │  ┌────────────────────────┐  │  │  [+ New Request]                 │    │
│  │  │ 12 Assigned            │  │  │  [📋 My Routines]                │    │
│  │  │  5 Due Today           │  │  │  [🔍 Search]                     │    │
│  │  │  2 Overdue             │  │  │  [📊 Dashboard]                  │    │
│  │  └────────────────────────┘  │  └──────────────────────────────────┘    │
│  └──────────────────────────────┘                                           │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  WORKBENCHES                                                        │    │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │    │
│  │  │ Dispute Ops     │  │ Fraud Review    │  │ Onboarding      │     │    │
│  │  │ 8 tasks         │  │ 4 tasks         │  │ 0 tasks         │     │    │
│  │  │ [Open →]        │  │ [Open →]        │  │ [Open →]        │     │    │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────┐    │
│  │  RECENT ACTIVITY             │  │  ROUTINES DUE                    │    │
│  │  • REQ-1234 updated          │  │  ☐ Morning queue review (08:00)  │    │
│  │  • Task completed: KYC...    │  │  ☐ Escalation check (12:00)      │    │
│  │  • Decision: Approved...     │  │  ☑ EOD summary (completed)       │    │
│  └──────────────────────────────┘  └──────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Personalization

| Aspect | Customization |
|--------|---------------|
| **Workbench Order** | Pin favorites, sort by activity |
| **Quick Actions** | Customize shortcuts |
| **Notification Preferences** | Filter alert types |
| **Default View** | Configure landing widgets |

---

## Related Documentation

- [Agent Persona](../08-personas-and-journeys/personas/agent.md)
- [Supervisor Persona](../08-personas-and-journeys/personas/supervisor.md)
- [Agent Desk](./agent-desk.md)
- [Supervisor Desk](./supervisor-desk.md)

---

*TODO: Detailed widget specifications, personalization options, mobile layout*

