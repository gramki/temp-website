# Agent Authority Controls in Seer: Capabilities Status

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-11

---

## Authority Ceilings

### Layered Ceiling Architecture
- ❌ Bank/Organization Policy ceilings (highest level)
- ❌ Agent Class Ceiling (Training Spec)
- ❌ Agent Instance Ceiling (Employment Spec)
- ❌ Request Context Ceiling (runtime)
- ❌ Ceiling immutability principle (training cannot be relaxed at employment)

### Ceiling Types
- ❌ Value ceilings (maxSingleTransaction, maxDailyTotal, maxPerCustomer)
- ❌ Rate ceilings (maxRequestsPerMinute, maxDecisionsPerHour, maxActionsPerDay)
- ❌ Scope ceilings (customerTiers, dataClasses, regions)
- ❌ Approval ceilings (threshold-based, always-required)

### Ceiling Enforcement
- ✅ Runtime enforcement via Policy Enforcement Points (PEPs) - `authority-enforcement.md` §Enforcement Points
- ✅ OPA policy-based ceiling evaluation - `authority-enforcement.md` §OPA Policy Model
- ❌ Audit logging of all ceiling evaluations
- ❌ Ceiling governance and change control

---

## Delegation Chains

### Delegation Models
- ❌ User delegation (agent acts as delegate of specific user)
- ✅ Role delegation (agent represents organizational role) - `authority-enforcement.md` §Integration with IAM §Role Delegation
- ❌ Multi-agent delegation (agents delegating to other agents)

### Authority Inheritance
- ❌ Real-time authority inheritance (agent authority shrinks with delegator)
- ❌ Authority narrowing (each link can only narrow, never expand)
- ❌ Delegation depth limits

### Delegation Governance
- ❌ Delegation audit trail (who, what, when, constraints)
- ❌ Chain verification (full delegation chain traceable)
- ❌ Approval workflows for high-risk delegations
- ❌ Time-bounded delegations
- ❌ Scope-restricted delegations (workbench, scenarios, customers)

---

## Kill Switches

### Kill Switch Functionality
- ❌ Authority revocation (not just process termination)
- ❌ Immediate policy update in Cipher IAM
- ❌ PEP enforcement (all Policy Enforcement Points reject immediately)
- ❌ Token invalidation (all outstanding tokens invalidated)
- ❌ Audit recording in CAF

### Kill Switch Scope
- ❌ Agent instance level
- ❌ Agent class level (all instances of agent type)
- ❌ Workbench level (all agents in workbench)
- ❌ Tenant level (all agents for tenant)
- ❌ Platform level (emergency only)

### Kill Switch Triggers
- ❌ Manual activation (authorized roles)
- ❌ Automated triggers (cost anomaly, security alert, regulatory order)

### Kill Switch Controls
- ❌ Activation channels (UI, CLI, API, Watch alerts)
- ❌ Authorization (ARE, Security Team, Manager, Platform Admin)
- ❌ Confirmation requirements (non-emergency)
- ❌ In-flight operation handling

### Kill Switch Governance
- ❌ Full audit trail of activations
- ❌ Recovery process (with approvals)
- ❌ Post-mortem processes
- ✅ API endpoints (activate, bulk by filter) - `agent-lifecycle-api.md` §Kill Switch

---

## Authority Enforcement

### Enforcement Points
- ✅ Sidecar Guardrails (tenant-defined, custom logic) - `authority-enforcement.md` §Enforcement Points §1. Sidecar Guardrails
- ✅ Tool Gateway (primary enforcement for tool invocations) - `authority-enforcement.md` §Enforcement Points §2. Tool Gateway
- ✅ Signal Exchange (policies on all agent updates) - `authority-enforcement.md` §Enforcement Points §3. Signal Exchange

### OPA Policy Model
- ✅ Policy definition in Training and Employment Specs - `authority-enforcement.md` §OPA Policy Model §Policy Definition
- ✅ Employment Spec override of Training Spec policies - `authority-enforcement.md` §OPA Policy Model §Employment Override
- ✅ OPA decision types (ALLOW, ALERT, REJECT) - `authority-enforcement.md` §OPA Policy Model §OPA Decision Format
- ✅ OPA context schema (AgentContext, AccessContext, ToolGatewayContext, SignalExchangeContext) - `authority-enforcement.md` §OPA Context Schema

### Policy Sources
- ✅ Tool Specification policies (per-tool defaults) - `authority-enforcement.md` §Enforcement Points §2. Tool Gateway §Policy Sources
- ✅ Training Specification policies (per-agent type) - `authority-enforcement.md` §Enforcement Points §2. Tool Gateway §Policy Sources
- ✅ Employment Specification policies (per-deployment, overrides training) - `authority-enforcement.md` §Enforcement Points §2. Tool Gateway §Policy Sources

### Violation Handling
- ✅ Violation recording on Request - `authority-enforcement.md` §Violation Handling §Recording
- ✅ Notification to observers, accountable person, workbench - `authority-enforcement.md` §Violation Handling §Notification
- ✅ Corrective actions (escalation, reassignment, intervention) - `authority-enforcement.md` §Violation Handling §Corrective Actions

### Compound Agents
- ✅ Enforcement scoped to outer agent only - `authority-enforcement.md` §Compound Agents
- ✅ Sub-agent actions attributed to outer agent - `authority-enforcement.md` §Compound Agents

---

## IAM Integration

### Role Delegation
- ✅ IAM role assignment in Employment Spec - `authority-enforcement.md` §Integration with IAM §Role Delegation
- ✅ Delegated scopes configuration - `authority-enforcement.md` §Integration with IAM §Role Delegation
- ✅ Accountable user designation - `authority-enforcement.md` §Integration with IAM §Role Delegation

### Scope Validation
- ✅ Tool Gateway scope validation - `authority-enforcement.md` §Integration with IAM §Scope Validation
- ✅ OPA policies for scope validation - `authority-enforcement.md` §Integration with IAM §Scope Validation

---

## Guardrails (Authority-Related)

### Behavioral Guidelines
- ✅ Prompt-based behavioral guidelines (advisory) - `guardrails.md` §Guardrail Types §Behavioral Guidelines (Prompt-Based)
- ✅ Verification pattern (pairing with sidecar enforcement) - `guardrails.md` §Guardrail Types §Behavioral Guidelines (Prompt-Based) §Verification Pattern

### Sidecar Guardrails
- ✅ Before guardrails (transform, reject, add context) - `guardrails.md` §Sidecar Guardrails
- ✅ After guardrails (transform response, reject, redact) - `guardrails.md` §Sidecar Guardrails
- ✅ Execution order (Training Spec first, then Employment Spec) - `guardrails.md` §Execution Order
- ✅ Training Spec guardrails (immutable) - `guardrails.md` §Execution Order
- ✅ Employment Spec guardrails (additional restrictions) - `guardrails.md` §Execution Order

---

## Observability & Metrics

### Authority Metrics
- ✅ Authority evaluation metrics (total, by decision type) - `authority-enforcement.md` §Observability §Metrics
- ✅ Violation metrics (by policy, by agent) - `authority-enforcement.md` §Observability §Metrics

### Dashboards
- ✅ Workbench Observations (violation timeline, top violating agents, policy effectiveness) - `authority-enforcement.md` §Observability §Dashboards

---

## Not Yet Documented (Required)

### Authority Controls
- ❌ Dynamic authority adjustment (runtime authority modification without redeployment)
- ❌ Authority delegation approval workflows (multi-step approval for delegations)
- ❌ Authority expiration and renewal (automatic expiration with renewal workflows)
- ❌ Authority testing framework (test authority policies before deployment)
- ❌ Authority simulation (what-if analysis for authority changes)

### Kill Switch Enhancements
- ❌ Kill switch rollback (undo recent kill switch activation)
- ❌ Kill switch scheduling (scheduled activation/deactivation)
- ❌ Kill switch dependencies (cascade kill switch to dependent agents)

### Delegation Enhancements
- ❌ Delegation templates (reusable delegation patterns)
- ❌ Delegation analytics (usage patterns, effectiveness metrics)
- ❌ Delegation compliance checks (verify delegations meet policy requirements)

### Integration Gaps
- ❌ Authority controls UI (visual interface for managing authority)
- ❌ Authority controls API completeness (all operations via API)
- ❌ Authority controls CLI (command-line interface for operations)

### Documentation Standards
- ❌ Persona-based documentation (all capabilities documented from perspective of defined personas: APO, CSA, AE, KMO, ARE, COS, ARAO, and SRE personas) - Reference: `olympus-seer-docs/seer-design/personas-and-needs/roles.md`
- ❌ Persona-specific use cases and examples for each capability
- ❌ Persona journey integration (how authority controls support each persona's journey)

---

## Document References

### Seer Design References
- `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md` - Authority enforcement architecture and OPA policies
- `olympus-seer-docs/seer-design/subsystems/guardrails.md` - Guardrails (behavioral and sidecar)
- `olympus-seer-docs/seer-design/subsystems/agent-lifecycle-api.md` - Kill switch API endpoints

### Hub Design References
- `olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md` - ADR on authority enforcement via OPA
