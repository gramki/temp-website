# Components Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/components`

**Group:** Build

**Purpose:** Ontology navigation — browse and manage Systems, capabilities, features.

---

## Page Sections

### 1. Product Structure Tree

```
Product (Workbench)
├── System A
│   ├── Capability 1
│   │   ├── Feature 1.1
│   │   └── Feature 1.2
│   └── Capability 2
├── System B
│   └── ...
└── System C
```

| Element | Description |
|---------|-------------|
| **Tree view** | Hierarchical product structure |
| **Expand/collapse** | Navigate the hierarchy |
| **Search** | Find by name |
| **Maturity indicators** | Status of each component |

### 2. Component Detail View

| Element | Description |
|---------|-------------|
| **Name** | Component identifier |
| **Type** | System, Capability, Feature |
| **Description** | What it does |
| **Olympus Product Module code** | For Systems (from Weave) |
| **Code repository** | Linked source repo |
| **Related PIs** | Product Intents touching this component |
| **Dependencies** | What it depends on |
| **Dependents** | What depends on it |

### 3. System Cards

| Element | Description |
|---------|-------------|
| **System name** | Identity |
| **Olympus Product Module code** | Weave identifier |
| **Repository** | Linked code repo |
| **Capabilities count** | How many capabilities |
| **Latest version** | Most recent release |
| **Deployment status** | From Weave |

### 4. Dependency Graph

| Element | Description |
|---------|-------------|
| **Visual graph** | Component dependencies |
| **Impact analysis** | What's affected by changes |
| **Circular detection** | Flag circular dependencies |

### 5. Supply Chain Tab

Software Bill of Materials (SBOM) and dependency inventory for each component.

#### SBOM Overview

| Element | Description |
|---------|-------------|
| **Component selector** | Choose System or component to view |
| **SBOM format** | CycloneDX, SPDX export options |
| **Last generated** | When SBOM was last updated |
| **Total dependencies** | Direct + transitive count |

#### Dependency List

| Column | Description |
|--------|-------------|
| **Name** | Dependency package name |
| **Version** | Currently used version |
| **Latest** | Latest available version |
| **Type** | Direct or transitive |
| **License** | SPDX license identifier |
| **Source** | Package registry (npm, Maven, PyPI, etc.) |
| **Used by** | Which components use this dependency |

#### Dependency Graph

| Element | Description |
|---------|-------------|
| **Tree view** | Hierarchical dependency tree |
| **Graph view** | Visual dependency graph |
| **Depth filter** | Limit transitive depth |
| **Highlight outdated** | Flag dependencies behind latest |

#### License Summary

| Element | Description |
|---------|-------------|
| **License distribution** | Breakdown by license type |
| **Approved licenses** | Count on approved list |
| **Unapproved licenses** | Count requiring review |
| **License details** | Per-dependency license info |

#### Supply Chain Actions

| Action | Who | Description |
|--------|-----|-------------|
| **Export SBOM** | All | Download CycloneDX or SPDX format |
| **View dependency** | All | See dependency details, where used |
| **Check for updates** | Engineer | See available upgrades |
| **View findings** | All | Jump to Findings Console filtered by this dependency |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Add System | Manager | Register new System (gets Olympus code from Weave) |
| Add Capability | Manager | Add capability to System |
| Add Feature | Manager | Add feature to Capability |
| Edit component | Manager | Update name, description |
| Link repository | Manager | Associate code repo |
| View dependencies | All | See dependency graph |

---

## Filters

- By type (System, Capability, Feature)
- By maturity status
- By repository
- Search by name

---

## Integrations

- **Ontology Service** — Source of product structure
- **Olympus Weave** — Olympus Product Module codes for Systems
- **Metadata Service** — Code repo references

---

## Related Consoles

- **Findings Console** — Vulnerabilities, license violations derived from Supply Chain
- **Release Artifacts** — Deployments by System
- **CI Console** — Builds by repository
- **Repositories & Tools** — Code repos
