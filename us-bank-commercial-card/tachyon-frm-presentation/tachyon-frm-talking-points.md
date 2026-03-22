# Tachyon FRM Talking Points

## Purpose

This is the working talking-points sheet for the Tachyon FRM deep-dive deck.
It will be refined in Q&A turns, slide by slide, using additional context from the pre-sales team.

Use this file to capture:
- exact presenter talking points
- proof statements and caveats
- expected client questions and recommended responses
- open items to confirm with product/operations/legal

---

## Working Principles

- Keep statements factual, specific, and defensible.
- Separate confirmed facts from assumptions/placeholders.
- Do not claim unapproved SLAs, metrics, or guarantees.
- Anchor each talking point to a slide objective.

---

## Canonical Glossary (Locked)

- **Tachyon FRM**: provides decisioning, case management, orchestration for events and notifications, user-managed risk controls, and actions usable in decision/case workflows.
- **Tachyon Switch (Transaction Processing Engine)**: transaction processing and transaction-risk-assessment event source.
- **Customer Lifecycle Management**: customer and demographic lifecycle event source.
- **Card Management System**: card issuance, re-issuance, and replacement event source.
- **Tachyon Credit**: repayments and credit-limit event source (single box representation).
- **Token Management System**: token creation and token status event source.
- **Cipher**: product name.
- **Notification Center**: module within Cipher used for IAM and notification capabilities.
- **Operations Center**: operations module used by bank teams to configure and run case workflows.
- **Featurespace**: pre-integrated risk rule engine partner.

**Terminology rules**
- Do not use internal module names (e.g., Athena, Aries, Acropolis, Aura/Ruby, Tethys) in client-facing talk tracks.
- Do not mention "Orcus" in client-facing content.
- Use expanded names (for example, "Customer Lifecycle Management" instead of "CLM").
- Use `Product Capability (Function)` formatting in architecture labels.

---

## Current Understanding Snapshot (Before Q&A Refinement)

- Tachyon FRM is the client-facing fraud capability layer across RT and NRT flows.
- Featurespace is a pre-integrated risk rule engine within the Tachyon FRM architecture.
- Tachyon FRM supports additional integrations and can orchestrate across multiple rule engines/providers (current capability).
- Confirmed source-system feeds (from Lucid walkthrough context):
  - Tachyon Switch (Transaction Processing Engine): transaction risk assessment
  - Customer Lifecycle Management: demographic detail changes
  - Card Management System: card issuance/re-issuance/replacement
  - Tachyon Credit: repayments and credit limit updates
  - Notification Center: two-way notification response inputs
  - Token Management System: token creation and token status updates
- FRM processing patterns include both RT and NRT (event subscription) paths.
- FRM outcomes include action recommendations and state/profile outputs that drive fraud operations.

---

## Slide-by-Slide Talking Points Capture

## Slide 1 - Executive Context and Objectives

**Draft talking points**
- Tachyon FRM positioning for this conversation is capability-first:
  - rich ML models
  - deep coverage for cards and tokens
  - rich set of actions
  - cardholder-managed risk controls
- Cardholder-managed risk controls are exercisable by cardholders and program admins.
- Operations Center provides governance and operational oversight for these controls.

**Scope exclusion (for presenter use if scope-creep questions arise)**
- This session covers transaction fraud decisioning and case management for commercial cards.
- Not in scope: AML/KYC, credit risk decisioning, network-level fraud detection.

**Likely client questions**
- Why this architecture vs existing bank FRM setup?
- What outcomes should be expected in phase 1?

**Open points to confirm**
- Client-specific success criteria language for opening slide.

---

## Slide 2 - Capability Coverage View

**Draft talking points**
- The deep-dive covers entities/events, recommendation actions, operations workflows, and governance contracts.
- RT and NRT behaviors are both covered explicitly.
- All discussed capabilities are ready out-of-box.
- Customer-specific work is limited to:
  - integrations into the customer ecosystem
  - workflow tailoring to the customer's operating model
- Capability blocks aligned to the 17-slide structure:
  - Entities/states/events (RT/NRT)
  - Decision model and action recommendations (RT/NRT)
  - Case management, commands, and financial actions
  - Notification and cardholder-managed risk
  - Extensibility/configurability
  - Reporting and analytics
  - Rule engine, model management, tenancy
  - Operational contracts
  - FRM-specific compliance

**Likely client questions**
- Which capabilities are day-1 vs phase-2?
- What is configurable by the bank team?

**Open points to confirm**
- Phase sequencing and any out-of-scope boundaries.

---

## Slide 3 - Solution Architecture: Tachyon + Featurespace

**Draft talking points**
- Tachyon FRM is the integration and orchestration layer for fraud decisioning, case workflows, event handling, and notifications.
- Featurespace is pre-integrated as a risk rule engine.
- Architecture supports additional integrations and orchestration across multiple rule engines/providers.
- In the Tachyon Switch (Transaction Processing Engine) transaction flow, Tachyon FRM can orchestrate:
  - Featurespace
  - an additional risk rule engine, where required by customer policy/architecture.
- 3DS / step-up authentication:
  - Full native ACS support with EMV Co 3DS 2.2 compliance.
  - Authentication events (AReq, CReq, CRes) are RT and correlated to the originating transaction at decision time.
  - The fraud decision is made with full authentication context in a single RT pass — not reconstructed after the fact.
- Performance characteristics:
  - RT risk rule execution, including Featurespace round-trip, completes in under 200ms.
  - Architecture is horizontally scalable; routinely load-tested up to 30,000 TPS.
  - Throughput ceiling is infrastructure-bound, not architecture-bound.

**Likely client questions**
- What changes if a non-Featurespace FRM is selected?
- Where are ownership boundaries and support boundaries?
- Does the 200ms include the full round-trip to Featurespace?
  - Yes — the under-200ms figure includes the Featurespace round-trip.
- What is the P99 latency, not just average?
- What is the degradation behavior under load — graceful degradation, circuit-breaking, or hard failure?
- If a second rule engine is added, are engines invoked in parallel or sequentially?
- Is the ACS Zeta-owned or a third-party integration?
- Does the bank control challenge flow policies (when to challenge vs frictionless)?

**Open points to confirm**
- Confirm parallel vs sequential invocation model when a second rule engine is added alongside Featurespace.

---

## Slide 4 - Exhaustive Entities, States, and Events (RT/NRT)

**Draft talking points**
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
  - CRUD changes to entities (Account Holder, Account, Cardholder Profile, Card, Token) — NRT
  - Customer custom events — NRT
- Processing/decision split:
  - Transaction events and 3DS authentication events are RT.
  - Authentication events are correlated to the originating transaction so the rule engine receives both signals in a single decisioning pass.
  - All other events update rule-engine state and can trigger NRT rules and NRT decisions.
  - Custom events can be streamed to Tachyon FRM and to rule engines.

**Likely client questions**
- Is the event set exhaustive for all card programs?
- How are schema/version changes handled?
- Are 3DS authentication outcomes (success, failure, abandon) available as NRT events for rule tuning?
- How does this interact with scheme mandates for SCA / step-up thresholds?

**Open points to confirm**
- Final exhaustive list and schema governance process.

---

## Slide 5 - FRM Decision Model and Action Recommendations

**Draft talking points**
- This slide establishes the canonical recommendation catalog — shown once, referenced by all later slides.
- Decision trigger model: risk scores and rule triggers translate into specific action recommendations.
- Complete recommendation catalog:
  - Transaction: Decline
  - Card: Temp Block (time-bound), Temp Block Card and All Tokens, Block and Replace, Block-Replace-Disable-Tokens, Block Card and All Tokens
  - Token: Temp Block, Block
  - Cardholder: Notify, Notify-for-Feedback
- Applicability varies: some recommendations are RT-eligible, others NRT-only, others available across all contexts.
- Tachyon FRM maps rule-engine recommendation tags to these executable action types.
- Decision proportionality: the system selects the right-sized response based on risk signal strength.
- Case-specific financial actions (provisional credits, transaction reversals) are covered in Slide 7.

**Likely client questions**
- How does the system decide between a temporary block vs permanent closure?
- Which recommendations are available in RT vs NRT vs case workflows?

**Open points to confirm**
- None for action catalog baseline.

---

## Slide 6 - Case Management Capabilities

**Draft talking points**
- Case lifecycle includes trigger, triage, investigation, action, closure, and auditability.
- Case management is bank-operated.
- Bank teams can design workflows as needed using Operations Center capabilities provided in the solution.
- Slide includes demo link to Disputes Workbench in Operations Center.
- Workbench supports fraud-alert review, dispute-case creation, and resolution.
- Custom workflows can be authored using BPMN for any alert/case pattern.
- Cardholder input can be captured and used in case resolution.
- Supports card-scheme dispute resolution approaches end-to-end.
- SLAs can be configured/tracked at both task and case levels.
- Action depth includes provisional credits, transaction reversals, and other case actions in addition to Slide 5 fraud actions.

**Likely client questions**
- What are SLA controls and queueing/routing rules?
- How complete is audit history and evidence handling?
- How are BPMN workflow changes governed (versioning, approvals, rollback)?
- What level of card-scheme dispute integration is out-of-box vs integration-specific?

**Open points to confirm**
- Official case-state model and integration list for client-facing narrative.
- Final list of card-scheme dispute lifecycle states to show in demo narration.

---

## Slide 7 - Case Commands: Block, Re-Issuance, and Financial Actions

**Draft talking points**
- This slide covers the complete set of commands available within case workflows.
- All fraud-control actions from Slide 5 are available within case workflows.
- Additional case-only financial commands:
  - provisional credits
  - transaction reversals
- Execution controls are configurable in workflows as required by the customer:
  - auto-executable vs approval-gated designation
  - maker/checker controls for high-impact commands
  - escalation triggers within workflows
  - full auditability: command execution log, override tracking, evidence linkage to case
- Compromise and re-issuance flow (example):
  - detection -> block -> case -> review -> re-issue -> downstream updates.
- BIN attack handling with merchant blocklisting as an operational flow example.

**Likely client questions**
- Can execution controls (auto/manual, maker/checker) be configured per our operating model?
  - Yes — all execution governance is modeled in workflows and configurable per customer requirements.
- How are bulk compromise events managed?
- What guardrails exist for high-impact financial actions (credits/reversals)?

**Open points to confirm**
- Final policy matrix for auto/manual execution and approvals by command type.

---

## Slide 8 - Notification Capabilities

**Draft talking points**
- Summary headline: 6 channels, BYO provider support, closed-loop feedback.
- Notification and IAM capabilities are provided through Notification Center.
- Out-of-box channels: SMS, email, mobile push (iOS/Android), browser push (Chrome/Edge), outbound webhooks, outbound voice calls.
- Bring-your-own provider support is available; multiple providers can be used for load distribution, resiliency, and cost-based routing.
- Routing is policy-driven with static rules using recipient address/endpoint.
- Notification policies are sensitivity-category based.
- Recipient preferences are supported via API endpoints.
- Multi-cast is supported: one message to multiple recipients across multiple channels.
- Read-receipt tracking is available (channel-specific).
- Feedback forms and response workflows are supported (embedded/deep-link based on channel capability).
- Outbound telephony supports retry/escalation to alternate channels where configured.
- Notification outcomes can feed back into case and rule workflows through configured transitions.
- Incident portal monitoring and follow-up workflow hooks are supported.

**Likely client questions**
- What are localization and rate-limiting capabilities?
- What customer experience controls exist for high-alert frequency?
- Is provider routing dynamic or static policy?
- Can notification preferences be managed externally through APIs?
- Are webhooks outbound only?

**Open points to confirm**
- Final sensitivity-category model and policy examples to show.
- Final outcome mapping from notification response states to case/rule transitions.

---

## Slide 9 - User-Managed Risk and Self-Serve Operations

**Draft talking points**
- In this deck context, user-managed risk means cardholder-managed risk.
- Cardholders can:
  - restrict transactions of certain kinds using rule grammar
  - specify temporary overrides to allow transactions
  - suppress eligible risk rules
  - respond to fraud alerts
- This is especially relevant for commercial cards where corporate issuers can constrain usage by:
  - specific merchant IDs/terminals
  - business hours
  - IP addresses
- Guardrail logic:
  - cardholder restrictions cannot override product-specified controls
  - only risk rules tagged `suppressible` can be suppressed by cardholders
  - rule-level `suppressible` tag determines suppressibility eligibility
- Operations Center governs boundaries, approvals, and auditability.

**Likely client questions**
- What can USB change directly vs require vendor intervention?
- How quickly can approved changes be activated?
- Can cardholders bypass core product controls?
- How is suppressibility controlled per rule?

**Open points to confirm**
- Final examples of suppressible vs non-suppressible rule categories for demo narration.

---

## Slide 10 - Extensibility and Configurability

**Draft talking points**
- Configurability and extensibility should be presented as distinct:
  - configurability: policy/workflow tuning within existing platform surfaces
  - extensibility: adding new engines/events/entities/providers/actions
- Design supports policy/config evolution without core platform rewrites.
- Integration contracts should be presented as explicit and stable (API/event/schema boundaries).
- Extensibility examples to call out:
  - support for custom entities (in addition to custom events)
  - support for custom actions for use in workflows
  - multi-engine orchestration with pre-integrated and additional providers.

**Likely client questions**
- What customizations are low-risk configuration changes?
- Which changes are roadmap-level enhancements?
- How are custom entities modeled and used in rule/workflow context?
- Can custom actions be governed with the same approval/audit controls as default actions?

**Open points to confirm**
- Client-safe examples of configuration-only customization.
- Final examples to show for custom entities and custom workflow actions.

---

## Slide 11 - Reporting and Analytics

**Draft talking points**
- Data foundation:
  - All fraud evaluation data (decisioning, scoring, event data) and case data are exported to a managed data lake.
  - Real-time events are available for streaming consumption.
  - A well-structured data mart is refreshed daily for analytical use.
  - Data lake is fully tenant-isolated in storage, serving, and processing.
  - Data retention and purge policies are custom and configurable per tenant.
- Two analytics interfaces — acknowledge this honestly:
  - Rule performance analytics (rule hit rates, model score distributions, detection-rate metrics) are currently accessed through Featurespace's native portal.
  - All other analytics (SLA adherence, agent performance, case lifecycle, custom reports) are unified in Tachyon FRM's Superset-based BI layer. Bank teams build, schedule, and distribute their own reports and dashboards.
- Data mart is accessible to the bank's own BI tools (Tableau, Power BI, Looker, etc.) in addition to Superset.
- All card-scheme reporting is handled end-to-end by Tachyon FRM and/or Tachyon Switch.
- Common report catalog:
  - Operational: daily fraud summary, alert-to-case conversion, case aging/backlog, agent workload/throughput, SLA compliance (Reg E/Z timelines, scheme deadlines).
  - Risk and rule performance: rule hit-rate analysis, model score distributions, fraud trend analysis (by MCC, merchant, geography, CP/CNP, time), decline rate by rule/threshold, cardholder impact.
  - Financial: fraud loss summary (gross/recovered/net), provisional credit outstanding, chargeback/representment status, write-off tracking.
  - Cardholder experience: notification delivery and response rates, cardholder feedback analysis, rule suppression activity and outcomes, customer contact rate.

**Likely client questions**
- Can we connect our existing BI tools to the data mart?
  - Yes — the data mart is accessible to external BI tools.
- Is the Featurespace analytics in the same interface as Superset?
  - No — Featurespace analytics are accessed through a separate Featurespace portal.
- What is the data mart refresh latency?
  - Daily refresh; real-time events available separately for streaming use cases.
- Can we build our own reports?
  - Yes — Superset is positioned as self-serve BI for the bank team.
- How is analytics access controlled?
  - Tenant-isolated with role-based access controls.

**Open points to confirm**
- None.

---

## Slide 12 - Rule Engine Setup: Model Management, Supervision, Tenancy

**Draft talking points**
- Tachyon FRM is fully tenant-isolated:
  - workflows, actions, rules, and policies are localized to tenant.
- Featurespace model:
  - dedicated customer tenant
  - Featurespace provides the default model
  - customer can bring own Featurespace relationship
  - customer can bring own model
  - Zeta can build model or help customer build model
  - Zeta supports rule authoring and model management for Featurespace.
- If any other risk engine is used:
  - customer works with that provider for rules/models
  - Tachyon FRM continues orchestration/integration role.
- Transaction alert monitoring and case resolution are expected to be tenant-handled by default.
- Zeta can provide outsourced transaction operations services if requested.

**Likely client questions**
- What exactly is tenant-isolated at the Tachyon FRM layer?
- Who owns model/rule responsibilities for Featurespace vs other engines?
- Can operations be tenant-run or outsourced?

**Open points to confirm**
- Final customer-safe wording for outsourced transaction operations scope boundaries.

---

## Slide 13 - Operational Contracts with the Bank

**Draft talking points**
- Zeta's default role is technology provider. Zeta owns platform availability and uptime. Zeta does not represent the efficacy of fraud rules, models, or fraud outcomes.
- Default responsibility split:
  - Zeta: platform availability/uptime, notification delivery (shared with BYO provider).
  - Issuer or their partners: rule authoring/tuning, model updates/deployment, transaction alert monitoring, case resolution/dispute handling, emergency controls, fraud outcomes.
- Two distinct service categories — present these as separate:
  - Model and rule management services: always issuer or their partners.
  - Transaction monitoring and operations services: issuer or their partners by default; Zeta can provide as BPO services.
- When Zeta provides BPO services:
  - Zeta is responsible for SLAs corresponding to those specific services.
  - Model and rule management remain with the issuer or their partners.
- Emergency controls (BIN blocks, throttling, etc.) are exercised by the issuer or their transaction monitoring partner.
- Audit evidence is self-serve from Zeta Trust Center.
- Regulatory accountability follows the role structure: the bank is always accountable to the regulator.

**Likely client questions**
- Who is accountable during incidents and model/rule failures?
  - Platform incidents: Zeta. Rule/model efficacy: issuer or their partners.
- What does Zeta own even in the default model?
  - Platform availability, uptime, and shared notification delivery. Nothing else operationally.
- What exactly is included in the BPO services?
  - Transaction monitoring and operations. Model and rule management remain with the issuer.
- Who handles emergency controls at 2 AM?
  - The issuer or their transaction monitoring partner. If Zeta is engaged as BPO, Zeta handles this per BPO SLAs.
- Where do we get audit evidence for examiners?
  - Self-serve from Zeta Trust Center.

**Open points to confirm**
- None — responsibility model confirmed.

---

## Slide 14 - FRM-Specific Compliance Posture

**Draft talking points**
- Position this slide as FRM-layer-specific compliance; general platform security, privacy, and DR/BCP are in the suite deck.
- Regulatory compliance enforced through FRM workflows:
  - Reg E / EFTA: dispute timelines (10 business days / 45 calendar days), provisional credit obligations — enforced through case management SLAs and workflow automation.
  - Reg Z / TILA: credit card billing dispute requirements (60-day filing, 2-billing-cycle resolution) — directly relevant for commercial credit card programs.
  - BSA/AML: FRM case data and investigation evidence feed SAR filing workflows.
  - UDAAP: fraud-control actions do not create unfair outcomes; relevant to cardholder-managed controls and suppression logic.
  - GLBA / Reg P: financial privacy in fraud data sharing, notification content, and analytics access.
  - CCPA / CPRA: state privacy for cardholder data in investigation records, data retention, right-to-know/right-to-delete.
- Card network compliance:
  - Visa / Mastercard Operating Regulations: chargeback lifecycle, reason-code handling, representment timelines, pre-arbitration/arbitration.
  - Scheme dispute integration is end-to-end (as demonstrated in Slide 6).
- Security and controls attestations:
  - PCI DSS: tokenization of PAN in analytics/reporting, access controls on case data, audit logging.
  - SOC 2 Type II: security, availability, and processing integrity.
  - ISO 27001: information security management certification.
- Model and financial controls governance:
  - FFIEC / SR 11-7 / OCC 2011-12: model risk management for Featurespace model lifecycle (cross-ref Slide 12).
  - SOX: provisional credits and transaction reversals are financial transactions with SOX implications.

**Likely client questions**
- How are Reg E/Z timelines enforced in the workflow — is it configurable?
- What audit evidence is available for examiners?
- How does PCI DSS apply to the analytics/data mart layer?
- Where is the boundary between FRM-layer compliance and platform-suite compliance?

**Open points to confirm**
- None.

---

## Slide 15 - Deep-Dive Demo Scenarios

**Draft talking points**
- Scenario 1:
  - transaction is declined due to risk rule
  - customer provides feedback and suppresses the eligible rule
  - transaction is reattempted and succeeds
  - demonstrate that suppression is allowed only for rules tagged `suppressible`
- Scenario 2:
  - transaction rule triggers card block
  - card block is executed and reflected in subsequent controls
- Close each scenario with measurable control outcomes and operational implications.

**Likely client questions**
- How does customer feedback map to rule suppression and re-decisioning?
- What prevents suppression of non-eligible rules?
- How quickly does card block take effect after rule trigger?

**Open points to confirm**
- Final demo trace artifacts/screens to show decline reason, suppression decision, and reattempt success.

---

## Slide 16 - Why Tachyon FRM for USB Commercial Cards

**Draft talking points**
- This is the conviction slide. Everything demonstrated in the preceding slides converges here.
- Lead with commercial-card-specific differentiators — these are the capabilities where a competing FRM would struggle to say "we do that too":
  - Cardholder-managed risk controls with `suppressible` guardrails — employees unblock themselves for legitimate business transactions within corporate policy. No blanket overrides; only rules tagged `suppressible` are eligible.
  - Corporate-issuer policy boundaries — merchant ID, terminal, business hours, IP restrictions. Purpose-built for commercial card governance.
  - Unified RT decisioning with 3DS — transaction and authentication signals correlated in a single pass. Full authentication context at decision time, not a post-hoc reconstruction.
  - Unified card + token command model — single atomic actions across card and all associated tokens. Reflects a platform designed with tokens as first-class entities, not bolted on later.
  - Token-level independent controls — act on a specific token without affecting the card. Most legacy FRM systems can't do this.
- Then architecture-level differentiators:
  - Under 200ms end-to-end including Featurespace round-trip.
  - End-to-end scheme dispute integration with financial action execution — FRM and dispute lifecycle in one platform. No handoff to a separate dispute system.
  - Notify-for-Feedback as a native closed-loop action — cardholder response feeds case and rule workflows, not just a one-way alert.
- Close with the footer: "All capabilities are production-ready, tenant-isolated, and configurable per your operating model."

**Likely client questions**
- How does the card + token command model compare to what we have today?
- Can we start with a pilot on a subset of card programs?

**Open points to confirm**
- None — this slide uses content confirmed across all prior slides.

---

## Slide 17 - Next Steps

**Draft talking points**
- Three decisions that determine the shape, scope, and timeline of the implementation.
- Present each as a decision USB needs to make, not an ask from Zeta:
  1. Operating model decision: in-house vs outsourced transaction alert monitoring and case resolution. This determines implementation shape.
  2. Integration assessment: share current auth flow, notification provider landscape, and BI tool stack. This determines scope and timeline.
  3. Rule engine strategy: Featurespace-only or multi-engine. This determines architecture and onboarding.
- This slide stays on screen during closing Q&A.

**Likely client questions**
- What does a typical implementation timeline look like?
- What is the commercial model (licensing, per-transaction, etc.)?
- Can we get a scoped proposal based on today's discussion?

**Open points to confirm**
- None.

---

## Q&A Log (To Be Filled During Discussion)

### Turn 1
- Slide: Terminology/architecture baseline (cross-slide)
- Context provided:
  - Replace internal module names with client-facing functional names.
  - Do not mention Orcus.
  - Use Cipher as product and Notification Center as module.
  - Use Tachyon Credit as one box.
  - Case management is bank-operated via Operations Center capabilities.
  - Featurespace is pre-integrated; multi-engine orchestration is current capability.
- Updated talking points:
  - Added canonical glossary and terminology rules.
  - Updated architecture and source-system mapping language.
  - Updated case management ownership narrative.
  - Updated notification narrative with Notification Center.
- New open items:
  - None from terminology baseline.

### Turn 2
- Slide: Slide 1
- Context provided:
  - Positioning focus: rich ML models, deep cards/tokens coverage, rich actions, and user risk controls.
  - "User-managed" clarified as cardholder-managed controls.
- Updated talking points:
  - Reframed controls as exercisable by cardholders and program admins.
  - Added Operations Center governance framing.
- New open items:
  - None.

### Turn 3
- Slide: Slide 2 and Slide 3
- Context provided:
  - All discussed capabilities are out-of-box.
  - Custom work only for customer-required integrations/workflows.
  - Architecture slide should show Tachyon FRM + Featurespace + additional risk rule engine in Tachyon Switch flow.
- Updated talking points:
  - Added out-of-box plus customization boundary language.
  - Added multi-engine architecture statement in transaction flow.
- New open items:
  - Diagram artifact to be provided by user.

### Turn 4
- Slide: Slide 4
- Context provided:
  - Final entity list and event list provided.
  - Only transaction events are RT.
  - Non-transaction events are for rule-engine state updates and NRT rules/decisions.
  - Custom events are streamable to Tachyon FRM and rule engine.
- Updated talking points:
  - Added exhaustive entity/event inventory and explicit RT/NRT split.
  - Added custom-event ingestion statement.
- New open items:
  - Confirm desired wording on clearing messages when narrating RT vs post-authorization operations.

### Turn 5
- Slide: Slide 5
- Context provided:
  - Action catalog provided by entity with explicit availability across RT, NRT, and case workflows.
  - Card actions: Temp Block (time-bound), Temp Block Card and All Tokens, Block and Replace, Block-Replace-Disable-Tokens, Block Card and All Tokens.
  - Token actions: Temp Block, Block.
  - Cardholder actions: Notify, Notify-for-Feedback.
- Updated talking points:
  - Added entity-based action catalog and execution applicability language.
  - Reframed client questions to focus on automation/approval controls.
- New open items:
  - Confirm if any customer policy constraints limit specific actions by channel/program.

### Turn 6
- Slide: Slide 4
- Context provided:
  - Event list should also include transaction reversal, repayment, and repayment reversal.
- Updated talking points:
  - Added transaction reversal, repayment, and repayment reversal to transaction events.
- New open items:
  - None.

### Turn 7
- Slide: Slide 4
- Context provided:
  - Event list should also include card PIN reset and card PIN changed.
- Updated talking points:
  - Added card PIN reset and card PIN changed to transaction events.
- New open items:
  - None.

### Turn 8
- Slide: Slide 4
- Context provided:
  - Event list should also include credit limit updated.
- Updated talking points:
  - Added credit limit updated to transaction events.
- New open items:
  - None.

### Turn 9
- Slide: Slide 6
- Context provided:
  - Slide should include Disputes Workbench demo link in Operations Center.
  - Include capabilities: fraud alert review, dispute-case create/resolve, BPMN custom workflows, cardholder input in case resolution, card-scheme dispute integration, SLA at task/case, and advanced actions (provisional credits, transaction reversals).
- Updated talking points:
  - Expanded Slide 6 with dispute-workbench capability depth and governance/performance points.
  - Added boundary note so Slide 6 focuses on disputes/case workflows while Slide 7 covers the case command catalog and execution governance.
- New open items:
  - Confirm exact card-scheme lifecycle/state names to mention in presenter script.

### Turn 10
- Slide: Slide 7
- Context provided:
  - Case commands should also reflect the expanded command model discussed across prior turns.
- Updated talking points:
  - Added entity-based case command catalog for card, token, and cardholder actions.
  - Included dispute/financial commands: provisional credits and transaction reversals.
  - Added automation/approval/auditability framing and likely client questions on control guardrails.
- New open items:
  - Confirm final command policy matrix by program/channel.

### Turn 11
- Slide: Slide 8
- Context provided:
  - Notification channels include SMS, email, mobile push, browser push, outbound webhooks, and outbound telephony.
  - BYO provider support with multiple providers for load distribution, resiliency, and cost-based routing.
  - Routing should be static policy with rules based on recipient address/endpoint.
  - Use notification policy terminology, based on sensitivity categorization.
  - Read receipts are channel-specific; feedback forms supported as channel allows; webhooks are outbound only.
  - Telephony should include retries/escalation to alternate channels.
  - Keep notification SLA metrics out of this slide.
- Updated talking points:
  - Expanded Slide 8 to full out-of-box channel and provider model with policy/routing details.
  - Added response/workflow integration and channel-capability constraints.
- New open items:
  - Confirm final sensitivity-category taxonomy labels for slide visuals.

### Turn 12
- Slide: Slide 9
- Context provided:
  - User-managed risk should be framed as cardholder-managed risk.
  - Cardholders can apply transaction restrictions via rule grammar, specify overrides, suppress eligible risk rules, and respond to fraud alerts.
  - Commercial-card controls can be constrained by merchant IDs/terminals, business hours, and IP addresses under corporate policy.
  - Restrictions cannot override product-specified controls.
  - Only rules tagged `suppressible` are eligible for cardholder suppression.
  - There is no `max_suppress_window` concept to mention.
- Updated talking points:
  - Reframed Slide 9 around cardholder-managed controls with explicit policy guardrails.
  - Added `suppressible` tag as rule-level eligibility model.
- New open items:
  - Final suppressible/non-suppressible example set for deck visuals.

### Turn 13
- Slide: Slide 12 (Rule Engine Setup) and Slide 13 (Operational Contracts)
- Context provided:
  - Tachyon FRM is fully tenant-isolated (workflows/actions/rules/policies localized per tenant).
  - Featurespace model: dedicated tenant, Featurespace provides the default model, BYOM support, customer can bring own relationship, Zeta can build/help build model.
  - For other engines, customer works with that provider for rules/models.
  - Alert monitoring and case resolution expected to be tenant-handled; optional outsourced transaction operations services by Zeta.
  - Do not discuss SLA terms in these slides.
- Updated talking points:
  - Reframed Slide 12 tenancy/model management with explicit responsibility split.
  - Reframed Slide 13 around operating model options and accountability without SLA terms.
- New open items:
  - Final scoped wording for outsourced operations service boundaries.

### Turn 14
- Slide: Slide 13 (now Slide 15)
- Context provided:
  - Demo scenario 1: transaction decline due to risk rule, followed by customer feedback to suppress rule, followed by transaction reattempt and success.
  - Demo scenario 2: card block from transaction rule.
- Updated talking points:
  - Reframed Slide 15 to the two specified demo scenarios.
  - Added explicit `suppressible` guardrail callout in scenario 1.
- New open items:
  - Confirm exact demo artifacts/screens for scenario trace.

### Turn 15
- Slide: Cross-document consistency pass
- Context provided:
  - Review and fix consistency/completeness issues.
- Updated talking points:
  - Aligned Slide 10 with explicit configurability vs extensibility framing.
  - Added custom entities and custom workflow actions to Slide 10 narrative.
  - Harmonized Slide 5 action catalog with explicit transaction decline across docs.
  - Removed internal-name references from source notes in the outline doc.
- New open items:
  - None.

### Turn 16
- Slide: Cross-slide additions (Slides 3, 4, 11, 14, and structural updates)
- Context provided:
  - Performance: RT rules execute in under 200ms including Featurespace round-trip. 30K TPS routinely tested. Horizontally scalable.
  - 3DS: full native ACS support, EMV Co 3DS 2.2. AReq/CReq/CRes are RT and correlated to the originating transaction at decision time.
  - Reporting: fraud evaluation and case data exported to data lake. Daily-refreshed data mart. Tenant-isolated. Featurespace portal for rule performance. Superset for self-serve BI. Bank's own BI tools can connect. Scheme reporting handled by Tachyon FRM/Switch. Configurable data retention per tenant.
  - Compliance: Reg E/EFTA, Reg Z/TILA, BSA/AML, UDAAP, GLBA/Reg P, CCPA/CPRA, Visa/Mastercard Operating Regulations, PCI DSS, SOC 2 Type II, ISO 27001, FFIEC/SR 11-7, SOX. General platform compliance (including DR/BCP) covered in suite deck; do not mention FedRAMP.
  - Slide 5/7 restructured: Slide 5 owns the canonical action catalog (decision model). Slide 7 focuses on execution governance (auto/manual, maker/checker, auditability) without repeating the list.
  - Business-impact "Why this matters" callout added to every slide (2-15).
- Updated talking points:
  - Added performance and 3DS content to Slide 3.
  - Added 3DS authentication events to Slide 4.
  - Added new Slide 11 (Reporting and Analytics).
  - Renumbered old Slides 11/12/13 to 12/13/15.
  - Added new Slide 14 (Compliance).
  - Restructured Slides 5 and 7 to eliminate overlap.
- New open items:
  - Confirm parallel vs sequential invocation model for second rule engine.

