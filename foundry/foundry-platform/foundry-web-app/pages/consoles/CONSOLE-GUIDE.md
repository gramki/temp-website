# Foundry Web App Console Guide

This guide helps Foundry Platform product, design, and engineering teams decide where capabilities belong in the Workbench Home console structure and when a new console is justified.

## Core console groups

| Console group | Primary question |
|---------------|------------------|
| **Work** | What orchestration items exist? What's their progress? What rituals drive the work? |
| **Workspaces** | What's happening in each Workspace? Who's working where? What sessions are active? |
| **Build** | What is the engineering/build/release state of artifacts and systems? |
| **Workforce** | Who or what is doing the work, with what capacity, contribution, and recognition? |
| **Governance** | Is the work healthy, controlled, evidenced, authorized, efficient, compliant, and improving? |
| **Resources** | Where are repositories, tools, and external systems? |
| **Settings** | How is the Workbench configured? |

## Work consoles

Use Work consoles when the primary object is orchestration items, progress tracking, work rituals, or personal work views.

Belongs here:

- orchestration items (Product Intent, Discovery Case, Release Intent);
- progress by Orchestration / Track / Workspace / Initiative / Release;
- burndown and say/do ratio;
- work rituals (standups, sprint ceremonies, kanban boards);
- personal work views (my day, my week, my month);
- blocked items and attention queues.

Examples:

- Work Overview
- Orchestration
- Progress
- Rituals
- My Work

Do not put workspace execution details, team/agent management, governance authority, risk/debt registers, or repository configuration in Work.

## Workspaces consoles

Use Workspaces consoles when the primary object is execution within a specific Workspace type.

Belongs here:

- Workspace Sessions;
- Work Orders within a Workspace;
- Session capacity and distribution;
- Workspace-specific queues and work execution.

Examples:

- Workspaces Overview
- Product Specification
- UX Design
- Development
- QA
- Release Workspace
- Governance Workspace

Each of the 6 ACE Workspace types has its own console for focused execution view. Workspaces Overview provides the cross-workspace landing.

## Workforce consoles

Use Workforce consoles when the primary object is people, teams, agents, roles, capacity, contribution, or recognition.

Belongs here:

- human contributors;
- agents;
- teams;
- roles;
- capacity and workload;
- contribution and effectiveness;
- availability;
- Kudos / Recognition entries;
- agent/human task split.

Examples:

- Workforce Overview
- Team Console
- Agent Console

Kudos / Recognition belongs here because the system of record is the Workforce Repository. Workforce Overview provides a landing page with combined team and agent summary.

## Governance consoles

Use Governance consoles when the primary question is whether the work system is healthy, controlled, evidenced, authorized, efficient, compliant, and improving.

Belongs here:

- Governance Rituals;
- Governance Enforcement;
- Control Objectives;
- Control Objective Indicators;
- evidence completeness;
- Debt + Catch-Up;
- Exceptions / Waivers;
- risks;
- compliance obligations;
- governance findings;
- approvals / rejections;
- cost / velocity / efficiency governance;
- operating health indicators;
- release readiness.

Examples:

- Governance Overview
- Rituals
- Controls & Enforcement
- Registers
- Reports & Dashboards
- Quality Controls

## Work vs Governance boundary

### Sprint Planning

Sprint Planning is a Work / Team Operating Cadence.

Governance may check:

- planning occurred;
- commitments were recorded;
- capacity was considered;
- dependencies were identified;
- repeated overcommitment triggers Evolve.

### Velocity

Raw velocity charts belong in Progress.

Velocity below a Control Objective belongs in Governance Overview / Reports & Dashboards.

### Team overload

Team workload belongs in Team Console.

Repeated overcapacity risk belongs in Governance Registers and Monthly Workbench Governance Review.

## When to expand an existing console

Expand an existing console when:

1. the new capability answers the same primary user question;
2. the same persona uses it in the same workflow;
3. it shares the same primary entity;
4. it can be a tab, filter, panel, or detail view;
5. separating it would confuse users.

Examples:

| Need | Expand | Why |
|------|--------|-----|
| Product Intent type filter | Orchestration | Same entity, filter is enough |
| Governance status on orchestration item | Orchestration | Overlay badge, not separate console |
| Work Order governance badges | Workspace consoles | Overlay badge on existing queue |
| Team recognition (Kudos) | Team Console | Workforce data, same persona |
| Agent cost per task | Agent Console | Analytics view on same entity |
| Debt aging chart | Registers | Same register entity, analytics view |
| Build quality threshold breach | Quality Controls (Governance) | Governance evaluates build thresholds |
| Test coverage trends | Quality Status (Build) | Build-time quality metrics |
| Release readiness status | Release Artifacts + Governance overlay | Release owns status; Governance adds gate badge |

## When to create a new console

Create a new console when:

1. it answers a distinct primary question;
2. it has its own primary entity or workflow;
3. it has multiple tabs, details, and actions;
4. it serves a distinct operating role;
5. it needs first-class navigation.

Examples:

| Need | New console? | Why |
|------|--------------|-----|
| Manage all governance obligation registers | Yes: Registers | Risk/debt/exception/compliance/finding workflows are distinct. |
| Configure authority matrix | Yes or Settings tab | Distinct admin workflow. |
| View governance health | Yes: Governance Overview | Cross-governance landing page. |
| Manage rituals | Yes: Rituals | Distinct cadence/event workflow. |
| Show one risk badge on Product Intent | No | PI overlay is enough. |
| Show agent recognition | No | Team/Agent consoles own workforce recognition. |
| View all controls/enforcement | Yes: Controls & Enforcement | Distinct control evaluation workflow. |

## Console type patterns

Console types describe the interaction pattern, independent of which group (Work, Workforce, etc.) the console belongs to.

| Type | Meaning | Primary interaction |
|------|---------|---------------------|
| **Landing** | Overview / health / summary | Scan, triage, navigate |
| **Queue** | Items needing action | Pick up, process, complete |
| **List + Detail** | Browse entities, drill into one | Browse, select, inspect |
| **Analytics** | Metrics, trends, reports | Analyze, export, share |
| **Workflow** | Multi-step process management | Configure, schedule, review |
| **Admin** | Configuration and permissions | Configure, authorize |
| **Resource** | Repositories / tools / external systems | Access, link, manage |

## Console type examples

| Group      | Console                     | Type(s)                   |
|------------|-----------------------------|---------------------------|
| Work       | **Work Overview**           | Landing                   |
| Work       | **Orchestration**           | List + Detail             |
| Work       | **Progress**                | Analytics                 |
| Work       | **Rituals**                 | Workflow                  |
| Work       | **My Work**                 | Landing                   |
| Workspaces | **Workspaces Overview**     | Landing                   |
| Workspaces | **Product Specification**   | Queue, List + Detail      |
| Workspaces | **UX Design**               | Queue, List + Detail      |
| Workspaces | **Development**             | Queue, List + Detail      |
| Workspaces | **QA**                      | Queue, List + Detail      |
| Workspaces | **Release Workspace**       | Queue, List + Detail      |
| Workspaces | **Governance Workspace**    | Queue, List + Detail      |
| Build      | **CI Console**              | Queue, Analytics          |
| Build      | **Components Console**      | List + Detail             |
| Build      | **Findings Console**        | Queue, Analytics          |
| Build      | **Quality Status**          | Analytics                 |
| Build      | **Release Artifacts**       | List + Detail, Workflow   |
| Workforce  | **Workforce Overview**      | Landing                   |
| Workforce  | **Team Console**            | List + Detail, Analytics  |
| Workforce  | **Agent Console**           | List + Detail, Analytics  |
| Governance | **Governance Overview**     | Landing                   |
| Governance | **Rituals**                 | Workflow                  |
| Governance | **Controls & Enforcement**  | List + Detail, Workflow   |
| Governance | **Registers**               | Queue, List + Detail      |
| Governance | **Reports & Dashboards**    | Analytics                 |
| Governance | **Quality Controls**        | List + Detail, Workflow   |
| Resources  | **Repositories & Tools**    | Resource                  |
| Settings   | **Admin Console**           | Admin                     |
| Settings   | **Governance Admin**        | Admin                     |

## Detail pages vs consoles

Some consoles have **detail pages** — standalone pages for deep inspection of a single entity, accessible via URL.

| Detail page | Parent console | URL pattern |
|-------------|----------------|-------------|
| Orchestration Item Details | Orchestration | `/workbenches/{id}/orchestration/{type}/{itemId}` |
| Team Member Workbench Profile | Team Console | `/workbenches/{id}/team/{memberId}` |
| Workspace Session Details | Workspace consoles | `/workbenches/{id}/sessions/{sessionId}` |

Detail pages are appropriate when:
- The entity has enough content for a full page (history, metrics, actions).
- Multiple consoles need to link to the same entity view.
- The URL must be shareable and bookmarkable.

Detail pages are NOT new consoles — they don't appear in side navigation.

## New console checklist

Before adding a new console, answer:

1. What user question does this console answer?
2. Who is the primary persona?
3. What is the primary entity?
4. What actions does the user perform?
5. What existing console almost covers it?
6. Why is a tab/panel insufficient?
7. What module owns the data?
8. What repository/entity is source of truth?
9. Is this Phase 1, Phase 2, or later?
10. What would be confusing if this were not first-class?

## Phase maturity guidance

| Maturity | Console guidance |
|----------|------------------|
| Phase 1 | All consoles listed in README.md exist. Focus on core workflows: Work Overview, Orchestration, Workspaces Overview + per-workspace consoles, Governance Overview, Registers, Controls & Enforcement. Detail pages for Orchestration Items, Team Member Profile, and Workspace Session. |
| Phase 2 | Richer Progress analytics, full Rituals coverage (sprint and kanban), fuller Registers workflows, release governance overlays, workforce recognition views, advanced Team/Agent analytics. |
| Phase 3 | Full Governance Admin with authority matrix editor, control inheritance UI, cross-Workbench governance views, recognition trend analytics, My Work personalization, advanced detail pages. |

## Canonical statement

Work consoles show orchestration items, progress, and rituals. Workspaces consoles show execution within each Workspace type. Workforce consoles show the people and agents doing the work. Governance consoles show whether the work system is healthy, controlled, evidenced, authorized, efficient, compliant, and improving. A new console is justified only when it answers a distinct user question that cannot be served clearly as a tab, panel, or overlay inside an existing console.
