---
name: "Agentic Banking Opportunity Analysis"
overview: "McKinsey-grade two-part opportunity analysis (Part I: independent analyst assessment, Part II: Zeta strategic advisory) for the Agentic Banking engagement area. Replaces the current CIO-facing capability catalogue."
todos:
  - id: "p1b1"
    content: "Phase 1 Batch 1 — Research Streams 1–4 (market sizing, regulatory landscape, competitive landscape, structural shifts). Raw output saved to _research/agentic-banking/s1–s4 files."
    status: "pending"
  - id: "p1b2"
    content: "Phase 1 Batch 2 — Research Streams 5–6 (SOHO/SME business banking AI, AI agent governance and operational model). Raw output saved to _research/agentic-banking/s5–s6 files."
    status: "pending"
  - id: "p2-synthesis"
    content: "Phase 2 — Synthesis & gap-fill: cross-reference streams, rate evidence quality, verify URLs, assemble target universe, map Right to Play / Right to Win. Save synthesis-notes.md and unverified-claims.md."
    status: "pending"
  - id: "p3-market"
    content: "Phase 3 Part I §1 — Market section. Constructed TAM from adjacent AI-in-banking categories."
    status: "pending"
  - id: "p3-history"
    content: "Phase 3 Part I §2 — How We Got Here. From chatbots to agents: three generations of AI in banking."
    status: "pending"
  - id: "p3-shifts"
    content: "Phase 3 Part I §3 — Structural Shifts (6–8 shifts). Each shift evidenced with data, regulatory citations, bank-tier and geographic analysis."
    status: "pending"
  - id: "p3-engagements"
    content: "Phase 3 Part I §4 — Engagement Landscape. Concrete engagement types mapped to bank tier and structural shift."
    status: "pending"
  - id: "p3-competitive"
    content: "Phase 3 Part I §5 — Competitive Landscape. Conversational AI, banking AI platforms, agent platforms, core vendors."
    status: "pending"
  - id: "p3-targets"
    content: "Phase 3 Part I §6 — Target Universe. Named institutions with cited evidence across USA, India, UK/EU."
    status: "pending"
  - id: "p3-position"
    content: "Phase 3 Part II §7 — Zeta's Position. Evolution Fabric, Seer, Quark, CAF, Trust Fabric mapped honestly."
    status: "pending"
  - id: "p3-wheretoplay"
    content: "Phase 3 Part II §8 — Where to Play. Segments, geographies, bank tiers. Explicit deferrals."
    status: "pending"
  - id: "p3-risks"
    content: "Phase 3 Part II §9 — Risks and Gaps. Prerequisites, window risks, capability gaps."
    status: "pending"
  - id: "p3-actions"
    content: "Phase 3 Part II §10 — Recommended Actions. Near-term and medium-term, prioritized."
    status: "pending"
  - id: "p3-execsummary"
    content: "Phase 3 §11 — Executive Summary. Written last, covers both Part I and Part II."
    status: "pending"
  - id: "p4-partI"
    content: "Phase 4 — Part I review: citations verified, no Zeta references, no commercial voice, segment/geographic specificity confirmed, target universe evidenced."
    status: "pending"
  - id: "p4-partII"
    content: "Phase 4 — Part II review: recommendations trace to Part I evidence, gaps stated honestly, product references verified."
    status: "pending"
  - id: "p4-editorial"
    content: "Phase 4 — Editorial rigor review (Part I only): all 8 tests from editorial-rigor-review skill."
    status: "pending"
isProject: true
---

# Agentic Banking — Opportunity Analysis & Strategic Advisory Plan

**Engagement Area:** Agentic Banking
**Output:** `org-8.0/what-we-sell/strategy/engagement-areas/agentic-banking.md`
**Target length:** 5,500–7,500 words (two-part structure)
**Current state:** 112-line CIO-facing capability catalogue covering consumer, business (SOHO/SME), and family banking agent capabilities. Must be fully replaced.

**Scope constraint:** "Business Banking" in this engagement area means **SOHO and SME only** — sole proprietors, micro-enterprises, and small-to-medium enterprises. It does NOT include corporate banking, institutional banking, treasury services, or large-enterprise relationship management. The analysis, competitive landscape, and recommendations must respect this boundary throughout.

---

## 1. Model Recommendation

**Orchestration:** Default model (most capable). The orchestrator must manage six parallel research streams, construct a TAM from adjacent categories (no established "agentic banking" market exists), enforce the analyst/advisor voice boundary, and apply all eight editorial rigor tests. This requires sustained reasoning across sparse evidence and a large document.

**Research sub-agents:** Default model for all six streams. Rationale:

- **Analyst coverage for "agentic banking" is thin.** No analyst firm publishes a market size for "AI agents resolving banking customer situations." The category sits at the intersection of conversational AI in banking, contact center AI, enterprise AI agent platforms, and banking operations automation — but none of these adjacent categories maps cleanly to the engagement area's scope.
- **Streams 1 and 3** (market sizing, competitive landscape) require the model to **construct** a TAM and competitive map from adjacent categories, not merely synthesize existing reports. This is reasoning-intensive.
- **Streams 4 and 5** (structural shifts, SOHO/SME business banking) have **thin analyst coverage** and must emphasize primary evidence: vendor product launches, bank earnings calls, regulatory proposals, AI deployment case studies, and standards body publications (A2A protocol, MCP). The model must reason across sparse primary sources.
- **Stream 6** (AI agent governance) overlaps with research already conducted for Cloud & Platform Operations (`_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md`, `s5-aiops-agentic-operations.md`) and Digital Identity & Trust (`_research/digital-identity-and-trust/s5-ai-agent-identity.md`). The model must cross-reference rather than re-research — but must also distinguish governance requirements for **customer-facing** AI agents (which interact directly with bank customers) from those for **back-office** AI agents (covered by the Agentic Operations engagement area) and **infrastructure** agents (covered by Cloud & Platform Operations).

**Impact of thin coverage on research approach:** Research streams must emphasize primary evidence sources — bank press releases, vendor product launches (Salesforce Agentforce, Google CCAI, Amazon Connect AI, Kasisto, Personetics), regulatory guidance (OCC/FDIC/Fed joint statement on AI, CFPB guidance, EU AI Act Annex III), standards body publications (A2A protocol, MCP), and bank earnings call transcripts — rather than relying on analyst market sizing that does not exist for this specific category. Where market sizing must be constructed from adjacent categories, the construction methodology must be transparent and the resulting figures flagged as estimates.

---

## 2. Phase 1: Parallel Research (6 Streams)

### Stream 1: Market Sizing and Revenue Pools — Constructed TAM

**What to gather:**

"Agentic banking" does not exist as a separately reported analyst category. The vendor-addressable TAM must be constructed by triangulating across adjacent categories that collectively bound the opportunity:

- **Conversational AI in banking / Contact center AI** — what banks spend on AI-powered customer interaction platforms (chatbots, virtual assistants, voice AI, agent-assist tools). This is the closest existing category but undercounts the scope: it captures the interaction layer but not the operational resolution layer.
- **AI in banking operations / Banking automation** — what banks spend on AI-driven automation of customer-facing operations (dispute resolution, application processing, servicing workflows). Overlaps with BPM and case management modernization.
- **Enterprise AI agent platforms** — the emerging platform category for building, deploying, and governing AI agents in enterprise settings. Banking's share of this category. Cross-reference with existing research: `market-study/agentic-systems-development-platforms/background/agentic-systems-platform-tam.md` (projects global platform TAM at USD 7–12B conservative / 16–25B aggressive by 2030).
- **Banking customer servicing technology** — what banks spend on customer servicing infrastructure (case management, CRM, workflow, knowledge management) that AI agents would partially or fully replace.
- **Total banking AI spending** — the aggregate AI investment by banks, from which the share attributable to customer-facing agentic use cases can be estimated.

For each category:
- Total market size (2025, 2030 projection, CAGR)
- Banking vertical share (percentage of total)
- Breakdown by sub-segment: consumer banking, business banking (SOHO/SME only), wealth/family banking
- Breakdown by geography: USA, India, UK/EU
- Breakdown by bank tier where available (Tier 1, Tier 2, Tier 3)
- Build vs. buy patterns by bank tier

**Sources to target:**

- Gartner (Magic Quadrant for Enterprise Conversational AI Platforms; Hype Cycle for AI in Banking; CIO Survey AI spending data)
- Forrester (Wave for Conversational AI in Customer Service; AI in Financial Services reports)
- IDC (AI in Banking spending forecasts; Conversational AI market)
- MarketsandMarkets, Grand View Research, Mordor Intelligence (conversational AI, AI in BFSI market reports)
- McKinsey (Global Banking Annual Review — AI impact on banking operations; "AI-powered banking operations" estimates)
- BCG (AI in financial services spending data)
- Celent (IT spending in banking — AI allocation; "Dimensions" series on banking IT priorities)
- Cornerstone Advisors ("What's Going On in Banking" survey — AI adoption data by bank tier)
- Juniper Research (AI in banking, chatbot savings estimates)
- Bank IT spending proxies: JPMorgan tech budget ($20B), Capital One AI investment, BoA technology spending disclosures
- Cross-reference: `market-study/agentic-systems-development-platforms/background/agentic-systems-platform-tam.md`

**Geographic scope:** Global with USA, India, UK/EU breakdowns.

**How data will be used:** Part I, Section 1 (Market). Establishes the prize. The constructed TAM must be transparent about its methodology — the reader should understand that this is a synthesized estimate from adjacent categories, not a single analyst figure. The construction itself is an analytical contribution.

**Citation requirement:** Every data point must include a navigable URL or full bibliographic detail. When constructing a TAM from adjacent categories, cite each input category's source independently and make the arithmetic transparent. Flag all estimates as `[constructed estimate — see methodology]`.

---

### Stream 2: Regulatory Landscape — AI Agents in Customer-Facing Banking

**What to gather:**

Specific regulations that govern or constrain AI agent deployment in **customer-facing** banking operations — with compliance deadlines, enforcement actions, and infrastructure implications. This stream focuses on the regulatory environment for AI that interacts directly with bank customers (dispute resolution, application processing, servicing, advisory), which is subject to consumer protection, fair lending, and explainability requirements that back-office AI is not.

**Regulations to cover by geography:**

**USA:**

- OCC/FDIC/Federal Reserve joint statement on AI in financial services — principles for AI risk management, third-party risk, model risk
- CFPB guidance on AI in consumer lending and servicing — adverse action notice requirements, fair lending implications when AI makes or influences credit decisions, consumer complaint data on AI interactions
- CFPB enforcement actions related to chatbots / automated customer service (if any)
- SR 11-7 (Model Risk Management) — applicability to customer-facing AI agents. Cross-reference: `_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md` documents SR 11-7 strain under agentic AI
- ECOA / Regulation B — adverse action requirements when AI agents participate in credit decisions or dispute resolution
- FFIEC guidance on authentication and access — implications for AI agent-mediated customer interactions
- State-level AI regulation: Colorado AI Act (SB 24-205, effective 2026) — high-risk AI systems in insurance/lending; Illinois BIPA implications for biometric AI interactions; NYC Local Law 144 (automated employment decision tools — precedent for banking AI)

**India:**

- RBI guidance on AI/ML in banking — customer-facing applications, data privacy, model governance
- RBI Master Direction on Digital Payment Security Controls — implications for AI-mediated payment operations
- DPDP Act 2023 — consent and data protection requirements when AI agents process customer data
- SEBI and IRDAI AI guidance (where applicable to banking-adjacent financial services)
- RBI customer grievance redressal framework — implications when AI agents handle complaints

**UK/EU:**

- EU AI Act — Annex III high-risk classification for AI in financial services (creditworthiness assessment, credit scoring, insurance). Transparency, human oversight, and accountability requirements. Specific attention to whether customer-facing banking AI agents fall under "high-risk" classification
- FCA Consumer Duty (July 2023) — obligations when AI agents interact with retail banking customers (good outcomes, fair value, consumer understanding, consumer support). FCA has signaled that firms using AI for customer interactions must demonstrate compliance with Consumer Duty
- PRA / BoE approach to AI supervision — principles-based, outcomes-focused. Cross-reference existing research: `_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md` documents PRA CRO roundtable positions
- FCA / PRA joint consultation on AI in financial services (if published)
- GDPR Art. 22 — automated individual decision-making, right to explanation when AI agents make consequential decisions

**Sources to target:**

- Official regulatory texts (Federal Register, OCC bulletins, CFPB guidance, EUR-Lex, FCA handbook, RBI circulars)
- OCC/FDIC/Fed interagency guidance and FAQ documents
- CFPB complaint database — AI/chatbot-related consumer complaints
- Law firm analyses (Davis Polk, Sullivan & Cromwell, Linklaters, Clifford Chance)
- Regulatory conference proceedings (ABA AI risk conference, FCA TechSprint outputs)
- Cross-reference: `_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md` (regulatory positions on autonomous AI — extensive coverage already exists; adapt for customer-facing context)
- Cross-reference: `_research/digital-identity-and-trust/s2-regulatory-landscape.md` (GDPR Art. 22, EU AI Act requirements)

**Geographic scope:** USA, India, UK/EU.

**How data will be used:** Part I, Sections 2 (How We Got Here) and 3 (Structural Shifts). Regulations forcing banks to invest in governed AI agent infrastructure rather than deploying ungoverned chatbots. The regulatory environment for customer-facing AI is stricter than for back-office AI — this distinction is central to the analysis.

**Citation requirement:** Every regulation cited must link to the official text or a specific regulatory guidance document. Law firm summaries are acceptable as secondary sources but must reference the underlying regulation.

---

### Stream 3: Competitive Landscape

**What to gather:**

For each competitor category, identify the key players and for each: positioning, target market (bank tier, geography), revenue model, product scope (chatbot vs. copilot vs. autonomous agent), strengths, weaknesses, and vulnerabilities.

**Categories and key players to map:**

| Category | Players to Research |
|---|---|
| **Conversational AI for banking** | Kasisto (KAI — banking-specific), Personetics (financial data-driven engagement), Clinc (acquired by U.S. Bank), Avaamo (enterprise conversational AI), Haptik (India), Yellow.ai (India) |
| **Contact center / CX AI platforms** | Google Contact Center AI (CCAI), Amazon Connect + Q in Connect, NICE CXone SmartAssist, Genesys Cloud AI, Five9 Intelligent CX, Verint |
| **Enterprise AI agent platforms** | Salesforce Agentforce (financial services focus), Microsoft Copilot Studio + Azure AI Agent Service, AWS Bedrock Agents, Google Vertex AI Agent Builder, ServiceNow AI Agents |
| **BPM / Case management + AI** | Pegasystems (Customer Decision Hub, banking-specific AI), Appian (AI Process Platform), Newgen Software (banking BPM + AI) |
| **Core banking vendors with AI** | Temenos (Temenos AI), FIS (AI capabilities), Fiserv (AI modules), Backbase (AI-powered engagement banking), Thought Machine (limited AI), Mambu (limited AI) |
| **Bank-built solutions** | Bank of America (Erica — 2B+ interactions), JPMorgan (LLM Suite, internal AI), Capital One (ML-driven operations), Wells Fargo (Fargo virtual assistant), HDFC Bank (Eva chatbot, India), DBS Bank (DBS Joy, Singapore) |

**For each player, capture:**

- Annual revenue or ARR (where public or estimable)
- Banking-specific customer count or deployment data
- Geographic focus
- Capability level: chatbot (FAQ/navigation) → copilot (human-assist) → agent (autonomous resolution within guardrails). Most current deployments are chatbots or copilots. Identify which vendors are genuinely shipping autonomous resolution capabilities.
- Whether the platform provides the **operational model** (domain context, governance, audit) or only the **AI interaction layer** (conversation management, NLU/NLG). This distinction is the central competitive insight.
- Consumer banking vs. business banking (SOHO/SME) coverage
- Recent AI agent product launches (2024–2026)
- Vulnerabilities: where the platform lacks domain knowledge, governance, audit, or operational model depth

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled investment in AI agents for customer-facing banking operations — through earnings calls, press releases, RFP announcements, analyst commentary, vendor partnership disclosures, or conference presentations. For each: bank name, tier, geography, the signal, the source, and a navigable URL.

**Evidence to seek for bank signals:**

- Earnings call transcripts: search for "AI agent," "virtual assistant," "customer servicing AI," "agentic," "dispute resolution AI," "intelligent automation," "conversational banking"
- Vendor partnership announcements with banks (Kasisto + specific bank, Salesforce Agentforce + bank deployment, Pega + bank)
- Bank press releases on AI strategy / AI labs / AI deployment
- Conference presentations (Money 20/20, Finovate, BAI, American Banker conferences)
- Analyst commentary (Celent, Aite-Novarica/Datos Insights, Cornerstone Advisors) on bank AI adoption

**Sources to target:**

- Gartner (Magic Quadrant for Enterprise Conversational AI Platforms; Market Guide for AI in Banking)
- Forrester (Wave for Conversational AI; AI in Financial Services)
- SEC filings (10-K/10-Q) for public competitors: Salesforce, Pega, NICE, Five9, Verint
- Earnings call transcripts (Seeking Alpha, Motley Fool Transcripts) — both vendor and bank
- Vendor press releases and product announcements
- Bank technology reports (JPMorgan annual report tech section, Capital One tech blog, BoA investor day presentations)
- Crunchbase / PitchBook (funding rounds, M&A in banking AI)
- Cross-reference: `market-study/agentic-systems-development-platforms/background/players-and-products.md` (comprehensive vendor catalog already exists — adapt for banking-specific context)
- Cross-reference: `market-study/agentic-systems-development-platforms/background/enterprise-ai-agent-platform-backdrop.md` (strategic gap analysis)

**Geographic scope:** Global, with emphasis on USA, India, UK vendors.

**How data will be used:** Part I, Section 5 (Competitive Landscape) and Part II, Section 7 (Zeta's Position — relative to competitors).

**Citation requirement:** Every competitive claim must be sourced. Revenue figures from SEC filings or credible analyst estimates. Product scope claims from vendor documentation. Bank deployment claims from press releases or earnings transcripts. Distinguish between vendor marketing claims and verified production deployments.

---

### Stream 4: Structural Shifts and Bank Modernization Activity

**What to gather:**

Evidence for 6–8 structural shifts reshaping how banks deploy AI agents in customer-facing operations. Each shift must be evidenced with data, regulatory citations, competitive activity, and bank-tier analysis.

**Candidate structural shifts to investigate:**

1. **AI moving from chatbot supplement to operational resolution.** The first generation of banking AI was FAQ chatbots. The second was copilots assisting human agents. The third — now emerging — is AI agents that autonomously resolve customer situations (disputes, inquiries, applications) within governed boundaries. Evidence: vendor product launches (Salesforce Agentforce, NICE Enlighten Autopilot, Pega GenAI), bank deployment announcements, customer satisfaction data comparing chatbot vs. agent resolution, Gartner's projection that by 2027 25% of customer service interactions will be resolved by AI agents without human involvement.

2. **Experienced banking staff becoming scarce and expensive.** Dispute investigators, relationship managers, compliance specialists, and underwriters are aging out of the workforce faster than they can be replaced. The knowledge they carry — how disputes are resolved, how exceptions are handled, how regulations are interpreted — is not documented. Evidence: Bureau of Labor Statistics data on banking employment trends, American Bankers Association workforce surveys, bank earnings call commentary on headcount pressure, average age of banking operations staff, time-to-fill for specialized banking roles.

3. **Project-by-project AI failing to scale beyond the pilot.** Most banks have deployed AI in isolated experiments — a chatbot for FAQs, a document classifier for compliance, a recommendation engine for cross-sell. Each project reverse-engineers its operational context. The 50th AI project costs as much as the 1st because nothing compounds. Evidence: McKinsey / BCG surveys on AI pilot-to-production rates in banking (typically <20%), Gartner data on AI project failure rates, bank CIO commentary on "pilot purgatory," specific bank examples where AI investment has not produced enterprise-level results.

4. **Consumer protection regulators forcing governed AI deployment.** CFPB scrutiny of AI in lending and servicing, EU AI Act high-risk classification for financial services AI, FCA Consumer Duty requiring firms to demonstrate good customer outcomes from AI interactions. Banks can no longer deploy ungoverned chatbots — they need AI agents with accountability, explainability, and audit trails. Evidence: CFPB enforcement actions, EU AI Act text and timelines, FCA Consumer Duty guidance on AI, bank compliance investment data.

5. **Business banking (SOHO/SME) as the most underserved AI segment.** Consumer banking has received the majority of banking AI investment (BoA Erica, chatbots, mobile features). Corporate banking has relationship-driven AI (Bloomberg Terminal AI, institutional analytics). SOHO and SME banking — where relationships are deeper than consumer but budgets are smaller than corporate — has received minimal AI investment. These customers need AI that understands multi-product relationships, cash flow patterns, and business lifecycle — not consumer-grade chatbots. Evidence: SME banking satisfaction surveys, SME banking technology investment data, fintech challengers targeting SME banking (Brex, Mercury, Relay), bank commentary on the SME opportunity.

6. **Domain knowledge becoming the bottleneck — not AI capability.** Foundation model capability has outpaced the banking industry's ability to deploy it. The constraint is not whether an LLM can reason about a dispute — it is whether the bank has an explicit model of how disputes work, what evidence is needed, what policies apply, and who has authority to resolve them. Without this operational model, each AI agent deployment requires months of domain engineering. Evidence: AI integration cost data, time-to-deploy for banking AI projects, comparison of AI capability benchmarks vs. banking AI deployment rates, commentary from banking AI vendors on the "last mile" problem.

7. **Multi-channel continuity becoming table stakes.** Customers interact with their bank across mobile, web, chat, voice, branch, and API channels — often within a single issue resolution journey. AI agents that cannot maintain context across channels produce worse outcomes than no AI at all. Evidence: customer expectation surveys, cross-channel interaction data, bank investment in omnichannel platforms, vendor product announcements on cross-channel AI.

8. **Family and household banking emerging as a distinct AI domain.** Multi-member accounts, delegated authority, generational financial interactions (parents managing children's accounts, adult children managing elderly parents' finances), and household-level financial planning create operational complexity that neither consumer nor business banking AI addresses. Evidence: household banking product launches, multi-member account growth, fintech challengers in family banking (Greenlight, GoHenry, FamZoo), demographic data on multi-generational financial management needs.

**For each shift, gather:**

- 3–5 data points with sources and URLs
- Regulatory citations that create or accelerate the shift
- Competitive activity (vendors capitalizing on the shift)
- Analysis by bank tier (how does this shift affect Tier 1 vs. Tier 2 vs. Tier 3 differently?)
- Geographic variation (USA vs. India vs. UK/EU)

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled investment in AI agents for customer-facing banking operations. For each: bank name, tier, geography, the signal, the source, and a navigable URL.

**Sources to target:**

- McKinsey Global Banking Annual Review; BCG Global Retail Banking reports
- Gartner Hype Cycle for AI in Banking; Gartner predictions on AI in customer service
- Bureau of Labor Statistics (banking employment data)
- American Bankers Association (workforce surveys, technology adoption surveys)
- CFPB Consumer Complaint Database (AI-related complaints)
- Bank earnings call transcripts (search for "AI agent," "virtual assistant," "Erica," "customer servicing," "dispute resolution," "agentic," "copilot")
- Bank annual reports and investor day presentations (technology sections)
- Vendor partnership announcements
- Conference proceedings (Money 20/20, Finovate, BAI Banking Strategies)
- Cross-reference: `_research/cloud-and-platform-operations/s5-aiops-agentic-operations.md` and `gap-fill-agentic-ops-banking.md` for bank deployment evidence that may include customer-facing AI context

**Geographic scope:** USA, India, UK/EU.

**How data will be used:** Part I, Sections 2 (How We Got Here), 3 (Structural Shifts — the core), 4 (Engagement Landscape), and 6 (Target Universe).

**Citation requirement:** Every structural shift claim must be grounded in at least three independent data points with navigable URLs. Assertions without evidence are flagged or dropped.

---

### Stream 5: SOHO/SME Business Banking AI Opportunity

**Why a separate stream:** The user's scope constraint requires that "Business Banking" means SOHO and SME only — not corporate banking. This segment has distinct dynamics that generic "business banking AI" research will miss. SOHO/SME banking is structurally different from both consumer banking (deeper relationships, more complex products, multi-entity structures) and corporate banking (smaller deal sizes, higher volume, less bespoke service). AI agent opportunity in this segment must be researched independently.

**Scope boundary — what is included and excluded:**

| Included (SOHO/SME) | Excluded (Corporate) |
|---|---|
| Sole proprietors, freelancers, gig economy | Large corporates ($250M+ revenue) |
| Micro-enterprises (1–9 employees) | Institutional banking and treasury |
| Small enterprises (10–49 employees) | Correspondent banking |
| Medium enterprises (50–249 employees) | Trade finance for multinationals |
| Cash management for small business | Complex treasury and FX operations |
| SME lending and credit lines | Syndicated lending |
| Business account servicing | Custody and securities services |
| Merchant services for SMBs | Investment banking services |

**What to gather:**

- Size of the SOHO/SME banking market by geography (USA, India, UK/EU) — number of businesses, total banking revenue from SOHO/SME segment, technology spending on SME banking platforms
- Current AI deployment in SME banking vs. consumer banking — evidence of an investment gap
- SME banking pain points that AI agents could address: slow loan decisions, limited advisory, reactive servicing, manual cash management
- Fintech challengers targeting SME banking with AI: Brex, Mercury, Relay Financial, Tide (UK), NiYO (India), Open (India), RazorpayX (India)
- Relationship management AI for SME: how AI agents can augment relationship managers who are stretched across too many SME clients
- Cash management advisory AI: evidence of banks or fintechs using AI to advise SMEs on cash flow optimization, sweep configurations, working capital
- SME satisfaction with banking services — evidence that the segment is underserved
- Bank announcements on SME banking AI initiatives

**Sources to target:**

- Federal Reserve Small Business Credit Survey (USA)
- SBA / Census Bureau data on small business demographics
- British Business Bank (UK SME banking data)
- RBI MSME lending data and priority sector reporting
- World Bank Global Findex (SME banking access data)
- J.D. Power US Small Business Banking Satisfaction Study
- Cornerstone Advisors (SME banking technology survey)
- Fintech funding data: Crunchbase/PitchBook for Brex, Mercury, Tide, RazorpayX
- Bank annual reports: search for "small business," "SME," "commercial banking" technology investment
- Analyst reports on SME banking: Celent, Javelin (Datos Insights), Oliver Wyman

**Geographic scope:** USA (primary), India (MSME lending is a massive market), UK.

**How data will be used:** Part I, Section 3 (Structural Shift 5 — SOHO/SME as underserved AI segment), Section 4 (Engagement Landscape — SME-specific engagements), Section 6 (Target Universe — banks with SME banking AI signals). Part II, Section 8 (Where to Play — whether to pursue SME banking as a distinct segment or only as an expansion from consumer banking).

**Citation requirement:** SME banking market data must come from regulatory, census, or established research sources — not from fintech marketing material. Fintech competitor claims about market gaps must be cross-referenced with bank data.

---

### Stream 6: AI Agent Governance and the Operational Model Gap

**Why a separate stream:** The central thesis of the agentic banking engagement area is that AI agents cannot participate effectively in banking operations because there is no explicit model of the work for them to participate in. This stream gathers evidence for that thesis — and for the counter-thesis (that existing AI platforms are solving the operational model problem without a purpose-built substrate). The evidence determines whether Zeta's "operational model" positioning (Evolution Fabric + Seer) is a genuine differentiator or an over-engineered solution to a problem the market is solving differently.

**What to gather:**

- Evidence that AI agent deployment in banking is constrained by the operational model gap (lack of explicit scenarios, governed delegation, tool contracts, audit trails) — not by AI capability
- Evidence of banks struggling to scale AI beyond pilots — and whether the bottleneck is operational context, governance, data, talent, or AI capability
- How existing platforms address the operational model problem:
  - Salesforce Agentforce: how does it provide domain context and governance?
  - Pega Customer Decision Hub: pre-built banking decisioning models — how deep?
  - Google CCAI: conversation flow + backend integration — does it provide an operational model or just a conversation layer?
  - ServiceNow AI Agents: ITSM domain model — is there a banking equivalent?
- AI agent identity and accountability requirements specific to customer-facing banking (distinct from back-office agents): when an AI agent resolves a dispute, who is accountable? How is the decision auditable? What happens when the customer challenges the agent's resolution?
- Standards body activity relevant to banking AI agents:
  - Google's Agent-to-Agent (A2A) protocol — multi-agent coordination
  - Anthropic's Model Context Protocol (MCP) — agent-tool interaction
  - IEEE / ISO standards on AI transparency and accountability
- Industry evidence on compounding vs. non-compounding AI deployment — do banks that invest in an operational substrate deploy AI agents faster for the 5th domain than the 1st?

**Sources to target:**

- McKinsey / BCG / Deloitte surveys on AI scaling challenges in banking
- Gartner / Forrester on AI pilot-to-production barriers
- Bank CIO interviews and conference presentations on AI deployment challenges
- Vendor documentation: Salesforce Agentforce architecture, Pega banking modules, Google CCAI architecture
- Standards body publications: A2A protocol spec, MCP spec, IEEE AI transparency standards
- Cross-reference: `_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md` (extensive coverage of AI governance barriers — adapt for customer-facing context)
- Cross-reference: `_research/digital-identity-and-trust/s5-ai-agent-identity.md` (AI agent identity requirements)
- Cross-reference: `market-study/agentic-systems-development-platforms/background/enterprise-ai-agent-platform-backdrop.md` (strategic gap in enterprise agent platforms)

**Geographic scope:** Global (governance challenges are universal, though regulatory specifics vary).

**How data will be used:** Part I, Section 3 (Structural Shift 6 — domain knowledge as bottleneck), Section 5 (Competitive Landscape — evaluating whether competitors solve the operational model problem). Part II, Sections 7–10 (Zeta's position on the operational model via Evolution Fabric + Seer, and whether this is a genuine differentiator).

**Citation requirement:** Evidence must distinguish between vendor marketing claims about "AI governance" and verified production capabilities. Cross-reference claims across multiple sources. Flag any claim that relies solely on vendor documentation.

---

## 3. Phase 2: Synthesis and Gap-Fill

### Cross-referencing

- **Market sizing methodology transparency:** The TAM is constructed, not directly sourced. Document the construction methodology explicitly — which adjacent categories were used, what overlap assumptions were made, what banking vertical share percentages were applied. Compare the constructed figure against any available validation points (bank IT spending surveys, vendor revenue proxies).
- **Regulatory-competitive alignment:** Map each regulation (Stream 2) to the vendors positioned to benefit (Stream 3) and the structural shift it accelerates (Stream 4). Identify regulations where no vendor has a strong solution — these are the whitespace opportunities.
- **Chatbot → agent transition evidence:** Cross-reference Stream 3 (competitive landscape — vendor capability levels) with Stream 4 (structural shifts — evidence of banks moving beyond chatbots). Identify which banks have genuinely deployed autonomous agent resolution vs. which are still using enhanced chatbots with AI-assist. The distinction is critical — the market overstates "AI agent" deployment by relabeling chatbots.
- **SOHO/SME gap confirmation:** Cross-reference Stream 5 (SME banking AI) with Stream 3 (competitive landscape) to confirm whether the "underserved SME" thesis holds. If multiple vendors are actively addressing SME banking with AI agents, the opportunity may be smaller than hypothesized.
- **Operational model gap validation:** Cross-reference Stream 6 (governance and operational model) with Stream 3 (competitive landscape) to test whether Salesforce Agentforce, Pega, or other platforms are solving the operational model problem. If they are, Part II must acknowledge this honestly — Zeta's Evolution Fabric positioning is only differentiated if the gap is real.
- **Bank signal aggregation:** Consolidate bank modernization signals from Streams 3 and 4 into a single target universe. De-duplicate. Verify each bank's tier classification and geography. Confirm each signal source URL resolves.

### Evidence quality assessment

For each structural shift, rate evidence quality:

- **Strong:** 3+ independent data points with navigable URLs, confirmed by both analyst and primary sources
- **Moderate:** 2 data points or analyst-only without primary confirmation
- **Thin:** Single source or vendor-provided only
- **Hypothesis:** No external evidence found — flag as hypothesis and state explicitly in the document

Given that analyst coverage for agentic banking is thin, expect more "Moderate" and "Thin" ratings than in the payments or digital identity analyses. Shifts with "Hypothesis" evidence must be either dropped from Part I or explicitly flagged as emerging observations. The analyst voice does not assert without evidence.

### URL and citation verification

- Verify every URL resolves to the cited content (not a homepage, not a 404, not a paywall with no preview)
- For paywalled sources, confirm full bibliographic detail (publication, author, date, title, issue)
- Flag unverifiable claims in `unverified-claims.md`
- Verify constructed TAM figures against available validation points

### Targeted gap-fill research

Based on synthesis, conduct targeted follow-up for:

- Any structural shift with fewer than 3 data points
- Market sizing validation — if the constructed TAM produces an implausible figure, investigate why
- Bank deployment evidence — if the target universe has fewer than 12 named institutions, conduct targeted search for banks in underrepresented tiers/geographies
- SOHO/SME evidence — if business banking AI evidence is too thin, reassess whether to include it as a full structural shift or fold it into a broader shift on underserved segments
- Operational model gap evidence — if the thesis that "the operational model is the bottleneck" cannot be independently evidenced, the advisory positioning must be adjusted

### Right to Play / Right to Win mapping

Map findings to the distillation framework:

**Right to Play questions to answer:**

- Is the vendor-addressable TAM large enough to justify entry? (Note: the TAM is constructed and may be less precise than payments or identity — acknowledge this.)
- Are banks actively investing in AI agents for customer-facing operations? Or is investment still concentrated in back-office automation?
- Does "agentic banking" represent a distinct purchasing decision for bank CIOs — or is it bundled into broader "AI strategy" or "digital transformation" budgets?
- Can Zeta enter given Evolution Fabric, Seer, Quark, Trust Fabric, and CAF? What is genuinely production-ready vs. architectural vision?
- What is the regulatory runway — does the EU AI Act create urgency or uncertainty?

**Right to Win questions to answer:**

- Does Evolution Fabric's operational model (Hubs, Streams, Loops, Scenarios, Teams, Machines) represent a genuine architectural advantage over platforms that provide only a conversation/interaction layer?
- Does Seer's AI agent governance (lifecycle, identity, delegation, guardrails, OPD) address a need that Salesforce Agentforce, Pega, and others do not?
- Does Quark (pre-built domain hubs with pre-modeled Scenarios) accelerate deployment in a way that generic AI platforms cannot?
- Does CAF's decision auditability address the explainability/accountability requirements that regulators are imposing?
- Are there switching costs, network effects, or compounding advantages that strengthen with each domain deployed?
- Where is Zeta's position genuinely weak? (e.g., NLU/NLG capability, conversational AI maturity, contact center integration, brand recognition in AI, customer-facing channel experience)

### Assembling the target universe

From bank signals collected across Streams 3 and 4:

- Organize by geography (USA, India, UK/EU)
- Classify by tier (Tier 1 / $100B+ assets, Tier 2 / $10B–$100B, Tier 3 / $1B–$10B)
- Classify by horizon (Near-term 0–2 years: active signals; Medium-term 2–5 years: structural pressure)
- For each bank, record: name, tier, geography, signal type, source, URL
- Minimum 12 named institutions across all tiers and geographies
- Include banks with SOHO/SME banking AI signals where available

### Grounding the Zeta advisory

Cross-reference competitive landscape (Stream 3) with Zeta's product-line files:

- **Evolution Fabric (Hub + Seer)** — primary asset. Hub provides the operational model (domain hubs, Streams, Loops, Scenarios, Teams, Channels, Machines). Seer provides AI agent governance (lifecycle, identity, authority, context assembly, guardrails, OPD). Map against the "operational model gap" — is this what banks need? Is it what they know they need?
- **Quark domain hubs** — pre-built operational domains (Customer Servicing, Payments, Credit Card, CLM, Lending, Origination). How much of the customer-facing banking AI use case do these cover? What is genuinely pre-modeled vs. still placeholder?
- **Cognitive Audit Fabric** — decision auditability for every AI agent judgment. Critical for regulated customer-facing AI (dispute resolution, credit decisions). Map against EU AI Act and CFPB requirements.
- **Trust Fabric** — agent identity and delegation. When an AI agent resolves a dispute, Trust Fabric governs who authorized it and who is accountable. Map against the "AI agent accountability" regulatory requirement.
- **Neutrino** — channel infrastructure. AI agents interact with customers through channels (chat, voice, web, API, MCP). Neutrino provides the multi-channel interaction surface. Map against the "multi-channel continuity" structural shift.

Identify gaps honestly:

- Does Zeta have production-grade NLU/NLG and conversational AI capability? Or is this a gap vs. Google CCAI, Salesforce, Amazon Connect?
- Does Zeta have a contact center integration story? Banks deploying customer-facing AI agents need integration with existing contact center infrastructure.
- How deep are the Quark domain hub Scenario models? Are they genuinely pre-built with the specificity needed for AI agent resolution, or are they structural templates that require extensive domain engineering?
- What is Zeta's go-to-market position for selling "agentic banking" to bank CIOs? Is this a natural extension of existing engagements, or a new conversation with a new buyer?
- Does Zeta have reference deployments of AI agents resolving customer situations in production? If not, the advisory must acknowledge the credibility gap.

---

## 4. Phase 3: Document Writing

Section-by-section writing order. Target word counts are guidelines, not hard limits.

### PART I — THE OPPORTUNITY (Analyst voice, no Zeta references)

**Section 1: Market (~600 words)**

- Constructed TAM for AI agents in customer-facing banking operations, with methodology transparent
- Revenue by sub-segment: consumer banking AI, business banking AI (SOHO/SME only), family/household banking AI
- Revenue by geography (USA, India, UK/EU)
- Revenue by bank tier
- Growth rates and acceleration signals
- Framing: the market is emerging and the TAM is constructed from adjacent categories — but the directional evidence is strong. Banks are moving from chatbot spending to agent spending. The vendor-addressable opportunity is migrating from "conversation layer" to "operational resolution layer."

**Section 2: How We Got Here (~400 words)**

- Three generations of AI in banking:
  - Gen 1: FAQ chatbots (2016–2020) — rule-based, scripted, limited to navigation and information retrieval. BoA Erica, Capital One Eno, HDFC Eva. Contained value, but did not resolve customer situations.
  - Gen 2: AI-assisted copilots (2020–2024) — ML-powered, human-agent assist, intent detection, suggested responses, knowledge retrieval. Improved agent productivity but did not change the resolution model. Customers still spoke to humans.
  - Gen 3: Autonomous resolution agents (2024+) — LLM-powered, multi-step reasoning, tool use, governed delegation, autonomous resolution within guardrails. Emerging. The shift from "AI helps the human resolve" to "AI resolves, human governs."
- What was deferred: banks deployed AI for customer interaction without building the operational model that would make AI a resolution participant. The conversational layer advanced; the operational substrate did not.

**Section 3: Structural Shifts (6–8 shifts, ~2,500 words — the core)**

Each shift follows the pattern established in the payments and digital identity analyses:

- The evidence (data points with citations)
- The opportunity by segment (Tier 1 / Tier 2 / Tier 3)
- Market-specific dynamics (USA / India / UK/EU)

Anticipated shifts (final list determined by evidence quality in Phase 2):

1. AI moving from chatbot supplement to operational resolution
2. Experienced banking staff becoming scarce and expensive
3. Project-by-project AI failing to scale beyond the pilot
4. Consumer protection regulators forcing governed AI deployment
5. Business banking (SOHO/SME) as the most underserved AI segment
6. Domain knowledge becoming the bottleneck — not AI capability
7. Multi-channel continuity becoming table stakes
8. Family and household banking emerging as a distinct AI domain

**Section 4: The Engagement Landscape (~500 words)**

Concrete engagement types banks are commissioning:

- Customer servicing AI agent deployment (dispute resolution, inquiry resolution, status tracking)
- Application processing AI (credit applications, account opening, onboarding)
- Relationship management AI for SOHO/SME (context preparation, opportunity identification, communication drafting)
- Proactive engagement AI (cross-sell, retention, dormancy re-activation — based on customer lifecycle signals, not batch campaigns)
- Multi-channel AI continuity (AI agents maintaining context across chat, voice, web, mobile)
- AI governance and operational model deployment (the substrate — before the agents)

Map each engagement type to bank tier and structural shift.

**Section 5: Competitive Landscape (~600 words)**

- By category: conversational AI for banking, contact center/CX AI, enterprise agent platforms, BPM/case management + AI, core banking vendors with AI, bank-built solutions
- Capability spectrum: chatbot → copilot → agent. Most vendors are still at copilot level. Identify which are genuinely shipping autonomous resolution.
- The operational model gap: which vendors provide only the interaction/conversation layer vs. which also provide the operational substrate (domain context, governance, audit, delegation)?
- Banking domain depth: which vendors have banking-specific domain knowledge vs. horizontal AI platforms that require extensive domain engineering?
- Consumer vs. business banking coverage: which vendors address SOHO/SME specifically?
- Gaps and vulnerabilities: where no vendor provides a governed, domain-aware AI agent platform for customer-facing banking operations

**Section 6: Target Universe (~500 words)**

Named institutions organized by:

- Geography (USA, India, UK/EU)
- Bank tier (Tier 1 / Tier 2 / Tier 3)
- Horizon (Near-term / Medium-term)
- For each: the observable evidence with navigable URL
- Framed as analytical observation, not sales targeting
- Where possible, distinguish between banks investing in consumer banking AI vs. SOHO/SME banking AI

---

### PART II — THE ADVISORY (Advisor voice, Zeta-specific)

**Section 7: Zeta's Position (~500 words)**

- Evolution Fabric (Hub + Seer) as the operational substrate that makes AI agent deployment repeatable across domains — the differentiator if the "operational model gap" thesis holds
- Quark domain hubs as pre-built operational domains with pre-modeled Scenarios — the accelerant
- CAF as decision auditability for every agent judgment — the regulatory enabler
- Trust Fabric as agent identity and delegation — the accountability layer
- Neutrino as multi-channel interaction surface — the reach layer
- Honest gap assessment:
  - Conversational AI / NLU maturity vs. Google, Salesforce, Amazon
  - Contact center integration vs. NICE, Genesys, Five9
  - Quark domain model depth — how much is genuinely pre-modeled vs. placeholder
  - Production reference deployments — any AI agents resolving customer situations in production?
  - Go-to-market readiness for "agentic banking" as a distinct offering

**Section 8: Where to Play (~500 words)**

- Which banking segments to pursue first: consumer servicing (highest volume, most structured), then SOHO/SME banking (underserved), then family banking (niche)
- Which engagement types to lead with: dispute resolution and inquiry resolution (clearest ROI, most structured Scenarios, strongest governance narrative)
- Which bank tiers to target: Tier 2 US banks (most likely to buy platform; Tier 1 builds internally; Tier 3 buys through core banking vendor)
- Which geographies to prioritize: USA (primary revenue), India (accessible, digital-first), UK (regulatory-driven, AI governance-forward)
- Explicit "not yet" calls:
  - Do not pursue family banking as a standalone offering — insufficient market evidence and no Quark domain hub
  - Defer Tier 1 banks as primary targets — they build internally and the sales cycle exceeds Zeta's current position
  - Do not compete on conversational AI maturity — lead with operational model and governance, not NLU/NLG
- Explicit "do not pursue" calls:
  - Do not enter the contact center AI market directly — compete on what happens after the conversation, not the conversation itself
  - Do not pursue corporate banking AI (out of scope; different buying center, different complexity profile)

**Section 9: Risks and Gaps (~400 words)**

- **What must be true for Zeta to win:**
  - Banks must recognize the "operational model gap" as the bottleneck to AI scaling (not AI capability, not data, not talent alone)
  - Evolution Fabric and Seer must be production-ready for customer-facing AI agent deployment — not just back-office
  - Quark domain hubs must have sufficient Scenario depth for AI agent resolution — not just structural templates
- **What could close the window:**
  - Salesforce Agentforce achieves banking domain depth through acquisition or partnership (Salesforce + Kasisto, Salesforce + banking BPM vendor)
  - Google/Amazon/Microsoft embed agent governance into their cloud AI platforms, making a separate operational substrate unnecessary
  - Core banking vendors (Temenos, FIS, Fiserv) add competent AI agent capability to their existing platform — making a separate "agentic banking" vendor unnecessary since the operational context already exists within the core
  - Regulatory uncertainty (EU AI Act enforcement, CFPB stance) slows bank AI adoption, delaying the market
- **Capability gaps to address:**
  - Conversational AI maturity — partnership or build?
  - Contact center integration — partner with NICE/Genesys/Five9?
  - Quark domain model depth for customer-facing Scenarios
  - Production reference deployment for credibility
  - Go-to-market for a new category ("agentic banking platform" vs. "AI in banking" vs. "banking operations modernization with AI")

**Section 10: Recommended Actions (~400 words)**

- Near-term (0–2 years): specific actions, specific capability investments, specific bank targets
- Medium-term (2–5 years): platform positioning, geographic expansion, segment expansion
- Priority order: what to do first, second, third
- Which banks to approach first, and why (based on Target Universe evidence)
- Partnership strategy: which conversational AI or contact center vendors to partner with vs. build vs. acquire

**Section 11: Executive Summary (~400 words)**

- Written last
- Covers both Part I and Part II
- A board member who reads only this section should understand: the market opportunity (constructed TAM), the structural shifts creating it, the competitive landscape and where no vendor has a complete solution, Zeta's position and honest gaps, and the recommended actions with priority order

---

## 5. Phase 4: Review

### Part I Checks

- Every data point has a source citation with a navigable, verified URL — or full bibliographic detail for paywalled sources
- No broken links — every URL confirmed to resolve to cited content
- No "according to [authority]" citations without a traceable reference
- All unverifiable claims flagged as `[unverified — needs manual confirmation]`
- Constructed TAM methodology is transparent and the construction arithmetic is verifiable
- No structural shift relies on assertion without evidence
- Segment analysis (Tier 1/2/3) grounded in research, not generic
- Geographic analysis specific to USA, India, UK/EU — not generic "global" claims
- No Zeta references, product names, or commercial voice anywhere in Part I
- Every bank named in the Target Universe has a citable evidence basis with navigable source link
- Document reads as external strategic analysis, not internal marketing
- The "operational model gap" thesis is treated as an analytical observation supported by evidence, not as a product category assertion
- "Business banking" refers only to SOHO/SME throughout — no scope creep into corporate banking
- The distinction between chatbot, copilot, and agent is maintained consistently — no conflation

### Part II Checks

- Every recommendation traces back to evidence presented in Part I
- Gaps and weaknesses stated honestly, not minimized
- Recommendations specific and prioritized, not a generic list
- "Do not pursue" and "delay" recommendations included where warranted
- Product and asset references accurate against repo's product-line files (Evolution Fabric: `strategy/product-lines/infra-product-lines/evolution-fabric.md`, Trust Fabric: `trust-fabric.md`, CAF: `cogntive-audit-fabric.md`, Quark: `banking-product-lines/quark.md`, Neutrino: `banking-product-lines/neutrino.md`)
- Go-to-market challenges acknowledged (agentic banking is a new category; Zeta may not have the brand recognition or reference deployments to compete with Salesforce or Google)
- Conversational AI capability gap acknowledged honestly — Zeta is not a conversational AI company
- "Business banking" scope constraint (SOHO/SME only, not corporate) maintained in all recommendations

### Editorial Rigor (Part I only) — Eight Tests

1. **Does every sentence earn its place?** No dead weight. Every sentence advances the argument.
2. **Tonal consistency.** Board-grade prose throughout. No drops to filing-cabinet language.
3. **Commercial voice.** Zero first-person plural. Zero market opportunity language. Zero buyer-readiness framing. Zero competitive positioning.
4. **Meta-narration.** No "this section will explore..." The structure speaks for itself.
5. **Vocabulary discipline.** Consistent terms throughout. "AI agent" not alternating with "virtual assistant," "chatbot," "copilot," and "digital worker" without clear definitional distinction. If the document distinguishes chatbot/copilot/agent, the distinction must be defined once and held throughout.
6. **Shelf life.** No time-fragile language. Structural arguments survive without timestamps.
7. **Specificity vs. thesis level.** No performance claims without evidence. No implementation details. Constructed TAM is presented as a constructed estimate, not as a definitive market size.
8. **Audience neutrality.** Consumable by bank CIOs, bank CEOs, Zeta's board. Not a sales document.

---

## 6. Key Differences from Other Engagement Areas

| Dimension | Payments | Digital Identity & Trust | Agentic Banking |
|---|---|---|---|
| **Market structure** | Single, well-defined category. Analyst firms size it consistently. | Fragmented across 5+ adjacent categories. No analyst sizes the converged category. | **No established category.** "Agentic banking" does not exist as an analyst-reported market. TAM must be constructed from adjacent categories (conversational AI, banking automation, enterprise AI agents). |
| **Competitive landscape** | Dominated by incumbents (FIS, Fiserv) with clear modern challengers (Marqeta, Stripe). Relatively consolidated. | Highly fragmented. No single vendor covers the converged trust surface. | **Converging from multiple directions.** Conversational AI vendors (Kasisto, Personetics) moving up the stack. Enterprise AI platforms (Salesforce, Google, AWS) moving into banking. Core banking vendors adding AI. Banks building internally. No single vendor provides operational resolution + governance. |
| **Primary driver** | Real-time payments mandates + technology debt forcing infrastructure replacement. | Regulatory convergence + AI agent identity as a new category. | **Talent scarcity + AI capability outpacing deployment infrastructure.** Banks have the AI capability to resolve customer situations but lack the operational model to deploy it at scale. Regulatory pressure (EU AI Act, CFPB) is accelerating governance requirements. |
| **Geographic concentration** | USA 30–40%. India (UPI). UK/EU. Brazil. | USA (IAM/CIAM). EU (regulatory driver). India (Aadhaar). | **USA dominant** (largest AI banking investment). India (digital-first banking, cost pressure). UK (FCA Consumer Duty, AI governance-forward). No Brazil equivalent for agentic banking. |
| **Central strategic argument** | Banks must replace aging payment infrastructure. | Banks must converge fragmented identity point solutions. | **Banks have deployed AI at the conversation layer but not at the operational resolution layer.** The bottleneck is the operational model — not AI capability. The vendor that provides the governed operational substrate for AI agent deployment captures the most durable position. |
| **Bank buying behavior** | Payments is a defined budget line item. CIOs know what they're buying. | Identity spend scattered across CISO, CIO, compliance, fraud, privacy budgets. | **AI in banking is an active budget item, but "agentic banking platform" is not yet a recognized purchasing category.** The buyer may be the CIO (technology), COO (operations), or CDO (digital). The engagement must be sold as an outcome ("AI agents resolving customer situations at scale") not as a category ("agentic banking platform"). |
| **Zeta's position** | Strong — Photon product lines directly address card issuance, tokenization, processing. | Architectural — Trust Fabric defines the converged vision, but production depth uncertain. | **Architectural and unproven.** Evolution Fabric + Seer define the operational substrate thesis. Quark provides pre-built domain hubs. But Zeta has no production-grade conversational AI, no contact center integration story, and (likely) no reference deployment of AI agents resolving customer situations. The position is genuinely differentiated at the architecture level but commercially unproven. |
| **Analyst coverage** | Strong. Multiple market sizing reports, MQs, Forrester Waves. | Moderate for IAM/CIAM, strong for IDV, thin for converged trust layer. | **Thin.** No analyst sizes "agentic banking." Conversational AI in banking is covered (Gartner, Forrester) but conflates chatbots with agents. Enterprise AI agent platforms are an emerging category. Research must rely heavily on primary evidence. |

---

## 7. Execution Approach

### Sub-agent batching strategy

Six research streams, max 4 concurrent sub-agents:

**Batch 1 (4 concurrent):**

- Stream 1: Market sizing and revenue pools — constructed TAM
- Stream 2: Regulatory landscape — AI agents in customer-facing banking
- Stream 3: Competitive landscape
- Stream 4: Structural shifts and bank modernization activity

**Batch 2 (2 concurrent):**

- Stream 5: SOHO/SME business banking AI opportunity
- Stream 6: AI agent governance and operational model gap

### Estimated turns

| Phase | Estimated Turns |
|---|---|
| Phase 1, Batch 1 (Streams 1–4) | 1 turn (parallel) |
| Phase 1, Batch 2 (Streams 5–6) | 1 turn (parallel) |
| Phase 2: Synthesis and gap-fill | 2–3 turns (expect more gap-fill due to thin coverage) |
| Phase 3: Document writing (Part I) | 2–3 turns |
| Phase 3: Document writing (Part II) | 1–2 turns |
| Phase 4: Review and editorial rigor | 1–2 turns |
| **Total** | **8–12 turns** |

Higher estimate than digital identity (8–11 turns) due to thin analyst coverage requiring more gap-fill research and more careful TAM construction.

### Output file path

`org-8.0/what-we-sell/strategy/engagement-areas/agentic-banking.md`

---

## 8. Output Files

### Primary document

`org-8.0/what-we-sell/strategy/engagement-areas/agentic-banking.md` — replaces the current CIO-facing capability catalogue with the two-part opportunity analysis and advisory.

### Research retention

**Location:** `org-8.0/what-we-sell/strategy/_research/agentic-banking/`

**Files to create:**

| File | Contents |
|---|---|
| `s1-market-sizing.md` | Constructed TAM from adjacent categories. Methodology, input data, arithmetic, validation. Claim/Value/Source/URL/Verified table. |
| `s2-regulatory-landscape.md` | USA, India, UK/EU regulations governing AI agents in customer-facing banking. Consumer protection, fair lending, AI governance, explainability requirements. |
| `s3-competitive-landscape.md` | By-category competitor profiles. Capability level (chatbot/copilot/agent), banking domain depth, operational model depth. Bank modernization signals. |
| `s4-structural-shifts.md` | Evidence for each structural shift. Data points, regulatory citations, bank-tier analysis, geographic variation. Bank deployment signals. |
| `s5-soho-sme-business-banking.md` | SOHO/SME banking market data, AI deployment gap, fintech challengers, bank investment signals. Scope: SOHO/SME only, not corporate. |
| `s6-governance-operational-model.md` | AI agent governance requirements, operational model gap evidence, platform comparison (how vendors address the gap), standards body activity. |
| `synthesis-notes.md` | Cross-references, contradictions, evidence quality ratings, Right to Play / Right to Win mapping, TAM construction methodology notes, editorial decisions, target universe assembly notes. |
| `unverified-claims.md` | Every claim flagged as `[unverified — needs manual confirmation]` with context. |

**Format for stream files:**

- Research date and engagement area
- Data table: Claim | Value | Source | URL | Verified (Yes/No)
- Key findings as structured bullets
- Gaps and unresolved questions
- Raw notes and excerpts

**Cross-references to existing research:**

- `_research/cloud-and-platform-operations/s5-aiops-agentic-operations.md` — AIOps vendor capabilities and banking adoption. Reference for competitive context but distinct domain (infrastructure ops vs. customer-facing banking).
- `_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md` — Bank production deployments of agentic AI, regulatory positions, SR 11-7 strain analysis. Critical cross-reference for governance requirements — adapt for customer-facing context.
- `_research/digital-identity-and-trust/s5-ai-agent-identity.md` — AI agent identity and EU AI Act requirements. Cross-reference for agent accountability; do not re-research.
- `market-study/agentic-systems-development-platforms/background/agentic-systems-platform-tam.md` — Platform TAM estimates. Cross-reference for market sizing validation.
- `market-study/agentic-systems-development-platforms/background/players-and-products.md` — Vendor catalog for enterprise AI agent platforms. Cross-reference; do not re-research.
- `market-study/agentic-systems-development-platforms/background/enterprise-ai-agent-platform-backdrop.md` — Strategic gap analysis. Cross-reference for competitive landscape.

Note all cross-references in `synthesis-notes.md`.

---

## 9. What This Plan Does NOT Do

- Does not write the opportunity analysis itself. This is a research and writing plan only.
- Does not produce generic research streams applicable to any engagement area. Every stream, competitor, regulation, and structural shift is specific to agentic banking.
- Does not include more than 3 geographic markets (USA, India, UK/EU).
- Does not plan for a document shorter than 5,500 words or longer than 7,500 words.
- Does not blend the analyst and advisor voices. Part I and Part II are structurally separated.
- Does not include banks in the Target Universe without specifying evidence sources.
- Does not cite sources without navigable URLs or full bibliographic detail.
- Does not discard research output. Every stream's raw findings are saved to `_research/agentic-banking/`.
- Does not expand "Business Banking" scope beyond SOHO/SME. Corporate banking, institutional banking, and treasury services are explicitly excluded.
- Does not present the constructed TAM as a definitive market size. The construction methodology is transparent and the figures are clearly labeled as estimates.
- Does not claim Zeta has production-grade conversational AI capability unless the evidence supports it. Gaps are stated honestly.
