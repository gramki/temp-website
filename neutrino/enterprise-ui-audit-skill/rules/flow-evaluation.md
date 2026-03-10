
# Enterprise Workflow Flow Evaluation Rules

file: flow-evaluation.md
version: 2.0
purpose: Evaluate multi-screen enterprise workflow journeys for usability, continuity, decision support, handoff clarity, exception handling, and operational resilience.

---

# 0. Agent Instructions

You are an enterprise workflow flow evaluation agent. Your job is to assess end-to-end multi-step workflows — not individual screens in isolation, but the journey a user takes from flow entry to completion (or abandonment).

## 0.1 What You Will Receive

You may receive input from one or more of these sources, listed from richest to most limited:

- **Live application (browser/MCP)** — walk through the full flow interactively: trigger transitions, test exception paths, interrupt and resume, test concurrent access, observe real validation and loading behavior.
- **Figma or design file** (any form: exported file, shared link, plugin) — extract or infer the full page/screen sequence, interaction definitions linking frames, component states at each step, and variant states for error/exception paths to the extent the format allows. Proactively map the flow from prototype connections when available.
- **Interactive prototype** — click through each step, observe transitions and context carry-forward, trigger branching paths, test back navigation and interruption behavior.
- **Video recording** — observe real transition timing, loading between steps, context preservation, error recovery sequences, and handoff behavior. Note what the recording shows vs. what paths were not demonstrated.
- **Accessibility tree / DOM snapshot** — inspect step indicator semantics, form field associations per step, and focus management during transitions.
- **Screenshots (sequence)** — evaluate layout per step, state visibility, action clarity, and progress indication. Cannot assess transition quality, timing, or context preservation.
- **Textual inputs** — process diagrams (BPMN, flowcharts, swimlanes), step-by-step descriptions, user journey narratives.

When richer input sources are available, proactively use them to evaluate transition quality, exception paths, and interruption/resumption — rules that cannot be assessed from static screenshots.

## 0.2 How to Conduct the Evaluation

Step 1 — Identify the flow type (onboarding, approval, investigation, triage, etc.)
Step 2 — Identify the personas involved (who initiates, who reviews, who approves, who acts on the outcome)
Step 3 — Map the flow: list every step, transition, decision point, and handoff
Step 4 — Identify the happy path (normal completion) and all exception paths (rejection, rework, escalation, timeout, cancellation)
Step 5 — Evaluate each step and transition against every rule in this document
Step 6 — Evaluate the flow as a whole for end-to-end continuity, efficiency, and resilience
Step 7 — Produce the structured report defined in the Evaluation Output section

## 0.3 Evaluation Perspective

- Evaluate from the perspective of every persona involved, not just the initiator.
- Assume users process dozens or hundreds of items through this flow daily.
- Pay special attention to handoff points — these are where most operational failures occur.
- Exception paths deserve equal scrutiny to the happy path. In enterprise operations, exceptions are the norm, not the edge case.
- Consider what happens when the user is interrupted mid-flow and returns later.

## 0.4 Evaluation Depth by Input Source

| Capability | Screenshots | Figma | Prototype | Video | Browser |
|---|---|---|---|---|---|
| Step sequence and layout | Full | Full | Full | Full | Full |
| Transition quality | No | Partial (connections) | Full | Full (observe) | Full |
| Context preservation | No | No | Full (test) | Full (observe) | Full |
| Exception path design | Partial (if shown) | Partial (if pages exist) | Full (navigate) | Partial (if recorded) | Full |
| Timing and animation | No | No | Partial | Full | Full |
| Interruption/resumption | No | No | Partial (navigate away) | Partial (if recorded) | Full |
| Concurrent access | No | No | No | No | Full |
| Branching logic | Partial (if shown) | Partial (connections) | Full | Partial (if recorded) | Full |
| Progress indicators | Full | Full | Full | Full | Full |

**Key:** Full = can fully evaluate. Partial = can partially evaluate (note limitations). No = cannot evaluate (mark as N/E in report).

If you receive only a subset of the flow, evaluate what you can see, note missing steps, and flag rule categories that require the full flow.

If you receive only the happy path, evaluate it fully and flag the absence of exception paths as a Critical finding.

---

# 1. Purpose

These rules define how an evaluation agent should assess an end-to-end workflow, not just an individual screen. Flow evaluation examines the journey between screens, the transitions, the handoffs, and the overall coherence of a multi-step process.

Examples of enterprise flows:
- customer onboarding (account opening, KYC, document collection, activation)
- loan origination (application, credit check, underwriting, approval, disbursement)
- payment exception review (alert, investigation, resolution, reporting)
- dispute resolution (intake, evidence collection, adjudication, settlement, notification)
- ticket triage to closure (creation, categorization, assignment, resolution, verification, closure)
- compliance approval (submission, review, approval/rejection, remediation, re-review)
- KYC / KYB review (data collection, verification, risk assessment, decision, periodic re-review)
- procurement (requisition, sourcing, approval, purchase order, receipt, payment)
- incident management (detection, triage, escalation, resolution, post-mortem)

The objective is to determine whether the flow:
- supports efficient end-to-end task completion
- preserves user context and data across steps
- handles exceptions, rework, and rejection gracefully
- supports clean handoffs between roles and teams
- minimizes avoidable operational delays and errors
- supports interruption, resumption, and parallel work
- maintains auditability throughout
- provides appropriate feedback at every stage

---

# 2. Evaluation Methodology

The evaluating agent must assess the flow at five levels:

### Level 1: Step Quality
Does each individual step provide what the user needs to complete that step?

### Level 2: Transition Quality
Are the transitions between steps clear, predictable, and safe?

### Level 3: End-to-End Continuity
Does the flow hold together as a coherent journey? Is context preserved? Is progress trackable?

### Level 4: Exception and Recovery Handling
Does the flow handle errors, rejections, rework, and edge cases as first-class scenarios?

### Level 5: Operational Resilience
Does the flow support interruption, resumption, concurrent users, SLA tracking, and audit requirements?

For each step in the flow, the agent should answer:
- What is the user trying to achieve at this step?
- What information does the user need to make the decision or complete the action?
- Is that information available on this screen, or must the user go elsewhere?
- What decision is being made, and are the consequences clear?
- What action is required, and is the action label explicit?
- What can go wrong at this step, and how does the UI handle it?
- Who owns the next step, and is that ownership transfer explicit?
- What happens if the user stops here and comes back later?

---

# 3. Scoring Model

Each category is scored from 1 to 5:

| Score | Label        | Definition                                                                                  |
|-------|--------------|---------------------------------------------------------------------------------------------|
| 5     | Excellent    | Fully compliant. No violations. Flow is smooth, resilient, and well-instrumented.           |
| 4     | Good         | Compliant with minor polish opportunities. No operational risk.                             |
| 3     | Acceptable   | Functional but has notable gaps. Users can complete the flow but experience friction.        |
| 2     | Problematic  | Multiple violations. Flow breakdowns likely under real conditions. Error risk is elevated.   |
| 1     | Poor         | Critical violations. Flow is fragile, confusing, or likely to cause operational failures.    |

Severity:
- Critical = likely to cause operational failure, data loss, incorrect decisions, or compliance violations
- Major = likely to slow work, increase confusion, or require workarounds
- Minor = improvement opportunity that would increase efficiency or polish

Scoring constraints:
- If any Critical-severity rule is violated, the overall flow score cannot exceed 3.
- If any single category scores 1, the overall score cannot exceed 2.
- Exception path quality has a 2x weight multiplier — poor exception handling disproportionately impacts real-world operations.

---

# 4. Core Flow Principles

Enterprise workflow flows must prioritize:

1. **Task completion over screen elegance** — A flow that is visually plain but reliably guides the user to completion is better than a beautiful flow that confuses or breaks.

2. **Continuity over isolated screen quality** — A flow where individual screens are polished but transitions lose context is worse than a flow where screens are simple but context persists.

3. **Clear transitions over hidden logic** — Users must always know what happens when they move forward. Invisible routing, silent status changes, and background processing without feedback erode trust.

4. **Exception handling over happy-path-only design** — In enterprise operations, the "exception" path is used as frequently as (or more than) the happy path. Rejection, rework, escalation, and partial completion must be designed, not afterthoughts.

5. **Role clarity over implicit ownership** — At every handoff point, it must be unambiguous who is responsible for the next action. Ambiguous ownership is the most common source of stalled workflows.

6. **Recovery and resumption over fragile session behavior** — Users get interrupted. Sessions expire. Browsers crash. The flow must support saving progress and resuming without data loss.

7. **Auditability throughout** — Every step of the flow must be traceable: who did what, when, with what inputs, and what outcome.

8. **Feedback at every transition** — Users must receive confirmation that their action was accepted, what changed, and what happens next.

---

# 5. Flow Entry Rules

RULE FE1 — The flow entry point must establish context

When a user enters a flow, they must immediately understand:
- why they are here (what triggered this flow — a queue item, a notification, a manual action)
- what record or case they are acting on (with key identifiers visible)
- what the intended outcome of this flow is (what does "done" look like)
- where they are in the overall process (if entering mid-flow)

What to look for:
- Is the flow title or header descriptive (e.g., "Review Dispute Claim #4821" not just "Review")?
- Are key record identifiers visible (customer name, case number, amount)?
- If the user entered from a queue or notification, is the triggering context preserved?
- If the user is re-entering a previously started flow, is their prior progress acknowledged?

Good: Header reads "KYC Review — Acme Corp (App #7842)". Subheader: "Submitted Mar 5, 2026. Pending your review. Step 2 of 4."
Bad: Page title is "Form". No case number, no customer name, no indication of which step this is.

Severity: Major

RULE FE2 — Preconditions and blockers must be surfaced early

If completing the flow depends on prerequisites (documents uploaded, prior approvals, permissions, external data), these must be visible at or near entry — not discovered mid-flow.

What to look for:
- Are missing prerequisites shown before the user begins (not after they've filled out a form)?
- Are blockers presented as actionable items ("3 documents pending upload") not just warnings?
- Can the user see which prerequisites are met and which are outstanding?
- Is the user prevented from starting a flow they cannot complete, with an explanation?

Good: Entry screen shows a checklist: "✓ Identity documents uploaded. ✓ Credit check completed. ✗ Manager approval pending — request sent Mar 6." With a note: "You can begin the review but cannot submit until manager approval is received."
Bad: User fills out a 10-field form, clicks Submit, and sees: "Error: Manager approval required." All form data is lost.

Severity: Major

RULE FE3 — Re-entry must restore the user's prior state

When a user returns to a flow they previously started (saved draft, interrupted session, reassigned item), the UI must restore their context.

What to look for:
- Is the user returned to the step they left off on?
- Are their previously entered values preserved?
- Is a summary of prior progress shown ("You completed steps 1-3 on Mar 6. Resuming at step 4.")?
- Is it clear what has changed since they last worked on this item (new comments, status updates, assignment changes)?

Good: "Welcome back. You saved a draft of this review on Mar 6. 2 new comments have been added since your last visit. [Resume at Step 3] [Start Over]"
Bad: User opens a previously started item and sees a blank form with no indication of prior work.

Severity: Major

---

# 6. Step-to-Step Transition Rules

RULE FT1 — Every transition must be explainable

Before the user moves to the next step, they must understand:
- what happens when they continue (data is saved? status changes? notification sent?)
- where the item goes next (next step in their queue? transferred to another team?)
- who owns it after the transition (remains with them? moves to a reviewer? goes to a system queue?)
- whether the transition is reversible (can they come back and edit?)

What to look for:
- Does the "Continue" or "Submit" button indicate the consequence (e.g., "Submit for Compliance Review")?
- If the transition triggers notifications or external actions, is this stated?
- Is there a summary or confirmation before committing?
- For irreversible transitions, is a confirmation dialog shown with specific consequences?

Good: Button reads "Submit for Manager Approval". Clicking it shows: "This case will be assigned to the Approval Queue. You will not be able to edit after submission. Manager will be notified by email. [Cancel] [Submit for Approval]"
Bad: Button reads "Next". Clicking it silently moves the item to a different team's queue with no warning.

**Input modality:** If prototype is available, click through each transition to observe confirmation dialogs and consequence visibility. If video is available, observe transition timing and context carry-forward between steps. Screenshots can only evaluate button labels and visible confirmation content.

Severity: Critical

RULE FT2 — Step progression must be continuously visible

Users must see where they are, what they've completed, and what remains — at every step.

What to look for:
- Is a progress indicator visible on every step (stepper bar, breadcrumb, progress percentage)?
- Are completed steps visually marked as done?
- Is the current step highlighted?
- Are future steps visible (even if not yet accessible)?
- Are optional steps distinguished from required steps?
- Does the progress indicator update in real time?

Good: A horizontal stepper across the top: "1. Data Entry ✓ → 2. Document Upload ✓ → 3. Review (current) → 4. Approval → 5. Settlement". Visible on every screen in the flow.
Bad: No progress indicator. User has no idea how many steps remain or what the overall process looks like.

Severity: Major

RULE FT3 — Backward navigation must be safe and predictable

Users must be able to go back to previous steps without losing data or causing unexpected state changes.

What to look for:
- Can the user click on a completed step to review it?
- Is previously entered data preserved when navigating back?
- If editing a previous step invalidates later steps, is this communicated ("Changing the amount will require re-approval")?
- Is the browser back button handled (doesn't break the flow or lose data)?
- Are there guardrails if backward navigation would undo a committed action?

Good: User clicks "Step 2: Document Upload" in the stepper. Their Step 3 data is preserved. A note reads: "Changes to uploaded documents will require the review step to be repeated."
Bad: Clicking the browser back button exits the flow entirely and loses all progress.

Severity: Major

RULE FT4 — State changes between steps must not be surprising

Hidden or implicit state changes during transitions erode user trust and cause errors.

What to look for:
- Are all state changes that occur during a transition visible to the user?
- If automated actions occur during a transition (e.g., risk score recalculation, notification sent), is the user informed?
- Does the UI show what changed after a transition (confirmation banner, updated status)?
- Are there no silent field resets, recalculations, or reassignments?

Good: After clicking "Submit for Review", a confirmation banner reads: "Case #4821 submitted. Status changed to 'Under Review'. Notification sent to Compliance Team. Risk score recalculated: 72 → 78."
Bad: User submits a step and the risk score changes silently. The next reviewer sees a different score than what the submitter reviewed.

Severity: Major

RULE FT5 — Conditional branching must be transparent

When a flow branches based on user input, system rules, or data conditions, the branching logic must be visible.

What to look for:
- If the next step depends on the user's input (e.g., amount > $50k triggers additional approval), is this rule stated?
- Can the user predict which branch they'll enter?
- After branching, does the progress indicator update to reflect the actual path?
- Are skipped steps explained ("Step 4: Additional Approval — Skipped. Amount is within auto-approval threshold.")?

Good: Before submission: "Note: Amounts over $50,000 require an additional compliance review step." After submission: stepper updates to show the additional step.
Bad: The flow suddenly gains an extra step that wasn't visible before, with no explanation.

Severity: Major

---

# 7. Context Preservation Rules

RULE FC1 — User context must persist across the entire flow

Data entered or selected in earlier steps must remain accessible in later steps without re-entry.

What to look for:
- Are earlier inputs visible or reviewable from later steps (summary sidebar, review step)?
- If a later step references an earlier input, is the value shown (not just the field name)?
- Are temporary selections (filters, toggles, view preferences) preserved within the flow?
- If the flow spans multiple sessions (save and resume), is all context restored?

Good: Step 3 (Review) shows a summary panel on the right with all values from Steps 1 and 2, allowing the reviewer to verify without navigating back.
Bad: Step 3 asks the user to re-enter the customer ID that was already provided in Step 1.

Severity: Critical

RULE FC2 — Users must not re-enter information the system already has

Redundant data entry wastes time and introduces inconsistency.

What to look for:
- Are fields that can be derived from prior steps, the logged-in user, or the system context prefilled?
- If an earlier step collected the customer name, does a later step that needs it prefill it?
- If the user is resuming a flow, are their prior entries restored?
- Are cross-entity lookups performed automatically (e.g., entering an account number populates the customer name)?

Good: After selecting the customer in Step 1, all subsequent steps display the customer name, account number, and tier automatically.
Bad: Step 4 asks the user to type the customer's account number again.

Severity: Major

RULE FC3 — Supporting context must remain accessible throughout

Reference information the user may need at any step (prior notes, attachments, audit history, policy documents) must be reachable without leaving the flow.

What to look for:
- Can the user access case notes, attached documents, and prior communication at any step?
- Is the audit trail viewable within the flow (not only in a separate system)?
- Are policy or procedure references accessible inline or in a side panel?
- Does accessing supporting context preserve the user's current step position and entered data?

Good: A collapsible "Case History" panel is available on every step, showing prior actions, notes, and attachments. Opening it does not reset the current step.
Bad: To view attached documents, the user must navigate to a separate document management screen. Returning to the flow resets their progress.

Severity: Major

RULE FC4 — Cross-step data dependencies must be visible

When a value entered in one step affects validation, options, or behavior in a later step, this dependency must be transparent.

What to look for:
- If Step 2 options depend on Step 1 selections, is this relationship visible?
- If changing a Step 1 value invalidates Step 3 data, is the user warned before the change?
- Are cascading impacts shown ("Changing the product type will reset the pricing in Step 3")?

Severity: Major

---

# 8. Decision Support Rules

RULE FDV1 — Decision-critical information must appear before the commitment point

The information a user needs to make a decision must be visible on the screen where the decision is made — not on a prior step, not behind a click, not in a separate system.

What to look for:
- At each decision point (approve/reject, select an option, assign), is all necessary information visible?
- Is the user forced to leave the decision screen to gather information?
- Are comparison views provided when choosing between options?
- Are risk indicators, policy thresholds, and historical precedents shown at decision points?

Good: The approval screen shows: customer profile, claim amount, policy limit, risk score, prior claims history, and the analyst's notes — all on one screen. The approve/reject buttons are at the bottom with the full context above.
Bad: The approval screen shows only the claim amount and a "View Details" link that opens a new page.

Severity: Critical

RULE FDV2 — Consequences of major decisions must be explicitly stated

Before a user commits to a significant action (approval, rejection, escalation, closure), the UI must state what will happen.

What to look for:
- Does the UI explain the downstream effects ("Approving will trigger settlement of $12,450 to the customer's account within 48 hours")?
- Are irreversible consequences flagged ("This action cannot be undone")?
- Are notification effects stated ("Customer will be notified via email")?
- Is the impact on related records noted ("Closing this case will also close 3 linked sub-cases")?

Good: Confirmation dialog: "Approve Claim #4821 for $12,450? Settlement will be initiated within 48 hours. Customer will receive email notification. This case will be closed. 3 linked sub-cases will also be closed."
Bad: "Approve? [Yes] [No]" — no indication of amount, timeline, or side effects.

Severity: Critical

RULE FDV3 — The flow should reduce avoidable decision ambiguity

The UI should provide tools and context that help users make confident, consistent decisions.

What to look for:
- Are reason code dropdowns provided for decisions (approval reasons, rejection reasons, escalation reasons)?
- Are policy hints or thresholds shown ("Auto-approval threshold: $10,000. This claim is $12,450 — manual review required.")?
- Are precedent indicators available ("Similar claims in the last 90 days: 14 approved, 2 rejected")?
- Are checklists or guided criteria provided for complex decisions?
- Are mandatory documentation requirements enforced before decision ("Provide rejection reason and supporting notes")?

Good: Rejection form requires: reason code (dropdown), detailed notes (text area with minimum character count), and supporting document upload. Below the form: "Similar cases rejected in the last 90 days: 7. Most common reason: insufficient documentation (5 of 7)."
Bad: A single "Reject" button with no reason code, no notes, no context about precedents.

Severity: Major

RULE FDV4 — Decision review and verification must be supported

Before final commitment, users should be able to review all inputs and decisions in a summary view.

What to look for:
- Is there a review/confirmation step before final submission?
- Does the review show all inputs from all previous steps?
- Are key decision points highlighted in the review?
- Can the user navigate back to edit specific steps from the review screen?
- Are calculated or derived values shown with their source logic?

Good: A "Review & Submit" step displays all entered data in a read-only summary, organized by step. Each section has an "Edit" link. Key decisions are highlighted: "Decision: Approve. Amount: $12,450. Reason: Within policy limits."
Bad: No review step. The user clicks "Submit" from the last data entry step with no chance to verify.

Severity: Major

---

# 9. Handoff and Ownership Rules

RULE FH1 — Handoffs between users or teams must be explicit and structured

When a flow transitions from one person's responsibility to another's, this must be an explicit, visible event.

What to look for:
- Is the handoff step clearly labeled ("Assign to Compliance Review")?
- Does the UI show who the item is being assigned to (specific person or team/queue)?
- Is the sender required to provide context for the recipient (notes, priority, instructions)?
- Is the handoff confirmed with feedback ("Case #4821 assigned to Compliance Team. Expected response: 24 hours.")?
- Does the recipient's queue show enough context to start work without re-investigation?

Good: "Assign for Review" screen with fields: Assignee (dropdown of eligible reviewers or teams), Priority (dropdown), Due Date (date picker), Notes for Reviewer (text area). Confirmation: "Assigned to Sarah Chen, Compliance Team. Priority: High. Due: Mar 10, 2026."
Bad: A "Send" button with no indication of who will receive the item, what they need to know, or when action is expected.

Severity: Critical

RULE FH2 — Required handoff inputs must be structured

Unstructured handoffs lead to incomplete information reaching the next person.

What to look for:
- Are handoff forms structured with required fields (assignee, reason, priority, due date, notes)?
- Are reason codes or categorization required for routing?
- Are templates or standard note formats available?
- Is free-text the only option for communicating context (it shouldn't be)?

Good: Escalation form: Escalation Reason (dropdown: "Policy Exception", "Amount Exceeds Authority", "Customer Request", "Regulatory Requirement"), Priority (High/Medium/Low), Additional Context (structured text with template), Requested Action (dropdown: "Approve", "Review", "Override").
Bad: A single free-text "Notes" field with no structure. Half the handoffs arrive with "Please review" and no useful context.

Severity: Major

RULE FH3 — Pending ownership must never be ambiguous

At every moment, it must be clear who is responsible for the next action on a work item.

What to look for:
- Is there always a current owner visible (not "Unassigned" for extended periods)?
- Are queues monitored for unassigned items?
- Is there a timeout or escalation if no one picks up an unassigned item?
- Do handoff confirmations explicitly name the new owner?
- Is the handoff logged in the audit trail?

Good: Queue shows owner for every item. Items in "Unassigned" state for more than 2 hours are highlighted in yellow. Items unassigned for more than 4 hours trigger a notification to the team lead.
Bad: Items can sit in a queue with "Owner: —" for days with no escalation mechanism.

Severity: Critical

RULE FH4 — Handoff recipients must have sufficient context to act

The person receiving a handoff should not need to re-investigate the case from scratch.

What to look for:
- Does the recipient's view show a summary of all prior steps and decisions?
- Are the sender's notes and attachments visible?
- Is the original request or trigger visible?
- Are relevant data points carried forward (not just a case ID requiring lookup)?
- Is it clear what the recipient is expected to do?

Good: The reviewer's screen shows: case summary (auto-generated from prior steps), sender notes, attached documents, risk assessment from prior step, and a clear header: "Action Required: Review and approve or reject this KYC application."
Bad: The reviewer sees only a case ID and must click through multiple tabs to understand what needs to be done.

Severity: Major

RULE FH5 — Return-to-sender paths must be structured

When a reviewer sends an item back for rework, the original submitter must understand what needs to change.

What to look for:
- Does the return action require structured feedback (what was wrong, what needs to change)?
- Is the submitter notified of the return with specific instructions?
- When the submitter re-opens the item, are the reviewer's comments visible and linked to specific fields?
- Is the item's history preserved (original submission, rejection reason, resubmission)?

Good: Reviewer clicks "Return for Rework". Required fields: Rework Reason (dropdown), Specific Fields to Correct (multi-select of form fields), Detailed Instructions (text area). The submitter sees: "Returned by Sarah Chen on Mar 7. Reason: Incomplete documentation. Please upload updated financial statements for Q4 2025 and correct the revenue figure in Section 3."
Bad: Item reappears in the submitter's queue with status "Returned" and no explanation.

Severity: Major

---

# 10. Exception Path Rules

RULE FX1 — Exception paths must be first-class, designed flows

Exceptions are not edge cases — they are routine in enterprise operations. The flow must handle them as designed paths, not error conditions.

Common exception scenarios:
- missing or invalid data requiring correction
- validation failure at submission
- approval rejection requiring rework
- escalation to a higher authority
- timeout or SLA breach
- system integration failure (external service unavailable)
- cancellation or abandonment
- partial completion requiring resume
- duplicate detection requiring merge or discard

What to look for:
- Does each exception scenario have a designed UI path (not just an error message)?
- Can the user navigate the exception path without losing their work?
- Is the exception path as well-structured as the happy path?
- Are exception flows tested and polished, or do they feel like afterthoughts?

Good: When a reviewer rejects a KYC application, a structured "Rejection & Rework" flow begins: the rejector provides reasons, the submitter is notified with specific instructions, the item returns to the submitter's queue with the rejection context, and the resubmission follows a defined path back to review.
Bad: Rejection sends a generic email. The submitter must create a new submission from scratch with no link to the original.

Severity: Critical

RULE FX2 — Users must know how to recover from exceptions

When an exception occurs, the UI must provide a clear recovery path.

What to look for:
- Does the exception state explain what went wrong?
- Does it explain what the user needs to do to recover?
- Is recovery achievable within the flow (not requiring external action)?
- Are recovery actions explicit ("Upload the missing document", "Correct the highlighted fields")?
- Is previous work preserved so the user only needs to fix the specific issue?

Good: "Submission rejected: The uploaded ID document has expired. Please upload a valid ID issued within the last 5 years. Your other entries have been saved. [Upload New Document]"
Bad: "Submission failed. Please try again." — user re-enters everything.

Severity: Critical

RULE FX3 — Rework loops must be understandable and bounded

When an item is sent back for correction, the user must understand:
- how many times it has been through the loop
- what changed each time
- what the original vs. current values are
- whether there is a maximum number of rework cycles

What to look for:
- Is rework iteration count visible ("Rework attempt 2 of 3")?
- Is the history of prior submissions and rejections accessible?
- Are changes between iterations highlighted (diff view)?
- Is there an escalation path if rework cycles are exhausted?

Good: "Rework attempt 2 of 3. Prior rejections: Mar 5 (expired ID document), Mar 7 (revenue figure mismatch). Changes since last submission highlighted in yellow. If this submission is rejected again, the case will be escalated to the Regional Manager."
Bad: No indication of how many times the item has been reworked, no history of prior reasons, no escalation path.

Severity: Major

RULE FX4 — Timeout and SLA breach paths must be defined

What happens when a step in the flow exceeds its expected duration or SLA?

What to look for:
- Are SLA timers visible on pending items?
- Is there a defined path for SLA breaches (auto-escalation, notification, reassignment)?
- Are at-risk items visually flagged before breach (warning at 75% of SLA, critical at 90%)?
- Is the escalation path visible to the user ("If not acted on by Mar 10, this will escalate to the Team Lead")?

Good: Item shows "SLA: 4 hours remaining (of 24 hours)". At 75% SLA, the item turns yellow. At 90%, it turns red and the team lead is notified. At breach, it auto-escalates with full context.
Bad: Items sit in queues indefinitely with no visibility into how long they've been waiting.

Severity: Major

RULE FX5 — Cancellation and abandonment must be handled gracefully

What to look for:
- Can the user cancel a flow in progress with a confirmation step?
- Does cancellation preserve a record of what was done (for audit)?
- Is the reason for cancellation captured?
- Are downstream parties notified if a cancellation affects their queue?
- Are partially completed items clearly marked as "Cancelled" (not just removed)?

Good: "Cancel Application? This will close Application #7842 with status 'Cancelled — User Request'. All entered data will be preserved in the case history. Reason for cancellation: [dropdown]. The underwriting team will be notified."
Bad: "Cancel" button deletes the record with no confirmation, no reason capture, and no notification.

Severity: Major

---

# 11. Confirmation and Commitment Rules

RULE FCM1 — Confirmation screens must summarize all decisions and their consequences

Before a user commits to a significant action (submit, approve, reject, escalate), a summary must be shown.

What to look for:
- Does the confirmation screen list all key data points and decisions?
- Are downstream consequences stated (notifications, status changes, SLA starts)?
- Is the summary organized by step or category (not a wall of text)?
- Can the user go back to edit from the confirmation screen?
- Is the confirmation action button specific (not "OK" or "Yes")?

Good: "Review & Submit" screen: Customer: Acme Corp. Application Type: KYC Review. Risk Score: 72. Decision: Approve. Documents Verified: 4 of 4. Notes: "All documents current and verified." Action: Clicking "Approve Application" will notify the onboarding team and begin account provisioning. Status will change to "Approved — Pending Activation." [Edit] [Approve Application]
Bad: "Are you sure? [Yes] [No]"

Severity: Major

RULE FCM2 — Confirmation dialog action labels must describe the action

What to look for:
- Do dialog buttons use specific verbs matching the action ("Approve Application", "Reject Claim", "Delete Record")?
- Is the destructive action visually distinct (red)?
- Is the safe action (Cancel) visually de-emphasized?
- Are generic labels avoided ("Yes", "No", "OK", "Confirm")?

Good: [Cancel] [Approve Application] — where "Approve Application" is the primary blue button.
Bad: [No] [Yes] — with no indication of what "Yes" does.

Severity: Major

RULE FCM3 — Post-commitment confirmation must state what happened and what comes next

After the user commits, they need to know: it worked, what changed, and what happens next.

What to look for:
- Is there a success confirmation with specific details ("Case #4821 approved. Settlement of $12,450 will be processed within 48 hours.")?
- Is the next step or next likely action suggested?
- Is a reference ID or confirmation number provided?
- Can the user navigate to the next item in their queue easily?

Good: "Application #7842 approved. ✓ Notification sent to Onboarding Team. ✓ Account provisioning initiated. Expected activation: Mar 12, 2026. Reference: APR-2026-4821. [Return to Queue] [View Application]"
Bad: "Success." — no details, no reference, no next action.

Severity: Major

---

# 12. Interruption and Resumption Rules

RULE FI1 — The flow must support interruption at any point

Enterprise users are routinely interrupted by phone calls, urgent requests, and shift changes.

What to look for:
- Is auto-save implemented (saving progress without explicit user action)?
- Can the user explicitly save a draft at any step?
- Is the save state clearly communicated ("Draft saved at 2:34 PM")?
- Does the flow survive session expiration (data not lost if the user's session times out)?
- Does the flow survive browser crashes or accidental tab closure?

Good: Auto-save every 30 seconds with a visible "Saved" indicator. Explicit "Save Draft" button on every step. If the session expires, the user sees "You have a saved draft for Case #4821 from Mar 7, 2:34 PM" when they log back in.
Bad: No save mechanism. A 20-minute flow must be completed in a single session. Tab closure = total data loss.

**Input modality:** If browser access is available, test interruption directly — navigate away mid-flow, close the tab, and return to verify save/resume behavior. If video shows a user resuming a flow, observe the restoration experience. Screenshots and prototypes cannot fully evaluate this.

Severity: Major

RULE FI2 — Resumption must restore meaningful context

Returning to an interrupted flow must feel seamless.

What to look for:
- Does the user return to the exact step they left off on?
- Are all previously entered values restored?
- Is a summary of progress shown ("You completed Steps 1-3 on Mar 6.")?
- Are changes that occurred during the interruption surfaced ("2 new comments added since your last visit. The risk score was recalculated from 72 to 78.")?
- Is the user prompted to review changes before continuing?

Good: "Welcome back. Resuming KYC Review for Acme Corp. You were on Step 3: Risk Assessment. Since your last visit: 1 new document uploaded by the applicant, risk score updated from 72 to 78. [Review Changes] [Continue Where I Left Off]"
Bad: User opens the item and sees Step 1 with no indication of prior progress.

Severity: Major

RULE FI3 — Concurrent access and locking must be handled

What happens when two users attempt to work on the same flow simultaneously?

What to look for:
- Is optimistic locking or conflict detection implemented?
- Does the UI warn when another user is currently editing the same record?
- Are conflicts resolved gracefully (merge, last-write-wins with notification, or exclusive lock)?
- Is the lock holder identified ("Currently being edited by Sarah Chen since 2:15 PM")?

Good: "This case is currently being edited by Sarah Chen. You can view it in read-only mode. [View Read-Only] [Request Edit Access]"
Bad: Two users edit simultaneously, and one user's changes silently overwrite the other's.

Severity: Major

---

# 13. Parallel and Concurrent Path Rules

RULE FP1 — Parallel paths must be visible and trackable

Some enterprise flows have steps that can proceed in parallel (e.g., document review and credit check can happen simultaneously).

What to look for:
- Are parallel paths visually represented in the progress indicator?
- Can the user see the status of each parallel path?
- Is it clear which parallel paths must complete before the flow can advance?
- Is there a consolidated view showing progress across all parallel tracks?

Good: Flow diagram shows two parallel branches: "Document Review (In Progress)" and "Credit Check (Complete)". Both must complete before "Underwriting Decision" can begin.
Bad: Parallel tasks are invisible. The user sees a single-track stepper and doesn't understand why they can't proceed to the next step (a parallel task is blocking).

Severity: Major

RULE FP2 — Merge points must be clearly defined

When parallel paths converge, the merge logic must be transparent.

What to look for:
- Is it clear when all parallel paths are complete?
- Does the UI show which paths are still pending at the merge point?
- Is a summary of all parallel path outcomes available before proceeding?
- Are conflicts between parallel paths identified and resolved?

Severity: Major

---

# 14. Efficiency Rules

RULE FF1 — The flow must minimize unnecessary steps

Every step must earn its place. Steps that add no decision or action value should be eliminated or combined.

What to look for:
- Are there steps that only display information already available in the previous step?
- Are there steps that exist only for system/database reasons (not user reasons)?
- Could adjacent steps be combined without overwhelming the user?
- Are purely informational "read and acknowledge" steps necessary, or could the information be integrated elsewhere?

Good: A 4-step flow where each step involves a distinct user action (enter data, upload documents, review summary, approve). No redundant intermediate steps.
Bad: A 9-step flow where 3 steps are just "click Next to continue" with no user action required.

Severity: Major

RULE FF2 — Common expert paths should have accelerators

Repeat expert users who process hundreds of items daily need shortcuts.

What to look for:
- Can experts skip optional steps that don't apply?
- Are keyboard shortcuts available for common actions (approve, reject, next item)?
- Are bulk processing modes available for homogeneous items?
- Can frequently used configurations be saved as templates?
- Is a "quick action" mode available for simple items (approve directly from the queue without opening the full flow)?

Good: In the queue view, straightforward claims under $1,000 have an inline "Quick Approve" button. Keyboard shortcut 'A' approves the current item and advances to the next. Complex items open the full review flow.
Bad: Every item, regardless of complexity, requires the same 6-step flow to complete.

Severity: Minor

RULE FF3 — Bulk workflows must be supported for repetitive tasks

When users need to process many similar items, the flow must support batch operations.

What to look for:
- Can users select multiple items and apply the same action?
- Is the batch action confirmed with a count and summary?
- Are individual exceptions within a batch handled (some succeed, some fail)?
- Can users review and override individual items within a batch?
- Is batch progress shown during processing?

Good: "You selected 15 low-risk claims for batch approval. 14 meet auto-approval criteria. 1 requires manual review (Claim #4823 — amount exceeds threshold). [Approve 14] [Review Exceptions]"
Bad: Users must open and process each of 15 identical items through the full 6-step flow individually.

Severity: Major

RULE FF4 — The flow should support "next item" progression

After completing one item, users processing a queue should be able to immediately move to the next.

What to look for:
- Is there a "Next Item" button on the completion screen?
- Does "Next Item" respect the user's queue filters and sort order?
- Is the item count remaining shown ("14 items remaining in your queue")?
- Does the flow avoid returning to the queue list between items?

Good: "Case #4821 approved. ✓ [Next Case in Queue (14 remaining)] [Return to Queue]"
Bad: After every case, the user returns to the queue, must re-apply filters, and click the next item.

Severity: Minor

---

# 15. Audit Trail Rules (Flow-Level)

RULE FA1 — Every step transition must be logged

What to look for:
- Is there a flow-level audit trail (not just per-field change tracking)?
- Does the audit trail show: step entered, actions taken, decisions made, step completed, transition to next step?
- Are timestamps and user identities captured at each transition?
- Is the audit trail viewable within the flow?

Severity: Major

RULE FA2 — Decision rationale must be captured

What to look for:
- Are reason codes or structured justifications captured at decision points?
- Are free-text notes preserved as part of the audit trail?
- Can an auditor reconstruct the reasoning behind every decision by reading the audit trail?

Good: Audit trail entry: "Mar 7, 14:32 — Sarah Chen — Approved (Step 3: Underwriting Decision). Reason: Within policy limits. Risk score: 72 (acceptable). Notes: 'Customer has 5-year clean history. All documents verified.'"
Bad: Audit trail entry: "Mar 7 — Approved."

Severity: Major

RULE FA3 — System-initiated actions must be logged with the same detail as human actions

What to look for:
- Are auto-escalations, auto-assignments, auto-calculations, and system notifications logged in the audit trail?
- Is the triggering rule or condition recorded?
- Can an auditor distinguish between human and system actions?

Severity: Major

---

# 16. Notification Rules (Flow-Level)

RULE FN1 — Stakeholders must be notified at critical transition points

What to look for:
- Are the right people notified at the right times (not too many notifications, not too few)?
- Are notification triggers aligned with operational needs (handoff, completion, rejection, SLA warning)?
- Can users see what notifications were sent and to whom?
- Can notification preferences be configured?

Severity: Major

RULE FN2 — Notification content must be actionable

What to look for:
- Do notifications include enough context to act (case number, action required, link to the record)?
- Is the notification specific ("Case #4821 requires your approval. Amount: $12,450. SLA: 24 hours.")?
- Does the notification link take the user directly to the correct step in the flow (not just the case detail page)?

Good: Email/in-app notification: "Action Required: Approve or reject KYC Application #7842 for Acme Corp. Amount: $145,000. Risk Score: 72. SLA: 24 hours (due Mar 10, 14:00). [Open Application]" — link goes directly to the approval step.
Bad: "You have a new item in your queue." — no context, no link.

Severity: Major

---

# 17. Completion Rules

RULE FEND1 — Flow completion must confirm the outcome clearly

What to look for:
- Does the completion screen confirm what happened (decision, status change, downstream effects)?
- Is a reference number or confirmation ID provided?
- Is a summary of all key decisions and data points shown?
- Is the timestamp and completing user recorded?

Good: "KYC Review Complete. ✓ Application #7842 — Acme Corp — Approved. Risk Score: 72. Reviewed by: Sarah Chen on Mar 8, 2026, 14:32. Notification sent to Onboarding Team. Account activation expected: Mar 12, 2026. Reference: KYC-APR-2026-7842."
Bad: "Done." — no reference, no confirmation of what was decided.

Severity: Major

RULE FEND2 — Completion should support the next likely action

After completing one item, users typically want to:
- process the next item in their queue
- view the completed record
- return to their dashboard or queue
- start a new flow

What to look for:
- Are these next actions offered as clear options?
- Is the most common next action highlighted as primary?
- Does "Return to Queue" preserve the user's filters and position?

Good: "[Next Item in Queue (14 remaining)] [View Completed Application] [Return to Queue] [Start New Review]"
Bad: A blank page or the application's home screen with no suggested next action.

Severity: Minor

RULE FEND3 — Incomplete flows must be recoverable

What happens when a flow is not completed (user abandons, session expires, system error)?

What to look for:
- Are incomplete flows visible in a "Drafts" or "In Progress" section?
- Can incomplete flows be resumed from where they stopped?
- Are incomplete flows periodically reviewed for cleanup (stale drafts)?
- Can supervisors see which flows are stalled and intervene?

Severity: Major

---

# 18. Evaluation Output Format

The evaluating agent must produce the following structured report.

---

## Workflow Flow Evaluation Report

### Metadata

- Application: [application name]
- Flow: [flow name, e.g., "KYC Review", "Dispute Resolution"]
- Flow Type: [onboarding / approval / investigation / triage / settlement / other]
- Personas Involved: [list of roles who participate in this flow]
- Number of Steps: [total steps in the flow, including exception paths]
- Evaluator: [agent or human identifier]
- Evaluation Date: [date]
- Input Provided: [screenshots / recording / walkthrough / process diagram / prototype]
- Evaluation Limitations: [what could not be fully evaluated and why]

### Flow Map

[Describe or diagram the flow: list each step, decision point, handoff, and exception path evaluated.]

### Overall Assessment

Overall Score: X.X / 5.0
Verdict: [Excellent | Good | Acceptable | Problematic | Poor]

One-paragraph summary of the flow's quality, highlighting the strongest aspects and the most critical deficiencies.

### Category Scores

| Category                          | Score | Key Findings                                    |
|-----------------------------------|-------|-------------------------------------------------|
| Flow Entry (FE)                   | X/5   | [1-line summary]                                |
| Step Transitions (FT)            | X/5   | [1-line summary]                                |
| Context Preservation (FC)        | X/5   | [1-line summary]                                |
| Decision Support (FDV)           | X/5   | [1-line summary]                                |
| Handoff & Ownership (FH)        | X/5   | [1-line summary]                                |
| Exception Paths (FX)             | X/5   | [1-line summary]                                |
| Confirmation & Commitment (FCM) | X/5   | [1-line summary]                                |
| Interruption & Resumption (FI)  | X/5   | [1-line summary]                                |
| Parallel Paths (FP)              | X/5   | [1-line summary]                                |
| Efficiency (FF)                   | X/5   | [1-line summary]                                |
| Audit Trail (FA)                  | X/5   | [1-line summary]                                |
| Notifications (FN)               | X/5   | [1-line summary]                                |
| Completion (FEND)                | X/5   | [1-line summary]                                |

Mark categories that could not be evaluated as "N/E" with a note.

### Violations

List every violation in severity order (Critical first, then Major, then Minor).

| Field           | Value                                                              |
|-----------------|--------------------------------------------------------------------|
| Rule            | [Rule ID, e.g., FT1]                                              |
| Severity        | [Critical / Major / Minor]                                        |
| Step/Transition | [Which step or transition in the flow]                            |
| Description     | [What is the violation? Be specific.]                             |
| Evidence        | [What did you observe?]                                           |
| Impact          | [What operational risk does this create?]                         |
| Recommendation  | [Specific, actionable fix.]                                       |

### Exception Path Analysis

For each exception path identified (or expected but missing):

| Exception Scenario          | Designed Path Exists? | Quality | Notes                         |
|-----------------------------|-----------------------|---------|-------------------------------|
| Approval rejection/rework   | Yes/No                | X/5     | [How well is it handled?]     |
| Missing data/documentation  | Yes/No                | X/5     |                               |
| SLA breach/timeout          | Yes/No                | X/5     |                               |
| Cancellation/abandonment    | Yes/No                | X/5     |                               |
| System/integration failure  | Yes/No                | X/5     |                               |
| Duplicate detection         | Yes/No                | X/5     |                               |
| Escalation                  | Yes/No                | X/5     |                               |

### Strengths

List 3-5 things the flow does well, with specific rule IDs.

### Priority Recommendations

Rank the top 5 improvements by impact:

1. [Highest impact fix — rule ID, what to change, expected benefit]
2. [Second highest]
3. [Third]
4. [Fourth]
5. [Fifth]

### Not Evaluable

List any rule categories or specific rules that could not be evaluated, with what input would be needed.

---

# 19. Heuristic Summary

A strong enterprise workflow flow allows the user to answer at every step:

1. **Why am I here?** — The trigger and context for this flow are clear.
2. **What has happened already?** — Prior steps, decisions, and history are visible.
3. **What do I need to do now?** — The required action is explicit and supported with information.
4. **What information do I need to decide?** — Decision-critical data is on this screen.
5. **What will happen when I act?** — Consequences and downstream effects are stated.
6. **Who owns it after this?** — The next responsible party is explicitly identified.
7. **What if something goes wrong?** — Exception and recovery paths are designed and clear.
8. **What if I need to stop and come back?** — Interruption and resumption are supported.
9. **Can someone audit what I did?** — Every action is traceable.
10. **How do I get to the next item?** — Post-completion navigation is efficient.

If a user hesitates on any of these questions at any step, the flow has a gap.

---

# Appendix A: Rule Quick Reference

| Rule ID | Rule Name                                       | Severity |
|---------|--------------------------------------------------|----------|
| FE1     | Flow entry must establish context                | Major    |
| FE2     | Preconditions must be surfaced early             | Major    |
| FE3     | Re-entry must restore prior state                | Major    |
| FT1     | Every transition must be explainable             | Critical |
| FT2     | Step progression must be visible                 | Major    |
| FT3     | Backward navigation must be safe                 | Major    |
| FT4     | State changes must not be surprising             | Major    |
| FT5     | Conditional branching must be transparent        | Major    |
| FC1     | Context must persist across the flow             | Critical |
| FC2     | No re-entry of known information                 | Major    |
| FC3     | Supporting context must remain accessible        | Major    |
| FC4     | Cross-step data dependencies must be visible     | Major    |
| FDV1    | Decision info must appear before commitment      | Critical |
| FDV2    | Consequences must be explicit                    | Critical |
| FDV3    | Reduce avoidable decision ambiguity              | Major    |
| FDV4    | Decision review and verification                 | Major    |
| FH1     | Handoffs must be explicit and structured         | Critical |
| FH2     | Required handoff inputs must be structured       | Major    |
| FH3     | Pending ownership must never be ambiguous        | Critical |
| FH4     | Handoff recipients must have sufficient context  | Major    |
| FH5     | Return-to-sender paths must be structured        | Major    |
| FX1     | Exception paths must be first-class              | Critical |
| FX2     | Users must know how to recover                   | Critical |
| FX3     | Rework loops must be understandable              | Major    |
| FX4     | Timeout and SLA breach paths defined             | Major    |
| FX5     | Cancellation handled gracefully                  | Major    |
| FCM1    | Confirmation must summarize decisions            | Major    |
| FCM2    | Confirmation action labels must be specific      | Major    |
| FCM3    | Post-commitment confirmation must state outcome  | Major    |
| FI1     | Flow must support interruption                   | Major    |
| FI2     | Resumption must restore context                  | Major    |
| FI3     | Concurrent access and locking handled            | Major    |
| FP1     | Parallel paths visible and trackable             | Major    |
| FP2     | Merge points clearly defined                     | Major    |
| FF1     | Minimize unnecessary steps                       | Major    |
| FF2     | Expert paths should have accelerators            | Minor    |
| FF3     | Bulk workflows supported                         | Major    |
| FF4     | Next-item progression supported                  | Minor    |
| FA1     | Every step transition logged                     | Major    |
| FA2     | Decision rationale captured                      | Major    |
| FA3     | System actions logged with same detail           | Major    |
| FN1     | Stakeholders notified at critical transitions    | Major    |
| FN2     | Notification content must be actionable          | Major    |
| FEND1   | Completion must confirm outcome                  | Major    |
| FEND2   | Completion should support next action            | Minor    |
| FEND3   | Incomplete flows must be recoverable             | Major    |

---

# Appendix B: Flow Evaluation Checklist (Quick Pass)

Use this for rapid first-pass evaluation. Answer Yes/No for each:

- [ ] Is the flow entry point clear (why am I here, what record, what outcome)?
- [ ] Are preconditions and blockers surfaced before work begins?
- [ ] Can the user see their progress through the flow at every step?
- [ ] Are step transitions labeled with consequences (not just "Next")?
- [ ] Can the user go back without losing data?
- [ ] Is all decision-critical information visible at the decision point?
- [ ] Are consequences of major actions explicitly stated before commitment?
- [ ] Are handoffs structured with required context (not just "send")?
- [ ] Is ownership always clear (never "unassigned" without escalation)?
- [ ] Are exception paths designed (rejection, rework, timeout, cancellation)?
- [ ] Do rework loops include specific instructions?
- [ ] Is there a confirmation/review step before final commitment?
- [ ] Can the user save progress and resume later?
- [ ] Is an audit trail visible within the flow?
- [ ] Are notifications sent at critical transitions with actionable content?
- [ ] Does completion confirm the outcome and suggest next actions?
- [ ] Can expert users work faster (shortcuts, bulk, quick actions)?
- [ ] Is concurrent access handled (locking, conflict detection)?
- [ ] Are conditional branches transparent (user can predict the path)?
- [ ] Does the flow handle partial failures in batch operations?
