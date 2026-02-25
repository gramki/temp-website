# Maintenance Task

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

Routine preventative work — scheduled, recurring operational tasks that maintain system health, security, and compliance.

## Purpose

Captures planned, recurring operational hygiene. Unlike Change Requests (which are one-off planned changes), Maintenance Tasks are routine and preventative.

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
| Maintains | Deployment Environment (Dim 7) | Maintenance Task keeps a Deployment Environment healthy |
| May be created by | Deployment Planning Task (Track 3) | Deployment Planning may discover maintenance prerequisites |
| May be created by | Deployment Plan (Track 3) | Deployment Plan deliberation may identify maintenance needs |

## Example

"Rotate bank API vault secrets."
