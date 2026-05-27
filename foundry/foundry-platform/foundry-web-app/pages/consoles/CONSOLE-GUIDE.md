# Foundry Web App Console Guide

This guide helps Foundry Platform product, design, and engineering teams decide where capabilities belong in the Workbench Home console structure and when a new console is justified.

## Core console groups

| Console group | Primary question |
|---------------|------------------|
| **Work** | What work is moving, where is it, and what happens next? |
| **Workforce** | Who or what is doing the work, with what capacity, skill, contribution, and recognition? |
| **Governance** | Is the work healthy, controlled, evidenced, authorized, efficient, compliant, and improving? |
| **Build** | What is the engineering/build/release state of artifacts and systems? |
| **Resources** | Where are repositories, tools, and external systems? |
| **Settings** | How is the Workbench configured? |

## Work consoles

Use Work consoles when the primary object is work movement.

Belongs here:

- orchestration item state;
- Work Orders;
- Track flow;
- Workspace execution;
- Product Intent;
- Discovery Case;
- work state and progress;
- bottlenecks;
- handoffs.

Examples:

- PI Console
- Workspaces Console
- Progress Console
- Track Console

Do not put team skill inventory, agent performance, governance authority, risk/debt registers, or repository configuration primarily in Work.

## Workforce consoles

Use Workforce consoles when the primary object is people, teams, agents, roles, capacity, skill, contribution, or recognition.

Belongs here:

- human contributors;
- agents;
- teams;
- roles and skills;
- capacity and workload;
- contribution and effectiveness;
- availability;
- Kudos / Recognition entries;
- agent/human task split.

Examples:

- Team Console
- Agent Console

Kudos / Recognition belongs here because the system of record is the Workforce Repository.

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

Raw velocity charts belong in Progress Console.

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

| Need | Expand |
|------|--------|
| Product Intent type filter | PI Console |
| Governance status on Product Intent | PI Console |
| Work Order governance badges | Workspaces Console |
| Team recognition | Team Console |
| Agent cost per task | Agent Console |
| Debt aging chart | Registers / Governance Overview |
| Build quality threshold detail | Quality Controls |
| Release readiness status | Release Console + Governance overlay |

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

| Type | Meaning |
|------|---------|
| **Landing console** | Overview / health / summary |
| **Operational queue** | Items needing action |
| **Detail console** | Deep view of one entity type |
| **Analytics console** | Metrics, trends, reports |
| **Admin console** | Configuration and permissions |
| **Resource console** | Repositories/tools/external systems |

Examples:

| Console | Type |
|---------|------|
| Governance Overview | Landing |
| Workspaces Console | Operational queue |
| PI Console | Operational + traceability |
| Registers | Operational queue + detail |
| Reports & Dashboards | Analytics |
| Governance Admin | Admin |
| Repositories & Tools | Resource |
| Team Console | Workforce analytics + profile |
| Agent Console | Workforce analytics |

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
| Phase 1 | Prefer fewer consoles, strong overlays, clear action queues. Add Governance Overview, Controls & Enforcement, Registers. Enhance PI, Workspaces, Track, Reports, Quality Controls, Admin. |
| Phase 2 | Add/expand Rituals, richer Reports & Dashboards, fuller Registers workflows, release governance overlays, workforce recognition views. |
| Phase 3 | Full Governance Admin, authority matrix editor, control inheritance UI, advanced analytics, cross-Workbench governance, recognition trend analytics. |

## Canonical statement

Work consoles show the movement of work. Workforce consoles show the people and agents doing the work. Governance consoles show whether the work system is healthy, controlled, evidenced, authorized, efficient, compliant, and improving. A new console is justified only when it answers a distinct user question that cannot be served clearly as a tab, panel, or overlay inside an existing console.
