# Specification Task

**Model:** Work Model
**Track:** Discovery
**Owner:** Product Manager

## Definition

A granular PSD-authoring action — scoping modules, writing acceptance criteria, coordinating feasibility with engineering, decomposing into shippable increments. Represents the substantial work of refining an accepted Product Intent into one or more completed PSDs.

## Purpose

Makes the PSD-authoring work explicit in the Work Model. A Go or Pivot PDR may create Product Intent, but that intent is not yet a buildable module contract. Refinement requires significant effort: defining scope boundaries per module, writing detailed acceptance criteria, coordinating with engineering on feasibility, and identifying cross-module dependencies. Specification Tasks track this work (see FAQ Q5). They consume Product Intent; they do not originate it.

## Fields

| Field | Type | Description |
|---|---|---|
| Originating Discovery Case | Reference (Discovery) | Discovery Case this specification work belongs to, if any |
| _To be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| _To be refined._ | |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Originates from | Discovery Case (Discovery) | Sub-item of a Discovery Case when specification work is case-scoped |
| Refines | Product Intent (Strategy) | Specification Tasks refine an accepted Product Intent |
| Produces | PSD (Strategy) | Specification Tasks produce PSDs under a Product Intent |
| Justified by | Product Decision Record (Strategy) | Work is authorized by a Go or Pivot decision in a PDR |

## Example

"Define webhook payload contract with Platform team." "Write acceptance criteria for FX module." "Author PSD for Cross-Border Payments API Module — define API Operations, SLO targets, and Compatibility Contract for v2 launch."
