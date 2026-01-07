# Hypothesis Records

> **Status:** 🔴 Stub — Placeholder for expansion

Hypothesis Records capture **learned patterns and insights from experience**—probabilistic beliefs that may eventually be promoted to Enterprise Knowledge. CAF provides the **catalog and schema** for hypothesis records; the records themselves are stored in **Enterprise Memory** (Semantic Memory layer).

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Capture organizational learning that is not yet asserted truth |
| **Nature** | Probabilistic, revisable, challengeable |
| **Lifecycle** | Draft → Active → Promoted/Rejected |
| **Promotion Path** | Hypothesis → Review → Enterprise Knowledge |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, review workflows, promotion governance |

---

## Why Hypothesis Records Matter

Without hypothesis records:
- Learnings stay locked in individual agents
- Patterns are rediscovered repeatedly
- No path from experience to institutional knowledge
- Cannot challenge or validate emerging beliefs

---

## Hypothesis Record Schema

```yaml
hypothesis_record:
  # Identity
  id: uuid                         # Unique identifier (UUID v4)
  created_at: datetime
  updated_at: datetime
  case_id: uuid                    # Universal binding ID (optional - hypotheses may span cases)
  
  # Hub Metadata (optional - populated when discovered within Hub context)
  hub_metadata:
    tenant_id: string              # Tenant identifier
    subscription_id: string        # Subscription within tenant
    workbench_id: string           # Workbench where hypothesis originated
    scenario_id: string            # Scenario from which hypothesis emerged (optional)
    request_id: string             # Request that triggered discovery (optional)
    parent_request_id: string      # Parent request if nested (optional)
  
  # The Hypothesis
  statement: text                  # Clear statement of the hypothesis
  domain: string                   # Domain this applies to (fraud, disputes, etc.)
  category: string                 # Type of hypothesis (pattern, rule, insight)
  
  # Scope
  scope:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.hypothesis-scope.v1+json"
      schema: string
      schema_version: string
    entity_types: array            # What entities this applies to
    segments: array                # Customer/merchant segments
    conditions: array              # When this hypothesis applies
    conditions_content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.hypothesis-condition.v1+json"
      schema: string
      schema_version: string
    time_range: object             # Temporal bounds (if any)
    geographic_scope: array        # Geographic applicability
  
  # Confidence & Evidence
  confidence:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.confidence-assessment.v1+json"
      schema: string
      schema_version: string
    score: number                  # 0-1 confidence level
    trend: enum                    # increasing | stable | decreasing
    last_validated: datetime       # When confidence was last assessed
    
  supporting_evidence:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.evidence-link.v1+json"
      schema: string
      schema_version: string
    items:
      - record_type: string        # Decision, Outcome, Override, etc.
        record_id: uuid            # → Any CAF record
        contribution: text         # How this supports the hypothesis
        strength: enum             # strong | moderate | weak
      
  counter_evidence:
    content_type:
      mime: string                 # Same schema as supporting_evidence
      schema: string
      schema_version: string
    items:
      - record_type: string
        record_id: uuid            # → Any CAF record
        challenge: text            # How this challenges the hypothesis
        strength: enum
  
  # Statistical Basis
  statistics:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.statistical-basis.v1+json"
      schema: string
      schema_version: string
    sample_size: integer           # Number of observations
    time_window: duration          # Over what period
    significance: number           # Statistical significance
    effect_size: number            # Magnitude of effect
  
  # Lifecycle
  status: enum                     # draft | active | under_review | promoted | rejected | deprecated
  status_history:
    - status: string
      timestamp: datetime
      changed_by: string
      reason: text
  
  # Review
  review_cadence: duration         # How often to review (e.g., 30d)
  next_review_date: datetime
  review_assignments:
    - reviewer: string
      role: string
      status: enum                 # pending | approved | rejected | abstained
      comments: text
  
  # Origin
  origin:
    discovered_by: string          # Agent/human who identified pattern
    discovery_method: enum         # automated_detection | manual_observation | analysis
    discovery_context: text        # How it was discovered
    
  # Actions
  recommended_actions:
    - action: text                 # What to do based on this hypothesis
      conditions: text             # When to apply
      risk_level: enum             # low | medium | high
  
  # Promotion
  promotion:
    eligible: boolean              # Whether ready for promotion
    promotion_criteria: array      # What would trigger promotion
    target_knowledge_type: string  # What it would become (policy, SOP, etc.)
    
  # Metadata
  tags: array
  linked_records: array
  supersedes: string               # Previous hypothesis this replaces
  superseded_by: string            # If deprecated, what replaced it
```

---

## Hypothesis Categories

| Category | Description | Example |
|----------|-------------|---------|
| **Pattern** | Observed behavioral pattern | "Merchant X has elevated chargeback rate" |
| **Correlation** | Relationship between factors | "Device mismatch + velocity → higher fraud" |
| **Rule Candidate** | Potential policy/rule | "Step-up auth for >$500 cross-border" |
| **Exception Pattern** | Common override scenario | "Currency conversion disputes usually approved" |
| **Process Insight** | Workflow improvement | "Earlier merchant contact reduces resolution time" |

---

## Lifecycle States

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYPOTHESIS LIFECYCLE                          │
│                                                                  │
│  ┌─────────┐    ┌─────────┐    ┌──────────────┐    ┌─────────┐ │
│  │  Draft  │───▶│  Active │───▶│ Under Review │───▶│Promoted │ │
│  └─────────┘    └─────────┘    └──────────────┘    └─────────┘ │
│       │              │                │                  │       │
│       │              │                │                  │       │
│       ▼              ▼                ▼                  ▼       │
│  ┌─────────┐    ┌─────────┐    ┌──────────────┐  ┌───────────┐ │
│  │Abandoned│    │Deprecated│    │   Rejected   │  │ Knowledge │ │
│  └─────────┘    └─────────┘    └──────────────┘  └───────────┘ │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Promotion Criteria

A hypothesis may be promoted to Enterprise Knowledge when:

| Criterion | Threshold |
|-----------|-----------|
| **Confidence Score** | > 0.9 |
| **Sample Size** | > N observations |
| **Time Validated** | > 90 days active |
| **Review Approval** | Required reviewers approved |
| **Counter-Evidence** | None significant |
| **Business Approval** | Domain owner sign-off |

---

## Anti-Patterns

| Anti-Pattern | Risk | Mitigation |
|--------------|------|------------|
| **Policy Laundering** | Hypothesis treated as rule without promotion | Require explicit promotion |
| **Stale Hypothesis** | Never reviewed, confidence decays | Enforce review cadence |
| **Confirmation Bias** | Only supporting evidence captured | Require counter-evidence search |
| **Overfitting** | Pattern too specific to generalize | Require scope validation |

---

## Related Documentation

- [CAF Overview](../README.md)
- [Episodic Memory Store](./README.md)
- [Decision Records](./decision-records.md)
- [Outcome Records](./outcome-records.md)
- [Enterprise Memory](../memory-services/hub-enterprise-memory.md)
- [Enterprise Knowledge](../knowledge-services/README.md)

---

*TODO: Detailed design — automated pattern detection, review workflow, promotion workflow, statistical validation*

