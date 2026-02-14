# Domain Engineering

## Purpose

**Domain Engineering** is the PLE layer that develops and maintains **core assets**—the platforms and frameworks that Customer Solutions are derived from. Domain Teams own platform maturity, reliability, maintainability, and reusability. They do not own customer-specific delivery; that is Win Engineering.

---

## Domain Teams Structure

Zeta’s domain platforms and their owning teams:

| Domain Team | Platform | Primary Focus |
|-------------|----------|---------------|
| **Olympus Domain Team** | Olympus (Cloud & Application Management) | Agent runtime, operations orchestration, observability |
| **Tachyon Domain Team** | Tachyon (Core Banking & Payments Hub) | Payment processing, transaction orchestration, settlement |
| **Neutrino Domain Team** | Neutrino (Consumer Digital Banking & Servicing) | Customer interaction, channel orchestration, servicing agents |
| **Electron Domain Team** | Electron (Commercial Cards) | Card lifecycle, expense management, policy engines |
| **Quark Domain Team** | Quark (Business Operations Automation) | Workflow engines, integration patterns, automation |

Almost every Customer Solution uses **Olympus** and **Tachyon**; other platforms are included as needed. Domain Teams provide:

- Core platform capabilities and APIs
- Extension points and configuration mechanisms
- Reference integration patterns
- Platform operations (via SRE; platform is always Zeta-operated)

---

## Domain Engineer Role

**Domain Engineers** develop and maintain core platform assets. They:

- Build and evolve platform capabilities, frameworks, and APIs
- Design for reusability and clear extension boundaries
- Participate in inner source: review and accept contributions from Win Engineering Teams (when acting as or supporting Domain Maintainers)
- May be **loaned** to Win Engineering Teams for engagements (rotation model)

**Expectations:**

- Focus on platform maturity, reliability, maintainability, and efficiency
- Align with platform roadmap and Council-defined standards
- When on engagement: deliver per Win Engineering Team needs while adhering to DoD and platform standards; contribute back via inner source where appropriate

**Home team:** A Domain Engineer’s home team is their Domain Team. Engagement assignment is temporary; return is guaranteed per the [rotation model](../processes/rotation-model.md).

---

## Domain Maintainer Role

**Domain Maintainers** are dedicated to **governing contributions** to a domain platform. They:

- Review and approve (or reject) PRs from Win Engineering Teams and others
- Enforce [Definition of Done](../governance/inner-source-guidelines.md#definition-of-done) and platform standards
- Coach contributors on approach and quality
- Escalate disputes or quality issues to the Platform Architecture & Practice Council

**Rotation:** Domain Maintainer is a dedicated role but **rotated** (e.g. quarterly or semester) so that the burden and expertise are shared and no single person becomes a bottleneck.

**Authority:** Maintainers can approve, request changes, or accept with tech-debt tagging per [tech debt policy](../governance/tech-debt-policy.md). They do not unilaterally merge substandard work without tagging or escalation.

**Relationship:** Maintainers work within the Domain Team; they may also do development work, but their primary accountability is gatekeeping and quality for contributions to that platform.

---

## Relationship to Win Engineering

- **Loaning engineers:** Domain Teams loan Domain Engineers to Win Engineering Teams for the duration of an engagement (or a rotation period within it). Capacity planning and engagement forecasting are used to balance platform work and loaned capacity.
- **Inner source:** Win Engineering Teams may contribute code to domain platforms via PRs. Domain Maintainers review and merge (or reject, or accept with tech debt). See [Inner Source Guidelines](../governance/inner-source-guidelines.md).
- **No “intake” bottleneck as sole path:** The primary path for new platform capability from engagements is inner source (consult, build, PR). Formal intake for larger initiatives may still exist for strategic roadmap items.

Domain Teams retain ownership of core assets. Win Engineering Teams own the Customer Solution; they use and extend platforms within governance boundaries.

---

## Success Metrics for Domain Engineering

| Metric | Purpose |
|--------|---------|
| **Platform activation time** | Time from contract to platform-ready for an engagement |
| **Asset reusability** | Proportion of Customer Solution that comes from core assets vs. custom build |
| **Platform reliability** | Uptime, performance, error rates (e.g. SLAs) |
| **Inner source health** | PR cycle time, proportion merged vs. rejected, tech debt trend |
| **Developer productivity** | Time to implement common patterns; feedback from Win Engineering Teams |

Domain Teams are evaluated on platform quality and reuse, not on engagement count. Delivery success is owned by Win Engineering and Engagement Lead.

---

## References

- [PLE Overview](ple-overview.md)
- [Win Engineering](win-engineering.md)
- [Inner Source Guidelines](../governance/inner-source-guidelines.md)
- [Rotation Model](../processes/rotation-model.md)
- [Domain Maintainer Role](../roles/domain-maintainer.md)
