# Process Architect Primer: Hub as Your BPM Solution

> **Audience:** Process Architects, Business Analysts, and BPM practitioners evaluating Hub for capturing business process requirements and automating them.

---

## Executive Summary

**Olympus Hub** provides a modern approach to business process management where processes become **executable Scenarios** that combine human expertise with AI capabilities. Unlike traditional BPM tools, Hub treats operations holistically—capturing not just the workflow, but the roles, goals, decisions, and knowledge needed for effective execution.

**Key Value:** Your process designs become living, executable operations with built-in flexibility for human judgment and AI assistance.

---

## The BPM Challenges You Face

### The Gap Between Design and Execution

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TRADITIONAL BPM CHALLENGE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DESIGN PHASE                         EXECUTION REALITY                     │
│   ────────────                         ─────────────────                     │
│                                                                              │
│   ┌─────────────────────┐             ┌─────────────────────┐               │
│   │  Process Diagram    │             │  Real Exceptions    │               │
│   │  (Happy Path)       │             │  Not in Model       │               │
│   └─────────────────────┘             └─────────────────────┘               │
│                                                                              │
│   ┌─────────────────────┐             ┌─────────────────────┐               │
│   │  Rigid Workflow     │             │  Human Judgment     │               │
│   │  Steps              │             │  Needed             │               │
│   └─────────────────────┘             └─────────────────────┘               │
│                                                                              │
│   ┌─────────────────────┐             ┌─────────────────────┐               │
│   │  Document-Based     │             │  Tribal Knowledge   │               │
│   │  SOPs               │             │  Rules              │               │
│   └─────────────────────┘             └─────────────────────┘               │
│                                                                              │
│   Pain Points:                                                               │
│   • Processes are too rigid or too vague                                    │
│   • Edge cases fall outside the model                                       │
│   • Human expertise isn't captured in the system                            │
│   • AI can't participate meaningfully                                       │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## How Hub Approaches Process Management

### Scenarios, Not Just Workflows

Hub introduces the concept of **Scenarios** — recognizable operational situations that need response. Unlike rigid workflows, Scenarios define:

| Element | What It Captures |
|---------|------------------|
| **Roles** | Who is responsible (not just "a user") |
| **Goals** | What outcomes we're trying to achieve |
| **SOPs** | How to handle the situation |
| **Decision Criteria** | How to make judgment calls |
| **Compliance** | Regulatory requirements |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SCENARIO = COMPLETE OPERATIONAL CONTEXT                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   Scenario: "Standard Dispute Resolution"                                    │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  NORMATIVE (What ought to be done)                                   │   │
│   │                                                                      │   │
│   │  Roles:           Goals:                 SOPs:                       │   │
│   │  • Dispute Analyst • Resolve in 72h     • SOP-Investigation         │   │
│   │  • Supervisor      • Fair decision      • SOP-Communication          │   │
│   │                    • Document findings  • SOP-Decision               │   │
│   │                                                                      │   │
│   │  Decision Criteria:                     Compliance:                  │   │
│   │  • Liability matrix                     • Reg E requirements        │   │
│   │  • Evidence requirements                • 10-day provisional credit  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  AUTOMATION (How it's codified)                                      │   │
│   │                                                                      │   │
│   │  Hub Application:  Triggers:              Tools:                     │   │
│   │  • dispute-handler • dispute.filed        • transaction-lookup      │   │
│   │                    • document.uploaded    • customer-notification    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  DEPLOYMENT (How it's operationalized)                               │   │
│   │                                                                      │   │
│   │  Queues:            SLAs:                Agents:                     │   │
│   │  • tier-1-disputes  • 72h completion     • dispute-analysts pool    │   │
│   │  • supervisor-queue • 48h warning        • AI dispute agent         │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Value for Process Architects

### 1. Express Process Intent, Not Just Steps

| Traditional BPM | Hub Approach |
|-----------------|--------------|
| "Task 1 → Task 2 → Decision → Task 3" | "Analyst should investigate, document findings, and recommend resolution" |
| Rigid sequence | Goal-directed with flexibility |
| Hard to accommodate exceptions | Built-in escalation and judgment |

### 2. Capture the Complete Picture

**Your process documentation becomes executable:**

```yaml
# Scenario Normative Specification (Your Design)
scenario:
  name: standard-dispute
  
  roles:
    - name: dispute-analyst
      goals:
        - "Investigate dispute within 24 hours"
        - "Document all findings"
        - "Make fair determination"
      responsibilities:
        - "Review transaction history"
        - "Contact customer for clarification"
        - "Gather evidence from merchant"
        
  sops:
    - ref: sop-dispute-investigation
    - ref: sop-customer-communication
    
  decision_criteria:
    - name: liability-determination
      description: "How to determine who bears liability"
      document_ref: dispute-liability-matrix
      
  evidence_requirements:
    - type: transaction-history
      mandatory: true
    - type: customer-statement
      mandatory: true
    - type: merchant-response
      mandatory: false
```

### 3. Enable Human-AI Collaboration

**Design for both human and AI agents:**

| Agent Type | What They Handle |
|------------|------------------|
| **AI Agent** | Initial triage, data gathering, pattern recognition |
| **Human Agent** | Judgment calls, customer communication, complex cases |
| **Supervisor** | Escalations, quality review, exception handling |

Your Scenario design specifies when AI can act autonomously and when human judgment is needed.

### 4. Built-in Flexibility

**Three types of operations for different needs:**

| Type | When to Use | Example |
|------|-------------|---------|
| **Procedure** | Deterministic, single-role | Password reset |
| **Workflow** | Multi-role, predictable flow | Loan approval |
| **Case** | Non-deterministic, evolving | Dispute investigation |

You choose the right model for each Scenario.

---

## The Design-to-Execution Flow

### Your Journey as Process Architect

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROCESS ARCHITECT JOURNEY                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. ANALYZE                           2. DESIGN                             │
│   ────────                             ────────                              │
│   Understand the                       Create Scenario                       │
│   operational situation                Normative Spec                        │
│                                                                              │
│   • What triggers this?                • Define roles and goals              │
│   • Who is involved?                   • Document SOPs                       │
│   • What decisions are made?           • Specify decision criteria           │
│   • What are the goals?                • Set compliance requirements         │
│                                                                              │
│                           ▼                                                  │
│                                                                              │
│   3. HANDOFF                           4. VALIDATE                           │
│   ────────                             ────────                              │
│   Developer builds                     Review in staging                     │
│   automation                           with real scenarios                   │
│                                                                              │
│   • Application implementation         • Test edge cases                     │
│   • Tool integrations                  • Validate with operators            │
│   • Trigger configurations             • Refine based on feedback            │
│                                                                              │
│                           ▼                                                  │
│                                                                              │
│   5. OPERATE                           6. EVOLVE                             │
│   ───────                              ────────                              │
│   Monitor in                           Update based on                       │
│   production                           learnings                             │
│                                                                              │
│   • Track SLA compliance               • Change Normative Spec              │
│   • Review decisions                   • Developer updates automation       │
│   • Gather feedback                    • Promote new version                │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Three-Specification Model

Hub separates process design from implementation:

| Specification | Owner | Focus |
|---------------|-------|-------|
| **Normative Spec** | Process Architect (You) | What ought to be done |
| **Automation Spec** | Developer | How it's codified |
| **Deployment Spec** | Supervisor | How it's operationalized |

**Benefit:** You focus on the "what" without worrying about the "how." Developers implement your design. Changes to your Normative Spec don't require changing automation code.

---

## Comparison with Traditional BPM

| Aspect | Traditional BPM | Hub Approach |
|--------|-----------------|--------------|
| **Process Model** | Flowchart with tasks | Scenario with roles, goals, SOPs |
| **Flexibility** | Rigid paths | Goal-directed with judgment |
| **Human Role** | Task executor | Goal-oriented agent |
| **AI Role** | Limited/separate | First-class team member |
| **Exceptions** | Separate handling | Built-in escalation |
| **Knowledge** | Separate documents | Linked SOPs and decision criteria |
| **Audit** | Activity logs | Decision records with explanation |

---

## Real-World Scenario Example

### Dispute Resolution Process

**Traditional BPM Approach:**

```
Receive Dispute → Assign to Agent → Investigate → Document → Decide → Notify
```

**Hub Scenario Approach:**

```
SCENARIO: Standard Dispute Resolution

WHEN: Customer files dispute (trigger: dispute.filed)

THEN:
  ROLES:
    - Dispute Analyst: Investigate, recommend
    - Supervisor: Review high-value, approve exceptions
    
  GOALS:
    - Resolve within 72 hours
    - Fair determination based on evidence
    - Complete documentation for audit
    
  DECISION GUIDANCE:
    - Use liability matrix for determination
    - Escalate if value > $5000
    - Provisional credit per Reg E if eligible
    
  AUTOMATION:
    - AI Agent handles initial data gathering
    - Human reviews AI recommendation
    - System enforces evidence requirements
    
  COMPLIANCE:
    - All decisions logged with rationale
    - Evidence bundle created automatically
```

---

## Getting Started

### Pilot a Single Scenario

1. **Select a scenario** with clear boundaries and measurable outcomes
2. **Document current state** — How is it handled today?
3. **Define the Normative Spec** — Roles, goals, SOPs, decisions
4. **Work with Developer** — They build the automation
5. **Configure deployment** — Queues, SLAs, agents
6. **Pilot and refine** — Learn from real execution

### Your Toolkit

| Tool | Purpose |
|------|---------|
| **Workbench Studio** | Design and configure Scenarios |
| **SOP Templates** | Structure your procedures |
| **Decision Matrix Tools** | Define decision criteria |
| **Simulation Mode** | Test scenarios before production |

---

## Next Steps

1. **Understand the ontology** → [Ontology Reference](../01-concepts/ontology-reference.md)
2. **See Scenario structure** → [Scenario Specification Types](../02-system-design/implementation-concepts/scenario-specification-types.md)
3. **Follow the journey** → [Scenario Development Journey](../08-personas-and-journeys/journeys/scenario-development.md)
4. **Try Workbench Studio** → [Workbench Setup Guide](../10-guides/workbench-setup-guide.md)

