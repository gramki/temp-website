# UX Design Workspace

## Purpose

Design the user experience for specified intent. The UX Design Workspace co-evolves designs with specifications through a bidirectional intent transfer with the Product Specification Workspace.

## Inbound and outbound intent

- **Inbound:** from Product Specification (intent that has been specified to a level where UX Design can engage). Source: [`../ace-model.md`](../ace-model.md) line 54.
- **Outbound:** to Product Specification (intent returning with design implications). Source: [`../ace-model.md`](../ace-model.md) line 55.

This is the only **strictly bidirectional** edge in the base [Product Evolution Cycle](../product-evolution-cycle.md).

## Primary scenarios (illustrative)

This workspace owns scenarios such as:

- Triggering on intent arrival from Product Specification and producing user experience designs.
- Co-evolving designs and specifications by sending intent back to Specification with design-driven changes.
- Producing assets and narratives that downstream workspaces (Development, QA) can reference.

Concrete scenario catalogs live in [`../../foundry-platform/`](../../foundry-platform/) under "UX Workspace Engineering" (see [`../../foundry-platform/platform.TODO`](../../foundry-platform/platform.TODO) line 26).

## Repositories touched

- **Design & Architecture Repository (DAR)** — read and write. Design output and architecture-shaped UX assets.
- **Product Intent Repository (PIR)** — read and write. The workspace consumes intent and may modify it on the return path.
- **Product Ontology Repository (POR)** — read.
- **Domain Knowledge Repository (DKB)** — read.
- **Practitioner Repository (PPR)** — read. UX practices, design system standards.
- **Work Repository (WR)** — write.

See [`../repositories.md`](../repositories.md).

## See also

- [`../product-evolution-cycle.md`](../product-evolution-cycle.md) — the cycle this workspace participates in.
- [`../governance.md`](../governance.md) — governance on intent transitions.
- [`../../foundry-platform/platform.TODO`](../../foundry-platform/platform.TODO) — UX Workspace Engineering.
