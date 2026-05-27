
- Fee Programs
- Interest Programs
- Reward Programs
- Rebate Programs (filler-tier, picker-tier)
- AMC (Purchase Category, Posting Category)


OU Hierarchy (Organize Parties/Members - Employees, Contractors, Vendors, Customers, etc., )
Limit Hierarchy/Forest (The Underwriting context and the financial controller limits)
Programs (The Purpose by which expenses could be organized)
Repayment Accounts (Bank Accounts used for Payments)



--> Large Supplier
--> Bank Affiliated Merchant
--> Network-provided Negotiated Customer





## Virtual Cards – Scale, Controls, Lifecycle, and Reporting

**1. Large Scale Virtual Card Lifecycle**  
- Walk through the end to end lifecycle of a large scale virtual card program (e.g., a corporate customer generating >10,000 virtual cards per day).

**2. Throughput & Scalability**  
- How many virtual cards can be requested per minute?  
- Describe both vertical and horizontal scaling limits.

---

## Network, Fees, and Notifications

**1. PAN vs UUID Mapping**  
- Explain the use of PANs versus UUIDs.
- Where is the PAN‑to‑UUID mapping stored?
- Who owns and controls the mapping?
- How is it secured and used across systems?

**2. PIN Validation (including PIN Select and Change)**  
- How is PIN validation handled end‑to‑end?
- How are initial PIN selection and ongoing PIN changes managed?
- Who controls and supports these functions (network, processor, US Bank, or the company)?

---

## Migration Cutover & Authorization / Fraud Flow

**1. Cutover Downtime**
- Is any downtime or outage expected for authorizations or card usage during cutover?
- If so, how long?

**2. Third Party Fraud Integration**
- How does your authorization platform integrate with third party fraud service providers as part of real time authorization flow?

**3. Authorization Decisioning & Resiliency**
- When an authorization request is received from the network, what is the sequence of decisioning?
- Are account level controls evaluated before or after third party fraud checks?
- What incremental latency is added?
- How are timeouts or outages handled (fail open vs. fail closed)?
- Are fallback rules configurable?
- Describe any known issues and how they were mitigated.