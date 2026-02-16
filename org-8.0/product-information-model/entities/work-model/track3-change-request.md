# Change Request

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

A scheduled production alteration — a planned change to infrastructure, configuration, or deployment that requires formal approval and execution.

## Purpose

Captures planned operational changes that carry risk and need controlled execution. Change Requests ensure production stability through formal change management.

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
| Modifies | Environment (Dim 7) | Change Request modifies an operational Environment |
| Modifies | Cluster / Host (Dim 7) | Change Request may modify infrastructure |

## Example

"Migrate Payment DB to larger instance."
