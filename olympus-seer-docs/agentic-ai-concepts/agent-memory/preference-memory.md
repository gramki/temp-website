# Preference Agent Memory

## Definition

**Preference Agent Memory** captures learned or stated **biases that guide behavior** (format, tone, risk appetite, tool choices, etc.).

It answers:

> *“How should I behave for this user/environment, given past feedback?”*

Preferences are typically **soft constraints** (advisory) rather than rules.

## When preference memory applies

Preference memory is appropriate when:

- there is a **choice set** (multiple acceptable behaviors/actions)
- repeated feedback reveals a **stable bias** (e.g., concise vs verbose)
- the bias is **contextual** (per-user, per-tenant, per-application)

Preference memory is not appropriate when:

- the constraint is **binding** (security/compliance/policy) → model as policy/knowledge
- it is a **one-off signal** → keep in episodic memory until it repeats

## What to store

- **Interaction preferences**: verbosity, tone, format (“bullets”, “tables”), language
- **Tooling preferences**: “prefer tool A over tool B” under conditions
- **Risk preferences**: “escalate earlier”, “be conservative by default”

## Storage patterns

- **Typed key-value** with confidence (e.g., `verbosity=concise`, `confidence=0.7`)
- **Scoped namespaces** (user/app/tenant) with explicit precedence rules
- **Decay model** (preferences weaken without reinforcement)

## Retrieval + conflict resolution

- Retrieve preferences by scope: user → app → tenant → default
- Resolve conflicts by: explicit user statement > repeated behavior > inferred weak signals

## Failure modes to guard against

- **Overfitting**: one interaction becomes permanent preference
- **Sticky mislearning**: wrong preference persists without decay/review
- **Preference-policy conflict**: preferences must not override policy/knowledge constraints

## Navigation

- Back: [README.md](./README.md)
- Prev: [semantic-memory.md](./semantic-memory.md)
- Next: [procedural-memory.md](./procedural-memory.md)

