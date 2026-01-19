# Review-Based Work

Review-based work focuses on evaluation and judgment — assessing the quality, correctness, compliance, or effectiveness of artifacts, decisions, or outcomes. The goal is to render a judgment with rationale.

---

## What Is Review-Based Work?

In review-based work, something already exists (an artifact, a decision, an outcome, a past event) and must be evaluated. Reviewers apply criteria to determine quality, correctness, or approval.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Purpose** | Evaluation, not creation |
| **Inputs** | Artifact, decision, or outcome to review |
| **Output** | Assessment, approval/rejection, feedback |
| **Agents** | Reviewers with relevant expertise |
| **Goal** | Judgment rendered with rationale |

### Examples

- Code review
- Document review and approval
- Post-incident review (PIR)
- Performance review
- Audit and compliance review
- Design review
- Security review
- Quality assurance

---

## Anatomy of Review-Based Work

### Review Lifecycle

```
1. Review Requested
   Item identified for review
        ↓
2. Context Gathered
   Relevant information assembled
        ↓
3. Evaluation
   Reviewers assess against criteria
        ↓
4. Feedback
   Findings documented
        ↓
5. Determination
   Approve, reject, or request changes
        ↓
6. Resolution
   Review closed with outcome
```

### Participant Roles

| Role | Responsibility |
|------|----------------|
| **Requester** | Submits item for review |
| **Reviewer** | Evaluates against criteria |
| **Approver** | Has authority to approve/reject |
| **Author** | May respond to feedback (if artifact) |

### Review Types

| Type | What's Reviewed | Criteria | Examples |
|------|-----------------|----------|----------|
| **Quality** | Artifacts | Standards, best practices | Code review, document review |
| **Compliance** | Processes, decisions | Regulatory requirements | Audit, policy review |
| **Retrospective** | Past work/incidents | What happened, what to learn | PIR, sprint retro |
| **Approval** | Artifacts, requests | Authority to proceed | Change approval, sign-off |
| **Assessment** | People, performance | Skills, outcomes | Performance review, interview |

---

## Review Outcomes

| Outcome | Description |
|---------|-------------|
| **Approved** | Meets criteria, can proceed |
| **Rejected** | Does not meet criteria, cannot proceed |
| **Approved with conditions** | Proceed with noted exceptions |
| **Changes requested** | Revise and resubmit |
| **Deferred** | Not ready to decide |

---

## Post-Incident Review (PIR): A Case Study

PIR (Post-Incident Review) is a prominent example of review-based work focused on learning from incidents.

### PIR Lifecycle

```
Incident resolved
        ↓
PIR scheduled (timeline established)
        ↓
Context gathered (timeline, actions, decisions)
        ↓
Review meeting (what happened, why, impact)
        ↓
Findings documented
        ↓
Action items identified
        ↓
PIR report published
        ↓
Action items tracked to completion
```

### What Makes PIR Review-Based

| Aspect | Review Nature |
|--------|---------------|
| **Focus** | Evaluate past incident handling |
| **Criteria** | What could be improved |
| **Output** | Findings, action items |
| **Goal** | Organizational learning |

---

## Review vs. Artifact-Centric

| Dimension | Review-Based | Artifact-Centric |
|-----------|--------------|------------------|
| **Primary activity** | Evaluation | Creation |
| **Input** | Something that exists | Need for something new |
| **Output** | Judgment, feedback | Artifact |
| **Goal** | Assess quality/correctness | Produce approved artifact |

**Relationship:** Review is often *part* of artifact-centric work (the review stage), but review-based work can stand alone (PIR, audit, assessment).

---

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Review request | Signal → Scenario |
| Review instance | Request |
| Item under review | Entity attached to Request |
| Reviewer | Agent with reviewer Role |
| Evaluation criteria | Goals, SOPs in Normative Layer |
| Feedback | Task outcomes, comments |
| Review decision | Activity with decision outcome |
| Action items | Follow-up Tasks or Requests |

### How Hub Models Review-Based Work

```
Signal (review requested)
    ↓
Trigger (matches review type)
    ↓
Scenario (defines review process)
    ↓
Request (review instance)
    ↓
Item to review attached as Entity
    ↓
Tasks assigned to Reviewers
    ↓
Evaluation against criteria
    ↓
Findings documented as outcomes
    ↓
Determination made (approve/reject/request changes)
    ↓
Request completes with decision
```

### Why Review-Based Work Suits Hub

| Hub Concept | Why It Fits |
|-------------|-------------|
| **Scenario as review type** | Different reviews have different processes |
| **Request tracks review** | History of evaluation, feedback, decision |
| **Tasks for reviewers** | Assign evaluation work |
| **Decision as outcome** | Formal approval/rejection recorded |
| **Follow-up Requests** | Action items become new work |

---

## Multi-Reviewer Patterns

| Pattern | Description |
|---------|-------------|
| **Serial** | Reviewers evaluate in sequence |
| **Parallel** | Multiple reviewers evaluate simultaneously |
| **Consensus** | All must agree |
| **Majority** | Most must agree |
| **Designated** | One person has final authority |

Hub supports all patterns through Task configuration.

---

## Related

- [Ontology: Activity](../01-concepts/ontology-3-execution-layer.md#activity)
- [Ontology: Decision](../01-concepts/ontology-2-normative-layer.md#decision)
- [Artifact-Centric Work](./artifact-centric-work.md) — Reviews are often part of artifact lifecycle
- [Case-Based Work](./case-based-work.md) — PIR often involves case-like investigation
