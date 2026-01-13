# Session Notes: Request Sentinel Type Implementation

**Date**: 2026-01-14  
**Focus**: Implement third Sentinel type (`request`) for AI agents to observe/participate in other agents' requests

---

## Objective

Add a third Sentinel type to the Seer Sentinels subsystem. Unlike Realtime and Analytical Sentinels that generate Observations/Exceptions via Cronus, Request Sentinels operate as Employed Agents within a Workbench, observing/participating in requests through the Hub Request model.

---

## Work Completed

### Phase 1: CRD Definitions (3 new files)

Created three new SentinelScenarioSpec CRD documentation files:

| File | Description |
|------|-------------|
| `sentinel-scenario-normative-spec.md` | Extends Hub ScenarioNormativeSpec (no additions) |
| `sentinel-scenario-automation-spec.md` | Extends with `sentinel` section: participation mode, filters, OPA policy |
| `sentinel-scenario-deployment-spec.md` | Extends with `sentinel_deployment` section: limits, notification delivery |

### Phase 2: Sentinel Subsystem Updates (4 files)

Updated core Seer Sentinels documentation:

| File | Changes |
|------|---------|
| `sentinel-spec-manager.md` | Added `request` type, Request Sentinel specification section, type-specific validation |
| `sentinel-directory.md` | Added Request Sentinel registry entry structure, new indexes (by Trained Agent, Scenario, Participation Mode) |
| `sentinel-operators.md` | Added Request Sentinel registration flow, Hub Operators coordination, state transitions |
| `sentinel-levers.md` | Added Request Sentinel controls (enrollment enable/disable, suspend, archive) |

### Phase 3: Hub Integration Documentation (3 files)

Created and updated Hub integration documentation:

| File | Changes |
|------|---------|
| `hub-integration/sentinel-scenario-processing.md` | NEW: How Hub Operators process SentinelScenarioSpec CRDs |
| `signal-exchange/README.md` | Added "Request Sentinel Auto-Enrollment" section |
| `request-management/request-hierarchy.md` | Added "Request Sentinel Child Requests" section |

### Phase 4: Main Documentation Updates (3 files)

Updated main Agent Session Sentinel documentation:

| File | Changes |
|------|---------|
| `README.md` | Updated to "Three Sentinel Types", added architecture diagram with Request Sentinel |
| `SCOPE.md` | Updated scope description, added SentinelScenarioSpec documents to coverage |
| `agent-session-supervision.md` | Added "Why Request Sentinels" and "Request Sentinel Use Cases" sections |

### Phase 5: Decision Logs (2 new ADRs)

Created architecture decision records:

| ADR | Title |
|-----|-------|
| `0116-request-sentinel-type.md` | Decision to introduce Request Sentinel type with rationale and alternatives |
| `0117-sentinel-scenario-spec-crds.md` | Decision for three-CRD extension pattern |

### Phase 6: Example (1 new file)

Created complete example:

| File | Description |
|------|-------------|
| `examples/request-sentinel-example.md` | Token Usage Governance sentinel with all spec types, webhook examples, flow diagrams |

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Three separate SentinelScenarioSpec CRD types | Extend corresponding Hub ScenarioSpec types cleanly |
| Trained Agent reference chain preserved | `SentinelScenarioAutomationSpec` → `HubApplicationSpec` → `seerTrainingRef` |
| Sentinel filters in isolated `sentinel` section | Clean separation from standard Scenario fields |
| Child request created on enrollment | Immediate association with Sentinel's scenario |
| Asynchronous webhook delivery, no acknowledgment | Aligns with existing Notification Service patterns |

---

## Files Created (7 new files)

| File Path | Type |
|-----------|------|
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-scenario-normative-spec.md` | New |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-scenario-automation-spec.md` | New |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-scenario-deployment-spec.md` | New |
| `olympus-seer-docs/seer-design/hub-integration/sentinel-scenario-processing.md` | New |
| `olympus-hub-docs/decision-logs/0116-request-sentinel-type.md` | New |
| `olympus-hub-docs/decision-logs/0117-sentinel-scenario-spec-crds.md` | New |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/examples/request-sentinel-example.md` | New |

*Note: The examples directory was also created.*

## Files Modified

| File Path | Changes |
|-----------|---------|
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-spec-manager.md` | Added Request Sentinel type |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-directory.md` | Added Request Sentinel fields/indexes |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-operators.md` | Added Request Sentinel flows |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-levers.md` | Added Request Sentinel controls |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/README.md` | Updated to three types |
| `olympus-seer-docs/seer-design/subsystems/seer-sentinels/SCOPE.md` | Updated scope and coverage |
| `olympus-seer-docs/seer-design/implementation-concepts/agent-session-supervision.md` | Added Why/Use Cases sections |
| `olympus-hub-docs/04-subsystems/signal-exchange/README.md` | Added auto-enrollment section |
| `olympus-hub-docs/04-subsystems/request-management/request-hierarchy.md` | Added sentinel child requests |

---

## Request Sentinel Use Cases Documented

1. **Token Usage Governance** — Monitor and intervene when budgets exceeded
2. **Compliance Monitoring** — Sample decisions, verify evidence, create remediation tasks
3. **Quality Assurance Sampling** — Score outputs, flag outliers, create training data
4. **Fraud Pattern Detection** — Correlate across requests, escalate patterns
5. **Escalation Pattern Analysis** — Categorize escalations, identify training gaps
6. **Cross-Request Correlation** — Link related requests, notify agents, flag conflicts

---

## Architecture Summary

```
Sentinel Types:
├── Realtime Sentinel → Observe SX events → OPA → Cronus Observations
├── Analytical Sentinel → Query Analytics → SQL → Cronus Observations  
└── Request Sentinel → Enroll in Requests → Employed Agent → Child Requests
```

Request Sentinels differ fundamentally:
- Output is child requests and agent actions (not Cronus Observations)
- Operate as Employed Agents within Workbench
- Use Hub Request model (context inheritance, lifecycle cascade)
- Enable AI-to-AI oversight pattern

---

## Related Documentation

- [Seer Sentinels README](../olympus-seer-docs/seer-design/subsystems/seer-sentinels/README.md)
- [ADR-0116: Request Sentinel Type](../olympus-hub-docs/decision-logs/0116-request-sentinel-type.md)
- [ADR-0117: SentinelScenarioSpec CRD Structure](../olympus-hub-docs/decision-logs/0117-sentinel-scenario-spec-crds.md)

---

*Session completed with all phases implemented.*
