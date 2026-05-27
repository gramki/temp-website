# Designing an Agent (Enterprise Knowledge + Memory + Operational Data + Agent Memory)

> **Audience:** AI engineers and architects building production agents  
> **Goal:** Teach a practical way to design agents that use **Enterprise Knowledge**, **Enterprise Memory**, **Operational Data Stores**, and **Agent Memory** *together* — without confusing “where data lives” for “what it means cognitively.”

## The core coaching principle

> **Classify information by its cognitive role, not by the storage system or the colloquial word people use.**

The same database can hold multiple cognitive categories. A “knowledge base” can contain content that is not knowledge-of-record. A warehouse can store facts that are *derived artifacts*, not institutional memory.

See also:

- Cognitive classification and vocabulary mapping: [./enterprise-knowledge-memory-other-data.md](./enterprise-knowledge-memory-other-data.md)
- Enterprise Memory types: [./enterprise-memory/README.md](./enterprise-memory/README.md)
- Enterprise Knowledge types: [./enterprise-knowledge/README.md](./enterprise-knowledge/README.md)
- Agent context compiler mechanics: [./agent-memory/context-building.md](./agent-memory/context-building.md)
- Worked example story (fraud case resolution): [../../olympus-hub-docs/aosm-and-hub/fraud-case-resolution-agent.md](../../olympus-hub-docs/aosm-and-hub/fraud-case-resolution-agent.md)

## Where this doc fits (so you don’t read the wrong thing)

- **This doc** is the applied “coach” guide: how to use all sources together in context compilation with worked examples.
- **Canonical conceptual model** (definitions, “storage ≠ cognition”, vocabulary mapping): [./enterprise-knowledge-memory-other-data.md](./enterprise-knowledge-memory-other-data.md)
- **Operational handbooks**: [./enterprise-memory/README.md](./enterprise-memory/README.md), [./enterprise-knowledge/README.md](./enterprise-knowledge/README.md), [./agent-memory/README.md](./agent-memory/README.md)

---

## 1) The four sources you will use (and what question each answers)

### Enterprise Knowledge (normative)

- **Question**: *“What is true / correct / required?”*
- **Examples**: policies, rules, regulatory obligations, definitions, reference data
- **Where it should live**: governed knowledge layer (docs, knowledge graph, knowledge services)

### Enterprise Memory (institutional, experiential)

- **Question**: *“What happened and why, and what did we learn from it?”*
- **Examples**: decision records, override histories, incident timelines, outcome records
- **Where it should live**: memory services / case systems / audit stores (append-only + provenance)

### Operational Data Stores (business applications / OLTP)

- **Question**: *“What is the current operational state and event history?”*
- **Examples**: payments ledger, case management DB, ticketing system, CRM, KYC vendor results
- **Key caution**: authority for operational state ≠ knowledge or memory by default

### Agent Memory (local, tactical)

- **Question**: *“Given what I’ve experienced, how should I act now?”*
- **Examples**: short-term state, user preferences, tool usage outcomes, agent-local procedures
- **Key caution**: agent memory is not enterprise truth; it must not silently become policy

---

## 2) The context compilation recipe (use this every time)

Use a context compiler, not “paste everything into the prompt”.

Minimal pipeline (expanded in [./agent-memory/context-building.md](./agent-memory/context-building.md)):

1. **Clarify the goal** (decision + required output)
2. **Select sources by type** (knowledge, enterprise memory, operational, agent memory)
3. **Retrieve candidates**
4. **Filter + dedupe**
5. **Resolve conflicts** (policy precedence, freshness, confidence)
6. **Token budget by section**
7. **Assemble a structured frame**
8. **Log provenance** (what was included and why)

Recommended precedence (coaching baseline):

> system policy > procedural allowlist > asserted enterprise knowledge > verified operational state > enterprise memory > agent memory/preferences

---

## 3) Common anti-patterns (learn these once; you’ll avoid months of pain)

- **Storage = cognition**: “it’s in the warehouse, so it’s knowledge”
- **RAG = memory**: retrieval results are knowledge access, not memory management
- **Top‑K chunks = memory**: unstable prompts, no provenance, high token cost
- **Policy laundering**: repeated decisions silently become “rules” without governance
- **Agent memory becomes enterprise truth**: a local preference overrides binding constraints
- **Pointing agents at raw OLTP/logs**: no semantics, no rationale, no audit trail

---

## 4) Worked examples (with sources + anti-patterns)

Each example includes:

- **What the agent is trying to do**
- **What to retrieve (by category)**
- **Where it comes from (storage)**
- **What to put into context**
- **Anti-patterns to watch for**

### Example A — Transaction fraud decisioning agent (approve/decline/step-up/review)

**Goal**: decide action for a payment and generate an explanation suitable for an analyst + customer support.

**Enterprise Knowledge (normative)**

- fraud policy thresholds, regulatory constraints (e.g., required step-up for certain conditions)
- definition of risk scores and reason codes
- approved playbooks for escalation

**Enterprise Memory (institutional)**

- historical override records for similar cases (what was overridden and outcomes)
- prior disputes on the customer/merchant and their resolutions
- incident notes if fraud models were degraded recently

**Operational data stores (OLTP)**

- transaction attributes from payments system
- account status from core banking
- device fingerprint outcomes from fraud vendor
- current case state from case management (if already under review)

**Agent memory (local)**

- “this analyst prefers concise bullets” (if you have a human-in-the-loop UI)
- tool-call success/failure patterns (vendor API flakiness)
- current step state (“we already queried vendor X”)

**Context frame (what you compile)**

- Constraints: must-follow policies + tool allowlists
- Goal: choose action and produce explanation
- Ground truth facts: transaction + account state + vendor results (with provenance)
- Relevant episodes: last 2–3 similar overrides + outcomes (summarized)
- Preferences: analyst formatting preference (if applicable)
- Procedure: “fraud decision workflow vN” steps for review/escalation
- Working state: tool outputs, pending calls

**Anti-patterns**

- **Treating risk score as knowledge**: the score is a derived artifact/signal; policy defines how it constrains action.
- **Using warehouse aggregates as “memory”**: aggregates are useful but don’t preserve rationale; link to decision/override records for explainability.
- **Letting analyst preferences override policy**: preferences can change formatting, not decision constraints.

---

### Example B — Dispute handling agent (card dispute intake → investigation → resolution)

**Goal**: guide intake, gather evidence, route correctly, and draft a decision memo.

**Enterprise Knowledge**

- dispute policy: eligibility, timelines, burden of proof
- SOP: required evidence bundle content and steps
- reference data: dispute reason code taxonomy

**Enterprise Memory**

- past disputes for this customer/merchant (outcomes, rationale)
- exceptions previously granted (and why)
- postmortems for common failure patterns (e.g., merchant category edge cases)

**Operational data stores**

- transaction ledger records and settlement status
- CRM interaction history (complaints, prior concessions)
- ticketing/case management state and SLAs

**Agent memory**

- session state and what documents have already been requested
- preferred communication style for this customer segment (if explicitly configured)

**Anti-patterns**

- **Treating CRM notes as enterprise knowledge**: they are episodic signals; use them as context, not binding truth.
- **Storing case rationale only in chat transcripts**: capture structured decision records into enterprise memory for audit.

---

### Example C — Production incident response agent (SRE assistant)

**Goal**: triage an incident, propose mitigations, and document the decision trail.

**Enterprise Knowledge**

- incident response policy (severity definitions, comms requirements)
- runbooks for known failure modes
- service ownership and escalation matrix

**Enterprise Memory**

- prior incident timelines + what fixed them
- exceptions/overrides applied during past incidents (and outcomes)
- known “gotchas” learned over time (semantic memory) that were validated and promoted

**Operational data stores**

- observability data (logs, traces, metrics)
- deployment history and feature flags
- current service status and dependency graph

**Agent memory**

- working hypotheses and which mitigations were tried in this incident
- short-term scratchpad notes for the current investigation

**Anti-patterns**

- **Logs as memory**: logs are raw experience; institutional memory requires narrative structure and decision linkage.
- **Runbooks stored as untyped notes**: procedures must be versioned and approved (procedural knowledge), with drift detection via memory.

---

### Example D — Customer onboarding / KYC agent (human-in-the-loop)

**Goal**: complete onboarding while meeting KYC/AML requirements and minimizing unnecessary friction.

**Enterprise Knowledge**

- KYC/AML policy and jurisdiction rules
- definitions (what “beneficial owner” means)
- reference data: sanctioned country codes, document types

**Enterprise Memory**

- historical exceptions granted in similar edge cases (and which evidence was accepted)
- outcomes of escalations (how long they took; why they were approved/denied)

**Operational data stores**

- onboarding workflow state
- KYC vendor responses and document verification results
- customer-provided docs and metadata

**Agent memory**

- what has already been asked of the customer
- per-channel messaging constraints (SMS vs email)

**Anti-patterns**

- **Preference as policy**: “we usually let this pass” must not override binding AML requirements.
- **Vendor outputs as truth**: treat them as evidence with confidence; policies decide required corroboration.

---

## 5) Design checklist (use before you ship)

- Have you explicitly listed what inputs are **knowledge vs memory vs operational vs agent-local**?
- Do you have a **context frame** with separate sections (constraints/facts/episodes/preferences/procedures)?
- Do you record **provenance** for every retrieved item used in a decision?
- Do you have a promotion path: **enterprise memory → enterprise knowledge** (governed)?
- Have you named anti-patterns you are actively preventing (and how)?

---

## 6) Where these concepts live in this repo

- Enterprise Memory: [./enterprise-memory/README.md](./enterprise-memory/README.md)
- Agent Memory and context compiler: [./agent-memory/README.md](./agent-memory/README.md)
- Enterprise Knowledge: [./enterprise-knowledge/README.md](./enterprise-knowledge/README.md)
- Cognitive classification + “storage ≠ cognition”: [./enterprise-knowledge-memory-other-data.md](./enterprise-knowledge-memory-other-data.md)

