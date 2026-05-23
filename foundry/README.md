# Foundry — the platform for agent-driven software delivery

The way software is built is about to change — not incrementally, but structurally.

Agents can already write code. That's no longer the frontier. The frontier is what happens when you stop treating agents as tools that help individuals, and start treating them as workers who share the line with humans — where a spec flows through stations, work carries its context, every transition is governed, and the whole system knows what the product is.

That system doesn't exist yet. Foundry is an attempt to build it.

**Start here:** [tldr.md](tldr.md) — the one-page intro to Foundry for builders. 

---

## About this folder

This folder is the home of the documentation that defines, describes, and engineers Foundry — the system in which Zeta builds software with human–agent teams. It contains both the theoretical model that justifies the system and the engineering work that delivers the Foundry Platform.

The primary readers are the **product and engineering teams building the Foundry Platform**. A secondary reader is anyone joining the team and looking for orientation. A third, indirect, reader is the customer (typically a Bank CIO) whose value perspective we capture for the team — but customer-facing material is written for builders to internalize, not for external distribution.

## Foundry vs Foundry Platform

Two senses of the word "Foundry" are used throughout these documents. They are related but distinct, and the documents try hard to keep them apart.

- **Foundry (the concept in ACE).** An architectural construct described in [ace/ace-model.md](ace/ace-model.md): the place where software products are crafted, governed by the Product, Work, and Operating models, and hosting workshops. When a sentence is talking about boundaries, governance, intent flow, or containment, it is usually using "Foundry" in this conceptual sense.
- **Foundry Platform (the implementation).** The software and infrastructure being built — specifications, modules, deployments, security and compliance posture, observability, CI. When a sentence is talking about something that can be deployed, operated, or shipped, it is the platform. Capitalized as **Foundry Platform** to make it visually clear.

The two are the same word in different roles: a *type* and an *instance*. Some other documents in this tree may say "the Foundry" — interpret from context, or prefer the qualified phrase.

## Key documents

| Document | What it is |
|---|---|
| [tldr.md](tldr.md) | One-page intro to Foundry for builders — the vision, core abstractions, platform modules, and what you'd be working on. |
| [tldr-faq.md](tldr-faq.md) | FAQ companion to the tldr — captures clarifications and design decisions. |
| [glossary.md](glossary.md) | Single source of truth for terminology — every overloaded or load-bearing term in this tree. |

## Subfolder map

| Folder | What it contains | Primary reader |
|---|---|---|
| [ace/](ace/README.md) | The Agent-Centric Engineering theory: why ACE exists, its objectives, formal concepts, the Product Evolution Cycle, governance, illustrations, and references. The starting point for understanding the system Foundry implements. | Builders + new joiners |
| [product-information-model/](product-information-model/README.md) | UPIM — the Unified Product Information Model. A formal information model with three layers: Definition Model (what the product is), Work Model (what work exists), Operating Model (how the org executes). UPIM is a concretization layer of ACE — it gives entities, dimensions, and lifecycles to what ACE governs — and can also stand independently. | Modelers, PMs, builders |
| [foundry-platform/](foundry-platform/README.md) | Architecture, module specifications, UX, deployment, security/compliance, observability, and CI for the Foundry Platform — the implementation that delivers ACE and UPIM capabilities. | Builders |
| [foundry-work-plan/](foundry-work-plan/README.md) | The project plan for building the platform: people, milestones, budget, governance cadences, value-realized checkpoints. | Builders + leadership |
| [engagement-engineering/](engagement-engineering/README.md) | An extension to ACE for delivering software to clients (multi-tenant, multi-engagement reality). Includes tenant developer tooling. | Builders |
| [propeller/](propeller/README.md) | A parallel workstream of the Foundry engineering team that builds cross-stack frameworks, libraries, and conventions. **Not** Foundry Platform internals — these are reusable foundations consumed by workspaces. | Wider Zeta engineering |
| [stakeholder-briefs/](stakeholder-briefs/README.md) | The customer (Bank CIO) value perspective, written *for* builders to internalize. Not external collateral. | Builders |

## Suggested reading paths

**New joiner (orientation):** start with [tldr.md](tldr.md) for the one-page overview, then [ace/README.md](ace/README.md), then [product-information-model/README.md](product-information-model/README.md). The [glossary.md](glossary.md) is a useful companion throughout.

**Platform engineer (building or specifying a module):** start with [tldr.md](tldr.md) for context, then [tldr-faq.md](tldr-faq.md) for module design decisions, then [ace/concepts.md](ace/concepts.md) for the model entities, [ace/repositories.md](ace/repositories.md) for the repository taxonomy your module reads or writes, and [foundry-platform/README.md](foundry-platform/README.md) for where the module fits.

**PM owning a workspace:** start with [ace/README.md](ace/README.md), then [ace/product-evolution-cycle.md](ace/product-evolution-cycle.md), then the relevant doc under [ace/workspaces/](ace/workspaces/README.md). Cross-check entity definitions in [product-information-model/README.md](product-information-model/README.md).

**Working with a customer engagement:** read [engagement-engineering/README.md](engagement-engineering/README.md) and [engagement-engineering/extension-to-ace.md](engagement-engineering/extension-to-ace.md) before the platform docs; the engagement extension reframes several ACE concepts (Workshop, Workforce, Repositories) for client delivery.

## Conventions for documents in this tree

- Markdown only. Diagrams use Mermaid. Images and prompt files live in [ace/illustrations/](ace/illustrations/README.md).
- New concepts must trace to existing source material in this tree. Do not invent ontology in narrative documents; if a concept is needed and not yet defined, propose it in the relevant TODO file first.
- Each subfolder owns a `README.md` that explains its purpose, primary reader, and how it relates to its siblings.
- Where a term is overloaded (Foundry, Product, Workshop), use the qualified form ("Foundry Platform", "Home Workshop", "Product Intent") and cross-link the glossary.
