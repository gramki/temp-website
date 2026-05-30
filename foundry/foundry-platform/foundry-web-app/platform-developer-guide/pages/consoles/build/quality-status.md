# Quality Status Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/quality-status`

**Group:** Build

**Purpose:** Test results, coverage, and automation health — current state of quality.

---

## Page Sections

### 1. Quality Summary

| Metric | Description |
|--------|-------------|
| **Test pass rate** | % of tests passing |
| **Test coverage** | Code coverage % |
| **Automation rate** | % of test cases automated |
| **Flaky tests** | Tests with inconsistent results |
| **Last run** | Most recent test execution |

### 2. Test Results Overview

| Element | Description |
|---------|-------------|
| **Pass/Fail/Skip** | Aggregate counts |
| **Trend chart** | Pass rate over time |
| **By component** | Results per System/Capability |
| **By test type** | Unit, integration, E2E |

### 3. Test Run History

| Column | Description |
|--------|-------------|
| Run ID | Identifier |
| Triggered by | CI, manual, scheduled |
| Timestamp | When it ran |
| Pass/Fail/Skip | Counts |
| Duration | How long |
| Coverage | If measured |

### 4. Failed Tests Detail

| Element | Description |
|---------|-------------|
| **Test name** | Which test failed |
| **Failure reason** | Error message/stack |
| **Last passed** | When it last succeeded |
| **Flaky?** | Intermittent failure flag |
| **Linked PI** | Related Product Intent |
| **Actions** | View in TestRail, rerun |

### 5. Coverage Report

| Element | Description |
|---------|-------------|
| **Overall coverage** | Aggregate % |
| **By repository** | Per-repo coverage |
| **By component** | Per-System coverage |
| **Uncovered areas** | Files/functions with low coverage |

---

## Filters

- By component (System, Capability)
- By test type (unit, integration, E2E)
- By status (passed, failed, flaky)
- By date range
- By repository

---

## Integrations

- **TestRail** — Test case definitions, results sync
- **Quality automation repo** — Automation code
- **CI Console** — Test runs from pipelines
- **Quality Service** — Unified access wrapper

---

## Related Consoles

- **CI Console** — Build/test pipelines
- **Findings Console** — Code quality findings
- **Quality Controls** — Governance quality controls and thresholds
- **Release Artifacts** — Quality gates for release
