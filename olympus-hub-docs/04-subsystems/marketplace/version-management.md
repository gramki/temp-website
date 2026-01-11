# Version Management

> **Status:** 🟡 WIP — Design Complete

This document describes semantic versioning for packages, update notifications, the Blueprint update workflow, and handling of divergent resources.

---

## Overview

Marketplace uses semantic versioning (semver) for package versions with explicit, user-controlled updates.

| Aspect | Approach |
|--------|----------|
| **Versioning** | Semantic versioning (MAJOR.MINOR.PATCH) |
| **Updates** | Explicit pull (no automatic propagation) |
| **Notifications** | All subscribers notified of new versions |
| **Workflow** | Hybrid (system suggests, user approves) |

---

## Semantic Versioning

### Version Format

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]

Examples:
  1.0.0              # Release version
  1.2.3              # Release version
  2.0.0-beta.1       # Pre-release
  1.2.3+abc123       # With build metadata
```

### Version Semantics

| Version Change | Meaning | Upgrade Compatibility |
|----------------|---------|----------------------|
| **MAJOR** | Breaking changes | May require migration |
| **MINOR** | Backward-compatible features | In-place upgradable |
| **PATCH** | Backward-compatible fixes | In-place upgradable |

### Publisher Requirements

- **Minor versions must be in-place upgradable** (no breaking changes)
- Major versions may require explicit migration
- Publishers should provide release notes for all versions

---

## Version References

Subscribers can reference packages using version specifications:

### Reference Types

| Reference | Meaning |
|-----------|---------|
| `1.2.3` | Exact version |
| `^1.2.3` | Compatible with 1.x.x (≥1.2.3, <2.0.0) |
| `~1.2.3` | Compatible with 1.2.x (≥1.2.3, <1.3.0) |
| `>=1.2.3 <2.0.0` | Explicit range |

### Benefits of Range References

- Reduces manual update toil
- Automatically compatible with minor/patch updates
- Explicit control over major version changes

---

## Update Notifications

When a publisher releases a new version:

### Notification Flow

```
1. Publisher publishes new package version
2. Marketplace identifies all package-subscribers
3. Notification sent to each subscriber:
   - Tenant Admin
   - Users with package management permissions

4. Notification includes:
   - New version number
   - Release notes / changelog
   - Compatibility information
   - Link to update
```

### Notification Content

```
New Version Available: Dispute Operations Suite

Current: v1.2.0 → Available: v1.3.0

What's New:
- Enhanced dispute categorization
- Performance improvements

Compatibility: Minor version (in-place upgradable)

[View Details] [Update Now] [Dismiss]
```

---

## Update Workflow

Updates follow a **hybrid approach**: system suggests, user approves.

### Update Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           UPDATE WORKFLOW                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. NEW VERSION NOTIFICATION                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User receives notification of new version                         │    │
│   │  Marketplace Console shows update available                        │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   2. USER REVIEWS                                                           │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  • Reviews release notes                                           │    │
│   │  • Checks compatibility                                            │    │
│   │  • Decides whether to update                                       │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   3. PULL NEW VERSION                                                       │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User initiates update                                             │    │
│   │  • New BlueprintSpec version available in workbench                │    │
│   │  • Old version still available                                     │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   4. UPDATE DERIVED RESOURCES                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  For each derived resource:                                        │    │
│   │  • System suggests changes from new Blueprint                      │    │
│   │  • User reviews and approves                                       │    │
│   │  • Derived resource updated                                        │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   5. DEPLOY                                                                 │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Updated resources deployed through normal workflow                │    │
│   │  • New containers cloned if needed                                 │    │
│   │  • Rollout controlled by user                                      │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Key Principles

- **No automatic propagation** — Users must explicitly pull updates
- **User control** — Users decide when and what to update
- **Partial updates allowed** — Can update some resources, not others
- **Nothing forced** — System suggests, never forces

---

## Divergent Resources

When a derived resource is modified after creation, it becomes **divergent**.

### Divergence States

| State | Description |
|-------|-------------|
| **Synced** | Derived resource matches Blueprint |
| **Update Available** | Newer Blueprint version exists |
| **Divergent** | Derived resource modified from Blueprint |
| **Out-of-Sync** | User chose not to apply available update |

### Handling Divergence

```
Derived Resource Created from Blueprint v1.0.0
                    │
                    ▼
User Modifies Derived Resource
                    │
                    ▼
Resource becomes DIVERGENT
                    │
                    ▼
Blueprint v1.1.0 released
                    │
                    ▼
Update workflow:
  • System shows diff between:
    - Current derived resource
    - Blueprint v1.1.0
  • User can:
    - Apply Blueprint changes (may require merge)
    - Skip (resource becomes out-of-sync)
    - Manual merge (cherry-pick changes)
```

### Merge Workflow

For divergent resources, users can:

1. **Accept Blueprint** — Overwrite local changes with Blueprint
2. **Keep Local** — Skip Blueprint update (mark out-of-sync)
3. **Manual Merge** — Selectively apply changes

---

## Out-of-Sync Tracking

Marketplace Console tracks resources that are out-of-sync with their Blueprints.

### Visibility

| Location | Information Shown |
|----------|-------------------|
| **Marketplace Console** | List of out-of-sync resources |
| **Workbench View** | Indicators on affected resources |
| **Notifications** | Periodic reminders (optional) |

### Resource Status Indicators

```
ScenarioNormativeSpec: dispute-triage
  Blueprint: dispute-triage (v1.0.0)
  Status: ⚠️ Out-of-Sync (v1.2.0 available)
  Last Updated: 2026-01-10
  Divergent: No
```

---

## Withdrawn Blueprints

When a publisher withdraws a package:

### Behavior

| Aspect | Behavior |
|--------|----------|
| **Discovery** | Package hidden from search |
| **Existing Subscriptions** | Continue to work |
| **Derived Resources** | Continue to function |
| **Status** | Marked as "Orphaned and Unsupported" |

### User Experience

```
ScenarioNormativeSpec: dispute-triage
  Blueprint: dispute-triage (v1.0.0)
  Status: ⚠️ Orphaned (Blueprint withdrawn)
  Support: None (publisher withdrew package)
  Action: Consider migrating to alternative
```

### Recommendations

- Publishers should deprecate before withdrawing
- Publishers should provide migration guidance
- Subscribers should plan migration when deprecation announced

---

## Version Compatibility

### Container Updates

- Containers are updated only when derived resources are updated
- Updates don't impact running pods until rollout
- Subscriber controls rollout timing

### Cross-Workbench Consistency

When same Blueprint is used across workbenches:
- Each workbench has its own subscription
- Each workbench can be at different versions
- Version alignment is subscriber's responsibility

---

## Related Documentation

- [Blueprints and Packages](./blueprints-and-packages.md) — Package model
- [Subscription Services](./subscription-services.md) — Subscription lifecycle
- [ADR-0095: BlueprintSpec Transformation Model](../../decision-logs/0095-blueprintspec-transformation.md)
- [Managing Blueprint Updates Guide](../../10-guides/managing-blueprint-updates.md)

