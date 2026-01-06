# Hub Test Runner

> **Category:** DevOps and Lifecycle

---

## Overview

The **Hub Test Runner** is the integration testing framework for Hub scenarios. It invokes requests at the I/O Gateway, validates responses and request updates, and supports test suites with dependencies. Unlike Runtime CI (unit tests), Hub Test Runner tests the complete signal-to-response flow.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address testing. Hub Test Runner is an implementation concept for validating operational scenarios.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Scenario | Test target | Tests validate scenarios |
| Signal | Test input | Tests send signals |

### Gap This Fills

The ontology focuses on runtime. Hub Test Runner addresses:
1. **Integration testing**: How are scenarios tested end-to-end?
2. **Test management**: How are tests organized?
3. **Data management**: How is test data handled?

---

## Definition

**Hub Test Runner** is an integration testing framework that:
- Runs tests against I/O Gateway (full signal flow)
- Uses CRDs for test and test suite definitions
- Supports test data setup and cleanup
- Provides test result storage and reporting

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; tests scenarios in workbench |
| **Lifecycle** | On-demand execution |
| **Ownership** | Developer creates tests; runner executes |
| **Multiplicity** | Many tests per workbench |

---

## Structure

### Test CRD (Placeholder)

```yaml
apiVersion: hub.olympus.io/v1
kind: Test
metadata:
  name: dispute-filing-test
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-dev
  
  # Test description
  display_name: "Dispute Filing Test"
  description: "Verify dispute filing creates request correctly"
  
  # Signal to send
  signal:
    type: dispute.filed
    gateway: heracles
    payload:
      customer_id: "TEST-CUST-001"
      transaction_id: "TEST-TXN-001"
      amount: 500.00
      reason: "unauthorized_charge"
      
  # Expected outcomes
  assertions:
    - type: request_created
      within_seconds: 5
    - type: request_status
      status: IN_PROGRESS
      within_seconds: 30
    - type: task_created
      task_type: investigate
      
  # Cleanup
  cleanup:
    cancel_request: true
```

### Test Suite CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: TestSuite
metadata:
  name: dispute-scenario-suite
spec:
  workbench_ref: dispute-ops-dev
  
  # Ordered test execution
  tests:
    - ref: dispute-filing-test
    - ref: document-upload-test
      depends_on: dispute-filing-test
    - ref: resolution-test
      depends_on: document-upload-test
      
  # Pre-flight setup
  setup:
    reset_data: true
    environment_ref: test-environment
    
  # Suite-level cleanup
  cleanup:
    reset_data: true
```

---

## Behavior

### Test Execution

```
1. Developer triggers test/suite
   └── Via CLI, UI, or schedule

2. Test Runner prepares
   ├── Check environment ready
   ├── Run pre-flight setup
   └── Initialize test context

3. For each test:
   ├── Send signal to I/O Gateway
   ├── Wait for assertions
   ├── Record results
   └── Run test cleanup

4. Compile results
   └── Pass/fail summary
```

### Assertion Types

| Type | Checks |
|------|--------|
| **request_created** | Request exists with correct type |
| **request_status** | Request reaches expected status |
| **task_created** | Task of expected type created |
| **task_completed** | Task completed with outcome |
| **response_body** | Response contains expected data |
| **update_count** | Expected number of updates |

### Data Management

```
Pre-flight setup:
├── Reset data stores to clean state
├── Load test fixtures
└── Configure test environment

Cleanup:
├── Cancel test requests
├── Reset modified data
└── Clear test artifacts
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| I/O Gateway | → invokes | Send test signals |
| Signal Exchange | (via gateway) | Full flow tested |
| Test Environment | ↔ uses | Test-specific config |
| Test Store | → writes | Test results |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Workbench-scoped** | Tests run against single workbench |
| **Integration only** | Not for unit tests |
| **Idempotent setup** | Setup produces consistent state |
| **Cleanup required** | Tests must clean up |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Full flow** | Tests complete signal path |
| ✅ **CRD-based** | Declarative test definitions |
| ✅ **Suite support** | Ordered, dependent tests |
| ✅ **Data management** | Setup and cleanup built-in |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Slower than unit tests** | Use for integration; unit for speed |
| ⚠️ **Environment complexity** | Dedicated test environment |

---

## Examples

### Example 1: Running Test Suite

```bash
# Run integration test suite
hub test run \
  --suite dispute-scenario-suite \
  --workbench dispute-ops-dev
  
# Output:
Test Suite: dispute-scenario-suite
├── dispute-filing-test: PASSED (2.3s)
├── document-upload-test: PASSED (1.8s)
└── resolution-test: PASSED (3.1s)

Overall: 3/3 PASSED
```

### Example 2: Test with Assertions

```yaml
spec:
  signal:
    type: dispute.filed
    payload:
      amount: 10000.00  # High value
      
  assertions:
    - type: request_created
    - type: task_created
      task_type: investigate
    - type: task_escalated     # High value triggers escalation
      to_level: 1
      within_seconds: 60
```

---

## Implementation Notes

### For Developers

- Write tests for key scenarios
- Use suites for dependent flows
- Clean up test data properly
- Keep assertions focused

### For Operators

- Monitor test execution duration
- Manage test environment resources
- Review test result trends

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [CI Subsystem](./ci-subsystem.md) | CI for unit tests |
| [I/O Gateway](./io-gateway.md) | Tests invoke via gateway |
| [Hub Environment](./hub-environment.md) | Test environment config |

---

## References

- [Hub Test Runner](../../04-subsystems/ci-subsystem/test-runner.md)
- [Test CRDs](../../04-subsystems/ci-subsystem/test-crds.md)

