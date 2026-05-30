# User Journey

**Model:** Definition Model
**Dimension:** User Experience
**Owner:** UX Designers, Product Management

## Definition

The end-to-end path a User Persona follows to accomplish a Job through a specific UX Channel. A Journey is scoped to a single Channel — the same Job may have different Journeys across different Channels, with each Journey adapted to that Channel's interaction modality and constraints.

## Purpose

User Journey maps the sequential experience of a user from intent to completion. It connects:
- The *who* (Persona) and the *why* (Job) to the *how* (the actual flow of steps)
- The experiential surface (User Experience) to the product's structural flows (Value Streams in Structural)

Without User Journeys:
- Feature design has no experiential context — features are built for capabilities, not for user flows
- Cross-channel experience strategy is implicit — no way to identify equivalent or continuous flows
- Value Stream traversal (Structural) has no user-facing representation

**Touchpoints are below the Journey level.** Specific UI elements (buttons, forms, dropdowns) are Build Track work artifacts, not Definition Model entities. The Definition Model captures down to the Journey level; screen-level detail lives in PSDs, prototypes, and design specifications.

**Discovery provenance:** Journeys are designed during Specification (PSD authoring), validated through Prototypes/Spikes, and refined iteratively.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive journey name (e.g., "Initiate and approve a cross-border payout") |
| Job(s) Accomplished | List of References (User Experience) | Which Job(s) this journey accomplishes |
| User Persona(s) | List of References (User Experience) | Which Persona(s) follow this journey |
| UX Channel | Reference (User Experience) | Through which Channel this journey is experienced |
| Steps (Summary) | Text | High-level step sequence — not screen-level detail but enough to convey the flow shape |
| Value Stream(s) Traversed | List of References (Structural) | Which Value Streams this journey traverses (maps UX flow to product structure) |
| Capabilities Engaged | List of References (Structural) | Which Capabilities are engaged during this journey. Provides finer-grained structural mapping than Value Stream alone — identifies which specific product abilities the journey requires at each step. |
| Equivalent Journeys | List of References (User Experience) | Journeys in other channels that accomplish the same Job (independent alternatives) |
| Continuable From | List of References (User Experience) | Journeys in other channels that can hand off to this journey |
| Continuable To | List of References (User Experience) | Journeys in other channels that this journey can hand off to |

## Statuses

| Status | Description |
|---|---|
| Designed | Journey has been specified (PSD authored) but not yet built |
| Prototyped | Journey has been validated through a prototype or spike |
| Active | Journey is live in the product |
| Deprecated | Journey is being replaced or phased out |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Accomplishes | Job (User Experience) | Journey accomplishes one or more Jobs |
| Followed by | User Persona (User Experience) | One or more Personas follow this Journey |
| Experienced through | UX Channel (User Experience) | Journey is experienced through a specific Channel |
| Traverses | Value Stream (Structural) | Journey traverses Value Stream(s) |
| Engages | Capability (Structural) | Journey engages specific Capabilities within the traversed Value Streams |
| Equivalent to | User Journey (User Experience) | Same Job, different Channel — independent alternatives |
| Continuable from/to | User Journey (User Experience) | Sequential handoff across Channels |
| Work Model | Specification Task (Discovery) | PSDs specify Journeys |
| Work Model | Prototype / Spike (Discovery) | Prototypes validate Journey design |

## Examples

| Journey | Job | Persona | Channel | Value Stream | Capabilities Engaged | Cross-Channel |
|---|---|---|---|---|---|---|
| "Initiate and approve a cross-border payout" | Process cross-border payout | AP Clerk | Web + Self-serve (Dashboard) | Cross-Border Payout Processing | Payment Initiation, Automated Rate Locking, OFAC Screening, Payment Execution | Equivalent to: "Approve payout" (Mobile); Continuable from: "Request payout approval" (Email) |
| "Approve payout" | Process cross-border payout | AP Manager | Mobile + Self-serve | Cross-Border Payout Processing | Payment Approval, Payment Execution | Equivalent to: "Initiate and approve" (Web); Continuable from: "Request payout approval" (Email) |
| "Request payout approval" | Process cross-border payout | AP Clerk | Email + Self-serve | Cross-Border Payout Processing | Payment Notification | Continuable to: "Approve payout" (Mobile), "Initiate and approve" (Web) |
| "Analyze FX exposure dashboard" | Analyze FX exposure | Treasury Analyst | Web + Self-serve (Dashboard) | Multi-Currency Reporting | FX Exposure Analysis, Report Generation | — |
| "Generate compliance audit report" | Generate compliance audit report | Compliance Officer | Web + Self-serve (Dashboard) | Compliance Screening | OFAC Screening, Audit Trail, Report Generation | — |
| "Resolve payment issue via support" | Process cross-border payout | AP Clerk | Chat + Assisted | Cross-Border Payout Processing | Payment Inquiry, Transaction Lookup | — |
