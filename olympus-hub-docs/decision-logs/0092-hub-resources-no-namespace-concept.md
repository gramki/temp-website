# ADR-0092: Hub Resources Do Not Use Namespace Concept

> **Status:** Accepted  
> **Date:** 2026-01-11  
> **Deciders:** Architecture Team  
> **Category:** CLI, CRD Design, Developer Experience

---

## Context

Hub resources and CLI commands were using "namespace" terminology inconsistently:

1. **CLI commands** used `-n <namespace>` flags in some documentation
2. **CRD examples** included `namespace:` fields in metadata and spec references
3. **Developer confusion** about whether namespace was a Hub concept or Kubernetes concept
4. **Inconsistent scoping** - unclear if commands were scoped to namespace or workbench instance

The relationship between Hub's workbench instance model and Kubernetes namespaces needed clarification.

---

## Decision

**Hub resources do not use "namespace" as a concept.** All Hub CLI commands are scoped to a **workbench instance**, not a namespace.

### Key Principles

1. **No namespace in Hub CRDs**: Remove all `namespace:` fields from Hub CRD examples and specifications
2. **Workbench instance scoping**: All `hub` commands are automatically scoped to the workbench instance associated with the remote workspace
3. **No `-n` flag needed**: CLI commands do not require or accept a namespace flag
4. **Kubernetes namespace mapping**: Workbench instance → Kubernetes namespace is n:1, configured by Tenant Admin at deployment time (one-time choice)

### Implementation

1. **CLI Commands**: Remove all `-n <namespace>` flags from command examples
   - Commands are auto-scoped to workbench instance from workspace context
   - Example: `hub sync scenario my-scenario` (not `hub sync scenario my-scenario -n my-namespace`)

2. **CRD Examples**: Remove `namespace:` fields from:
   - `metadata.namespace` in all Hub CRD examples
   - `spec.*Ref.namespace` in reference fields (use workbench instance references instead)
   - `workbenchInstance.namespace` fields

3. **Documentation**: Clarify that:
   - Workbench instance is the Hub-level scoping mechanism
   - Kubernetes namespace mapping is an implementation detail (n:1, configured by Tenant Admin)
   - Developers never specify namespace—it's handled by the platform

---

## Rationale

### Why Remove Namespace from Hub?

| Factor | With Namespace | Without Namespace |
|--------|----------------|-------------------|
| **Conceptual Clarity** | Confusion between Hub and K8s concepts | Clear: workbench instance is Hub concept |
| **Developer Experience** | Must remember to add `-n` flag | Commands auto-scoped, simpler |
| **CRD Complexity** | Extra field to manage | Cleaner CRDs, less confusion |
| **Consistency** | Mixed usage across docs | Consistent workbench instance model |

### Why Workbench Instance Scoping?

1. **Semantic Alignment**: Workbench instance represents the operational context (dev, staging, prod), which is what developers care about
2. **Simpler UX**: No need to remember namespace names or flags—workspace context provides scoping automatically
3. **Clear Ownership**: Workbench instance is a Hub concept; Kubernetes namespace is an implementation detail
4. **One-to-One Mapping**: n:1 relationship is simple and predictable (one workbench instance = one Kubernetes namespace)

---

## Consequences

### Positive

- **Simpler CLI**: No namespace flags to remember or manage
- **Clearer Mental Model**: Workbench instance is the primary scoping concept
- **Consistent Documentation**: All docs use workbench instance consistently
- **Reduced Confusion**: Clear separation between Hub concepts and Kubernetes implementation details
- **Better Developer Experience**: Commands work automatically within workspace context

### Negative

- **Breaking Change**: Existing documentation and examples need updates
- **Migration**: Any scripts or automation using `-n` flags need updates
- **Learning Curve**: Developers need to understand workbench instance model (but this is already required)

### Mitigations

- **Documentation Updates**: All relevant docs updated to reflect new model
- **Clear Examples**: Examples show workbench instance scoping without namespace
- **Migration Guide**: If needed, provide guidance for updating existing scripts

---

## Alternatives Considered

### Alternative 1: Keep Namespace as Hub Concept

Keep `namespace:` fields in CRDs and require `-n` flags in CLI commands.

**Rejected because:**
- Creates confusion with Kubernetes namespace concept
- Adds unnecessary complexity (workbench instance already provides scoping)
- Inconsistent with workbench instance model

### Alternative 2: Support Both Namespace and Workbench Instance

Allow either `-n <namespace>` or `--workbench-instance <instance>` flags.

**Rejected because:**
- Adds complexity without clear benefit
- Two ways to do the same thing creates confusion
- Workbench instance is the correct abstraction

### Alternative 3: Namespace as Alias for Workbench Instance

Treat namespace as an alias that maps to workbench instance.

**Rejected because:**
- Still creates conceptual confusion
- Doesn't simplify the model
- Workbench instance is clearer and more semantic

---

## Related ADRs

- [ADR-0014: GitOps-Based Operator Model](./0014-gitops-operator-model.md)
- [ADR-0012: Control Plane / Data Plane Channel Separation](./0012-control-plane-data-plane-channel-separation.md)

---

## References

- [CLI Channels for Developers](../06-ux-architecture/tenant-domain/cli-channels-for-developers.md)
- [Hub Application Deployment](../02-system-design/implementation-concepts/hub-application-deployment.md)
- [Agent Development Lifecycle Guide](../../olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md)

---

## Implementation Notes

### Files Updated

1. **CLI Documentation**:
   - `cli-channels-for-developers.md` - Removed all `-n` flags, added workbench instance mapping section

2. **Agent Development Docs**:
   - `agent-development-lifecycle.md` - Removed 17 instances of `-n acme-disputes`, removed all `namespace:` fields from CRD examples
   - `agent-lifecycle-faq.md` - Removed all `-n` flags and `namespace:` fields

3. **CRD Documentation**:
   - `hub-application.md` - Removed `namespace:` from metadata
   - `hub-application-deployment.md` - Removed 7 `namespace:` fields from various locations

4. **Setup Guides**:
   - `hub-cli-setup.md` - Removed `hub apply` reference (already deprecated)

### Workbench Instance → Kubernetes Namespace Mapping

- **Relationship**: n:1 (one workbench instance maps to one Kubernetes namespace)
- **Configuration**: Set by Tenant Admin at workbench instance creation time
- **Mutability**: One-time choice, cannot be changed after deployment
- **Visibility**: Implementation detail, not exposed in Hub CRDs or CLI commands
