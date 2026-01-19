# Process Architect Primer: Your Expertise, Amplified

> **Audience:** Process Architects, Business Analysts, and BPM practitioners

---

## The Frustration You Know

You've been here before:

- **You design processes; they get lost in translation to IT** — what you envisioned is not what got built
- **Your knowledge lives in documents nobody reads** — SOPs gather dust while tribal knowledge rules
- **Edge cases and exceptions defeat your models** — reality is messier than flowcharts
- **AI is happening around you, not through you** — teams experiment without your designs
- **You model tasks, but work is really about judgment** — procedures can't capture expertise

---

## The Shift: From Procedures to Situations

Traditional process modeling assumes you can predict every step in advance. Define the flowchart. Assign the tasks. Execute the sequence.

But real work doesn't operate that way. Real work is:

- **Situations that need resolution** — not tasks that need execution
- **Judgment applied in context** — not procedures followed blindly
- **Goals achieved through collaboration** — not boxes checked in sequence

This is always how work actually operated. We've just been modeling it wrong.

### What Changes

| Traditional Model | Situation-Oriented Model |
|-------------------|--------------------------|
| Define procedures | Define **goals** |
| Assign tasks | Specify **roles and responsibilities** |
| Script the happy path | Describe **decision criteria** |
| Handle exceptions separately | Build in **judgment and escalation** |
| Hope it gets implemented | **Your design is the system** |

---

## What This Means for You

### Your Designs Become Executable

In Hub, a **Scenario** is not documentation — it's operational.

When you define a Scenario, you specify:
- **Roles** — who is responsible, what are their goals
- **Decision criteria** — how to make judgment calls
- **SOPs** — linked procedures that guide agents in real-time
- **Escalation patterns** — what happens when judgment is needed
- **Compliance requirements** — regulatory constraints built in

Your design *is* the system. Not a description of what the system should do — the actual operational definition.

### Your Expertise Becomes Infrastructure

The knowledge you capture doesn't sit in documents. It becomes **operational infrastructure**:

- **Decision criteria you define** guide human and AI agents in the moment
- **SOPs you write** are referenced in real-time, not filed away
- **Your knowledge accumulates** as organizational memory

When an agent handles a dispute, they see your SOP. When AI makes a recommendation, it references your decision criteria. Your expertise is operationalized.

### AI Works Through Your Designs

AI doesn't bypass you. It works through the structures you define:

- **You specify when AI can act autonomously** — within your governance
- **You define escalation patterns** — when AI should defer to humans
- **AI becomes a team member you design for** — not a tool you react to

The Scenario you design governs how human and AI agents collaborate. AI doesn't exist outside your architecture — it participates within it.

### Your Models Handle Reality

Goal-oriented Scenarios accommodate the messiness of real work:

- Agents apply **judgment within your guardrails** — not rigid sequences
- **Exceptions don't break the model** — they're anticipated
- **The model flexes; the intent persists** — goals over procedures

---

## What You Can Now Do

| Before | Now |
|--------|-----|
| Document processes | Define **executable Scenarios** |
| Hope IT implements correctly | **See your design in operation** |
| Write SOPs nobody reads | SOPs **guide agents in real-time** |
| Model happy paths | Model **situations with judgment** |
| React to AI initiatives | **Design human-AI collaboration** |
| Capture knowledge in documents | Knowledge becomes **operational memory** |

---

## How Hub Works (The Mechanics)

### The Three Specifications

Hub separates concerns cleanly:

| Specification | Owner | Focus |
|---------------|-------|-------|
| **Normative Spec** | You (Process Architect) | What ought to be done — roles, goals, SOPs, decisions |
| **Automation Spec** | Developer | How it's codified — application logic, tool bindings |
| **Deployment Spec** | Supervisor | How it's operationalized — queues, SLAs, agent enrollment |

You focus on the "what" — the goals, the roles, the judgment criteria. Developers implement the "how." Supervisors configure the deployment.

### A Scenario Example

```yaml
scenario:
  name: standard-dispute-resolution
  
  roles:
    - name: dispute-analyst
      goals:
        - "Investigate dispute within 24 hours"
        - "Document all findings"
        - "Make fair determination based on evidence"
      responsibilities:
        - "Review transaction history"
        - "Contact customer for clarification"
        - "Gather evidence from merchant"
    
  decision_criteria:
    - name: liability-determination
      description: "How to determine who bears liability"
      document_ref: dispute-liability-matrix
      
  sops:
    - ref: sop-dispute-investigation
    - ref: sop-customer-communication
    
  escalation:
    - condition: "amount > 5000"
      escalate_to: supervisor
    - condition: "fraud_suspected"
      escalate_to: fraud-specialist
      
  compliance:
    - requirement: "Reg E provisional credit"
      description: "Issue provisional credit within 10 days if eligible"
```

### Scenarios, Not Workflows

Traditional workflows define sequences. Scenarios define goals.

| Workflow | Scenario |
|----------|----------|
| Step 1 → Step 2 → Decision → Step 3 | Goal: Resolve dispute fairly |
| Rigid sequence | Flexible collaboration toward goal |
| Prescribes how | Describes what ought to be achieved |
| Hard to accommodate exceptions | Judgment and escalation built in |

---

## Your Journey

### The Design-to-Execution Flow

```
ANALYZE                          DESIGN
────────                         ────────
Understand the                   Create Scenario
operational situation            Normative Spec

• What triggers this?            • Define roles and goals
• Who is involved?               • Document SOPs
• What decisions are made?       • Specify decision criteria
• What are the goals?            • Set compliance requirements

              ↓

HANDOFF                          VALIDATE
────────                         ────────
Developer builds                 Review in staging
automation                       with real scenarios

• Application implementation     • Test edge cases
• Tool integrations              • Validate with operators
• Trigger configurations         • Refine based on feedback

              ↓

OPERATE                          EVOLVE
───────                          ────────
Monitor in                       Update based on
production                       learnings

• Track SLA compliance           • Change Normative Spec
• Review decisions               • Developer updates automation
• Gather feedback                • Promote new version
```

---

## Getting Started

1. **Pick one scenario** — A situation with clear boundaries and measurable outcomes
2. **Document current state** — How is it handled today? What works? What doesn't?
3. **Define the Normative Spec** — Roles, goals, SOPs, decision criteria
4. **Partner with Developer** — They implement the automation
5. **Configure with Supervisor** — Queues, SLAs, agent enrollment
6. **See it run** — Your design, operational

---

## Deeper Understanding

- [Vision and Mission](../00-_why/vision.md) — The larger purpose
- [Foundational Beliefs](../00-_why/foundational-beliefs.md) — The thinking behind Hub
- [Scenario-Oriented Thinking](../11-decision-frameworks/scenario-oriented-thinking/scenario-oriented-thinking.md) — The design philosophy
- [Scenario Specification Types](../02-system-design/implementation-concepts/scenario-specification-types.md) — The three-spec model

---

## Next Steps

- [Scenario Development Journey](../08-personas-and-journeys/journeys/scenario-development.md) — The full journey
- [Glossary](../01-concepts/glossary.md) — Key terminology
- [Applicability Guide](../01-concepts/olympus-hub-applicability-guide.md) — Where Hub fits
