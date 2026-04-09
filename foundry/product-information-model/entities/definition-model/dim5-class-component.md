# ~~Class / Component~~ (DEPRECATED)

> **DEPRECATED** — Below the Definition Model waterline. Code-level structure (classes, modules, packages) belongs in PSD/Build Track artifacts. Same deprecation pattern as Touchpoint (Dim 4), Payload Schema (Dim 6), Cluster/Host (Dim 7). See DR-024.

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Developers

## Definition

The structural code definition — a class, module, or component within a Subsystem.

## Purpose

Provides the mid-level code organization within a Subsystem. Classes contain Functions/Methods.

## Fields

| Field | Type | Description |
|---|---|---|
| _To be refined._ | | |

## Statuses

_Not applicable — structural descriptor._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Subsystem / Service (Dim 5) | Class belongs to a Subsystem |
| Contains | Function / Method (Dim 5) | Class contains Functions |

## Example

`ExchangeRateCalculator`.
