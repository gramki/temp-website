# Preference Enterprise Memory

## Definition

**Preference Enterprise Memory** captures **revealed priorities and trade-offs** in how the organization actually decides:

- what risk it accepts in practice
- what it prioritizes under constraint
- where it tolerates SLA breaches
- what it repeatedly overrides (and why)

It answers:

> *“Given repeated choices, what do we tend to favor?”*

Preference memory is often politically and operationally sensitive because it can expose misalignment between stated policy and real behavior.

## When preference memory is applicable (and when it isn’t)

Preference memory is applicable when:

- there is a **choice set** (multiple defensible actions/options)
- the outcome is governed by a **trade-off** (loss vs friction, speed vs certainty, cost vs risk)
- the organization exhibits a **repeatable bias** in that trade-off across many cases
- the bias is **not explicitly codified** as a policy/rule (or is observed to diverge from it)

Preference memory is **not** the right construct when:

- the behavior is **binding** (regulatory, contractual, safety-critical) → model as **Enterprise Knowledge** (policy/standard)
- the content is a **learned pattern about the world** (“this feature correlates with fraud”) → model as **Semantic Enterprise Memory**
- it is a **one-off exception** without repetition → keep as **Episodic Enterprise Memory** (override/decision record), but don’t generalize yet

Practical test:

> If you can say “we tend to choose A over B when conditions C hold”, you are likely in preference-memory territory.

## What belongs here (signals worth remembering)

Preference memory is inferred from **choice patterns**, especially under constraint:

- repeated overrides in the same direction (leniency vs strictness)
- consistent prioritization of one customer segment/channel over others
- escalation aversion or escalation bias
- “we always do X when Y, even though policy says Z”
- tolerated exceptions and the conditions that justify them

Strong candidates for preference memory (high-signal patterns):

- **Override-rate asymmetries**: one team/shift/channel repeatedly overrides a control in the same direction
- **Stable thresholds in practice**: analysts consistently “act at ~X” even when models/policies don’t specify X
- **Routing bias**: “send to manual review” vs “step-up auth” preference by segment or geography
- **Time-pressure behaviors**: different choices near SLA breach windows (e.g., more auto-approve to clear queues)
- **Customer-impact prioritization**: repeated decisions that minimize customer friction even at higher expected loss (or the inverse)

## Capture (recommended artifacts)

Preference memory should be captured as **aggregated, interpretable evidence**, not as “the enterprise prefers X” assertions.

Recommended artifact shapes:

- **ChoicePatternSummary**: repeated choice, context features, frequency, outcome distribution
- **OverrideStatistics**: override rate by policy/rule, approver group, segment, jurisdiction
- **TradeoffProfile**: observed trade-offs (speed vs certainty; fraud loss vs friction), with time windows
- **ToleranceThreshold**: inferred thresholds (“escalate only after N failures”), with confidence

Minimum capture fields:

- **pattern statement** (what seems preferred)
- **conditions/features** (when it holds)
- **evidence window** (time range, sample size)
- **confidence** (and sensitivity/robustness)
- **outcomes** (did the preference lead to better/worse results?)
- **review owner** (who can validate, challenge, or act on it)

## Retention & forgetting

Preferences are not permanent.

Recommended mechanisms:

- **decay without reinforcement** (preferences weaken if behavior changes)
- **reset on policy/leadership shifts** (new regimes create new patterns)
- **time-windowed reporting** (avoid mixing different operating contexts)

## Retrieval (how it gets used)

Preference memory is most useful for:

- surfacing likely operator choices (“historically we accept this exception under X”)
- flagging drift from policy (“practice diverges from written truth”)
- prioritization guidance (“these cases tend to get escalated faster”)

In agentic systems, treat preference memory as **advisory**:

- it can inform decision calibration
- it must not override enterprise knowledge/policy constraints

## Promotion (preference → knowledge)

Preference memory should trigger **deliberate review**, not automatic policy updates.

Common promotion outcomes:

- revise policy to match reality (if acceptable)
- strengthen enforcement if drift is undesirable
- adjust incentives, tooling, or training
- introduce explicit exception rules with bounded scope

## Governance (non-negotiables)

- **Avoid normativity by accident**: “we tend to do X” must not become “we should do X” without governance
- **Fairness and compliance checks**: preferences can encode bias; evaluate impacts
- **Privacy and aggregation**: keep preference artifacts aggregated where possible
- **Explainability**: always pair preferences with evidence and outcomes

## Examples (transaction fraud) + modeling guidance

In fraud decisioning, “preference” usually manifests as *how the organization chooses among*:

- **decline vs approve vs step-up authentication vs manual review**
- **how aggressive thresholds are**
- **which customer experience to optimize** under fraud and operational constraints

### Single-variable preferences (categorical or numerical)

Single-variable preferences are anchored to one primary feature/attribute (often conditional on a simple scope like region/product).

- **Categorical**: “Prefer **step-up authentication** over **manual review** for `channel = ecomm`.”
  - Choice set: {step-up, manual review}
  - Variable: `channel` (categorical)
  - Signal: repeated routing decisions for similar ecomm cases

- **Numeric / threshold**: “Prefer **auto-decline** when `risk_score ≥ 0.92`.”
  - Choice set: {decline, step-up, manual review, approve}
  - Variable: `risk_score` (numeric)
  - Signal: stable analyst/model-ops threshold emerging from actions over time

### Multi-variable preferences (trade-offs / conditional)

Multi-variable preferences express a **trade-off** or a **conditional policy-shaped bias** without being formal policy.

- **Trade-off (loss vs friction)**: “Prefer **step-up** (not decline) when `amount < $200` and `customer_tenure > 2y`, even if `risk_score` is high, because false declines are costly.”
  - Variables: `amount`, `customer_tenure`, `risk_score`
  - Encodes a utility trade-off (customer friction/complaints vs fraud loss)

- **Operational constraint conditional**: “Prefer **auto-approve** for borderline cases when `review_queue_depth` is high and `SLA_time_remaining < 15m`, unless `device_reputation` is very low.”
  - Variables: `review_queue_depth`, `SLA_time_remaining`, `device_reputation`
  - Captures time-pressure behavior that otherwise becomes invisible drift

- **Segment-conditioned strictness**: “Prefer **manual review** (not step-up) when `merchant_category = crypto` and `geo = cross-border` and `device_reputation` is unknown.”
  - Variables: `merchant_category`, `geo`, `device_reputation`
  - Captures “where we want humans in the loop” preferences

### Modeling guidance (how to represent preference memory)

Model preference memory as a **relation over alternatives** (a choice set) with explicit scope/conditions. Variables (categorical or numerical) usually appear in the **conditions** and **evidence summaries**, but the preference itself is about **choosing among options**.

Recommended fields (minimum viable schema):

- **choice_set**: the alternatives (e.g., `{approve, decline, step_up, manual_review}`)
- **preferred_order / winner**: preferred option(s) or ranking (e.g., `step_up > manual_review > decline`)
- **conditions (scope)**: feature predicates that define applicability (can reference categorical and numeric variables)
- **strength**: how strong the preference is (e.g., probability/odds ratio, confidence score, or “soft/medium/hard”)
- **evidence_window**: time range + sample size; segmentation notes
- **outcomes**: impact metrics (fraud loss, false-positive rate, customer complaints, conversion drop, SLA adherence)
- **exceptions / guardrails**: explicit “do not apply when …” conditions
- **owner + review cadence**: who validates it and how often it’s revisited

Recommended practices:

- **Prefer conditional expressions over prose** for applicability (even if stored alongside a narrative)
- **Store both**: (a) the preference statement and (b) the aggregated evidence that justifies it
- **Do not treat preference as policy**: preferences inform; policies constrain (until promotion)
- **Detect and record conflicts**: two preferences can apply; you need tie-breakers (freshness, strength, policy precedence)

## Common failure modes

- **Overfitting to small samples**: a few overrides become a “preference”
- **Confusing preference with policy**: drift becomes precedent becomes “rule”
- **Ignoring outcomes**: preferences that harm outcomes persist unnoticed

## Further reading

- Kahneman, D. *Thinking, Fast and Slow* (biases and revealed preferences): [https://us.macmillan.com/books/9780374533557](https://us.macmillan.com/books/9780374533557)
- Christiano et al., *Deep Reinforcement Learning from Human Preferences* (learning from behavior): [https://arxiv.org/abs/1706.03741](https://arxiv.org/abs/1706.03741)
- Ouyang et al., *Training Language Models with Human Feedback* (preference learning as a first-class signal): [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)

## Related concepts (Hub docs)

- [`../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md`](../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md): CAF governance (consent, retention, access logging)
- [`../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md`](../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md): Exception history and override records (stub)

## Navigation

- Back to overview: [`README.md`](./README.md)
- Prev: [`procedural-memory.md`](./procedural-memory.md)

