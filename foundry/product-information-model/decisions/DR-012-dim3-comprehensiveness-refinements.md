# DR-012: Customer Value Comprehensiveness Refinements — Buying Committee, Pain, Barrier Types

**Status:** Accepted
**Date:** 2026-02-15

## Context

A critical review of Customer Value identified several gaps in the model's comprehensiveness:

1. **Narrow buyer representation.** Only the Economic Buyer (budget holder) was modeled. In enterprise B2B, a buying committee with multiple roles evaluates the product — Technical Buyer (integration/security), User Buyer (usability/adoption), Coach/Champion (internal advocacy). Deals often stall at non-economic evaluations.

2. **Missing Pains.** The JTBD mapping was incomplete. Business Outcome captured the buyer's strategic job, but user-level pains — the visceral, daily suffering that makes the buying decision *urgent* — were implicit. The distinction between "who endures" (user) and "who cares" (buyer) was not modeled.

3. **Incomplete barrier types.** Only 4 types (Regulatory, Technical, Organizational, Competitive) existed. Financial, Contractual, Data, and Cultural barriers were being misclassified.

4. **Missing Barrier → Promise relationship.** Barriers could undermine Customer Promises, but this tension was invisible.

5. **Customer Value Metric had "Actual" values.** Actual measured values are operational state, not product definition. The Definition Model should capture targets and thresholds only.

6. **TCO gap.** Total Cost of Ownership was identified as a gap but deferred — the right anchoring point needs further discussion.

## Decisions

### 1. Rename Economic Buyer Persona → Buying Persona with role types

The entity now has a `Role Type` field: Economic Buyer, Technical Buyer, User Buyer, Coach/Champion. Each role has different evaluation criteria, key concerns, and Pains they care about. One entity with role types (rather than four separate entities) keeps the model compact.

### 2. Introduce Pain as a Customer Value entity

Pain captures user-level suffering in the current workflow:
- **Endured by** User Persona (User Experience) — who experiences it
- **Cared about by** Buying Persona (Customer Value) — who is motivated to solve it
- **Relieved by** Value Proposition (Customer Value) — how the product addresses it

This completes the JTBD mapping: Business Outcome (buyer's job) + Pain (user's suffering) → Value Proposition (value delivered).

### 3. Expand Adoption Barrier to 8 types + Barrier → Promise relationship

New types: Financial, Contractual, Data, Cultural (added to existing Regulatory, Technical, Organizational, Competitive). New relationship: Barrier "challenges" Customer Promise — exposing gaps between what the product promises and what prevents adoption.

### 4. Refine Customer Value Metric: drop Actual, add SLA Threshold

The Definition Model captures Target (aspirational/promised value) and SLA Threshold (contractual minimum before breach). Actual measured values are operational state tracked at runtime, not part of the product's self-description.

### 5. Park TCO for later

TCO is acknowledged as a gap. The anchoring point (Customer Segment? Customer Promise?) and qualification approach need further discussion.

## Rationale

- **Complete buying committee coverage** enables role-specific messaging, identifies where deals stall, and connects Pains to the people who care about them
- **Pain + Business Outcome** provides both strategic justification (buyer) and visceral urgency (user), matching how enterprise purchases are actually motivated
- **Expanded barrier types** prevent misclassification and capture the full spectrum of adoption impediments
- **Barrier → Promise relationship** exposes contradictions between commitments and reality — a direct input to discovery prioritization
- **Target + SLA Threshold** maintains the Definition/Work Model boundary — "what we promise" vs. "what we measured"

## Consequences

### Positive
- Complete JTBD mapping (Buyer's Job → Business Outcome, User's Pain → Pain, Value delivered → VP, User's Job → User Journey in User Experience)
- Buying committee visibility — Technical Buyer and User Buyer influence is now capturable
- Pain entity connects Customer Value (buying logic) to User Experience through User Persona
- Barrier analysis is richer — 8 types + explicit challenge to Customer Promises
- Clean Definition/Work boundary for metrics

### Negative
- Customer Value now has 7 entities (up from 6) — one more than before, though still well-scoped
- Buying Persona with 4 role types requires more upfront modeling work per segment
- Pain granularity needs governance — too granular becomes a feature list, too abstract loses sales value
- TCO remains unresolved (parked)
