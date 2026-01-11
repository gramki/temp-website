# ADR-0095: BlueprintSpec Transformation Model

## Status

Accepted

## Date

2026-01-11

## Context

When Marketplace packages are subscribed to by a workbench, a key question arises: How do the package contents become usable in the subscriber's workbench?

### Options Considered

1. **Direct copy** — Copy specifications directly into workbench
2. **Reference-based** — Reference specifications from package (live link)
3. **BlueprintSpec transformation** — Transform to intermediate type, then create derived resources

### Constraints

- Blueprints should not directly become part of workbench definition
- Subscribers need to customize specifications for their context
- Update tracking from source Blueprint is desirable
- Clear distinction between "template" and "deployed resource"

### Requirements

- Blueprints remain separate from workbench resources
- Derived resources can be customized
- Update path from Blueprint to derived resources
- Clear ownership (subscriber owns derived resources)

## Decision

**When specifications are exported to a Package, their CRD types transform to corresponding BlueprintSpec types.** When subscribed, BlueprintSpecs are usable but must be converted to regular specifications to become part of the workbench.

### Transformation Flow

```
Export to Package:
  ScenarioNormativeSpec  →  ScenarioBlueprintSpec
  WorkbenchSpec          →  WorkbenchBlueprintSpec
  MachineSpec            →  MachineBlueprintSpec
  ToolSpec               →  ToolBlueprintSpec

Subscription:
  BlueprintSpecs become available/usable in workbench
  (Not directly part of workbench definition)

Usage:
  ScenarioBlueprintSpec  →  ScenarioNormativeSpec + ScenarioAutomationSpec
  (Derived resources created from BlueprintSpecs)
```

### Blueprint Reference Tracking

Derived resources include a reference section:
- Package SHA (integrity verification)
- Package URI (source location)
- BlueprintSpec name and type
- Package version

This enables:
- Update tracking from later Blueprint versions
- Divergence detection (if derived resource is modified)
- Manual merge capability for updates

### Derived Resource Behavior

- **Unmodified** — Can receive updates from Blueprint
- **Divergent** — Modified after creation; manual merge required
- **Out-of-sync** — User chose not to update; tracked in Marketplace Console

## Alternatives Considered

### Alternative 1: Direct Copy

Copy specifications directly into workbench at subscription time.

**Pros:**
- Simple model
- No intermediate type

**Cons:**
- No distinction between template and deployed resource
- No update tracking
- Unclear provenance

**Why rejected:** Loses valuable update tracking and provenance information.

### Alternative 2: Reference-Based (Live Link)

Workbench references package specifications directly.

**Pros:**
- Automatic updates
- No duplication

**Cons:**
- No customization ability
- Package changes affect all subscribers immediately
- No subscriber control over updates

**Why rejected:** Subscribers need control over when/if to update; customization is essential.

## Consequences

### Positive

- Clear distinction between Blueprint (template) and deployed resource
- Subscribers can customize derived resources
- Update path from Blueprint to derived resources
- Divergence is tracked and visible
- Subscribers control update timing

### Negative

- More complex than direct copy
- Two-step process (subscribe, then create derived resources)
- BlueprintSpec types add to CRD taxonomy

### Neutral

- Marketplace Console shows update availability and out-of-sync resources
- Hybrid update workflow (system suggests, user approves)

## Implementation Notes

- BlueprintSpec types mirror regular Spec types with "Blueprint" prefix
- Blueprint reference section added to derived resource CRDs
- Workbench Management handles derived resource creation
- Marketplace Console tracks sync status

## References

- [Blueprints and Packages](../04-subsystems/marketplace/blueprints-and-packages.md)
- [Subscription Services](../04-subsystems/marketplace/subscription-services.md)
- [Version Management](../04-subsystems/marketplace/version-management.md)

