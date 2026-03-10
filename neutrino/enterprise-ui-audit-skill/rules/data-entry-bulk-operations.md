
# Enterprise Data Entry and Bulk Operations Evaluation Rules

file: data-entry-bulk-operations.md
version: 1.0
purpose: Comprehensive rules for AI agents to evaluate data entry screens, bulk operations, import/upload workflows, spreadsheet-style editing, and batch processing interfaces in enterprise workflow applications.

---

# 0. Agent Instructions

You are an enterprise UI evaluation agent specializing in data entry and bulk operations. Your job is to assess how effectively an enterprise application supports high-volume, repetitive data input — from single-record entry at scale to multi-record bulk operations, file imports, and batch processing.

In enterprise workflow applications, data entry is a core production activity, not a secondary task. Operators may enter, validate, or correct hundreds to thousands of records per shift. The UI must support speed, accuracy, and error recovery at scale.

## 0.1 What You Will Receive

You may receive input from one or more of these sources, listed from richest to most limited:

- **Live application (browser/MCP)** — test the full data entry workflow: tab through form fields with keyboard only, test Enter-to-submit, navigate grid cells with arrow keys, paste data from clipboard, trigger inline validation, test undo/redo in grids, observe import workflow end-to-end, test batch selection and action confirmation.
- **Figma or design file** (any form: exported file, shared link, plugin) — extract or infer form layouts, grid component designs, validation state variants (empty, valid, error, warning), import flow step sequences, and batch action dialog designs to the extent the format allows. Proactively enumerate all form fields and their validation states.
- **Interactive prototype** — click through data entry forms, test tab order if wired, trigger validation states, walk through import mapping and preview steps, test batch action confirmation flows.
- **Video recording** — observe data entry speed, keyboard navigation efficiency, validation timing, import processing, and batch operation progress. Note friction points and time-per-record estimates.
- **Accessibility tree / DOM snapshot** — verify form field labels, tab order, required field indicators, validation message associations, and grid cell semantics.
- **Screenshots** — evaluate form layout, field ordering, validation message placement, import step design, and batch action UI. Cannot assess keyboard flow, paste behavior, or timing.
- **Textual inputs** — data entry workflow descriptions, volume expectations, field specifications, import format requirements.

When richer input sources are available, proactively test the keyboard-only entry cycle — this is the critical performance path for high-volume operators.

## 0.2 How to Conduct the Evaluation

Step 1 — Identify the data entry pattern (single-record form, multi-record grid, file import, batch action, template-driven)
Step 2 — Determine the operator persona and volume expectations (how many records per session?)
Step 3 — Evaluate each visible element against the rules below
Step 4 — Score each applicable category
Step 5 — Produce the structured evaluation report

## 0.3 Evaluation Principles

1. **Speed over ceremony** — Every unnecessary click, confirmation, or page load costs the operator time multiplied by hundreds of records.
2. **Accuracy over trust** — The UI must prevent errors, not just hope operators get it right. Validation, constraints, and smart defaults are essential.
3. **Partial success is normal** — Bulk operations will have exceptions. The UI must handle partial success as a first-class outcome.
4. **Keyboard-first** — High-volume data entry operators work from keyboard. Mouse-dependent workflows are a failure.
5. **Undo over prevent** — For high-volume work, making actions easily reversible is better than adding confirmation dialogs to every operation.

## 0.4 Evaluation Depth by Input Source

| Capability | Screenshots | Figma | Prototype | Video | Browser |
|---|---|---|---|---|---|
| Form layout and field ordering | Full | Full | Full | Full | Full |
| Keyboard tab order | No | No | Partial (if wired) | Partial (if shown) | Full |
| Cell navigation (grid) | No | No | Partial | Partial (if shown) | Full |
| Paste-from-clipboard | No | No | No | Partial (if shown) | Full |
| Validation timing | No | Partial (states) | Partial (if wired) | Full (observe) | Full |
| Grid undo behavior | No | No | No | Partial (if shown) | Full |
| Import preview accuracy | Partial (if shown) | Full (states) | Full (navigate) | Full (observe) | Full |
| Batch progress feedback | Partial (if shown) | Partial (states) | Full | Full (observe) | Full |

**Key:** Full = can fully evaluate. Partial = can partially evaluate (note limitations). No = cannot evaluate (mark as N/E in report).

If you see a form without volume context, evaluate for both single-entry and high-volume scenarios. Always evaluate what is visible. Note what cannot be assessed.

---

# 1. Purpose and Scope

These rules evaluate data entry and bulk operation interfaces in enterprise applications.

**In scope:**
- Single-record entry forms optimized for throughput
- Multi-record inline/grid editing
- File import and upload workflows (CSV, Excel, XML)
- Column/field mapping screens
- Batch validation and error correction
- Bulk selection and bulk action interfaces
- Template-driven and clone/duplicate entry
- Data transformation and enrichment screens
- Batch processing progress and results

**Out of scope:**
- Basic form design (covered in `enterprise-ui-main-rules.md` FD1-6)
- Search and retrieval (covered in `search-browse-retrieve.md`)
- Workflow transitions for individual records (covered in `flow-evaluation.md`)

Note: This file covers patterns beyond basic forms. For standard form design rules (field ordering, validation, required fields), see `enterprise-ui-main-rules.md`. This file covers throughput optimization, multi-record operations, and bulk processing — the patterns that differentiate enterprise data entry from simple forms.

---

# 2. Scoring Model

## 2.1 Score Definitions

| Score | Label | Definition |
|---|---|---|
| **5** | Excellent | Fully compliant. Supports high-volume operation with minimal friction. |
| **4** | Good | Compliant with minor optimization opportunities. Operators work efficiently. |
| **3** | Acceptable | Functional but notable friction. Operators can work but throughput is reduced. |
| **2** | Problematic | Multiple violations. High error rates or slow throughput likely. |
| **1** | Poor | Critical violations. Bulk operations are error-prone or effectively unusable at scale. |

## 2.2 Severity Definitions

| Severity | Definition | Priority |
|---|---|---|
| **Critical** | Likely to cause data corruption, mass errors, or make bulk operations unusable. | Must fix before release. |
| **Major** | Significantly reduces throughput, increases error rate, or makes error recovery difficult. | Fix in current cycle. |
| **Minor** | Polish or optimization opportunity. Does not block high-volume work. | Fix when possible. |

## 2.3 Overall Score Calculation

- If any Critical-severity rule is violated, the overall score cannot exceed 3.
- If any single category scores 1, the overall score cannot exceed 2.
- A form that works fine for 1 record but breaks down at 100 records should score poorly.

---

# 3. High-Throughput Entry Rules

RULE HT1 — Data entry forms must support keyboard-only operation

For high-volume entry, operators must be able to complete an entire entry cycle (fill fields, validate, submit, start next) without touching the mouse.

What to look for:
- Can the operator tab through all fields in logical order?
- Does Enter or a keyboard shortcut submit the form?
- Does the form automatically prepare for the next entry after submission?
- Are dropdowns and selectors keyboard-navigable?
- Are keyboard shortcuts documented or discoverable?

Good: After submitting a record, the form clears and the cursor is placed in the first field. Tab order follows the visual layout. Ctrl+Enter submits. A shortcut legend is shown at the bottom of the screen.

Bad: After submission, a success modal appears requiring a mouse click to dismiss. The cursor does not return to the first field. The operator must click "New Entry" to start the next record.

**Input modality:** If browser access is available, test the full tab-through and Enter-submit cycle — this is the only way to fully evaluate keyboard-only operation. If video shows an operator completing entries, observe their keyboard usage and friction points. Screenshots and prototypes cannot evaluate this rule — mark as N/E.

Severity: Critical for high-volume entry scenarios.

---

RULE HT2 — Entry forms must support smart defaults and auto-population

When operators enter many similar records in sequence, the UI should reduce redundant input.

What to look for:
- Are values from the previous entry carried forward where appropriate?
- Are frequently used values available as defaults or recent selections?
- Are dependent fields auto-populated (e.g., selecting a customer fills their address)?
- Can the operator configure default values for a session?

Good: After entering a batch of claims for the same provider, the provider name, address, and standard fee schedule carry forward. Only claim-specific fields (amount, date, patient) need entry. A "Session Defaults" panel lets the operator pin common values.

Bad: Every field starts blank for each new entry. The operator re-enters the same provider information 50 times.

Severity: Major.

---

RULE HT3 — Entry forms must minimize page loads and context switches

Each entry should not require a full page reload. Multi-step entry should avoid unnecessary intermediate screens.

What to look for:
- Does the form submit without a full page reload (AJAX/inline)?
- Is the success confirmation shown inline (not a separate page)?
- Are multi-step entries handled in a single view (accordion, tabs) rather than separate pages?
- Can the operator see their recent submissions while entering the next one?

Good: Form submits inline. A success bar appears at the top: "Claim #4821 saved. [Undo]" while the form resets for the next entry. A collapsible panel shows "Recent entries (last 10)" for reference.

Bad: Each submission redirects to a "Success" page. The operator clicks "Enter Another" to reload the empty form. No visibility into recent entries.

Severity: Major.

---

RULE HT4 — Duplicate detection must be proactive, not post-submission

When entering records that may duplicate existing data, the UI must check before submission, not after.

What to look for:
- Is real-time duplicate detection active as the operator types?
- Are potential duplicates shown with enough context to confirm or dismiss?
- Can the operator proceed despite a potential duplicate (with acknowledgment)?
- Is the duplicate check based on meaningful fields (not just exact match)?

Good: After entering a customer name and date of birth, a panel appears: "Possible duplicate: John Smith (DOB: 1985-03-15) — Account #A-7842. Created Mar 1, 2026. [View Existing Record] [This is a different person — Continue]"

Bad: The operator submits. A vague error appears: "Duplicate entry detected." The operator must search for the existing record manually to determine if it's a true duplicate.

Severity: Major.

---

# 4. Grid and Inline Editing Rules

RULE GE1 — Grid editing must support cell-level navigation and editing

Spreadsheet-style grids must allow operators to click into any cell, type, and move to the next cell — mimicking familiar spreadsheet behavior.

What to look for:
- Can the operator click a cell to edit it inline?
- Do Tab, Enter, and arrow keys navigate between cells predictably?
- Is the active cell visually highlighted?
- Can the operator edit without a separate edit dialog or modal?
- Is Escape used consistently to cancel cell edits?

Good: Clicking a cell enters edit mode with the cursor positioned in the value. Tab moves right, Enter moves down, Escape cancels the edit. The active cell has a blue border. Edited cells show a change indicator (dot or color).

Bad: Each cell requires double-clicking to open an edit modal. Tab does not navigate between cells. The operator must click "Save Row" after each row change.

**Input modality:** If browser access is available, test cell navigation with keyboard (Tab, Enter, arrow keys, Escape) and verify edit mode behavior directly. Screenshots can evaluate grid layout and change indicators but not navigation behavior — mark keyboard navigation as N/E.

Severity: Critical for grid-intensive applications.

---

RULE GE2 — Grid editing must show unsaved changes clearly

When editing multiple cells before saving, the operator must see which cells have pending changes.

What to look for:
- Are modified cells visually marked (color, indicator, bold)?
- Is there a "pending changes" count or summary?
- Can the operator review all changes before saving?
- Can individual cell edits be reverted?
- Is there a "Save All" action for batch commits?

Good: Modified cells have an orange triangle in the corner. A bar at the bottom: "8 cells modified in 3 rows. [Review Changes] [Save All] [Discard All]". The review panel shows old → new values.

Bad: No visual indication of which cells have been modified. The operator must remember what they changed. "Save" saves everything without a review step.

Severity: Major.

---

RULE GE3 — Grid editing must support copy-paste from external sources

Enterprise operators frequently paste data from Excel, email, or other systems. The grid must accept pasted data intelligently.

What to look for:
- Can the operator paste a block of cells from Excel/spreadsheet?
- Are pasted values mapped to the correct columns?
- Is a preview shown before pasted data is committed?
- Are format mismatches (dates, numbers, text) handled gracefully?
- Are paste errors reported per cell, not as a single failure?

Good: Operator selects a 5-row × 3-column range in Excel, copies, and clicks the target cell in the grid. A preview dialog: "Pasting 5 rows × 3 columns starting at Row 12, Column C. [Preview] [Paste] [Cancel]". Format mismatches are highlighted: "Row 14, Column D: '03/08/26' converted to 'Mar 8, 2026'."

Bad: Paste inserts all values into a single cell. Or paste is not supported — the operator must type each value manually.

**Input modality:** If browser access is available, test paste from clipboard directly — copy a multi-cell range from a spreadsheet and paste into the grid. This is the only way to verify paste mapping and format handling. Mark as N/E from screenshots, Figma/design file, or prototypes.

Severity: Major.

---

RULE GE4 — Grid operations must support undo at cell, row, and batch level

Operators must be able to undo changes at multiple granularity levels.

What to look for:
- Is Ctrl+Z supported for undoing cell edits?
- Can individual rows be reverted?
- Is multi-level undo supported (undo the last 5 changes)?
- Is there a "Discard All Changes" option?

Good: Ctrl+Z undoes the last cell edit. Right-clicking a row offers "Revert Row to Original". The undo stack tracks the last 20 operations.

Bad: No undo. Once a cell is edited, the only option is to manually re-enter the original value (if the operator remembers it).

Severity: Major.

---

# 5. File Import and Upload Rules

RULE FI1 — File import must show a preview before processing

Before importing data from a file, the operator must see a preview of the parsed data, the column mapping, and any detected issues.

What to look for:
- Is a preview of the first N rows shown after file selection?
- Is the column mapping shown and editable?
- Are data type mismatches or format issues highlighted?
- Can the operator skip rows or columns?
- Is the total row count shown?

Good: After uploading claims.csv (2,450 rows): "Preview: Showing first 10 of 2,450 rows. Column mapping: File Column A → Claim Number, B → Amount ($), C → Date (auto-detected as MM/DD/YYYY), D → Provider Name. 3 rows have formatting issues (highlighted). [Edit Mapping] [Import 2,450 Rows] [Cancel]"

Bad: File is uploaded and processing begins immediately. The operator sees a progress bar with no preview. Errors are discovered only after the entire import completes.

Severity: Critical.

---

RULE FI2 — Column mapping must be intelligent and editable

The import workflow must auto-detect column mappings and allow the operator to override them.

What to look for:
- Are columns auto-mapped by header name or content pattern?
- Can the operator manually override any mapping?
- Are unmapped columns flagged?
- Are required target fields highlighted if not mapped?
- Can mappings be saved as templates for repeated imports?

Good: Auto-mapping panel: "Column A ('Claim #') → Claim Number ✓ (auto-matched). Column B ('Amt') → Amount ✓ (auto-matched). Column C ('Dt') → ? (ambiguous — could be Claim Date or Service Date) [Select]. Column E ('Notes') → Not mapped [Map to field...]". Template: "[Save this mapping as 'Provider X Monthly Import']"

Bad: All columns must be manually mapped from dropdowns. No auto-detection. No saved templates.

Severity: Major.

---

RULE FI3 — Import validation must report errors per row with resolution guidance

Validation errors in imported data must be reported at the row and field level, not as a single pass/fail result.

What to look for:
- Are errors reported per row and per field?
- Is each error described with what's wrong and how to fix it?
- Can the operator fix errors inline (in the import preview) without re-uploading?
- Are valid rows importable separately from error rows?
- Is there an error report that can be exported?

Good: "Import validation: 2,410 of 2,450 rows valid. 40 rows have errors. [Import 2,410 valid rows now] [Fix errors first]. Error breakdown: 22 rows — Amount is negative (must be positive). 15 rows — Date is in the future. 3 rows — Provider code not found in system. [Download error report] [Edit errors inline]"

Bad: "Import failed: 40 errors found." No detail. The operator must fix errors in the source file, re-upload, and re-validate the entire file.

Severity: Critical.

---

RULE FI4 — Import must support partial success with clear outcome reporting

When some rows succeed and others fail, the UI must report the split clearly.

What to look for:
- Is the count of successful vs. failed rows shown?
- Can the operator download or view the failed rows?
- Are the successfully imported rows identifiable (IDs, row numbers)?
- Can the failed rows be retried after correction?

Good: "Import complete: 2,410 rows imported successfully. 40 rows failed. Failed rows have been saved to your drafts for correction. [View Imported Records] [Download Failed Rows] [Fix and Retry Failed Rows]"

Bad: "Import complete. Some errors occurred." No breakdown. The operator cannot determine which rows succeeded and which failed.

Severity: Critical.

---

# 6. Batch Selection and Batch Action Rules

RULE BA1 — Batch selection must support multiple selection strategies

Operators selecting records for bulk actions need more than row-by-row checkbox clicking.

What to look for:
- Is "Select All" available (with "Select all X matching records" beyond the current page)?
- Is shift-click for range selection supported?
- Is "Select all matching current filters" available?
- Can the operator select all and then deselect exceptions?
- Is the selection count always visible?

Good: Checkbox header offers: "Select this page (25)" and "Select all 1,247 matching records". After selecting all, a bar: "1,247 records selected. [Deselect 3 exceptions] [Clear Selection]". Shift-click selects a range.

Bad: Only individual checkboxes. No select-all. No range selection. To select 100 records, the operator clicks 100 checkboxes.

Severity: Major.

---

RULE BA2 — Batch actions must confirm with scope, count, and consequences

Before executing a bulk action, the operator must see exactly what will happen.

What to look for:
- Is the exact count of affected records shown?
- Is the action described specifically (not "Process selected")?
- Are consequences stated?
- Can the operator review the list before proceeding?
- Is the action reversible, and is this stated?

Good: "Approve 47 claims (total value: $234,500). All claims will move to 'Approved — Pending Settlement'. Notifications will be sent to 12 providers. This action is reversible within 24 hours. [Review List] [Approve 47 Claims] [Cancel]"

Bad: "Process selected items? [OK] [Cancel]"

Severity: Critical.

---

RULE BA3 — Batch processing must show progress and handle exceptions

During batch processing, the operator must see progress and be able to handle individual failures.

What to look for:
- Is a progress indicator shown (X of Y processed)?
- Are individual failures shown as they occur (not just at the end)?
- Can the operator stop or pause the batch?
- Is the final result summary clear (succeeded, failed, skipped)?
- Can failed items be retried?

Good: "Processing: 35 of 47 claims approved. 2 exceptions: Claim #4821 — amount exceeds auto-approval limit. Claim #4856 — provider suspended. [Pause] [Skip Exceptions and Continue]". Final: "45 approved. 2 exceptions require manual review. [View Exceptions] [Done]"

Bad: A spinner with no progress indication. After 3 minutes, "Batch complete. Some items could not be processed." No details.

Severity: Critical.

---

# 7. Template and Clone Rules

RULE TC1 — Template-driven entry must clearly show which fields are pre-filled and which need input

When creating records from templates, the operator must see what's provided by the template and what they need to fill in.

What to look for:
- Are template-provided values visually distinct from empty fields?
- Can the operator override template values?
- Is the template source identified?
- Can templates be created from existing records ("Save as Template")?

Good: Template "Standard Provider Claim" pre-fills: provider type (Hospital), fee schedule (Standard-2026), currency (USD). These fields show a template icon and are editable. Remaining fields (patient, amount, dates) are highlighted as "Required — enter value". A link: "Based on template: Standard Provider Claim [View Template] [Detach]"

Bad: All fields are pre-filled with no indication of which values came from the template. The operator cannot tell what they should review vs. what they should enter.

Severity: Major.

---

RULE TC2 — Cloning records must show a clear diff from the source

When duplicating an existing record, the operator must see what was copied and what needs to change.

What to look for:
- Is the source record identified?
- Are unique fields cleared or highlighted (IDs, dates, references)?
- Is the operator prompted to review fields that should change?
- Is the clone marked as a draft until submitted?

Good: "Creating new claim based on Claim #4821. Copied: Provider, fee schedule, category, notes. Cleared (enter new values): Claim date, amount, patient name, service date. This is a draft — review and submit when ready. [View Source Claim #4821]"

Bad: An exact copy is created including dates and amounts. The operator may submit without realizing they need to update claim-specific fields.

Severity: Major.

---

# 8. Data Validation and Correction Rules

RULE DV1 — Validation must be immediate, not deferred to submission

For high-volume entry, validation errors discovered at submission waste all the time spent filling the form.

What to look for:
- Do fields validate on blur (when the cursor leaves)?
- Are format constraints shown before the operator types (masks, examples)?
- Are cross-field validations triggered as early as possible?
- Are validation errors cleared when the operator corrects the value?

Good: Amount field shows format hint "$0.00" as placeholder. On blur, if negative: "Amount must be positive" appears immediately below the field. Date field validates against service date on blur: "Claim date cannot be before service date."

Bad: All validation occurs on form submission. The operator fills 20 fields, clicks Submit, and sees 5 errors — then must scroll to find and fix each one.

Severity: Major.

---

RULE DV2 — Validation errors in grids must be navigable

In grid/bulk editing, operators must be able to jump between validation errors efficiently.

What to look for:
- Is there an error count and "Next Error" navigation?
- Are error cells visually highlighted across the grid?
- Can the operator filter to show only rows with errors?
- Does clicking an error navigate to the specific cell?

Good: Error bar: "12 validation errors in 8 rows. [Next Error ↓] [Previous Error ↑] [Show only error rows]". Error cells have red borders. Clicking an error in the summary scrolls to and focuses the cell.

Bad: Error cells have red borders but no navigation. With 500 rows, the operator must scroll manually to find each error.

Severity: Major.

---

RULE DV3 — Cross-record validation must detect conflicts across the batch

When entering multiple records in a batch, the system should detect conflicts between records within the batch (not just against existing data).

What to look for:
- Are duplicate entries within the batch detected?
- Are conflicting values across batch records flagged?
- Are aggregate constraints checked (e.g., total batch amount exceeds limit)?

Good: "Batch validation: 2 potential duplicates found within this batch (rows 15 and 42 — same patient, same service date). Total batch amount: $125,000 — exceeds your daily batch limit of $100,000. [Review Duplicates] [Split Batch]"

Bad: Each record is validated independently. Duplicates within the batch are not detected until after import.

Severity: Major.

---

# 9. Evaluation Output Format

## Data Entry and Bulk Operations Evaluation Report

### Metadata
- **Application:** [name and version]
- **Screen(s) evaluated:** [entry form / grid / import wizard / batch action]
- **Data entry pattern:** [single-record / multi-record grid / file import / batch action / template-driven]
- **Operator persona:** [data entry clerk / operations officer / reviewer]
- **Volume context:** [records per session if known]
- **Date:** [evaluation date]

### Overall Assessment
- **Score:** X.X / 5.0
- **Verdict:** [Excellent | Good | Acceptable | Problematic | Poor]
- **Summary:** [One paragraph on data entry efficiency and error risk at scale]

### Category Scores

| Category | Score | Key Finding |
|---|---|---|
| High-throughput entry (HT1-4) | X/5 | |
| Grid and inline editing (GE1-4) | X/5 | |
| File import and upload (FI1-4) | X/5 | |
| Batch selection and actions (BA1-3) | X/5 | |
| Template and clone (TC1-2) | X/5 | |
| Data validation and correction (DV1-3) | X/5 | |

### Throughput Assessment

| Operation | Estimated time (per record) | Bottleneck | Optimization |
|---|---|---|---|
| [e.g., Single claim entry] | [e.g., ~45 seconds] | [e.g., Mouse-dependent dropdowns] | [e.g., Add keyboard-navigable dropdowns] |

### Violations
[Ordered by severity, each with rule ID, severity, location, evidence, impact, and recommendation]

### Priority Recommendations
1. [Rule ID — What to change — Throughput or accuracy improvement]
2. ...
3. ...

---

# 10. Heuristic Summary

A strong data entry interface allows an operator to answer instantly:

1. Can I complete an entry cycle without touching the mouse?
2. Can I enter 100 records in a session without redundant effort?
3. Can I see what I changed before saving?
4. Can I undo mistakes at cell, row, and batch level?
5. Can I paste data from Excel and have it map correctly?
6. Can I preview imported data before it's committed?
7. Can I fix import errors inline without re-uploading?
8. When a batch partially fails, do I know exactly which items failed and why?
9. Does the system catch duplicates before I submit, not after?
10. Can I create records from templates and clearly see what needs my input?

If the entry interface fails any of these, call it out with the specific rule reference.

---

# Appendix A: Rule Quick Reference

| Rule ID | Summary | Severity |
|---|---|---|
| HT1 | Keyboard-only operation supported | Critical |
| HT2 | Smart defaults and auto-population | Major |
| HT3 | Minimize page loads and context switches | Major |
| HT4 | Proactive duplicate detection | Major |
| GE1 | Cell-level navigation and inline editing | Critical |
| GE2 | Unsaved changes clearly shown | Major |
| GE3 | Copy-paste from external sources supported | Major |
| GE4 | Undo at cell, row, and batch level | Major |
| FI1 | File import shows preview before processing | Critical |
| FI2 | Column mapping intelligent and editable | Major |
| FI3 | Import errors reported per row with guidance | Critical |
| FI4 | Partial success with clear outcome reporting | Critical |
| BA1 | Multiple selection strategies supported | Major |
| BA2 | Batch actions confirm scope, count, consequences | Critical |
| BA3 | Batch processing shows progress, handles exceptions | Critical |
| TC1 | Template-driven entry shows pre-filled vs. needed fields | Major |
| TC2 | Cloning shows diff from source record | Major |
| DV1 | Validation immediate, not deferred to submission | Major |
| DV2 | Validation errors in grids are navigable | Major |
| DV3 | Cross-record validation detects intra-batch conflicts | Major |

# Appendix B: Evaluation Checklist (Quick Pass)

- [ ] Can the operator complete an entry cycle keyboard-only?
- [ ] Does the form prepare for the next entry after submission?
- [ ] Are smart defaults and carry-forward values supported?
- [ ] Does duplicate detection happen before submission?
- [ ] Can grid cells be edited inline without modals?
- [ ] Are unsaved grid changes visually indicated?
- [ ] Does copy-paste from Excel work correctly?
- [ ] Is multi-level undo available (cell, row, batch)?
- [ ] Does file import show a preview before processing?
- [ ] Are import errors reported per row with fix guidance?
- [ ] Can valid rows be imported while errors are fixed separately?
- [ ] Does batch action confirmation show count, scope, and consequences?
- [ ] Does batch processing show progress and surface exceptions?
- [ ] Are templates clearly distinguished from operator-entered values?
