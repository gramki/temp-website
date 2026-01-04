
# Modern Core Banking Provider  
## Market Study  
**An Evidence-Based Analysis of Next-Generation Core Banking Platforms**  
Deployments, Learnings, and Market Positioning  
December 2025  
*Industry Analyst Research Report*  
   
## Executive Summary  
The core banking technology market is undergoing a generational shift. Cloud-native platforms built on microservices architectures are increasingly replacing legacy mainframe systems that have powered banking for decades. This study examines the leading next-generation core banking providers, analyzing their deployment track records, documented outcomes, and key learnings from implementations worldwide.  

**Key findings from this research include:**  
- Greenfield digital bank launches consistently outperform legacy migration projects in terms of speed (12-18 months vs. multi-year) and risk profile  
- Migration complexity remains the dominant challenge, accounting for approximately 40% of overall program spend across all vendors  
- Strategic investor relationships signal commitment: Banks like JPMorgan Chase, Lloyds, Intesa Sanpaolo, and SEB have invested directly in their core provider (Thought Machine), creating deeper alignment than typical vendor relationships  
- The sidecar/parallel core strategy is gaining momentum: IDC projects 40% of global banks will pursue sidecar strategies by 2026  
- Market consolidation is evident: Fiserv acquired Finxact, traditional vendors (Temenos, FIS) are adding cloud-native capabilities, while pure-play cloud-native vendors (Thought Machine, 10x, Mambu) continue to win Tier 1 deals  

This report provides detailed analysis of five leading modern core providers: Thought Machine, 10x Banking, Temenos, Mambu, and Finxact/Fiserv, examining their deployment track records, target market segments, and documented learnings from implementations.  
   

---  

## 1. Thought Machine  
### 1.1 Company Overview  
Founded in 2014 by Paul Taylor, former Google head of text-to-speech, Thought Machine has positioned itself as the premium cloud-native core banking platform for Tier 1 institutions. The company was named a Leader in the 2025 Gartner Magic Quadrant for Retail Core Banking Systems, recognized for both Completeness of Vision and Ability to Execute.  

Vault Core, Thought Machine's primary platform, is trusted by leading banks and financial institutions worldwide, including Intesa Sanpaolo, ING Bank Śląski, Lloyds Banking Group, Standard Chartered, SEB, Lunar, Atom Bank, Curve, and JPMorgan Chase.  
_Notable pattern:_ Many of Thought Machine's customers have invested in the company's funding rounds (Lloyds, SEB, Intesa Sanpaolo, JPMorgan Chase), creating strategic alignment beyond typical vendor relationships.  

### 1.2 Major Deployments  
- **JPMorgan Chase (US & UK)**  
  - *Scale:* Vault Core deployment across Consumer & Community Banking, serving 66+ million US households  
  - *UK Approach:* Chase UK built from ground up on 10x core as a sidecar/greenfield, applying lessons to broader US migration  
  - *Strategic rationale (per CIO Rohan Amin):* Unify deposit, lending, and rewards relationships on single platform; enable real-time processing; support embedded banking via APIs  
- **Standard Chartered – Mox Bank (Hong Kong)**  
  - *Timeline:* 18 months from licensing to market deployment  
  - *Scale:* 550,000+ customers; 10%+ penetration of bankable population; 20% penetration among under-40 demographic  
  - *Processing performance:* 80% of credit applications processed straight-through; average credit decision in 7 seconds  
  - *Strategic value:* Tech stack replicated for Trust Bank Singapore; positioned as 'future operating model of Standard Chartered'  
- **Intesa Sanpaolo – Isybank (Italy)**  
  - *Timeline:* 12 months from deal initiation to go-live  
  - *Investment:* €5 billion technology program; €650 million for Isybank specifically; £40 million investment in Thought Machine  
  - *Expansion plan:* Migrate main bank to Isytech platform by end-2025/early-2026; private banking and wealth management in 2026  
  - *Validation:* 'Infrastructure has proven reliable; successfully tested with 20 million accounts'  
- **Lloyds Banking Group (UK)**  
  - *Partnership began:* 2018 with £11 million investment (10% stake)  
  - *Initial scope:* Migration of 500,000 customers from Intelligent Finance division  
  - *Strategic context:* Part of broader digital transformation serving nearly half of UK adult population  
- **Shawbrook Bank (UK) – 2025 Deployment**  
  - *Timeline:* Partnership began September 2024; first product (buy-to-let mortgage) launched May 2025 – under 9 months  
  - *Focus:* Commercial SME lending; demonstrates Vault Core versatility beyond retail banking  

### 1.3 Key Learnings from Thought Machine Deployments  
1. **Migration complexity dominates program costs:** Approximately 40% of overall program spend goes to migration from legacy systems. Custom tooling investment is essential for accuracy and efficiency.  
2. **Deep legacy knowledge is critical:** "The more people understand how it currently works, the more likely you are to complete your migration quickly and safely." Banks must ringfence key SMEs from day jobs and formally bring them into program structure.  
3. **Cloud-native skills must pre-exist:** Banks with existing cloud workloads experience minimal learning curves; those without require significant upfront investment in skills development.  
4. **Smart Contracts provide product autonomy:** Banks gain control to replicate existing products and launch new ones without vendor dependency, using developer-friendly code abstracted via configuration layer.  
5. **Greenfield implementations are faster and lower risk:** Mox (18 months), Isybank (12 months), and Shawbrook (9 months) demonstrate speed advantages of greenfield vs. legacy migration.  
   

---  

## 2. 10x Banking  
### 2.1 Company Overview  
Founded by Antony Jenkins, former CEO of Barclays, 10x Banking positions itself as "founded by bankers, built by technologists." The company raised $45 million in January 2024, led by BlackRock and JPMorgan. In July 2024, 10x launched what it calls the world's first "meta core" – a platform designed to bridge legacy and neo-core challenges.  

10x was named a Leader in both the IDC MarketScape: Asia/Pacific Digital Core Banking Platforms 2024 and the IDC MarketScape for EMEA Digital Core Banking Platforms. The company also became the first core banking platform to achieve B Corp certification.  

### 2.2 Major Deployments  
- **Chase UK:** Powers the UK's fastest-growing challenger bank, built from ground up on 10x core  
- **Westpac (Australia):** Banking-as-a-Service platform built on 10x 'SuperCore' technology, deployed on AWS  
- **Old Mutual (Africa):** First client in Africa; Africa's second-largest financial services company  
- 10x reports serving millions of end-customers globally through banks, mutuals, building societies, and banking-as-a-service partners.  

### 2.3 The 'Meta Core' Differentiator  
10x's meta core approach targets specific product or business use cases for a minimum viable product, which can then be scaled to include other products or business areas. This avoids a "big bang" cutover and its associated risks. Key claims include:  
- Banks can create and maintain as little as 2,000 lines of code for a single customized banking product  
- Up to 10x reduction in codebase compared to neo-core platforms; up to 10,000x reduction vs. legacy cores  
- ProductKit tool abstracts common product elements including core ledger  
- Interoperable with .NET, Java, Python and other programming languages  

### 2.4 2024 Milestones and Outlook  
- Increased commercial pipeline by over 300%  
- Maintained 100% gross revenue retention  
- New partnerships with Deloitte, LTI Mindtree, Suntec, Zafin, Alloy, and Flexys  
- Trained 60+ people through 10x Delivery Training and partner certification  
- On track to achieve profitability from second half of 2025  
   

---  

## 3. Temenos  
### 3.1 Company Overview  
Temenos is the established market leader with the largest installed base globally. The company was named Best Core Banking System at Banking Tech Awards 2025 (both global and USA), Best Core Banking Solution by Euromoney 2025, and best-selling core banking provider for the 20th consecutive year in the IBS Intelligence Sales League Table 2025. Trusted by over 950 banks worldwide.  

Temenos invests approximately 20% of revenues in R&D annually. Recent innovations include Gen AI Copilot for product design and optimization, and FCM AI Agent for sanctions screening with significantly reduced false positives.  

### 3.2 Deployment Scale and Approach  
Temenos reported 347 go-lives globally in 2024, including 47 in Asia Pacific. The company emphasizes "industrialized transformation" – a delivery methodology combining pre-configured model banks, partner integration frameworks, and reusable toolkits. Recent notable implementations include MUFG, Rabobank, Bank of Queensland, and Vietnam Maritime Commercial Joint Stock Bank.  

**Example: National Bank of Iraq**  
- *Timeline:* Implementation completed in less than one year  
- *Scope:* First in Capital Bank Group to adopt Temenos Payments  
- *Success factors:* Pre-configured capabilities and APIs minimized customization requirements  

**Example: IIG Bank (Malta)**  
- *Timeline:* Upgraded core banking to R24 AMR release December 2024; instant payments January 2025; SWIFT CBPR+ June 2025 – major go-lives within months  
- *Scope:* Instant payment module (TIPS) implemented within existing Temenos Payments Hub environment  

### 3.3 Market Position and Strategy  
Temenos offers both best-of-suite core banking and modular core solutions deployable on-premises, in the cloud, or as SaaS. The IDC MarketScape describes Temenos as a "universal soldier" suitable for any type of bank. The company's cloud-native, microservices-based architecture can evolve to accommodate new needs, enabling banks to compose, extend, and deploy banking capabilities at scale.  
   

---  

## 4. Mambu  
### 4.1 Company Overview  
Mambu pioneered the concept of "composable banking" over ten years ago. The company's SaaS cloud core banking platform powers digital banking propositions for over 200 customers in more than 65 countries, including traditional banks embracing transformation and greenfield "speedboat" propositions. Mambu was named to the CNBC World's Top Fintech Companies 2024 list and recognized as a Leader in digital core banking platforms in APAC.  

### 4.2 2024 Go-Lives and Notable Implementations  
Several banks, fintechs, and lenders went live on Mambu in 2024, many in less than nine months:  
- BridgeFund: Launched deposit services to expand account volumes and product offerings  
- Bank Muamalat (Malaysia): Partnered with Mambu and Google Cloud for personalized digital Islamic banking services  
- Kuady (Latin America): Multi-currency digital wallet launched across Peru, Chile, and Argentina in under 9 months  
- INDEXO (Latvia): Full-service banking experience launched in under one year; 10,000 customers acquired rapidly  
- Leeds Building Society: Pilot digital savings offering on Mambu Cloud Banking platform  

### 4.3 Migration Principles  
Based on 80+ migrations, Mambu advocates that "the future of core banking migration is incremental transformation aligned with business strategy and customer outcomes." The company identifies three primary migration routes:  
- Dual core (shared legacy): Progressive customer migration based on lifecycle events such as new products or rollovers  
- On the edge: New customer proposition and experience layer focused on acquisition, with aggressive migration of existing customers  
- Legacy replaced: Upgrading or replacing the monolithic legacy system, with selected core components replaced based on architecture roadmap  

### 4.4 Value Proposition  
Mambu claims 30% savings on typical integrations and upgrades and 35% savings on product customizations and changes. The platform enables test-and-learn methodology with minimal disruption. Mambu allocates up to 20% of product innovation budgets to resolving technical debt issues.  
   

---  

## 5. Finxact (Fiserv)  
### 5.1 Company Overview  
Finxact is a cloud-native, API-first core banking platform acquired by Fiserv. The platform is designed for banking, fintech, and embedded finance use cases. Finxact claims to rank #1 in production clients on next-gen banking tech in the US. The Fiserv integration provides access to broad ecosystem including card networks, payment rails, and the established Fiserv client base (Fiserv cores are used by a significant portion of US banks).  

### 5.2 Notable Deployments  
- First Horizon Bank: First regional bank in the US to convert an existing line of business from legacy core to Finxact  
- Live Oak Bank: Early adopter; moved deposits to Finxact to eliminate batch processing; positioned to migrate loans  
- ONE Finance (Walmart): Embedded financial services for one of world's largest retailers; enables consumers to save, spend, and borrow in one app  
- Thread Bank (2025): Selected Finxact to power embedded banking strategies; positioned as blueprint for community bank innovation  
- VirtualBank: Leveraging Finxact to build new digital partnerships and add value for customers  

### 5.3 Target Segments and Approach  
- **Large Financial Institutions:** Finxact uses an incremental, smaller-scope approach that minimizes risk and avoids disruption of complete core conversion. Can work alongside traditional core – bank can use Finxact to set up digital bank or new products, test results, then expand over time.  
- **Embedded Finance Providers:** System-of-record capabilities for retailers and businesses embedding financial services into customer experience.  
- **Community Banks and Credit Unions:** Levels playing field with largest banks and fintechs through access to modern, API-first platform.  
   

---  

## 6. Comparative Analysis  
### 6.1 Platform Comparison Matrix  

| Criteria              | Thought Machine             | 10x Banking                  | Temenos                 | Mambu                    | Finxact                  |
|-----------------------|----------------------------|------------------------------|-------------------------|--------------------------|--------------------------|
| **Primary Target**    | Tier 1 banks, digital banks| All bank sizes, mutuals, BaaS| Universal - all types   | Fintechs, digital banks, lenders | US banks, embedded finance |
| **Installed Base**    | Growing; major Tier 1 wins | Smaller but high-profile      | 950+ banks globally     | 200+ in 65 countries     | #1 US next-gen (claimed) |
| **Deployment Model**  | Cloud-native, multi-cloud, SaaS | Cloud-native SaaS         | On-prem, cloud, SaaS    | SaaS only                | Cloud-native, SaaS       |
| **Greenfield Speed**  | 9-18 months                | 12-18 months                 | <12 months possible     | <9 months                | Variable                 |
| **Key Differentiator**| Smart Contracts; Tier 1 credibility | Meta core; banker founder | Scale; proven track record | Composable; speed   | Fiserv ecosystem; US focus|

### 6.2 Common Success Factors  
Across all vendors, successful implementations share common characteristics:  
- **Executive sponsorship at C-level/Board:** Every major success story involves visible CEO or Board-level commitment  
- **Greenfield-first strategy:** Launch new digital entity, prove the platform, then expand – not "big bang" migration  
- **Strong partner ecosystem:** System integrators, specialist vendors, and technology partners extend capabilities  
- **Investment in talent:** Cloud-native skills, legacy system expertise, and change management capabilities  
- **Realistic expectations on migration:** 40% of program spend; multi-year timelines for legacy migration at scale  
   

---  

## 7. Conclusions and Recommendations  
### 7.1 Key Findings  
1. The sidecar/parallel core strategy has emerged as the dominant de-risking approach. Banks increasingly launch new digital entities or product lines on modern cores before attempting full migration.  
2. Speed-to-market claims are validated for greenfield deployments. Multiple vendors demonstrate 9–18 month greenfield launches. Legacy migration timelines remain multi-year.  
3. Vendor selection increasingly driven by strategic fit, not just features. Banks investing in vendor equity (Thought Machine model) signal deeper strategic alignment.  
4. Market bifurcation between "pure-play" cloud-native and "hybrid" vendors. Thought Machine, 10x, Mambu offer cloud-only; Temenos and Fiserv/Finxact provide on-prem, cloud, and SaaS options.  
5. Ecosystem partnerships are essential for success. No core vendor succeeds in isolation – system integrators, payments processors, and specialist vendors are critical.  

### 7.2 Recommendations by Bank Segment  
- **Tier 1/Super-Regional Banks ($100B+ assets):** Consider Thought Machine or 10x for greenfield digital bank; Temenos for hybrid deployment options. Prioritize vendors with proven Tier 1 implementations and investor relationships that signal long-term commitment.  
- **Mid-Size Banks ($10–100B assets):** Mambu or Finxact offer compelling speed and cost profiles. Consider greenfield approach with <$100M investment vs. full replacement. Partner ecosystem depth is critical.  
- **Community Banks (<$10B assets):** Finxact (via Fiserv relationship) or Mambu provide accessible entry points. Focus on progressive modernization through existing core provider upgrades before considering full replacement.  
- **Digital-First/Challenger Banks:** Thought Machine, 10x, or Mambu all have strong track records with neobanks and digital challengers. Speed-to-market and product configurability are primary selection criteria.  

### 7.3 Final Observation  
The question is no longer whether to modernize, but how to modernize with acceptable risk. The evidence suggests that greenfield/sidecar strategies, executive sponsorship, realistic migration expectations, and strong partner ecosystems are the common ingredients of success – regardless of which platform is selected.  
   

---  

## Sources and References  
- Thought Machine case studies and press releases ([thoughtmachine.net](https://thoughtmachine.net))  
- 10x Banking news releases and research reports ([10xbanking.com](https://10xbanking.com))  
- Temenos press releases and Banking Tech Awards announcements  
- Mambu 2024 Year in Review and customer announcements  
- Finxact/Fiserv press releases and customer case studies  
- IDC MarketScape reports for Digital Core Banking Platforms (EMEA, APAC, North America)  
- Gartner Magic Quadrant for Retail Core Banking Systems 2025  
- IBS Intelligence Sales League Table 2025  
- Accenture, McKinsey, and other consultancy research on core banking transformation  
- American Banker, Computer Weekly, Fintech Futures industry coverage  
- Company investor presentations and earnings materials  

— End of Report —
