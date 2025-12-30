# 9. Channels, Interaction Surfaces & UX Integration
FFOS surfaces capabilities across the bank's existing and emerging channels through a channel abstraction layer. Each adapter enforces security, consent, and UX constraints while presenting unified APIs to experience agents.

## 9.1 Primary Bank Channels

### 9.1.1 FFOS Integration into Mobile Banking
Embed concierge surfaces, obligation calendars, approvals, and goal trackers inside mobile apps using SDKs or web views backed by channel adapters. Secure session handoffs, device binding, and consent-aware data filters ensure only scoped information is rendered. Push notifications reference workflow IDs and link back into FFOS contexts.

### 9.1.2 FFOS Integration into Internet Banking
Expose advanced planning tools, document submissions, governance dashboards, and RM collaboration panels on web portals. Integrate with existing authentication journeys, leveraging embedded widgets or micro-frontends that call FFOS APIs through the channel layer. Browser telemetry feeds observability dashboards for usability and performance monitoring.

## 9.2 Conversational & Agentic Channels

### 9.2.1 Chatbot / VA Integration
Conversational interfaces route intents to orchestrator agents via IPC. Responses include structured cards referencing household state, action options, and audit metadata. Bot frameworks enforce consent redaction rules and escalate high-risk intents to human channels.

### 9.2.2 Voice Interface Integration
Voice channels leverage speech-to-text adapters, multi-factor verification, and limited-scope interactions suited for auditory confirmations. Audio transcripts are stored in document services, linked to workflows, and reviewed by governance agents when disputes arise.

## 9.3 Third-Party & Embedded Surfaces

### 9.3.1 Embedded Views in RM Workbenches
RM tools receive widgets summarizing family state vectors, pending approvals, and risk flags. RMs can trigger orchestrated actions directly from their workbench; FFOS handles guardrails, audit logging, and state synchronization.

### 9.3.2 Partner Channel Embeds (where applicable)
Where regulators permit, FFOS exposes read-only or action-limited views through secure APIs for partners (insurers, schools, caregiving networks). Channel policies enforce tokenized identities, consent verification, throttling, and kill-switch capabilities managed by governance agents.
