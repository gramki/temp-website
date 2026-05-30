# DR-008: Introduce Value Stream as a Structural Entity

**Status:** Accepted
**Date:** 2026-02-15

## Context

Structural (Topology) contained only a vertical decomposition: Product → Module → Capability → Feature. This hierarchy describes *what the product can do* — a taxonomy of abilities — but not *how it delivers end-to-end customer value*.

Many customer outcomes require orchestrating activities across multiple modules. For example, "Cross-Border Payout Processing" involves Invoice (instruction), FX (rate-locking), Compliance (screening), Payment (execution), and Settlement (reconciliation). No single module "owns" this outcome.

Without a horizontal composition entity, outcome-based Value Propositions (Customer Value) could only point to a list of Capabilities — losing the orchestration narrative that shows *how* those capabilities collaborate to produce the outcome.

## Decision

Introduce **Value Stream** as a Structural entity representing an end-to-end sequence of activities — crossing multiple modules and capabilities — that delivers a complete unit of value to the customer.

Structural now has two complementary views:
- **Vertical decomposition:** Product → Module → Capability → Feature (what the product *can do*)
- **Horizontal composition:** Value Stream → traverses Modules → engages Capabilities (how the product *delivers value*)

## Rationale

### Why not just list Capabilities in Value Propositions?

A list of Capabilities ("Automated Rate Locking + OFAC Screening + Payment Execution") describes the ingredients but not the recipe. Value Stream captures the *sequence*, *handoff points*, *end-to-end SLA*, and *module orchestration* that produce the outcome. This is critical for:
- **Outcome-based metrics:** End-to-end cycle time, throughput, cost per flow — these are properties of the *stream*, not of individual Capabilities.
- **Reliability analysis:** Handoff points between modules are where failures occur. Value Streams make these explicit.
- **Optimization:** Bottleneck identification requires knowing the flow, not just the components.

### Distinction from related concepts

| Concept | Perspective | Nature | Example |
|---|---|---|---|
| **Capability** | What the product *can do* | Static ability (a point) | "Automated Rate Locking" |
| **Value Stream** | How the product *delivers value* | Dynamic flow (a path) | "Cross-Border Payout Processing" |
| **User Journey** (User Experience) | How the *user experiences* the flow | Human experience (a path) | "AP Clerk processes payout" |

Value Streams and User Journeys often align but are not identical — Value Streams include automated steps invisible to users; User Journeys include cognitive/emotional steps invisible to the system.

### Impact on Customer Value Metrics

Value Stream-mapped Value Propositions produce **end-to-end flow metrics** (cycle time, throughput, cost per transaction). Capability-mapped Value Propositions produce **point metrics** (feature performance, coverage, availability). This distinction must be reflected in the ROI Metric subtype of Customer Value Metric.

## Consequences

### Positive
- Outcome-based Value Propositions now map precisely to end-to-end flows
- Cross-module orchestration is visible and documentable
- Handoff points (failure/bottleneck risks) are explicit
- End-to-end SLAs can be defined per Value Stream
- Modeling Tasks can explicitly target Value Stream mapping work

### Negative
- One more entity type in Structural (five total: Product, Value Stream, Module, Capability, Feature)
- Value Stream boundaries may overlap or be subjective — need governance for scoping
- Requires understanding of cross-module flows, which may not be immediately known for all parts of the product
