# Appendix N — End‑to‑End Journey of a Requirement

Purpose: Show, in one place, how a realistic requirement progresses MAR → Decomposed → RfP → Planned → In Development → Done, including fields, labels, gates, dashboards, and forum handoffs.

## N.1 Scenario
- Requirement: "Reduce card fraud false‑positives by 20% while maintaining approval SLAs"
- Subsystems: Payments Authorization, Fraud/Risk, Notifications
- Constraints: PCI DSS; P95 auth < 150ms; no increase in checkout abandonment

## N.2 MAR (Minimally Acceptable Requirement)
- Fields: Intent, Boundaries, Dependencies, Constraints, Initial AC
- Labels: (none or `new-requirement`)
- Dashboards: %MAR (Appendix A); volatility baseline
- Forum: none yet; prepare for decomposition

## N.3 Decomposed
- Features identified (subsystem‑scoped):
  1) Authorization: risk signal on `/authorize`
  2) Fraud/Risk: risk‑based exemptions policy engine
  3) Notifications: step‑up comms and OTP fallback
- Labels: `decomposed`
- Dashboards: %Decomposed
- Forum: queue for RfP Readiness Workshop (Section 9.8)

## N.4 RfP (Ready‑for‑Planning)
- Evidence: feature definitions, AC/NFR, design/impact addenda, dependency map, Risk Surfaces
- Labels: `rfp-yes`, `features-pending-signoff` (until signed)
- Gates: Feature Decomposition Gates (Section 5.8)
- Forum: RfP Readiness Workshop → Customer sign‑off

## N.5 Planned
- Evidence: features mapped to epics/stories; sprint allocation
- Labels: `planned`, `design-complete`
- Dashboards: time‑in‑state; Ready coverage; dependency readiness
- Forums: Grooming (9.5); Sprint Planning (9.6)

## N.6 In Development
- Evidence: stories in progress; tests linked; traceability in Allure/Jira
- Labels: `in-development`, `partially-delivered` (as features accept)
- Dashboards: progress (% story points), feature acceptance rate, stagnation flags
- Forums: Daily Flow (9.3); Weekly Review (9.4); Debt Clearance (9.7); Sprint‑End (9.11)

## N.7 Done
- Evidence: all features accepted; release passes gates; dashboards green
- Labels: `done`, `delivered`
- Forums: Monthly Review/Steering (9.9/9.10) close‑out decisions

## N.8 Snapshots & Examples
- Fields (Requirement): Total/Completed Story Points; Progress%; RfP Signed Date; Affected Subsystems
- Labels (risk): `ac-missing`, `integration-risk`, `dependency-blocked`
- JQL (examples): see §5.12 "Sample Queries"
- Widgets: %RfP, shelf‑life, volatility; feature acceptance rate; progress bar; dependency variance

## N.9 Integration Readiness (if applicable)
- Checklist: Contracts; Testability; Non‑functionals; Security; Observability; Change Control; Failure modes; Idempotency/ordering (Section 5.10)
- Rule: Green‑to‑proceed required before Planned/In Dev; exceptions per Appendix M

## Cross‑references
- Section 5.3/5.7 (RfP & Hierarchy), 5.8 (Gates), 5.10 (Integrations)
- Section 9.8 (RfP Workshop), 9.5/9.6 (Grooming/Planning), 9.11 (Sprint‑End)
- Appendix L (Jira Schema), Appendix A/B (Dashboards/Alerts)
