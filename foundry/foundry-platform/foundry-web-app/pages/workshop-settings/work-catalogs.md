# Workshop Work Catalogs Settings

**URL pattern:** `/workshops/{workshopId}/settings/work-catalogs`

**Purpose:** Manage Workshop-level Work Catalog content — OI Workflows and Scenarios that apply to all Workbenches in the Workshop.

---

## Page Sections

### 1. Workshop Catalog Overview

| Element | Description |
|---------|-------------|
| **Repository link** | Link to `workshop-{id}/work-catalog/` in GitHub |
| **Last sync** | When catalog was last synced to Metadata Service |
| **Item count** | Number of OI Workflows and Scenarios defined at Workshop level |
| **Inheritance from** | Foundry catalog this Workshop inherits from |

### 2. Catalog Browser

#### Workshop-Defined Content

Lists content defined at the Workshop level (not inherited):

| Tab | Content |
|-----|---------|
| **OI Workflows** | Workflows defined in Workshop catalog |
| **Scenarios** | Scenarios defined in Workshop catalog |

| Column | Description |
|--------|-------------|
| **Name/ID** | Item identifier |
| **Track/Workspace** | Where it applies |
| **Status** | Active, Draft, Deprecated |
| **Overrides** | Whether it overrides a Foundry or Platform definition |
| **Used by** | Count of Workbenches using this definition |

#### Inherited Content

Shows what this Workshop inherits from Foundry and Platform:

| Column | Description |
|--------|-------------|
| **Name/ID** | Item identifier |
| **Source** | Foundry or Platform |
| **Overridden here** | Whether Workshop has an override |

### 3. Effective Catalog Preview

Preview the effective catalog for any Workbench in this Workshop:

| Element | Description |
|---------|-------------|
| **Workbench selector** | Choose a Workbench to preview |
| **Effective view** | Merged catalog for selected Workbench |
| **Source indicators** | Visual badges showing source level |

---

## Actions

### Management Actions

| Action | Who | Description |
|--------|-----|-------------|
| Open in GitHub | Workshop Admin | Open Workshop catalog repo |
| Sync now | Workshop Admin | Force sync to Metadata Service |
| View sync history | Workshop Admin | See sync events and errors |

### Content Actions

| Action | Who | Description |
|--------|-----|-------------|
| Add OI Workflow | Workshop Admin | Create new workflow (opens IDE) |
| Add Scenario | Workshop Admin | Create new scenario (opens IDE) |
| Override Foundry item | Workshop Admin | Create Workshop-level override |
| Remove override | Workshop Admin | Revert to inherited definition |
| Deprecate | Workshop Admin | Mark item as deprecated |

### Promotion Actions

| Action | Who | Description |
|--------|-----|-------------|
| Promote to Foundry | Workshop Admin | Request promotion to Foundry level |
| Accept from Workbench | Workshop Admin | Accept PR from Workbench |

---

## Workflow: Adding a Workshop Scenario

1. **Click "Add Scenario"** — Opens Scenario Editor in IDE
2. **Author in IDE** — Schema-aware editing with validation
3. **Test in Workbench** — Dry-run in a test Workbench
4. **Create PR** — Submit to Workshop catalog repo
5. **Review & Merge** — Workshop Admin reviews and merges
6. **Auto-sync** — Workshop Sync Service updates Metadata Service

---

## Inheritance Model

```
Platform defaults
    │
    └── Foundry catalog ──────┐
            │                 │
            └── Workshop catalog (this level)
                    │
                    ├── Workbench A catalog
                    ├── Workbench B catalog
                    └── ...
```

Workshop-level content:
- **Overrides** Foundry and Platform definitions (same ID = replacement)
- **Extends** with Workshop-specific content (new IDs)
- **Is inherited by** all Workbenches in this Workshop

---

## Governance

| Policy | Description |
|--------|-------------|
| **PR required** | All Workshop catalog changes require PR |
| **Reviewer approval** | At least one Workshop Admin must approve |
| **Validation required** | Workshop Validation Service must pass |
| **Sync verification** | Changes verified in Metadata Service after merge |

---

## Related Pages

- **Foundry Settings > Work Catalogs** — Foundry-level catalog management
- **Workbench Consoles > Work Catalogs** — Effective catalog view for Workbenches
- **Workshop Settings > General** — Workshop configuration

---

## Related Documentation

- [../../work-catalogues/README.md](../../work-catalogues/README.md) — Work Catalog overview
- [../../work-catalogues/user-guide/authoring-scenarios.md](../../work-catalogues/user-guide/authoring-scenarios.md) — Scenario authoring guide
- [../../management/work-catalog-management/README.md](../../management/work-catalog-management/README.md) — Implementation details
