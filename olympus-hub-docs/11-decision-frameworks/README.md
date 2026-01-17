# Decision Frameworks

> **Purpose:** Design rationale, modeling guidance, and decision frameworks for leveraging Hub and Seer effectively.

---

## Overview

This section provides **decision frameworks** and **conceptual clarifications** for leveraging Hub and Seer effectively. These documents help you:

- **Understand design rationale** — Why certain distinctions and patterns exist
- **Model problems effectively** — How to map business problems to Hub/Seer concepts
- **Make informed decisions** — When to use which patterns, concepts, or approaches
- **Avoid common pitfalls** — Anti-patterns and when NOT to use certain approaches

> **Key Distinction:** This section is about **"when" and "why"** decisions. For **"how"** step-by-step instructions, see [10-guides](../10-guides/README.md).

---

## Document Index

### Hub Agent vs Seer Agent Documentation Suite

| Document | Audience | Description | Status |
|----------|----------|-------------|--------|
| [Hub Agent vs Seer Agent](./hub-agent-vs-seer-agent/hub-agent-vs-seer-agent.md) | All | Entry point with overview, reading guide, and quick reference | 🟢 Design Complete |
| [Core Concepts](./hub-agent-vs-seer-agent/hub-agent-vs-seer-agent-core.md) | All | Comprehensive understanding, building basics, and decision framework | 🟢 Design Complete |
| [Examples](./hub-agent-vs-seer-agent/hub-agent-vs-seer-agent-examples.md) | All | Concrete use cases and scenarios | 🟢 Design Complete |
| [Anti-patterns](./hub-agent-vs-seer-agent/hub-agent-vs-seer-agent-anti-patterns.md) | All | When NOT to use Hub Agent pattern and alternatives | 🟢 Design Complete |
| [Architectural Details](./hub-agent-vs-seer-agent/hub-agent-vs-seer-agent-architectural-details.md) | Developers, Agent Engineers | C2-level architectural details and implementation references | 🟢 Design Complete |
| [Customer Guide](./hub-agent-vs-seer-agent/hub-agent-vs-seer-agent-customer-guide.md) | CSAs | Customer-facing explanations and decision guidance | 🟢 Design Complete |

---

## When to Use This Section

### Use Design Guidance When:

1. **You need to understand "why"** — Why certain design decisions were made, why distinctions exist
2. **You're modeling a problem** — You need to map a business problem to Hub/Seer concepts
3. **You're making architectural decisions** — Choosing between patterns, approaches, or technologies
4. **You're confused about concepts** — Multiple similar concepts exist and you need clarity
5. **You want to avoid mistakes** — Understanding anti-patterns and common pitfalls

### This Section is NOT For:

- **Step-by-step "how-to" guides** → See [10-guides](../10-guides/README.md) ("How do I configure X?")
- **Specific platform constructs** → See [02-system-design/implementation-concepts](../02-system-design/implementation-concepts/README.md)
- **Composition patterns** → See [09-composite-systems-and-patterns](../09-composite-systems-and-patterns/README.md)
- **System architecture details** → See [02-system-design](../02-system-design/README.md)

---

## Relationship to Other Sections

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCUMENTATION HIERARCHY                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  01-concepts/              What Hub/Seer concepts exist         │
│      │                                                           │
│      ├── 02-system-design/  How Hub/Seer implements concepts    │
│      │      │                                                      │
│      │      ├── 11-decision-frameworks/  When/why decisions     │
│      │      │      │                                                │
│      │      │      └── 09-composite-patterns/  How to compose     │
│      │      │              │                                        │
│      │      │              └── 10-guides/  Step-by-step how-to   │
│      │      │                                                      │
│      │      └── 04-subsystems/  Detailed subsystem docs          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Document Structure

Each design guidance document should include:

1. **The Confusion** — What ambiguity or question this addresses
2. **Core Distinction** — Clear explanation of the concepts
3. **Relationship** — How concepts relate to each other
4. **Decision Guidance** — When to use what
5. **Examples** — Concrete examples illustrating the concepts
6. **Anti-Patterns** — When NOT to use certain approaches
7. **Related Documentation** — Links to implementation details

---

## Contributing

When creating new design guidance documents:

1. **Identify the confusion** — What question or ambiguity needs clarification?
2. **Provide rationale** — Why does this distinction matter?
3. **Include decision guidance** — Help readers choose the right approach
4. **Show examples** — Concrete, real-world examples
5. **Document anti-patterns** — When NOT to use certain approaches
6. **Link to implementation** — Connect to specific implementation docs

---

## Related Sections

- [01-concepts](../01-concepts/README.md) — Core concepts and ontology
- [02-system-design](../02-system-design/README.md) — System architecture
- [09-composite-systems-and-patterns](../09-composite-systems-and-patterns/README.md) — Composition patterns
- [10-guides](../10-guides/README.md) — Step-by-step guides
