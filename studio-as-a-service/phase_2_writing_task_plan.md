# Phase 2 Writing Task Plan (Detailed)

Purpose: Break down each backlog item into concrete tasks with owners, inputs/outputs, dependencies, and acceptance criteria to execute Phase 2 efficiently.

Conventions
- Roles: VP Delivery (VPD), Section Owner (SO-2/5/6/7/8/9/L), Studio Council Member (SCM), Technical Writer/Editor (TW), Designer (DS).
- Estimates: S (≤0.5d), M (1–2d), L (3–5d). Adjust per context.
- DoD: Merged, cross-links added, checklist updated, glossary updated (if new terms), no linter issues.

---

## Section 2 — Context
1) Add TL;DR + rule summaries (2.1–2.7) [M]
- Owner: SO-2 (with VPD/TW)
- Inputs: the-studio-delivery-manual/2_Context.md
- Output: TL;DR (3–5 bullets) at top; “Rules we will operate by” (2–3 bullets) per sub-section
- Dependencies: None
- Acceptance: Skimmable bullets present; links to §9.13 and Appendix B

---

## Section 5 — Requirements & Evolution
2) Decomposition flow diagram (Mermaid) [S]
- Owner: DS (with SO-5)
- Inputs: §5.3/§5.7; gates language
- Output: Mermaid diagram embedded near §5.3 or §5.7
- Acceptance: Shows Requirement→(MAR)→Decomposed→(RfP)→Planned→In Dev and Feature→Epic→Story with Design/Impact & AC/NFR gates

3) Integration Readiness visual checklist (§5.10) [M]
- Owner: SO-5/TW
- Inputs: §5.10; Appendix A/B widgets
- Output: icon/table checklist + “Green to proceed” rule
- Acceptance: Linked from §5.10 and Appendix A/B

4) End-to-end requirement walkthrough [L]
- Owner: SO-5/TW
- Inputs: Appendix L (schema), Appendix A (dashboards), §5 states
- Output: New sub-section or appendix reference showing MAR→RfP→Planned→In Dev→Done with field/label/dashboard snapshots
- Acceptance: Links to §5.3/§5.7, Appendix L/A; one realistic BFSI example

---

## Section 6 — Adaptive Refinements & Debt
5) Sample portfolio row [S]
- Owner: SO-6/TW
- Inputs: §6 portfolio fields
- Output: One anonymized example row + brief annotation
- Acceptance: Reason×Impact demonstrated; referenced by Appendix A (Debt)

---

## Section 7 — Quality, Bugs & Defect Governance
6) Minimum viable quality signals strip [S]
- Owner: SO-7/TW
- Inputs: §7 metrics; Appendix A/B; Appendix T defaults
- Output: Starter set banner and targets
- Acceptance: Clear starter set; links to Appendix T for tuning

---

## Section 8 — Commercial (SFM/TCM)
7) SFM vs TCM crib sheet [M]
- Owner: SO-8/TW
- Inputs: §8A/§8B/§8C; Appendix J
- Output: One-page summary (table/list)
- Acceptance: “When to choose”, top risks, top widgets, key clauses; links to §8A/§8B/J

8) Model selection flow (Mermaid) [S]
- Owner: DS (with SO-8)
- Inputs: crib sheet
- Output: Simple decision flow
- Acceptance: Decision path to SFM/TCM with caveats

---

## Section 9 — Operational Governance
9) Delivery Manager quick start [M]
- Owner: SO-9/TW
- Inputs: Appendix E/H, §9.13, Appendix A/B
- Output: Compact “weekly rhythm + dashboards” subsection or appendix link
- Acceptance: Lists daily dashboards, weekly pack, primary signals; cross-links added

10) Elevate “Ritual → Primary signals” map [S]
- Owner: SO-9/TW
- Inputs: §9.13
- Output: Condensed map near top of §9; full detail remains in §9.13
- Acceptance: Present early; no duplication drift

---

## Appendix L — Jira Schema
11) Example board + automation JSON [M]
- Owner: SO-L/TW
- Inputs: L.5/L.6 current text
- Output: Illustrative board config + 2–3 automation rules (JSON/YAML), clearly marked as examples
- Acceptance: Linked to fields/dictionary and Appendix A

---

## Cross-section improvements
12) Evidence pack one-pager (template) [S]
- Owner: TW (with VPD)
- Inputs: §8/§9 templates, Appendix M
- Output: Template in Appendix M; links from §8, §9, §10
- Acceptance: Shows context, signals, options/impacts, recommendation, forum/date, owners

13) Operating defaults callout [S]
- Owner: VPD/TW
- Inputs: Appendix T and current thresholds
- Output: Defaults callout in §9 intro; link to Appendix T
- Acceptance: Defaults listed (quality/debt reserve, exception time-box, %RfP, Steering SLA, dependency/unfunded thresholds)

---

## New Appendices & Guides
14) Quick Start Guide (role-based) [M]
- Owner: VPD/TW (with SO-9)
- Inputs: roles_reference, Appendix E/G/H, §9.13
- Output: New guide with role cards (EO, Commercial, Account; Studio Owner, DM, DPO, DPM, EM, Tech Lead, QA Lead)
- Acceptance: Cards include first-week actions, dashboards, forums, SOPs/templates, top 3 signals, common escalations; linked from README and §9

15) Appendix — Example Artifacts [M]
- Owner: TW/SCM
- Inputs: examples from sections; redactions
- Output: New appendix with redacted examples (decision paper, exception record, continuity pack, dependency register export, RfP feature spec, evidence pack)
- Acceptance: Each artifact has “why this exists” + links to owning sections; cross-linked from §5/§8/§9/§10/M

16) Appendix — Studio Council Member Roles & Playbook [M]
- Owner: SCM (with VPD)
- Inputs: §11, Appendix H/T, §9 forums
- Output: New appendix (conception; incubation/pre-flight; infancy; steady-state; close-out), cadence, artifacts, versioning, adoption KPIs
- Acceptance: Cross-linked from §11; aligned with §9 forums; referenced in Appendix H/T

17) Appendix — End-to-End Journey of a Requirement [M]
- Owner: SO-5/TW
- Inputs: §5, Appendix L/A
- Output: New appendix walking MAR→Decomposed→RfP→Planned→In Dev→Done with fields/labels/AC/NFR/design-impact/dashboards/forum handoffs
- Acceptance: Cross-linked from §5.3/§5.7; references Appendix L/A

18) Appendix — Communication_Templates (Delivery Manager) [M]
- Owner: VPD/TW
- Inputs: §8/§9/§10, Appendix B/M, Appendix J
- Output: Scripts/templates for: exception request; integration not ready; error budget depleted; dependency variance; unfunded exposure; SFM scope trade-offs; TCM idle-time/standby; governance change continuity; risk surface clarification; RfP revalidation; gate failure before release
- Acceptance: Each template includes objective, 2–3 phrasing options, lighter-control suggestions; cross-links to §8/§9/§10, Appendix B/M

---

## Sequencing & Dependencies
- Recommended order: 9(quick start) → 5(diagram/checklist) → 7(signals) → 8(crib+flow) → 6(sample row) → L(examples) → cross-section templates → 2(TL;DR) → new appendices.
- Hard dependencies: §5 walkthrough depends on Appendix L/A clarity; communication templates depend on clause references in Appendix J and alert routes in Appendix B.

## Review & Acceptance
- Editorial pass by TW; sign-off by VPD; SCM updates checklist and audit references.
- DoD for each task as stated; add items to `writing_checklist.md` and check off on merge.
