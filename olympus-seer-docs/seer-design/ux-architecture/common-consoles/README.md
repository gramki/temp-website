# Common Consoles

> **Status:** 🔴 Planning  
> **Last Updated:** 2026-01-13  
> **Related:** [UX Architecture Overview](../README.md) | [Desk Requirements](../desk-requirements.md)

---

## Overview

Common consoles are shared UI components that appear across multiple Seer desks. They provide consistent functionality for capabilities that span personas while respecting role-based permissions.

---

## Why Common Consoles?

Some capabilities are needed by multiple personas:

| Capability | Used By | Rationale |
|------------|---------|-----------|
| Agent Behavior Analysis | APO, CSA, AE, ARE, COS, ARAO | All need to understand agent reasoning |
| Agent Catalog Browsing | All personas | Universal need to find agents |
| Audit Trail Viewing | ARE, COS, ARAO | Shared need for decision history |
| Alert Management | All personas | Everyone receives relevant alerts |

Rather than duplicating these across desks, common consoles provide:
- **Consistent UX** — Same interface regardless of access point
- **Persona-Specific Views** — Content filtered by role
- **Centralized Maintenance** — Single codebase to maintain
- **Permission Enforcement** — Role-based access control

---

## Common Consoles

| Console | Description | Documentation |
|---------|-------------|---------------|
| **Agent Behavior Console** | Deep analysis of agent reasoning, decisions, and traces | [agent-behavior-console.md](./agent-behavior-console.md) |
| **Agent Catalog Console** | Browse and search all agents | [agent-catalog-console.md](./agent-catalog-console.md) |
| **Alert Console** | Manage notifications and alerts | [alert-console.md](./alert-console.md) |

---

## Permission Model

### Console-Level Permissions

Each common console has defined permission levels:

| Permission | Description |
|------------|-------------|
| **Read** | View data, cannot modify |
| **Write** | View and modify data |
| **Admin** | Full access including configuration |

### Persona-to-Permission Mapping

| Console | APO | CSA | AE | KMO | ARE | COS | ARAO |
|---------|-----|-----|-----|-----|-----|-----|------|
| Agent Behavior | Read | Read | Write | Read | Write | Write | Read |
| Agent Catalog | Write | Read | Write | Read | Write | Read | Read |
| Alerts | Read | Read | Read | Read | Admin | Read | Read |

### View Filtering

Even with the same permission level, personas see different views:

| Console | View Filter Logic |
|---------|-------------------|
| Agent Behavior | Detail level varies by role (APO sees outcomes, AE sees implementation) |
| Agent Catalog | Filters by ownership (APO sees owned agents) |
| Alerts | Filters by relevance (ARE sees operational, COS sees behavioral) |

---

## Integration with Desks

Common consoles are embedded in desks through:

1. **Tab Embedding** — Console appears as a tab within a desk
2. **Panel Embedding** — Console appears as a side panel
3. **Modal Launch** — Console opens as a modal from a desk action
4. **Linked Navigation** — Desk links to console as separate view

### Example: Agent Behavior Console

```
Agent Portfolio Desk (APO)
├── Portfolio Console
├── Outcomes Console
├── Autonomy Console
└── [Agent Behavior Console] ← Embedded common console
```

---

## Technical Architecture

### Component Structure

```
common-consoles/
├── agent-behavior-console/
│   ├── AgentBehaviorConsole.tsx
│   ├── components/
│   │   ├── TraceViewer.tsx
│   │   ├── DecisionTimeline.tsx
│   │   └── PersonaView.tsx
│   └── hooks/
│       └── useAgentBehavior.ts
├── agent-catalog-console/
│   └── ...
└── alert-console/
    └── ...
```

### Permission Enforcement

```typescript
// Example permission check
const AgentBehaviorConsole: FC = () => {
  const { persona, permissions } = useAuth();
  
  // Filter view based on persona
  const viewConfig = getPersonaViewConfig(persona);
  
  // Check permissions
  if (!permissions.canAccessAgentBehavior) {
    return <PermissionDenied />;
  }
  
  return (
    <ConsoleContainer config={viewConfig}>
      {/* Persona-filtered content */}
    </ConsoleContainer>
  );
};
```

---

## REST API Integration

Common consoles use the same REST APIs as desk-specific consoles:

| Console | Primary API Channel | MCP Equivalent |
|---------|---------------------|----------------|
| Agent Behavior | `/api/seer/behavior/v1` | `seer-behavior-mcp` |
| Agent Catalog | `/api/seer/catalog/v1` | `seer-catalog-mcp` |
| Alerts | `/api/seer/alerts/v1` | `seer-alerts-mcp` |

---

## Console Documentation Template

Each common console document includes:

1. **Purpose** — Why this console exists
2. **Personas** — Who uses it and how
3. **Sections** — UI sections and capabilities
4. **Persona Views** — How views differ by role
5. **Data Sources** — Where data comes from
6. **Permissions** — Who can do what
7. **REST APIs** — Supporting APIs
8. **Indicative Wireframes** — Visual mockups

---

## Next Steps

Detailed documentation for each common console:

- [ ] [Agent Behavior Console](./agent-behavior-console.md) — Detailed specification
- [ ] [Agent Catalog Console](./agent-catalog-console.md) — Detailed specification  
- [ ] [Alert Console](./alert-console.md) — Detailed specification

---

*Status: 🔴 Planning — Structure defined, detailed specs TBD*
