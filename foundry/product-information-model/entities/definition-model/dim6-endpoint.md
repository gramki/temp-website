# Endpoint / Event Topic

**Model:** Definition Model
**Dimension:** Dimension 6: The Ecosystem & Extensibility Dimension (Platform)
**Owner:** Tech Leads, Developers

## Definition

The programmatic address or trigger — an API endpoint, webhook event, or message topic that external systems use to interact with the product.

## Purpose

Defines the specific integration points. Endpoints trigger Functions (Dimension 5) and exchange data via Payload Schemas.

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
| Upstream | Interface Type (Dim 6) | Endpoint belongs to an Interface Type |
| Triggers | Function / Method (Dim 5) | Endpoint triggers Functions |
| Defines | Payload Schema (Dim 6) | Endpoint sends/receives a Payload Schema |

## Example

`POST /v1/payments/cross-border` and `payment.cleared` webhook.
