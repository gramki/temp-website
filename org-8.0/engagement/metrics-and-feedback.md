# Metrics and Feedback Loops

[← Back to Guide](README.md)

---

## Metrics and Measurement

| Category | Metric | Owner |
|----------|--------|-------|
| **Delivery** | Delivery velocity (Initiate to production) | EPM |
| **Reuse** | Product Line reuse ratio | EA |
| **Inner source** | Inner source contribution rate | EA, ELs |
| **Quality** | Assembly certification pass rate | AVA |
| **Verification** | Verification module coverage (criteria testable vs. total) | AVA |
| **Verification** | Continuous verification pass rate | AVA |
| **Customer** | Customer satisfaction / adoption | EPM (Engagement Success) |
| **Handover** | Handover quality | EPM, SRE Lead |
| **Architecture** | Archetype coverage | EA |
| **Commercial** | Revenue, margin, contract value | Account Management, EPM |

---

## Knowledge Capture Mechanisms

See [knowledge-capture.md](../product-line-engineering/processes/knowledge-capture.md) for detailed mechanisms.

- **Engagement retrospectives** at Transfer and Complete
- **Decision logs** maintained by EA throughout the Engagement
- **Archetype updates** proposed by EA at Transfer
- **Pattern extraction** via PAC Practice Mode sessions

---

## Engagement → Product Line Feedback

- Inner source contributions flow from CP and Studio squads back to Product Line Squads
- Gap analysis findings inform Product Line roadmaps
- Archetype evolution is driven by Engagement experience

Product Managers may serve as both PL PM (Product Line roadmap) and Customer Product PM (Engagement-specific priorities). This dual vantage tightens the feedback loop between delivery reality and Product Line evolution.

---

## Inner Source Debt Management

- EA maintains the inner source debt and priority view
- ELs execute contributions per EA's prioritization
- Product Line Maintainers review and govern per [Inner Source Guidelines](../product-line-engineering/governance/inner-source-guidelines.md)
- PAC Practice Mode reviews inner source health across the portfolio

---

[← Previous: Governance and Escalation](governance.md) | [→ Next: Completion and Termination](completion-and-termination.md)
