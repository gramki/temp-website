# Stakeholder Concerns Matrix

## Purpose

This document maps **concerns by role** so that leaders can anticipate and address them during PLE adoption. For each concern we summarize: The Worry, Reality Check, and Mitigation. Use this together with the [Executive Coaching Guide](executive-coaching-guide.md) when communicating with teams.

For the complete Engagement role structure, see the [Engagement Operating Model Guide](../../engagement/README.md).

> **Why this document lives in PLE:** The concerns addressed here arise specifically from PLE adoption — the introduction of Product Line Squads, inner source, rotation, and the structural separation of platform and Engagement work. The concerns are organized by operating model role (defined in the [Engagement Operating Model](../../engagement/README.md)) because that is how people experience the change, but the change being managed is the PLE transformation.

---

## 1. Product Line Engineers

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'll be stuck on Engagements forever"** | Fear of becoming permanent Engagement staff, losing platform expertise | Engagement squads are Engagement-bound (e.g. up to ~2 years); rotation model guarantees return to Product Line Squad | Enforce rotation model; document return dates; reserve Product Line Squad capacity so return is meaningful |
| **"Engagement work is less interesting"** | Configuration/integration feels less creative than platform development | Some engineers prefer platform work; Engagement work builds breadth and customer context | Honor preference where possible; frame Engagement as "seeing your work in action"; don't force everyone to rotate |
| **"My platform will suffer while I'm away"** | Platform quality degrades when senior engineers are on Engagements | Risk is real if everyone is assigned at once | Reserve capacity; not all senior engineers on Engagement at same time; Maintainers stay on platform |
| **"I'll have to clean up Engagement team's PRs"** | Fear that inner source = more work reviewing or fixing bad code | DoD and Maintainer governance are designed to prevent this | DoD and governance in place; Maintainers can reject or request changes; tech debt is tagged and tracked |
| **"Career path unclear"** | Does Engagement rotation help or hurt my growth? | Rotation can build breadth; platform depth is still valued | Articulate career paths (Product Line depth vs. Engagement breadth); document how rotation is recognized |

---

## 2. Engagement Architects

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'll be stretched too thin"** | Assigned to multiple Engagements simultaneously | Real risk if EA capacity is overloaded | Cap concurrent Engagements per EA (e.g. 2–3); capacity planning with ERC |
| **"Engineering Leads will override my decisions"** | Delivery pressure trumps architecture quality | Tension is real in matrix model | Clear authority: EA owns architecture and variability; EL owns squad delivery; EPM resolves cross-role disputes; escalation to EO |
| **"How do I work with AVA?"** | Unclear boundary between architecture and verification | Peer relationship needs definition | EA and AVA are peers: EA owns architecture decisions; AVA owns verification/release. Architecture disputes default to EA; release disputes default to AVA. EPM resolves if needed |
| **"Archetype ownership is extra work"** | Maintaining archetypes on top of Engagement work | Archetype work is part of the role | Allocate time for archetype maintenance; value archetype work in performance and recognition |
| **"I'm accountable but don't control the team"** | Responsible for solution quality, but team members report elsewhere | Matrix accountability is a real tension | RACI and escalation path; EL and EA alignment from Engagement start; EPM and EO as escalation |
| **"Pattern extraction never happens"** | Too busy with current Engagement to capture learnings | Risk if not institutionalized | Council forces cadence (monthly); knowledge capture checkpoints in Engagement lifecycle; EA time for archetype updates |

---

## 3. Engineering Leads (ELs)

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I don't control my team"** | Team members are assigned, have other loyalties | True matrix challenge | Clear RACI; EL owns squad delivery; Product Line Squad Leads commit to staffing; EPM facilitates; escalation path for conflicts |
| **"Inner source slows me down"** | PRs to platforms take time; reviewers become blockers | Tension between speed and quality | Soft gate + tech debt where justified; PR review SLAs; escalation if SLA missed |
| **"I'm accountable for quality I can't enforce"** | Customer blames the squad, but platform issues are out of my control | Boundary must be clear | Define platform vs. solution accountability; contracts and operating model clarify who owns what post go-live |
| **"Scope creep from customer"** | Customer expects more than solution archetype covers | Change management is part of the operating model | Archetype sets baseline expectations; EPM manages scope discipline with Account Management; EL escalates to EPM |
| **"Transition is messy"** | Handover to run team or customer is unclear | Operating model should clarify | Operating model (Fully Managed, Co-Managed, Customer-Operated) and handover criteria in contract and process; SRE Lead drives operational readiness |
| **"Too many cooks"** | Navigating EO, EPM, EA, AVA, EPO feels like overhead | Real concern if roles are poorly coordinated | Clear escalation model (see guide); EPM integrates; regular alignment cadence reduces friction |

---

## 4. Engagement Program Managers (EPMs)

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'm pulled in too many directions"** | Customer-facing, commercial, squads, ERC — too many masters | Role breadth is by design, but overload is a risk | Clear role boundaries; ERC governs but does not micromanage; one EPM per Engagement (person may span multiple only if bandwidth permits) |
| **"ELs push back on my coordination"** | ELs own squad delivery and may resist EPM involvement | Healthy tension if boundaries are clear | EPM coordinates, does not direct engineering; EL owns squad; disputes escalate to EA then EO |
| **"Engagement Success is vague"** | Unclear what "adoption and value delivery" means in practice | Must be operationalized with metrics | Define Engagement Success metrics per Engagement (adoption, satisfaction, value delivery); EPM owns tracking |
| **"Account Management overlap"** | Who owns the customer relationship? | AM owns commercial; EPM owns delivery-facing relationship | Clear boundary: AM = contract and commercial; EPM = delivery communication and alignment; EPM keeps AM informed |

---

## 5. Assembly Verification Architects (AVAs)

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'll be the bottleneck"** | Every release needs my sign-off; squads will pressure me | Release authority is the point, but it must not become a chokepoint | Early involvement (from Discover); continuous certification (every increment, not just at release); AVA plans verification module proactively |
| **"EA will override my verification decisions"** | Architecture-driven release pressure | AVA release authority is independent and not overridable by EA | Clear escalation: verification/release disputes default to AVA; EA prevails on architecture; EPM resolves, then EO |
| **"I can't cover the full technical breadth"** | Assembly spans CP, Studio, PL — hard to verify everything | AVA must be a strong engineer; scope may be large | Select strong engineers for AVA; scope verification module to assembly points; squads own unit/component testing; AVA owns cross-squad integration |
| **"Verification module handover is thankless work"** | At Transfer, handing over the verification module is extra effort | Critical for operational quality | Recognize verification module as a first-class deliverable; include in handover criteria; SRE Lead and EPO collaborate on transition |

---

## 6. Engagement Product Owners (EPOs)

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"Squad PMs won't use my requirements"** | I detail requirements but squads prioritize differently | Squad PMs pick and prioritize within squad context | EPO feeds requirements; Squad PM prioritizes; disputes escalate through EPM then EA then EO |
| **"Customer training is undervalued"** | Training and enablement get cut when delivery pressure mounts | Enablement is critical for adoption | EPO owns training; EPM ensures it's in the plan; Engagement Success metrics include adoption |
| **"I'm caught between customer and EA"** | Customer wants something; EA says architecture won't support it | Healthy tension; both perspectives are needed | EPO and EA are peers; requirements-architecture translation is collaborative; EPM resolves if needed |

---

## 7. Integration Engineers / Product Line Analysts

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I'm a pawn"** | Moved from Engagement to Engagement without agency | Can feel disempowering if not framed well | Home team is Product Line Squad (or designated pool); Engagements are assignments; career path values Engagement breadth |
| **"No home team"** | Live in platform team but work on Engagements; belong nowhere | Identity matters | Platform team is home; Engagement is assignment; manager and career path are clear |
| **"Context switching is exhausting"** | Different customers, domains, tech stacks | Valid concern | Rotation cadence and Engagement duration matter; avoid overly short rotations; protect learning time |
| **"Skills get stale"** | Always doing integration work; no time to learn platform depth | Growth matters | Training and growth time; option to deepen in one platform or broaden across Engagements |

---

## 8. Product Line Squad Leads / Product Line Maintainers

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"I can't plan capacity"** | Engineers pulled to Engagements unpredictably | Unpredictability is costly | Engagement forecasting; capacity reservation; visibility (e.g. weeks ahead) for assignment requests; ERC Portfolio Program Manager maintains cross-Engagement view |
| **"Inner source quality burden"** | I'm accountable for platform quality, but Engagement teams contribute code | Maintainer role is gatekeeping + coaching | Maintainer authority to reject or request changes; DoD; tech debt tracking; Council escalation |
| **"My roadmap gets derailed"** | Customer-driven work (inner source) displaces platform roadmap | Balance needed | Reserve roadmap capacity; some customer-driven work is expected; Council can help prioritize |
| **"Tech debt piles up"** | Soft gate means substandard code merges | Must be tracked and remediated | Tech debt policy with tagging, ownership, and remediation timeline; Council oversight; reserved remediation capacity |
| **"No recognition for enabling others"** | Success is Engagement's; problems are platform's | Recognition matters | Recognize platform contribution to wins; Maintainer and Product Line Squad impact in performance and communication |

---

## 9. SRE / Platform Operations

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"Every Engagement adds operational burden"** | More customer instances = more to monitor, more incidents | Can't scale linearly with Engagements | Operational scaling model (e.g. tooling, runbooks, tiering); not every Engagement gets same ops intensity |
| **"Solution operations is ambiguous"** | Operating model varies per Engagement; hard to standardize | Complexity is real | Operating model templates (Fully Managed, Co-Managed, Customer-Operated); clear responsibility matrix; SRE Lead named per Engagement |
| **"Engagement teams build things we have to run"** | Solutions deployed without operational readiness | Must be part of Definition of Done and handover | Operational readiness criteria in Engagement lifecycle; SRE Lead active from Discover (advisory); AVA includes operational verification |
| **"Incident escalation is chaotic"** | Who owns what when things break at 2am? | Must be clear per Engagement | Escalation matrix per Engagement; runbooks; operating model defines Zeta vs. customer responsibility |

---

## 10. Engagement Owners (EOs)

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"Everything rolls up to me"** | Final accountability for the entire Engagement; hard to stay across all details | EO is the escalation endpoint, not the day-to-day operator | EPM, EA, AVA handle day-to-day in their domains; EO sets direction, unblocks, makes hard calls; clear delegation model |
| **"I'm accountable for roles I didn't choose"** | ERC assigns EPM and EA; EO inherits them | ERC provides "ingredients of success"; EO can flag concerns | EO raises concerns to ERC if assignment is a poor fit; ERC adjusts where possible |
| **"Multiple Engagements compete for my attention"** | EO may sponsor more than one Engagement | Real risk if portfolio is large | Cap EO load; EPM runs day-to-day; EO focuses on strategic decisions and escalations |

---

## 11. Squad Product Managers (Squad PMs)

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"Too many inputs"** | EPO, EL, EA, customer — everyone has priorities | Competing inputs are by design; prioritization is the job | Clear escalation: Squad PM prioritizes within squad; disputes go through EPM then EA then EO |
| **"I'm not the real PM"** | EPO owns customer-level requirements; I'm just backlog grooming | Squad PM owns squad-level prioritization; EPO owns customer discovery | Roles are complementary, not competing; Squad PM translates EPO requirements into actionable sprint items |
| **"Architect reviews slow us down"** | EA and AVA reviews add overhead to sprint delivery | Reviews are mandatory but should be lightweight and integrated | EA/AVA attend key ceremonies; review is part of DoD, not a gate after the fact |

---

## 12. Portfolio Program Managers (PPMs)

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"Demand visibility is poor"** | Can't consolidate demand if ELs and EPMs don't submit requests consistently | Process discipline is required | Standard request format; EPM ensures squad-level requests flow through PPM; ERC enforces the process |
| **"Product Line Squad leads don't commit"** | Capacity negotiations are slow; PL Squad leads protect their people | Healthy tension; both Engagement delivery and platform work matter | Engineering Leadership resolves priority conflicts; PPM presents data-driven portfolio view; escalation path is clear |
| **"I'm a bottleneck"** | Centralizing demand through one role could slow everything down | Risk if PPM is under-resourced or over-centralized | PPM is a coordination function, not an approval gate; ELs and PL Squad leads can communicate directly for urgent needs; PPM maintains the portfolio view |

---

## 13. Senior Leadership / Engineering Management

| Concern | The Worry | Reality Check | Mitigation |
|---------|-----------|---------------|------------|
| **"This is a big change"** | Restructuring at this scale is risky | True; phased adoption and pilots reduce risk | Phased rollout; pilot first; learn and adjust; communicate clearly |
| **"What if we lose people?"** | Change triggers attrition | Possible if concerns are ignored | Address concerns proactively; involve people in design where possible; use coaching guide |
| **"How do we measure success?"** | PLE benefits are hard to quantify | Define metrics upfront | Metrics per phase (e.g. time to compose team, inner source health, archetype reuse); measure before and after |
| **"What about existing Engagements?"** | Transition mid-Engagement is messy | New model for new Engagements first | New Engagements follow PLE; existing Engagements migrate gradually; migration playbook |
| **"Too many new roles"** | EO, EPM, EA, AVA, EPO, SRE Lead, EL — will this create overhead? | Role clarity reduces overhead compared to undefined responsibilities | Each role has clear accountability; escalation model prevents ambiguity; start with pilot to validate |

---

## Priority Ranking

| Priority | Concern | Who Feels It | When to Address |
|----------|---------|--------------|-----------------|
| 1 | Rotation and return guarantees | Product Line Engineers | Before pilot; reinforce throughout |
| 2 | Matrix accountability (who owns what) | Engineering Leads, Engagement Architects, EPMs | Before pilot; RACI and escalation in place |
| 3 | Inner source quality vs. speed | Product Line Maintainers, Engineering Leads | At inner source launch; DoD and SLAs from day one |
| 4 | Career path clarity | All engineers | Phase 1–2; document and communicate paths |
| 5 | Capacity planning | Product Line Squad Leads | Before pilot; forecasting and reservation |
| 6 | New role onboarding | EPMs, AVAs, EPOs, EOs, Squad PMs, PPMs | Before pilot; role guides and training |
| 7 | Demand coordination and capacity visibility | PPMs, Product Line Squad Leads | Before pilot; PPM process and tooling |
| 8 | Operational scaling | SRE | Phase 2+; operating model and readiness criteria |

---

## References

- [Engagement Operating Model Guide](../../engagement/README.md) — Complete role structure and escalation model
- [Executive Coaching Guide](executive-coaching-guide.md) — How to respond in conversation
- [Rollout Plan](rollout-plan.md) — Phases and milestones
- [PLE Overview](../framework/ple-overview.md) — What we are and aren't doing
