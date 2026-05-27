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

- **Release Console** — Deployments by System
- **CI Console** — Builds by repository
- **Repositories & Tools** — Code repos
