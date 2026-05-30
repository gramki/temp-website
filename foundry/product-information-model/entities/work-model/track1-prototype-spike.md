# Prototype / Spike

**Model:** Work Model
**Track:** Discovery
**Owner:** Product Manager, UX Researcher, Developers

## Definition

A throwaway or low-fidelity artifact built to test a specific assumption around desirability or feasibility. Distinct from an Experiment (which has formal pass/fail criteria) — a Prototype/Spike explores through building rather than measuring.

## Purpose

Enables learning-by-doing within the Discovery Track. Prototypes test desirability (UX mockups, clickable wireframes). Spikes test feasibility (technical proof-of-concepts, integration tests). Both are intentionally disposable — their value is the knowledge they produce, not the artifact itself. They are referenced by Product Decision Records (Dimension 1) as evidence.

## Fields

| Field | Type | Description |
|---|---|---|
| Originating Discovery Case | Reference (Discovery) | Discovery Case this prototype/spike belongs to, if any |
| _To be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| _To be refined._ | |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Originates from | Discovery Case (Discovery) | Sub-item of a Discovery Case; carries bidirectional reference |
| Tests | Idea (Strategy) | Prototype/Spike tests an Idea's feasibility or desirability |
| Referenced by | Product Decision Record (Strategy) | PDR cites this Prototype/Spike as evidence |
| May be requested by | Product Intent (Strategy) | Discovery Support or Technical Validation Product Intent may request bounded Build evidence work |

## Examples

- "Figma mockup of the FX rate-lock confirmation flow." (validates Journey design — User Experience)
- "Technical spike: can we get sub-200ms FX quotes from provider X?"
- "Clickable prototype of mobile approval journey — tests Job 'Approve payout' in Mobile + Self-serve channel" (validates Journey + Channel combination — User Experience)
- "SDK ergonomics spike: build sample Python integration for Create Payment and payment.settled webhook — validate developer experience before committing to hand-crafted SDK" (validates Ecosystem SDK design choices)
