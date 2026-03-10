
# Enterprise Collaboration and Annotation Evaluation Rules

file: collaboration-annotation.md
version: 1.0
purpose: Comprehensive rules for AI agents to evaluate collaboration features — comments, activity feeds, assignments, shared views, mentions, and real-time presence indicators in enterprise workflow applications.

---

# 0. Agent Instructions

You are an enterprise UI evaluation agent specializing in collaboration and annotation patterns. Your job is to assess how effectively an enterprise application supports multi-user collaboration on records, cases, and workflows — including commenting, activity tracking, assignment, shared context, and real-time awareness.

In enterprise workflow applications, records are rarely handled by a single person. A claim may pass through five reviewers. A compliance case may accumulate notes over weeks. A customer onboarding file may involve operations, compliance, and sales teams simultaneously. Collaboration features are the connective tissue that lets multiple participants work on the same record without confusion, duplication, or lost context.

## 0.1 What You Will Receive

You may receive input from one or more of these sources, listed from richest to most limited:

- **Live application (browser/MCP)** — interact with collaboration features: post a comment and verify threading, test @mention autocomplete, observe real-time presence indicators, test assignment flows, filter activity feeds, test watching/subscription controls, verify concurrent editing indicators.
- **Figma or design file** (any form: exported file, shared link, plugin) — extract or infer comment thread layouts, activity feed designs, assignment UI components, mention autocomplete designs, presence indicator variants, and internal-vs-external note distinction patterns to the extent the format allows. Proactively enumerate all collaboration UI states.
- **Interactive prototype** — click through comment posting, assignment, and mention flows. Test activity feed filtering. Observe the internal/external note distinction UI.
- **Video recording** — observe real-time presence updates, concurrent editing behavior, comment posting and threading, and activity feed scrolling/filtering. Note collaboration timing and response latency.
- **Accessibility tree / DOM snapshot** — verify comment thread structure, activity feed semantics, mention accessibility, and presence indicator labeling.
- **Screenshots** — evaluate thread layout, feed structure, assignment UI design, and visual distinction between internal/external notes. Cannot assess real-time features or autocomplete behavior.
- **Textual inputs** — collaboration workflow descriptions, handoff processes, notification requirements.

When richer input sources are available, proactively test the collaboration round-trip: post a comment, verify it threads correctly, test @mention to verify it resolves to users, and check the activity feed updates.

## 0.2 How to Conduct the Evaluation

Step 1 — Identify the collaboration pattern (commenting, activity tracking, assignment, shared context, real-time)
Step 2 — Determine the participant types (reviewers, operators, managers, external parties)
Step 3 — Evaluate each visible element against the rules below
Step 4 — Score each applicable category
Step 5 — Produce the structured evaluation report

## 0.3 Evaluation Principles

1. **Context over communication** — Comments and notes should enrich the record's context, not replace structured data fields.
2. **Attribution is mandatory** — Every comment, note, and action must be attributed to a specific user with a timestamp.
3. **Relevance over completeness** — Activity feeds must be filterable so users see what matters to their role, not every system event.
4. **Structured over freeform** — Where possible, capture collaboration through structured mechanisms (assignment, status change, checklist) rather than freeform text.
5. **Notification control** — Users must control what notifications they receive. Collaboration features that generate noise undermine adoption.

## 0.4 Evaluation Depth by Input Source

| Capability | Screenshots | Figma | Prototype | Video | Browser |
|---|---|---|---|---|---|
| Thread structure | Full | Full | Full | Full | Full |
| Internal/external distinction | Full (if shown) | Full (variants) | Full | Full | Full |
| Activity feed filtering | Partial (layout) | Partial (states) | Full | Full (if shown) | Full |
| Mention autocomplete | No | Partial (design) | Full (if wired) | Partial (if shown) | Full |
| Real-time presence | No | Partial (indicators) | No | Full (observe) | Full |
| Concurrent editing indicators | No | Partial (variants) | No | Full (if shown) | Full |
| Assignment flow | Partial (layout) | Full (states) | Full | Full (if shown) | Full |

**Key:** Full = can fully evaluate. Partial = can partially evaluate (note limitations). No = cannot evaluate (mark as N/E in report).

If you see a comment thread without the broader record context, evaluate the thread quality and note the missing context. If collaboration features are absent from a screen that clearly involves multi-user work, flag it as a gap. Always evaluate what is visible.

---

# 1. Purpose and Scope

These rules evaluate collaboration and annotation interfaces in enterprise applications.

**In scope:**
- Comment threads and threaded discussions on records
- Activity feeds and audit timelines
- Assignment, delegation, and ownership transfer UI
- @mention and notification features
- Watching/subscribing to records
- Shared views and team workspaces
- Real-time presence and co-editing indicators
- Internal notes vs. external-visible notes
- Checklists and structured task tracking within records
- Notification preferences and delivery controls

**Out of scope:**
- Chat/messaging applications (standalone communication tools)
- Workflow transitions (covered in `flow-evaluation.md`)
- Audit trails for compliance (covered in `enterprise-ui-main-rules.md` AU1-3)
- Notification display patterns (covered in `enterprise-ui-main-rules.md` NF1-4)

---

# 2. Scoring Model

## 2.1 Score Definitions

| Score | Label | Definition |
|---|---|---|
| **5** | Excellent | Fully compliant. Collaboration is structured, contextual, and non-disruptive. |
| **4** | Good | Compliant with minor gaps. Multi-user workflows are well-supported. |
| **3** | Acceptable | Functional but notable friction. Users can collaborate with workarounds. |
| **2** | Problematic | Multiple violations. Collaboration is confusing, noisy, or unreliable. |
| **1** | Poor | Critical violations. Multi-user work is effectively unsupported or dangerous. |

## 2.2 Severity Definitions

| Severity | Definition | Priority |
|---|---|---|
| **Critical** | Likely to cause lost context, misattribution, unauthorized disclosure, or handoff failure. | Must fix before release. |
| **Major** | Creates confusion, noise, or friction in multi-user collaboration. | Fix in current cycle. |
| **Minor** | Polish or convenience improvement. Does not impede collaboration. | Fix when possible. |

## 2.3 Overall Score Calculation

- If any Critical-severity rule is violated, the overall score cannot exceed 3.
- If any single category scores 1, the overall score cannot exceed 2.
- A record that multiple users work on but that has no visible collaboration history should score poorly.

---

# 3. Comment and Discussion Rules

RULE CD1 — Comments must be threaded and contextual

Comments on a record must support threading (replies to specific comments) and should be attached to the record's context.

What to look for:
- Can users reply to specific comments (threaded discussion)?
- Are comments attached to the record (not free-floating)?
- Can comments be linked to specific fields or sections of the record?
- Is there a "resolved" or "closed" state for discussion threads?
- Are threads collapsible to reduce visual noise?

Good: A compliance review has a comment section. Each comment shows author, timestamp, and content. Reply arrows create threaded sub-conversations. A comment on the risk score is tagged "[Risk Assessment]" and appears both in the general timeline and inline next to the risk score field. Resolved threads are collapsed: "3 resolved comments — [Expand]".

Bad: Comments are a flat chronological list with no threading. A reply to a question posted 20 comments ago appears at the bottom with no connection to the original. No way to mark discussions as resolved.

Severity: Major.

---

RULE CD2 — Comments must distinguish internal notes from external-visible content

In applications where records may be visible to external parties (customers, partners, regulators), internal notes must be clearly separated from external-visible comments.

What to look for:
- Is there a clear visual distinction between internal and external comments?
- Is the visibility scope labeled ("Internal Only", "Visible to Customer")?
- Is the default set to the safer option (internal)?
- Is there a confirmation when posting externally-visible comments?
- Can internal notes be converted to external (with confirmation) but not vice versa?

Good: Two tabs: "Internal Notes" (yellow background, lock icon) and "Customer Communication" (blue background, globe icon). When posting: "This note is visible to: [Internal Team Only ▼]". Switching to "Customer" triggers: "This comment will be visible to the customer (Acme Corp). Confirm? [Post to Customer] [Keep Internal]"

Bad: A single comment box with no visibility controls. All comments are visible to customers. An operator posts internal deliberation ("This claim looks fraudulent, escalate to legal") visible to the claimant.

Severity: Critical.

---

RULE CD3 — Comments must support rich content and attachments

Enterprise comments often need more than plain text — screenshots, file attachments, formatted text, and links to other records.

What to look for:
- Can users attach files or images to comments?
- Is basic formatting supported (bold, lists, code blocks)?
- Can users link to other records or external URLs?
- Are attachments previewed inline?
- Is there a size limit clearly communicated?

Good: Comment editor supports bold, bullet lists, and code formatting. Drag-and-drop for images and files. Attached images show inline thumbnails. Links to other records are rendered as clickable cards showing the record's title and status.

Bad: Plain text only. To share a screenshot, the user must upload it elsewhere and paste a URL. No formatting options.

Severity: Minor — Major when document-heavy processes require image sharing.

---

RULE CD4 — Comments must be editable and deletable with audit preservation

Users should be able to correct their own comments, but edits must be transparent.

What to look for:
- Can users edit their own comments (with an "edited" indicator and timestamp)?
- Can users delete their own comments (or is deletion restricted)?
- Is the edit history preserved (original content accessible)?
- Is deletion soft (marked as deleted) rather than hard (erased)?
- Are edit/delete permissions time-limited ("editable for 15 minutes after posting")?

Good: Edit shows "(edited Mar 8, 14:35)" with a "View edit history" link showing the original text. Deleted comments show "[Comment removed by Sarah Chen — Mar 8, 14:40]" preserving the thread structure.

Bad: Comments can be silently edited with no indication. Deleted comments disappear entirely, breaking thread context ("Reply to what?").

Severity: Major.

---

# 4. Activity Feed and Timeline Rules

RULE AF1 — Activity feeds must distinguish user actions from system events

When a record shows an activity timeline, human actions (comments, status changes, assignments) must be visually distinct from automated system events (notifications sent, background calculations, scheduled updates).

What to look for:
- Are user actions and system events visually differentiated (icons, colors, labels)?
- Can the feed be filtered by type (comments only, status changes only, all)?
- Are system events less visually prominent than user actions?
- Is the feed chronological with clear timestamps?

Good: Timeline with color-coded entries: blue person icon for user actions ("Sarah Chen changed status to 'Under Review'"), gray gear icon for system events ("Risk score recalculated: 72 → 78"), green comment icon for comments. Filter bar: "[All] [Comments] [Status Changes] [Assignments] [System]".

Bad: A flat list of text entries with no visual distinction: "Status changed. Comment added. Notification sent. Risk score updated." All look the same.

Severity: Major.

---

RULE AF2 — Activity feeds must be filterable and searchable for long-lived records

Records that accumulate months of activity must support filtering and searching the timeline.

What to look for:
- Can the timeline be filtered by date range, event type, or user?
- Can the user search within the activity feed?
- Are old entries paginated or lazy-loaded (not blocking page load)?
- Is there a "Jump to" feature for key milestones?

Good: A case open for 6 months shows: "Showing 247 events. [Filter: Type ▼] [User ▼] [Date Range ▼] [Search]. Key milestones: Created (Sep 8) → First Review (Oct 2) → Escalated (Nov 15) → Resolution (Mar 5). [Jump to milestone ▼]"

Bad: All 247 events loaded on page load, causing a 5-second delay. No filtering. The user scrolls through months of activity to find a specific event.

Severity: Major.

---

RULE AF3 — Activity feeds must show the "so what" for each entry

Each activity entry must communicate not just what happened, but why it matters.

What to look for:
- Do status changes show old → new values?
- Do field changes show what was changed (not just "record updated")?
- Do assignment changes name both the previous and new owner?
- Are related changes grouped (5 fields changed in one save → one entry with details)?

Good: "Mar 8, 14:32 — Sarah Chen changed Status: 'Pending Review' → 'Under Review'. Assigned to: Mike Lee → Sarah Chen. Priority: Normal → High (reason: SLA deadline in 2 days)."

Bad: "Mar 8, 14:32 — Record updated by Sarah Chen." No indication of what changed.

Severity: Major.

---

# 5. Assignment and Ownership Rules

RULE AO1 — Assignment must show current owner, assignment history, and transfer context

When a record is assigned to a user, the current owner, the assignment chain, and the reason for each assignment must be visible.

What to look for:
- Is the current owner prominently displayed?
- Is the assignment history visible (who assigned to whom, when, why)?
- Can the user see the full ownership chain for the record?
- Is the reason for the current assignment shown ("Assigned by auto-routing rule" vs. "Manually assigned by Mike Lee")?

Good: Header: "Owner: Sarah Chen (assigned Mar 8 by Mike Lee — 'Specialized compliance expertise needed')". Assignment history: "Mar 1: Auto-assigned to Operations Queue → Mar 5: Claimed by Mike Lee → Mar 8: Reassigned to Sarah Chen (reason: compliance expertise)."

Bad: "Owner: Sarah Chen" with no history, no reason, and no indication of how the assignment occurred.

Severity: Major.

---

RULE AO2 — Reassignment and delegation must require context

When transferring ownership, the new owner must receive context about why they're receiving the record and what's expected.

What to look for:
- Does the reassignment form require a reason or instruction?
- Is the context visible to the new owner when they open the record?
- Can the reassigner attach specific instructions or highlight relevant sections?
- Is the reassignment notification informative (not just "You have a new assignment")?

Good: Reassignment dialog: "Reassign to: [Sarah Chen ▼]. Reason: [Compliance expertise needed — customer flagged by screening system]. Instructions: [Please review the new screening results in the Documents tab. Prior review by Mike Lee found no issues but new data has arrived.] [Reassign]"

Bad: Reassignment is a dropdown change with no context field. Sarah Chen opens the record and has no idea why it was sent to her or what she should focus on.

Severity: Critical.

---

RULE AO3 — Workload visibility must support informed assignment decisions

When assigning work, the assigner should see the target user's current workload to make informed decisions.

What to look for:
- Is the target user's current assignment count visible?
- Can the assigner compare workloads across team members?
- Are SLA deadlines for the target user's existing work shown?
- Is the target user's availability status visible (active, away, on leave)?

Good: Assignment dropdown shows: "Sarah Chen — 12 active items (2 due today). Mike Lee — 8 active items (0 due today). Available capacity indicator: 🟢🟡🔴."

Bad: A plain dropdown of user names. The assigner has no idea who's overloaded.

Severity: Major.

---

# 6. Mention and Notification Rules

RULE MN1 — @mentions must be supported and must generate targeted notifications

Users must be able to bring specific colleagues' attention to a record or comment using mentions.

What to look for:
- Does typing "@" trigger a user picker/autocomplete?
- Does the mentioned user receive a notification linked to the specific comment?
- Are mentions visually highlighted in the comment?
- Can teams or roles be mentioned (e.g., @ComplianceTeam)?
- Does the notification take the recipient directly to the relevant comment?

Good: Typing "@sa" in a comment shows an autocomplete: "Sarah Chen (Compliance), Sam Wright (Operations)". After posting: "@Sarah Chen" is rendered as a clickable name tag. Sarah receives a notification: "Mike Lee mentioned you in Case #7842: 'Please review the updated risk assessment.' [View Comment]"

Bad: No mention support. To get someone's attention, the user must send a separate email or chat message with a link to the record.

Severity: Major.

---

RULE MN2 — Notification preferences must be granular and user-controlled

Users must be able to control what generates a notification, how they receive it, and how often.

What to look for:
- Can users choose notification channels (in-app, email, both, none)?
- Can users set preferences per event type (mentions, assignments, status changes, comments)?
- Are digest/batch options available (hourly/daily summary vs. real-time)?
- Can users mute specific records or threads?
- Are defaults sensible (critical items notify, minor items don't)?

Good: "Notification Preferences: Mentions → In-app + Email (real-time). Assignments → In-app + Email (real-time). Comments on my records → In-app (daily digest). Status changes → In-app only. System events → Off. [Mute specific records]"

Bad: All collaboration events generate real-time email notifications. No way to reduce the volume. Users stop reading notifications.

Severity: Major.

---

# 7. Shared Views and Workspace Rules

RULE SV1 — Shared views must distinguish personal from team-shared

When users create saved views or filter configurations, it must be clear whether the view is personal or shared with the team.

What to look for:
- Is view visibility labeled (Personal / Team / Organization)?
- Can the creator control who sees a shared view?
- Can shared views be modified only by the creator or designated editors?
- Are personal views not visible to others?

Good: "My Views: High Priority Queue (personal), Pending Compliance (personal). Team Views: Weekly Review Queue (shared by Mike Lee — read-only), SLA Breaches (shared by Ops Lead — editable by team). [Create View] [Share View]"

Bad: All saved views are visible to all users. The sidebar has 40 views from different team members with no filtering or organization.

Severity: Major.

---

RULE SV2 — Real-time presence must indicate who else is viewing or editing a record

When multiple users may access the same record, the UI should show who else is currently viewing or editing.

What to look for:
- Are active viewers shown (avatars, names)?
- Is "editing" distinguished from "viewing"?
- Is there a conflict warning when two users edit simultaneously?
- Are presence indicators unobtrusive (not blocking the interface)?

Good: Top-right of the record shows two avatar circles: "SC (viewing)" and "ML (editing Section 3)". When both try to edit the same section: "Mike Lee is currently editing this section. Your changes may conflict. [View their edits] [Edit anyway — changes will be merged]"

Bad: No presence indicators. Two users edit the same record. The second save silently overwrites the first user's changes.

**Input modality:** If browser access is available, open the same record in two sessions to observe real-time presence and conflict handling. If video shows concurrent usage, observe presence indicator updates and conflict resolution. Screenshots can evaluate the presence indicator design but not real-time behavior — mark as N/E.

Severity: Critical for records with concurrent access.

---

# 8. Checklist and Structured Collaboration Rules

RULE SC1 — Checklists must support assignment, tracking, and completion

When records have multi-step review or action items, structured checklists are preferred over freeform comments.

What to look for:
- Can checklist items be assigned to specific users?
- Do checklist items show completion status with who and when?
- Can checklist items have due dates?
- Is the overall checklist progress shown (3 of 7 complete)?
- Are incomplete items surfaced in assignments and notifications?

Good: "Review Checklist: ✅ Verify identity documents (Sarah Chen, Mar 7). ✅ Check credit history (Mike Lee, Mar 7). ⬜ Review financial statements (assigned to Sarah Chen — due Mar 10). ⬜ Compliance sign-off (unassigned). Progress: 2 of 4 complete."

Bad: Review steps are tracked in freeform comments: "I checked the ID docs" / "Credit history looks fine." No structured tracking. The manager must read through 20 comments to determine status.

Severity: Major.

---

# 9. Evaluation Output Format

## Collaboration and Annotation Evaluation Report

### Metadata
- **Application:** [name and version]
- **Screen(s) evaluated:** [record detail / activity feed / assignment / workspace]
- **Collaboration pattern:** [commenting / activity feed / assignment / shared views / real-time]
- **Participant types:** [reviewers / operators / managers / external parties]
- **Date:** [evaluation date]

### Overall Assessment
- **Score:** X.X / 5.0
- **Verdict:** [Excellent | Good | Acceptable | Problematic | Poor]
- **Summary:** [One paragraph on collaboration quality and multi-user support]

### Category Scores

| Category | Score | Key Finding |
|---|---|---|
| Comments and discussions (CD1-4) | X/5 | |
| Activity feed and timeline (AF1-3) | X/5 | |
| Assignment and ownership (AO1-3) | X/5 | |
| Mentions and notifications (MN1-2) | X/5 | |
| Shared views and workspaces (SV1-2) | X/5 | |
| Checklists and structured collaboration (SC1) | X/5 | |

### Collaboration Gap Assessment

| Multi-user scenario | Supported? | Quality | Notes |
|---|---|---|---|
| [e.g., Handoff between reviewers] | Yes/No | X/5 | [Assessment] |

### Violations
[Ordered by severity, with rule ID, severity, location, evidence, impact, recommendation]

### Priority Recommendations
1. [Rule ID — What to change — Collaboration improvement]
2. ...
3. ...

---

# 10. Heuristic Summary

A strong collaboration interface allows a participant to answer instantly:

1. What has happened on this record since I last looked?
2. Who is currently working on this and what are they doing?
3. Why was this assigned to me and what am I expected to do?
4. Can I tag a colleague and bring their attention to a specific issue?
5. Can I distinguish my internal notes from what the customer sees?
6. Can I find a specific discussion or decision in the record's history?
7. Is my comment reaching the right people without spamming everyone?
8. Can I see what items are waiting for my action across all my records?
9. Who had this before me and what did they decide?
10. Are discussions resolved and tracked, or lost in a comment stream?

If the collaboration interface fails any of these, call it out with the specific rule reference.

---

# Appendix A: Rule Quick Reference

| Rule ID | Summary | Severity |
|---|---|---|
| CD1 | Comments threaded and contextual | Major |
| CD2 | Internal notes distinguished from external-visible | Critical |
| CD3 | Rich content and attachments supported | Minor-Major |
| CD4 | Editable/deletable with audit preservation | Major |
| AF1 | User actions distinguished from system events | Major |
| AF2 | Activity feeds filterable and searchable | Major |
| AF3 | Activity entries show the "so what" | Major |
| AO1 | Current owner, history, and transfer context visible | Major |
| AO2 | Reassignment requires context and instructions | Critical |
| AO3 | Workload visibility supports informed assignment | Major |
| MN1 | @mentions supported with targeted notifications | Major |
| MN2 | Notification preferences granular and user-controlled | Major |
| SV1 | Personal vs. team-shared views distinguished | Major |
| SV2 | Real-time presence indicates concurrent viewers/editors | Critical |
| SC1 | Checklists support assignment, tracking, completion | Major |

# Appendix B: Evaluation Checklist (Quick Pass)

- [ ] Are comments threaded with reply capability?
- [ ] Are internal notes visually distinct from external-visible content?
- [ ] Does the activity feed distinguish user actions from system events?
- [ ] Can the activity feed be filtered and searched?
- [ ] Do activity entries show old → new values, not just "updated"?
- [ ] Is the current owner and assignment chain visible?
- [ ] Does reassignment require context/instructions for the new owner?
- [ ] Are @mentions supported with autocomplete?
- [ ] Can users control notification frequency and channels?
- [ ] Are shared views distinguished from personal views?
- [ ] Are concurrent viewers/editors indicated?
- [ ] Are structured checklists used instead of freeform tracking?
