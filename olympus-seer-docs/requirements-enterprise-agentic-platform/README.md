# Zeta Agent Platform Guidance

## Bank-Grade, Cloud-Portable AI Agents

---

> **A cloud-portable, bank-grade agent platform must exist above CSP offerings—and Zeta is uniquely positioned to build it.**

---

## Document Purpose

This guidance document explains **how Zeta should build an AI agent platform** that enables:

1. **Agent-based products for large and mid-sized banks**
2. **Deployment inside customer cloud accounts / landing zones**
3. **Portability across AWS, Azure, and GCP**
4. **Business continuity via multi-region and multi-cloud setups**
5. **Minimal lock-in to CSP-specific agent frameworks**, while still leveraging hyperscaler value

---

## Audience

| Audience | What They Get |
|----------|---------------|
| **CTO and Board** | Strategic clarity, risk assessment, defensibility |
| **Enterprise Architects** | System design, portability, failure modes |
| **Product Managers** | Scope boundaries, roadmap implications |

---

## Document Structure

### Core Sections

| Section | Title | Description |
|---------|-------|-------------|
| **1** | [Executive Summary](./01-executive-summary.md) | Platform stance, key messages, one-page board summary |
| **2** | [Problem Statement & Strategic Context](./02-problem-statement.md) | Why banks want agents, why agents are hard, regulatory context |
| **3** | [System & Infrastructure Requirements](./03-system-requirements.md) | What the platform must do, independent of CSP |
| **4** | [State of the World: CSP Offerings](./04-csp-offerings.md) | AWS, Azure, GCP comparison with lock-in analysis |
| **5** | [What CSP Offerings Cannot Address](./05-csp-gaps.md) | Structural gaps in CSP platforms |
| **6** | [Zeta's Solution Principles](./06-solution-principles.md) | Non-negotiable design principles |
| **7** | [Conceptual Architecture](./07-conceptual-architecture.md) | Control plane vs. execution plane |
| **8** | [Platform Components & Design Rationale](./08-platform-components.md) | Detailed component specifications |
| **9** | [Platform Services Summary Table](./09-platform-services-table.md) | Ownership and portability matrix |
| **10** | [Product & Go-To-Market Implications](./10-gtm-implications.md) | Why this matters commercially |
| **11** | [Non-Goals and Boundaries](./11-non-goals.md) | What Zeta will not build |

### Appendices

| Appendix | Title | Description |
|----------|-------|-------------|
| **A** | [Regulatory & Legal Considerations](./appendix-a-regulatory.md) | SR 11-7, EU AI Act, accountability models |
| **D** | [Failure Scenarios & Leading Indicators](./appendix-d-failures.md) | Failure modes, detection, response |

---

## Key Messages

### For Banks

> "Deploy AI agents with confidence: bank-grade controls, cloud portability, regulator-ready—without building the platform yourself."

### For Regulators

> "Clear accountability, decision traceability, human oversight, and documented evidence for every agent decision."

### For Zeta Leadership

> "Platform ownership creates defensibility. We own agent semantics; CSPs provide infrastructure."

---

## The Platform Stance

| Principle | Statement |
|-----------|-----------|
| **Agent Ownership** | Zeta owns agent semantics—identity, authority, memory, lifecycle |
| **Substrate Neutrality** | CSPs are interchangeable execution layers; no CSP owns the control plane |
| **State Portability** | All persistent state is portable across regions and clouds |
| **Failure-First Design** | Resilience is designed, not assumed |
| **Products First** | Agents are products with SLAs, not experiments |

---

## Reading Guide

### For Executives (30 min)

1. [Section 1: Executive Summary](./01-executive-summary.md)
2. [Section 6: Solution Principles](./06-solution-principles.md)
3. [Section 10: GTM Implications](./10-gtm-implications.md)

### For Architects (2-3 hours)

1. All core sections (1-11)
2. [Appendix D: Failure Scenarios](./appendix-d-failures.md)

### For Compliance/Legal (1-2 hours)

1. [Section 3: System Requirements](./03-system-requirements.md) (Sections 3.2, 3.4)
2. [Section 5: CSP Gaps](./05-csp-gaps.md) (Section 5.2, 5.4)
3. [Appendix A: Regulatory Considerations](./appendix-a-regulatory.md)

### For Product Managers (1-2 hours)

1. [Section 2: Problem Statement](./02-problem-statement.md)
2. [Section 10: GTM Implications](./10-gtm-implications.md)
3. [Section 11: Non-Goals](./11-non-goals.md)

---

## Key References

### Regulatory

- [OCC SR 11-7: Model Risk Management](https://www.occ.gov/news-issuances/bulletins/2011/bulletin-2011-12.html)
- [OCC Bulletin 2023-37: Third-Party Risk Management](https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-37.html)
- [Fed SR 21-3: Third-Party Guidance](https://www.federalreserve.gov/supervisionreg/srletters/sr2103.htm)
- [EU AI Act](https://artificialintelligenceact.eu/)
- [DORA: Digital Operational Resilience Act](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en)
- [CFPB AI and Credit Guidance](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/)

### CSP Documentation

- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [AWS Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [Azure AI Agent Service](https://azure.microsoft.com/en-us/products/ai-services/ai-agent-service/)
- [Google Vertex AI](https://cloud.google.com/vertex-ai)
- [Google Agent Builder](https://cloud.google.com/products/agent-builder)

### Open Standards

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [OpenTelemetry](https://opentelemetry.io/)

---

## Document Information

| Property | Value |
|----------|-------|
| **Version** | 1.0.0 |
| **Date** | January 2026 |
| **Status** | Draft for Review |
| **Owner** | Zeta Platform Team |
| **Classification** | Internal / Confidential |

---

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-02 | Initial release |

---

*This document represents Zeta's strategic guidance for building a bank-grade, cloud-portable AI agent platform. It should be reviewed and updated as the technology landscape evolves.*

