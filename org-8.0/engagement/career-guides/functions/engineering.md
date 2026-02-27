# Engineering — Function Coaching Guide

[← Back to Career Guides](../README.md) | [Career Paths — Engineering](../../career-paths.md#3a-engineering)

---

## Purpose

This guide helps engineers at every level understand what is expected of them within the Engagement Operating Model, how to build the craft needed at their current level, and how to prepare for the next. There is **one engineering ladder** — engineers work across Product Line, Customer Product, Studio, and Verification contexts through rotation. There are no separate "Platform" and "Engagement" tracks, and there are no QA, Test Engineer, or SDET titles.

---

## Junior Engineer

### Required Craft, Skills, Competencies

- **Craft:** Write production-quality code in the platform's primary stack. Write unit and integration tests as part of every change — testing is engineering, not a separate discipline. Read and navigate an existing Product Line codebase and its configuration layer.
- **Skills:** Follow the squad Definition of Done, including submitting work for EA mandatory review when the change is architecture-significant. Use the inner source contribution workflow (fork, PR, review by Product Line Maintainer) even if the contribution is small.
- **Competencies:** Ask for help early rather than guessing at integration boundaries. Accept code review feedback from seniors and from EA/AVA mandatory reviews without treating it as personal criticism — these reviews protect the assembly.

### Roles Expected to Play and Challenges

- **Squad engineer** in a CP, Studio, or PL Squad under an EL. Not yet expected to play EL, EA, or AVA.
- **Challenge:** Joining a squad that was assembled from multiple Product Line contexts — unfamiliar codebases, different conventions, engineers who will rotate back. Build context quickly by reading the archetype cookbook and the EA's solution architecture summary before writing code.
- **Challenge:** Understanding that "verification" is part of engineering work, not a handoff to a separate team. The AVA may require assembly-level tests that span your squad's boundary.

### How to Learn

- **On the job:** Rotate across at least two contexts (e.g. PL Squad, then CP Squad) within your first 18 months. Each context exposes different concerns — PL work teaches platform thinking; CP work teaches customer-specific integration; Studio work teaches reusable component design.
- **Feedback:** EL provides execution-axis input; your Engineering Manager provides functional-axis evaluation and tracks your cross-context exposure.
- **Knowledge sharing:** Attend PAC Practice Mode sessions as a listener. Review inner source PRs from other Engagements to see how senior engineers handle platform-level contributions.
- **External reading:** *Team Topologies* (Skelton & Pais) — why squad boundaries matter and how interaction modes (collaboration, X-as-a-Service, facilitation) apply to the PL/CP/Studio structure in this model.

---

## Engineer

### Required Craft, Skills, Competencies

- **Craft:** Design and implement features that extend a Product Line without forking. Understand the configuration layer well enough to implement customer-specific behaviour through configuration rather than code duplication. Write assembly-level tests when the AVA identifies integration seams that cross your squad's boundary.
- **Skills:** Run a gap analysis with the EA and produce an inner source vs. custom recommendation for a bounded scope. Participate in architecture-significant reviews with EA — present the design rationale, not just the code. Contribute inner source PRs that meet the Product Line Maintainer's quality bar on the first or second iteration.
- **Competencies:** Manage the tension between delivery pressure and EA's inner source bar without escalating prematurely — try to meet the bar first; bring concrete evidence if the bar is unreachable within the sprint. Understand that inner source contributions have a longer feedback loop than Engagement-only code and plan accordingly.

### Roles Expected to Play and Challenges

- **Squad engineer** in any context. May take on technical ownership of a feature area within the squad.
- **Challenge:** Inner source velocity — your squad EL's delivery commitment may conflict with the time needed to meet PL Maintainer standards. Document the trade-off (time to meet inner source bar vs. custom build risk) and bring it to the EL and EA together, not to one without the other.
- **Challenge:** Working in a Verification Squad context under AVA direction. The AVA is not an EL — direction comes through architectural authority, and work is verification infrastructure (IaC, CI orchestration, test data), not "test cases."

### How to Learn

- **On the job:** Seek cross-context rotation. If you have only worked in PL Squads, volunteer for a CP or Studio Squad assignment. If you have only worked in Engagements, spend a rotation cycle in a PL Squad maintaining the platform.
- **Feedback:** Dual-axis feedback — your EL rates squad delivery; your Engineering Manager evaluates growth across assignments and inner source contribution quality.
- **Knowledge sharing:** Propose an inner source contribution pattern from your Engagement for discussion at PAC Practice Mode.
- **External reading:** *Inner Source Patterns* (InnerSource Commons) — [innersourcecommons.org/learn/patterns](https://innersourcecommons.org/learn/patterns/) — practical patterns for cross-team contribution that directly apply to the PL Maintainer / Engagement contributor relationship in this model.

---

## Senior Engineer

### Required Craft, Skills, Competencies

- **Craft:** Design integration adapters that extend a Product Line without forking — understand the platform's extension points and configuration contract deeply enough to make "extend, don't fork" real. Own the technical design of a feature area that spans squad boundaries (e.g. an integration between CP and a PL component). Architect verification infrastructure when assigned to a Verification Squad under AVA.
- **Skills:** Lead gap analysis sessions with the EA — identify gaps between platform capability and customer need, evaluate inner source feasibility (effort, PL Maintainer capacity, timeline), and recommend build vs. contribute. Mentor junior engineers on the squad in inner source workflow, mandatory review preparation, and cross-context working.
- **Competencies:** Navigate the multi-authority environment (EL for delivery, EA for architecture, AVA for verification, EPM for coordination) without waiting for someone to resolve every ambiguity. When EA and EL disagree on inner source priority, bring data (effort estimate, PL Maintainer feedback, delivery impact) rather than taking a side.

### Roles Expected to Play and Challenges

- **Squad engineer** with feature-area ownership. On smaller Engagements, may play **EA or AVA** while remaining in the Engineering function (this is a role, not a cross-track jump — see [Career Paths](../../career-paths.md#4-cross-track-jumps)).
- **Potential EL candidate** — if moving into the management branch, see the EL role coaching guide.
- **Challenge:** Playing EA or AVA from the Engineering function requires architecture-level thinking (functional, commercial, operational synthesis for EA; verification system design for AVA) beyond deep technical skill. If you are asked to play EA, invest time understanding the archetype, the operating model choice, and the commercial context — not just the code.
- **Challenge:** Mentoring across unfamiliar contexts — a senior engineer in a CP Squad may mentor someone whose background is entirely PL. Bridge the gap by explaining the customer context that drives Engagement-specific decisions.

### How to Learn

- **On the job:** Take multi-Engagement assignments. Seniority at this level is demonstrated by breadth across Engagement contexts, not just depth in one platform. Ask your Engineering Manager to sequence assignments that build cross-PL exposure.
- **Feedback:** Request feedback from EA and AVA (not just EL) after each Engagement — they see your architecture-level judgment, which is critical if you are considering a cross-track jump into Architecture.
- **Knowledge sharing:** Lead a PAC Practice Mode session on a pattern you discovered or refined in an Engagement. Contribute to archetype documentation updates.
- **External reading:** *Software Product Lines: Practices and Patterns* (Clements & Northrop) — [link](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=5765) — foundational treatment of product line engineering and variability management, directly relevant to the "extend, don't fork" discipline and inner source contribution decisions.

---

## Staff Engineer (PE-1)

### Required Craft, Skills, Competencies

- **Craft:** Span multiple product line concerns — configuration contracts, platform extension points, cross-PL integration, inner source architecture. Design solutions that other Engagements can reuse. Define inner source contribution patterns that PL Maintainers will accept.
- **Skills:** Serve as EA or AVA on complex Engagements — lead the gap analysis, define the assembly acceptance criteria with AVA (or verification architecture with EA), and maintain the variability documentation. Provide architectural review of squad work across all squad types. Evaluate archetype fitness for a new Engagement and propose adaptations.
- **Competencies:** Operate effectively in the dual-authority space between Engineering function and Architecture role. When playing EA, exercise architectural authority without becoming a bottleneck — set standards, delegate squad-level design to ELs, and focus mandatory review on architecture-significant boundaries. Accept that your functional home is Engineering even when you are doing architecture work — the cross-track jump to Architecture is deliberate and separate (see [Career Paths](../../career-paths.md#4-cross-track-jumps)).

### Roles Expected to Play and Challenges

- **EA or AVA** on Engagements of medium complexity. **Senior squad engineer or technical lead** on complex Engagements where Architecture function members play EA/AVA.
- **Challenge:** The EA role demands more than technical depth — it requires functional, commercial, and operational synthesis. A Staff Engineer playing EA must understand why the customer chose a particular operating model, what the archetype covers vs. what the customer needs beyond it, and how inner source contributions affect the Product Line roadmap. This is architecture thinking applied from an engineering home.
- **Challenge:** When playing AVA, the hardest moment is exercising release-block authority under commercial and delivery pressure. The authority is independent — Client Partner, EO, and EPM cannot override it. Be prepared to defend a release block with certification evidence and to document the governance event if EO overrides.

### How to Learn

- **On the job:** Play EA or AVA on at least two Engagements before this level becomes your steady state. Request Engagements that use different archetypes or Product Lines to build breadth.
- **Feedback:** If you are considering a cross-track jump to Architecture, request a developmental review from Architecture leadership (not just Engineering leadership). They will evaluate your synthesis breadth, not just your technical depth.
- **Knowledge sharing:** Own or co-own an archetype update proposal. Contribute a case study to PAC Practice Mode documenting a non-obvious architecture decision from an Engagement.
- **External reading:** *Just Enough Software Architecture* (Fairbanks) — [link](https://www.georgefairbanks.com/e-book/) — practical guide to architecture risk-driven thinking, directly applicable to EA gap analysis and the "how much architecture is enough" question for each Engagement.

---

## Principal Engineer

### Required Craft, Skills, Competencies

- **Craft:** Deep technical IC spanning product line concerns. Define or reshape platform extension points that affect multiple Product Lines. Evaluate and evolve the inner source architecture — not just individual contributions, but the contribution model itself (submission standards, review turnaround, merge/reject criteria). Serve as a technical reference for EAs and AVAs across multiple Engagements.
- **Skills:** Assess platform readiness for a new Engagement archetype — identify where the platform's configuration contract is insufficient and what extensions are needed. Provide architectural guidance that influences archetype evolution. Review cross-Engagement inner source debt and recommend consolidation or deprecation.
- **Competencies:** Influence without authority across multiple Engagements and Product Lines. The Principal Engineer is not an EA or AVA by default — they are a technical compass that EAs, AVAs, and PL Maintainers consult. Navigate the tension between platform stability (PL Maintainers' concern) and Engagement velocity (ELs' and EPMs' concern) by proposing solutions that serve both.

### Roles Expected to Play and Challenges

- **Principal Engineer** is a terminal destination — a legitimate career endpoint in the Engineering function. It is not a waypoint to Architect; entering the Architecture function is a cross-track jump (see [Career Paths](../../career-paths.md#4-cross-track-jumps)).
- May play **EA** on highly complex Engagements, but this is role assignment, not a career change.
- **Challenge:** Maintaining influence across Product Lines and Engagements without a formal role in any specific Engagement. Your impact is through the quality of the platform, the inner source architecture, and the guidance you give to EAs — not through a delivery hierarchy.
- **Challenge:** Resisting the pull to become an "architecture function in disguise." If you find yourself making architecture decisions rather than providing technical input to architects, that is a signal to consider a cross-track jump.

### How to Learn

- **On the job:** Lead platform evolution initiatives that affect multiple Product Lines. Serve as a technical advisor to ERC on technology readiness for new Engagement types.
- **Feedback:** Your Engineering VP and Architecture leadership jointly assess your impact on platform quality and inner source health.
- **Knowledge sharing:** Contribute to PAC Governance Mode on standards that affect platform boundaries. Mentor Staff Engineers preparing for EA/AVA roles.

---

## Engineering Management Branch

### Engineering Lead (EL)

See the [EL Role Coaching Guide](../roles/engineering-lead.md) for role-specific coaching.

**Designation context:** EL is both a designation level (on the Engineering ladder, after Senior Engineer) and an Engagement role. An Engineering Lead who is not currently assigned to an Engagement may work as a senior engineer in a PL Squad or serve as a technical lead in other contexts.

### Engineering Manager

- **Craft:** Manage engineers on the functional axis across PL and Engagement contexts. Evaluate engineer growth across multiple Engagement assignments — you see the full history that no single EL sees.
- **Key model construct:** You are the career home for engineers who rotate through Engagements. Provide the continuity that Engagement roles cannot — multi-Engagement track record assessment, designation advancement, cross-PL rotation planning, inner source contribution recognition.
- **Challenge:** Providing meaningful career guidance when you are not in the Engagement where your reports work daily. Build relationships with ELs and EPMs so that execution-axis feedback flows reliably to you.

### Sr. Engineering Manager

- **Craft:** Own a segment of the Engineering function (e.g. multiple PL engineering teams). Shape engineering practice and standards in coordination with Architecture leadership and PAC.
- **Key model construct:** Resolve priority conflicts when multiple Engagements compete for the same engineering capacity. Work with PPM on demand consolidation and with ERC on heritage-matching for EO candidates from the Engineering function.
- **Challenge:** Balancing platform investment (long-term, PL Maintainer-driven) with Engagement velocity (short-term, delivery-driven). Neither side is wrong; the Sr. Engineering Manager is where these tensions are structurally resolved.

---

## Further Reading

| Resource | Why Relevant |
|----------|--------------|
| *Software Product Lines: Practices and Patterns* — Clements & Northrop ([SEI](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=5765)) | Foundational treatment of product line engineering; explains the variability management and "extend, don't fork" discipline that engineers practice daily |
| *Inner Source Patterns* — InnerSource Commons ([innersourcecommons.org](https://innersourcecommons.org/learn/patterns/)) | Practical patterns for cross-team contribution directly applicable to the PL Maintainer / Engagement contributor relationship |
| *Team Topologies* — Skelton & Pais ([teamtopologies.com](https://teamtopologies.com/book)) | Explains squad interaction modes (collaboration, X-as-a-Service, facilitation) that map to the PL/CP/Studio/Verification squad structure |
| *Just Enough Software Architecture* — Fairbanks ([georgefairbanks.com](https://www.georgefairbanks.com/e-book/)) | Risk-driven architecture thinking for engineers who play EA/AVA — helps calibrate "how much architecture is enough" per Engagement |
| *Understanding the InnerSource Checklist* — Cooper & Stol ([O'Reilly](https://www.oreilly.com/library/view/understanding-the-innersource/9781491986899/)) | Concise guide to inner source mechanics; useful for engineers learning the contribution workflow and PL Maintainer expectations |

---

[← Back to Career Guides](../README.md)
