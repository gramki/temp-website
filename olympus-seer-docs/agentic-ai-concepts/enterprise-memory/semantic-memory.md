# Semantic Enterprise Memory (Learned)

## Definition

**Semantic Enterprise Memory** captures **learned beliefs and patterns derived from experience**.

Unlike enterprise knowledge (asserted truth), semantic enterprise memory is:

- **probabilistic** (confidence-scored)
- **revisable** (challengeable)
- **scoped** (context-dependent)
- **grounded in episodes** (traceable to supporting evidence)

It answers:

> *“What have we learned from experience that should inform future decisions?”*

## Scope clarification (agent vs enterprise)

- **Semantic enterprise memory (this doc)**: institutional learned patterns/hypotheses derived from episodes (shared across agents and humans).
- **Semantic agent memory**: an agent’s local store of stable facts/concepts used to act in-the-moment.  
  See: [../agent-memory/semantic-memory.md](../agent-memory/semantic-memory.md)

## What belongs here (signals worth remembering)

Semantic memory arises from **patterns across episodes**, not single events.

Common sources:

- recurring incident clusters with common precursors
- repeated override rationales (“we keep accepting this risk under these conditions”)
- consistent failure modes in a workflow/tool chain
- anomaly analysis and investigations
- model evaluation results (“agent strategy A outperforms B under condition C”)

## Capture (recommended artifacts)

Capture semantic memory as **hypotheses with evidence**, not as “facts”.

Recommended artifact shapes:

- **HypothesisRecord**: statement, scope, confidence, supporting episodes, counterexamples
- **PatternSummary**: pattern description, features/conditions, observed outcomes, caveats
- **LearnedConstraint**: “avoid X when Y”; scope, confidence, expiry/review date
- **EvaluationFinding**: benchmark result, population, metric, significance, regression notes

Minimum capture fields:

- **statement** (what is believed)
- **scope** (where it applies; explicit exclusions)
- **confidence** (and how computed)
- **evidence links** (episodes, cases, incident timelines, decisions)
- **freshness** (last corroborated, decay model)
- **owner for review** (who can promote/retire it)

## Retention & forgetting

Semantic memory should weaken before it disappears.

- **confidence decay** without reinforcement
- **replacement** by stronger, newer patterns
- **explicit invalidation** when disproven
- **scheduled review** for high-impact hypotheses

Treat semantic memory as **decision support**, not binding constraint, until promoted.

## Retrieval (how it gets used)

Retrieval is usually:

- **query-by-condition** (“under these inputs, what patterns matter?”)
- **entity-/segment-conditioned** (“for this product/customer segment, what’s learned?”)
- **risk- and exception-aware** (“when do we tend to override?”)

In agentic systems, semantic memory is valuable for:

- risk calibration (“this approach often fails in region X”)
- proactive escalation (“pattern suggests high probability of dispute”)
- decision explanation (“we acted cautiously due to learned pattern P”)

## Promotion (semantic memory → knowledge)

Semantic memory may be promoted to **Enterprise Knowledge** when:

- evidence is strong and replicated
- scope is clear and stable
- governance accepts the commitment (policy/standard/definition update)

Promotion creates **new truth** (versioned, owned, enforceable). Until then, semantic memory remains **informative**, not normative.

## Governance (non-negotiables)

- **Provenance**: every semantic claim must link back to episodic evidence
- **Challengeability**: make it easy to contest and retire hypotheses
- **Scope discipline**: unclear scope is the fastest path to overgeneralization
- **Guard against “policy laundering”**: do not let repeated decisions silently become policy without explicit promotion

## Common failure modes

- **Treating learned patterns as truth**: memory becomes policy without governance
- **No counterexamples**: only storing supporting evidence creates brittle beliefs
- **Stale beliefs**: no decay, no review cadence, no supersession model

## Further reading

- Tulving, E. *Elements of Episodic Memory* (semantic memory as generalized learning): [https://psycnet.apa.org/record/1984-98218-000](https://psycnet.apa.org/record/1984-98218-000)
- Zhou et al., *Exploring Agent Procedural and Semantic Memory* (formation/refinement of learned memory): [https://arxiv.org/html/2508.06433v2](https://arxiv.org/html/2508.06433v2)
- Wang et al., *A Survey on the Memory Mechanism of LLM‑Based Agents* (semantic memory extraction from episodic traces): [https://dl.acm.org/doi/10.1145/3748302](https://dl.acm.org/doi/10.1145/3748302)

## Related concepts (Hub docs)

- [../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md](../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md): CAF policy enforcement, retention, audit trails
- [../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md](../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md): Promotion to Enterprise Knowledge (stub)

## Navigation

- Back to overview: [README.md](./README.md)
- Prev: [episodic-memory.md](./episodic-memory.md)
- Next: [procedural-memory.md](./procedural-memory.md)

