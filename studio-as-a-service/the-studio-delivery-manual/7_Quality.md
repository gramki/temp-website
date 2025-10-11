# 7. Quality, Bugs & Defect Governance

## Purpose

This section defines how the Studio governs quality: set realistic expectations, connect requirements to tests, manage leakage, invest in the right automations, run with SLOs and error budgets, and make quality visible to the right forums.

> VP Reflection: "Zero bugs is a slogan. Bounded risk with discipline is a delivery commitment."

### Minimum Viable Quality Signals (Defaults)
- Release Gate Snapshot: P0/P1 open = 0; P2s triaged with mitigation and target release
- Critical Path Test Pass Rate: ≥ 99% per build on main
- Defect Leakage (last release): ≤ N P1/P2 per 100 story points delivered (primary); optionally also track customer‑impact rate ≤ 1 P1 per 10k txns (txn = critical‑path business transactions, e.g., payment authorization attempts)
- Flake Rate: ≤ 2% (rolling 7 days)
- Critical Path Automation Coverage: ≥ 80%
- Pipeline Stability (main): ≥ 95% green; quarantined tests repaired or removed within ≤ 2 sprints
- Integration Readiness Flags (in‑scope Features): Contracts/Credentials/Environments = Yes/Yes/Yes
- Quality Error Budgets Remaining: ≥ 20% (defect, leakage, flake budgets)
- Customer Acceptance: Signed for scope included in the release

Note: Tune thresholds per program in Appendix T; map to dashboards in Appendix A; enforce via readiness gates in 7.1 and budgets in 7.6.

### Definitions (Shared Language)
- Defect: Any variance from expected behavior (AC/NFR) — can be due to code, config, data, environment, integration, or missing/ambiguous AC.
- Bug: A code‑caused defect (implementation error). Every bug is a defect; not every defect is a bug.
- Leakage: Defects escaping internal stages into UAT/production.
- Acceptance Criteria (AC): Verifiable behaviors that define “done.”
- Non‑Functional Requirements (NFR): Performance, security, availability, operability, etc.
- SLI/SLO/Error Budget: Measured indicator / target commitment / allowable error margin (1 − SLO) that gates feature releases.
- Flake Rate: Percentage of tests that fail intermittently for non‑product reasons.
- Readiness Gate: Pass/fail release criteria (e.g., P0/P1=0 in scope, leakage ≤ threshold, error budget ≥ Y%).
- Severity (P0–P5): Impact tiers for triage/SLA
  - P0 (Critical outage): Defect detected in production that caused a SEV‑0/SEV‑1 outage and cannot be recovered without fixing the Defect (no viable workaround). Immediate rollback/fix; release blocked.
  - P1 (High impact): Major function broken with significant user/business impact. Workaround may exist but is unacceptable for release. Hotfix in current/next window.
  - P2 (Medium impact): Function degraded or edge case fails; acceptable workaround available. Fix in next planned release.
  - P3 (Low impact functional): Minor functional defect with negligible business impact; acceptable workaround available. Schedule in maintenance backlog (next 1–2 releases) or batch with related work.
  - P4 (Cosmetic/Trivial): UI text/layout issues, minor log noise, non‑blocking polish. Fix opportunistically; no hard SLA.
  - P5 (Informational): Observation/clarification/suggestion or known limitation; no expectation that it be fixed. Track for awareness or convert to debt/enhancement if later prioritized.
- Root Cause: Primary cause category (AC gap, test gap, data/env gap, code bug, integration drift).
- Risk Surface(s): A documented category of behavior, scenario, or environment that is expressly excluded from current scope or insufficiently specified for commitment. Risk Surfaces shall be listed for each Requirement or maintained in a program‑level register and reviewed at RfP; items not listed are treated as in‑scope by default.
- Traceability: Links Requirement → AC → Tests → Defects (via IDs in Jira/Allure).

---

## 7.1 Realistic Expectations: Bug‑Free vs “Ready”

- Bug‑free (absolute) is not credible for evolving enterprise systems. “Ready for release” means known risks are within agreed bounds and gates pass.
- Readiness Gate (example):
  - No open P0/P1 defects in scope
  - Known P2s triaged with mitigation and target release
  - Leakage in last release ≤ agreed threshold (e.g., ≤ X P1 per 1k txns)
  - Error budget remaining ≥ Y% for critical services

> Caution: Don’t signal “done” without naming residual risks. Ambiguity here breaks trust post‑release.

---

## 7.2 Traceability: Defects ↔ Acceptance Criteria (AC)

- Every defect must trace to: (a) missed/ambiguous AC or NFR; or (b) a risk surface declared out‑of‑scope.
- Working rules:
  - Defect ticket includes: originating story/requirement link, AC/NFR reference (or risk note), environment, reproduction steps, evidence.
  - Create/adjust AC for newly discovered scenarios to prevent “orphan” bugs.
  - Keep AC in the requirement source (Jira/Doc) and mirror in tests via IDs.

> Why This Matters: Unconnected bugs fuel blame cycles and hide process gaps.

---

## 7.3 Bug Leakage & Root Causes

- Leakage Taxonomy:
  - Internal: caught in dev/QA/UAT
  - External: discovered in production or by customers
- Root‑Cause Review (lightweight, within 48h for P1/P2):
  - Was AC missing/ambiguous? Was automation absent/flaky? Was data/setup unrealistic?
  - Produce one preventative action (add AC, add contract test, fix pipeline flake, add synthetic data).

> From the Field: “A leaked edge‑case once cost us a month of credibility. Linking it to a missing AC and adding a contract test won back trust.”

---

## 7.4 Automation Strategy & Realistic Coverage

- Prioritize by risk and frequency, not quotas.
  - Automate: critical revenue paths, high‑frequency flows, brittle integrations.
  - Manual/Exploratory: rare edge cases, UX nuance, first‑time risky areas (until stabilized).
- Test Pyramid (what to automate where):
  - Contract/Component (broad base): provider contracts, domain components — fast, many, run on every change
  - Customer Service (middle): logical journey APIs a customer invokes end‑to‑end — may span multiple services; moderate count, run on CI and before release
  - UI/E2E (tip): smoke + happy paths only — few, deterministic, run per release/critical changes
- Component Tests = Module‑Level Tests
  - Purpose: verify the business logic of a single module (subsystem boundary) independently, with neighboring modules/services stubbed or mocked
  - Execution: we run automated module‑level suites in the cluster certification environment to validate real runtime configs (secrets, service mesh, policies) before broader integration
- Signals (when to add/remove automation):
  - Flake Rate: > 2–3% sustained → fix or delete tests; block merges on chronic flake
  - Failure/Leakage Trends: rising external leakage → add contract/customer‑service tests on affected paths
  - Critical Path Coverage: gaps on top revenue/risk flows → add tests before new feature work
  - MTTR for Flaky Tests: > 3 days median → assign ownership, repair window

> Pro Tip: Start with the 20–30% of flows that cover ~80% of use; expand as leakage trends demand.

---

## 7.5 Allure TestOps Integration & Coverage

- Objectives:
  - Single pane for manual + automated tests; link tests ↔ requirements/stories ↔ defects
  - Report coverage by feature and critical path
- Integration Pattern:
  - CI (Jenkins) posts test results to Allure TestOps; tests reference requirement IDs/AC IDs
  - Manual test cases authored in Allure; scheduled and recorded alongside automated runs
  - Dashboards per subsystem show pass/fail, flake, coverage by criticality
- Useful Views:
  - Coverage by Feature/Subsystem and by Criticality
  - Flaky Test Leaderboard with MTTR for fixes
  - Traceability report: Requirement → AC → Tests → Defects

> Reference: Use Allure TestOps docs for CI adapters and traceability mapping.

---

## 7.6 Quality KPIs, SLIs, SLOs & Error Budgets

- SLIs (quality/test governance examples):
  - Critical Path Test Pass Rate (% per build)
  - Defect Leakage Rate (per release window, severity‑segmented)
  - Flake Rate (% of tests failing intermittently)
  - MTTR for P1/P2 Defects (time to remediate)
  - MTTD for P1/P2 Defects (time to detect)
  - Automation Coverage for Critical Paths (%)
  - Change Failure Rate (prod incidents/regressions per release)
  - Pipeline Stability (% green runs on main; quarantine count)

- SLOs (commitments — tune per program):
  - Critical Path Pass Rate ≥ 99% per build on main
  - Leakage ≤ N P1/P2 per 100 story points delivered (primary); also monitor customer‑impact rate ≤ 1 P1 per 10k txns (secondary)
  - Flake Rate ≤ 2% (rolling 7 days)
  - P1 MTTR ≤ 4 hours during support window; P2 MTTR ≤ 2 business days
  - Automation Coverage for Critical Paths ≥ 80%
  - Pipeline Stability ≥ 95% green for last 7 days; flaky tests repaired or quarantined ≤ 2 sprints

- Error Budgets (quality):
  - Defect Budget: allowed P1/P2 counts per release; when exhausted → stabilization focus
  - Leakage Budget: allowed leaked defect rate; when exhausted → pause features until mitigations land
  - Flake Budget: allowed flake rate; when exceeded → dedicated repair window
  - Coverage Budget (critical paths): allowed shortfall vs target; when exceeded → add tests before new features

- Quality KPIs (reporting set):
  - Defect Density by module, Leakage Rate, MTTR/MTTD trends, Flake Rate trend, Critical Path Coverage, Pipeline Stability, Change Failure Rate
  - Leakage per 100 story points (primary), Leakage per 10k txns (secondary/customer impact)

> Caution: Don’t weaponize metrics. Use them to trigger the right conversation and trade‑offs.

---

## 7.7 Dashboards & Alerts (Quality)

Audience Views:
- Steering (EO): release readiness, leakage trend, error budget remaining, top risks
- Program (Studio Owner/Delivery Manager): defect aging, flake rate, coverage of critical paths, risk gates
- Team (Squads/QA): today’s failing tests, flaky tests, defect triage board

Core Widgets:
- Release Readiness: P0/P1 open, leakage vs threshold, error budget remaining
- Critical Path Coverage: % of automated tests for top flows
- Flake & Failure Trends: last 14/30 days
- Defect Aging: P1/P2 by aging buckets

Alerts (defaults):
- Any P0/P1 in release scope → block release
- Leakage above threshold in last release → raise Steering agenda
- Error budget < 20% remaining → pause features, focus on stabilization
- Flake rate > 5% week‑over‑week → mandate repair window

---

## 7.8 Contractual Clauses for Quality (Guidance)

- Release Readiness. The Parties agree that a release may proceed only when the following readiness criteria are satisfied for the scope of the release: (i) no open P0 or P1 Defects remain; (ii) known P2 Defects are documented with accepted mitigations and target remediation release; (iii) the measured Defect Leakage for the prior release is at or below the agreed threshold; and (iv) the Quality Error Budgets defined in this Agreement (including Leakage and Flake Budgets) remain above the agreed minimums.

- Defect Triage and Remediation SLAs. The Delivery Team shall triage newly reported Defects within [X] hours during the support window. Production P0 Defects shall be remediated immediately by rollback or hotfix; P1 Defects shall be remediated within [Y] hours; P2 Defects shall be remediated in the next planned release unless otherwise agreed in writing; P3–P5 Defects shall be scheduled per the maintenance backlog. These SLAs are suspended when Quality Error Budgets are exhausted, in which case stabilization activities shall take precedence over new feature delivery.

- Error Budgets and Feature Pauses. The Parties agree to maintain Quality Error Budgets for (a) Defect Leakage, (b) Test Flake Rate, and (c) Critical Path Coverage. If any Quality Error Budget is exhausted, the Parties shall pause new feature releases for the affected scope and prioritize stabilization, test repair, and defect remediation until the budget is restored above the agreed threshold.

- Traceability and Acceptance Criteria. The Customer shall provide or approve Acceptance Criteria (functional and non‑functional) for each Requirement in scope. The Delivery Team shall maintain traceability between Requirements, Acceptance Criteria, Tests, and Defects. A Defect is deemed valid if and only if it violates approved Acceptance Criteria or agreed Non‑Functional Requirements for the in‑scope environment and does not fall within a listed Risk Surface.

- Risk Surfaces Register. The Parties shall maintain a written register of Risk Surfaces associated with the scope of work (either per Requirement or as a consolidated annex). Risk Surfaces not listed in the register shall be deemed in‑scope for quality commitments. Defects arising solely within listed Risk Surfaces shall not constitute grounds for rejection of a deliverable and may be tracked as informational, enhancement, or debt items. The register shall be reviewed at each RfP gate and prior to release.

- Test Data and Environments. The Customer shall provide, or enable the Delivery Team to provision, suitable non‑production environments and test data with sufficient fidelity (including masking policies) to execute the agreed test suites. Where third‑party environments or data are required, the Customer shall secure access and credentials or provide written waivers for any untestable scenarios.

- Exclusions and Dependencies. The Delivery Team shall not be held responsible for failures caused by (i) third‑party systems outside its operational control, (ii) ambiguous or unstable Requirements not approved by the Customer, (iii) Customer‑managed environments or configuration changes, or (iv) data issues originating from Customer or third‑party sources, except where the Parties have agreed mitigation responsibilities in writing.

- Acceptance of Deliverables. A deliverable shall be deemed accepted when (i) it passes the agreed Readiness Gate, (ii) all Acceptance Criteria for the scope are met, and (iii) the agreed test suites (manual and automated) have passed in the designated environment(s). Any failure shall be documented with specific Acceptance Criteria or test references; the Delivery Team shall remedy failures per the SLA above.

- Management of Flaky Tests. Tests identified as flaky (intermittent failures without product changes) shall not be used as a basis for rejection of a deliverable. The Delivery Team shall quarantine or repair flaky tests within [N] business days and maintain a public register of quarantined tests and planned repair dates.

- Change Freeze and Gate Enforcement. Within [T] business days prior to a scheduled release, changes to scope or Acceptance Criteria shall require written approval and may trigger re‑execution of the Readiness Gate. The Parties agree that gate failures block release until remedied or waived by Steering in writing.

- Integration Interfaces. For integrations covered by this Agreement, the Parties shall maintain documented interface contracts (schemas, error codes, idempotency, rate limits). Material changes to such contracts require prior notice and a mutually agreed validation window; defects arising from unannounced breaking changes are excluded from Delivery Team responsibility.

> Pro Tip: Use error budgets, readiness gates, and traceability as the backbone of contractual language — they convert quality intent into measurable, enforceable commitments.

---

## Practitioner Guidance (Quality Play)

1) Align on “Ready,” not “Perfect”
- Share the readiness gate early; rehearse it before release.

2) Trace everything
- Map Requirement → AC → Tests → Defects in Allure/Jira; reject defects without origin.

3) Invest where it pays
- Automate critical paths first; reduce flake; measure ROI via leakage reduction.

4) Run with budgets
- Publish SLOs and error budgets; pause features when budgets are exhausted.

5) Make risk visible
- Keep dashboards simple; show trends; avoid vanity metrics.

> VP Insight: "Our credibility went up when we paused features on budget exhaustion. We shipped fewer surprises and gained permission to move faster later."
