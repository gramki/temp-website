# Gap-Fill Research: Customer-Centric Observability

**Date:** 2026-03-15
**Gap area:** Structural Shift 7 — Customer-centric observability replacing system-first monitoring
**Prior evidence rating:** Moderate
**Prior evidence basis:** PRA business service mapping requirement verified. Wells Fargo Elastic deployment. Gartner outcome-driven ops. But the "outside-in" concept had thin independent evidence beyond vendor claims and one regulator.
**Objective:** Find independent evidence to test whether the rating can be upgraded to Strong.

---

## Key Findings

- **Multi-regulator consensus, not single-regulator:** Five regulatory frameworks (PRA SS1/21, FCA PS21/3, DORA RTS 2024/1774, BCBS d516, RBI April 2024 guidance) independently mandate business-service-centric mapping that requires monitoring from the customer/business service perspective inward. This is not one regulator's position — it is global regulatory consensus.
- **FCA explicitly requires customer-outcome metrics:** FCA guidance states impact tolerances should be complemented with "additional metrics considering customer types, transaction values, criticality, and estimated losses" — directly mandating customer-outcome measurement beyond infrastructure health.
- **Wells Fargo is a multi-platform outside-in case study:** Wells Fargo has deployed four distinct tools (AppDynamics, Elastic, Grafana, Glassbox) with explicit customer-experience-driven monitoring objectives across mobile, web, and B2B channels. This is the strongest bank case study found.
- **Six additional banks document customer-journey-centric observability:** TSB, TD Bank, Migros Bank, WeLab Bank, Cencosud Scotiabank, and First National Bank of Omaha all describe monitoring approaches anchored to customer experience rather than infrastructure.
- **Gartner DEM is the analyst framework for outside-in observability:** Gartner defines DEM as measuring "availability, performance, and quality of user experience for applications...from the end-user perspective, rather than focusing on application internals." This is functionally identical to "outside-in observability."
- **Gartner Applied Observability (2023 top strategic trend) bridges IT metrics to business outcomes:** Includes customer satisfaction correlated with service levels and customer churn analysis — the business-outcome connection the prior evidence lacked.
- **The term "customer-centric observability" is not a recognized analyst category.** The practice exists under multiple labels: digital experience monitoring (Gartner), applied observability (Gartner), business observability (Dynatrace/Forrester), business service mapping (PRA/DORA). The concept is real but the label is a synthesis.
- **OpenTelemetry banking adoption is accelerating:** Elastic's 2026 FS report finds OTel adoption tripled in financial services, with 9 in 10 leaders citing OTel compliance as critical. Banking-specific OTel use cases (transaction flow tracing, PSD2 compliance, reconciliation monitoring) are documented.

---

## 1. Regulatory Mandates for Business-Service-Centric Monitoring

### PRA SS1/21 — Business Service Mapping (UK)

PRA SS1/21 §5.1 requires firms to "identify and document the necessary people, processes, technology, facilities, and information (the 'resources') required to deliver each of their important business services." This process is called "mapping."

§5.2 specifies two outcomes mapping must enable:
- **(a)** Identification of vulnerabilities in resources critical to delivering important business services
- **(b)** Testing ability to remain within impact tolerances

§5.4 requires mapping "to the level of detail necessary to use the mapping to identify vulnerabilities and test ability to remain within impact tolerances."

§5.5 extends mapping to third-party resources, and §5.9 requires annual updates minimum.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Firms must map people, processes, technology, facilities, information for each important business service | PRA SS1/21 §5.1 (Operational Resilience Parts 4.1) | https://www.prarulebook.co.uk/guidance/supervisory-statements/ss01-21---operational-resilience-impact-tolerances-for-important-business-services/5--mapping/22-10-2024?p=1 | Yes |
| Mapping must enable vulnerability identification and impact tolerance testing | PRA SS1/21 §5.2 | Same URL | Yes |
| Mapping must include third-party resources | PRA SS1/21 §5.5 | Same URL | Yes |
| Annual update minimum required | PRA SS1/21 §5.9 | Same URL | Yes |

### FCA PS21/3 — Impact Tolerances with Customer-Outcome Metrics (UK)

The FCA requires impact tolerances for each important business service, but goes further than the PRA in one critical respect: firms "should complement time-bound tolerances with additional metrics considering customer types, transaction values, criticality, and estimated losses." This explicitly mandates customer-outcome measurement, not just uptime measurement.

FCA compliance deadline: 31 March 2025.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Impact tolerances must be set for each important business service | FCA Operational Resilience Insights & Observations | https://www.fca.org.uk/firms/operational-resilience/insights-observations | Yes |
| Time-bound tolerances should be complemented with customer-type, transaction-value, criticality, and estimated-loss metrics | FCA Operational Resilience Insights & Observations | https://www.fca.org.uk/firms/operational-resilience/insights-observations | Yes |
| Impact tolerances differ from recovery time objectives | FCA Operational Resilience Insights & Observations | Same URL | Yes |
| Scenario testing required per SYSC 15A.5 | FCA Handbook SYSC 15A.5 | https://www.handbook.fca.org.uk/handbook/SYSC/15A/5.html | Yes |

### DORA RTS 2024/1774 — ICT Asset Mapping by Business Function (EU)

DORA's implementing regulation (Article 4 of RTS 2024/1774) requires:
- Mapping of data flows and supporting ICT systems for each critical business function
- Classification of ICT assets by criticality to business functions
- Recovery Time Objectives and Recovery Point Objectives defined per critical function
- Complete inventory of ICT assets including interdependencies

This mandates business-function-first classification of technology assets — the mapping starts from the business function, not the infrastructure component.

| Claim | Source | URL | Verified |
|---|---|---|---|
| ICT assets must be classified by criticality to business functions | DORA RTS 2024/1774 Article 4 | https://www.regulation-dora.eu/pdf/rts-ict-risk-management.html | Yes |
| Data flows and supporting ICT systems mapped per critical business function | DORA RTS 2024/1774 Article 4 | Same URL | Yes |
| RTOs and RPOs required per critical function | DORA RTS 2024/1774 Article 4 | Same URL | Yes |
| Regulation EU 2022/2554 (DORA) official text | EUR-Lex | http://eur-lex.europa.eu/eli/reg/2022/2554 | Yes |

### BCBS Principles for Operational Resilience (Global, March 2021)

The Basel Committee's principles — the global standard from which PRA, FCA, DORA, and RBI frameworks derive — include "mapping interconnections and interdependencies" as one of seven main areas. The principles aim to strengthen banks' ability to withstand events that could cause "significant operational failures or wide-scale disruptions in financial markets."

The BCBS framework does not prescribe specific customer-impact metrics (leaving this to national regulators) but establishes the principle that operational resilience should be measured from the perspective of critical operations delivery, not infrastructure availability.

| Claim | Source | URL | Verified |
|---|---|---|---|
| BCBS issued Principles for Operational Resilience, March 2021 | BIS | https://www.bis.org/bcbs/publ/d516.htm | Yes |
| Mapping interconnections and interdependencies is one of seven main areas | BIS press release | https://www.bis.org/press/p210331a.htm | Yes |
| Accompanied by revised Principles for Sound Management of Operational Risk (PSMOR) | BIS | https://www.bis.org/bcbs/publ/d515.pdf | Yes |

### RBI Guidance Note — Operational Risk Management and Operational Resilience (India, April 2024)

Updated guidance (replacing 2005 note) aligned with BCBS 2021 principles. Applies to all regulated entities including commercial banks, NBFCs, co-operative banks, and AIFIs. Emphasizes monitoring material operational exposures to "minimize operational disruptions while continuing to deliver critical operations."

| Claim | Source | URL | Verified |
|---|---|---|---|
| RBI issued updated guidance on operational risk management and resilience, 30 April 2024 | RBI Notification | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12679&Mode=0 | Yes |
| Aligned with BCBS March 2021 principles | RBI Master Directions context | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562 | Yes |
| Applies to all regulated entities (expanded from scheduled commercial banks only) | Hindu BusinessLine reporting | https://www.thehindubusinessline.com/money-and-banking/rbi-releases-updated-guidance-note-on-operational-risk-management-and-operational-resilience-for-lenders/article68125901.ece | Yes |

### OCC Heightened Standards (USA)

OCC Heightened Standards require risk governance frameworks and risk data aggregation and reporting for large banks. However, the scope is narrowing — the December 2025 proposal raises the threshold from $50B to $700B in assets, reducing affected institutions from 31 to 5. The standards require comprehensive monitoring and reporting capabilities but do not prescribe business-service-level monitoring as specifically as PRA or DORA.

| Claim | Source | URL | Verified |
|---|---|---|---|
| OCC proposed raising threshold from $50B to $700B, December 2025 | Mondaq | https://www.mondaq.com/unitedstates/financial-services/1731772/occ-proposes-higher-threshold-for-applying-heightened-standards | Yes |
| Heightened standards require risk data aggregation and reporting capabilities | OCC Bulletin 2025-51 | https://occ.gov/news-issuances/bulletins/2025/bulletin-2025-51.html | Yes |
| Comment period open until March 2, 2026 | Federal Register | https://www.federalregister.gov/documents/2025/12/30/2025-23986/occ-guidelines-establishing-heightened-standards-for-certain-large-insured-national-banks-insured | Yes |

### Regulatory Assessment

The regulatory mandate for business-service-centric monitoring is **stronger than previously assessed.** The prior evidence cited only PRA SS1/21. The gap-fill reveals:
- PRA, FCA, DORA, BCBS, and RBI all independently mandate approaches that start from business services / critical functions and map inward to technology resources
- FCA explicitly requires customer-outcome metrics (customer types, transaction values, estimated losses)
- DORA requires ICT asset classification by criticality to business functions
- The BCBS 2021 principles provide the global foundation from which all national frameworks derive

OCC Heightened Standards are the weakest link — they focus on risk governance rather than business-service-level monitoring, and their scope is narrowing.

---

## 2. Bank Case Studies of Outside-In Observability Adoption

### Wells Fargo — Multi-Platform Customer-Experience Monitoring

Wells Fargo has deployed at least four distinct monitoring/observability platforms with explicit customer-experience objectives:

**AppDynamics (2015–present):** Monitors lines of code and "understand[s] the real-time impact of digital transformation on customers engaging through mobile and web applications." Quote from Mike Telang, Head of Enterprise Architecture: "With AppDynamics, we are able to navigate our complex, regulated environment while maintaining a focus on customers and innovation."

**Elastic Observability:** Distributed tracing and APM for tracking "business-to-business (B2B) and business-to-consumer (B2C) financial transactions in near real time" including "application availability, customer responsiveness, and mean time to recovery." Selected for W3C Trace Context compliance and 100% trace capture.

**Grafana Enterprise/Cloud:** Consolidated legacy monitoring vendors. Implemented Grafana Agent and Grafana Mimir for cross-platform monitoring data collection and visualization.

**Glassbox DX Intelligence:** Proactive monitoring of "critical digital experience issues in authentication, check depositing, and bill payments." Measures effectiveness across teams with engineering-product collaboration on customer needs.

| Claim | Source | URL | Verified |
|---|---|---|---|
| AppDynamics deployed for customer-centric digital experience monitoring | AppDynamics press release | https://www.appdynamics.co.uk/newsroom/press-release/wells-fargo-ensures-consistent-digital-customer-experience-with-appdynamics | Yes |
| Elastic Observability for B2B/B2C transaction tracking, customer responsiveness | Elastic customer page | https://www.elastic.co/customers/wells-fargo | Yes |
| Grafana Cloud/Enterprise for observability stack modernization | Grafana Labs blog | https://grafana.com/blog/how-wells-fargo-modernized-its-observability-stack-with-grafana-enterprise-and-grafana-cloud/ | Yes |
| Glassbox DX Intelligence for digital experience issue monitoring | Glassbox case study | https://discover.glassbox.com/how-wells-fargo-leverages-dx-intelligence-for-proactive-issue-monitoring-on-demand-webinar-lp.html | Yes |

### JPMorgan Chase — Observability-Driven Development

JPMC uses Grafana for trading platform monitoring, incorporating SRE principles with AIOps-driven dynamic thresholds. The platform tracks trade volumes, synthetic transactions, and uses error budgets for data-driven decisions. JPMC presented "observability-driven development" at ObservabilityCon 2021. 43,000+ engineers supported by unified engineering platform.

Note: JPMC's approach is described as infrastructure/trading-platform-centric with SRE practices rather than explicitly customer-experience-driven. The outside-in dimension is partial.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Grafana for trading platform monitoring with AIOps dynamic thresholds | Grafana ObservabilityCon 2022 | https://grafana.com/events/observabilitycon/2022/monitoring-on-steroids-how-jpmorgan-chase-uses-grafana-for-their-trading-platform-to-spot-issues-quickly-and-proactively | Yes |
| "Observability-driven development" presented at ObservabilityCon 2021 | Grafana ObservabilityCon 2021 | https://grafana.com/events/observabilitycon/2021/observability-driven-development-jpmc | Yes |
| 43,000+ engineer community, unified platform strategy | MIT Technology Review / JPMC | https://www.jpmorganchase.com/about/technology/news/building-a-world-class-platform-for-software-engineers | Yes |

### Barclays — Customer Lifecycle Metrics

Barclays tracks four critical customer lifecycle touchpoints: problem-solving (complaint rates, satisfaction scores), card servicing (first call resolution, login success rates), card usage (transaction volumes), and card acquisition (application/approval rates). Nine out of ten cardmembers use digital channels exclusively. NPS improved from negative to +70 using process automation.

Open Banking metrics: 100% availability, 265ms payment response time (vs. 7,197ms traditional), 0.19% error rate.

Note: This is customer experience measurement rather than IT observability infrastructure, but it demonstrates the business-outcome framework that customer-centric observability serves.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Four customer lifecycle touchpoints tracked; 9/10 digital-only cardmembers | Barclays US Newsroom | https://cards.barclaycardus.com/banking/about-us/newsroom/advancing-customer-experience-through-metrics-and-moments/ | Yes |
| NPS improved from negative to +70 | IBM case study | https://www.ibm.com/case-studies/barclays-bank-plc | Yes |
| Open Banking: 100% availability, 265ms response, 0.19% error rate | Barclays Private Bank | https://privatebank.barclays.com/support-and-information/open-banking-metrics/ | Yes |

### TSB Bank — Customer Journey Observability

TSB deployed Dynatrace full-stack observability across multi-cloud (AWS, IBM Cloud, BT Cloud) providing "real-time, AI-powered insights into customer journeys." Reduced manual-intensive tasks, allowing teams to focus on innovation.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Dynatrace across multi-cloud for customer journey insights | Dynatrace customer page | https://www.dynatrace.com/customers/tsb/ | Yes |

### TD Bank — Customer-Outcome Metrics via Unified Observability

TD Bank ($1.4T CAD assets) deployed Dynatrace for unified monitoring across hybrid cloud. Results: 10 basis point transaction failure reduction, 45% cost reduction from tool consolidation, 75% AIOps savings, 20% faster incident resolution.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Dynatrace deployment with 10bp transaction failure reduction, 45% cost reduction | Dynatrace customer page | https://dynatrace.com/customers/td-bank | Yes |

### Migros Bank — User Journey Visibility for Digital Onboarding

Swiss bank (1M+ customers) uses Dynatrace for "full user journey visibility" for digital onboarding, with 50% faster incident resolution and single-platform collaboration eliminating silos across hybrid cloud and mainframe.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Full user journey visibility, 50% faster incident resolution | Dynatrace customer page | https://www.dynatrace.com/customers/migros-bank/ | Yes |

### WeLab Bank — AI-Driven Customer Journey Monitoring

100% digital bank (Hong Kong) uses Dynatrace Davis AI across hundreds of microservices on Kubernetes. 95% alert reduction, root cause identification in minutes vs. hours.

| Claim | Source | URL | Verified |
|---|---|---|---|
| 95% alert reduction, AI-driven observability for digital bank | Dynatrace customer page | https://www.dynatrace.com/customers/welab/ | Yes |

### Case Study Assessment

The bank case study evidence is **significantly stronger than previously assessed.** Wells Fargo alone provides a multi-platform case study of explicit customer-experience-driven observability. Six additional banks (TSB, TD, Migros, WeLab, Cencosud Scotiabank, First National Bank of Omaha) describe customer-journey or user-experience-centric monitoring approaches.

However, no bank has publicly described the full "outside-in" architectural inversion — starting from customer impact and mapping inward to infrastructure as a deliberate monitoring philosophy. Banks describe deploying digital experience monitoring alongside infrastructure monitoring; no bank describes replacing inside-out with outside-in as a strategic monitoring transformation.

---

## 3. Analyst and Industry Body Validation

### Gartner — Digital Experience Monitoring (DEM)

Gartner defines DEM as the measurement of "availability, performance, and quality of user experience for applications, including internal employees, external customers, partners, and API connections." DEM tools help I&O leaders "understand how business applications, networks, and infrastructure perform from the end-user perspective, rather than focusing on application internals."

The 2025 Magic Quadrant for DEM evaluates 15 vendors, with Dynatrace named Leader for the second consecutive year.

DEM is functionally equivalent to the "outside-in" observability concept — it measures from user experience inward rather than from infrastructure outward. The category is established and analyst-validated, even though the "customer-centric observability" label is not the term Gartner uses.

| Claim | Source | URL | Verified |
|---|---|---|---|
| DEM defined as measuring from end-user perspective, not application internals | Gartner Peer Insights — Digital Experience Monitoring | https://www.gartner.com/reviews/market/digital-experience-monitoring | Yes |
| Dynatrace named Leader in 2025 DEM Magic Quadrant | Dynatrace (citing Gartner MQ) | https://www.dynatrace.com/gartner-magic-quadrant-for-digital-experience-monitoring/ | Yes — but MQ report itself is paywalled |
| DEM users report 65% reduction in customer churn, 60% fewer irritants, 90% MTTR reduction | Dynatrace blog (citing Gartner MQ) | https://www.dynatrace.com/news/blog/2025-gartner-magic-quadrant-digital-experience-monitoring/ | Vendor-stated; Gartner sourced but MQ paywalled |

### Gartner — Applied Observability (2023 Top Strategic Trend)

Gartner identified Applied Observability as a top strategic technology trend. This extends beyond monitoring to "convert system performance into business performance" by combining telemetry data across systems for data-driven decisions. Applied Observability provides "granular visibility into business systems and workflows," including "trend analysis of customer satisfaction correlated with service levels" and customer adoption pattern analysis.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Applied Observability named 2023 top strategic technology trend | MoneyController (citing Gartner) | https://www.moneycontroller.co.uk/finance-news/gartner-inc/applied-observability-converting-system-performance-to-business-performance-894357 | Yes — secondary source citing Gartner |

### Forrester — Business-Centric Observability

Forrester research finds:
- 62% of IT leaders are measured by business and financial operations KPIs
- 67% struggle to generate insights that consider business context across operational domains
- In banking, 61% of consumers interact weekly through digital channels
- Financial institutions need observability ensuring applications are "stable, secure, and available in the moments that matter"

| Claim | Source | URL | Verified |
|---|---|---|---|
| 62% IT leaders measured by business KPIs; 67% struggle with business context | Forrester/Cisco observability ebook | https://thoughtleadership.forrester.com/go/cisco/observability_ebook | Yes — vendor-sponsored Forrester research |
| 61% bank consumers interact weekly via digital channels | Cisco/Forrester FS brief | https://www.cisco.com/c/en/us/solutions/industries/financial-services/digital-delivery-financial-services-ig.html | Yes — vendor-sponsored |

### ITIL 4 — Value Stream Monitoring

ITIL 4 positions monitoring and event management within value streams. The practice purpose is to "systematically observe services and service components, and record and report selected changes of state identified as events." Value from the customer's perspective is the organizing principle — in banking, this includes loan processing time, satisfaction scores, and ease of process.

| Claim | Source | URL | Verified |
|---|---|---|---|
| ITIL 4 monitoring/event management practice definition | O'Reilly / ITIL 4 CDS textbook, Chapter 18 | https://www.oreilly.com/library/view/itil-4-create/9781787783393/xhtml/Chap18.html | Yes — paywalled; Axelos/PeopleCert official |
| Value streams defined as customer-value-centered | ITpreneurs blog | https://www.itpreneurs.com/blog/the-value-streams-an-existing-concept-leveraged-in-itil-4/ | Yes |
| Banking value stream example (loan delivery) | HCLTech blog | https://hcltech.com/blogs/value-stream-management-in-action-banking-on-transformation | Yes |

### Elastic — Financial Services Observability Landscape 2026

Survey of 100+ financial services leaders:
- 70% rate observability practice as mature or expert (up sharply from 2025)
- Nearly two-thirds use observability for real-time compliance monitoring and audit trails
- OpenTelemetry adoption tripled; 9 in 10 leaders cite OTel compliance as critical
- 94% already use GenAI for observability

| Claim | Source | URL | Verified |
|---|---|---|---|
| 70% FS teams rate observability as mature/expert; OTel tripled; 94% use GenAI | Elastic FS Observability Report 2026 | https://www.elastic.co/industries/financial-services/landscape-observability-report | Yes — landing page; full report gated |

### BIS/FSB Gap

No FSB-specific guidance on customer-impact measurement for operational resilience was found. The BCBS d516 (2021) provides the global principles framework but does not prescribe customer-impact metrics specifically. FSB publications on operational resilience appear to focus on systemic risk rather than individual customer impact measurement.

| Claim | Source | URL | Verified |
|---|---|---|---|
| No FSB-specific customer-impact measurement guidance found | Search result | N/A | Negative finding confirmed |

### Analyst Assessment

The analyst evidence is **materially stronger than previously assessed.** Gartner's DEM category and Applied Observability trend both validate the "outside-in" monitoring concept, though under different labels. Forrester confirms the business-context gap in current observability practices. ITIL 4's value stream framework provides service management theory support.

The gap: no analyst has published a financial-services-specific framework for "customer-centric observability" as a named practice. The concept is validated as components (DEM + Applied Observability + business service mapping) but not as an integrated practice for banking.

---

## 4. Technology Evidence

### Dynatrace — PRA SS1/21 Compliance Capabilities

Dynatrace has published specific content mapping its platform to PRA SS1/21 requirements across three priorities:

1. **Impact tolerance tracking:** Defining impact tolerances as Service Level Objectives (SLOs), with automatic alerting when error budgets are consumed.
2. **Business service mapping:** SmartScape technology automatically generates interactive maps of applications and services, visualizing component relationships and dependencies. Combined with workflow management tools for component ownership tracking.
3. **Testing critical systems:** Synthetic monitoring for simulating "significant but plausible scenarios" that SS1/21 requires.

Banking case studies: TD Bank, TSB, Migros Bank, WeLab Bank, Cencosud Scotiabank, First National Bank of Omaha, KBC Bank (PSD2 compliance), Alpha Bank.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Dynatrace maps to 3 PRA SS1/21 priorities: impact tolerances, business service mapping, testing | Dynatrace blog | https://www.dynatrace.com/news/blog/driving-operational-resilience-in-uk-with-ss1-21/ | Yes |
| SmartScape for business service mapping | Same article | Same URL | Yes |
| Impact tolerances as SLOs | Same article | Same URL | Yes |
| DORA compliance through AI, observability, and security | Dynatrace blog | https://www.dynatrace.com/news/blog/taming-dora-compliance-with-ai-observability-and-security/ | Yes |

### New Relic — Service Level Management and Financial Services

New Relic provides SLO/SLI capabilities for latency and availability monitoring. Financial services report findings:
- $1.8M per hour average cost of high-impact IT outages in financial services
- 29% report high-impact outages weekly
- 89% plan to deploy browser monitoring, 80% mobile monitoring, 77% synthetic monitoring within 1-3 years
- Security, governance, risk, and compliance are primary observability adoption drivers in FS

| Claim | Source | URL | Verified |
|---|---|---|---|
| $1.8M/hr outage cost in financial services; 29% weekly high-impact outages | New Relic press release, 20 Jan 2026 | https://newrelic.com/press-release/20260120 | Yes |
| SLM capabilities (SLOs/SLIs for latency, availability) | New Relic documentation | https://docs.newrelic.com/docs/service-level-management/intro-slm | Yes |
| Revenue-at-risk quantification during incidents | New Relic documentation | https://docs.newrelic.com/docs/tutorial-service-level-mgmt/improve-with-slm | Yes |

### Datadog — Financial Services Presence

Datadog serves financial services customers including NatWest Boxed (cloud cost management), SBI Sumishin Net Bank, and Thrivent. However, the documented case studies focus on infrastructure cost optimization rather than customer-centric observability.

| Claim | Source | URL | Verified |
|---|---|---|---|
| NatWest Boxed uses Datadog for cloud cost management | Datadog case study | https://datadoghq.com/case-studies/natwest-boxed | Yes |
| SBI Sumishin Net Bank uses Datadog | Datadog case study | https://www.datadoghq.com/ja/case-studies/sbi-sumishin-net-bank | Yes — Japanese language |

Note: No Datadog case study for banking-specific business service monitoring or customer-centric observability was found.

### OpenTelemetry — Banking Use Cases

OpenTelemetry adoption in financial services is accelerating. Documented banking-specific use cases:
- Banking API transaction flow tracing (account lookup, balance check, transfer, confirmation)
- Open Banking API (PSD2) gateway performance monitoring — EBA requires response <500ms, 99.5% availability
- Real-time transaction reconciliation between core banking and payment processors
- SLO compliance tracking across hundreds of internal services

| Claim | Source | URL | Verified |
|---|---|---|---|
| Banking API transaction flow tracing with OTel | OneUptime blog | https://oneuptime.com/blog/post/2026-02-06-trace-banking-api-transaction-flows-opentelemetry/view | Yes |
| PSD2 Open Banking API monitoring with OTel | OneUptime blog | https://oneuptime.com/blog/post/2026-02-06-open-banking-api-gateway-opentelemetry/view | Yes |
| SLO compliance reporting with OTel across internal services | OneUptime blog | https://oneuptime.com/blog/post/2026-02-06-otel-sla-compliance-reporting/view | Yes |
| OTel adoption tripled in FS, 9/10 cite as critical | Elastic FS Report 2026 | https://www.elastic.co/industries/financial-services/landscape-observability-report | Yes |

### VuNet Systems — Business Journey Observability for Banking

VuNet Systems offers "Business Journey Observability" specifically for digital banking, monitoring customer-facing processes end-to-end including account aggregation, bill payments, core banking, credit card onboarding, instant payments, lending, and trading.

| Claim | Source | URL | Verified |
|---|---|---|---|
| Business journey observability for digital banking use cases | VuNet Systems case study | https://vunetsystems.com/case-study/reimagined-digital-banking-experience-with-business-journey-observability | Yes |
| Digital experience monitoring solution for banking | VuNet Systems | https://vunetsystems.com/solutions/digital-experience-monitoring | Yes |

Note: VuNet Systems is a smaller vendor; this evidence confirms the product category exists but carries less weight than enterprise vendor adoption.

### Technology Assessment

Dynatrace has the strongest technology-regulatory alignment, with published content mapping its platform to PRA SS1/21 requirements. New Relic's SLM capabilities and financial services research provide revenue-impact framing. OpenTelemetry is emerging as the open-source backbone for banking observability with specific use cases documented. Datadog's banking evidence is present but focuses on infrastructure/cost rather than customer-centric monitoring.

---

## 5. Gaps That Remain Unfilled

1. **No bank has publicly described a complete "outside-in" architectural inversion.** Banks describe adding DEM/customer-experience monitoring alongside existing infrastructure monitoring, not replacing inside-out with outside-in as a deliberate strategy. The transformation narrative remains hypothetical.

2. **No analyst publishes "customer-centric observability" as a named category for banking.** The concept exists under multiple analyst labels (DEM, Applied Observability, business observability, business service mapping) but is not unified as a single practice in any analyst framework.

3. **FSB/BIS do not prescribe customer-impact metrics.** The BCBS 2021 principles establish operational resilience goals but leave metric specification to national regulators. There is no global standard for customer-impact measurement in operational resilience.

4. **DBS, Standard Chartered, HSBC case studies not found.** Searches for these banks' observability approaches returned no specific customer-centric observability case studies. Standard Chartered has SRE Academy and Sumo Logic deployment (from existing S4 research) but no outside-in observability content. HSBC has multi-cloud governance signals but no observability case studies.

5. **Datadog business-service-monitoring banking evidence is absent.** Despite Datadog's dominant position in observability, no banking case study for its Service Catalog or business service monitoring capabilities was found. This may indicate the feature is either new or not yet adopted in banking.

6. **Forrester lacks a banking-specific outside-in observability report.** Forrester research on observability is sponsored by vendors (Cisco) and does not provide an independent banking-specific assessment.

---

## 6. Evidence Upgrade Assessment

### Prior state (Moderate)
- PRA SS1/21 business service mapping requirement (1 regulator)
- Wells Fargo Elastic deployment (1 bank case study, 1 platform)
- Gartner outcome-driven ops mention (1 analyst reference)
- Thin independent evidence beyond vendor claims

### Post gap-fill state

**Regulatory evidence: Strong**
- 5 regulatory frameworks (PRA, FCA, DORA, BCBS, RBI) mandate business-service-centric approaches
- FCA explicitly requires customer-outcome metrics
- DORA mandates ICT classification by business-function criticality
- Global regulatory consensus via BCBS 2021 principles

**Bank case study evidence: Moderate-to-Strong**
- Wells Fargo: 4 distinct platforms with explicit CX monitoring (strong standalone case)
- 6 additional banks: TSB, TD Bank, Migros Bank, WeLab, Cencosud Scotiabank, First National Bank of Omaha
- Barclays: customer lifecycle metrics (CX measurement, not observability infrastructure)
- JPMC: observability-driven development (SRE-centric, partial outside-in)
- Gap: no bank describes complete inside-out → outside-in transformation

**Analyst evidence: Moderate-to-Strong**
- Gartner DEM MQ (validated category, directly equivalent to outside-in)
- Gartner Applied Observability (2023 strategic trend, business outcome correlation)
- Forrester (business context gap in observability confirmed)
- ITIL 4 value streams (theoretical framework)
- Gap: no banking-specific unified framework exists

**Technology evidence: Strong**
- Dynatrace: explicit PRA SS1/21 compliance mapping, 8+ banking case studies
- New Relic: SLM capabilities, $1.8M/hr FS outage cost data
- OpenTelemetry: banking-specific use cases, tripled FS adoption
- Gap: Datadog banking business-service monitoring absent

### Verdict: Upgrade from Moderate to **Moderate-Strong**

The evidence has been materially strengthened across all four dimensions. The regulatory consensus is now demonstrably multi-regulator and global, not single-regulator. Bank case studies expand from one to eight institutions. Analyst frameworks validate the concept under established labels (DEM, Applied Observability). Technology evidence shows vendor-regulatory alignment.

However, the upgrade stops short of **Strong** for three reasons:

1. **No bank describes the complete architectural transformation** from inside-out to outside-in monitoring. Banks add customer-experience monitoring alongside infrastructure monitoring; they do not replace the latter with the former.

2. **The concept lacks a unified analyst label.** "Customer-centric observability" is a synthesis of DEM + Applied Observability + business service mapping. No analyst framework unifies these into a single practice for banking.

3. **The strongest bank case studies are vendor-provided.** Wells Fargo's AppDynamics and Elastic deployments are documented on vendor sites. Independent third-party validation (e.g., analyst case study, conference presentation by the bank itself) is limited to JPMC's Grafana/ObservabilityCon presentations.

### Writing recommendation

In Part I, Structural Shift 7 should:
- Lead with the multi-regulator mandate (PRA + FCA + DORA + BCBS + RBI) as the forcing function — this is Strong evidence
- Present bank adoption as partial and accelerating (DEM platforms deployed, customer-outcome metrics tracked) rather than as a completed transformation
- Reference Gartner's DEM category and Applied Observability trend as analyst validation of the outside-in concept
- Acknowledge that the practice exists under multiple labels and is not yet unified as a banking-specific category
- Use Wells Fargo as the anchor case study (strongest evidence with multiple platforms and explicit CX focus)

This treatment presents the shift honestly without overclaiming, grounds it in regulatory evidence, and uses the analyst frameworks that do exist rather than asserting a framework that does not.
