# Variability Management

## Why Variability Management Matters

Customer Solutions differ in configuration, extensions, and integrations. Without explicit variability management:

- It becomes unclear what varies between customers and why
- Reuse and consistency suffer; similar needs are solved differently
- Scaling to more engagements increases divergence and support cost

Even **lightweight** variability management — documenting what varies, how, and who uses it—improves alignment, reuse, and governance. Zeta does not require heavy formal tooling (e.g. feature models) at the start; we use documentation and Council governance. Tooling can be added later if scale or complexity justify it.

---

## Critical Requirement: Solution Architects and Council

**Solution Architects** and the **Platform Architecture & Practice Council** are responsible for variability documentation and governance.

- **Solution Architects** document variability **per engagement**: which configuration points were used, which options were chosen, binding time, and how this maps to the chosen archetype and customer.
- **Council** owns **variability governance**: reviewing variability across engagements, approving new configuration points or options, deprecating unused or harmful variants, and ensuring the variability model stays coherent and documented.

This is a **mandatory** part of the Solution Architect role and of Council practice, not optional.

---

## Variability Documentation Template

For each **configuration point** (a place where Customer Solutions can differ), document:

| Field | Description | Example |
|-------|-------------|---------|
| **Configuration Point** | Name and scope of the variation | Payment rails |
| **Options** | Allowed values or choices | Visa, Mastercard, RuPay, UPI, RTP |
| **Binding Time** | When the choice is made | Design time, deploy time, runtime |
| **Which Customers Use What** | Mapping of customer/engagement to chosen option(s) | Bank A: Visa, Mastercard, UPI; Bank B: Visa, RuPay |
| **Archetype** | Which solution archetype(s) this applies to | Credit Card Issuer, Payments Hub |
| **Owner** | Who owns this configuration point (e.g. Domain Team) | Tachyon Domain Team |

**Format:** A spreadsheet, wiki table, or lightweight database is sufficient initially. The important part is that every engagement’s variability choices are recorded and that Council can review them.

**Per-engagement:** The Solution Architect ensures that for their engagement, all configuration points used are documented and that any new option or point is proposed to Council if it’s not already in the variability model.

---

## Council’s Role in Variability Governance

The Platform Architecture & Practice Council:

- **Reviews variability** on a regular cadence (e.g. quarterly): what’s used, what’s unused, what’s inconsistent
- **Approves new configuration points or options** when an engagement needs something not yet in the model
- **Deprecates** options or points that are unused or harmful (with migration path)
- **Resolves disputes** when engagements need conflicting or overlapping variants
- **Feeds back to Domain Teams** when variability suggests platform or archetype changes

Council does not need to approve every single engagement’s choices if they fall within already-documented options; it governs the **model** and the **exceptions**.

---

## Quarterly Variability Review Process

1. **Collect** — Solution Architects submit (or update) variability documentation for their engagements; Council secretariat aggregates.
2. **Analyze** — Council reviews: usage frequency, consistency across archetypes, overlap with platform capabilities.
3. **Decide** — Council agrees: new points/options to add, existing ones to deprecate or clarify, guidance to Domain Teams or archetype owners.
4. **Document** — Decisions and updated variability model are documented and communicated.
5. **Follow-up** — Domain Teams and Solution Architecture update archetypes and platform configuration docs as needed.

---

## Future: Tooling for Variability Management

If engagement count or complexity grows, consider:

- A simple **variability registry** (e.g. structured store or tool) instead of only spreadsheets
- **Feature or configuration models** for high-variability platforms
- **Automated checks** that engagements only use approved options

Until then, documented configuration points, options, binding time, and customer usage—owned by Solution Architects and governed by Council—are the standard.

---

## References

- [Solution Architect Role](../roles/solution-architect.md) — Variability tracking ownership
- [Council Charter](../governance/council-charter.md) — Variability governance
- [Solution Archetypes](solution-archetypes.md) — How archetypes relate to variability
