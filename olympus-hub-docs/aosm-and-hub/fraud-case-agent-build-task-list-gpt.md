# Fraud Case Resolution Agent — Build Task List (Hub + Seer)

> **Audience:** engineers building a production fraud-case-resolution agent  
> **Goal:** a practical task breakdown with an approach per task, mapped to **Hub vs Seer**, including **confidence** and explicit **gaps** where the design docs are incomplete/stubs.
>
> **Note (2026-01-08):** This is a historical planning document. References to `hub-enterprise-memory.md` and `hub-agent-memory.md` refer to files that have been superseded:
> - `hub-enterprise-memory.md` → `enterprise-memory/README.md`
> - `hub-agent-memory.md` → `agent-memory/README.md`
> 
> Many gaps identified here have been resolved. See [GAPS.TODO](./GAPS.TODO) for current status.

## 0) Inputs / anchor docs used

- Story: `./fraud-case-resolution-agent.md`
- Seer: `../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md` (placeholder but has the ownership split)
- Hub:
  - Knowledge Services / Knowledge Bank: `../../olympus-hub-docs/04-subsystems/knowledge-services/README.md`, `../../olympus-hub-docs/02-system-design/implementation-concepts/knowledge-bank.md`
  - Memory Services / Agent & Enterprise Memory: `../../olympus-hub-docs/04-subsystems/memory-services/README.md`, `../../olympus-hub-docs/04-subsystems/memory-services/hub-agent-memory.md`, `../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md`
  - CAF: `../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md`, `../../olympus-hub-docs/decision-logs/0029-caf-control-plane.md`, `../../olympus-hub-docs/04-subsystems/cognitive-audit-fabric/decision-records.md`, `../../olympus-hub-docs/04-subsystems/cognitive-audit-fabric/evidence-bundles.md`

## 1) Quick framing (what we are actually building)

**Fraud case resolution** ≠ fraud scoring. This agent drives a fraud *case* to resolution:

- compiles decision context (knowledge + memory + state)
- proposes decisions and (when allowed) executes actions via tools
- always writes audit-grade artifacts: **DecisionRecord** + **EvidenceBundle** (and optional Override/Outcome/Handoff)

## 2) Task breakdown (engineer checklist)

Each task includes:

- **Owner**: Hub / Seer / Both / External system
- **Approach**: how to do it using the current Hub+Seer design
- **Confidence**: High / Medium / Low (based on doc completeness)
- **Gaps**: what we still need defined if unclear

---

### Phase A — Define the product contract and guardrails (before any coding)

#### A1. Define agent scope, authority, and “definition of done”
- **Owner**: Both (product + platform)
- **Approach**:
  - Define the agent’s allowed outcomes and actions: e.g., “freeze account”, “step-up auth”, “escalate to analyst”, “deny reimbursement”, etc.
  - Classify each action into risk tiers and required approvals (human-in-loop for high-risk).
  - Encode this as policy constraints that the context compiler always includes.
- **Confidence**: Medium
- **Gaps**:
  - A concrete policy/authorization model doc for “who can an agent act for?” and “how approvals are represented” in Hub.

#### A2. Define the required outputs per run (agent contract)
- **Owner**: Both
- **Approach**:
  - Standardize the output schema: ProposedAction, ActionPlan, EvidenceBundleRef, Rationale, RiskFlags.
  - Map it to CAF artifacts: DecisionRecord must reference an EvidenceBundle and a ContextSnapshot.
  - Treat any tool execution as producing an audit trail entry + linking to the DecisionRecord.
- **Confidence**: High (CAF decision record / evidence bundle schemas are defined)
- **Gaps**:
  - Where “ContextSnapshot” is stored and how it is referenced (CAF mentions it, but the storage/ID contract is not fully specified).

---

### Phase B — Set up knowledge-of-record (Enterprise Knowledge via Hub)

#### B1. Identify the knowledge-of-record sources for fraud resolution
- **Owner**: Hub application team + Process Architect
- **Approach**:
  - List authoritative artifacts: fraud policies, reimbursement rules, escalation SOPs, reason-code taxonomy, regulatory constraints.
  - Ensure each has: owner, scope (tenant/workbench), version/effective dates.
  - Put curated docs into Knowledge Bank (RAG) where appropriate; keep structured policy/rules in structured stores if available.
- **Confidence**: Medium
- **Gaps**:
  - Which knowledge types are expected to be “structured APIs” vs “docs in Knowledge Bank” for early versions.

#### B2. Configure a Knowledge Bank for the fraud workbench
- **Owner**: Hub (Knowledge Bank)
- **Approach**:
  - Create a Knowledge Bank config similar to the example in Hub docs (`KnowledgeBankConfig`) but scoped to `fraud-ops-<env>`.
  - Define chunking strategy per doc type (SOP vs policy vs compliance).
  - Require consistent tagging for retrieval filtering (fraud_category, jurisdiction, product, etc.).
- **Confidence**: Medium (the concept + config are documented; runtime APIs are stubby)
- **Gaps**:
  - Concrete CLI/API/CRD implementation for Knowledge Bank creation and document ingestion in Hub (docs show examples but the subsystem is marked stub).

#### B3. Define retrieval “filters first” patterns for knowledge
- **Owner**: Seer (context assembly) + Hub (knowledge access layer)
- **Approach**:
  - Use metadata filters (type=policy/sop, jurisdiction=…, fraud_type=…) before semantic search.
  - Prefer small, typed excerpts and citations over raw top‑K chunks.
  - Log retrieved items and scores into the EvidenceBundle.
- **Confidence**: Medium
- **Gaps**:
  - Retrieval API supports for filters + provenance fields (document_id, version, hash, source_url).

---

### Phase C — Define enterprise memory artifacts and storage (Hub Memory Services + CAF)

#### C1. Choose which enterprise memory record types we will write for fraud cases
- **Owner**: Hub (Memory Services) + CAF policy owner
- **Approach**:
  - Use Hub Enterprise Memory categories as baseline:
    - DecisionRecord (CAF schema)
    - EvidenceBundle (CAF schema)
    - OutcomeRecord (post-resolution results)
    - Exception/Override (manual overrides)
    - HandoffContext (agent ↔ analyst transitions)
  - Ensure each record is scoped by tenant, entity_type=`fraud_case`, entity_id=`case_id`.
- **Confidence**: High (categories and base storage model exist in hub-enterprise-memory.md)
- **Gaps**:
  - A canonical enterprise memory schema registry (CAF “catalog”) and how record_type enums are extended.

#### C2. Implement DecisionRecord write at every consequential decision point
- **Owner**: Both (Seer creates it; Hub stores it; CAF governs it)
- **Approach**:
  - In the agent workflow, treat “decision point” as a hard boundary:
    1) compile context
    2) decide
    3) write DecisionRecord immediately (“written at decision time”)
  - Fill fields aligned to CAF schema (`decision_type=fraud_case_resolution`, `entity_id`, `actor_type=ai_agent`, `accountable_party`).
- **Confidence**: Medium
- **Gaps**:
  - Exact API path: does the agent call CAF “record decision” which then writes to Memory Services, or does it write to Memory Services and CAF validates? ADR implies CAF validation happens before storage, but API shape is not specified.

#### C3. Capture EvidenceBundle for each DecisionRecord
- **Owner**: Both (Seer collects; Hub stores; CAF catalogs)
- **Approach**:
  - Capture the *frozen* context at decision time (knowledge retrieval results, enterprise memory retrieval results, agent session state, key OLTP snapshots).
  - Store it in Enterprise Memory with checksums.
  - Link EvidenceBundle → DecisionRecord (and DecisionRecord → EvidenceBundle).
- **Confidence**: Medium
- **Gaps**:
  - The “context_snapshot_id” lifecycle: creation, storage tiering, and replay support are described conceptually but not specified as concrete APIs.

#### C4. Configure retention + archival policies appropriate for fraud cases
- **Owner**: Hub (CAF policy + Memory Services storage)
- **Approach**:
  - Use CAFPolicy to enforce retention per scope:
    - enterprise_memory retention (days/years)
    - audit retention years
  - Align with the Hub Enterprise Memory retention table defaults (Decision/Outcome 7y, Exception 10y, Handoff 1y) unless fraud requires stricter.
- **Confidence**: High (CAFPolicy example exists; retention semantics described)
- **Gaps**:
  - How “legal holds” are represented and enforced (CAF mentions retention manager, but no specific “hold” mechanics here).

---

### Phase D — Define agent memory and session handling (Seer runtime + Hub Agent Memory)

#### D1. Decide what agent memory is allowed for fraud resolution
- **Owner**: Both (policy) + Hub (storage) + Seer (runtime usage)
- **Approach**:
  - Default: keep agent episodic memory short-lived (session + small TTL), and avoid storing raw PII.
  - Use preference memory only if there is a defined operator/human preference model.
  - Keep procedural memory as versioned artifacts, not freeform notes.
- **Confidence**: Medium
- **Gaps**:
  - PII classification + redaction strategy for fraud data in memories (CAF policy talks about pii_detection/anonymization, but no concrete classifier pipeline described).

#### D2. Use Hub Agent Memory for persistence; Seer SDK for retrieval
- **Owner**: Both (Seer SDK + Hub storage)
- **Approach**:
  - Write agent memory via Hub Agent Memory operations (`write/query/search/delete/promote` as per hub-agent-memory.md).
  - Retrieve during context compilation per Seer Context Assembly Engine spec.
- **Confidence**: Medium
- **Gaps**:
  - The actual SDK/API and how authentication/authorization is handled for memory operations.

#### D3. Promotion flows: agent memory → enterprise memory
- **Owner**: Hub (memory services) + CAF policy
- **Approach**:
  - Use `promote` (Hub Agent Memory) to elevate certain artifacts into Enterprise Memory when they become institutional (e.g., handoff context, confirmed outcomes).
  - Keep promotion deliberate and auditable.
- **Confidence**: Low–Medium
- **Gaps**:
  - Promotion criteria and workflow (who approves, what evidence thresholds, where approvals are recorded).

---

### Phase E — Implement context assembly for fraud cases (Seer Context Assembly Engine)

#### E1. Build the “fraud case context frame” and precedence rules
- **Owner**: Seer (context compiler) with Hub inputs
- **Approach**:
  - Implement the structured frame from the story:
    1) Constraints
    2) Goal/DoD
    3) Verified facts (OLTP)
    4) Precedent (Enterprise Memory)
    5) Procedures (SOP + agent procedures)
    6) Working state
  - Enforce precedence per docs: policy > allowlisted procedures > asserted knowledge > verified operational state > enterprise memory > agent memory/preferences.
- **Confidence**: High for conceptual approach; Medium for concrete implementation (Seer doc is placeholder)
- **Gaps**:
  - Concrete “Context Assembly Engine” APIs (retrieval orchestration, ranking, truncation) and how they’re invoked from a Seer agent.

#### E2. Retrieval orchestration: what to pull from Hub and when
- **Owner**: Seer
- **Approach**:
  - Knowledge: query Knowledge Bank by fraud type/jurisdiction and policy tags.
  - Enterprise Memory: query by entity_id=case_id for decisions/outcomes/exceptions/handoffs; optionally semantic-search for “similar cases”.
  - Agent Memory: retrieve session state + procedure candidates.
  - Log all retrieval queries + results into EvidenceBundle (`retrieval.queries/results/rankings`).
- **Confidence**: Medium
- **Gaps**:
  - Query interfaces and “filters + semantic” support for Enterprise Memory search (hub-enterprise-memory.md lists query/search but not parameters).

#### E3. Token budgeting + truncation strategy tuned for fraud
- **Owner**: Seer
- **Approach**:
  - Always include constraints/goal.
  - Prefer structured facts over narrative.
  - Summarize enterprise memory to “decision snippets” with pointers, rather than dumping full records.
  - Keep SOPs as checklists/steps.
- **Confidence**: Medium
- **Gaps**:
  - A standard token budget policy per model and how it’s configured in Seer/Hub.

---

### Phase F — Tooling: safe actions in real systems (Hub tool registry + runtime)

#### F1. Define the tool catalog for fraud resolution
- **Owner**: Hub (tool registry) + external systems owners
- **Approach**:
  - Enumerate tools with schemas and guardrails:
    - get_case(case_id)
    - list_transactions(account_id, window)
    - freeze_account(account_id)
    - step_up_auth(customer_id, method)
    - create_task_for_analyst(case_id, reason)
    - add_case_note(case_id, note_type, content)
  - Add preconditions/postconditions and idempotency keys.
  - Classify each tool call as “audit-required”.
- **Confidence**: Medium
- **Gaps**:
  - The existing Hub tool registry/operator docs were not pulled into this pass; we need the canonical tool registration flow and runtime invocation contract.

#### F2. Enforce policy gates and human-in-loop checkpoints before high-impact tools
- **Owner**: Hub (CAF policy + application policy) + Seer (runtime compliance)
- **Approach**:
  - Encode “tool allowlists” and “approval required” flags into constraints injected into context.
  - For high-risk actions, require an explicit “approval step” (human task) before executing.
  - Log denial/approval into DecisionRecord or separate override/approval record.
- **Confidence**: Medium
- **Gaps**:
  - The canonical representation of approval workflows (task system hooks, queue routing) and how agents request approvals in Hub.

---

### Phase G — Workflow + state machine (cases, tasks, handoffs)

#### G1. Define the fraud case state machine and allowed transitions
- **Owner**: External case system + Hub application
- **Approach**:
  - Document allowed case status transitions (new → investigating → actioned → resolved → closed).
  - Ensure the agent checks current state before acting (race condition prevention).
  - Treat each transition as a “decision point” with DecisionRecord + EvidenceBundle.
- **Confidence**: Medium
- **Gaps**:
  - The specific Hub task/case management integration approach for this scenario (where case state lives; how Hub models it).

#### G2. Handoff context and analyst collaboration
- **Owner**: Hub (Enterprise Memory) + Seer (agent)
- **Approach**:
  - Write HandoffContext record whenever the agent escalates or transfers.
  - Include open items, evidence checklist status, and links to relevant DecisionRecords.
- **Confidence**: High (Enterprise Memory includes Handoff Context as a category)
- **Gaps**:
  - The exact schema and how it ties to Hub task management UI/UX.

---

### Phase H — Observability, audit, replay

#### H1. Ensure every decision is reproducible
- **Owner**: Both (Seer captures; Hub stores; CAF governs)
- **Approach**:
  - EvidenceBundle stores retrieval queries/results + key OLTP snapshots + model prompts/completions where allowed.
  - Record “context compilation log” (why each item was included) to support replay and debugging.
- **Confidence**: Medium
- **Gaps**:
  - How model prompts/completions are stored given privacy constraints; and whether “full prompt storage” is permitted per tenant policy.

#### H2. Implement explanation requests (audit or customer support)
- **Owner**: Hub (CAF explanation service concept) + application
- **Approach**:
  - For any dispute/audit: fetch DecisionRecord + EvidenceBundle and generate an explanation narrative.
  - Keep the explanation separate from the decision record (decision record is immutable; explanation can be regenerated).
- **Confidence**: Medium
- **Gaps**:
  - The actual “Explanation Service” API (it’s referenced but not present in the files reviewed here).

---

### Phase I — Evaluation + safety testing (before production)

#### I1. Build a golden-case suite for fraud case resolution
- **Owner**: Both (product + engineering)
- **Approach**:
  - Collect representative cases (synthetic + redacted real) with expected decisions and required evidence.
  - Include failure cases: vendor outage, contradictory data, policy conflicts.
  - Validate: decision correctness, required artifacts written, tool safety gates, audit completeness.
- **Confidence**: Medium
- **Gaps**:
  - A standard Hub/Seer evaluation harness and how it replays contexts deterministically.

#### I2. Policy tests for knowledge-of-record
- **Owner**: Hub (knowledge) + process owners
- **Approach**:
  - For each policy/SOP version, run test fixtures and store expected outcomes.
  - Gate deployment on passing policy tests (especially for compliance-bound rules).
- **Confidence**: Medium
- **Gaps**:
  - Where these tests live (CI/CD integration) and what “policy test runner” exists in Hub tooling.

---

## 3) Explicit gaps to address (what I need to know / what’s underspecified)

These are the biggest “unknowns” blocking a fully concrete build plan:

1. **Seer Context Assembly Engine APIs** (currently a placeholder)
   - Need: concrete SDK interface for “compile context”, retrieval adapters, ranking, truncation, provenance logging.
2. **CAF ↔ Memory Services write path**
   - Need: exact API sequence for writing DecisionRecords/EvidenceBundles (who calls whom; how schema validation is enforced).
3. **Tool registry + tool execution governance**
   - Need: canonical tool registration flow, runtime invocation contract, and how approvals/human-in-loop are modeled.
4. **Case/task management integration**
   - Need: where the fraud case state machine lives in Hub, how tasks/escalations are represented, and how the agent interacts with them.
5. **PII detection / anonymization pipeline**
   - Need: implementation details for pii_detection/anonymization referenced in CAFPolicy (classifier, redaction semantics, storage strategy).
6. **Explanation Service**
   - Need: the concrete subsystem doc/API for explanation generation and how it consumes DecisionRecords/EvidenceBundles.
7. **Deterministic replay harness**
   - Need: how we replay a decision using stored evidence bundles + fixed retrieval state (and where model nondeterminism is handled).

## 4) Hub + Seer mapping summary (who does what)

- **Seer**
  - agent runtime execution
  - context compilation / orchestration
  - local session state + agent memory retrieval logic
- **Hub**
  - Knowledge Services (Knowledge Bank + access layer)
  - Memory Services (Agent Memory + Enterprise Memory storage)
  - CAF (governance control plane: policies, schemas, audit logs, retention, consent)

## 5) Next step (what we should do after this file)

To proceed from “task list” to “implementable plan”, we should pick 1–2 of the gaps above and resolve them via the corresponding Hub/Seer subsystem docs (or write missing stubs), starting with:

- Seer Context Assembly Engine concrete APIs, and
- CAF+Memory Services write flow for DecisionRecord + EvidenceBundle.


