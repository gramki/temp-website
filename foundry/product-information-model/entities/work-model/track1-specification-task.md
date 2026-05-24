# Specification Task

**Model:** Work Model
**Track:** Track 1: The Discovery Track (Learning)
**Owner:** Product Manager

## Definition

A granular PSD-authoring action — scoping modules, writing acceptance criteria, coordinating feasibility with engineering, decomposing into shippable increments. Represents the substantial work of refining an accepted Product Intent into one or more completed PSDs.

## Purpose

Makes the PSD-authoring work explicit in the Work Model. A Go or Pivot PDR may create Product Intent, but that intent is not yet a buildable module contract. Refinement requires significant effort: defining scope boundaries per module, writing detailed acceptance criteria, coordinating with engineering on feasibility, and identifying cross-module dependencies. Specification Tasks track this work (see FAQ Q5). They consume Product Intent; they do not originate it.

## Fields

| Field | Type | Description |
|---|---|---|
| _To be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| _To be refined._ | |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Refines | Product Intent (Dim 1) | Specification Tasks refine an accepted Product Intent |
| Produces | PSD (Dim 1) | Specification Tasks produce PSDs under a Product Intent |
| Justified by | Product Decision Record (Dim 1) | Work is authorized by a Go or Pivot decision in a PDR |

## Example

"Define webhook payload contract with Platform team." "Write acceptance criteria for FX module." "Author PSD for Cross-Border Payments API Module — define API Operations, SLO targets, and Compatibility Contract for v2 launch."
