# Scenario-Oriented Thinking: Adoption and Migration

> **Status**: 🟢 Design Complete  
> **Target Audience**: All (APOs, PAs, Developers)  
> **Purpose**: How to get started with scenario-oriented thinking and migrate existing processes

---

## Every Process Needs Fundamentals

### The Fundamental Requirements

Any process automation — regardless of complexity — needs:

| Requirement | Why It's Universal | What Happens Without It |
|-------------|-------------------|------------------------|
| **Explicit rules** | Regulations change, business changes, people leave | Rules buried in code, knowledge lost |
| **Sandboxed development** | You need to iterate before production | Changes go live untested |
| **Controlled deployment** | You need to know what's running | No visibility, no control |
| **Sustainable evolution** | Everything changes over time | Rewrite code for every change |

**The scenario model provides all of these.** Not as optional features, but as the foundational structure.

### "It's Simple, Just Write Code"

This is the common alternative. What happens?

```
"Simple process, just code it"
    ↓
Rules embedded in code
    ↓
Works fine initially
    ↓
Regulation changes, business asks for update
    ↓
Developer hunts for the code, tries to understand it
    ↓
Makes changes, hopes nothing breaks
    ↓
No one remembers why the code does what it does
    ↓
Fear of touching anything
    ↓
"Legacy system" — 2 years old
```

**Every process evolves.** The question is whether evolution is sustainable or a rewrite.

### One Scenario Is Valid

You don't need multiple scenarios to benefit from this model.

**Single scenario examples:**
- Invoice processing with consistent rules → one scenario
- Email routing → one scenario
- Data sync → one scenario

**What you still get:**
- Normative spec documenting the rules
- Clear ownership (business, developer, ops)
- Sandboxed development
- Controlled promotion to production
- AI can derive automation from normative
- Evolution without rewriting

### Multiple Scenarios When Situations Differ

| Domain | One Scenario | Multiple Scenarios |
|--------|--------------|-------------------|
| **Disputes** | All are the same type of problem | Standard vs. fraud vs. high-value are fundamentally different situations |
| **Payments** | All are the same type of transaction | Domestic vs. international vs. high-risk are different situations with different signals |
| **Onboarding** | All are the same type of customer | Individual vs. business vs. regulated entity are different situations requiring different normative specs |

### How to Decide

**Same scenario** if:
- The situation is fundamentally the same
- The same signal type indicates it
- Differences are parameter values within the same situation (amount thresholds, etc.)

**Different scenarios** if:
- The situation is fundamentally different (business recognizes it as a distinct problem)
- Different signals indicate it (fraud flag vs. standard dispute filing)
- It requires a different normative specification (different goals, roles, compliance context)

**The test:** Would business stakeholders say "that's a different situation entirely" or "that's the same situation with different parameters"?

---

## Starting with Scenario Thinking

### Step 1: Identify Scenarios

- What situations does your business need to respond to?
- What signals indicate each situation?
- What makes each situation fundamentally different (not how it's processed, but what it IS)?

**Key question:** "What problem or situation are we sensing?" Not "How do we handle it?"

### Step 2: Validate with Stakeholders

- Do business stakeholders recognize these scenarios?
- Are the boundaries clear?
- Are any scenarios missing?

**Validation criteria:**
- Business stakeholders can name and describe the scenarios
- Scenarios represent distinct situations, not just different handling approaches
- Boundaries are clear and non-overlapping

### Step 3: Design Normative Specifications

- For each scenario: who, what goals, what rules
- This is the source of truth — invest here
- Document SOPs, decision criteria, compliance requirements

**What to include:**
- Roles and responsibilities
- Goals and success criteria
- Decision criteria and rules
- Escalation paths
- Compliance requirements
- Evidence/documentation needs

### Step 4: Derive Automation

- What automation approach fits each scenario?
- AI can assist with generation from normative
- Human developers review and refine

**Considerations:**
- Some scenarios suit rule-based automation
- Some scenarios suit workflow orchestration
- Some scenarios suit AI agents
- Some scenarios need human handling
- The automation approach is derived from the normative spec

### Step 5: Configure Deployment

- How will work be assigned?
- What are the SLA requirements?
- AI can suggest; operators approve

**What to configure:**
- Task queues
- Agent enrollment (human and AI)
- SLA parameters
- Activation settings
- Operational overrides

---

## Migrating Existing Processes

### From Hardwired Code to Scenarios

1. **Identify triggers** — What starts the process?
2. **Identify variation** — Are there distinct handling patterns?
3. **Extract business rules from code** → normative spec
4. **Identify implementation** → automation spec
5. **Extract operational settings** → deployment spec

**Common challenges:**
- Business rules are buried in code
- No clear documentation of "why"
- Multiple developers touched the code over time
- Knowledge left with people who moved on

**Approach:**
- Start with what you know (code, comments, people)
- Extract the "what" (rules, goals) from the "how" (implementation)
- Validate with business stakeholders
- Document as normative spec

### From BPM to Scenarios

1. **The BPMN diagram becomes input, not source of truth**
2. **Capture the normative that was implicit**
3. **Scenario boundaries may differ from process boundaries**

**Key differences:**
- BPM focuses on workflow steps
- Scenarios focus on situations
- One BPM process may map to multiple scenarios
- Normative requirements were likely implicit or in separate docs

**Approach:**
- Review BPMN diagrams to understand current flow
- Identify distinct situations (not just branches in the flow)
- Extract implicit business rules and goals
- Create normative specs for each scenario
- Map BPMN steps to automation specs

### What Makes a Different Scenario

Scenarios are **coarse-grained** — they represent recognizable business situations, not individual decision rules.

| Different Scenario | Same Scenario, Different Rules |
|-------------------|-------------------------------|
| Fraud Dispute vs. Standard Dispute (different situation entirely) | Amount thresholds within Standard Dispute |
| Individual Onboarding vs. Business Onboarding (different verification, roles) | Different document requirements based on income |
| International Payment vs. Domestic Payment (different compliance, processing) | Different fee tiers based on amount |

**The test:** Do business stakeholders recognize this as a **fundamentally different situation** with different roles, goals, or compliance requirements? Or is it the same situation with different decision branches inside?

**Decision rules belong IN the normative spec, not as separate scenarios:**
```yaml
scenario: standard-dispute
normative:
  decision_criteria:
    - amount < 500 AND merchant_clean: auto_resolve
    - amount 500-1000: analyst_review  
    - customer_high_risk: extra_verification
```
These are rules **within** the Standard Dispute scenario — not separate scenarios.

---

## Best Practices

### Normative-First

- Start with normative specification — it's the source of truth
- Get business validation before automation
- AI can generate automation from good normative specs

**Why this matters:**
- Normative is the authoritative source
- Automation derives from normative, not the other way around
- Business owns and validates normative before implementation begins

### Scenario Design

- One scenario per distinct situation
- Clear, recognizable names
- Start with fewer, split later if needed

**Naming guidance:**
- Use business language, not technical terms
- Names should be recognizable to business stakeholders
- Avoid implementation details in names (e.g., "Automated Dispute" vs. "Standard Dispute")

### Ownership

- Process Architect owns normative
- Developer owns automation
- Supervisor owns deployment
- Clear boundaries reduce coordination overhead

**Benefits:**
- Each persona owns their domain
- Changes don't require coordination across all personas
- Clear accountability for each specification

### Common Pitfalls to Avoid

**Pitfall 1: Creating scenarios based on implementation differences**
- ❌ Wrong: "Automated Dispute" vs. "Manual Dispute"
- ✅ Right: "Standard Dispute" vs. "Fraud Dispute" (different situations)

**Pitfall 2: Treating decision rules as separate scenarios**
- ❌ Wrong: "Low-Amount Dispute" vs. "High-Amount Dispute"
- ✅ Right: "Standard Dispute" with decision criteria for amount thresholds

**Pitfall 3: Mixing normative and automation concerns**
- ❌ Wrong: Putting business rules in automation spec
- ✅ Right: Business rules in normative, implementation in automation

**Pitfall 4: Skipping normative specification**
- ❌ Wrong: Jumping straight to automation
- ✅ Right: Design normative first, derive automation from it

---

## Related Documentation

- [Entry Point](./scenario-oriented-thinking.md) — Overview and reading guide
- [Core Concepts](./scenario-oriented-thinking-core.md) — Foundations and specifications
- [Examples](./scenario-oriented-thinking-examples.md) — Concrete use cases
- [Anti-patterns](./scenario-oriented-thinking-anti-patterns.md) — When NOT to use

---

[← Back to Entry Point](./scenario-oriented-thinking.md)
