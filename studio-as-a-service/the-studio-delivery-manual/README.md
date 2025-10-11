# The Studio Delivery Manual

## What this is
This is a practical operating system for enterprise delivery. It connects requirements discipline (MAR → RfP), quality and gates, debt portfolio, commercial models (SFM/TCM), operational governance, and the human contract into one coherent system. It is written from a Studio VP of Delivery perspective and anchored in BFSI (Payments/Card Issuer) examples.

## How to use this manual
- Start with Section 4 (Principles) to internalize the guardrails.
- Fix your weakest link first: Requirements (5), Quality (7), Debt (6), Commercial (8), Operations (9), Human Contract (10).
- Use the appendices as plug‑and‑play tools (dashboards, SOPs, templates, contracts, thresholds).
- Steward changes via Section 11 (SCM, continuous improvement) and Appendix T (tuning thresholds).

## Documentation style guide
- Voice & tone: clear, explanatory Google developer‑docs style; VP‑coach voice. Avoid hype; prefer evidence and examples.
- Terminology: use Delivery/Customer vocabulary consistently. Align roles/orgs with `studio-as-a-service/roles_reference.md`.
- Wisdom layers: weave callouts where they help comprehension:
  - VP Insight — leadership rationale
  - From the Field — concise, concrete experience
  - Pro Tip — tactical guidance
  - Caution — traps/anti‑patterns
  - Why This Matters — business linkage
- Practitioner triad (only for Customer–Delivery interaction topics): Ideal State, Likely Reality, Delivery Team Survival Guide.
- Examples: ground in BFSI (Payments/Card Issuer). Prefer subsystem‑scoped Features, measurable AC/NFR, realistic constraints.
- Diagrams: Mermaid. Label forum ownership (EO vs Studio). Keep under ~30 nodes; add notes/links.
- Metrics: prefer few, strong signals. Tie every alert to an owner/forum.

## Authoring workflow (for updates or new sections)
1) Blueprint first
   - Draft a short blueprint with: purpose, audience, promised outcomes, section outline, wisdom anchors, cross‑references.
   - Review and align before writing.
2) Build a detailed checklist
   - Translate the blueprint into an itemized checklist in `studio-as-a-service/writing_checklist.md`.
   - Include deliverables, wisdom elements, governance/ownership labels, dashboards/alerts, and quality gates.
3) Write section by section with the agent
   - Implement the section content; keep examples specific and subsystem‑scoped; add callouts and cross‑links.
   - Validate role/org consistency, terminology, and forum ownership.
4) Review each section thoroughly
   - Verify against the checklist; add/remove items to reflect reality.
   - Run a content pass for: realism, BFSI anchoring, governance alignment, dashboards/alerts, contract language.
5) Wire governance and contracts
   - Add signals/thresholds in dashboards (Appendix A/B), SOPs/ritual templates (Appendix E/G), clauses (Appendix J), and thresholds (Appendix T) as needed.
6) Close with validation gates
   - Check phase gates and wisdom‑layer counts at the end of each major pass.

## Conventions & tooling
- Tools: Grafana & Jira; TestOps: Allure; CI: Jenkins; Environments: dev → staging → UAT → prod.
- Jira schema: Appendix L (issue types, workflows, labels, automations, dashboards, data dictionary).
- Governance forums: Section 9; label owning org and chair (EO vs Studio) on every invite.

## Change control for this manual
- Propose changes with the one‑pager in Section 11 (Practice Change Proposal); the SCM curates approvals/versioning.
- Version tags (e.g., v1.0) and release notes are maintained by the SCM; thresholds live in Appendix T.
