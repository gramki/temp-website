# Open Points — CI Subsystem

## Overview

This document tracks unresolved questions and pending decisions for the CI Subsystem.

**Last Updated:** 2026-01-06

---

## Resolved

*No items resolved yet.*

---

## Under Discussion

### Runtime CI

- [ ] **Admin Override for Defaults**
  - **Context:** Should admins be able to override system-provided CI defaults?
  - **Current state:** Future feature
  - **Blocking:** Advanced CI customization

- [ ] **Build Caching**
  - **Context:** How to handle build caching for faster builds?
  - **Options:**
    1. Layer caching in container builds
    2. Dependency caching per runtime
    3. Full artifact caching
  - **Blocking:** Build performance optimization

### Test Runner

- [ ] **Test Result Impact on Promotion**
  - **Context:** Should test failures block promotion?
  - **Options:**
    1. Mandatory pass for promotion
    2. Advisory only (can override)
    3. Configurable per promotion path
  - **Blocking:** Promotion workflow integration

- [ ] **Parallel Test Execution**
  - **Context:** Support for parallel test execution within a suite?
  - **Current state:** Sequential only
  - **Blocking:** Large test suite performance

- [ ] **Test Data Isolation**
  - **Context:** How to ensure test isolation when multiple tests run?
  - **Options:**
    1. Transaction rollback
    2. Unique test data per run
    3. Environment cloning
  - **Blocking:** Test reliability

### Test CRDs

- [ ] **Assertion DSL**
  - **Context:** Finalize assertion syntax and operators
  - **Blocking:** Test authoring

- [ ] **Async Test Patterns**
  - **Context:** How to test long-running scenarios with multiple updates?
  - **Blocking:** Complex scenario testing

---

## Deferred

### CI Features

- [ ] **CLI Tool for Test Execution**
  - **Reason:** Post-initial release
  - **Deferred until:** Developer tooling phase

- [ ] **Test Coverage Reporting**
  - **Reason:** Requires tracing integration
  - **Deferred until:** Observability enhancement phase

- [ ] **Visual Test Editor**
  - **Reason:** UI investment
  - **Deferred until:** UX enhancement phase

### Integrations

- [ ] **IDE Integration**
  - **Reason:** Post-GA feature
  - **Deferred until:** Developer experience phase

- [ ] **Slack/Teams Notifications for CI**
  - **Reason:** Notification Services scope
  - **Deferred until:** Notification enhancement phase

---

## Out of Scope

- **Infrastructure Testing** — Managed by Olympus Weave
- **Security Scanning** — Separate security tooling
- **Performance Testing** — Separate performance testing subsystem (future)


