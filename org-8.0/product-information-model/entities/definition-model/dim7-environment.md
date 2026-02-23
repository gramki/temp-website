# ~~Environment~~ (DEPRECATED)

> **DEPRECATED** — Superseded by **Deployment Environment** (`dim7-deployment-environment.md`), which adds vendor purpose, tenancy architecture, compliance zone, scale policy, and full relationship set. See DR-023.

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** DevOps, SRE

## Definition

An isolated deployment ecosystem — a distinct runtime context (e.g., dev, staging, production) where the product operates.

## Purpose

Establishes the top-level operational boundary. Environments contain Clusters/Hosts that run Containers.

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
| Contains | Cluster / Host (Dim 7) | Environment contains Clusters |

## Example

Production (PCI-DSS Compliant Zone).
