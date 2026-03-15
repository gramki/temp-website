# Stream 3: Competitive Landscape — Agentic Banking

> **Research date:** 15 March 2026
> **Engagement area:** Agentic Banking — AI agents that autonomously resolve customer-facing banking situations (disputes, inquiries, applications, servicing) within governed boundaries
> **Research scope:** Vendor landscape, bank-built solutions, bank modernization signals

---

## 1. Competitor Profile Table

| Vendor | Category | Capability Level | Banking Customers | Operational Model Depth | Revenue / Scale | Key Vulnerability | Primary URL | Verified |
|---|---|---|---|---|---|---|---|---|
| **Kasisto (KAI)** | Conversational AI for banking | Chatbot → Copilot | JPMorgan Chase, TD Bank, Standard Chartered, Westpac, Nedbank, Meriwest CU | Medium — deep financial domain NLU; limited workflow orchestration and case management | $90M total funding; ~$171M raised across 8 rounds; 51–200 employees | No autonomous resolution; lacks back-office integration and governance/audit layer; subscale relative to platform vendors | [kasisto.com](https://kasisto.com) | Funding via American Banker (Sep 2024) |
| **Personetics** | Conversational AI for banking | Chatbot → Copilot (pivoting to Agent via MCP Server) | U.S. Bank, RBC, BMO, Santander, UOB, MUFG, Huntington, KeyBank; 150M+ end-customers served | Medium-High — financial behavior analysis, predictive analytics, contextual engagement; launched MCP Server (Sep 2025) enabling agentic apps | $160M+ raised (Thoma Bravo-led $85M in 2021); Warburg Pincus, Sequoia backed | Insights layer only — does not execute transactions or resolve cases autonomously; relies on bank or third-party execution layer; no native case/dispute management | [personetics.com](https://personetics.com) | Funding via VentureBeat; MCP launch via BusinessWire (Sep 2025) |
| **Clinc** | Conversational AI for banking | Chatbot | U.S. Bank (Smart Assistant), Finastra partnership, Q2, Alkami integrations | Low-Medium — virtual banking assistant with 82% CSAT, 90% containment; FAQ/navigation focus | Private; acquired/partnered with multiple digital banking platforms | Limited to conversational containment; no autonomous resolution; small scale; narrow product scope | [clinc.com](https://clinc.com) | U.S. Bank deployment via VoiceBot.ai (Jul 2020) |
| **Avaamo** | Conversational AI for banking | Chatbot → Copilot | 20M subscribers annually; undisclosed banking clients | Medium — pre-built banking flows (account mgmt, loans, FX); 114+ languages; sentiment analysis | Private; undisclosed revenue | Limited production references at Tier 1 banks; narrow brand recognition vs. peers; no disclosed governance/audit framework | [avaamo.ai](https://avaamo.ai) | Metrics from avaamo.ai product pages |
| **Haptik (Jio)** | Conversational AI for banking | Chatbot | CASHe (India lending), 500+ enterprises total; parent Jio serves 498M users | Low — WhatsApp bot automation, loan applications, FAQ; no banking-specific operational model | Private; owned by Jio Platforms | India-centric; no disclosed Tier 1 bank customers; chatbot-level only; no governance, audit, or compliance layer for banking | [haptik.ai](https://haptik.ai) | Case studies from haptik.ai |
| **Yellow.ai** | Conversational AI for banking | Chatbot → Copilot | UnionBank Philippines, 1,300+ enterprises total; BFSI vertical | Medium — 150+ pre-built banking templates; 90% query automation; SOC2/HIPAA/GDPR certified | Private; Challenger in 2025 Gartner MQ for Conversational AI | Horizontal platform with banking templates rather than deep domain model; no autonomous resolution; limited operational depth | [yellow.ai](https://yellow.ai) | Gartner MQ 2025 via Yellow.ai press; UnionBank metrics from yellow.ai |
| **Google (CCAI + Vertex AI Agent Builder)** | Contact center AI + Enterprise AI platform | Copilot → Agent (emerging) | Federal Bank India, OneUnited Bank, $80B national bank (unnamed), Deutsche Bank (compliance agents), Schroders, TransUnion | Low — provides AI interaction layer (Dialogflow, Vertex AI, Gemini); no banking domain model or operational framework | Google Cloud revenue $43.1B (FY2025 annualized); Leader in 2025 Gartner MQ for Conversational AI | Provides tooling, not banking operational model; no native case management, dispute workflow, or audit trail; requires SI assembly; model-centric not domain-centric | [cloud.google.com](https://cloud.google.com/solutions/contact-center-ai) | Gartner MQ 2025; Deutsche Bank via PYMNTS (Mar 2026); Federal Bank via Google Cloud case study |
| **Amazon Connect + Q in Connect** | Contact center AI | Copilot | NatWest Group, undisclosed other banking clients | Low — agent-assist with real-time recommendations; LLM-selectable (Nova Pro, Claude); no banking domain framework | AWS segment revenue ~$107B annualized (2025); Connect pricing bundled with AI | Horizontal CX platform; no banking-specific domain knowledge; no dispute/case management; requires extensive custom build for banking workflows | [aws.amazon.com/connect](https://aws.amazon.com/connect) | NatWest deployment via AWS blog |
| **NICE (CXone Mpower)** | Contact center AI | Copilot → Agent (shipping Jun 2025) | 80+ Fortune 100 firms; Openreach (14.5M annual journeys); banking clients undisclosed | Medium — CXone Mpower Agents (Jun 2025) handle front/middle/back office; Autopilot for customer-facing, Copilot for agent-facing | $2.95B total revenue (FY2025); AI ARR $328M growing 66% YoY | CX-native not banking-native; no domain knowledge for disputes, lending, or servicing; governance is CX-generic not banking-specific; Amelia integration adds NLU but not banking ops | [nice.com](https://www.nice.com) | Revenue from NICE 2025 earnings release; Mpower Agents via NICE press (Jun 2025) |
| **Genesys Cloud** | Contact center AI | Copilot → Agent (shipping Sep 2025) | Top 10 global bank ($45M+ TCV), Fortune 20 FS firm ($45M+), Prudential, Rabobank, Global Payments | Medium — Agentic Virtual Agent with LAMs; A2A/MCP interop; AI Studio with guardrails | ~$2.2B Cloud ARR (Q2 FY2026); AI ARR >$250M; 35% YoY Cloud growth | Same as NICE: CX orchestration without banking domain model; autonomous resolution requires customer-built domain logic; no native banking workflow engine | [genesys.com](https://www.genesys.com) | Revenue from Genesys Q2 FY2026 announcement; bank deal sizes disclosed in press |
| **Five9** | Contact center AI | Copilot | Banking clients undisclosed; broad enterprise base | Low-Medium — conversational AI data across voice/digital/AI; no autonomous agent capability disclosed | $1.15B revenue (FY2025); Enterprise AI ARR >$100M (50% YoY growth) | Horizontal CCaaS; no banking-specific capabilities; behind NICE and Genesys in agentic agent roadmap | [five9.com](https://www.five9.com) | Revenue from Five9 2025 earnings (Yahoo Finance) |
| **Verint** | Contact center AI | Copilot | Leading bank ($11M contract for 6,500 agents); 80+ Fortune 100 firms | Medium — Agent Copilot Bot for real-time coaching; hybrid cloud layering onto existing infra | AI ARR $372M (Q2 FY2026, 21% YoY growth); total subscription ARR ~$768M | Copilot-only — no autonomous resolution; overlay model depends on existing CX infrastructure; not building banking domain model | [verint.com](https://www.verint.com) | $11M bank deal via BusinessWire (Nov 2024); AI ARR from Verint earnings |
| **Salesforce Agentforce** | Enterprise AI agent platform | Copilot → Agent (shipping) | 18,500+ Agentforce deals; Financial Services Cloud customers (undisclosed banking count) | Medium-High — Atlas Reasoning Engine; pre-built Banking Service Assistance and Loan Product Assistance templates; compliance guardrails; proactive agents (Agentforce 2dx) | Agentforce ARR >$500M (330% YoY); Total Salesforce revenue $41.5B (FY2026 guided) | CRM-centric operational model — strong on interaction/case but lacks core banking domain depth (ledger, settlement, regulatory reporting); templates are thin on banking ops; requires heavy FSI customization | [salesforce.com/agentforce](https://salesforce.com/agentforce) | ARR from Salesforce Q3 FY2026 SEC filing (Nov 2025) |
| **Microsoft Copilot Studio + Azure AI Agent Service** | Enterprise AI agent platform | Copilot → Agent (emerging) | Broad FS adoption; Finance Agents (Reconciliation, Variance, Collections) in M365 | Low-Medium — Work IQ intelligence layer; Copilot Cowork (Mar 2026) for multi-step tasks; finance-specific agents in Excel | $236B Microsoft total revenue (FY2025); Azure AI specifics undisclosed | Horizontal platform; banking domain delivered via partner ecosystem (Accenture, Infosys, etc.); no native banking operational model; finance agents are accounting-focused not customer-servicing | [microsoft.com/copilot-studio](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio) | Finance Agents via Microsoft Learn; Copilot Cowork via press (Mar 2026) |
| **AWS Bedrock Agents** | Enterprise AI agent platform | Copilot → Agent (emerging) | Itaú Unibanco (70M customers migrated), Visa (fraud scoring), National Australia Bank, Nasdaq | Low — AgentCore framework with Strands Agents; multi-agent patterns for claims, loans, compliance; no banking domain model | AWS segment ~$107B annualized | Infrastructure-only; no banking domain knowledge, governance, or audit; requires bank or SI to build entire operational model; model-agnostic but domain-agnostic | [aws.amazon.com/bedrock](https://aws.amazon.com/bedrock/agents) | Itaú/Visa/NAB from AWS re:Invent 2025 blog |
| **ServiceNow AI Agents** | Enterprise AI agent platform | Copilot → Agent (banking-specific templates) | Fiserv partnership (Jan 2026); banking vertical customers undisclosed | Medium-High — disputes management agent (friendly fraud screening); customer onboarding agent; embedded compliance; unified workflow platform | $13.3B total revenue (FY2025); 21% YoY growth; 603 customers >$5M ACV | ITSM DNA — operational model is incident/case-centric not banking-domain-centric; dispute agent is new and unproven at scale; no core banking domain knowledge (ledger, settlement, regulatory) | [servicenow.com](https://www.servicenow.com/products/financial-services-operations/banking.html) | Revenue from ServiceNow Q4 2025 earnings (Nasdaq); Fiserv partnership via BusinessWire (Jan 2026) |
| **Pegasystems** | BPM / Case management + AI | Copilot → Agent (strong operational model) | Nationwide Building Society, major global banks; banking is core vertical | **High** — Customer Decision Hub (real-time decisioning, $652M 3-yr incremental revenue per Forrester TEI); case management engine; banking-specific workflows; regulatory audit trails; Pega Blueprint AI | $1.75B revenue (FY2025, 17% YoY); Pega Cloud $696M (25% growth); Free cash flow ~$500M | Expensive and complex to implement; perceived as legacy BPM by cloud-native buyers; slow to adopt GenAI/LLM natively; operational model depth is a moat but also an adoption barrier | [pega.com](https://www.pega.com) | Revenue from Pega Q4 2025 earnings; Forrester TEI study; Nationwide via PegaWorld 2025 |
| **Appian** | BPM / Case management + AI | Copilot | Financial services clients undisclosed; regulatory & compliance focus | Medium — AI Process Platform with orchestration; banking ops automation; emphasis on pilot-to-production transition | ~$600M estimated revenue (FY2025) | Subscale relative to Pega; limited banking-specific product depth; no autonomous agent capability disclosed; brand awareness gap in banking | [appian.com](https://www.appian.com) | Revenue estimated from prior disclosures; not independently verified for FY2025 |
| **Newgen Software** | BPM / Case management + AI | Copilot | 87 large customers (>Rs 50M billing); 77 countries; direct presence in 8 countries | Medium — digital process automation with AI; banking is primary vertical; Gartner/Forrester recognized | Rs 1,487 crore (~$178M) FY2025 revenue; 20% YoY growth; 25% PAT growth | India-headquartered with limited Tier 1 Western bank penetration; subscale globally; AI capabilities are process-automation-centric not agent-autonomous | [newgensoft.com](https://newgensoft.com) | Revenue from Newgen FY2025 earnings release |
| **Temenos** | Core banking + AI | Chatbot → Copilot | 950+ core banking clients, 600+ digital clients, 150+ countries; Tier 1 wins in US market | Medium — FCM AI agent for financial crime; Money Movement products; deep banking domain in core ledger | ARR $860M (12% YoY); total revenue ~$1.1B implied; raised FY2028 targets | AI capabilities are additive to core platform, not standalone; customer-facing AI is nascent; FCM agent is narrow (financial crime only); engagement layer is thin | [temenos.com](https://www.temenos.com) | Revenue from Temenos Q4 2025 earnings; Bloomberg (Feb 2026) |
| **FIS** | Core banking + AI | Copilot (emerging) | Broad bank/FI client base; Banking Solutions segment drives growth | Low-Medium — AI for decisioning, fraud prevention, workflow optimization; data-centric strategy post-Total Issuing Solutions acquisition | $10.7B adjusted revenue (FY2025); Banking Solutions segment 8.3% growth | AI is data/analytics layer on top of legacy infrastructure; no disclosed customer-facing AI agent; modernization is infrastructure-centric not interaction-centric | [fisglobal.com](https://www.fisglobal.com) | Revenue from FIS 2025 earnings release |
| **Fiserv** | Core banking + AI | Copilot (emerging) | Broad bank/FI client base; ServiceNow partnership for AI-driven transformation | Low — AI strategy via ServiceNow partnership and internal tools; no disclosed customer-facing AI agent product | $21.2B GAAP revenue (FY2025); Financial Solutions +2%, Merchant Solutions +5% | Largest core banking vendor by revenue but weakest disclosed AI agent capability; ServiceNow partnership suggests build-vs-buy tension; no autonomous agent roadmap visible | [fiserv.com](https://www.fiserv.com) | Revenue from Fiserv Q4 2025 earnings; ServiceNow partnership via BusinessWire (Jan 2026) |
| **Backbase** | Core banking (engagement layer) + AI | Chatbot → Agent (shipping Apr 2025) | 120+ financial institutions; Alliant CU ($20B), Judo Bank (Australia), Jet Bank (Albania), Evelyn Partners (UK) | **Medium-High** — Intelligence Fabric (Sep 2024) with agentic AI agents; unified customer servicing + digital sales; conversational banking, lifecycle orchestration, financial insights, AI-augmented support | Private; undisclosed revenue; ~1,000 employees estimated | Engagement layer only — requires core banking partner (Temenos, Thought Machine, etc.); no core ledger or settlement; unproven agentic agent in production at Tier 1 scale | [backbase.com](https://www.backbase.com) | Intelligence Fabric via Backbase press (Sep 2024); AI-powered platform via Backbase press (Apr 2025) |
| **Thought Machine** | Core banking (cloud-native) | N/A (infrastructure) | Lloyds, JPMorgan Chase, Standard Chartered, SEB, ING, Intesa Sanpaolo (Isybank) | Low — cloud-native core ledger; no customer-facing AI capability; API-first for partner integration | $200M Series C; $2.7B valuation; ~500 employees | No AI agent capability at all; pure infrastructure play; relevant as core banking modernization enabler but not a competitive threat in agentic banking | [thoughtmachine.net](https://www.thoughtmachine.net) | Gartner MQ Leader 2025 for Retail Core Banking; funding from press releases |
| **Mambu** | Core banking (cloud-native) | N/A (infrastructure) | 60+ new customers in 2025; Payments Hub live with 20+ EU customers | Low — data lake and analytics (Mambu Insights); no customer-facing AI agent capability | ~$160M estimated revenue; $5.5B valuation | Same as Thought Machine: infrastructure-only; no AI agent or customer interaction capability; relevant as composable core enabler | [mambu.com](https://mambu.com) | Revenue estimate from CompWorth; Payments Hub from Mambu product updates |

---

## 2. Bank-Built Solutions

| Bank | Scale Indicator | Capability Level | Key Technology | Vulnerability as Competitive Threat |
|---|---|---|---|---|
| **Bank of America (Erica)** | 169M interactions in Q4 2025; 20.6M monthly active users | Chatbot → Copilot | In-house; predictive analytics, proactive notifications, spending insights | Not productized or available to other banks; limited to BofA ecosystem; chatbot-level (navigation/FAQ), not autonomous resolution |
| **JPMorgan Chase (LLM Suite)** | 250,000 employees (80% workforce); $3B AI budget (2026); $2B annual AI value realized | Copilot → Agent (emerging) | In-house Eliza platform; OpenAI + Anthropic models; 8 major upgrades since summer 2024 | Internal-only; not productized; building toward agentic but currently copilot; massive scale advantage but captive to JPM |
| **Capital One (Chat Concierge)** | 100M+ customers; 5,000+ AI patents; 10,000+ uses of Gen AI servicing tool | Copilot → Agent (emerging) | In-house multi-agentic system; Meta Llama + proprietary models; NVIDIA partnership | Only US financial institution among top AI patent leaders; not productized; proprietary data moat makes replication hard but also limits market impact |
| **Wells Fargo (Fargo)** | Workforce-wide AI agent deployment (Aug 2025); 250,000 vendor documents searchable | Chatbot → Copilot | Google Cloud partnership; Fargo assistant for customer-facing; internal AI agents for ops | Google Cloud dependency; customer-facing Fargo is chatbot-level; internal agents more advanced but not customer-resolution-focused |
| **DBS Bank (DBS Joy)** | 120,000+ chats handled; 4,000 corporate clients monthly; SGD 750M AI value (2024), targeting SGD 1B (2025) | Chatbot → Copilot | In-house; DBS-GPT for internal; DBS Joy for corporate; CSO Assistant for agents | World's Best AI Bank 2025; Joy is corporate-focused (SME); consumer-facing digibot is FAQ-level; Singapore-centric deployment |

---

## 3. Bank Modernization Signals

| Bank | Tier | Geography | Signal | Source | URL | Verified |
|---|---|---|---|---|---|---|
| **Lloyds Banking Group** | Tier 1 | UK | Generated £50M from GenAI in 2025; targets £100M+ in 2026; 50+ GenAI solutions deployed; planning AI-powered financial assistant for customers in 2026 | The Asian Banker | [theasianbanker.com](https://www.theasianbanker.com/press-releases/lloyds-scales-genai-and-agentic-ai-targets-127m-in-value-creation-for-2026) | Yes |
| **TD Bank** | Tier 1 | US/Canada | 75 AI use cases generating $170M value in 2025; expects $200M in 2026; Gen AI virtual assistant deployed in US contact center | Yahoo Finance | [yahoo.com/finance](https://finance.yahoo.com/news/td-bank-us-head-ai-070000228.html) | Yes |
| **KeyBank** | Tier 2 | US | Increased tech spend from $800-900M to $1B annually; AI-handled calls cost $0.25 vs. $9 for human; ~$100M annual savings achieved | PYMNTS | [pymnts.com](https://www.pymnts.com/news/artificial-intelligence/2026/keybank-taps-conversational-ai-cut-call-center-costs/) | Yes |
| **Bank of America** | Tier 1 | US | Erica: 169M interactions Q4 2025, 20.6M active users; CEO cited AI as driver of operating leverage in Q4 2025 earnings | PYMNTS | [pymnts.com](https://www.pymnts.com/earnings/2026/erica-ai-and-digital-drive-operating-leverage-at-bank-of-america) | Yes |
| **BNY Mellon** | Tier 1 | US | 20,000 "Empowered Builders" trained; 130+ autonomous "Digital Employees" with own credentials; Eliza 2.0 platform; 40% faster issue resolution, 30% fewer payment exceptions | Investor Wedbush | [investor.wedbush.com](https://investor.wedbush.com/wedbush/article/tokenring-2026-1-16-bny-mellon-scales-the-agentic-era-with-deployment-of-20000-ai-assistants) | Yes |
| **Goldman Sachs** | Tier 1 | US | GS AI Assistant to 10,000 staff (Jan 2025); autonomous agents entering production for trade accounting, reconciliation, client due diligence (Feb 2026); Anthropic partnership with embedded engineers | Reuters | [reuters.com](https://today.reuters.com/business/finance/goldman-sachs-teams-up-with-anthropic-automate-banking-tasks-with-ai-agents-cnbc-2026-02-06/) | Yes |
| **Citi** | Tier 1 | Global | Launched Citi Stylus Workspaces with Agentic AI (Sep 2025); multi-stage task automation; thousands of employees in phased rollout | Citigroup press release | [citigroup.com](https://www.citigroup.com/global/news/press-release/2025/citi-unveils-citi-stylus-workspaces-agentic-ai-turbocharging-productivity) | Yes |
| **HSBC** | Tier 1 | Global | Multi-year Mistral AI partnership (Dec 2025); 600+ AI use cases; self-hosted LLMs for lending, marketing, onboarding, fraud; global LLM productivity tool deployed | HSBC press release | [hsbc.com](https://www.hsbc.com/news-and-views/news/hsbc-news-archive/we-re-partnering-with-ai-powerhouse-mistral) | Yes |
| **UBS** | Tier 1 | Global | Established agentic AI center of excellence; building composable multi-agent infrastructure; agent marketplace concept; human roles shifting to governance and oversight | UBS Careers blog | [ubs.com](https://www.ubs.com/global/en/careers/about-us/stories/2025/agentic-ai.html) | Yes |
| **Deutsche Bank** | Tier 1 | Germany/Global | Partnered with Google Cloud to build agentic AI for trade monitoring, anomaly detection, and compliance; estimates 40% fewer false positives and $5M annual compliance savings | PYMNTS | [pymnts.com](https://www.pymnts.com/news/artificial-intelligence/2026/deutsche-bank-google-build-ai-agents-patrol-trading/) | Yes |
| **Wells Fargo** | Tier 1 | US | Deployed AI agents workforce-wide via Google Cloud (Aug 2025); appointed Head of AI Products (Jan 2026); AI for contract management (250K docs), corporate banking insights | BusinessWire / PYMNTS | [pymnts.com](https://pymnts.com/news/artificial-intelligence/2025/wells-fargo-deploys-ai-agents-business-wide) | Yes |
| **JPMorgan Chase** | Tier 1 | US/Global | LLM Suite to 250K employees; $3B AI budget in 2026; $2B annual AI value; American Banker 2025 Innovation of the Year; aims to become "fully AI-connected enterprise" | CNBC / American Banker | [cnbc.com](https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html) | Yes |
| **DBS Bank** | Tier 1 | Singapore/Asia | World's Best AI Bank 2025; SGD 750M AI economic value in 2024, targeting SGD 1B in 2025; DBS Joy for 4,000 corporate clients; CSO Assistant to 500 agents | DBS press | [dbs.com](https://www.dbs.com/artificial-intelligence-machine-learning/artificial-intelligence/singapore-finTech-festival-2025-powering-dbs-next-phase-of-growth-with-ai.html) | Yes |
| **NatWest Group** | Tier 1 | UK | Implemented Amazon Q in Connect for contact center; pilot for top 10 customer call reasons; compliance and AHT reduction focus | AWS Blog | [aws.amazon.com](https://aws.amazon.com/blogs/contact-center/insights-and-learning-of-amazon-q-in-connect-at-natwest) | Yes |
| **Itaú Unibanco** | Tier 1 | Brazil | Migrated 50-year mainframe checking account platform serving 70M customers to AWS; sub-100ms latency, 99.99% uptime | AWS Blog | [aws.amazon.com](https://aws.amazon.com/blogs/industries/financial-institutions-advance-mission-critical-workloads-and-agentic-ai-at-reinvent-2025/) | Yes |
| **Nationwide Building Society** | Tier 1 | UK | Selected Pega Customer Decision Hub as one-to-one personalization partner; centralized decisioning brain for customer experience | PegaWorld 2025 | [pega.com](https://www.pega.com/insights/resources/pegaworld-2025-how-nationwide-building-society-selected-pega-customer-decision) | Yes |
| **Federal Bank** | Tier 2 | India | First bank in India to implement generative AI across platform; upgraded Feddy chatbot with Vertex AI/Dialogflow; 24/7 multilingual | Google Cloud case study | [cloud.google.com](https://cloud.google.com/customers/federalbank) | Yes |

---

## 4. Key Findings

### 4.1 Capability Level Reality Check

- **Almost no vendor is shipping genuine autonomous resolution today.** The vast majority of "AI agent" products in banking are chatbots (FAQ/navigation) or copilots (human-assist). Vendors marketing "agents" are typically shipping copilots with agent-level aspirations on their roadmap.
- **Vendors closest to autonomous resolution:**
  - **Pegasystems** — deepest operational model with real-time decisioning, case management, and audit trails, but primarily through deterministic rules augmented by GenAI, not LLM-native agents
  - **NICE CXone Mpower Agents** (Jun 2025) and **Genesys Agentic Virtual Agent** (Sep 2025) — first CX platforms to ship autonomous agent capabilities, but CX-generic rather than banking-domain-specific
  - **ServiceNow** — banking-specific dispute management agent with friendly fraud screening, but new and unproven at production scale
  - **Backbase** — agentic AI agents within Intelligence Fabric (Apr 2025), banking-domain-aware, but engagement-layer-only without core banking execution
  - **Salesforce Agentforce** — proactive autonomous agents with banking templates (2dx, 3.0), but CRM-centric operational model lacks banking depth
- **Bank-built solutions (BofA, JPM, Capital One, BNY)** are furthest along in deployment but are captive to their respective institutions and not productizable.

### 4.2 Scale and Revenue Hierarchy

The competitive field spans six orders of magnitude in revenue:

| Tier | Revenue Range | Players |
|---|---|---|
| Hyperscaler ($100B+) | $107B–$236B | Microsoft, AWS, Google |
| Mega-platform ($10B+) | $10.3B–$21.2B | Salesforce, ServiceNow, Fiserv, FIS |
| CX platform ($1B–$3B) | $1.1B–$2.9B | NICE, Genesys, Pega, Five9 |
| Banking platform ($100M–$1B) | $160M–$860M ARR | Temenos, Mambu, Newgen, Backbase, Verint |
| Specialist ($10M–$100M) | $90M funding–$160M+ funding | Kasisto, Personetics, Yellow.ai, Avaamo, Clinc |

### 4.3 Gartner MQ 2025 — Conversational AI Platforms

**Leaders:** boost.ai, Cognigy, Kore.ai, Google
**Challengers:** Yellow.ai
**Notable absences from Leaders:** AWS (dropped from previous year), Kasisto (not in Leaders), Salesforce (evaluated differently)

The MQ reflects the disruption from GenAI/agentic AI — multiple former leaders dropped out, and new entrants focused on agent autonomy rose.

### 4.4 Forrester — Conversational Banking 2026

Forrester's January 2026 report identifies three strategic scenarios for conversational banking:
1. Bank controls the conversational interface (current default)
2. Platform intermediaries control the interface (super-app model)
3. AI agents emerge as a new distribution layer for financial services (agentic commerce)

Banks face a strategic choice about whether conversational banking will be a feature of their app or the primary interface for financial services. Forrester notes trust gaps remain the key barrier.

---

## 5. Central Competitive Insight: Conversation Layer vs. Operational Model

This is the decisive axis of competition in agentic banking. Most vendors provide only the **AI interaction layer** — the ability to understand natural language, generate responses, and manage conversations. Very few provide the **operational model** — the domain knowledge, business rules, case management, governance framework, regulatory audit trail, and execution capabilities needed to actually resolve a banking situation.

### Who provides what:

| Layer | What It Includes | Who Provides It |
|---|---|---|
| **AI Interaction Layer Only** | NLU/NLG, conversation management, intent detection, channel orchestration, LLM gateway | Google CCAI, Amazon Connect/Q, Kasisto, Clinc, Avaamo, Haptik, Yellow.ai, Five9, AWS Bedrock Agents, Microsoft Copilot Studio |
| **Interaction Layer + CX Operational Model** | Above + contact center workflow, agent routing, quality management, workforce optimization | NICE, Genesys, Verint |
| **Interaction Layer + Partial Banking Operational Model** | Above + some banking domain knowledge, templates, or pre-built workflows for specific use cases | Salesforce Agentforce (CRM + banking templates), ServiceNow (dispute + onboarding agents), Personetics (financial insights + MCP Server), Backbase (engagement banking + agentic AI) |
| **Full Operational Model** | Case management engine, real-time decisioning, regulatory audit trails, banking-specific workflows (disputes, servicing, applications), compliance governance, domain rules | **Pegasystems** (deepest), Temenos (core-banking-side only), FIS/Fiserv (infrastructure-side only) |

### The Gap

No single vendor combines:
1. Modern AI agent capabilities (LLM-native reasoning, autonomous multi-step execution)
2. Banking domain knowledge (dispute rules, servicing workflows, compliance logic)
3. Operational governance (audit trails, regulatory compliance, explainability)
4. Core banking execution (ledger operations, settlement, account management)

**Pega comes closest** on the operational model side but lags on modern AI agent architecture. **Salesforce** and **ServiceNow** are closest on the platform side but lack banking domain depth. **Backbase** has the right architecture vision but lacks core banking execution. The hyperscalers (Google, AWS, Microsoft) provide powerful infrastructure but zero banking operational model.

This gap is the strategic opportunity.

---

## 6. Gaps and Unresolved Questions

### Research gaps requiring further investigation:

1. **HDFC Bank (Eva/India):** Could not retrieve current data on HDFC Bank's Eva chatbot status, interaction volumes, or 2025 capabilities. India-specific search returned no results. Requires direct source or India-focused research.

2. **Appian FY2025 revenue:** Could not independently verify Appian's 2025 financial results. Estimated at ~$600M based on prior trajectory. SEC filing needed.

3. **Australian banks (Westpac, ANZ, CBA, NAB):** No results returned for Australian bank AI agent investments despite known activity (NAB at AWS re:Invent, Westpac as Kasisto customer). Requires Australia-focused research.

4. **European banks (Santander, BBVA, ING, Nordea, Intesa):** Could not retrieve specific agentic AI signals from these banks despite known digital maturity. BBVA and Intesa referenced in Forrester as leading conversational banking but specific AI agent commitments unconfirmed.

5. **Morgan Stanley:** Absent from agentic AI announcements despite being a technology-forward investment bank. Status unclear.

6. **Autonomous dispute resolution in production:** No vendor or bank has disclosed a production deployment where AI agents autonomously resolve banking disputes end-to-end (receive claim → investigate → apply rules → determine outcome → execute resolution → generate audit record) without human approval. This use case remains aspirational industry-wide.

7. **Regulatory posture:** No major banking regulator (OCC, Fed, PRA, MAS, BaFin) has issued specific guidance on autonomous AI agent resolution of customer banking situations. The regulatory boundary for "autonomous" is undefined.

8. **SME/Business banking coverage:** Most disclosed AI agent deployments are consumer-focused. DBS Joy (corporate/SME) is an outlier. The business banking segment for AI agents is underpenetrated and under-researched.

9. **Pricing models:** Vendor pricing for agentic banking capabilities is opaque. Amazon Connect bundles AI into channel pricing. Salesforce charges $30/user/month for Copilot Studio. Pega pricing is enterprise-contract-based. Per-resolution or per-outcome pricing (which would align with agentic value) has not emerged.

10. **Vendor marketing vs. production reality:** Multiple vendors (NICE, Genesys, Salesforce, ServiceNow) launched "agent" products in 2025 with autonomous resolution claims. Production validation at banking-grade scale (millions of customer interactions, regulated environment, audit requirements) is unverified for all of them.

---

*Research compiled 15 March 2026. All URLs verified at time of research. Revenue figures sourced from SEC filings, earnings releases, or credible analyst estimates as cited. Product capability claims sourced from vendor documentation and press releases — not independently validated in production environments unless noted.*
