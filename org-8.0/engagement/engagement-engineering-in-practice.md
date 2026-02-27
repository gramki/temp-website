# Engagement Engineering in Practice

[← Back to Guide](README.md)

---

## Why Engagement Engineering Exists

Zeta's platforms (Olympus, Tachyon, Neutrino, Electron, Quark) are **accelerators and frameworks**, not turnkey SaaS products. Most enterprises need solutioning, implementation, integration, and product thinking to get an integrated system that fits their needs. The gap between "what's in the box" and "what the customer needs" must be closed through deliberate engineering — not ad-hoc project work.

Engagement Engineering exists to make that assembly **repeatable, scalable, and governed**. Without it, every customer delivery becomes a bespoke project: knowledge stays in people's heads, patterns are reinvented, platforms are forked instead of extended, and delivery quality depends on who happens to be on the team. With it, assembly follows a defined discipline — reusable archetypes, managed variability, inner source contribution, and structured verification — so that each Engagement strengthens the next.

The [PLE guide](../product-line-engineering/framework/ple-overview.md) provides the structural ingredients (Product Line Squads, inner source, archetypes, variability management). This guide defines the delivery methodology that uses those ingredients.

---

## What Engagement Engineering Is

Engagement Engineering is the discipline of designing and assembling customer-specific product instantiations by leveraging Product Lines and studio-built components.

In practice: Engagement squads configure and extend Product Line platforms to deliver customer-specific product instantiations. They do not own the core platforms — Product Line Squads do. They own the **derived product**: the assembled Customer Product, its Studio Components, and the verification module that certifies the assembly.

This ownership boundary is fundamental. Every decision — where to build, how to contribute back, what to own long-term — flows from it.

---

## What We Produce — Three Artifact Groups

An Engagement produces three groups of artifacts that together constitute the assembled product:

- **Customer Product artifacts** — Product Line configurations, extensions, platform integrations, and customer-specific business logic. These are the core of what the customer receives.
- **Studio Component artifacts** — integration adapters, orchestration flows, custom experiences (UIs, workflows, applications), and operational artifacts (runbooks, escalation matrices, monitoring configurations). Studio work stays anchored to the Customer Product and Product Lines.
- **Verification artifacts** — IaC environment definitions, assembly-level test suites, test data preparation tooling, CI orchestration configurations, and certification records. These are codified engineering — version-controlled and maintained with the same rigor as functional code. See [Verification and Certification](verification-and-certification.md).

All three are deliverables. At Transfer, the verification module is handed over alongside the functional product.

---

## How We Relate to Product Line Squads

Three relationships define the boundary between Engagement work and platform work:

- **Assigning people** — Product Line Squads assign engineers for the Engagement duration (or a rotation period within it). Return is guaranteed per the [Rotation Model](../product-line-engineering/processes/rotation-model.md). Product Line Squad leads reserve the right to decline or delay if platform capacity is at risk.
- **Using platforms** — Engagement squads configure and extend platforms. They never fork or own platform code. Ownership of core assets stays with Product Line Squads.
- **Contributing back** — when the Engagement needs a platform capability that doesn't exist, the pattern is inner source: EA prioritizes the contribution, ELs execute, Product Line Maintainers review and merge (or reject). See the next section.

---

## Inner Source — What It Means for Squads

Inner source is how Engagement squads contribute platform capabilities back to Product Lines. For an EL planning squad work, this is what it means in practice:

- **EA identifies and prioritizes.** During gap analysis (Discover), the EA determines what the Engagement needs that the platform doesn't have. The EA decides which gaps are best closed through inner source vs. custom (Engagement-specific) components.
- **EL plans inner source into squad capacity.** Inner source contributions are engineering work — they require design, implementation, review, and iteration. They are not overhead or side-work. Plan them as you would any other engineering task.
- **Consult before building.** Before implementing a contribution, the squad consults the relevant Product Line Maintainer to align on approach, API design, and standards. This consult-before-build pattern (step 3 in [Inner Source Guidelines](../product-line-engineering/governance/inner-source-guidelines.md)) significantly reduces rework.
- **PL Maintainers review against DoD.** Product Line Maintainers may approve, request changes, or merge with a tech debt tag per [Tech Debt Policy](../product-line-engineering/governance/tech-debt-policy.md). The squad does not bypass this review.
- **EPM must have visibility.** Inner source contributions may affect squad delivery timelines — especially when PL Maintainer review takes longer than expected or when changes are requested. EPM needs to know this is happening so the integrated schedule reflects it.

---

## What We Do Not Build

Engagement Engineering extends platforms; it does not replace them. The guardrails:

- **Extend, don't fork.** No duplicating Product Line logic, no parallel data models, no standalone systems that bypass the Customer Product.
- **Studio work stays anchored.** Integration adapters, custom UIs, and orchestration flows are built on top of the Customer Product and Product Lines — not alongside them.
- **No parallel standalone systems.** If the work isn't amplifying a Product Line, it doesn't belong in the Engagement.
- **Borderline cases go to the EA.** When it's unclear whether work is extension or divergence, the EA makes the call — escalating to engineering leadership if needed.
- **Reusable work goes back to the platform.** When Engagement-specific work proves generally useful, it must be contributed back to Product Lines via inner source — not kept as Engagement-owned code that duplicates platform capability. EA identifies what should go back; ELs execute. Work that remains one-off must be documented and owned by the Engagement squad for the lifecycle of the Engagement.

The leader test: *"Is this amplifying the Product Line, or replacing it?"*

---

## Where to Go Next

| To understand... | Read... |
|-----------------|---------|
| Pre-Engagement work | [Exploration](exploration.md) |
| Who does what | [Roles and Responsibilities](roles.md) |
| Phase-by-phase delivery | [Lifecycle](lifecycle.md) |
| How squads are composed and staffed | [Squad Model and Staffing](squad-model.md) |
| Architecture and archetype application | [Architecture and Archetypes](architecture-and-archetypes.md) |
| How the assembly is verified | [Verification and Certification](verification-and-certification.md) |
| Governance and escalation | [Governance and Escalation](governance.md) |
| How success is measured | [Metrics and Feedback](metrics-and-feedback.md) |

---

[→ Next: Exploration](exploration.md)
