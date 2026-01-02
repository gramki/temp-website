# Clarifications Required — Follow-up Items

This document tracks items requiring further clarification or elaboration in the olympus-seer-docs.

---

## From: `raw-trained-employed.md` Review

### High Priority

- [ ] **OPD Operationalization**
  - OPD (Observability, Predictability, Directability) is currently stated as a requirement but not operationalized
  - Need to define what OPD means concretely for:
    - Raw Agents (System Operator perspective)
    - Employed Agents (HAT participant perspective)
  - Discuss: Is OPD conflated? Should it be decomposed further?
  - **Owner:** TBD
  - **Status:** Awaiting discussion

- [ ] **Failure Mode Examples**
  - Add examples of failures at each layer
  - Include: Raw Agent crash, Training guardrail violation, Employment Spec misconfiguration, Authority revocation scenario
  - Illustrate incident response flow for each
  - **Owner:** TBD
  - **Status:** Pending

### Medium Priority

- [ ] **Governance Model Variability**
  - The document notes that governance is not prescriptive
  - Consider adding examples of how different organizations might adapt the change management matrix
  - **Owner:** TBD
  - **Status:** Pending

- [ ] **Emergency Override Model**
  - Kill switches are mentioned in examples but not formalized
  - Define the override model: Who can invoke? What happens? How is it audited?
  - **Owner:** TBD
  - **Status:** Pending

- [ ] **Capacity/Quota Relationship**
  - Raw Agent has capacity constraints, Employed Agent has quotas
  - Clarify the relationship: Quota cannot exceed available capacity
  - Define overflow behavior
  - **Owner:** TBD
  - **Status:** Pending

### Lower Priority

- [ ] **Agent Diagram Examples**
  - Consider adding AOSM-style Agent Diagrams for the example scenarios
  - Would help readers familiar with AOSM methodology
  - **Owner:** TBD
  - **Status:** Pending

- [ ] **Tool Specification Examples**
  - Add examples of what a Tool Specification artifact looks like
  - Include versioning and compatibility examples
  - **Owner:** TBD
  - **Status:** Pending

- [ ] **Guardrail Specification Examples**
  - Add examples of what a Guardrail artifact looks like
  - Include enforcement semantics examples
  - **Owner:** TBD
  - **Status:** Pending

---

## From: Other Documents

*(Add items from other document reviews here)*

---

## Completed Items

*(Move completed items here with completion date)*

---

*Last Updated: January 2026*

