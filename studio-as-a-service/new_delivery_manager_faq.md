# New Delivery Manager FAQ (Unanswered Questions)

A running list of questions that arose while reading the manual and are not fully answered within it. Intended for clarification with leadership or section owners.

## Requirements & RfP
- What is the expected cadence for RfP confirmation workshops on long‑running requirements (monthly vs per‑increment)? Who approves exceptions?
- How do we handle partial revalidation when only some Features under a Requirement are impacted by policy/architecture changes?
- Are there recommended templates/examples for a “good” Feature spec at RfP (beyond text) — e.g., minimal diagram, API sketch, data constraints?

## Integrations & Dependencies
- For providers that do not offer realistic sandboxes, what’s the expected minimum evidence before green‑lighting development (traffic shadowing vs simulators)?
- When dependency variance is caused by internal customer teams, which forum enforces accountability (Weekly vs Monthly vs Steering), and what are standard escalations?
- Do we have a sample “dependency financial ledger” layout and owner RACI?

## Quality & Test Governance
- What’s the minimum viable automation suite when starting a new subsystem (counts by layer)?
- How do we choose between quarantining flaky tests vs deleting and re‑writing? Is there a numeric rule beyond the flake threshold?
- When error budget is exhausted mid‑sprint, do we pause the sprint goal or renegotiate scope for the remaining days? Who decides?

## Debt & Refinements
- If debt reserve (15–25%) is repeatedly consumed due to unplanned work, what’s the default policy: increase reserve vs freeze intake vs escalate to Steering?
- How do we prioritize debt that is “low touch but high residual risk” vs “high touch but medium risk” beyond the narrative examples?

## Commercial (SFM/TCM)
- If a program starts as SFM but shifts to TCM mid‑year, is there a recommended transition checklist (dashboards, contract appendix updates, governance changes)?
- For TCM, what is the default grace period for idle‑time protections before standby charges apply? Can we publish example bands?
- In SFM, what constitutes sufficient evidence to classify exposure as “unfunded” when approvals exist “in principle” but no PO/CR id is issued?

## Operational Governance
- Is there a model calendar (sample invites) and suggested invitee list for each ritual that I can reuse?
- When two primary signals conflict (e.g., FVS healthy but RfP % low), which forum arbitrates and what’s the default decision rule?

## Human Contract & Exceptions
- For reversible experiments, how do we record rollback criteria concretely (numeric thresholds vs qualitative notes)?
- Are there recommended “lighter control” menus per gate that we can pick from during negotiations?

## Continuous Improvement
- What are examples of “practice change proposals” that were accepted vs rejected and why?
- How do we measure “adoption” for a governance change (beyond listing it on dashboards) — any standard KPIs?

## Tooling & Templates
- Where do we store redacted examples (decision paper, exception record, continuity pack) so new PMs can learn by sight?
- Do we have example Jira board configurations and JSON for automations to import, or is it all manual per program?
