# DR-007: Restructure Dimension 3 as the Customer Value Dimension

**Status:** Accepted
**Date:** 2026-02-15

## Context

Dimension 3 originally contained only three entities — Economic Buyer Persona, Business Outcome, and ROI Metric — modeling a narrow "Customer ROI" perspective. This was insufficient because:

1. **Incomplete promise representation.** The product's promise to customers extends beyond financial ROI. Customers also evaluate reliability guarantees (SLA), compliance certifications (PCI-DSS, SOC 2), and security posture. These are distinct commitments with different audiences, metrics, and lifecycles.

2. **No customer segmentation.** Buyer personas were unanchored — "CFO" is too generic. Different customer segments (LATAM Enterprise vs. US Mid-Market) have different buyers, outcomes, promises, and adoption barriers.

3. **No adoption barriers.** Understanding why customers *don't* buy is as important as understanding why they *do*. Barriers (regulatory, technical, competitive) inform discovery prioritization but had no home in the model.

4. **Metric conflation.** A single "ROI Metric" entity tried to cover financial return, service level performance, and compliance adherence — fundamentally different measurement types.

## Decision

Restructure Dimension 3 as "The Customer Value Dimension (Why Buy)" with six entities organized around the complete buying decision:

1. **Customer Segment** — the organizing entity anchoring all other Dim 3 entities.
2. **Economic Buyer Persona** — the budget-holder within a segment.
3. **Business Outcome** — the buyer's strategic "job to be done."
4. **Customer Promise** — the product's commitment to a segment, with three subtypes:
   - **Value Proposition** — maps outcomes to Value Streams (outcome-based) or Capabilities (ability-based).
   - **Service Commitment** — reliability/performance/support guarantees.
   - **Compliance Posture** — regulatory/security certifications and standards.
5. **Customer Value Metric** — unified metric entity with three subtypes: ROI Metric, Service Level Metric, Compliance Metric.
6. **Adoption Barrier** — impediments to purchase/adoption within a segment.

The three Customer Promise subtypes are **peers, not nested**. Service Commitment and Compliance Posture are NOT types of Value Proposition — they are separate categories of commitment with different audiences, mapping targets, metric types, and lifecycle cadences (see FAQ Q17).

## Rationale

- **Complete buying decision coverage:** The restructured dimension answers "Who buys?" (Segment, Buyer), "What do they achieve?" (Outcome), "What do we promise?" (Promise — three types), "How do we prove it?" (Metric — three types), and "What stops them?" (Barrier).
- **Segment-anchored:** All entities are contextual to specific customer segments, enabling segment-specific positioning, pricing, and roadmap prioritization.
- **Metric precision:** Different promise types require fundamentally different metrics. ROI Metrics measure financial/time return (end-to-end flow metrics vs. point metrics, depending on Value Proposition mapping type). Service Level Metrics measure operational performance. Compliance Metrics measure adherence to standards.
- **Separation of concerns between promise types:** Value Propositions map to structural entities (Dim 8). Service Commitments map to operational entities (Dim 7). Compliance Posture influences both structure and operations. Mixing them in a single entity would obscure these distinct relationships.
- **Absorption of ROI Metric:** The previous standalone ROI Metric entity is absorbed as a subtype of the unified Customer Value Metric, which also covers Service Level and Compliance measurement.

## Consequences

### Positive
- Complete "Why Buy" / "Why NOT Buy" narrative for each segment
- Segment-specific customer promises with distinct, measurable metrics
- Adoption Barriers surface as Signals (Dim 1) for discovery prioritization
- Clean separation between value promise, reliability promise, and compliance promise
- Modeling Tasks (Track 1) can now target specific Dim 3 entities

### Negative
- Six entities in Dim 3 (up from three) — increased model surface
- Customer Promise subtype structure may require explanation for stakeholders unfamiliar with the distinction
- Overlap between Dim 3 (customer-facing commitment) and Dim 7 (operational implementation) for Service Commitments must be managed explicitly
