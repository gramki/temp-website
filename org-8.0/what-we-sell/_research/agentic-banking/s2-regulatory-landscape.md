# Stream 2: Regulatory Landscape — AI Agents in Customer-Facing Banking

| Field | Value |
|---|---|
| **Research date** | 15 March 2026 |
| **Engagement area** | Agentic Banking |
| **Stream** | S2 — Regulatory Landscape |
| **Analyst scope** | Regulations governing or constraining AI agent deployment in customer-facing banking operations (dispute resolution, application processing, servicing, advisory) |
| **Geographies** | USA, India, UK/EU |

---

## 1. Regulation Data Table

### 1.1 United States

| Regulation | Issuing Body | Date / Status | Key Requirements for Customer-Facing AI | Infrastructure Implications | URL | Verified |
|---|---|---|---|---|---|---|
| **SR 11-7 — Supervisory Guidance on Model Risk Management** | Federal Reserve / OCC | April 2011; in force. Being stress-tested against agentic AI (see GARP Feb 2025 analysis) | Comprehensive model governance: development documentation, independent validation, effective challenge, board-level oversight. Defines "model" as any system processing inputs to produce quantitative estimates — agentic AI's probabilistic, continuously-learning nature strains this definition. Traditional periodic review cycles are insufficient for agents that evolve between validations. | Immutable model lineage / versioning; real-time drift detection; continuous validation pipelines; audit-trail infrastructure that captures every agent reasoning step, not just periodic snapshots. | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm | Yes |
| **Interagency RFI on AI/ML in Financial Institutions** | Federal Reserve, OCC, FDIC, CFPB, NCUA | March 2021; comment period closed July 2021. No final rule issued. | Sought input on AI governance, risk management, and controls; challenges in AI adoption; whether regulatory clarification needed. Signals future rulemaking direction. | No direct mandate, but foreshadows forthcoming supervisory expectations around AI governance infrastructure. | https://www.federalreserve.gov/newsevents/pressreleases/bcreg20210329a.htm | Yes |
| **CFPB Circular 2023-03 — Adverse Action Notice Requirements for AI** | CFPB | September 2023; in force | No AI exemption from ECOA/Reg B. Creditors using AI/ML for credit decisions must provide *specific, accurate* principal reasons for adverse action — not merely check boxes on sample forms. When algorithms use non-traditional data (spending behavior, profession, browsing), the specific negative factors must be disclosed. | Explainability layer mandatory: every AI credit decision must produce human-readable reason codes traceable to specific model features. Black-box models are non-compliant by design. Requires feature-attribution infrastructure (SHAP/LIME or equivalent). | https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ | Yes |
| **CFPB Advisory Opinion — Section 1034(c) (Chatbots and Automated Customer Service)** | CFPB | October 2023; enforcement began 1 Feb 2024 | Large banks (>$10B assets) must provide timely, accurate, complete responses to consumer information requests. Chatbots that fail to recognize requests, provide inaccurate/incomplete information, or lack quality-assurance processes violate federal law. Cannot charge fees for information requests. Must allow escalation to human agents. | Real-time response-quality monitoring; intent-classification accuracy tracking; mandatory human escalation pathways; consumer interaction logging with completeness/accuracy metrics. | https://files.consumerfinance.gov/f/documents/cfpb-1034c-advisory-opinion-2023_10.pdf | Yes |
| **CFPB Issue Spotlight — Chatbots in Consumer Finance** | CFPB | June 2023 | 37% of US population interacted with bank chatbots in 2022. All top-10 commercial banks deploy chatbots. Identifies consumer harms: inaccurate information, wasted time, junk fees, inability to resolve complex issues, lack of transparency about non-human interaction. | Conversational AI must integrate with core banking systems for accurate, real-time data retrieval; cannot operate as isolated FAQ bots. | https://files.consumerfinance.gov/f/documents/cfpb_chatbot-issue-spotlight_2023-06.pdf | Yes |
| **CFPB Supervisory Highlights Issue 38 — Advanced Technologies (Winter 2025)** | CFPB | January 2025; in force | "There is no 'advanced technology' exception to Federal consumer financial laws." Found disparate impact in AI/ML credit scoring on Black/African American and Hispanic applicants. Auto lenders using >1,000 input variables failed adverse action specificity. Institutions must test models for bias, consider less discriminatory alternatives. | Bias testing and fair lending analysis pipeline must be embedded in model lifecycle. Alternative model evaluation (less discriminatory alternatives analysis) required pre-deployment. | https://files.consumerfinance.gov/f/documents/cfpb_supervisory-highlights-advanced-technologies_2025-01.pdf | Yes |
| **ECOA / Regulation B — Adverse Action Requirements** | CFPB (originally Federal Reserve Reg B) | 1974 (ECOA); codified 12 CFR 1002 | When AI agents participate in credit decisions or dispute resolution that results in adverse action, specific reasons must be provided. AI cannot obscure the basis for denial. Applies to any "creditor" — including automated systems acting on behalf of creditors. | Every AI-mediated credit decision must produce auditable, consumer-facing explanation. Decision pipeline must separate "model inference" from "reason-code generation" and validate both independently. | https://www.consumerfinance.gov/rules-policy/regulations/1002/ | Yes |
| **CFPB 2024 Enforcement Announcement — Crackdown on Chatbots** | CFPB | August 2024; rulemaking pending | CFPB announced rules to: (1) identify when chatbot use is unlawful, (2) require disclosure when customer is interacting with non-human agent, (3) mandate single-button access to human representative. | Bot-or-not disclosure infrastructure; human-handoff architecture with single-action trigger; chatbot interaction classification and monitoring. | [unverified — CFPB press release referenced in ABA Banking Journal and Venable LLP analyses; no standalone regulatory text URL identified] | No |
| **FFIEC Guidance on Authentication and Access** | FFIEC | August 2021; in force | MFA or equivalent controls for all high-risk interactions. Authentication requirements extend to system-to-system communications (relevant for AI agent API access). Layered security: network segmentation, monitoring, least-privilege access. Risk assessment required for digital banking tools including AI. | AI agents accessing customer data or executing transactions need machine identity management, API-level MFA, session-scoped permissions, and real-time anomaly detection on agent behavior. | https://www.consumerfinance.gov/about-us/newsroom/ffiec-issues-guidance-on-authentication-and-access-to-financial-institution-services-and-systems/ | Yes |
| **Colorado AI Act (SB 24-205)** | Colorado General Assembly | Signed May 2024; effective **30 June 2026** (postponed from Feb 2026 via SB 25B-004) | High-risk AI in financial services/lending must: written risk management policy; impact assessments and annual reviews; consumer disclosure when AI contributes to adverse consequential decisions; consumer right to appeal and correct data; public statement describing deployed high-risk systems. Safe harbor for entities under federal prudential regulator examination with published AI-specific guidance. Affirmative defense for NIST AI RMF / ISO 42001 compliance. | Impact assessment tooling; consumer notification pipeline integrated into decisioning; data correction and appeals workflow; public disclosure registry. NIST AI RMF alignment provides defensive advantage. | https://leg.colorado.gov/bills/sb24-205 | Yes |
| **Illinois BIPA** | Illinois General Assembly | 2008; amended August 2024 (SB 2979) | Written consent required before collecting biometric data (facial recognition, voiceprints, fingerprints). Cannot sell or profit from biometric data. Retain only until purpose fulfilled or 3 years after last interaction. 2024 amendment: damages per-person rather than per-scan, but liability remains substantial. | Any AI agent using voice biometrics or facial recognition for authentication must implement pre-collection consent workflow, biometric data lifecycle management, and Illinois-specific data handling policies. | https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004 | Yes |
| **NYC Local Law 144 — Automated Employment Decision Tools** | NYC Council | Effective July 2023; enforcement found "ineffective" by NY Comptroller Dec 2025; remediation underway | Annual independent bias audits for automated decision tools; public disclosure of audit results; candidate notification 10 days before assessment. While focused on employment, establishes precedent for bias audit requirements in AI decision-making. Penalties: $500–$1,500/day per violation. | Bias audit infrastructure and public reporting mechanisms. While employment-focused, the regulatory pattern is migrating to financial services. | https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page | Yes |

### 1.2 India

| Regulation | Issuing Body | Date / Status | Key Requirements for Customer-Facing AI | Infrastructure Implications | URL | Verified |
|---|---|---|---|---|---|---|
| **RBI FREE-AI Framework** (Framework for Responsible and Ethical Enablement of AI) | Reserve Bank of India | August 2025; advisory (not yet binding regulation) | 7 Sutras: Trust, People First, Innovation over Restraint, Fairness & Equity, Accountability, Understandable by Design, Safety/Resilience/Sustainability. 26 actionable recommendations across 6 pillars (Infrastructure, Policy, Capacity, Governance, Protection, Assurance). AI augments rather than replaces human judgment. Responsibility rests with deploying entity. | Explainability-by-design architecture; model governance framework; incident reporting; AI innovation sandbox participation; indigenous financial AI model development capability. | https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=1306 | Yes |
| **Digital Personal Data Protection Act 2023 (DPDP Act)** | Ministry of Electronics and IT (MeitY) | Enacted August 2023. DPDP Rules 2025 notified 13 Nov 2025. Phase 1 (Board setup) immediate; Phase 2 (consent managers) Nov 2026; Phase 3 (full compliance) May 2027 | Consent must be free, specific, informed, unconditional, unambiguous — explicit opt-in required. Purpose-specific consent (no bundling). Consent revocable; withdrawal must be as easy as provision. KYC data, credit bureau sharing, AML screening, credit assessment each require separate consent. Data localization: customer/financial data on India-based servers only. | Consent management system (CMS) with immutable audit trails; per-purpose consent collection UI integrated into AI agent interactions; data residency enforcement; consent lifecycle management across AI training and inference pipelines. Penalties up to ₹250 crore per breach. | https://www.meity.gov.in/static/uploads/2024/06/2a5ef610a85e2b05965a5a6bbd7e4c25.pdf | Yes |
| **RBI Master Direction — Digital Payment Security Controls** | RBI | July 2024; phased compliance: Large PSOs by April 2025, Medium by April 2026, Small by April 2028 | Comprehensive cyber resilience and security controls for payment system operators. Covers application security lifecycle, vendor risk management, data security, incident response, cloud security. Applies to AI-powered security and monitoring systems within payment operations. | Security-by-design in AI agent payment interactions; vendor risk assessment for AI model providers; incident response protocols for AI-mediated payment anomalies. | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12896 | Yes |
| **RBI Integrated Ombudsman Scheme 2026 (RB-IOS 2026)** | RBI | Effective 1 July 2026; replaces 2021 scheme | Widened "customer" definition — any person availing financial products/services. Complaints filed if no response within 30 days or if dissatisfied. Ombudsman can award up to ₹30 lakh for consequential loss, ₹3 lakh for mental anguish. Summary proceedings not bound by strict evidence rules. | AI agents handling complaints must maintain complete interaction records for Ombudsman review. Automated escalation to human when complaint complexity exceeds agent capability. Response-time SLAs must be engineered into agent workflows. Risk: AI-handled complaint deemed inadequate → Ombudsman awards enhanced compensation. | https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62052 | Yes |
| **SEBI Consultation Paper — Responsible AI/ML in Securities Markets** | SEBI | June 2025; consultation stage (comments closed July 2025) | Guidelines for model governance, investor protection, testing, fairness, bias mitigation, data privacy. Tiered approach: lighter framework for AI not directly impacting customers. Addresses concentration risk, herding behavior, explainability, and accountability. | Model governance and bias testing infrastructure; tiered compliance based on customer-impact classification. Not yet final — monitor for binding regulations. | https://www.sebi.gov.in/reports-and-statistics/reports/jun-2025/consultation-paper-on-guidelines-for-responsible-usage-of-ai-ml-in-indian-securities-markets_94687.html | Yes |
| **IRDAI Fraud Management Framework** | IRDAI | Effective 1 April 2026 | Board-approved anti-fraud policies; dedicated fraud monitoring committees; continuous AI-led surveillance across underwriting, claims, and distribution. Expanded fraud definitions to cover cyber-enabled "new-age" digital channel risks. | AI fraud detection systems mandatory; real-time surveillance infrastructure across insurance value chain. Relevant for AI agents in insurance-adjacent banking products. | [unverified — referenced in Moneycontrol analysis; IRDAI circular URL not independently confirmed] | No |

### 1.3 UK / EU

| Regulation | Issuing Body | Date / Status | Key Requirements for Customer-Facing AI | Infrastructure Implications | URL | Verified |
|---|---|---|---|---|---|---|
| **EU AI Act (Regulation 2024/1689)** | European Parliament / Council | Published OJ 12 July 2024. Prohibited practices effective 2 Feb 2025. GPAI obligations effective 2 Aug 2025. **High-risk AI requirements effective 2 Aug 2026.** Full product-integration rules by 2 Aug 2027. | **Annex III, ¶5**: AI systems evaluating creditworthiness of natural persons or establishing credit scores are **high-risk** (exception: fraud detection). High-risk requirements: risk management system, data governance, technical documentation, record-keeping, transparency, human oversight, accuracy/robustness/cybersecurity. Penalties: up to €35M or 7% global annual turnover. Profiling of natural persons in creditworthiness context is *always* high-risk (no derogation). | Immutable audit logs for every model decision; data governance pipelines with bias mitigation; human-in-the-loop review architecture; Annex IV technical documentation; conformity assessment processes; market surveillance notification capability; AI literacy training for all staff. | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 | Yes |
| **GDPR Article 22 — Automated Individual Decision-Making** | European Parliament / Council | In force since 25 May 2018 | Right not to be subject to solely automated decisions with legal/significant effects — including profiling. Exceptions: contractual necessity, legal authorization, explicit consent. Even under exceptions: right to human intervention, right to express view, right to contest. Must disclose: existence of automated decision-making, meaningful information about logic, significance and consequences. | Explanation-generation infrastructure for every automated decision; human review queue for contested decisions; consent management for automated processing; decision audit trails with logic documentation accessible to data subjects. | https://gdpr.eu/article-22-automated-individual-decision-making/ | Yes |
| **FCA Consumer Duty (PRIN 2A)** | Financial Conduct Authority (UK) | Effective 31 July 2023 (existing customers from 31 July 2024) | Four outcomes: Products & Services, Price & Value, Consumer Understanding, Consumer Support. Firms must deliver "good outcomes" for retail customers. 100% monitoring of customer interactions (voice, chat, email) — traditional 2-5% sampling insufficient. Must identify when specific customer groups (especially vulnerable) receive poorer outcomes from AI. Board-level accountability. Audit trails demonstrating Consumer Duty compliance. | Full-interaction monitoring and analytics platform; vulnerability detection in AI interactions; outcome measurement dashboards; real-time bias detection across customer segments; integration with SM&CR accountability mapping. | https://www.handbook.fca.org.uk/handbook/PRIN/2A.htm | Yes |
| **PRA / Bank of England AI Supervision Approach** | PRA / Bank of England | April 2024 letter to HMT; ongoing supervisory dialogue via roundtables (late 2025) | Technology-agnostic approach: existing prudential rules apply to AI. Four focus areas: operational resilience & third-party risk, governance, model risk management, data management. 75% of supervised firms already use AI; only 2% have fully autonomous decision-making. SM&CR places accountability on senior managers for AI in their areas. No AI-specific rules planned — reliance on existing framework with heightened supervisory attention. | Must demonstrate how existing governance frameworks (SM&CR, operational resilience, outsourcing) apply to AI systems. Third-party AI model risk assessment required. Board-level AI risk reporting. | https://www.bankofengland.co.uk/prudential-regulation/letter/2024/artificial-intelligence-and-machine-learning-letter | Yes |
| **FCA AI Update (April 2024)** | FCA | April 2024; advisory | Maps FCA framework to 5 Government AI Principles: safety/security/robustness, transparency/explainability, fairness, accountability/governance, contestability/redress. Confirms existing regulatory framework applies; no AI-specific rules forthcoming. Launched AI Lab (Jan 2025) and AI Live Testing programme. | Firms must self-assess AI systems against the 5 principles and demonstrate compliance through existing regulatory channels. | https://www.fca.org.uk/publication/corporate/ai-update.pdf | Yes |
| **FCA / PRA Joint AI Consultation** | FCA / PRA | **Not published as of March 2026.** Engagement ongoing via separate letters, roundtables, and AI Lab initiatives. | N/A — no formal joint consultation paper issued. Both regulators have communicated positions through individual channels. | Monitor for potential joint consultation in 2026-2027. | N/A | N/A |
| **UK Data (Use and Access) Act** | UK Parliament | Royal Assent received; key provisions effective from 19 June 2025 onwards | Will trigger reviews of data protection guidance relevant to automated decision-making, potentially updating the UK GDPR Art. 22 equivalent framework. | Monitor ICO guidance updates for implications on AI decision-making in financial services. | [unverified — referenced in ICO guidance; specific Act URL not independently confirmed] | No |

---

## 2. Key Findings

### 2.1 Universal Regulatory Principles Emerging Across Jurisdictions

- **No AI exemption.** Every jurisdiction studied has established — through guidance, enforcement, or statute — that existing consumer protection, fair lending, and prudential regulations apply fully to AI systems. There is no "advanced technology" carve-out. The CFPB's January 2025 formulation — "there is no 'advanced technology' exception to Federal consumer financial laws" — is the sharpest articulation, but the principle is universal.

- **Explainability is non-negotiable for credit-adjacent decisions.** ECOA/Reg B (US), GDPR Art. 22 (EU/UK), DPDP Act (India), and the EU AI Act all require that automated decisions affecting consumers include specific, understandable explanations. Black-box AI agents that participate in credit decisions, dispute resolution, or adverse actions are structurally non-compliant across all four jurisdictions.

- **Human escalation is a hard requirement, not a design choice.** The CFPB Section 1034(c) advisory opinion (US), FCA Consumer Duty (UK), GDPR Art. 22 right to human intervention (EU), and RBI Integrated Ombudsman Scheme (India) all mandate that consumers can reach a human decision-maker. Fully autonomous AI agents without human escalation pathways are non-compliant.

- **Bias testing is shifting from recommended to mandatory.** The CFPB Supervisory Highlights (2025) found institutions deploying AI/ML credit models without adequate fair lending testing. Colorado SB 24-205 requires impact assessments. The EU AI Act mandates data governance with bias mitigation. This is no longer optional — it is an examination finding.

### 2.2 US-Specific Findings

- **SR 11-7 is the binding constraint and the weakest link.** The 2011 framework's assumptions (static models, deterministic outputs, periodic review) are incompatible with agentic AI's continuous learning, probabilistic reasoning, and autonomous action. GARP's February 2025 analysis identifies this as the primary governance gap. Regulators have not updated SR 11-7 but are applying its principles with heightened expectations. Banks deploying customer-facing AI agents operate in a regulatory grey zone where the foundational governance framework does not map cleanly to the technology.

- **CFPB is the most aggressive enforcement actor.** Between the Section 1034(c) advisory (Oct 2023), Circular 2023-03 (Sept 2023), Supervisory Highlights Issue 38 (Jan 2025), and the August 2024 enforcement announcement, the CFPB has constructed a comprehensive enforcement framework for AI in consumer finance — all without new legislation. This is enforcement-by-guidance.

- **State-level regulation is fragmenting the compliance landscape.** Colorado SB 24-205 (effective June 2026), Illinois BIPA (biometric AI interactions), and NYC LL 144 (bias audits) each impose distinct obligations. Banks deploying customer-facing AI agents nationally face a patchwork of state requirements with no federal preemption. The Trump Administration has signaled interest in federal preemption but no legislation has been enacted as of March 2026.

- **Over 350 agentic AI risks identified in banking.** Deloitte's 2025 analysis catalogued risks spanning hallucination, data leakage, bias, off-policy behavior, and compound reasoning errors. Existing governance frameworks (SR 11-7, third-party risk management) were not designed to address autonomous agent behavior at machine speed.

### 2.3 India-Specific Findings

- **RBI FREE-AI is advisory, not binding — yet.** The August 2025 framework establishes principles and recommendations but has not been codified into enforceable circulars. However, RBI examination teams are likely to reference it in supervisory assessments. The gap between guidance and enforcement creates compliance uncertainty.

- **DPDP Act consent requirements are operationally intensive for AI agents.** Per-purpose consent, no bundling, revocability as easy as provision, and data localization requirements mean AI agents cannot simply inherit blanket consent. Every AI interaction that processes personal data for a new purpose requires fresh, specific consent — a significant UX and infrastructure challenge.

- **The Integrated Ombudsman Scheme 2026 creates material risk for AI-mediated complaints.** If an AI agent handles a customer complaint inadequately and the customer escalates to the Ombudsman, the bank faces potential awards of ₹30 lakh for consequential loss plus ₹3 lakh for mental anguish. Summary proceedings that are not bound by strict evidence rules further increase exposure. This is a strong incentive for human oversight of AI-handled complaints.

### 2.4 UK/EU-Specific Findings

- **The EU AI Act's August 2026 deadline is the most consequential near-term milestone.** High-risk AI requirements (Articles 6-49) become enforceable, with penalties up to €35M or 7% of global turnover. Any AI system evaluating creditworthiness or credit scoring is automatically high-risk. Banks deploying customer-facing AI agents in the EU have ~5 months to achieve compliance.

- **FCA Consumer Duty's 100% monitoring requirement is the most operationally demanding.** Moving from 2-5% sampling to full-interaction monitoring across all channels (voice, chat, email) for AI-mediated customer interactions requires real-time analytics infrastructure that most banks do not currently operate.

- **UK regulators are deliberately not creating AI-specific rules.** Both FCA and PRA rely on existing frameworks (Consumer Duty, SM&CR, operational resilience) to regulate AI. This is intentional — it provides flexibility but creates interpretive uncertainty. Firms must self-assess how existing obligations apply to AI, without prescriptive guidance.

- **GDPR Art. 22 is the oldest and most tested regulatory constraint on automated decision-making.** Its requirements (right to human intervention, right to contest, meaningful explanation of logic) were designed before modern AI but apply directly. The contractual-necessity exception is commonly used in banking but does not eliminate the safeguard requirements.

---

## 3. Customer-Facing AI vs. Back-Office AI: Regulatory Divergence

| Dimension | Customer-Facing AI | Back-Office AI |
|---|---|---|
| **Consumer disclosure** | Mandatory. Must disclose AI involvement in decisions (Colorado SB 24-205), disclose non-human interaction (CFPB Aug 2024), provide specific reasons for adverse actions (ECOA/Reg B). | Generally not required. Internal process optimization does not trigger consumer notification obligations. |
| **Explainability** | Hard requirement. ECOA, GDPR Art. 22, EU AI Act, DPDP Act all require meaningful explanation of automated decisions affecting individuals. | Desirable but not legally mandated for most use cases. Model risk management (SR 11-7) requires documentation but not consumer-facing explanation. |
| **Human escalation** | Mandatory across all jurisdictions. CFPB § 1034(c), FCA Consumer Duty, GDPR Art. 22, RBI IOS 2026 all require access to human decision-makers. | Not required. Back-office AI can operate with periodic human review rather than on-demand escalation. |
| **Bias testing** | Increasingly mandatory. CFPB Supervisory Highlights (2025) treats absence of fair lending testing as an examination finding. EU AI Act requires bias mitigation for high-risk systems. | Recommended under SR 11-7 but enforcement focus is lower. Back-office models not directly affecting consumers face less scrutiny. |
| **Data consent** | Heightened requirements. DPDP Act requires per-purpose consent for customer data processing. GDPR requires lawful basis for each processing activity. | Generally covered by employment contracts (for employee data) or legitimate interest basis. Lower consent burden. |
| **Penalties for failure** | Severe and growing. CFPB enforcement actions, EU AI Act fines (€35M / 7% turnover), DPDP Act (₹250 crore), Colorado ($20K/violation). Consumer harm creates reputational and litigation risk. | Model risk management failures can lead to supervisory actions but typically do not trigger consumer-facing penalties or class-action exposure. |
| **Regulatory classification** | Likely "high-risk" under EU AI Act (Annex III) if involved in credit scoring, insurance, or consequential decisions. | May qualify for derogation under EU AI Act if performing narrow procedural tasks, improving prior human activity, or performing preparatory tasks. |

**Net assessment:** Customer-facing AI agents operate in a materially more restrictive regulatory environment than back-office AI. The combination of consumer disclosure, explainability, human escalation, bias testing, and enhanced data consent requirements creates a compliance surface that back-office AI simply does not face. This asymmetry should drive architectural decisions: customer-facing AI agents require purpose-built compliance infrastructure that cannot be reused from back-office AI deployments.

---

## 4. Gaps and Unresolved Questions

### 4.1 Regulatory Gaps

1. **No jurisdiction has AI-agent-specific regulation.** All current frameworks were designed for traditional software, static models, or narrow AI. Agentic AI — systems that reason, plan, and take autonomous action — falls between existing categories. SR 11-7's "model" definition, the EU AI Act's "AI system" definition, and the CFPB's chatbot guidance were not written with autonomous agents in mind.

2. **Accountability attribution for autonomous agent actions is undefined.** When an AI agent autonomously resolves a dispute incorrectly or provides misleading information, existing frameworks place liability on the deploying institution — but the governance mechanisms for preventing and detecting such failures are not specified for autonomous systems.

3. **Cross-border regulatory arbitrage is unaddressed.** A bank deploying a single AI agent platform across US, EU, India, and UK operations faces conflicting requirements (e.g., GDPR Art. 22 right to explanation vs. DPDP Act per-purpose consent vs. CFPB adverse action specificity). No mutual recognition or harmonization framework exists.

4. **Real-time validation of continuously-learning agents has no regulatory standard.** SR 11-7 assumes periodic validation; the EU AI Act requires accuracy and robustness but does not specify validation frequency for adaptive systems. How often must a customer-facing AI agent be re-validated? No regulator has answered this.

5. **Multi-agent system governance is entirely uncharted.** If a customer-facing agent delegates to a back-office agent which delegates to a third-party API, the regulatory treatment of this chain is undefined. Which agent's decision triggers adverse action notice requirements? Which entity bears liability?

### 4.2 Questions Requiring Manual Verification

1. **CFPB August 2024 chatbot enforcement announcement:** No standalone regulatory text URL identified. The announcement was covered by ABA Banking Journal and Venable LLP but the CFPB rulemaking status needs confirmation. Has this progressed to a proposed rule under the current administration?

2. **IRDAI fraud management framework circular URL:** Referenced in industry analyses but the original IRDAI circular URL was not independently verified. Needs manual confirmation from irdai.gov.in.

3. **UK Data (Use and Access) Act:** Royal Assent confirmed but specific provisions affecting AI decision-making in financial services need detailed review once ICO updates its guidance.

4. **Trump Administration federal preemption of state AI laws:** Ballard Spahr (March 2026) references federal-state tension on AI regulation. Status of any preemption legislation or executive order needs confirmation.

5. **CFPB operational status under current administration:** Multiple reports suggest CFPB enforcement priorities may have shifted. The August 2024 chatbot enforcement agenda and January 2025 Supervisory Highlights were issued under the prior administration. Current enforcement posture needs verification.

---

## 5. Raw Notes and Excerpts

### 5.1 SR 11-7 and Agentic AI (GARP, February 2025)

> "SR 11-7 defines models as systems processing input data to produce quantitative estimates, but agentic AI agents continuously learn, adapt, and initiate autonomous actions in real-time, exceeding this narrow definition."

> "Traditional software treats deterministic logic, while AI agents are probabilistic and sensitive to data, context, and interaction changes."

> "The framework relies on periodic review cycles and bounded use cases, but agentic systems can evolve materially between validation cycles and propagate risks at speeds that challenge traditional controls."

Source: GARP Risk Intelligence, "SR 11-7 in the Age of Agentic AI: Where the Framework Holds – and Where It Strains" (February 2025). https://www.garp.org/risk-intelligence/operational/sr-11-7-age-agentic-ai-260227

### 5.2 Deloitte: Agentic AI Risks in Banking (2025)

> "Over 350 agentic AI risks have been identified in banking, including hallucinations, data leakage, bias, and off-policy behavior — many existing frameworks don't address these fully."

> "Human-in-the-loop designs may be insufficient or counterproductive for agentic workflows where human intervention at every decision point defeats efficiency gains."

Source: Deloitte Insights, "Agentic AI risks in banking" (2025). https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-risks-banking.html

### 5.3 CFPB Director Rohit Chopra on AI Adverse Action (2023)

> "Creditors must be able to specifically explain their reasons for denial. There is no special exemption for artificial intelligence."

Source: CFPB Press Release, "CFPB Issues Guidance on Credit Denials by Lenders Using Artificial Intelligence." https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/

### 5.4 CFPB Supervisory Highlights Issue 38 (January 2025)

> "There is no 'advanced technology' exception to Federal consumer financial laws. Financial institutions are under an obligation to comply with these laws when using advanced computational methods, including artificial intelligence and machine learning (AI/ML), the same as if they used more traditional methods."

Source: CFPB Supervisory Highlights, Advanced Technologies Special Edition, Issue 38 (Winter 2025).

### 5.5 RBI FREE-AI: AI Adoption Statistics (August 2025)

> "20.8% of surveyed entities (banks, NBFCs, fintechs) currently deploy AI systems, primarily in customer support (15.6%), credit underwriting (13.7%), sales and marketing (11.8%), and cybersecurity (10.6%). 67% of entities expressed interest in exploring AI use cases."

Source: RBI FREE-AI Committee Report. https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=1306

### 5.6 PRA / Bank of England: AI Adoption Survey (November 2024)

> "75% of firms already use AI, with 10% planning adoption over the next three years. Foundation models represent 17% of AI use cases. 33% of AI use cases are third-party implementations (up from 17% in 2022). Only 2% of use cases have fully autonomous decision-making. 46% of firms have only partial understanding of their AI systems."

Source: Bank of England, "Artificial intelligence in UK financial services — 2024." https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024

### 5.7 Ballard Spahr: Agentic AI in Consumer Financial Services (March 2026)

> "In complex financial product markets (credit cards, mortgages, insurance), AI-powered personalization may harm consumers who misjudge product value — for example, algorithms setting prices just below a consumer's mistaken valuation."

> Key concerns: accountability, fairness, model risk management, governance, UDAAP compliance, consumer disclosure, fair lending, and liability attribution.

Source: Ballard Spahr, "Agentic AI in Consumer Financial Services: Opportunities, Risks, and Emerging Legal Frameworks" (March 2026). https://www.ballardspahr.com/insights/blogs/2026/03/podcast-agentic-ai-in-consumer-financial-services

### 5.8 EU AI Act — Annex III, Paragraph 5 (Credit Scoring)

> AI systems "intended to be used to evaluate the creditworthiness of natural persons or establish their credit score" are classified as high-risk. Exception for fraud detection. **Any AI system performing profiling of natural persons in this context remains always high-risk** — no derogation available.

Source: EU AI Act, Annex III. https://artificialintelligenceact.eu/annex/3/

### 5.9 FCA Consumer Duty — Monitoring Shift

> "Firms must monitor all customer interactions (100% coverage across voice, chat, email, etc.) to track performance against Consumer Duty outcomes in real-time. Traditional sampling methods (2-5%) are no longer sufficient."

Source: Sedric AI / FCA Consumer Duty analysis. https://www.sedric.ai/uk-fca-compliance-resources/consumer-duty-ai-tools-how-uk-firms-can-meet-fca-expectations-with-confidence

### 5.10 India DPDP Act — Consent Granularity for Banking

> "Banks must collect explicit, separate consent for different KYC uses — including credit bureau sharing, AML/CFT screening, and financial assessment — rather than bundling these with general terms and conditions."

> "Financial institutions must store all customer and financial data on India-based servers only; backup and disaster recovery data cannot be stored outside India without explicit consent."

Source: DPDPA.com compliance analysis. https://www.dpdpa.com/blogs/dpdpa_banks_nbfcs_financial_data_protection.html

---

## 6. Source Index

| # | Source | Type | URL |
|---|---|---|---|
| 1 | Federal Reserve SR 11-7 | Official regulation | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm |
| 2 | Federal Reserve et al. RFI on AI (2021) | Official regulatory document | https://www.federalreserve.gov/newsevents/pressreleases/bcreg20210329a.htm |
| 3 | CFPB Circular 2023-03 | Official regulatory circular | https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ |
| 4 | CFPB Section 1034(c) Advisory Opinion | Official regulatory guidance | https://files.consumerfinance.gov/f/documents/cfpb-1034c-advisory-opinion-2023_10.pdf |
| 5 | CFPB Chatbot Issue Spotlight | Official report | https://files.consumerfinance.gov/f/documents/cfpb_chatbot-issue-spotlight_2023-06.pdf |
| 6 | CFPB Supervisory Highlights Issue 38 | Official supervisory guidance | https://files.consumerfinance.gov/f/documents/cfpb_supervisory-highlights-advanced-technologies_2025-01.pdf |
| 7 | ECOA / Regulation B (12 CFR 1002) | Official regulation | https://www.consumerfinance.gov/rules-policy/regulations/1002/ |
| 8 | FFIEC Authentication Guidance | Official regulatory guidance | https://www.consumerfinance.gov/about-us/newsroom/ffiec-issues-guidance-on-authentication-and-access-to-financial-institution-services-and-systems/ |
| 9 | Colorado SB 24-205 | Official legislation | https://leg.colorado.gov/bills/sb24-205 |
| 10 | EU AI Act (Reg. 2024/1689) | Official legislation | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 |
| 11 | GDPR Article 22 | Official legislation | https://gdpr.eu/article-22-automated-individual-decision-making/ |
| 12 | FCA Consumer Duty (PRIN 2A) | Official handbook | https://www.handbook.fca.org.uk/handbook/PRIN/2A.htm |
| 13 | PRA / BoE AI Letter (April 2024) | Official regulatory letter | https://www.bankofengland.co.uk/prudential-regulation/letter/2024/artificial-intelligence-and-machine-learning-letter |
| 14 | FCA AI Update (April 2024) | Official publication | https://www.fca.org.uk/publication/corporate/ai-update.pdf |
| 15 | RBI FREE-AI Framework (August 2025) | Official report | https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=1306 |
| 16 | India DPDP Act 2023 | Official legislation | https://www.meity.gov.in/static/uploads/2024/06/2a5ef610a85e2b05965a5a6bbd7e4c25.pdf |
| 17 | RBI Master Direction — Digital Payment Security Controls | Official regulation | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12896 |
| 18 | RBI Integrated Ombudsman Scheme 2026 | Official regulation | https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62052 |
| 19 | SEBI AI/ML Consultation Paper (June 2025) | Official consultation | https://www.sebi.gov.in/reports-and-statistics/reports/jun-2025/consultation-paper-on-guidelines-for-responsible-usage-of-ai-ml-in-indian-securities-markets_94687.html |
| 20 | BoE AI in UK Financial Services (2024) | Official report | https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024 |
| 21 | GARP — SR 11-7 and Agentic AI (Feb 2025) | Industry analysis | https://www.garp.org/risk-intelligence/operational/sr-11-7-age-agentic-ai-260227 |
| 22 | Deloitte — Agentic AI Risks in Banking (2025) | Industry analysis | https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-risks-banking.html |
| 23 | Ballard Spahr — Agentic AI in Consumer Finance (Mar 2026) | Law firm analysis | https://www.ballardspahr.com/insights/blogs/2026/03/podcast-agentic-ai-in-consumer-financial-services |
| 24 | Skadden — CFPB Adverse Action and AI (2024) | Law firm analysis | https://www.skadden.com/insights/publications/2024/02/cfpb-applies-adverse-action-notification-requirement-to-artificial-intelligence-models |
| 25 | EU AI Act Annex III | Official legislation (annotated) | https://artificialintelligenceact.eu/annex/3/ |
