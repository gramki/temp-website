# COS Need: Behavioral Monitoring and Drift Detection

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [COS Role Definition](../cos.md) | [Roles Overview](../roles.md#6-cognitive-operations-steward-cos)

---

## Overview

The **Cognitive Operations Steward (COS)** ([role definition](../roles.md#6-cognitive-operations-steward-cos)) is responsible for maintaining the **day-to-day cognitive health** of agents. Unlike ARE who monitors system health (latency, errors, cost), COS monitors **thinking health** (quality, consistency, drift).

This document details the behavioral monitoring and drift detection needs for platform developers building COS capabilities.

---

## The COS Monitoring Model

### What COS Monitors

| Category | ARE Monitors | COS Monitors |
|----------|--------------|--------------|
| **Health** | System health | Cognitive health |
| **Failures** | Crashes, timeouts | Wrong decisions, confusion |
| **Quality** | Latency, throughput | Reasoning quality |
| **Changes** | Configuration drift | Behavioral drift |
| **Users** | Availability | Satisfaction, trust |

### Why This Matters

An agent can be:
- **Operationally healthy** (ARE sees green dashboards)
- **Cognitively unhealthy** (COS sees degrading reasoning)

Example: An agent with 99.9% uptime and fast response times that consistently gives subtly wrong answers is an ARE success and COS failure.

---

## Behavioral Monitoring Needs

### 1. Decision Quality Monitoring

COS needs to assess whether agent decisions are **correct, consistent, and appropriate**.

#### Quality Dimensions

| Dimension | Question | Measurement |
|-----------|----------|-------------|
| **Accuracy** | Is the decision correct? | Validation against ground truth |
| **Consistency** | Same input → same output? | Variance analysis |
| **Appropriateness** | Is the decision suitable for context? | Context-decision alignment |
| **Confidence Calibration** | Does confidence match accuracy? | Confidence vs. outcome analysis |
| **Coherence** | Does reasoning flow logically? | Reasoning chain analysis |

#### Platform Requirements

COS needs:
- **Decision Sampling** — Random sample of decisions for review
- **Validation Queue** — Decisions flagged for human validation
- **Quality Scoring** — Automated quality metrics
- **Quality Trends** — Track quality over time

### 2. Reasoning Trace Analysis

COS needs visibility into **how agents think**, not just what they decide.

#### Trace Analysis Needs

| Analysis Type | Purpose | Example |
|---------------|---------|---------|
| **Step Analysis** | Understand reasoning flow | "Why did it take 15 steps?" |
| **Decision Points** | Identify where choices are made | "What alternatives were considered?" |
| **Context Usage** | How context influences reasoning | "Did it use all relevant context?" |
| **Tool Selection** | Why specific tools were chosen | "Why calculator for text task?" |
| **Confidence Evolution** | How confidence changes through reasoning | "Why did confidence drop mid-task?" |

#### Platform Requirements

COS needs:
- **Trace Viewer** — Visualize reasoning steps
- **Reasoning Annotator** — Add notes to reasoning traces
- **Pattern Detector** — Identify reasoning patterns
- **Trace Comparison** — Compare traces across similar tasks

### 3. User Signal Monitoring

COS monitors signals from users interacting with agents.

#### User Signals

| Signal | Meaning | COS Response |
|--------|---------|--------------|
| **Override** | User rejected agent decision | Investigate decision quality |
| **Escalation** | Agent couldn't handle task | Check scope alignment |
| **Rework** | Output needed correction | Check accuracy |
| **Abandonment** | User gave up | Check usability |
| **Positive Feedback** | User satisfied | Note for patterns |
| **Negative Feedback** | User frustrated | Investigate cause |

#### Platform Requirements

COS needs:
- **User Signal Dashboard** — Aggregate user signals per agent
- **Signal Trends** — Track signals over time
- **Signal Drill-down** — See specific interactions behind signals
- **Signal-to-Trace Linking** — Connect signals to reasoning traces

---

## Drift Detection Needs

### What is Drift?

**Drift** is gradual, unintended change in agent behavior over time. It's dangerous because:
- Changes are small, so they're not caught as errors
- Changes accumulate, creating significant deviation
- By the time drift is noticed, the agent is far from intended behavior

### Types of Drift

| Drift Type | Cause | Detection Method |
|------------|-------|------------------|
| **Prompt Drift** | Accumulated prompt changes | Version comparison |
| **Knowledge Drift** | Underlying data changed | Knowledge source monitoring |
| **Model Drift** | LLM behavior changed | Behavioral baseline comparison |
| **Context Drift** | Agent's world model became stale | Context freshness tracking |
| **Population Drift** | Input distribution changed | Input analysis |

### Drift Detection Methods

#### Baseline Comparison

COS compares current behavior to established baselines:

```
Baseline (established)     Current (observed)
─────────────────────     ──────────────────
Response time: 2.5s       Response time: 2.8s  ← Within tolerance
Approval rate: 85%        Approval rate: 72%   ← DRIFT ALERT
Confidence: 0.8           Confidence: 0.7      ← DRIFT ALERT
Step count: 5-8           Step count: 8-12     ← DRIFT ALERT
```

#### Statistical Anomaly Detection

COS uses statistical methods to detect unusual patterns:

| Method | Use Case |
|--------|----------|
| **Z-score** | Detect outliers in continuous metrics |
| **Chi-square** | Detect distribution changes in categorical data |
| **CUSUM** | Detect gradual shifts over time |
| **Isolation Forest** | Detect multi-dimensional anomalies |

#### Platform Requirements

COS needs:
- **Baseline Manager** — Define, store, and update baselines
- **Drift Alerting** — Automatic alerts when drift detected
- **Drift Severity** — Classify drift as minor, moderate, severe
- **Drift Diagnosis** — Tools to investigate drift causes

### Drift Response

When drift is detected, COS must:

1. **Classify the drift** — What type? How severe?
2. **Identify the cause** — What changed?
3. **Assess impact** — Who is affected?
4. **Route appropriately** — Who should fix it?

| Drift Type | Route To | Action Expected |
|------------|----------|-----------------|
| Prompt drift | AE | Review prompt changes |
| Knowledge drift | KMO | Update knowledge |
| Model drift | ARE | Investigate model version |
| Context drift | KMO | Refresh context |
| Intent drift | APO | Review agent charter |

---

## Confusion Detection

### What is Confusion?

**Confusion** occurs when an agent doesn't understand its situation. Unlike drift (gradual), confusion is **episodic** — it happens on specific tasks.

### Confusion Signals

| Signal | Example | Severity |
|--------|---------|----------|
| **Wrong tool selection** | Calculator for text analysis | Medium |
| **Misunderstood context** | Treating question as command | High |
| **Circular reasoning** | Going in loops | High |
| **Inappropriate confidence** | High confidence on unclear input | Medium |
| **Context blindness** | Ignoring relevant context | High |
| **Goal wandering** | Pursuing wrong objective | Critical |

### Confusion Detection Methods

| Method | Detection |
|--------|-----------|
| **Loop Detection** | Repeated reasoning steps |
| **Tool Mismatch** | Tool doesn't match task type |
| **Confidence Mismatch** | High confidence + low accuracy |
| **Context Ignore** | Available context not used |
| **Goal Drift** | Intermediate goals diverge from final goal |

### Platform Requirements

COS needs:
- **Confusion Alerting** — Real-time confusion detection
- **Confusion Classification** — Categorize confusion type
- **Confusion Context** — Full context when confusion occurs
- **Confusion Patterns** — Identify recurring confusion scenarios

---

## Pattern Detection for Enterprise Learning

### COS Role in Enterprise Learning

COS plays a critical role in detecting patterns worth promoting to enterprise knowledge:

```
Agent interactions
       ↓
COS detects recurring pattern
       ↓
COS validates pattern is stable (not noise)
       ↓
COS flags to KMO with evidence
       ↓
KMO evaluates for promotion
       ↓
If promoted, COS verifies effect
```

### Patterns COS Detects

| Pattern Type | Example | Promotion Target |
|--------------|---------|------------------|
| **Recurring decisions** | Same conclusion across agents | Semantic memory |
| **Stable corrections** | Consistent user overrides | Knowledge update |
| **Emergent best practices** | High-quality reasoning patterns | SOP candidate |
| **Cross-agent learning** | One agent's success helps others | Shared memory |
| **Knowledge gaps** | Repeated failures in same area | Knowledge request |

### Detection Criteria

Before flagging to KMO, COS validates:

| Criterion | Threshold |
|-----------|-----------|
| **Frequency** | Pattern seen 3+ times |
| **Consistency** | Same result 80%+ of times |
| **Stability** | Pattern stable over 7+ days |
| **Value** | Positive impact on outcomes |

### Platform Requirements

COS needs:
- **Pattern Detection Engine** — Automated pattern recognition
- **Pattern Evidence Collector** — Gather supporting evidence
- **KMO Handoff** — Structured handoff to KMO
- **Promotion Verification** — Check if promotion had intended effect

---

## Issue Routing

### COS as Router

COS doesn't fix issues — COS **finds** and **routes** them. This requires:

1. **Detection** — Find the issue
2. **Classification** — Understand what kind of issue
3. **Routing** — Send to the right owner
4. **Tracking** — Monitor resolution

### Routing Matrix

| Issue Type | Symptoms | Route To | Expected Response |
|------------|----------|----------|-------------------|
| **Intent misalignment** | Agent pursuing wrong goals | APO | Clarify charter |
| **Design flaw** | Reasoning pattern broken | CSA | Revise design |
| **Implementation bug** | Code/prompt error | AE | Fix implementation |
| **System reliability** | Operational issues | ARE | Investigate |
| **Compliance concern** | Policy violations | ARAO | Assess risk |
| **Knowledge issue** | Wrong information | KMO | Update knowledge |

### Platform Requirements

COS needs:
- **Issue Queue** — All detected issues in one view
- **Smart Classification** — AI-assisted issue classification
- **One-Click Routing** — Easy handoff to owners
- **Resolution Tracking** — Monitor through resolution
- **Closed-Loop Feedback** — Confirm issue was resolved

---

## OPDA Requirements Summary

| OPDA Dimension | COS Need |
|----------------|----------|
| **Observable** | Full visibility into agent reasoning and behavior |
| **Predictable** | Baselines and drift detection enable prediction |
| **Directable** | COS can route issues and trigger interventions |
| **Authority Enforceable** | COS monitors policy adherence |

---

## Desk Support

These needs are supported through the **Cognitive Health Desk**:

| Console | Capabilities |
|---------|--------------|
| **Behavior Console** | Quality dashboard, user signals, baseline comparisons |
| **Patterns Console** | Drift alerts, anomaly feed, pattern candidates |
| **Issues Console** | Issue queue, classification, routing |

See [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md) for detailed specifications.

---

## Anti-Patterns

| Pattern | Why It's Problematic |
|---------|---------------------|
| "Metrics are green, so it's fine" | Operational metrics miss cognitive issues |
| "That's an edge case" | Edge cases reveal deeper problems |
| "Users will adapt" | Users shouldn't work around agent flaws |
| "We'll catch it in the next release" | Drift compounds if unaddressed |
| "Not my job to fix it" | COS routes, doesn't ignore |

---

## Success Criteria

COS behavioral monitoring needs are met when:

- [ ] Decision quality metrics are available per agent
- [ ] Reasoning traces are accessible and analyzable
- [ ] User signals are tracked and trended
- [ ] Baselines are established and maintained
- [ ] Drift is detected automatically
- [ ] Confusion is detected in real-time
- [ ] Patterns are flagged to KMO with evidence
- [ ] Issues are routed to the right owners
- [ ] Resolution is tracked through closure

---

*End of document*
