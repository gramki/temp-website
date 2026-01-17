# Scenario-Oriented Thinking: Comparison with Alternatives

> **Status**: 🟢 Design Complete  
> **Target Audience**: All (APOs, PAs, Developers)  
> **Purpose**: How scenario-oriented thinking compares to other process automation approaches

---

## The Central Question

Every process automation approach has normative requirements — roles, goals, rules, SOPs, compliance. **The question is: where do they live, and what's the source of truth?**

| Approach | Where Normative Lives | Source of Truth | AI-Ready? |
|----------|----------------------|-----------------|-----------|
| **BPM** | Separate docs, annotations | BPMN diagram | Partially — structure exists but normative is secondary |
| **Low-Code** | Implicit in flows | The visual flow | Limited — rules scattered, not structured |
| **Workflow-as-Code** | In code, comments | The code | No — business rules are implementation details |
| **Custom Code** | Buried in code | The code | No — opaque to business and AI |
| **Scenario-Oriented** | Explicit normative spec | Normative specification | Yes — structured input for derivation |

---

## Traditional BPM (Camunda, Pega, Appian)

### Strengths

- Mature, proven, industry-adopted
- Visual process modeling
- Strong workflow orchestration

### The Paradigm Issue

BPM treats the BPMN diagram as the source of truth. But BPMN is implementation — it's *how* the process flows. The normative requirements (why, what goals, what rules, what compliance) live elsewhere:

- In requirements documents that get written once and forgotten
- In analysts' heads
- In BPMN annotations that mix with implementation

**The result:** Process diagrams and business requirements drift apart. When audit asks "what are the rules?", you piece together docs and code.

**BPM's assumption:** Someone else captures requirements; we handle execution.

**Scenario model's approach:** Normative IS the source of truth; execution derives from it.

---

## Low-Code (Power Automate, Zapier, OutSystems)

### Strengths

- Fast to build
- Accessible to non-developers
- Good for simple integrations

### The Paradigm Issue

Low-code optimizes for speed to first deployment. Rules become implicit in the visual flow — drag, drop, configure, ship.

- Where are the business rules? In the flow configuration.
- Where are the SOPs? Not captured.
- Who owns what? The person who built it.

**The result:** Fast automation, unclear rules, governance problems. Works for departmental automation; breaks down for enterprise processes.

**Low-code's assumption:** Speed matters more than structure.

**Scenario model's approach:** Structure enables sustainable evolution; speed without structure is debt.

---

## Workflow-as-Code (Temporal, Cadence)

### Strengths

- Excellent developer experience
- Durable execution, reliability guarantees
- Strong debugging and observability

### The Paradigm Issue

Temporal is developer tooling. Business rules live in code:

```python
if amount < 500 and merchant.is_clean():
    return auto_resolve()
else:
    return escalate_to_analyst()
```

This is clean code. But:
- Business can't read it
- Business can't change it without developers
- Audit requires reading code
- Knowledge leaves when developers leave

**The result:** Developer-owned automation. Works when developers own the full lifecycle. Breaks down when business needs visibility and control.

**Temporal's assumption:** Developers own everything.

**Scenario model's approach:** Business owns normative; developers implement; the separation is structural.

---

## Custom Code (Microservices, Event-Driven)

### Strengths

- Complete flexibility
- No platform constraints
- Can be optimized for anything

### The Paradigm Issue

This is where "rules buried in code" is the default:

```java
// Auto-resolve if under threshold and clean history
// Updated by @john in 2019, not sure why 500
if (amount < 500 && merchantHistory.isClean()) {
    return autoResolve();
}
```

- Why 500? Who decided? What's the SOP?
- When regulations change, who finds this code?
- When John leaves, who knows this exists?

**The result:** Flexibility that becomes rigidity. No one dares change what they don't understand.

**Custom code's assumption:** Developers will document and maintain.

**Scenario model's approach:** Make the normative explicit; derivation handles implementation.

---

## The Paradigm Shift: Normative as Source of Truth

**Every approach has normative requirements. The question is:**

| Question | Traditional | Scenario-Oriented |
|----------|-------------|-------------------|
| Where do requirements live? | Separate docs, code, heads | Normative specification |
| What's the source of truth? | Implementation (code/diagram) | Normative (business rules) |
| Who can read/change rules? | Developers | Business (with governance) |
| How does change happen? | Manually update code | Update normative → derive automation |
| What about AI? | AI can't read scattered docs | AI has structured input for derivation |

### The AI-Ready Dimension

In a world where AI agents generate automation:
- **BPM/Low-Code:** AI could generate flows, but from what input? Scattered docs?
- **Workflow-as-Code:** AI could write code, but what are the rules?
- **Scenario-Oriented:** AI has structured normative spec → can derive automation

**This is why normative-first matters:**
- AI needs structured input
- Business understands normative (it's their domain)
- Derivation keeps things in sync
- Evolution is sustainable

---

## When to Choose What

### Choose Traditional BPM When:

- You need mature, proven workflow orchestration
- Visual process modeling is important
- You have separate requirements management processes
- AI-assisted automation is not a priority

### Choose Low-Code When:

- Speed to first deployment is critical
- Simple integrations and departmental automation
- Governance and long-term evolution are not concerns
- Non-developers need to build automations

### Choose Workflow-as-Code When:

- Developers own the full lifecycle
- Durable execution and reliability are critical
- Business doesn't need direct visibility/control
- Code-first approach fits your culture

### Choose Custom Code When:

- You need complete flexibility
- No platform constraints are acceptable
- You can maintain documentation discipline
- Long-term evolution is not a concern

### Choose Scenario-Oriented When:

- AI-assisted automation is part of your strategy
- Business needs direct control over rules
- Processes evolve over time
- Compliance and audit requirements matter
- You want sustainable evolution without technical debt

---

## Related Documentation

- [Entry Point](./scenario-oriented-thinking.md) — Overview and reading guide
- [The Core Argument](./scenario-oriented-thinking-argument.md) — Why normative-first matters
- [Examples](./scenario-oriented-thinking-examples.md) — Concrete use cases
- [Adoption Guide](./scenario-oriented-thinking-adoption.md) — How to get started

---

[← Back to Entry Point](./scenario-oriented-thinking.md)
