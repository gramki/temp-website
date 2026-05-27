# DR-038: Customer Release Intent and PI Console Formation Views

**Status:** Accepted
**Date:** 2026-05-25

## Context

PI Console requirements expanded from listing Product Intents to visualizing how Product Intent forms from multiple sources: strategy, Signals, product decisions, customer commitments, and Release learnings.

Two terminology and UX risks emerged:

1. **Customer Release ambiguity.** In Strategy, "Customer Release" meant the intended customer-facing delivery outcome. In Release execution, it can also mean the realized release event/package. The same phrase was doing both jobs.
2. **Generic graph exploration.** A "Graph View" could look like arbitrary relationship browsing rather than a purposeful view answering stakeholder questions.

The Strategy layer also needed a clearer boundary: it should contain decision-grade direction and commitments, not raw requests, tasks, incidents, or implementation detail.

## Decision

1. Rename the Strategy-layer concept to **Customer Release Intent**.
   - Customer Release Intent = planned customer-facing delivery outcome.
   - Customer Release = realized release event/package that fulfills the intent.

2. Define **Strategy** as decision-grade direction and constraints:
   - Portfolio context
   - Strategic Themes
   - Objectives / KRAs / measurable goals
   - SLAs and customer commitments that shape product evolution
   - Initiatives
   - Customer Release Intents
   - Strategic constraints such as regulatory, contractual, partner, market, and customer-committed dates
   - PDRs and Product Intents

3. Explicitly exclude non-strategy items from Strategy:
   - raw customer requests
   - untriaged Signals
   - individual bugs
   - Jira stories
   - engineering tasks
   - UX tasks
   - implementation designs
   - PSD body content
   - deployment records
   - incident logs
   - unprocessed stakeholder opinions

4. Define PI Console as the **Product Intent Formation Console**.

5. Replace generic Graph View with stakeholder-specific **Traceability Maps**:
   - Executive Strategy Map
   - Product Manager Intent Map
   - Delivery Execution Map
   - Governance Evidence Map
   - Customer Value Map
   - Vendor Value Map
   - Release Renewal Map

## Rationale

Customer Release Intent makes clear that the Strategy layer holds intent, not execution records. It also aligns with Product Intent: both are strategy/intent constructs that guide downstream work, while Release/Win execution realizes them.

Traceability Maps make graph visualization purposeful. The PI Console should not ask users to browse arbitrary relationships; it should ask which stakeholder question they need to answer and show the appropriate traceability map.

## Consequences

- PI Console must include explicit views for Funnel, Strategy Frame, Signals, Decisions, Product Intents, Traceability Maps, and Bottlenecks.
- Strategy Frame must show what belongs in strategy and what must not go into strategy.
- Customer-committed deadlines belong in Strategy when they constrain product evolution; they should attach to the appropriate Objective, KRA/SLA, Initiative, Customer Release Intent, Customer Promise, or Product Intent.
- Existing references to Strategy-layer Customer Release should be interpreted as Customer Release Intent unless explicitly discussing realized release execution.
