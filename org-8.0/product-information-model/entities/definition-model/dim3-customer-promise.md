# Customer Promise

**Model:** Definition Model
**Dimension:** Dimension 3: The Customer Value Dimension (Why Buy)
**Owner:** Product Management, Product Marketing (Value Proposition); PM + SRE (Service Commitment); PM + Security/Compliance (Compliance Posture)

## Definition

The product's formal commitment to a Customer Segment. Customer Promise is a classification with three distinct subtypes — Value Proposition, Service Commitment, and Compliance Posture — each representing a different category of commitment to the customer.

## Purpose

Customer Promise unifies the three categories of commitment a product makes to its customers under a single parent concept. This enables a complete view: "What are ALL our promises to this segment?" Each subtype has specialized fields but shares common properties (segment, owner, status, evidencing metrics). The three subtypes are peers, not nested — a Service Commitment is not a type of Value Proposition, and a Compliance Posture is not a type of Service Commitment (see FAQ Q17).

## Subtypes

### Value Proposition

Articulates how the product's capabilities deliver the buyer's outcomes and relieve user pains. Maps Business Outcomes and Pains (Dim 3) to the product's structural delivery mechanism:

- **Outcome-based promises** → map to **Value Streams** (Dim 8) — because outcomes require end-to-end flows across modules.
- **Ability-based promises** → map to **Capabilities** (Dim 8) — because the promise is about a specific product ability.

Value Proposition also captures competitive positioning: Primary Alternative (what the customer uses today) and Key Differentiator (why this product is better).

| Field | Type | Description |
|---|---|---|
| Customer Segment | Reference (Dim 3) | Which segment this proposition targets |
| Business Outcome(s) | List of References (Dim 3) | Which buyer outcomes this addresses |
| Pain(s) Relieved | List of References (Dim 3) | Which user pains this relieves |
| Promise Mapping Type | Enum | `Outcome-based` (maps to Value Stream) or `Ability-based` (maps to Capability) |
| Value Stream(s) | List of References (Dim 8) | For outcome-based: which Value Streams deliver the promise |
| Capability(ies) | List of References (Dim 8) | For ability-based: which Capabilities deliver the promise |
| Primary Alternative | Text | What the customer uses today (competitor, manual process, status quo) |
| Key Differentiator | Text | Why this product over the alternative |
| Positioning Statement | Text | Narrative articulation for sales/marketing use |

*Outcome-based example:* "Reduce cross-border payment cost by 60%" → maps to Value Stream "Cross-Border Payout Processing." Measured by end-to-end flow metrics: cycle time, throughput, cost per transaction.

*Ability-based example:* "Real-time FX rate locking for 24 hours" → maps to Capability "Automated Rate Locking." Measured by point metrics: lock speed (200ms), supported currencies (35+).

### Service Commitment

Guarantees reliability, performance, and support levels to the customer. The customer-facing commitment about how the product's infrastructure (Dim 7) will behave.

| Field | Type | Description |
|---|---|---|
| Customer Segment / Tier | Reference | Which customers this commitment applies to (may vary by pricing tier) |
| Availability SLA | String | Guaranteed uptime (e.g., "99.9%") |
| Performance SLA | String | Latency, throughput guarantees (e.g., "sub-200ms P95") |
| Support SLA | String | Response/resolution time guarantees (e.g., "P1: 15-min response, 4-hour resolution") |
| Data SLA | String | Backup frequency, retention, recovery objectives (RPO/RTO) |
| Remedies | Text | What happens when the SLA is breached (credits, penalties) |

*Example:* "99.9% API uptime, sub-200ms P95 latency, SEV-1 incidents: 15-minute response, 4-hour resolution. Breach remedy: 5% monthly credit per 0.1% downtime."

### Compliance Posture

Certifies that the product meets regulatory, security, or industry standards. Compliance goes beyond operations — it is a core aspect of the product that influences many capabilities across Dim 8.

| Field | Type | Description |
|---|---|---|
| Standard / Certification | String | The regulatory or security standard (PCI-DSS, SOC 2, GDPR, HIPAA, etc.) |
| Level / Type | String | The specific level or type (e.g., PCI-DSS Level 1, SOC 2 Type II) |
| Scope | List of References (Dim 8) | Which modules/capabilities are covered |
| Certification Date | Date | When last certified |
| Renewal Date | Date | When recertification is needed |
| Influences | List of References (Dim 8) | Which Capabilities are shaped by this compliance requirement |

*Example:* "PCI-DSS Level 1 certified. Scope: all payment processing modules. Certified: 2026-01-15, renewal: 2027-01-15. Influences: Payment Execution, Data Storage, API Security capabilities."

## Common Fields (all subtypes)

| Field | Type | Description |
|---|---|---|
| Subtype | Enum | `Value Proposition` / `Service Commitment` / `Compliance Posture` |
| Customer Segment | Reference (Dim 3) | Which segment this promise applies to |
| Owner | Reference | Who is accountable for this promise |
| Status | Enum | Draft / Active / Under Review / Retired |

## Statuses

| Status | Description |
|---|---|
| Draft | Promise is being defined |
| Active | Promise is in effect and communicated to customers |
| Under Review | Promise is being reassessed (e.g., SLA change, new compliance requirement) |
| Retired | Promise is no longer in effect |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Anchored to | Customer Segment (Dim 3) | Customer Promise is made to a Segment |
| Evidenced by | Customer Value Metric (Dim 3) | Customer Value Metrics measure/evidence this promise |
| Maps to (VP) | Value Stream (Dim 8) | Value Proposition (outcome-based) maps to Value Stream(s) |
| Maps to (VP) | Capability (Dim 8) | Value Proposition (ability-based) maps to Capability(ies) |
| Addresses (VP) | Business Outcome (Dim 3) | Value Proposition addresses Business Outcome(s) |
| Relieves (VP) | Pain (Dim 3) | Value Proposition relieves Pain(s) |
| Overlaps (SC) | Operational Dimension (Dim 7) | Service Commitment overlaps with Dim 7 infrastructure |
| Influences (CP) | Capability (Dim 8) | Compliance Posture influences Capabilities |
| Work Model | Modeling Task (Track 1) | Modeling Tasks define/refine Customer Promises |
| Assessed by | Win Review (Track 4) | Win Reviews assess whether Customer Promises are being fulfilled |
| Tested by | Win Case (Track 4) | Win Case complaints test whether Service Commitments are being met |
| Tested by | Incident (Track 3, artifact) | Incidents test whether Service Commitments are being met — every SEV-0/1/2 incident evaluates SLA breach |
| Justified by | PDR (Dim 1) | Significant promise changes are justified by a PDR |

## Example

For Customer Segment "LATAM Enterprise":
- **Value Proposition:** "Reduce cross-border payment cost by 60% through automated rate-locking and payout consolidation" → addresses Business Outcome "Eliminate manual FX hedging and reduce wire fees" + relieves Pain "AP Clerk spends 4 hours/day on manual reconciliation" → maps to Value Stream "Cross-Border Payout Processing."
- **Service Commitment:** "99.9% API uptime, sub-200ms P95 latency, dedicated CSM for accounts >$1M TPV."
- **Compliance Posture:** "PCI-DSS Level 1, SOC 2 Type II, LGPD compliant (Brazil data protection)."
