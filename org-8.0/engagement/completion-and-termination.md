# Engagement Completion and Termination

[← Back to Guide](README.md)

---

## Successful Completion

An Engagement completes successfully when the assembled product is in production, the customer is operating per the agreed model, and all deliverables have been handed over. This corresponds to the final stages of the [Lifecycle](lifecycle.md) — Transfer and Complete.

The completion process:

- Post-go-live stabilization — resolve remaining defects or transition issues; EPM drives adoption tracking and value delivery assessment (Engagement Success)
- Verification Squad wind-down — AVA confirms the verification module handover is complete; Verification Squad engineers rotate back to Product Line Squads or other Engagements
- Functional squad release per plan — CP and Studio squad members released; rotation back to PL Squads documented
- Knowledge capture — Engagement retrospective, decision log, archetype update proposals, pattern extraction submitted to PAC Practice Mode
- Inner source repatriation — Engagement-specific work that proved reusable is contributed back to Product Lines
- Engagement formally closed; final status communicated to ERC and Client Partner

---

## Early Termination

When an Engagement must be terminated before completion:

- Controlled wind-down process led by EPM and EO
- Handover of any artifacts produced to date
- Verification Squad wind-down — AVA preserves the verification module (environment definitions, test suites, test data tooling) for potential future use or reference
- Knowledge capture for what was learned
- Squad release with documented learnings

---

## Scope Reduction

When scope must be reduced mid-Engagement:

- EPM manages scope change process
- EA adjusts architecture and archetype application
- AVA adjusts verification module scope — updates acceptance criteria, test suites, and environment definitions to match the reduced scope
- EPO communicates changed requirements to squads

---

## Handover Artifacts

| Artifact | Owner |
|----------|-------|
| Verification module (test suites, environment definitions, test data tooling, CI orchestration, certification records) | AVA |
| Architecture documentation | EA |
| Variability documentation | EA |
| Archetype update proposals | EA |
| Decision log | EA |
| Training materials | EPO |
| Operational runbooks | SRE Lead |
| Customer communication materials | EPM |

---

[← Previous: Metrics and Feedback](metrics-and-feedback.md)
