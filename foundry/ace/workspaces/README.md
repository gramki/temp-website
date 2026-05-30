# Workspaces

ACE defines six workspace types. Each is a specialized station inside a Workbench, owned by a single functional team, with a Human–Agent Team and an IDE context, owning Scenarios that decompose into Tasks. Each workspace reads and writes the workshop's repositories and participates in the [Product Evolution Cycle](../product-evolution-cycle.md).

> **Stations are functional teams, not stages.** The six workspaces are reused across all tracks (Build, Discovery, Run, Win, Evolve, Governance) — they represent *who* does the work by SDLC function, not *where* in a lifecycle the work sits. The Build ordering below (Specification → UX → Development → QA → Release) is incidental to how Product Intent happens to flow; other tracks route work to the same teams in different patterns, often fanning a single OI stage out to several stations in parallel. A track does not get its own teams. Two stations are named after their concern rather than the team — **Product Specification** (not "Product") and **Release** (not "Release Engineering"); see [../concepts.md](../concepts.md) for the rationale.

The docs in this folder are **stub-grade** today. They establish purpose, primary scenarios, intent inbound/outbound, and the key repositories each workspace touches. Detailed scenario catalogs, runtime specifications, and per-workspace platform engineering live under [../../foundry-platform/](../../foundry-platform/README.md) as those modules are specified.

## Index

| Workspace | Doc | Concern |
|---|---|---|
| Product Specification | [product-specification.md](product-specification.md) | Refine Product Intent into PSDs and specification artifacts. |
| UX Design | [ux-design.md](ux-design.md) | Design experience for specified intent. |
| Development | [development.md](development.md) | Build the specified solution. |
| QA | [qa.md](qa.md) | Verify and validate built artifacts. |
| Release | [release.md](release.md) | Manage and produce Product Delivery; renew Product Intent. |
| Governance | [governance.md](governance.md) | Validate every transition of Product Intent. |

## Common pattern

Every workspace in this list follows the same pattern (see [../concepts.md](../concepts.md) for the formal definition):

- A **Human–Agent Team** completes the work.
- A **dedicated IDE context** (Olympus Workspace + Olympus Rocket profile) is the human entry surface.
- **Scenarios** create **Tasks**.
- **Repositories** are read and written.
- **Transitions** of Product Intent into and out of the workspace invoke governance scenarios.

The differences below are about which scenarios each workspace owns, which repositories it touches most, and which transitions it participates in.
