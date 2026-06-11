# ERE Team Structure

[← Back to ERE Guide](../README.md)

---

This section describes the team that builds and operates ERE — from initial dedicated squads through mature state with rotating contributors.

---

## Team Evolution

ERE follows a deliberate evolution from dedicated capacity to a hybrid model:

```
Initial State                    Mature State
─────────────                    ────────────
Dedicated Squad(s)    ───►    Core Team + Rotating Contributors
All roles internal              Platform maintained by core
Full-time focus                 Contributions from Engagements
                                Knowledge Stewards from domains
```

---

## Contents

| Document | What It Covers |
|----------|----------------|
| [Roles](roles.md) | Product Manager, Engineering Lead, Engineers, Designer, Knowledge Engineer, AI/ML Engineer |
| [Capacity Allocation](capacity-allocation.md) | How Engagement capacity is allocated to knowledge and tooling contribution |
| [Success Metrics](success-metrics.md) | Metrics by category: Efficiency, Reuse, Compliance, Adoption, Customer, Knowledge, AI |

---

## Initial State: Dedicated Squad(s)

The function starts with dedicated product and engineering capacity operating as an internal product team with clear OKRs. The squad(s) report into ERC leadership.

Key characteristics:
- Full ownership of ERE roadmap and delivery
- Clear accountability for tool adoption and reliability
- Direct line to ERC for prioritization and resource allocation
- Focused investment to establish foundation

See [Roles](roles.md) for the detailed breakdown of initial team composition.

---

## Mature State: Rotating Contributors

As tooling matures and patterns stabilize:

| Component | Ownership |
|-----------|-----------|
| **Core Team** | Maintains platform, high-complexity components, and AI agents |
| **Knowledge Engineer + Domain Stewards** | Maintain knowledge base (Stewards are rotating SMEs) |
| **Engineers rotating from Engagements** | Contribute improvements, templates, patterns, knowledge artifacts |

### Contribution Model

Engineers rotating from Engagements contribute through a structured inner source model:

| Contribution Type | Examples |
|-------------------|----------|
| Bug fixes | Issues discovered during Engagement use |
| Incremental improvements | UX refinements, performance optimizations |
| New templates and patterns | Templates derived from Engagement experience |
| Feedback-driven enhancements | Addressing user pain points |
| Knowledge artifacts | Case studies, pattern candidates, retrospective insights |

Contributions flow through structured PRs reviewed by the core team, mirroring the inner source model used for Product Line contributions.

---

## Reporting Structure

```
ERC Leadership
      │
      ▼
ERE Product Manager
      │
      ├── Engineering Lead
      │         │
      │         ├── Engineers
      │         └── AI/ML Engineer
      │
      ├── Designer
      │
      └── Knowledge Engineer
                │
                └── Domain Stewards (rotating)
```

---

## Success Criteria

ERE team success is measured across multiple dimensions:

- **Efficiency:** Cycle time reduction at lifecycle phase transitions
- **Adoption:** Active tool usage by role and phase
- **Compliance:** Gate pass rates (delivery and knowledge)
- **Customer:** Portal NPS and Concierge resolution rate
- **Knowledge:** Capture completion, reuse rate, coverage
- **AI:** Agent accuracy and autonomy progression

See [Success Metrics](success-metrics.md) for the complete metrics framework.

---

## Next Steps

- [Roles](roles.md) — Detailed role descriptions
- [Capacity Allocation](capacity-allocation.md) — How time is budgeted for knowledge and contribution
- [Success Metrics](success-metrics.md) — How we measure team effectiveness

---

[← Previous: Governance Enforcement](../06-governance-enforcement/README.md) | [→ Next: Roadmap](../08-roadmap/README.md)
