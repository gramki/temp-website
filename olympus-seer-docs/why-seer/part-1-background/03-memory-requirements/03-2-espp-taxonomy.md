# 3.2 The Memory Taxonomy (ESPP)

*A conceptual framework for understanding what agents remember and why.*

---

## Purpose

This subsection introduces the ESPP memory taxonomy—a four-type classification system that provides the conceptual foundation for enterprise memory management. Understanding these memory types is essential for designing agents that can learn from experience, explain their behavior, and satisfy governance requirements.

The taxonomy is not arbitrary. Each memory type corresponds to a distinct cognitive function, carries different governance implications, and requires different storage and retrieval mechanisms.

---

## Core Concepts & Definitions

### The Four Memory Types

The ESPP taxonomy classifies memory into four canonical types:

| Memory Type | What It Captures | Core Question |
|-------------|------------------|---------------|
| **Episodic** | What happened—events, decisions, outcomes | *What occurred?* |
| **Semantic** | What is believed—patterns, facts, constraints | *What do we know?* |
| **Procedural** | How to do things—skills, workflows, procedures | *How do we act?* |
| **Preference** | What is preferred—settings, behaviors, choices | *How should we personalize?* |

### Episodic Memory

**Definition**: Episodic memory captures specific events, decisions, and interactions anchored in time and case context.

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Time, case, event |
| **Purpose** | Audit trail, precedent lookup, experience replay |
| **Mutability** | Immutable in enterprise context |
| **Governance** | Highest—7+ year retention for regulatory compliance |

**What it contains**:
- Decision records with rationale
- Context snapshots at decision time
- Outcome records linking decisions to results
- Override records documenting human intervention
- Handoff context for agent-to-agent transfers

**Why it matters**: Episodic memory is the foundation of auditability. When a regulator asks "Why did you make that decision in 2024?", the answer comes from episodic memory. Without it, enterprise agents cannot be defended.

### Semantic Memory

**Definition**: Semantic memory captures learned beliefs, recognized patterns, and inferred constraints that the organization treats as knowledge (though not yet authoritative).

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Entity, domain, workbench |
| **Purpose** | Pattern recognition, hypothesis formation, institutional learning |
| **Mutability** | Confidence can be updated; records can be deprecated |
| **Governance** | Moderate—requires provenance and confidence tracking |

**What it contains**:
- Hypothesis records (patterns pending validation)
- Pattern summaries (recurring correlations)
- Learned constraints (advisory guidelines)
- Entity beliefs (probabilistic attributes)
- Relationship beliefs (inferred connections)

**Why it matters**: Semantic memory represents what the organization has learned from experience. It bridges the gap between individual episodic events and authoritative enterprise knowledge. Patterns detected in episodic memory can be promoted to semantic memory as hypotheses, which—with sufficient evidence and human approval—may eventually become official policy.

### Procedural Memory

**Definition**: Procedural memory captures learned skills, successful workflows, and effective action patterns.

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Skill, task, role |
| **Purpose** | Skill reuse, workflow optimization, best practice codification |
| **Mutability** | Refinable based on outcomes |
| **Governance** | Moderate—requires versioning and effectiveness tracking |

**What it contains**:
- Learned skills (reusable capabilities)
- Procedures (step-by-step guidance)
- Action sequences (successful tool invocation patterns)
- Tool usage patterns (effective combinations)

**Why it matters**: Procedural memory enables agents to improve at their tasks without explicit reprogramming. When an agent discovers that a particular sequence of tool calls consistently produces good outcomes, that sequence can be captured as procedural memory and reused in similar situations.

### Preference Memory

**Definition**: Preference memory captures subject-specific settings, behavioral adaptations, and contextual preferences.

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Subject (user or agent) + context |
| **Purpose** | Personalization, behavioral adaptation, context sensitivity |
| **Mutability** | Fully mutable—preferences change |
| **Governance** | Lower—but may contain derived personal data |

**What it contains**:
- User preferences (communication style, notification settings)
- Agent behaviors (observed decision patterns)
- Interaction patterns (how entities prefer to engage)
- Contextual preferences (situation-dependent variations)

**Why it matters**: Preference memory enables agents to adapt to individual users and contexts. However, preferences must not override binding constraints. An agent may remember that a customer prefers email over phone, but this preference cannot override a regulatory requirement for verbal confirmation.

---

## Conceptual Model

### Memory Type Relationships

The four memory types form a coherent cognitive architecture:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           AGENT COGNITION                                    │
│                                                                              │
│   EPISODIC                          SEMANTIC                                 │
│   "What happened?"                  "What do we know?"                       │
│   ┌──────────────────┐              ┌──────────────────┐                    │
│   │ Events           │──promotes───▶│ Patterns         │                    │
│   │ Decisions        │              │ Beliefs          │                    │
│   │ Outcomes         │              │ Hypotheses       │                    │
│   └──────────────────┘              └──────────────────┘                    │
│                                              │                               │
│                                              │ promotes (with governance)    │
│                                              ▼                               │
│                               ┌──────────────────────────────┐              │
│                               │    ENTERPRISE KNOWLEDGE       │              │
│                               │    (Authoritative, curated)   │              │
│                               └──────────────────────────────┘              │
│                                                                              │
│   PROCEDURAL                        PREFERENCE                               │
│   "How do we act?"                  "How to personalize?"                    │
│   ┌──────────────────┐              ┌──────────────────┐                    │
│   │ Skills           │              │ User prefs       │                    │
│   │ Procedures       │              │ Agent behaviors  │                    │
│   │ Action patterns  │              │ Context settings │                    │
│   └──────────────────┘              └──────────────────┘                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Promotion Pathways

Memory is not static—it can be promoted across types as confidence increases:

1. **Episodic → Semantic**: Recurring patterns in events become hypotheses
2. **Episodic → Procedural**: Successful action sequences become learned skills
3. **Episodic → Preference**: Observed choices become preference records
4. **Semantic → Knowledge**: Validated hypotheses become authoritative facts (with governance approval)

These promotions are not automatic. Each transition requires evidence thresholds and—for the semantic-to-knowledge transition—explicit human approval.

---

## Governance Implications by Memory Type

| Memory Type | Retention | PII Handling | Immutability | Promotion Target |
|-------------|-----------|--------------|--------------|------------------|
| **Episodic** | 7+ years | Entity references only | Append-only | Semantic, Procedural, Preference |
| **Semantic** | 5 years | Aggregated, anonymized | Confidence updates | Enterprise Knowledge |
| **Procedural** | 3 years | N/A (no user data) | Versioned refinement | — |
| **Preference** | 2 years | May contain derived PII | Fully mutable | — |

### Why Episodic Memory Requires Special Treatment

Episodic memory is the most governance-sensitive memory type because:

1. **Regulatory requirement**: Financial regulations require decision documentation for 7+ years
2. **Audit defense**: Episodic records are the primary evidence in regulatory inquiries
3. **Immutability requirement**: Records cannot be modified after creation (append-only)
4. **PII prohibition**: Entity references only—personal data resolved at query time

These requirements stem from the nature of episodic memory as evidentiary record. Unlike semantic memory (which represents current beliefs) or preference memory (which adapts to users), episodic memory represents historical fact and must be preserved without alteration.

---

## Common Misconceptions

### Misconception 1: "These Are Just Database Tables"

**The error**: Implement ESPP as four database tables and call it done.

**Why it fails**: Each memory type requires different storage models. Episodic needs event logs with vector embeddings. Semantic needs knowledge graphs with confidence scores. Procedural needs executable representations. Preference needs typed key-value stores.

**The fix**: Design for polyglot persistence with type-appropriate storage backends.

### Misconception 2: "Preferences Can Override Policies"

**The error**: If a user prefers X, the agent should do X.

**Why it fails**: Preferences are subordinate to policies and binding constraints. An agent must never allow preference memory to override guardrails, authority ceilings, or regulatory requirements.

**The fix**: Design context assembly with explicit precedence: Policy > Knowledge > Semantic > Preference.

### Misconception 3: "Automatic Promotion Is Fine"

**The error**: When a pattern appears N times, automatically promote it to semantic memory or knowledge.

**Why it fails**: Automatic promotion creates silent policy drift. What the agent "learned" effectively becomes policy without human review.

**The fix**: Promotion requires governance gates. Episodic-to-semantic promotion may be automated with thresholds, but semantic-to-knowledge promotion must require human approval.

---

## Practical Implications

### For Enterprise Architects

When designing memory architectures:

1. Implement all four memory types—partial implementations leave cognitive gaps
2. Design for type-appropriate governance (episodic is not preference)
3. Establish explicit promotion workflows with governance gates
4. Plan storage backends appropriate to each memory type

### For Agent Developers

When building agents:

1. Classify memory writes by type at creation time
2. Respect precedence hierarchies when memories conflict
3. Log which memories influenced decisions (for auditability)
4. Never allow preference memory to override policy constraints

### For Compliance Officers

When evaluating agent systems:

1. Verify that episodic memory is truly immutable
2. Confirm that no PII exists in long-retained episodic records
3. Review promotion workflows for appropriate governance gates
4. Ensure preference memory cannot circumvent binding constraints

---

## Cross-References

- **Section 3.3**: How ESPP applies differently to organizational vs. operational memory
- **Section 3.4**: Governance imperatives that apply to each memory type
- **Section 3.5**: The learning imperative and controlled promotion
- **Section 4.3**: How the Cognitive Audit Fabric manages episodic memory

For detailed ESPP specifications, see:
- `olympus-hub-docs/04-subsystems/memory-services/shared/espp-taxonomy.md`

---

*The ESPP taxonomy provides the vocabulary for discussing what agents remember. Each memory type serves a distinct purpose and carries distinct governance requirements.*
