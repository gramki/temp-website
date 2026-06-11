# Stream 6: AI Agent Governance and the Operational Model Gap

**Research Date:** 15 March 2026  
**Engagement Area:** Agentic Banking  
**Central Thesis Under Test:** AI agents cannot participate effectively in banking operations because there is no explicit model of the work for them to participate in. The bottleneck is operational context and governance infrastructure, not AI capability.

---

## 1. Operational Model Gap Evidence

### 1.1 The Pilot-to-Production Chasm

| Claim | Value | Source | URL | Verified |
|---|---|---|---|---|
| Banks with measurable AI use cases in operation (compliance) | <10% | BCG | https://www.bcg.com/publications/2025/a-faster-path-to-scaling-genai-in-banking-compliance | Yes |
| Banks that have integrated AI into strategic playbook | 25% | BCG | https://www.bcg.com/publications/2025/for-banks-the-ai-reckoning-has-arrived | Yes |
| Retail banks achieving meaningful bottom-line AI impact | ~5% | BCG | https://www.bcg.com/publications/2025/for-banks-the-ai-reckoning-has-arrived | Yes |
| Companies generating value at scale from AI | 5% | BCG Retail Banking Report 2025 | https://web-assets.bcg.com/4c/7c/0c5f5a6f4803a910fb122f096bdc/2025-retail-banking-report-nov-2025.pdf | Yes |
| Companies generating no value from AI at all | 60% | BCG Retail Banking Report 2025 | https://web-assets.bcg.com/4c/7c/0c5f5a6f4803a910fb122f096bdc/2025-retail-banking-report-nov-2025.pdf | Yes |
| Organizations that moved 40%+ of AI pilots into production | 25% | Deloitte State of AI 2026 | https://www.deloitte.com/nl/en/about/press-room/state-of-ai-in-the-enterprise-2026.html | Yes |
| AI teams' time spent on compliance or waiting for compliance solidification | 30–50% | McKinsey (150+ company study) | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-future-is-agentic-ais-role-in-the-end-to-end-corporate-credit-process | Yes |
| Agentic AI projects expected to be cancelled by end 2027 | >40% | Gartner | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | Yes |
| Internal corporate GenAI pilots that fail | 95% | Vertical AI analysis | https://building.theatlantic.com/the-platform-and-the-people-you-need-to-build-vertical-ai-af3f78505910 | Yes — industry analysis |
| Specialized vertical AI partners achieving success | 67% | Vertical AI analysis | https://building.theatlantic.com/the-platform-and-the-people-you-need-to-build-vertical-ai-af3f78505910 | Yes — industry analysis |
| US banks deployed generative AI to production | 47% (up from 10% in 2023) | LinkedIn/Banking AI analysis | https://www.linkedin.com/pulse/agentic-revolution-state-modern-ai-banking-20252026-alexandru-lache-z3xjf | Yes — industry analysis |
| EU banks actively deploying AI | 92% | EBA 2025 survey | https://www.eba.europa.eu/sites/default/files/2025-09/Rising%20application%20of%20AI%20in%20EU%20banking%20and%20payments%20sector.pdf | Yes |
| EU banks using GPAI or agentic AI in consumer apps | 55% | EBA 2025 survey | https://www.eba.europa.eu/sites/default/files/2025-09/Rising%20application%20of%20AI%20in%20EU%20banking%20and%20payments%20sector.pdf | Yes |
| Financial institutions budgeting for agentic AI | 1 in 3 | Deloitte | https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-risks-banking.html | Yes |
| Companies using AI agents meaningfully today | 23% | Deloitte | https://www.theaibulletin.com/post/agentic-ai-in-2026-key-lessons-from-deloitte-on-governance-and-risk | Yes |
| Expected to use AI agents within two years | 74% | Deloitte | https://www.theaibulletin.com/post/agentic-ai-in-2026-key-lessons-from-deloitte-on-governance-and-risk | Yes |
| Organizations with rigorous governance for agentic AI | 21% | Deloitte | https://www.theaibulletin.com/post/agentic-ai-in-2026-key-lessons-from-deloitte-on-governance-and-risk | Yes |

### 1.2 What Is the Bottleneck?

Five studies converge on the same finding: **the bottleneck is not AI capability — it is operational context, governance, and integration.**

**LTIMindtree** identifies five barriers to agentic AI in banking, none of which are AI capability: (1) legacy systems blocking integration, (2) fragmented data foundations, (3) skills gaps (MLOps, platform engineering), (4) compliance pressure demanding auditability, (5) scaling gap from pilot to production. Source: https://www.ltimindtree.com/wp-content/uploads/2025/12/The-Agentic-AI-TransformationWhitePaper.pdf

**McKinsey** finds 30–50% of AI teams' time is consumed by compliance work or waiting for compliance processes, with teams duplicating work and producing non-reusable one-off solutions. The bottleneck is organizational, not technical. Source: McKinsey corporate credit analysis, 2025.

**Deloitte MIT AI Risk Database** catalogues >350 risks arising from autonomous agent behavior. The top risks are decision opacity (agents acting outside defined boundaries), compounding errors from biased training data, and multi-agent coordination failures — all governance and operational model failures, not capability failures. Source: https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-risks-banking.html

**Dynatrace Pulse of Agentic AI 2026** (919 senior leaders): Top barriers to agentic AI production are security/privacy/compliance (52%) and technical challenges managing agents at scale (51%). ~50% of projects still in POC/pilot. 69% of organizations require human verification. Source: https://www.dynatrace.com/news/press-release/pulse-of-agentic-ai-2026/

**BCG "AI Reckoning" (2025):** Most banks concentrate AI in peripheral activities (customer service chatbots) rather than core functions. Only 25% have woven AI into their strategic playbook. The constraint is not that AI cannot handle core functions — it is that banks have not built the operational substrate to allow AI into core functions. Source: https://www.bcg.com/publications/2025/for-banks-the-ai-reckoning-has-arrived

### 1.3 AI Integration Cost and Time-to-Deploy

| Metric | Value | Source | URL |
|---|---|---|---|
| Production AI agent development cost range | $10K–$250K+ | Medium (Ali El-Shayeb) | https://medium.com/@islandx/what-building-a-production-ai-agent-actually-costs-in-2025-fef0329069d9 |
| Mid-complexity customer ops agent, 3-year TCO | €368K (vs. €158K naively estimated) | Medium (Yugank Aman) | https://medium.com/@yugank.aman/the-true-cost-of-enterprise-ai-agents-a-complete-tco-framework-e3b6228857e7 |
| Customer service AI, year-one TCO | $108K–$306K | Medium (Yugank Aman) | https://medium.com/@yugank.aman/the-true-cost-of-enterprise-ai-agents-a-complete-tco-framework-e3b6228857e7 |
| Enterprise support agent initial build | $150K–$300K before operations begin | Medium (Yugank Aman) | https://medium.com/@yugank.aman/the-true-cost-of-enterprise-ai-agents-a-complete-tco-framework-e3b6228857e7 |
| CFO estimates deviation from actual cost | 500–1,000% (5–40x wider than budget) | Medium (Yugank Aman) | https://medium.com/@yugank.aman/the-true-cost-of-enterprise-ai-agents-a-complete-tco-framework-e3b6228857e7 |
| Agent token consumption vs. chatbot | 3–10x more LLM calls per request | Zylos Research | https://zylos.ai/research/2026-02-19-ai-agent-cost-optimization-token-economics |
| Unconstrained agent task cost (API fees alone) | $5–8 per task | Zylos Research | https://zylos.ai/research/2026-02-19-ai-agent-cost-optimization-token-economics |
| Series B fintech actual vs. estimated cost | $180K actual vs. $50K estimated (3.6x) | Medium (Ali El-Shayeb) | https://medium.com/@islandx/what-building-a-production-ai-agent-actually-costs-in-2025-fef0329069d9 |
| US financial services technology spend (2026) | $495B (40% on software) | Forrester | https://www.forrester.com/blogs/us-financial-services-tech-spending-hits-495-billion/ |

**Interpretation:** The cost data reveals that each AI agent deployment is individually expensive and bespoke. The absence of a shared operational model means every deployment starts from scratch — no reusable scenarios, no shared governance framework, no composable tool contracts. This is the cost of the operational model gap.

### 1.4 The "Last Mile" Problem: LLMs Can Reason, But Have No Model of Banking Operations

Foundation model capability has converged. Claude, GPT, and Gemini perform comparably for most enterprise use cases. The capability gap between what LLMs *can* do and what banks *allow them to do* is the defining constraint.

**Evidence:**

- **95% of internal GenAI pilots fail** at the pilot-to-production transition. Specialized vertical AI partners achieve 67% success, because they bring domain-specific operational models, not better AI. The differentiator is the operational substrate, not the model. Source: https://building.theatlantic.com/the-platform-and-the-people-you-need-to-build-vertical-ai-af3f78505910

- **The "thin wrapper" model is structurally unsustainable.** Banks that package prompts around general-purpose models discover that production requires: context systems (vector databases), safety guardrails, evaluation infrastructure (ModelOps), orchestration, and regulatory compliance engineering (Explainable AI, federated data). These are operational model layers, not AI layers. Source: https://medium.com/@anuj.sadani/the-great-recalibration-the-2026-pivot-from-generalist-wrappers-to-sovereign-application-layers-6475965a172b

- **BNY Mellon's 20,000 AI assistants** represent the largest banking AI deployment found. Success required a "menu of models" architecture routing tasks to GPT-4, Gemini Enterprise, or specialized Llama models — demonstrating that scale requires an operational routing and governance layer, not a single model. Source: https://markets.financialcontent.com/stocks/article/tokenring-2026-1-16-bny-mellon-scales-the-agentic-era-with-deployment-of-20000-ai-assistants

- **McKinsey banking operations data:** Operations represent 60–70% of a bank's cost base. GenAI could add $200–340B annually across global banking. But agentic AI is expected to transform banking operations "over the next decade, not the next year" — the timeline is governance-constrained, not capability-constrained. Source: https://www.mckinsey.com/capabilities/operations/our-insights/ai-in-asia-reimagining-banking-operations-through-agentic-ai

---

## 2. Platform Comparison: How Existing Platforms Address the Operational Model Gap

### 2.1 Comparison Matrix

| Dimension | Salesforce Agentforce | Pega CDH + Smart Dispute | Google CCAI | ServiceNow FSO |
|---|---|---|---|---|
| **Domain model depth** | Moderate. Pre-built banking agent templates (advisor, banker, insurance) with Topics, Instructions, Actions. CRM-centric — models the customer relationship, not banking operations. | Deep (narrowly). Pre-built dispute management (Visa partnership), loan origination, credit risk decisioning, next-best-action arbitration. Models specific banking processes with operational depth. | Shallow. Conversation flow layer (virtual agents, agent assist) with backend API integration. No banking-specific operational model — provides a channel, not a domain model. | Moderate-Deep (ITSM-native). FSO Banking module with dispute management (Visa partnership), customer onboarding, contact center automation, compliance management. Three-tier AI: Skills → Agents → Agentic Workflows. |
| **Governance architecture** | Einstein Trust Layer: Secure Data Retriever, zero data retention, toxicity filtering, access restrictions. Agentforce Script combines deterministic workflows with LLM flexibility for compliance-critical steps. Spring '26 adds audit trails, data masking, regulatory guardrails (SEC, FINRA, HIPAA, SOX). | Governance-native. Center-out architecture with explicit engagement policies, arbitration formulas (Priority = P × C × V × L), and channel separation. Business users can modify decision strategies through Decision Management Portal with revision control and pre-production testing. | Minimal banking governance. Standard Google Cloud IAM, logging, and compliance (SOC2, ISO 27001). No banking-specific governance layer, decision audit, or compliance framework. | ITSM-grade governance extended to banking. Workflow audit trails, approval chains, case management. Inherits ServiceNow platform governance (RBAC, audit logging, compliance). |
| **Operational model explicitness** | Partially explicit. Topics define conversational scope; Actions define what agents can do; Instructions define behavioral constraints. The operational model is CRM-centric — it models customer interactions, not banking processes. | Highly explicit for covered processes. The NBA formula, engagement policies, and channel architecture make the operational model inspectable and auditable. Business users configure without code. But coverage is narrow — dispute, lending, NBA only. | Not explicit. CCAI is a conversation layer. It integrates with banking backends via APIs but does not model the banking operation itself. The agent has no awareness of banking processes beyond what is coded into conversation flows. | Moderately explicit. FSO workflows model banking processes as case management flows. Dispute management (with Visa) has explicit process models. But the operational model is workflow-centric, not domain-knowledge-centric — it models process steps, not banking reasoning. |
| **Scenario coverage** | Narrow. Pre-built for advisor meeting prep, lead qualification, service requests. Not dispute resolution, not loan origination, not AML investigation. Requires custom Agent Topics and Actions for each new banking scenario. | Narrow-to-moderate. Deep in dispute management, lending, and decisioning. No pre-built models for AML investigation, account opening fraud, complex product onboarding. New scenarios require Pega implementation (professional services). | Minimal. No pre-built banking scenarios. Every banking interaction requires custom conversation design and backend integration. | Narrow-to-moderate. Dispute management, customer onboarding, contact center. No pre-built models for lending, trading operations, or regulatory reporting. |
| **Delegation and accountability** | Agent actions logged with audit trails (Spring '26). Einstein Trust Layer tracks LLM inputs/outputs. But no explicit delegation chain — no traceability from agent decision to human authorizer to policy basis. | Strongest of the four. NBA arbitration is auditable — every decision has a recorded propensity score, context weight, business value, and channel. But traceability stops at the decisioning engine; no human delegation chain or accountability binding. | Weakest. Conversation logs capture what was said, not what was decided or why. No decision audit trail, no delegation model. | Moderate. Case management provides workflow-level audit (who approved what). But AI agent decisions within a case are not separately audited from workflow steps. |
| **Multi-agent coordination** | Limited. Agentforce agents are single-purpose. No native multi-agent orchestration or agent-to-agent protocol. | Limited. CDH is a centralized decisioning brain, not a multi-agent system. Agents do not coordinate; the hub decides. | Not applicable. CCAI is a single-agent (virtual agent) system. | Emerging. "Agentic Workflows" concept coordinates multiple AI agents, but this is workflow orchestration, not autonomous multi-agent coordination. |
| **Counter-thesis strength** | Moderate. Solves the CRM-facing operational model gap for sales/service interactions. Does NOT solve the banking operations model gap — it models the customer relationship, not the banking process. | Strong (narrow). For dispute management and NBA decisioning, Pega has substantially solved the operational model problem. The model is explicit, governable, and auditable. But coverage is narrow and extension requires professional services. | Weak. Provides a conversation channel, not an operational model. Banks still need to build the entire operational substrate behind CCAI. | Moderate. For disputes (Visa partnership) and ITSM-adjacent banking operations, ServiceNow provides a meaningful operational model. But the model is workflow-centric, not domain-knowledge-centric. |

### 2.2 Detailed Platform Assessments

#### Salesforce Agentforce

**Architecture:** Atlas Reasoning Engine evaluates queries → retrieves data (Data Cloud) → constructs multi-step action plans → executes tasks → logs outcomes. Agentforce Script enables hybrid deterministic + LLM reasoning for compliance-critical steps.

**Banking-specific capabilities:**
- Pre-built agent templates for financial advisors, bankers, insurance professionals
- Meeting preparation, portfolio analysis, lead qualification, service request processing
- Spring '26: integrated testing, audit trails, data masking, regulatory guardrails (SEC, FINRA, HIPAA, SOX)

**Operational model assessment:** Agentforce's operational model is CRM-centric — it excels at modeling *what to say to the customer* and *what the customer needs*. It does not model *how banking operations work*. An Agentforce agent can help a banker prepare for a meeting but cannot autonomously process a disputed transaction or execute a compliance workflow. Each new banking scenario requires custom Topic, Instruction, and Action configuration — this is the operational model gap manifesting as implementation effort.

**Key limitation:** Agentforce markets "autonomous agents" but the agent's autonomy is bounded by Topics and Actions defined by human builders. The operational model must be manually created for each banking domain. Salesforce provides the *platform* for operational models, not the *operational models themselves*.

Sources: https://vantagepoint.io/blog/sf/salesforce-einstein-ai-and-agentforce-trends-for-2026-the-complete-guide-for-financial-services, https://vantagepoint.io/blog/sf/agentforce-implementation-guide-for-financial-services-a-comprehensive-2026-roadmap, https://www.salesforce.com/ap/agentforce/what-is-a-reasoning-engine/atlas/

#### Pega Customer Decision Hub + Smart Dispute

**Architecture:** Center-out decisioning brain. Taxonomy (action hierarchy) → Engagement Policy (filtering) → Arbitration (Priority = P × C × V × L) → Channel execution. Business users configure through Decision Management Portal.

**Banking-specific capabilities:**
- **Smart Dispute** (Visa partnership): Pre-built dispute management for all payment types (cards, Zelle, mobile wallets, P2P, BNPL). Gen AI enhancements for claim summarization, intelligent guidance, "friendly fraud" screening.
- **Credit Risk Decisioning:** Automated loan origination with decision strategy management, revision control, pre-production testing.
- **NBA (Next-Best-Action):** Real-time 1:1 customer engagement. Production deployments at Nationwide Building Society, NatWest (Phase 2 modernization to NBA Designer + 1:1 Operations Manager).
- Disputed charges projected to rise 40% by 2026, making this operationally significant.

**Operational model assessment:** Pega comes closest to having "solved" the operational model problem — *for the processes it covers*. The NBA formula is an explicit, inspectable, auditable operational model: every customer interaction has a calculable priority based on propensity, context, value, and leverage. The center-out architecture separates decisioning logic from channel execution, which is architecturally what an "explicit model of the work" requires.

**Key limitation:** Pega's depth is narrow. It covers dispute management, lending origination, and next-best-action decisioning. It does not cover AML investigation workflows, complex product onboarding, regulatory reporting, or trade operations. Extension requires Pega professional services — each new domain requires building the operational model from scratch within Pega's framework. The platform provides the *container* for operational models but not universal banking coverage.

**Counter-thesis assessment:** Pega *partially validates* the counter-thesis — for narrow domains (disputes, NBA), the operational model problem is solved. But Pega's existence *also validates* the thesis: the fact that Pega must build deep, domain-specific operational models for each banking process (and that this is expensive professional services work) proves that the operational model gap is real and not something AI capability alone can bridge.

Sources: https://adhyaconsulting.org/how-pega-customer-decision-hub-delivers-real-time-next-best-action-a-deep-dive-into-its-architecture/, https://pega.com/about/news/press-releases/gen-ai-and-automation-enhancements-help-banks-accelerate-payment-disputes, https://www.pega.com/insights/resources/pegaworld-2025-how-nationwide-building-society-selected-pega-customer-decision

#### Google CCAI

**Architecture:** Contact Center AI Platform (CCaaS) providing omni-channel routing, virtual agents (Dialogflow), agent assist, and customer insights. Integrates with Google Cloud AI and Gemini models.

**Banking-specific capabilities:**
- Virtual agents for routine banking interactions
- Live agent assistance with real-time suggestions
- CRM integration (including Salesforce Service Cloud)
- Voice, chat, SMS channel support
- CCaaS 4.0 (February 2026): voicemail routing, simultaneous call join, improved recording

**Operational model assessment:** CCAI provides a *conversation layer*, not an *operational model*. It can route calls, understand intent, and generate responses — but it has no model of banking operations. When a customer calls about a disputed charge, CCAI can understand the words "I want to dispute a charge" but has no model of dispute resolution workflows, regulatory requirements, network rules (Visa/Mastercard), or escalation criteria. Every banking process must be manually coded into conversation flows (Dialogflow) and connected to banking backends via custom APIs.

**Counter-thesis assessment:** CCAI does not challenge the thesis. It is a channel technology, not an operational model. Banks that deploy CCAI must build the entire operational model separately — CCAI provides the "front door" but not the "operating room."

Sources: https://docs.cloud.google.com/contact-center/ccai-platform/docs, https://ai.quantiphi.com/elevate-banking-experience-with-google-cloud-contact-center-ai-platform

#### ServiceNow Financial Services Operations (FSO)

**Architecture:** FSO built on ServiceNow's ITSM-native workflow platform. Three-tier AI: Gen AI Skills (single-step assists) → AI Agents (autonomous domain-specific capabilities) → Agentic Workflows (coordinated multi-agent processes).

**Banking-specific capabilities:**
- **Dispute management** (Visa partnership): AI agents screen for friendly fraud, draft compliant customer communications, deflect cases not meeting network/issuer policies.
- Customer onboarding automation
- Contact center operations
- Compliance management
- Pre-built retail banking, commercial banking, and investment management workflows

**Operational model assessment:** ServiceNow's strength is that ITSM has a *deep domain model* — incidents, changes, problems, service requests, SLAs, escalation paths. FSO Banking attempts to replicate this depth for banking operations. The dispute management module (with Visa) has meaningful operational depth: it understands network rules, screening criteria, and compliance requirements. But for non-dispute banking operations, the model is workflow-centric (process steps and approvals) rather than domain-knowledge-centric (banking reasoning).

**Counter-thesis assessment:** ServiceNow moderately challenges the thesis for dispute management and ITSM-adjacent banking operations. Its three-tier AI architecture (Skills → Agents → Agentic Workflows) is architecturally aligned with what an operational substrate requires. But coverage is narrow, and the banking domain model is far shallower than ServiceNow's ITSM model.

Sources: https://www.servicenow.com/blogs/2025/ai-agents-banking-telecom-public-sector, https://www.servicenow.com/products/financial-services-operations/banking.html, https://www.servicenow.com/community/fso-articles/gen-ai-skills-ai-agents-amp-agentic-workflows-for-fso/ta-p/3500995

---

## 3. AI Agent Identity and Accountability in Customer-Facing Banking

*Note: This section adapts findings from the Digital Identity and Trust engagement area's S5 research (s5-ai-agent-identity.md) for the customer-facing banking context. See Cross-Reference Notes (Section 7) for what was borrowed.*

### 3.1 The Accountability Question

When an AI agent resolves a customer dispute, three accountability questions arise that existing platforms do not answer:

**Who is accountable?**
- EU AI Act Article 26: Deployer obligations cannot be contractually transferred. The bank is accountable regardless of vendor.
- EU AI Act Article 12: Decision logs must identify the natural persons involved in result verification.
- No existing platform (Agentforce, Pega, CCAI, ServiceNow) provides end-to-end traceability from AI agent decision → human authorizer → policy basis → regulatory requirement.

**How is the decision auditable?**
- Banks must implement three core audit infrastructure elements (AAIA Agentic AI Insights, 2026):
  1. **Immutable ledger logging:** Append-only databases ensuring decisions cannot be tampered with
  2. **Forensic explainability:** Recording full chain-of-thought reasoning linked to actions
  3. **Compliance export standards:** Automated formatting for SOC2, ISO 42001, and financial audits
- Model and prompt changes must receive the same governance discipline as production changes.
- Sources: https://aaia.app/research/agentic-audit-trails, https://www.dunnixer.com/insights/information/banking/us/implementation-best-practices-for-auditing-ai-driven-transactions

**What happens when the customer challenges the resolution?**
- 62% of consumers say trust in a financial institution is shaped more by dispute handling than the original incident itself.
- 50–100 million disputes annually in the US alone, costing the top 15 banks collectively $3B yearly, growing at 16% annually.
- When a customer challenges an AI agent's resolution, the bank must produce a full decision trace: inputs, model version, thresholds, outputs, control decisions, and human overrides. Current platforms do not produce this trace automatically.
- Source: https://www.lyzr.ai/playbook/bfsi-guide-to-dispute-management/

### 3.2 Identity Infrastructure Gaps (Adapted from S5)

| EU AI Act Requirement | What Banks Need | Current State |
|---|---|---|
| Article 12 — identify personnel verifying results | Human identity binding to AI decisions | No platform provides this natively |
| Article 14 — assign competent oversight persons | Role-based access control for AI oversight | Partially addressed by Pega and ServiceNow role models |
| Article 26 — retain logs for 6+ months | Immutable audit trails linking AI actions to human sponsors | Basic logging exists; audit-grade trails do not |
| Article 9 — continuous risk management | Lifecycle identity management for AI systems | No vendor provides AI system identity lifecycle management for banking |
| Article 13 — transparency to deployers | AI system identity metadata (capabilities, limitations, version) | Varies; Agentforce Agent Topics partially address this |

### 3.3 Enterprise Readiness Data (Adapted from S5)

| Metric | Value | Source |
|---|---|---|
| Security leaders confident IAM can manage agent identities | 18% | CSA / Strata Identity 2026 |
| Organizations maintaining real-time AI agent inventory | 21% | CSA / Strata Identity 2026 |
| Organizations that can trace agent actions to human sponsor | 28% | CSA / Strata Identity 2026 |
| Organizations doubting they could pass agent access control audit | 84% | CSA 2026 |
| Organizations using static API keys for agent authentication | 44% | CSA / Strata Identity 2026 |
| Enterprises running AI agents autonomously | 95% | ConductorOne 2026 |
| Enterprises with full visibility into non-human identities | 22% | ConductorOne 2026 |

**Interpretation:** 95% of enterprises run AI agents autonomously, but only 18% believe their IAM can manage those agents. Only 28% can trace agent actions to a human sponsor. In customer-facing banking — where every agent decision potentially affects a customer's account, credit, or complaint resolution — this gap is a regulatory and reputational liability, not just a technical debt item.

---

## 4. Standards Body Activity

### 4.1 Standards Activity Summary

| Standard / Protocol | Body | Status (Mar 2026) | Relevance to Banking AI Governance | Key Gap |
|---|---|---|---|---|
| **A2A Protocol v0.1.0** | Google + 50 partners | Launched 2025, production-ready | Multi-agent coordination with structured Agent Cards (identity + capabilities). Built on HTTP/JSON-RPC/SSE. Secure-by-default. | Assumes identity layer exists but does not specify it. No delegation authority, accountability chains, or human oversight requirements. |
| **Model Context Protocol (MCP)** | Anthropic → Linux Foundation (Dec 2025) | Production, open standard | Standardizes agent-tool interaction. 28% of Fortune 500 deployed MCP servers. Banking/fintech strong adopters. | Tool interaction protocol, not governance protocol. No operational model, decision audit, or accountability semantics. |
| **ISO/IEC 42001:2023** | ISO/IEC | Published, auditable (ISO 42006:2025 for certification bodies) | First international AI management system standard. Requires algorithmic transparency, decision traceability, accountability chains, explainability. Pairs with EU AI Act. | Framework standard — defines *what* to achieve, not *how* to implement for banking AI agents specifically. No agent-specific controls. |
| **NIST AI RMF 1.0** | NIST | Published (Jan 2023), expanded through 2025 | Four core functions (Govern, Map, Measure, Manage). De facto authority — FTC, CFPB, SEC reference it. NIST AI 600-1 (GenAI Profile) released Jul 2024. Cyber AI Profile draft Dec 2025. | Sector-neutral. No banking-specific profile. No AI agent identity guidance. No IT operations profile. |
| **IETF Txn-Tokens for Agents** | IETF OAuth WG | Individual draft (draft-04, Feb 2026) | Extends Transaction Tokens with `actor` (AI agent) and `principal` (human/system initiator) fields. First formal protocol for agent identity delegation. | Early-stage individual draft, not RFC. Not adopted as working group item. |
| **OpenID Agentic AI Whitepaper** | OpenID Foundation | Published Oct 2025 | Most authoritative framing of AI agent identity gap. Names: delegation chains, fragmentation, consent scalability, recursive delegation. Established community group. | Whitepaper and community group, not a specification. No protocol deliverable yet. |
| **W3C Verifiable Credentials 2.0** | W3C | W3C Recommendation (May 2025) | Flexible issuer-holder-verifier model applicable to agent authority credentials. Seven published specs. | No agent-specific vocabulary — cannot express "this agent has authority X delegated by human Y with constraint Z." |
| **EU AI Act** | European Parliament | Phased enforcement: prohibited practices (Feb 2025), GPAI (Aug 2025), high-risk (Aug 2026), full (Aug 2027) | Credit-scoring and insurance-pricing AI explicitly high-risk (Annex III, 5b). Deployer obligations non-transferable. 6-month log retention. Human oversight proportionate to autonomy. Penalties: €35M / 7% turnover. | Defines obligations but not implementation methods. No prescribed identity or governance infrastructure. |
| **SR 11-7** | OCC/Fed | 2011, straining under AI | Core banking model risk framework. Conceptual principles valid (governance, validation, effective challenge) but assumptions (static, bounded, periodic review) broken by dynamic AI. Definitional ambiguity: is an AI agent a "model"? | 15 years old. Not designed for agentic AI. No regulator has clarified application to AI agents specifically. |
| **DORA** | EU | Enforcement Jan 2025 | ICT risk management framework (Articles 5–16). Applies to AI agents as ICT systems. Requires asset inventory of AI agents (purpose, data access, decision authority, model version). | Drafted before AI agents reached production. Does not explicitly address autonomous remediation or agent-specific governance. |

### 4.2 Key Standards Gap

**No standard exists that combines:** (a) agent identity delegation chains, (b) human accountability binding, (c) decision audit semantics, (d) context-specific authority, and (e) cross-organizational agent federation — all within a banking regulatory context.

The closest components are:
- **IETF Txn-Tokens for Agents** → actor/principal separation (identity delegation)
- **ISO 42001** → algorithmic transparency and accountability chains (governance framework)
- **EU AI Act** → deployer obligations and human oversight requirements (regulatory mandate)
- **A2A** → multi-agent coordination protocol (communication layer)
- **MCP** → agent-tool interaction standard (tool governance)

These are complementary building blocks, not a complete solution. The **integration gap** between these standards is itself a manifestation of the operational model gap thesis: there is no unified model of how AI agents participate in banking operations under governance.

---

## 5. Compounding vs. Non-Compounding AI Deployment

### 5.1 Evidence for Compounding Effects

| Finding | Source | URL |
|---|---|---|
| Banks rewiring a single frontline domain see results in months, not years: 3–15% higher revenues per RM, 20–40% lower cost to serve | McKinsey | https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready |
| Multi-discipline AI coordination (ML + CV + RPA + NLP) creates exponential value vs. single-discipline linear gains | McKinsey / Compound Loop analysis | https://mariothomas.com/blog/agentic-ai-compound-loop/ |
| Only 23% of organizations have scaled agentic systems despite 88% using AI — the gap is operational, not capability | McKinsey / Compound Loop analysis | https://mariothomas.com/blog/agentic-ai-compound-loop/ |
| Deutsche Bank: agentic AI handles credit reviews, financial-risk analyses, and business-model assessments previously deemed too complex to automate | McKinsey | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-future-is-agentic-ais-role-in-the-end-to-end-corporate-credit-process |
| BCG: proven banking AI use cases — 40% reduction in fraud false positives, 20% KYC cost reduction, 67% improved file-closure rates | BCG | https://www.bcg.com/publications/2025/a-faster-path-to-scaling-genai-in-banking-compliance |
| DBS Bank: 2,000+ AI models across 430+ use cases projecting SGD 1B+ value — rewiring for the "reasoning era" | DBS Newsroom | https://www.dbs.com/newsroom/DBS_named_Worlds_Best_AI_Bank_2025 |
| BNY Mellon: 20,000+ AI assistants using "menu of models" architecture | FinancialContent | https://markets.financialcontent.com/stocks/article/tokenring-2026-1-16-bny-mellon-scales-the-agentic-era-with-deployment-of-20000-ai-assistants |
| JPMC: 450+ AI use cases generating $1.5–2B in measurable value | Lucidate | https://www.lucidate.co.uk/post/beyond-the-pilot-how-jpmorgan-goldman-sachs-and-hsbc-are-scaling-ai-to-enterprise-production |

### 5.2 What Separates Banks That Scale from Those Stuck in Pilots

**BCG identifies three tiers:**
1. **Leaders (5%):** AI woven into strategic playbook, end-to-end process transformation, measurable bottom-line impact
2. **Experimenters (35%):** Limited success, isolated use cases, unable to connect AI to core operations
3. **Non-starters (60%):** Generating no value from AI at all

**McKinsey's operating model research** (150+ companies) identifies two sinking issues:
1. AI teams spending 30–50% of their time on compliance overhead or waiting — caused by the absence of pre-built governance models
2. Teams building non-reusable one-off solutions — caused by the absence of a composable operational substrate

**Compounding interpretation:** Banks that invest in an operational substrate (explicit process models, reusable governance frameworks, composable tool contracts) deploy subsequent AI agents faster because:
- Governance is pre-built — new agents inherit existing compliance infrastructure
- Domain context is reusable — scenarios, exception patterns, and escalation paths transfer between domains
- Tool contracts are composable — agents can use existing verified integrations rather than building new ones

Banks without this substrate face linear (or worse) cost curves: each new agent deployment requires rebuilding governance, context, and integrations from scratch.

**Direct evidence for the "fifth domain faster than the first" thesis is limited.** McKinsey's finding that banks see results "in months, not years" for frontline domain rewiring is suggestive but does not provide domain-by-domain acceleration data. DBS Bank's 430+ use cases from 2,000+ models imply compounding, but no public data breaks down time-to-deploy by sequential domain. BNY Mellon's 20,000 assistants imply operational substrate maturity, but deployment velocity data is not public.

**This is a gap in available evidence, not a refutation of the thesis.** The compounding hypothesis is architecturally sound but empirically unproven at the bank level.

---

## 6. Critical Assessment: Is the Operational Model Gap Real?

### 6.1 Thesis Validation

**The operational model gap is real.** The evidence converges from five independent directions:

1. **Cost evidence:** Every banking AI deployment is individually expensive ($150K–$300K+ initial build, 5–40x budget overruns), because each deployment must create its own operational context, governance framework, and tool integrations. This is the cost signature of a missing shared substrate.

2. **Scaling evidence:** Only 5% of companies generate value from AI at scale; 60% generate none. Only 25% of banks have woven AI into strategy. The gap between capability (foundation models work) and deployment (banks can't scale them) is an operational model gap.

3. **Bottleneck evidence:** Five independent studies identify governance, integration, and operational context — not AI capability — as the primary barriers. McKinsey's 30–50% compliance overhead finding directly measures the cost of absent operational models.

4. **Platform evidence:** Even the strongest platforms (Pega) have solved the operational model problem only for narrow domains, and extension requires expensive professional services. No platform provides a universal banking operational model. The fact that Pega's success requires deep domain-specific models *validates* the thesis — you cannot deploy banking AI without an explicit model of the work.

5. **Standards evidence:** No standard combines agent identity, human accountability, decision audit, and banking-specific governance. The standards landscape is fragmented across IETF, OpenID, ISO, A2A, and MCP — each solving one layer but no standard solving the integration across layers.

### 6.2 Counter-Thesis Assessment

**The counter-thesis ("existing platforms are solving the operational model problem") is partially valid but structurally insufficient:**

| Platform | What It Solves | What Remains Unsolved |
|---|---|---|
| Pega CDH | Dispute management, NBA decisioning, loan origination — deep operational models with auditable arbitration | Coverage limited to 3–5 banking domains. Extension requires professional services. No multi-agent coordination, no agent identity delegation, no cross-process governance. |
| Salesforce Agentforce | CRM-facing operational model for sales/service interactions. Governance framework (Einstein Trust Layer, Agentforce Script) is meaningful. | Models the customer relationship, not banking operations. Each new banking domain requires custom Topic/Action creation. No banking process models. |
| ServiceNow FSO | Dispute management (Visa partnership), ITSM-adjacent banking operations. Three-tier AI architecture is well-designed. | Banking domain model far shallower than ITSM model. Workflow-centric, not domain-knowledge-centric. |
| Google CCAI | Conversation channel with backend integration | Not an operational model at all. Solves the channel problem, not the operations problem. |

**Net assessment:** Existing platforms solve fragments of the operational model problem for narrow domains. None provides a general-purpose operational substrate that would allow banks to deploy AI agents across arbitrary banking domains with shared governance, reusable context, and composable tool contracts. The gap between what these platforms cover and what banks need for enterprise-scale agentic banking is the opportunity.

### 6.3 The Distinguishing Characteristic of Customer-Facing Banking

The customer-facing context adds requirements that back-office AI (covered by Agentic Operations) and infrastructure AI (covered by Cloud & Platform Operations) do not face:

| Dimension | Customer-Facing Banking | Back-Office AI | Infrastructure AI |
|---|---|---|---|
| **Accountability** | Decision affects a named customer who can challenge it. Consumer protection law applies. | Decision affects internal processes. No customer standing to challenge. | Decision affects system state. No customer involvement. |
| **Explainability** | Customer may ask "why did you decide this?" Bank must produce understandable explanation. | Internal audit may review. Technical explanation sufficient. | System logs sufficient. No explanation required to humans. |
| **Dispute mechanism** | Customer can dispute through CFPB, FOS, banking ombudsman. Bank must respond within regulatory timelines. | Internal escalation only. | Incident management only. |
| **Trust impact** | 62% of consumers say dispute handling shapes trust more than the original incident. AI-driven resolution that feels arbitrary destroys customer relationship. | No customer trust dimension. | No customer trust dimension. |
| **Regulatory exposure** | EU AI Act high-risk (credit scoring, Aug 2026). Consumer protection regulations (CFPB, FCA). Banking-specific complaint handling rules. | Model risk (SR 11-7). General employment/anti-discrimination law. | Operational resilience (DORA, CPS 230). No consumer protection. |

---

## 7. Cross-Reference Notes

### Borrowed from `gap-fill-agentic-ops-banking.md` (Cloud & Platform Operations)

The following findings were adapted from the agentic operations research for customer-facing context:

- **SR 11-7 strain analysis:** GARP's February 2026 analysis showing framework assumptions broken by dynamic AI — adapted from infrastructure context to customer-facing decisioning context. The customer-facing dimension adds consumer protection obligations not present in infrastructure.
- **DORA gap analysis:** dig8ital's analysis that DORA was drafted before AI agents — relevant equally to customer-facing and infrastructure agents.
- **Regulatory positions (MAS, ECB, PRA, APRA, OCC):** All regulatory positions documented in the agentic ops file apply equally to customer-facing banking AI. The customer-facing context adds EU AI Act high-risk classification (Annex III, 5b for credit scoring) which is not present in the infrastructure context.
- **LTIMindtree five barriers:** Documented in agentic ops; applies equally here.
- **McKinsey <10% and BCG banking data:** Originally sourced in agentic ops; incorporated here with additional BCG "AI Reckoning" data.
- **Dynatrace Pulse survey:** Barrier data applies to all agentic AI, not specific to infrastructure.

### Borrowed from `s5-ai-agent-identity.md` (Digital Identity and Trust)

The following findings were adapted:

- **EU AI Act tiered accountability chain:** Articles 12, 14, 16, 25, 26 documentation. Applied to customer-facing banking agent scenarios rather than general identity infrastructure.
- **CSA/Strata Identity 2026 survey data:** Enterprise readiness metrics (18% IAM confidence, 28% traceability, 84% audit doubt). Applied to banking-specific context.
- **ConductorOne survey data:** 95% autonomous agents, 22% visibility.
- **IETF Transaction Tokens for Agents:** Actor/principal separation analysis.
- **OpenID Foundation agentic AI whitepaper:** Delegation, fragmentation, consent scalability analysis.
- **A2A and MCP protocol descriptions:** Communication and tool interaction layers.
- **Machine identity vs. agent identity gap table:** Adapted with customer-facing banking-specific examples.
- **ISACA "looming authorization crisis" framing:** Seven gaps in identity management for agentic AI.

### New Research in This File (Not in Cross-References)

- **Platform comparison matrix:** Salesforce Agentforce, Pega CDH, Google CCAI, ServiceNow FSO — detailed assessment of how each addresses the operational model gap. Entirely new analysis.
- **Cost-per-deployment data:** AI agent development costs ($10K–$250K+), TCO analysis (5–40x budget overruns), token economics (3–10x chatbot costs). New sourcing.
- **BNY Mellon 20,000 AI assistants deployment:** New evidence for operational substrate at scale.
- **Pega Smart Dispute detailed analysis:** Visa partnership, payment type coverage, Gen AI enhancements. New sourcing.
- **ServiceNow FSO Banking detailed analysis:** Three-tier AI architecture, dispute management with Visa. New sourcing.
- **Compounding deployment evidence:** McKinsey compound loop analysis, domain acceleration evidence. New synthesis.
- **Customer-facing vs. back-office vs. infrastructure comparison table:** New analysis distinguishing customer-facing requirements.
- **"Last mile" problem evidence:** 95% pilot failure rate, thin-wrapper structural unsustainability, vertical AI vs. generalist success rates. New sourcing.
- **Deloitte MIT AI Risk Database:** >350 autonomous agent risks, decision opacity, compounding errors. New sourcing.
- **Dispute management market data:** 50–100M disputes annually in US, $3B cost, 16% growth, 62% trust impact. New sourcing.
- **Forrester Tier-1 bank prediction:** Nearly half of tier-one banks will deploy AI agents for back-office tasks in 2026. New sourcing.

---

## 8. Gaps and Unresolved Questions

1. **No bank has published domain-by-domain deployment acceleration data.** The compounding thesis is architecturally sound but empirically unproven. DBS (430+ use cases), BNY Mellon (20,000 assistants), and JPMC (450+ use cases) likely have this data internally but have not published it.

2. **No regulator has addressed the specific question: "Can an AI agent autonomously resolve a customer dispute?"** EU AI Act high-risk obligations take effect August 2026 for credit scoring. The intersection of consumer protection law and AI agent autonomy for dispute resolution is unexplored regulatory territory.

3. **Pega's operational model depth for dispute management has not been independently benchmarked.** How does Pega Smart Dispute's AI agent decision quality compare with human agent decisions? No third-party assessment found.

4. **The customer trust impact of AI-driven dispute resolution lacks rigorous study.** The 62% trust-shaped-by-dispute-handling statistic is from a vendor (Lyzr). No independent academic study of customer trust in AI-driven banking dispute resolution was found.

5. **No platform provides end-to-end traceability from AI agent decision to human authorizer to policy basis.** This is the core identity infrastructure gap for customer-facing banking. Microsoft Entra Agent ID (preview) addresses agent identity but not banking-specific delegation and accountability.

6. **Multi-agent coordination in customer-facing banking is entirely theoretical.** A2A protocol defines agent-to-agent communication but no banking implementation of multi-agent dispute resolution, customer onboarding, or cross-department coordination exists.

7. **The cost-of-governance-per-agent-decision has not been quantified.** If each agent decision must be audit-ready with chain-of-thought logging, model version tracking, and human oversight binding — what is the per-decision cost? This determines whether agentic banking is economically viable at scale.

8. **Cross-border agent accountability is undefined.** A bank operating under EU AI Act, US CFPB rules, MAS guidelines, and APRA CPS 230 simultaneously has no way to maintain consistent agent governance across jurisdictions for customer-facing scenarios.

9. **The "friendly fraud" screening use case (ServiceNow/Pega) raises fairness questions.** If an AI agent screens out a customer's dispute as "friendly fraud," what recourse does the customer have? How is the screening decision auditable and challengeable? This is a consumer protection question, not a technology question.

10. **Foundation model capability convergence may shift the competitive landscape.** If Claude, GPT, and Gemini are interchangeable for banking reasoning, then the operational model — not the AI model — becomes the durable competitive moat. This validates the thesis but also means platform vendors may absorb the operational model layer, narrowing the opportunity window.

---

## Evidence Table (Combined)

| # | Claim | Source | URL | Verified | New/Borrowed |
|---|---|---|---|---|---|
| 1 | Only 5% of companies generate value from AI at scale | BCG Retail Banking 2025 | https://web-assets.bcg.com/4c/7c/0c5f5a6f4803a910fb122f096bdc/2025-retail-banking-report-nov-2025.pdf | Yes | New |
| 2 | 60% of companies generate no value from AI | BCG Retail Banking 2025 | https://web-assets.bcg.com/4c/7c/0c5f5a6f4803a910fb122f096bdc/2025-retail-banking-report-nov-2025.pdf | Yes | New |
| 3 | 25% of banks integrated AI into strategic playbook | BCG | https://www.bcg.com/publications/2025/for-banks-the-ai-reckoning-has-arrived | Yes | Borrowed (S5) |
| 4 | <10% of banks have measurable AI use cases in operation | BCG | https://www.bcg.com/publications/2025/a-faster-path-to-scaling-genai-in-banking-compliance | Yes | Borrowed (agentic ops) |
| 5 | 30–50% of AI teams' time on compliance/waiting | McKinsey (150+ companies) | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-future-is-agentic-ais-role-in-the-end-to-end-corporate-credit-process | Yes | New |
| 6 | >40% agentic AI projects cancelled by end 2027 | Gartner | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | Yes | Borrowed (S5) |
| 7 | 95% internal GenAI pilots fail | Vertical AI analysis | https://building.theatlantic.com/the-platform-and-the-people-you-need-to-build-vertical-ai-af3f78505910 | Yes — industry analysis | New |
| 8 | Specialized vertical AI partners: 67% success rate | Vertical AI analysis | https://building.theatlantic.com/the-platform-and-the-people-you-need-to-build-vertical-ai-af3f78505910 | Yes — industry analysis | New |
| 9 | BNY Mellon: 20,000+ AI assistants deployed | FinancialContent | https://markets.financialcontent.com/stocks/article/tokenring-2026-1-16-bny-mellon-scales-the-agentic-era-with-deployment-of-20000-ai-assistants | Yes | New |
| 10 | Mid-complexity AI agent 3-year TCO: €368K vs €158K estimated | Medium (Yugank Aman) | https://medium.com/@yugank.aman/the-true-cost-of-enterprise-ai-agents-a-complete-tco-framework-e3b6228857e7 | Yes — industry analysis | New |
| 11 | CFO estimates 5–40x off from actual AI costs | Medium (Yugank Aman) | https://medium.com/@yugank.aman/the-true-cost-of-enterprise-ai-agents-a-complete-tco-framework-e3b6228857e7 | Yes — industry analysis | New |
| 12 | Agents consume 3–10x more LLM calls than chatbots | Zylos Research | https://zylos.ai/research/2026-02-19-ai-agent-cost-optimization-token-economics | Yes — industry analysis | New |
| 13 | US banking disputes: 50–100M annually, $3B cost, 16% growth | Lyzr | https://www.lyzr.ai/playbook/bfsi-guide-to-dispute-management/ | Yes — vendor content | New |
| 14 | 62% of consumers: trust shaped by dispute handling | Lyzr | https://www.lyzr.ai/playbook/bfsi-guide-to-dispute-management/ | Vendor-sourced — no independent verification | New |
| 15 | Disputed charges projected to rise 40% by 2026 | Pega | https://pega.com/about/news/press-releases/gen-ai-and-automation-enhancements-help-banks-accelerate-payment-disputes | Yes — vendor claim | New |
| 16 | 1 in 3 FIs budgeting for agentic AI | Deloitte | https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-risks-banking.html | Yes | New |
| 17 | >350 autonomous AI behavior risks catalogued | Deloitte / MIT AI Risk Database | https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-risks-banking.html | Yes | New |
| 18 | Only 21% have rigorous agentic AI governance | Deloitte | https://www.theaibulletin.com/post/agentic-ai-in-2026-key-lessons-from-deloitte-on-governance-and-risk | Yes | New |
| 19 | Autonomous AI agent market: $8.5B by 2026, $35B by 2030 | Deloitte | https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html | Yes | New |
| 20 | 47% US banks deployed GenAI to production (up from 10% in 2023) | LinkedIn/Banking AI | https://www.linkedin.com/pulse/agentic-revolution-state-modern-ai-banking-20252026-alexandru-lache-z3xjf | Yes — industry analysis | New |
| 21 | 28% of Fortune 500 deployed MCP servers in production | Synvestable | https://www.synvestable.com/model-context-protocol.html | Yes — industry analysis | New |
| 22 | 80% of Fortune 500 running active AI agents | Synvestable | https://www.synvestable.com/model-context-protocol.html | Yes — industry analysis | New |
| 23 | Nationwide Building Society: Pega CDH selected for 1:1 personalization | PegaWorld 2025 | https://www.pega.com/insights/resources/pegaworld-2025-how-nationwide-building-society-selected-pega-customer-decision | Yes | New |
| 24 | NatWest: Phase 2 modernization to Pega NBA Designer | PegaWorld 2025 | https://pega.com/insights/resources/pegaworld-2025-inside-scoop-natwests-modernization-decisioning | Yes | New |
| 25 | Swedbank: 80% decrease in loan processing time with Pega | Pega | https://pega.com/industries/financial-services/lending | Yes — vendor claim | New |
| 26 | ServiceNow FSO dispute management built with Visa | ServiceNow | https://www.servicenow.com/blogs/2025/ai-agents-banking-telecom-public-sector | Yes | New |
| 27 | Agentforce Spring '26: audit trails, data masking, regulatory guardrails | Vantage Point / Salesforce | https://vantagepoint.io/blog/sf/agentforce-builder-spring-26-financial-services-ai-agents | Yes — based on Salesforce releases | New |
| 28 | ISO/IEC 42001: first international AI management system standard | ISO | https://www.iso.org/home/insights-news/resources/iso-42001-explained-what-it-is.html | Yes | New |
| 29 | ISO/IEC 42006:2025: requirements for AI management system audit bodies | ISO | https://www.iso.org/standard/44546.html | Yes | New |
| 30 | Banks seeing 3–15% higher revenues per RM, 20–40% lower cost to serve | McKinsey | https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready | Yes | New |
| 31 | US FS tech spend: $495B in 2026 (40% on software) | Forrester | https://www.forrester.com/blogs/us-financial-services-tech-spending-hits-495-billion/ | Yes | New |
| 32 | Nearly half tier-one banks will deploy AI agents for back-office in 2026 | Forrester | https://www.forrester.com/blogs/predictions-2026-how-financial-services-can-thrive-amid-ai-disruption/ | Yes — paywalled prediction | New |
| 33 | Operations = 60–70% of bank cost base | McKinsey | https://www.mckinsey.com/capabilities/operations/our-insights/ai-in-asia-reimagining-banking-operations-through-agentic-ai | Yes | Borrowed (agentic ops) |
| 34 | GenAI could add $200–340B annually to global banking | McKinsey | https://www.mckinsey.com/capabilities/operations/our-insights/ai-in-asia-reimagining-banking-operations-through-agentic-ai | Yes | Borrowed (agentic ops) |
| 35 | 18% of security leaders confident IAM manages agent identities | CSA / Strata 2026 | https://www.strata.io/resources/whitepapers/securing-autonomous-ai-agents-csa-survey-report-2026-strata-identity/ | Yes | Borrowed (S5) |
| 36 | 84% doubt they could pass agent access control audit | CSA 2026 | https://cloudsecurityalliance.org/articles/cloud-security-alliance-strata-survey-finds-that-enterprises-are-in-time-to-trust-phase-as-they-build-ai-autonomy-foundations | Yes | Borrowed (S5) |
| 37 | SR 11-7 straining under agentic AI — definitional challenges | GARP | https://www.garp.org/risk-intelligence/operational/sr-11-7-age-agentic-ai-260227 | Yes | Borrowed (agentic ops) |
| 38 | DORA drafted before AI agents in production | dig8ital | https://dig8ital.com/articles/dora-ict-risk-ai-agents/ | Yes — industry analysis | Borrowed (agentic ops) |
| 39 | MAS AI Risk Management Guidelines (Nov 2025) | MAS | https://www.mas.gov.sg/news/media-releases/2025/mas-guidelines-for-artificial-intelligence-risk-management | Yes | Borrowed (agentic ops) |
| 40 | 92% EU banks deploying AI; 55% using GPAI/agentic in consumer apps | EBA | https://www.eba.europa.eu/sites/default/files/2025-09/Rising%20application%20of%20AI%20in%20EU%20banking%20and%20payments%20sector.pdf | Yes | Borrowed (S5) |
| 41 | DBS: 2,000+ AI models, 430+ use cases, SGD 1B+ value | DBS Newsroom | https://www.dbs.com/newsroom/DBS_named_Worlds_Best_AI_Bank_2025 | Yes | Borrowed (agentic ops) |
| 42 | JPMC: 450+ AI use cases, $1.5–2B measurable value | Lucidate | https://www.lucidate.co.uk/post/beyond-the-pilot-how-jpmorgan-goldman-sachs-and-hsbc-are-scaling-ai-to-enterprise-production | Yes | Borrowed (agentic ops) |

---

## Summary of Key Findings

1. **The operational model gap is real and is the primary constraint on banking AI scaling.** Five independent evidence streams (cost, scaling, bottleneck analysis, platform comparison, standards landscape) converge on the same conclusion: AI capability is not the bottleneck — operational context, governance infrastructure, and domain-specific process models are.

2. **Existing platforms solve fragments, not the whole problem.** Pega comes closest for dispute management and decisioning (deep, auditable operational model), but coverage is narrow (3–5 processes) and extension requires expensive professional services. Salesforce, ServiceNow, and Google each solve different fragments. No platform provides a general-purpose banking operational substrate.

3. **The cost signature of the gap is measurable.** AI agent deployments cost $150K–$300K+ per use case with 5–40x budget overruns. Each deployment rebuilds governance, context, and integrations from scratch. McKinsey's finding that 30–50% of AI team time is spent on compliance overhead directly quantifies the cost of absent operational models.

4. **Customer-facing banking AI has unique accountability requirements** not shared by back-office or infrastructure AI: named-customer impact, consumer protection law, regulatory complaint timelines, explainability obligations, and trust consequences. Only 28% of organizations can trace agent actions to a human sponsor.

5. **Standards are emerging but 2–3 years from banking-ready.** IETF Txn-Tokens for Agents (identity delegation), ISO 42001 (governance framework), A2A (multi-agent coordination), and MCP (tool interaction) are building blocks, but no standard integrates them for banking-specific governance. The August 2026 EU AI Act high-risk deadline will arrive before standards mature.

6. **The compounding hypothesis is architecturally valid but empirically unproven.** Banks with operational substrates (DBS, BNY Mellon, JPMC) appear to deploy AI faster, but no public data provides domain-by-domain acceleration metrics. This is a gap in available evidence.

7. **Pega's existence validates both the thesis and the opportunity.** Pega's success in dispute management and NBA proves that deep, domain-specific operational models enable effective AI deployment. But Pega's narrowness — and the cost of extending it — proves that the operational model gap is real and commercially significant.

8. **The window is 2026–2028.** EU AI Act high-risk obligations (Aug 2026), Gartner's predicted >40% agentic project cancellation (end 2027), OSFI E-23 (May 2027), and foundation model convergence all create pressure. Banks that build operational substrates in this window gain compounding advantage. Those that don't will face escalating costs and regulatory risk.
