# Fraud Case Resolution Agent (story for engineers)

> **Audience:** engineers building a production “fraud case resolution” agent  
> **Goal:** show how to design the agent using **Enterprise Knowledge**, **Enterprise Memory**, **Operational Data Stores**, and **Agent Memory** together—without confusing storage with cognition.

## 1) The scenario (what the agent is for)

**Job:** given an existing (or newly opened) fraud case, the agent helps drive it to resolution:

- collect/validate evidence
- propose actions (e.g., freeze, step-up auth, reimburse/deny, file SAR referral, escalate)
- execute *allowed* steps via tools
- document the outcome with audit-grade rationale

**Key constraint:** this is not “fraud scoring.” It’s **case resolution**: decisions + actions + documentation under governance.

## 2) Inputs by cognitive role (don’t start with “which database”)

### 2.1 Enterprise Knowledge (normative: what must be true/required)

**Question:** *“What is required/permitted?”*

Typical knowledge-of-record inputs:

- fraud policy (thresholds, mandatory step-up conditions, reimbursement rules)
- jurisdiction/regulatory obligations (timelines, disclosures, reporting triggers)
- reason-code taxonomy and definitions (what “Account Takeover” means, etc.)
- approved SOPs/runbooks for specific fraud categories
- tool allowlists and action policies (what this agent is authorized to do)

**Rule:** if it must **constrain behavior**, it must live here (owned, versioned, approved).

### 2.2 Operational Data Stores (state/events: what the systems say happened)

**Question:** *“What is the current operational state and event history?”*

Typical OLTP inputs:

- case management system state (status, SLA, assigned queue/owner)
- transaction ledger + auth history (what happened)
- customer/account state (balances, limits, flags, KYC status)
- device and session telemetry (device fingerprint results)
- vendor responses (risk signals, watchlist hits, 3DS/step-up outcomes)

**Caution:** OLTP is authoritative for *state*, not for *why*.

### 2.3 Enterprise Memory (institutional: what happened before and why)

**Question:** *“What precedents/outcomes/exceptions matter?”*

Typical enterprise memory inputs:

- prior overrides for similar cases (with outcomes and rationale)
- prior disputes/chargebacks patterns for customer/merchant segment
- incident timelines (e.g., “vendor X degraded last week”)
- learned patterns/hypotheses (semantic enterprise memory) that are **informative** until promoted

### 2.4 Agent Memory (local/tactical: what I’m doing now)

**Question:** *“Given what I’ve experienced in this session/workflow, how should I act now?”*

- working state (which tools were called, what’s pending)
- short-lived scratchpad hypotheses for this case
- procedural agent memory: reusable, policy-gated workflows/tool chains
- (optional) operator preferences (format/tone) — never overrides policy

## 3) The agent’s contract (what it must output)

Every run should produce (at minimum):

- **Proposed action**: approve/deny/reimburse/freeze/step-up/escalate/etc.
- **Action plan**: concrete next steps + which tools will be invoked
- **Evidence bundle**: what facts were used and where they came from (provenance)
- **Rationale**: policy references + how evidence satisfied them
- **Risk flags**: uncertainty, missing evidence, or conflicts

## 4) Context compiler recipe (how the agent “thinks” safely)

Use a compiled context frame (see `agent-memory/context-building.md`), not “paste everything.”

Recommended precedence baseline:

> system policy > procedural allowlist > asserted enterprise knowledge > verified operational state > enterprise memory > agent memory/preferences

**Context frame (suggested):**

1. **Constraints** (tool allowlists, safety rules, escalation rules)
2. **Goal / definition of done** (resolve case to a specific state + artifacts written)
3. **Ground truth facts** (verified OLTP facts; cite sources)
4. **Relevant precedent** (enterprise memory summaries + pointers)
5. **Applicable procedures** (approved SOP/runbook + agent procedure)
6. **Working state** (tool outputs, partial progress)

## 5) Tools and actions (make it safe to act)

Before building the agent, you should have a crisp tool catalog with:

- **Tool schemas** (inputs/outputs, error modes)
- **Authorization model** (agent identity vs user-on-behalf-of)
- **Preconditions** (required evidence, required case state)
- **Postconditions** (what must be written to memory/case system)
- **Idempotency** (prevent double-freeze / double-refund)
- **Human-in-the-loop** checkpoints for high-impact actions

## 6) What the agent writes (enterprise memory artifacts)

Design these artifacts first; they are the backbone of auditability and learning.

- **DecisionRecord**
  - decision, timestamp, actor (agent/human), policy references
  - evidence links, confidence/uncertainty, alternatives considered
- **OverrideRecord**
  - what was overridden, by whom, why, and outcome
  - explicit link to the original DecisionRecord
- **IncidentTimeline**
  - sequence of events across systems/agents/humans (especially during outages/model degradation)
- **HypothesisRecord** (semantic enterprise memory)
  - learned pattern statement + scope + confidence + supporting/counter evidence
  - explicit review cadence; promotable only via governance

## 7) Failure modes to design against (fraud-case specific)

- **Policy laundering**: repeated decisions become “rule” without explicit promotion
- **Vendor output = truth**: treat vendor signals as evidence with confidence; policy decides required corroboration
- **No provenance**: can’t explain why a case was resolved a certain way
- **Action without state checks**: acting on stale case state (race conditions)
- **Unbounded memory**: retaining full transcripts instead of structured summaries + TTL
- **Prompt injection via case notes**: treat retrieved notes/memory as untrusted input

## 8) Minimal end-to-end walkthrough (one case)

1. **Start**
   - Input: `case_id`
   - Goal: “resolve to {approved remediation or escalation} and write DecisionRecord”
2. **Compile constraints**
   - policy gates, jurisdiction, tool allowlists for this case type
3. **Fetch operational state**
   - case status, transaction facts, account flags, vendor results
4. **Retrieve precedent**
   - similar overrides/outcomes; relevant incident notes; segment patterns
5. **Select procedure**
   - approved SOP + (optional) agent procedure (tool chain), policy-gated
6. **Decide / act**
   - propose action; run allowed tools; checkpoint if high-risk
7. **Write artifacts**
   - DecisionRecord (+ OverrideRecord if applicable) + update case system
8. **Post-run**
   - log provenance/context assembly
   - trigger consolidation jobs (optional) for HypothesisRecord candidates

## 9) What I’d want defined before coding

- The **policy-of-record** location and versioning rules (and test fixtures)
- The **case system API** contract and state machine (allowed transitions)
- The **tool allowlist** + approval/override workflow
- The concrete **memory artifact schemas** (Decision/Override/Timeline/Hypothesis)
- Retention + deletion semantics (PII, legal hold)
- Observability requirements (what must be logged and who can see it)

## Related docs (in this folder)

- Canonical cognitive model: [`../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge-memory-other-data.md`](../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge-memory-other-data.md)
- Applied guide: [`../../olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md`](../../olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md)
- Context compiler mechanics: [`../../olympus-seer-docs/agentic-ai-concepts/agent-memory/context-building.md`](../../olympus-seer-docs/agentic-ai-concepts/agent-memory/context-building.md)
- Agent memory governance: [`../../olympus-seer-docs/agentic-ai-concepts/agent-memory/governance.md`](../../olympus-seer-docs/agentic-ai-concepts/agent-memory/governance.md)
- Enterprise knowledge lifecycle: [`../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/lifecycle-and-management.md`](../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/lifecycle-and-management.md)
- Derived artifacts vs signals: [`../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/derived-artifacts-and-signals.md`](../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/derived-artifacts-and-signals.md)


