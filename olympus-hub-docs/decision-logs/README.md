# Decision Log

Architecture Decision Records (ADRs) for Olympus Hub.

---

## About

This folder contains Architecture Decision Records documenting significant design decisions made during the development of Olympus Hub. Each ADR captures the context, decision, and consequences to provide a historical record and rationale for future reference.

### Format

All ADRs follow the standard format:
- **Status**: Proposed, Accepted, Deprecated, or Superseded
- **Context**: Why the decision was needed
- **Decision**: What was decided
- **Consequences**: Positive, negative, and neutral outcomes

---

## Index

| # | Decision | Status | Date | Category |
|---|----------|--------|------|----------|
| [0001](./0001-signal-normalization.md) | Normalize signal format between Signal Providers and Signal Exchange | Accepted | 2026-01-05 | integration |
| [0002](./0002-scenario-specification-types.md) | Three specification types for Scenarios (Normative, Automation, Deployment) | Accepted | 2026-01-05 | architecture |
| [0003](./0003-signal-exchange-responsibility-boundaries.md) | Signal Exchange routes to Applications, not tasks or agents | Accepted | 2026-01-05 | architecture |
| [0004](./0004-reminder-kind-attribute.md) | Semantic typing for reminder requests via kind attribute | Accepted | 2026-01-05 | integration |
| [0005](./0005-notification-services-architecture.md) | Single Notification Service with persona-specific handlers | Accepted | 2026-01-05 | architecture |
| [0006](./0006-task-queue-escalation-model.md) | Cumulative assignment across escalation levels | Accepted | 2026-01-06 | process |
| [0007](./0007-composite-pattern-technology-agnostic.md) | Scenario-as-Agent pattern does not require AI capabilities | Accepted | 2026-01-06 | composite |
| [0008](./0008-persona-channel-usecase-meta-approach.md) | UX organized by Persona, Channel, and Use Case | Accepted | 2026-01-06 | architecture |
| [0009](./0009-headless-services-with-channel-adapters.md) | Headless access services with channel adapters for rendering | Accepted | 2026-01-06 | architecture |
| [0010](./0010-ai-assistants-first-class-channel.md) | AI assistants (ChatGPT, Claude, Gemini) as first-class interaction channel | Accepted | 2026-01-06 | architecture |
| [0011](./0011-persona-scoped-api-channels.md) | MCP and REST APIs organized by persona, not function | Accepted | 2026-01-06 | integration |
| [0012](./0012-control-plane-data-plane-channel-separation.md) | Business User on Data Plane; other channels on Control Plane | Accepted | 2026-01-06 | architecture |
| [0013](./0013-shared-utility-consoles.md) | Agent and Supervisor share utility consoles | Accepted | 2026-01-06 | ux |
| [0014](./0014-gitops-operator-model.md) | GitOps-based operator model for Hub resources | Accepted | 2026-01-06 | operators |
| [0015](./0015-persona-based-operator-grouping.md) | Operators grouped by persona | Accepted | 2026-01-06 | operators |
| [0016](./0016-typed-data-store-crds.md) | Typed CRDs for data stores (Ganymede, Callisto, Europa) | Accepted | 2026-01-06 | operators |
| [0017](./0017-trigger-as-standalone-specification.md) | TriggerSpec as standalone CRD | Accepted | 2026-01-06 | operators |
| [0018](./0018-dedicated-apm-operator.md) | Dedicated APM operator for Hub observability | Accepted | 2026-01-06 | operators |
| [0019](./0019-signal-exchange-observer-pattern.md) | Observer pattern for SX module integration | Accepted | 2026-01-06 | signal-exchange |
| [0020](./0020-request-level-granularity.md) | Signal Exchange operates at Request level only | Accepted | 2026-01-06 | signal-exchange |
| [0021](./0021-cns-as-delivery-layer.md) | Cipher Notification Service as delivery layer | Accepted | 2026-01-06 | notification |
| [0022](./0022-workbench-scoped-user-preferences.md) | User preferences scoped to workbench with tenant fallback | Accepted | 2026-01-06 | notification |
| [0023](./0023-http-tool-calling-application.md) | HTTP Tool Calling Application as built-in Hub Application | Accepted | 2026-01-06 | hub-native-utilities |
| [0024](./0024-javascript-transformation-functions.md) | JavaScript transformation functions for DTO mapping | Accepted | 2026-01-06 | hub-native-utilities |
| [0025](./0025-stateless-decision-prediction-tools.md) | Decision and Prediction Tools as stateless utilities | Accepted | 2026-01-06 | hub-native-utilities |
| [0026](./0026-signal-exchange-reminder-capability.md) | Signal Exchange built-in reminder capability | Accepted | 2026-01-06 | signal-exchange |
| [0027](./0027-four-layer-storage-model.md) | Four-layer storage model for Hub data | Accepted | 2026-01-06 | data-architecture |
| [0028](./0028-data-classification.md) | Cognitive vs Operational vs Domain data classification | Accepted | 2026-01-06 | data-architecture |
| [0029](./0029-caf-control-plane.md) | CAF as control plane for Memory Services (not storage) | Accepted | 2026-01-06 | data-architecture |
| [0030](./0030-workbench-scoped-data-stores.md) | Application Data Stores are workbench-scoped (not runtime-scoped) | Accepted | 2026-01-06 | data-architecture |
| [0031](./0031-optional-data-stores.md) | Application Data Stores are optional (not mandated) | Accepted | 2026-01-06 | data-architecture |

---

## By Category

### Architecture
- [0002](./0002-scenario-specification-types.md) - Three specification types for Scenarios
- [0003](./0003-signal-exchange-responsibility-boundaries.md) - Signal Exchange responsibility boundaries
- [0005](./0005-notification-services-architecture.md) - Notification Services architecture
- [0008](./0008-persona-channel-usecase-meta-approach.md) - Persona-Channel-UseCase meta approach
- [0009](./0009-headless-services-with-channel-adapters.md) - Headless services with channel adapters
- [0010](./0010-ai-assistants-first-class-channel.md) - AI assistants as first-class channel
- [0012](./0012-control-plane-data-plane-channel-separation.md) - Control Plane vs Data Plane separation

### Integration
- [0001](./0001-signal-normalization.md) - Signal normalization between SPs and SX
- [0004](./0004-reminder-kind-attribute.md) - Reminder kind attribute for semantic typing
- [0011](./0011-persona-scoped-api-channels.md) - Persona-scoped API channels

### Process
- [0006](./0006-task-queue-escalation-model.md) - Task queue escalation model

### Composite
- [0007](./0007-composite-pattern-technology-agnostic.md) - Composite patterns are technology agnostic

### UX
- [0013](./0013-shared-utility-consoles.md) - Shared utility consoles between Agent and Supervisor

### Operators
- [0014](./0014-gitops-operator-model.md) - GitOps-based operator model for Hub resources
- [0015](./0015-persona-based-operator-grouping.md) - Operators grouped by persona
- [0016](./0016-typed-data-store-crds.md) - Typed CRDs for data stores (Ganymede, Callisto, Europa)
- [0017](./0017-trigger-as-standalone-specification.md) - TriggerSpec as standalone CRD
- [0018](./0018-dedicated-apm-operator.md) - Dedicated APM operator for Hub observability

### Signal Exchange
- [0019](./0019-signal-exchange-observer-pattern.md) - Observer pattern for SX module integration
- [0020](./0020-request-level-granularity.md) - Signal Exchange operates at Request level only
- [0026](./0026-signal-exchange-reminder-capability.md) - Signal Exchange built-in reminder capability

### Notification
- [0021](./0021-cns-as-delivery-layer.md) - Cipher Notification Service as delivery layer
- [0022](./0022-workbench-scoped-user-preferences.md) - User preferences scoped to workbench with tenant fallback

### Hub Native Utilities
- [0023](./0023-http-tool-calling-application.md) - HTTP Tool Calling Application as built-in Hub Application
- [0024](./0024-javascript-transformation-functions.md) - JavaScript transformation functions for DTO mapping
- [0025](./0025-stateless-decision-prediction-tools.md) - Decision and Prediction Tools as stateless utilities

### Data Architecture
- [0027](./0027-four-layer-storage-model.md) - Four-layer storage model for Hub data
- [0028](./0028-data-classification.md) - Cognitive vs Operational vs Domain data classification
- [0029](./0029-caf-control-plane.md) - CAF as control plane for Memory Services (not storage)
- [0030](./0030-workbench-scoped-data-stores.md) - Application Data Stores are workbench-scoped
- [0031](./0031-optional-data-stores.md) - Application Data Stores are optional (not mandated)

---

## Contributing

When making significant design decisions:

1. Create a new ADR file with the next sequential number
2. Follow the standard ADR format
3. Update this README with the new entry
4. Link to related documentation

See `.cursor/rules/decision-logs.mdc` for detailed guidelines.
