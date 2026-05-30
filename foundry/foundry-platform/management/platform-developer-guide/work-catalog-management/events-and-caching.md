# Events and Caching

This document specifies the event system and caching strategy for Work Catalog Management.

## Overview

Work Catalog Management uses events for coordination between services and caching for performance. Events notify consumers of changes; caches reduce latency for repeated queries.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              Event Flow                                          │
│                                                                                  │
│  ┌─────────────┐     publish     ┌─────────────┐     consume    ┌─────────────┐ │
│  │    Sync     │ ───────────────▶│   Message   │───────────────▶│ Orchestrator│ │
│  │   Service   │                 │    Bus      │                │ WO Runtime  │ │
│  └─────────────┘                 │  (Kafka)    │                │   IDE       │ │
│        │                         └─────────────┘                └─────────────┘ │
│        │ invalidate                    │                                         │
│        ▼                               │                                         │
│  ┌─────────────┐                       │                                         │
│  │    Cache    │◀──────────────────────┘                                         │
│  │   (Redis)   │     invalidate on event                                         │
│  └─────────────┘                                                                 │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Events

### Event Types

| Event | Description | Published By | Consumed By |
|-------|-------------|--------------|-------------|
| `catalog.synced` | Work Catalog repository synced | Sync Service | Cache, Orchestrator, WO Runtime |
| `catalog.validation-failed` | Sync validation failed | Sync Service | Notifications |
| `scenario.created` | New Scenario added | Sync Service | WO Runtime, IDE |
| `scenario.updated` | Scenario modified | Sync Service | WO Runtime, IDE |
| `scenario.deleted` | Scenario removed | Sync Service | WO Runtime, IDE |
| `oi-workflow.created` | New OI Workflow added | Sync Service | Orchestrator |
| `oi-workflow.updated` | OI Workflow modified | Sync Service | Orchestrator |
| `oi-workflow.deleted` | OI Workflow removed | Sync Service | Orchestrator |
| `user-catalog.activated` | User activated their catalog | Session Service | Cache |
| `user-catalog.deactivated` | User deactivated their catalog | Session Service | Cache |

### Event Schemas

#### catalog.synced

```json
{
  "event_type": "catalog.synced",
  "timestamp": "2026-05-28T10:30:00Z",
  "source": "sync-service",
  "data": {
    "repo_type": "workshop",
    "repo_id": "acme/ecommerce-workshop-definition",
    "scope": {
      "foundry_id": "acme",
      "workshop_id": "ecommerce"
    },
    "commit_sha": "abc123",
    "artifacts": {
      "oi_workflows_created": 0,
      "oi_workflows_updated": 1,
      "oi_workflows_deleted": 0,
      "scenarios_created": 2,
      "scenarios_updated": 0,
      "scenarios_deleted": 1
    }
  }
}
```

#### scenario.created / scenario.updated

```json
{
  "event_type": "scenario.created",
  "timestamp": "2026-05-28T10:30:00Z",
  "source": "sync-service",
  "data": {
    "name": "implement-feature",
    "workspace": "development",
    "scope": "workspace-ingress",
    "catalog_level": "workshop",
    "catalog_scope": {
      "foundry_id": "acme",
      "workshop_id": "ecommerce"
    },
    "source": {
      "repository": "acme/ecommerce-workshop-definition",
      "path": "work-catalog/workspaces/development/scenarios/implement-feature.yaml",
      "commit_sha": "abc123"
    }
  }
}
```

#### scenario.deleted

```json
{
  "event_type": "scenario.deleted",
  "timestamp": "2026-05-28T10:30:00Z",
  "source": "sync-service",
  "data": {
    "name": "old-scenario",
    "workspace": "development",
    "catalog_level": "workshop",
    "catalog_scope": {
      "foundry_id": "acme",
      "workshop_id": "ecommerce"
    },
    "reason": "file_deleted"
  }
}
```

#### user-catalog.activated

```json
{
  "event_type": "user-catalog.activated",
  "timestamp": "2026-05-28T10:30:00Z",
  "source": "session-service",
  "data": {
    "user_id": "alice",
    "foundry_id": "acme",
    "session_id": "session-123",
    "activation_source": "session",
    "expires_at": "2026-05-28T18:00:00Z"
  }
}
```

### Event Publishing

```python
async def publish_event(event_type: str, data: dict):
    """Publish event to message bus."""
    
    event = {
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source": SERVICE_NAME,
        "event_id": str(uuid.uuid4()),
        "data": data
    }
    
    # Publish to Kafka topic
    await kafka_producer.send(
        topic="work-catalog-events",
        key=f"{event_type}:{data.get('name', 'unknown')}",
        value=json.dumps(event)
    )
    
    logger.info("Event published", extra={
        "event_type": event_type,
        "event_id": event["event_id"]
    })
```

### Event Consumption

```python
@kafka_consumer.handler("work-catalog-events")
async def handle_catalog_event(event: dict):
    """Handle work catalog events."""
    
    event_type = event["event_type"]
    
    if event_type == "catalog.synced":
        await invalidate_caches_for_sync(event["data"])
    
    elif event_type in ["scenario.created", "scenario.updated", "scenario.deleted"]:
        await invalidate_scenario_caches(event["data"])
    
    elif event_type in ["oi-workflow.created", "oi-workflow.updated", "oi-workflow.deleted"]:
        await invalidate_workflow_caches(event["data"])
    
    elif event_type == "user-catalog.activated":
        await invalidate_user_caches(event["data"])
```

---

## Caching Strategy

### Cache Layers

| Layer | Storage | TTL | Purpose |
|-------|---------|-----|---------|
| Resolution Cache | Redis | 5 min | Effective catalog and single artifact resolution |
| Validation Cache | Redis | 1 hour | Validation results for unchanged content |
| Recommendation Cache | Redis | 5 min | Agent recommendations for scenarios |
| Schema Cache | In-memory | Indefinite | Schema versions (immutable) |

### Cache Keys

| Cache Type | Key Pattern | Example |
|------------|-------------|---------|
| Effective Catalog | `effective-catalog:{foundry}:{workshop}:{workbench}:{user}` | `effective-catalog:acme:ecommerce:checkout:alice` |
| Single Artifact | `resolve:{type}:{name}:{foundry}:{workshop}:{workbench}:{user}` | `resolve:scenario:implement-feature:acme:ecommerce:checkout:alice` |
| Validation | `validation:{content_hash}:{api_version}` | `validation:sha256abc:foundry/v1` |
| Recommendations | `recommendations:{scenario_id}:{workspace_id}` | `recommendations:sc-123:checkout-dev` |
| Sources | `sources:{foundry}:{workshop}:{workbench}:{user}` | `sources:acme:ecommerce:checkout:alice` |

### Cache Operations

#### Get Effective Catalog (with cache)

```python
async def get_effective_catalog_cached(context: ResolutionContext) -> EffectiveCatalog:
    """Get effective catalog with caching."""
    
    cache_key = build_effective_catalog_key(context)
    
    # Try cache first
    cached = await redis.get(cache_key)
    if cached:
        metrics.cache_hit("effective_catalog")
        return EffectiveCatalog.from_json(cached)
    
    metrics.cache_miss("effective_catalog")
    
    # Compute effective catalog
    catalog = await compute_effective_catalog(context)
    
    # Store in cache
    await redis.setex(
        cache_key,
        EFFECTIVE_CATALOG_TTL,  # 5 minutes
        catalog.to_json()
    )
    
    return catalog


def build_effective_catalog_key(context: ResolutionContext) -> str:
    """Build cache key for effective catalog."""
    
    user_part = context.user_id if context.user_catalog_active else "none"
    
    return f"effective-catalog:{context.foundry_id}:{context.workshop_id}:{context.workbench_id}:{user_part}"
```

#### Validation Cache

```python
async def validate_with_cache(
    artifact_type: str,
    yaml_content: str,
    api_version: str
) -> ValidationResult:
    """Validate artifact with caching."""
    
    # Hash the content for cache key
    content_hash = hashlib.sha256(yaml_content.encode()).hexdigest()
    cache_key = f"validation:{content_hash}:{api_version}"
    
    # Try cache first
    cached = await redis.get(cache_key)
    if cached:
        metrics.cache_hit("validation")
        return ValidationResult.from_json(cached)
    
    metrics.cache_miss("validation")
    
    # Perform validation
    result = await validate_artifact(artifact_type, yaml_content, api_version)
    
    # Only cache valid results (invalid may be fixed quickly)
    if result.valid:
        await redis.setex(
            cache_key,
            VALIDATION_CACHE_TTL,  # 1 hour
            result.to_json()
        )
    
    return result
```

### Cache Invalidation

#### On Catalog Sync

```python
async def invalidate_caches_for_sync(sync_data: dict):
    """Invalidate caches affected by a catalog sync."""
    
    scope = sync_data["scope"]
    repo_type = sync_data["repo_type"]
    
    patterns_to_invalidate = []
    
    if repo_type == "platform":
        # Platform change: invalidate everything
        patterns_to_invalidate = [
            "effective-catalog:*",
            "resolve:*",
            "sources:*",
            "recommendations:*"
        ]
    
    elif repo_type == "foundry":
        foundry = scope["foundry_id"]
        patterns_to_invalidate = [
            f"effective-catalog:{foundry}:*",
            f"resolve:*:*:{foundry}:*",
            f"sources:{foundry}:*"
        ]
    
    elif repo_type == "workshop":
        foundry = scope["foundry_id"]
        workshop = scope["workshop_id"]
        patterns_to_invalidate = [
            f"effective-catalog:{foundry}:{workshop}:*",
            f"resolve:*:*:{foundry}:{workshop}:*",
            f"sources:{foundry}:{workshop}:*"
        ]
    
    elif repo_type == "workbench":
        foundry = scope["foundry_id"]
        workshop = scope["workshop_id"]
        workbench = scope["workbench_id"]
        patterns_to_invalidate = [
            f"effective-catalog:{foundry}:{workshop}:{workbench}:*",
            f"resolve:*:*:{foundry}:{workshop}:{workbench}:*",
            f"sources:{foundry}:{workshop}:{workbench}:*"
        ]
    
    elif repo_type == "user":
        user = scope["user_id"]
        foundry = scope["foundry_id"]
        patterns_to_invalidate = [
            f"effective-catalog:{foundry}:*:*:{user}",
            f"resolve:*:*:{foundry}:*:*:{user}",
            f"sources:{foundry}:*:*:{user}"
        ]
    
    # Execute invalidations
    for pattern in patterns_to_invalidate:
        keys = await redis.keys(pattern)
        if keys:
            await redis.delete(*keys)
            metrics.cache_invalidation(len(keys), repo_type)
```

#### On User Catalog Activation/Deactivation

```python
async def invalidate_user_caches(activation_data: dict):
    """Invalidate caches when user catalog activation changes."""
    
    user_id = activation_data["user_id"]
    foundry_id = activation_data["foundry_id"]
    
    # Invalidate user-specific caches
    patterns = [
        f"effective-catalog:{foundry_id}:*:*:{user_id}",
        f"resolve:*:*:{foundry_id}:*:*:{user_id}",
        f"sources:{foundry_id}:*:*:{user_id}"
    ]
    
    for pattern in patterns:
        keys = await redis.keys(pattern)
        if keys:
            await redis.delete(*keys)
```

---

## Metrics

### Cache Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `work_catalog_cache_hits_total` | Counter | cache_type | Cache hits |
| `work_catalog_cache_misses_total` | Counter | cache_type | Cache misses |
| `work_catalog_cache_invalidations_total` | Counter | cache_type, reason | Cache invalidations |
| `work_catalog_cache_size_bytes` | Gauge | cache_type | Current cache size |
| `work_catalog_cache_latency_ms` | Histogram | operation, cache_type | Cache operation latency |

### Event Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `work_catalog_events_published_total` | Counter | event_type | Events published |
| `work_catalog_events_consumed_total` | Counter | event_type, status | Events consumed |
| `work_catalog_event_processing_ms` | Histogram | event_type | Event processing latency |
| `work_catalog_event_lag_ms` | Gauge | consumer_group | Consumer lag |

### Implementation

```python
class CacheMetrics:
    def __init__(self):
        self.hits = Counter(
            "work_catalog_cache_hits_total",
            "Cache hits",
            ["cache_type"]
        )
        self.misses = Counter(
            "work_catalog_cache_misses_total",
            "Cache misses",
            ["cache_type"]
        )
        self.invalidations = Counter(
            "work_catalog_cache_invalidations_total",
            "Cache invalidations",
            ["cache_type", "reason"]
        )
        self.latency = Histogram(
            "work_catalog_cache_latency_ms",
            "Cache operation latency",
            ["operation", "cache_type"]
        )
    
    def cache_hit(self, cache_type: str):
        self.hits.labels(cache_type=cache_type).inc()
    
    def cache_miss(self, cache_type: str):
        self.misses.labels(cache_type=cache_type).inc()
    
    def cache_invalidation(self, count: int, reason: str):
        self.invalidations.labels(
            cache_type="all",
            reason=reason
        ).inc(count)

metrics = CacheMetrics()
```

---

## Cache Warming

On service startup or after major cache flush, warm critical caches:

```python
async def warm_caches():
    """Warm critical caches on startup."""
    
    # Get list of active foundries
    foundries = await metadata_service.list_foundries()
    
    for foundry in foundries:
        # Warm foundry-level effective catalog
        context = ResolutionContext(
            foundry_id=foundry.id,
            workshop_id=None,
            workbench_id=None,
            user_catalog_active=False
        )
        await get_effective_catalog_cached(context)
        
        # Warm workshop-level for active workshops
        workshops = await metadata_service.list_workshops(foundry.id)
        for workshop in workshops[:10]:  # Top 10 by activity
            context = ResolutionContext(
                foundry_id=foundry.id,
                workshop_id=workshop.id,
                workbench_id=None,
                user_catalog_active=False
            )
            await get_effective_catalog_cached(context)
    
    logger.info("Cache warming complete")
```

---

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [sync-mechanism.md](sync-mechanism.md) — Sync mechanism details
- [apis.md](apis.md) — API specification
- [resolution-algorithm.md](resolution-algorithm.md) — Resolution algorithm
