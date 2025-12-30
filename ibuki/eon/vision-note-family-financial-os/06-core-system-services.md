# 6. Core System Services (Infrastructure Layer)
Core services form the privileged substrate of FFOS. They host authoritative records, enforce security, manage workflows, and provide the shared capabilities on which all agents rely. Each service operates under strict IAM policies, emits telemetry, and exposes APIs/events with schema governance. Collectively they ensure that identity, memory, consent, workflows, documents, IPC/IAC, and channel I/O behave consistently regardless of which agent or channel invokes them.

## 6.1 Identity, Roles & Family Graph Service

### 6.1.1 Family Entity Model
Maintains household identities with persistent identifiers, lifecycle states, and binding to regulatory KYC records. Supports composite attributes (address, jurisdictions, household archetypes) and links to bank customer master data without duplicating authoritative sources.

### 6.1.2 Role Definitions and Delegation
Role templates define permissions (view, initiate, approve, administer) and constraints per channel. Delegations include effective dates, revocation hooks, and conditional scopes (e.g., payment limits). Delegation events update graph memory and trigger consent recalculations.

### 6.1.3 Lifecycle Management of Family Relationships
APIs manage onboarding, member additions/removals, guardianship transitions, and survivorship events. Workflows integrate document service for evidence, invoke consent capture, and update audit timelines.

## 6.2 Consent, Privacy & Access Management Service

### 6.2.1 Consent Models and Scopes
Consent artifacts specify subject, resource, action, channel, duration, and governing policy. Supports layered scopes (household-wide vs member-specific) and dynamic conditions triggered by obligations or thresholds.

### 6.2.2 Access Control Structures (View, Initiate, Approve, Administer)
Enforces fine-grained entitlements for data reads, workflow initiation, approvals, and administrative updates. Access tokens include consent references and policy digests for downstream enforcement.

### 6.2.3 Consent Capture, Renewal, and Revocation Workflows
Workflow service drives capture via digital signature, biometric, or RM attestation. Renewal reminders route through external I/O adapters. Revocations cascade across agent subscriptions, IPC topics, and cached context states.

### 6.2.4 Policy Configuration and Compliance Alignment
Policy repository stores regulator-aligned templates (DPDP, GDPR, GLBA) and bank-specific rules. Integration with legal/compliance tooling ensures version control, impact analysis, and certification workflows.

## 6.3 Security & Guardrail Service

### 6.3.1 Authentication and Binding to Bank IAM
Uses bank IAM (e.g., OAuth/OIDC, SAML, hardware tokens) for human and service identities. Issues short-lived scoped credentials for agents; maps to device risk scores and RM entitlements.

### 6.3.2 Policy Evaluation and Pre-Execution Checks
Every action request passes through guardrail evaluators verifying consent validity, role constraints, behavior heuristics, and product rules before execution agents act.

### 6.3.3 Behavioral and Anomaly Detection Hooks
Streaming analytics monitor IPC traffic, channel events, and feature anomalies. Alerts trigger governance agents for review, escalate to RM tools, or auto-throttle workflows.

### 6.3.4 Thresholds, Rate Limits, and Safety Rails
Configurable thresholds enforce cumulative limits (per member, per household, per timeframe). Rate limiting integrates with workflow scheduler for back-off and compensation.

## 6.4 Event & Timeline Service

### 6.4.1 Event Ingestion from Bank Systems
Connectors normalize feeds from core banking, payments, CRM, trade finance, and external sources. Supports streaming (Kafka) and batch ingestion with schema validation.

### 6.4.2 Event Normalization and Classification
Applies transformation pipelines to map events to canonical types (obligation, cashflow, consent, document, agent action). Tagging includes family, member, product, and risk metadata.

### 6.4.3 Event Storage and Retrieval APIs
Stores ordered timelines with retention aligned to regulatory policies. APIs allow agents to query windows, filter by type, and subscribe to change feeds.

### 6.4.4 Derived Event Streams for Agents
Generates enriched streams (e.g., aggregated cashflow spikes, delinquency precursors) feeding foundation agents and governance monitors.

## 6.5 Obligation & Billing Service

### 6.5.1 Detection of Recurring Obligations
Analyzes transactions, documents, and event metadata to identify recurring bills, mandates, tuition, caregiving payments, and loan installments. Uses feature store signals for prediction confidence.

### 6.5.2 Obligation Scheduling and Calendars
Maintains calendars with due dates, escalation tiers, and dependencies. Integrates with workflow scheduler for reminders, auto-pay prep, and contingency planning.

### 6.5.3 Responsibility Assignment Across Members
Maps obligations to responsible members or delegates, capturing oversight requirements. Updates graph memory and consent scopes accordingly.

### 6.5.4 Exception Handling and Escalation Events
Flagged exceptions trigger governance agents, create tasks, and notify via external I/O. Supports partial payments, deferrals, and RM intervention flows.

## 6.6 Workflow & Task Scheduler

### 6.6.1 Workflow Primitives (Start, Wait, Escalate, Retry)
Provides deterministic workflow engine with primitives for synchronous/asynchronous tasks, wait states, escalations, retries, and compensation. Every step logs to core memory for auditability.

### 6.6.2 Time-Based and Event-Based Triggers
Supports cron-like schedules and event-driven triggers (obligation due, consent expiry, anomaly detection) to start or adapt workflows.

### 6.6.3 Idempotency, Rollback, and Compensation Patterns
Persists workflow state, correlates retries, and exposes compensation templates (reverse payment, revoke recommendation) to maintain consistency despite partial failures.

## 6.7 Document & Evidence Service

### 6.7.1 Document Ingestion and Storage
Receives uploads from channels and RM systems, enforces virus/DLP scanning, and stores encrypted artifacts with lifecycle policies.

### 6.7.2 Metadata, Indexing, and Retrieval
Captures structured metadata (document type, issuing authority, expiry). Offers search APIs across households and workflows with access controls anchored to consent.

### 6.7.3 Document-to-Entity Linkages
Documents link to family graph nodes, obligations, workflows, and consent records to ensure traceable evidence chains.

## 6.8 Core Memory & Data Services

### 6.8.1 Family Financial Memory
Persistent chronological record of household finances.

#### 6.8.1.1 Transactional History
Normalized ledger of inflows/outflows across accounts, tagged with household and member context.

#### 6.8.1.2 Obligation and Commitment History
Stores detected obligations, statuses, adjustments, and responsible parties.

#### 6.8.1.3 Lifecycle & Milestone History
Tracks lifecycle events (births, education transitions, retirements) that influence workflows and guardrails.

### 6.8.2 Family Graph Memory
Durable record of relationship dynamics.

#### 6.8.2.1 Member & Relationship Graph
Captures nodes, edges, authority traits, and history of changes with temporal validity.

#### 6.8.2.2 Role and Permission History
Maintains snapshots of role assignments, delegations, and revocations for compliance evidence.

### 6.8.3 Feature Store (Derived Signals)
Computes shareable features for agents.

#### 6.8.3.1 Cashflow Features
Includes runway, burn rate, surplus/deficit forecasts, and smoothing buffers.

#### 6.8.3.2 Behavioral and Spend Features
Derives spend clusters, merchant exposure, discretionary vs essential ratios, and channel usage.

#### 6.8.3.3 Risk and Health Indicators
Generates stress flags, dependency ratios, insurance coverage gaps, and anomaly scores for governance.

## 6.9 Inter-Agent Communication (IAC) & Internal IPC

### 6.9.1 Messaging Patterns (Pub/Sub, Request/Response, Events)
Provides multi-protocol bus supporting pub/sub for state broadcasts, request/response for synchronous queries, and event sourcing for audits.

### 6.9.2 Shared Context Objects and Contracts
Defines schema-managed context bundles (family state vector, consent tokens, workflow handles) to ensure deterministic agent collaboration.

### 6.9.3 Agent Addressing, Discovery, and Routing
Registry maintains agent metadata, capabilities, and routing rules. Supports versioning and A/B deployments under governance oversight.

### 6.9.4 Consistency, Ordering, and Delivery Guarantees
Implements ordered topics for critical flows, idempotent handlers, and dead-letter queues with governance review triggers.

## 6.10 External I/O & Channel Abstraction

### 6.10.1 Outbound Communication (Notifications, Prompts, Alerts)
Sends contextualized messages via SMS, push, email, RM console, or partner integrations with policy-driven throttling and personalization.

### 6.10.2 Inbound Communication (User Inputs, Approvals, Exceptions)
Captures approvals, clarifications, and deviations from channels, normalizing payloads and mapping to workflow contexts.

### 6.10.3 Channel Adapters (Mobile App, Web, Chat, Voice, Third-Party)
Adapters enforce UI/UX constraints, security posture, and telemetry capture per channel while presenting a unified API to agents.

### 6.10.4 Channel Policy and Preference Management
Stores household and member preferences for notification modes, quiet hours, languages, and accessibility requirements. Policies feed guardrails to avoid consent breaches or channel fatigue.

## 6.11 Observability & Telemetry Service

### 6.11.1 Platform Metrics and Tracing
Collects infrastructure and application telemetry (latency, throughput, error budgets) across services, workflows, IPC topics, and channel adapters. Metrics are tagged with service, region, release, and workload identifiers for precise SLO tracking.

### 6.11.2 Logging and Distributed Traces
Provides centralized log pipelines, correlation IDs, and distributed tracing so engineers, SRE, and control teams can troubleshoot incidents. Retention policies align with regulatory logging requirements and feed audit stores.

### 6.11.3 Alerting and Incident Hooks
Integrates with guardrail and workflow services to trigger alerts, automate incident workflows, and capture evidence packages for regulators. Supports synthetic monitoring and chaos simulations to validate resiliency assumptions.
