# Test CRDs

> **Status:** 🔴 Placeholder — Detailed schemas to be defined

## Overview

Tests in Hub are defined as Custom Resource Definitions (CRDs). This document provides placeholder specifications for the Test and TestSuite CRDs.

---

## Test CRD

### Purpose

A **Test** CRD defines a single test case including:
- Target (Scenario signal or Tool operation)
- Input payload
- Expected outcomes
- Assertions

### Placeholder Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: Test
metadata:
  name: create-dispute-happy-path
  namespace: acme-bank
spec:
  # Test metadata
  display_name: "Create Dispute - Happy Path"
  description: "Verify successful dispute creation with valid input"
  tags:
    - smoke
    - regression
  
  # Test type
  type: scenario_integration  # scenario_integration | tool_invocation
  
  # Target configuration
  target:
    # For scenario_integration
    scenario: standard-dispute
    signal_type: dispute.submitted
    
    # For tool_invocation
    # tool: check-eligibility
    # operation: evaluate
  
  # Test environment (optional)
  environment:
    ref: test-env-01
    reset_before: true
  
  # Request configuration
  request:
    # Headers/context
    headers:
      x-correlation-id: "test-{{uuid}}"
    
    # Subject (for scenario tests)
    subject:
      id: "test-customer-001"
      type: customer
    
    # Payload
    payload:
      customer_id: "CUST-001"
      transaction_id: "TXN-12345"
      amount: 150.00
      dispute_type: "unauthorized"
  
  # Expected outcomes
  expectations:
    # Response expectations
    response:
      status_code: 200
      
      # Response body assertions
      body:
        - path: "$.request_id"
          exists: true
        - path: "$.status"
          equals: "CREATED"
    
    # Request update expectations (for async scenarios)
    request_updates:
      - type: REQUEST_CREATED
        within_seconds: 5
      - type: TASK_CREATED
        within_seconds: 10
        assertions:
          - path: "$.task.type"
            equals: "review-dispute"
  
  # Timeout
  timeout_seconds: 60
  
  # Retry configuration
  retry:
    max_attempts: 1
    on_failure: fail  # fail | retry
```

---

## TestSuite CRD

### Purpose

A **TestSuite** CRD groups Tests for ordered execution with shared configuration.

### Placeholder Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: TestSuite
metadata:
  name: dispute-full-flow
  namespace: acme-bank
spec:
  # Suite metadata
  display_name: "Dispute Full Flow"
  description: "End-to-end dispute lifecycle tests"
  tags:
    - integration
    - e2e
  
  # Shared configuration
  defaults:
    environment:
      ref: test-env-01
      reset_before: true
    
    timeout_seconds: 120
    
    # Shared headers
    headers:
      x-test-suite: "dispute-full-flow"
  
  # Pre-flight setup
  setup:
    reset_environment: true
    seed_data:
      enabled: true
      container:
        image: "registry.hub.acme.com/sub-001/test-data:latest"
  
  # Tests (ordered)
  tests:
    - ref: create-dispute-test
      order: 1
      
    - ref: add-evidence-test
      order: 2
      depends_on: create-dispute-test
      # Can override defaults
      timeout_seconds: 180
      
    - ref: escalate-dispute-test
      order: 3
      depends_on: add-evidence-test
      
    - ref: resolve-dispute-test
      order: 4
      depends_on: escalate-dispute-test
  
  # Execution behavior
  execution:
    parallel: false  # Sequential execution
    on_failure: stop  # stop | continue | skip_dependent
    
  # Post-flight cleanup
  teardown:
    reset_environment: false
    cleanup_test_data: true
```

---

## Assertion Types

### Placeholder Assertion Syntax

```yaml
assertions:
  # Equality
  - path: "$.status"
    equals: "CREATED"
  
  # Existence
  - path: "$.request_id"
    exists: true
  
  # Type checking
  - path: "$.amount"
    type: number
  
  # Comparison
  - path: "$.amount"
    greater_than: 0
    less_than: 10000
  
  # Pattern matching
  - path: "$.request_id"
    matches: "^REQ-[A-Z0-9]+$"
  
  # Contains
  - path: "$.tags"
    contains: "urgent"
  
  # Array length
  - path: "$.items"
    length: 3
    length_greater_than: 0
  
  # Nested assertions
  - path: "$.customer"
    assertions:
      - path: "$.name"
        exists: true
      - path: "$.status"
        equals: "active"
```

---

## Variable Substitution

Tests support variable substitution for dynamic values:

```yaml
request:
  payload:
    customer_id: "{{env.TEST_CUSTOMER_ID}}"
    transaction_id: "TXN-{{uuid}}"
    timestamp: "{{now}}"
    reference: "{{previous.response.request_id}}"  # From previous test in suite
```

### Built-in Variables

| Variable | Description |
|----------|-------------|
| `{{uuid}}` | Generate random UUID |
| `{{now}}` | Current timestamp (ISO 8601) |
| `{{today}}` | Current date (YYYY-MM-DD) |
| `{{random.int}}` | Random integer |
| `{{random.string:N}}` | Random string of length N |
| `{{env.VAR_NAME}}` | Environment variable |
| `{{previous.response.PATH}}` | Value from previous test response |

---

## Data-Driven Tests

Placeholder for parameterized test execution:

```yaml
apiVersion: hub.olympus.io/v1
kind: Test
metadata:
  name: dispute-amount-variations
spec:
  # ... base configuration ...
  
  # Data-driven execution
  data_driven:
    enabled: true
    
    # Inline data
    data:
      - name: "small_amount"
        amount: 10.00
        expected_queue: "tier-1"
        
      - name: "medium_amount"
        amount: 500.00
        expected_queue: "tier-1"
        
      - name: "large_amount"
        amount: 5000.00
        expected_queue: "tier-2"
    
    # Or external data source
    # data_source:
    #   type: csv
    #   path: test-data/dispute-amounts.csv
  
  request:
    payload:
      amount: "{{data.amount}}"
  
  expectations:
    response:
      body:
        - path: "$.assigned_queue"
          equals: "{{data.expected_queue}}"
```

---

## Open Points

### To Be Defined

- [ ] Complete assertion syntax and supported operators
- [ ] Variable substitution full specification
- [ ] Data-driven test execution details
- [ ] Request update waiting/polling mechanism
- [ ] Async scenario test patterns
- [ ] Test isolation guarantees
- [ ] Parallel test execution semantics

---

## Related Documentation

- [Hub Test Runner](./test-runner.md) — Test execution engine
- [Runtime CI](./runtime-ci.md) — Unit testing
- [Signal Exchange](../signal-exchange/README.md) — I/O Gateway


