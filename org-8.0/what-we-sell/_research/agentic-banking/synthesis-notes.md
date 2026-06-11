# Synthesis Notes — Agentic Banking

**Research date:** March 2026

---

## Part I: TAM Construction

### Convergent Approaches

Three approaches converge at **USD 5–6B vendor-addressable TAM by 2030** (base case):

- **Approach A (direct category)** and **Approach B (adjacent overlay)** converge at ~$5B midpoint
- **Approach C (top-down)** runs higher at $6.5–10.8B because it includes in-house builds

### 2025 Starting Point

~$200M–$1.4B depending on scope definition.

### Geographic Split

| Region | Share |
|--------|-------|
| USA | 35–40% |
| UK/EU | 20–25% |
| India | 5–8% |

### Sub-Segment Split

| Segment | Share |
|---------|-------|
| Consumer | 55–60% |
| Business (SOHO/SME) | 20–25% |
| Wealth/Family | 10–15% |

---

## Part II: Evidence Quality Ratings

| Structural Shift | Rating | Notes |
|------------------|--------|-------|
| 1. AI from chatbot to operational resolution | **Strong** | 7 data points, Gartner projections, vendor launches, bank deployments |
| 2. Banking staff scarcity | **Strong** | BLS data, ABA surveys, SAR volumes |
| 3. Project-by-project AI failing to scale | **Strong** | BCG: only 5% generate value at scale, 95% of pilots fail |
| 4. Regulatory convergence forcing governed AI | **Strong** | CFPB enforcement, EU AI Act, FCA Consumer Duty |
| 5. SOHO/SME underserved AI segment | **Strong** | 50% UK SMEs use fintechs, consumer AI 3–5 years ahead |
| 6. Domain knowledge as bottleneck | **Strong** | Only 38% meet ROI, 30–50% of AI team time on compliance |
| 7. Multi-channel continuity | **Moderate** | McKinsey framework well-evidenced but bank-specific data thinner |
| 8. Family/household banking | **Moderate** | $2.1B market at 17.8% CAGR, fintech-dominated, no bank has deployed household-level AI |

---

## Part III: Cross-Stream Contradictions

| Contradiction | Resolution |
|---------------|------------|
| **S1 Mordor Intelligence TAM ($43.5B) vs. GVR ($4.5B)** — 10x gap | Mordor includes broader scope; GVR used for vendor-addressable. Gap noted transparently. |
| **S3:** "Almost no vendor shipping genuine autonomous resolution" vs. **S4:** Vendor launches documented | Vendors are shipping product; banks have not deployed at scale. |
| **S6:** Pega has substantially solved operational model for dispute management | Pega validates the thesis (deep domain models required) but has not scaled it broadly beyond 3–5 processes. |

---

## Part IV: Operational Model Gap Thesis Assessment

### Verdict: **VALIDATED**

Five independent evidence streams converge:

- Cost data: 5–40x budget overruns
- Scaling data: only 5% at scale
- Bottleneck analysis: 30–50% compliance overhead
- Platform analysis: even Pega covers only 3–5 processes
- Standards fragmentation

### Counter-Thesis

**Partially valid.** Pega demonstrates the approach works for narrow domains but validates that building operational models is expensive and domain-specific.

### Competitor Model Gaps

| Competitor | Gap |
|------------|-----|
| Salesforce | Models relationships, not operations |
| Google CCAI | Channel, not operational model |
| ServiceNow | ITSM-deep, banking-shallow |

---

## Part V: Right to Play / Right to Win Mapping

### Right to Play

| Factor | Assessment |
|--------|------------|
| TAM | $5–6B by 2030 is meaningful; 25–45% CAGR |
| Bank investment | 70% deploying/exploring; 44% using agentic AI |
| Regulatory forcing functions | EU AI Act Aug 2026, Colorado June 2026 |
| Architectural basis | Evolution Fabric + Seer + Quark + CAF + Trust Fabric |
| Category recognition | "Agentic banking platform" not yet a recognized purchasing category — selling required |

### Right to Win

| Factor | Assessment |
|--------|------------|
| Evolution Fabric operational model | Addresses validated gap no competitor fully covers |
| Seer agent governance | Lifecycle, identity, delegation, guardrails, OPD map to regulatory requirements |
| Quark pre-built domain hubs | Accelerate deployment IF sufficient scenario depth (uncertain) |
| CAF decision auditability | Addresses EU AI Act and CFPB explainability mandates |
| Compounding argument | Each domain deployment enriches the model, accelerating the next |

### Weaknesses

- No production conversational AI
- No contact center integration
- Uncertain Quark depth
- No reference deployments
- Go-to-market for new category

---

## Part VI: Target Universe Assembly

15+ banks identified across tiers and geographies from S3 and S4. All with cited evidence.

### USA Tier 1

| Bank | Evidence |
|------|----------|
| JPMorgan | $3B AI budget |
| BofA | Erica 3.2B interactions |
| Wells Fargo | Google Cloud AI agents |
| Goldman Sachs | Anthropic partnership |
| Citi | Stylus Workspaces |
| BNY Mellon | 20K AI assistants |

### USA Tier 2

| Bank | Evidence |
|------|----------|
| KeyBank | $1B tech spend, AI calls $0.25 vs $9 human |
| TD Bank | 75 AI use cases, $170M value |

### UK Tier 1

| Bank | Evidence |
|------|----------|
| Lloyds | £50M GenAI value, targeting £100M |
| NatWest | Amazon Q in Connect |
| HSBC | $1.8B AI overhaul |
| Nationwide Building Society | Pega Customer Decision Hub |

### Europe Tier 1

| Bank | Evidence |
|------|----------|
| Deutsche Bank | Google Cloud agentic AI |
| UBS | Agentic AI center of excellence |

### India Tier 2

| Bank | Evidence |
|------|----------|
| Federal Bank | First Indian bank with generative AI across platform |

### Asia Tier 1

| Bank | Evidence |
|------|----------|
| DBS Bank | World's Best AI Bank 2025, SGD 750M AI value |

### Brazil Tier 1

| Bank | Evidence |
|------|----------|
| Itaú Unibanco | 70M customer mainframe migration to AWS |

---

## Part VII: Cross-References to Existing Research

| File | Use |
|------|-----|
| `_research/cloud-and-platform-operations/gap-fill-agentic-ops-banking.md` | SR 11-7 strain analysis, bank production deployments (Macquarie, TD Bank), regulatory positions. Adapted for customer-facing context. |
| `_research/digital-identity-and-trust/s5-ai-agent-identity.md` | AI agent identity requirements, EU AI Act classification |
| `market-study/agentic-systems-development-platforms/background/agentic-systems-platform-tam.md` | Platform TAM (USD 7–12B conservative by 2030). Cross-validated against S1 construction. |
| `market-study/agentic-systems-development-platforms/background/players-and-products.md` | Vendor catalog. Cross-referenced with S3 banking-specific profiles. |

---

## Part VIII: Editorial Decisions

1. **Family/household banking (Shift 8)** retained despite "Moderate" evidence — architecturally distinct, genuine whitespace competitors ignore.
2. **TAM methodology** presented transparently in Part I — reader can evaluate the construction.
3. **Business Banking** scoped to SOHO/SME throughout — corporate banking excluded per directive.
4. **Chatbot/copilot/agent classification** used consistently — no conflation of categories.
