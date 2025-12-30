# 8. Experience & Domain Agents (Application Layer)
Experience agents operationalize FFOS for customers, RMs, and partners. They own customer journeys, surface insights in channels, execute actions, and enforce guardrails in collaboration with core services and foundation agents.

## 8.1 Do Agents (Execution Agents)

### 8.1.1 Supported Action Types (Payments, Transfers, Product Ops)
Execute domestic/international payments, internal transfers, investment switches, standing instructions, document submissions, product service requests (limit changes, card controls), and obligation fulfilment actions. Catalogues of permissible actions tie directly to consent scopes and policy rules.

### 8.1.2 Interaction with Core System Services
Before execution, do agents call guardrail evaluators, retrieve consent tokens, validate workflow state, and reserve workflow steps. They leverage integration adapters to reach product systems, invoke document service for evidence, and update core memory with structured event payloads.

### 8.1.3 Execution Lifecycle and Error Handling
Lifecycle includes intent capture, validation, authorization, execution, confirmation, and reconciliation. Errors trigger compensation workflows, channel notifications, governance review tasks, and optional RM follow-up. Idempotency keys prevent double processing.

## 8.2 Think Agents (Advisory Agents)

### 8.2.1 Advisory Domains (Expense, Debt, Savings, Investment)
Deliver insights on spend optimization, debt restructuring, savings discipline, insurance adequacy, and investment allocations anchored to family goals, obligations, and risk posture.

### 8.2.2 Contextualization Using Foundation Agents
Consume cashflow, goals, and risk state vectors plus graph memory to tailor recommendations per member role, consent scope, persona, and channel context. They include sensitivity analyses and highlight policy constraints (e.g., minors cannot authorize investments).

### 8.2.3 Recommendation Generation & Explanation
Produce structured advice with rationale, referenced data points, recommended actions, and policy compliance tags. Explainability artifacts are stored in memory, surfaced to channels, and available to RM and audit teams.

## 8.3 Orchestrator Agents

### 8.3.1 Multi-Step Flows and State Management
Run structured journeys—stress-event mitigation, surplus allocation, education planning, inheritance transitions—using workflow primitives, checkpointed state, and compensation paths.

### 8.3.2 Scenarios (Stress Handling, Surplus Allocation, Renewals)
Scenario libraries include emergency liquidity orchestration, cash surplus deployment, renewal reminders, caregiving transitions, and lifecycle events. Orchestrators adapt flows dynamically when events or consents change mid-journey.

### 8.3.3 Coordination of Do and Think Agents via IAC
Use IPC topics to invoke think agents for analysis, trigger do agents for execution, and ping governance agents for approvals. Orchestrators persist context objects for replay, ensuring deterministic outcomes for regulators.

## 8.4 Governance Agents

### 8.4.1 Policy Enforcement and Guardrails
Centralize evaluation of household policies, product rules, and regulatory requirements before actions are executed. They evaluate channel, role, consent scope, monetary thresholds, and behavioural signals.

### 8.4.2 Approval, Escalation, and Overrides
Manage approval matrices, escalate to RM workbenches or supervisory queues for overrides, and log deviations with justification and supporting documents.

### 8.4.3 Logging, Explainability, and Audit Trails
Write structured audit events referencing consent artifacts, workflow IDs, data lineage, and explanations from think agents. Provide investigators with timeline views linking requests, decisions, and actions.

## 8.5 Family Concierge Experience Agents

### 8.5.1 Family Console and Household Overview
Curate unified dashboards summarizing obligations, goals, risk posture, action queues, and RM recommendations. Support cross-channel continuity by sharing state via channel adapters.

### 8.5.2 Member-Specific Concierges (Parent, Teen, Elder, Assistant)
Tailor interactions per persona with scoped data, suggested tasks, educational nudges, and channel-appropriate tone. Concierges honour quiet hours, accessibility preferences, and language settings from channel policy service.

### 8.5.3 Task Aggregation and “Next Best Action” Surfaces
Aggregate tasks across workflows, risk alerts, and RM follow-ups. Recommend next actions based on urgency, consent readiness, and household goals, and trigger channel notifications or RM handoffs with embedded workflow links.
