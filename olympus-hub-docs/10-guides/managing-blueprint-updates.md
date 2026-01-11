# Guide: Managing Blueprint Updates

> **Status:** 🟡 Draft
> **Audience:** Developer, Process Architect, Tenant Admin
> **Last Updated:** 2026-01-11

This guide explains how to handle version updates from Marketplace packages, including update notifications, applying updates, and managing divergent resources.

---

## Table of Contents

1. [Overview](#overview)
2. [Understanding Version Management](#understanding-version-management)
3. [Receiving Update Notifications](#receiving-update-notifications)
4. [Checking for Updates](#checking-for-updates)
5. [Applying Updates to Non-Divergent Resources](#applying-updates-to-non-divergent-resources)
6. [Handling Divergent Resources](#handling-divergent-resources)
7. [Version Ranges and Automatic Compatibility](#version-ranges-and-automatic-compatibility)
8. [Tracking Out-of-Sync Resources](#tracking-out-of-sync-resources)
9. [Best Practices](#best-practices)
10. [Related Documentation](#related-documentation)

---

## Overview

When publishers release new versions of Marketplace packages, you control when and how to apply updates to your derived resources. Updates are **never automatic** — you always decide.

### Update Principles

| Principle | Description |
|-----------|-------------|
| **Explicit Pull** | You must explicitly request updates |
| **User Control** | You decide timing and scope |
| **Hybrid Workflow** | System suggests, you approve |
| **No Forced Updates** | Skipping updates is allowed |

---

## Understanding Version Management

### Semantic Versioning

Packages follow semantic versioning (SemVer):

| Version Change | Meaning | Compatibility |
|----------------|---------|---------------|
| **MAJOR** (1.x.x → 2.x.x) | Breaking changes | May require migration |
| **MINOR** (1.1.x → 1.2.x) | New features | Backward compatible |
| **PATCH** (1.1.1 → 1.1.2) | Bug fixes | Backward compatible |

### Publisher Commitment

- Minor versions are **in-place upgradable**
- Major versions may require explicit migration

---

## Receiving Update Notifications

When a publisher releases a new version, you're notified.

### Notification Channels

| Channel | Description |
|---------|-------------|
| **Marketplace Console** | Notification badge and section |
| **Email** | If configured for Marketplace notifications |
| **CLI** | Status commands show updates |

### Notification Content

```
New Version Available: Dispute Operations Suite

Current: v1.2.0 → Available: v1.3.0

What's New:
- Enhanced dispute categorization
- Performance improvements
- Bug fixes

Compatibility: Minor version (in-place upgradable)
```

---

## Checking for Updates

### Via CLI

```bash
# Check all subscriptions for updates
hub marketplace subscriptions list --show-updates

# Check specific subscription
hub marketplace subscriptions status dispute-ops-sub
```

### Via Marketplace Console

1. Navigate to **Subscriptions**
2. Look for "Update Available" badges
3. Click to see details

### Update Information

| Field | Description |
|-------|-------------|
| **New Version** | Available version number |
| **Changelog** | What's new in this version |
| **Compatibility** | Breaking/non-breaking |
| **Affected Resources** | Your derived resources |

---

## Applying Updates to Non-Divergent Resources

For resources that haven't been modified after creation.

### Step 1: Pull New Version

```bash
hub marketplace subscriptions update dispute-ops-sub --version 1.3.0
```

This makes the new BlueprintSpecs available.

### Step 2: Update Derived Resources

```bash
# Update specific resource
hub update scenario-normative dispute-triage --from-blueprint

# Update all resources from package
hub marketplace subscriptions apply-updates dispute-ops-sub
```

### Step 3: Validate and Deploy

```bash
# Validate
hub validate scenario dispute-triage

# Redeploy
hub sync scenario-deployment dispute-triage-sandbox
```

### Container Updates

- New containers are cloned on deployment
- Running pods not affected until rollout
- You control rollout timing

---

## Handling Divergent Resources

If you've modified a derived resource, it becomes **divergent**. Updates require manual merge.

### Check Divergence Status

```bash
hub describe scenario-normative dispute-triage --show-blueprint
```

Output shows:
- Blueprint reference
- Divergence status
- Changes since creation

### Option 1: Accept Blueprint (Overwrite)

Replace your changes with Blueprint:

```bash
hub update scenario-normative dispute-triage --from-blueprint --overwrite
```

⚠️ **Warning**: Your customizations will be lost.

### Option 2: Keep Local (Skip Update)

Keep your version, mark as out-of-sync:

```bash
hub marketplace subscriptions skip-update dispute-triage
```

### Option 3: Manual Merge

Selectively apply changes:

```bash
# View diff between your resource and new Blueprint
hub diff --blueprint dispute-triage --new-version 1.3.0

# Interactive merge
hub merge --from-blueprint dispute-triage --interactive
```

During interactive merge:
- Review each change
- Accept or reject individual changes
- Result: Updated resource with your customizations preserved

---

## Version Ranges and Automatic Compatibility

Subscribe with version ranges to reduce update toil.

### Version Range Syntax

| Syntax | Meaning |
|--------|---------|
| `1.2.3` | Exact version only |
| `^1.2.3` | Compatible with 1.x.x (≥1.2.3, <2.0.0) |
| `~1.2.3` | Compatible with 1.2.x (≥1.2.3, <1.3.0) |

### Subscribe with Range

```bash
hub marketplace subscribe dispute-ops "^1.2.0" my-workbench
```

### Benefits

- Minor/patch updates available automatically
- Still requires explicit apply
- Protects from major version surprises

---

## Tracking Out-of-Sync Resources

Resources you've chosen not to update are tracked as "out-of-sync."

### View Out-of-Sync Resources

Via Marketplace Console:
1. Navigate to **Notifications**
2. View "Out-of-Sync Resources" section

Via CLI:

```bash
hub marketplace status --out-of-sync
```

### Resource States

| State | Description |
|-------|-------------|
| **Synced** | Matches current Blueprint version |
| **Update Available** | Newer version exists |
| **Out-of-Sync** | Chose to skip available update |
| **Divergent** | Modified after creation |
| **Orphaned** | Blueprint withdrawn |

---

## Best Practices

### 1. Stay Informed

Enable Marketplace notifications to know when updates are available.

### 2. Use Version Ranges

Subscribe with `^` to automatically see compatible updates.

### 3. Test Updates in DEV First

```bash
# Update in DEV workbench first
hub marketplace subscriptions update dispute-ops-sub-dev

# Test thoroughly
# Then update PROD
```

### 4. Document Customizations

Keep notes on why you diverged from Blueprint — helps with merge decisions.

### 5. Regular Review

Periodically review out-of-sync resources:

```bash
hub marketplace status --out-of-sync
```

### 6. Consider Re-basing

If significantly diverged, consider:
1. Document your changes
2. Create fresh from new Blueprint
3. Reapply your customizations

---

## Related Documentation

- [Subscribing to Packages](./subscribing-to-packages.md) — Package subscription
- [Using BlueprintSpecs](./using-blueprintspecs.md) — Creating derived resources
- [Building Scenario from Blueprint](./building-scenario-from-blueprint.md) — Complete workflow
- [Version Management](../04-subsystems/marketplace/version-management.md) — System documentation

