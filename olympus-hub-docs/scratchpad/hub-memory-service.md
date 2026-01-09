
@design-docs/olympus-hub-docs/04-subsystems/cognitive-audit-fabric given the context of caf, let us work on the following:

# Hub — Memory Services:
    ## P1 (High):
        [ ] HUB-MEM-001: Memory Services query API specification — cannot retrieve precedent
        [ ] HUB-MEM-002: Memory indexing and search (semantic + filter) implementation details
        [ ] HUB-MEM-003: Retention and deletion semantics (PII, legal hold) — compliance risk
        [ ] HUB-MEM-004: PII classification + redaction strategy for fraud data — no classifier pipeline
        [ ] HUB-MEM-005: Agent Memory SDK/API and authentication/authorization
    ## P2 (Medium):
        [ ] HUB-MEM-006: Promotion criteria and workflow (memory → ETSL knowledge) — see HUB-CAF-005 Enterprise Learning Services
        [ ] HUB-MEM-007: Unified ESPP taxonomy across Enterprise Memory — Enterprise uses different types than Agent
        [ ] HUB-MEM-008: HandoffContext schema and task management UI/UX integration


--
Hub provides inbuilt memory stores that adhere to CAF expectations. These are concrete implementations. A Tenant Admin can provision these resources using CRDs. Each memory store (logical) created will by default integrate with CAF.

An admin can provision them per workbench upon a developer's request or may delegate the rights to developers. The stores are always scoped to a workbench and are part of the workbench specification. 

The concrete stored provided by hub use Opensearch as the storage engine. It provides CAF-compliant APIs for read and write. In addition, the Hub memory stores provide an Atropos TOPIC per store to write records asynchronously. 

No Hub agent or application need to directly access the write APIs of Hub memory stores. All writes are hub are done by the Signal Exchange using the Atropos API. All agents and applications add all enterprise episodic memory records as updates to request. SX identifies such records and writes to the episodic memory store applicable to the corresponding scenario. Reads are application and agent specific. Each of them can use enterprise memory access 'tools'. How any of them use is specific to their needs and are detailed in their respective contexts. 

No Episodic memory record may have PII. this shoudl have been clarified in caf itself but can be repeated in hub memory stores documentation.

update the memory-services, signal exchange subsystems with this understanding and complete all relevant tasks  

>> Done
=====

# Cogntive Applications
- Not every application built for automation of a scenario is a 'cognitive' application
- Any application that relies that emits 'tasks' is advised to be modelled as a cognitive applicaiton
- A Cognitive application is an application that is capable of compiling the Context required for agents with every relevant update to the request. 
- Agents themselves may compile additional context required for thier role in the request as they neeed. THe context compilation capabilities of application and agent are mutually independent but an agent will very likely rely on the context of the request as compiled by the application to build its specialized context (this of course cannot be enforced and is solely dependent on the specification of the agent)
- Agents (human and ai) and Cognitive applications are expected to emit episodic memory records.
- Human agents are aided by the task solver components to build and emit appropriate memory records.
- All applications and agents must register their memory record schemas in their specifications. 
- Memory record schemas may be registered at workbench scope as well.
- The Schemas registered at Workbench scope or an application scope can be used by agents (Humans and AI)
- SX validates that the updates posted to request adhere to schema. Non-adhering updates are recorded as invalid, but are retained in the request history. 

Write a concept doc about Cognitive Application as a special case of Hub Application in system design. Update all relevant docs about Hub applications. Add references as requried.

Ask me any clarifications you may need.


Let me explore the existing Hub Application documentation to understand the current structure and identify what needs to be updated.

[9 tools called]

I have a good understanding of the existing Hub Application and related documentation. Let me clarify a few points before I proceed:

## Clarifying Questions

### 1. Context Scope
You mentioned "Cognitive Applications compile Context with every relevant update to the request." 

**Question:** Is this Context compiled for:
- **All tasks** emitted by the application for that request? (Request-level context)
- **Each task individually** at the time of task creation? (Task-level context)
- **Both** — a request-level context that is further specialized per task?

> Request level context, is default expectation.
> Task-level context specialization is left to the agents work on the task. An application may not be able to specialize this. But if an application is capable of refining context per task, it can add such context records to request and tag them specifically for a task. However context of all tasks is available for all agents working any task. 

### 2. Context Delivery Mechanism
How is the compiled Context made available to agents?
- Embedded in the **Task payload** when the task is created?
- Stored in a **Request Context Store** that agents query?
- Both?

> Agents can retrieve from request. Any update to context of a request or a task is notified to interested agents.

### 3. Memory Record Schema Registration Hierarchy
You mentioned schemas can be registered at Workbench scope or Application scope. 

**Question:** Is the precedence:
- Application schema > Workbench schema (more specific wins)?
- Or are they disjoint (different schemas registered at different scopes)?

> The schema entities themselves are usually disjoint. In any case, the latest version of the schema wins for any given type. If both Application and Workbench register same version, then the Workbench's definition survives. The corresponding operator howevr would have alerted about conflict.

### 4. Non-Cognitive Hub Applications
For non-cognitive Hub Applications (those that don't emit tasks), do they:
- Still emit memory records? (optional)
- Not interact with Task Management at all?
- Operate as simpler request-response automations?

> They can emit memory records. There is nothing preventing it. But if they did, probably they should have been called cognitive application (recommended). 

### 5. Cognitive Application as Seer-only or Multi-Runtime?
Can Cognitive Applications run on any Automation Runtime, or is this concept primarily associated with **Seer** (AI Case Orchestration)?

> There is no need or mandate that all conginitive applications are based on Seer.
---

Once you clarify these, I'll create:
1. **Concept doc**: `cognitive-application.md` in implementation-concepts
2. **Updates** to `hub-application.md`, Signal Exchange docs, and Memory Services as needed
3. **References** across related documents

> DONE
==== 
# Parent Requests and Child Requests
- When a hub application invokes another scenario in the same workbench as tool or as an agent, then request generated for that scenario is considered as a child request to the request context from which the hub application invoked the scenario.
- The child request can access the 'context' of the parent request (but not the environment of the parent). The SX APIs that provide the compiled-context of a request will include the context of the ancesstors and the current request in the response.
- As with any update, update to context of a request is a request update and will be notified to all observers.
- Scenario invocations across Workbenches do have any implicitly shared context. The invoker should explicitly forward the context as per the contract of the recepient.

Update SX, Request management, composite patterns, and any other subsystems with this information and contracts. 

Ask me any clarifications you may need

--
Let me clarify a few points before documenting:

## Clarifying Questions

### 1. Request Hierarchy Depth
Is there a limit to the nesting depth (parent → child → grandchild → ...)?
- **Unlimited** — any depth allowed?
- **Limited** — e.g., max 3-5 levels?
- **Configurable** — per workbench or scenario?

> No; Practically it shouldn't go beyond 5 levels
> Configurable per Workbench. Violations will cause scenario invocation failure.

### 2. Context Inheritance Model
When a child request accesses parent context, is it:
- **Copy-on-create** — Child gets a snapshot of parent context at creation time?
- **Live reference** — Child sees real-time updates to parent context?
- **Both** — Snapshot at creation + updates are propagated?

> Context record is an immutable record. It is accessed through reference.
> Updates lead to updated context record with a new version

### 3. Child Request Lifecycle
When the parent request completes or is cancelled:
- **Cascade** — Child requests are also completed/cancelled?
- **Independent** — Child requests continue independently?
- **Configurable** — per scenario or invocation?

> Cascade.

### 4. Context Merge in Response
When child request completes and returns to parent:
- Does child's context **merge back** into parent's context?
- Or is child context **isolated** and only the result payload returns?

> child context is isolated. 

### 5. Observability
For observers watching a parent request:
- Do they receive notifications for **child request updates** too?
- Or only updates to the **parent request itself**?

> Observes of a request received updates of that request not of the children or ancestors 

### 6. Cross-Workbench Terminology
For cross-workbench scenario invocations (no implicit context sharing):
- Is this still called "child request"?
- Or is it a different concept (e.g., "external invocation", "delegated request")?

> No, unrelated external machine/tool invocation
---

Once you clarify, I'll update:
- **Signal Exchange** — context inheritance, API responses
- **Request Management** — parent-child lifecycle, request hierarchy
- **Composite Patterns** — scenario-as-tool and scenario-as-agent with context
- **Implementation Concepts** — request lifecycle, possibly new concept doc

------
> DONE

=======
# Agent Memory Services

## Hub's Approach to Agent Memory
Unlike that of Enterprise Memory, Hub doesn't prescribe agent memory managent approaches, but enables agent memory persistence, isolation, retrieval, and lifecycle management with certain guardrails. 

How encourages that 'Raw Agents' be built any framework of choice. The landscape is in its infancy and there is a lot of evolution expected before we collectively learn various that could be deemed as standards or best practices. Hub therefore doesn't push any opinionated appraoches. However, Hub advocates agent developers to recognize the distinction between Enterprise Memory and Agent Memory and employ relevant approach for each of them. 

## Hub provided Agent Memory interfaces have the following characteristics:
- No in-memory stores; Hub Runtimes do not ensure durable execution on same VM. Hub Sessions (Requests) are long-lived. Agents participating in such sessions cannot expect in-memory stores to be reliably available.
- Storage scope is limited to a Request/Session. No accidental enterprise memory like patterns. 
- No user preferences that can last beyond the request scope; User's preferences that should persist across session should rely on enterprise memory systems or operational data stores with business entity semantics.
- Every agent gets its isolated (tenant, workbench, scenario, request, agent) scoped storage. All read/write APIs can't see any higher scope.
- Memory is available as tool (across all supported store types)

- Agent training is encouraged to incorporate memory management skills

## Supported
- Append-only Store - Session and Conversation
- Append-only Store with compaction/decay strategies - Conversation, Conversation Summary, and Token budget
- Key-value Store - Entity extraction, In-session user preferences, etc.,
- Vector DB (RAG) - on documents used in session, session snapshots, etc.,
- User Profile (Request Scoped)

// - User Profile as Business Entity is different from user profile as agent memory

## Not Supported:
- Cross-talk not supported or encouraged at a framework level
- Agent memory stores of Hub are peristence stores; All agents are encouraged to use only those stores. The agent exectuion is stateless and can't rely on affinity to a VM.
- Agent memory activity is not reported to request - no conflation with enterprise memory
- Multi-agent orchestration and agent memory sharing is out of scope. 
- Namespace-Scoped LTM Strategies - LTM goes to Enterprise Memory; Agent memory stores maximum lifespace is the life of Request/Session

## Left to individual frameworks using which Raw Agents are built:
- Preference Learning
- Entity Extraction
- Provenance in Context Compilation
- Multi-agent orchestration -  Requests is the shared context between agents in a Session. However, each agent could be a compound agent with an internal topology of sub-agents. Such sub-agents that may not be visible to Hub as agents are out of Hub's purview. They could access the memory of Hub Agent that spawned if that is how the raw agent is coded.  

## What's available to Agents and their frameworks
Storage Services:
1. Log Service - Append Only messages for Session; Last x and RAG retrieval supported
2. Conversation Service - Append Only messages for Conversation; Configurable compaction strategies per store and per agent with tunable token budgets. Strategies supported include LLM-based summarization.
3. KV Service - For entities, preferences, etc.,
4. Document Storage Service - For CLOBs and BLOBs referenced or exchanged in the session

All of then are available through a SDK and as tools with save and recall operations. Each Service can be accessed by agents with logical store names as well. kv_store.put(<store-name>, <key>, <value>) where store names could be "preferences", "merchant", etc. such business domain relevant logical names. When accessed without store name, the default store-name "." is used. 

with this lets document hub agent memory services. ask any clarification questions

This is very helpful context. Before I document Hub Agent Memory Services, let me ask some clarifying questions:

---

## Clarifying Questions

### 1. Storage Lifecycle and Cleanup
When a Request/Session completes or is cancelled:
- Are agent memory stores **automatically deleted**?
> yes, but after a retention period configured per store by the tenant admin
- Is there a **retention period** after session completion (e.g., for debugging/audit)?
- Can an agent explicitly request **early cleanup** of its memory?
> no; agent can override values

### 2. Store Provisioning
- Are stores **auto-provisioned** per agent on first access?
> Stores provisioned per Workbench by admin (on developer request, likely). 
- Or must an agent **declare** which stores it needs in its specification?
> Yes and at deployment time the requirements are mapped to workbench stores.
- Is there a **quota** per agent or per request for storage?
> yes

### 3. Logical Store Names
You mentioned `kv_store.put(<store-name>, <key>, <value>)` with business-relevant names like "preferences", "merchant".
- Are store names **validated against a schema** or free-form?
free-from, agent local. shouldn't contain PII and shoudld adhere to (a-zA-Z_-)+ regexp pattern in ASCII
- Can agents in the same request **share** a logical store if they use the same name, or are stores strictly isolated per agent?
> isolaged per agent

### 4. Vector DB (RAG) Service
- Is this backed by **OpenSearch/Europa** or a different vector store?
> could different vector store; choice to be made
- How are embeddings generated — **framework-provided** or agent-specified?
> hub framework provided
- Is there a **document size limit** or **embedding count limit** per session?
> both

### 5. Conversation Service Compaction
You mentioned "configurable compaction strategies per store and per agent with tunable token budgets."
- Who configures this — the **agent developer** in agent spec, or **runtime configuration**?
> developer in spec  but can be tuned in deployment CRD 
- Are compaction operations **synchronous** (blocking the agent) or **background**?
> sync, before write

### 6. SDK vs Tool Access
You mentioned both SDK and tool access:
- Is the **SDK for Raw Agent frameworks** (direct API calls)?
- Are **tools for Seer-based agents** (LLM invokes tool)?
- Or are both available to all agents?
> Both available to all

### 7. User Profile (Request Scoped)
- How does this differ from using **KV Store** for user data?
- Is there a **standard schema** for User Profile, or is it free-form?
- Is this populated from **Hub's identity context** or agent-supplied?
Not different. This is just a use-case wrapper, just for familiarity

### 8. Document Storage Service
- How do agents **reference** stored documents in other services (e.g., in conversation)?
> uri provided by document storage service
- Are documents **content-addressable** (hash-based) or **name-based**?
> uri (unique per content hash)
- Is there **virus scanning** or content validation?
> virus and malware scan is perfomed before the content is persisted
> the specific steps and processes are out of scope here

### 9. Cross-Request Agent Identity
You mentioned no cross-session memory for agents. However:
- Does Hub maintain **agent identity** across requests (same agent spec = same agent)?
> Yes
- If an agent needs to "remember" something across requests, is the **only path** to use Enterprise Memory or external business entity stores?
> Yes

Also note that all 'values' are encrypted at application layer before they are persisted. Agent memory is agent-private. Values are not logged and are not reterivable outside the session scope. Encryption keys are unique per agent, per session. The keys are derived from a Workbench scoped root key.

---

Once you clarify these, I'll create a comprehensive document for Hub Agent Memory Services in the `memory-services/agent-memory/` folder.
---
Recommendations from Opus from analysis of frameworks:

> Support typed session state — Like LangGraph and Strands, with explicit schema and JSON serialization
> Provide memory access tools — Like Semantic Kernel, make memory operations observable
/ Implement entity tracking — Automatic extraction and persistence
> Design decay models — Beyond simple windowing
> Separate preference memory — Explicit, not conflated with facts (learn from Strands+AgentCore strategies)
> Enable context assembly — Ranking and budget allocation from memory
> First-class session persistence — Like Strands, automatic save/restore with pluggable backends
> Pluggable conversation management — Like Strands, support windowing and summarization as strategies
/ Multi-agent session support — Like Strands, track orchestrator state and cross-agent context
> Namespace-based scoping — Like AgentCore, isolate memory by actor/session/workbench
----
 Preference memory - Session scope flattens taxonomy value 
There is more to it. Hub agent memory philosphy is to let agents be written in the agent development framework's native/idomatic style and not conflict with their practices. The design of this layer is maximally enabling such framework approaches without compromising on the enterprise memory isolation. Most frameworks do not classify agent memory into ESPP--taxonomy and allow the boundaries blur. While we will advise agent develooers to understand the nuances to achieve appropriate modelling, ultimately the code should be native to the development framework of their choice.  
To effectively articulate this rationale, you can clone @design-docs/olympus-hub-docs/scratchpad/agent-memory-framework-sow.md this analysis into agent-memory subsystem documentation and make relevant references.

ask me any questions you may have
---
Thank you for this important clarification. This articulates a key design principle: **framework-native idiom preservation**. Before I proceed, let me ask a few questions:

---

## Clarifying Questions

### 1. Document Placement

The scratchpad analysis (`agent-memory-framework-sow.md`) is currently ~500 lines. When cloning into agent-memory subsystem:

- **Option A**: Single document in `agent-memory/` (e.g., `framework-analysis.md`)
- **Option B**: Integrated into `design-rationale.md` as a detailed appendix
- **Option C**: Separate folder `agent-memory/framework-reference/` with the analysis + summary

Which approach do you prefer?

### 2. Content Transformation

When moving from scratchpad to formal documentation:

- **Keep as-is**: Preserve the analysis format (comparison tables, per-framework sections)
- **Summarize**: Condense to key patterns and Hub's response to each
- **Hybrid**: Full analysis in appendix, summary in main document

Which approach?

### 3. Cross-References

Should the design-rationale.md:
- **Reference** the framework analysis (as a separate doc)
- **Inline** key patterns with citations
- **Both** — summary inline, detailed reference linked

### 4. Scope Clarification Update

You mentioned "session scope flattens taxonomy value" was incomplete. Should I also update the `shared/espp-taxonomy.md` to clarify:
- ESPP is primarily for Enterprise Memory governance
- Agent Memory may use ESPP concepts but enforcement is optional
- Framework-native memory organization is preferred

### 5. Developer Guidance

Should I create or update a developer-facing guide (perhaps in `10-guides/`) that:
- Explains the ESPP taxonomy conceptually
- Advises on when to use which memory type
- Explicitly states: "Use your framework's idioms; Hub provides storage, not methodology"

---

Once you clarify these, I'll:
1. Move the framework analysis from scratchpad to formal docs
2. Update design-rationale.md with the "framework-native idiom" principle
3. Add appropriate cross-references
4. Update related documents as needed
----
1. C; and reference the analysis or summary in rationale
2. hybrid; retain the depth 
3. reference
4. yes
5. sure, that will help
---------
> DONE
---------
Review 
====
# Personas and UX Architecture
Learning Architect - Congtive Operations Desk
Learning Operations Engineer - Congtive Operations Desk
Enhancements to Steward Desk

