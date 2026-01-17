# Scenario-Oriented Thinking for Business Process Automation

> **Status**: 🟢 Design Complete  
> **Target Audience**: Automation Product Owners, Process Architects, Developers  
> **Purpose**: Entry point for understanding scenario-oriented thinking as a paradigm for business process automation

---

## Executive Summary

**Scenario-Oriented Thinking** is a way of modeling business operations as **situational responses** rather than **sequential workflows**. Instead of asking "What steps does this process have?", you ask "What situations does my business need to respond to, and how should each be handled?"

The core insight: **Normative specifications are the center of gravity**. In a world where AI agents increasingly handle automation, business should focus on **what should happen** (normative), while AI agents derive **how it's implemented** (automation). This paradigm shift addresses a fundamental problem: all traditional automation platforms focus on HOW to automate, leaving the WHY (purpose) and WHAT (situation, goals) largely unaddressed or scattered.

This documentation suite provides decision frameworks, examples, and guidance to help you understand when and how to apply scenario-oriented thinking to your business process automation.

---

## The Confusion

Traditional process automation approaches share a common blind spot:

- **BPM platforms** focus on workflow orchestration (HOW)
- **Low-code platforms** focus on visual flow building (HOW)
- **Workflow-as-code platforms** focus on durable execution (HOW)
- **Custom code** focuses on implementation (HOW)

But where does the **WHAT** live?
- In requirements documents that get written once and forgotten
- In analysts' heads
- In emails and meeting notes
- Eventually, buried in code as implementation details

This creates problems:
- **Drift** — Requirements and implementation drift apart
- **Knowledge loss** — When people leave, knowledge leaves
- **Evolution debt** — Changing rules requires code archaeology
- **AI-unfriendly** — AI can't reliably extract intent from scattered docs

**Scenario-Oriented Thinking addresses this by putting normative specifications (WHAT, WHY, goals) at the center as the authoritative source of truth.**

---

## Quick Reference

| Aspect | Traditional Process Thinking | Scenario-Oriented Thinking |
|--------|------------------------------|----------------------------|
| **Focus** | Sequential steps | Situational responses |
| **Question** | "What steps does this process have?" | "What situations must we respond to?" |
| **Source of Truth** | Implementation (code, BPMN diagram) | Normative specification (business rules) |
| **Specifications** | Single workflow definition | Three: Normative, Automation, Deployment |
| **Evolution** | Change code/diagrams | Change normative → derive automation |
| **AI-Ready** | Limited (scattered docs) | Yes (structured normative input) |
| **Business Alignment** | Technical workflow | Matches business understanding |

---

## Reading Guide by Audience

### Automation Product Owners (APOs)

**Start here**: [Core Concepts](./scenario-oriented-thinking-core.md#core-concepts) → [The Core Argument](./scenario-oriented-thinking-argument.md) → [Examples](./scenario-oriented-thinking-examples.md)

**Key questions answered**:
- How do I identify automation opportunities as scenarios?
- What makes a good scenario?
- How does this model help with business alignment?
- What are the benefits for my organization?

**Additional reading**:
- [Adoption Guide](./scenario-oriented-thinking-adoption.md#starting-with-scenario-thinking)
- [Anti-patterns](./scenario-oriented-thinking-anti-patterns.md)

### Process Architects (PAs)

**Start here**: [Core Concepts](./scenario-oriented-thinking-core.md#conceptual-foundations) → [The Three Specifications](./scenario-oriented-thinking-core.md#the-three-specifications) → [The Core Argument](./scenario-oriented-thinking-argument.md)

**Key questions answered**:
- How do I design normative specifications?
- What belongs in normative vs. automation vs. deployment specs?
- How do I identify scenario boundaries?
- How does this relate to DDD and AOSM?

**Additional reading**:
- [Examples](./scenario-oriented-thinking-examples.md)
- [Adoption Guide](./scenario-oriented-thinking-adoption.md)
- [Comparison with Alternatives](./scenario-oriented-thinking-alternatives.md)

### Developers

**Start here**: [Core Concepts](./scenario-oriented-thinking-core.md#core-concepts) → [The Three Specifications](./scenario-oriented-thinking-core.md#the-three-specifications) → [Adoption Guide](./scenario-oriented-thinking-adoption.md#migrating-existing-processes)

**Key questions answered**:
- How are automation requirements structured?
- What's the relationship between normative and automation specs?
- How do I migrate existing processes?
- What's my role vs. Process Architect vs. Supervisor?

**Additional reading**:
- [The Core Argument](./scenario-oriented-thinking-argument.md) (why this matters)
- [Examples](./scenario-oriented-thinking-examples.md)
- [Comparison with Alternatives](./scenario-oriented-thinking-alternatives.md)

---

## Document Map

This documentation suite consists of:

1. **[Core Concepts](./scenario-oriented-thinking-core.md)** — Foundations, concepts, and three specifications
   - Conceptual foundations (DDD and AOSM)
   - What is scenario-oriented thinking?
   - Core concepts (Scenario, Signal, Request)
   - The three specifications (Normative, Automation, Deployment)

2. **[The Core Argument](./scenario-oriented-thinking-argument.md)** — Why this paradigm shift matters
   - The problem with current automation platforms
   - Why normative-first matters for AI
   - Addressing concerns
   - The paradigm shift in summary

3. **[Examples](./scenario-oriented-thinking-examples.md)** — Concrete use cases
   - Dispute resolution scenarios
   - Payment processing scenarios
   - Customer onboarding scenarios
   - Support scenarios

4. **[Comparison with Alternatives](./scenario-oriented-thinking-alternatives.md)** — How this compares to other approaches
   - Traditional BPM (Camunda, Pega, Appian)
   - Low-code (Power Automate, Zapier)
   - Workflow-as-code (Temporal, Cadence)
   - Custom code

5. **[Adoption and Migration](./scenario-oriented-thinking-adoption.md)** — How to get started
   - Starting with scenario thinking
   - Migrating existing processes
   - Best practices

6. **[Anti-patterns](./scenario-oriented-thinking-anti-patterns.md)** — When NOT to use scenario-oriented thinking
   - Common mistakes
   - When the model may not fit
   - Alternatives to consider

---

## Decision Flowchart

```
Start: Do you need to automate a business process?
│
├─ No → Stop (this model is for process automation)
│
└─ Yes → Does the process involve:
    │
    ├─ Multiple roles/responsibilities?
    │   └─ Yes → Scenario-oriented thinking helps
    │
    ├─ Business rules that may change?
    │   └─ Yes → Scenario-oriented thinking helps
    │
    ├─ Different situations requiring different handling?
    │   └─ Yes → Scenario-oriented thinking helps
    │
    ├─ Compliance/audit requirements?
    │   └─ Yes → Scenario-oriented thinking helps
    │
    ├─ AI-assisted automation in your strategy?
    │   └─ Yes → Scenario-oriented thinking helps
    │
    └─ Truly one-off script that will never change?
        └─ Yes → May not need this model
            └─ But consider: will it really never change?
```

**See [Anti-patterns](./scenario-oriented-thinking-anti-patterns.md) for when NOT to use this model.**

---

## Key Takeaways

1. **Think in situations, not steps** — Scenarios are operational situations, not workflow diagrams
2. **Normative is the source of truth** — Everything else derives from it
3. **Three specifications with clear ownership** — Business owns normative, developers implement, ops deploys
4. **AI-ready model** — Normative specs can drive AI-generated automation
5. **Every process needs fundamentals** — Even simple processes benefit from explicit rules, sandboxed development, controlled deployment

---

## Related Documentation

- [Hub Development Flow Guide](../../10-guides/hub-development-flow/README.md) — Platform-specific development practices
- [Scenario Specification Types](../../02-system-design/implementation-concepts/scenario-specification-types.md) — Implementation details
- [Idea to Deployment Guide](../../10-guides/idea-to-deployment-guide.md) — End-to-end journey
- [Scenario Development Journey](../../08-personas-and-journeys/journeys/scenario-development.md) — Persona-specific journeys

---

[← Back to Decision Frameworks](../README.md)
