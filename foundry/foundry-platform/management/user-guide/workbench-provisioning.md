# Provisioning a New Workbench

## Purpose

This guide walks through the complete process of provisioning a new Workbench — the locus where a Product is evolved — from request submission through automated setup to a fully operational product workspace.

## Audience

| Role | When to use this guide |
|------|------------------------|
| Workshop Admin | When creating a new Workbench for a product within your Workshop |
| Foundry Admin | When assisting Workshop Admins with Workbench provisioning |

## Prerequisites

- **Access:** Workshop Admin role or higher in the target Workshop
- **Workshop:** Parent Workshop must exist and be active
- **GitHub:** Foundry GitHub App must be installed on the target GitHub organization
- **Jira:** Workshop must have Jira integration configured
- **Prior reading:** [Workshop provisioning](workshop-provisioning.md), [Workbench architecture](workbench-architecture.md)

---

## When to Create a Workbench vs a Workshop

Use this decision tree before provisioning:

```
Does this product belong to an existing business unit / team structure?
│
├─ YES → Is there already a Workshop for that business unit?
│        │
│        ├─ YES → Create a Workbench within that Workshop
│        │
│        └─ NO  → Create a Workshop first, then create the Workbench
│
└─ NO  → Is this a cross-cutting platform or shared service?
         │
         ├─ YES → Create a dedicated Workshop, then create the Workbench
         │
         └─ NO  → Consult your Foundry Admin about organizational placement
```

**Key distinctions:**

| Construct | Scope | When to create |
|-----------|-------|----------------|
| **Workshop** | Business unit, department, or product line | New organizational boundary, new team structure, different governance needs |
| **Workbench** | Individual product within a Workshop | New product, new service, new system within an existing team structure |

**Examples:**

| Situation | Create |
|-----------|--------|
| New "Checkout Service" for the Retail team | Workbench (in existing "Retail" Workshop) |
| New "Platform Infrastructure" team forming | Workshop (then Workbenches for each platform product) |
| Second product for an existing team | Workbench (in the team's existing Workshop) |
| Splitting a monolith into microservices | Multiple Workbenches (in the same Workshop) |

---

## Steps

### 1. Navigate to the Workshop and initiate provisioning (Workshop Admin)

In the Foundry Web App, navigate to your Workshop and click **Create Workbench**.

```
Foundry Web App
└── Workshops
    └── {Your Workshop}
        └── Workbenches
            └── [+ Create Workbench]
```

### 2. Provide Workbench details (Workshop Admin)

Fill in the Workbench creation form:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Human-readable Workbench name (e.g., "Checkout Service") |
| `product_code` | Yes | Unique identifier within the Workshop (e.g., "checkout") |
| `description` | Yes | Brief description of the product |
| `github_org` | Yes | GitHub organization (existing or new) |
| `raw_agents` | No | Raw Agents to enable (defaults inherited from Workshop) |

Example request payload:

```json
{
  "workshop_id": "ws-acme-retail",
  "name": "Checkout Service",
  "product_code": "checkout",
  "description": "Customer checkout and payment processing",
  "config": {
    "raw_agents": ["cursor-agent", "copilot"],
    "github_org": "acme-retail"
  }
}
```

### 3. Submit the creation request (Workshop Admin)

Click **Create Workbench**. The platform validates your request:

| Validation | What is checked |
|------------|-----------------|
| Workshop exists | Workshop is active |
| Product code unique | No existing Workbench in Workshop with this code |
| User permissions | You have Workshop Admin role |
| GitHub org | Org exists OR can be created |
| Jira integration | Configured at Workshop level |

If validation passes, a Workbench record is created with status **provisioning**.

### 4. Wait for GitHub setup (Platform)

The platform configures GitHub resources:

| Step | What happens |
|------|--------------|
| **Resolve GitHub org** | Verifies Foundry GitHub App is installed with required permissions |
| **Create Intent repo** | Creates `{product_code}-intent` repository with scaffold |
| **Create Design repo** | Creates `{product_code}-design` repository with scaffold |
| **Configure webhooks** | Sets up webhooks for push and pull request events |
| **Register Atropos tenant** | Registers Foundry with Olympus event fabric for module callbacks |

**Event transport:** Module coordination uses Atropos HTTP callbacks at `/{foundry-id}/foundry.{module}.{event}`. See [event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md).

**Intent Repository scaffold:**

```
{product_code}-intent/
├── README.md
├── .foundry/
│   └── config.yaml
└── intents/
    └── .gitkeep
```

**Design Repository scaffold:**

```
{product_code}-design/
├── README.md
├── .foundry/
│   └── config.yaml
├── mockups/
├── visual-designs/
└── prototypes/
```

### 5. Wait for Jira setup (Platform)

The platform configures Jira resources:

| Step | What happens |
|------|--------------|
| **Create Work Orders project** | Creates `{PRODUCT_CODE}-WO` project for Work Orders |
| **Configure custom fields** | Creates Foundry-specific fields for scenario tracking |
| **Configure issue types** | Ensures Epic, Story, Sub-task are available |
| **Link shared projects** | Links Operations and Feedback projects from Workshop |
| **Configure webhooks** | Sets up webhooks for issue events |

**Custom fields created:**

| Field | Type | Purpose |
|-------|------|---------|
| `foundry-scenario` | Text | Scenario identifier |
| `foundry-orchestration-item` | Text | Parent PI/DC/etc. |
| `foundry-workbench` | Text | Workbench ID |
| `foundry-wo-label` | Text | WO label for workflow |
| `foundry-wo-group` | Text | WO Group label |
| `foundry-parent-wo` | Text | Parent WO (for delegated tasks) |
| `foundry-task-workspace` | Text | Workspace session ID |

### 6. Wait for internal services setup (Platform)

The platform provisions internal services:

| Service | What happens |
|---------|--------------|
| **Metadata Service** | Creates instance with ID sequences for PI, RI, WO |
| **Ontology Service** | Creates instance with initial product structure |
| **Health check** | Verifies both services are responding |

### 7. Wait for Workshop Definition Repository setup (Platform)

The platform creates the Workbench scaffold in the Workshop Definition Repository:

```
workshop-{workshop-slug}/
└── workbenches/
    └── {product_code}/
        ├── config.yaml
        ├── knowledge/
        │   └── README.md
        ├── workspaces/
        │   ├── product-specification/
        │   │   ├── .devcontainer/
        │   │   ├── scenarios/
        │   │   │   └── catalog.yaml
        │   │   └── trained-agents/
        │   ├── ux-design/
        │   ├── development/
        │   ├── qa/
        │   ├── release/
        │   └── governance/
        └── integrations.yaml
```

**Workbench config.yaml:**

```yaml
name: {Workbench name}
product_code: {product_code}
description: {description}

raw_agents:
  - cursor-agent
  - copilot

defaults:
  workRepoProject: {PRODUCT_CODE}-WO   # Work Repository project key (Jira adapter in Phase 1)
  github_org: {github_org}
```

See [../../../foundry-work-plan/phase-1/repository-contracts.md](../../../foundry-work-plan/phase-1/repository-contracts.md) for entity and label conventions.

### 8. Create the default team (Workshop Admin)

After provisioning completes, create the initial team:

```json
POST /api/v1/workbenches/{workbench_id}/teams
{
  "name": "{Product} Team",
  "description": "Core team for {Product} development",
  "workspace_types": ["development", "qa", "release"]
}
```

### 9. Add team members (Workshop Admin)

Add team members with appropriate roles:

| Role | Capabilities |
|------|--------------|
| `admin` | Full Workbench configuration, manage teams, add Scenario Catalogs |
| `member` | Access Workspaces, execute Scenarios, add components |

```json
POST /api/v1/workbenches/{workbench_id}/teams/{team_id}/members
{
  "user_id": "alice@acme.com",
  "role": "admin"
}
```

Team members are automatically synced to the GitHub organization with appropriate permissions.

### 10. Verify activation (Workshop Admin)

The platform performs final validation and activates the Workbench:

| Check | Requirement |
|-------|-------------|
| GitHub repos | Accessible |
| Jira project | Configured |
| Metadata Service | Healthy |
| Ontology Service | Healthy |
| Repository scaffold | Committed |
| Team | At least one exists |

Status updates to **active** and notifications are sent.

---

## Expected outcome

After completing all steps:

- Workbench status is **Active**
- GitHub repositories created: `{product_code}-intent`, `{product_code}-design`
- Jira project created: `{PRODUCT_CODE}-WO`
- Metadata Service and Ontology Service running
- Workshop Definition Repository contains Workbench scaffold
- Team created with at least one admin member
- Workbench appears in the Workshop's Workbench list

---

## Provisioning Timeline

| Phase | Typical Duration | Can Fail? |
|-------|------------------|-----------|
| Validation | < 1s | Yes |
| GitHub Setup | 5–15s | Yes |
| Jira Setup | 5–10s | Yes |
| Metadata Service | 2–5s | Yes |
| Ontology Service | 2–5s | Yes |
| Repository Scaffold | 3–5s | Yes |
| **Total** | **20–45s** | |

---

## Post-Provisioning Tasks

Once active, the Workbench Admin can:

1. **Add code repositories** — Link existing repos to the Workbench
2. **Configure additional integrations** — Add Figma, TestRail, etc.
3. **Define Scenarios** — Create scenario definitions in workspace folders
4. **Define Trained Agents** — Create agent manifests for scenarios
5. **Create first Product Intent** — Start the product evolution cycle

---

## Related

### Concepts

- [Containment Hierarchy](../../concepts/containment-hierarchy.md) — Foundry → Workshop → Workbench → Workspace nesting structure
- [Repositories](../../concepts/repositories.md) — The 15 canonical repository types
- [Metadata Service](../../concepts/metadata-service.md) — Central configuration store
- [Declarative Provisioning](../concepts/declarative-provisioning.md) — Admins describe desired state (module-specific)

### Guides

- [Workbench architecture](workbench-architecture.md) — What a Workbench contains and how it works
- [Workshop provisioning](workshop-provisioning.md) — Creating Workshops (parent of Workbenches)
- [Workshop Definition Repository](../platform-developer-guide/workshop-repository.md) — Repository structure
- [Product Intent journey](../../orchestrator/user-guide/product-intent-journey.md) — What happens after Workbench is ready
- [Management README](README.md) — Foundry Management overview

---

## Troubleshooting

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Validation fails: "Workshop not found" | Workshop ID incorrect or Workshop not active | Verify Workshop exists and is active; check Workshop ID |
| Validation fails: "Product code not unique" | Another Workbench uses this code | Choose a different product code |
| GitHub repo creation fails | GitHub App not installed or insufficient permissions | Verify Foundry GitHub App is installed on the org with `repo:admin`, `org:read` |
| Jira project creation fails | OAuth token expired or insufficient permissions | Re-authorize Jira connection; verify account has project creation permissions |
| Metadata Service provisioning fails | Infrastructure issue | Check service logs; contact infrastructure team if persistent |
| Workbench stuck in "provisioning" | One or more provisioning steps failed | Check error details in UI; retry failed step or contact support |
| Team sync fails | GitHub org membership issues | Verify team members have GitHub accounts; check GitHub App permissions |
| "No Jira integration" error | Workshop-level Jira not configured | Workshop Admin must configure Jira integration on the Workshop first |
