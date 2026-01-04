# Seer Case Automation

> **Status:** 🔴 Stub — Placeholder for expansion

Seer Case Automation enables Hub to invoke the **Seer Agent Engine** as an Automation Runtime for non-deterministic, AI-agent-driven case management.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Operation Types** | AI-driven Cases, Goal-oriented Operations |
| **Runtime** | Seer Agent Engine |
| **Execution Model** | Agent-orchestrated, non-deterministic |
| **State Management** | Case entity managed by Seer, synced to Hub |
| **Integration** | Hub Request, Task Management, CAF, Enterprise Memory |

---

## The Seer-Hub Contract

From the Seer design documentation:

> *"Seer Agent Engine as an Automation Runtime for 'Seer Case' Automation; [Requires contract between Hub Request to Automation Runtime integration - Signals/Updates]"*

This document defines that contract.

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Complex Investigations** | Multi-agent investigation with human oversight |
| **Dispute Resolution** | AI-coordinated dispute handling with escalation |
| **Customer Problem Solving** | Goal-driven problem resolution |
| **Compliance Review** | AI-assisted compliance with human approval gates |
| **Multi-party Coordination** | Coordinating multiple stakeholders through AI facilitation |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     OLYMPUS HUB                                  │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  I/O GATEWAYS                            │    │
│  │        (Signal → Trigger → Request)                      │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │ Request                             │
│                            ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              SEER CASE AUTOMATION ADAPTER                │    │
│  │                                                          │    │
│  │  • Request → Case Specification binding                  │    │
│  │  • Case lifecycle sync                                   │    │
│  │  • Signal/Update relay                                   │    │
│  └─────────────────────────┬───────────────────────────────┘    │
└────────────────────────────┼────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     OLYMPUS SEER                                 │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  SEER AGENT ENGINE                       │    │
│  │                                                          │    │
│  │  ┌──────────────────────────────────────────────────┐   │    │
│  │  │            CASE COORDINATOR AGENT                 │   │    │
│  │  │                                                   │   │    │
│  │  │  • Goals, SOPs, Knowledge Base                    │   │    │
│  │  │  • Role-playing Agents                            │   │    │
│  │  │  • Case Context (Session Memory)                  │   │    │
│  │  └──────────────────────────────────────────────────┘   │    │
│  │                                                          │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │    │
│  │  │ Employed │  │ Employed │  │     Employed         │   │    │
│  │  │ Agent 1  │  │ Agent 2  │  │     Agent N          │   │    │
│  │  └──────────┘  └──────────┘  └──────────────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Case Specification

The Case Specification defines how Seer manages a case:

| Component | Description |
|-----------|-------------|
| **Goals** | What the case aims to achieve |
| **Agents** | Employed Agents to be involved (directly or via task-queue) |
| **Signal Translation** | How case updates become signals for agents |
| **Knowledge Base** | SOPs and reference materials for the case |
| **Case View Extensions** | Custom UI components for case visualization |

---

## Hub-Seer Integration Contract

### 1. Request → Case Binding

| Hub | Seer |
|-----|------|
| Request ID | Case ID (correlation) |
| Request Type | Case Specification selector |
| Request Parameters | Case initialization context |
| Subject (for Service Requests) | Case Subject |

### 2. Case Lifecycle Sync

| Seer Event | Hub Update |
|------------|------------|
| Case Created | Operation instance created |
| Case Updated | Operation status updated |
| Case Phase Changed | Operation phase updated |
| Case Completed | Operation completed |

### 3. Signal/Update Relay

| Direction | Description |
|-----------|-------------|
| **Hub → Seer** | New signals from I/O Gateways update running cases |
| **Seer → Hub** | Case events published as Hub signals for downstream triggers |

---

## Case Collaboration Channels

From the case management notes, Seer Cases support multiple collaboration channels:

| Channel | Integration |
|---------|-------------|
| **MS Teams** | Case entity as Chat Group |
| **Email** | Case notifications and updates |
| **Custom Applications** | Case Webview embedded in surfaces |
| **Jira** | Case entity synced with Jira tasks |

---

## Case Context (Session Memory)

| Component | Description |
|-----------|-------------|
| **Chat Log** | Conversation history |
| **Key/Value Store** | Scoped storage (case-level, agent-level) |
| **Decision Records** | Decisions made during case resolution |
| **Evidence Bundle** | Collected evidence and context |

---

## Agent Participation Patterns

### Direct Participation
- Specific Employed Agents assigned to the case
- Agents receive all case updates

### Task Queue Participation
- Tasks assigned to task queues
- Any qualified agent can pick up tasks

### Subscription-based Participation
- AI Agents subscribe to specific case progression events
- Only relevant updates delivered

---

## Integration Points

| System | Integration |
|--------|-------------|
| **Hub Request Management** | Request binding, lifecycle sync |
| **Hub Task Management** | Task creation for human/AI participants |
| **Hub Enterprise Memory** | Case decisions and outcomes stored |
| **Hub CAF** | Decision records, explanations, evidence |
| **Cipher IAM** | Agent identity and authority |

---

## Related Documentation

- [Automation Runtimes Overview](./README.md)
- [ChronoShift - Temporal](./chronoshift-temporal.md)
- [Case Management](../../03-operations/case-management.md)
- [Seer Introduction](../../../../olympus-seer-docs/seer-design/introduction.md)

---

*TODO: Detailed design — Case Specification schema, Hub-Seer API contract, lifecycle state machine, collaboration channel adapters*

