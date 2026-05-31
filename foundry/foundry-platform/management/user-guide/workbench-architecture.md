# Understanding Workbench Architecture

## Purpose

This document explains what a Workbench is, how it is structured, and how it supports product evolution. It provides a conceptual overview for administrators and team leads who need to understand Workbench capabilities without diving into implementation details.

## Audience

| Role | When to use this guide |
|------|------------------------|
| Foundry Admin | When designing Workbench strategy for the organization |
| Workshop Admin | When planning Workbench provisioning and configuration |
| Workbench Manager | When onboarding team members or explaining Workbench structure |

## Prerequisites

- Familiarity with [Foundry Management concepts](../README.md)
- Understanding of the Workshop → Workbench hierarchy
- Prior reading: [Workbench provisioning](workbench-provisioning.md)

---

## The Workbench Analogy

A Foundry Workbench is like a physical workbench in a repair shop: a dedicated surface where skilled workers (human or agent) perform specialized tasks using the right tools for the job.

Just as a bike repair workbench has dedicated workspaces — one for precision wheel truing, another for hydraulic work, a third for drivetrain cleaning — a Foundry Workbench has six standard Workspaces: Product Specification, UX Design, Development, QA, Release, and Governance. Each Workspace has its own tools (Scenarios), its own specialists (Skilled Agents), and its own part of the product to focus on.

The Workbench itself provides the shared infrastructure: the bench surface (repositories), the tool storage (Capable Agents), the parts catalog (Ontology), and the work tracking system (Jira integration). Workers move between Workspaces as needed, but each Workspace maintains its specialized focus.

---

## Workbench Identity

Each Workbench has a **single Workbench ID** used as the identity for all external integrations:

| Integration | How Workbench ID is used |
|-------------|--------------------------|
| Metadata Service | Identifier for all metadata operations |
| OAuth clients | Client ID for Figma, TestRail, Jira, Weave |
| GitHub App | Association with GitHub organization |
| Olympus Weave | Publisher identity |

This unified identity simplifies credential management and audit trails.

---

## Workbench Structure

A Workbench contains these key components:

| Component | Purpose |
|-----------|---------|
| **Metadata Service** | Commit tracking, ID generation, code repo references |
| **Ontology Service** | Product structure, capabilities, features |
| **Quality Service** | Unified access to TestRail and automation repos |
| **GitHub Organization** | Code storage with Intent, Design, and Code repositories |
| **Jira Integration** | Work Orders, Operations, Feedback tracking |
| **Olympus Weave** | Deployment publishing and tracking |
| **Capable Agents** | AI agents available for automation |
| **Standard Workspaces** | Six specialized areas for product work |
| **Team** | Managers and Members with defined permissions |

---

## Standard Workspaces

Every Workbench has these six Workspaces:

| Workspace | Purpose | Key activities |
|-----------|---------|----------------|
| **Product Specification** | Translate Intent to specs | Write PSDs, refine requirements |
| **UX Design** | Design user experience | Create mockups, prototypes |
| **Development** | Build the solution | Write code, implement features |
| **QA** | Verify and validate | Test, report findings |
| **Release** | Publish artifacts | Build releases, deploy |
| **Governance** | Validate transitions | Review gates, approvals |

Workbench Managers can add **Scenario Catalogs** to each Workspace to define available automation.

---

## Repository Structure

A Workbench manages several types of repositories:

| Repository | What it contains | Storage |
|------------|------------------|---------|
| **Intent** | Product Intents, PDRs, PSDs | GitHub (Intent Repository) |
| **Design** | Design artifacts, visual designs | GitHub (per Workbench) |
| **Code** | Source code for Systems/Components | GitHub (multiple repos) |
| **Quality Automation** | Test automation scripts | GitHub (per Workbench) |
| **Work Orders** | Execution tracking (Work Items) | Work Repository — dedicated `workRepoProject` |
| **Operations** | Incidents, problems | Work Repository — shared project, `foundry-workbench-{workbenchId}` label |
| **Feedback** | Bug reports, FIRs | Work Repository — shared project, `foundry-workbench-{workbenchId}` label |

All GitHub repositories are tagged with Foundry, Workshop, and Workbench identifiers for traceability.

---

## Team Structure

Workbench teams have two primary roles:

| Role | What they can do |
|------|------------------|
| **Manager** | Manage repositories, add Scenario Catalogs, configure integrations |
| **Member** | Access Workspaces, execute Scenarios, add components |

Both Managers and Members receive **repo-level** GitHub access. Organization-level management is handled exclusively through the Workbench interface — no direct org admin access is granted.

---

## Capable Agents

Capable Agents are AI systems (IDE agents, CLI agents) that can perform automated work in Scenarios. They are configured hierarchically:

```
Foundry (organization defaults)
    └── Workshop (team overrides)
            └── Workbench (product overrides)
```

| Configuration aspect | Inheritance behavior |
|---------------------|---------------------|
| **Enable/disable** | Disabled at parent = disabled for all children |
| **Credentials** | Resolved upward (Workbench → Workshop → Foundry) |
| **Model selection** | Configured at each level |

This hierarchy allows organization-wide policies while permitting product-specific customization.

---

## External Integrations

Workbenches can connect to external tools via OAuth:

| Tool | What it provides |
|------|------------------|
| **GitHub** | Repository management, commit tracking |
| **Figma** | Design file viewing and linking |
| **TestRail** | Test case management |
| **Jira** | Work tracking and issue management |
| **Olympus Weave** | Deployment and version tracking |

Additional tools can be linked as URL references for manual navigation.

---

## Expected Outcome

After understanding this architecture, you should be able to:

- Explain the Workbench analogy to team members
- Describe how Workspaces organize different types of work
- Identify which repositories store what content
- Understand the team permission model
- Configure Capable Agents appropriately for your product

---

## Related

- [workbench-provisioning.md](workbench-provisioning.md) — How to create a new Workbench
- [foundry-settings.md](foundry-settings.md) — Settings that cascade to Workbenches
- [../platform-developer-guide/workbench-architecture.md](../platform-developer-guide/workbench-architecture.md) — Implementation details
- [../platform-developer-guide/workshop-repository.md](../platform-developer-guide/workshop-repository.md) — Workshop Definition Repository structure
- [../../agent-fabric/user-guide/skilled-agents.md](../../agent-fabric/user-guide/skilled-agents.md) — Skilled Agents conceptual overview
- [README.md](README.md) — Foundry Management user guide overview

---

## Troubleshooting

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Cannot see Workbench in UI | Permissions not granted | Contact Workshop Admin to verify team membership |
| Repositories not appearing | GitHub App not installed | Verify Foundry GitHub App is installed on the org |
| Jira issues not syncing | Label filter misconfigured | Verify `foundry-workbench-{workbenchId}` labels in Admin Console |
| Capable Agent not available | Disabled at higher level | Check Foundry/Workshop settings for agent configuration |
| Cannot add Scenario Catalog | Not a Manager | Request Manager role from Workbench Admin |
