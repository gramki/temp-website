# S4: Compliance Operations Workflow and Architecture

**Stream:** S4 — Workflow & Architecture
**Engagement Area:** Compliance Operations
**Date:** March 2026
**Status:** Research Complete

---

## Executive Summary

Compliance operations at banks remain a labor-intensive, manually-stitched patchwork of point solutions connected by spreadsheets, email, and human effort. Despite $206B+ in annual global financial crime compliance spending, the industry detects only ~2% of illicit financial flows (McKinsey). The alert-to-resolution lifecycle traverses 5–12+ disconnected systems at a typical Tier 2 bank. Each handoff introduces delay, error, and audit risk.

No vendor today delivers a unified compliance operations platform that spans alert generation, triage, investigation, case management, regulatory filing, exam evidence assembly, and GRC/policy governance in a single system of record. The closest attempts (Fenergo FinCrime OS, Napier AI Continuum, Pega CLM) cover 2–3 of these stages but miss others entirely. This is the category-creation opportunity.

---

## A. Alert-to-Resolution Lifecycle in AML/Sanctions

### A1. End-to-End Workflow

| Stage | What Happens | Primary Systems | Manual vs. Automated | Typical Timeline | Error Rates / Bottlenecks |
|-------|-------------|----------------|---------------------|-----------------|--------------------------|
| **1. Alert Generation** | TM rules/models flag unusual patterns (large deposits, transfers to high-risk jurisdictions, structuring) | NICE Actimize, SAS, Verafin, Oracle FCCM, SymphonyAI, Fiserv AML Risk Manager | Automated (rules-based or ML) | Real-time or batch (daily) | Overly broad rules generate 95–98% false positives |
| **2. Alert Triage (L1)** | Analyst reviews alert, checks customer profile, filters duplicates, applies risk scoring; dispositions or escalates | Same TM system + core banking; manual toggling between 3–5 screens | Largely manual; some auto-disposition of low-risk alerts | 15–25 min per alert; analyst reviews 15–20 alerts/day | Fatigue drives inconsistent disposition; 28% annual turnover |
| **3. Investigation (L2/L3)** | Investigator gathers KYC/KYB data, screens sanctions/PEP/adverse media, analyzes transaction links, builds case narrative | KYC (Alloy, ComplyAdvantage), sanctions (LexisNexis, OFAC), entity resolution (Quantexa), adverse media tools | 60–80% manual; some AI-assisted enrichment | 1.5–4+ days per case (rising) | Evidence scattered across 5–8 applications |
| **4. Case Management** | Tracking investigation through disposition; documenting findings, evidence chain, approvals | NICE Actimize ActOne, Pega, Hummingbird, Unit21, internal tools | Semi-automated (workflow routing); documentation is manual | Days to weeks | 77% of banks cite analyst resourcing as top-3 challenge |
| **5. SAR/STR Filing** | Narrative preparation, BSA officer review, multi-level approval, electronic submission to FinCEN/FIU | FinCEN BSA E-Filing, Hummingbird, Verafin | Narrative is manual (GenAI now assists); filing is electronic | 30-day deadline from determination; continuing SARs on 120-day cycle | 4.6M SARs filed in 2023; some institutions 45+ day backlogs |
| **6. Regulatory Response** | Responding to FinCEN 314(a) (2-week window), 314(b) sharing, subpoenas, law enforcement inquiries | FinCEN SISS portal; internal search tools | 314(a) matching semi-automated; evidence assembly manual | 314(a): 2 weeks; subpoenas vary | Manual searches across fragmented systems |
| **7. Exam Documentation** | Assembling evidence for OCC/Fed/FDIC exams: policies, testing, training, case samples, board reports | GRC platforms, SharePoint, spreadsheets | Largely manual assembly | 3–5 weeks (poorly documented) to days (well documented) | Missing evidence is the primary exam finding source |

### A2. Alert Volume and False Positive Data

| Claim | Value | Source | URL | Verified |
|-------|-------|--------|-----|----------|
| AML alert false positive rate (legacy) | 95–98% | Trapets, Lenzo.AI, multiple sources | https://www.trapets.com/resources/blog/flagging-false-positives-in-aml-how-banks-can-reduce-98-wasted-alerts | Yes |
| Sanctions/watchlist false positive rate | ~99% | WorkFusion | https://www.prnewswire.com/news-releases/workfusion-ai-agents-now-process-1-million-sanctions-and-adverse-media-alerts-daily-302403635.html | Partial (vendor) |
| AI-driven false positive reduction | 20–60% (screening); up to 70% (TM) | Lenzo.AI, WJARR | https://www.lenzo.ai/blog/ofac-screening-false-positive-rates-industry-benchmarks-for-2025 | Yes |
| Napier AI false positive reduction | Up to 97% | Napier AI | https://www.napier.ai/continuum-pro | Partial (vendor) |
| Total SARs filed (2023) | 4.6M record; 3.8M original | FinCEN, Thomson Reuters | https://www.thomsonreuters.com/en-us/posts/corporates/sars-report-2024/ | Yes |
| Total SARs filed (2024) | ~3.8M original; ~4.5M total | Thomson Reuters | Same as above | Yes |
| SAR growth (pre-pandemic) | 2–3% annually | Thomson Reuters | https://www.thomsonreuters.com/en-us/posts/investigation-fraud-and-risk/sars-fraud-2024/ | Yes |
| SAR growth (post-pandemic) | 4–5% annually | Thomson Reuters | Same as above | Yes |
| SAR growth 2019–2022 | +57% (to 3.6M) | SKAN.AI citing FinCEN | https://www.skan.ai/blogs/how-process-intelligence-fixes-sar-backlogs | Yes |
| Investigation time per case | 1.5 to 4+ days (rising) | SKAN.AI | Same as above | Partial |
| L1 analyst alerts per day | 15–20 | Veridaq, industry consensus | https://veridaq.com/blog/reduce-aml-alert-fatigue-eu-bank-workflow-optimization | Yes |
| Time per false positive | 15–25 minutes | Lenzo.AI | https://www.lenzo.ai/blog/ofac-screening-false-positive-rates-industry-benchmarks-for-2025 | Yes |
| Financial crime detection rate | ~2% of illicit flows | McKinsey | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-agentic-ai-can-change-the-way-banks-fight-financial-crime | Yes |
| Workforce dedicated to KYC/AML | 10–15% | McKinsey | Same as above | Yes |

### A3. SAR Filing Process Detail

| Requirement | Detail | Source |
|-------------|--------|--------|
| Filing deadline | 30 calendar days from "initial detection" determination | FinCEN regulations |
| Clock trigger | Not the alert flag; the point at which institution concludes suspicious activity exists after review | FinCEN FAQ (Oct 2025) |
| Continuing activity cycle | Initial SAR, monitor 90 days, continuing SAR within 30 days = 120-day cycle | FinCEN FAQ (Oct 2025) |
| Review layers | Red flag > L1 analyst > L2 investigator > BSA officer > filing | Industry standard |
| Filing method | Electronic via FinCEN BSA E-Filing System | FinCEN |
| Narrative requirement | Detailed narrative: who/what/when/where/why/how | FinCEN SAR instructions |

### A4. FinCEN 314(a)/314(b) Process

| Process | Description | Timeline | Source |
|---------|-------------|----------|--------|
| 314(a) incoming | FinCEN posts bi-weekly subject lists from law enforcement via SISS | 2 weeks to respond with positive matches | FinCEN 314(a) Fact Sheet |
| 314(a) search scope | Accounts in preceding 12 months; non-account transactions in preceding 6 months | Within 2-week window | FinCEN |
| 314(a) response | Report positive matches only; no response if no matches | 2 weeks | FinCEN |
| 314(b) voluntary sharing | Institutions share information under safe harbor from liability | Voluntary; no fixed timeline | FinCEN 314(b) Fact Sheet |

---

## B. Exam Preparation Process

### B1. Exam Preparation Data

| Claim | Value | Source | URL | Verified |
|-------|-------|--------|-----|----------|
| Standard exam prep window | 30–90 days | Industry guidance (Whitlock, RADD) | https://whitlockco.com/blog/how-to-prepare-your-bank-for-an-it-regulatory-exam | Yes |
| Well-documented orgs | Days (vs. weeks) | Canarie AI | https://www.canarie.ai/blog/compliance-exam-preparation-banks | Partial |
| Poorly-documented orgs | 3–5 weeks scramble | Canarie AI | Same as above | Partial |
| OCC exam frequency | Every 12–18 months | OCC Examinations Overview | https://occ.gov/topics/supervision-and-examination/examinations/examinations-overview/index-examinations-overview.html | Yes |
| OCC special exam fee (2026) | $137/hour | OCC Bulletin 2025-43 | https://occ.gov/news-issuances/bulletins/2025/bulletin-2025-43.html | Yes |
| Cost allocated to audit/exam | 12% of compliance costs | APPIT Software Solutions | https://www.appitsoftware.com/blog/banking-compliance-cost-revolution | Partial |
| Manual processes impact | 7x more examiner questions vs. automated | Ncontracts 2026 Survey | https://www.ncontracts.com/nsight-blog/future-of-compliance-survey-report | Yes |
| Platform response improvement | 60% faster regulatory responses | RegScale | https://regscale.com/knowledge-hub/regulatory-response-management/ | Partial (vendor) |
| Primary exam finding cause | Missing evidence, not missing knowledge | Canarie AI | https://www.canarie.ai/blog/compliance-exam-preparation-banks | Partial |

### B2. Evidence Assembly Requirements

Examiners evaluate three components of a compliance management system:

1. **Board and management oversight** — Board resolutions, committee minutes, risk appetite statements, compliance reporting to board, response to prior findings
2. **Compliance program effectiveness** — Policies/procedures, training records, monitoring/testing results, complaint tracking, change management documentation
3. **Independent audit/testing** — Internal audit reports, independent BSA/AML testing, quality assurance reviews, sample case file reviews

Evidence is typically scattered across:
- Core banking system (transaction data)
- BSA/AML case management tool (alerts, investigations, SARs)
- GRC platform (policies, controls, risk assessments)
- Learning management system (training records)
- Board portal (minutes, resolutions)
- SharePoint/shared drives (miscellaneous documents)
- Email (approvals, communications)
- Spreadsheets (tracking logs, checklists)

### B3. OCC 2026 Supervisory Reset

| Change | Detail | Source |
|--------|--------|--------|
| Elimination of policy-based exams | Fixed checklists replaced with risk-based examiner discretion | OCC 2026 guidance |
| Expanded community bank definition | Now includes institutions up to $30B in assets | OCC 2026 guidance |
| Shift to self-examination | Banks must demonstrate credible self-assessment between exam cycles | OCC 2026 guidance |
| BSA/AML exam flexibility | Examiners determine whether/to what degree transaction testing is needed | OCC Bulletin 2025-37 |
| MLRS data collection discontinued | Annual Money Laundering Risk System collection ended for community banks | OCC 2026 guidance |
| FDIC supervisory reforms | Refocusing on material financial risks; independent appeals office (Jan 2026) | FDIC speeches (2026) |
| CAMELS revision | Refocusing on material financial risks rather than process compliance | FDIC/OCC interagency |

### B4. Continuous Examination Trend

The regulatory landscape is shifting from periodic point-in-time examinations toward continuous monitoring:

- **OCC 2026 reset** places responsibility on banks to maintain ongoing documentation, as examiners use discretion to assess institutional risk posture
- **FDIC reforms** emphasize actual noncompliance and consumer harm over policies/procedures
- Banks maintaining "examination-ready" posture continuously avoid the 3–5 week scramble
- Emerging platforms (Canarie, Skematic, RegScale) capture evidence at moment of work completion

**Implication for category-creation thesis:** Continuous examination readiness is impossible without a unified compliance operations platform. When evidence is scattered across 8–12 disconnected systems, no amount of manual effort creates continuous readiness.
