# Pattern Composition in Scenarios

> Scenarios rarely embody a single work pattern. Real-world operations are hybrids — a loan application starts in a queue, becomes an artifact under review, and may escalate to a case requiring investigation. Understanding how patterns compose is essential to modeling work accurately.

---

## The Core Insight

Traditional BPM models processes as **task sequences with routing logic**. Hub models work as **situations requiring attention**, where the *nature* of that attention — the pattern — may evolve as the work progresses.

This isn't a limitation to work around. It's a recognition that work doesn't respect clean categorical boundaries.

---

## Concepts

| Term | Definition |
|------|------------|
| **Work Pattern** | Fundamental archetype describing how attention is applied (queue, case, artifact, etc.) |
| **Scenario** | Hub's model of an operation — defines the goal, often composes multiple patterns |
| **Request** | A specific instance that may transition between patterns during its lifecycle |
| **Pattern Transition** | The shift from one pattern's attention style to another within the same Request |

---

## Why Patterns Compose

Work doesn't stay in one mode:

| Composition Type | What Happens | Example |
|------------------|--------------|---------|
| **Escalation** | Simple work becomes complex | Queue item → Case (investigation needed) |
| **Phases** | Work progresses through stages | Design work → Artifact work (after direction chosen) |
| **Nesting** | One pattern contains another | Case contains queue-based task assignments |
| **Parallel** | Multiple patterns active simultaneously | Artifact review + stakeholder conversation |
| **Fallback** | Primary pattern insufficient | Automated procedure → Human case handling |

---

## Detailed Examples

### Example 1: Loan Origination

A loan origination scenario demonstrates how work flows through multiple patterns as it progresses from intake to decision.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       LOAN ORIGINATION SCENARIO                         │
│                                                                         │
│   Signal: Application submitted                                         │
│   Goal: Decide loan eligibility and terms                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PHASE 1: INTAKE                    PHASE 2: PROCESSING                 │
│  ┌─────────────────────┐            ┌─────────────────────┐            │
│  │    QUEUE-BASED      │            │   ARTIFACT-CENTRIC  │            │
│  │                     │            │                     │            │
│  │  • Application      │     →      │  • Document         │            │
│  │    enters queue     │            │    completeness     │            │
│  │  • First-in         │            │  • Income           │            │
│  │    processing       │            │    verification     │            │
│  │  • SLA: 24 hours    │            │  • Asset            │            │
│  │    for assignment   │            │    documentation    │            │
│  └─────────────────────┘            └─────────────────────┘            │
│                                              │                          │
│                                              ▼                          │
│  PHASE 3: DECISION                  ┌─────────────────────┐            │
│  ┌─────────────────────┐            │    CASE-BASED       │            │
│  │    REVIEW-BASED     │            │                     │            │
│  │                     │     ←──    │  • Fraud suspicion  │            │
│  │  • Underwriter      │   (if      │  • Complex income   │            │
│  │    assessment       │  needed)   │  • Policy exception │            │
│  │  • Risk scoring     │            │  • Multiple parties │            │
│  │  • Terms decision   │            │                     │            │
│  └─────────────────────┘            └─────────────────────┘            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Pattern Transitions in Detail

| Transition | Trigger | What Changes |
|------------|---------|--------------|
| Queue → Artifact | Application assigned to processor | Focus shifts from "who handles this?" to "is the application complete?" |
| Artifact → Review | Documents verified | Focus shifts from "do we have what we need?" to "should we approve?" |
| Any → Case | Exception detected | Focus shifts to investigation; deterministic flow pauses |
| Case → Review | Investigation complete | Returns to decision flow with additional context |

#### Agent Behavior by Pattern

| Pattern Phase | Human Agent Focus | AI Agent Focus |
|--------------|-------------------|----------------|
| Queue-Based | Prioritization, escalation | Auto-assignment, SLA monitoring |
| Artifact-Centric | Document judgment, customer contact | Completeness checks, extraction, validation |
| Review-Based | Risk judgment, terms negotiation | Score calculation, policy verification |
| Case-Based | Investigation strategy, stakeholder management | Evidence correlation, similar case retrieval |

---

### Example 2: Product Development

Product development shows how creative/generative work transitions into structured artifact work.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     PRODUCT DEVELOPMENT SCENARIO                        │
│                                                                         │
│   Signal: Market opportunity identified                                 │
│   Goal: Deliver validated product increment                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PHASE 1: DISCOVERY          PHASE 2: DEFINITION                        │
│  ┌─────────────────────┐     ┌─────────────────────┐                   │
│  │  GENERATIVE/DESIGN  │     │   ARTIFACT-CENTRIC  │                   │
│  │                     │     │                     │                   │
│  │  • Explore problem  │  →  │  • PRD drafted      │                   │
│  │    space            │     │  • Spec refined     │                   │
│  │  • Generate         │     │  • Designs          │                   │
│  │    concepts         │     │    iterated         │                   │
│  │  • Create variants  │     │                     │                   │
│  │  • Select direction │     │                     │                   │
│  └─────────────────────┘     └─────────────────────┘                   │
│          ↑                           │                                  │
│          │                           ▼                                  │
│  ┌───────┴───────────────────────────────────────┐                     │
│  │            CONVERSATION-BASED                  │                     │
│  │   (Stakeholder alignment throughout)           │                     │
│  └───────────────────────────────────────────────┘                     │
│                                      │                                  │
│                                      ▼                                  │
│  PHASE 3: VALIDATION            PHASE 4: APPROVAL                       │
│  ┌─────────────────────┐        ┌─────────────────────┐                │
│  │    QUEUE-BASED      │        │    REVIEW-BASED     │                │
│  │                     │        │                     │                │
│  │  • Dev tasks        │   →    │  • Gate review      │                │
│  │    assigned         │        │  • Go/no-go         │                │
│  │  • Testing queued   │        │    decision         │                │
│  │  • Bug backlog      │        │                     │                │
│  └─────────────────────┘        └─────────────────────┘                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Why This Composition Matters

| Pattern | Why It's Needed | What Happens Without It |
|---------|-----------------|-------------------------|
| Generative/Design | Explore solution space before committing | Premature convergence, missed opportunities |
| Artifact-Centric | Crystallize decisions into reviewable form | Alignment lost, scope creep |
| Conversation-Based | Maintain stakeholder alignment | Surprises at gate reviews |
| Queue-Based | Manage development work capacity | Resource conflicts, unpredictable delivery |
| Review-Based | Formal go/no-go evaluation | Unclear accountability, quality gaps |

---

### Example 3: Incident Response

Incident response shows reactive work that may escalate through multiple patterns.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      INCIDENT RESPONSE SCENARIO                         │
│                                                                         │
│   Signal: Monitoring alert triggered                                    │
│   Goal: Restore service, prevent recurrence                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PHASE 1: DETECTION             PHASE 2: TRIAGE                         │
│  ┌─────────────────────┐        ┌─────────────────────┐                │
│  │    EVENT-DRIVEN     │        │    REVIEW-BASED     │                │
│  │                     │        │                     │                │
│  │  • Alert fires      │   →    │  • Severity         │                │
│  │  • Auto-enrichment  │        │    assessment       │                │
│  │  • Initial          │        │  • Impact scope     │                │
│  │    correlation      │        │  • Escalation       │                │
│  │                     │        │    decision         │                │
│  └─────────────────────┘        └─────────────────────┘                │
│                                          │                              │
│                    ┌─────────────────────┼─────────────────────┐       │
│                    ▼                     ▼                     ▼       │
│  ┌─────────────────────┐   ┌─────────────────────┐   ┌──────────────┐ │
│  │    QUEUE-BASED      │   │     CASE-BASED      │   │ CONVERSATION │ │
│  │    (Low severity)   │   │    (High severity)  │   │    -BASED    │ │
│  │                     │   │                     │   │              │ │
│  │  • Enters backlog   │   │  • War room         │   │ • Customer   │ │
│  │  • Standard         │   │  • Investigation    │   │   comms      │ │
│  │    remediation      │   │  • Multi-team       │   │ • Exec       │ │
│  │                     │   │    coordination     │   │   updates    │ │
│  └─────────────────────┘   └─────────────────────┘   └──────────────┘ │
│                                          │                              │
│                                          ▼                              │
│  PHASE 4: CLOSURE                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      REVIEW-BASED (PIR)                          │   │
│  │  • Root cause documented  • Prevention actions identified        │   │
│  │  • Timeline reviewed      • Process improvements proposed        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                          │                              │
│                                          ▼                              │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                  QUEUE-BASED (Remediation Tasks)                 │   │
│  │  • Prevention tasks created  • Assigned to teams  • Tracked     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Parallel Patterns

In incident response, multiple patterns often run simultaneously:

| Pattern | Runs Concurrently With | Coordination Need |
|---------|------------------------|-------------------|
| Case-Based (investigation) | Conversation-Based (comms) | Investigation findings inform communication |
| Case-Based (investigation) | Queue-Based (immediate fixes) | Quick wins don't wait for root cause |
| Review-Based (PIR) | Queue-Based (remediation) | PIR may generate additional remediation tasks |

---

### Example 4: Customer Onboarding

Customer onboarding shows a journey that combines multiple patterns with clear handoffs.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     CUSTOMER ONBOARDING SCENARIO                        │
│                                                                         │
│   Signal: Contract signed                                               │
│   Goal: Customer successfully using product                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────┐     ┌─────────────────────┐                   │
│  │    QUEUE-BASED      │     │   ARTIFACT-CENTRIC  │                   │
│  │                     │     │                     │                   │
│  │  • Provisioning     │  →  │  • Account setup    │                   │
│  │    tasks            │     │    document         │                   │
│  │  • License          │     │  • Configuration    │                   │
│  │    activation       │     │    spec             │                   │
│  └─────────────────────┘     └─────────────────────┘                   │
│                                      │                                  │
│                                      ▼                                  │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    CASE-BASED (The Customer)                     │   │
│  │   • Customer is the "case" — all activities relate to them      │   │
│  │   • Non-deterministic: different customers need different paths │   │
│  │   • Collaborative: multiple teams involved                      │   │
│  │                                                                  │   │
│  │   Contains:                                                      │   │
│  │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │   │
│  │   │ QUEUE-BASED │  │CONVERSATION │  │  ARTIFACT   │             │   │
│  │   │             │  │   -BASED    │  │  -CENTRIC   │             │   │
│  │   │ Training    │  │             │  │             │             │   │
│  │   │ sessions    │  │ Support     │  │ Custom      │             │   │
│  │   │             │  │ calls       │  │ docs        │             │   │
│  │   └─────────────┘  └─────────────┘  └─────────────┘             │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                      │                                  │
│                                      ▼                                  │
│  ┌─────────────────────┐     ┌─────────────────────┐                   │
│  │    REVIEW-BASED     │     │    EVENT-DRIVEN     │                   │
│  │                     │     │                     │                   │
│  │  • Readiness        │  →  │  • Usage monitors   │                   │
│  │    assessment       │     │  • Health signals   │                   │
│  │  • Go-live          │     │  • Renewal          │                   │
│  │    approval         │     │    triggers         │                   │
│  └─────────────────────┘     └─────────────────────┘                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Resolution Models Within Compositions

Pattern compositions can include fully automated segments. Different phases of a composition may be at different stages of the Novel → Automatable spectrum.

**Example: Loan Origination**

In Loan Origination, the Queue-Based intake and Artifact-Centric document processing might be fully automated, with agents engaging only at Review-Based decision points:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    LOAN ORIGINATION RESOLUTION MODELS                   │
│                                                                         │
│  PHASE 1: INTAKE                    PHASE 2: PROCESSING                 │
│  ┌─────────────────────┐            ┌─────────────────────┐            │
│  │  PURE AUTOMATION    │            │  PURE AUTOMATION    │            │
│  │                     │            │                     │            │
│  │  • Queue assignment │     →      │  • Document         │            │
│  │  • Data validation  │            │    extraction       │            │
│  │  • Routing logic    │            │  • Completeness     │            │
│  └─────────────────────┘            │    checks           │            │
│                                      └─────────────────────┘            │
│                                              │                          │
│                                              ▼                          │
│  PHASE 3: DECISION                  ┌─────────────────────┐            │
│  ┌─────────────────────┐            │  HUMAN-AI TEAMING    │            │
│  │  HUMAN-SUPERVISED   │            │                     │            │
│  │        AI           │     ←──    │  • Fraud            │            │
│  │                     │   (if      │    investigation    │            │
│  │  • AI risk scoring  │  needed)   │  • Complex income   │            │
│  │  • Human approval   │            │    analysis         │            │
│  │    required         │            │                     │            │
│  └─────────────────────┘            └─────────────────────┘            │
└─────────────────────────────────────────────────────────────────────────┘
```

**Key insight:** Agent involvement is at specific points, not throughout. The composition shows:
- **M2M segments** where machines handle routine work
- **Agent touchpoints** where judgment, exceptions, or novel situations require cognitive faculties

Different phases of a composition may be at different stages of the evolution from Novel → Understood → Automatable. As work matures, more phases may become automatable, but the composition structure remains.

---

## Modeling Implications

### For Process Architects

When designing a Scenario, ask:

1. **What pattern does work enter as?** 
   - Often Queue-Based (work arrives) or Event-Driven (something triggers)

2. **What pattern does the core work follow?**
   - Often Case-Based (investigation) or Artifact-Centric (creation)

3. **What patterns emerge at decision points?**
   - Often Review-Based (evaluation before proceeding)

4. **What triggers pattern transitions?**
   - Completeness thresholds, exceptions, time boundaries, human decisions

5. **What patterns run in parallel?**
   - Communication often runs alongside core work

### For Developers

Hub Applications may need to:

- **Support multiple work structures** within one Scenario
- **Handle transitions gracefully** — a queue item becoming a case shouldn't require data migration
- **Provide appropriate UI** per active pattern — queue views vs. case workspaces vs. artifact editors
- **Enable pattern-appropriate agent support** — different AI capabilities for different patterns

### For AI Agents

Different patterns require different reasoning modes:

| Pattern | Reasoning Style | AI Focus |
|---------|-----------------|----------|
| Queue-Based | Procedural, efficient | Throughput optimization, SLA prediction |
| Case-Based | Exploratory, evidence-based | Hypothesis generation, correlation |
| Artifact-Centric | Constructive, iterative | Content generation, consistency checking |
| Review-Based | Evaluative, criteria-driven | Assessment against standards, gap identification |
| Generative/Design | Divergent, creative | Option generation, variant comparison |
| Conversation-Based | Responsive, contextual | Intent understanding, solution recommendation |
| Event-Driven | Reactive, diagnostic | Pattern recognition, impact prediction |

---

## The BPM Contrast

| BPM Approach | Hub Approach |
|--------------|--------------|
| Define task flow upfront | Define goal; patterns emerge from situation |
| Routing logic determines path | Scenario evaluates what attention is needed |
| Exception = alternate path in same model | Exception = pattern shift (queue → case) |
| Process redesign for change | Pattern composition adapts dynamically |
| Single workflow engine | Pattern-appropriate execution |

---

## Pattern Composition Principles

1. **Patterns are lenses, not containers** — The same work can be viewed through multiple pattern lenses simultaneously

2. **Transitions are meaningful** — A pattern shift signals a change in how attention should be applied

3. **Composition is hierarchical** — Cases can contain queues; artifacts can require reviews

4. **The Scenario is the unity** — While patterns may shift, the Scenario's goal remains constant

5. **Agents adapt to patterns** — Both human and AI agents should recognize which pattern is active and adjust behavior

---

## Related

- [Queue-Based Work](./queue-based-work.md)
- [Case-Based Work](./case-based-work.md)
- [Conversation-Based Work](./conversation-based-work.md)
- [Event-Driven Operations](./event-driven-operations.md)
- [Artifact-Centric Work](./artifact-centric-work.md)
- [Review-Based Work](./review-based-work.md)
- [Generative/Design Work](./generative-design-work.md)
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
- [Ontology: Execution Layer](../01-concepts/ontology-3-execution-layer.md)
