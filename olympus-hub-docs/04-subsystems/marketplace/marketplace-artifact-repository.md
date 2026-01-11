# Marketplace Artifact Repository

> **Status:** 🟡 WIP — Design Complete

This document describes the storage architecture for Marketplace artifacts, including container cloning, hash-based deduplication, and signing mechanisms.

---

## Overview

The Marketplace Artifact Repository is a **platform-level storage system** that holds all published packages, separate from tenant subscription repositories.

| Attribute | Value |
|-----------|-------|
| **Scope** | Platform-level (shared infrastructure) |
| **Storage Types** | OCI containers, package-manifest-containers |
| **Deduplication** | Hash-based (SHA-256) |
| **Signing** | Publisher signature + Marketplace signature |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MARKETPLACE ARTIFACT REPOSITORY                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                     CONTAINER REGISTRY                               │   │
│   │                                                                      │   │
│   │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐         │   │
│   │  │  Container A   │  │  Container B   │  │  Container C   │         │   │
│   │  │  sha256:abc... │  │  sha256:def... │  │  sha256:ghi... │         │   │
│   │  │  (signed)      │  │  (signed)      │  │  (signed)      │         │   │
│   │  └────────────────┘  └────────────────┘  └────────────────┘         │   │
│   │                                                                      │   │
│   │  Deduplication: Containers stored once, referenced by hash          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                 PACKAGE-MANIFEST-CONTAINERS                          │   │
│   │                                                                      │   │
│   │  ┌────────────────────┐  ┌────────────────────┐                     │   │
│   │  │  Package A v1.0.0  │  │  Package A v1.1.0  │                     │   │
│   │  │  ┌──────────────┐  │  │  ┌──────────────┐  │                     │   │
│   │  │  │ manifest.yaml│  │  │  │ manifest.yaml│  │                     │   │
│   │  │  │ blueprints/  │  │  │  │ blueprints/  │  │                     │   │
│   │  │  │ metadata/    │  │  │  │ metadata/    │  │                     │   │
│   │  │  └──────────────┘  │  │  └──────────────┘  │                     │   │
│   │  └────────────────────┘  └────────────────────┘                     │   │
│   │                                                                      │   │
│   │  One container per package version                                   │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Storage Model

### Container Storage

| Aspect | Description |
|--------|-------------|
| **Format** | OCI container images |
| **Identification** | SHA-256 hash |
| **Deduplication** | Containers with same hash stored once |
| **Signing** | Publisher + Marketplace signatures |
| **Immutability** | Containers cannot be modified after publication |

### Package-Manifest-Container Storage

| Aspect | Description |
|--------|-------------|
| **Format** | OCI container |
| **Contents** | All CRDs + package manifest |
| **Identification** | Package ID + version |
| **One per version** | Each package version has its own container |

---

## Hash-Based Deduplication

Containers are deduplicated using SHA-256 hashes:

```
Publishing Package A:
  Container image-x (sha256:abc123) → Stored
  Container image-y (sha256:def456) → Stored

Publishing Package B:
  Container image-x (sha256:abc123) → Already exists, reference only
  Container image-z (sha256:ghi789) → Stored
```

### Benefits

- Reduced storage for shared base images
- Faster publishing for unchanged containers
- Efficient bandwidth usage

### Hash Verification

- Hash computed during publishing
- Hash stored in package manifest
- Hash verified during subscription/deployment

---

## Container Signing

All containers in the Marketplace are signed twice:

### Signing Flow

```
1. PUBLISHER SIGNS
   └── Publisher signs containers with their certificate
   └── Certificate submitted during publisher registration
   └── Signature embedded in container

2. MARKETPLACE VALIDATES
   └── Signature verified against publisher certificate
   └── Container integrity checked
   └── Malware/vulnerability scanning

3. MARKETPLACE RE-SIGNS
   └── Marketplace signs with its private key
   └── Enables subscriber verification
   └── Establishes chain of trust

4. SUBSCRIBER VERIFIES
   └── Subscriber verifies Marketplace signature
   └── Uses Marketplace public key
   └── Confirms integrity and authenticity
```

### Signature Chain

```
Publisher Certificate → Publisher Signature → Marketplace Validation
                                                      ↓
                                            Marketplace Signature
                                                      ↓
                                            Subscriber Verification
```

---

## Lazy Container Cloning

Containers are **not** cloned to tenant repositories at subscription time. Instead, they are cloned **lazily** on first deployment.

### Cloning Trigger

| Event | Action |
|-------|--------|
| Package Subscription | BlueprintSpecs added; containers remain in Marketplace |
| Scenario Deployment | Container cloned to tenant repository on first reference |
| Subsequent Deployments | Container already in tenant repository |

### Cloning Process

```
1. Scenario Deployment references container
2. Check tenant artifact registry
   └── If exists: Use existing container
   └── If not: Clone from Marketplace
3. Verify Marketplace signature
4. Store in tenant artifact registry
5. Deployment proceeds
```

### Benefits

- Minimal subscription overhead
- Storage optimized (only used containers cloned)
- Tenant isolation maintained

---

## Deep Clone Model

Publishing performs a **deep clone** of all resources to the Marketplace:

### What Gets Cloned

| Resource Type | Clone Behavior |
|---------------|----------------|
| **Container images** | Cloned individually; deduplicated by hash |
| **CRDs (specifications)** | Bundled into package-manifest-container |
| **Associated children** | Automatically included with parent |
| **Multi-media content** | Referenced from workbench git repository |

### Source Independence

- Cloned resources are **independent** of source
- Source can be modified/deleted without affecting Marketplace package
- Packages are self-contained snapshots
- No live links to source artifacts

---

## Relationship with Tenant Artifact Registry

| Registry | Purpose | Contents |
|----------|---------|----------|
| **Marketplace Artifact Repository** | Platform storage for published packages | All packages, all versions |
| **Tenant Artifact Registry** | Tenant-specific runtime artifacts | Deployed containers, promoted artifacts |

### Container Flow

```
Source Tenant Registry
        │
        │ Publish (deep clone)
        ▼
Marketplace Artifact Repository
        │
        │ Subscribe + Deploy (lazy clone)
        ▼
Subscriber Tenant Registry
```

---

## Security Considerations

| Aspect | Mechanism |
|--------|-----------|
| **Integrity** | SHA-256 hashes for all containers |
| **Authenticity** | Publisher + Marketplace signatures |
| **Scanning** | Malware and vulnerability scanning before acceptance |
| **Quarantine** | Artifacts held until security clearance |
| **Continuous Monitoring** | Periodic rescanning for new vulnerabilities |

---

## Related Documentation

- [Blueprints and Packages](./blueprints-and-packages.md) — Package model
- [Publishing Services](./publishing-services.md) — Publishing workflow
- [Security and Compliance](./security-and-compliance.md) — Security details
- [Artifact Registry](../artifact-registry/README.md) — Tenant artifact storage
- [ADR-0096: Lazy Container Cloning](../../decision-logs/0096-lazy-container-cloning.md)

