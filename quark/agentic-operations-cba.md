# Agentic Operations — CBA & OpEx Allocation (Indicative)

This note extends `quark/Agentic_Ops_Document.md` with an **economic rationale** (why agentic automation), an **indicative OpEx allocation** by back-office domain, and a **cost–benefit analysis (CBA) template** you can calibrate to a specific bank.

> Important: The % ranges below are **directional**. They vary materially by bank (retail vs corporate heavy), scale, product mix, country/regulation, sourcing model (in-house vs BPO), and maturity (STP %, legacy fragmentation). Use them to **prioritize** and to seed a CBA — then replace with your bank’s actual cost data.

---

## Scope & definitions

- **Bank “operations OpEx” (for this document)**: staff + vendor/BPO costs + run costs directly attributable to back-office processing, investigation, servicing, reconciliation, and control execution.  
  - Excludes most **front-office sales** costs.  
  - Excludes most **pure IT infrastructure** (unless embedded in operations run budgets).  
- **OpEx share % (shown below)**: percentage of **Operations OpEx** allocated to that domain.
  - Some banks book costs differently (e.g., AML under “Risk”, tech ops under “IT”). If you reclassify, **normalize** so the final allocation totals ~100%.

---

## Why banks should consider agentic automation (common value levers)

Agentic automation is attractive in back-office domains because work is typically:

- **High-volume and repeatable**: queue-based processing with standard operating procedures (SOPs).
- **Rules + evidence driven**: decisions require checking policies, documents, and system states.
- **Exception-heavy**: STP breaks create long tails where triage + root-cause mapping drives cost.
- **Control-intensive**: auditability, segregation of duties, and evidence packs are expensive manually.

**Primary value levers (used in the CBA model below):**

- **Labor productivity**: reduce AHT (average handling time), rework, and handoffs; increase throughput per FTE.
- **Quality and leakage reduction**: fewer posting errors, fewer missed fees, fewer reconciliation breaks.
- **Loss avoidance**: fraud loss reduction, earlier interdiction, better collections routing.
- **Compliance and audit**: faster evidence compilation, fewer findings, lower remediation cost.
- **Cycle time improvements**: faster onboarding/disbursement/settlement improves customer outcomes and reduces downstream exceptions.

---

## Summary table — OpEx share, “why agentic”, and CBA shape (indicative)

| # | Back-office function (domain) | Why consider agentic automation (high signal) | Indicative OpEx share of Ops (%) | Primary value levers | Typical savings / value potential (domain-level) |
|---|---|---|---:|---|---|
| 1 | Customer Lifecycle & Identity Ops | Document-heavy + rules-driven; repeated refresh cycles; high manual checks + audits | 8–15% | Productivity, quality, compliance | 15–35% cost reduction; fewer KYC breaches; faster onboarding |
| 2 | Payments & Clearing Ops | Reconciliation + exceptions are classic pattern matching; large volumes + STP breaks | 10–18% | Productivity, quality, leakage | 20–45% cost reduction; fewer breaks; faster settlement SLA adherence |
| 3 | Card & Digital Payments Ops | Disputes/chargebacks are workflow + evidence compilation; lifecycle changes are deterministic | 5–10% | Productivity, loss avoidance, CX | 15–35% cost reduction; improved dispute win-rate; faster resolution |
| 4 | Lending Ops | Documentation + booking/disbursement/servicing workflows; exception and covenant monitoring | 10–18% | Productivity, cycle time, quality | 15–35% cost reduction; faster TAT; fewer booking defects |
| 5 | AML, Compliance & Risk Ops | Alert triage + evidence gathering is labor intensive; reporting requires structured narratives | 7–14% | Productivity, compliance, loss avoidance | 10–30% cost reduction; higher analyst throughput; better SAR/STR quality |
| 6 | Treasury & Liquidity Ops | Time-sensitive, high-risk; strong need for controls + confirmations + reconciliations | 2–5% | Quality, control, cycle time | 10–25% cost reduction; fewer settlement fails; better control evidence |
| 7 | Deposits/CASA & Account Ops | Account lifecycle actions are rule-triggered (dormancy, holds, fees, closures) | 6–12% | Productivity, quality | 15–35% cost reduction; fewer service defects; faster processing |
| 8 | Customer Service Ops (ops layer) | Case triage, drafting, routing, and fulfillment are ideal for agentic workbenches | 8–16% | Productivity, CX, quality | 10–30% cost reduction; shorter TTR; fewer escalations |
| 9 | Trade Finance Ops | Document checking against rulebooks (UCP/ISBP) is structured but complex; high value per case | 2–6% | Productivity, quality, cycle time | 10–30% cost reduction; faster doc checking; fewer discrepancies |
| 10 | Cash Mgmt & Corporate Banking Ops | Mandates, virtual accounts, sweeps: configuration + verification + controls | 2–6% | Productivity, quality | 15–35% cost reduction; fewer setup errors; faster onboarding |
| 11 | Branch & Teller Back-Office Support | ATM/cheque/cash balancing are reconciliation-like; exception queues are scalable | 2–6% | Productivity, quality | 15–35% cost reduction; fewer suspense items; faster balancing |
| 12 | Compliance, Audit & Reporting Ops | Evidence collection and reporting are repeatable; strong ROI from “audit pack automation” | 3–8% | Compliance, productivity | 15–40% cost reduction; fewer findings; faster audits |
| 13 | Technology & Platform Support Ops (ops-linked) | Batch monitoring + STP exception classification + remediation are high-volume control loops | 3–8% | Productivity, resilience | 10–30% cost reduction; fewer incidents; faster MTTR |
| 14 | Collections & Recovery Ops | Segmentation, routing, reminders are data-driven; agentic workflows reduce contact cost | 4–10% | Loss avoidance, productivity | 10–30% cost reduction; uplift in recoveries; lower roll rates |
| 15 | Revenue Assurance & Finance Ops | Reconciliation + leakage detection are deterministic; high payoff from fewer breaks/leakage | 4–10% | Leakage reduction, productivity | 15–45% value (cost + leakage); fewer manual journals |

**How to read “Typical savings / value potential”**:
- It’s a **blended** view across labor savings, reduced rework, reduced exceptions, and (where relevant) loss/leakage improvements.
- Realized savings depend heavily on whether the bank is willing/able to **remove or redeploy capacity** (not just “assist” work).

---

## Domain-by-domain rationale + CBA drivers (what to measure)

Each domain below includes: **why**, **where agents fit**, and the **CBA measurement frame** (what to quantify).

### 1) Customer Lifecycle & Identity Operations

- **Why agentic**: high-volume document ingestion (KYC), repeated refresh cycles, deterministic validations, large manual effort in exception handling and audit evidence creation.
- **Where agents fit**:
  - **Think Agents**: document interpretation, entity resolution hints, risk narratives for EDD.
  - **Governance Agents**: policy gating (CDD/EDD thresholds), SoD and approval checks, audit-grade decision logs.
  - **Do Agents**: profile updates, workflow tasks, notifications, ticket actions (post-approval).
  - **Orchestrators**: sequence multi-step onboarding/refresh journeys with SLAs and HITL.
- **CBA drivers**:
  - **Productivity**: onboarding/refresh AHT; % straight-through processing; backlog aging.
  - **Quality**: rework rate; false rejects/accepts; data defect rates.
  - **Compliance**: SLA misses for periodic refresh; audit findings; remediation costs.

### 2) Payments & Clearing Operations

- **Why agentic**: reconciliation + STP breaks are pattern-rich; returns/rejects follow deterministic code workflows; high cost from exceptions, suspense, and SLA penalties.
- **Where agents fit**:
  - **Do Agents**: recon matching, auto-posting adjustments (within policy), returns processing.
  - **Think Agents**: break classification + root-cause mapping; evidence compilation for disputes.
  - **Governance Agents**: controls on postings/adjustments, limits, SoD, and mandatory approvals.
  - **Orchestrators**: end-to-end exception workflows (collect evidence → propose action → obtain approval → execute).
- **CBA drivers**:
  - **Productivity**: breaks per analyst per day; % auto-resolved breaks; recon cycle time.
  - **Quality/leakage**: suspense aging; write-offs; manual posting errors.
  - **Resilience**: reduced operational incidents during peak/batch.

### 3) Card & Digital Payments Operations

- **Why agentic**: disputes/chargebacks require structured rulebook reasoning + evidence packs; lifecycle operations (block/replace/reissue) are deterministic.
- **Where agents fit**:
  - **Think Agents**: dispute triage, evidence summarization, scheme-rule alignment drafts.
  - **Do Agents**: execute lifecycle changes and workflow actions post-approval.
  - **Governance Agents**: prevent unsafe actions (e.g., irreversible blocks, settlement postings) without controls.
  - **Orchestrators**: chargeback lifecycle management and SLA tracking.
- **CBA drivers**:
  - **Productivity**: cases per FTE; time-to-first-action; documentation time.
  - **Win-rate / loss**: representment success; chargeback loss; fraud loss reduction from faster actions.
  - **CX**: resolution time; complaint rates.

### 4) Lending Operations

- **Why agentic**: origination, booking, disbursement, servicing have standard checklists; major cost is document collection, covenant checks, and exceptions/rework.
- **Where agents fit**:
  - **Think Agents**: document interpretation, covenant extraction, exception narratives.
  - **Do Agents**: booking/disbursement steps (policy-gated), schedule generation, servicing updates.
  - **Governance Agents**: limit checks, KYC gating, compliance validations, approval hierarchy.
  - **Orchestrators**: multi-system workflows with SLAs and human approvals.
- **CBA drivers**:
  - **Cycle time**: TAT from approval to booking/disbursement; exception queue size.
  - **Quality**: booking defects; rework; downstream servicing complaints.
  - **Risk**: policy breaches; documentation gaps; audit issues.

### 5) AML, Compliance & Risk Operations

- **Why agentic**: alert triage and investigations are evidence aggregation + summarization heavy; reporting is narrative + structured data assembly; large long-tail of low-value alerts.
- **Where agents fit**:
  - **Think Agents**: alert triage, typology mapping, case summarization, SAR/STR drafting assistance.
  - **Governance Agents**: enforce policy, thresholds, approvals, data access, and audit logs.
  - **Do Agents**: case system updates, evidence packaging tasks, reversible actions where allowed.
  - **Orchestrators**: manage investigation workflow and deadlines.
- **CBA drivers**:
  - **Productivity**: alerts handled per analyst; time spent gathering evidence vs analysis.
  - **Quality**: escalation accuracy; SAR/STR completeness; regulator feedback/audit findings.
  - **Loss avoidance**: earlier interdiction; fewer false negatives (handle with care; measure via backtesting/QA).

### 6) Treasury & Liquidity Operations

- **Why agentic**: confirmations, reconciliations, margin calls are workflow-heavy; high need for audit and control; time sensitivity.
- **Where agents fit**: heavy **Governance + Orchestrator** usage; **Do Agents** execute only within strict controls; **Think Agents** assist with confirmation matching and exception narratives.
- **CBA drivers**:
  - **Settlement fails**: reduced fails/penalties; faster exception resolution.
  - **Control evidence**: reduced manual effort for approvals and audit packs.

### 7) Deposit, CASA, and Account Operations

- **Why agentic**: dormancy/reactivation, holds/liens, fees/interest ops, closures are rule-triggered and repeatable; high volume.
- **Where agents fit**:
  - **Do Agents**: rule-driven actions (post-approval), notifications, postings.
  - **Governance Agents**: SoD, risk gating, approval workflows.
  - **Orchestrators**: closure/consolidation journeys with checkpoints.
  - **Think Agents**: exception explanation, customer comms drafts (if applicable).
- **CBA drivers**:
  - **Productivity**: per-request cost; queue times; manual steps removed.
  - **Quality**: defect rates; complaint rates; reconciliation breaks from postings.

### 8) Customer Service Operations (ops layer)

- **Why agentic**: triage, routing, summarization, and fulfillment are ideal for agentic workbenches; major cost is handling time + rework + escalations.
- **Where agents fit**:
  - **Think Agents**: classify intent, draft responses, summarize context across systems.
  - **Orchestrators**: route and track SLAs; coordinate fulfillment steps.
  - **Do Agents**: execute low-risk fulfillment actions (policy gated).
  - **Governance Agents**: identity checks, entitlements, policy compliance.
- **CBA drivers**:
  - **Productivity**: AHT reduction; first-contact resolution; re-open rate.
  - **CX**: time-to-resolution; escalation rates.

### 9) Trade Finance Operations

- **Why agentic**: document checking is rules + exceptions; high-value per case; heavy evidence requirements.
- **Where agents fit**: **Think Agents** for document checking and discrepancy narratives; **Governance** for policy/SoD; **Do Agents** for templated generation; **Orchestrators** for LC/BG workflows.
- **CBA drivers**:
  - **Cycle time**: doc-checking TAT; discrepancy handling time.
  - **Quality**: discrepancy rates; rework; audit issues.

### 10) Cash Management & Corporate Banking Operations

- **Why agentic**: mandate management and virtual accounts are configuration-heavy and error-prone; strong ROI from fewer setup defects and faster onboarding.
- **Where agents fit**: **Orchestrator + Governance** to control approvals; **Do Agents** to execute configuration; **Think Agents** to interpret onboarding docs/requests.
- **CBA drivers**:
  - **Quality**: setup defect reduction; fewer downstream payment breaks.
  - **Productivity**: onboarding time; tickets per corporate client.

### 11) Branch & Teller Operations (Back-Office Support)

- **Why agentic**: ATM reconciliation, cheque clearing exceptions, vault balancing mirror reconciliation patterns; high incident cost when breaks accumulate.
- **Where agents fit**: **Do Agents** for reconciliation and postings (controlled); **Think Agents** for exception classification (e.g., cheque images); **Governance** for approvals; **Orchestrators** for daily close workflows.
- **CBA drivers**:
  - **Operational breaks**: suspense aging; daily close time; incident count.

### 12) Compliance, Audit & Reporting Operations

- **Why agentic**: evidence collection is repetitive; generating audit packs and structured reports is automatable; reduces findings and remediation effort.
- **Where agents fit**: **Think Agents** for evidence summarization; **Governance** for policy validation + access controls; **Orchestrators** for requests and SLA tracking; **Do Agents** for data pulls/pack assembly.
- **CBA drivers**:
  - **Audit effort**: hours per audit request; time to provide evidence.
  - **Findings**: number/severity; cost of remediation; repeat findings.

### 13) Technology & Platform Support Operations (Operations-linked)

- **Why agentic**: batch monitoring and STP exception classification are “continuous control loops”; strong ROI from reduced downtime and faster remediation.
- **Where agents fit**: **Orchestrators** for incident workflows; **Think Agents** for log/alert triage; **Do Agents** for safe runbooks; **Governance** for change controls and execution limits.
- **CBA drivers**:
  - **Reliability**: MTTR, incident frequency, automation of runbooks.
  - **Ops productivity**: tickets per engineer/analyst; false alert reduction.

### 14) Collections & Recovery Operations

- **Why agentic**: segmentation, routing, and reminder journeys scale well; improved prioritization reduces losses; agents reduce manual follow-ups and admin work.
- **Where agents fit**: **Think Agents** for prioritization and scripts; **Orchestrators** for multi-channel journeys; **Do Agents** for scheduling/updates; **Governance** for consent, communications policy, and approvals.
- **CBA drivers**:
  - **Loss avoidance**: roll-rate reduction; cure rates; recovery uplift (carefully controlled experiments).
  - **Productivity**: accounts per collector; contact attempts per success.

### 15) Revenue Assurance & Finance Operations

- **Why agentic**: reconciliation + leakage detection are deterministic; high value from catching missed charges/waivers and resolving breaks fast.
- **Where agents fit**: **Do Agents** for matching and postings (controlled); **Think Agents** for anomaly explanations; **Governance** for posting approvals; **Orchestrators** for close processes.
- **CBA drivers**:
  - **Leakage**: recovered fees; reduced missed charges; reduced write-offs.
  - **Close efficiency**: time to close; manual journals; break backlog.

---

## CBA model template (plug in your bank’s numbers)

### Step 1: Baseline cost per domain

For each domain \(d\):

- \( \textbf{OpsOpEx} \) = total annual operations OpEx (your bank)
- \( \textbf{Share}_d \) = OpEx share of domain \(d\) (as %; calibrated)
- \( \textbf{Cost}_d = \text{OpsOpEx} \times \text{Share}_d \)

### Step 2: Benefits (annual)

For each domain \(d\), estimate benefits in 3 buckets:

- **Hard productivity savings** (capacity removed / vendor cost reduced):
  - \( \text{HardSave}_d = \text{Cost}_d \times \text{SaveRate}_d \times \text{Realization}_d \)
  - Where:
    - \( \text{SaveRate}_d \) = achievable effort reduction (e.g., 20–40%)
    - \( \text{Realization}_d \) = % realized as actual cost-out (e.g., 30–80% depending on redeployment/capacity actions)
- **Loss / leakage avoidance** (where applicable):
  - \( \text{Avoid}_d = \text{BaselineLoss}_d \times \text{AvoidRate}_d \)
- **Compliance / audit savings**:
  - \( \text{CompSave}_d = \text{AuditEffortCost}_d \times \text{ReductionRate}_d \)

Total annual benefit:

- \( \textbf{Benefit}_d = \text{HardSave}_d + \text{Avoid}_d + \text{CompSave}_d \)

### Step 3: Costs (annualized + one-time)

Typical cost components:

- **One-time**: integration adapters, workflow build, controls design, evaluation harness, data remediation, change management.
- **Run-rate**: platform subscription/hosting, model/runtime costs, monitoring, QA, continued improvements, vendor support.

Represent as:

- \( \textbf{CostOneTime}_d \)
- \( \textbf{CostRun}_d \) (annual)

### Step 4: ROI, payback, and guardrails

- **Year-1 net**: \( \text{Net}_d = \text{Benefit}_d - (\text{CostRun}_d + \text{CostOneTime}_d) \)
- **Steady-state net** (post year-1): \( \text{NetSS}_d = \text{Benefit}_d - \text{CostRun}_d \)
- **Payback (months)** (rough): \( 12 \times \frac{\text{CostOneTime}_d}{\max(\text{NetSS}_d, \epsilon)} \)

**CBA quality gates (recommended)**:

- Measurable, monitored KPIs per domain (AHT, backlog, defect rate, SLA compliance, losses/leakage).
- Segregation-of-duties maintained: Think ≠ Execute; Governance gates high-risk actions.
- Controlled experiments (A/B or phased rollout) before counting loss-avoidance benefits.

---

## Inputs I need from you to turn this into a bank-specific CBA (quick)

If you share these, I can produce a calibrated version (still in Markdown) with numbers that *actually* tie out:

- Annual **Ops OpEx** (or total OpEx + % allocated to operations).
- Product mix: retail-heavy / SME / corporate / cards / trade / treasury heavy.
- Current sourcing: in-house vs BPO; major systems involved.
- Current volumes (ballparks): payments/day, chargebacks/month, KYC refresh counts, AML alerts/day, collections accounts/month.
- Any known “pain costs”: fraud loss, chargeback loss, reconciliation break backlog, audit finding remediation spend.


