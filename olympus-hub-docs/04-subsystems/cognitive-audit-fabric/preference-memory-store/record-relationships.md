# Preference Memory Record Relationships

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [Preference Memory README](./README.md)

---

## Overview

Preference Memory records are **subject-anchored** — preferences belong to a subject (user, agent, or role), with contextual variations layered on top.

---

## Relationship Diagram

```
                         SUBJECT
                     (user_id / agent_id)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
  USER PREFERENCE       AGENT BEHAVIOR      INTERACTION PATTERN
   (preference_id)       (behavior_id)          (pattern_id)
        │                     │                     │
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                              ▼
                   CONTEXTUAL PREFERENCE
                      (preference_id)
                              │
                              ▼
                     EPISODIC MEMORY
                       (case_ids)
```

---

## Traversal Patterns

### Pattern 1: Subject-Down (All Preferences for Entity)

Starting from a subject (user or agent), find all learned preferences:

```
subject_id (user_id or agent_id)
  └── (query UserPreference WHERE subject.user_id = X) ──► UserPreference[]
  └── (query AgentBehavior WHERE subject.agent_id = X) ─► AgentBehavior[]
  └── (query InteractionPattern WHERE parties contains X) ► InteractionPattern[]
  └── (query ContextualPreference WHERE subject_id = X) ─► ContextualPreference[]
```

**Use case**: "What do we know about this user/agent's preferences?"

### Pattern 2: Preference-to-Context (Contextual Variations)

Starting from a base preference, find contextual variations:

```
base_preference_id
  └── (query ContextualPreference WHERE base_preference.preference_id = X)
      └── ContextualPreference[] (all contextual variations)
```

**Use case**: "When does this preference change?"

### Pattern 3: Context-Based Resolution

Given a subject and current context, find applicable preferences:

```
subject_id + context_factors
  │
  ├── Find matching ContextualPreference (most specific match)
  │   └── If found: Apply contextual preference
  │
  └── Fall back to base UserPreference / AgentBehavior
      └── If found: Apply base preference
      └── If not: Use system default
```

**Use case**: "What preference applies right now?"

### Pattern 4: Interaction Discovery

Find interaction patterns involving an entity:

```
party_id
  └── (query InteractionPattern WHERE parties.party_id = X)
      └── InteractionPattern[]
          └── parties[] ──► Other involved parties
```

**Use case**: "How does this entity interact with others?"

### Pattern 5: Evidence Trail (To Episodic)

Any preference record can trace back to episodic evidence:

```
[Any Preference Record]
  └── evidence.sample_episodes[] ──► CaseRecord[]
      └── DecisionRecord (what choices were made)
      └── ContextSnapshot (what context was present)
```

**Use case**: "What observations led to learning this preference?"

---

## Key Relationships

| From | To | Relationship | Cardinality |
|------|-----|--------------|-------------|
| UserPreference | User | subject.user_id | N:1 |
| AgentBehavior | Agent | subject.agent_id | N:1 |
| InteractionPattern | User/Agent | parties[].party_id | N:N |
| ContextualPreference | UserPreference/AgentBehavior | base_preference | N:1 |
| ContextualPreference | Subject | subject.subject_id | N:1 |
| All Records | CaseRecord | evidence.sample_episodes | N:N |

---

## Subject Types and Scope

```
                    ENTERPRISE
                        │
            ┌───────────┼───────────┐
            │           │           │
        WORKBENCH   WORKBENCH   WORKBENCH
            │
      ┌─────┼─────┐
      │     │     │
    ROLE  ROLE  ROLE
      │
    ┌─┴─┐
    │   │
  USER AGENT
```

Preferences can exist at any level:
- **Enterprise**: Cross-domain defaults
- **Workbench**: Domain-specific preferences
- **Role**: Role-based preferences
- **Individual**: User or agent specific

**Resolution**: More specific wins (Individual > Role > Workbench > Enterprise)

---

## Cross-Memory Relationships

### To Episodic Memory (Evidence Source)

```
Preference Record
    │
    └── evidence.sample_episodes[]
        │
        └── CaseRecord (episodic)
            └── DecisionRecord (choices that indicated preference)
            └── ContextSnapshot (context when preference observed)
```

### From Episodic Memory (Promotion)

```
Enterprise Learning Services
    │
    └── Detects pattern in Episodic:
        │   - Consistent choices over time
        │   - Behavioral patterns
        │
        └── Creates Preference:
            - UserPreference
            - AgentBehavior
            - InteractionPattern
            - ContextualPreference
```

### To Semantic Memory (Correlated Beliefs)

```
UserPreference / AgentBehavior
    │
    └── Semantic Memory may contain:
        │   - HypothesisRecord ("Users who prefer X also prefer Y")
        │   - PatternSummary ("Preference correlates with outcome")
        │
        └── Semantic beliefs inform preference inference
```

### To Procedural Memory (Skill Context)

```
AgentBehavior
    │
    └── May inform how skills are applied:
        │   - LearnedSkill + AgentBehavior → Personalized execution
        │   - Procedure may reference agent behavioral preferences
```

---

## Query Examples

### "Get all preferences for a user"

```
GET /preference/user/{user_id}/all
  ?include_contextual=true
  &include_interaction_patterns=true
```

### "Get applicable preference for user in context"

```
GET /preference/resolve
  ?subject_id={user_id}
  &category=communication
  &dimension=verbosity
  &context.time_pressure=urgent
  &context.workload=heavy
```

### "Get interaction patterns for user-agent pair"

```
GET /preference/interactions
  ?party_ids={user_id},{agent_id}
  &interaction_type=handoff
```

### "Get agent behaviors flagged for review"

```
GET /preference/agent-behaviors
  ?status=flagged
  &assessment.alignment=concerning
```

---

## Preference Resolution Algorithm

```python
def resolve_preference(subject_id, category, dimension, context):
    # 1. Find contextual preferences matching context
    contextual = find_contextual_preferences(
        subject_id, category, dimension, context
    )
    
    if contextual:
        # Return most specific match (most context factors)
        return max(contextual, key=lambda p: p.context_specificity)
    
    # 2. Fall back to base preference
    base = find_base_preference(subject_id, category, dimension)
    
    if base:
        return base
    
    # 3. Check role-level preference
    role = get_subject_role(subject_id)
    role_pref = find_role_preference(role, category, dimension)
    
    if role_pref:
        return role_pref
    
    # 4. Check workbench default
    workbench = get_subject_workbench(subject_id)
    workbench_pref = find_workbench_default(workbench, category, dimension)
    
    if workbench_pref:
        return workbench_pref
    
    # 5. System default
    return get_system_default(category, dimension)
```

---

## Relationship Invariants

1. **Subject Link**: Every preference must reference a valid subject (user_id or agent_id)

2. **Evidence Required**: All records must have at least one evidence link to episodic memory

3. **Contextual → Base**: Every ContextualPreference should reference a valid base preference

4. **Interaction Bidirectional**: InteractionPatterns should be discoverable from any party

5. **Consistency Check**: Contextual preferences should not contradict each other for overlapping contexts

---

## Related Documents

- [Episodic Memory Relationships](../episodic-memory-store/record-relationships.md)
- [Semantic Memory Relationships](../semantic-memory-store/record-relationships.md)
- [Procedural Memory Relationships](../procedural-memory-store/record-relationships.md)
- [Enterprise Learning Services](../enterprise-learning-services.md) — Promotion flows

