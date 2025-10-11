# Common Planning & Delivery Pitfalls

*Recognize the patterns before they become problems*

> **VP Insight**: "Once you can name the danger, you can design the defense."

## Pitfall Catalog

### Vague or Ambiguous Requirements

**Smells**: "make it faster", "as expected", "intuitive", "user-friendly", "like the old system but better", "seamless integration", "real-time processing"

**Drivers**: Business uncertainty; fear of locking in requirements too early; lack of concrete examples

**Harm**: Estimation chaos, design churn, UAT disputes, scope creep

**Countermeasures**: 
- Implement MAR (Minimally Acceptable Requirements) gates
- Use RfP (Ready-for-Planning) criteria
- Require acceptance criteria maturity before planning
- Create SOPs for requirement definition

**Ideal State**: Stories are testable before planning; acceptance criteria describe concrete system actions.

**Likely Reality**: Stakeholders provide intent and vision, not specific system actions.

**Survival Guide**: Enforce MAR standards; require at least one concrete example per acceptance criterion; block planning without mature acceptance criteria.

### Scope Creep and Silent Inflation

**Smells**: Mid-sprint tweaks, "just this small change", unlogged deltas, "while you're at it", "can you also add...", "the business really needs...", "it's just a configuration change"

**Drivers**: Weak change governance; unplanned dependencies; pressure to accommodate requests

**Harm**: Budget overruns, team fatigue, missed deadlines, quality compromises

**Countermeasures**:
- Implement formal change control and CR lifecycle
- Log all scope changes as debt or funded changes
- Regular operational reviews to catch drift

**Ideal State**: All changes are logged with impact assessment and formal approval.

**Likely Reality**: Verbal "just this one" changes accumulate without tracking.

**Survival Guide**: No change without impact assessment; escalate when change thresholds are exceeded.

### Goal as Feature / Outcome as Scope

**Smells**: "reduce cycle time by X%" treated as a deliverable feature; outcomes masquerading as scope; "improve customer satisfaction" as a user story; "increase revenue by 15%" as a technical requirement

**Drivers**: Language misalignment between business and delivery; pressure to show measurable value

**Harm**: Mis-scoped backlog; priority churn; unclear deliverables

**Countermeasures**:
- Structure contracts to separate outcomes from features
- Implement proper decomposition and traceability
- Map outcomes to measurable indicators

**Ideal State**: Outcomes map to measurable indicators; features are concrete outputs that contribute to outcomes.

**Likely Reality**: Business outcomes are treated as technical deliverables.

**Survival Guide**: Translate goals into feature sets; set acceptance criteria on system actions, not business outcomes alone.

### Misaligned "Done" and Acceptance

**Smells**: Subjective UAT, "works for me", late acceptance friction, different definitions of complete

**Drivers**: Weak acceptance criteria; multiple stakeholder definitions of done; unclear success criteria

**Harm**: Rework cycles, stalled acceptance, blame cycles, delayed releases

**Countermeasures**:
- Establish AC discipline and shared definitions
- Create defect-to-AC traceability
- Implement SOPs for acceptance processes

**Ideal State**: Shared acceptance rubric with traceable acceptance criteria to tests.

**Likely Reality**: "Works for me" disputes surface during UAT.

**Survival Guide**: Use AC checklists; require AC-to-test links in dashboards; establish clear acceptance gates.

### Reporting vs. Execution Misalignment

**Smells**: Green status slides but red sprint metrics; different views of project health

**Drivers**: Milestone optics prioritized over operational reality; different audiences, different metrics

**Harm**: Surprise escalations; credibility loss; misinformed decision-making

**Countermeasures**:
- Align dashboards across all audiences
- Map steering metrics to operational metrics
- Ensure governance alignment

**Ideal State**: Steering committees see the same health indicators that delivery teams see.

**Likely Reality**: Green slides mask red sprint boards.

**Survival Guide**: Publish the same dashboards to steering; add milestone mapping to operational views.

### Communication Gaps & Escalation Blindspots

**Smells**: Late asks over chat/email, decision reversals after verbal agreements, “we escalated but nothing moved,” parallel side‑channels.

**Drivers**: Undefined escalation ladders; missing decision logs; forum ownership unclear (EO vs Studio); alerts without owners; evidence not attached.

**Harm**: Slow decisions, contradictory directions, reputation damage, idle teams while leaders debate.

**Countermeasures**:
- Publish escalation ladders per domain (Operational, Quality, Commercial, Architecture, Behavioral) with role‑to‑role steps and ceilings (see Appendix B.3).
- Move decisions from chat to records: use the decision log; attach options, impacts, owner/date (Sections 9.9/9.10).
- Route alerts to a forum with an owner (Appendix B.1); block items with no forum/owner.
- Label owning org and chair on all forums (EO vs Studio) in invites and docs (Section 9.1).

**Ideal State**: Issues rise through defined ladders with evidence; decisions recorded within SLAs; side‑channels converge on the forum.

**Likely Reality**: Parallel threads and late senior interventions override forum outcomes.

**Survival Guide**: Stop the thread, post one decision page with options/evidence, tag the right forum/owner, and book the decision per SLA; mirror outcome to the log and dashboards.

### Deadline-Induced Expediency Debt

**Smells**: Skip tests, documentation, or NFRs "just this time"; "we'll fix it later"

**Drivers**: External deadlines; political commitments; pressure to deliver on time

**Harm**: Hidden technical debt; future regressions; reduced velocity over time

**Countermeasures**:
- Classify and track expediency debt
- Implement stabilization cadence
- Reserve capacity for debt repayment

**Ideal State**: Expediency is logged, classified, and repaid with a clear plan.

**Likely Reality**: "Just this time" becomes habitual practice.

**Survival Guide**: Classify shortcuts as expediency debt; cap expediency percentage; reserve stabilization capacity.

### Underestimating Dependencies and Integration Risk

**Smells**: "simple API" assumptions, environment readiness slips, version mismatches, "it's just a database call", "the vendor said it's plug-and-play", "we'll figure out the integration later"

**Drivers**: Poor interface scoping; third-party reliance; inadequate dependency mapping

**Harm**: Schedule slippage, cost overruns, cross-team friction

**Countermeasures**:
- Create detailed integration specifications
- Implement risk rituals and dependency tracking
- Establish interface contracts

**Ideal State**: Interfaces have contracts, environment readiness plans, and version compatibility matrices.

**Likely Reality**: "Simple API" reveals complex integration challenges.

**Survival Guide**: Maintain a dependency register; block work on missing contracts; plan for integration complexity.

### Poor Quality and Automation Investment

**Smells**: Flaky tests, late surge of defects, manual testing bottlenecks

**Drivers**: Feature pressure over quality; lack of automation guardrails; insufficient testing investment

**Harm**: Production bugs, rework cycles, technical debt accumulation

**Countermeasures**:
- Implement quality KPIs and SLOs
- Establish error budgets
- Create quality councils

**Ideal State**: Risk-based automation on critical paths; error budgets enforced; quality gates prevent regression.

**Likely Reality**: Flaky tests and late defect surges during crunch periods.

**Survival Guide**: Treat test flakiness as a defect; pause feature development when error budget is exhausted.

### Weak Change Management

**Smells**: Every change is urgent; verbal approvals; no formal change process

**Drivers**: No formal workflow; stakeholder override of processes; lack of change governance

**Harm**: Project volatility, team confusion, budget erosion

**Countermeasures**:
- Implement formal change governance
- Create CR templates and workflows
- Establish change approval processes

**Ideal State**: All changes have impact assessment, approver, and funding allocation.

**Likely Reality**: Shadow changes bypass formal processes.

**Survival Guide**: "No funding, no movement"; escalate unfunded change exposure above thresholds.

## Mitigation Sequence

When you detect a pitfall smell, follow this sequence:

1. **Name it early** — Use the pitfall label to create shared understanding
2. **Probe root driver** — Is this business urgency, requirement gap, dependency, or constraint?
3. **Quantify delta** — Assess effort, risk, dependencies → cost/time/quality impact
4. **Offer trade-offs** — Trim scope, defer features, version delivery, or secure funding
5. **Document decision** — Log in decision register; classify as change or debt
6. **Escalate proportionally** — Risk council/operational review/Steering based on thresholds
7. **Embed learning** — Retrofit dashboards/rituals; adjust guardrails to prevent recurrence

> **Pro Tip**: Add a 2-minute "pitfall scan" to planning ceremonies. Ask: "Which trap are we drifting toward this sprint?"