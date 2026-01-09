# Procedural Memory Store

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Class**: Procedural (ESPP)  
> **Related**: [CAF README](../README.md) | [Enterprise Learning Services](../enterprise-learning-services.md)

---

## Overview

The **Procedural Memory Store** contains **learned capabilities** — skills, procedures, and action patterns derived from observing successful agent behavior across episodic data. These are "how-to" records that encode effective ways of accomplishing tasks.

### Core Distinction

| Procedural Memory | Enterprise Knowledge (SOPs) |
|-------------------|----------------------------|
| **Learned** from observation | **Authored** by experts |
| **Probabilistic** (success rate) | **Normative** (must follow) |
| **Advisory** ("this works well") | **Mandatory** ("you must do this") |
| **Agent-specific** or role-scoped | **Organization-wide** |
| **Emergent** from experience | **Prescribed** by policy |
| **Evolvable** automatically | **Versioned** through governance |

> **Key Insight**: Procedural Memory captures *what agents have learned works* — it complements, not replaces, normative SOPs in Enterprise Knowledge.

---

## Record Types

| Record Type | Description | Status |
|-------------|-------------|--------|
| [Learned Skill](./learned-skills.md) | A capability learned from successful patterns | 🟡 Draft |
| [Procedure](./procedures.md) | Step-by-step guidance derived from cases | 🟡 Draft |
| [Action Sequence](./action-sequences.md) | Successful tool invocation patterns | 🟡 Draft |
| [Tool Usage Pattern](./tool-usage-patterns.md) | Effective tool combinations and orderings | 🟡 Draft |
| [Record Relationships](./record-relationships.md) | How records link and traversal patterns | 🟡 Draft |

---

## Anchoring and Scope

Unlike Episodic Memory (case-bound) or Semantic Memory (entity-anchored), Procedural Memory is **skill-anchored**:

```
skill_id ─────┬──── Learned Skill
              │
              ├──── Procedure (implements skill)
              │
              ├──── Action Sequence (patterns for skill)
              │
              └──── Tool Usage Pattern (tools for skill)
```

### Scope Hierarchy

| Scope | Description | Example |
|-------|-------------|---------|
| **Agent-specific** | Learned by a specific employed agent | "agent-fraud-001's investigation style" |
| **Role-scoped** | Shared across agents with same role | "Senior Investigator skills" |
| **Workbench-scoped** | Shared within a domain | "Fraud Ops investigation patterns" |
| **Enterprise-wide** | Cross-domain skills | "Customer communication skills" |

---

## Hub Metadata

All procedural records include optional `hub_metadata` for context:

```yaml
hub_metadata:
  tenant_id: string          # Enterprise tenant
  subscription_id: string    # Subscription context
  workbench_id: string       # Domain (primary anchor for procedural)
  # Note: No scenario_id/request_id — procedural is not case-bound
```

---

## Promotion Source

Procedural Memory records are promoted from **Episodic Memory** via [Enterprise Learning Services](../enterprise-learning-services.md):

```
Episodic Memory                    Procedural Memory
─────────────────                  ──────────────────
DecisionRecord      ──┐
  + action taken       │
  + successful outcome ├──► Pattern Detection ──► LearnedSkill
  + repeated across    │                          Procedure
    multiple cases    ─┘                          ActionSequence
```

### Promotion Triggers

| Pattern Detected | Procedural Record Created |
|------------------|---------------------------|
| Same action sequence succeeds repeatedly | ActionSequence |
| Consistent resolution steps across similar cases | Procedure |
| Agent develops effective capability for task type | LearnedSkill |
| Tools used together effectively | ToolUsagePattern |

---

## Lifecycle

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Candidate  │───►│   Active    │───►│  Validated  │───►│  Archived   │
│   (new)     │    │   (in use)  │    │  (proven)   │    │ (obsolete)  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │
      │                  │                  │
      ▼                  ▼                  ▼
   Created by        Used by agents     May promote to
   Learning          Success tracked    Enterprise SOP
   Services          via outcomes       (Knowledge)
```

---

## Relationship to Enterprise Knowledge

Procedural Memory can be **promoted to Enterprise Knowledge** when:

1. Skill/procedure is validated across many agents
2. Success rate exceeds threshold (e.g., 95%)
3. Governance review approves formalization
4. The capability should become normative (mandatory)

**Promotion path**: Procedural Memory → Enterprise Learning Services → Governance → Enterprise Knowledge (SOP)

---

## Conventions

### IDs
- All IDs are **UUID v4**
- Primary key: `skill_id`, `procedure_id`, `sequence_id`, or `pattern_id`

### Content Typing
- All structured content follows the [Typed Content Convention](../README.md#typed-content-convention)
- Default format: JSON

### Serialization
- Human-readable formats only (JSON default, YAML allowed)
- See [Serialization Requirements](../README.md#serialization-format-requirements)

---

## Related Documents

- [CAF README](../README.md) — Cognitive Audit Fabric overview
- [Episodic Memory Store](../episodic-memory-store/README.md) — Source of procedural patterns
- [Enterprise Learning Services](../enterprise-learning-services.md) — Promotion orchestration
- [Enterprise Knowledge](../../../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/README.md) — Normative SOPs

