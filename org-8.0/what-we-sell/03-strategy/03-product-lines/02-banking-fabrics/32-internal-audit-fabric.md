# Chapter 03.02.32: Internal Audit Fabric — Product Note

**The system of record for internal audit and compliance monitoring — owning audit trails, policy enforcement, exception tracking, and the bank's internal control framework distinct from external regulatory filings.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Internal Audit Fabric is the authoritative system for internal compliance and audit operations: maintaining comprehensive audit trails across banking operations, enforcing internal policies, tracking exceptions and remediation, and supporting the three-lines-of-defense model. It governs the bank's internal control environment — the policies, monitoring, and evidence collection that demonstrate operational integrity to internal audit, risk committees, and external examiners.

Out of scope: external regulatory filings (Regulatory Compliance Fabric), fraud detection (respective Fraud and Risk fabrics), and financial accounting controls (Accounting Fabric GL controls). This fabric focuses on operational audit trails, policy compliance monitoring, and exception management across all banking activities.

---

## Source of Truth

- **Entities owned:** Audit trail record, policy definition, policy violation, exception record, remediation plan, audit finding, control test result, attestation record, access review record, segregation of duties matrix, audit workpaper
- **Key invariants:** Audit trails are append-only and tamper-evident; policy violations generate exceptions that must be resolved or formally accepted; exceptions have owners and remediation deadlines; control test evidence is retained for examination cycles; access reviews are completed on schedule with documented decisions; every material action in covered systems has an audit trail entry
- **Configurable vs. compliance floor:** Policy thresholds, exception escalation paths, audit scope, and review frequencies are configurable per risk appetite. Compliance floor: SOX 404 control documentation (for public companies), OCC/Fed safety and soundness requirements, segregation of duties for critical functions, and audit trail retention per regulatory expectations (typically 7+ years)

---

## Scope Highlights

- Audit trail capture: comprehensive logging of actions, decisions, and data changes across banking systems
- Policy definition and enforcement: codifying internal policies, monitoring compliance, and flagging violations
- Exception management: capturing policy exceptions, routing for approval, tracking remediation, and reporting
- Control testing: executing and documenting tests of internal controls per audit plan
- Access review and SOD: periodic access certifications and segregation of duties monitoring

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Audit Trail Capture and Retention
2. Policy Management and Enforcement
3. Exception and Violation Tracking
4. Control Testing and Documentation
5. Access Review and Certification
6. Audit Finding and Remediation Management

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Regulatory Compliance Fabric | Regulatory Fabric handles external filings; Audit Fabric handles internal compliance monitoring |
| Trust Fabric | Trust Fabric handles identity and access; Audit Fabric monitors access reviews and SOD |
| Accounting Fabric | Accounting Fabric has GL controls; Audit Fabric monitors broader operational controls |
| All Banking Fabrics | Audit Fabric captures audit trails from operations across all fabrics |
| Cognition Fabric | Cognition Fabric processes events; Audit Fabric may consume events for compliance monitoring |

---

## References

_To be added._
