# Work Catalogs Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/work-catalogs`

**Group:** Resources

**Purpose:** Browse the effective Work Catalog for this Workbench, view source repositories, and understand inheritance.

---

## Page Sections

### 1. Effective Catalog View

The primary view shows the **effective catalog** — the merged result of all catalog levels for this Workbench.

| Element | Description |
|---------|-------------|
| **Track filter** | Filter by Track (Build, Discovery, Run, Win, Evolve, Governance) |
| **OI type filter** | Filter by Orchestration Item type within selected Track |
| **Workspace filter** | Filter by Workspace type |
| **Search** | Search scenarios and workflows by name, description, or tags |

### 2. Catalog Browser

#### OI Workflows Tab

| Column | Description |
|--------|-------------|
| **OI Type** | Orchestration Item type (Product Intent, Discovery Case, etc.) |
| **Workflow Name** | Display name of the workflow |
| **Source** | Repository level (Platform, Foundry, Workshop, Workbench, User) |
| **Last Modified** | When the workflow was last changed |
| **Actions** | View, Compare to parent |

#### Scenarios Tab

| Column | Description |
|--------|-------------|
| **Scenario ID** | Unique identifier |
| **Workspace** | Target Workspace type |
| **Scope** | `workspace-ingress` (external contract) or `workspace-internal` |
| **Skilled Agent** | Recommended Skilled Agent |
| **Source** | Repository level |
| **Actions** | View, Compare to parent |

### 3. Source Display

Each item shows its source repository with visual indicators:

| Source | Badge | Meaning |
|--------|-------|---------|
| **Platform** | `PLATFORM` | Ships with Foundry Platform |
| **Foundry** | `FOUNDRY` | Defined at Foundry level |
| **Workshop** | `WORKSHOP` | Defined at Workshop level |
| **Workbench** | `WORKBENCH` | Defined at this Workbench |
| **User** | `USER` | User's personal catalog (if activated) |

Overridden items show an "Overrides: {parent level}" indicator.

### 4. Inheritance Visualization

Expand any catalog item to see the inheritance chain:

```
implement-feature (Scenario)
├── Platform default          ← base definition
│   └── Workshop override     ← adds workspace-specific config
│       └── Workbench active  ← current effective version
```

| Element | Description |
|---------|-------------|
| **Inheritance tree** | Visual hierarchy showing all levels |
| **Diff viewer** | Compare any two levels side-by-side |
| **Override summary** | What changed at each level |

### 5. User Catalog Status

Shows the current user's catalog activation status:

| Element | Description |
|---------|-------------|
| **Activation status** | Whether user catalog is active for this session |
| **User catalog link** | Link to user's personal Work Catalog repo |
| **Activation toggle** | Enable/disable for current session |
| **Profile link** | Link to user profile for persistent setting |

---

## Actions

### View Actions

| Action | Who | Description |
|--------|-----|-------------|
| View workflow | All | Open OI Workflow definition |
| View scenario | All | Open Scenario definition |
| Compare | All | Side-by-side diff with parent level |
| View in repo | All | Open source file in GitHub |

### Authoring Actions

| Action | Who | Description |
|--------|-----|-------------|
| Open in IDE | All | Launch Scenario Editor extension |
| Copy to clipboard | All | Copy YAML for use in authoring |

### User Catalog Actions

| Action | Who | Description |
|--------|-----|-------------|
| Activate user catalog | All | Enable personal catalog for session |
| Deactivate user catalog | All | Disable personal catalog for session |
| Open user catalog repo | All | View personal Work Catalog in GitHub |

---

## Catalog Levels Explained

| Level | Repository | Who Manages | Purpose |
|-------|------------|-------------|---------|
| **Platform** | `work-catalogues/platform-defaults/` | Foundry Platform team | Out-of-box defaults |
| **Foundry** | `foundry-{id}/work-catalog/` | Foundry Admin | Organization-wide customizations |
| **Workshop** | `workshop-{id}/work-catalog/` | Workshop Admin | Division-level customizations |
| **Workbench** | Workbench config in Workshop repo | Workbench Manager | Product-specific customizations |
| **User** | `user-work-catalog-{userId}/` | Individual user | Personal experimentation |

---

## Integrations

- **IDE** — Scenario Editor extension for authoring
- **GitHub** — Source repositories for all catalog levels
- **Metadata Service** — Effective catalog resolution

---

## Related Consoles

- **Repositories & Tools** — Access all Workbench repositories
- **Admin Console** — Workbench settings including Work Catalog config
- **My Work** — Active Work Orders using these Scenarios

---

## Related Documentation

- [../../work-catalogues/README.md](../../work-catalogues/README.md) — Work Catalog conceptual overview
- [../../work-catalogues/user-guide/browsing-catalogs.md](../../work-catalogues/user-guide/browsing-catalogs.md) — Browsing guide
- [../../management/work-catalog-management/resolution-algorithm.md](../../management/work-catalog-management/resolution-algorithm.md) — Resolution details
