# Stream 5: AIOps and Agentic Operations — Emerging Category

**Research date:** 15 March 2026
**Engagement area:** Cloud and Platform Operations — Banking Opportunity Analysis
**Stream:** S5 — AIOps Evolution and the Emergence of Agentic Autonomous Operations

---

## Why This Stream Is Separate

Analyst coverage conflates "AI-powered observability" (alert summarization, copilots) with architecturally distinct agent-first operations (autonomous diagnosis, swarm coordination, auto-resolution). This stream separates the two and assesses the maturity of the emerging "agentic operations" category.

---

## Methodology

Evidence gathered via targeted web research across vendor product announcements, analyst reports (Gartner, Forrester), vendor documentation, press releases, academic papers, SRE community reports (DORA, Catchpoint, Honeycomb), and conference presentations. Every data point is tagged with a source and navigable URL. Vendor-provided improvement claims are explicitly flagged as `[vendor-stated]` unless independently verified. Claims lacking independent verification are flagged `[unverified — needs manual confirmation]`.

---

## Section 1: AIOps Market Evolution — Three Generations

### Market Size

The AIOps market is valued between $16.6B and $38.5B in 2025 depending on analyst scope definitions, with projections reaching $85B–$303B by 2035 at a 17–23% CAGR (Research Nester, IMARC Group, Global Growth Insights). The wide variance reflects definitional disagreement on what counts as "AIOps."

| Source | 2025 Value | Forecast | CAGR | URL |
|--------|-----------|----------|------|-----|
| Research Nester | $16.6B | $85.4B by 2035 | 17.8% | https://www.researchnester.com/reports/aiops-market/3309 |
| IMARC Group | $32.5B | $132.2B by 2034 | 16.9% | https://www.imarcgroup.com/aiops-market |
| Global Growth Insights | $38.5B | $303.6B by 2035 | 22.95% | https://www.globalgrowthinsights.com/market-reports/aiops-market-123813 |
| AAC (citing Mordor Intelligence) | $11.7B (2023) | $32.4B by 2028 | 22.7% | https://www.aac.com/wp-content/uploads/2025/07/AIOps-an-IT-Operations-Opportunity.pdf |

### Three Generations Comparison

| Dimension | Gen 1: Event Correlation (2016–2021) | Gen 2: ML Anomaly Detection (2021–2025) | Gen 3: Agentic Autonomous Operations (2025+) |
|-----------|--------------------------------------|----------------------------------------|----------------------------------------------|
| **Core technique** | Rule-based event correlation, alert grouping, noise reduction | Machine learning anomaly detection, statistical RCA, predictive alerting | LLM-augmented reasoning, causal AI, autonomous decision-making, tool use |
| **Representative vendors** | BigPanda, Moogsoft (acquired by Dell 2023), early PagerDuty | Dynatrace Davis AI (causal), Datadog Watchdog, ServiceNow ITOM, Splunk ITSI | PagerDuty SRE Agent, Datadog Bits AI, Dynatrace Intelligence, ServiceNow Autonomous Workforce, New Relic Agentic Platform |
| **What it does** | Reduces alert volume by grouping related events; correlates across monitoring tools | Detects anomalies without predefined thresholds; identifies probable root cause from telemetry patterns | Autonomously investigates incidents, reasons about root cause using causal context, executes remediation actions with guardrails |
| **Human role** | Operator reviews correlated groups, decides action | Operator validates ML-suggested root cause, initiates remediation | Operator supervises; agent acts within policy boundaries; human approves high-risk actions |
| **Typical result** | 70–90% alert noise reduction `[vendor-stated]` | Minutes-to-hours RCA vs. hours-to-days; WeLab Bank: 100+ daily alerts → <5 | ServiceNow: 90% L1 ticket auto-resolution (internal deployment); PagerDuty: 50% faster incident resolution `[vendor-stated]` |
| **Limitations** | Rules brittle to topology changes; no prediction; requires manual correlation logic maintenance | ML models require training data; false positive rates still high; cannot remediate, only detect and suggest | Nascent; guardrail design unproven at scale; regulatory acceptance in banking uncertain; hallucination risk in diagnosis |
| **Banking adoption** | Widespread in Tier 1; partial in Tier 2 | Active in Tier 1/2; TD Bank (Dynatrace), WeLab Bank (Davis AI) | Emerging; no confirmed production deployment at a regulated bank with full autonomous remediation |

### Where the Market Is Today

The market is in a generational transition between Gen 2 and Gen 3. The evidence profile:

| Signal | Evidence | Source |
|--------|----------|--------|
| Gartner calls Agent-Native I&O "the biggest disruptor since cloud" | Identified as top I&O trend for 2025 | https://www.gartner.com/en/newsroom/press-releases/2024-12-11-gartner-identifies-the-top-trends-impacting-infrastructure-and-operations-for-2025 |
| Gartner predicts 70% of enterprises will deploy agentic AI in IT infrastructure ops by 2029 | Up from <5% in 2025 | https://www.itential.com/resource/analyst-report/gartner-predicts-2026-ai-agents-will-reshape-infrastructure-operations/ |
| Every major observability vendor launched agentic products in 2025–2026 | PagerDuty, Datadog, Dynatrace, New Relic, ServiceNow all announced within 12 months | See vendor table below |
| Gartner I&O Conference 2026 features "Self-Healing" and "Autonomous IT" sessions | LogicMonitor presenting "From Monitoring to Self-Healing" | https://www.gartner.com/en/conferences/na/infrastructure-operations-cloud-us/sessions/detail/4314349 |
| No confirmed production deployment at a regulated bank with full autonomous remediation | Gap between vendor capability and banking adoption | Research finding |

---

## Section 2: Vendor AI Capabilities

### Vendor AI Capabilities Table

| Vendor | Product | Launch | Type | Autonomous Actions | Banking-Specific Features | Evidence Quality | URL |
|--------|---------|--------|------|-------------------|--------------------------|-----------------|-----|
| **Datadog** | Bits AI (SRE Agent, Dev Agent, Security Analyst) | Dec 2025 (Limited Availability) | **Agent** — autonomously investigates; takes action via integrations | Investigates alerts 24/7; auto-generates code fixes via GitHub PRs; creates Jira tickets; pages engineers; sends Slack messages | None documented | Vendor product docs; press release | https://investors.datadoghq.com/news-releases/news-release-details/datadog-launches-bits-ai-sre-agent-resolve-incidents-faster |
| **PagerDuty** | PagerDuty Advance (SRE Agent, Scribe Agent, Shift Agent, Insights Agent) | Spring 2025 (SRE Agent); Spring 2026 (expanded) | **Agent** — SRE Agent acts as virtual first responder on schedules; autonomous triage and diagnosis | Added directly to on-call schedules; detects, triages, diagnoses before paging humans; auto-remediation of well-known issues; learns from past incidents | None documented beyond general enterprise controls | Press release; community announcement | https://www.pagerduty.com/newsroom/pagerduty-operations-cloud-spring-2026-release/ |
| **ServiceNow** | Now Assist + Autonomous Workforce + AI Agents | Now Assist GA 2024; Autonomous Workforce 2026 (internal, GA H2 2026) | **Agent** — Autonomous Workforce resolves tickets end-to-end; Now Assist is copilot | 90% of internal help desk tickets auto-resolved; >99% for targeted L1 categories (password resets, account unlocks, VPN, software access) | Financial Services Operations (FSO) module with domain-specific AI; Fiserv partnership for AI-driven financial services transformation | Strongest evidence: ServiceNow's own deployment documented by The Register; Fiserv partnership verified | https://www.theregister.com/2026/02/26/servicenow_ai_bot_helpdesk_tickets/ |
| **Dynatrace** | Davis AI + Dynatrace Intelligence + Dynatrace Assist | Davis AI (ongoing); Dynatrace Intelligence Feb 2026 | **Hybrid** — deterministic causal AI (Davis) + agentic AI (Intelligence) for autonomous operations | Automatic problem detection and RCA; agentic workflows turn automations into autonomous operations; bidirectional integrations with ServiceNow, AWS, Azure, GCP, Atlassian, GitHub | Banking customers: TD Bank (AIOps consolidation), WeLab Bank (95% alert reduction), Alpha Bank (cloud-native transformation) | Press release + verified customer deployments; benchmarked: deterministic agents solve problems 12x more often, 3x faster, at half the cost vs. external SRE agents `[vendor-stated]` | https://www.dynatrace.com/news/press-release/dynatrace-intelligence-redefines-observability/ |
| **New Relic** | NRAI + Agentic Platform + SRE Agent | NRAI GA Jun 2025; Agentic Platform Feb 2026 | **Agent** — no-code agent builder for SREs; SRE Agent for autonomous incident response | Automated issue triage, RCA, change management, incident lifecycle; custom agent creation without code | Enterprise governance: RBAC, audit logs, compliance controls; agentic integrations with ServiceNow and GitHub Copilot | Press release; product documentation | https://newrelic.com/press-release/20260224-1 |
| **Grafana Labs** | Grafana Assistant + LLM Plugin + Sift | LLM Plugin GA Mar 2025; Grafana Assistant May 2025 | **Copilot** — conversational assistant; no autonomous remediation | Error log explanation; incident auto-summary; dashboard creation via natural language; investigation assistance | None documented | Product blog; documentation | https://grafana.com/blog/2025/05/07/llm-grafana-assistant |
| **BigPanda** | Agentic ITOps | 2024–2025 (evolutionary) | **Hybrid** — event correlation roots with generative AI layer | Alert correlation + generative AI for investigation and summarization; positioning toward agentic ITOps | None documented | Blog post; positioning paper | https://www.bigpanda.io/gartner-predicts-2024-generative-ai/ |

### Classification: Copilot vs. Agent vs. Hybrid

| Classification | Definition | Vendors |
|---------------|------------|---------|
| **Copilot** | Assists human operators; summarizes, explains, suggests — does not take autonomous action | Grafana Assistant |
| **Agent** | Autonomously investigates and/or remediates within defined guardrails; can be placed on on-call schedules or resolve tickets end-to-end | Datadog Bits AI, PagerDuty SRE Agent, ServiceNow Autonomous Workforce, New Relic SRE Agent |
| **Hybrid** | Combines deterministic/causal AI (no LLM needed) with agentic AI capabilities; autonomous detection + optional autonomous remediation | Dynatrace Intelligence, BigPanda |

**Key finding:** As of March 2026, every major observability vendor except Grafana Labs has launched or announced an agent-class product. Grafana remains positioned as a copilot/assistant. The market has moved faster than most analysts predicted — Gartner's 2024 prediction of <5% enterprise agentic deployment by 2025 may already be conservative given vendor launch velocity.

---

## Section 3: Autonomous Remediation Evidence

### Auto-Resolution Evidence Table

| Vendor/Org | Claim | Scope | Auto-Resolution Rate | MTTR Impact | Evidence Type | Verified | Source |
|-----------|-------|-------|---------------------|-------------|--------------|----------|--------|
| **ServiceNow** | Autonomous Workforce resolving 90% of internal help desk tickets | Internal deployment (ServiceNow's own employee help desk) | 90% overall; >99% for targeted L1 categories | "Materially faster than human-only workflows" (no specific number) | Vendor's internal deployment, reported by The Register | Partially — self-reported but covered by independent tech press | https://www.theregister.com/2026/02/26/servicenow_ai_bot_helpdesk_tickets/ |
| **PagerDuty** | Up to 50% faster incident resolution from AI agents | General platform capability | Not disclosed | 50% faster `[vendor-stated]` | Vendor marketing claim via industry analysis | No independent verification | https://www.aicerts.ai/news/autonomous-workflow-repair-systems-cut-downtime-boost-resilience/ |
| **Dynatrace** (WeLab Bank) | Daily alerts reduced from 100+ to <5; root cause ID from hours to minutes | WeLab Bank (digital bank, Hong Kong) | >95% unnecessary alert reduction | Hours → minutes for RCA | Vendor customer case study | Partially — customer-named case study | https://dynatrace.com/customers/welab |
| **Dynatrace** (benchmark) | Deterministic agents solve problems 12x more often, 3x faster, at half the cost vs. external SRE agents | Vendor benchmark | N/A | 3x faster | Vendor press release | No — vendor benchmark `[vendor-stated]` | https://www.dynatrace.com/news/press-release/dynatrace-intelligence-redefines-observability/ |
| **New Relic** | 25% faster incident resolution for AI users vs. non-AI users | Platform usage data | Not disclosed | 25% faster | Vendor press release | No — vendor internal data `[vendor-stated]` | https://newrelic.com/press-release/20260224 |
| **CoComply** | 50–70% reduction in downstream incidents via automated quarantine and remediation | Risk data controls in banking governance | Not disclosed | Not disclosed | Vendor website | No `[vendor-stated]` | https://www.cocomply.ai/use-cases/risk-data-controls/ |
| **Research paper** | Significant MTTR reduction and SLA violation reduction in Kubernetes-based financial systems | Academic framework for autonomous incident handling in regulated financial systems | Not disclosed (framework paper) | "Significant reduction" | Peer-reviewed research (Research Square) | Yes — academic paper | https://www.researchsquare.com/article/rs-8715462/latest |
| **Zeta** (from S4) | 80% reduction in banking incident response time | Multi-tenant banking SaaS (Amazon OpenSearch) | N/A (detection, not auto-resolution) | 80% faster response | AWS case study | Yes — customer-named | https://noise.getoto.net/2025/08/21/zeta-reduces-banking-incident-response-time-by-80-with-amazon-opensearch-service-observability/ |
| **Standard Chartered** (from S4) | 25% decrease in incident response time; 40% reduction in system downtime | SRE Academy + Sumo Logic implementation | N/A (SRE process, not auto-resolution) | 25% faster response | QA Financial / Link Group case study | Yes — customer-named | https://qa-financial.com/how-site-reliability-engineering-is-driving-qa-stability-at-standard-chartered/ |

### Critical Assessment

**What is actually auto-resolved in production today (March 2026):**

1. **L1 help desk tickets** — password resets, account unlocks, software access, VPN connectivity. ServiceNow demonstrates 90%+ auto-resolution for these categories on its own help desk. This is real but narrow: these are high-volume, low-risk, well-understood patterns.

2. **Alert noise reduction** — WeLab Bank's 95% alert reduction via Dynatrace Davis AI eliminates unnecessary alerts, but this is auto-detection/filtering, not auto-remediation.

3. **Runbook-driven automation** — PagerDuty and Datadog can execute predefined runbooks when specific conditions match. This is automation, not autonomous reasoning.

**What is NOT auto-resolved in production today:**

1. **Complex multi-service incidents** requiring cross-domain diagnosis. No vendor has demonstrated autonomous resolution of cascading failures across microservices in a banking environment.

2. **Infrastructure remediation** (scaling, traffic routing, service restarts) in regulated banking environments with full audit trail and regulatory acceptance. This remains in early access / preview across all vendors.

3. **Novel incidents** — no evidence that any vendor's agentic system can autonomously resolve incident types it has not previously encountered.

**The gap between vendor claims and banking reality:**

| Dimension | Vendor Capability (March 2026) | Banking Readiness |
|-----------|-------------------------------|-------------------|
| L1 ticket auto-resolution | Production-ready (ServiceNow) | Applicable to internal IT; unclear for customer-facing banking operations |
| Alert correlation + RCA | Production-ready (Dynatrace, Datadog) | Deployed at TD Bank, WeLab Bank, Alpha Bank |
| Autonomous infrastructure remediation | Early Access / Preview (Datadog, PagerDuty, Dynatrace) | No confirmed regulated bank deployment |
| Multi-agent incident coordination | Architectural vision (Dynatrace ecosystem) | No production evidence |
| Autonomous remediation with full regulatory audit | Framework-level research (academic papers) | Not production-validated |

---

## Section 4: Swarm Coordination and Multi-Agent Operations

### Current State of Multi-Agent Operations

| Signal | Evidence | Assessment | Source |
|--------|----------|------------|--------|
| Dynatrace announces "agentic ecosystem" with SRE agents, ITSM agents, developer agents | Bidirectional integrations with ServiceNow, AWS, Azure, GCP, Atlassian, GitHub, Red Hat | **Architectural vision** — ecosystem announced, but multi-agent coordination for complex incident resolution is not documented in production | https://www.dynatrace.com/news/press-release/dynatrace-intelligence-redefines-observability/ |
| PagerDuty announces "agent-to-agent functionality" in Early Access | SRE Agent communicates with Scribe Agent, Shift Agent, Insights Agent; all Incident Management actions available via MCP by end H1 FY27 | **Early Access** — announced but not GA; multi-agent patterns are inter-product, not swarm-style autonomous coordination | https://www.pagerduty.com/newsroom/pagerduty-operations-cloud-spring-2026-release/ |
| Datadog Bits AI has SRE Agent, Dev Agent, Security Analyst | SRE Agent triggers Dev Agent to create code fixes via GitHub PRs | **Cross-agent handoff** — agent-to-agent orchestration within Datadog's own product suite; not open multi-agent | https://docs.datadoghq.com/bits_ai/bits_ai_sre/take_action/ |
| New Relic Agentic Platform allows custom multi-step agent creation | No-code builder; unified AI orchestration | **Platform for custom agents** — multi-agent potential, but documented examples are single-agent workflows | https://newrelic.com/press-release/20260224-1 |
| Gartner: "AI agents collaborate to understand stakeholder needs and automatically adapt systems" | Top I&O trend for 2025 | **Analyst prediction** — not observed in production | https://www.gartner.com/en/newsroom/press-releases/2024-12-11-gartner-identifies-the-top-trends-impacting-infrastructure-and-operations-for-2025 |

### Honest Assessment

**Multi-agent swarm coordination for IT operations is architectural vision, not production reality.** Evidence as of March 2026:

- **Vendor-internal agent-to-agent handoffs exist** (Datadog SRE → Dev Agent; PagerDuty SRE → Scribe/Shift/Insights agents) but these are product-internal orchestration patterns, not autonomous swarm behavior.
- **Dynatrace's agentic ecosystem** is the closest to a multi-agent architecture, but its announced integrations are bidirectional tool connections, not autonomous agent-to-agent negotiation or coordination.
- **No evidence** of multiple specialized agents autonomously collaborating to resolve a complex incident (e.g., a network agent, an application agent, and a database agent jointly diagnosing a cascading failure) in any production environment, banking or otherwise.

**Cross-reference with existing agentic systems research** (see `market-study/agentic-systems-development-platforms/`): The distinction between "agent fleet platforms" (managed orchestration of independent agents) and "agentic systems" (coordinated, adaptive, policy-governed ecosystems) applies directly. Current vendor offerings are agent fleet patterns. True agentic system coordination — with peer-to-peer negotiation, capability-based delegation, and emergent behavior — remains architecturally undefined for IT operations.

---

## Section 5: Banking-Specific Requirements for AI in Operations

### Requirement Analysis

| Requirement | Why It Matters in Banking | Current Vendor Handling | Gap Assessment |
|-------------|--------------------------|------------------------|----------------|
| **PII in operational data** | Logs, traces, and metrics may contain account numbers, transaction details, customer identifiers. AIOps tools ingest and analyze this data. | Dynatrace: data masking and anonymization capabilities in Grail. Datadog: sensitive data scanner. ServiceNow: data classification. Generic capability, not banking-specific by default. | **Moderate gap.** Vendors have data masking tools but PII-aware AI reasoning (where the AI must handle PII during diagnosis but cannot retain or expose it) is not a native capability. Banks must configure this. |
| **Audit trails for AI decisions** | Regulators (DORA, OCC, PRA) require traceability of operational decisions. If an AI agent restarts a service or reroutes traffic, the decision chain (what triggered it, what data was used, why this action was chosen, what the outcome was) must be auditable. | ServiceNow: audit logging native to platform. PagerDuty: action logs and approval chains. New Relic: RBAC + audit logs. Dynatrace: workflow audit trails. | **Significant gap.** Vendors log *what* the agent did but not *why* at the reasoning level. AI decision rationale (chain-of-thought, confidence scores, alternatives considered) is not captured in production audit trails. This is a first-order concern for banking regulators. See cognitive classification research in `market-study/agentic-systems-development-platforms/background/cognitive-classification.md`. |
| **Regulatory accountability for automated remediation** | Under DORA (EU), OCC (USA), and PRA (UK), a human must be accountable for operational decisions affecting important business services. Autonomous AI remediation creates an accountability gap: who is responsible when the AI makes a wrong call? | No vendor has solved this. PagerDuty's approach (human approves high-risk remediations) is the closest pattern but shifts the problem to approval latency. | **Critical gap.** Regulatory frameworks were written for human decision-makers. AI agent accountability is not addressed in DORA, OCC guidance, or PRA rules. Banks that deploy autonomous remediation are operating in regulatory grey area. |
| **Change management compliance** | Banking ITIL/ITSM processes require change approval boards (CABs) for production changes. Autonomous remediation bypasses these processes. | ServiceNow: integrates with change management workflows. Dynatrace: can trigger ServiceNow change requests. But autonomous agents that can bypass CAB processes are architecturally possible. | **Moderate gap.** Vendors provide integration hooks, but the governance question — whether an AI agent's remediation action constitutes a "change" requiring CAB approval — is unresolved. |
| **Model explainability for RCA** | When AI identifies root cause, the reasoning must be explainable to auditors and regulators. "The AI said so" is not acceptable in a regulatory examination. | Dynatrace Davis AI uses causal (deterministic) AI for RCA, which is inherently explainable (it traces actual dependency relationships). LLM-based agents (Datadog Bits AI, New Relic) rely on generative reasoning that is harder to audit. | **Varies by vendor.** Dynatrace's causal approach has a structural advantage for explainability. LLM-based agents face the standard explainability challenge. |
| **Multi-tenancy and data isolation** | Banks operating BaaS or multi-entity platforms must ensure AI operations data from one tenant cannot leak to another. | Not addressed by any vendor in the context of AI agent reasoning. Standard infrastructure-level isolation exists. | **Significant gap.** If an AI agent reasons across telemetry from multiple tenants to diagnose an issue, tenant data isolation at the AI reasoning layer is architecturally undefined. |

### AxonFlow and CoComply: Banking-Native AI Governance Patterns

Two emerging vendors target banking-specific AI governance:

| Vendor | Capability | Relevance | Source |
|--------|-----------|-----------|--------|
| **CoComply** | AI agents for banking governance; automated compliance; 85% reduction in manual governance tasks; SOC 2 Type II; end-to-end encryption | Governance-native approach to AI in banking operations; stores control evidence (run results, checksums, approver notes) for every operation | https://www.cocomply.ai/ |
| **AxonFlow** | PII masking (SSN, account numbers, credit cards) in audit trails; ECOA, FCRA, TILA compliance; PCI-DSS and RBI guideline enforcement | Production-ready patterns for PII protection in AI-driven banking operations | https://docs.getaxonflow.com/docs/examples/banking |

### DORA Implications for AI-Driven Operations

| DORA Requirement | Impact on AI Operations | Current Readiness |
|-----------------|------------------------|-------------------|
| ICT risk management framework (Art. 5–16) | AI agents that take operational actions are ICT systems requiring risk assessment, testing, and ongoing monitoring | No vendor provides DORA-specific risk assessment frameworks for AI agents |
| Incident reporting within 4 hours (Art. 17–23) | If an AI agent's autonomous remediation creates a new incident or worsens an existing one, reporting obligations apply | Vendors log agent actions but automated DORA incident reporting from AI agent failures is not a product feature |
| Resilience testing including TLPT (Art. 24–27) | AI agent behavior under stress must be tested; adversarial testing of AI decision-making in operations | No vendor offers adversarial testing of their AI agents' operational decision-making |
| Third-party ICT register (Art. 28–44) | AI agents from vendors (PagerDuty, Datadog, etc.) are third-party ICT services requiring registration and concentration risk assessment | Standard vendor management applies, but AI agent-specific risk factors (hallucination, drift, adversarial manipulation) are not in current vendor risk assessment templates |

---

## Section 6: AI Agent Governance in Operations

### How Banks Govern AI Agents That Take Operational Actions

**The governance challenge:** An AI agent that can restart services, scale infrastructure, route traffic, or execute runbooks has production-level authority. Banking governance frameworks (ITIL, ITSM, regulatory requirements) were designed for human operators.

| Governance Dimension | Current Best Practice (observed) | Gap |
|---------------------|--------------------------------|-----|
| **Permission boundaries** | PagerDuty: "full control over permissions and remediation approvals" for SRE Agent. Datadog: agent actions configured by admins. ServiceNow: RBAC and approval chains. | Permissions are coarse-grained (can/cannot take action). No fine-grained policy like "can restart service X only if fewer than 100 active sessions and not during market hours." |
| **Human-in-the-loop** | PagerDuty: human approves high-risk remediations. ServiceNow: escalates uncertain tickets rather than providing incorrect answers. | Approval latency defeats the purpose of autonomous operations. The industry has not solved the trade-off between speed and governance. |
| **Confidence thresholds** | Academic framework: "safety gates, confidence thresholds, auditable decision logs, rollback mechanisms, and controlled human escalation pathways" | Research-stage. No vendor has exposed confidence thresholds as configurable governance controls for banking customers. |
| **Rollback capability** | Dynatrace: workflows can include rollback steps. PagerDuty: process automation can include undo actions. | Rollback exists for predefined runbooks. Autonomous agent decisions that create novel actions (not from a runbook) do not have automatic rollback. |
| **Blast radius limitation** | No vendor has documented "blast radius" controls for AI agent actions — e.g., limiting the scope of an agent's remediation to a single service, cluster, or region. | **Critical gap.** An unconstrained AI agent that incorrectly diagnoses a problem could amplify the incident by taking broad remediation actions. |
| **Drift monitoring** | No vendor monitors whether AI agent decision quality degrades over time (decision drift, model drift in the operational context). | The concept from ML observability (Arize, WhyLabs, Fiddler) has not been applied to operational AI agents. |
| **Separation of duties** | Banking regulation requires separation between who designs automation and who approves it for production use. | No vendor separates AI agent development/configuration from production deployment approval in a way that satisfies banking separation-of-duties requirements. |

### Guardrails That Exist Today

| Guardrail | Vendor | Description | Source |
|-----------|--------|-------------|--------|
| Approval gates for high-risk actions | PagerDuty | Human must approve before agent executes remediation outside predefined safe actions | https://www.pagerduty.com/newsroom/pagerduty-operations-cloud-spring-2026-release/ |
| Escalation on uncertainty | ServiceNow | Autonomous Workforce escalates tickets rather than providing incorrect answers; avoids hallucination risk | https://www.theregister.com/2026/02/26/servicenow_ai_bot_helpdesk_tickets/ |
| RBAC and audit logging | New Relic | Fine-grained permissions, role-based access control, full audit logging for agentic platform | https://newrelic.com/press-release/20260224-1 |
| Deterministic AI grounding | Dynatrace | Uses causal (deterministic) AI grounded in real-time topology to prevent hallucinated diagnoses | https://www.dynatrace.com/news/press-release/dynatrace-intelligence-redefines-observability/ |
| Configurable agent scope | Datadog | Admin configures which actions Bits AI SRE can take; actions are predefined (page, create ticket, send message) | https://docs.datadoghq.com/bits_ai/bits_ai_sre/take_action/ |

### Guardrails That Do Not Exist

1. **Policy-as-code for AI agent behavior** — declarative policies that constrain AI agent actions based on business context (market hours, customer impact, regulatory state). No vendor offers this.
2. **Cross-agent governance** — when multiple agents from different vendors act on the same incident, there is no coordination or conflict resolution mechanism.
3. **Regulatory reporting for AI agent actions** — automated generation of regulatory-compliant reports documenting AI agent operational decisions.
4. **Adversarial testing frameworks** — systematic testing of AI agents' behavior under adversarial conditions (manipulated telemetry, poisoned training data, conflicting signals).
5. **AI agent change management** — treating updates to AI agent behavior (model updates, prompt changes, tool permission changes) as production changes subject to CAB review.

---

## Section 7: Patent and R&D Activity Signals

Direct patent search results were unavailable through web search. The following R&D investment signals are inferred from product launches and vendor announcements:

| Vendor | R&D Signal | Investment Direction | Source |
|--------|-----------|---------------------|--------|
| **Dynatrace** | Dynatrace Intelligence launched as "industry's first agentic operations system"; combines causal + agentic AI; Perform 2026 keynote positioned it as architectural foundation | Heavy investment in causal-deterministic AI combined with agentic capabilities; differentiated approach vs. pure-LLM competitors | https://www.dynatrace.com/news/press-release/perform-2026-ignites-new-era/ |
| **Datadog** | Bits AI expanded from copilot (2024) to autonomous SRE Agent + Dev Agent + Security Analyst (2025–2026); DASH conference keynote | Rapid expansion from copilot to multi-domain autonomous agents; investing in code-level remediation (Dev Agent creates PRs) | https://investors.datadoghq.com/news-releases/news-release-details/datadog-launches-bits-ai-sre-agent-resolve-incidents-faster |
| **ServiceNow** | Acquired Moveworks (conversational AI); developed Autonomous Workforce; AI Models v2.0 (SLM + LLM); investing in domain-specific agentic agents | Deepest internal deployment evidence (90% ticket resolution); acquisition-driven AI expansion; leveraging 20 years of structured ITSM data as training advantage | https://apnews.com/press-release/business-wire/servicenow-launches-autonomous-workforce-that-thinks-and-acts-adds-moveworks-to-the-servicenow-ai-platform-2ad68f422ae24bee86b89ece0edb83c6 |
| **PagerDuty** | SRE Agent positioned on on-call schedules (novel UX pattern); agent-to-agent via MCP; Rundeck/Process Automation integration for remediation execution | Investing in the "agent as teammate" paradigm; MCP adoption signals commitment to open agent interoperability | https://www.pagerduty.com/newsroom/pagerduty-operations-cloud-spring-2026-release/ |
| **New Relic** | No-code agentic platform; SRE Agent; MCP integration; evaluation engine for continuous agent testing | Platform play — enabling customers to build custom agents rather than only providing vendor-built agents; differentiated governance approach | https://newrelic.com/press-release/20260224-1 |
| **Grafana Labs** | LLM Plugin GA; Grafana Assistant; focus on open-source AI integration | Conservative approach — AI as assistant, not autonomous agent; maintaining open-source positioning | https://grafana.com/blog/2025/05/07/llm-grafana-assistant |

### R&D Investment Direction Summary

The vendor R&D signals point to three distinct investment theses:

1. **Causal + Agentic fusion** (Dynatrace): deterministic AI for trustworthy diagnosis + agentic AI for autonomous action. Strongest explainability story for regulated industries.

2. **Platform + ecosystem** (ServiceNow, New Relic): leverage existing ITSM/observability data and workflows as the foundation for agentic operations; enable customers to build custom agents on top of the platform.

3. **Developer-centric agent tooling** (Datadog, PagerDuty): agents as first-class participants in the developer/SRE workflow — on-call schedules, PR creation, Slack-native interaction.

---

## Section 8: Cross-Reference with Agentic Systems Research

The existing research at `market-study/agentic-systems-development-platforms/` provides architectural context that directly applies to IT operations agents:

### Applicable Findings

| Finding from Existing Research | Application to IT Operations |
|-------------------------------|------------------------------|
| **Agent vs. Agentic System distinction** (agent-vs-agentic-system.md): Current vendors provide agent fleet platforms, not agentic system platforms. | Current AIOps vendors provide individual operational agents (SRE Agent, Dev Agent) or fleet platforms (New Relic's Agentic Platform). No vendor provides a true agentic system for IT operations — coordinated, adaptive, policy-governed. |
| **Enterprise Memory is the missing middle layer** (cognitive-classification.md): Agents that act in isolation cannot learn institutionally. | IT operations agents that resolve incidents without capturing the reasoning and outcome in enterprise memory will repeat mistakes and cannot improve institutionally. No current vendor captures AI agent decision rationale in a promotable format. |
| **Promotion paths** (cognitive-classification.md): Agent Memory → Enterprise Memory → Enterprise Knowledge. | Incident resolution patterns identified by AI agents should be promotable: agent learns a fix → pattern validated across incidents → becomes enterprise runbook. This promotion path does not exist in any current product. |
| **Policy-as-constraint engine** (agent-vs-agentic-system.md): Agents must reason about policies, not just be gated by them. | Banking AIOps agents should be able to reason about regulatory constraints (market hours, change freezes, customer impact) as part of their decision-making, not just be blocked by approval gates. No vendor provides this. |

---

## Key Findings

### Market Position

1. **AIOps is undergoing a generational shift from ML-assisted detection (Gen 2) to agentic autonomous operations (Gen 3).** Every major observability vendor launched agentic products between December 2025 and February 2026. The transition happened faster than analyst predictions. Gartner calls Agent-Native I&O "the biggest disruptor since cloud."

2. **The copilot era was brief.** Most vendors skipped directly from "AI copilot" to "AI agent" within 12–18 months. Grafana is the only major holdout maintaining a copilot-only position. This acceleration suggests vendors believe the copilot positioning is commercially insufficient.

3. **Auto-resolution is real but narrow.** ServiceNow's 90% auto-resolution rate is the strongest evidence, but it covers L1 help desk tickets (password resets, account unlocks, VPN). Complex, cross-service, novel incidents remain human-resolved. The gap between "90% of L1 tickets" and "autonomous resolution of a cascading microservice failure in a banking payment system" is enormous.

### Banking-Specific Assessment

4. **No regulated bank has deployed full autonomous remediation in production.** TD Bank uses Dynatrace for AIOps consolidation. WeLab Bank uses Davis AI for alert reduction. Standard Chartered has SRE process improvements. None have documented AI agents autonomously remediating production infrastructure incidents.

5. **Regulatory frameworks do not address AI agent accountability.** DORA, OCC, and PRA were written for human decision-makers. Autonomous AI remediation in banking operates in a regulatory grey area. This is the single largest barrier to adoption.

6. **Audit trail requirements for AI reasoning are unmet.** Current vendor audit trails capture *what* the agent did, not *why*. Banking regulators will require chain-of-thought auditability — the inputs, reasoning, confidence levels, alternatives considered, and rationale for the chosen action. No vendor provides this at production quality.

7. **PII in operational data is a solvable but unconfigured problem.** Vendors have data masking tools (Datadog Sensitive Data Scanner, Dynatrace data privacy features) but PII-aware AI reasoning — where the agent must use PII during diagnosis but cannot retain or leak it — is architecturally undefined.

### Architectural Observations

8. **Dynatrace's causal AI approach has a structural advantage for banking.** Deterministic, topology-aware root cause analysis is inherently more explainable and auditable than LLM-based reasoning. Dynatrace's benchmark claim (12x more accurate, 3x faster, half the cost vs. external SRE agents) is vendor-stated but architecturally plausible — causal analysis over a known dependency graph should outperform LLM-based pattern matching for infrastructure problems.

9. **Multi-agent coordination for IT operations is architectural vision, not production reality.** Vendor announcements describe agent-to-agent handoffs within their own product suites. True swarm coordination — multiple specialized agents from different domains autonomously collaborating on complex incidents — does not exist in production.

10. **ServiceNow has a unique data advantage.** Its Autonomous Workforce operates on 20 years of structured ITSM data (live CMDB, workflows, policy engines, transaction history). This data moat is structural — competing vendors would need to replicate this depth of enterprise operational context.

### Opportunity Signals

11. **The governance layer for AI agents in operations does not exist as a product category.** Policy-as-code for agent behavior, cross-agent governance, confidence threshold management, blast radius limitation, drift monitoring, adversarial testing — none of these exist as products. This is an opportunity.

12. **Enterprise Memory for IT operations is an unmet need.** When AI agents resolve incidents, the reasoning and outcome are not captured in a way that enables institutional learning. This maps directly to the "Enterprise Memory" gap identified in the agentic systems research (see Section 8).

---

## Gaps and Unresolved Questions

### Data Gaps

1. **Banking-specific auto-resolution rates.** No published data on what percentage of incidents at a regulated bank are auto-resolved by AI. ServiceNow's 90% is their own help desk, not a bank. `[unverified — needs manual confirmation]`

2. **MTTR improvement from agentic operations in banking.** Vendor claims (PagerDuty: 50% faster; New Relic: 25% faster; Dynatrace: 3x faster) are all vendor-stated. No independent study has measured MTTR improvement from agentic AIOps in a banking environment.

3. **Regulatory position on autonomous remediation.** No regulator (ECB, OCC, PRA, RBI) has issued guidance specifically addressing AI agents taking autonomous operational actions in banking infrastructure. This regulatory silence creates uncertainty.

4. **Total cost of AI agent governance.** The overhead of governing AI agents in operations (approval workflows, audit trail generation, confidence monitoring, adversarial testing) may offset the efficiency gains. No data on this trade-off exists.

5. **Incident type distribution suitable for auto-resolution.** What percentage of banking production incidents are L1-type (amenable to auto-resolution) vs. complex multi-service incidents (requiring human judgment)? This distribution determines the addressable scope of autonomous remediation in banking.

### Unresolved Research Questions

1. **Will banking regulators explicitly permit or restrict autonomous AI remediation?** The first regulatory guidance on this topic will set the market trajectory.

2. **Can Dynatrace's causal AI approach be replicated?** Its Smartscape dependency graph is built on deep agent-based instrumentation. Competitors using LLM-based reasoning over log/metric data face a structural disadvantage for RCA accuracy. Is this defensible?

3. **Will the "agent as on-call teammate" paradigm (PagerDuty) or "agent as autonomous workforce" paradigm (ServiceNow) win?** These are architecturally different: PagerDuty embeds the agent alongside humans in existing SRE workflows; ServiceNow replaces the human for defined ticket categories.

4. **How will multi-vendor AI agent conflicts be resolved?** A bank running Dynatrace agents, ServiceNow agents, and PagerDuty agents simultaneously has no coordination mechanism. Agent actions from one vendor could conflict with or duplicate actions from another.

5. **What is the failure mode of autonomous AI remediation?** When an AI agent makes a wrong remediation decision, what is the blast radius? No incident post-mortem data exists for AI-caused operational incidents in banking.

---

## Raw Notes

### Key Reports Referenced

| Report | Publisher | Year | Relevance |
|--------|----------|------|-----------|
| Gartner Top Trends Impacting I&O for 2025 | Gartner | Dec 2024 | Agent-Native I&O identified as "biggest disruptor since cloud" |
| Gartner Predicts 2026: AI Agents Will Reshape I&O | Gartner | 2025 | 70% of enterprises will deploy agentic AI in IT infra ops by 2029 |
| Gartner 2025 Hype Cycle for I&O Automation | Gartner | 2025 | Positioned IaC at mature mainstream; GitOps at peak interest |
| DORA/Google Accelerate State of DevOps Report | Google DORA | 2024 | AI adoption correlated with 7.2% decline in delivery stability |
| AIOps: An IT Operations Opportunity | AAC | Jul 2025 | AIOps market $11.7B (2023), 22.7% CAGR to $32.4B (2028) |
| Autonomous Incident Handling in Regulated Financial Systems | Research Square | 2025 | Closed-loop AI framework for K8s financial environments |
| Towards Autonomous Financial Platforms | World Journal of Advanced Research and Reviews | 2025 | AI agents and microservices for self-healing infrastructure |

### Vendor Product Timelines

| Date | Vendor | Product | Significance |
|------|--------|---------|-------------|
| 2024 (ongoing) | Dynatrace | Davis AI (causal + predictive) | Gen 2 AIOps with causal RCA |
| Jun 2025 | New Relic | NRAI (AI Assistant) GA | First AI assistant for observability |
| Jul 2025 | New Relic | Agentic Integrations GA | GitHub Copilot + ServiceNow integrations |
| Mar 2025 | Grafana Labs | LLM Plugin GA | LLM integration for Grafana (copilot-level) |
| May 2025 | Grafana Labs | Grafana Assistant | Context-aware LLM agent for Grafana Cloud |
| Spring 2025 | PagerDuty | PagerDuty Advance (SRE Agent) | AI agent on on-call schedules |
| Oct 2025 | ServiceNow | AI Models v2.0 (SLM + LLM) | Enhanced reasoning for Now Assist |
| Dec 2025 | Datadog | Bits AI SRE Agent (Limited Availability) | Autonomous alert investigation |
| Jan 2026 | Dynatrace | Dynatrace Intelligence (Perform 2026) | "Industry's first agentic operations system" |
| Feb 2026 | Dynatrace | Dynatrace Intelligence GA | Agentic workflows, Dynatrace Assist |
| Feb 2026 | ServiceNow | Autonomous Workforce (internal + select customers) | 90% ticket auto-resolution |
| Feb 2026 | New Relic | Agentic Platform + SRE Agent | No-code agent builder |
| Spring 2026 | PagerDuty | Spring 2026 Release (expanded AI agents) | Agent-to-agent, MCP integration |

### Search Terms Used

- "AIOps market evolution 2025 2026 Gartner event correlation ML anomaly agentic"
- "Datadog Bits AI capabilities 2025 2026 autonomous agent copilot features"
- "PagerDuty Advance Copilot autonomous remediation capabilities 2025 2026"
- "ServiceNow Now Assist ITSM AI autonomous operations 2025 2026"
- "Dynatrace Davis AI hypermodal autonomous root cause analysis 2025 2026"
- "Dynatrace Intelligence agentic operations system February 2026"
- "New Relic AI NRAI capabilities 2025 2026 autonomous monitoring copilot"
- "Grafana Labs AI ML features Sift machine learning 2025"
- "AI auto-resolution incidents percentage MTTR improvement documented evidence"
- "autonomous remediation auto-resolution incidents percentage bank financial services"
- "multi-agent swarm coordination IT operations incident resolution agentic SRE"
- "banking AIOps PII operational data audit trail regulatory accountability automated remediation"
- "Gartner top trends infrastructure operations 2025 agent native I&O"
- "Gartner predicts 2026 AI agents infrastructure operations"
- "AIOps market size 2025 2026 forecast growth rate"
- "ServiceNow autonomous workforce 90 percent help desk tickets"
- "BigPanda agentic ITOps evolution AIOps"
- "Datadog Bits AI SRE agent autonomous investigation remediation"
- "Forrester Wave AIOps platforms 2024 2025"
- "DORA State of DevOps 2024 AI operations observability MTTR"
