# ADR-0089: Bidirectional DevOps Workbench Binding

## Status
Accepted

## Date
2026-01-09

## Context

The DevOps Workbench pattern (ADR-0088) requires bidirectional integration between Business Workbench (A) and DevOps Workbench (D):

- **A → D**: Signal routing (development lifecycle events)
- **D → A**: Resource access (knowledge, memory, data stores)

We needed to decide how to establish, manage, and secure this bidirectional relationship, especially when A and D are in different subscriptions.

### Key Questions

1. Where should the binding configuration live?
2. How are credentials provisioned and rotated?
3. How does D access A's resources?
4. What happens when A and D are in different subscriptions?

### Options Considered

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Single CRD in A** | A defines binding; D discovers | A controls what it exposes | D has no visibility |
| **B. Single CRD in D** | D declares what it needs; A approves | D is explicit | A loses control |
| **C. Two CRDs with Operators** | A defines binding; operator pushes manifest to D | Full control; automation; bidirectional | More complexity |

## Decision

We adopt **Option C: Two CRDs with Operators** for bidirectional binding.

### CRD Model

| CRD | Location | Created By | Purpose |
|-----|----------|------------|---------|
| `DevOpsWorkbenchBinding` | A (Business) | Tenant Admin | Define what to expose; configure signal routing |
| `BusinessWorkbenchManifest` | D (DevOps) | Operator in A | Machine/Tool definitions; credentials |

### Operator Model

| Operator | Location | Responsibility |
|----------|----------|----------------|
| `DevOpsBindingOperator` | A | Watch binding CRD; provision credentials; push manifest to D |
| `ManifestOperator` | D | Watch manifest CRD; register Machine; create Tool bindings |

### Flow

```
1. Tenant Admin creates DevOpsWorkbenchBinding in A
2. DevOpsBindingOperator in A:
   - Validates configuration
   - Creates ServiceAccount and BotToken
   - Generates BusinessWorkbenchManifest
   - Pushes manifest + credentials to D
3. ManifestOperator in D:
   - Validates manifest
   - Registers {workbench-name}-gateway Machine
   - Creates Tool bindings for exposed resources
   - Stores credentials securely
4. DevOps Agents can now access A's resources via gateway
```

### Credential Management

| Aspect | Design Choice |
|--------|---------------|
| **Auth Type** | Bot token (same-tenant) or mTLS (cross-tenant) |
| **Push Model** | A pushes credentials to D (A is the resource owner) |
| **Rotation** | Explicit rotation with configurable frequency and overlap |
| **Revocation** | Immediate revocation when binding is deleted |

### Resource Exposure

Tenant Admin explicitly specifies exposed resources:

- Knowledge Bank (collections)
- Enterprise Memory (scopes)
- Data Stores (Ganymede, Callisto, Europa)
- CAF Records (record types)
- Scenario Metadata (definitions, configurations)

## Consequences

### Positive

- **A Controls Exposure**: Business workbench owner controls what resources are accessible
- **Automated Provisioning**: Operators handle credential generation and machine registration
- **Secure Cross-Subscription**: Push model with explicit credentials; no implicit trust
- **Rotation and Revocation**: Built-in credential lifecycle management
- **Auditable**: All access via gateway is logged with full context

### Negative

- **Two Operators Required**: Increases operational complexity
- **Cross-Subscription API**: Requires secure API for pushing manifests
- **Configuration Burden**: Tenant Admin must explicitly configure exposed resources

### Neutral

- Same pattern can be used for non-DevOps cross-workbench access scenarios
- ManifestOperator can be extended to support other manifest types

## Related

- [DevOps Workbench Binding](../09-composite-systems-and-patterns/devops-workbench/devops-workbench-binding.md)
- [ADR-0088: DevOps Workbench as Composite Pattern](./0088-devops-workbench-composite-pattern.md)
- [ADR-0090: Signal Routing via Atropos for DevOps](./0090-signal-routing-via-atropos-devops.md)

