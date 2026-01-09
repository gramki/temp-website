# Procedural Memory Record Relationships

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [Procedural Memory README](./README.md)

---

## Overview

Procedural Memory records are **skill-anchored** — the `LearnedSkill` serves as the primary aggregation point, with procedures, action sequences, and tool usage patterns linked to it.

---

## Relationship Diagram

```
                         LEARNED SKILL
                        (skill_id: uuid)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   PROCEDURE           ACTION SEQUENCE       TOOL USAGE PATTERN
 (procedure_id)          (sequence_id)           (pattern_id)
        │                     │                     │
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   TOOL REGISTRY     │
                    │   (tool_id refs)    │
                    └─────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │  EPISODIC MEMORY    │
                    │    (case_ids)       │
                    └─────────────────────┘
```

---

## Traversal Patterns

### Pattern 1: Skill-Down (From Skill to Details)

Starting from a skill, traverse to all implementing artifacts:

```
skill_id
  └── implements[] ──────────► Procedure[]
  └── patterns[] ────────────► ActionSequence[]
  └── tool_patterns[] ───────► ToolUsagePattern[]
```

**Use case**: "Show me everything we know about this skill"

### Pattern 2: Procedure-to-Examples

Starting from a procedure, find concrete execution examples:

```
procedure_id
  └── (query ActionSequence WHERE procedure_id = X) ──► ActionSequence[]
      └── evidence.source_episodes[] ──────────────► CaseRecord[] (episodic)
```

**Use case**: "Show me actual executions of this procedure"

### Pattern 3: Tool-to-Patterns

Starting from a tool, find effective usage patterns:

```
tool_id
  └── (query ToolUsagePattern WHERE tools contains tool_id) ──► ToolUsagePattern[]
      └── skill_id ──────────────────────────────────────────► LearnedSkill
```

**Use case**: "How is this tool best used? What skills need it?"

### Pattern 4: Evidence Trail (To Episodic)

Any procedural record can trace back to episodic evidence:

```
[Any Procedural Record]
  └── evidence.source_episodes[] ──► CaseRecord[]
  └── evidence.episode_refs[] ─────► CaseRecord[]
      └── (full episodic traversal available from there)
```

**Use case**: "What cases led to learning this skill/procedure?"

### Pattern 5: Cross-Memory (Semantic Correlation)

Link to semantic memory for beliefs about the skill:

```
skill_id
  └── (query SemanticMemory WHERE subject.entity_id = skill_id)
      └── HypothesisRecord ("This skill works better for X cases")
      └── PatternSummary ("Skill success correlates with Y")
```

**Use case**: "What have we learned about when this skill works?"

---

## Key Relationships

| From | To | Relationship | Cardinality |
|------|-----|--------------|-------------|
| LearnedSkill | Procedure | implements | 1:N |
| LearnedSkill | ActionSequence | patterns | 1:N |
| LearnedSkill | ToolUsagePattern | tool_patterns | 1:N |
| Procedure | LearnedSkill | skill_id | N:1 |
| Procedure | ActionSequence | exemplified_by | 1:N (implicit) |
| ActionSequence | LearnedSkill | skill_id | N:1 |
| ActionSequence | Procedure | procedure_id | N:1 |
| ActionSequence | CaseRecord | evidence.source_episodes | N:N |
| ToolUsagePattern | LearnedSkill | skill_id | N:1 |
| ToolUsagePattern | ActionSequence | evidence.source_sequences | N:N |
| All Records | Tool Registry | tool_id refs | N:N |

---

## Scope Filtering

All traversals can be filtered by scope:

```yaml
# Workbench-scoped query
GET /procedural/skills
  ?workbench_id=wb-fraud-ops-001
  &status=validated

# Role-scoped query  
GET /procedural/skills
  ?scope.level=role
  &scope.role=senior_fraud_investigator
```

### Scope Hierarchy

```
Enterprise-wide
    └── Workbench-scoped
        └── Role-scoped
            └── Agent-specific
```

Skills at broader scopes are shared; narrower scopes are more specialized.

---

## Cross-Memory Relationships

### To Episodic Memory

```
Procedural Record
    │
    └── evidence.source_episodes[] / episode_refs[]
        │
        └── CaseRecord (episodic)
            └── DecisionRecord (what decisions were made)
            └── OutcomeRecord (how it turned out)
            └── ContextSnapshot (what context was used)
```

### From Episodic Memory (Promotion)

```
Enterprise Learning Services
    │
    └── Detects pattern in Episodic:
        │   - Repeated successful action sequences
        │   - Consistent resolution patterns
        │
        └── Creates Procedural:
            - LearnedSkill
            - Procedure
            - ActionSequence
            - ToolUsagePattern
```

### To/From Semantic Memory

```
LearnedSkill
    │
    └── Semantic Memory may contain:
        │   - HypothesisRecord about skill effectiveness
        │   - PatternSummary about usage contexts
        │
        └── Semantic beliefs inform skill evolution
```

---

## Query Examples

### "Get all validated skills for fraud investigation"

```
GET /procedural/skills
  ?task_types=fraud_case_investigation
  &status=validated
  &scope.level=workbench
  &workbench_id=wb-fraud-ops-001
```

### "Get procedures implementing a skill with success > 80%"

```
GET /procedural/procedures
  ?skill_id={skill_id}
  &metrics.success_rate[gte]=0.80
  &status=active
```

### "Get action sequences for a procedure"

```
GET /procedural/sequences
  ?procedure_id={procedure_id}
  &status=template
```

### "Get tool usage patterns for a tool"

```
GET /procedural/tool-patterns
  ?tools.tool_id={tool_id}
  &status=recommended
```

---

## Relationship Invariants

1. **Skill Anchor**: Every Procedure, ActionSequence, and ToolUsagePattern should reference a `skill_id` (may be null during early observation)

2. **Evidence Links**: All records must have at least one evidence link to episodic memory for traceability

3. **Scope Consistency**: Child records (Procedure, ActionSequence) should have scope ≤ parent skill scope

4. **Status Propagation**: If a LearnedSkill is deprecated, child records should be reviewed for deprecation

---

## Related Documents

- [Episodic Memory Relationships](../episodic-memory-store/record-relationships.md)
- [Semantic Memory Relationships](../semantic-memory-store/record-relationships.md)
- [Enterprise Learning Services](../enterprise-learning-services.md) — Promotion flows

