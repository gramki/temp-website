# DR-039: Discovery Case and Build Orchestration

**Status:** Accepted
**Date:** 2026-05-25

## Context

DR-037 clarified Product Intent as the bridge from product decision to downstream product evolution work. Subsequent modeling exposed two remaining gaps:

1. Discovery work was still implicitly treated as Signal-led and Product Manager-only.
2. Build work was still easy to read as customer-delivery-only, even though Discovery may need Build evidence through experiments, PoCs, spikes, and technical validation.

In practice, Discovery can originate from any function and may start without an external Signal. Architecture concerns, technical ideas, operational insights, QA concerns, release learnings, customer commitments, executive direction, and Product Manager judgment can all require discovery before a product decision is made.

## Decision

1. Introduce **Discovery Case** as the primary Discovery Track orchestration item.
   - Discovery Case is a Work Model entity, not a Definition Model entity.
   - It is signal-optional: Signals may be inputs, outputs, or absent.
   - It coordinates cross-functional Discovery sub-work until a decision or routing outcome is reached.

2. Discovery Case may be created by any authorized function.
   - Product Management, UX, Engineering, Architecture, QA, Run, Win, Governance, executives, and authorized agents may originate cases.
   - Product Management alignment is still required for PDRs that change product direction.

3. Add **Discovery Support** as a Product Intent purpose.
   - Discovery Support Product Intent requests bounded Build Track work to produce evidence for an open Discovery Case.
   - It does not commit product direction and cannot by itself imply customer delivery.
   - A later Go/Pivot PDR creates a separate Evolution/Delivery Product Intent if the product should change.

4. Build Track has one primary orchestration item: **Product Intent**.
   - Product Intent may be delivery-oriented or discovery-supporting.
   - Build can produce customer deliverables, internal/enabling capabilities, technical validation, PoC/spike outputs, or operational enablement.

5. Architectural refactoring does not get a separate top-level Build orchestration item.
   - It must fit under an existing Product Intent,
   - become Product Intent through a Discovery Case,
   - route to Run or Evolve if operational/process-oriented,
   - or remain local engineering hygiene if small and internal.

## Rationale

Discovery Case provides the same envelope pattern for Discovery that FIR provides for reactive Win intake: it groups sub-work, preserves origin and participation, and makes routing outcomes visible. It also prevents forcing every investigation into the Signal lifecycle when the origin is PM judgment, architecture, operations, compliance, or executive direction.

Discovery Support Product Intent preserves the rule that Build is orchestrated by Product Intent while recognizing that not every Build request is a customer-committed deliverable.

## Consequences

- Add `track1-discovery-case.md`.
- Add Discovery Case to Discovery Track and Work Execution Framework docs.
- Add Product Intent purpose classifications.
- Add PM alignment fields to PDR.
- Update modeling FAQs and narrative seeds.
- Update ACE practitioner guidance and Orchestrator docs so orchestration items are track-scoped and Work Orders are workspace-scoped.
