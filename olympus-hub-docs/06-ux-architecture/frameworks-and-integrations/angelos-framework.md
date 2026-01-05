# Angelos Framework

> **Status:** 🔴 Stub — Placeholder for expansion

**Angelos** is an internal framework for building web components used in Hub operational interfaces — from standard consoles to custom task solvers.

---

## Overview

### Framework Relationship

| Framework | Purpose |
|-----------|---------|
| **Angelos** | Internal framework for building web components |
| **Hercules** | Framework for web application development and hosting |
| **Angelos Action Repository** | Pre-built actions cataloged and made available through Hercules |

> Angelos components are the building blocks; Hercules is the hosting and launch platform.

### Angelos provides:
- **Reusable UI components** for operational interfaces
- **Page Builder** for visual composition
- **Event Binders** for component communication
- **Action Repository** for reusable actions (via Hercules)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ANGELOS FRAMEWORK                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      PAGE BUILDER                                    │    │
│  │  Visual tool for composing pages from components                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      COMPONENT LIBRARY                               │    │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │    │
│  │  │  Task   │  │ Entity  │  │  Data   │  │ Action  │  │  Form   │   │    │
│  │  │ Comps   │  │ Comps   │  │ Comps   │  │ Comps   │  │ Comps   │   │    │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────┐    │
│  │      EVENT BINDERS           │  │      ACTION REPOSITORY          │    │
│  │  Wire events between         │  │  Reusable action definitions    │    │
│  │  components on a page        │  │  (API calls, navigation, etc.)  │    │
│  └──────────────────────────────┘  └──────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Categories

### Task Components

| Component | Purpose |
|-----------|---------|
| **Task List** | Display list of tasks with filters |
| **Task Card** | Summary view of a single task |
| **Task Detail** | Full task information panel |
| **Task Timer** | SLA countdown and time tracking |
| **Task Actions** | Action buttons for task operations |

### Entity Components

| Component | Purpose |
|-----------|---------|
| **Entity Header** | Entity summary and key attributes |
| **Entity Timeline** | Chronological event history |
| **Entity Attributes** | Attribute display/edit panel |
| **Entity Relationships** | Related entities visualization |
| **Entity Documents** | Associated documents and files |

### Data Components

| Component | Purpose |
|-----------|---------|
| **Data Table** | Sortable, filterable data grid |
| **Data Chart** | Charts and visualizations |
| **Data Card** | Summary cards with metrics |
| **Data Filter** | Filter controls |
| **Search Bar** | Search with suggestions |

### Action Components

| Component | Purpose |
|-----------|---------|
| **Action Button** | Trigger an action |
| **Action Menu** | Dropdown of actions |
| **Confirmation Modal** | Confirm before action |
| **Decision Panel** | Structured decision capture |
| **Evidence Capture** | Attach evidence to decision |

### Form Components

| Component | Purpose |
|-----------|---------|
| **Dynamic Form** | Schema-driven form rendering |
| **Field Set** | Grouped form fields |
| **Validation Display** | Error and validation messages |
| **Wizard** | Multi-step form process |

### Notification Components

| Component | Purpose |
|-----------|---------|
| **Alert Banner** | Page-level alerts |
| **Toast** | Transient notifications |
| **Badge** | Status indicators |
| **Progress Indicator** | Loading and progress states |

---

## Page Builder

The Page Builder enables Process Architects and Developers to compose custom consoles visually.

### Capabilities

| Capability | Description |
|------------|-------------|
| **Drag & Drop** | Place components on canvas |
| **Layout Grid** | Responsive grid system |
| **Component Configuration** | Set properties, data bindings |
| **Preview** | Live preview of page |
| **Save & Publish** | Version and deploy pages |

### Page Types

| Type | Purpose |
|------|---------|
| **Console** | Full-page application (e.g., Custom Entity Console) |
| **Task Solver** | Task-specific work interface |
| **Dashboard** | Metrics and overview display |
| **Modal** | Popup dialogs |

---

## Event Binders

Event Binders wire components together, enabling one component's events to trigger actions in another.

### Example Bindings

```yaml
bindings:
  - source:
      component: task-list
      event: task-selected
    target:
      component: task-detail
      action: load-task
      params:
        task_id: "{{event.task_id}}"
  
  - source:
      component: decision-panel
      event: decision-made
    targets:
      - component: task-detail
        action: refresh
      - component: timeline
        action: add-event
```

---

## Action Repository

Reusable action definitions that can be invoked by components. The Action Repository is cataloged and made available through Hercules.

### Contributors

| Contributor | Actions |
|-------------|---------|
| **Hub Platform** | Pre-built actions for Hub platform entities (Tasks, Requests, etc.) |
| **Business Entity Providers** | Pre-built actions for common business entities |
| **Tenant Developers** | Custom actions contributed by tenant developers |

### Action Types

| Type | Examples |
|------|----------|
| **API Actions** | Call Hub APIs, external services |
| **Navigation Actions** | Navigate to page, open modal |
| **Data Actions** | Refresh data, update state |
| **Notification Actions** | Show toast, display alert |

### Action Definition Example

```yaml
action:
  id: complete-task
  name: "Complete Task"
  type: api
  endpoint: "/api/tasks/{{task_id}}/complete"
  method: POST
  payload:
    decision: "{{decision}}"
    rationale: "{{rationale}}"
  on_success:
    - action: show-toast
      params:
        message: "Task completed successfully"
    - action: navigate
      params:
        page: task-list
  on_error:
    - action: show-alert
      params:
        message: "{{error.message}}"
```

---

## Related Documentation

- [Workbench Studio](../tenant-domain/workbench-studio.md)
- [Agent Desk](../tenant-domain/agent-desk.md)
- [Hercules Launcher](./hercules-launcher.md)

---

*TODO: Detailed component specifications, page builder workflows, binding patterns*

