# QA Workspace

## Purpose

Verify and validate what is built. The QA Workspace receives intent in parallel with Development (from Product Specification) and receives built artifacts from Development for verification. Verified intent moves to Release as Product Delivery.

## Inbound and outbound intent

- **Inbound:** from Product Specification (intent fans out to QA in parallel with Development). Source: [../ace-model.md](../ace-model.md) line 56. Also from Development (built artifacts). Source: [../ace-model.md](../ace-model.md) line 57.
- **Outbound:** to Release (verified intent as Product Delivery). Source: [../ace-model.md](../ace-model.md) line 58. Optionally back to Product Specification when verification reveals a specification gap.

## Why QA receives intent in parallel

QA is **not** strictly downstream of Development. Both Development and QA receive intent from Product Specification at the same time. QA's parallel involvement allows:

- Test design to begin alongside build, not after it.
- Verification artifacts (test cases, acceptance tests) to be specified before built artifacts arrive.

This parallelism is captured explicitly in [../ace-model.md](../ace-model.md) line 56 and is structural in the cycle — see [../product-evolution-cycle.md](../product-evolution-cycle.md).

## Primary scenarios (illustrative)

This workspace owns scenarios such as:

- Triggering on intent arrival from Product Specification and producing verification plans and test artifacts.
- Triggering on built-artifact arrival from Development and executing verification.
- Producing build quality indicators (BQI) and evidence packs.
- Returning intent to Product Specification when verification reveals a specification gap.
- Releasing verified intent to Release as Product Delivery.

Concrete scenario catalogs live in [../../foundry-platform/](../../foundry-platform/README.md) under "QA Workspace Engineering" (see [../../foundry-platform/platform.TODO](../../foundry-platform/platform.TODO) line 25).

## Repositories touched

- **Quality & Verification Repository (QVS)** — read and write. Test cases, acceptance tests, verification evidence.
- **Source Repository (CAR)** — read.
- **Product Intent Repository (PIR)** — read and write.
- **Product Feedback Repository (PFR-Build)** — read.
- **Practitioner Repository (PPR)** — read. Verification policies and standards.
- **Work Repository (WR)** — write.

See [../repositories.md](../repositories.md).

## CI integration

QA leans on Foundry CI for evidence packs, test runners and reports, build quality indicators, and agentic quality gates. See [../../foundry-platform/release-tools/platform-developer-guide/ci/ci.TODO](../../foundry-platform/release-tools/platform-developer-guide/ci/ci.TODO).

## See also

- [../product-evolution-cycle.md](../product-evolution-cycle.md) — the cycle this workspace participates in.
- [../governance.md](../governance.md) — governance on intent transitions.
- [../../foundry-platform/platform.TODO](../../foundry-platform/platform.TODO) — QA Workspace Engineering.
