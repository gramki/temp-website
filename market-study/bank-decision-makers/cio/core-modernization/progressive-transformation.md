# Progressive Core Banking Transformation

**Beyond Sidecar and Replacement: A Practitioner's Guide**  
**Purpose:** Enable business teams to understand the full spectrum of transformation approaches  
**Date:** January 2026

---

## Executive Summary

Core banking transformation is not binary. Between "do nothing" and "rip-and-replace" lies a spectrum of progressive strategies that manage risk while delivering incremental value. This document catalogs these approaches with real-world examples, helping business teams understand **what's possible** beyond the two extremes that dominate vendor conversations.

**Key Insight:** The most successful transformations combine multiple approaches. DBS used at least four strategies over nine years. The "right" approach depends on your bank's size, risk tolerance, competitive pressure, and starting architecture.

---

## The Transformation Spectrum

```
LOW RISK / LOW DISRUPTION                                    HIGH RISK / HIGH DISRUPTION
├──────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  API         Channel      Data Layer    Functional    Product-by-   Sidecar    Full     │
│  Overlay     Refresh      Extraction    Carve-Out     Product       (Greenfield) Replace │
│                                                                                          │
└──────────────────────────────────────────────────────────────────────────────────────────┘
         ← Progressive Transformation Approaches →           ← Documented in other materials →
```

---

## 1. API LAYER / MIDDLEWARE OVERLAY

### Strategy Description

Add a modern API layer on top of the legacy core without replacing underlying systems. The overlay translates legacy protocols (batch files, screen scraping, proprietary interfaces) into modern REST/GraphQL APIs consumable by digital channels and partners.

### How It Works

1. Deploy integration platform (MuleSoft, Apigee, Kong, AWS API Gateway)
2. Build adapters that connect to legacy core interfaces
3. Expose standardized APIs for accounts, transactions, customers
4. Route all new channel development through API layer
5. Legacy core continues processing transactions unchanged

### Real-World Examples

| Bank | Approach | Outcome |
|------|----------|---------|
| **Capital One** | Built internal API platform ("Exchange") on top of mainframe | Enabled mobile-first development without core replacement; became tech talent attractor |
| **BBVA** | API Market platform exposed 100+ APIs | Created new revenue stream from API monetization; enabled BaaS partnerships |
| **Fidor Bank** (pre-acquisition) | "FidorOS" API layer over legacy | Attracted fintech partnerships; positioned for acquisition by BPCE |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ⚡ Moderate | Depends on core provider API maturity; may require vendor support |
| Mid-Size ($10-100B) | ✅ High | Sweet spot — sufficient scale to justify investment, manageable complexity |
| Large/Super-Regional ($100B+) | ✅ High | Often first step before broader transformation |
| GSIBs | ✅ High | Standard practice; most have mature API platforms already |

### Value Delivered

- **Time-to-market:** New channels/products in weeks vs. months
- **Partnership enablement:** Fintech/BaaS integrations without core changes
- **Risk profile:** Low — legacy core unchanged; rollback is simple
- **Cost:** $2-10M depending on scope and platform choice

### Limitations

- Does not address underlying batch processing constraints
- Performance limited by legacy system speed
- Technical debt remains; overlay adds another layer to maintain
- No cost reduction on core operations

---

## 2. CHANNEL MODERNIZATION

### Strategy Description

Replace customer-facing digital channels (mobile app, online banking, branch terminals) with modern platforms while keeping the legacy core as system of record. The new channel layer handles UX, session management, and orchestration; legacy handles transactions.

### How It Works

1. Deploy modern digital banking platform (Backbase, Temenos Infinity, Q2, Alkami)
2. Integrate to legacy core via APIs or adapters
3. Sunset legacy channel applications (often decades-old)
4. Implement new UX/UI progressively by journey (onboarding, payments, etc.)
5. Add capabilities not in legacy (PFM, notifications, biometrics) in new layer

### Real-World Examples

| Bank | Approach | Outcome |
|------|----------|---------|
| **Rabobank** | Backbase as digital engagement layer | 1M+ users on new platform; legacy core continues for transaction processing |
| **Navy Federal Credit Union** | Temenos Digital for member engagement | Improved NPS scores; progressive feature rollout without core changes |
| **BOK Financial** | Q2 platform for digital banking | Enhanced mobile experience; integrated wealth, retail, commercial |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ✅ High | Core providers (FIS, Fiserv, Jack Henry) offer bundled digital layers |
| Mid-Size ($10-100B) | ✅ High | Clear ROI in customer experience without core risk |
| Large/Super-Regional ($100B+) | ✅ High | Standard practice; often combined with API overlay |
| GSIBs | ⚡ Moderate | Usually build custom; may use for specific segments |

### Value Delivered

- **Customer experience:** Modern UX without waiting for core transformation
- **Feature velocity:** Add PFM, budgeting, notifications independent of core
- **Risk profile:** Low to moderate — integration complexity varies by legacy core
- **Cost:** $5-25M depending on scope and vendor

### Limitations

- Real-time constraints persist if core is batch-based
- Complex integrations for non-standard products
- Doesn't address regulatory reporting or back-office efficiency
- Customer experience limited by data available from legacy

---

## 3. DATA LAYER EXTRACTION

### Strategy Description

Extract core banking data to a modern data platform (data lake, warehouse, or real-time streaming layer) while legacy systems remain the transaction processor. The modern data layer enables analytics, AI/ML, regulatory reporting, and customer 360 views that legacy cannot support.

### How It Works

1. Implement Change Data Capture (CDC) from legacy core (Informatica, Talend, Debezium)
2. Stream transactions to modern data platform (Snowflake, Databricks, AWS/GCP/Azure)
3. Build unified data models for customers, accounts, transactions
4. Enable real-time and batch analytics on extracted data
5. Legacy core continues authoritative transaction processing

### Real-World Examples

| Bank | Approach | Outcome |
|------|----------|---------|
| **JPMorgan Chase** | Unified data platform extracting from multiple cores | Enabled AI/ML at scale; fraud detection improvements; customer 360 |
| **ING** | "Data Highway" streaming architecture | Real-time customer insights; personalization engine; regulatory reporting automation |
| **US Bank** | Cloud-based data lake with CDC from mainframe | Analytics transformation without core replacement; ML model deployment |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ⚡ Moderate | May leverage core provider data extracts; limited internal capability |
| Mid-Size ($10-100B) | ✅ High | Enables analytics/AI without core risk; clear competitive value |
| Large/Super-Regional ($100B+) | ✅ High | Essential for regulatory reporting, AML, personalization at scale |
| GSIBs | ✅ High | Standard practice; often multi-year enterprise data initiatives |

### Value Delivered

- **Analytics capability:** Customer 360, propensity models, churn prediction
- **Regulatory efficiency:** Automated reporting, stress testing data
- **AI/ML foundation:** Training data, feature stores, real-time inference
- **Risk profile:** Low to moderate — read-only from legacy; no transaction risk
- **Cost:** $10-50M+ depending on scope and platform

### Limitations

- Data latency depends on CDC frequency (near-real-time vs. batch)
- Data quality issues in legacy surface in new platform
- Does not improve transaction processing speed
- Governance and lineage complexity across two worlds

---

## 4. FUNCTIONAL CARVE-OUT (Decomposition)

### Strategy Description

Extract specific functional domains (payments, cards, lending, deposits) from the monolithic core to purpose-built modern platforms while the legacy core handles remaining functions. Over time, legacy shrinks as more functions migrate out.

### How It Works

1. Identify target function for carve-out (often payments or cards first)
2. Select specialized platform (e.g., Zeta for cards, FIS/ACI for payments)
3. Build integration layer between legacy core and new platform
4. Migrate function with cutover or parallel run
5. Legacy core retains general ledger, deposits, or other functions
6. Repeat for additional functions over multi-year roadmap

### Real-World Examples

| Bank | Function Carved Out | Platform | Outcome |
|------|---------------------|----------|---------|
| **First Horizon Bank** | Line of business (not disclosed) | Finxact | First regional US bank to migrate a LoB to next-gen; incremental approach validated |
| **Live Oak Bank** | Deposits (first), Loans (planned) | Finxact | Eliminated batch processing for deposits; controlled expansion |
| **SEB (Sweden)** | Card processing | Modern card platform | Card operations modernized; core banking unchanged |
| **Multiple US banks** | Payments hub | ACI, FIS, Volante | ISO 20022 readiness without core changes; FedNow/RTP enablement |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ✅ High | Payments hub for FedNow is common first step |
| Mid-Size ($10-100B) | ✅ High | Ideal for controlled transformation; can start with one product line |
| Large/Super-Regional ($100B+) | ✅ High | Orchestrator model per McKinsey; standard approach for Tier 1 |
| GSIBs | ✅ High | Long-standing practice; cards, payments, securities often on separate platforms |

### Value Delivered

- **Targeted modernization:** Focus investment where value is highest
- **Reduced risk:** Smaller scope = more manageable migrations
- **Specialized capability:** Best-of-breed for each function vs. monolith compromises
- **Incremental value:** Each carve-out delivers before next begins
- **Cost:** Varies by function; $20-100M per major carve-out

### Limitations

- Integration complexity between legacy and modern platforms
- Data consistency challenges during transition
- May create "spaghetti" of point-to-point integrations without orchestration layer
- End-state architecture must be planned to avoid technical debt

---

## 5. PRODUCT-BY-PRODUCT MIGRATION

### Strategy Description

Migrate specific product portfolios (savings accounts, CDs, mortgages, auto loans) from legacy core to modern platform one at a time. Each product migration is a complete cutover for that product, with other products remaining on legacy until their turn.

### How It Works

1. Select first product for migration (often simple savings or new product)
2. Configure product on target core platform
3. Migrate customer and account data for that product
4. Cutover transaction processing to new platform
5. Decommission product on legacy core
6. Repeat for next product in priority sequence

### Real-World Examples

| Bank | Approach | Outcome |
|------|----------|---------|
| **Lloyds Banking Group** | Started with Intelligent Finance (500K customers) | Validated platform; lessons applied to broader migration |
| **Isybank (Intesa Sanpaolo)** | Launched with specific product set | 12-month launch; validation for main bank migration |
| **Community banks (various)** | New CD or savings products on modern platform | Test modern core without migrating existing books |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ⚡ Moderate | Simpler product sets; but may lack scale to justify dual cores |
| Mid-Size ($10-100B) | ✅ High | Can afford dual operation; clear path from simple to complex products |
| Large/Super-Regional ($100B+) | ✅ High | Standard approach; often 5-10 year roadmap across product lines |
| GSIBs | ⚡ Moderate | Products are often already on specialized platforms |

### Value Delivered

- **Learning curve:** Build migration capability on simpler products first
- **De-risked approach:** Failure on one product doesn't affect others
- **Continuous value:** Each migrated product delivers modern capabilities
- **Risk profile:** Moderate — each product migration is a mini-program
- **Cost:** $10-50M per product migration depending on complexity

### Limitations

- Customer fragmentation: Same customer may have products on different platforms
- Unified customer view requires integration layer
- Long timeline to complete full migration
- Complexity increases for products with dependencies (e.g., overdraft linked to checking)

---

## 6. CUSTOMER SEGMENT MIGRATION

### Strategy Description

Migrate specific customer cohorts to modern platform based on segment characteristics (new-to-bank, digital-only, specific geography, employee testing). Segment receives full modern experience; other customers remain on legacy until migrated.

### How It Works

1. Define target segment (often: new customers first)
2. Configure full product suite on modern platform for that segment
3. Route segment acquisition and onboarding to new platform
4. Migrate existing customers in segment if applicable
5. Expand segment criteria over time until legacy is emptied

### Real-World Examples

| Bank | Segment Strategy | Outcome |
|------|------------------|---------|
| **DBS** | New digital customers routed to modern infrastructure | Digital customers bring 2x income; grew from 33% to 48% of base |
| **BBVA (Spain)** | Mobile-first customers on modern stack | Validated platform before broader rollout |
| **Chase UK** | Entire new market (UK) on modern core | Clean-sheet design; lessons inform US transformation |
| **Standard Chartered (Mox)** | New Hong Kong digital customers | 550K customers; platform replicated for Trust Bank Singapore |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ⚡ Moderate | Smaller customer base; segment economics may not justify |
| Mid-Size ($10-100B) | ✅ High | New customer acquisition on modern core is low-risk starting point |
| Large/Super-Regional ($100B+) | ✅ High | Can sustain dual operations; clear segment strategies |
| GSIBs | ✅ High | Often combined with geographic or line-of-business segmentation |

### Value Delivered

- **Clean customer experience:** No migration artifacts for new customers
- **Natural runoff:** Legacy customer base shrinks over time
- **Competitive positioning:** Modern experience for target demographics
- **Risk profile:** Low to moderate — new customers only initially
- **Cost:** Platform investment + dual operations; $30-100M+

### Limitations

- Dual operations cost until legacy empties (may be 10+ years)
- Existing customer migration still required eventually
- Same customer may have relationships on both platforms
- Requires clear segment definition and routing logic

---

## 7. HOLLOW CORE / CORE ABSTRACTION

### Strategy Description

Reduce legacy core to minimal "thin" transaction processor by extracting all business logic, product configuration, and orchestration to modern platforms. Legacy becomes a highly reliable, simple ledger; intelligence lives elsewhere.

### How It Works

1. Build or deploy modern orchestration/decisioning layer
2. Extract product rules, pricing logic, fee calculations to external engines
3. Extract customer data, relationship logic to modern CRM/MDM
4. Extract workflow and process logic to BPM platforms
5. Legacy core handles only: post transactions, maintain balances, close positions
6. All intelligence and flexibility resides in modern layer

### Real-World Examples

| Bank | Approach | Outcome |
|------|----------|---------|
| **Capital One** | Extensive extraction of business logic from mainframe | Mainframe handles transactions; pricing, offers, decisions in modern cloud services |
| **Several European banks** | BPM-driven processes with legacy posting | Workflow flexibility without core replacement |
| **Various via Zafin** | Product and pricing externalization | Product agility without core changes; Zafin manages pricing/packaging |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ❌ Low | Complexity exceeds capability; over-engineered for scale |
| Mid-Size ($10-100B) | ⚡ Moderate | May be appropriate for specific functions (pricing externalization) |
| Large/Super-Regional ($100B+) | ✅ High | Viable long-term architecture; reduces core dependency |
| GSIBs | ✅ High | Common pattern; enables best-of-breed in each layer |

### Value Delivered

- **Business agility:** Product and pricing changes without core modifications
- **Extended legacy life:** Core can run for decades more in simplified state
- **Incremental investment:** Extract functions as needed vs. big-bang
- **Risk profile:** Moderate — integration complexity; but no core replatforming
- **Cost:** $20-100M+ depending on scope; distributed over years

### Limitations

- Architectural complexity; requires strong enterprise architecture capability
- Integration and data consistency challenges
- Latency from orchestration layer to core
- May be "kicking the can" if core must eventually be replaced

---

## 8. PARALLEL CORE / DUAL RUNNING

### Strategy Description

Operate modern core alongside legacy for extended period, with clear rules for which platform handles which customers/products. Unlike "sidecar" (greenfield digital bank), parallel core means running equivalent capabilities on both platforms with intent to eventually consolidate.

### How It Works

1. Deploy modern core for subset of products/customers
2. Operate both cores with shared customer data layer or integration
3. Migrate customers/products incrementally based on lifecycle events
4. Validate modern core under production load
5. Expand modern core scope until legacy can be decommissioned

### Real-World Examples

| Bank | Approach | Outcome |
|------|----------|---------|
| **Commonwealth Bank of Australia** | 5-year parallel operation during migration | Real-time for new accounts; batch for legacy; 50% cost gap closed |
| **Mambu clients (various)** | "Dual core (shared legacy)" approach | Progressive migration based on customer lifecycle events |
| **First Horizon** | LoB on Finxact while main operations on legacy | Controlled expansion; proof point before broader migration |

### Applicability by Bank Segment

| Segment | Fit | Rationale |
|---------|-----|-----------|
| Community (<$10B) | ❌ Low | Dual core economics rarely work at this scale |
| Mid-Size ($10-100B) | ⚡ Moderate | Possible if tied to specific growth strategy or acquisition |
| Large/Super-Regional ($100B+) | ✅ High | Standard for de-risked transformation |
| GSIBs | ✅ High | Often multiple cores already; adding modern core is incremental |

### Value Delivered

- **Production validation:** Modern core proves under real load before full migration
- **Fallback option:** Legacy core remains if modern core fails
- **Gradual learning:** Organization builds capability over time
- **Risk profile:** Moderate to high — dual operations complexity
- **Cost:** 1.5-2x steady-state operations during overlap; $50-200M+ for program

### Limitations

- Extended dual operations cost
- Integration and data synchronization complexity
- Staff must maintain expertise in both platforms
- Potential for "never-ending" dual state if migration stalls

---

## Comparison Matrix: All Progressive Approaches

| Approach | Risk Level | Investment | Time to Value | Core Expertise Required | Best First Step For |
|----------|------------|------------|---------------|------------------------|---------------------|
| API Overlay | Low | $2-10M | 3-6 months | Low | Digital partnerships, mobile app refresh |
| Channel Modernization | Low-Medium | $5-25M | 6-12 months | Low | Customer experience improvement |
| Data Layer Extraction | Low-Medium | $10-50M | 6-18 months | Medium | Analytics, AI/ML, regulatory reporting |
| Functional Carve-Out | Medium | $20-100M per function | 12-24 months | High | Payments modernization, FedNow/RTP |
| Product-by-Product | Medium | $10-50M per product | 12-24 months | High | Simple products (savings, CDs) |
| Customer Segment | Medium | $30-100M+ | 12-18 months | High | New customer acquisition |
| Hollow Core | Medium-High | $20-100M+ | 18-36 months | Very High | Product/pricing flexibility |
| Parallel Core | High | $50-200M+ | 24-60 months | Very High | De-risked full transformation |

---

## Recommended Approach by Bank Segment

### Community Banks (<$10B Assets)

**Recommended Starting Points:**
1. **Channel Modernization** — Core provider digital banking upgrade
2. **Functional Carve-Out (Payments)** — FedNow/RTP via payments hub
3. **API Overlay** — If core provider supports; enables fintech partnerships

**Avoid:** Hollow core, parallel core, full replacements — complexity exceeds organizational capability and economics rarely justify.

**Key Vendors to Explore:** 
- Digital: Alkami, Q2, NCR Digital Banking
- Payments: FIS, Jack Henry, core provider payment hubs
- APIs: Core provider API offerings (Fiserv, FIS, Jack Henry increasingly capable)

---

### Mid-Size Banks ($10B-$100B Assets)

**Recommended Starting Points:**
1. **Data Layer Extraction** — Enable analytics/AI without core risk
2. **Functional Carve-Out** — Payments or cards as first domain
3. **Customer Segment Migration** — New customers to modern core

**Build Toward:** Product-by-product migration or parallel core if competitive pressure demands.

**Key Vendors to Explore:**
- Data: Snowflake, Databricks, cloud-native platforms
- Payments: ACI, Volante, FIS
- Cards: Zeta, Marqeta, i2c
- Modern cores (for segment/product): Finxact, Mambu, Temenos

---

### Large/Super-Regional Banks ($100B+ Assets)

**Recommended Starting Points:**
1. **API Overlay + Data Extraction** — Foundation for all else
2. **Functional Carve-Out (multiple domains)** — Orchestrator architecture per McKinsey
3. **Customer Segment Migration** — Greenfield digital for new/digital-first segments

**Build Toward:** Hollow core or parallel core as multi-year end-state.

**Key Vendors to Explore:**
- Orchestration: MuleSoft, Apigee, internal platforms
- Data: Snowflake, Databricks, cloud-native
- Modern cores: Thought Machine, 10x, Temenos
- Specialist platforms: Zeta (cards), ACI (payments), Zafin (product/pricing)

---

### GSIBs (Systemically Important Banks)

**Standard Practice:**
- Most already have functional carve-outs (cards, payments, securities separate)
- API platforms mature; data platforms mature
- Focus on: next-gen cores for specific lines of business, AI-readiness, regulatory efficiency

**Current Patterns:**
- JPMorgan: Thought Machine for specific applications; greenfield (Chase UK) on 10x
- Standard Chartered: Mox (Thought Machine) for digital; replication model
- Large European banks: Temenos, Thought Machine for digital entities

---

## Combining Approaches: The DBS Example

DBS Bank's transformation (2009-2018) is instructive because it combined multiple progressive approaches over nine years:

| Phase | Approach Used | Outcome |
|-------|---------------|---------|
| 2009-2012 | Channel Modernization | New mobile/online platforms; legacy core unchanged |
| 2012-2014 | Data Layer Extraction | Customer 360; analytics foundation |
| 2014-2016 | Functional Carve-Out | Payments, specific product domains modernized |
| 2016-2018 | Customer Segment Migration | Digital customers to modern infrastructure |
| Ongoing | Hollow Core elements | Business logic increasingly in modern services |

**Result:** 
- ROE: 16.3% (record)
- Cost-income ratio: 40%
- 99% of apps cloud-native or cloud-enabled
- Digital customers: 48% of base, 2x income contribution
- Named "World's Best Bank" (Global Finance), "World's Best Digital Bank" (Euromoney)

**Key Lesson:** No single approach; sequenced combination over multi-year horizon.

---

## Decision Framework: Choosing Your Approach

### Step 1: Assess Your Starting Point

| Question | If Yes → Consider |
|----------|-------------------|
| Do we have modern APIs exposing core capabilities? | If no → API Overlay first |
| Is our digital experience competitive? | If no → Channel Modernization |
| Can we do analytics/AI on core data? | If no → Data Layer Extraction |
| Do we need FedNow/RTP/instant payments? | If yes → Payments Carve-Out |
| Are we losing digital-first customers? | If yes → Customer Segment Migration |

### Step 2: Match to Your Constraints

| Constraint | Implication |
|------------|-------------|
| Limited IT capability | Favor vendor-supported approaches (Channel, API via core provider) |
| Limited capital | Start with lowest-cost approaches (API Overlay, Channel) |
| Competitive pressure (urgent) | Customer Segment or Functional Carve-Out for faster impact |
| Regulatory pressure | Data Extraction (reporting), Payments Carve-Out (FedNow) |
| Board risk aversion | API Overlay, Channel — no core transaction risk |

### Step 3: Sequence for Value

**General Sequencing Principle:**
1. **Foundation:** API Overlay + Data Extraction (enables all else)
2. **Quick wins:** Channel Modernization (visible customer impact)
3. **Strategic capability:** Functional Carve-Out (payments, cards)
4. **Competitive positioning:** Customer Segment Migration
5. **End-state architecture:** Hollow Core or Parallel Core (optional, long-term)

---

## Key Takeaways for Business Teams

1. **Transformation is not binary.** Between "keep legacy" and "replace legacy" are 8+ proven approaches with different risk/reward profiles.

2. **Start with foundation, not core.** API layer and data extraction unlock value without touching transaction processing.

3. **Sequence matters.** Build capability and confidence with lower-risk approaches before attempting product or customer migrations.

4. **Combine approaches.** Successful transformations (DBS, CBA, JPMorgan) use multiple strategies sequenced over years.

5. **Match approach to segment.** Community banks should not attempt what GSIBs do; mid-size banks have the most options.

6. **Plan for dual operations.** Any progressive approach means running old and new simultaneously — budget and staff accordingly.

7. **Measure incrementally.** Each approach should have clear success metrics and decision points to expand or adjust.

---

## References

- McKinsey: "How to get a core banking transformation right" (2023)
- McKinsey: "Core systems strategy for banks" 
- Mambu: "Progressive Migration" methodology documentation
- Thought Machine: Migration playbook and case studies
- Finxact: Incremental modernization approach
- Federal Reserve Bank of Kansas City: "Core Banking Systems and Options for Modernization" (2024)
- DBS Bank case studies: Harvard, MIT Sloan, Singapore Management University
- CBA Core Banking Modernisation program documentation
- Industry analyst coverage: Celent, Aite-Novarica, Gartner

---

*This document provides strategic context. Individual approach selection requires assessment of your bank's specific architecture, capabilities, competitive position, and risk tolerance.*
