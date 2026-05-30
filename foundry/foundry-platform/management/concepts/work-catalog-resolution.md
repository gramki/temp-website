# Work Catalog Resolution

Work Catalog Resolution is the algorithm that computes the effective Work Catalog by walking the hierarchy from Platform defaults down to User customizations — with the closest definition winning at each level.

## What it is

The Work Catalog hierarchy enables customization at multiple levels while providing sensible defaults:

```
Platform                    ← Platform defaults (shipped with Foundry)
    └── Foundry             ← Foundry-level overrides/additions
        └── Workshop        ← Workshop-level overrides/additions
            └── Workbench   ← Workbench-level overrides/additions
                └── User    ← User-level customizations (requires activation)
```

**Resolution rule:** Closest definition wins. A Scenario defined at User level shadows the same-named Scenario at Workbench level, which shadows Workshop level, and so on.

The resolution algorithm:

```python
def resolve_artifact(name, context):
    # Check User catalog (if active)
    if context.user_catalog_active:
        if found in user_catalog: return with source "user"
    
    # Check Workbench catalog
    if found in workbench_catalog: return with source "workbench"
    
    # Check Workshop catalog
    if found in workshop_catalog: return with source "workshop"
    
    # Check Foundry catalog
    if found in foundry_catalog: return with source "foundry"
    
    # Check Platform defaults
    if found in platform_defaults: return with source "platform"
    
    return None
```

**User catalog activation** is a key safeguard. User-level customizations are not included in resolution by default — they require explicit activation via session flag or user profile setting. This prevents accidental production impact from experimental Scenarios.

**Merge vs Override semantics:**

- OI Workflows: Same-named workflows completely replace parent-level workflows
- Scenarios: Same-named scenarios completely replace parent-level scenarios
- Catalog: The collection of available artifacts is merged; only same-named conflicts are resolved by override

Every artifact in the effective catalog includes source tracking:

```json
{
  "name": "implement-feature",
  "source": {
    "level": "workbench",
    "id": "checkout",
    "repository": "acme/checkout-workshop-definition",
    "path": "workbenches/checkout/work-catalog/build/.../implement-feature.yaml"
  }
}
```

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Resolution Engine** (WCM) | Computes effective catalog for any scope |
| **Cache** (Redis) | Stores computed effective catalogs |
| **Metadata Service** | Source of synced catalog content per level |
| **Orchestrator** | Queries effective OI Workflows |
| **WO Runtime** | Queries effective Scenarios |

Resolution API:

```
GET /api/v1/work-catalog/effective
  ?foundry_id=...&workshop_id=...&workbench_id=...&user_id=...

GET /api/v1/work-catalog/resolve
  ?type=scenario&name=implement-feature&...
```

Cache invalidation is scoped to minimize recomputation:

| Event | Invalidation Scope |
|-------|-------------------|
| Platform upgrade | All caches |
| Foundry catalog sync | All Workshops/Workbenches in Foundry |
| Workshop catalog sync | All Workbenches in Workshop |
| Workbench catalog sync | That Workbench only |
| User catalog sync | That User's sessions only |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Work Catalog](../../concepts/work-catalog.md) | Resolution makes the catalog executable |
| [Containment Hierarchy](../../concepts/containment-hierarchy.md) | Resolution follows the hierarchy |
| [Scenario](../../concepts/scenario.md) | Scenarios are resolved artifacts |

Resolution operationalizes the ACE principle that work definitions can be customized at each level of the hierarchy. UPIM defines the Work Model; Resolution determines which version of that model applies in a given context.

## Related concepts

- [Work Catalog](../../concepts/work-catalog.md) — The catalog that resolution navigates
- [Scenario](../../concepts/scenario.md) — Primary artifact type resolved
- [Containment Hierarchy](../../concepts/containment-hierarchy.md) — Structure resolution follows
- [Validation Module](validation-module.md) — Validates before resolution
- [Workshop Sync](workshop-sync.md) — Populates each level of the hierarchy

## Further reading

- [../platform-developer-guide/work-catalog-management/resolution-algorithm.md](../platform-developer-guide/work-catalog-management/resolution-algorithm.md) — Full algorithm specification
- [../platform-developer-guide/work-catalog-management/README.md](../platform-developer-guide/work-catalog-management/README.md) — Work Catalog Management overview
- [../../work-catalogues/README.md](../../work-catalogues/README.md) — Conceptual overview of Work Catalogs
