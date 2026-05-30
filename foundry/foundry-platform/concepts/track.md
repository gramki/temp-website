# Track

A Track is a value stream that organizes work into cohesive flows — Build, Discovery, Run, Win, Evolve, and Governance — each with its own orchestration items, work entities, and lifecycle patterns.

## What it is

Tracks are UPIM's way of partitioning the product lifecycle into distinct value streams. Each Track addresses a different question in product evolution:

| Track | Question | Primary Work |
|-------|----------|--------------|
| **Discovery** | What should we build? | Signal exploration, deliberation, research, experiments |
| **Build** | How do we build it? | Epics, stories, tasks, bugs |
| **Run** | How do we keep it running? | Deployments, changes, incidents, maintenance |
| **Win** | How do we support customers? | Win cases, queries, complaints, escalations |
| **Evolve** | How do we improve our practices? | Process reviews, model evolution, practice adoption |
| **Governance** | How do we ensure quality and compliance? | Rituals, enforcement, evidence, registers |

Each Track has a **primary orchestration item** — the coordination token that flows through the Track's lifecycle. Product Intent flows through Build; Discovery Cases flow through Discovery; Run Cases flow through Run. The Orchestrator routes these items through Workspaces, creating Work Orders at each station.

Tracks are not isolated silos. Discovery produces signals that become Build Product Intents. Build releases trigger Run deployments. Win feedback creates Discovery signals or Build bugs. Evolve improves practices used by all Tracks. Governance validates transitions everywhere.

## Where it lives in Foundry

| Module | Track Involvement |
|--------|-------------------|
| **Orchestrator** | Routes orchestration items per Track; executes Track-specific OI Workflows |
| **WO Runtime** | Executes Work Orders for all Tracks |
| **Work Catalogues** | Organizes OI Workflows and Scenarios by Track |
| **Work Repository** | Stores live work instances across all 5 Tracks |
| **Feedback Repository** | Win, Run, Build feedback views aligned to Tracks |

The [Work Catalog](work-catalog.md) folder structure reflects Track organization: `work-catalog/{track}/{orchestration-item}/{workspace}/scenarios/`.

## ACE/UPIM alignment

| UPIM Track | ACE Extension |
|------------|---------------|
| Discovery, Build, Run, Win, Evolve | UPIM defines these five tracks |
| Governance | ACE introduces Governance as a first-class Track |

UPIM's Work Model defines the five value-stream Tracks. ACE extends this by introducing Governance as a Track (not just a Workspace), with its own orchestration items (Governance Ritual, Governance Enforcement) and lifecycle.

The [Governance](governance.md) concept documents this extension in detail.

## Related concepts

- [Orchestration Item](orchestration-item.md) — The coordination tokens that flow through Tracks
- [Work Catalog](work-catalog.md) — Where Track workflows and scenarios are defined
- [Work Order](work-order.md) — Execution instances created when items reach Workspaces
- [Governance](governance.md) — The Governance Track specifically

## Further reading

- [../orchestrator/README.md](../orchestrator/README.md) — How Orchestrator routes per Track
- [../work-catalogues/README.md](../work-catalogues/README.md) — Track organization in Work Catalogs
- [../../ace/repositories.md](../../ace/repositories.md) — Track alignment of repositories
- [../../product-information-model/README.md](../../product-information-model/README.md) — UPIM Work Model and Tracks
