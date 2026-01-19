---
name: Information-Centric Work Folder
overview: Rename 03-operations to 03-information-centric-work and populate with work pattern documents that describe prominent information-centric work patterns and how they map to Hub ontology concepts — without referencing subsystems.
todos:
  - id: rename-folder
    content: Rename 03-operations to 03-information-centric-work
    status: pending
  - id: create-readme
    content: Create README.md with pattern index and introduction
    status: pending
  - id: refactor-case
    content: Refactor case-management.md to case-based-work.md
    status: pending
  - id: create-queue
    content: Create queue-based-work.md
    status: pending
  - id: create-document
    content: Create document-centric-work.md
    status: pending
  - id: create-conversation
    content: Create conversation-based-work.md
    status: pending
  - id: create-event
    content: Create event-driven-operations.md
    status: pending
  - id: update-main-readme
    content: Update main README.md index references
    status: pending
  - id: cleanup-08-operations
    content: Move 08-operations/runbooks to 05-infrastructure and delete 08-operations
    status: pending
---

# Rename 03-operations to 03-information-centric-work

Create a conceptual section describing prominent information-centric work patterns and how they map to Hub's ontology. Each document describes a work pattern in domain-neutral terms, then shows how Hub concepts (Scenario, Request, Agent, Task, etc.) model that pattern.

---

## Folder Structure

```
03-information-centric-work/
├── README.md                     # Overview and pattern index
├── case-based-work.md            # Refactored from case-management.md
├── queue-based-work.md           # NEW
├── document-centric-work.md      # NEW
├── conversation-based-work.md    # NEW
└── event-driven-operations.md    # NEW
```

---

## 1. README.md — Section Overview

**Purpose:** Introduce the section, connect to glossary definition, and provide a pattern index.

**Outline:**

```markdown
# Information-Centric Work Patterns

> Information-centric work is work where the primary inputs, transformations, 
> and outputs are information rather than physical matter.
> — [Glossary](../01-concepts/glossary.md#information-centric-work)

## Purpose of This Section

This section describes prominent patterns of information-centric work and how 
they map to Hub's ontology. Each pattern represents a common way work operates 
across industries and functions.

## Why Patterns Matter

Understanding work patterns helps:
- Recognize which Hub concepts apply to your domain
- Design Scenarios that fit how work actually operates
- Choose appropriate collaboration models

## Pattern Index

| Pattern | Characteristics | Key Ontology Mapping |
|---------|-----------------|----------------------|
| Case-Based | Non-deterministic, evolving, collaborative | Case, Request, Agent collaboration |
| Queue-Based | Task-driven, throughput-oriented | Task Queue, Procedure, Assignment |
| Document-Centric | Artifact-centered, iterative | Request as document lifecycle |
| Conversation-Based | Dialogue-centered, real-time | Signal as message, Agent as participant |
| Event-Driven | Reactive, signal-triggered | Signal, Trigger, Scenario |

## How Patterns Relate to Ontology

Brief diagram showing: Work Pattern → Scenario → (Procedure | Workflow | Case) → Activities → Tasks → Agents

## Related

- [Glossary: Information-Centric Work](../01-concepts/glossary.md#information-centric-work)
- [Glossary: Operation](../01-concepts/glossary.md#operation)
- [Ontology Reference](../01-concepts/ontology-reference.md)
```

---

## 2. case-based-work.md — Refactor from [case-management.md](olympus-hub-docs/03-operations/case-management.md)

**Purpose:** Describe case-based work as a pattern, then map to Hub ontology.

**Outline:**

```markdown
# Case-Based Work

## What Is Case-Based Work?

Case-based work is non-deterministic, evolving collaboration to resolve a 
situation. Unlike procedure-based work, the path forward is not known in 
advance — it emerges through investigation, judgment, and collaboration.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Determinism** | Non-deterministic — path emerges during execution |
| **Agents** | Multiple agents collaborate toward resolution |
| **Duration** | Hours to weeks — depends on complexity |
| **State** | Evolves — new information changes direction |
| **Goal** | Resolution of a situation, not completion of steps |

### Examples

- Security incident investigation
- Customer dispute resolution
- Medical diagnosis and treatment
- Legal case management
- Product defect analysis

## Anatomy of a Case

### Lifecycle
1. **Initiation** — A situation triggers the case
2. **Investigation** — Agents gather information, form hypotheses
3. **Collaboration** — Multiple agents contribute perspectives
4. **Decision** — Resolution determined based on evidence
5. **Closure** — Case resolved, outcomes recorded

### Participants
- **Case Coordinator** — Orchestrates but doesn't dictate
- **Domain Experts** — Contribute specialized knowledge
- **Decision Makers** — Have authority for final determination
- **Observers** — Track progress, ensure compliance

### Case Context
- **Case Record** — The evolving documentation
- **Evidence** — Information gathered during investigation
- **Communication Log** — History of collaboration
- **Decision Trail** — How conclusions were reached

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Case | Case (Execution Layer) |
| Situation that triggers case | Signal → Scenario |
| Case instance | Request |
| Participants | Agents (Human, AI) |
| Work items within case | Tasks |
| Evidence, documentation | Knowledge artifacts |
| Decisions | Activities with decision outcomes |
| Case resolution | Request completion |

### How Hub Models Case-Based Work

```

Signal (situation occurs)

↓

Scenario (defines case type)

↓

Request (case instance)

↓

Case Operation (non-deterministic execution)

↓

Tasks assigned to Agents

↓

Collaboration toward resolution

↓

Request completes (case closed)

```

### Why Case-Based Work Suits Hub

- **Goal-oriented Scenarios** — Define what success looks like, not how to get there
- **Agent collaboration** — Multiple agents work toward shared goal
- **Evolving state** — Request accumulates history as case progresses
- **Non-deterministic flow** — Case can branch, loop, escalate based on findings

## Collaboration Surfaces for Cases

Cases naturally occur in different contexts:

| Surface | Characteristics | Example |
|---------|-----------------|---------|
| **Conversation** | Real-time dialogue, quick decisions | Incident war room |
| **Document** | Artifact-centered, iterative review | Legal brief development |
| **Notebook** | Analytical, exploratory | Data investigation |
| **Ticket** | Structured, tracked | Support case |

## Related

- [Ontology: Case](../01-concepts/ontology-3-execution-layer.md#case)
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
```

---

## 3. queue-based-work.md — NEW

**Purpose:** Describe queue-driven, throughput-oriented work patterns.

**Outline:**

```markdown
# Queue-Based Work

## What Is Queue-Based Work?

Queue-based work is driven by work items that arrive in a stream and must 
be processed — typically with SLAs, throughput targets, and assignment logic.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Determinism** | Mostly deterministic — known procedures |
| **Agents** | Often single agent per item |
| **Duration** | Minutes to hours per item |
| **State** | Progression through defined states |
| **Goal** | Throughput, quality, SLA compliance |

### Examples

- Customer service tickets
- Claims processing
- Transaction reconciliation
- Application reviews
- Support request handling

## Anatomy of Queue-Based Work

### The Queue
- **Intake** — Items arrive from signals
- **Prioritization** — Items ordered by urgency, SLA, type
- **Assignment** — Items routed to qualified agents
- **Processing** — Agent works the item
- **Completion** — Item resolved, next item pulled

### Assignment Patterns
- **Round-robin** — Distribute evenly
- **Skill-based** — Match item type to agent capability
- **Load-based** — Consider agent current load
- **Pull** — Agent selects next item
- **Push** — System assigns to agent

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Queue | Task Queue |
| Work item | Task |
| Item type | Scenario |
| Assignment logic | Task Queue configuration |
| Processing | Procedure (deterministic steps) |
| Agent handling item | Agent assigned to Task |
| SLA | Goal with time constraint |

### How Hub Models Queue-Based Work

```

Signals arrive (work items)

↓

Triggers match to Scenarios

↓

Requests created

↓

Tasks created and queued

↓

Assignment logic routes to Agents

↓

Agent processes Task (Procedure)

↓

Task completes, Request advances

```

## Related

- [Ontology: Task Queue](../01-concepts/ontology-3-execution-layer.md#task-queue)
- [Ontology: Procedure](../01-concepts/ontology-3-execution-layer.md#procedure)
```

---

## 4. document-centric-work.md — NEW

**Purpose:** Describe work centered around artifact creation and iteration.

**Outline:**

```markdown
# Document-Centric Work

## What Is Document-Centric Work?

Document-centric work is organized around the creation, review, and evolution 
of an artifact — a document, design, code, or specification.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Center** | An artifact that evolves |
| **Collaboration** | Multiple contributors and reviewers |
| **Duration** | Days to weeks |
| **State** | Draft → Review → Approved |
| **Goal** | Artifact meeting quality/approval criteria |

### Examples

- PRD creation and review
- Design document development
- Code review and approval
- Contract negotiation
- Report generation

## Anatomy of Document-Centric Work

### Lifecycle
1. **Initiation** — Need for artifact identified
2. **Drafting** — Initial version created
3. **Review** — Feedback gathered
4. **Revision** — Changes incorporated
5. **Approval** — Final sign-off
6. **Publication** — Artifact released

### Roles
- **Author** — Creates and revises
- **Reviewer** — Provides feedback
- **Approver** — Authorizes final version
- **Consumer** — Uses the final artifact

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Artifact | Entity attached to Request |
| Document lifecycle | Scenario (goal: approved artifact) |
| Review round | Activity |
| Feedback request | Task for Reviewer |
| Approval decision | Decision with outcome |

### How Hub Models Document-Centric Work

```

Signal (artifact needed)

↓

Scenario (document type + approval process)

↓

Request (artifact lifecycle instance)

↓

Tasks for drafting, review, approval

↓

Agents collaborate on artifact

↓

Request completes when approved

```

## Related

- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
- [Ontology: Workflow](../01-concepts/ontology-3-execution-layer.md#workflow)
```

---

## 5. conversation-based-work.md — NEW

**Purpose:** Describe dialogue-centered, real-time collaborative work.

**Outline:**

```markdown
# Conversation-Based Work

## What Is Conversation-Based Work?

Conversation-based work unfolds through dialogue — questions and answers, 
proposals and responses, clarifications and decisions — in real-time or 
near-real-time exchanges.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Medium** | Dialogue (chat, voice, video) |
| **Pace** | Real-time or near-real-time |
| **Agents** | Two or more in active exchange |
| **Duration** | Minutes to hours per session |
| **Goal** | Resolution through understanding |

### Examples

- Customer support chat
- Technical troubleshooting
- Sales qualification
- Expert consultation
- Incident triage

## Anatomy of Conversation-Based Work

### The Conversation
- **Opening** — Context established
- **Exploration** — Questions, clarifications
- **Resolution** — Answer, decision, or handoff
- **Closing** — Summary, next steps

### Participant Roles
- **Initiator** — Starts the conversation (often a customer/user)
- **Responder** — Provides information, guidance, decisions
- **Observer** — Monitors, may escalate or intervene

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Conversation | Request (collaboration surface) |
| Message | Signal (inbound) or Action (outbound) |
| Participant | Agent |
| Conversation goal | Scenario goal |
| Resolution | Request completion |

### How Hub Models Conversation-Based Work

```

Signal (conversation initiated)

↓

Scenario (conversation type)

↓

Request (conversation instance)

↓

Messages flow as Signals/Actions

↓

Agents respond to Signals

↓

Resolution → Request completes

```

## Related

- [Ontology: Signal](../01-concepts/ontology-1-perception-layer.md#signal)
- [Ontology: Agent](../01-concepts/ontology-3-execution-layer.md#agent)
```

---

## 6. event-driven-operations.md — NEW

**Purpose:** Describe reactive, signal-triggered operational patterns.

**Outline:**

```markdown
# Event-Driven Operations

## What Are Event-Driven Operations?

Event-driven operations are triggered by events in the environment — system 
alerts, schedule triggers, threshold breaches, or external notifications — 
and require response within defined time constraints.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Trigger** | External event or condition |
| **Response** | Reactive, often time-sensitive |
| **Determinism** | Often starts deterministic, may branch |
| **Duration** | Varies — minutes to resolution |
| **Goal** | Handle the event appropriately |

### Examples

- Alert response
- Scheduled batch processing
- Threshold-triggered actions
- Webhook handling
- Scheduled reports

## Anatomy of Event-Driven Operations

### Event Flow
1. **Detection** — Event occurs in environment
2. **Signal** — Event communicated to system
3. **Evaluation** — Determine if response needed
4. **Response** — Execute appropriate action
5. **Resolution** — Event handled

### Event Types
- **System events** — Alerts, errors, state changes
- **Time events** — Schedules, deadlines, timers
- **Business events** — Transactions, approvals, exceptions
- **External events** — Webhooks, notifications, feeds

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Event | Signal |
| Event type matching | Trigger |
| Response definition | Scenario |
| Response instance | Request |
| Response execution | Procedure or Case |

### How Hub Models Event-Driven Operations

```

Event occurs in environment

↓

Signal received by Hub

↓

Trigger evaluates conditions

↓

Matching Scenario invoked

↓

Request created

↓

Appropriate response executed

```

## Related

- [Ontology: Signal](../01-concepts/ontology-1-perception-layer.md#signal)
- [Ontology: Trigger](../01-concepts/ontology-1-perception-layer.md#trigger)
```

---

## Implementation Tasks

| Task | Description |

|------|-------------|

| 1 | Rename `03-operations` folder to `03-information-centric-work` |

| 2 | Create `README.md` with pattern index |

| 3 | Refactor `case-management.md` → `case-based-work.md` |

| 4 | Create `queue-based-work.md` |

| 5 | Create `document-centric-work.md` |

| 6 | Create `conversation-based-work.md` |

| 7 | Create `event-driven-operations.md` |

| 8 | Update main `README.md` index (change 03-operations references) |

| 9 | Delete `08-operations` folder (move runbooks to `05-infrastructure/runbooks/`) |

---

## Document Style Guidelines

Each work pattern document follows this structure:

1. **What Is X Work?** — Plain-language description
2. **Characteristics** — Table of key dimensions
3. **Examples** — Industry-neutral examples
4. **Anatomy** — Lifecycle, participants, structure
5. **Mapping to Hub Ontology** — Table mapping pattern concepts to Hub concepts
6. **How Hub Models X** — Flow diagram (text-based)
7. **Related** — Links to ontology docs

**No subsystem references.** Documents refer only to:

- [Ontology Reference](olympus-hub-docs/01-concepts/ontology-reference.md)
- [Glossary](olympus-hub-docs/01-concepts/glossary.md)
- Specific ontology layer documents