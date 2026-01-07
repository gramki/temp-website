
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

=======
Agent Memory Services


====
# Personas and UX Architecture
Learning Architect - Congtive Operations Desk
Learning Operations Engineer - Congtive Operations Desk
Enhancements to Steward Desk

