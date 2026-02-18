# Opportunity

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management, Strategy, Sales Leadership

## Definition

An internally originated initiative to increase revenue, reduce cost, or expand target market segments. The beneficiary of an Opportunity is always the vendor (the builder of the product). Opportunities are created exclusively by internal stakeholders. Opportunities may also originate from internal teams identifying cost efficiencies, technical optimizations, or architectural improvements.

*Signal Type:* Opportunity.

## Purpose

One of three Signal types in the Strategy Dimension (alongside Problem and Need). Opportunities capture **vendor-side business optimization** — they align naturally with the Business Dimensions (2 and 3). As a Signal, an Opportunity is an indicator to be *investigated*, not an approved initiative (see FAQ Q16). Unlike Problems (fix existing) and Needs (expand for customers), Opportunities are driven by the vendor's strategic and economic interests.

## Common Signal Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Brief description of the opportunity |
| Description | Text | Detailed context — what the opportunity is, why it matters |
| Source | Text | Who/where this Signal came from |
| Source Type | Enum | `Customer` / `Prospect` / `Internal - Engineering` / `Internal - Operations` / `Internal - Strategy` / `Internal - Support` / `Data/Analytics` |
| Date Captured | Date | When first recorded |
| Related Signals | List of References (Dim 1) | Links to Signals that may point to the same underlying issue |

## Opportunity-Specific Fields

| Field | Type | Description |
|---|---|---|
| Objective Type | Enum | `Increase Revenue` / `Reduce Cost` / `Expand Market` / `Technical Optimization` / `Other` |
| Sponsor | Reference | The internal stakeholder championing this opportunity |
| Estimated Impact | Text | Rough quantification of the opportunity (e.g., "$2M ARR", "40% infra cost reduction") |

## Statuses

| Status | Description |
|---|---|
| New | Captured but not yet reviewed |
| Triaged | Reviewed, acknowledged as legitimate (not noise) |
| Exploring | Under active Signal Exploration |
| Associated | Linked to an Initiative for coordinated discovery |
| Addressed | A PDR has been produced that addresses this Signal |
| Dismissed | Judged to be noise, duplicate, or not worth pursuing |
| Parked | Legitimate but not currently prioritized |

**State Diagram:**

```
New ──[PM reviews, confirms legitimacy]──► Triaged
 │                                            │
 │  [judged as noise/duplicate]               ├──[Signal Exploration Task created]──► Exploring
 └──────────────────────────────► Dismissed    │                                        │
                                               │  [linked to Initiative                 │
                                               │   during planning]                     │
                                               ├──────────────────────► Associated ◄────┘
                                               │                           │    [also linked
                                               │                           │     to Initiative]
                                               │  [not prioritized         │
                                               │   this cycle]             │
                                               └──────► Parked             │
                                                   │                       │
                                                   │  [re-prioritized      ▼
                                                   │   in future cycle]  [PDR produced
                                                   └──► Triaged          addressing this Signal]
                                                                           │
                                                                           ▼
                                                                       Addressed
```

**Key transitions:** Same as Problem — see Problem entity for detailed transition descriptions.

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Downstream | Idea (Dim 1) | Opportunity spawns Idea(s) — one Opportunity may generate multiple candidate hypotheses |
| Targets | Business KPI (Dim 2) | Opportunity targets improvement in vendor Business KPIs |
| References | Delivery Friction (Dim 2) | Opportunity may aim to address a known Delivery Friction |
| References | Win Barrier (Dim 2) | Opportunity may aim to overcome a known Win Barrier |
| Work Model | Signal Exploration Task (Track 1) | Signal Exploration Tasks investigate this Opportunity |
| Work Model | Research Task (Track 1) | Research Tasks may gather targeted evidence about this Opportunity |
| Work Model | Deliberation (Track 1) | Deliberations may discuss this Opportunity |
| Associated | Initiative (Dim 1) | Opportunity ← associated → Initiative(s) (many-to-many, during planning) |
| Related | Signal (Dim 1) | Related Signals that may point to the same underlying issue |

## Example

"Expanding FX payout support to LATAM currencies could capture a $2M ARR segment currently served by competitors." (Source: Internal - Strategy, Objective Type: Expand Market, Sponsor: VP Product)
