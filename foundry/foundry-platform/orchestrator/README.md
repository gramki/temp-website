# Foundry Orchestrator

**Module scope:** Coordination — move Product Intent across workspaces, create Work Orders, invoke Governance Scenarios, enforce gates.

## What this module does

Foundry Orchestrator is the coordination layer that moves work through the SDLC. It provides:

- **Product Intent movement** — move Product Intent across Workspaces as it progresses through Tracks
- **Work Order creation** — instantiate Scenarios as Work Orders when triggered
- **Governance invocation** — invoke Governance Scenarios at gates and transitions
- **Gate enforcement** — validate transitions, block or allow based on Governance Scenario outcomes

## ACE concepts realized

- **Track** — value streams (Discovery, Build, Run, Win, Evolve, Governance); Orchestrator moves work through Tracks
- **Workspace** — stations on the line; Orchestrator routes Product Intent to Workspaces
- **Product Intent** — the root of the graph; Orchestrator moves it
- **Governance** — Orchestrator invokes Governance Scenarios at transitions

## Key design decisions

- **Governance is distributed.** Definition is via Scenarios (Scenario Authoring), enforcement is via Orchestrator, evidence is captured in repositories.
- **Governance Scenarios are first-class.** They're invoked like any other Scenario, but at transition points.

## Open questions

- How is Product Intent movement triggered? (event-driven, explicit API, Scenario completion?)
- Work Order creation API
- Gate enforcement mechanics — blocking vs advisory
- Governance Scenario invocation timing

## Read next

- [../../ace/governance.md](../../ace/governance.md) — governance model
- [../../ace/product-evolution-cycle.md](../../ace/product-evolution-cycle.md) — how Product Intent moves
- [../../tldr-faq.md](../../tldr-faq.md) — orchestration design decisions
