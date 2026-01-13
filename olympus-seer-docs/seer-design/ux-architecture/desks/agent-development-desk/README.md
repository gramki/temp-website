# Agent Development Desk

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Primary Persona:** [Agent Engineer (AE)](../../../personas-and-needs/roles.md#3-agent-engineer-ae)  
> **Related:** [AE Reference](../../../personas-and-needs/ae.md) | [AE Lifecycle Needs](../../../personas-and-needs/needs/ae-lifecycle-coverage.md)

---

## Purpose

The Agent Development Desk is the primary workspace for the **Agent Engineer (AE)** ([role definition](../../../personas-and-needs/roles.md#3-agent-engineer-ae)). It provides capabilities to:

- Build agents with code, prompts, workflows, and tool bindings
- Test agents across behavioral, integration, and stress scenarios
- Release agents through staged deployment pipelines
- Support the full feedback-to-implementation lifecycle

---

## Consoles

| Console | Purpose | Documentation |
|---------|---------|---------------|
| **Development Console** | Code, prompts, workflows, tool bindings, telemetry | [development-console.md](./development-console.md) |
| **Test Console** | Behavioral, integration, regression, stress testing | [test-console.md](./test-console.md) |
| **Release Console** | Versioning, deployment pipeline, ARE handoff | [release-console.md](./release-console.md) |

---

## Key Journeys

| Journey | Description | Consoles Used |
|---------|-------------|---------------|
| **Agent Implementation** | Build agent per CSA design | Development Console |
| **Tool Integration** | Bind and test external tools | Development Console, Test Console |
| **Validation** | Run test suites, fix issues | Test Console |
| **Production Readiness** | Complete checklist, submit for ARE review | Release Console |
| **Incident Support** | Investigate issues flagged by COS/ARE | Development Console (Scenario Replay) |
| **Feedback Response** | Receive feedback, investigate, fix | All Consoles |

---

## OPDA Integration

The Agent Development Desk demonstrates OPDA capabilities for AE:

| OPDA | Capability | Console |
|------|------------|---------|
| **Observable** | Test results, telemetry validation, traces | Test Console, Development Console |
| **Predictable** | Behavioral tests, regression tests | Test Console |
| **Directable** | Code/prompt changes, safety hook implementation | Development Console |
| **Authority Enforceable** | Release approval, production readiness gates | Release Console |

### How AE Actions, Assesses, and Evidences OPDA

| OPDA | AE Actions | AE Assesses | AE Evidences |
|------|------------|-------------|---------------|
| **Observable** | Implement telemetry | Validate telemetry output | Telemetry contract compliance |
| **Predictable** | Write behavioral tests | Review test results | Test coverage reports |
| **Directable** | Implement safety hooks | Test hook functionality | Hook implementation docs |
| **Authority Enforceable** | Implement bounds | Validate bound enforcement | Bound test results |

---

## Full Lifecycle Coverage

The Agent Development Desk supports the complete agent development lifecycle:

```
Feedback → Issue → Design → Implement → Test → Release → Monitor
   ↑                                                        │
   └────────────────────────────────────────────────────────┘
```

### Lifecycle Support by Console

| Stage | Console | Capability |
|-------|---------|------------|
| **Feedback** | Development | Feedback Inbox |
| **Issue** | Development | Scenario Replay, Trace Analysis |
| **Design** | Development | CSA Design Spec Access |
| **Implement** | Development | Code, Prompts, Workflows, Tools |
| **Test** | Test | All test types |
| **Release** | Release | Deployment Pipeline |
| **Monitor** | Development | Production View |

---

## Channel Access

| Channel | Capabilities |
|---------|--------------|
| **Web UI** | Full desk access via Seer Portal |
| **REST API** | `/api/creator/v1/seer` — [API Documentation](../../rest-channels/ae-rest-channel.md) |
| **MCP** | `seer-ae-mcp` server for AI assistant integration |
| **CLI** | Development tooling, test automation |
| **IDE Plugin** | In-editor development |

---

## Integration Points

### Receives From

| Source | Data |
|--------|------|
| **CSA** | Design specifications |
| **COS** | Behavioral issues, implementation bugs |
| **ARE** | Operational issues, production feedback |
| **APO** | Improvement priorities |

### Sends To

| Destination | Data |
|-------------|------|
| **CSA** | Implementation review requests |
| **ARE** | Production readiness submission |
| **KMO** | Knowledge integration requests |

---

## Indicative Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT DEVELOPMENT DESK                                      AE: Chris M.   │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Development] [Test] [Release]                                 🔔 🔍 ⚙️    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ Agent: invoice-processor-v2                           Version: 2.3.1  │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │  [Code & Prompts] [Workflows] [Tool Bindings] [Telemetry]             │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │                                                                        │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │ SYSTEM PROMPT                                          v2.3.1   │  │  │
│  │  ├─────────────────────────────────────────────────────────────────┤  │  │
│  │  │ You are an invoice processing agent. Your role is to:          │  │  │
│  │  │                                                                 │  │  │
│  │  │ 1. Extract invoice details from submitted documents            │  │  │
│  │  │ 2. Validate against matching purchase orders                   │  │  │
│  │  │ 3. Apply approval rules based on amount and vendor status      │  │  │
│  │  │ 4. Route for human review when confidence is below threshold   │  │  │
│  │  │                                                                 │  │  │
│  │  │ You MUST:                                                       │  │  │
│  │  │ - Never approve invoices exceeding $1000 without PO match      │  │  │
│  │  │ - Escalate new vendors to human review                         │  │  │
│  │  │ - Log all decisions with reasoning                             │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                        │  │
│  │  [Save] [Preview] [Compare Versions] [Run Test]                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─────────────────────────────────┐  ┌──────────────────────────────────┐  │
│  │ FEEDBACK INBOX           [3]    │  │ TEST STATUS                      │  │
│  │                                 │  │                                  │  │
│  │ 🔴 COS: Inconsistent on >$5k   │  │ ✅ Unit Tests: 45/45 passing     │  │
│  │ 🟡 ARE: Retry storm detected   │  │ ✅ Behavioral: 12/12 passing     │  │
│  │ 🟢 APO: Enhancement request    │  │ ⚠️ Integration: 8/10 passing     │  │
│  └─────────────────────────────────┘  └──────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Console Summaries

### Development Console

The primary development environment for building agents.

**Sections:**
- **Code & Prompts** — Agent code, system prompts, task prompts, tool prompts
- **Workflows** — Reasoning flows, decision trees, orchestration logic
- **Tool Bindings** — Connect external tools, configure inputs/outputs
- **Telemetry** — Define events, configure traces, validate observability

**Key Features:**
- Live preview of agent behavior
- Prompt versioning with diff view
- Tool binding validation (schema, auth, sandbox testing)
- Telemetry contract checker (validates ARE requirements)
- Feedback Inbox for receiving COS/ARE issues
- Scenario Replay for debugging production issues

[Full specification →](./development-console.md)

---

### Test Console

Comprehensive testing environment for agent validation.

**Test Types:**
- **Behavioral Tests** — Validate reasoning patterns match design
- **Integration Tests** — Validate tool bindings work correctly
- **Regression Tests** — Catch prompt/code changes that break behavior
- **Stress Tests** — Validate execution bounds under load
- **Scenario Replay** — Replay production scenarios for debugging

**Key Features:**
- Test suite management
- Expected vs. actual comparison
- Automated test runs on commit
- Coverage reporting (scenarios covered)

[Full specification →](./test-console.md)

---

### Release Console

Deployment and production handoff management.

**Sections:**
- **Version Manager** — Create versions, view history, compare versions
- **Deployment Pipeline** — Stage → Canary → Production rollout
- **ARE Handoff** — Production readiness checklist, operability contract
- **Rollback** — Quick rollback to previous versions

**Production Readiness Checklist:**
- [ ] Agent contract complete
- [ ] Safety controls implemented
- [ ] Telemetry validated
- [ ] Cost attribution configured
- [ ] Tests passing
- [ ] CSA design validation complete
- [ ] ARE sign-off requested

[Full specification →](./release-console.md)

---

## REST API Overview

The AE REST channel extends the Hub Creator channel:

```
Base: /api/creator/v1/seer

Agents:
  GET    /agents                    - List agents
  GET    /agents/{id}               - Get agent details
  POST   /agents                    - Create agent
  PUT    /agents/{id}               - Update agent
  GET    /agents/{id}/prompts       - Get prompts
  PUT    /agents/{id}/prompts       - Update prompts

Versions:
  GET    /agents/{id}/versions      - List versions
  POST   /agents/{id}/versions      - Create version
  GET    /agents/{id}/versions/{v}  - Get version
  POST   /agents/{id}/deploy        - Deploy version

Tests:
  GET    /agents/{id}/tests         - List test suites
  POST   /agents/{id}/tests/run     - Run tests
  GET    /agents/{id}/tests/results - Get results

Tools:
  GET    /agents/{id}/tools         - List tool bindings
  POST   /agents/{id}/tools         - Add tool binding
  POST   /agents/{id}/tools/test    - Test tool binding
```

[Full API documentation →](../../rest-channels/ae-rest-channel.md)

---

*Status: 🟡 Draft — Overview and console specifications complete*
