# Knowledge Ownership

[← Back to Knowledge Engineering](README.md) | [← Back to ERE](../README.md)

Knowledge Engineering is not the responsibility of the whole team — it is owned by **1-2 dedicated people** who own the *system*, with contributions coming from across the organization.

---

## Ownership Model

| Role | Responsibility |
|------|----------------|
| **Knowledge Engineer** | Owns the knowledge base system, taxonomy, quality standards, and curation workflows |
| **Domain Stewards** (rotating) | SMEs from Engagements who validate and enrich domain-specific content |

---

## Knowledge Engineer

The Knowledge Engineer is a dedicated role within the ERE team, accountable for the health and effectiveness of the knowledge base.

### Responsibilities

| Area | Responsibility |
|------|----------------|
| **System ownership** | Knowledge base infrastructure, search, taxonomy, access controls |
| **Quality standards** | Defines completeness criteria, reusability scores, tagging requirements |
| **Curation workflows** | Processes for contribution, review, approval, and retirement |
| **Metrics & reporting** | Coverage dashboards, freshness tracking, contribution leaderboards |
| **Steward coordination** | Recruits, onboards, and supports Domain Stewards |
| **Gap analysis** | Identifies domains and archetypes with insufficient coverage |

### Accountability

| Metric | Knowledge Engineer Accountable For |
|--------|-----------------------------------|
| **Coverage** | % of archetypes/domains with adequate knowledge artifacts (target: >80%) |
| **Quality score** | Average quality rating across knowledge base (target: >4.0/5.0) |
| **Freshness** | % of knowledge artifacts reviewed within policy period (target: >90% current) |

### Not Responsible For

The Knowledge Engineer does **not** personally create all knowledge artifacts. They:
- Own the *system* that enables capture
- Define *standards* for quality
- Coordinate *Stewards* who validate domain content
- Track *metrics* that drive accountability

---

## Domain Stewards

Domain Stewards are **rotating SMEs from Engagements** who bring deep domain expertise and validate knowledge artifacts in their area.

### Selection Criteria

| Criterion | Description |
|-----------|-------------|
| **Domain expertise** | Deep knowledge of specific archetype, technology, or business domain |
| **Recent experience** | Active in Engagements within the past 6 months |
| **Credibility** | Respected by peers as authoritative source |
| **Availability** | Capacity to dedicate ~5% of time to stewardship |

### Responsibilities

| Area | Responsibility |
|------|----------------|
| **Content validation** | Reviews contributed artifacts for technical accuracy |
| **Enrichment** | Adds context, examples, or connections that increase reusability |
| **Gap identification** | Flags missing knowledge in their domain |
| **Pattern recognition** | Identifies recurring themes that should become formal patterns |
| **Quality assessment** | Provides ratings on completeness and reusability |

### Rotation Model

| Aspect | Policy |
|--------|--------|
| **Term length** | 6 months (renewable) |
| **Overlap** | New Steward shadows outgoing for 2-4 weeks |
| **Domain coverage** | At least one Steward per major archetype |
| **Recognition** | Stewardship visible in career development; contribution to ERE acknowledged |

---

## Contribution Model

Knowledge artifacts flow from Engagements into the knowledge base through a structured contribution model:

```
┌─────────────────────────────────────────────────────────┐
│                    Engagements                          │
│   (EPMs, EAs, ELs create artifacts as work products)    │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              AI-Assisted Extraction                     │
│   (Pattern Curator Agent proposes knowledge artifacts)  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Domain Steward Review                      │
│   (Validates accuracy, enriches context)                │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Knowledge Base                             │
│   (Searchable, tagged, quality-scored)                  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Reuse in Future Engagements                │
│   (Proposals, architectures, patterns)                  │
└─────────────────────────────────────────────────────────┘
```

---

## Accountability Summary

| Role | Accountable For | Reports To |
|------|-----------------|------------|
| **EPM** | Knowledge capture within their Engagement (contribution rate) | ERC reviews aggregate |
| **Knowledge Engineer** | Knowledge base health (coverage, quality, freshness) | ERE Product Manager |
| **Domain Steward** | Domain content accuracy and enrichment | Knowledge Engineer |
| **ERC** | Aggregate knowledge metrics; policy decisions | — |

---

*See also: [Lifecycle Capture](lifecycle-capture.md) | [Pattern Curator Agent](pattern-curator.md) | [Knowledge Governance](../06-governance-enforcement/knowledge-governance.md)*
