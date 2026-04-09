# ~~Function / Method~~ (DEPRECATED)

> **DEPRECATED** — Below the Definition Model waterline. Executable code blocks are PSD/Build Track artifacts. Same deprecation pattern as Touchpoint (Dim 4), Payload Schema (Dim 6), Container/Process (Dim 7). See DR-024.

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Developers

## Definition

The executable block of code — the most granular unit of technical behavior.

## Purpose

Represents the atomic unit of logic. Functions are triggered by Endpoints (Dimension 6) and compose the internal behavior of Classes.

## Fields

| Field | Type | Description |
|---|---|---|
| _To be refined._ | | |

## Statuses

_Not applicable — structural descriptor._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Class / Component (Dim 5) | Function belongs to a Class |
| Triggered by | Endpoint / Event Topic (Dim 6) | Endpoint triggers Function |

## Example

`calculateConversion(baseCurrency, targetCurrency, amount)`.
