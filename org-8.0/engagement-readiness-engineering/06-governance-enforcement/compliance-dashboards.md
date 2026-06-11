# Compliance Dashboards

[← Back to Governance Enforcement](README.md) · [ERE Guide](../README.md)

ERC gains visibility into governance health through three categories of compliance dashboards.

---

## Delivery Compliance

Metrics tracking Engagement lifecycle governance:

| Metric | What It Measures | Target |
|--------|------------------|--------|
| **Gate pass rate** | Percentage of Engagements passing gates without exception | >90% |
| **Exception frequency** | Volume and reasons for documented exceptions | Decreasing trend |
| **Time at gates** | Cycle time blocked at each gate (identifies friction points) | <5 days average |
| **Tool adoption** | Usage metrics by tool, role, and Engagement | >80% active usage |

### Gate Pass Rate Breakdown

| Gate | Pass Rate | Common Exception Reasons |
|------|-----------|-------------------------|
| Exploration → Initiate | % | (populated from data) |
| Initiate | % | |
| Discover | % | |
| Build | % | |
| Transfer | % | |
| Complete | % | |

### Exception Analysis

| Exception Category | Count | Trend | Action Required |
|--------------------|-------|-------|-----------------|
| Documentation gaps | — | — | — |
| Staffing constraints | — | — | — |
| Customer dependencies | — | — | — |
| Tool limitations | — | — | — |

---

## Knowledge Compliance

Metrics tracking knowledge capture and contribution:

| Metric | What It Measures | Target |
|--------|------------------|--------|
| **Capture completion** | % of required knowledge artifacts captured at each gate | 100% |
| **Contribution leaderboard** | Individuals and teams ranked by contribution rate and reuse | Visible recognition |
| **Gap alerts** | Domains or archetypes with insufficient coverage | <5 critical gaps |

### Contribution Rate by Phase

| Phase Transition | Required Artifacts | Capture Rate |
|------------------|-------------------|--------------|
| Exploration → Initiate | Exploration summary, qualification rationale | % |
| Discover → Build | Architecture decisions, gap analysis | % |
| Build → Transfer | Variability docs, inner source contributions | % |
| Transfer → Complete | Retrospective, lessons learned | % |
| Complete | Case study draft, patterns tagged | % |

### Coverage by Domain

| Domain / Archetype | # Artifacts | # Gaps | Coverage % |
|--------------------|-------------|--------|------------|
| (populated by archetype) | — | — | — |

### Contribution Leaderboard

| Rank | Contributor | Artifacts | Reuse Count | Quality Score |
|------|-------------|-----------|-------------|---------------|
| 1 | — | — | — | — |
| 2 | — | — | — | — |
| 3 | — | — | — | — |

---

## AI Agent Compliance

Metrics tracking AI agent performance and governance:

| Metric | What It Measures | Target |
|--------|------------------|--------|
| **Agent accuracy** | % of agent outputs accepted without modification | >85% |
| **Escalation rate** | % of requests escalated to humans | <10% for routine tasks |
| **Autonomy utilization** | % of automative capacity actually used | >70% |

### Agent Performance by Type

| Agent | Accuracy | Escalation Rate | Autonomy Level | Status |
|-------|----------|-----------------|----------------|--------|
| Engagement Concierge | % | % | Assistive / Automative | — |
| Proposal Agent | % | % | Assistive / Automative | — |
| BRD Agent | % | % | Assistive / Automative | — |
| Governance Agent | % | % | Assistive / Automative | — |
| Retrospective Agent | % | % | Assistive / Automative | — |

### Autonomy Progression Tracking

| Agent | Current Level | Progression Criteria | Progress | Ready for Advancement |
|-------|---------------|---------------------|----------|----------------------|
| Engagement Concierge | Assistive | 90%+ accuracy; <5% escalation | —% / —% | ☐ |
| Proposal Agent | Assistive | 80%+ acceptance rate | —% | ☐ |
| Governance Agent | Assistive | 95%+ accuracy on completeness | —% | ☐ |

### Error Analysis

| Error Category | Count | Impact | Remediation |
|----------------|-------|--------|-------------|
| Factual errors | — | — | — |
| Format issues | — | — | — |
| Scope exceeded | — | — | — |
| Confidence miscalibration | — | — | — |

---

## Dashboard Access

| Role | Delivery | Knowledge | AI Agent |
|------|----------|-----------|----------|
| ERC | Full | Full | Full |
| EPM | Own Engagement | Own Engagement | Summary |
| Knowledge Engineer | Summary | Full | — |
| EO / Client Partner | Own Engagement | Own Engagement | — |

---

## Refresh Cadence

| Dashboard | Refresh Frequency |
|-----------|-------------------|
| Delivery Compliance | Real-time |
| Knowledge Compliance | Daily |
| AI Agent Compliance | Hourly |

---

## Related Content

- [Gates and Checkpoints](gates-checkpoints.md) — what the gates require
- [Knowledge Governance](knowledge-governance.md) — contribution metrics detail
- [AI Architecture](../03-ai-architecture/README.md) — agent capabilities and design
