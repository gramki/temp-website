# Job (JTBD)

**Model:** Definition Model
**Dimension:** User Experience
**Owner:** Product Management, UX Research

## Definition

What a User Persona needs to accomplish — the user-level "job to be done." A Job is a functional, emotional, or social goal that the product must enable. In JTBD terminology, this is the *user's job* — the task-level goal the person using the product needs to complete. It is distinct from the *buyer's job* (Business Outcome in Customer Value), which is the strategic goal the budget-holder needs to achieve.

## Purpose

Job is the structural bridge between three concerns:
- **User intent (User Experience):** What the persona needs to do → Job is pursued by User Persona(s)
- **Product structure (Structural):** What the product can do → Job is enabled by Value Stream(s) / Capability(ies)
- **Buyer justification (Customer Value):** Why the purchase is justified → Job contributes to Business Outcome(s)

Without Job:
- Journeys have no purpose — "why does this flow exist?" has no formal answer
- The connection between user experience (User Experience) and product structure (Structural) is implicit
- Capabilities (Structural) can't be evaluated against user needs — only against buyer outcomes

**Jobs are reusable across Personas.** Different personas may share the same functional job but approach it through different Journeys and Channels. "Verify FX rate applied to a payment" is a job shared by the AP Clerk (checking their own work), the Treasury Analyst (monitoring exposure), and the Compliance Officer (auditing transactions).

**Discovery provenance:** Jobs are identified through user research (Research Tasks — interviews, contextual inquiry, diary studies), validated through Experiments and Prototypes, and formalized through Modeling Tasks.

## Job Types

| Type | Description | Example |
|---|---|---|
| **Functional** | The practical task the persona needs to complete | "Process a cross-border payout without errors" |
| **Emotional** | How the persona wants to feel while doing the job | "Feel confident that compliance requirements are met" |
| **Social** | How the persona wants to be perceived by others | "Demonstrate to management that treasury processes are under control" |

Most jobs have a primary functional dimension with secondary emotional/social dimensions. The product's Features and experience attributes address the emotional and social dimensions — simplicity conveys control, real-time feedback conveys confidence.

## Fields

| Field | Type | Description |
|---|---|---|
| Job Statement | String | Concise statement in the form: "[verb] + [object] + [qualifier]" (e.g., "Process a cross-border payout without errors") |
| Job Type | Enum | `Functional` / `Emotional` / `Social` (primary type; secondary types noted in description) |
| Pursued by | List of References (User Experience) | Which User Persona(s) have this job |
| Frequency | Enum | `Per-transaction` / `Daily` / `Weekly` / `Periodic` / `Ad-hoc` |
| Criticality | Enum | `Mission-critical` / `Important` / `Convenience` — how much failure matters |
| Current Alternative | Text | How the persona accomplishes this job today without the product (or with the current product version) |
| Enabled by (Structural) | List of References (Structural) | Which Value Streams or Capabilities enable this job |
| Contributes to | List of References (Customer Value) | Which Business Outcome(s) this job contributes to |

## Statuses

| Status | Description |
|---|---|
| Hypothesized | Job has been identified but not yet validated with users |
| Validated | Job has been confirmed through user research |
| Served | Product currently enables this job (one or more Journeys exist) |
| Underserved | Product partially enables this job (gaps identified) |
| Unserved | Product does not currently enable this job |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Pursued by | User Persona (User Experience) | One or more Personas have this Job |
| Accomplished through | User Journey (User Experience) | Journeys accomplish this Job |
| Enabled by | Value Stream (Structural) | Value Streams provide the end-to-end flow for this Job (primary mapping) |
| Enabled by | Capability (Structural) | Capabilities provide specific abilities required by this Job (direct mapping for simpler jobs) |
| Contributes to | Business Outcome (Customer Value) | This Job contributes to the buyer's strategic outcome |
| Relieves | Pain (Customer Value) | Accomplishing this Job relieves specific user Pains |
| Work Model | Research Task (Discovery) | Research Tasks identify and validate Jobs |
| Work Model | Modeling Task (Discovery) | Modeling Tasks formalize Jobs in User Experience |

## Examples

| Job Statement | Type | Persona(s) | Frequency | Criticality | Enabled by (Structural) | Contributes to (Customer Value) |
|---|---|---|---|---|---|---|
| "Process a cross-border payout without errors" | Functional | AP Clerk | Per-transaction | Mission-critical | Cross-Border Payout Processing (VS) | "Eliminate manual FX hedging and reduce wire fees" |
| "Verify FX rate applied to a payment" | Functional | AP Clerk, Treasury Analyst, Compliance Officer | Per-transaction | Important | Automated Rate Locking (Capability) | "Eliminate manual FX hedging" |
| "Analyze FX exposure across all pending transactions" | Functional | Treasury Analyst | Daily | Important | Multi-Currency Reporting (Capability) | "Consolidate payment operations" |
| "Generate compliance audit report for OFAC screenings" | Functional | Compliance Officer | Weekly | Mission-critical | Compliance Screening (Capability) | "Maintain regulatory compliance" |
| "Configure payment approval rules for my team" | Functional | Finance Admin | Ad-hoc | Important | Payment Configuration (Capability) | "Consolidate payment operations" |
| "Feel confident that all transactions met compliance" | Emotional | Compliance Officer | Daily | Mission-critical | — | — |
