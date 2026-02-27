# Product Line Engineering

## Purpose

**Product Line Engineering** is the PLE layer that develops and maintains **core assets**—the platforms and frameworks that Customer Products are derived from. Product Line Squads own platform maturity, reliability, maintainability, and reusability. They do not own customer-specific delivery; that is Engagement Engineering.

---

## Product Line Squads Structure

Zeta’s Product Line platforms and their owning teams:

| Product Line Squad | Platform | Primary Focus |
|-------------|----------|---------------|
| **Olympus Product Line Squad** | Olympus (Cloud & Application Management) | Agent runtime, operations orchestration, observability |
| **Tachyon Product Line Squad** | Tachyon (Core Banking & Payments Hub) | Payment processing, transaction orchestration, settlement |
| **Neutrino Product Line Squad** | Neutrino (Consumer Digital Banking & Servicing) | Customer interaction, channel orchestration, servicing agents |
| **Electron Product Line Squad** | Electron (Commercial Cards) | Card lifecycle, expense management, policy engines |
| **Quark Product Line Squad** | Quark (Business Operations Automation) | Workflow engines, integration patterns, automation |

Almost every Customer Product uses **Olympus** and **Tachyon**; other platforms are included as needed. Product Line Squads provide:

- Core platform capabilities and APIs
- Extension points and configuration mechanisms
- Reference integration patterns
- Platform operations (via SRE; platform is always Zeta-operated)

---

## Product Line Engineer Role

**Product Line Engineers** develop and maintain core platform assets. They:

- Build and evolve platform capabilities, frameworks, and APIs
- Design for reusability and clear extension boundaries
- Participate in inner source: review and accept contributions from Customer Product Squads (when acting as or supporting Product Line Maintainers)
- May be **assigned** to Customer Product Squads for Engagements (rotation model)

**Expectations:**

- Focus on platform maturity, reliability, maintainability, and efficiency
- Align with platform roadmap and Council-defined standards
- When on Engagement: deliver per Customer Product Squad needs while adhering to DoD and platform standards; contribute back via inner source where appropriate

**Home team:** A Product Line Engineer’s home team is their Product Line Squad. Engagement assignment is temporary; return is guaranteed per the [rotation model](../processes/rotation-model.md).

---

## Product Line Maintainer Role

**Product Line Maintainers** are dedicated to **governing contributions** to a Product Line platform. They:

- Review and approve (or reject) PRs from Customer Product Squads and others
- Enforce [Definition of Done](../governance/inner-source-guidelines.md#definition-of-done) and platform standards
- Coach contributors on approach and quality
- Escalate disputes or quality issues to the Platform Architecture Council

**Rotation:** Product Line Maintainer is a dedicated role but **rotated** (e.g. quarterly or semester) so that the burden and expertise are shared and no single person becomes a bottleneck.

**Authority:** Maintainers can approve, request changes, or accept with tech-debt tagging per [tech debt policy](../governance/tech-debt-policy.md). They do not unilaterally merge substandard work without tagging or escalation.

**Relationship:** Maintainers work within the Product Line Squad; they may also do development work, but their primary accountability is gatekeeping and quality for contributions to that platform.

---

## Relationship to Engagement Engineering

- **Assigning engineers:** Product Line Squads assign Product Line Engineers to Customer Product Squads for the duration of an Engagement (or a rotation period within it). Capacity planning and Engagement forecasting are used to balance platform work and assigned capacity.
- **Inner source:** Customer Product Squads may contribute code to Product Line platforms via PRs. Product Line Maintainers review and merge (or reject, or accept with tech debt). See [Inner Source Guidelines](../governance/inner-source-guidelines.md).
- **No “intake” bottleneck as sole path:** The primary path for new platform capability from Engagements is inner source (EA prioritizes, consult, build, PR). Formal intake for larger initiatives may still exist for strategic roadmap items.

Product Line Squads retain ownership of core assets. Customer Product Squads own the Customer Product; they use and extend platforms within governance boundaries.

---

## Success Metrics for Product Line Engineering

| Metric | Purpose |
|--------|---------|
| **Platform activation time** | Time from contract to platform-ready for an Engagement |
| **Asset reusability** | Proportion of Customer Product that comes from core assets vs. custom build |
| **Platform reliability** | Uptime, performance, error rates (e.g. SLAs) |
| **Inner source health** | PR cycle time, proportion merged vs. rejected, tech debt trend |
| **Developer productivity** | Time to implement common patterns; feedback from Customer Product Squads |

Product Line Squads are evaluated on platform quality and reuse, not on Engagement count. Delivery success is owned by Engineering Leads (ELs) and EPM within the Engagement.

---

## References

- [PLE Overview](ple-overview.md)
- [Engagement Engineering](engagement-engineering.md)
- [Inner Source Guidelines](../governance/inner-source-guidelines.md)
- [Rotation Model](../processes/rotation-model.md)
- [Product Line Maintainer Role](../roles/product-line-maintainer.md)
