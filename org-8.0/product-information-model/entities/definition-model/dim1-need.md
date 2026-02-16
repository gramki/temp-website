# Need

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management

## Definition

A missing Capability or Feature expressed by one or more customers or prospects. A Need always originates externally and is always about expanding the product — adding something that does not exist today. When picked for discovery, PMs should be able to trace back to the specific customers or users who expressed the need.

*Signal Type:* Need.

## Purpose

One of three Signal types in the Strategy Dimension (alongside Problem and Opportunity). Needs capture what the product **does not yet do** from the customer's perspective. As a Signal, a Need is an indicator of demand to be *investigated*, not a customer requirement to be fulfilled (see FAQ Q16). Needs align naturally with the User-Centric Dimension — they represent user/customer demand for new functionality. Each customer or user may upvote a Need to express their interest, providing a demand indicator for prioritization.

## Common Signal Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Brief description of the need |
| Description | Text | Detailed context — what is missing, who wants it, why |
| Source | Text | Who/where this Signal came from |
| Source Type | Enum | `Customer` / `Prospect` / `Internal - Engineering` / `Internal - Operations` / `Internal - Strategy` / `Internal - Support` / `Data/Analytics` |
| Date Captured | Date | When first recorded |
| Related Signals | List of References (Dim 1) | Links to Signals that may point to the same underlying issue |

## Need-Specific Fields

| Field | Type | Description |
|---|---|---|
| Requesting Customers | List of References | Customers or prospects who expressed this need |
| Upvotes | Count | Number of customers/users who have expressed this need |

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
| Downstream | Idea (Dim 1) | Need spawns Idea(s) — one Need may generate multiple candidate hypotheses |
| Work Model | Signal Exploration Task (Track 1) | Signal Exploration Tasks investigate this Need |
| Work Model | Research Task (Track 1) | Research Tasks may gather targeted evidence about this Need |
| Work Model | Deliberation (Track 1) | Deliberations may discuss this Need |
| Associated | Initiative (Dim 1) | Need ← associated → Initiative(s) (many-to-many, during planning) |
| Related | Signal (Dim 1) | Related Signals that may point to the same underlying issue |
| Upstream | Feedback (Track 4) | A Feedback item from the Win Track may correspond to a Need |

## Example

"Three enterprise prospects require batch payout file upload (CSV/SFTP) — a capability the product does not currently offer." (Source: Prospect, 3 requesting customers, 12 upvotes)
