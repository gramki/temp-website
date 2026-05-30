# Foundry Work Catalogs Settings

**URL pattern:** `/foundries/{foundryId}/settings/work-catalogs`

**Purpose:** Manage Foundry-level Work Catalog content — OI Workflows and Scenarios that apply to all Workshops in the Foundry.

---

## Page Sections

### 1. Foundry Catalog Overview

| Element | Description |
|---------|-------------|
| **Repository link** | Link to `foundry-{id}/work-catalog/` in GitHub |
| **Last sync** | When catalog was last synced to Metadata Service |
| **Item count** | Number of OI Workflows and Scenarios defined at Foundry level |
| **Platform version** | Version of Platform defaults this Foundry inherits from |

### 2. Catalog Browser

#### Foundry-Defined Content

Lists content defined at the Foundry level (not inherited from Platform):

| Tab | Content |
|-----|---------|
| **OI Workflows** | Workflows defined in Foundry catalog |
| **Scenarios** | Scenarios defined in Foundry catalog |

| Column | Description |
|--------|-------------|
| **Name/ID** | Item identifier |
| **Track/Workspace** | Where it applies |
| **Status** | Active, Draft, Deprecated |
| **Overrides Platform** | Whether it overrides a Platform definition |
| **Used by** | Count of Workshops inheriting this definition |

#### Platform Defaults

Shows Platform defaults and their override status:

| Column | Description |
|--------|-------------|
| **Name/ID** | Item identifier |
| **Platform version** | Version in Platform defaults |
| **Overridden here** | Whether Foundry has an override |
| **Action** | Override, View |

### 3. Effective Catalog Preview

Preview the effective catalog for any Workshop or Workbench:

| Element | Description |
|---------|-------------|
| **Workshop selector** | Choose a Workshop |
| **Workbench selector** | Optional: drill down to Workbench |
| **Effective view** | Merged catalog for selection |
| **Source indicators** | Visual badges showing source level |

### 4. User Catalog Policy

Configure organization-wide policy for User Work Catalogs:

| Setting | Options | Description |
|---------|---------|-------------|
| **User catalogs enabled** | Yes/No | Allow users to create personal catalogs |
| **Default activation** | Opt-in/Opt-out | Default state for new users |
| **Auto-provisioning** | On first use/Manual | When to create user catalog repos |

---

## Actions

### Management Actions

| Action | Who | Description |
|--------|-----|-------------|
| Open in GitHub | Foundry Admin | Open Foundry catalog repo |
| Sync now | Foundry Admin | Force sync to Metadata Service |
| View sync history | Foundry Admin | See sync events and errors |
| Update Platform version | Foundry Admin | Upgrade to newer Platform defaults |

### Content Actions

| Action | Who | Description |
|--------|-----|-------------|
| Add OI Workflow | Foundry Admin | Create new workflow (opens IDE) |
| Add Scenario | Foundry Admin | Create new scenario (opens IDE) |
| Override Platform item | Foundry Admin | Create Foundry-level override |
| Remove override | Foundry Admin | Revert to Platform definition |
| Deprecate | Foundry Admin | Mark item as deprecated |

### Promotion Actions

| Action | Who | Description |
|--------|-----|-------------|
| Accept from Workshop | Foundry Admin | Accept promotion request from Workshop |
| Submit to Platform | Foundry Admin | Propose for inclusion in Platform defaults |

---

## Inheritance Model

```
Platform defaults (work-catalogues/platform-defaults/)
    │
    └── Foundry catalog (this level)
            │
            ├── Workshop A catalog
            │       ├── Workbench 1
            │       └── Workbench 2
            │
            └── Workshop B catalog
                    └── ...
```

Foundry-level content:
- **Overrides** Platform definitions (same ID = replacement)
- **Extends** with Foundry-specific content (new IDs)
- **Is inherited by** all Workshops and Workbenches in this Foundry

---

## Platform Upgrade Workflow

When a new Platform version is available:

1. **Review changes** — See what's new, changed, or deprecated
2. **Compatibility check** — Verify Foundry overrides still make sense
3. **Test in Workshop** — Test new Platform content in a test Workshop
4. **Apply upgrade** — Update Foundry to new Platform version
5. **Propagate** — Changes flow to all Workshops and Workbenches

---

## Governance

| Policy | Description |
|--------|-------------|
| **PR required** | All Foundry catalog changes require PR |
| **Reviewer approval** | At least one Foundry Admin must approve |
| **Validation required** | Validation module must pass (`foundry-validation` check) |
| **Sync verification** | Changes verified in Metadata Service after merge |
| **Change log** | All changes recorded for audit |

---

## Related Pages

- **Workshop Settings > Work Catalogs** — Workshop-level catalog management
- **Workbench Consoles > Work Catalogs** — Effective catalog view for Workbenches
- **Foundry Settings > General** — Foundry configuration

---

## Related Documentation

- [../../work-catalogues/README.md](../../work-catalogues/README.md) — Work Catalog overview
- [../../work-catalogues/user-guide/publishing-workflow.md](../../work-catalogues/user-guide/publishing-workflow.md) — Publishing and promotion guide
- [../../management/platform-developer-guide/validation/README.md](../../../../management/platform-developer-guide/validation/README.md) — Validation module
