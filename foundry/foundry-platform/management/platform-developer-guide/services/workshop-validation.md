# GitHub Integration (Validation Module)

> **Canonical module:** [../validation/README.md](../validation/README.md)
>
> This document covers GitHub-specific integration for the Validation module. The historical name "Workshop Validation Service" referred to the same capability before Validation was unified as a Management subsystem.

## Purpose

- Receive GitHub PR events for Foundry and Workshop definition repos
- Post `foundry-validation` check runs
- Gate merges — only the Validation module can merge to main on definition repos
- Provide fast feedback via check annotations

## How It Works

```
┌─────────────────┐
│ Definition Repo │
│      (Git)      │
└────────┬────────┘
         │ PR opened
         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Validation Module                          │
│                                                             │
│  1. Receive GitHub check run trigger                        │
│  2. Fetch PR diff                                           │
│  3. Route changed files to domain validators:               │
│     - ConfigValidator (entity YAML)                         │
│     - WorkCatalogValidator (work-catalog/**)                │
│     - KnowledgeValidator (domain/, practices/)              │
│  4. Report results as foundry-validation check              │
│  5. If all pass, merge PR                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
         │
         │ check status
         ▼
┌─────────────────┐
│   PR Status     │
│  (pass/fail)    │
└─────────────────┘
```

## Check Run Configuration

```yaml
name: foundry-validation
trigger:
  - pull_request:
      branches: [main]
      paths:
        - 'work-catalog/**'
        - 'workbenches/**'
        - 'workspaces/**'
        - 'domain/**'
        - 'practices/**'
        - 'foundry.yaml'
        - 'workshop.yaml'
        - '*.yaml'
```

## Merge Control

The Validation module is the **only entity** with merge permission on definition repos:

1. Branch protection requires the `foundry-validation` check to pass
2. Direct pushes to main are disabled
3. The Validation module uses a GitHub App token to perform the merge

## Error Reporting

Errors are reported as GitHub check annotations:

```
❌ workbenches/checkout/work-catalog/build/product-intent/development/scenarios/implement-feature.yaml
   Line 6: [SC-005] Invalid scope: external. Must be 'workspace-ingress' or 'workspace-internal'
   Line 25: [SC-030] Unknown skill: advanced-coding
```

## Service Errors

| Error | Handling |
|-------|----------|
| GitHub API unavailable | Retry with exponential backoff |
| Schema not found | Fail validation with clear error |
| Timeout | Fail check, allow re-run |

## Read Next

- [../validation/README.md](../validation/README.md) — Validation module scope and architecture
- [../validation/requirements.md](../validation/requirements.md) — APIs and triggers
- [workshop-sync.md](workshop-sync.md) — What happens after merge
- [metadata-service.md](metadata-service.md) — Where validated config is stored
