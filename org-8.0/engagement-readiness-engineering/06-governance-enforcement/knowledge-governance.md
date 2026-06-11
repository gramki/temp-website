# Knowledge Governance

[← Back to Governance Enforcement](README.md) · [ERE Guide](../README.md)

Knowledge capture is governed with the same rigor as delivery. This ensures knowledge becomes an organizational asset, not an afterthought.

---

## Contribution Metrics

| Metric | What It Measures | Target | Visibility |
|--------|------------------|--------|------------|
| **Contribution rate** | # of knowledge artifacts contributed per Engagement | 100% of phase transitions have required artifacts | EPM dashboard, ERC portfolio view |
| **Reuse rate** | # of times contributed artifacts are reused in other Engagements | Increasing trend | Individual recognition, team metrics |
| **Coverage** | % of archetypes/domains with adequate knowledge artifacts | >80% coverage | Knowledge Engineer dashboard |
| **Quality score** | Average quality rating (completeness, reusability, findability) | >4.0/5.0 | Contributor profiles |
| **Freshness** | % of knowledge artifacts reviewed within policy period | >90% current | Knowledge Engineer dashboard |

---

## Accountability Model

Clear accountability ensures knowledge capture happens:

| Role | Accountable For | Measured By |
|------|-----------------|-------------|
| **EPM** | Knowledge capture within their Engagement | Contribution rate — all required artifacts at each phase transition |
| **Knowledge Engineer** | Knowledge base health | Coverage, quality, freshness metrics |
| **ERC** | Aggregate knowledge metrics | Quarterly review of portfolio-level knowledge health |

### EPM Accountability

EPMs are accountable for ensuring their Engagement produces required knowledge artifacts:

- **At each phase transition** — required artifacts captured per [Knowledge Gates](gates-checkpoints.md)
- **Visible in staffing** — knowledge capture is 5-10% of Engagement capacity (not hidden overhead)
- **Part of Engagement success** — knowledge contribution is a success metric alongside delivery

### Knowledge Engineer Accountability

The Knowledge Engineer owns the system, not the content:

- **Taxonomy and structure** — knowledge is organized and findable
- **Quality standards** — content meets reusability criteria
- **Curation workflows** — contributor submissions are reviewed and improved
- **Gap identification** — proactively identifies coverage gaps

### ERC Accountability

ERC reviews aggregate knowledge metrics quarterly:

- **Coverage trends** — are we capturing knowledge across all archetypes?
- **Contribution patterns** — are some teams/Engagements under-contributing?
- **Quality trends** — is content quality improving?
- **Utilization** — is captured knowledge being reused?

---

## Quality Criteria

Each knowledge artifact is evaluated against four quality dimensions:

| Criterion | What It Measures | How It's Assessed |
|-----------|------------------|-------------------|
| **Completeness** | All required sections populated; no significant gaps | Automated checklist + human review |
| **Reusability** | Content structured for future reuse; not Engagement-specific jargon | Human review (Knowledge Engineer or Domain Steward) |
| **Findability** | Proper tagging, categorization, and linking | Automated tagging validation + search testing |
| **Freshness** | Content reviewed within policy period (e.g., 6 months) | Automated tracking + review reminders |

### Quality Score Calculation

Quality score (1-5) is computed as:

```
Quality Score = (Completeness × 0.3) + (Reusability × 0.3) + (Findability × 0.2) + (Freshness × 0.2)
```

Each dimension is scored 1-5 by reviewer.

---

## Contribution Recognition

Knowledge contribution is visible and recognized:

| Recognition Mechanism | Description |
|----------------------|-------------|
| **Contribution leaderboard** | Public dashboard showing top contributors by volume and quality |
| **Reuse attribution** | When content is reused, original contributor is credited |
| **Quality badges** | High-quality contributions earn badges (visible in profiles) |
| **Quarterly recognition** | ERC recognizes top contributors quarterly |
| **Career impact** | Contribution history is part of performance discussions |

---

## Coverage Management

### Coverage Targets

| Category | Minimum Coverage | Current | Gap |
|----------|------------------|---------|-----|
| Each archetype | 3+ case studies | — | — |
| Each domain | 5+ reusable patterns | — | — |
| Each Product Line | Architecture decisions documented | — | — |

### Gap Alerts

The Knowledge Engineer monitors for:

- **Archetype gaps** — archetypes with <3 case studies
- **Domain gaps** — domains with <5 patterns
- **Freshness gaps** — content not reviewed in >6 months
- **Engagement gaps** — completed Engagements with missing retrospectives

Gap alerts appear in the Knowledge Compliance dashboard and trigger outreach to relevant EPMs.

---

## Freshness Policy

Knowledge has a shelf life. The freshness policy ensures content stays current:

| Content Type | Review Cadence | Trigger for Review |
|--------------|----------------|-------------------|
| Architecture patterns | 6 months | Technology changes, pattern superseded |
| Case studies | Annual | Customer reference approval, outcome updates |
| Best practices | 6 months | Process changes, feedback incorporation |
| Retrospective themes | Quarterly | Aggregation into systemic improvements |

### Stale Content Process

1. **Alert** — content marked stale after review period
2. **Assignment** — Knowledge Engineer assigns reviewer (original author or Domain Steward)
3. **Review** — content updated, archived, or marked as "historical"
4. **Completion** — freshness reset; appears current in dashboard

---

## Integration with Delivery

Knowledge capture is integrated into delivery, not a separate activity:

| Delivery Activity | Knowledge Capture |
|-------------------|-------------------|
| Discovery meetings | Meeting notes auto-extracted to knowledge base |
| Architecture decisions | ADRs tagged for pattern library |
| Retrospectives | Themes extracted for systemic analysis |
| Go-live | Case study template pre-populated |

This "capture at the source" approach reduces the burden on EPMs while ensuring completeness.

---

## Related Content

- [Gates and Checkpoints](gates-checkpoints.md) — knowledge gates at phase transitions
- [Compliance Dashboards](compliance-dashboards.md) — knowledge compliance visibility
- [Knowledge Engineering](../04-knowledge-engineering/README.md) — ownership and principles
