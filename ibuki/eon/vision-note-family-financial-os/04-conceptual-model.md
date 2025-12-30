# 4. Conceptual Model

## 4.1 The Family as a Financial Entity
FFOS treats the family as a sovereign entity with its own legal identity, lifecycle, obligations, entitlements, cashflow view, and risk posture. The entity persists beyond individual product relationships, enabling intergenerational continuity, caregiving transitions, and multi-household constructs (e.g., blended families, dependent elders, MSME hybrids). Household context becomes queryable and executable through system services rather than tribal knowledge.

### 4.1.1 Family Graph and Roles
A graph service captures members, dependents, caregivers, power-of-attorney delegates, and trusted professionals. Edges encode legal authority, consent scopes, oversight rules, and temporal validity. Role templates (primary steward, co-steward, guardian, teen, elder, assistant, professional advisor) drive entitlement bundles, approval matrices, channel privileges, and notification routes. The graph memory records all changes with provenance, enabling regulators to trace why an individual had certain rights at any time.

### 4.1.2 Individual vs Household Contexts
Every event, document, feature, and workflow maintains both household and member context. Agents evaluate actions by intersecting household objectives (cashflow runway, risk posture, goal priorities) with member entitlements (limits, persona, consent tokens). This dual-context model enables personalized experiences without duplicating data or undermining joint decision-making; a teen receives spend nudges while parents see consolidated obligation calendars, yet all operate on the same underlying state vectors.

## 4.2 Agents as First-Class Applications
Agents are modular, policy-bound services that interpret memory, exchange context via IPC/IAC, and emit verifiable outputs. Each agent declares required inputs, decision contracts, guardrail hooks, and observable telemetry. They can be bank-built, vendor-built, or partner-built, but all must run inside the FFOS governance perimeter, respect consent scopes, and log decisions back into core memory for audit.

### 4.2.1 Do, Think, Orchestrator, and Governance Agents
- **Do Agents** convert instructions into atomic executions (payments, transfers, product requests, document submissions) with pre/post validations and compensation hooks.
- **Think Agents** analyze memory, feature vectors, and risk signals to generate advice, alerts, or parameterized workflows, returning explainability payloads for audit and RM consumption.
- **Orchestrator Agents** compose multi-step flows, persist intermediate state in workflow memory, and coordinate do/think/governance agents through IPC topics with deterministic state transitions.
- **Governance Agents** enforce policy, capture approvals, trigger external I/O for escalations, and log audit artifacts; they mediate all high-risk actions and maintain separation-of-duty evidence.

## 4.3 FFOS as a Continuous Operating Environment
FFOS is always-on. Event and timeline services ingest signals from core banking, payments, CRM, external billers, and partner ecosystems. Foundation agents consume these events, update core/graph memories and the feature store in near real time, and publish refreshed state vectors. Experience agents subscribe to relevant topics, maintain durable contexts, and act through workflows or channel prompts. Shared services—identity, consent, guardrails, workflow, document management, IPC, external I/O—are uniformly available, ensuring consistent behaviour regardless of channel, time of day, or initiating persona. This continuous environment enables proactive interventions (e.g., cashflow stress), orchestrated obligations, and RM-assisted journeys without rehydrating context manually.
