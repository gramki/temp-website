# Portfolio

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Executive Leadership

## Definition

A thin, local reference entity representing the product portfolio that this UPIM instance belongs to. The Portfolio is NOT owned or managed by the UPIM — it is a reference anchor that enables portfolio-scoped Strategic Themes to be traced to their organizational source.

> **Boundary Note:** The UPIM is a *product*-level model. Portfolio management, portfolio strategy, and cross-product coordination live outside the UPIM's scope. This entity exists solely so that portfolio-scoped Strategic Themes have a traceable origin, and so the product's place within the portfolio is documented.

## Purpose

Without a Portfolio reference, portfolio-scoped Strategic Themes would be orphaned — the product would know the Theme exists but not where it came from. The thin Portfolio entity provides just enough context to answer: "Which portfolio does this product belong to?" and "Where do our portfolio-scoped Themes originate?"

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Portfolio name (e.g., "Payments Platform Portfolio") |
| Owner | String | Who manages this portfolio (e.g., "VP Product, Payments") |
| External Reference | String | Link/ID to the portfolio's canonical source (external system, strategy doc) |
| _Intentionally minimal. Portfolio details are managed outside the UPIM._ | | |

## Statuses

_Not applicable — reference entity._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Contains | Product (Dim 8) | This Portfolio contains this Product (and potentially others, outside this UPIM's scope) |
| Downstream | Strategic Theme (Dim 1) | Portfolio-scoped Themes originate from Portfolio strategy |

## Example

"Payments Platform Portfolio" — owned by VP Product, Payments. Contains: Core Payment Gateway, Merchant Portal, Settlement Platform.
