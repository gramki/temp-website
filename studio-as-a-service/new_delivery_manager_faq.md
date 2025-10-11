# New Delivery Manager FAQ (Unanswered Questions)

A running list of questions that arose while reading the manual and are not fully answered within it. Intended for clarification with leadership or section owners.

## Requirements & RfP
-- What is the expected cadence for RfP confirmation workshops on long‑running requirements (monthly vs per‑increment)? Who approves exceptions?
  - Answer: Run the RfP Readiness Workshop weekly by default and before each planning increment (Section 9.8). For long‑running requirements, add a monthly re‑affirmation checkpoint for items nearing shelf‑life. Exceptions to RfP gate criteria: DPO + Customer PM can approve minor clarifications in the workshop; policy/gate relaxations (process exceptions) require Steering approval per 9.10 and must be recorded as M.2 with a reversion date.
-- How do we handle partial revalidation when only some Features under a Requirement are impacted by policy/architecture changes?
  - Answer: Re‑affirm only the impacted Features. Keep the Requirement state unchanged; update shelf‑life and links for affected Features, add a brief RfP addendum (Appendix M.5) and tag with `RfP` + `integration-risk` if applicable.
-- Are there recommended templates/examples for a “good” Feature spec at RfP (beyond text) — e.g., minimal diagram, API sketch, data constraints?
  - Answer: Yes — use M.5 (RfP Design/Impact Addendum) and O.5 (worked example). Include: AC/NFR, subsystem boundary, latency/error budgets, a small Mermaid diagram (Appendix K), API sketch or schema, audit/log fields, integration readiness flags, and dependency notes.

## Integrations & Dependencies
-- For providers that do not offer realistic sandboxes, what’s the expected minimum evidence before green‑lighting development (traffic shadowing vs simulators)?
  - Answer: Minimum: contract specs pinned, simulators for happy/error paths, synthetic datasets, error taxonomy mapped, mTLS credentials provisioned in non‑prod, and (where possible) read‑only traffic shadowing on a small cohort. Set integration readiness flags to Yes/Yes/Yes before release (Section 5.10); otherwise, label `integration-risk` and block at gate.
-- When dependency variance is caused by internal customer teams, which forum enforces accountability (Weekly vs Monthly vs Steering), and what are standard escalations?
  - Answer: Weekly Health & Risk Review assigns owner/date and tracks evidence (9.4). If variance persists 2 cycles, escalate to Monthly (9.9) to secure commitments; unresolved funding/lead‑time requires Steering (9.10). Use the dependency register with Funding/Lead‑time fields and DependencyFunding% (8A).
-- Do we have a sample “dependency financial ledger” layout and owner RACI?
  - Answer: Use the ledger fields from 8A widgets and dependency register: Owner team/org, Funding status (CR/PO id), Lead‑time commitment (date/SLA), Contract/Access readiness (Y/N), and Dependency Financial Risk ($/day). RACI: Owner=Dependency team; Compiler=Delivery Manager; Validator=EO Commercial; Decider=Steering.

## Quality & Test Governance
-- What’s the minimum viable automation suite when starting a new subsystem (counts by layer)?
  - Answer: Defaults (tune per subsystem): Component 30–50 core business‑rule tests; Contract 10–20 per provider interface (success + common 4xx/5xx); Customer Service 4–8 journey paths (happy + critical errors); UI/E2E 2–4 smokes. Ensure critical path coverage ≥ 80% within first two sprints (Section 7.4/7.6).
-- How do we choose between quarantining flaky tests vs deleting and re‑writing? Is there a numeric rule beyond the flake threshold?
  - Answer: If a test fails ≥ 3 of the last 10 runs or contributes to flake > 2% (rolling 7 days), quarantine and fix within ≤ 2 sprints. Delete only if redundant or unfixable by design; replace with a more deterministic test before deletion. Track in a flake register and enforce repair SLAs (Section 7.6/7.8).
-- When error budget is exhausted mid‑sprint, do we pause the sprint goal or renegotiate scope for the remaining days? Who decides?
  - Answer: Pause net‑new intake and pivot the sprint to stabilization (Section 7). DM chairs a short decision huddle with EM, DPM, QA to adjust scope; if milestones or external dates are impacted, bring options to Steering (10).

## Debt & Refinements
-- If debt reserve (15–25%) is repeatedly consumed due to unplanned work, what’s the default policy: increase reserve vs freeze intake vs escalate to Steering?
  - Answer: Default ladder: (1) raise reserve to 20% next sprint; (2) freeze net‑new feature intake for one sprint to restore signals; (3) if accumulation > paydown for 2 cycles, escalate to Steering to authorize a stabilization window or additional capacity (Section 6.5/6.6).
-- How do we prioritize debt that is “low touch but high residual risk” vs “high touch but medium risk” beyond the narrative examples?
  - Answer: Use Reason×Impact plus Touch Frequency. Prioritize any item with High residual risk first; next, items that block multiple subsystems; then apply Touch‑Risk Index to schedule high‑touch areas. Low‑touch/high‑risk should be scheduled early even if switching cost is non‑trivial (Section 6.3/6.5).

## Commercial (SFM/TCM)
-- If a program starts as SFM but shifts to TCM mid‑year, is there a recommended transition checklist (dashboards, contract appendix updates, governance changes)?
  - Answer: Checklist: (a) Contract appendix updates (J.6, model name everywhere); (b) Dashboards: swap FVS widgets for Capacity Health (8B); (c) Governance: add idle‑time protections and Ready runway to Monthly; (d) Alerts: add TCM alerts (8B.3); (e) Communicate model change in Steering minutes and README.
-- For TCM, what is the default grace period for idle‑time protections before standby charges apply? Can we publish example bands?
  - Answer: Defaults (Appendix T): idle‑time grace up to 10 business days in a rolling 6‑week window; trigger protections when idle > 10% over 4 rolling weeks or dependency variance > threshold for 2 cycles. Bands are tunable per engagement and recorded in Appendix T.
-- In SFM, what constitutes sufficient evidence to classify exposure as “unfunded” when approvals exist “in principle” but no PO/CR id is issued?
  - Answer: “Approved in principle” without a PO/CR id is treated as unfunded. Evidence of funding = PO/CR id with amount or written budget line reference; otherwise include in Unfunded CR Exposure and freeze net‑new scope if exposure > 10% (8A.3/8A.4).

## Operational Governance
-- Is there a model calendar (sample invites) and suggested invitee list for each ritual that I can reuse?
  - Answer: Yes — Appendix E provides run‑books/agenda and participants per ritual. Copy the calendar notes in 9.1 and E.* templates; label chair and owning org on every invite.
-- When two primary signals conflict (e.g., FVS healthy but RfP % low), which forum arbitrates and what’s the default decision rule?
  - Answer: Weekly Review arbitrates first using gate precedence: planning requires RfP readiness regardless of funding health. If trade‑offs affect scope/date/capacity, escalate options to Monthly/Steering with a Decision Paper.

## Human Contract & Exceptions
-- For reversible experiments, how do we record rollback criteria concretely (numeric thresholds vs qualitative notes)?
  - Answer: Use numeric criteria where possible (e.g., pass rate ≥ 99%, error budget ≥ 20%, latency P95 < 150ms). Record rollback criteria and reversion date in M.2; attach an Evidence Pack with before/after signals (10.9/M.6).
-- Are there recommended “lighter control” menus per gate that we can pick from during negotiations?
  - Answer: Examples: RfP — contract‑first stub + design note addendum; Quality — reduced suite + replay pack and extended mini‑hardening; Commercial — time‑boxed CR deferral with freeze guardrail; Operations — temporary twice‑weekly risk review during spikes. Always include reversion date and owner.

## Continuous Improvement
-- What are examples of “practice change proposals” that were accepted vs rejected and why?
  - Answer: Accepted: pre‑merge component‑test gate on critical path — evidence showed 40% defect leakage reduction (M.6). Rejected: mandatory 100% E2E tests per story — evidence showed high flake and cycle time with no leakage improvement; replaced with stronger contract tests.
-- How do we measure “adoption” for a governance change (beyond listing it on dashboards) — any standard KPIs?
  - Answer: Use Appendix P KPIs: Adoption Rate (% reaching adopted ≤ 90 days), Time‑to‑Adoption, Decision Latency, Audit Remediation %, Version Currency. Also track “% forums run on time with required signals.”

## Tooling & Templates
-- Where do we store redacted examples (decision paper, exception record, continuity pack) so new PMs can learn by sight?
  - Answer: See Appendix O (Example Artifacts). Store alongside related Jira items and link from decision logs and dashboards (Appendix M usage notes).
-- Do we have example Jira board configurations and JSON for automations to import, or is it all manual per program?
  - Answer: Yes — Appendix L, section L.9 contains illustrative board JQL and Jira Automation JSON for RfP labeling, integration readiness guards, and exception reversion tasks. Start there and adapt to your instance/field IDs.
