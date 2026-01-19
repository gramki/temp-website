# Artifact-Centric Work

Artifact-centric work is organized around the creation, review, and evolution of a single artifact — a document, design, specification, or code. The artifact is the center of attention, and the work follows its lifecycle from draft to approval.

---

## What Is Artifact-Centric Work?

In artifact-centric work, the goal is to produce an artifact that meets quality and approval criteria. Work progresses through a lifecycle: drafting, reviewing, revising, and approving. The artifact evolves through iterations until it's ready.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Center** | A single artifact that evolves |
| **Collaboration** | Multiple contributors and reviewers |
| **Duration** | Days to weeks |
| **State** | Draft → Review → Revision → Approved |
| **Goal** | Artifact meeting quality/approval criteria |

### Examples

- PRD (Product Requirements Document) creation
- Design document development
- Code development and review
- Contract drafting and negotiation
- Policy document creation
- Report generation
- Specification authoring

---

## Anatomy of Artifact-Centric Work

### Lifecycle

```
1. Initiation
   Need for artifact identified
        ↓
2. Drafting
   Initial version created by author
        ↓
3. Review
   Feedback gathered from reviewers
        ↓
4. Revision
   Changes incorporated based on feedback
        ↓
   (Repeat Review → Revision as needed)
        ↓
5. Approval
   Final sign-off from approvers
        ↓
6. Publication
   Artifact released for use
```

### Participant Roles

| Role | Responsibility |
|------|----------------|
| **Author** | Creates and revises the artifact |
| **Reviewer** | Provides feedback on quality, correctness, completeness |
| **Approver** | Authorizes the final version |
| **Consumer** | Uses the approved artifact |
| **Stakeholder** | Provides input, requirements, constraints |

### Artifact States

| State | Description |
|-------|-------------|
| **Draft** | Work in progress, not ready for review |
| **In Review** | Submitted for feedback |
| **Revising** | Being updated based on feedback |
| **Approved** | Ready for use |
| **Published** | Released and accessible |
| **Archived** | Superseded or no longer active |

---

## Contrast with Generative/Design Work

| Artifact-Centric | Generative/Design |
|------------------|-------------------|
| One artifact iterated | Multiple variants created |
| Feedback → revision | Evaluation → selection |
| Linear progression (mostly) | Exploration → convergence |
| Goal: approved artifact | Goal: chosen direction |

**When to use which:**
- **Artifact-Centric:** You know what you're building; need to refine it
- **Generative/Design:** You're exploring options; need to discover what to build

Often, generative work produces a direction, which then becomes artifact-centric as you develop the chosen approach.

---

## Version Control and History

Artifact-centric work generates a history:

| Element | Purpose |
|---------|---------|
| **Versions** | Named snapshots of the artifact |
| **Change History** | What changed between versions |
| **Review Comments** | Feedback at each review cycle |
| **Approval Records** | Who approved what version |

This history is valuable for:
- Understanding how the artifact evolved
- Auditing decisions
- Rolling back if needed
- Learning from past work

---

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Need for artifact | Signal |
| Artifact type/process | Scenario |
| Artifact lifecycle instance | Request |
| The artifact itself | Entity attached to Request |
| Drafting | Activity (author Task) |
| Review round | Activity (reviewer Tasks) |
| Feedback | Task outcomes |
| Approval | Activity with decision outcome |
| Published artifact | Request completion with artifact |

### How Hub Models Artifact-Centric Work

```
Signal (artifact needed)
    ↓
Trigger (matches artifact type)
    ↓
Scenario (defines artifact lifecycle)
    ↓
Request (artifact instance)
    ↓
Task: Drafting (assigned to Author)
    ↓
Author creates artifact draft
    ↓
Task: Review (assigned to Reviewers)
    ↓
Reviewers provide feedback
    ↓
Task: Revision (back to Author)
    ↓
(Repeat Review → Revision as needed)
    ↓
Task: Approval (assigned to Approvers)
    ↓
Approvers sign off
    ↓
Request completes with approved artifact
```

### Why Artifact-Centric Work Suits Hub

| Hub Concept | Why It Fits |
|-------------|-------------|
| **Request as lifecycle** | Request tracks artifact through states |
| **Entity attachment** | Artifact attached to Request |
| **Tasks for stages** | Each lifecycle stage is a Task |
| **Role-based assignment** | Author, Reviewer, Approver roles |
| **Memory** | History of changes, feedback, decisions |

---

## Common Patterns

### Serial Review
```
Author → Reviewer 1 → Revise → Reviewer 2 → Revise → Approver
```

### Parallel Review
```
Author → [Reviewer 1, Reviewer 2, Reviewer 3] → Consolidate → Revise → Approver
```

### Staged Approval
```
Author → Technical Review → Revise → Business Review → Revise → Final Approval
```

Hub supports all these patterns through Task configuration and workflow.

---

## Related

- [Ontology: Workflow](../01-concepts/ontology-3-execution-layer.md#workflow)
- [Review-Based Work](./review-based-work.md) — Review is often part of artifact lifecycle
- [Generative/Design Work](./generative-design-work.md) — Exploration before artifact development
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
