# Case-Based Work

Case-based work is non-deterministic, evolving collaboration to resolve a situation. Unlike procedure-based work, the path forward is not known in advance — it emerges through investigation, judgment, and collaboration.

---

## What Is Case-Based Work?

A **case** represents a situation that requires investigation, analysis, and resolution by multiple agents working together. The distinguishing feature is that you cannot predetermine the exact steps — the work evolves based on what you discover.

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
- Compliance investigation
- Complex customer support issues

---

## Anatomy of Case-Based Work

### Lifecycle

```
1. Initiation
   A situation triggers the case — alert, complaint, request
        ↓
2. Investigation
   Agents gather information, form hypotheses
        ↓
3. Collaboration
   Multiple agents contribute perspectives, expertise
        ↓
4. Decision
   Resolution determined based on evidence and judgment
        ↓
5. Closure
   Case resolved, outcomes recorded, learnings captured
```

### Participants

| Role | Responsibility |
|------|----------------|
| **Case Coordinator** | Orchestrates the case; ensures progress without dictating path |
| **Domain Experts** | Contribute specialized knowledge relevant to the case |
| **Decision Makers** | Have authority to determine final resolution |
| **Observers** | Track progress, ensure compliance, may escalate |

### Case Context

Every case accumulates context as it progresses:

| Element | Purpose |
|---------|---------|
| **Case Record** | The evolving documentation of the case |
| **Evidence** | Information gathered during investigation |
| **Communication Log** | History of all collaboration |
| **Decision Trail** | How conclusions were reached and why |
| **Timeline** | Chronology of events and actions |

---

## Collaboration Surfaces for Cases

Cases naturally occur in different contexts, and agents may collaborate through various surfaces:

| Surface | Characteristics | Example |
|---------|-----------------|---------|
| **Conversation** | Real-time dialogue, quick decisions | Incident war room in chat |
| **Document** | Artifact-centered, iterative review | Investigation report |
| **Notebook** | Analytical, exploratory | Data investigation in Jupyter |
| **Ticket** | Structured, tracked | Support case in ticketing system |
| **Meeting** | Synchronous, multi-party | Case review meeting |

The same case may span multiple surfaces — conversation for quick decisions, documents for formal findings.

---

## Incident Response: A Case-Based Pattern

**Incident Response** is a prominent example of case-based work that combines event-driven triggers with collaborative investigation.

### Incident Response Lifecycle

```
Event occurs (alert, outage, breach)
        ↓
Incident declared (case initiated)
        ↓
Triage — assess severity, scope, impact
        ↓
Investigation — identify root cause
        ↓
Mitigation — contain and resolve
        ↓
Recovery — restore normal operations
        ↓
Post-Incident Review — learn and improve
```

### What Makes Incident Response Case-Based

| Aspect | Why It's Case-Based |
|--------|---------------------|
| **Path unknown** | You don't know what caused the incident until you investigate |
| **Multi-agent** | Multiple specialists collaborate (ops, security, dev, business) |
| **Evolving** | New information changes the direction of investigation |
| **Judgment required** | Decisions about severity, response, communication |
| **Resolution-oriented** | Goal is to resolve the incident, not follow a script |

---

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Situation that triggers case | Signal |
| Case type definition | Scenario |
| Case instance | Request |
| Case operation | Case (Execution Layer) |
| Work items within case | Tasks |
| Participants | Agents (Human, AI) |
| Evidence, documentation | Knowledge artifacts |
| Decisions | Activities with decision outcomes |
| Case resolution | Request completion |

### How Hub Models Case-Based Work

```
Signal (situation occurs)
    ↓
Trigger (matches case scenario)
    ↓
Scenario (defines case type, goals, roles)
    ↓
Request (case instance created)
    ↓
Case Operation (non-deterministic execution)
    ↓
Tasks created and assigned to Agents
    ↓
Agents collaborate, investigate, decide
    ↓
Activities complete with outcomes
    ↓
Request completes (case closed)
```

### Why Case-Based Work Suits Hub

| Hub Concept | Why It Fits |
|-------------|-------------|
| **Goal-oriented Scenarios** | Define what success looks like, not how to get there |
| **Agent collaboration** | Multiple agents work toward shared goal |
| **Request as collaboration surface** | Case accumulates history as it progresses |
| **Non-deterministic flow** | Case can branch, loop, escalate based on findings |
| **Memory** | Case context persists and accumulates |

---

## Case vs. Procedure vs. Workflow

| Dimension | Case | Procedure | Workflow |
|-----------|------|-----------|----------|
| **Determinism** | Non-deterministic | Deterministic | Deterministic |
| **Agents** | Multiple, collaborative | Single role | Multiple roles, sequential |
| **Path** | Emerges | Predefined | Predefined |
| **Exceptions** | Anticipated, handled | Errors | Handled or escalated |
| **Best for** | Investigation, judgment | Routine tasks | Cross-role handoffs |

---

## Related

- [Ontology: Case](../01-concepts/ontology-3-execution-layer.md#case)
- [Ontology: Procedure](../01-concepts/ontology-3-execution-layer.md#procedure)
- [Ontology: Workflow](../01-concepts/ontology-3-execution-layer.md#workflow)
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
- [Event-Driven Operations](./event-driven-operations.md) — Cases often start with events
