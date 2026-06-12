# Pattern Curator Agent

[← Back to Knowledge Engineering](README.md) | [← Back to ERE](../README.md)

The Pattern Curator Agent is an AI agent that continuously maintains the health and utility of the knowledge base.

---

## Purpose

Unlike drafting agents that assist with specific document creation, the Pattern Curator operates continuously in the background, scanning, analyzing, and improving the knowledge base.

---

## Capabilities

The Pattern Curator Agent continuously:

| Capability | Description |
|------------|-------------|
| **Scan for pattern candidates** | Analyzes new artifacts for recurring solutions worthy of formal pattern status |
| **Identify duplicates** | Detects similar content across the knowledge base; suggests consolidation |
| **Flag coverage gaps** | Alerts when archetypes or domains lack adequate knowledge artifacts |
| **Propose taxonomy updates** | Suggests new tags or categories based on emerging themes |
| **Answer questions** | Synthesizes across the knowledge base to answer complex queries |

---

## Detailed Behaviors

### Pattern Scanning

```
New Artifact → Pattern Curator Analysis → Pattern Candidate? → Domain Steward Review → Pattern Library
```

The agent:
- Compares new artifacts against existing patterns
- Identifies structural similarities across Engagements
- Proposes candidate patterns with supporting evidence
- Routes candidates to appropriate Domain Steward

For Work Model artifacts, the same flow validates candidates into the [Work Model Library](README.md): the Pattern Curator and Domain Stewards check that proposals from engagement teams and the Discovery Swarm capture structure only — scenario shapes, Tool Contract templates, governance structures, regulatory mappings — and that no bank-specific operational intelligence crosses the confidentiality boundary.

### Duplicate Detection

| Detection Type | Action |
|----------------|--------|
| **Exact duplicate** | Flags for removal; preserves canonical version |
| **Near duplicate** | Suggests consolidation; human decides which to keep |
| **Complementary content** | Suggests merge or cross-reference |

### Gap Identification

The agent monitors coverage metrics and proactively alerts:

| Gap Type | Alert Example |
|----------|---------------|
| **Archetype gap** | "No case studies for [Archetype X] in 6 months" |
| **Domain gap** | "Integration patterns for [System Y] have no recent contributions" |
| **Outcome gap** | "No lessons learned tagged with [Technology Z]" |

Alerts route to:
- Knowledge Engineer (for systemic gaps)
- Relevant Domain Steward (for domain-specific gaps)
- EPMs of relevant Engagements (for contribution prompts)

### Taxonomy Evolution

As the knowledge base grows, the agent:
- Identifies frequently co-occurring tags that might indicate a new category
- Detects tags that are rarely used (candidates for retirement)
- Proposes tag hierarchy adjustments based on usage patterns
- All taxonomy changes require Knowledge Engineer approval

### Query Answering

When users ask complex questions that span multiple artifacts:

| Query Type | Agent Behavior |
|------------|----------------|
| **Comparison** | "How did we handle [X] in similar Engagements?" → Synthesizes across case studies |
| **Best practice** | "What's the recommended approach for [Y]?" → Aggregates from patterns and lessons learned |
| **Gap analysis** | "Do we have experience with [Z]?" → Searches and reports coverage |

---

## Governance

The Pattern Curator Agent operates under the same governance model as all ERE agents:

| Control | Implementation |
|---------|----------------|
| **Autonomy level** | Assistive — proposes actions; humans approve |
| **Escalation** | Complex taxonomic changes escalate to Knowledge Engineer |
| **Audit trail** | All suggestions and decisions logged |
| **Feedback loop** | Accepted/rejected suggestions improve future recommendations |

### Progression Path

| Capability | Current State | Progression Criteria | Target State |
|------------|---------------|---------------------|--------------|
| **Pattern identification** | Proposes candidates | 80%+ of proposals accepted | Auto-creates draft patterns |
| **Duplicate detection** | Flags for review | 95%+ accuracy | Auto-consolidates exact duplicates |
| **Gap alerting** | Generates alerts | Alerts consistently actionable | Proactively routes to contributors |

---

## Integration with Knowledge Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                    Knowledge Base                             │
└──────────────────────────────────────────────────────────────┘
        ▲                    ▲                    ▲
        │                    │                    │
   ┌────┴────┐          ┌────┴────┐          ┌────┴────┐
   │ Pattern │          │ Coverage │          │ Query   │
   │ Scanning│          │ Analysis │          │ Service │
   └────┬────┘          └────┬────┘          └────┬────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────┴────────┐
                    │  Pattern Curator │
                    │      Agent       │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ Domain Steward│    │   Knowledge   │    │    Users      │
│    Alerts     │    │   Engineer    │    │   (Q&A)       │
│               │    │    Alerts     │    │               │
└───────────────┘    └───────────────┘    └───────────────┘
```

---

## Metrics

| Metric | What It Measures | Target |
|--------|------------------|--------|
| **Pattern identification rate** | Patterns proposed vs. accepted | >80% acceptance |
| **Duplicate reduction** | Redundant content removed | Decreasing duplicate count |
| **Gap closure rate** | Gaps flagged vs. addressed | >70% addressed within quarter |
| **Query satisfaction** | User ratings on synthesized answers | >4.0/5.0 |

---

*See also: [Ownership](ownership.md) | [Lifecycle Capture](lifecycle-capture.md) | [Knowledge Platform](../02-systems/knowledge-platform.md) | [AI Agents](../03-ai-architecture/agents.md)*
