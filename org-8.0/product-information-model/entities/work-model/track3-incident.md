# Incident

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

Unplanned service degradation — an event where the production system is performing below expected SLAs or is unavailable.

## Purpose

Captures urgent, unplanned operational work. Incidents require immediate response and resolution to restore service. Post-incident reviews may feed back into the Build Track (as Bugs or Technical Tasks) or the Discovery Track (as new Problems).

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
| May produce | Bug (Track 2) | Incident investigation may reveal a Bug |
| May produce | Problem (Dim 1) | Recurring incidents may surface a new Problem |

## Example

"FX API latency spiked to 5000ms."
