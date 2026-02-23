# ~~Subsystem / Service~~ (DEPRECATED)

> **DEPRECATED** — Subsumed by **System** (`dim5-system.md`), which adds technology stack fields, many-to-many Module mapping, Deployment Environment reference, and full relationship set. See DR-024.

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Developers

## Definition

A standalone, deployable unit of backend logic. Aligned with the C4 model's "Container" level.

## Purpose

Establishes the top-level technical building blocks of the system. Subsystems contain Classes/Components and are executed as Containers (Dimension 7).

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
| Contains | Class / Component (Dim 5) | Subsystem contains Classes/Components |
| Runtime | Container / Process (Dim 7) | Subsystem is executed as a Container |

## Example

The FX (Foreign Exchange) Microservice.
