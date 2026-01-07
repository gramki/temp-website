# ESPP Memory Taxonomy

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Shared Concepts](./README.md)

---

## Overview

The **ESPP (Episodic-Semantic-Procedural-Preference)** taxonomy provides a unified structure for memory across Hub Memory Services. Both Enterprise Memory and Agent Memory implement this taxonomy, though with different scopes and semantics.

---

## Taxonomy Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ESPP MEMORY TAXONOMY                                │
│                                                                               │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐           │
│   │    EPISODIC     │   │    SEMANTIC     │   │   PROCEDURAL    │           │
│   │                 │   │                 │   │                 │           │
│   │  What happened  │   │  What we know   │   │   How to act    │           │
│   │                 │   │                 │   │                 │           │
│   │  • Events       │   │  • Patterns     │   │  • Skills       │           │
│   │  • Decisions    │   │  • Beliefs      │   │  • Procedures   │           │
│   │  • Outcomes     │   │  • Constraints  │   │  • Sequences    │           │
│   │  • Handoffs     │   │  • Findings     │   │  • Tool usage   │           │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘           │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                          PREFERENCE                                  │   │
│   │                                                                      │   │
│   │              How to personalize — subject-specific settings          │   │
│   │                                                                      │   │
│   │  • User preferences  • Agent behaviors  • Interaction patterns      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Memory Classes

### Episodic Memory

**What happened** — Event-based, time-ordered, case-bound records.

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Case/Event/Time |
| **Binding** | `case_id` (universal binding) |
| **Ordering** | Chronological |
| **Mutability** | Enterprise: Immutable; Agent: Mutable |

#### Enterprise Episodic Record Types

| Record Type | Purpose |
|-------------|---------|
| CaseRecord | Root anchor for a case |
| DecisionRecord | Decision with rationale |
| EvidenceBundle | Context at decision time |
| ContextSnapshot | Compiled context per turn |
| OutcomeRecord | Post-decision outcome |
| OverrideRecord | Manual override documentation |
| HandoffContext | Agent-to-agent state transfer |
| HypothesisRecord | Observed pattern (may promote to Semantic) |
| IncidentTimeline | Chronological event sequence |

#### Agent Episodic Contents

| Content | Purpose |
|---------|---------|
| Conversation turns | Recent chat history |
| Tool invocations | Recent tool calls and results |
| Session context | Current session state |
| Errors encountered | Recent errors for debugging |

---

### Semantic Memory

**What we know** — Learned beliefs, patterns, and inferences.

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Entity/Domain/Workbench |
| **Binding** | `workbench_id` (domain scope) |
| **Ordering** | By confidence, recency |
| **Mutability** | Confidence updates allowed |

#### Enterprise Semantic Record Types

| Record Type | Purpose |
|-------------|---------|
| HypothesisRecord | Pattern pending validation |
| PatternSummary | Recurring correlation with conditions |
| LearnedConstraint | Advisory "avoid X when Y" guideline |
| EvaluationFinding | Benchmark and test results |
| EntityBelief | Probabilistic entity attribute |
| RelationshipBelief | Inferred entity connection |

#### Agent Semantic Contents

| Content | Purpose |
|---------|---------|
| User facts | "User prefers email" |
| Inferred preferences | Patterns from behavior |
| Context facts | Learned context attributes |

---

### Procedural Memory

**How to act** — Learned skills, procedures, and action patterns.

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Skill/Task/Role |
| **Binding** | `workbench_id` + `role` |
| **Ordering** | By effectiveness, frequency |
| **Mutability** | Refinement allowed |

#### Enterprise Procedural Record Types

| Record Type | Purpose |
|-------------|---------|
| LearnedSkill | Reusable capability |
| Procedure | Step-by-step guidance |
| ActionSequence | Successful tool invocation pattern |
| ToolUsagePattern | Effective tool combinations |

#### Agent Procedural Contents

| Content | Purpose |
|---------|---------|
| Task patterns | "User always does X then Y" |
| Workflow shortcuts | Learned optimizations |
| Tool preferences | Preferred tool sequences |

---

### Preference Memory

**How to personalize** — Subject-specific settings and behaviors.

| Attribute | Description |
|-----------|-------------|
| **Anchoring** | Subject (User/Agent) |
| **Binding** | `subject_id` + context |
| **Ordering** | By recency, confidence |
| **Mutability** | Fully mutable |

#### Enterprise Preference Record Types

| Record Type | Purpose |
|-------------|---------|
| UserPreference | Learned user preferences |
| AgentBehavior | Observed agent patterns |
| InteractionPattern | How entities prefer to interact |
| ContextualPreference | Context-dependent variations |

#### Agent Preference Contents

| Content | Purpose |
|---------|---------|
| Communication style | "Prefers concise responses" |
| Timezone/locale | User's context |
| Notification preferences | When/how to notify |
| Delegation preferences | What agent can decide |

---

## Cross-Memory Type Comparison

| Aspect | Enterprise Memory | Agent Memory |
|--------|-------------------|--------------|
| **Episodic Scope** | Case-bound (organizational) | Session-bound (individual) |
| **Episodic Retention** | 7+ years | 24 hours - 7 days |
| **Semantic Scope** | Workbench/domain | Agent/user |
| **Semantic Retention** | 5 years | 30 days |
| **Procedural Scope** | Role/workbench | Agent-specific |
| **Procedural Retention** | 3 years | Indefinite |
| **Preference Scope** | User/agent (organizational) | User/agent (individual) |
| **Preference Retention** | 2 years | 90 days |

---

## Promotion Paths

Memory can be **promoted** across types and scopes:

```
Agent Episodic
     │
     │ Pattern observed across sessions
     ▼
Agent Semantic
     │
     │ Pattern validated across agents
     ▼
Enterprise Semantic
     │
     │ High confidence + governance approval
     ▼
ETSL (Enterprise Knowledge)
```

See [Enterprise Learning Services](../../cognitive-audit-fabric/enterprise-learning-services.md) for promotion workflows.

---

## Schema Compatibility

Both Enterprise and Agent Memory follow CAF schema conventions:

| Convention | Enterprise | Agent |
|------------|------------|-------|
| Record ID | UUID v4 (required) | UUID v4 (required) |
| Content Hash | SHA-256 (required) | Optional |
| Typed Content | MIME-based (required) | Simplified (optional) |
| Hub Metadata | Full hub_metadata block | Minimal (agent_id, session_id) |

---

## Related Documents

- [Enterprise Memory](../enterprise-memory/README.md) — Organizational memory
- [Agent Memory](../agent-memory/README.md) — Agent-level memory
- [CAF README](../../cognitive-audit-fabric/README.md) — CAF integration
- [Enterprise Learning Services](../../cognitive-audit-fabric/enterprise-learning-services.md) — Promotion workflows

