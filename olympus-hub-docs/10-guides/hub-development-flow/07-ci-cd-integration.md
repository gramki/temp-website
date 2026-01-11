# CI/CD Integration

[← Previous: Collaboration Patterns](./06-collaboration-patterns.md) | [Back to Index](./README.md) | [Next: Merits →](./08-merits.md)

---

## Overview

Hub provides integrated CI/CD capabilities through two main components:

| Component | Purpose |
|-----------|---------|
| **Runtime CI** | Build and unit test Hub Applications |
| **Hub Test Runner** | Integration testing of Scenarios |

---

## How CI/CD Fits in Hub

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CI/CD IN HUB                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEVELOPMENT                                                                │
│   ┌──────────┐     ┌──────────────────────────────────────────────────┐     │
│   │          │     │                RUNTIME CI                        │     │
│   │  Source  │────▶│  ┌─────────┐  ┌─────────┐  ┌─────────────────┐  │     │
│   │  Code    │     │  │ Build   │─▶│ Unit    │─▶│ Push to         │  │     │
│   │          │     │  │         │  │ Test    │  │ Snapshot Reg.   │  │     │
│   └──────────┘     │  └─────────┘  └─────────┘  └─────────────────┘  │     │
│                    └──────────────────────────────────────────────────┘     │
│                                         │                                    │
│                                         ▼                                    │
│   TESTING                                                                    │
│   ┌──────────────────────────────────────────────────────────────────────┐  │
│   │                    HUB TEST RUNNER                                    │  │
│   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                   │  │
│   │  │ Test CRDs   │─▶│ Execute via │─▶│ Assertions  │                   │  │
│   │  │             │  │ I/O Gateway │  │ & Reports   │                   │  │
│   │  └─────────────┘  └─────────────┘  └─────────────┘                   │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
│                                         │                                    │
│                                         ▼                                    │
│   DEPLOYMENT                                                                 │
│   ┌──────────────────────────────────────────────────────────────────────┐  │
│   │                    PROMOTION                                          │  │
│   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                   │  │
│   │  │ Request     │─▶│ Approve     │─▶│ Deploy to   │                   │  │
│   │  │ Promotion   │  │             │  │ PROD        │                   │  │
│   │  └─────────────┘  └─────────────┘  └─────────────┘                   │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Runtime CI

### What It Does

Runtime CI is provided by each Hub Application Runtime:

| Runtime | Build Tool | Test Framework |
|---------|------------|----------------|
| **Atlantis** | Maven/Gradle | JUnit |
| **Rhea** | Rhea Builder | Rhea Test |
| **Seer** | pip/poetry | pytest |
| **Perseus** | Perseus Builder | Perseus Tests |

### Triggering a Build

**Via hub CLI (in remote workspace):**
```bash
hub build application dispute-handler
hub get build dispute-handler --watch
```

**Via Developer Console:**
```
Applications → [Your App] → Build → Trigger
```

**Automatic triggers (if configured):**
- On Git push to application source
- On schedule (e.g., nightly)
- On dependency update

### Build Output

```
Build Result:
├── Container image: dispute-handler:1.2.3-beta.1+abc123
├── Build logs: Available in CI console
├── Unit test results: 45 passed, 0 failed
└── Pushed to: Snapshot Registry
```

### Viewing Build Status

```
Developer Console → Applications → dispute-handler → Builds

BUILD HISTORY:
┌─────────┬─────────────────────┬────────┬───────────┬────────────┐
│ Build # │ Version             │ Status │ Tests     │ Duration   │
├─────────┼─────────────────────┼────────┼───────────┼────────────┤
│ 42      │ 1.2.3-beta.1+abc123 │ ✅     │ 45/45     │ 3m 22s     │
│ 41      │ 1.2.2+def456        │ ✅     │ 45/45     │ 3m 18s     │
│ 40      │ 1.2.2-alpha+ghi789  │ ❌     │ 43/45     │ 2m 55s     │
└─────────┴─────────────────────┴────────┴───────────┴────────────┘
```

---

## Hub Test Runner

### What It Does

The Test Runner executes integration tests against your Scenarios:

| Aspect | Description |
|--------|-------------|
| **Scope** | Workbench-level integration tests |
| **Mechanism** | Invokes Scenarios via I/O Gateway |
| **Assertions** | Response validation, request update checks |
| **Results** | Stored and reportable |

### Defining Tests

```yaml
# scenarios/standard-dispute/tests/create-dispute.yaml

apiVersion: hub.olympus.io/v1
kind: Test
metadata:
  name: create-dispute-happy-path
spec:
  type: scenario_integration
  
  target:
    scenario: standard-dispute
    signal_type: dispute.submitted
  
  request:
    payload:
      customer_id: "TEST-001"
      amount: 500.00
      dispute_type: "unauthorized"
  
  expectations:
    response:
      status_code: 200
      body:
        - path: "$.request_id"
          exists: true
        - path: "$.status"
          equals: "CREATED"
```

### Creating Test Suites

```yaml
# scenarios/standard-dispute/tests/suite.yaml

apiVersion: hub.olympus.io/v1
kind: TestSuite
metadata:
  name: dispute-full-flow
spec:
  display_name: "Dispute Full Flow"
  
  tests:
    - ref: create-dispute-happy-path
      order: 1
    - ref: add-evidence
      order: 2
      depends_on: create-dispute-happy-path
    - ref: resolve-dispute
      order: 3
      depends_on: add-evidence
  
  execution:
    on_failure: stop
```

### Running Tests

**Via hub CLI (in remote workspace):**
```bash
# Validate scenario (optional, before committing)
hub validate scenario standard-dispute

# Commit changes (GitOps requirement)
git add .
git commit -m "feat: update scenario"
git push

# Run test suite
hub test suite dispute-full-flow
```

**Via Developer Console:**
```
Test Runner → Suites → dispute-full-flow → Run
```

**Viewing Results:**
```
TEST RUN RESULTS:

Suite: dispute-full-flow
Status: ✅ Passed
Duration: 12.3 seconds

Tests:
┌──────────────────────────┬────────┬──────────┐
│ Test                     │ Status │ Duration │
├──────────────────────────┼────────┼──────────┤
│ create-dispute-happy-path│ ✅     │ 1.2s     │
│ add-evidence             │ ✅     │ 0.9s     │
│ resolve-dispute          │ ✅     │ 2.1s     │
└──────────────────────────┴────────┴──────────┘
```

---

## CI/CD Workflow

### Recommended Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RECOMMENDED CI/CD WORKFLOW                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. CODE CHANGE                                                             │
│      └── Developer edits code/CRDs                                          │
│                                                                              │
│   2. COMMIT TO GIT (GitOps requirement)                                     │
│      └── git add . && git commit && git push                               │
│      └── All hub commands read from committed Git files                     │
│                                                                              │
│   3. BUILD (if code changes)                                                 │
│      └── Runtime CI builds and unit tests                                   │
│      └── ❌ Fail? → Fix and retry                                           │
│                                                                              │
│   4. SYNC TO DEV                                                             │
│      └── Developer syncs scenario from Git to DEV workbench               │
│      └── hub sync scenario <name> (reads from Git)                          │
│                                                                              │
│   5. INTEGRATION TEST                                                        │
│      └── Hub Test Runner executes tests                                     │
│      └── ❌ Fail? → Fix and retry                                           │
│                                                                              │
│   6. REQUEST PROMOTION                                                       │
│      └── Developer requests promotion to STAGING/PROD                       │
│                                                                              │
│   7. APPROVAL                                                                │
│      └── Admin reviews and approves                                         │
│      └── ❌ Rejected? → Address feedback                                    │
│                                                                              │
│   8. DEPLOYMENT                                                              │
│      └── Artifacts promoted to target                                       │
│      └── Migrations executed (if any)                                       │
│                                                                              │
│   9. VERIFICATION                                                            │
│      └── Smoke tests in target environment (optional)                       │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Differences from Traditional CI/CD

| Traditional CI/CD | Hub CI/CD |
|-------------------|-----------|
| Pipeline defined in YAML (Jenkins, GitHub Actions) | Built into platform |
| Deploys to environments via scripts | Promotion is the deployment |
| Environment-specific configs managed separately | Workbenches contain configs |
| Branch triggers pipeline | Promotion request triggers deployment |
| Pipeline approvals are add-ons | Approvals are first-class |

---

## Integration with External Tools

### Build Logs → Olympus Watch

```
All CI logs stream to Olympus Watch:
├── Searchable
├── Correlated with other logs
└── Retained per policy
```

### Notifications

```yaml
# CI/CD notifications via Notification Services

Events:
├── Build started
├── Build completed (success/failure)
├── Test run completed
├── Promotion requested
├── Promotion approved/rejected
└── Deployment completed
```

---

## Best Practices

### Testing

| Practice | Recommendation |
|----------|----------------|
| **Coverage** | At least one integration test per Scenario |
| **Independence** | Tests should be independent (reset state) |
| **Speed** | Keep tests fast (< 30 seconds each) |
| **Clarity** | Clear test names and failure messages |

### Build Management

| Practice | Recommendation |
|----------|----------------|
| **Version tags** | Use semantic versioning |
| **Build on commit** | Trigger builds on source changes |
| **Clean builds** | Don't rely on cached state |
| **Review failures** | Investigate all build failures |

---

## Summary

| Component | Purpose | When to Use |
|-----------|---------|-------------|
| **Runtime CI** | Build and unit test | Code changes |
| **Test Runner** | Integration test | Before promotion |
| **Promotion** | Deployment | Moving to STAGING/PROD |

---

## Related Documentation

- [CLI Channels for Developers](../../06-ux-architecture/tenant-domain/cli-channels-for-developers.md) — Full CLI command reference
- [Hub CLI Setup](../hub-cli-setup.md) — Installation guide

---

[← Previous: Collaboration Patterns](./06-collaboration-patterns.md) | [Back to Index](./README.md) | [Next: Merits →](./08-merits.md)

