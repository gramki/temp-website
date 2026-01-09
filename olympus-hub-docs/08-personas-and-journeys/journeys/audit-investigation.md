# Journey: Audit Investigation

> **Status:** 🔴 Stub — Placeholder for expansion

This journey describes how an **Auditor** investigates decisions, reviews compliance, and generates audit reports using CAF and Memory Services.

---

## Overview

The **Audit Investigation** journey enables retrospective examination of decisions made within Hub operations — verifying compliance, understanding rationale, and generating evidence for regulatory requirements.

| Phase | Activities |
|-------|------------|
| **1. Scope Definition** | Define investigation parameters |
| **2. Decision Discovery** | Query CAF for relevant decisions |
| **3. Evidence Examination** | Review evidence bundles |
| **4. Explanation Generation** | Generate human-readable explanations |
| **5. Reporting** | Compile findings and recommendations |

---

## Phase 1: Scope Definition

### Activities

1. **Define Time Range**
   - Start and end dates
   - Specific periods of interest

2. **Define Criteria**
   - Scenario types
   - Decision categories
   - Agents involved
   - Outcome types

3. **Set Investigation Goals**
   - Compliance verification
   - Pattern detection
   - Incident investigation
   - Regulatory response

---

## Phase 2: Decision Discovery

### Actor: CAF (Cognitive Audit Fabric)

### Activities

1. **Query Decision Catalog**
   - Filter by criteria
   - Retrieve decision records from Enterprise Memory

2. **Identify Patterns**
   - Group by category
   - Detect anomalies
   - Track trends

### Query Example

```yaml
investigation_query:
  time_range:
    start: "2025-12-01"
    end: "2025-12-31"
  
  filters:
    scenario_ids: ["payment-dispute-filed"]
    decision_types: ["final-resolution"]
    outcomes: ["rejected"]
  
  aggregations:
    - field: "agent_id"
      type: "count"
    - field: "decision_rationale"
      type: "terms"
```

---

## Phase 3: Evidence Examination

### Activities

1. **Retrieve Evidence Bundles**
   - Access supporting documents
   - Review context snapshots
   - Examine tool invocation records

2. **Verify Completeness**
   - Check required evidence captured
   - Verify evidence integrity

3. **Cross-Reference**
   - Link decisions to requests
   - Track decision chains

---

## Phase 4: Explanation Generation

### Actor: CAF Explanation Service

### Activities

1. **Generate Explanations**
   - Human-readable decision narratives
   - Factor contribution analysis
   - Counterfactual explanations

2. **Produce Lineage**
   - Decision dependency graphs
   - Input-to-output traces

### Explanation Types

| Type | Purpose |
|------|---------|
| **Narrative** | Human-readable story |
| **Factored** | Contribution breakdown |
| **Counterfactual** | "What if" analysis |
| **Contrastive** | "Why X not Y" |

---

## Phase 5: Reporting

### Activities

1. **Compile Findings**
   - Summarize investigation results
   - Document exceptions
   - Identify systemic issues

2. **Generate Reports**
   - Compliance reports
   - Exception reports
   - Trend analysis

3. **Recommend Actions**
   - SOP updates
   - Training needs
   - Process improvements

---

## CAF Capabilities Used

| Capability | Usage |
|------------|-------|
| **Decision Catalog** | Query and filter decisions |
| **Evidence Access** | Retrieve evidence bundles |
| **Explanation Service** | Generate explanations |
| **Policy Validation** | Verify compliance |

---

## Related Documentation

- [Auditor Persona](../personas/auditor.md)
- [Cognitive Audit Fabric](../../04-subsystems/cognitive-audit-fabric/README.md)
- [Enterprise Memory](../../04-subsystems/memory-services/enterprise-memory/README.md)
- [Decision Records](../../04-subsystems/cognitive-audit-fabric/episodic-memory-store/decision-records.md)

---

*TODO: Query patterns, report templates, integration workflows*

