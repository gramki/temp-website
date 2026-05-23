# Release Workspace

## Purpose

Manage and produce **Product Delivery**, and emit new **Product Intent** that triggers the next cycle. Release is both the *exit* of the Product Evolution Cycle (where verified intent becomes deliverable) and its *source* (where direction, evidence, and learnings produce the next cycle's intent). Source: [../ace-model.md](../ace-model.md) lines 52, 58.

## Inbound and outbound intent

- **Inbound:** from QA (verified intent as Product Delivery). Source: [../ace-model.md](../ace-model.md) line 58.
- **Outbound:** to Product Specification (new Product Intent emitted at cycle start). Source: [../ace-model.md](../ace-model.md) line 52.

The cycle closes here.

## Primary scenarios (illustrative)

This workspace owns scenarios such as:

- Producing release plans, checklists, debt management, and product risk management content.
- Performing release verification and validation.
- Producing release notes and documentation.
- Emitting new Product Intent at cycle start, anchored in delivered evidence and learnings.

Concrete scenario catalogs are listed under "Release Workspace Engineering" in [../../foundry-platform/platform.TODO](../../foundry-platform/platform.TODO) lines 18-22.

## Repositories touched

- **Product Intent Repository (PIR)** — write (new intent at cycle start) and update (intent state at delivery).
- **Operations Repository (OPR)** — write. Deployment descriptors and records, operational artifact versions.
- **Quality & Verification Repository (QVS)** — read.
- **Product Feedback Repository (PFR-Run)** — read. Operational observation summaries inform new intent.
- **Practitioner Repository (PPR)** — read. Release standards, checklists, templates.
- **Work Repository (WR)** — write.

See [../repositories.md](../repositories.md).

## Engagement-extension note

In the engagement view, customer-facing releases are produced from **Engagement Workbenchs** (each corresponds to a Product in UPIM inside an **Engagement Workshop**). Release artifacts include customer-facing content (Customer Product Artifacts, Verification Artifacts, Documentation Artifacts, Evidence Artifacts, Knowledge Base) and may need to satisfy customer-side delivery contracts. Source: [../../engagement-engineering/1.TODO](../../engagement-engineering/1.TODO) lines 17-26. Full behavior is in [../../engagement-engineering/extension-to-ace.md](../../engagement-engineering/extension-to-ace.md).

## See also

- [../product-evolution-cycle.md](../product-evolution-cycle.md) — the cycle this workspace participates in.
- [../governance.md](../governance.md) — governance on intent transitions.
- [../../foundry-platform/platform.TODO](../../foundry-platform/platform.TODO) — Release Workspace Engineering.
