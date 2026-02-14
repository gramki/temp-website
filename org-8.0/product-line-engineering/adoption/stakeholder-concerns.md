# Stakeholder Concerns Matrix

## Purpose

This document maps **concerns by role** so that leaders can anticipate and address them during PLE adoption. For each concern we summarize: The Worry, Reality Check, and Mitigation. Use this together with the [Executive Coaching Guide](executive-coaching-guide.md) when communicating with teams.

---

## 1. Domain Engineers

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'll be stuck on engagements forever"** | Fear of becoming permanent engagement staff, losing platform expertise | Win Engineering Teams are engagement-bound (e.g. up to ~2 years); rotation model guarantees return to Domain Team | Enforce rotation model; document return dates; reserve Domain capacity so return is meaningful |
| **"Engagement work is less interesting"** | Configuration/integration feels less creative than platform development | Some engineers prefer platform work; engagement work builds breadth and customer context | Honor preference where possible; frame engagement as "seeing your work in action"; don’t force everyone to rotate |
| **"My platform will suffer while I'm away"** | Platform quality degrades when senior engineers are on engagements | Risk is real if everyone is loaned at once | Reserve capacity; not all senior engineers on engagement at same time; Maintainers stay on platform |
| **"I'll have to clean up engagement team's PRs"** | Fear that inner source = more work reviewing or fixing bad code | DoD and Maintainer governance are designed to prevent this | DoD and governance in place; Maintainers can reject or request changes; tech debt is tagged and tracked |
| **"Career path unclear"** | Does engagement rotation help or hurt my growth? | Rotation can build breadth; platform depth is still valued | Articulate career paths (Domain depth vs. Win breadth); document how rotation is recognized |

---

## 2. Solution Architects

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'll be stretched too thin"** | Loaned to multiple engagements simultaneously | Real risk if SA capacity is overloaded | Cap concurrent engagements per SA (e.g. 2–3); capacity planning with Solution Architecture lead |
| **"Engagement Leads will override my decisions"** | Delivery pressure trumps architecture quality | Tension is real in matrix model | Clear authority: SA owns architecture and variability; EL owns delivery; escalation to Council for disputes |
| **"Archetype ownership is extra work"** | Maintaining archetypes on top of engagement work | Archetype work is part of the role | Allocate time for archetype maintenance; value archetype work in performance and recognition |
| **"I'm accountable but don't control the team"** | Responsible for solution quality, but team members report elsewhere | Matrix accountability is a real tension | RACI and escalation path; EL and SA alignment from engagement start; Council as escalation |
| **"Pattern extraction never happens"** | Too busy with current engagement to capture learnings | Risk if not institutionalized | Council forces cadence (monthly); knowledge capture checkpoints in engagement lifecycle; SA time for archetype updates |

---

## 3. Engagement Leads

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I don't control my team"** | Team members are loaned, have other loyalties | True matrix challenge | Clear RACI; EL owns delivery; Domain Team Leads commit to staffing; escalation path for conflicts |
| **"Inner source slows me down"** | PRs to platforms take time; reviewers become blockers | Tension between speed and quality | Soft gate + tech debt where justified; PR review SLAs; escalation if SLA missed |
| **"I'm accountable for quality I can't enforce"** | Customer blames me, but platform issues are out of my control | Boundary must be clear | Define platform vs. solution accountability; contracts and operating model clarify who owns what post go-live |
| **"Scope creep from customer"** | Customer expects more than solution archetype covers | Change management is part of the role | Archetype sets baseline expectations; change process and scope governance; EL owns scope discipline |
| **"Transition is messy"** | Handover to run team or customer is unclear | Operating model should clarify | Operating model (Fully Managed, Co-Managed, Customer-Operated) and handover criteria in contract and process |

---

## 4. Integration Engineers / QA / Domain Analysts

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'm a pawn"** | Moved from engagement to engagement without agency | Can feel disempowering if not framed well | Home team is Domain Team (or designated pool); engagements are assignments; career path values engagement breadth |
| **"No home team"** | Live in platform team but work on engagements; belong nowhere | Identity matters | Platform team is home; engagement is assignment; manager and career path are clear |
| **"Context switching is exhausting"** | Different customers, domains, tech stacks | Valid concern | Rotation cadence and engagement duration matter; avoid overly short rotations; protect learning time |
| **"Skills get stale"** | Always doing integration/QA; no time to learn platform depth | Growth matters | Training and growth time; option to deepen in one platform or broaden across engagements |

---

## 5. Domain Team Leads / Domain Maintainers

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I can't plan capacity"** | Engineers pulled to engagements unpredictably | Unpredictability is costly | Engagement forecasting; capacity reservation; visibility (e.g. weeks ahead) for loan requests |
| **"Inner source quality burden"** | I'm accountable for platform quality, but engagement teams contribute code | Maintainer role is gatekeeping + coaching | Maintainer authority to reject or request changes; DoD; tech debt tracking; Council escalation |
| **"My roadmap gets derailed"** | Customer-driven work (inner source) displaces platform roadmap | Balance needed | Reserve roadmap capacity; some customer-driven work is expected; Council can help prioritize |
| **"Tech debt piles up"** | Soft gate means substandard code merges | Must be tracked and remediated | Tech debt policy with tagging, ownership, and remediation timeline; Council oversight; reserved remediation capacity |
| **"No recognition for enabling others"** | Success is engagement's; problems are platform's | Recognition matters | Recognize platform contribution to wins; Maintainer and Domain Team impact in performance and communication |

---

## 6. SRE / Platform Operations

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"Every engagement adds operational burden"** | More customer instances = more to monitor, more incidents | Can’t scale linearly with engagements | Operational scaling model (e.g. tooling, runbooks, tiering); not every engagement gets same ops intensity |
| **"Solution operations is ambiguous"** | Operating model varies per engagement; hard to standardize | Complexity is real | Operating model templates (Fully Managed, Co-Managed, Customer-Operated); clear responsibility matrix |
| **"Engagement teams build things we have to run"** | Solutions deployed without operational readiness | Must be part of Definition of Done and handover | Operational readiness criteria in engagement lifecycle; handover checklist; SRE input to DoD where relevant |
| **"Incident escalation is chaotic"** | Who owns what when things break at 2am? | Must be clear per engagement | Escalation matrix per engagement; runbooks; operating model defines Zeta vs. customer responsibility |

---

## 7. Senior Leadership / Engineering Management

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"This is a big change"** | Restructuring at this scale is risky | True; phased adoption and pilots reduce risk | Phased rollout; pilot first; learn and adjust; communicate clearly |
| **"What if we lose people?"** | Change triggers attrition | Possible if concerns are ignored | Address concerns proactively; involve people in design where possible; use coaching guide |
| **"How do we measure success?"** | PLE benefits are hard to quantify | Define metrics upfront | Metrics per phase (e.g. time to compose team, inner source health, archetype reuse); measure before and after |
| **"What about existing engagements?"** | Transition mid-engagement is messy | New model for new engagements first | New engagements follow PLE; existing engagements migrate gradually; migration playbook |

---

## Priority Ranking

| Priority | Concern | Who Feels It | When to Address |
|----------|---------|--------------|-----------------|
| 1 | Rotation and return guarantees | Domain Engineers | Before pilot; reinforce throughout |
| 2 | Matrix accountability (who owns what) | Engagement Leads, Solution Architects | Before pilot; RACI and escalation in place |
| 3 | Inner source quality vs. speed | Domain Maintainers, Engagement Leads | At inner source launch; DoD and SLAs from day one |
| 4 | Career path clarity | All engineers | Phase 1–2; document and communicate paths |
| 5 | Capacity planning | Domain Team Leads | Before pilot; forecasting and reservation |
| 6 | Operational scaling | SRE | Phase 2+; operating model and readiness criteria |

---

## References

- [Executive Coaching Guide](executive-coaching-guide.md) — How to respond in conversation
- [Rollout Plan](rollout-plan.md) — Phases and milestones
- [PLE Overview](../framework/ple-overview.md) — What we are and aren’t doing
