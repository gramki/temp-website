# ~~Container / Process~~ (DEPRECATED)

> **DEPRECATED** — Below the Definition Model waterline. Runtime instances (Docker containers, processes, serverless functions) belong in PSD/Run Track artifacts. Same deprecation pattern as Touchpoint (User Experience) and Payload Schema (Ecosystem). See DR-023.

**Model:** Definition Model
**Dimension:** Operational
**Owner:** DevOps, SRE

## Definition

The isolated runtime instance executing a Subsystem (Dimension 5) — a Docker container, process, or serverless function.

## Purpose

Connects the operational dimension to the technical dimension by defining the runtime manifestation of a Subsystem.

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
| Upstream | Cluster / Host (Operational) | Container runs within a Cluster |
| Executes | Subsystem / Service (Technical) | Container executes a Subsystem |

## Example

FX Microservice Docker Container.
