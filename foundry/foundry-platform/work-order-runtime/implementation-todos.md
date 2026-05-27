# Implementation TODOs

This document captures open questions and implementation details needed for a senior engineer to take the WO Runtime and Agent Model architecture to implementation.

## 1. Data Model / Schemas

### Capable Agent Registration Schema

**Questions:**
- What is the exact YAML schema for `capable-agents.yaml` at each level (Foundry/Workshop/Workbench)?
- How are credential references validated at parse time?
- How is the enabled/disabled cascade computed and cached?

**Deliverable:** JSON Schema or TypeScript types for Capable Agent configuration.

### Skilled Agent Definition Schema

**Questions:**
- What is the exact schema for `agent.yaml`?
- How are skill references resolved (relative path vs package name)?
- What guardrail types are supported and how are they validated?
- How are evaluation datasets referenced and versioned?

**Deliverable:** JSON Schema for `agent.yaml` with validation rules.

### Employed Agent Runtime State

**Questions:**
- What state is persisted vs ephemeral for an Employed Agent?
- Is agent memory (conversation history) persisted across task boundaries?
- What state survives a workspace restart?
- How is partial work preserved on crash?

**Deliverable:** State persistence model with clear persistence boundaries.

### Delegation Token Structure

**Questions:**
- What are the exact JWT claims in a Delegation Token?
- What is the signing algorithm and key management?
- What is the token expiry policy (fixed? session-scoped? refreshable)?
- How is token refresh handled mid-execution?

**Deliverable:** JWT spec with all claims, signing requirements, and refresh protocol.

### Task State Representation in Jira

**Questions:**
- What Jira issue types are used (Epic, Story, Sub-task)?
- What custom fields are required (`scenario`, `dependencies`, etc.)?
- How are dependencies represented (linked issues? custom field?)?
- What Jira workflows map to task states?

**Deliverable:** Jira project configuration template with issue types, custom fields, and workflows.

### Task Tree / Dependency Graph

**Questions:**
- How is the task DAG represented in memory?
- How is cycle detection implemented?
- How are cross-WO dependencies handled?
- What is the maximum tree size before performance degrades?

**Deliverable:** Data structure design for in-memory task graph with operations.

---

## 2. APIs / Interfaces

### WO Runtime ↔ Jira MCP Protocol

**Questions:**
- What MCP tools are required for WO Runtime operation?
- What is the authentication model for Jira MCP?
- What is the polling frequency and strategy (polling vs webhook)?
- How are Jira rate limits handled?

**Deliverable:** MCP tool specifications with input/output schemas.

### Task Creation Tool Specification

**Questions:**
- What is the exact tool interface for skills to create tasks?
- How are task templates defined and resolved?
- How are dependencies specified (by key? by semantic reference?)?
- How is scenario association validated?

**Deliverable:** Task creation tool spec with input schema and examples.

### Task Completion Notification Interface

**Questions:**
- How does an agent signal task completion?
- Is it a Jira transition? A WO Runtime API call? Both?
- What metadata is included in completion (verdict, artifacts)?
- How is partial completion signaled?

**Deliverable:** Completion notification protocol spec.

### Orchestrator ↔ Coder Session Activation API

**Questions:**
- What Coder API is used to start/stop workspaces?
- How does Orchestrator authenticate to Coder?
- What is the startup time expectation?
- How are startup failures handled?

**Deliverable:** Coder API integration spec with error handling.

### Orchestrator ↔ WO Runtime Completion Notification API

**Questions:**
- How does WO Runtime notify Orchestrator of completion?
- Is it push (webhook) or pull (polling)?
- What is the payload structure?
- How are retries and failures handled?

**Deliverable:** Completion notification API spec.

### Access Gateway HTTPS API

**Questions:**
- What is the API format? (OpenAI-compatible? Custom?)
- How are different model providers normalized?
- What headers are required (Delegation Token, context)?
- How are streaming responses handled?

**Deliverable:** OpenAPI spec for Access Gateway.

---

## 3. Capable-Agent-Specific Spawning

### Cursor Agent

**Questions:**
- What is the spawn command and arguments?
- How are skills injected (system prompt? rules files?)?
- How is I/O routed (stdin/stdout? IPC?)?
- How is the VS Code integration handled?

**Deliverable:** Cursor Agent spawn specification.

### Copilot

**Questions:**
- What is the spawn mechanism for headless Copilot?
- How is GitHub authentication handled?
- What is the skill injection mechanism?
- How does Copilot report completion?

**Deliverable:** Copilot spawn specification.

### Claude Code

**Questions:**
- What is the CLI invocation for Claude Code?
- How is context provided (files? prompt?)?
- How is the Access Gateway configured as the API endpoint?
- What is the output format?

**Deliverable:** Claude Code spawn specification.

### Codex CLI

**Questions:**
- What is the current Codex CLI interface?
- How is workspace context provided?
- How are long-running executions managed?
- What is the completion signaling mechanism?

**Deliverable:** Codex CLI spawn specification.

### Generic Spawn Interface

**Questions:**
- Can we define a common spawn interface for all agents?
- What are the minimum required capabilities?
- How do we handle agent-specific quirks?

**Deliverable:** Generic spawn interface design.

---

## 4. Lifecycle State Machines

### Workspace Session States

**Questions:**
- What are the exact states (Active, Stopped, Archived, Errored)?
- What triggers transitions?
- What cleanup happens on state transitions?
- How is state persisted?

**Deliverable:** Workspace Session state machine diagram with triggers.

### Task States

**Questions:**
- Are there additional states beyond (Blocked, Ready, In-Progress, Completed, Failed, Cancelled)?
- Can tasks be paused? Resumed?
- How is retry count tracked?
- What is the failed → ready transition policy?

**Deliverable:** Task state machine with all transitions and triggers.

### Work Order States

**Questions:**
- What are WO states beyond the task states?
- Can a WO be completed with failed tasks?
- How is partial completion handled?
- What is the WO archival policy?

**Deliverable:** WO state machine.

### Employed Agent Lifecycle

**Questions:**
- What are agent states (Starting, Active, Waiting, Completed, Failed)?
- What happens when an agent is interrupted?
- How is agent cleanup handled?
- What state survives process restart?

**Deliverable:** Employed Agent lifecycle diagram.

---

## 5. Session Activation Config

### User Configuration Schema

**Questions:**
- What is the exact schema for auto-activation config?
- What trigger patterns are supported?
- How are quiet hours defined (per timezone)?
- Are there notification preferences?

**Deliverable:** User activation config schema.

### Configuration Storage

**Questions:**
- Where is user config stored? (Foundry Management DB? Workshop repo? Jira user properties?)
- How is config accessed by Orchestrator?
- How are changes propagated?

**Deliverable:** Config storage design.

### Rule Matching Logic

**Questions:**
- How are WOs matched against trigger scenarios?
- Is there priority ordering?
- How are wildcards/patterns handled?
- How are conflicting rules resolved?

**Deliverable:** Rule matching algorithm spec.

---

## 6. Error Handling

### Agent Failure Mid-Task

**Questions:**
- What constitutes agent "failure"?
- Is automatic retry attempted? How many times?
- When does the task transition to Failed vs remain In-Progress?
- How is human handoff triggered?

**Deliverable:** Agent failure handling flowchart.

### Partial Task Tree Completion

**Questions:**
- Can a WO complete with some tasks failed?
- Who decides (automatic policy? human approval?)?
- What artifacts are produced for partial completion?

**Deliverable:** Partial completion policy spec.

### Quota Exhaustion

**Questions:**
- What happens when quota is exhausted mid-task?
- Graceful degradation: how much buffer?
- Hard stop: how is state preserved?
- How is quota refreshed (daily? on request?)?

**Deliverable:** Quota exhaustion handling spec.

### Session Crash Recovery

**Questions:**
- What state is preserved on crash?
- How is task state recovered from Jira?
- Is in-progress agent work recoverable?
- What is the recovery procedure?

**Deliverable:** Crash recovery runbook.

### Skill Execution Timeout

**Questions:**
- What are default timeout values?
- Are timeouts skill-configurable?
- What happens on timeout (retry? fail? prompt user?)?

**Deliverable:** Timeout policy spec.

---

## 7. Observability

### Metrics

**Questions:**
- What metrics are collected? (throughput, latency, agent utilization, cost)
- What is the metrics backend? (Prometheus? Datadog? Custom?)
- What dashboards are needed?
- What SLOs are defined?

**Deliverable:** Metrics catalog with collection points.

### Audit Granularity

**Questions:**
- Is audit per-task? Per-model-call? Per-tool-invocation?
- What fields are mandatory?
- What is the retention policy?
- How are audit queries supported?

**Deliverable:** Audit schema with retention policy.

### Distributed Tracing

**Questions:**
- What is the trace format (OpenTelemetry? Custom?)?
- How are traces correlated across Orchestrator → WO Runtime → Agent → Gateway?
- What span boundaries are defined?

**Deliverable:** Tracing implementation spec.

### Cost Attribution

**Questions:**
- How is cost attributed hierarchically (Session → WO → Task → Model call)?
- How are costs aggregated for billing?
- What reports are generated?

**Deliverable:** Cost attribution model.

---

## 8. Security

### Delegation Token Validation

**Questions:**
- Where is token validation performed? (Access Gateway? Each MCP?)
- How is signature verified?
- How is token revocation handled?
- What is the token scope validation logic?

**Deliverable:** Token validation spec.

### Scope Limitations

**Questions:**
- Can delegation be limited to specific tools?
- Can delegation be limited to specific repos?
- How are scope violations detected and blocked?

**Deliverable:** Scope limitation design.

### Revocation

**Questions:**
- Can session owner revoke delegation mid-execution?
- What is the revocation propagation delay?
- How does the agent handle revocation?

**Deliverable:** Revocation mechanism spec.

### Sensitive Data Handling

**Questions:**
- How are secrets in skill context handled?
- Is redaction applied to audit logs?
- How are credentials rotated?

**Deliverable:** Sensitive data handling guidelines.

### Jira MCP Authentication

**Questions:**
- How does WO Runtime daemon authenticate to Jira MCP?
- Is it per-session-owner OAuth? Service account?
- How are Jira permissions enforced?

**Deliverable:** Jira authentication design.

---

## 9. Skill Authoring

### Task Creation Tool

**Questions:**
- Is it an SDK function or raw Jira MCP call?
- What abstractions does the SDK provide?
- How are dependencies specified in a type-safe way?

**Deliverable:** Skill SDK for task creation.

### Task Template Format

**Questions:**
- What is the template format (YAML? JSON? DSL?)?
- How are variables resolved?
- How are templates versioned?

**Deliverable:** Task template spec with examples.

### Scenario Association in Sub-Tasks

**Questions:**
- How does a skill specify the scenario for sub-tasks?
- Is scenario inheritance supported?
- How are invalid scenarios handled?

**Deliverable:** Scenario association design.

### Skill Testing

**Questions:**
- How are skills tested in isolation?
- Is there a mock Employed Agent for testing?
- What test harness is provided?
- How is skill evaluation automated?

**Deliverable:** Skill testing framework spec.

---

## 10. Integration Testing

### End-to-End Test Scenarios

**Questions:**
- What e2e scenarios are required?
- What is the test environment setup?
- How are tests automated?

**Deliverable:** E2E test plan.

### Mock Jira MCP

**Questions:**
- What mock capabilities are needed?
- How is mock state managed?
- Is there an in-memory Jira for testing?

**Deliverable:** Jira MCP mock implementation spec.

### Mock Access Gateway

**Questions:**
- How are model responses mocked?
- How is quota behavior simulated?
- How are latency and errors injected?

**Deliverable:** Access Gateway mock implementation spec.

### Session Activation Testing

**Questions:**
- How is Coder activation tested without real Coder?
- What is the test strategy for activation rules?

**Deliverable:** Activation testing strategy.

---

## 11. Migration / Rollout

### Migration from Existing Workflows

**Questions:**
- What existing workflows need migration?
- What is the migration path?
- How is backward compatibility maintained during migration?

**Deliverable:** Migration plan.

### Feature Flags

**Questions:**
- What feature flags are needed for gradual rollout?
- How are flags managed?
- What is the flag-off behavior?

**Deliverable:** Feature flag inventory.

### Backward Compatibility

**Questions:**
- What backward compatibility is required?
- How long is the compatibility window?
- What deprecation notices are needed?

**Deliverable:** Compatibility requirements.

---

## Priority Recommendations

### High Priority (Must have for MVP)

1. Task state representation in Jira
2. Delegation Token structure and validation
3. Agent spawning for Cursor Agent (primary agent)
4. Task creation tool specification
5. Session activation config storage

### Medium Priority (Required for production)

6. All Capable Agent spawn specifications
7. Access Gateway API
8. Error handling policies
9. Observability metrics
10. Security validations

### Lower Priority (Can iterate)

11. Skill testing framework
12. Integration testing infrastructure
13. Migration tooling
14. Advanced features (pause/resume, partial completion)
