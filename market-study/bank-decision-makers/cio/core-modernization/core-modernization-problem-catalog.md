# Core Banking Modernization: Problem Catalog by Bank Segment

**Purpose:** Quick-reference catalog of problems modernization addresses, with evidence on delivered value  
**Format:** Scannable tables; detailed problem briefs in linked documents  
**Date:** January 2026

---

## How to Read This Document

| Column | Description |
|--------|-------------|
| **Problem** | Specific pain point or limitation |
| **Perceived Value** | Expected benefit (High/Medium/Low + descriptor) |
| **Bank Beneficiaries** | Internal stakeholders who gain |
| **Customer Beneficiaries** | End-customer segments affected |
| **Migration Reality** | Is value delivered? Evidence from actual migrations |

---

## 1. TECHNOLOGY & IT SEGMENT

### 1.1 Talent & Skills

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **COBOL talent cliff** — 65% of mainframe workers retiring soon; average age 50-70 | **HIGH** — Existential risk mitigation | CIO, IT Operations, Risk | None directly | ⚠️ **Deferred, not solved.** New skills gap emerges (cloud-native, Kubernetes). Banks report 71% understaffed post-migration on new platforms. |
| **Developer productivity** — Legacy code maintenance consumes 70-80% of IT budget | **HIGH** — Cost reallocation to innovation | CIO, Dev Teams | Indirect (faster features) | ⚡ **Partially delivered.** Modern cores reduce code (10x: 2,000 lines vs. legacy). But migration absorbs ~40% of program spend; net savings take 3-5 years. |
| **Talent attraction** — Modern developers avoid COBOL/mainframe roles | **MEDIUM** — Workforce sustainability | HR, IT Leadership | None | ✅ **Generally validated.** Cloud-native platforms attract talent. Chase UK, Mox cited as talent magnets. |

### 1.2 Architecture & Integration

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **Monolithic architecture** — Changes require full regression; tightly coupled systems | **HIGH** — Agility, reduced change risk | CIO, Enterprise Arch, Dev Teams | Indirect | ⚡ **Mixed results.** Microservices enable isolation but introduce distributed system complexity. DBS succeeded; many banks underestimate integration overhead. |
| **API limitations** — Legacy cores lack modern APIs for fintech/BaaS partnerships | **HIGH** — Enable embedded finance, partnerships | Digital, Partnerships, Revenue | SMB (BaaS), Digital-first consumers | ✅ **Strong evidence.** Westpac (10x), ONE Finance/Walmart (Finxact) prove API-first enables partnerships impossible on legacy. |
| **Cloud migration blockers** — Mainframe workloads can't move to cloud-native infra | **MEDIUM** — Infra cost optimization | IT Infrastructure, CFO | None | ⚠️ **Slower than promised.** CBA took 5 years, $1B+. Cloud benefits require full platform shift, not just hosting. |
| **Batch processing constraints** — Nightly batch windows limit real-time capabilities | **HIGH** — Enable real-time banking | IT Ops, Product, Compliance | All (real-time balances) | ✅ **Validated.** CBA eliminated 2-3 day account opening. Mox: 7-second credit decisions. Real-time is achievable. |

### 1.3 Security & Compliance

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **Compliance update velocity** — Regulatory changes require months of core updates | **MEDIUM** — Faster compliance, lower risk | Compliance, Legal, IT | None | ⚡ **Partially delivered.** Temenos: 347 go-lives in 2024 with regulatory pre-configuration. But customization still adds time. |
| **Security patching burden** — Legacy systems harder to patch, maintain security posture | **MEDIUM** — Reduced vulnerability window | CISO, IT Security | All (data protection) | ⚠️ **Not proven.** Modern platforms have different, not fewer, security challenges. Cloud config errors emerging as new risk class. |

---

## 2. OPERATIONS SEGMENT (COO Domain)

### 2.1 Cost Structure

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **High cost-per-account** — Legacy ops: $210/customer vs. neobanks: $25-63 | **HIGH** — Dramatic cost reduction | CFO, COO, Shareholders | Indirect (lower fees possible) | ❌ **Largely overstated.** McKinsey: 10x comparison is "apples-to-oranges" — compares greenfield fintechs to migrated incumbents. Post-migration, 73% found cost management harder (IBM). |
| **Manual processing overhead** — Batch-driven workflows require manual exception handling | **MEDIUM** — Straight-through processing | Ops Teams, Branch Staff | Faster service | ✅ **Validated.** Mox: 80% straight-through credit processing. Automation gains are real for greenfield. Migration to existing products retains complexity. |
| **Vendor maintenance fees** — Legacy providers charge premium for declining value | **MEDIUM** — Cost avoidance | Procurement, CFO | None | ⚠️ **Traded, not eliminated.** New vendors have different pricing models. Some banks report higher total ownership on modern platforms. |

### 2.2 Operational Resilience

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **System stability** — Aging infrastructure increases outage risk | **MEDIUM** — Improved uptime | IT Ops, Risk, COO | All | ❌ **Counter-evidence strong.** TSB: 1.9M customers locked out. McKinsey: "Legacy cores have proven reliable for decades." Modern platforms introduce new failure modes. |
| **Disaster recovery limitations** — Legacy DR is costly, slow to failover | **MEDIUM** — Faster recovery | IT Ops, Risk | All | ✅ **Cloud advantage real.** Multi-region cloud architectures improve RPO/RTO. CBA, DBS cite resilience improvements. |
| **Scalability constraints** — Legacy can't handle transaction volume spikes | **MEDIUM** — Elastic scaling | IT Ops, Product | High-transaction customers | ⚡ **Context-dependent.** Cloud elasticity proven for new digital banks. Migration doesn't automatically solve for existing workloads without rearchitecture. |

---

## 3. BUSINESS LINE SEGMENT

### 3.1 Product Innovation

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **Time-to-market** — Legacy: 6-18 months; modern: 2-3 months for new products | **HIGH** — Competitive response, revenue capture | Product, Marketing, Revenue | Digital-first, Gen Z/Millennials | ✅ **Best-validated claim.** Shawbrook: 9 months from contract to launch. Kuady: multi-country launch in <9 months. Mascoma Bank CEO cites Amazon's "every 8 seconds" as benchmark. |
| **Product rigidity** — Core constrains product design (fees, rates, terms) | **HIGH** — Product differentiation | Product, Marketing | All seeking personalization | ✅ **Validated.** Thought Machine Smart Contracts, Temenos Model Bank enable product flexibility. Isybank launched customized products in 12 months. |
| **Limited personalization** — Can't tailor pricing/rewards to customer segments | **HIGH** — Revenue, retention | Product, Marketing, Analytics | High-value, relationship customers | ⚡ **Capability delivered; execution varies.** Platform enables personalization; governance and analytics maturity determine actual use. |
| **Annual release cycles** — Vendor upgrades once/year vs. daily deployment capability | **MEDIUM** — Continuous improvement | Product, Digital | All | ✅ **Validated.** Modern platforms enable CI/CD. But organizational change management often lags technical capability. |

### 3.2 Channel Experience

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **Digital experience gaps** — Legacy cores can't support modern app experiences | **HIGH** — Retention, acquisition | Digital, Marketing | Mobile-first, young demographics | ⚡ **Partially delivered.** API-first cores enable better apps. But UX is front-end driven; core is enabler, not solution. |
| **Omnichannel inconsistency** — Different balances/states across channels | **MEDIUM** — Customer trust | Ops, Digital, Branch | All | ✅ **Validated.** Real-time cores eliminate reconciliation. Single source of truth is achievable. |
| **Instant payments friction** — Legacy can't post FedNow/RTP in real-time | **HIGH** — Competitive parity | Payments, Product | SMB, instant-payment users | ⚡ **Sidecar solves.** 78% of FedNow participants are community banks using sidecar approaches, not full core replacement. |

### 3.3 Revenue & Growth

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **Embedded finance exclusion** — Can't participate in BaaS/embedded economy | **HIGH** — New revenue streams | Strategy, Partnerships | SMB, retail via partners | ✅ **Proven.** ONE Finance (Walmart), Westpac BaaS demonstrate new revenue models. Requires modern core + partner ecosystem. |
| **Cross-sell limitations** — Can't create unified customer view for offers | **MEDIUM** — Revenue per customer | Analytics, Product, Sales | Relationship customers | ⚡ **Enabling, not solving.** Core provides data; analytics/AI capabilities determine cross-sell effectiveness. DBS: digital customers bring 2x income. |

---

## 4. EXECUTIVE/STRATEGIC SEGMENT

### 4.1 Competitive Position

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **Fintech competitive threat** — 60% of leaders cite fintechs as significant threat | **HIGH** — Strategic relevance | CEO, Board, Strategy | Digital-first segments | ⚠️ **Threat real; solution uncertain.** Core modernization is necessary but not sufficient. Execution, culture, talent matter more (DBS case). |
| **AI/GenAI exclusion** — Legacy can't support AI at scale | **HIGH** — Future capability | CIO, CEO, Chief Digital Officer | All (via AI-driven experiences) | ⚡ **Emerging.** IBM: "Flexible modular system is necessity for AI ROI." Temenos GenAI Copilot shows potential. Too early for migration evidence. |
| **Acquisition/merger friction** — Integration of acquired banks is costly | **MEDIUM** — M&A efficiency | CFO, Strategy, M&A | None | ⚡ **Mixed.** Modern platforms easier to integrate in theory. TSB counter-example: migration as part of acquisition was catastrophic. |

### 4.2 Stakeholder Value

| Problem | Perceived Value | Bank Beneficiaries | Customer Beneficiaries | Migration Reality |
|---------|-----------------|-------------------|------------------------|-------------------|
| **Shareholder return drag** — High cost structure limits ROE | **HIGH** — Valuation improvement | CEO, CFO, Shareholders | None | ⚡ **Rare success.** DBS: ROE 16.3%, cost-income ratio 40%. CBA closed 50% of cost gap. But these are 5-10 year transformations with exceptional execution. |
| **Innovation perception** — Seen as "legacy bank" vs. modern competitors | **MEDIUM** — Brand, talent, partnerships | CEO, CMO, HR | None | ✅ **Achieved by leaders.** DBS "World's Best Digital Bank" improved brand. Chase UK positioned as innovative despite parent legacy. |

---

## 5. SEGMENT-SPECIFIC PRIORITIES (By Bank Size)

### 5.1 Community Banks (<$10B Assets)

| Priority Problems | Why These | Migration Reality |
|-------------------|-----------|-------------------|
| 1. **Instant payments enablement** (FedNow/RTP) | Competitive parity; customer expectation | ✅ Sidecar approaches work; 78% of FedNow participants are community banks without full replacement |
| 2. **Digital account opening** | Branch-to-digital transition | ✅ Can be achieved via middleware/overlays without core replacement |
| 3. **Fee personalization for relationship banking** | Retention, differentiation | ⚡ Possible via tier configurations on existing cores |

**Key Learning:** Full core replacement rarely justified at this scale. Progressive modernization through existing provider upgrades is lower risk.

---

### 5.2 Mid-Size Banks ($10B-$100B Assets)

| Priority Problems | Why These | Migration Reality |
|-------------------|-----------|-------------------|
| 1. **Time-to-market** for new products | Direct fintech competition | ✅ Greenfield digital bank in <$100M, 9 months possible (McKinsey) |
| 2. **Deposit pricing personalization** | Rate competition, deposit retention | ⚡ Requires both core capability and governance maturity |
| 3. **API-enabled partnerships** | Embedded finance revenue | ✅ Modern cores enable; Finxact, Mambu show mid-size success |

**Key Learning:** Sidecar/parallel core strategy (new digital entity on modern core) is emerging best practice. Over half of mid-size banks favor progressive transformation.

---

### 5.3 Large/Super-Regional Banks ($100B+ Assets)

| Priority Problems | Why These | Migration Reality |
|-------------------|-----------|-------------------|
| 1. **Product innovation velocity** | Scaled fintech competition | ⚡ Possible but complex; Chase UK greenfield proves model |
| 2. **AI integration at scale** | Future competitive necessity | ⚠️ Too early for evidence; modern architecture is prerequisite |
| 3. **Operating cost transformation** | Margin pressure | ❌ Multi-year, $300-400M+ investment with uncertain ROI |

**Key Learning:** "Orchestrator approach" (insulate existing, extract data real-time, incremental migration) is recommended. Big-bang replacement carries unacceptable risk at this scale.

---

## 6. MIGRATION LEARNINGS SUMMARY

### What Consistently Delivers Value

| Claim | Evidence Rating | Notes |
|-------|-----------------|-------|
| Faster product launch (greenfield) | ✅ Strong | 9-18 months to market, validated across vendors |
| Real-time processing | ✅ Strong | Batch elimination proven (CBA, Mox, DBS) |
| API/partnership enablement | ✅ Strong | Embedded finance requires modern core |
| Product configurability | ✅ Strong | Smart Contracts, Model Bank concepts work |
| Developer productivity (new dev) | ✅ Moderate | Reduced codebase, modern tools attract talent |

### What Often Disappoints

| Claim | Evidence Rating | Notes |
|-------|-----------------|-------|
| Cost reduction (migrating bank) | ❌ Weak | 73% found cost management harder (IBM); "10x" is greenfield comparison |
| Operational stability (during/after) | ❌ Weak | TSB, others show migration risk; 70% transformations fail (BCG) |
| Short migration timelines | ❌ Weak | 30% achieve complete migration (McKinsey); multi-year is norm |
| AI/GenAI enablement | ⚠️ Too Early | Premise is sound; insufficient evidence from migrations |

### Critical Success Factors (From Documented Successes)

1. **CEO/Board commitment** — DBS, CBA, Isybank all had visible executive sponsorship
2. **Phased, multi-year approach** — Not "big bang"; DBS: 9 years; CBA: 5 years
3. **Greenfield-first strategy** — Prove platform on new entity before migration
4. **40% budget for migration** — Plan for this; under-estimation is #1 failure cause
5. **Legacy SME ringfencing** — "The more people understand how it currently works, the more likely you are to complete migration" (Thought Machine)
6. **Willingness to abort** — Successful programs have kill switches; TSB did not

---

## 7. BOTTOM LINE BY STAKEHOLDER

| Stakeholder | Core Question to Ask | Evidence-Based Answer |
|-------------|---------------------|----------------------|
| **CIO** | "Will this reduce my technical debt and talent risk?" | Maybe — trades one debt for another; talent crisis is real but 3-5 year window exists |
| **COO** | "Will this reduce operational costs?" | Unlikely in medium term — migration costs offset savings; operational risk is high |
| **Business Line** | "Will this let me launch products faster?" | Yes, if greenfield — validated consistently across vendors; migration of existing products is slower |
| **CEO/Board** | "Is this existential or optional?" | Not yet existential — COBOL talent cliff is the only non-negotiable driver; competitive threat is real but execution risk is equally real |

---

## References

- McKinsey: "Should US banks be moving to next-generation core banking platforms?" (2022)
- IBM Institute for Business Value: "The 94% core banking problem" (2024)
- BCG: Digital transformation failure rates research
- ABA: 2024 Core Platforms Survey
- Thought Machine, 10x, Temenos, Mambu, Finxact deployment case studies
- DBS Bank: Harvard/MIT/SMU case studies
- CBA: Core Banking Modernisation program documentation
- TSB: Slaughter & May independent review; FCA enforcement

---

*Next Steps: Detailed problem briefs for priority areas to be developed in individual documents.*
