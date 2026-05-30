# Pain

**Model:** Definition Model
**Dimension:** Customer Value (Why Buy)
**Owner:** Product Management, UX Research, Customer Success

## Definition

A specific, concrete suffering or frustration experienced by a User Persona (User Experience) in their current workflow — before or outside the product's intervention. Pains are endured by users but *cared about* by Buying Personas, who are motivated to purchase a solution that relieves them.

## Purpose

Pain completes the JTBD mapping in the Customer Value Dimension:

| JTBD Concept | UPIM Entity | Perspective | Example |
|---|---|---|---|
| **Buyer's Job** | Business Outcome | What the buyer needs to achieve strategically | "Reduce cross-border payment costs by 40%" |
| **User's Pain** | **Pain** | What the user suffers operationally/experientially | "AP Clerk spends 4 hours/day manually reconciling FX transactions" |
| **Value delivered** | Value Proposition | How the product addresses both | "Automated reconciliation eliminates manual work, cutting costs by 60%" |

Business Outcome captures the *strategic justification* (buyer-level). Pain captures the *visceral urgency* (user-level). Together they form the complete "Why Buy" motivation — the buyer wants the outcome, but the pain is what makes it *feel urgent*.

**Key distinction: who endures vs. who cares.**
- The **User Persona** (User Experience) *endures* the Pain — they experience it daily in their workflow.
- The **Buying Persona** (Customer Value) *cares about* the Pain — it motivates their purchase decision, even if they never personally experience it.

This separation matters because the same Pain can be cared about by different Buying Personas for different reasons: the CFO cares about the cost impact, the Operations Manager cares about team productivity, the CTO cares about error rates affecting system reliability.

## Fields

| Field | Type | Description |
|---|---|---|
| Description | Text | What the pain is — specific, concrete, observable |
| User Persona | Reference (User Experience) | Who endures/faces this pain |
| Customer Segment | Reference (Customer Value) | Which segment this pain applies to |
| Frequency | Enum | `Constant` / `Daily` / `Weekly` / `Occasional` / `Event-triggered` |
| Severity | Enum | `Critical` (blocks work) / `Significant` (degrades work) / `Minor` (annoyance) |
| Current Workaround | Text | How the user copes today (manual process, competitor tool, spreadsheet, etc.) |
| Quantifiable Impact | Text | Measurable cost of the pain (time lost, error rate, $ cost) |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Identified | Pain is known but not yet validated |
| Validated | Pain is confirmed through research (interviews, data, observation) |
| Addressed | Pain is relieved by the product (linked to active Value Proposition) |
| Accepted | Pain is acknowledged but not being addressed (documented trade-off) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Endured by | User Persona (User Experience) | User Persona endures this Pain |
| Cared about by | Buying Persona (Customer Value) | Buying Persona(s) care about this Pain (motivates purchase) |
| Anchored to | Customer Segment (Customer Value) | Pain exists within a Customer Segment context |
| Addressed by | Value Proposition (Customer Promise, Customer Value) | Value Proposition relieves this Pain |
| May surface as | Signal — Problem or Need (Strategy) | A Pain may generate a Problem or Need Signal |
| Work Model | Modeling Task (Discovery) | Modeling Tasks identify and validate Pains |
| Work Model | Signal Exploration Task (Discovery) | Signal Exploration may uncover Pains |

## Examples

| Pain | User Persona (User Experience) | Buying Personas who care (Customer Value) | Quantifiable Impact |
|---|---|---|---|
| "AP Clerk spends 4 hours/day manually reconciling FX transactions across 3 systems" | AP Clerk | CFO (cost), AP Ops Manager (productivity) | 1,000 hours/year, 12% error rate |
| "6-click FX rate confirmation flow causes rate expiry on 15% of transactions" | AP Clerk | CFO (lost money), VP Eng (UX quality) | $45K/year in expired rate re-quotes |
| "Integrating a new payment provider requires 6 weeks of custom adapter work" | Integration Engineer | CTO (engineering cost), VP Eng (velocity) | 6 weeks engineering time per provider |
| "Compliance team manually prepares PCI-DSS evidence packages — 3 weeks per audit cycle" | Compliance Analyst | CFO (audit cost), CTO (compliance risk) | 120 hours/audit, risk of missed deadlines |

## Notes

- Pain is about the *current state* — what the user suffers today, before or outside the product's intervention. It is not a feature request or a requirement. A Pain may inspire a Signal (Problem or Need) in Strategy, which then enters the Discovery Track.
- Pains should be captured at a granularity that makes them actionable for positioning and sales, not at feature-level detail. "4 hours/day manual reconciliation" is the right level; "reconciliation screen lacks a filter dropdown" is too granular (that's a Feature concern in Structural).
- A single Pain may be relieved by multiple Value Propositions, and a single Value Proposition may relieve multiple Pains.
