# 6. Adaptive Refinements & Debt Management

## Purpose

This section is the governance framework for the costs of delivery trade‑offs. It treats refinements, shortcuts, and structural inefficiencies as visible, fundable artifacts — not failures — and provides a disciplined way to track, repay, and steer them without destabilizing delivery.

> VP Insight: "Speed is not free. The only question is whether you pay on purpose with a plan — or by surprise with interest."

---

## 6.1 Adaptive Refinements vs Rework

- Adaptive Refinement: Rework that arises from learning (new information discovered during build, user insight, integration reality). Not a scope change; not a defect. Managed within the feature’s intent, using buffers and refinement capacity.
- Rework (Defect/Misinterpretation): Corrections due to incorrect behavior vs acceptance criteria, or misread requirement intent. Tracked as defects and handled by quality governance.

How to decide quickly:
- Does the change preserve the original business intent? If yes → likely Adaptive Refinement.
- Did the behavior violate written AC or a known non‑functional? If yes → Rework/Defect.
- Did new facts emerge (integration, data shape, risk control)? If yes → Adaptive Refinement.

> Caution: Calling genuine defects “refinements” hides quality signals and undermines trust.

---

## 6.2 The Debt Spectrum & Classification

Use a simple, MECE scheme: classify by Reason Bucket (why the debt exists) and tag by Impact Domain (what it harms). This keeps ownership, prioritization, and remediation clear.

Reason Buckets (pick one):
1) Time Pressure — deadlines, risk‑containment, prototypes, phased delivery
2) Information & Volatility — ambiguity, discovery, late change, shifting constraints
3) Constraints — legacy coupling, external dependency limits, compliance/security mandates, provider/platform limits, budget caps
4) Capability & Process — skills/tooling gaps, manual ops, weak CI/CD, missing reviews

Impact Domains (multi‑select):
- Stability/Availability, Security/Privacy, Performance/Scale, Operability/Supportability, Compliance/Audit, Maintainability/Modularity, Financial/Cost

> From the Field: The same shortcut (manual failover) had a Capability & Process reason; its impact was Availability. Reason drove who funded; impact drove how urgent.

### 6.2.1 Classification Examples (Reason × Impact)

- Fraud check added in Checkout UI
  - Reason: Constraints (Fraud subsystem lead time/org boundary)
  - Impact: Security, Maintainability
  - Notes: Plan migration to Fraud subsystem; fund per origin.

- Skipped contract tests for provider due to deadline
  - Reason: Time Pressure
  - Impact: Stability/Availability, Operability
  - Notes: Add contract tests in next increment; alert until done.

- Shared table across Ledger and Settlements
  - Reason: Constraints (legacy coupling/shared database)
  - Impact: Maintainability, Compliance
  - Notes: Extract bounded contexts; phase data migration.

- Manual deploys, no rollback
  - Reason: Capability & Process
  - Impact: Operability/Supportability, Stability
  - Notes: Add CI/CD, blue‑green/feature flags; runbooks.

- Provider sandbox differs from prod (rate limits, schema)
  - Reason: Constraints (external dependency limits)
  - Impact: Stability/Availability, Performance
  - Notes: Chaos tests; client‑side rate budgeting; schema guards.

---

## 6.3 Debt Portfolio & Catch‑Up Plans

Maintain a single portfolio for visibility and funding decisions. Recommended fields:
- Title
- Reason Bucket (time pressure / information & volatility / constraints / capability & process)
- Impact Domains (stability, security, performance, operability, compliance, maintainability, financial)
- Subsystem (e.g., Payments Authorization, Ledger, Fraud, Checkout)
- Origin (who/why: date, decision link)
- Principal (estimated effort or cost to repay)
- Residual Risk (impact if unpaid: stability, security, scalability, regulatory)
- Touch Frequency (how often the area changes)
- Status (proposed, planned, in‑repayment, paused, done)
- Catch‑Up Plan (milestones, phasing, target dates)
- Funding Source (Studio capacity, Customer budget, shared)

Catch‑Up Plans (prefer amortization over “big‑bang”):
- Milestone 1: Remove critical risk (e.g., add tests/observability) — early win
- Milestone 2: Structural fix (e.g., boundary extraction)
- Milestone 3: Hardening (e.g., performance/scale, operability)

> Pro Tip: Tie catch‑up work to upcoming feature touches in the same subsystem. You lower switching cost and reduce re‑work risk.

Prioritization heuristics:
- High residual risk + high touch frequency = repay first
- Dependencies blocked across subsystems = accelerate
- Security/compliance exposure = escalate to Steering

---

## 6.4 Funding Responsibility & Commercial Treatment

Origin‑based funding clarifies accountability and prevents endless debates:
- Delivery Team–Induced Debt: Our shortcuts (e.g., skipped tests). Studio funds repayment from capacity unless agreed otherwise.
- Customer‑Induced Debt: Customer constraints (e.g., imposed tech, forced timeline cuts). Customer funds via CR or dedicated debt budget.
- Shared Trade‑offs: Jointly agreed expediency (e.g., deadline‑driven). Split funding per agreement; document decision and repayment plan at time of trade‑off.

Decision rules:
- Document the trade‑off at the moment it’s taken (who, why, payback plan).
- Cap new expediency per increment (e.g., 10% of effort) unless Steering approves.
- Reserve a stable capacity band (e.g., 10–20%) for debt repayment each sprint.

> Caution: Ambiguous funding kills accountability. If origin isn’t recorded, repayment never arrives.

---

## 6.5 Dashboarding Debt & KPIs

KPIs that leadership can steer:
- Debt Principal: Sum of estimated repayment effort
- Funded vs Unfunded: Principal with budget/capacity assigned vs not
- Amortization Rate: Principal repaid per sprint/month
- Accumulation vs Paydown: New debt principal created vs principal repaid (trend)
- Residual Exposure: Count of high‑risk items (security, availability, compliance)
- Debt Ratio: Debt principal / new feature effort (keep below an agreed band)

Alert examples (defaults):
- Accumulation > Paydown for 2 consecutive months → Re‑baseline proposal
- Residual high‑risk items > N (e.g., 5) → Steering escalation
- Debt Ratio > 0.3 for 2 sprints → Expand catch‑up capacity to 20%
- Unfunded principal > budgeted principal → Commercial review

> Why This Matters: Leaders manage trends, not one‑off numbers. You can’t steer what you can’t see.

---

## 6.6 Governance & Steering Review of Debt

Embed debt review in existing forums; label owning org and chair:
- Operational Review (Studio; Chair: Delivery Manager): Weekly
  - Inputs: Portfolio changes, hotspot subsystems, alert breaches
  - Outputs: Re‑prioritized catch‑up items, capacity allocation decisions
- Architecture Roundtable (Studio; Chair: Solution/Delivery Product Owner): Bi‑weekly
  - Inputs: Solution/architectural debt items, boundary/scale risks
  - Outputs: Technical decisions, sequencing, dependency handling
- Steering (EO; Chair: Engagement Owner): Monthly/Quarterly
  - Inputs: Debt KPIs (amortization, residual risk, funding), accumulation vs paydown
  - Outputs: Funding approvals, policy changes (caps/thresholds), re‑baseline decisions

Agenda (monthly Steering):
1) Trends (accumulation vs paydown, residual high‑risk)
2) Top 5 risks and catch‑up progress
3) Funding and capacity asks; policy thresholds
4) Decisions: approve, defer with rationale, or replace with stronger guardrails

> VP Insight: "Debt review is moral — it shows you’re not hiding your shortcuts and you’re paying back what you borrowed from the future."

---

## Practitioner Guidance (Use This in the Studio)

1) Name it immediately
- Every shortcut gets a debt entry with origin, principal, residual risk, and a payback sketch.

2) Prefer amortization
- Repay in phases, aligned to feature touches; avoid big‑bang “stabilization phases” unless urgent.

3) Guardrails, not heroics
- Keep a visible capacity band for debt (10–20%). Don’t raid it without explicit Steering approval.

4) Fund by origin
- Studio funds Studio‑induced debt; Customer funds Customer‑induced; shared trade‑offs are split at decision time.

5) Escalate on thresholds
- If accumulation > paydown or residual high‑risk grows, take it to Steering with options (expand capacity, defer features, re‑scope).

6) Instrument dashboards
- Track principal, amortization rate, residual exposure, and debt ratio per subsystem; alert on breaches.

7) Prevent silent growth
- Add a short “debt scan” in sprint review: what shortcuts did we take, did we log them, who owns payback?

### Optional Heuristic: Touch‑Risk Index — When and How to Use
- Purpose: Coarse prioritization to spot hot subsystems where frequent change meets high residual risk.
- When: Monthly or quarterly, during capacity allocation for catch‑up work; skip if dashboards already surface hotspots.
- How (numeric): For each subsystem, compute Index = Σ (Touches_i × ResidualRiskScore_i).
  - ResidualRiskScore: 1–5 (low→high)
  - Touches: count of changes in last N sprints (e.g., 4–6)
  - Normalize per sprint/team size if needed; start with alert threshold ≈12 and tune per program.
- Lightweight proxies if heavy: (a) High‑risk items touched ≥2 sprints in a row → flag; (b) Top 3 subsystems by touch count where any risk score ≥4 → review.
- Caveat: Not a KPI. Use to inform sequencing — not to score teams.

> From the Field: “Updating this monthly helped us move catch‑up capacity to the real hotspots and cut ‘surprise’ incidents in half over a quarter.”
