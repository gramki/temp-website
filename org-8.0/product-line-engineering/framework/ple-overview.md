# Product Line Engineering: Overview

## What is Product Line Engineering (SEI Definition)

**Product Line Engineering (PLE)** is a systematic approach to developing and managing a family of related products. The Carnegie Mellon Software Engineering Institute (SEI) defines it through:

1. **Core Asset Development (Domain Engineering)** — Proactively building reusable assets (code, designs, tests, documentation) that serve the entire product family.
2. **Win Engineering** (in SEI terms: Product Development / Application Engineering) — Deriving specific products by selecting, configuring, and extending core assets according to a production plan. At Zeta we use the term **Win Engineering** for this layer.
3. **Management** — Orchestrating both activities so the product line thrives: scoping, variability management, process, and organization.

**Critical success factors (SEI):**

- **Proactive, planned reuse** — Reuse is designed in, not opportunistic.
- **Explicit variability management** — What varies and how is formally modeled (feature diagrams, binding times, constraints).
- **Organizational commitment** — Structure, process, and funding aligned to the product line.

PLE originated in embedded systems (automotive, aerospace) where many product variants share a large common base and differ in controlled ways.

---

## Why Zeta Is Adopting PLE

Zeta’s platforms (Olympus, Tachyon, Neutrino, Electron, Quark) were positioned as “SaaS” products. That positioning caused friction:

- **Customer expectation:** Everything needed is “in the box”; minimal customization.
- **Zeta reality:** Platforms are **accelerators and frameworks**. Most enterprises need solutioning, implementation, integration, and product thinking to get an integrated system that fits their needs.

PLE provides:

1. **A clear mental model** — Core assets (platforms) vs. derived products (Customer Solutions). Shared vocabulary for internal and external stakeholders.
2. **Explicit boundaries** — What’s in the box (domain) vs. what’s configured/extended per engagement (Win Engineering).
3. **Operational clarity** — Who owns core assets (Domain Teams), who owns delivery (Win Engineering Teams), who governs (Council).
4. **Commercial alignment** — Platform subscription vs. solution delivery vs. Studio (out of PLE scope) can be separated and communicated clearly.

---

## How Zeta Adapts PLE for Enterprise Solution Delivery

Zeta’s model is **PLE-inspired**, not a strict implementation of SEI PLE. Key adaptations:

| SEI PLE Concept | Zeta Adaptation |
|-----------------|-----------------|
| **Application Engineering teams** | **Win Engineering Teams** — Composed per engagement; may remain on a Customer Solution for up to ~2 years. Not permanent “application engineering” teams. |
| **Product instance** | **Customer Solution** — The integrated solution delivered under an engagement. |
| **Formal variability management** | **Lightweight variability management** — Configuration points, options, binding time, and customer usage documented (e.g. template); no heavy feature-model tooling initially. |
| **Application Engineering contributes via intake** | **Inner source** — Win Engineering Teams contribute code to domain platforms via PRs; Domain Maintainers review and merge. |
| **Prescriptive derivation** | **Solution archetypes as guides** — Blueprints, cookbooks, and playbooks inform derivation but don’t rigidly constrain it. See [Solution Archetypes](solution-archetypes.md#blueprint-cookbook-playbook-definitions-and-role-in-win-engineering) for definitions and their role in Win Engineering. |

These adaptations fit Zeta’s context: project-based engagements, enterprise variability, and the need for both reuse and flexibility.

---

## What We Are and Aren’t Doing

### What We Are Doing

- **Adopting the PLE mental model** — Core assets (domain platforms) and derived products (Customer Solutions); Domain Engineering vs. Win Engineering.
- **Defining clear ownership** — Domain Teams own core assets; Win Engineering Teams (composed per engagement) own Customer Solution delivery; Engagement Lead owns delivery accountability.
- **Managing variability in a lightweight way** — Solution Architects and Council document and govern configuration points, options, binding time, and which customers use what.
- **Using inner source** — Win Engineering Teams can contribute to domain platforms via PRs, with Domain Maintainer review and governance (DoD, soft gate, tech debt tracking).
- **Using solution archetypes** — Reusable patterns (blueprint, cookbook, playbook) per solution class; owned by Solution Architecture; evolved via Council and engagement feedback.
- **Keeping Studio out of PLE** — Studio (customer-exclusive apps, portals, back-office tools) is a separate engagement type; customer IP; no PLE derivation.

### What We Aren’t Doing

- **Pure SEI PLE** — We are not claiming full SEI compliance. We adopt the mental model and adapt structure and process.
- **Permanent Win Engineering teams** — Win Engineering Teams are composed per engagement and may last up to ~2 years; they are not permanent “application engineering” departments.
- **Heavy formal variability tooling** — No mandatory feature-model or variability-management tools at the start; we use documentation and Council governance. Tooling may be added later if needed.
- **Rigid derivation** — Customer Solutions are not generated from a formal feature model; archetypes guide, they don’t fully prescribe.
- **PLE for Studio** — Studio work remains bespoke, customer IP; learnings may be shared but we do not aggregate Studio IP into a product line.

### Why These Choices

- **Ephemeral-ish Win Engineering Teams:** Engagements are project-based; teams form and disband around engagements. Long-lived teams (e.g. ~2 years) allow continuity on a Customer Solution while rotation preserves knowledge and breadth.
- **Light variability management:** At current scale (10–30 engagements), lightweight documentation and Council governance are sufficient. Heavier formalization can be added if scale or complexity demands it.
- **Inner source:** Reduces intake bottleneck and leverages Win Engineering expertise; governance (Maintainers, DoD, tech debt) keeps core asset quality.
- **Archetypes as guides:** Enterprise solutions vary; archetypes standardize where it helps without over-constraining.

---

## Anticipated Criticisms and Responses (For Leaders)

### “This isn’t real PLE.”

**Response:** We’re not claiming it is. We use PLE as the **mental model and organizational frame**: core assets vs. derived products, Domain Engineering vs. Win Engineering, explicit ownership and variability. We’ve adapted it for enterprise solution delivery—project-based engagements, inner source, lightweight variability. We call it “Zeta’s PLE framework” or “PLE-inspired.”

### “Ephemeral teams will lose knowledge.”

**Response:** Win Engineering Teams can stay on a Customer Solution for up to ~2 years, so they’re not “ephemeral” in a weeks-long sense. We mitigate knowledge loss with: (1) solution archetypes (blueprints, cookbooks, playbooks), (2) engagement retrospectives and decision logs, (3) rotation that brings people back to Domain Teams or other engagements, (4) Council-led pattern extraction. Knowledge lives in artifacts and practice, not only in permanent teams.

### “Inner source will hurt platform quality.”

**Response:** We govern it: Definition of Done, Domain Maintainer review, soft gate with tech debt tracking, and Council oversight. Maintainers can reject or request changes; tech debt is tagged and remediated. The alternative—only Domain Teams changing platforms—creates an intake bottleneck and underuses Win Engineering expertise.

### “Lightweight variability isn’t enough.”

**Response:** For our current scale and engagement mix, documented configuration points, options, binding time, and customer usage—owned by Solution Architects and governed by Council—are the right level. We can introduce more formal variability management (e.g. tooling, feature models) later if we see variability creep or scaling issues.

### “Who’s accountable when something goes wrong?”

**Response:** Engagement Lead is accountable for **delivery** of the Customer Solution. Solution Architect is accountable for **architecture and variability documentation**. Domain Teams are accountable for **core asset quality and maintenance**. Platform operations are always Zeta (SRE). Customer Solution operations depend on the chosen operating model (Fully Managed, Co-Managed, Customer-Operated). Contracts and RACI spell this out.

### “This is a big reorg. Why now?”

**Response:** We had ownership confusion (no single owner for the integrated solution), friction from “SaaS” positioning, and unclear boundaries between platform and custom work. PLE gives us a shared model, clear ownership, and a path to scale delivery without scaling chaos. We’re doing it in phases (Foundation, Launch & Pilot, Expand & Steady State) so we can learn and adjust.

---

## Summary

Zeta uses **Product Line Engineering** as the organizing idea and operational framework for how we build and deliver Customer Solutions from our platforms. We **adopt** the core-asset vs. derived-product mental model and Domain vs. Win Engineering structure. We **adapt** for our context: engagement-composed Win Engineering Teams, inner source, lightweight variability, and solution archetypes as guides. We are **explicit** about what we are and aren’t doing so leaders can address criticism and questions consistently.

For details, see [Domain Engineering](domain-engineering.md), [Win Engineering](win-engineering.md), [Variability Management](variability-management.md), and [Governance](../governance/council-charter.md).
