# Prototype / Spike

**Model:** Work Model
**Track:** Track 1: The Discovery Track (Learning)
**Owner:** Product Manager, UX Researcher, Developers

## Definition

A throwaway or low-fidelity artifact built to test a specific assumption around desirability or feasibility. Distinct from an Experiment (which has formal pass/fail criteria) — a Prototype/Spike explores through building rather than measuring.

## Purpose

Enables learning-by-doing within the Discovery Track. Prototypes test desirability (UX mockups, clickable wireframes). Spikes test feasibility (technical proof-of-concepts, integration tests). Both are intentionally disposable — their value is the knowledge they produce, not the artifact itself. They are referenced by Product Decision Records (Dimension 1) as evidence.

## Fields

| Field | Type | Description |
|---|---|---|
| Originating Discovery Case | Reference (Track 1) | Discovery Case this prototype/spike belongs to, if any |
| _To be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| _To be refined._ | |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Originates from | Discovery Case (Track 1) | Sub-item of a Discovery Case; carries bidirectional reference |
| Tests | Idea (Dim 1) | Prototype/Spike tests an Idea's feasibility or desirability |
| Referenced by | Product Decision Record (Dim 1) | PDR cites this Prototype/Spike as evidence |
| May be requested by | Product Intent (Dim 1) | Discovery Support or Technical Validation Product Intent may request bounded Build evidence work |

## Examples

- "Figma mockup of the FX rate-lock confirmation flow." (validates Journey design — Dim 4)
- "Technical spike: can we get sub-200ms FX quotes from provider X?"
- "Clickable prototype of mobile approval journey — tests Job 'Approve payout' in Mobile + Self-serve channel" (validates Journey + Channel combination — Dim 4)
- "SDK ergonomics spike: build sample Python integration for Create Payment and payment.settled webhook — validate developer experience before committing to hand-crafted SDK" (validates Dim 6 SDK design choices)
