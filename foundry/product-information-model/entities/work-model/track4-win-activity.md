# Win Activity

**Model:** Work Model
**Track:** Win
**Category:** Activity
**Owner:** Sales, Pre-Sales Engineering, Customer Success, Account Management, Product Marketing

## Definition

Win Activity is the proactive, customer-facing execution work that advances Win Outcomes across the AAARRR lifecycle. It is the parent entity for all engagement subtypes — the hands-on work of winning, activating, retaining, and expanding customers.

**PLG / self-service segments:** For segments where the Product lever dominates (e.g., self-service onboarding, free trial, in-product expansion), Win Activity subtypes operate differently. "Implementation/Onboarding" becomes in-product self-service; the Win Track monitors completion funnels and intervenes on stuck accounts. "Pre-sales Engagement" becomes free trial or sandbox; Win Track monitors conversion and intervenes on high-value prospects. The Build Track effectively does "Win" work for these segments (building self-service flows, in-product upsell prompts). Win Monitoring becomes the primary Win Track activity — continuous funnel monitoring — with human engagement reserved for exceptions. The same subtypes apply; the balance shifts from human execution to monitoring + exception-based intervention.

Win Activities operate at two granularities:
- **Account-level** (one-to-one) — work directed at a single customer or prospect account
- **Segment-level** (one-to-segment) — work directed at a customer segment, applicable both pre-sale and post-sale

## Purpose

Makes customer-facing execution work explicit in the Win Track. Without Win Activity, the model captures *what winning looks like* (Vendor Value) and *what to plan* (Win Planning) but not *the actual work of engaging customers and prospects*. Win Activity is where value realization happens — through POCs, onboarding, health interventions, upsell conversations, and segment-wide programs.

The seven subtypes cover the full AAARRR lifecycle:

| Subtype | Granularity | AAARRR Stage | Description |
|---|---|---|---|
| **Pre-sales Engagement** | Account | Acquisition | POC, custom demo, technical evaluation, RFP response. References CRM Deal/Opportunity (external entity, not UPIM). |
| **Implementation / Onboarding** | Account | Activation | Integration, configuration, go-live — including API integration work when customers consume API Modules. See `track4-implementation-onboarding.md` for detailed entity. |
| **Retention Engagement** | Account | Retention | Health intervention, QBR preparation, renewal management. |
| **Expansion Engagement** | Account | Revenue | Upsell proposal, cross-sell campaign, account planning. |
| **Segment Engagement** | Segment | Any AAARRR stage | Awareness campaigns, feature webinars, advocacy workshops, community events, **customer training sessions**, **developer workshops**, and **API capability sessions**. Applies both pre-sale and post-sale. Customer education (training, certification delivery, workshops) is delivered via Segment Engagement; advocacy encompasses both referral/case-study work and education. |
| **Partner Engagement** | Account | Awareness, Acquisition | Partner onboarding, co-selling, partner account management, partner pipeline management. Work directed at a specific partner (one-to-one). References external PRM (Partner Relationship Management) records. Distinct from customer-facing engagement — the "account" here is the partner. |
| **Revenue Operations Engagement** | Account | Revenue | Operational, customer-facing work to ensure revenue is realized: invoicing/billing communication, collections follow-up, renewal processing, revenue recognition coordination with Finance. Distinct from Expansion Engagement (which is upsell/cross-sell); Revenue Operations ensures committed revenue is collected. Billing disputes are handled as Win Case (Complaint). |

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Brief description of the engagement work |
| Subtype | Enum | `Pre-sales` / `Implementation` / `Retention` / `Expansion` / `Segment` / `Partner` / `Revenue Operations` |
| Granularity | Enum | `Account` / `Segment` |
| AAARRR Stage | Enum | `Awareness` / `Acquisition` / `Activation` / `Retention` / `Revenue` / `Referral` |
| Customer / Prospect | Reference (Customer Value) | The specific customer or prospect account (for Account-level engagements) |
| Customer Segment | Reference (Customer Value) | The target customer segment (for Segment-level engagements) |
| Win Outcome(s) | List of References (Vendor Value) | Which Win Outcomes this engagement advances |
| Win Stakeholder(s) | List of References (Vendor Value) | Which Win Stakeholders perform this engagement work |
| Initiative | Reference (Strategy) | Which Initiative this engagement aligns to |
| Win Enablement Assets | List of References | Which enablement assets are used in this engagement |
| CRM Deal / Opportunity | External Reference | CRM deal or opportunity record (for Pre-sales subtype; external entity, not UPIM) |
| PRM Partner | External Reference | Partner record in PRM system (for Partner subtype; external entity, not UPIM) |
| Description | Text | Detailed description of the engagement scope and approach |
| Owner | String | Role/person accountable for this engagement |

## Statuses

Status lifecycle varies by subtype:

**Pre-sales Engagement:**

| Status | Description |
|---|---|
| Qualified | Prospect is qualified; engagement is scoped |
| Engaged | Active engagement with prospect (demos, technical discussions) |
| POC | Proof-of-concept is underway |
| Won | Deal closed successfully |
| Lost | Deal lost or prospect disqualified |

**Implementation / Onboarding:**

| Status | Description |
|---|---|
| Scoped | Implementation requirements are defined |
| In Progress | Integration and configuration work is underway |
| Go-Live | Customer is live with initial capabilities |
| Complete | Full onboarding is complete; customer is self-sufficient |

**Retention Engagement:**

| Status | Description |
|---|---|
| Identified | Health risk or renewal event identified |
| In Progress | Intervention or renewal preparation is underway |
| Resolved | Health issue addressed or renewal secured |
| Churned | Customer churned despite intervention |

**Expansion Engagement:**

| Status | Description |
|---|---|
| Identified | Expansion opportunity identified |
| Proposed | Upsell/cross-sell proposal presented to customer |
| Negotiating | Commercial terms under discussion |
| Closed | Expansion deal closed successfully |
| Declined | Customer declined the expansion opportunity |

**Segment Engagement:**

| Status | Description |
|---|---|
| Planned | Segment engagement is scoped and scheduled |
| In Progress | Campaign, event, or program is actively running |
| Completed | Engagement has concluded; results captured |

**Partner Engagement:**

| Status | Description |
|---|---|
| Onboarding | Partner is being onboarded; enablement and certification in progress |
| Active | Partner is active; co-selling, pipeline management, ongoing support |
| Review | Partner performance or contract under review |
| Inactive | Partner is paused or no longer active |

**Revenue Operations Engagement:**

| Status | Description |
|---|---|
| In Progress | Invoicing, collections, or renewal processing underway |
| Resolved | Billing/renewal cycle complete; revenue recognized or issue closed |
| Escalated | Dispute or exception escalated (may spawn Win Case) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Advances | Win Outcome (Vendor Value) | Win Activity advances specific Win Outcomes |
| Aligned to | Initiative (Strategy) | Win Activity aligns to strategic Initiatives |
| Performed by | Win Stakeholder (Vendor Value) | Win Activity is performed by Win Stakeholders |
| Uses | Win Enablement | Win Activity uses enablement assets (decks, demos, playbooks) |
| Scoped to | Customer Segment (Customer Value) | Segment Engagements target a specific Customer Segment |
| References | CRM Deal / Opportunity (External) | Pre-sales Engagements reference external CRM records |
| References | PRM Partner (External) | Partner Engagements reference external PRM (Partner Relationship Management) records |
| Driven by | Win Planning (Win) | Win Planning drives engagement activities |
| Assessed by | Win Review (Win) | Win Reviews assess engagement results and may produce Feedback |
| Serves | Developer Persona (Ecosystem) | Developer-facing engagement work (API POCs, developer workshops, integration support) |
| References | API Module (Ecosystem) | Engagement may involve API integration work |

## Examples

**Pre-sales Engagement (Account-level):**

"Run POC for Prospect X — LATAM Enterprise, SAP integration, 3-week timeline."
- **Subtype:** Pre-sales
- **Granularity:** Account
- **AAARRR Stage:** Acquisition
- **Win Outcome:** Close LATAM deals in 90-day cycle
- **Win Stakeholder:** Pre-Sales Engineer
- **Win Enablement:** LATAM demo environment, competitive battlecard
- **CRM Deal:** Prospect X — $600K ACV opportunity

**Segment Engagement (Segment-level):**

"LATAM Enterprise feature webinar: batch payout processing launch."
- **Subtype:** Segment
- **Granularity:** Segment
- **AAARRR Stage:** Activation
- **Win Outcome:** First live transaction within 30 days (Activation)
- **Customer Segment:** LATAM Enterprise (40 existing customers)
- **Win Stakeholder:** Product Marketing Manager
- **Win Enablement:** Batch processing demo script, customer success stories

"LATAM API integration workshop: Cross-Border Payments API hands-on session for integration engineers."
- **Subtype:** Segment
- **Granularity:** Segment
- **AAARRR Stage:** Activation
- **Win Outcome:** First live transaction within 30 days (Activation)
- **Customer Segment:** LATAM Enterprise (developers/integration engineers)
- **Win Stakeholder:** Developer Relations, Implementation Consultants
- **Win Enablement:** Cross-Border API developer onboarding guide, sandbox
- **References:** Cross-Border Payments API Module (Ecosystem)

**Partner Engagement (Account-level):**

"Onboard and enable Banco Regional as LATAM channel partner — co-marketing, certification, Q3 pipeline target."
- **Subtype:** Partner
- **Granularity:** Account
- **AAARRR Stage:** Awareness, Acquisition
- **Win Outcome:** 80% brand recall in LATAM fintech CFO community; close LATAM deals in 90-day cycle
- **Win Stakeholder:** Partner Manager
- **Win Enablement:** LATAM partner co-marketing kit, partner certification program
- **PRM Partner:** Banco Regional — LATAM referral partner
