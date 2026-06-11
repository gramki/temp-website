# Chapter 03.02.10: Underwriting Fabric — Product Note

**The authoritative system of record for credit decisioning — evaluating creditworthiness, approving credit lines and loans, conducting continuous account review, and managing exception-based limit assessments.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Underwriting Fabric owns credit decisions — the evaluation of whether to extend credit, how much, and under what terms. This includes initial credit decisions (new applications), continuous account review (existing portfolio monitoring), overlimit assessments, and exception processing for non-standard requests.

In scope: credit application evaluation, credit scoring integration, decision rules and policy execution, credit line determination, loan approval/denial, decision documentation, continuous account review (behavioral scoring, limit adjustment recommendations), overlimit authorization, exception assessment for out-of-policy requests. Out of scope: the credit line storage and enforcement (Line and Limits Fabric), the loan or card account itself (domain fabrics), and fraud detection (Issuer Fraud and Risk Fabric).

---

## Source of Truth

- **Entities owned:** Credit applications, credit decisions (approvals, denials, counteroffers), decision rationale records, credit policy rules, scoring model references, continuous review assessments, exception requests, exception approvals
- **Key invariants:** Every credit decision is documented with rationale sufficient for adverse action notice. Decision rules are versioned — the rule version that governed a decision is preserved. Approvals do not exceed policy limits without documented exception. Adverse action triggers are identified and recorded.
- **Configurable vs. compliance floor:** Credit policy rules, scoring thresholds, debt-to-income limits, and exception approval hierarchies are configurable. Fair lending compliance (ECOA, fair credit), adverse action notice requirements, and decision auditability are the compliance floor.

---

## Scope Highlights

- Evaluates credit applications using bureau data, internal data, and configured decision rules
- Integrates with credit bureaus for credit reports, scores, and attributes
- Executes credit policy: debt-to-income limits, credit score thresholds, adverse criteria, product eligibility
- Produces decisions: approve, deny, counteroffer, refer to manual review
- Documents decision rationale for adverse action compliance and audit
- Performs continuous account review: behavioral scoring, proactive limit adjustments, account-level risk reassessment

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Application Evaluation** — Application intake, data gathering, completeness validation, bureau pull orchestration
2. **Decision Engine** — Policy rule execution, scoring model integration, decision tree processing, decision output
3. **Credit Policy Management** — Rule configuration, threshold management, policy versioning, A/B testing support
4. **Adverse Action** — Adverse action reason identification, notice generation triggers, reason code mapping
5. **Continuous Review** — Portfolio monitoring, behavioral score tracking, limit adjustment recommendations, risk flagging
6. **Exception Management** — Out-of-policy request handling, exception approval workflow, exception documentation

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Line and Limits Fabric | Underwriting approves credit lines; Line and Limits stores and enforces them |
| Revolving Credit Fabric | Underwriting approves credit card applications; Revolving Credit manages the account |
| Term Loans Fabric | Underwriting approves loan applications; Term Loans books and services the loan |
| Mortgage Fabric | Underwriting approves mortgage applications; Mortgage Fabric manages the loan |
| Customer Record Fabric | Credit decisions reference customer data; Customer Record provides identity and relationship data |
| Credit Bureau Fabric | Bureau pulls and reporting flow through Credit Bureau Fabric; Underwriting consumes bureau data |
| Product Fabric | Product eligibility rules may invoke Underwriting for credit-based eligibility |
| Sourcing Fabric | Credit applications originate through Sourcing; Underwriting evaluates them |
| Collections Fabric | Account review may identify accounts trending toward delinquency; recommendations may flow to Collections |

---

## References

_To be added._
