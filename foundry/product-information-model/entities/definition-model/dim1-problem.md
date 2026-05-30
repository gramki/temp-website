# Problem

**Model:** Definition Model
**Dimension:** Strategy
**Owner:** Product Management

## Definition

A limitation, gap, or challenge associated with delivered Modules, Capabilities, or Features — but not a functional Bug (which belongs in the Build Track). Problems represent issues discovered in production that degrade the user experience, hinder adoption, or create operational friction. A Problem can be specified at any granularity of Module (M), Capability (C), or Feature (F).

*Signal Type:* Problem.

## Purpose

One of three Signal types in the Strategy Dimension (alongside Need and Opportunity). Problems capture what is **wrong or insufficient** with the existing product. They are reported by both internal and external stakeholders. As a Signal, a Problem is an observation to be *investigated*, not a requirement to be fulfilled (see FAQ Q16). Problems align naturally with the Technical and Bridge tiers of the Definition Model — they reference existing product structure (Dimension 8).

## Common Signal Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Brief description of the problem |
| Description | Text | Detailed context — what is wrong, who is affected, how it manifests |
| Source | Text | Who/where this Signal came from |
| Source Type | Enum | `Customer` / `Prospect` / `Internal - Engineering` / `Internal - Operations` / `Internal - Strategy` / `Internal - Support` / `Data/Analytics` |
| Date Captured | Date | When first recorded |
| Related Signals | List of References (Strategy) | Links to Signals that may point to the same underlying issue |

## Problem-Specific Fields

| Field | Type | Description |
|---|---|---|
| Granularity | Enum (M/C/F) | The level at which the problem is specified: Module, Capability, or Feature |
| Affected Entity | Reference (Structural) | The specific M/C/F this problem is associated with |
| Reporter | Reference | The stakeholder who reported the problem |
| Upvotes | Count | Number of stakeholders who have expressed interest in resolution |

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

**Key transitions:**
- `New → Triaged`: PM reviews Signal, confirms it is legitimate and not noise
- `New → Dismissed`: Signal is noise, duplicate, or already addressed
- `Triaged → Exploring`: Signal Exploration Task created to investigate
- `Triaged → Associated`: Linked to an Initiative during a planning cycle (may skip Exploring if Initiative provides sufficient context)
- `Triaged → Parked`: Legitimate but no current capacity or strategic fit
- `Exploring → Associated`: Exploration reveals relevance to an Initiative
- `Associated → Addressed`: A PDR is produced that addresses this Signal (Go, Kill, or Pivot)
- `Parked → Triaged`: Re-enters active consideration in a future planning cycle

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Downstream | Idea (Strategy) | Problem spawns Idea(s) — one Problem may generate multiple candidate hypotheses |
| Structural ref | Module / Capability / Feature (Structural) | Problem references the M/C/F it is associated with |
| Work Model | Signal Exploration Task (Discovery) | Signal Exploration Tasks investigate this Problem |
| Work Model | Research Task (Discovery) | Research Tasks may gather targeted evidence about this Problem |
| Work Model | Deliberation (Discovery) | Deliberations may discuss this Problem |
| Associated | Initiative (Strategy) | Problem ← associated → Initiative(s) (many-to-many, during planning) |
| Related | Signal (Strategy) | Related Signals that may point to the same underlying issue |
| Upstream | Feedback (Win) | A Feedback item from the Win Track may correspond to a Problem |
| May originate from | FIR (Track 4, PFR-Win) | A Problem Signal may be routed from an FIR when triage identifies a product limitation (DR-032) |

## Example

"The FX rate-lock confirmation flow takes 6 clicks — mid-market AP clerks report it as too cumbersome for high-volume payout runs." (Source: Customer, Granularity: Feature, Affected Entity: FX Rate-Lock Confirmation)
