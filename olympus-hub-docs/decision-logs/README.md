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
| [0032](./0032-bots-as-persona-copilots.md) | MS Teams bots designed as persona copilots | Accepted | 2026-01-06 | ms-teams-integration |
| [0033](./0033-chat-groups-as-collaboration-surfaces.md) | Chat groups as collaboration surfaces for requests | Accepted | 2026-01-06 | ms-teams-integration |
| [0034](./0034-workbench-scoped-bots.md) | One bot of each kind per workbench | Accepted | 2026-01-06 | ms-teams-integration |
| [0035](./0035-two-stage-message-classification.md) | Two-stage message classification pipeline | Accepted | 2026-01-06 | ms-teams-integration |
| [0036](./0036-cross-channel-update-attribution.md) | Cross-channel update attribution via credential sharing | Accepted | 2026-01-06 | ms-teams-integration |
| [0037](./0037-ms-teams-module-as-observer.md) | MS Teams module as Signal Exchange observer | Accepted | 2026-01-06 | ms-teams-integration |
| [0038](./0038-group-orchestration-bot-construct.md) | Group Orchestration Bot as MS Teams module construct | Accepted | 2026-01-06 | ms-teams-integration |
| [0039](./0039-direct-services-bypass.md) | Direct services bypass Signal Exchange | Accepted | 2026-01-06 | ms-teams-integration |
| [0040](./0040-direct-tool-dispatcher.md) | Direct Tool Dispatcher as platform utility | Accepted | 2026-01-06 | hub-native-utilities |
| [0041](./0041-standalone-tool-variation.md) | Standalone Tool as ToolInstance variation | Accepted | 2026-01-06 | operators |
| [0042](./0042-scenario-as-tool-granularity.md) | Scenario as Tool granularity (entire scenario = one tool) | Accepted | 2026-01-06 | composite-patterns |
| [0043](./0043-workbench-as-machine-transitive-exposure.md) | Workbench as Machine transitive tool exposure | Accepted | 2026-01-06 | composite-patterns |
| [0044](./0044-platform-agnostic-registry.md) | Platform-agnostic container registry via Olympus Weave | Accepted | 2026-01-06 | artifact-registry |
| [0045](./0045-subscription-scoped-git-repository.md) | One Git repo per subscription, main branch only | Accepted | 2026-01-06 | artifact-registry |
| [0046](./0046-semver-promotion-compatibility.md) | Semantic version compatibility for promotion | Accepted | 2026-01-06 | artifact-registry |
| [0047](./0047-scenario-atomic-promotion-unit.md) | Scenario as atomic promotion unit | Accepted | 2026-01-06 | artifact-registry |
| [0048](./0048-physical-copy-cross-subscription.md) | Physical copy for cross-subscription promotion | Accepted | 2026-01-06 | artifact-registry |
| [0049](./0049-git-as-storage-manual-sync.md) | Git as storage with manual sync triggers | Accepted | 2026-01-06 | artifact-registry |
| [0050](./0050-test-runner-as-hub-application.md) | Hub Test Runner as Hub Application on Atlantis | Accepted | 2026-01-06 | ci-subsystem |
| [0051](./0051-developer-responsibility-stubbing.md) | Developer responsibility for machine/tool stubbing | Accepted | 2026-01-06 | ci-subsystem |
| [0052](./0052-caf-record-type-taxonomy.md) | CAF defines 8 record types in 3 categories | Accepted | 2026-01-07 | caf |
| [0053](./0053-caf-record-id-traversal.md) | UUID IDs, case_id binding, traversal conventions | Accepted | 2026-01-07 | caf |
| [0054](./0054-caf-typed-content-convention.md) | MIME-based content typing with human-readable formats | Accepted | 2026-01-07 | caf |
| [0055](./0055-caf-memory-store-contract.md) | CRD registration, HTTPS retrieval, JWS auth for memory stores | Accepted | 2026-01-07 | caf |
| [0056](./0056-caf-episodic-memory-scope.md) | Episodic Memory scope, Case Record as root anchor | Accepted | 2026-01-07 | caf |
| [0057](./0057-episodic-memory-immutability.md) | Episodic records are immutable with content hash | Accepted | 2026-01-07 | caf |
| [0058](./0058-caf-semantic-explainers.md) | Every schema includes semantic explainer section | Accepted | 2026-01-07 | caf |
| [0059](./0059-caf-memory-not-knowledge.md) | CAF governs Memory only; ETSL governs Knowledge | Accepted | 2026-01-07 | caf |
| [0060](./0060-learning-services-deferred-automation.md) | Learning Services manual initially, automation deferred | Accepted | 2026-01-07 | caf |
| [0061](./0061-no-pii-in-episodic-memory.md) | No PII allowed in episodic memory records | Accepted | 2026-01-07 | memory-services |
| [0062](./0062-memory-writes-via-signal-exchange.md) | All memory writes routed through Signal Exchange | Accepted | 2026-01-07 | memory-services |
| [0063](./0063-memory-reads-via-access-tools.md) | Memory reads via defined access tools only | Accepted | 2026-01-07 | memory-services |
| [0064](./0064-memory-services-subfolder-organization.md) | Memory Services organized into subfolders | Accepted | 2026-01-07 | memory-services |
| [0065](./0065-cognitive-application-capability-profile.md) | Cognitive Application as capability profile of Hub Application | Accepted | 2026-01-07 | architecture |
| [0066](./0066-request-hierarchy-context-inheritance.md) | Request hierarchy, context inheritance, and lifecycle cascade | Accepted | 2026-01-07 | request-management |
| [0067](./0067-agent-memory-session-scope.md) | Agent Memory strictly session-scoped | Accepted | 2026-01-08 | memory-services |
| [0068](./0068-agent-memory-framework-native-idioms.md) | Agent Memory enables framework-native idioms | Accepted | 2026-01-08 | memory-services |
| [0069](./0069-agent-memory-storage-services.md) | Four storage services for Agent Memory | Accepted | 2026-01-08 | memory-services |
| [0070](./0070-agent-memory-encryption-isolation.md) | Agent Memory encryption and isolation model | Accepted | 2026-01-08 | memory-services |
| [0071](./0071-agent-memory-storage-backends.md) | Agent Memory storage backends (Callisto + Europa + S3) | Accepted | 2026-01-08 | memory-services |
| [0072](./0072-seer-guardrails-two-layer-model.md) | Seer guardrails: behavioral guidelines + sidecar enforcement | Accepted | 2026-01-08 | seer |
| [0073](./0073-seer-authority-enforcement-opa.md) | Seer authority enforcement via OPA at Tool Gateway and SX | Accepted | 2026-01-08 | seer |
| [0074](./0074-seer-runtime-atlantis-based.md) | Seer runtime on Atlantis (EKS, Heracles, Istio) | Accepted | 2026-01-08 | seer |
| [0075](./0075-seer-model-gateway-bifrost.md) | Seer Model Gateway based on Bifrost OSS | Accepted | 2026-01-08 | seer |
| [0076](./0076-seer-observability-watch-based.md) | Seer agent observability via Olympus Watch | Accepted | 2026-01-08 | seer |
| [0077](./0077-seer-evaluation-deferred.md) | Seer Agent Evaluation deferred to post-MVP | Accepted (Deferred) | 2026-01-08 | seer |
| [0078](./0078-agent-directability-rejection-escalation.md) | Agent Directability via Rejection-Escalation Model | Accepted | 2026-01-08 | directability |
| [0079](./0079-scenario-escalation-matrix.md) | Scenario Escalation Matrix for Application Exceptions | Accepted | 2026-01-08 | directability |
| [0080](./0080-directability-operations.md) | Directability Operations in Task Management | Accepted | 2026-01-08 | directability |
| [0081](./0081-production-feedback-loop.md) | Production Feedback Loop to Development Workbench | Accepted | 2026-01-09 | workbench-management |
| [0082](./0082-hub-desk-restructuring.md) | Hub Desk Restructuring (Workbench Studio → 3 Desks) | Accepted | 2026-01-09 | ux-architecture |
| [0083](./0083-apo-as-hub-persona.md) | Automation Product Owner as Hub Persona | Accepted | 2026-01-09 | personas |
| [0084](./0084-automation-lifecycle-split.md) | Automation Lifecycle Split (Conventional vs Agentic) | Accepted | 2026-01-09 | journeys |
| [0085](./0085-seer-desk-naming-convention.md) | Seer Desk Naming Convention (Standardize on "Desk") | Accepted | 2026-01-09 | ux-architecture |
| [0086](./0086-are-role-naming.md) | Agent Reliability Engineer (ARE) Role Naming | Accepted | 2026-01-09 | personas |
| [0087](./0087-idea-intent-charter-model.md) | Idea-Intent-Charter Model for Automation Ideation | Accepted | 2026-01-09 | ideation |
| [0088](./0088-devops-workbench-composite-pattern.md) | DevOps Workbench as Composite Pattern | Accepted | 2026-01-09 | devops-workbench |
| [0089](./0089-bidirectional-devops-workbench-binding.md) | Bidirectional DevOps Workbench Binding (Two CRDs) | Accepted | 2026-01-09 | devops-workbench |
| [0090](./0090-signal-routing-via-atropos-devops.md) | Signal Routing via Atropos for DevOps | Accepted | 2026-01-09 | devops-workbench |
| [0091](./0091-git-based-crd-publishing.md) | Git-Based CRD Publishing for DevOps Workbench | Accepted | 2026-01-09 | devops-workbench |
| [0092](./0092-hub-resources-no-namespace-concept.md) | Hub Resources Do Not Use Namespace Concept | Accepted | 2026-01-11 | CLI, CRD Design |
| [0103](./0103-machine-signal-emission.md) | Machine Signal Emission Through Signal Providers | Accepted | 2026-01-15 | integration |

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
- [0065](./0065-cognitive-application-capability-profile.md) - Cognitive Application as capability profile

### Integration
- [0001](./0001-signal-normalization.md) - Signal normalization between SPs and SX
- [0004](./0004-reminder-kind-attribute.md) - Reminder kind attribute for semantic typing
- [0011](./0011-persona-scoped-api-channels.md) - Persona-scoped API channels
- [0103](./0103-machine-signal-emission.md) - Machine Signal Emission Through Signal Providers

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
- [0041](./0041-standalone-tool-variation.md) - Standalone Tool as ToolInstance variation

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
- [0040](./0040-direct-tool-dispatcher.md) - Direct Tool Dispatcher as platform utility

### Data Architecture
- [0027](./0027-four-layer-storage-model.md) - Four-layer storage model for Hub data
- [0028](./0028-data-classification.md) - Cognitive vs Operational vs Domain data classification
- [0029](./0029-caf-control-plane.md) - CAF as control plane for Memory Services (not storage)
- [0030](./0030-workbench-scoped-data-stores.md) - Application Data Stores are workbench-scoped
- [0031](./0031-optional-data-stores.md) - Application Data Stores are optional (not mandated)

### MS Teams Integration
- [0032](./0032-bots-as-persona-copilots.md) - MS Teams bots designed as persona copilots
- [0033](./0033-chat-groups-as-collaboration-surfaces.md) - Chat groups as collaboration surfaces for requests
- [0034](./0034-workbench-scoped-bots.md) - One bot of each kind per workbench
- [0035](./0035-two-stage-message-classification.md) - Two-stage message classification pipeline
- [0036](./0036-cross-channel-update-attribution.md) - Cross-channel update attribution via credential sharing
- [0037](./0037-ms-teams-module-as-observer.md) - MS Teams module as Signal Exchange observer
- [0038](./0038-group-orchestration-bot-construct.md) - Group Orchestration Bot as MS Teams module construct
- [0039](./0039-direct-services-bypass.md) - Direct services bypass Signal Exchange

### Composite Patterns
- [0042](./0042-scenario-as-tool-granularity.md) - Scenario as Tool granularity (entire scenario = one tool)
- [0043](./0043-workbench-as-machine-transitive-exposure.md) - Workbench as Machine transitive tool exposure

### Artifact Registry
- [0044](./0044-platform-agnostic-registry.md) - Platform-agnostic container registry via Olympus Weave
- [0045](./0045-subscription-scoped-git-repository.md) - One Git repo per subscription, main branch only
- [0046](./0046-semver-promotion-compatibility.md) - Semantic version compatibility for promotion
- [0047](./0047-scenario-atomic-promotion-unit.md) - Scenario as atomic promotion unit
- [0048](./0048-physical-copy-cross-subscription.md) - Physical copy for cross-subscription promotion
- [0049](./0049-git-as-storage-manual-sync.md) - Git as storage with manual sync triggers

### CI Subsystem
- [0050](./0050-test-runner-as-hub-application.md) - Hub Test Runner as Hub Application on Atlantis
- [0051](./0051-developer-responsibility-stubbing.md) - Developer responsibility for machine/tool stubbing

### Cognitive Audit Fabric (CAF)
- [0029](./0029-caf-control-plane.md) - CAF as control plane for Memory Services (not storage)
- [0052](./0052-caf-record-type-taxonomy.md) - 9 record types in 3 categories (Core, Lifecycle, Learning)
- [0053](./0053-caf-record-id-traversal.md) - UUID IDs, case_id universal binding, traversal patterns
- [0054](./0054-caf-typed-content-convention.md) - MIME-based content typing, human-readable serialization
- [0055](./0055-caf-memory-store-contract.md) - CRD registration, reader/writer protocols, JWS authentication
- [0056](./0056-caf-episodic-memory-scope.md) - Episodic Memory scope, Case Record as root
- [0057](./0057-episodic-memory-immutability.md) - Episodic records immutable with SHA-256 content hash
- [0058](./0058-caf-semantic-explainers.md) - Semantic explainer section in every content schema
- [0059](./0059-caf-memory-not-knowledge.md) - CAF governs Memory; ETSL governs Knowledge
- [0060](./0060-learning-services-deferred-automation.md) - Learning Services manual initially, automation deferred

### Memory Services — Enterprise
- [0061](./0061-no-pii-in-episodic-memory.md) - No PII allowed in episodic memory records
- [0062](./0062-memory-writes-via-signal-exchange.md) - All memory writes routed through Signal Exchange
- [0063](./0063-memory-reads-via-access-tools.md) - Memory reads via defined access tools only
- [0064](./0064-memory-services-subfolder-organization.md) - Memory Services organized into subfolders (enterprise/agent/shared)

### Memory Services — Agent
- [0067](./0067-agent-memory-session-scope.md) - Agent Memory strictly session-scoped (not cross-session)
- [0068](./0068-agent-memory-framework-native-idioms.md) - Agent Memory enables framework-native idioms (no ESPP enforcement)
- [0069](./0069-agent-memory-storage-services.md) - Four storage services: Log, Conversation, KV, Documents
- [0070](./0070-agent-memory-encryption-isolation.md) - Application-layer encryption with agent+session unique keys
- [0071](./0071-agent-memory-storage-backends.md) - Storage backends: KV→Callisto, Log/Conv/Docs→Europa+S3

### Request Management
- [0066](./0066-request-hierarchy-context-inheritance.md) - Request hierarchy, context inheritance, lifecycle cascade

### Seer (AI Runtime)
- [0072](./0072-seer-guardrails-two-layer-model.md) - Two-layer guardrails: behavioral guidelines + sidecar enforcement
- [0073](./0073-seer-authority-enforcement-opa.md) - Authority enforcement via OPA at Tool Gateway and Signal Exchange
- [0074](./0074-seer-runtime-atlantis-based.md) - Runtime on Atlantis (EKS, Heracles, Istio)
- [0075](./0075-seer-model-gateway-bifrost.md) - Model Gateway based on Bifrost OSS
- [0076](./0076-seer-observability-watch-based.md) - Agent observability via Olympus Watch
- [0077](./0077-seer-evaluation-deferred.md) - Agent Evaluation deferred to post-MVP

### Agent Directability
- [0078](./0078-agent-directability-rejection-escalation.md) - Agent Directability via Rejection-Escalation Model
- [0079](./0079-scenario-escalation-matrix.md) - Scenario Escalation Matrix for Application Exceptions
- [0080](./0080-directability-operations.md) - Directability Operations in Task Management

### Workbench Management
- [0081](./0081-production-feedback-loop.md) - Production Feedback Loop to Development Workbench

### UX Architecture
- [0082](./0082-hub-desk-restructuring.md) - Hub Desk Restructuring (Workbench Studio → 3 Desks)
- [0085](./0085-seer-desk-naming-convention.md) - Seer Desk Naming Convention

### Personas
- [0083](./0083-apo-as-hub-persona.md) - Automation Product Owner as Hub Persona
- [0086](./0086-are-role-naming.md) - Agent Reliability Engineer (ARE) Role Naming

### Journeys
- [0084](./0084-automation-lifecycle-split.md) - Automation Lifecycle Split (Conventional vs Agentic)

### Ideation
- [0087](./0087-idea-intent-charter-model.md) - Idea-Intent-Charter Model for Automation Ideation

### DevOps Workbench
- [0088](./0088-devops-workbench-composite-pattern.md) - DevOps Workbench as Composite Pattern for automation development
- [0089](./0089-bidirectional-devops-workbench-binding.md) - Two-CRD model with operators for bidirectional binding
- [0090](./0090-signal-routing-via-atropos-devops.md) - Signal routing via Atropos for cross-workbench events
- [0091](./0091-git-based-crd-publishing.md) - Git-based CRD publishing with PR approval workflow

### CLI & CRD Design
- [0092](./0092-hub-resources-no-namespace-concept.md) - Hub Resources Do Not Use Namespace Concept (workbench instance scoping)

---

## Contributing

When making significant design decisions:

1. Create a new ADR file with the next sequential number
2. Follow the standard ADR format
3. Update this README with the new entry
4. Link to related documentation

See `.cursor/rules/decision-logs.mdc` for detailed guidelines.
