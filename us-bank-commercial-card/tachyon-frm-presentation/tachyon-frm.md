# Tachyon FRM Deep Dive Presentation Outline

## 1) Purpose of This Document

This outline translates FRM deep-dive questions into a marketing-ready presentation structure for the US Bank Commercial Cards prospect discussion.

Use this as the source-of-truth brief for the deck team:
- What each slide must cover
- What proof/artifacts to include
- What to demo vs what to present
- What open inputs are still needed

---

## 2) Audience + Outcome

**Primary audience**
- Fraud leadership
- Operations and risk teams
- Product/platform stakeholders

**Desired outcome**
- Establish confidence in Tachyon + Featurespace fraud architecture
- Demonstrate operational control (rules, governance, case management)
- Show end-to-end response for fraud, compromise, token fraud, and re-issue
- Clarify deployment model (multi-tenant), ownership model, and rollout path

---

## 3) Deck Storyline (Recommended Flow)

1. Why this matters for USB Commercial Cards
2. Tachyon FRM architecture, partner model, and performance characteristics
3. Exhaustive entities, states, and events reported to FRM (RT and NRT), including 3DS authentication events
4. FRM decision model and action recommendations (RT and NRT)
5. Case management capabilities and workflows
6. Case commands: block, re-issuance, and financial actions
7. Notification capabilities
8. User-managed risk and self-serve capabilities
9. Extensibility and configurability
10. Reporting and analytics
11. Rule engine setup: model management, supervision capabilities, and tenancy
12. Operational contracts with the bank (ownership model, controls, and governance)
13. FRM-specific compliance posture
14. Deep-dive demo scenarios and proof points
15. Why Tachyon FRM for USB Commercial Cards
16. Next steps

---

## 4) Slide-by-Slide Outline with Build Instructions

## Slide 1 - Executive Context and Objectives

**Slide goal**
- Align on the FRM deep-dive scope and business outcomes.

**What to include**
- One-line positioning: "Tachyon FRM delivers rich ML-led decisioning, deep card/token coverage, rich actions, and cardholder-managed risk controls."
- 3-4 objectives: reduce fraud loss, reduce false positives, preserve customer experience, improve operational control.
- Cardholder-managed controls are exercisable by cardholders and program admins; Operations Center provides governance/oversight.
- Scope callout: authorization flow, case management, alert routing, token and compromise handling.
- Scope exclusion: this deck focuses on transaction fraud decisioning and case management for commercial cards. AML/KYC, credit risk decisioning, and network-level fraud detection are not in scope for this session.

**Infographic type:** Title card with icon tiles

**Slide layout**
- *Top third:* Slide title ("Tachyon FRM Deep Dive: USB Commercial Cards") with the one-line positioning statement as a subtitle.
- *Middle:* Four equal-width tiles in a single row, each with an icon and 3-5 word label:
  - Tile 1: Reduce fraud loss
  - Tile 2: Reduce false positives
  - Tile 3: Preserve cardholder experience
  - Tile 4: Improve operational control
- *Below tiles:* One line: "Cardholder-managed controls are exercisable by cardholders and program admins; Operations Center provides governance and oversight."
- *Lower section:* Scope callout as a light-shaded box with two rows:
  - Row 1 (In scope): authorization flow, case management, alert routing, token and compromise handling.
  - Row 2 (Scope exclusion — smaller font, gray or footnote-style): "AML/KYC, credit risk decisioning, and network-level fraud detection are not in scope for this session."

**Build notes**
- Keep this non-technical; set stakes in business language.
- The scope exclusion is visually subordinate — there for the presenter to reference if scope-creep questions arise, not a prominent callout.

---

## Slide 2 - FRM Capability Map (Coverage View)

**Slide goal**
- Show complete coverage of the deep-dive asks in one visual.

**Why this matters**
- Every capability discussed today is production-ready and out-of-box — reducing implementation timeline and integration risk to day-1 operations.

**What to include**
- Out-of-box readiness statement for all discussed capabilities.
- Customization boundary statement: customer-specific work is primarily integrations and workflow tailoring.
- Capability blocks aligned to storyline:
  - Entities/states/events (RT/NRT)
  - Decision model and action recommendations (RT/NRT)
  - Case management, commands, and financial actions
  - Notification and cardholder-managed risk
  - Extensibility/configurability
  - Reporting and analytics
  - Rule engine, model management, tenancy
  - Operational contracts
  - FRM-specific compliance
- Legend: "Presentation", "Demo", "Bank decision required."

**Infographic type:** 3x3 block grid (or radial hub-and-spoke)

**Slide layout**
- *Top:* Two statement banners:
  - "All capabilities are production-ready and out-of-box."
  - "Customer-specific work is primarily integrations and workflow tailoring."
- *Center (main visual):* Nine capability blocks arranged in a 3x3 grid with "Tachyon FRM" as the central label. Each block shows:
  - Block label (from the capability list)
  - Slide number reference (e.g., "→ Slide 4")
  - A small icon badge: one of three legend markers (Presentation / Demo / Bank decision required)
  - The nine blocks:
    1. Entities/states/events (RT/NRT) → Slide 4
    2. Decision model and action recommendations (RT/NRT) → Slide 5
    3. Case management, commands, and financial actions → Slides 6-7
    4. Notification and cardholder-managed risk → Slides 8-9
    5. Extensibility/configurability → Slide 10
    6. Reporting and analytics → Slide 11
    7. Rule engine, model management, tenancy → Slide 12
    8. Operational contracts → Slide 13
    9. FRM-specific compliance → Slide 14
- *Bottom-left corner:* Legend strip — three icons with labels: "Presentation", "Demo", "Bank decision required"
- Each capability block maps back to the following deep-dive topics from the original engagement:
  - Fraud and compromised card handling (virtual cards, BIN attacks)
  - Fraud decisioning architecture (Featurespace integration, model types, latency)
  - Tenancy model (data isolation, encryption boundaries, config separation)
  - Rule authoring, testing, versioning, change control, rollback, and deployment
  - Fraud model and profile maturation (supervised ML, custom models, silent-mode ramp)
  - Case management and workflow (triggers, states, SLA tracking, audit trail)
  - Fraud alert routing (cardholder vs program admin, channels, confirmation flows)
  - Tokenization and token fraud handling (provisioning signals, device binding, token-specific controls)
  - Compromised card detection, blocking, and re-issuance (timing, PAN/token replacement, bulk actions)

**Build notes**
- The 3x3 grid is lower production risk than a radial diagram; either works.
- Add numbered references to later slides for easy navigation in Q&A.
- The storyline (Section 3) has 16 narrative beats; the deck has 17 slides because Slide 2 (this capability map) is a navigation aid, not a storyline beat. Storyline item N maps to Slide N+1 for items 2 onward.

---

## Slide 3 - Solution Architecture: Tachyon + Featurespace

**Slide goal**
- Explain platform roles, integration boundaries, and performance characteristics.

**Why this matters**
- Under-200ms decisioning with 30K TPS capacity means fraud decisions happen inside the authorization window without adding perceptible latency to the cardholder or merchant experience.

**What to include**
- Pre-integrated fraud provider: Featurespace.
- Extensibility statement: additional risk rule engines/providers can be integrated (current capability).
- High-level flow: transaction event -> Tachyon FRM -> one or more risk rule engines -> action tags -> Tachyon action execution.
- Integration touchpoints: auth stream, risk scoring, action callback, case/incident feed.
- 3DS / step-up authentication integration:
  - Full native support for ACS (Access Control Server) authentication events.
  - EMV Co 3DS 2.2 compliant ACS included in the platform.
  - Authentication events (AReq, CReq, CRes) are RT and correlated to the originating transaction at decision time.
  - The rule engine sees both the transaction event and its authentication lifecycle signals in a single RT pass.
- Use this product naming in the architecture:
  - Tachyon Switch (Transaction Processing Engine) -> transaction events and switch decisions
  - ACS (3DS 2.2) -> authentication events (AReq, CReq, CRes) correlated to transactions
  - Customer Lifecycle Management -> demographic detail changes
  - Card Management System -> card issuance/re-issuance/replacement
  - Tachyon Credit -> repayments and credit-limit updates
  - Notification Center -> two-way notification response inputs
  - Token Management System -> token creation and status updates
- Diagram callout: include Tachyon FRM + Featurespace + an additional risk rule engine in Tachyon Switch transaction processing flow. Show ACS as an RT event source feeding into the decisioning flow.
- Performance characteristics:
  - RT risk rule execution, including Featurespace round-trip, completes in under 200ms.
  - Architecture is horizontally scalable; routinely load-tested up to 30,000 TPS.
  - Throughput ceiling is infrastructure-bound, not architecture-bound.

**Infographic type:** Left-to-right architecture diagram with callout boxes

**Slide layout**
- *Main area (70% of slide):* Architecture diagram flowing left to right:
  - Left column (Event Sources) — seven labeled boxes stacked vertically, each with a thin arrow feeding into Tachyon FRM:
    - Tachyon Switch (Transaction Processing Engine) → transaction events, switch decisions
    - ACS (3DS 2.2) → AReq, CReq, CRes (mark with "RT" badge, dashed correlation arrow connecting to Tachyon Switch)
    - Customer Lifecycle Management → demographic changes
    - Card Management System → card issuance/re-issuance/replacement
    - Tachyon Credit → repayments, credit-limit updates
    - Notification Center → two-way notification response inputs
    - Token Management System → token creation, status updates
  - Center box: Tachyon FRM (largest box, labeled "Decisioning · Case Management · Orchestration")
  - Right column (Rule Engines) — two boxes fed by Tachyon FRM:
    - Featurespace (labeled "Pre-integrated")
    - Additional Risk Rule Engine (labeled "Extensible — current capability")
  - Return arrow from rule engines back to Tachyon FRM labeled "Action tags"
  - Right edge: Tachyon Action Execution box receiving the final output
  - Ownership boundary lines: dashed vertical lines separating "Tachyon Platform" / "FRM Layer" / "USB Operations" — labeled at top
- *Bottom-left callout box (3DS integration):*
  - "Full native ACS support · EMV Co 3DS 2.2 · Authentication events correlated to transaction in a single RT pass"
- *Bottom-right callout box (Performance):*
  - Bold: **< 200ms** RT risk rule execution (incl. Featurespace round-trip)
  - Bold: **30,000 TPS** routinely load-tested
  - Small text: "Throughput ceiling is infrastructure-bound, not architecture-bound."

**Build notes**
- The ownership boundaries are what the buyer's architects will scrutinize — label them explicitly.
- The callout boxes for 3DS and performance keep high-value points visible without cluttering the diagram.

---

## Slide 4 - Exhaustive Entities, States, and Events (RT/NRT)

**Slide goal**
- Provide a complete inventory of data domains fed to FRM for decisioning.

**Why this matters**
- The more signal the rule engine sees at decision time, the more precise the decision. Unified RT correlation of transaction and 3DS authentication events reduces the gap between "suspicious" and "confirmed fraud" — directly lowering false positives.

**What to include**
- Entity inventory:
  - Account Holder (including segments, addresses)
  - Account
  - Card Holder Profile
  - Card
  - Token
- Event inventory:
  - Transaction events (RT): auth, pre-auth, incremental auth, clearing messages, transaction reversal, repayment, repayment reversal, card PIN reset, card PIN changed, credit limit updated
  - Authentication events (RT, correlated to transaction): AReq, CReq, CRes (EMV Co 3DS 2.2 from ACS)
  - Transaction decision (from Tachyon Switch) — NRT
  - Review decision — NRT
  - Cardholder feedback — NRT
  - CRUD changes to entities — NRT
  - Customer custom events — NRT
- Processing split:
  - Transaction events and 3DS authentication events are RT; authentication events are correlated to the originating transaction so the rule engine receives both signals in a single decisioning pass.
  - All non-transaction events update rule-engine state and can trigger NRT rules/NRT decisions.
  - Customer custom events can be streamed to Tachyon FRM and to rule engines.

**Infographic type:** Color-coded matrix table with a processing-split visual

**Slide layout**
- *Left half (55%):* Source-to-event matrix table:
  - Columns: Source System | Entity | Event Type | RT / NRT
  - Rows grouped by entity:
    - Account Holder (segments, addresses) — CRUD changes — NRT
    - Account — CRUD changes — NRT
    - Card Holder Profile — CRUD changes — NRT
    - Card — CRUD changes — NRT
    - Token — CRUD changes — NRT
  - Transaction events row (highlighted for RT): auth, pre-auth, incremental auth, clearing messages, transaction reversal, repayment, repayment reversal, card PIN reset, card PIN changed, credit limit updated — all RT
  - Authentication events row (highlighted for RT): AReq, CReq, CRes (EMV Co 3DS 2.2 from ACS) — RT, correlated to transaction
  - Other event rows (subdued for NRT): transaction decision (from Switch), review decision, cardholder feedback, customer custom events — all NRT
- *Right half (45%):* Two-zone processing-split visual:
  - Top zone (RT — highlighted): Transaction events + 3DS authentication events → single decisioning pass → action recommendation. Callout: "Authentication events are correlated to the originating transaction — both signals in one pass."
  - Bottom zone (NRT — subdued): All other events → rule-engine state update → can trigger NRT rules/decisions. Note: "Custom events can be streamed to Tachyon FRM and rule engines."

**Build notes**
- Use color coding: green/blue for RT rows, gray for NRT rows.
- Add examples for one card event, one token event, one authentication event, and one customer custom event.
- The two-zone processing visual makes the RT/NRT split visually immediate rather than buried in a list.

---

## Slide 5 - FRM Decision Model and Action Recommendations

**Slide goal**
- Show the full range of decisions FRM can make and the complete recommendation taxonomy.

**Why this matters**
- A rich, entity-specific action catalog means the system can respond proportionally — temporary block instead of permanent closure, notification instead of decline — preserving cardholder relationships while still containing fraud.

**What to include**
- Decision trigger model: how risk scores and rule triggers translate into specific action recommendations.
- Complete action recommendation catalog (canonical list — shown once here, referenced by all later slides):
  - Transaction:
    - Decline
  - Card:
    - Temp Block (time-bound)
    - Temp Block Card and All Tokens
    - Block and Replace
    - Block-Replace-Disable-Tokens
    - Block Card and All Tokens
  - Token:
    - Temp Block
    - Block
  - Cardholder:
    - Notify
    - Notify-for-Feedback
- Applicability matrix: which recommendations are available in RT, NRT, and case workflows.
- Mapping from rule-engine recommendation tags to Tachyon FRM action types.
- Decision proportionality: how the system selects the right-sized response (temporary block vs permanent closure, notification vs decline).

**Infographic type:** Canonical action catalog table + mini decision-flow diagrams

**Slide layout**
- *Top banner:* "Canonical Action Recommendation Catalog" — with a note: "Shown once here, referenced by all later slides"
- *Main area (65%):* Single table — the action catalog:
  - Columns: Entity | Action Recommendation | RT | NRT | Case
  - Rows grouped by entity with colored left borders (one color per entity type):
    - Transaction: Decline
    - Card: Temp Block (time-bound), Temp Block Card and All Tokens, Block and Replace, Block-Replace-Disable-Tokens, Block Card and All Tokens
    - Token: Temp Block, Block
    - Cardholder: Notify, Notify-for-Feedback
  - Each row has checkmarks for RT / NRT / Case availability
- *Right side (35%):* Two mini decision-flow strips stacked vertically:
  - Strip 1 (RT walkthrough): Transaction → risk score/rule trigger → Decline recommendation → action executed. Label: "RT example"
  - Strip 2 (NRT walkthrough): Pattern detected → rule trigger → Temp Block recommendation → action executed. Label: "NRT example"
- *Below table:* One line: "Decision proportionality: the system selects the right-sized response — temporary block instead of permanent closure, notification instead of decline."
- *Bottom-right small note:* "Case-specific financial actions (provisional credits, transaction reversals) → Slide 7"

**Build notes**
- The table is the definitive artifact this slide exists to establish.
- The mini flows give two concrete walkthroughs without crowding the table.
- The cross-reference to Slide 7 sets up the next pair of slides cleanly.

---

## Slide 6 - Case Management Capabilities

**Slide goal**
- Demonstrate end-to-end investigation and case workflow capabilities.

**Why this matters**
- BPMN-driven workflows with task- and case-level SLA tracking give your fraud operations team the ability to manage dispute volumes at scale while demonstrating Reg E/Z timeline compliance to examiners.

**What to include**
- Demo link callout: Disputes Workbench in Operations Center.
- Case creation triggers (rule alerts, risk thresholds, pattern detections).
- Workflow states (new, triage, investigate, actioned, closed).
- Alert review to dispute-case creation and case resolution flow.
- Workflow authoring via BPMN for alert-specific/custom case workflows.
- Cardholder input capture in case resolution.
- Full integration with card-scheme dispute approaches.
- Queueing/routing, SLA tracking (task-level and case-level), audit trail, evidence attachments.
- Sophisticated dispute/case actions: all fraud-control actions from Slide 5, plus case-only financial commands (provisional credits, transaction reversals) detailed in Slide 7.
- Integration options with CMS, transaction systems, reporting.

**Infographic type:** Horizontal swimlane workflow diagram

**Slide layout**
- *Top-left:* Demo badge — "Demo: Disputes Workbench in Operations Center" (clickable link or QR code for live demo)
- *Main area (75%):* Four-lane horizontal swimlane diagram:
  - Lane 1 — System: case creation triggers (rule alerts, risk thresholds, pattern detections) → automatic case creation
  - Lane 2 — Fraud Analyst: alert review → dispute-case creation → investigation → cardholder input capture → resolution actions
  - Lane 3 — Supervisor: BPMN workflow authoring, SLA monitoring (task-level + case-level), approval gates
  - Lane 4 — Downstream Platform: CMS integration, transaction system updates, scheme dispute flow, reporting feed
  - Workflow states labeled along the timeline axis: New → Triage → Investigate → Actioned → Closed
  - At the "Actioned" stage: callout listing available actions — "Fraud-control actions from Slide 5, plus case-only financial commands (provisional credits, transaction reversals) → Slide 7"
- *Right sidebar (25%):* Stacked capability badges (small rounded rectangles):
  - BPMN custom workflows
  - Cardholder input in case resolution
  - Card-scheme dispute integration (end-to-end)
  - Task + case SLA tracking
  - Audit trail + evidence attachments
  - Queueing/routing
- *Bottom note:* "Slide 6 = case workflow (create, triage, investigate, resolve). Slide 7 = case command catalog + execution governance."

**Build notes**
- Include one BPMN snippet and one SLA dashboard example.
- The sidebar badges ensure no capability is lost from the outline while keeping the diagram uncluttered.
- Swimlanes are the standard visual for operational workflows in enterprise presentations.

---

## Slide 7 - Case Commands: Block, Re-Issuance, and Financial Actions

**Slide goal**
- Show the complete set of commands available within case workflows, including card/token controls and financial actions.

**Why this matters**
- Case workflows can be configured with execution controls (auto-execute, approval gates, maker/checker, escalation) as required by your operating model — reducing operational risk while maintaining response speed during compromise events.

**What to include**
- Case-specific command catalog (extends Slide 5 recommendations with case-only actions):
  - All fraud-control actions from Slide 5 are available within case workflows.
  - Additional case-only financial commands:
    - provisional credits
    - transaction reversals
- Execution controls (all configurable in workflows as required by the customer):
  - auto-executable vs approval-gated command designation
  - maker/checker controls for high-impact commands
  - escalation triggers within workflows
  - full auditability: command execution log, override tracking, evidence linkage to case
- Compromise and re-issuance flow (example):
  - detection -> block -> case -> review -> re-issue -> downstream updates (Card Management System, Token Management System notifications).
- BIN attack handling with merchant blocklisting example.

**Infographic type:** Two-part slide — command catalog table (top) + sequence diagram (bottom)

**Slide layout**
- *Top half — Command catalog table:*
  - Columns: Command | Entity | Source | Auto/Manual | Approval Required | Maker/Checker | SLA
  - Row group 1 — Fraud-control actions (from Slide 5): all 10 actions listed with a note: "Available in case workflows"
  - Row group 2 — Case-only financial commands (highlighted):
    - Provisional credits
    - Transaction reversals
  - Each row shows execution control configuration as checkmark/configurable indicators
  - Column header note: "All execution controls are configurable in workflows per customer requirements"
- *Bottom half — Sequence diagram (compromise-to-reissue flow):*
  - Detection → Block (card + tokens) → Case creation → Agent review → Re-issue decision → Card Management System (new card) → Token Management System (token updates) → Downstream notifications
  - Label each step with the responsible actor (System / Analyst / Supervisor / Platform)
  - Inset callout: BIN attack variant — "Detection → merchant identification → blocklisting"
- *Right edge — Execution governance callout (vertical strip):*
  - Auto-executable vs approval-gated
  - Maker/checker for high-impact commands
  - Escalation triggers
  - Full auditability: execution log, override tracking, evidence linkage

**Build notes**
- The table establishes the complete command set (including how it extends Slide 5).
- The sequence diagram gives a concrete operational flow the buyer can walk through mentally.
- The governance strip on the right reinforces that everything is configurable.

---

## Slide 8 - Notification Capabilities

**Slide goal**
- Show who is notified, through what channels, and based on which policies.
- Summary headline: 6 channels, BYO provider support, closed-loop feedback.

**Why this matters**
- Multi-channel notification with feedback-form responses creates a closed loop: the cardholder confirms or denies fraud in real time, which feeds directly into case resolution — reducing time-to-resolution and agent workload.

**What to include**
- Recipient options: cardholder, program admin, fraud ops, combinations.
- Out-of-box channel coverage:
  - SMS
  - Email
  - Mobile push (iOS, Android)
  - Browser push (Chrome, Edge)
  - Webhooks (outbound)
  - Telephony (outbound voice calls)
- Bring-your-own channel providers/relationships support.
- Multiple provider support for load distribution, resiliency, and cost-based routing.
- Routing model:
  - static rule policies based on recipient address/endpoint
  - notification policies by sensitivity category.
- Recipient preference handling via API endpoints.
- Multi-cast support: one message to multiple recipients across multiple channels.
- Read receipt tracking by channel and response workflows.
- Feedback forms in notifications where channel supports it (embedded/deep-link as applicable).
- Telephony retries/escalation to alternate channels where configured.
- Notification outcomes can feed case/rule workflows through configured response handling.
- Incident portal monitoring and follow-up workflow hooks.

**Infographic type:** Channel capability matrix + closed-loop flow diagrams

**Slide layout**
- *Top banner:* Headline — "6 Channels · BYO Provider Support · Closed-Loop Feedback"
- *Left half (55%) — Channel capability matrix:*
  - Columns: Channel | Direction | BYO Provider | Read Receipt | Feedback Form | Retry/Escalation
  - Rows:
    - SMS — outbound — yes — yes — embedded/deep-link — to alternate channel
    - Email — outbound — yes — yes — embedded — to alternate channel
    - Mobile push (iOS, Android) — outbound — yes — yes — deep-link — to alternate channel
    - Browser push (Chrome, Edge) — outbound — yes — channel-specific — channel-specific — to alternate channel
    - Webhooks — outbound only — yes — n/a — n/a — n/a
    - Telephony (voice calls) — outbound — yes — n/a — n/a — retry + escalate
- *Right half (45%) — Two mini flow diagrams stacked:*
  - Flow 1 — High-risk confirmation: Fraud detected → notification policy (sensitivity category) → channel selection (static rules by recipient address/endpoint) → multi-cast to cardholder + program admin → read receipt tracked → response feeds case workflow
  - Flow 2 — Feedback-form response: Notification with feedback form → cardholder responds (confirm/deny) → response enters Tachyon FRM → case/rule workflow transition triggered
- *Below matrix — Additional capabilities as compact icon+label strip:*
  - Multiple provider support (load distribution, resiliency, cost-based routing)
  - Recipient preferences via API
  - Multi-cast: one message → multiple recipients × multiple channels
  - Notification policies by sensitivity category
  - Incident portal monitoring + follow-up workflow hooks

**Build notes**
- The matrix gives the exhaustive channel inventory.
- The two flows demonstrate the closed-loop model — the differentiator on this slide.
- The icon strip captures remaining features without adding rows to the already-dense matrix.
- Keep notification SLA metrics out of this slide; keep focus on capability and control.

---

## Slide 9 - User-Managed Risk and Self-Serve Operations

**Slide goal**
- Clarify what USB can control directly vs what is platform-managed.

**Why this matters**
- Giving commercial cardholders governed self-serve controls (within corporate guardrails) reduces the volume of false-positive declines that generate support calls, while the `suppressible` tag model ensures product-level controls are never bypassed.

**What to include**
- Cardholder-managed risk model for commercial cards:
  - cardholders can restrict transactions using rule grammar
  - cardholders can specify temporary overrides to allow transactions
  - cardholders can suppress selected risk rules and respond to fraud alerts
- Commercial-card policy relevance:
  - controls can be scoped by merchant IDs/terminals, business hours, and IP-address restrictions
  - corporate issuer defines these policy boundaries
- Guardrail model:
  - user restrictions never override product-specified controls
  - only risk rules tagged `suppressible` are eligible for cardholder suppression
  - suppressibility is governed per rule by the `suppressible` tag
- Governance and control plane:
  - Operations Center manages policy boundaries, approvals, traceability, and override auditability.

**Infographic type:** Concentric guardrail model (layered rings) + persona-control matrix

**Slide layout**
- *Left half (50%) — Concentric ring diagram (3 rings, inside-out):*
  - Inner ring (darkest): Product-specified controls — "Never overridden by cardholder or corporate policy"
  - Middle ring: Corporate issuer policy boundaries — "Scoped by merchant ID/terminal, business hours, IP address. Defined by the corporate issuer."
  - Outer ring (lightest): Cardholder-managed controls — "Restrict transactions (rule grammar), temporary overrides, suppress eligible rules (`suppressible=true`), respond to fraud alerts"
  - Annotation arrow from outer to inner with a "blocked" icon: "User restrictions never override product-specified controls"
  - Tag callout on outer ring: "`suppressible` tag governs which rules are eligible for cardholder suppression"
- *Right half (50%) — Persona-control matrix table:*
  - Columns: Control | Cardholder | Program Admin | Operations Center
  - Rows:
    - Restrict transactions by rule grammar — yes — yes — governance
    - Temporary override to allow transactions — yes — yes — governance
    - Suppress eligible risk rules — yes (if `suppressible=true`) — yes — governance + audit
    - Respond to fraud alerts — yes — yes — monitoring
    - Set policy boundaries (merchant, hours, IP) — no — yes — governance
    - Override auditability — n/a — n/a — full trail
- *Below diagram — Two example callouts side by side:*
  - Example A (green): Rule tagged `suppressible=true` — cardholder suppresses after false-positive decline → reattempt succeeds
  - Example B (red): Rule not tagged `suppressible` — suppression attempt blocked by system

**Build notes**
- The concentric model communicates the guardrail hierarchy intuitively — inner layers can't be overridden by outer layers.
- Keep terminology explicit: cardholder-managed controls within issuer/corporate guardrails.

---

## Slide 10 - Extensibility and Configurability

**Slide goal**
- Demonstrate how the bank can tailor FRM behavior without core rewrites.

**Why this matters**
- Configuration changes (thresholds, routing, policies) take effect without platform releases or vendor dependency — your fraud team can adapt to emerging fraud patterns at the speed of the threat, not the speed of a release cycle.

**What to include**
- Configurability scope:
  - configurable thresholds, action mapping, routing logic, and tenant-level policy separation
  - workflow and policy behavior tuning without core platform rewrites
- Extensibility posture:
  - pre-integrated Featurespace with ability to integrate other risk engines/providers
  - integration boundaries and contract points (schemas, APIs, events)
  - support for customer custom events and custom entities
  - support for custom actions for use in workflows

**Infographic type:** Three-column classification table + one end-to-end example flow

**Slide layout**
- *Main area (70%) — Three-column table:*
  - Column 1 — Configurable (no code change) [green]:
    - Thresholds
    - Action mapping
    - Routing logic
    - Tenant-level policy separation
    - Workflow and policy behavior tuning
  - Column 2 — Extensible (platform-supported extension points) [blue]:
    - Additional risk engines/providers (beyond Featurespace)
    - Custom events streamed to FRM and rule engines
    - Custom entities
    - Custom actions for use in workflows
  - Column 3 — Integration-required (external coordination) [orange]:
    - Integration boundaries and contract points (schemas, APIs, events)
    - Third-party rule engine setup (customer works with that provider)
- *Bottom area (30%) — One end-to-end customization example:*
  - Horizontal flow: e.g., "New merchant-category fraud pattern detected → fraud team adjusts threshold [configurable] → adds custom event for new data signal [extensible] → connects to third-party enrichment API [integration-required]"
  - Each step color-coded to match the table column

**Build notes**
- The three-column classification is what a buyer's implementation team needs to assess effort and ownership.
- The color-coded example ties the classification back to a real operational scenario.

---

## Slide 11 - Reporting and Analytics

**Slide goal**
- Show how fraud data flows to analytics and what reporting capabilities are available out-of-box and via self-serve.

**Why this matters**
- Self-serve BI on a tenant-isolated data mart means your fraud leadership can measure rule effectiveness, agent performance, and loss trends without waiting for vendor-built reports — and the same data mart feeds your own BI tools.

**What to include**
- Data foundation:
  - All fraud evaluation data (decisioning, scoring, event data) and case data are exported to a managed data lake.
  - Real-time events are available for streaming consumption.
  - A well-structured data mart is refreshed daily for analytical use.
  - Data lake is fully tenant-isolated in storage, serving, and processing.
  - Data retention and purge policies are custom and configurable per tenant.
- Two analytics surfaces:
  - Featurespace portal: out-of-box rule performance analytics, model score distributions, detection-rate metrics.
  - Tachyon FRM (Apache Superset): SLA adherence, agent performance, case lifecycle metrics, and self-serve custom analytics.
- Self-serve BI:
  - Bank teams build, schedule, and distribute their own reports and dashboards using Superset.
  - Data mart is accessible to the bank's own BI tools (Tableau, Power BI, Looker, etc.).
- Scheme reporting:
  - All card-scheme reporting is handled by Tachyon FRM and/or Tachyon Switch.
- Common report catalog:
  - Operational: daily fraud summary, alert-to-case conversion, case aging/backlog, agent workload/throughput, SLA compliance (Reg E/Z timelines, scheme deadlines).
  - Risk and rule performance: rule hit-rate analysis, model score distributions, fraud trend analysis (by MCC, merchant, geography, CP/CNP, time), decline rate by rule/threshold, cardholder impact.
  - Financial: fraud loss summary (gross/recovered/net), provisional credit outstanding, chargeback/representment status, write-off tracking.
  - Cardholder experience: notification delivery and response rates, cardholder feedback analysis, rule suppression activity and outcomes, customer contact rate.

**Infographic type:** Two-panel layout — data architecture flow (left) + report catalog grid (right)

**Slide layout**
- *Left panel (45%) — Data architecture flow diagram (top-to-bottom):*
  - Top: All fraud evaluation data + case data
  - Arrow down to: Managed data lake (badge: "tenant-isolated in storage, serving, processing")
  - Fork into two paths:
    - Path 1: Real-time events → streaming consumption
    - Path 2: Daily refresh → structured data mart
  - From data mart, three output arrows:
    - Arrow 1 → Featurespace portal: "Rule performance analytics, model scores, detection rates" (label: "separate interface")
    - Arrow 2 → Apache Superset: "SLA adherence, agent performance, case lifecycle, custom analytics" (label: "self-serve BI")
    - Arrow 3 → Bank's own BI tools: "Tableau, Power BI, Looker, etc." (label: "data mart accessible")
  - Bottom note on data mart: "Retention and purge policies are custom and configurable per tenant"
  - Scheme reporting callout: "All card-scheme reporting handled by Tachyon FRM and/or Tachyon Switch"
- *Right panel (55%) — Report catalog as a 2x2 grid of themed boxes:*
  - Box 1 — Operational: daily fraud summary, alert-to-case conversion, case aging/backlog, agent workload/throughput, SLA compliance (Reg E/Z timelines, scheme deadlines)
  - Box 2 — Risk & Rule Performance: rule hit-rate analysis, model score distributions, fraud trend analysis (MCC, merchant, geography, CP/CNP, time), decline rate by rule/threshold, cardholder impact
  - Box 3 — Financial: fraud loss summary (gross/recovered/net), provisional credit outstanding, chargeback/representment status, write-off tracking
  - Box 4 — Cardholder Experience: notification delivery/response rates, cardholder feedback analysis, rule suppression activity/outcomes, customer contact rate
- *Between panels — Honest framing note:* "Rule performance analytics are accessed through Featurespace's native portal; all other analytics are unified in Superset."

**Build notes**
- Present the two interfaces honestly as a current-state architecture decision, not as a design feature.
- Include one example dashboard screenshot or wireframe per analytics surface.
- Call out self-serve positioning: bank builds its own reports.

---

## Slide 12 - Rule Engine Setup: Model Management, Supervision, Tenancy

**Slide goal**
- Explain rule/model lifecycle and operating environment design.

**Why this matters**
- Full tenant isolation with dedicated Featurespace tenancy means your models, rules, and policies are never co-mingled with other tenants — a prerequisite for model risk management under SR 11-7 and for examiner confidence.

**What to include**
- Tenancy and isolation anchor:
  - Tachyon FRM is fully isolated by tenant.
  - workflows, actions, rules, and policies are all tenant-localized.
- Featurespace operating model:
  - dedicated tenant for the customer
  - Featurespace provides the default model
  - customer can bring own Featurespace relationship
  - customer can bring own model
  - Zeta can build models or help customer build models
  - Zeta supports rule authoring and model management for Featurespace.
- Other risk engines:
  - customer works with the selected provider for rules/models.
  - Tachyon FRM handles orchestration/integration across engines/providers.
- Operating model handoff:
  - transaction alert monitoring and case resolution are expected to be tenant-handled.
  - Zeta can provide outsourced transaction operations services when requested.

**Infographic type:** Two-layer stacked diagram + responsibility split table

**Slide layout**
- *Top layer (40%) — Tenancy and isolation visual:*
  - A horizontal bar labeled "Tachyon FRM" containing three isolated tenant compartments side by side, each showing: Workflows | Actions | Rules | Policies
  - One compartment is highlighted and labeled "USB Tenant — fully isolated"
  - Caption: "Workflows, actions, rules, and policies are all tenant-localized"
- *Bottom layer (60%) — Responsibility split table:*
  - Columns: Capability | Tenant (USB) | Zeta | Engine Provider (Featurespace / Other)
  - Rows:
    - Default model → — | — | Featurespace provides
    - Bring own model → USB | — | deploys in Featurespace
    - Bring own FS relationship → USB manages | Zeta integrates | Featurespace delivers
    - Zeta builds/helps build model → USB approves | Zeta builds | Featurespace hosts
    - Rule authoring + management (FS) → — | Zeta supports | Featurespace tooling
    - Other risk engine rules/models → USB | — | Provider delivers
    - Orchestration across engines → — | Tachyon FRM | —
    - Alert monitoring + case resolution → USB (default) | Zeta (optional BPO) | —

**Build notes**
- The stacked layers separate the two concepts (isolation architecture vs. operating responsibilities) cleanly.
- The responsibility table is the artifact the buyer's procurement and risk teams will reference during evaluation.

---

## Slide 13 - Operational Contracts with the Bank

**Slide goal**
- Define Zeta's role and the issuer's responsibilities with concrete accountability splits.

**Why this matters**
- Zeta's default role is technology provider — platform availability, not fraud outcomes. This gives you full control over your rules, models, and operations, with the option to engage Zeta for transaction monitoring and operations as BPO services if needed.

**What to include**
- Zeta's role as technology provider (default):
  - Platform availability and uptime: Zeta.
  - Notification delivery: Zeta + BYO provider (shared responsibility).
  - Rule authoring and tuning: issuer or their partners.
  - Model updates and deployment: issuer or their partners.
  - Transaction alert monitoring: issuer or their partners.
  - Case resolution and dispute handling: issuer or their partners.
  - Emergency controls (e.g., BIN blocks, throttling): issuer or their transaction monitoring partner.
  - Fraud rule/model efficacy and fraud outcomes: issuer or their partners.
- Key positioning: as technology provider, Zeta does not represent the efficacy of fraud rules, models, or fraud outcomes. Zeta provides the platform; the issuer and their partners own decisioning and operational outcomes.
- Two distinct service categories:
  - Model and rule management services — always issuer or their partners.
  - Transaction monitoring and operations services — issuer or their partners by default; Zeta can provide these as BPO services.
- Optional BPO engagement:
  - Zeta can provide transaction monitoring and operations as BPO services.
  - When enrolled, Zeta is responsible for SLAs corresponding to those specific services.
  - Model and rule management remain with the issuer or their partners even when BPO is engaged.
- Audit and compliance evidence:
  - Self-serve from Zeta Trust Center (website).
  - Regulatory accountability follows the role structure: the bank is always accountable to the regulator, with Zeta as technology provider or BPO service provider as applicable.

**Infographic type:** Two-column comparison view + responsibility matrix

**Slide layout**
- *Top banner:* Key positioning statement in a highlighted box: "As technology provider, Zeta does not represent the efficacy of fraud rules, models, or fraud outcomes. Zeta provides the platform; the issuer and their partners own decisioning and operational outcomes."
- *Main area — Two-column comparison (side by side):*
  - Left column — "Technology Provider (Default)":
    - Zeta: platform availability + uptime, notification delivery (shared with BYO provider)
    - Issuer or their partners: rule authoring/tuning, model updates/deployment, transaction alert monitoring, case resolution/dispute handling, emergency controls (BIN blocks, throttling), fraud outcomes
  - Right column — "With BPO Services (Optional)":
    - Shifts to Zeta: transaction monitoring + operations (with corresponding SLAs)
    - Stays with issuer: model and rule management (always), fraud outcomes accountability
    - New: Zeta responsible for SLAs on enrolled BPO services
  - Visual: items that shift are connected by arrows between columns
- *Below comparison — Two callout boxes side by side:*
  - Box 1 — Service categories:
    - Model and rule management services → always issuer or their partners
    - Transaction monitoring and operations → default: issuer; optional: Zeta BPO
  - Box 2 — Audit and compliance:
    - Self-serve from Zeta Trust Center
    - Regulatory accountability follows the role structure: bank is always accountable to the regulator

**Build notes**
- The two-column comparison answers "what changes if we engage BPO?" — the single most likely question on this slide.
- The shift arrows make the delta visual.
- Keep SLA/OLA term specifics out — but state that BPO SLAs apply when enrolled.

---

## Slide 14 - FRM-Specific Compliance Posture

**Slide goal**
- Demonstrate that Tachyon FRM meets all regulatory and compliance obligations specific to fraud risk management for a US commercial card program.

**Why this matters**
- Every regulatory obligation (Reg E/Z timelines, PCI DSS, scheme rules, SOX controls) maps to a specific platform enforcement mechanism already shown in earlier slides — compliance is built into the workflow, not bolted on afterward.

**What to include**
- Positioning: general platform security, privacy, DR/BCP, and related compliance are covered in the platform suite deck. This slide focuses on obligations directly exercised or enforced by the FRM layer.
- Regulatory compliance:
  - Reg E / EFTA: dispute investigation timelines (10 business days / 45 calendar days), provisional credit obligations, error-resolution notice requirements — enforced through case management SLAs and workflow automation.
  - Reg Z / TILA: credit card billing dispute requirements (60-day filing window, 2-billing-cycle resolution, credit-while-investigating rules) — directly relevant for commercial credit card programs.
  - BSA/AML (SAR filing support): FRM case data and investigation evidence as inputs to SAR filing workflows.
  - UDAAP: fraud-control actions (declines, blocks, notification policies) do not create unfair or deceptive consumer outcomes; relevant to cardholder-managed controls and suppression logic.
  - GLBA / Reg P: financial privacy in fraud data sharing, notification content, and analytics access.
  - CCPA / CPRA: state privacy obligations for cardholder data in fraud investigation records, data retention, and right-to-know/right-to-delete implications on case archives.
- Card network compliance:
  - Visa / Mastercard Operating Regulations: chargeback lifecycle compliance, reason-code handling, representment timelines, pre-arbitration/arbitration flows.
  - Scheme dispute integration is end-to-end (as demonstrated in Slide 6).
- Security and controls attestations:
  - PCI DSS: card data handling within FRM decisioning, case management, and notification flows — tokenization of PAN in analytics/reporting, access controls on case data, audit logging.
  - SOC 2 Type II: controls attestation covering security, availability, and processing integrity of the FRM layer.
  - ISO 27001: information security management certification for FRM and case management.
- Model and financial controls governance:
  - FFIEC guidance and SR 11-7 / OCC 2011-12: model risk management for Featurespace model lifecycle (directly relevant to Slide 12).
  - SOX: internal controls over financial reporting — provisional credits and transaction reversals in case management constitute financial transactions with SOX implications.

**Infographic type:** Grouped compliance matrix table with slide cross-references

**Slide layout**
- *Top note (small, italic):* "General platform security, privacy, DR/BCP, and related compliance are covered in the platform suite deck. This slide focuses on obligations directly exercised or enforced by the FRM layer."
- *Main area — Compliance matrix table with four row groups:*
  - Columns: Obligation | FRM Capability | Enforcement Mechanism | Slide Cross-Ref
  - Group 1 — Regulatory (blue left border):
    - Reg E / EFTA → dispute timelines, provisional credits, error-resolution notices → case management SLAs + workflow automation → Slide 6
    - Reg Z / TILA → 60-day filing, 2-billing-cycle resolution → case workflows → Slide 6
    - BSA/AML → SAR filing support → case data + investigation evidence → Slide 6
    - UDAAP → fair outcomes in fraud actions → cardholder-managed controls + suppression logic → Slide 9
    - GLBA / Reg P → financial privacy → fraud data sharing, notification content, analytics access → Slides 8, 11
    - CCPA / CPRA → state privacy → investigation records, data retention, right-to-know/delete → Slide 11
  - Group 2 — Card Network (green left border):
    - Visa / Mastercard Operating Regulations → chargeback lifecycle, reason codes, representment, pre-arb/arb → end-to-end scheme dispute integration → Slide 6
  - Group 3 — Security & Attestations (orange left border):
    - PCI DSS → card data handling → tokenization of PAN in analytics, access controls, audit logging → Slides 5, 6, 11
    - SOC 2 Type II → controls attestation → security, availability, processing integrity → platform-wide
    - ISO 27001 → ISMS certification → FRM and case management → platform-wide
  - Group 4 — Model & Financial Governance (purple left border):
    - FFIEC / SR 11-7 / OCC 2011-12 → model risk management → Featurespace model lifecycle → Slide 12
    - SOX → internal controls over financial reporting → provisional credits + transaction reversals → Slide 7

**Build notes**
- The slide cross-references turn the matrix into a live navigation tool — the presenter can click through to demonstrate each enforcement mechanism.
- Color-coded group borders provide visual scanning across the four compliance categories.

---

## Slide 15 - Deep-Dive Demo Scenarios

**Slide goal**
- Prove capability through scenario-led narratives that map to bank concerns.

**Why this matters**
- These scenarios prove that the system handles the two most operationally disruptive fraud events — a false-positive decline and a card compromise — end-to-end, with the cardholder back to normal operations in minutes, not days.

**What to include**
- Scenario 1: Transaction decline due to risk rule -> customer feedback to suppress rule -> transaction reattempt -> success.
  - Show decline reason and linked rule trigger.
  - Show customer feedback flow and suppression action on eligible rule (`suppressible=true`).
  - Show reattempt decision path and successful authorization outcome.
- Scenario 2: Card block triggered from transaction rule.
  - Show transaction-rule trigger -> card block command execution.
  - Show downstream effect on card usage and related controls.
- Explicit RT/NRT touchpoints for both scenarios.

**Infographic type:** Two horizontal swimlane timelines (stacked)

**Slide layout**
- *Top half — Scenario 1 swimlane: "False-Positive Decline → Cardholder Recovery":*
  - Lanes: System | Cardholder | Rule Engine
  - Steps along timeline:
    1. Transaction submitted (RT)
    2. Risk rule triggers decline → show decline reason + linked rule trigger
    3. Cardholder receives notification (NRT)
    4. Cardholder provides feedback → suppresses rule (only if `suppressible=true` — highlighted guardrail callout)
    5. Transaction reattempted (RT)
    6. Rule suppressed → authorization succeeds
  - End callout: Business impact — "Cardholder back to normal operations in minutes, not days"
- *Bottom half — Scenario 2 swimlane: "Card Compromise → Block":*
  - Lanes: System | Fraud Analyst | Card Management
  - Steps along timeline:
    1. Transaction triggers risk rule (RT)
    2. Card block command executed
    3. Downstream effect: card usage blocked, token controls applied
    4. Case created for analyst review (NRT)
  - End callout: Control takeaway — "Atomic block across card and associated tokens in a single command"

**Build notes**
- Each step has a small RT/NRT badge. Timestamps on the timeline axis. Decision-point diamonds at key steps.
- For Scenario 1, highlight policy guardrails: only suppressible rules can be user-suppressed.
- Swimlanes with timestamps give the presenter a script to follow during the live demo.

---

## Slide 16 - Why Tachyon FRM for USB Commercial Cards

**Slide goal**
- Anchor conviction. The audience should leave this slide thinking "this was built for our problem."

**Why this matters**
- Tachyon FRM is built for the complexity of commercial card programs — governed cardholder controls, proportional actions, and full operational flexibility, all production-ready today.

**What to include**
- Commercial-card-specific differentiators (top tier — no other FRM does this the same way):
  - Cardholder-managed risk controls with `suppressible` guardrails — employees unblock themselves within corporate policy.
  - Corporate-issuer policy boundaries — controls scoped by merchant ID, terminal, business hours, IP address.
  - Unified RT decisioning with 3DS authentication — transaction and AReq/CReq/CRes correlated in a single pass, not reconstructed post-authorization.
  - Unified card + token command model — atomic actions across card and all associated tokens in a single command, reflecting token-first architecture.
  - Token-level independent controls — act on a specific token without affecting the card.
- Architecture-level differentiators (stronger than typical):
  - Under 200ms end-to-end including Featurespace round-trip.
  - End-to-end scheme dispute integration with financial action execution — FRM and dispute lifecycle in one platform, including provisional credits and reversals.
  - Notify-for-Feedback as a native closed-loop action — cardholder response feeds directly into case and rule workflows.
- Footer positioning line: "All capabilities are production-ready, tenant-isolated, and configurable per your operating model."

**Infographic type:** Two-tier differentiator layout with icons

**Slide layout**
- *Top tier (60% of slide) — "Commercial-Card-Specific" label with a distinctive accent bar:*
  - Five items in a single row, each as an icon + one-line description card:
    1. Cardholder-managed risk controls with `suppressible` guardrails — employees unblock themselves within corporate policy
    2. Corporate-issuer policy boundaries — controls scoped by merchant ID, terminal, business hours, IP
    3. Unified RT decisioning with 3DS — transaction and AReq/CReq/CRes correlated in a single pass
    4. Unified card + token command model — atomic actions across card and all tokens in one command
    5. Token-level independent controls — act on a specific token without affecting the card
- *Bottom tier (30%) — "Architecture-Level" label with a secondary accent bar:*
  - Three items in a single row:
    1. Under 200ms end-to-end including Featurespace round-trip
    2. End-to-end scheme dispute integration with financial action execution — FRM and dispute lifecycle in one platform
    3. Notify-for-Feedback as a native closed-loop action — cardholder response feeds case and rule workflows
- *Bottom edge — Footer positioning line (full width, distinctive styling):*
  - "All capabilities are production-ready, tenant-isolated, and configurable per your operating model."

**Build notes**
- Keep descriptions to one line each — the detail has already been presented in the preceding slides.
- Use icons or visual markers to distinguish the two tiers.
- The presenter can dwell here if the room needs more convincing, or move quickly to Slide 17 if conviction is established.

---

## Slide 17 - Next Steps

**Slide goal**
- Advance the deal. The audience should leave knowing exactly what is being asked of them.

**Why this matters**
- Three clear decisions determine the shape, scope, and timeline of the implementation.

**What to include**
1. **Operating model decision**: confirm whether USB will operate transaction alert monitoring and case resolution in-house, or engage Zeta's outsourced operations services — this determines the implementation shape.
2. **Integration assessment**: share USB's current auth flow, notification provider landscape, and BI tool stack so Zeta can scope integration work and timeline.
3. **Rule engine strategy**: confirm whether USB will use Featurespace exclusively or bring an additional risk engine — this affects architecture and onboarding.

**Infographic type:** Clean numbered list — minimal design

**Slide layout**
- *Title:* "Next Steps: Three Decisions"
- *Three numbered items, each as a card with bold label + one sentence:*
  1. **Operating model decision** — Confirm whether USB will operate transaction alert monitoring and case resolution in-house, or engage Zeta's outsourced operations services. *This determines the implementation shape.*
  2. **Integration assessment** — Share USB's current auth flow, notification provider landscape, and BI tool stack so Zeta can scope integration work and timeline. *This determines scope and timeline.*
  3. **Rule engine strategy** — Confirm whether USB will use Featurespace exclusively or bring an additional risk engine. *This affects architecture and onboarding.*
- No other visual elements. White space is intentional — this slide stays on screen during the closing Q&A.

**Build notes**
- CTA slides must be clean. Three numbered items are scannable.
- The italic "this determines..." lines give each item urgency without being pushy.
- Do not add differentiator content here — that belongs on Slide 16.

---

## 5) Content Production Checklist for Marketing Team

- Keep language factual and defensible; avoid unapproved superlatives.
- Show architecture and process visuals over text-heavy slides.
- For each major claim, pair with proof artifact:
  - Lucid architecture view
  - Featurespace overview deck
  - Model design document
  - Product screenshots/demo capture
  - Superset dashboard examples (for Slide 11)
- Maintain consistent terminology per the canonical glossary:
  - Use "Tachyon FRM", "Tachyon Switch", "Featurespace", "Notification Center", "Operations Center" — no internal module names.
  - Use "cardholder-managed risk controls" (not "user-managed").
  - Use "tenant-isolated" for isolation language.
  - Use "suppressible" for rule suppression eligibility.
- Do not reference FedRAMP in this deck; general platform compliance is covered in the suite deck.
- Business-impact footer: each slide includes a "Why this matters" statement. Render this as a consistent footer strip or accent box at the bottom of each slide — same position, same styling, one sentence. Use USB-specific language ("your fraud operations team", "your cardholders"). Do not attach specific dollar figures or basis-point claims unless pre-approved.

---

## 6) Open Inputs Needed from Pre-Sales/SME Before Final Deck

1. Confirm parallel vs sequential invocation model when a second rule engine is added alongside Featurespace.
2. Confirm exact card-scheme dispute lifecycle/state names for Slide 6 demo narration.
3. Confirm final sensitivity-category taxonomy labels for Slide 8 notification policy visuals.
4. Confirm final outcome mapping from notification response states to case/rule transitions (Slide 8).
5. Confirm final examples of suppressible vs non-suppressible rule categories for Slide 9 demo narration.
6. Confirm final examples to show for custom entities and custom workflow actions (Slide 10).
7. Confirm final customer-safe wording for outsourced transaction operations scope boundaries (Slide 12).
8. Confirm final RACI for default vs outsourced operating model (Slide 13).
9. Confirm exact demo artifacts/screens for Slide 15 scenario trace.
10. Case management screenshots/slides for Disputes Workbench demo.
11. Any client-approved metrics or case-study outcomes.

---

## 7) Source Material

- **Lucid FRM architecture and workflow diagrams** (authenticated access required):
  - FRM integration and orchestration view (Tachyon FRM with pre-integrated and additional rule engines)
  - RT/NRT processing view and state/profile output flow
  - Card_Not_Present Fraud page (rule/fraud scenario branch)
  - BIN attack detection flow: invalid decline pattern detection -> merchant identification -> blocklisting
  - Compromised card flow: detection -> card block -> case creation -> agent review -> re-issuance -> ABU network notification
  - Token fraud handling: token provisioning signals, device binding, token lifecycle events feeding into Featurespace rules
- **Featurespace high-level overview presentation** (authenticated access required):
  - Tenancy and data isolation architecture
  - Rule authoring interface, versioning, change control, UAT, and rollback capabilities
  - Rule deployment turnaround (seconds after approver sign-off)
  - Action tags model (block, step-up/2-way notification, etc.)
- **Featurespace model design document** (authenticated access required):
  - Core card AI model: risk scoring based on customer behavior and identified fraud patterns
  - Supervised ML model: deployable in ~2 weeks, silent mode for 4-6 months while learning from transaction data
  - Custom model support: clients can deploy their own pre-trained models for immediate scoring
- **Case management and Disputes Workbench** — slides/screenshots to be provided by product team.

Note: all external links require authenticated access during deck production.
