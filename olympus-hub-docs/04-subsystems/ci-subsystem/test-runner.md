# Hub Test Runner (CI Subsystem)

## Overview

The **Hub Test Runner** is a platform-provided subsystem for executing integration tests against Scenarios and standalone Tools. It operates by invoking requests through the I/O Gateway and asserting responses and request updates.

> **Implementation Note:** The Test Runner is itself a Hub Application built on the Atlantis Runtime.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HUB TEST RUNNER ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   TEST DEFINITION                                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │   Test Suite CRD                                                     │   │
│   │   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐           │   │
│   │   │    Test 1     │  │    Test 2     │  │    Test 3     │           │   │
│   │   │    (CRD)      │  │    (CRD)      │  │    (CRD)      │           │   │
│   │   └───────────────┘  └───────────────┘  └───────────────┘           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              │ Execute                                       │
│                              ▼                                               │
│   TEST EXECUTION ENGINE                                                      │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐           │   │
│   │   │  Pre-flight  │──▶│   Execute    │──▶│   Assert     │           │   │
│   │   │   Setup      │   │   Request    │   │   Response   │           │   │
│   │   └──────────────┘   └──────────────┘   └──────────────┘           │   │
│   │          │                   │                   │                   │   │
│   │          ▼                   ▼                   ▼                   │   │
│   │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐           │   │
│   │   │ Hub Env      │   │ I/O Gateway  │   │   Collect    │           │   │
│   │   │ Reset        │   │              │   │   Results    │           │   │
│   │   └──────────────┘   └──────────────┘   └──────────────┘           │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   TEST RESULTS                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐           │   │
│   │   │   Storage     │  │   Reports     │  │   Console     │           │   │
│   │   │               │  │               │  │   Views       │           │   │
│   │   └───────────────┘  └───────────────┘  └───────────────┘           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Scope

| Scope | Supported |
|-------|-----------|
| **Per Workbench** | Tests are scoped to a single workbench |
| **Integration Tests** | Requests via I/O Gateway |
| **Standalone Tools** | Direct tool invocation tests |
| **Unit Tests** | ❌ Not supported (use Runtime CI) |

---

## Test Invocation

### Manual / On-Demand

Tests are invoked manually by Developers or Admins:

| Method | Description |
|--------|-------------|
| **UI** | Test Runner console in Developer interface |
| **API** | REST API for test execution |
| **CLI** | Hub CLI tool (future) |

> **Note:** Automated triggers (on promotion, scheduled) are configurable but test execution itself is manual/on-demand.

---

## Test Execution Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TEST EXECUTION FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. PRE-FLIGHT SETUP                                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │   • Reset Hub Environment (if configured)                            │   │
│   │   • Initialize test data                                             │   │
│   │   • Verify dependencies available                                    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   2. EXECUTE TESTS (per Test CRD)                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │   For each test in suite (respecting order):                         │   │
│   │   • Prepare request payload                                          │   │
│   │   • Send to I/O Gateway                                              │   │
│   │   • Wait for response / request updates                              │   │
│   │   • Execute assertions                                               │   │
│   │   • Record result                                                    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   3. POST-FLIGHT (optional)                                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │   • Cleanup test data                                                │   │
│   │   • Reset environment                                                │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   4. REPORT                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │   • Aggregate results                                                │   │
│   │   • Store in Test Runner storage                                     │   │
│   │   • Generate report                                                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Hub Environment for Testing

Tests can specify a dedicated **Hub Environment** with resettable resources:

```yaml
apiVersion: hub.olympus.io/v1
kind: HubEnvironment
metadata:
  name: test-env-01
  namespace: acme-bank
spec:
  workbench: dispute-ops-dev
  
  # Environment designation
  purpose: testing
  
  # Resettable resources
  resources:
    data_stores:
      - ref: ganymede-test-db
        reset_on_test_run: true
        reset_script: migrations/test-reset.sql
    
    caches:
      - ref: callisto-test-cache
        flush_on_test_run: true
  
  # Test data seeding
  seed_data:
    enabled: true
    container:
      image: "registry.hub.acme.com/sub-001/test-data:latest"
      command: ["./seed-test-data.sh"]
```

---

## Test Types

### Scenario Integration Tests

Test complete Scenario flows via I/O Gateway:

```yaml
apiVersion: hub.olympus.io/v1
kind: Test
metadata:
  name: create-dispute-happy-path
spec:
  type: scenario_integration
  
  target:
    scenario: standard-dispute
    signal_type: dispute.submitted
  
  # ... (see test-crds.md for full spec)
```

### Standalone Tool Tests

Test Tools directly:

```yaml
apiVersion: hub.olympus.io/v1
kind: Test
metadata:
  name: eligibility-check-approved
spec:
  type: tool_invocation
  
  target:
    tool: check-eligibility
    operation: evaluate
  
  # ... (see test-crds.md for full spec)
```

---

## Test Dependencies and Ordering

### Test Suite Ordering

Tests within a suite execute in defined order:

```yaml
apiVersion: hub.olympus.io/v1
kind: TestSuite
metadata:
  name: dispute-full-flow
spec:
  # Ordered execution
  tests:
    - ref: create-dispute-test
      order: 1
    - ref: add-evidence-test
      order: 2
      depends_on: create-dispute-test  # Also waits for previous
    - ref: resolve-dispute-test
      order: 3
      depends_on: add-evidence-test
  
  # Failure handling
  on_failure: stop  # stop | continue | skip_dependent
```

### Recommendation

> **Best Practice:** Use Test Suites for any tests with execution dependencies. Individual tests should be independent when possible.

---

## Test Results

### Storage

Test results are stored by the Test Runner:

| Data | Retention |
|------|-----------|
| Test execution history | 90 days (configurable) |
| Detailed logs | 30 days (configurable) |
| Summary metrics | Indefinite |

### Report Format

```yaml
test_run:
  id: run-2026-01-06-001
  suite: dispute-full-flow
  workbench: dispute-ops-dev
  
  started_at: "2026-01-06T10:00:00Z"
  completed_at: "2026-01-06T10:02:45Z"
  duration_seconds: 165
  
  summary:
    total: 5
    passed: 4
    failed: 1
    skipped: 0
  
  tests:
    - name: create-dispute-test
      status: passed
      duration_ms: 1250
      
    - name: add-evidence-test
      status: passed
      duration_ms: 890
      
    - name: resolve-dispute-test
      status: failed
      duration_ms: 2100
      error:
        type: assertion_failed
        message: "Expected status 'RESOLVED', got 'PENDING'"
        assertion: response.status
        expected: RESOLVED
        actual: PENDING
```

---

## Console Views

The Test Runner provides dedicated console views:

| View | Audience | Content |
|------|----------|---------|
| **Test Suites** | Developer | List of test suites, last run status |
| **Test Run History** | Developer | Historical runs with drill-down |
| **Test Details** | Developer | Individual test results, logs |
| **Workbench Summary** | Admin | Aggregate test health per workbench |

---

## Machine and Tool Stubbing

> **Developer Responsibility:** The Test Runner does not provide built-in stubbing. Developers must:

| Approach | Description |
|----------|-------------|
| **Mock Implementations** | Create stub Machine/Tool instances |
| **Test Environment** | Configure test-specific instances |
| **Dedicated Workbench** | Use separate DEV workbench for testing |

### Example: Test Environment with Stubs

```yaml
# Test-specific tool instance pointing to mock
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: email-sender-test
  namespace: acme-bank
spec:
  definition_ref: email-sender
  
  environment: test-env-01
  
  # Mock endpoint
  endpoint:
    type: http
    url: https://mock-email.internal.acme.com/send
  
  # Test mode flag
  config:
    mode: mock
    capture_requests: true
```

---

## Enablement

Enabled by Tenant Admin per subscription/workbench:

```yaml
apiVersion: hub.olympus.io/v1
kind: TestRunnerConfig
metadata:
  name: test-runner-config
  namespace: acme-bank
spec:
  subscription:
    enabled: true
  
  workbenches:
    - name: dispute-ops-dev
      enabled: true
      dedicated_environment: test-env-01
      
    - name: dispute-ops-staging
      enabled: true
      dedicated_environment: test-env-staging
      
    - name: dispute-ops-prod
      enabled: false  # No testing in production
```

---

## Related Documentation

- [Test CRDs](./test-crds.md) — Test and TestSuite CRD specifications
- [Runtime CI](./runtime-ci.md) — Unit testing via Runtime CI
- [Signal Exchange](../signal-exchange/README.md) — I/O Gateway for test invocation


