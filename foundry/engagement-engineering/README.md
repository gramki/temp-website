# Engagement Engineering

## Purpose

Engagement Engineering is the body of work that **extends ACE for client delivery**. ACE's base model describes intra-organization product development. When the same product is being delivered to a client — multi-tenant, program-managed, customer-side feedback channels, evidence requirements, multi-Workshop evolution — additional concepts and machinery are needed.

This folder documents that extension. It is **part of the Foundry Platform's body of engineering work**, but treated as a distinct extension rather than a Foundry Platform module, because it modifies ACE concepts (Workshop, Workforce, Repositories) rather than only adding platform features.

## Audience

Primary readers are platform builders working on engagement-aware capabilities. Secondary readers are PMs and engagement leads on customer-facing teams.

## What lives here

| File / folder | Purpose |
|---|---|
| [`extension-to-ace.md`](extension-to-ace.md) | The full extension argument: which ACE concepts change for client delivery, and how. |
| [`1.TODO`](1.TODO) | The current backlog of engagement-engineering work — model, objectives, release artifacts, approach. |
| [`tenant-developer-tooling/`](tenant-developer-tooling/) | Tooling for tenant developers (Olympus Workspace, Olympus Rocket, Hub Workbench). Moved here from the top level because it serves the engagement context. |

## What changes for client delivery (one-paragraph summary)

A few of the most consequential shifts (full treatment in [`extension-to-ace.md`](extension-to-ace.md)):

- **Engagement is a Workshop** — a client program (e.g. Bank-X) is modeled as a Workshop named for that engagement, program-managed for Velocity, Predictability, Quality, Cost, and Risk. Source: [`extension-to-ace.md`](extension-to-ace.md); [`../1.TODO`](../1.TODO) lines 11-12.
- **Workshop Project corresponds to a Product in UPIM** — each Product built for the client is evolved in an **Engagement Workshop Project** inside that Engagement Workshop; the Workshop Project is the locus of evolution, not the Product entity. **Home Workshop**, **Home Workshop Project**, **Contributing Workshop Project**, and standalone engagement-only Products are defined in [`extension-to-ace.md`](extension-to-ace.md). Source: [`../1.TODO`](../1.TODO) lines 4, 7-8 (historical phrasing); [`../ace/relationships.md`](../ace/relationships.md).
- **Operational shape.** A Workshop Project remains a collection of git repos, Jira boards, CI jobs, release artifacts, deployment trains, and people, adhering to the UPIM Work Model. Source: [`1.TODO`](1.TODO) lines 2-4.
- **Win Workforce** is associated with the Foundry of the Home Workshop and directs Run-related work to the appropriate **Estate** (production-operations boundary). Source: [`../1.TODO`](../1.TODO) lines 15-17.
- **Customer-facing release artifacts** become first-class: Customer Product Artifacts, Studio Component Artifacts, Verification Artifacts, Documentation Artifacts (Admin/User/Developer Guides), Evidence Artifacts, Knowledge Base. Source: [`1.TODO`](1.TODO) lines 17-26.

## What this folder is *not*

- It is **not** a Foundry Platform module. Modules live in [`../foundry-platform/`](../foundry-platform/).
- It is **not** the customer-facing GTM narrative. That kind of material — written for internal builders to internalize — lives in [`../stakeholder-briefs/`](../stakeholder-briefs/).
- It is **not** a Run/Operations specification. Run concerns are split between this extension (the Engagement–Estate handoff) and production-operations engineering that is **out of scope** of this folder. See [`../1.TODO`](../1.TODO) lines 14-17; [`extension-to-ace.md`](extension-to-ace.md).

## Read next

- [`extension-to-ace.md`](extension-to-ace.md) — the extension argument.
- [`tenant-developer-tooling/TD.TODO`](tenant-developer-tooling/TD.TODO) — concrete tenant tooling (Olympus Workspace, Rocket, Hub).
- [`../ace/relationships.md`](../ace/relationships.md) — how ACE, UPIM, and the Foundry Platform fit together; the engagement extension sits at the boundary of this triangle.
