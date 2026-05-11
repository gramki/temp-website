# Development Workspace

## Purpose

Build the specified solution. The Development Workspace turns specifications and designs into source code, build artifacts, and module-level work products.

## Inbound and outbound intent

- **Inbound:** from Product Specification (intent ready to be built; arrives in parallel with QA). Source: [`../ace-model.md`](../ace-model.md) line 56.
- **Outbound:** to QA (built artifacts move forward). Source: [`../ace-model.md`](../ace-model.md) line 57. Optionally back to Product Specification when learnings demand re-specification. Source: [`../ace-model.md`](../ace-model.md) line 58.

## Primary scenarios (illustrative)

This workspace owns scenarios such as:

- Triggering on intent arrival from Product Specification and decomposing it into Module-scoped Epics and System-scoped Tasks (UPIM Track 2 vocabulary).
- Producing three-tier versioned artifacts (System, Module, Product versions).
- Returning intent to Product Specification when build-time learning reveals a specification gap.

Concrete scenario catalogs live in [`../../foundry-platform/`](../../foundry-platform/) under "Development Workspace Engineering" (see [`../../foundry-platform/platform.TODO`](../../foundry-platform/platform.TODO) line 23).

## Repositories touched

- **Source Repository (CAR)** — read and write. Source code, build artifacts.
- **Quality & Verification Repository (QVS)** — write. Build-time quality evidence.
- **Design & Architecture Repository (DAR)** — read.
- **Product Intent Repository (PIR)** — read.
- **Product Feedback Repository (PFR-Build)** — read. Bug report mirrors and technical debt observations.
- **Practitioner Repository (PPR)** — read. Coding standards, templates.
- **Work Repository (WR)** — write.

See [`../repositories.md`](../repositories.md).

## Cross-stack dependencies

Development depends heavily on the **Propeller** workstream — the cross-stack frameworks, libraries, and conventions that Workspaces consume but do not own. See [`../../propeller/`](../../propeller/).

## See also

- [`../product-evolution-cycle.md`](../product-evolution-cycle.md) — the cycle this workspace participates in.
- [`../governance.md`](../governance.md) — governance on intent transitions.
- [`../../foundry-platform/platform.TODO`](../../foundry-platform/platform.TODO) — Development Workspace Engineering.
- [`../../foundry-platform/ci/`](../../foundry-platform/ci/) — Foundry CI capabilities used here.
