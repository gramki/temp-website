# ~~Cluster / Host~~ (DEPRECATED)

> **DEPRECATED** — Below the Definition Model waterline. Specific compute infrastructure (Kubernetes clusters, VM hosts) belongs in PSD/Run Track artifacts. Same deprecation pattern as Touchpoint (User Experience) and Payload Schema (Ecosystem). See DR-023.

**Model:** Definition Model
**Dimension:** Operational
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
| Upstream | Environment (Operational) | Cluster belongs to an Environment |
| Contains | Container / Process (Operational) | Cluster runs Containers |

## Example

Dedicated Kubernetes Cluster (EKS).
