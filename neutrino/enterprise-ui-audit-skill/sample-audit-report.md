# UI Audit Report

**Subject:** Claims Processing — Case Detail Screen
**Date:** 2026-03-08
**Input:** Screenshot of case detail view (single screen)

---

## 0. Input Sources and Coverage

| Source | Used | Coverage Impact |
|---|---|---|
| Live browser / MCP | No | Keyboard navigation, validation timing, responsive behavior not testable. |
| Figma / design file | No | Component consistency and design token analysis not available (any form: exported file, link, plugin would enable partial or full extraction). |
| Interactive prototype | No | Hover states, transition quality, confirmation dialogs not testable. |
| Video recording | No | Performance timing and feedback sequences not observable. |
| Accessibility tree / DOM | No | ARIA labels, tab order, and screen reader support not verifiable. |
| Screenshots | Yes | Primary input. Layout, hierarchy, copy, and visual rules fully evaluated. |
| Textual inputs | No | No supplementary documentation provided. |

**Evaluation depth:** Evaluation limited to visual and structural rules. Rules requiring interaction (AC1-3, PF1-3, NF2) marked as N/E. Tooltip, hover state, and keyboard behavior rules cannot be assessed from screenshots alone.

## 1. Summary

- **Overall score:** 2.8 / 5.0
- **Verdict:** Acceptable
- **Overall assessment:** The case detail screen displays comprehensive data but fails to guide the operator toward the next action. Status is buried in a secondary section, the primary action ("Approve") is visually identical to five other buttons, and error messages use system codes instead of plain language. Expert users can complete the task, but cognitive load is unnecessarily high and error risk is elevated.
- **Primary operational risk:** Operator may approve a case without noticing a pending compliance hold, because blocking conditions are not surfaced in the header.
- **Primary strength:** Complete audit history is visible in a chronological timeline with user identity and timestamps.
- **Rule files applied:** `enterprise-ui-main-rules.md`, `copy-style.md`

## 2. Category Scores

| Category | Score | Key Finding |
|---|---|---|
| Task framing | 3/5 | Case number visible but purpose of current step unclear |
| Workflow state | 2/5 | Status buried below fold; no blocking condition visibility |
| Information hierarchy | 3/5 | All data present but no visual priority differentiation |
| Action design | 2/5 | Six equal-weight buttons; primary action not distinguished |
| Forms and inputs | N/A | No form fields on this screen |
| Copy and language | 2/5 | System codes in error messages; inconsistent date formats |
| Error prevention and recovery | 2/5 | No guard on "Approve" despite pending compliance review |
| Navigation and wayfinding | 4/5 | Breadcrumb present; deep-linkable URL |
| Search, browse, and retrieve | N/A | Not a search/list screen |
| Data tables and lists | 3/5 | Supporting documents table lacks sort capability |
| Dashboard and metrics | N/A | Not a dashboard |
| Notifications and feedback | 3/5 | Success toast present but non-specific ("Action completed") |
| Help and guidance | 2/5 | No contextual help for complex fields |
| Continuity and resilience | 3/5 | Back button preserves list state |
| Auditability and trust | 5/5 | Full audit trail with timestamps and user identity |
| Accessibility | 3/5 | Keyboard navigation works; color-only status indicators |
| Consistency | 3/5 | Button styling consistent; date format inconsistent |

## 3. Key Findings

### Finding 1

| Field | Value |
|---|---|
| **Rule ID(s)** | WS1, WS2 |
| **Severity** | Critical |
| **Location** | Case detail header |
| **Issue** | Current workflow status ("Pending Compliance Review") is displayed in a small text label in the third section below the fold, not in the page header. |
| **Evidence** | Status appears at line 4 of the "Case Information" section, visually identical to other metadata fields. |
| **Why it matters** | Operators processing 80+ cases/day may approve a case without seeing the compliance hold, creating a regulatory violation. |
| **Recommendation** | Move status to the page header as a prominent badge. Add a blocking-condition banner when compliance review is pending: "This case cannot be approved until compliance review is complete." |

### Finding 2

| Field | Value |
|---|---|
| **Rule ID(s)** | AD1, AD3 |
| **Severity** | Critical |
| **Location** | Action button bar |
| **Issue** | Six buttons ("Approve", "Reject", "Escalate", "Hold", "Reassign", "Close") are displayed as visually identical outlined buttons in a horizontal row. |
| **Evidence** | All buttons use the same gray outline style, same size, same font weight. |
| **Why it matters** | The primary action ("Approve") is not visually distinguished, increasing the risk of accidental clicks on destructive actions like "Reject" or "Close". |
| **Recommendation** | Make "Approve" a filled primary button. Move "Reject" and "Close" to a secondary group separated by a divider. Add confirmation dialogs for destructive actions naming the case ID and consequence. |

### Finding 3

| Field | Value |
|---|---|
| **Rule ID(s)** | CER1, CER3 |
| **Severity** | Major |
| **Location** | Error notification area |
| **Issue** | Error message reads: "ERR_COMPL_4012: Validation failed." |
| **Evidence** | System error code displayed verbatim to the user with no explanation or resolution guidance. |
| **Why it matters** | Operator must contact IT or consult documentation to understand the error, increasing resolution time from seconds to minutes. |
| **Recommendation** | Replace with: "Compliance check incomplete — the customer's KYC documents have not been verified. Open the KYC tab to review pending documents." |

### Finding 4

| Field | Value |
|---|---|
| **Rule ID(s)** | CDF1 |
| **Severity** | Minor |
| **Location** | Case detail — date fields |
| **Issue** | "Created Date" shows "2026-03-08T14:32:00Z" while "Last Updated" shows "Mar 8, 2026 2:45 PM". |
| **Evidence** | Two date fields on the same screen use different formats. |
| **Why it matters** | Inconsistent formatting increases parsing effort and undermines professional polish. |
| **Recommendation** | Standardize all dates to "Mar 8, 2026 2:45 PM" format (human-readable, with time). |

## 4. Screen or Step-Level Review

### Case Detail Screen

- **What works:** Complete audit trail timeline with user identity and timestamps (AU1 — Excellent). Breadcrumb navigation clearly shows position in case hierarchy (NV1). Case number and customer name visible in header.
- **What is unclear:** What action the operator should take next. Whether the case is blocked or ready for action. Which of the six buttons is the expected primary action.
- **Operational risks:** Approval of a compliance-blocked case (WS1 — Critical). Accidental destructive action due to undifferentiated buttons (AD3 — Critical). Delayed error resolution due to system error codes (CER1 — Major).
- **Suggested changes:** (1) Add status badge and blocking-condition banner to header. (2) Visually differentiate primary vs. secondary vs. destructive actions. (3) Replace system error codes with plain-language messages including resolution steps.

## 5. Copy Rewrite Suggestions

| Current text | Problem | Rule violated | Suggested rewrite |
|---|---|---|---|
| "ERR_COMPL_4012: Validation failed." | System code, no resolution guidance | CER1, CER3 | "Compliance check incomplete — KYC documents have not been verified. Open the KYC tab to review pending documents." |
| "Action completed" | Non-specific success message | CER2 | "Case #78421 approved and forwarded to Settlement team." |
| "Submit" (button) | Generic, doesn't name the action | CAT1 | "Approve Claim" |
| "2026-03-08T14:32:00Z" | ISO timestamp, not human-readable | CDF1 | "Mar 8, 2026 2:32 PM" |
| "Process" (button) | Ambiguous — process what? | CAT2 | "Start Compliance Review" |

## 6. Metric Audit

N/A — not a dashboard screen.

## 7. Exception Path Analysis

N/A — single screen evaluated (not a multi-step flow).

## 8. Top 5 Improvements

1. **WS1, WS2** — Move workflow status and blocking conditions to the page header — prevents operators from acting on blocked cases.
2. **AD1, AD3** — Visually differentiate primary action from secondary and destructive actions — reduces accidental clicks.
3. **CER1, CER3** — Replace system error codes with plain-language messages including resolution steps — cuts error resolution time.
4. **AD4** — Add specific confirmation dialogs for "Reject" and "Close" naming the case and consequence — prevents accidental destructive actions.
5. **CDF1** — Standardize date format across all fields — improves scanning speed and professional consistency.

## 9. Open Questions / Uncertainties

- **Keyboard navigation (AC1-3):** Cannot assess from screenshot input. Requires: live browser access or accessibility tree/DOM snapshot.
- **Validation timing (FV2):** Cannot confirm whether inline validation occurs on field exit or only on submission. Requires: live browser access or interactive prototype.
- **Concurrent access (SV2):** Cannot determine whether locking or conflict detection is implemented. Requires: live browser access with two simultaneous sessions.
- **Performance (PF1-3):** Cannot assess load time or perceived responsiveness. Requires: live browser access or video recording.
- **Role-based visibility:** Cannot confirm whether different user roles see different action buttons or data sections. Requires: live browser access with multiple role accounts.
- **Tooltip content (CTT1-2):** Cannot evaluate tooltip quality on icon-only buttons and abbreviated labels. Requires: interactive prototype or browser access to trigger hover states.
