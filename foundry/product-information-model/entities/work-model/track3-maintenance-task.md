# Maintenance Task

**Model:** Work Model
**Track:** Run
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
| Maintains | Deployment Environment (Operational) | Maintenance Task keeps a Deployment Environment healthy |
| May be created by | Deployment Planning Task (Run) | Deployment Planning may discover maintenance prerequisites |
| May be created by | Deployment Plan (Run) | Deployment Plan deliberation may identify maintenance needs |

## Example

"Rotate bank API vault secrets."
