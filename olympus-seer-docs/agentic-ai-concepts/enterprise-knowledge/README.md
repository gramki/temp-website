# Enterprise Knowledge

**Enterprise Knowledge** is the set of **codified, curated, and asserted truths** an organization recognizes as authoritative at a point in time.

It answers the question:

> *“What does the enterprise believe to be true or correct?”*

This folder makes enterprise knowledge **operable**: the major knowledge types, how they differ from enterprise memory, and how knowledge is governed and evolved over time.

## Doc ownership (avoid duplication)

- **Canonical conceptual model** (definitions, “Truth × Semantics”, “storage ≠ cognition”, vocabulary mapping, core anti-patterns): [../enterprise-knowledge-memory-other-data.md](../enterprise-knowledge-memory-other-data.md)
- **This folder** is the Enterprise Knowledge handbook (types + lifecycle + management).
- **Applied guide** with worked examples: [../designing-an-agent.md](../designing-an-agent.md)

## Knowledge vs memory (quick intuition)

- **Enterprise Knowledge** is **normative**: it constrains and guides action (“what should happen”).
- **Enterprise Memory** is **experiential**: it captures what happened and why (“what did happen”).

Promotion from enterprise memory is deliberate and governed; see [lifecycle-and-management.md](./lifecycle-and-management.md) and the canonical model in [../enterprise-knowledge-memory-other-data.md](../enterprise-knowledge-memory-other-data.md).

## Knowledge types (map)

- **Policies, rules, and regulatory obligations**: binding constraints and decision criteria  
  See: [policy-and-rules.md](./policy-and-rules.md)

- **Procedural knowledge (SOPs, runbooks)**: codified “how-to” guidance (may diverge from procedural memory in practice)  
  See: [procedural-knowledge.md](./procedural-knowledge.md)

- **Reference and master data**: canonical code tables, product catalogs, identifiers  
  See: [reference-and-master-data.md](./reference-and-master-data.md)

- **Definitions, metrics, and canonical KPIs**: agreed meanings for measurement and reporting  
  See: [definitions-and-metrics.md](./definitions-and-metrics.md)

- **Semantics and ontologies (metadata)**: meaning systems (taxonomies, data catalogs, ontologies) that make knowledge usable  
  See: [semantics-and-ontologies.md](./semantics-and-ontologies.md)

- **Derived knowledge artifacts vs signals**: what “looks like knowledge” but is not knowledge-of-record by default  
  See: [derived-artifacts-and-signals.md](./derived-artifacts-and-signals.md)

## Lifecycle and management

- **Lifecycle** (author → validate → publish → govern → evolve → retire): [lifecycle-and-management.md](./lifecycle-and-management.md)

## Related docs

- Conceptual framing: [../enterprise-knowledge-memory-other-data.md](../enterprise-knowledge-memory-other-data.md)
- Enterprise memory types: [../enterprise-memory/README.md](../enterprise-memory/README.md)
- Designing an agent (practical guide): [../designing-an-agent.md](../designing-an-agent.md)
- Hub implementation docs:
  - Knowledge Services: [../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md](../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md)
  - Knowledge Bank: [../../../olympus-hub-docs/02-system-design/implementation-concepts/knowledge-bank.md](../../../olympus-hub-docs/02-system-design/implementation-concepts/knowledge-bank.md)

