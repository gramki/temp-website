# Open Questions

[← Back to ERE Guide](../README.md)

Unresolved decisions and questions that require further discussion and resolution. Organized by category.

---

## Integration & Data

| Question | Context | Stakeholders |
|----------|---------|--------------|
| **Integration points** | Which existing systems (Jira, Confluence, Salesforce, ERP) must these tools integrate with? What's the integration strategy? | Engineering, IT, Operations |
| **Data model** | Is there a unified Engagement data model across tools, or will each tool own its data? | Engineering, Architecture |
| **Knowledge base platform** | Build custom or configure existing (Confluence, Notion, custom wiki)? | Engineering, Knowledge Engineering |

### Considerations

- **Build vs. buy** — custom solutions offer flexibility but require maintenance; existing platforms offer maturity but may constrain design
- **Data ownership** — centralized model simplifies reporting but creates coupling; distributed model offers autonomy but complicates cross-tool analytics
- **Integration complexity** — each integration point adds maintenance burden and failure modes

---

## Security & Access

| Question | Context | Stakeholders |
|----------|---------|--------------|
| **Customer portal isolation** | Per-Engagement isolation, role-based access within Engagement, audit logging requirements? | Security, Architecture, Legal |
| **AI agent data access** | What data can agents access? How is sensitive information protected? | Security, Legal, AI/ML Engineering |

### Considerations

- **Multi-tenancy model** — strict isolation vs. shared infrastructure with access control
- **Audit requirements** — regulatory and contractual logging requirements
- **Agent boundaries** — principle of least privilege for AI systems; explicit data access grants

---

## Adoption & Migration

| Question | Context | Stakeholders |
|----------|---------|--------------|
| **Migration** | How do existing Engagements onboard to these tools? Grandfather clause or mandatory transition? | EPMs, ERC, Operations |
| **Training** | What enablement is required for each role to adopt the tools and work with AI agents? | Training, HR, EPMs |
| **Resistance** | How do we handle teams that prefer existing workflows? | Change Management, ERC |

### Considerations

- **Transition period** — parallel systems create overhead but reduce risk; hard cutover is clean but risky
- **Role-specific training** — different roles need different depths of training
- **Change management** — resistance is normal; need clear value proposition and escalation path

---

## AI-Specific

| Question | Context | Stakeholders |
|----------|---------|--------------|
| **Agent training data** | What data is used to fine-tune agents? How is data quality ensured? | AI/ML Engineering, Legal |
| **Agent accountability** | When an agent makes an error with customer impact, who is accountable? | Legal, ERC, Product |
| **Autonomy escalation** | What is the process to advance an agent from Assistive to Automative? | Product, ERC, AI/ML Engineering |

### Considerations

- **Training data provenance** — must ensure data rights and avoid bias
- **Error attribution** — need clear chain of responsibility from agent action to human accountability
- **Progression criteria** — quantitative thresholds plus qualitative review

---

## Knowledge-Specific

| Question | Context | Stakeholders |
|----------|---------|--------------|
| **Incentives** | Beyond metrics, how do we incentivize knowledge contribution? Recognition programs? Career impact? | HR, ERC, Knowledge Engineering |
| **Curation burden** | How do we prevent the Knowledge Engineer from becoming a bottleneck? | Knowledge Engineering, Operations |
| **Stale content** | What is the policy for archiving or retiring outdated knowledge? | Knowledge Engineering, Legal |

### Considerations

- **Intrinsic vs. extrinsic motivation** — recognition visible to peers may be more effective than formal rewards
- **Scalable curation** — AI-assisted triage, Domain Steward delegation, quality thresholds
- **Archival vs. deletion** — legal/compliance requirements may mandate retention; visibility management vs. true deletion

---

## Resolution Process

Questions should be resolved through:

1. **Analysis** — gather data, explore options, document trade-offs
2. **Stakeholder input** — consult affected parties
3. **Decision record** — document decision with rationale (ADR format)
4. **Communication** — inform all stakeholders of resolution

Resolved questions move from this document to:
- Relevant section of the ERE documentation (updated with decision)
- ADR in appropriate repository (if architectural decision)

---

## Status Tracking

| Category | Total | Resolved | Pending |
|----------|-------|----------|---------|
| Integration & Data | 3 | 0 | 3 |
| Security & Access | 2 | 0 | 2 |
| Adoption & Migration | 3 | 0 | 3 |
| AI-Specific | 3 | 0 | 3 |
| Knowledge-Specific | 3 | 0 | 3 |
| **Total** | **14** | **0** | **14** |

---

## Related Content

- [Roadmap](../08-roadmap/README.md) — phased approach may inform resolution order
- [Governance Enforcement](../06-governance-enforcement/README.md) — some questions relate to enforcement approach
- [AI Architecture](../03-ai-architecture/README.md) — AI-specific questions context
