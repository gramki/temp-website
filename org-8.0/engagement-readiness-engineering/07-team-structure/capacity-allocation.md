# ERE Capacity Allocation

[← Back to Team Structure](README.md) · [← Back to ERE Guide](../README.md)

---

This document defines how Engagement capacity is allocated to support ERE objectives — specifically for knowledge capture and tool contribution.

---

## Allocation Model

| Activity | % of Engagement Capacity | Accountability |
|----------|--------------------------|----------------|
| **Knowledge capture** | 5-10% | EPM ensures time is budgeted; ERC reviews aggregate |
| **Tool feedback/contribution** | Included in inner source budget | ELs track; reported to ERC |

---

## Knowledge Capture Allocation

### What It Includes

The 5-10% allocation for knowledge capture covers:

| Activity | Examples |
|----------|----------|
| Artifact creation | Case study drafts, pattern candidates, lessons learned |
| Artifact review | Validating and enriching knowledge base content |
| Tagging and categorization | Ensuring artifacts are findable and properly classified |
| Retrospective participation | Contributing to Retrospective Synthesizer inputs |

### How It's Budgeted

- **Staffing plans** must explicitly show knowledge capture capacity — this is not hidden overhead
- **EPM** is accountable for ensuring the budget is allocated and used
- **ERC** reviews aggregate knowledge contribution rates across the portfolio

### Visibility

Knowledge capture time appears in:
- Engagement staffing plans
- PI capacity allocations
- EPM dashboards
- ERC portfolio reviews

---

## Tool Contribution Allocation

### What It Includes

Tool contribution follows the inner source model and includes:

| Contribution Type | Examples |
|-------------------|----------|
| Bug fixes | Issues discovered during Engagement use |
| Incremental improvements | UX refinements, workflow optimizations |
| New templates | Engagement-specific templates that become reusable |
| Feedback | Structured feedback on tool usability and gaps |

### How It's Tracked

- Contributions flow through **structured PRs** reviewed by the ERE core team
- **ELs** track contribution activity within their squads
- Contribution metrics are **reported to ERC** alongside inner source metrics

### Relationship to Inner Source

ERE tool contribution shares the same budget as Product Line inner source contributions. Both are governed by:

- Structured PR process with core team review
- Quality standards (tests, documentation, code style)
- Recognition in contributor profiles

---

## Accountability Model

| Role | Accountability |
|------|----------------|
| **EPM** | Knowledge capture within their Engagement (contribution rate, artifact quality) |
| **EL** | Tool contributions within their squad (PR submissions, feedback quality) |
| **Knowledge Engineer** | Knowledge base health (coverage, quality, freshness) |
| **ERC** | Aggregate portfolio metrics; capacity adequacy; policy adjustments |

---

## Visibility in Staffing

Capacity allocation is visible — not hidden:

```
Engagement Staffing Plan
────────────────────────
Squad A: 5 engineers
  - Feature delivery: 85%
  - Inner source (PL + ERE): 10%
  - Knowledge capture: 5%
```

This ensures:
- **Transparency:** Leadership sees true cost of knowledge and contribution
- **Accountability:** EPMs can be held accountable for actual vs. budgeted
- **Sustainability:** Teams don't treat knowledge capture as unbudgeted overhead

---

## Adjustment Triggers

Capacity allocation may be adjusted when:

| Trigger | Response |
|---------|----------|
| Knowledge gaps in critical domains | Increase capture allocation for relevant Engagements |
| Low tool adoption | Increase feedback/contribution allocation to address usability |
| High ERE backlog | Temporary increase in rotating contributor capacity |
| Mature knowledge coverage | Reduce capture allocation; shift to maintenance mode |

ERC reviews capacity adequacy quarterly and adjusts policy as needed.

---

## Next Steps

- [Success Metrics](success-metrics.md) — How we measure effectiveness of allocated capacity
- [Roles](roles.md) — Who is accountable for each allocation area
- [Team Structure Overview](README.md) — Full team structure context
