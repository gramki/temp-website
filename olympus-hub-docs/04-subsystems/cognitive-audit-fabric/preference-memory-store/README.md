# Preference Memory Store

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Class**: Preference (ESPP)  
> **Related**: [CAF README](../README.md) | [Enterprise Learning Services](../enterprise-learning-services.md)

---

## Overview

The **Preference Memory Store** contains **learned preferences and behavioral patterns** — observations about how users and agents prefer to work, communicate, and make decisions. These are inferred from consistent choices, not explicitly stated settings.

### Core Distinction

| Preference Memory | Explicit Settings |
|-------------------|-------------------|
| **Learned** from observation | **Configured** by user/admin |
| **Inferred** from behavior | **Stated** explicitly |
| **Probabilistic** ("tends to prefer") | **Deterministic** ("always use") |
| **Contextual** (may vary by situation) | **Global** (applies everywhere) |
| **Evolving** (updates with new evidence) | **Static** (until changed) |
| **Advisory** (guides personalization) | **Binding** (enforces behavior) |

> **Key Insight**: Preference Memory captures *what we've learned about how someone prefers things* — it informs personalization without overriding explicit settings.

---

## Record Types

| Record Type | Description | Status |
|-------------|-------------|--------|
| [User Preference](./user-preferences.md) | Learned preferences for human users | 🟡 Draft |
| [Agent Behavior](./agent-behaviors.md) | Observed agent behavioral patterns | 🟡 Draft |
| [Interaction Pattern](./interaction-patterns.md) | How entities prefer to interact | 🟡 Draft |
| [Contextual Preference](./contextual-preferences.md) | Context-dependent preferences | 🟡 Draft |
| [Record Relationships](./record-relationships.md) | How records link and traversal patterns | 🟡 Draft |

---

## Anchoring and Scope

Preference Memory is **subject-anchored** — preferences belong to a subject (user or agent):

```
subject_id ─────┬──── User Preference
                │
                ├──── Agent Behavior
                │
                ├──── Interaction Pattern
                │
                └──── Contextual Preference
```

### Subject Types

| Subject Type | Description | Example |
|--------------|-------------|---------|
| **User** | Human operator/customer | User prefers detailed explanations |
| **Agent** | Employed agent instance | Agent tends toward conservative decisions |
| **Role** | All users/agents in role | Investigators prefer tabular data |
| **Workbench** | Domain-level default | Fraud ops prefers formal communication |

---

## Hub Metadata

All preference records include optional `hub_metadata` for context:

```yaml
hub_metadata:
  tenant_id: string          # Enterprise tenant
  subscription_id: string    # Subscription context
  workbench_id: string       # Domain context (if workbench-scoped)
  # Note: No scenario_id/request_id — preferences are not case-bound
```

---

## Promotion Source

Preference Memory records are promoted from **Episodic Memory** via [Enterprise Learning Services](../enterprise-learning-services.md):

```
Episodic Memory                    Preference Memory
─────────────────                  ──────────────────
DecisionRecord      ──┐
  + choices made       │
  + alternatives       ├──► Pattern Detection ──► UserPreference
    available          │                          AgentBehavior
  + consistent over   ─┘                          InteractionPattern
    time
```

### Promotion Triggers

| Pattern Detected | Preference Record Created |
|------------------|---------------------------|
| User consistently chooses option A over B | UserPreference |
| Agent repeatedly uses strategy X | AgentBehavior |
| Parties prefer communication style Y | InteractionPattern |
| Preference varies by context C | ContextualPreference |

---

## Preference Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Communication** | How to communicate | Verbose vs. concise, formal vs. casual |
| **Presentation** | How to present information | Tables vs. prose, charts vs. numbers |
| **Risk** | Risk tolerance | Conservative vs. aggressive |
| **Timing** | Temporal preferences | Quick response vs. thorough analysis |
| **Interaction** | Interaction style | Proactive vs. reactive, frequent vs. batched |
| **Escalation** | Escalation tendencies | Early escalation vs. autonomous resolution |

---

## Lifecycle

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Observed   │───►│   Active    │───►│   Stable    │───►│  Archived   │
│   (new)     │    │   (in use)  │    │  (proven)   │    │  (stale)    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │
      │                  │                  │
      ▼                  ▼                  ▼
   Detected by       Applied to           May inform
   Learning          personalize          explicit
   Services          experience           settings
```

---

## Precedence with Explicit Settings

When both learned preferences and explicit settings exist:

| Scenario | Resolution |
|----------|------------|
| Explicit setting exists | Setting wins, preference ignored |
| No explicit setting, preference exists | Preference applies |
| Conflicting preferences (context-dependent) | Most specific context wins |
| No preference, no setting | System default applies |

---

## Privacy Considerations

Preference Memory contains potentially sensitive personal information:

| Consideration | Approach |
|---------------|----------|
| **Transparency** | Users can view their learned preferences |
| **Correction** | Users can override/delete learned preferences |
| **Minimization** | Only capture decision-relevant preferences |
| **Retention** | Preferences decay with stale evidence |
| **Scope limiting** | Preferences don't leak across workbenches |

---

## Conventions

### IDs
- All IDs are **UUID v4**
- Primary key: `preference_id`, `behavior_id`, `pattern_id`
- Subject reference: `subject_id` (user_id or agent_id)

### Content Typing
- All structured content follows the [Typed Content Convention](../README.md#typed-content-convention)
- Default format: JSON

### Serialization
- Human-readable formats only (JSON default, YAML allowed)
- See [Serialization Requirements](../README.md#serialization-format-requirements)

---

## Related Documents

- [CAF README](../README.md) — Cognitive Audit Fabric overview
- [Episodic Memory Store](../episodic-memory-store/README.md) — Source of preference patterns
- [Enterprise Learning Services](../enterprise-learning-services.md) — Promotion orchestration
- [Semantic Memory Store](../semantic-memory-store/README.md) — Related beliefs

