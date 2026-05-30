# State

**Model:** Definition Model
**Dimension:** Data
**Owner:** Business Analysts, Developers

## Definition

The allowed lifecycle statuses of a Data Entity — the finite set of states an entity can occupy and the valid transitions between them.

## Purpose

Defines the behavioral lifecycle of data. States govern what operations are valid at any point in an entity's existence.

## Fields

| Field | Type | Description |
|---|---|---|
| _To be refined._ | | |

## Statuses

_Not applicable — State itself defines statuses for Data Entities, not for itself._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Governs | Data Entity (Data) | State defines the lifecycle of a Data Entity |

## Example

`Initiated` → `Processing` → `Cleared` → `Settled`.
