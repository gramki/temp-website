# Foundry — the platform for agent-driven software delivery (Builders)

## Why now

The way software is built is about to change — not incrementally, but structurally.

Agents can already write code. That's no longer the frontier. The frontier is what happens when you stop treating agents as tools that help individuals, and start treating them as workers who share the line with humans — where a spec flows through stations, work carries its context, every transition is governed, and the whole system knows what the product is.

That system doesn't exist yet. Foundry is an attempt to build it.

## The picture

Software delivery is not one assembly line — it's several. Each **Track** of the SDLC — Discovery, Build, Run, Win, Evolve, and Governance — is a value stream, and Foundry runs an assembly line for each one.

Work flows through stations called **Workspaces**. A Workspace is a station for a collection of agents and humans playing a specific function in the SDLC — Product Specification, UX Design, Development, QA, Release, Governance. The same Workspaces participate in multiple Tracks; the work passing through them is what differs.

## The interface

Each Workspace is interfaced through an IDE based on **VS Code**. Builders log in to their IDE to access the Workspace, with all the Product context UPIM supplies pre-loaded. Think GitHub Codespaces, but for agentic software work.

## Who uses it

Engineers at Zeta, and the engineers at the customer banks Zeta delivers software to. Foundry is multi-tenant by design.

## The core abstractions

- **Track** — a value stream in the SDLC (Discovery, Build, Run, Win, Evolve). Each Track is an assembly line.
- **Workspace** — a station on the line, owned by a single function. A Workspace knows what work it can do and houses the agents and humans who do it.
- **Scenario** — a defined kind of work a Workspace knows how to execute. Automated by an agent with skills, decomposing into Tasks.
- **Product Intent** — the root concept describing what the product is meant to be and to do. Every piece of work in Foundry traces back to a Product Intent, and the graph rooted at it carries the context that work needs.
- **Work Order** — an instance of a Scenario, attached to a Product Intent graph that carries its context.
- **Agent** — an AI worker with a defined set of skills, spun up per Scenario to execute it end-to-end.
- **Task** — the granular unit of work inside a Work Order. Either an **Agent Task** (executed by an agent) or a **Human Task** (assigned to a human, or waiting on one).

When a builder logs into a Workspace, they see Work Orders in flight, the Human Tasks waiting on them, progress on every Order, and the context they can refine or add.

## Where Foundry fits

Three layers, one stack:

- **UPIM** specifies the *Work* and *Context* — for a specific model of products.
- **ACE** specifies the *execution model* for the Work that UPIM defines.
- **Foundry** *implements* ACE.

You don't need to absorb UPIM and ACE on day one. You'll learn them as you build the platform that runs on them — and you'll help evolve them: building Foundry will teach us what UPIM and ACE need to be.

## Phase 1

Phase 1 commits to four Tracks: **Discovery**, **Build**, **Release**, and **Governance**. All Workspaces are in scope for these Tracks; only a subset of Scenarios per Workspace will be required to ship Phase 1.

> Note: "Release" here is the Build-Track activity of publishing verified artifacts — deployment lives in the Run Track and is out of Phase 1 scope. Governance is introduced at the ACE layer as a Track that extends UPIM's set.

## What you'd be working on

Pick any one — each has 18 months of interesting, foundational work:

- **Foundry Management** — Workbenches for Products, repositories (as services), teams, agents, knowledge, tenancy
- **Foundry IDE** — builder-facing views on work, tasks, context, progress — workspace-specific
- **Work Order Runtime** — context compilation, agent lifecycle for WO execution, agent delegation, human-task surfacing
- **Foundry Orchestrator** — move Product Intent across workspaces, create Work Orders, invoke Governance Scenarios, enforce gates
- **Scenario Authoring (per Track, Workspace)** — scenario discovery & definition; Skills, Knowledge, and Tools; agent recommendations
- **Release Tools** — CI/CD pipelines with embedded agents, CD integrations, distribution stores
- **Platform Ops** — observability dashboards, standard tooling, infrastructure plumbing

## Closing

The question isn't whether agents will do software work. They already do.

The question is: who builds the system that lets them?

If that question sounds like your kind of problem — we should talk.
