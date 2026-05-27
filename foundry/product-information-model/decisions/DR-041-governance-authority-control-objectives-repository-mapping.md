# DR-041: Governance Authority, Control Objectives, and Repository Mapping

**Status:** Accepted
**Date:** 2026-05-26

## Context

DR-040 established Governance Rituals, Governance Enforcement, governance artifacts/registers, and the Operating Model foundation. Further refinement was needed for enterprise-safe terminology and portability:

- the model should not use organization-specific job titles;
- configuration authority should not be conflated with accountability;
- BQO/BQI should not become a one-off build-quality-only taxonomy;
- temporary deviations and true exceptions need separate treatment;
- control inheritance across Foundry, Workspace, and Workbench needs to be explicit;
- repository mapping must use UPIM semantics, not implementation service names.

## Decision

1. Use **Governance Admin** for configuration roles.
   - Foundry Governance Admin
   - Workspace Governance Admin
   - Workbench Governance Admin

2. Reserve **Owner** for accountability roles.
   - Control Owner
   - Policy Owner
   - Evidence Owner
   - Risk Owner
   - Debt Owner

3. Use **Approver** for authorization roles.
   - Exception Approver
   - Debt Approver
   - Risk Acceptance Approver

4. Generalize BQO/BQI into the control model.
   - Build Quality Objective is a Build-quality **Control Objective**.
   - Build Quality Indicator is a Build-quality **Control Objective Indicator**.

5. Use **Debt + Catch-Up Plan** as the default temporary-deviation mechanism when remediation is required.

6. Retain **Exception / Waiver** for non-applicability, alternate controls, or bounded one-time bypasses.

7. Define control inheritance:

```text
Foundry control
  -> Workspace configuration
    -> Workbench configuration
```

Lower scopes may override only where the parent scope permits. Exception and debt requests route to the effective Control Owner or delegated Approver.

8. Use semantic UPIM repository mapping only.
   - Do not name implementation registry services in UPIM.
   - Map definitions, active obligations, evidence, audit, and recognition to their semantic repositories.

## Rationale

This keeps the UPIM portable across enterprises. Each organization may bind roles such as Control Owner or Debt Approver to its own job titles, but the reference model should not encode those titles.

The Control Objective / Indicator model prevents future fragmentation. Build quality, evidence completeness, security, release readiness, and operational readiness can all share the same governance pattern.

## Consequences

- Operating Model governance docs use Admin / Owner / Approver distinctly.
- BQO/BQI are treated as aliases or specializations, not the general model.
- Debt and Catch-Up Plan are modeled separately from Exception / Waiver.
- Governance docs include Foundry -> Workspace -> Workbench control inheritance.
- Repository mapping uses PPR, WFR, WR, PEIR, and source-specific evidence repositories.
