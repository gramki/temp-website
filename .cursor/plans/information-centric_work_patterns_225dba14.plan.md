---
name: Information-Centric Work Patterns
overview: Rename 03-operations to 03-information-centric-work and populate with 7 work pattern documents describing prominent information-centric work patterns and their mapping to Hub ontology concepts.
todos:
  - id: rename-folder
    content: Rename 03-operations to 03-information-centric-work
    status: completed
  - id: create-readme
    content: Create README.md with pattern index and introduction
    status: completed
  - id: refactor-case
    content: Refactor case-management.md to case-based-work.md with Incident Response example
    status: completed
  - id: create-queue
    content: Create queue-based-work.md
    status: completed
  - id: create-artifact
    content: Create artifact-centric-work.md
    status: completed
  - id: create-conversation
    content: Create conversation-based-work.md
    status: completed
  - id: create-event
    content: Create event-driven-operations.md
    status: completed
  - id: create-review
    content: Create review-based-work.md
    status: completed
  - id: create-generative
    content: Create generative-design-work.md
    status: completed
  - id: update-main-readme
    content: Update main README.md index references
    status: completed
  - id: cleanup-08-operations
    content: Move 08-operations/runbooks to 05-infrastructure and delete folder
    status: completed
---

# Information-Centric Work Patterns

Rename `03-operations` to `03-information-centric-work` and create documentation for 7 prominent work patterns, each describing the pattern and how it maps to Hub ontology concepts — without referencing subsystems.

---

## Folder Structure

```
03-information-centric-work/
├── README.md                        # Overview and pattern index
├── queue-based-work.md              # Task stream processing
├── case-based-work.md               # Investigation/resolution (includes Incident Response)
├── conversation-based-work.md       # Dialogue-centered
├── event-driven-operations.md       # Signal-triggered
├── artifact-centric-work.md         # Single artifact lifecycle
├── review-based-work.md             # Evaluation/assessment
└── generative-design-work.md        # Exploration, variants, selection
```

---

## Pattern Summary

| # | Pattern | Focus | Key Characteristic |

|---|---------|-------|-------------------|

| 1 | Queue-Based | Throughput | Serial processing of work items |

| 2 | Case-Based | Investigation | Non-deterministic collaborative resolution |

| 3 | Conversation-Based | Dialogue | Real-time exchange toward understanding |

| 4 | Event-Driven | Reaction | Signal-triggered response |

| 5 | Artifact-Centric | Creation | Single artifact: draft → review → approve |

| 6 | Review-Based | Evaluation | Assessing artifacts, decisions, outcomes |

| 7 | Generative/Design | Exploration | Diverge → variants → select → converge |

---

## 1. README.md — Section Overview

**Outline:**

```markdown
# Information-Centric Work Patterns

## Purpose
Describes prominent patterns of information-centric work and how they 
map to Hub's ontology.

## Pattern Index
Table of 7 patterns with characteristics and key ontology mappings.

## How Patterns Relate to Hub Ontology
Diagram: Work Pattern → Scenario → (Procedure | Workflow | Case) → Tasks → Agents

## Related
- Glossary: Information-Centric Work, Operation, Scenario
- Ontology Reference
```

---

## 2. queue-based-work.md

**Focus:** Task stream processing with SLAs and assignment logic.

**Key sections:**

- What Is Queue-Based Work? (characteristics, examples)
- Anatomy: Queue, assignment patterns, processing flow
- Mapping to Hub Ontology: Signal → Scenario → Task Queue → Agent
- Examples: Customer service tickets, claims processing, transaction reconciliation

---

## 3. case-based-work.md

**Focus:** Non-deterministic, evolving collaboration to resolve a situation.

**Key sections:**

- What Is Case-Based Work? (characteristics, examples)
- Anatomy: Lifecycle, participants, case context
- Mapping to Hub Ontology: Signal → Scenario → Request (Case) → Agent collaboration
- Collaboration surfaces: Conversation, document, notebook, ticket
- **Incident Response as Example:** Event triggers → investigation → resolution → learning

---

## 4. conversation-based-work.md

**Focus:** Dialogue-centered, real-time collaborative problem-solving.

**Key sections:**

- What Is Conversation-Based Work? (characteristics, examples)
- Anatomy: Opening, exploration, resolution, closing
- Mapping to Hub Ontology: Message as Signal, participant as Agent
- Examples: Support chat, troubleshooting, sales qualification, consultation

---

## 5. event-driven-operations.md

**Focus:** Reactive, signal-triggered operational response.

**Key sections:**

- What Are Event-Driven Operations? (characteristics, examples)
- Anatomy: Detection → Signal → Evaluation → Response → Resolution
- Event types: System, time, business, external
- Mapping to Hub Ontology: Event as Signal, Trigger evaluation, Scenario invocation
- Examples: Alert response, scheduled processing, threshold-triggered actions

---

## 6. artifact-centric-work.md

**Focus:** Work centered on creation and iteration of a single artifact.

**Key sections:**

- What Is Artifact-Centric Work? (characteristics, examples)
- Anatomy: Initiation → Drafting → Review → Revision → Approval → Publication
- Roles: Author, Reviewer, Approver, Consumer
- Mapping to Hub Ontology: Artifact as entity, lifecycle as Scenario, review as Task
- Examples: PRD creation, contract negotiation, report generation, code development

**Contrast with Generative/Design:** Artifact-centric iterates one artifact; generative creates variants and selects.

---

## 7. review-based-work.md — NEW

**Focus:** Evaluating artifacts, decisions, or outcomes to produce assessments.

**Outline:**

```markdown
# Review-Based Work

## What Is Review-Based Work?
Work focused on evaluation and judgment — assessing quality, correctness, 
compliance, or effectiveness of artifacts, decisions, or outcomes.

### Characteristics
| Dimension | Description |
|-----------|-------------|
| Purpose | Evaluation, not creation |
| Inputs | Artifact, decision, or outcome to review |
| Output | Assessment, approval/rejection, feedback |
| Agents | Reviewers with relevant expertise |
| Goal | Judgment rendered with rationale |

### Examples
- Code review
- Document review and approval
- Post-incident review (PIR)
- Performance review
- Audit and compliance review
- Design review

## Anatomy of Review-Based Work

### Lifecycle
1. Review requested — artifact/decision identified for review
2. Context gathered — relevant information assembled
3. Evaluation — reviewers assess against criteria
4. Feedback — findings documented
5. Determination — approve, reject, or request changes
6. Resolution — review closed with outcome

### Review Types
| Type | What's Reviewed | Criteria |
|------|-----------------|----------|
| Quality | Artifacts | Standards, best practices |
| Compliance | Processes, decisions | Regulatory requirements |
| Retrospective | Past work/incidents | What happened, what to learn |
| Approval | Artifacts, requests | Authority to proceed |

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Review request | Signal → Scenario |
| Review instance | Request |
| Item under review | Entity attached to Request |
| Reviewer | Agent with reviewer Role |
| Evaluation criteria | Goals, SOPs in Normative Layer |
| Review decision | Activity outcome |

### How Hub Models Review-Based Work

Signal (review requested)
    ↓
Scenario (review type)
    ↓
Request (review instance)
    ↓
Tasks assigned to Reviewers
    ↓
Evaluation against criteria
    ↓
Determination recorded
    ↓
Request completes

## Related
- Ontology: Activity, Decision
- Case-Based Work (PIR often becomes a case)
```

---

## 8. generative-design-work.md — NEW

**Focus:** Exploratory work that creates variants and selects among them.

**Outline:**

```markdown
# Generative/Design Work

## What Is Generative/Design Work?
Creative, exploratory work that generates multiple possibilities and 
converges on a selected direction through evaluation and elimination.

### Characteristics
| Dimension | Description |
|-----------|-------------|
| Approach | Divergent → Convergent |
| Artifacts | Multiple variants created |
| Selection | Choose/discard rather than iterate-in-place |
| Agents | Creators, evaluators, decision-makers |
| Goal | Arrive at a viable direction/solution |

### Contrast with Artifact-Centric
| Artifact-Centric | Generative/Design |
|------------------|-------------------|
| One artifact iterated | Multiple variants created |
| Feedback → revision | Evaluation → selection |
| Linear progression | Exploration → convergence |
| Goal: approved artifact | Goal: chosen direction |

### Examples
- Software design (multiple approaches explored)
- Product design (prototypes created, tested, selected)
- Strategy development (options analyzed, direction chosen)
- Architecture decisions (alternatives evaluated)
- Creative work (drafts, concepts, selection)

## Anatomy of Generative/Design Work

### Lifecycle
1. Problem framing — Define what needs to be solved
2. Exploration — Generate multiple approaches/variants
3. Prototyping — Develop variants sufficiently to evaluate
4. Evaluation — Assess variants against criteria
5. Selection — Choose direction, discard alternatives
6. Refinement — Develop selected approach (may become artifact-centric)

### Participant Roles
- Creators — Generate variants
- Evaluators — Assess against criteria
- Decision-makers — Select direction
- Stakeholders — Provide constraints and feedback

### Variant Management
- Multiple parallel tracks
- Some variants discarded early
- Some variants merged
- Final selection may combine elements

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Design challenge | Signal → Scenario |
| Design effort | Request (parent) |
| Variants | Sub-requests or Tasks |
| Evaluation criteria | Goals in Normative Layer |
| Selection decision | Activity with decision outcome |
| Chosen direction | Request outcome |

### How Hub Models Generative/Design Work

Signal (design challenge identified)
    ↓
Scenario (design type)
    ↓
Request (design effort)
    ↓
Multiple Tasks: create variants
    ↓
Agents develop variants
    ↓
Evaluation Tasks: assess variants
    ↓
Selection Decision
    ↓
Request completes with chosen direction

## Related
- Ontology: Decision, Goal
- Review-Based Work (evaluation phase)
- Artifact-Centric Work (refinement phase)
```

---

## Implementation Tasks

| # | Task | Description |

|---|------|-------------|

| 1 | Rename folder | `03-operations` → `03-information-centric-work` |

| 2 | Create README | Pattern index and introduction |

| 3 | Refactor case-based | `case-management.md` → `case-based-work.md` with Incident Response example |

| 4 | Create queue-based | `queue-based-work.md` |

| 5 | Create artifact-centric | `artifact-centric-work.md` (was document-centric) |

| 6 | Create conversation-based | `conversation-based-work.md` |

| 7 | Create event-driven | `event-driven-operations.md` |

| 8 | Create review-based | `review-based-work.md` |

| 9 | Create generative-design | `generative-design-work.md` |

| 10 | Update main README | Change `03-operations` references to `03-information-centric-work` |

| 11 | Cleanup 08-operations | Move `runbooks/` to `05-infrastructure/` and delete folder |

---

## Document Style

Each pattern document follows this structure:

1. **What Is X Work?** — Plain-language description
2. **Characteristics** — Table of key dimensions
3. **Examples** — Industry-neutral examples
4. **Anatomy** — Lifecycle, participants, structure
5. **Mapping to Hub Ontology** — Table mapping pattern → Hub concepts
6. **How Hub Models X** — Text-based flow diagram
7. **Related** — Links to ontology docs only (no subsystem references)