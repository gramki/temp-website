# Workspaces

ACE defines six workspace types. Each is a specialized station inside a Workshop Project, owned by a single functional team, with a Human–Agent Team and an IDE context, owning Scenarios that decompose into Tasks. Each workspace reads and writes the workshop's repositories and participates in the [Product Evolution Cycle](../product-evolution-cycle.md).

The docs in this folder are **stub-grade** today. They establish purpose, primary scenarios, intent inbound/outbound, and the key repositories each workspace touches. Detailed scenario catalogs, runtime specifications, and per-workspace platform engineering live under [`../../foundry-platform/`](../../foundry-platform/) as those modules are specified.

## Index

| Workspace | Doc | Concern |
|---|---|---|
| Product Specification | [`product-specification.md`](product-specification.md) | Translate Product Intent into specifications. |
| UX Design | [`ux-design.md`](ux-design.md) | Design experience for specified intent. |
| Development | [`development.md`](development.md) | Build the specified solution. |
| QA | [`qa.md`](qa.md) | Verify and validate built artifacts. |
| Release | [`release.md`](release.md) | Manage and produce Product Delivery; emit new Product Intent. |
| Governance | [`governance.md`](governance.md) | Validate every transition of Product Intent. |

## Common pattern

Every workspace in this list follows the same pattern (see [`../concepts.md`](../concepts.md) for the formal definition):

- A **Human–Agent Team** completes the work.
- A **dedicated IDE context** (Olympus Workspace + Olympus Rocket profile) is the human entry surface.
- **Scenarios** create **Tasks**.
- **Repositories** are read and written.
- **Transitions** of Product Intent into and out of the workspace invoke governance scenarios.

The differences below are about which scenarios each workspace owns, which repositories it touches most, and which transitions it participates in.
