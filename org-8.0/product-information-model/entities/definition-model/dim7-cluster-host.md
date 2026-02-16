# Cluster / Host

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** DevOps, SRE

## Definition

The orchestration group running the software — a Kubernetes cluster, VM pool, or server group within an Environment.

## Purpose

Provides the compute infrastructure layer. Clusters run Containers that execute Subsystems (Dimension 5).

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
| Upstream | Environment (Dim 7) | Cluster belongs to an Environment |
| Contains | Container / Process (Dim 7) | Cluster runs Containers |

## Example

Dedicated Kubernetes Cluster (EKS).
