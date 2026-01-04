# Hub Applications

> **Status:** 🔴 Stub — Placeholder for expansion

Hub Applications are the automation artifacts that execute Scenarios within Olympus Hub. Each Automation Runtime provides one or more specialized Hub Application types.

---

## Overview

A **Hub Application** represents:
- The executable automation corresponding to a Scenario
- A specialized artifact type provided by an Automation Runtime
- The target for Request routing via the Signal Exchange

---

## Hub Application Types by Automation Runtime

| Automation Runtime | Hub Application Type | Description |
|-------------------|---------------------|-------------|
| **Atlantis** | Procedure App | Stateless, single-step procedure execution |
| **Atlantis** | Decision App | ML/AI model invocation for business decisions |
| **Atlantis** | Prediction App | ML model for predictions and forecasting |
| **Perseus** | File App | Single or multi-file processing |
| **Perseus** | Map-Reduce App | Parallel distributed data processing |
| **Perseus** | Complex Event App | Event pattern detection and processing |
| **Rhea** | Workflow App | BPMN workflow execution |
| **ChronoShift** | Durable Workflow App | Long-running durable workflows (Temporal) |
| **Seer** | Seer Case Orchestration Agent | AI-driven case management and orchestration |

---

## Application Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        HUB APPLICATION                           │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    APPLICATION SPEC                       │   │
│  │                                                           │   │
│  │  • Application type (from Automation Runtime)              │   │
│  │  • Configuration (system-specific)                        │   │
│  │  • Resource requirements                                  │   │
│  │  • Scaling policy                                         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    REQUEST CONTRACT                       │   │
│  │                                                           │   │
│  │  • Input: Request payload schema                          │   │
│  │  • Output: Response payload schema                        │   │
│  │  • Updates: Allowed Request updates during execution      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    EXECUTION CONTEXT                      │   │
│  │                                                           │   │
│  │  • Workbench scope                                        │   │
│  │  • Available Tools (from Tool Registry)                   │   │
│  │  • Accessible Machines (from Machine Registry)            │   │
│  │  • Agent Identity (from Cipher)                           │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Request as Application Session

A **Request** represents a potentially long-running session for a Hub Application:

| Concept | Description |
|---------|-------------|
| **Initial Signal** | Creates the Request, starts the Application session |
| **Request Updates** | Subsequent signals update the Request, delivered to active session |
| **Session State** | Request state reflects Application processing state |
| **Session End** | Request completes when Application finishes processing |

```
Signal₁ → Request(created) → Application Session Started
Signal₂ → Request(updated) → Application Session Continues
Signal₃ → Request(updated) → Application Session Continues
         Request(completed) ← Application Session Ended
```

---

## Application Invocation Patterns

Different Automation Runtimes have different invocation patterns:

| Pattern | Description | Automation Runtimes |
|---------|-------------|-------------------|
| **Synchronous** | Immediate request-response | Atlantis (Procedure, Decision, Prediction) |
| **Async Job** | Submit job, poll for completion | Perseus (File, Map-Reduce, Complex Event) |
| **Process Start** | Instantiate process, track via process ID | Rhea (Workflow) |
| **Workflow Signal** | Start workflow or signal active workflow | ChronoShift (Durable Workflow) |
| **Case Event** | Initiate case or deliver event to active case | Seer (Case Orchestration) |

---

## Application Lifecycle

```
[Defined] → [Deployed] → [Active] → [Deprecated] → [Retired]
                           │
                           └─→ [Suspended] → [Active]
```

| State | Description |
|-------|-------------|
| **Defined** | Configuration exists in Workbench |
| **Deployed** | Application deployed to Automation Runtime |
| **Active** | Ready to receive Requests |
| **Suspended** | Temporarily not accepting Requests |
| **Deprecated** | Still active but slated for retirement |
| **Retired** | No longer deployed |

---

## Relationship to Other Concepts

| Concept | Relationship |
|---------|--------------|
| **Scenario** | One Scenario → one Hub Application |
| **Trigger** | Triggers route to Scenarios, which bind to Applications |
| **Request** | Request is routed to Application for processing |
| **Automation Runtime** | Provides the runtime for Application execution |

---

## Related Documentation

- [Workbench Management](../04-subsystems/workbench-management/README.md) — Application configuration
- [Application Router](../04-subsystems/signal-exchange/application-router.md) — Request routing
- [Automation Runtimes](../04-subsystems/automation-runtimes/README.md) — Runtime hosts

---

*TODO: Detailed design — application registry, versioning, deployment*

