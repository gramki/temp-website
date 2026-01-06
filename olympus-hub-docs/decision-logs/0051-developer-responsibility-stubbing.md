# ADR-0051: Developer Responsibility for Machine and Tool Stubbing

## Status

Accepted

## Date

2026-01-06

## Context

Integration testing requires isolation from external dependencies (Machines, Tools). A decision is needed on whether the platform provides stubbing infrastructure or whether this is a developer responsibility.

### Constraints

- Machines and Tools can be external systems with complex behaviors
- Stubbing requirements vary widely by use case
- Platform cannot anticipate all stubbing needs
- Test environments need predictable behavior

### Requirements

- Support for isolated testing
- Predictable test execution
- Flexibility for diverse stubbing needs
- Clear responsibility boundaries

## Decision

**Stubbing of Machines and Tools is a developer responsibility.** The platform does not provide built-in stubbing infrastructure. Developers should create mock implementations and configure test-specific Machine/Tool instances.

### What Can Be Promoted vs Configured

| Artifact | Can Be Promoted | Notes |
|----------|-----------------|-------|
| Machine Definitions (contracts) | ✅ | Abstract specifications |
| Tool Definitions (contracts) | ✅ | Abstract specifications |
| Machine Instances (concrete) | ❌ | Configured per subscription |
| Tool Instances (concrete) | ❌ | Configured per subscription |
| Environment configurations | ❌ | Configured per subscription |

### Recommended Approach

1. Create mock implementations for external dependencies
2. Configure test-specific Machine/Tool instances pointing to mocks
3. Use dedicated test Hub Environments
4. Use separate DEV workbenches for testing

## Alternatives Considered

### Alternative 1: Platform-Provided Stubbing

Build stubbing infrastructure into Hub.

**Pros:**
- Consistent stubbing approach
- Easier for developers
- Platform-managed

**Cons:**
- Cannot anticipate all stubbing needs
- Complex to implement generically
- High maintenance burden
- May not match real behavior

**Why rejected:** Too complex and unlikely to meet diverse needs.

### Alternative 2: Record/Replay Infrastructure

Provide traffic recording and replay for stubbing.

**Pros:**
- Realistic test data
- Developer doesn't write stubs

**Cons:**
- Complex infrastructure
- Privacy concerns with recorded data
- Fragile to API changes
- Storage overhead

**Why rejected:** Complexity and privacy concerns.

### Alternative 3: Service Mesh-Based Stubbing

Use service mesh capabilities for request interception.

**Pros:**
- Infrastructure-level
- Transparent to applications

**Cons:**
- Requires service mesh
- Complex configuration
- Not all environments have mesh

**Why rejected:** Infrastructure dependency too strong.

## Consequences

### Positive

- Clear responsibility boundary
- Developers have full control over stub behavior
- No platform stubbing infrastructure to maintain
- Flexibility for any stubbing approach

### Negative

- Developers must build/manage stubs
- No standardized stubbing
- Potential for inconsistent testing practices

### Neutral

- Promotes/enforces specifications (contracts), not concrete instances
- Test environments must be explicitly configured

## Implementation Notes

- Tool instances can point to mock endpoints for testing
- Hub Environments can be dedicated to testing with specific configurations
- Developers can use any mocking framework/tool of choice

## References

- [Hub Test Runner](../04-subsystems/ci-subsystem/test-runner.md)
- [CI Subsystem README](../04-subsystems/ci-subsystem/README.md)

