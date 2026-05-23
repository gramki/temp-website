# Scenario Authoring

**Module scope:** Per (Track, Workspace) — scenario discovery & definition; Skills, Knowledge, and Tools; agent recommendations.

## What this module does

Scenario Authoring is the capability for defining what work each Workspace can do. It provides:

- **Scenario discovery** — identify and catalogue the kinds of work a Workspace can execute for a given Track
- **Scenario definition** — formally define Scenarios with inputs, outputs, steps, and success criteria
- **Skills curation** — define and manage the Skills agents need to execute Scenarios
- **Knowledge curation** — curate the Knowledge a Scenario needs (domain knowledge, practices, context)
- **Tools curation** — define the Tools agents use within Scenarios
- **Agent recommendations** — recommend which agent configurations are suited for which Scenarios

## Folder structure

Scenarios are organized by **(Track, Workspace)** pairs:

```
scenario-authoring/
├── discovery/           # Discovery Track
│   ├── product-specification/
│   ├── ux-design/
│   ├── development/
│   ├── qa/
│   ├── release/
│   └── governance/
├── build/               # Build Track
│   └── ...
├── run/                 # Run Track (out of Phase 1)
│   └── ...
├── win/                 # Win Track (out of Phase 1)
│   └── ...
├── evolve/              # Evolve Track (out of Phase 1)
│   └── ...
└── governance/          # Governance Track (ACE extension)
    └── ...
```

### Track folders

| Track | Folder | Phase 1? |
|-------|--------|----------|
| Discovery | [discovery/](discovery/README.md) | Yes |
| Build | [build/](build/README.md) | Yes |
| Run | [run/](run/README.md) | No |
| Win | [win/](win/README.md) | No |
| Evolve | [evolve/](evolve/README.md) | No |
| Governance | [governance/](governance/README.md) | Yes |

Each Track folder contains 6 Workspace sub-folders. Scenario definitions grow within the appropriate (Track, Workspace) folder.

## ACE concepts realized

- **Scenario** — a defined kind of work a Workspace knows how to execute
- **Skill** — a unit of agent capability
- **Track** — Scenarios are scoped to (Track, Workspace) pairs
- **Workspace** — each Workspace owns a catalogue of Scenarios

## Key design decisions

- **Scenarios are not global.** They're scoped to (Track, Workspace) pairs.
- **Skills, Knowledge, Tools are curated per Scenario.** Not a global pool — each Scenario declares what it needs.

## Open questions

- Scenario decomposition — deterministic (declared upfront) or dynamic (agent-decided)?
- Skill → Scenario mapping mechanism
- Scenario catalogue format and storage
- Agent recommendation algorithm

## Read next

- [../../ace/concepts.md](../../ace/concepts.md) — Scenario, Skill definitions
- [../../ace/workspaces/](../../ace/workspaces/README.md) — the six Workspace types
- [../../tldr-faq.md](../../tldr-faq.md) — scenario authoring design decisions
