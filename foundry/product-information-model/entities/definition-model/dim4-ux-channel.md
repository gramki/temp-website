# UX Channel

**Model:** Definition Model
**Dimension:** User Experience
**Owner:** Product Management, UX Design

## Definition

The access mechanism through which a human persona reaches the product, typed by two orthogonal axes: **Interaction Modality** (by technology) and **Engagement Mode** (by service model). Each UX Channel is implemented by exactly one Human-Interactive Module (Structural). A product defines which cells in the Modality × Mode matrix it occupies; most products serve a subset.

UX Channels serve **all human personas** — User Experience User Personas and Operational Operational Personas. An SRE uses Web dashboards, receives Email alerts, runs CLI commands, gets Voice/IVR escalation calls, and uses Mobile apps for on-call — the same interaction modalities and engagement modes. The channel taxonomy is universal for any human accessing the product. UX Channel is defined in User Experience (the natural home for human experience concepts) but referenced cross-dimensionally by Operational Operational Journeys. See DR-023.

## Purpose

UX Channel answers "through what medium does the persona access the product?" This is a strategic product decision — each channel requires a dedicated Human-Interactive Module, with its own capabilities, features, and technical implementation. Without UX Channel:
- The distinction between "what the product can do" (Capabilities) and "how the user accesses it" (Channel) is implicit
- Channel investment decisions ("should we build a mobile app?" or "should we build an operational CLI?") have no entity to anchor to
- Journey design has no context — a web journey and a mobile journey for the same Job (user or operational) have fundamentally different constraints

**Channel investment is a PDR-level decision.** Building a new channel means building a new HI Module — it's a significant investment in design, engineering, and ongoing maintenance. UX Channels carry a lifecycle and are governed through Discovery (Deliberation → PDR). This applies equally to customer-facing channels and operational channels.

## Interaction Modality (by technology)

| Modality | Description | Constraints |
|---|---|---|
| **Web** | Browser-based application | Full screen real estate; keyboard + mouse; session-based |
| **Mobile** | Native mobile application | Small screen; touch-based; intermittent connectivity; push notifications |
| **Chat** | Conversational interface (Slack, Teams, in-app chat, chatbot) | Linear conversational flow; short exchanges; text-primary |
| **Voice** | IVR, voice assistant, phone-based | No visual context; sequential interaction; hands-free |
| **Email** | Asynchronous notification with embedded actions | Asynchronous; limited interactivity; wide reach |
| **CLI** | Command-line / terminal interface | Developer-facing; scriptable; text-only |
| **Embedded** | Widget, plugin, or component hosted within a customer's or third-party application | Vendor controls the component, not the host page; fragment of a journey, not a full journey; must be self-contained; governed by host's constraints (iframe, SDK, web component) |

## Engagement Mode (by service model)

| Mode | Description | Win Track Implication |
|---|---|---|
| **Self-serve** | Persona acts independently; product guides through UI/UX | Win Track monitors funnels; intervenes on stuck accounts (PLG pattern) |
| **Assisted** | Persona + human agent collaborate through the product | Win Track manages agent engagement (CS, Support); co-browsing, screen sharing |
| **Managed** | Agent acts on behalf of persona; persona receives outcome | Win Track drives all engagement; product is the agent's tool |

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive channel name (e.g., "Customer Dashboard — Web Self-serve") |
| Interaction Modality | Enum | `Web` / `Mobile` / `Chat` / `Voice` / `Email` / `CLI` / `Embedded` |
| Engagement Mode | Enum | `Self-serve` / `Assisted` / `Managed` |
| Implemented by | Reference (Structural) | Which Human-Interactive Module implements this channel |
| Target Persona(s) | List of References (User Experience) | Which User Personas primarily use this channel |
| Journeys Supported | List of References (User Experience) | Which User Journeys are experienced through this channel |
| Rationale | Text | Why this channel exists — what user need or strategic goal it serves |
| Accessibility Standard | String | Accessibility compliance target (e.g., WCAG 2.1 AA, Section 508). Influences HI Module design and testing requirements. |

## Statuses

| Status | Description |
|---|---|
| Proposed | Channel has been identified as a candidate (pre-Deliberation) |
| Approved | Channel investment has been approved via PDR |
| Active | Channel is live and serving users |
| Deprecated | Channel is being phased out (existing users supported; no new investment) |
| Retired | Channel is fully decommissioned |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Implemented by | Human-Interactive Module (Structural) | One-to-one: each Channel is implemented by one HI Module |
| Supports | User Journey (User Experience) | Channel supports one or more Journeys |
| Used by | User Persona (User Experience) | User Personas access the product through this Channel |
| Used by | Operational Persona (Operational) | Operational Personas access the product through this Channel (cross-dimensional) |
| Referenced by | Operational Journey (Operational) | Operational Journeys are experienced through UX Channels |
| Justified by | PDR (Strategy) | Channel investment is justified by a PDR |
| Work Model | Deliberation (Discovery) | Channel decisions emerge from Deliberations |
| Work Model | Specification Task (Discovery) | PSDs specify Channel's HI Module |

## Examples

| Channel | Modality | Mode | HI Module (Structural) | Personas | Status |
|---|---|---|---|---|---|
| Customer Dashboard | Web | Self-serve | Dashboard Web Module | AP Clerk, Treasury Analyst, Finance Admin | Active |
| Mobile Approvals | Mobile | Self-serve | Mobile Approvals App | AP Manager, Treasury Analyst | Active |
| Support Chat | Chat | Assisted | Support Chat Module | AP Clerk, Finance Admin | Active |
| Admin Console | Web | Managed | Admin Console Module | CS Manager (agent acts for customer) | Active |
| Developer Portal | Web | Self-serve | Developer Portal Module | Integration Engineer | Active |
| Email Notifications | Email | Self-serve | Notification Service (HI) | AP Clerk, Treasury Analyst | Active |
| Payment Chatbot | Chat | Self-serve | Chatbot Module | AP Clerk | Proposed |
| Payment Widget | Embedded | Self-serve | Payment Widget Module | Customer's End-User (via customer's app) | Active |
| Salesforce Plugin | Embedded | Self-serve | Salesforce Integration Module | Account Executive (via Salesforce) | Active |
| Monitoring Dashboard | Web | Self-serve | Monitoring Dashboard Module | Reliability Operator (Operational) | Active |
| On-Call Alerts | Email + Voice | Self-serve | Alert Notification Module | Reliability Operator (Operational) | Active |
| Ops CLI | CLI | Self-serve | Ops CLI Module | Platform Operator, Reliability Operator (Operational) | Active |
