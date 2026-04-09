# Prioritization Task

**Model:** Work Model
**Track:** Track 1: The Discovery Track (Learning)
**Owner:** Product Management

## Definition

Work to evaluate, score, and rank Signals (Problems, Needs, Opportunities) and associate them with active Initiatives for discovery investment. Typically performed during planning cycles (quarterly, per-horizon).

## Purpose

Makes the prioritization and association work explicit. Signals may exist independently before being associated with an Initiative during a planning cycle. This entity represents the deliberate, periodic work of evaluating Signals against active Objectives and Initiatives, determining which warrant discovery investment, and establishing the many-to-many associations between Signals and Initiatives (see FAQ Q11).

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
| Evaluates | Problem (Dim 1) | Prioritization Task evaluates and ranks Problems |
| Evaluates | Need (Dim 1) | Prioritization Task evaluates and ranks Needs |
| Evaluates | Opportunity (Dim 1) | Prioritization Task evaluates and ranks Opportunities |
| Associates to | Initiative (Dim 1) | Prioritization Task associates Signals to Initiatives |
| Informed by | Signal Monitoring (Track 1) | Signal Monitoring may surface need for re-prioritization when backlog or velocity thresholds are breached |

## Example

"Quarterly review: rank and associate top 30 Signals to Q3 Initiatives."
