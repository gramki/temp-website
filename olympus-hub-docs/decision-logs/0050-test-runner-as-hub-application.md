# ADR-0050: Hub Test Runner as Hub Application on Atlantis

## Status

Accepted

## Date

2026-01-06

## Context

Hub needs integration testing capabilities for Scenarios and standalone Tools. The platform must provide a test execution engine that integrates with Hub's architecture and can be enabled per subscription/workbench.

### Constraints

- Tests must invoke Scenarios through standard I/O Gateway paths
- Test execution must be scoped to workbenches
- Results must be stored and reportable
- Solution should leverage existing Hub infrastructure

### Requirements

- Integration test execution via I/O Gateway
- Test and TestSuite defined as CRDs
- Workbench-scoped testing
- Result storage and reporting
- Enablement control by Tenant Admin

## Decision

The **Hub Test Runner is implemented as a Hub Application** built on the Atlantis Runtime. It executes tests by invoking requests through the I/O Gateway and provides its own storage for results and reporting.

### Key Characteristics

| Aspect | Implementation |
|--------|----------------|
| Runtime | Atlantis (Java/Kotlin) |
| Scope | Per workbench |
| Invocation | Manual/on-demand |
| Test Definition | CRDs (Test, TestSuite) |
| Results Storage | Test Runner managed |

## Alternatives Considered

### Alternative 1: External Testing Tool

Use external tools (Postman, k6, etc.) for testing.

**Pros:**
- Familiar tooling
- Rich ecosystems

**Cons:**
- Not Hub-aware
- Cannot leverage Hub semantics
- Separate authentication/authorization
- No CRD-based test definitions

**Why rejected:** External tools lack Hub integration depth.

### Alternative 2: Dedicated Testing Infrastructure

Build separate testing infrastructure (not a Hub Application).

**Pros:**
- Specialized for testing
- Independent scaling

**Cons:**
- Duplicates Hub capabilities
- Separate deployment/management
- Doesn't benefit from Hub ecosystem

**Why rejected:** Hub Application model provides better integration.

### Alternative 3: Testing as Signal Exchange Feature

Build testing into Signal Exchange.

**Pros:**
- Deep integration
- No separate service

**Cons:**
- Overloads SX responsibilities
- Harder to maintain
- Testing is not SX's core purpose

**Why rejected:** Violates single responsibility.

## Consequences

### Positive

- Leverages existing Hub Application patterns
- Benefits from Atlantis runtime capabilities
- CRD-based tests are declarative and version-controlled
- Natural workbench scoping
- Reuses Hub authentication/authorization

### Negative

- Test Runner is a service that needs to be deployed
- Atlantis dependency for test execution
- Additional Hub Application to manage

### Neutral

- Test Runner follows same lifecycle as other Hub Applications
- Results are managed by Test Runner, not Hub core

## Implementation Notes

- Unit tests remain the responsibility of Runtime CI (per runtime)
- Test Runner focuses on integration tests only
- Machine/Tool stubbing is developer responsibility (not Test Runner)

## References

- [Hub Test Runner](../04-subsystems/ci-subsystem/test-runner.md)
- [Test CRDs](../04-subsystems/ci-subsystem/test-crds.md)
- [CI Subsystem README](../04-subsystems/ci-subsystem/README.md)

