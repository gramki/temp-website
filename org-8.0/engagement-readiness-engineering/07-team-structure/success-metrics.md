# ERE Success Metrics

[← Back to Team Structure](README.md) · [← Back to ERE Guide](../README.md)

---

This document defines the metrics used to measure ERE effectiveness across all objectives.

---

## Metrics by Category

| Category | Metric | What It Measures |
|----------|--------|------------------|
| **Efficiency** | Cycle time reduction | Improvement in phase durations (Exploration → Initiate, Build → Go-live) |
| **Reuse** | Reuse ratio | % of proposals/architectures derived from existing artifacts |
| **Compliance** | Gate pass rate | Engagements passing gates (delivery + knowledge) on first attempt |
| **Adoption** | Tool adoption | Active usage by tool, role, and phase |
| **Customer** | Portal NPS | Customer satisfaction with self-service portal |
| **Customer** | Concierge resolution rate | % of customer queries resolved by Engagement Concierge without escalation |
| **Knowledge** | Capture completion | % of required knowledge artifacts captured at each gate |
| **Knowledge** | Reuse rate | # of times contributed artifacts are reused |
| **Knowledge** | Coverage | % of archetypes/domains with adequate knowledge artifacts |
| **AI** | Agent accuracy | % of agent outputs accepted without modification |
| **AI** | Autonomy progression | # of agents advanced from Assistive to Automative |

---

## Efficiency Metrics

### Cycle Time Reduction

**Definition:** Improvement in elapsed time for key phase transitions.

| Transition | Baseline | Target |
|------------|----------|--------|
| Exploration → Initiate | Measured at start | Reduction over baseline |
| Discover → Build | Measured at start | Reduction over baseline |
| Build → Go-live | Measured at start | Reduction over baseline |

**Measurement:** Compare phase duration averages before and after tool adoption.

**Owner:** Product Manager

---

## Reuse Metrics

### Reuse Ratio

**Definition:** Percentage of new proposals, architectures, or other artifacts that incorporate content from the knowledge base.

**Target:** Increasing trend; specific targets set per artifact type.

**Measurement:** Track reuse flags in Proposal Kit, Architecture Agent, BRD Author.

**Owner:** Knowledge Engineer

---

## Compliance Metrics

### Gate Pass Rate

**Definition:** Percentage of Engagements passing gates without exceptions on first attempt.

| Gate Type | What It Measures |
|-----------|------------------|
| Delivery gates | Lifecycle phase transitions (Initiate, Discover, Build, etc.) |
| Knowledge gates | Required artifact capture at each transition |

**Target:** >90% first-attempt pass rate at maturity.

**Measurement:** Governance Prep Suite tracking.

**Owner:** Product Manager (delivery); Knowledge Engineer (knowledge)

---

## Adoption Metrics

### Tool Adoption

**Definition:** Active usage measured by tool, role, and lifecycle phase.

| Dimension | Measurement |
|-----------|-------------|
| By tool | % of Engagements using each tool |
| By role | % of EPMs, EAs, etc. actively using relevant tools |
| By phase | Tool usage concentration across lifecycle phases |

**Target:** >80% adoption for core tools within target roles.

**Owner:** Product Manager

---

## Customer Metrics

### Portal NPS

**Definition:** Customer satisfaction with the self-service portal (Net Promoter Score).

**Measurement:** Periodic survey of portal users.

**Target:** >50 NPS at maturity.

**Owner:** Designer (UX); Product Manager (overall)

### Concierge Resolution Rate

**Definition:** Percentage of customer queries resolved by the Engagement Concierge without escalation to human team members.

**Target:** >70% resolution rate for routine queries.

**Measurement:** Concierge interaction logs.

**Owner:** AI/ML Engineer

---

## Knowledge Metrics

### Capture Completion

**Definition:** Percentage of required knowledge artifacts captured at each gate.

| Phase Transition | Required Artifact |
|------------------|-------------------|
| Exploration → Initiate | Exploration summary, qualification rationale |
| Discover → Build | Architecture decisions, gap analysis |
| Build → Transfer | Variability documentation, inner source contributions |
| Transfer → Complete | Retrospective, lessons learned |
| Complete (exit) | Case study draft, reusable artifacts tagged |

**Target:** 100% of required artifacts captured.

**Owner:** EPM (per Engagement); Knowledge Engineer (aggregate)

### Reuse Rate

**Definition:** Number of times contributed artifacts are reused in other Engagements.

**Measurement:** Tracked via Proposal Repository, Pattern Library, Case Study citations.

**Owner:** Knowledge Engineer

### Coverage

**Definition:** Percentage of archetypes and domains with adequate knowledge artifacts.

**Target:** >80% coverage across active archetypes.

**Measurement:** Knowledge base inventory vs. archetype/domain taxonomy.

**Owner:** Knowledge Engineer

---

## AI Metrics

### Agent Accuracy

**Definition:** Percentage of agent outputs (drafts, recommendations, responses) accepted without modification.

| Agent | Initial Target | Mature Target |
|-------|----------------|---------------|
| Proposal Agent | 70% | 85% |
| BRD Agent | 75% | 90% |
| Concierge | 80% | 95% |

**Measurement:** User acceptance/rejection tracking in agent interfaces.

**Owner:** AI/ML Engineer

### Autonomy Progression

**Definition:** Number of agents advanced from Assistive to Automative autonomy level.

**Measurement:** ERC quarterly autonomy reviews.

**Owner:** AI/ML Engineer; ERC (governance)

---

## Dashboard Structure

Metrics are surfaced through three dashboards:

### Delivery Compliance Dashboard

- Gate pass rate
- Exception frequency
- Time at gates (friction points)
- Tool adoption

### Knowledge Compliance Dashboard

- Capture completion
- Contribution leaderboard
- Gap alerts
- Freshness metrics

### AI Agent Dashboard

- Agent accuracy
- Escalation rate
- Autonomy utilization
- Feedback loop health

---

## Review Cadence

| Review | Frequency | Owner |
|--------|-----------|-------|
| Operational metrics | Weekly | Engineering Lead |
| Adoption and compliance | Monthly | Product Manager |
| Knowledge health | Monthly | Knowledge Engineer |
| AI agent performance | Monthly | AI/ML Engineer |
| Full portfolio review | Quarterly | ERC |

---

## Next Steps

- [Capacity Allocation](capacity-allocation.md) — How capacity supports these metrics
- [Roles](roles.md) — Who owns each metric
- [Roadmap](../08-roadmap/README.md) — How metrics evolve across phases
