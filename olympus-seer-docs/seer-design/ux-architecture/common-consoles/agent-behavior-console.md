# Agent Behavior Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Type:** Common Console (shared across desks)  
> **Related:** [Common Consoles Overview](./README.md) | [Agent Observability](../../subsystems/agent-observability.md)

---

## Purpose

The Agent Behavior Console provides a comprehensive, persona-appropriate view of an agent's role and behavior within a Request/Session context. It enables all stakeholders to understand, analyze, and act on agent behavior.

This is a **common console** that appears across multiple desks with persona-specific views and permissions.

---

## Personas and Use Cases

| Persona | Primary Use Case | Access Level |
|---------|------------------|--------------|
| **Automation Product Owner (APO)** ([role definition](../../personas-and-needs/roles.md#1-automation-product-owner-apo)) | Understand business outcomes, validate intent alignment | Read |
| **Cognitive Systems Architect (CSA)** ([role definition](../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)) | Validate design compliance, analyze reasoning patterns | Read |
| **Agent Engineer (AE)** ([role definition](../../personas-and-needs/roles.md#3-agent-engineer-ae)) | Debug implementation issues, analyze traces | Write |
| **Knowledge & Memory Owner (KMO)** ([role definition](../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)) | Analyze knowledge usage, monitor memory operations | Read |
| **Agent Reliability Engineer (ARE)** ([role definition](../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)) | Monitor health, investigate incidents | Write |
| **Cognitive Operations Steward (COS)** ([role definition](../../personas-and-needs/roles.md#6-cognitive-operations-steward-cos)) | Detect drift, analyze quality, route issues | Write |
| **AI Risk & Audit Owner (ARAO)** ([role definition](../../personas-and-needs/roles.md#7-ai-risk--audit-owner-arao)) | Audit compliance, review security | Read |

---

## Core Filtering and Navigation

### Primary Filters

| Filter | Description | Examples |
|--------|-------------|----------|
| **Employed Agent** | Filter by agent identity | Agent ID, name, workbench, scenario |
| **Request ID** | Filter by specific request | Includes all related requests in hierarchy |
| **Session ID** | Filter by session | Multi-request session context |
| **Time Range** | Absolute or relative | Last 1 hour, custom range |
| **Scenario** | Filter by scenario | Scenario participation |
| **Workbench** | Filter by workbench | Workbench context |

### Secondary Filters

| Filter | Options |
|--------|---------|
| **Request Status** | Success, error, timeout, cancelled |
| **Agent State** | Active, suspended, degraded |
| **Decision Type** | Approval, denial, escalation, delegation |
| **Cost Threshold** | Filter by cost ranges |
| **Security Events** | Filter by security event types |
| **Persona View** | Pre-configured views per persona |

---

## Console Sections

### 1. Request/Session Context

#### Request Overview

Displays request metadata and lifecycle:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ REQUEST OVERVIEW                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ Request ID: req-2026-0113-abc123          Session: sess-xyz789             │
│ Parent: req-2026-0113-def456 (delegated)                                   │
│ Scenario: invoice-processing              Workbench: finance-ops           │
│ Priority: HIGH                            SLA: Tier 1 (< 5 min)            │
├─────────────────────────────────────────────────────────────────────────────┤
│ Started: 2026-01-13 14:30:00              Duration: 2.3s                   │
│ Status: ✅ COMPLETED                       Outcome: Approved               │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Data Elements:**
- Request Metadata (ID, Session ID, Parent Request ID)
- Scenario, Workbench, Customer/Subject context
- Request type, priority, SLA tier
- Timestamps (initiation, completion, duration)
- Status and final outcome

#### Request Hierarchy

Visual representation of request chain:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ REQUEST HIERARCHY                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌────────────────────┐                                                    │
│   │ req-def456         │ ← Parent (Orchestrator)                           │
│   │ orchestrator-agent │                                                    │
│   └─────────┬──────────┘                                                    │
│             │ delegated                                                     │
│   ┌─────────▼──────────┐                                                    │
│   │ req-abc123 ★       │ ← Current Request                                 │
│   │ invoice-processor  │                                                    │
│   └─────────┬──────────┘                                                    │
│             │ delegated                                                     │
│   ┌─────────▼──────────┐                                                    │
│   │ req-ghi789         │ ← Child (PO Validator)                            │
│   │ po-validator       │                                                    │
│   └────────────────────┘                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Request Lifecycle

State transitions with actors:

| Timestamp | State | Actor | Reason |
|-----------|-------|-------|--------|
| 14:30:00.000 | CREATED | Signal Exchange | Dispatch from scenario |
| 14:30:00.050 | ASSIGNED | Agent Runtime | Agent selected |
| 14:30:00.100 | PROCESSING | invoice-processor | Started reasoning |
| 14:30:02.100 | DELEGATED | invoice-processor | PO validation needed |
| 14:30:02.300 | RESUMED | invoice-processor | Child request complete |
| 14:30:02.350 | COMPLETED | invoice-processor | Decision: Approved |

---

### 2. Agent Memory Operations

#### Memory Changes

Timeline of all memory operations:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ MEMORY OPERATIONS                                           [12 operations] │
├─────────────────────────────────────────────────────────────────────────────┤
│ Time       │ Op     │ Store      │ Key                    │ TTL           │
│ ───────────────────────────────────────────────────────────────────────────│
│ 14:30:00.1 │ READ   │ Session    │ conversation_history   │ —             │
│ 14:30:00.2 │ READ   │ Episodic   │ vendor_interactions    │ —             │
│ 14:30:01.5 │ WRITE  │ Session    │ extracted_invoice_data │ 1h            │
│ 14:30:02.1 │ READ   │ Semantic   │ approval_thresholds    │ —             │
│ 14:30:02.3 │ WRITE  │ Episodic   │ decision_record        │ 7y            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Data Elements:**
- Timestamp, operation type (store, update, delete, read)
- Memory store type (conversation, session, episodic, semantic)
- Memory key, value preview (with PII redaction)
- Memory TTL and retention policy
- Hit/miss status for reads

#### Memory Context

| Memory Type | Owner | Contents |
|-------------|-------|----------|
| **Agent Memory** | AE/ARE | Conversation history, session variables, temporary context |
| **Enterprise Memory** | KMO | Episodic memory references, semantic memory queries |

---

### 3. Tool Invocations

#### Tool Call Details

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TOOL INVOCATIONS                                              [5 calls]     │
├─────────────────────────────────────────────────────────────────────────────┤
│ Time       │ Tool              │ Duration │ Status │ Authority             │
│ ───────────────────────────────────────────────────────────────────────────│
│ 14:30:00.5 │ extract_invoice   │ 120ms    │ ✅     │ Read: Financial Docs  │
│ 14:30:01.0 │ lookup_po         │ 85ms     │ ✅     │ Read: PO Database     │
│ 14:30:01.2 │ check_vendor      │ 45ms     │ ✅     │ Read: Vendor Registry │
│ 14:30:02.0 │ validate_amount   │ 15ms     │ ✅     │ Execute: Calculator   │
│ 14:30:02.2 │ record_decision   │ 50ms     │ ✅     │ Write: Audit Log      │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Expandable Detail per Tool:**
- Protocol, tool name, alias
- Request/response payloads (with PII redaction)
- Gateway routing decisions
- Authority checks (OPA policy evaluations)
- Access granted/denied with reasons

#### Tool Performance

| Metric | Value |
|--------|-------|
| Success Rate | 100% (5/5) |
| Avg Latency | 63ms |
| Retries | 0 |
| Circuit Breaker | Closed |

---

### 4. LLM Calls and Reasoning

#### LLM Request/Response

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ LLM CALLS                                                    [3 calls]      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Call │ Model              │ Input    │ Output   │ Cost    │ Latency        │
│ ─────────────────────────────────────────────────────────────────────────── │
│ 1    │ gpt-4-turbo        │ 2,150    │ 342      │ $0.052  │ 1.2s           │
│ 2    │ gpt-4-turbo        │ 1,890    │ 128      │ $0.041  │ 0.8s           │
│ 3    │ gpt-4-turbo        │ 1,420    │ 95       │ $0.031  │ 0.5s           │
├─────────────────────────────────────────────────────────────────────────────┤
│ TOTAL                     │ 5,460    │ 565      │ $0.124  │ 2.5s           │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Expandable Detail per Call:**
- Full prompt sent (with PII redaction)
- System prompts, user prompts, context assembly
- Prompt version and template used
- Response content and metadata
- Guardrail checks applied

#### Reasoning Traces

Visual reasoning flow:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ REASONING TRACE                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Step 1: REASON ─────────────────────────────────────────────────────────    │
│   Input: Invoice PDF received                                               │
│   Thought: Need to extract invoice details first                            │
│   Confidence: 0.95                                                          │
│                                                                             │
│ Step 2: ACT ────────────────────────────────────────────────────────────    │
│   Action: extract_invoice(document=invoice.pdf)                             │
│   Result: {amount: $750, vendor: "Acme Corp", po_ref: "PO-12345"}          │
│                                                                             │
│ Step 3: REASON ─────────────────────────────────────────────────────────    │
│   Input: Extracted data, need PO validation                                 │
│   Thought: Amount < $1000 and PO exists, verify PO match                   │
│   Confidence: 0.92                                                          │
│                                                                             │
│ Step 4: ACT ────────────────────────────────────────────────────────────    │
│   Action: lookup_po(po_number="PO-12345")                                  │
│   Result: {status: "Active", amount: $750, vendor: "Acme Corp"}            │
│                                                                             │
│ Step 5: DECIDE ─────────────────────────────────────────────────────────    │
│   Decision: APPROVE                                                         │
│   Rationale: Amount matches, vendor verified, PO active                    │
│   Confidence: 0.98                                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 5. Context Assembly

#### Context Compilation Details

| Source | Tokens | Relevance |
|--------|--------|-----------|
| System Prompt | 450 | — |
| Knowledge: Invoice Policy | 280 | 0.95 |
| Knowledge: Approval Rules | 180 | 0.92 |
| Memory: Vendor History | 120 | 0.88 |
| Request Context | 350 | 1.00 |
| **Total** | **1,380** | — |

**Context Budget:** 4,000 tokens | **Used:** 1,380 (35%)

---

### 6. Authority and Policy Enforcement

#### Authority Checks

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTHORITY CHECKS                                            [8 checks]      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Check                    │ Ceiling Source     │ Result │ Value             │
│ ─────────────────────────────────────────────────────────────────────────── │
│ Value Ceiling            │ Employment Spec    │ ✅     │ $750 < $1,000     │
│ Rate Ceiling             │ Employment Spec    │ ✅     │ 5/hr < 100/hr     │
│ Tool Access: extract     │ Employment Spec    │ ✅     │ Allowed           │
│ Tool Access: lookup_po   │ Employment Spec    │ ✅     │ Allowed           │
│ Tool Access: record      │ Employment Spec    │ ✅     │ Allowed           │
│ Autonomy Level           │ Employment Spec    │ ✅     │ Full < Full       │
│ Decision Authority       │ Delegation Chain   │ ✅     │ Approve permitted │
│ Cost Budget              │ Request Budget     │ ✅     │ $0.12 < $5.00     │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Guardrail Execution

| Guardrail | Type | Result | Details |
|-----------|------|--------|---------|
| Input Validation | Inbound | ✅ Allow | Clean input |
| PII Detection | Inbound | ✅ Allow | No PII found |
| Output Sanitization | Outbound | ✅ Allow | No sensitive data |
| Decision Validation | Outbound | ✅ Allow | Within policy |

---

### 7. Cost and Performance

#### Cost Breakdown

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ COST BREAKDOWN                                               Total: $0.127  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   LLM Costs ██████████████████████████████████████████░░░░░░░░  $0.124 (98%)│
│   Tool Costs █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  $0.002 (2%) │
│   Infra Costs ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  $0.001 (<1%)│
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Attribution: Agent=invoice-processor | Workbench=finance-ops | Scenario=inv│
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Performance Metrics

| Metric | Value | SLA | Status |
|--------|-------|-----|--------|
| End-to-End Latency | 2.35s | < 5s | ✅ |
| LLM Latency | 2.50s | — | — |
| Tool Latency | 0.32s | — | — |
| Error Rate | 0% | < 1% | ✅ |

---

### 8. Security and Compliance

#### Security Events

| Event Type | Count | Status |
|------------|-------|--------|
| Prompt Injection Attempts | 0 | ✅ |
| Unauthorized Tool Access | 0 | ✅ |
| PII Exposure Attempts | 0 | ✅ |
| Jailbreak Attempts | 0 | ✅ |

#### Audit Trail

**Decision Record:**
```json
{
  "decision_id": "dec-2026-0113-abc123",
  "timestamp": "2026-01-13T14:30:02.350Z",
  "agent": "invoice-processor-v2",
  "decision": "APPROVE",
  "confidence": 0.98,
  "rationale": "Amount matches PO, vendor verified, within authority",
  "evidence": ["invoice.pdf", "po-lookup-result", "vendor-check"],
  "authority_used": "Full autonomy for < $1000"
}
```

---

## Persona-Specific Views

### APO View: Business Outcomes

Focus on outcomes and value:

| Section | Content |
|---------|---------|
| **Outcome Summary** | Request outcome, success criteria achievement |
| **Value Metrics** | Business value delivered, ROI indicators |
| **SLA Compliance** | Performance against service levels |
| **User Satisfaction** | Customer feedback, escalation status |

**APO View Filters:** Hide technical details, show business context

### CSA View: Design Validation

Focus on reasoning patterns:

| Section | Content |
|---------|---------|
| **Pattern Compliance** | Reasoning pattern adherence |
| **Cognitive Flow** | Design boundary compliance |
| **Failure Semantics** | Failure mode validation |
| **Multi-Agent System** | Agent interaction patterns |

**CSA View Filters:** Show reasoning traces, hide cost details

### AE View: Implementation Debugging

Focus on implementation details:

| Section | Content |
|---------|---------|
| **Execution Traces** | Code execution, stack traces |
| **Tool Integration** | Tool binding issues, API responses |
| **Telemetry** | Event emission, trace validation |
| **Error Analysis** | Error details, debug logs |

**AE View Filters:** Show debug-level details, full payloads

### ARE View: System Health

Focus on operational health:

| Section | Content |
|---------|---------|
| **Health Metrics** | AHS, CHR, latency, errors |
| **Cost Analysis** | Cost breakdown, budget usage |
| **Control Status** | Kill switch, bounds, levers |
| **Incident Indicators** | Anomalies, threshold breaches |

**ARE View Filters:** Show system metrics, control status

### COS View: Cognitive Health

Focus on behavior quality:

| Section | Content |
|---------|---------|
| **Quality Metrics** | Consistency, confidence calibration |
| **Drift Detection** | Behavior drift indicators |
| **Issue Routing** | Identified issues, suggested routes |
| **Pattern Analysis** | Emerging patterns for learning |

**COS View Filters:** Show quality signals, behavior patterns

### ARAO View: Compliance Audit

Focus on compliance and security:

| Section | Content |
|---------|---------|
| **Policy Compliance** | Policy adherence, violations |
| **Audit Evidence** | Decision records, evidence bundles |
| **Security Posture** | Security events, controls |
| **Risk Indicators** | Authority usage, risk signals |

**ARAO View Filters:** Show compliance details, audit trail

### KMO View: Knowledge Usage

Focus on knowledge and memory:

| Section | Content |
|---------|---------|
| **Knowledge Access** | Knowledge queries, relevance |
| **Memory Operations** | Memory reads/writes, governance |
| **Knowledge Gaps** | Missing information, failures |
| **Learning Candidates** | Patterns for promotion |

**KMO View Filters:** Show knowledge context, memory details

---

## Detail Level Filtering

| Level | Content | Use Case |
|-------|---------|----------|
| **Summary** | Outcome, cost, duration, key decisions | Quick review |
| **Standard** | Requests, LLM calls, tool calls, memory | Normal investigation |
| **Detailed** | All spans, all logs, full context | Deep investigation |
| **Debug** | Raw payloads, internal state, debug logs | Implementation debugging |

---

## Data Sources

| Source | Data Provided |
|--------|---------------|
| **Agent SDK** | Agent-level metrics, logs, traces |
| **Seer Sidecar** | Guardrail execution, policy enforcement |
| **Model Gateway** | LLM calls, cost tracking, routing |
| **Tools Gateway** | Tool invocations, access control |
| **Signal Exchange** | Request routing, dispatch events |
| **Context Compiler** | Context assembly logs |
| **Agent Runtime** | Pod logs, resource usage |
| **Cipher IAM** | Authority checks, policy evaluations |
| **Hub Services** | Knowledge queries, memory operations |

---

## REST API

The Agent Behavior Console uses the behavior analysis API:

```
Base: /api/seer/behavior/v1

Requests:
  GET    /requests/{id}              - Get request details
  GET    /requests/{id}/hierarchy    - Get request hierarchy
  GET    /requests/{id}/lifecycle    - Get lifecycle events
  GET    /requests/{id}/memory       - Get memory operations
  GET    /requests/{id}/tools        - Get tool invocations
  GET    /requests/{id}/llm          - Get LLM calls
  GET    /requests/{id}/reasoning    - Get reasoning trace
  GET    /requests/{id}/authority    - Get authority checks
  GET    /requests/{id}/cost         - Get cost breakdown
  GET    /requests/{id}/security     - Get security events
  GET    /requests/{id}/audit        - Get audit record

Sessions:
  GET    /sessions/{id}              - Get session details
  GET    /sessions/{id}/requests     - Get session requests

Agents:
  GET    /agents/{id}/requests       - Get agent requests
  GET    /agents/{id}/summary        - Get agent summary

Export:
  POST   /requests/{id}/export       - Export request data
  POST   /sessions/{id}/export       - Export session data
```

---

## Indicative Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AGENT BEHAVIOR CONSOLE                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Agent: [invoice-processor-v2 ▼]  Request: [req-abc123]  View: [AE ▼]       │
│ Time: [Last 1 hour ▼]  Status: [All ▼]  Detail: [Standard ▼]               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ┌─────────────────────────────────┐ ┌────────────────────────────────────┐  │
│ │ REQUEST OVERVIEW                │ │ COST & PERFORMANCE                 │  │
│ │ ID: req-abc123                  │ │ Total Cost: $0.127                 │  │
│ │ Status: ✅ COMPLETED            │ │ Duration: 2.35s                    │  │
│ │ Outcome: Approved               │ │ LLM Calls: 3                       │  │
│ │ Duration: 2.35s                 │ │ Tool Calls: 5                      │  │
│ └─────────────────────────────────┘ └────────────────────────────────────┘  │
│                                                                             │
│ ┌───────────────────────────────────────────────────────────────────────┐   │
│ │ [Overview] [Reasoning] [Tools] [Memory] [LLM] [Authority] [Security]  │   │
│ ├───────────────────────────────────────────────────────────────────────┤   │
│ │                                                                       │   │
│ │ REASONING TRACE                                                       │   │
│ │ ─────────────────────────────────────────────────────────────────────│   │
│ │ Step 1: REASON                                                        │   │
│ │   Thought: Need to extract invoice details first                      │   │
│ │   Confidence: 0.95                                                    │   │
│ │                                                                       │   │
│ │ Step 2: ACT                                                           │   │
│ │   Action: extract_invoice(document=invoice.pdf)                       │   │
│ │   Result: {amount: $750, vendor: "Acme Corp", po_ref: "PO-12345"}    │   │
│ │                                                                       │   │
│ │ Step 3: REASON                                                        │   │
│ │   Thought: Amount < $1000 and PO exists, verify PO match              │   │
│ │   Confidence: 0.92                                                    │   │
│ │                                                                       │   │
│ │ [Expand All] [Collapse All] [Export Trace]                            │   │
│ └───────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│ ┌───────────────────────────────────────────────────────────────────────┐   │
│ │ TIMELINE                                                    [Zoom: 1x] │   │
│ │ ─────────────────────────────────────────────────────────────────────│   │
│ │ 14:30:00 ├──────────────────────────────────────────────┤ 14:30:02.35│   │
│ │          │ LLM ████████████████                          │            │   │
│ │          │ TOOLS   ██  ██  ██  ██  █                     │            │   │
│ │          │ MEMORY ██ ██    ██      ██                    │            │   │
│ └───────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## OPDA Contribution

The Agent Behavior Console supports OPDA across all personas:

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Full visibility into agent reasoning, decisions, and operations |
| **Predictable** | Baseline comparison, pattern analysis, confidence tracking |
| **Directable** | Evidence for intervention decisions, issue identification |
| **Authority Enforceable** | Authority check visibility, compliance evidence, audit trail |

---

## Integration Points

### Desk Integration

| Desk | Integration Method | Use Case |
|------|-------------------|----------|
| Agent Portfolio Desk | Tab embed | APO: Review agent outcomes |
| Agent Design Desk | Tab embed | CSA: Validate design compliance |
| Agent Development Desk | Panel + Modal | AE: Debug and investigate |
| Agent Operations Desk | Tab embed | ARE: Incident investigation |
| Cognitive Health Desk | Tab embed | COS: Behavior analysis |
| Agent Compliance Desk | Tab embed | ARAO: Audit evidence |
| Knowledge Governance Desk | Tab embed | KMO: Knowledge usage |

### MCP Equivalent

The Agent Behavior Console functionality is available via MCP:

```
MCP Server: seer-behavior-mcp

Tools:
  - seer_get_request_details(request_id)
  - seer_get_reasoning_trace(request_id)
  - seer_get_tool_invocations(request_id)
  - seer_get_llm_calls(request_id)
  - seer_get_authority_checks(request_id)
  - seer_export_audit_record(request_id)
```

---

*Status: 🟡 Draft — Comprehensive specification, implementation TBD*
