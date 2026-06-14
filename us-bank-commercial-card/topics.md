
## Component Programs (inside ESP Account Variant)

- [ ] Fee Programs — no dedicated section; one-line table entry in Ch 8 only
- [ ] Interest Programs — no dedicated section; one-line table entry in Ch 8 only
- [ ] Reward Programs — partially covered in Ch 8 (rewards/rebates computation, ~4 paragraphs); needs dedicated treatment
- [ ] Rebate Programs (filler-tier, picker-tier) — rebates mentioned in Ch 8; **filler-tier / picker-tier taxonomy not drafted anywhere**
- [ ] AMC (Purchase Category, Posting Category) — AMC concept well-drafted in Ch 12; **Purchase Category vs. Posting Category distinction not addressed**


## Corporate Structure

- [ ] OU Hierarchy (Organize Parties/Members — Employees, Contractors, Vendors, Customers) — Ch 6 defines OU structure and Member types; **policy/limit cascade through the hierarchy and full member-type governance not dedicated**
- [x] Limit Hierarchy/Forest (Underwriting context and financial controller limits) — **DONE** → Ch 9 (credit-facility-budget-account.md)
- [x] Programs (The Purpose by which expenses could be organized) — **DONE** → Ch 10 (corporate-payment-program.md)
- [x] Repayment Accounts (Bank Accounts used for Payments) — **DONE** → Ch 13 Settlement Profile (booking-settlement-profile.md)


## Merchant / Supplier Types

- [ ] Large Supplier — referenced contextually in supplier-payments chapters; no dedicated section
- [ ] Bank Affiliated Merchant — **not drafted anywhere**
- [ ] Network-provided Negotiated Customer — **not drafted anywhere**


---

## Virtual Cards – Scale, Controls, Lifecycle, and Reporting

**1. Large Scale Virtual Card Lifecycle**
- [ ] Walk through the end to end lifecycle of a large scale virtual card program (e.g., a corporate customer generating >10,000 virtual cards per day).

**2. Throughput & Scalability**
- [ ] How many virtual cards can be requested per minute?
- [ ] Describe both vertical and horizontal scaling limits.

---

## Network, Fees, and Notifications

**1. PAN vs UUID Mapping**
- [ ] Explain the use of PANs versus UUIDs.
- [ ] Where is the PAN‑to‑UUID mapping stored?
- [ ] Who owns and controls the mapping?
- [ ] How is it secured and used across systems?

**2. PIN Validation (including PIN Select and Change)**
- [ ] How is PIN validation handled end‑to‑end?
- [ ] How are initial PIN selection and ongoing PIN changes managed?
- [ ] Who controls and supports these functions (network, processor, US Bank, or the company)?

---

## Migration Cutover & Authorization / Fraud Flow

**1. Cutover Downtime**
- [ ] Is any downtime or outage expected for authorizations or card usage during cutover?
- [ ] If so, how long?

**2. Third Party Fraud Integration**
- [ ] How does your authorization platform integrate with third party fraud service providers as part of real time authorization flow?

**3. Authorization Decisioning & Resiliency**
- [ ] When an authorization request is received from the network, what is the sequence of decisioning?
- [ ] Are account level controls evaluated before or after third party fraud checks?
- [ ] What incremental latency is added?
- [ ] How are timeouts or outages handled (fail open vs. fail closed)?
- [ ] Are fallback rules configurable?
- [ ] Describe any known issues and how they were mitigated.
