
# Enterprise Reporting and Scheduled Output Evaluation Rules

file: reporting-analytics.md
version: 1.0
purpose: Comprehensive rules for AI agents to evaluate report builders, report viewers, scheduled report management, ad-hoc query interfaces, and report distribution screens in enterprise workflow applications.

---

# 0. Agent Instructions

You are an enterprise UI evaluation agent specializing in reporting and analytics interfaces. Your job is to assess how effectively an enterprise application lets users build, view, schedule, and distribute structured reports — from ad-hoc queries to regulatory compliance packages.

Reporting is distinct from dashboards. Dashboards are real-time operational pulse checks (evaluated by `dashboard-metrics.md`). Reports are structured, point-in-time artifacts that are generated, reviewed, distributed, and often archived for compliance.

In enterprise applications, reporting serves three purposes:
- **Operational reporting** — daily/weekly reports for team leads and managers (volume, throughput, exceptions)
- **Regulatory/compliance reporting** — mandated reports with specific formats, deadlines, and distribution requirements
- **Ad-hoc analysis** — on-demand queries to investigate specific questions or trends

## 0.1 What You Will Receive

You may receive input from one or more of these sources, listed from richest to most limited:

- **Live application (browser/MCP)** — interact with the report builder: set parameters and preview results, drill down from aggregate numbers to source records, test export/download, test scheduling UI, observe report generation time, verify run history.
- **Figma or design file** (any form: exported file, shared link, plugin) — extract or infer report builder layouts, parameter control designs, output viewer layouts, scheduling form designs, and all label text to the extent the format allows. Proactively enumerate all parameter controls and their states.
- **Interactive prototype** — click through the report builder flow: parameter selection → preview → run → view results. Test drill-down from summary rows. Navigate scheduling and distribution screens.
- **Video recording** — observe report generation timing, drill-down behavior, parameter interaction, and export workflow. Note any delays or loading states during report execution.
- **Accessibility tree / DOM snapshot** — verify report table semantics, parameter form labels, and output data table structure.
- **Screenshots** — evaluate parameter layout, result formatting, data presentation quality, and scheduling UI design. Cannot assess drill-down behavior or generation timing.
- **Textual inputs** — reporting requirements, compliance report specifications, distribution workflows, data source documentation.

When richer input sources are available, proactively test the drill-down path: click an aggregate number and verify it navigates to the underlying source records with matching filters.

## 0.2 How to Conduct the Evaluation

Step 1 — Identify the report type (operational, regulatory, ad-hoc)
Step 2 — Determine the user persona (manager, compliance officer, analyst, auditor)
Step 3 — Evaluate each visible element against the rules below
Step 4 — Score each applicable category
Step 5 — Produce the structured evaluation report

## 0.3 Evaluation Principles

1. **Self-service over IT dependency** — Business users should be able to create, modify, and schedule reports without developer assistance.
2. **Reproducibility over flexibility** — A report run today and re-run next month with the same parameters must produce consistent, explainable results.
3. **Trust through transparency** — Every number in a report must be traceable to its source, filters, and calculation logic.
4. **Distribution as a feature** — Reports are shared artifacts. Scheduling, delivery, and access control are first-class features.
5. **Performance awareness** — Users must understand when a report will take time and must not be blocked while it runs.

## 0.4 Evaluation Depth by Input Source

| Capability | Screenshots | Figma | Prototype | Video | Browser |
|---|---|---|---|---|---|
| Parameter layout and labels | Full | Full | Full | Full | Full |
| Result preview quality | Partial (if shown) | Full (states) | Full | Full (if shown) | Full |
| Drill-down from aggregates | No | Partial (connections) | Full (click) | Full (if shown) | Full |
| Scheduling UI | Full (if shown) | Full | Full | Full | Full |
| Export functionality | No | Partial (states) | Partial | Partial (if shown) | Full |
| Run history | Full (if shown) | Full | Full | Full | Full |
| Report generation timing | No | No | No | Full (observe) | Full (measure) |

**Key:** Full = can fully evaluate. Partial = can partially evaluate (note limitations). No = cannot evaluate (mark as N/E in report).

If you see a report output without the builder, evaluate the output quality and note that builder assessment is not possible. If you see a builder without output, evaluate the builder experience and note output quality as not evaluable. Always evaluate what is visible.

---

# 1. Purpose and Scope

These rules evaluate reporting and analytics interfaces in enterprise applications.

**In scope:**
- Report parameter selection and builder screens
- Report output/viewer screens (tables, summaries, detail sections)
- Report scheduling and recurrence management
- Report distribution (email, export, portal publishing)
- Saved report templates and shared reports
- Ad-hoc query builders (filter + column selection + aggregation)
- Report access control and audit
- Report versioning and archival

**Out of scope:**
- Real-time operational dashboards (use `dashboard-metrics.md`)
- Data entry and bulk operations (use `data-entry-bulk-operations.md`)
- Search and record retrieval (use `search-browse-retrieve.md`)

---

# 2. Scoring Model

## 2.1 Score Definitions

| Score | Label | Definition |
|---|---|---|
| **5** | Excellent | Fully compliant. Self-service reporting with scheduling, distribution, and audit. |
| **4** | Good | Compliant with minor gaps. Users can build and schedule most reports independently. |
| **3** | Acceptable | Functional but requires workarounds. Some report types need IT assistance. |
| **2** | Problematic | Multiple violations. Users cannot reliably build or schedule reports. |
| **1** | Poor | Critical violations. Reports are untrustworthy, unscheduable, or undistributable. |

## 2.2 Severity Definitions

| Severity | Definition | Priority |
|---|---|---|
| **Critical** | Report outputs are misleading, unauditable, or fail regulatory requirements. | Must fix before release. |
| **Major** | Report building, scheduling, or distribution requires significant workarounds. | Fix in current cycle. |
| **Minor** | Polish or convenience improvement. Reports are functional but not optimized. | Fix when possible. |

## 2.3 Overall Score Calculation

- If any Critical-severity rule is violated, the overall score cannot exceed 3.
- If any single category scores 1, the overall score cannot exceed 2.
- A report that produces numbers without showing their derivation should score poorly.

---

# 3. Report Builder and Parameter Rules

RULE RP1 — Report parameters must be clearly labeled with their effect on output

Every parameter in a report builder must explain what it filters, groups, or changes in the output.

What to look for:
- Are parameter labels descriptive (not just field names)?
- Is the effect of each parameter clear ("Filter by" vs. "Group by" vs. "Sort by")?
- Are default values shown and meaningful?
- Are required parameters distinguished from optional ones?
- Are parameter dependencies visible ("Available only when Region is selected")?

Good: "Date Range: [Mar 1 - Mar 31, 2026] (Report covers transactions within this period). Region: [All Regions ▼] (Optional — leave blank for all). Group By: [Product Category ▼] (Rows will be grouped by this field). Include: ☑ Subtotals ☑ Trend comparison vs. prior period"

Bad: "Start: [field] End: [field] Region: [dropdown] Col1: [dropdown]" — no labels explaining what these parameters do to the output.

Severity: Major.

---

RULE RP2 — Report builder must show an estimated result size and run time

Before running a report, the user should know whether to expect 50 rows or 50,000 rows, and whether it will take 2 seconds or 2 minutes.

What to look for:
- Is an estimated row count shown based on current parameters?
- Is an estimated run time shown for large reports?
- Is there a warning for very large result sets?
- Can the user choose to run in the background for large reports?

Good: "Estimated results: ~12,400 rows. Estimated run time: ~15 seconds. [Run Now]". For larger queries: "Estimated results: ~450,000 rows. This report may take 3-5 minutes. [Run in Background — We'll notify you when ready] [Run Now and Wait]"

Bad: The user clicks "Run" and stares at a spinner for 4 minutes with no indication of progress or expected completion.

Severity: Major.

---

RULE RP3 — Report builder must support saved parameter sets (templates)

Users who run the same report with the same parameters regularly must be able to save and reuse parameter configurations.

What to look for:
- Can the user save a parameter set with a name?
- Can saved reports be shared with team members?
- Can saved reports be used as the basis for scheduling?
- Is the list of saved reports searchable and organized?

Good: "Save this report configuration: [Name: 'Weekly Claims Summary - East Region'] [Visibility: Team / Personal] [Save]. Your saved reports: Weekly Claims Summary - East Region (last run: Mar 7), Monthly Compliance Package (scheduled: 1st of month)."

Bad: No save functionality. The user must re-enter the same 8 parameters every time they run the weekly report.

Severity: Major.

---

RULE RP4 — Ad-hoc query builders must support iterative refinement

Ad-hoc queries are exploratory. The builder must support adding/removing columns and filters without starting over.

What to look for:
- Can the user add/remove columns after seeing initial results?
- Can filters be modified and re-run without resetting the query?
- Is the current query state visible as the user refines?
- Can the user pivot or re-aggregate without rebuilding?
- Is the query expressed in human-readable form?

Good: Results table shows data. Above it: "Showing: Claim Amount, Status, Provider, Region | Filtered by: Date = Mar 2026, Status = Pending | Grouped by: Region. [+ Add Column] [+ Add Filter] [Change Grouping]". The user adds a column; results refresh without losing filters.

Bad: After running a query, changing any parameter requires clicking "New Query" and rebuilding from scratch.

Severity: Major.

---

# 4. Report Output and Viewer Rules

RULE RO1 — Report output must clearly state its parameters and generation context

Every rendered report must show what parameters produced it, when it was generated, and from what data source.

What to look for:
- Are the active parameters/filters shown in the report header?
- Is the generation timestamp shown?
- Is the data freshness indicated ("Data as of Mar 8, 2026 14:30")?
- Is the report version or definition identified?

Good: Report header: "Claims Summary Report — March 2026. Region: East. Status: All. Generated: Mar 8, 2026 14:32 by Sarah Chen. Data as of: Mar 8, 2026 14:00. Report version: v3.2."

Bad: A table of numbers with a title "Claims Summary" and no indication of time period, filters, or when it was generated.

Severity: Critical.

---

RULE RO2 — Report numbers must be traceable to source records

Users must be able to drill down from any aggregated number to the underlying records that compose it.

What to look for:
- Can the user click an aggregated value to see the detail records?
- Is the record count shown alongside aggregated values?
- Is the drill-down path clear (which records are included)?
- Are exclusions and filters visible in the drill-down?

Good: "Total Pending Claims: $1,234,567 (47 claims)". Clicking opens a list of 47 claims with their individual amounts, sorted by value. Header: "47 claims contributing to 'Total Pending Claims' — filtered by Region: East, Status: Pending, March 2026."

Bad: "Total Pending Claims: $1,234,567" as a static number. No way to see which claims are included. The user must manually run a separate query to verify.

**Input modality:** If browser access is available, click aggregated values and verify the drill-down reaches source records with correct filters. If prototype is available, test drill-down links. Screenshots can only evaluate whether drill-down affordances are visually present — mark drill-down behavior as N/E.

Severity: Critical.

---

RULE RO3 — Report output must support multiple export formats

Enterprise reports need to be distributed in multiple formats for different audiences.

What to look for:
- Is PDF export available (for distribution and archival)?
- Is Excel/CSV export available (for further analysis)?
- Do exported files include the report header, parameters, and generation context?
- Is the formatting preserved in exports (especially PDF)?
- Are large datasets handled in exports (not truncated silently)?

Good: "Export: [PDF] [Excel] [CSV]. PDF includes: Cover page with parameters, summary, detail tables, page numbers, generation timestamp. Excel includes: Parameters sheet + Data sheet with all rows (12,400 rows — no truncation)."

Bad: Only CSV export available. No header information in the export. Report is truncated at 1,000 rows with no warning.

Severity: Major.

---

RULE RO4 — Report pagination and navigation must support large result sets

Reports with hundreds or thousands of rows must be navigable without overwhelming the user.

What to look for:
- Is pagination available with configurable page size?
- Is there a table of contents or section navigation for long reports?
- Can the user jump to a specific page or section?
- Are summary/totals visible on every page?
- Is the total record count always visible?

Good: "Showing rows 1-50 of 12,400. [First] [Prev] [Page 1 of 248] [Next] [Last]. Jump to page: [___]. Summary row at bottom of each page: Subtotal, Running total."

Bad: All 12,400 rows rendered on a single scrollable page. Browser becomes unresponsive. No section navigation.

Severity: Major.

---

# 5. Report Scheduling and Automation Rules

RULE RS1 — Report scheduling must support common recurrence patterns

Users must be able to schedule reports to run automatically at meaningful business intervals.

What to look for:
- Are common frequencies supported (daily, weekly, monthly, quarterly)?
- Can the user specify day of week, day of month, or specific dates?
- Is timezone handling explicit?
- Can schedules be paused and resumed?
- Is the next scheduled run date shown?

Good: "Schedule: Run every [Monday ▼] at [8:00 AM ▼] [EST ▼]. Next run: Monday, Mar 10, 2026 8:00 AM EST. [Pause Schedule] [Edit]". Monthly option: "Run on the [1st ▼] business day of each month."

Bad: Only "Daily" and "Weekly" options. No timezone selector. No indication of when the next run will occur.

Severity: Major.

---

RULE RS2 — Scheduled report delivery must support multiple channels

Report distribution must match how the organization actually shares information.

What to look for:
- Can reports be delivered via email (with attachment or link)?
- Can reports be published to a shared portal or folder?
- Can different recipients receive different formats?
- Is the distribution list manageable (add/remove recipients)?
- Are delivery failures surfaced to the report owner?

Good: "Deliver to: ☑ Email (Sarah Chen, Mike Lee — PDF attachment). ☑ Reports Portal (Compliance folder — accessible to Compliance team). ☑ SFTP drop (partner-reports/daily/ — CSV format). Delivery confirmation: Email to report owner on success/failure."

Bad: Reports can only be viewed in the application. No email, no export on schedule, no portal publishing.

Severity: Major.

---

RULE RS3 — Scheduled reports must show run history with status

The user must be able to see whether scheduled reports ran successfully and access past outputs.

What to look for:
- Is there a run history log for each scheduled report?
- Are failures shown with error details and timestamps?
- Can past report outputs be accessed from the history?
- Is the run duration recorded?
- Are alerts sent on failure?

Good: "Run History: Mar 8 — Success (14s, 12,400 rows, delivered to 3 recipients). Mar 7 — Success (12s). Mar 6 — Failed: Data source timeout. Retried at 8:15 AM — Success. [View output] [Re-run] [Download]"

Bad: No run history. The user does not know if scheduled reports ran or failed. Past outputs are not archived.

Severity: Major.

---

# 6. Report Access and Audit Rules

RULE RA1 — Report access must be controlled and auditable

Sensitive reports must have access controls, and report access must be logged.

What to look for:
- Can the report owner control who can view, edit, and schedule the report?
- Is report access logged (who viewed, when, what parameters)?
- Are sensitive reports restricted by default (not public)?
- Can access be granted to teams or roles, not just individuals?

Good: "Report Access: Owner: Sarah Chen. Viewers: Compliance Team (role), Mike Lee (individual). Edit: Sarah Chen only. Access log: 12 views in the last 30 days. [Manage Access] [View Access Log]"

Bad: All reports are visible to all users. No access controls. No access logging.

Severity: Critical for reports containing sensitive data. Major for operational reports.

---

RULE RA2 — Report definitions must support versioning

When a report definition changes (new columns, modified calculations, updated filters), the version history must be preserved.

What to look for:
- Is there a version history for report definitions?
- Can the user see what changed between versions?
- Can the user run a previous version of the report?
- Is the version shown on report output?

Good: "Report Definition: Claims Summary v3.2 (updated Mar 5 by Sarah Chen). Changes from v3.1: Added 'Average Processing Time' column, changed 'Region' filter default from 'All' to 'User's Region'. [View v3.1] [Compare v3.1 ↔ v3.2] [Revert to v3.1]"

Bad: Report definitions are modified in place. No way to see what changed or revert.

Severity: Minor — Major for regulatory reports.

---

# 7. Data Trust and Calculation Transparency Rules

RULE DT1 — Calculated fields must show their formula or derivation

When a report contains calculated values (averages, ratios, percentages, custom metrics), the calculation logic must be accessible.

What to look for:
- Can the user see the formula for any calculated column?
- Are calculation assumptions documented?
- Are null/zero handling rules explicit?
- Can the user verify a calculation by seeing the inputs?

Good: Hovering over "Average Processing Time: 4.2 days" shows: "Sum of processing days (1,234) ÷ Count of completed claims (294). Excludes claims with status 'Cancelled' (12 excluded). Null processing dates treated as current date."

Bad: "Average Processing Time: 4.2 days" — no indication of what's included/excluded or how nulls are handled.

Severity: Critical for regulatory reports. Major for operational reports.

---

RULE DT2 — Report totals must reconcile visibly

Subtotals and grand totals must be verifiable. The user must be able to see that detail rows sum to the subtotals.

What to look for:
- Are subtotals shown at group breaks?
- Does the grand total match the sum of subtotals?
- Are rounding differences explained?
- Are excluded records noted (filtered out, null values)?

Good: Each region group shows a subtotal row. The grand total row shows: "Grand Total: $1,234,567 (sum of 5 region subtotals). 12 records excluded (cancelled status)."

Bad: Grand total is $1,234,567 but the visible region subtotals sum to $1,232,100. No explanation of the $2,467 difference.

Severity: Critical.

---

# 8. Evaluation Output Format

## Reporting and Analytics Evaluation Report

### Metadata
- **Application:** [name and version]
- **Screen(s) evaluated:** [report builder / viewer / scheduler / distribution]
- **Report type:** [operational / regulatory / ad-hoc]
- **User persona:** [manager / compliance officer / analyst / auditor]
- **Date:** [evaluation date]

### Overall Assessment
- **Score:** X.X / 5.0
- **Verdict:** [Excellent | Good | Acceptable | Problematic | Poor]
- **Summary:** [One paragraph on reporting capability and trustworthiness]

### Category Scores

| Category | Score | Key Finding |
|---|---|---|
| Report builder and parameters (RP1-4) | X/5 | |
| Report output and viewer (RO1-4) | X/5 | |
| Scheduling and automation (RS1-3) | X/5 | |
| Access and audit (RA1-2) | X/5 | |
| Data trust and calculations (DT1-2) | X/5 | |

### Report Trust Assessment

| Report element | Traceable? | Formula visible? | Reconciles? | Verdict |
|---|---|---|---|---|
| [e.g., Total Claims Amount] | Yes/No | Yes/No/N/A | Yes/No | [✓/✗] |

### Violations
[Ordered by severity, with rule ID, severity, location, evidence, impact, recommendation]

### Priority Recommendations
1. [Rule ID — What to change — Trust or usability improvement]
2. ...
3. ...

---

# 9. Heuristic Summary

A strong reporting interface allows a user to answer instantly:

1. Can I build this report myself without IT help?
2. Do I know what parameters are shaping the output?
3. Can I trace any number back to its source records?
4. Do I know when this data was last refreshed?
5. Can I schedule this report to run weekly and email to my team?
6. Did last week's scheduled report run successfully?
7. Can I see what changed in this report definition since last month?
8. Can I export this in the format my stakeholders need (PDF, Excel)?
9. Can I share this report with my team and control who else sees it?
10. Can I verify that the totals reconcile?

If the reporting interface fails any of these, call it out with the specific rule reference.

---

# Appendix A: Rule Quick Reference

| Rule ID | Summary | Severity |
|---|---|---|
| RP1 | Parameters clearly labeled with effect on output | Major |
| RP2 | Estimated result size and run time shown | Major |
| RP3 | Saved parameter sets (templates) supported | Major |
| RP4 | Ad-hoc queries support iterative refinement | Major |
| RO1 | Output states parameters and generation context | Critical |
| RO2 | Numbers traceable to source records | Critical |
| RO3 | Multiple export formats supported | Major |
| RO4 | Pagination and navigation for large result sets | Major |
| RS1 | Common recurrence patterns supported | Major |
| RS2 | Multiple delivery channels supported | Major |
| RS3 | Run history with status shown | Major |
| RA1 | Access controlled and auditable | Critical-Major |
| RA2 | Report definitions versioned | Minor-Major |
| DT1 | Calculated fields show derivation | Critical-Major |
| DT2 | Report totals reconcile visibly | Critical |

# Appendix B: Evaluation Checklist (Quick Pass)

- [ ] Can a business user build a report without developer help?
- [ ] Are report parameters clearly labeled with their effect?
- [ ] Is estimated result size/run time shown before execution?
- [ ] Can parameter sets be saved and reused?
- [ ] Does report output show parameters, timestamp, and data freshness?
- [ ] Can users drill from aggregated numbers to source records?
- [ ] Are PDF and Excel export available with full context?
- [ ] Can reports be scheduled with common recurrence patterns?
- [ ] Are scheduled reports delivered via email and/or portal?
- [ ] Is run history visible with success/failure status?
- [ ] Are report access controls available for sensitive reports?
- [ ] Are calculated values traceable to their formula and inputs?
- [ ] Do subtotals and grand totals reconcile?
