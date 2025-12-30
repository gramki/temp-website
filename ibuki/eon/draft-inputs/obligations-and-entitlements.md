## Obligations and Entitlements in FFOS: Bi-Party Model

To ensure semantic fidelity and practical utility, **obligations** and **entitlements** in FFOS must always be represented as relationships between two parties—not just as “the family owes/is owed” in the abstract. Each must explicitly define both the **liable party** and the **beneficiary party** for every commitment or right, accommodating both intra-family and external connections.

---

### 1. Formal Definitions

#### 1.1 Obligation

> **Definition:**  
An **Obligation** is a structured, time-bound financial or operational commitment requiring a *liable party* (e.g., household, one or more members) to fulfill a payment or action in favor of a *beneficiary party* (another member, the household, or an external entity) by a specific due date or event trigger.

**Key Elements:**
- **Liable Party:** Entity responsible to perform or pay (family, member, subgroup).
- **Beneficiary Party:** Entity that receives the benefit or payment (could be internal within the family graph or external).

**Illustration:**  
Instead of “family owes X,” FFOS expresses  
> **Party A (within the family graph) owes [amount/action] to Party B (internal or external) under agreed terms and schedule.**

---

#### 1.2 Entitlement

> **Definition:**  
An **Entitlement** is a structured financial or operational right entitling a *beneficiary party* (family or member) to receive money, benefits, or actions from a *liable party* (could be another member, the household, or an external entity like employer, tenant, insurer), subject to time or event-based criteria.

**Key Elements:**
- **Beneficiary Party:** Entity in whose favor the right exists.
- **Liable Party:** Counterparty obligated to deliver the entitlement (internal or external).

**Illustration:**  
Rather than “family expects X,” FFOS defines  
> **Party A (internal or external) owes [amount/action] to Party B (in the family graph) under defined terms and conditions.**

---

### 2. Modeling Intra-Family & External Relationships

Examples of how this model applies:

- **Loan: Family Member → Family Member**  
  - *Obligation*: Liable = Borrower; Beneficiary = Lender  
  - *Entitlement*: Beneficiary = Lender; Liable = Borrower

- **Loan: Friend → Family Member**  
  - *Obligation*: Liable = Family Member; Beneficiary = Friend (external)

- **Loan: Family Member → Friend**  
  - *Entitlement*: Beneficiary = Family Member; Liable = Friend (external)

- **Salary: Employer → Family Member**  
  - *Entitlement*: Beneficiary = Family Member; Liable = Employer (external)

- **Rent Paid: Household → Landlord**  
  - *Obligation*: Liable = Household or Member; Beneficiary = Landlord (external)

- **Rent Received: Tenant → Family**  
  - *Entitlement*: Beneficiary = Household or Member; Liable = Tenant (external)

This approach enables FFOS to uniformly model money flows—within the family graph or involving external parties.

---

### 3. Data Model Refinements

#### 3.1 Party Abstraction

A **Party** is a generalized entity:

```typescript
Party {
  party_id
  type: family | member | external_person | organization | account_entity
  reference // Internal graph node or external identifier
}
```

All obligations and entitlements reference parties, enabling flexible and consistent linkage.

---

#### 3.2 Obligation Entity

```typescript
Obligation {
  obligation_id
  liable_party: Party         // who must pay/perform
  beneficiary_party: Party    // who receives the benefit

  owner: family | member      // viewpoint for FFOS dashboards and rights
  type: financial | operational
  amount | value
  currency
  due_date | recurrence_rule
  priority
  category                   // e.g., rent, loan_repayment, school_fee,
                             // intra_family_loan, etc.
  source: detected | declared | inferred | integrated
  status: upcoming | due | overdue | completed | canceled

  consent_requirements        // roles/parties needed
  metadata                   // e.g. product/contract/document links
}
```

---

#### 3.3 Entitlement Entity

```typescript
Entitlement {
  entitlement_id
  beneficiary_party: Party   // who is owed
  liable_party: Party        // who owes

  owner: family | member     // viewpoint for FFOS UI/policy
  type: financial | operational
  expected_amount | value
  currency
  expected_date | trigger_condition
  confidence_score
  category                   // e.g., salary, rent_receivable, reimbursement,
                             // claim_payout, intra_family_loan_receivable, etc.
  source: declared | system-integrated | inferred | contract-linked
  status: expected | pending | received | delayed | canceled

  consent_requirements
  metadata                   // e.g. claim_id, contract_id, product_id, etc.
}
```

---

### 4. Integration with the Family Financial Graph

- Each **Obligation** or **Entitlement** forms a directed edge between two parties (graph nodes), labeled with:
  - **Direction:** Liable → Beneficiary
  - **Type:** obligation or entitlement
  - **Category:** (e.g., loan, rent, claim)
  - **Temporal Attributes:** start, end, recurrence

This architecture enables:
- Visualization of intrafamily and external “who owes whom” relationships
- Distinction between internal vs. external cashflows
- Consolidated net positions (e.g., “Member X is a net lender”)
- Improved family advice and governance (e.g., flagging high intra-family credit risk)

---

### 5. Agent Usage Patterns

- **Cashflow Foundation Agent**:  
  Models liquidity scenarios using obligation outflows and entitlement inflows, always counterparty-aware.
- **Goals Foundation Agent**:  
  Prioritizes satisfying obligations and optimizing entitlement leverage towards family/individual goals.
- **Risk & Family Health Agent**:  
  Assesses concentration risks (e.g., excess intra-family loans, dependency on single external payer).
- **Governance Agents**:  
  Enforce family policy (e.g., restrict loans to minors, approvals for non-family lending).
- **Concierge/Experience Agents**:  
  Provide contextualized narratives (“You have ₹X from A receivable and ₹Y owed to B this month”).

---

*Next steps available upon request:*
- Propose a family graph DB schema for obligations and entitlements
- Draft FFOS Data Architecture guidance for banking and architecture teams  