# 7. FSOS Foundation Agents (System Intelligence Layer)
Foundation agents convert raw events, memories, and feature pipelines into authoritative household state vectors. They operate as continuously running daemons with strict SLAs, deterministic versioning, and explainability payloads so downstream agents can trust the derived insights.

## 7.1 Cashflow Foundation Agent

### 7.1.1 Inputs (Events, Balances, Obligations)
Consumes normalized transaction timelines, current balances, obligation calendars, direct debit mandates, external income feeds, and contextual signals (seasonality, employer schedules). Subscribes to feature-store updates for behavioural adjustments, including discretionary spend ratios and payment reliability.

### 7.1.2 Core Computations (Forecasts, Buffers, Gaps)
Produces rolling liquidity forecasts, buffer adequacy scores, deficit warnings, stress-test outcomes (e.g., loss of income, bill spikes), and categorizes flows into essential vs discretionary buckets. Applies policy rules for reserve targets per segment and can simulate interventions such as automatic sweeps or temporary credit line usage.

### 7.1.3 Exposed State and APIs for Other Agents
Publishes structured state vectors over IPC with metadata (timestamp, consent scope, model identifier, confidence). Provides APIs for retrieving forecast windows, buffer recommendations, anomaly explanations, and suggested actions (e.g., reschedule obligation, trigger surplus orchestration).

## 7.2 Goals Foundation Agent

### 7.2.1 Goal Modeling (Family and Individual)
Maintains canonical representations of multi-horizon goals (education, housing, caregiving, retirement, wealth transfer) with owner roles, funding sources, constraints, and dependencies on obligations or life events. Supports shared funding and cascading ownership (e.g., grandparents funding college).

### 7.2.2 Progress, Shortfall, and Conflict Analysis
Calculates funded ratios, projected shortfalls, contribution cadence adherence, and conflicts between goals vs obligations. It reconciles with cashflow forecasts to recommend reprioritization or reallocation strategies and flags when governance approvals are required to change goals.

### 7.2.3 Goal State APIs for Orchestrator and Think Agents
Exposes goal trees, dependency graphs, required tasks, and sensitivity analyses. Orchestrators request goal sub-flows (e.g., goal funding increase) while think agents fetch contextual narratives to explain advice in channels. All responses are scoped to consented members.

## 7.3 Risk & Family Health Foundation Agent

### 7.3.1 Liquidity, Stability, and Dependency Metrics
Derives liquidity coverage ratios, expense volatility, dependency ratios (number of dependents per income earner), insurance adequacy, credit utilization, and protection gaps using core memory, graph memory, and feature store signals.

### 7.3.2 Risk Posture Signals
Issues alert levels (normal, watch, intervention) with justification referencing data sources, policy thresholds, and historical trends. Integrates anomaly detections from guardrail services and behavioural analytics to surface potential fraud, elder abuse, or financial distress indicators.

### 7.3.3 Health Score APIs and Flags
Publishes health scores, flags, and recommended mitigations for governance, concierge, and RM dashboards. Includes evidence pointers (event IDs, documents, model outputs) so regulators and audit teams can trace derivations.

## 7.4 Household Engagement Insights Foundation Agent

### 7.4.1 Household & Member Engagement Metrics
Aggregates family-level KPIs such as obligation completion rates, goal progress velocity, concierge engagement, and member-specific adoption (e.g., teen card usage) while enforcing consent-based redaction. Supports cohort analysis by persona, jurisdiction, or segment.

### 7.4.2 Behavioral & Sentiment Telemetry
Derives behavioral signals (responsiveness to prompts, escalation frequency, RM interaction quality) and sentiment indicators from channel interactions or surveys. Normalizes data for comparability and flags when members deviate from typical patterns.

### 7.4.3 Feedback Loops into Agents & RM Dashboards
Feeds household metrics back into think/orchestrator agents to adapt nudges, task prioritization, or campaign eligibility. Publishes curated insights to RM dashboards, enabling targeted outreach and measurement of intervention efficacy. All outputs include lineage to underlying events for auditability.
