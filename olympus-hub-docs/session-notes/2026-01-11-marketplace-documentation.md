# Session: Marketplace Subsystem Documentation

**Date:** 2026-01-11  
**Focus:** Complete documentation of the Marketplace subsystem

---

## Summary

Implemented the comprehensive Marketplace documentation plan, creating 31 new files and updating 11 existing files across 6 phases.

---

## Work Completed

### Phase 1: Decision Logs (9 ADRs)

Created Architecture Decision Records in `olympus-hub-docs/decision-logs/`:

| ADR | Title |
|-----|-------|
| 0093 | Marketplace as Platform Service |
| 0094 | Hub Package as Atomic Publishing Unit |
| 0095 | BlueprintSpec Transformation Model |
| 0096 | Lazy Container Cloning |
| 0097 | Package Subscription Isolation |
| 0098 | Visibility Controls for Private Marketplace |
| 0099 | Publisher Registration Approval |
| 0100 | Federated IAM for Marketplace |
| 0101 | Platform Notifications Subsystem |

### Phase 2: Marketplace Subsystem Core (9 files)

Created `olympus-hub-docs/04-subsystems/marketplace/`:

| File | Description |
|------|-------------|
| README.md | Subsystem overview with architecture diagrams |
| blueprints-and-packages.md | Hub Package model, BlueprintSpec types |
| marketplace-artifact-repository.md | Container storage, signing, deduplication |
| catalog-services.md | OpenSearch catalog, search, visibility |
| publishing-services.md | Publisher registration, workflow, validation |
| subscription-services.md | Subscription model, BlueprintSpec delivery |
| version-management.md | Semver, updates, divergent resources |
| security-and-compliance.md | Federated IAM, scanning, blacklisting |
| integration-points.md | Integration with other subsystems |

### Phase 3: Platform Notifications Subsystem (3 files)

Created new subsystem at `olympus-hub-docs/04-subsystems/platform-notifications/`:

| File | Description |
|------|-------------|
| README.md | Platform-to-tenant notifications overview |
| marketplace-notifications.md | Marketplace event notifications |
| subscription-notifications.md | Tenant subscription lifecycle notifications |

### Phase 4: Subsystem Updates

**New file:**
- `olympus-hub-docs/04-subsystems/operators/marketplace-operators.md`

**Updated files:**
- `olympus-hub-docs/04-subsystems/operators/README.md` - Added Marketplace operators section
- `olympus-hub-docs/04-subsystems/artifact-registry/README.md` - Added Marketplace integration
- `olympus-hub-docs/04-subsystems/artifact-registry/promotion-model.md` - Added Blueprint promotion
- `olympus-hub-docs/04-subsystems/workbench-management/README.md` - Added BlueprintSpecs section
- `olympus-hub-docs/04-subsystems/registry-services/README.md` - Added platform resources in packages
- `olympus-hub-docs/04-subsystems/subscription-management/README.md` - Added publisher registration

### Phase 5: UX Architecture Updates

**New file:**
- `olympus-hub-docs/06-ux-architecture/tenant-domain/marketplace-console.md`

**Updated files:**
- `olympus-hub-docs/06-ux-architecture/tenant-domain/automation-development-desk.md`
- `olympus-hub-docs/06-ux-architecture/tenant-domain/scenario-design-desk.md`
- `olympus-hub-docs/06-ux-architecture/tenant-domain/automation-product-desk.md`
- `olympus-hub-docs/06-ux-architecture/tenant-domain/hub-control-center.md`
- `olympus-hub-docs/06-ux-architecture/publisher-domain/hub-win-ops-center.md`
- `olympus-hub-docs/06-ux-architecture/tenant-domain/cli-channels-for-developers.md`

### Phase 6: Guides (8 files)

Created in `olympus-hub-docs/10-guides/`:

**Publisher Guides:**
- `marketplace-publisher-registration.md`
- `publishing-scenario-blueprints.md`
- `publishing-workbench-blueprints.md`
- `package-manifest-reference.md`

**Subscriber Guides:**
- `subscribing-to-packages.md`
- `using-blueprintspecs.md`
- `building-scenario-from-blueprint.md`
- `managing-blueprint-updates.md`

---

## Key Design Decisions Documented

1. **Platform Service** - Marketplace is platform-level, not tenant-scoped
2. **Hub Package** - Atomic unit of publishing; self-sufficient Blueprint collections
3. **BlueprintSpec Transformation** - Specs become BlueprintSpecs when exported
4. **Lazy Container Cloning** - Containers cloned on first deployment, not subscription
5. **Package Isolation** - No cross-package dependencies
6. **Visibility Controls** - Allow/disallow lists in package manifest for privacy
7. **Publisher Registration** - Hub Win team approval required
8. **Federated IAM** - Tenant IAM federates with Marketplace IAM
9. **Platform Notifications** - Separate subsystem from business domain notifications

---

## Files Summary

| Category | Created | Updated |
|----------|---------|---------|
| Decision Logs | 9 | - |
| Marketplace Subsystem | 9 | - |
| Platform Notifications | 3 | - |
| Other Subsystems | 1 | 5 |
| UX Architecture | 1 | 6 |
| Guides | 8 | - |
| **Total** | **31** | **11** |

---

## Related Documents

- [Marketplace Exploration (scratchpad)](../scratchpad/hub-marketplace-exploration.md)
- [Marketplace Open Questions (scratchpad)](../scratchpad/hub-marketplace-open-questions.md)

