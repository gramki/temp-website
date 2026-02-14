# Executive Coaching Guide

## Purpose

This guide helps **leaders** communicate the PLE change and respond to **concerns and criticism** in a consistent, constructive way. Use it together with the [Stakeholder Concerns Matrix](stakeholder-concerns.md). The principles: acknowledge first, be specific, involve people, show don’t just tell, ask what they need, and follow through.

---

## How to Communicate Change

1. **Start with why** — SaaS positioning caused friction; we need clear ownership and a shared mental model. PLE gives us that.
2. **Be clear on what’s changing** — Domain vs. Win Engineering; engagement-composed teams; inner source; variability documentation; Council.
3. **Be clear on what’s not changing** — Platform quality bar; customer commitment; Studio remains separate and customer IP.
4. **Invite questions** — Leave time for Q&A; use concerns matrix to prepare.
5. **Point to next steps** — Rollout plan, pilot, where to find more (docs, Council, managers).

---

## Role-by-Role Coaching Scripts

### Domain Engineers

**Concern:** "I'll be stuck on engagements forever."

**Do:**
- Acknowledge: "That’s a valid concern."
- Be specific: "Engagement assignments are time-boxed (e.g. up to X months or rotation cycle). Your return to your Domain Team is guaranteed and we’ll document it."
- Show: "We’ll have a rotation plan and return dates in the staffing plan."
- Ask: "What would make you feel confident about the rotation model?"

**Don’t say:**
- "You’ll love engagement work."
- "We’ll figure it out as we go."
- "Just trust us."

---

### Solution Architects

**Concern:** "I'll be stretched too thin."

**Do:**
- Acknowledge: "This is a real risk we’re taking seriously."
- Be specific: "No SA will be assigned to more than [2–3] concurrent engagements. We’ll do capacity planning with your lead."
- Show: "We’ll have a staffing model that caps your load."
- Ask: "What engagement load feels sustainable to you?"

**Don’t say:**
- "We need you to be flexible."
- "It’s temporary."

---

### Engagement Leads

**Concern:** "I don’t control my team."

**Do:**
- Acknowledge: "Matrix accountability is hard; we’re not pretending otherwise."
- Be specific: "You own delivery outcomes. Domain Team Leads own platform quality and staffing. Here’s the RACI. Here’s the escalation path when there’s a conflict."
- Empower: "You have authority to escalate to [X] when team or scope issues block delivery."
- Ask: "What authority do you need to feel accountable for delivery?"

**Don’t say:**
- "Just make it work."
- "Build relationships."

---

### Integration Engineers / QA / Domain Analysts

**Concern:** "I'm a pawn."

**Do:**
- Acknowledge: "Being moved often can feel disempowering."
- Be specific: "Your home is [Domain Team or designated pool]. Engagements are assignments, not transfers. Your manager is [X]."
- Show career path: "Here’s how engagement breadth is valued and where it can lead."
- Ask: "What would help you feel more agency in this model?"

**Don’t say:**
- "This is how matrix organizations work."
- "Be flexible."

---

### Domain Team Leads / Maintainers

**Concern:** "I can't plan capacity."

**Do:**
- Acknowledge: "Unpredictability makes planning hard."
- Be specific: "We’re putting in engagement forecasting so you have [X weeks] visibility. [Y%] of your team is reserved for platform work."
- Involve: "We need your input on the capacity reservation model."
- Ask: "What visibility window do you need to plan effectively?"

**Don’t say:**
- "Engagements are the priority."
- "We’ll give you more headcount" (unless that’s the plan).

---

### SRE / Platform Operations

**Concern:** "Every engagement adds operational burden."

**Do:**
- Acknowledge: "We can’t scale ops linearly with every new customer."
- Be specific: "We’re defining operational readiness criteria. Engagements must meet them before go-live. We’re also investing in [tooling/runbooks/tiering] so each new instance doesn’t add the same load."
- Involve: "We need your input on the readiness criteria and scaling model."
- Ask: "What would make each new customer instance easier to operate?"

**Don’t say:**
- "We’ll hire more SREs."
- "It’s the same platform, how hard can it be?"

---

## Handling Resistance

- **Listen first** — Let the person state the concern fully before responding.
- **Acknowledge** — "I hear you" or "That’s a valid concern." Don’t dismiss.
- **Use the matrix** — Refer to [Stakeholder Concerns](stakeholder-concerns.md) for the worry, reality check, and mitigation.
- **Be specific** — Vague reassurance erodes trust. Use numbers, roles, and process (e.g. return dates, caps, escalation path).
- **Escalate if needed** — If you can’t resolve or the concern is systemic, escalate to Engineering Leadership or Council.
- **Follow up** — If you promise something (e.g. document, process), follow through and communicate when it’s done.

---

## Handling PLE Criticism ("That's Not Real PLE")

**Criticism:** "This isn’t real PLE."

**Response:** "We’re not claiming it is. We use PLE as the mental model and organizational frame: core assets vs. derived products, Domain Engineering vs. Win Engineering, clear ownership and variability. We’ve adapted it for our context—engagement-composed teams, inner source, lightweight variability. We call it ‘Zeta’s PLE framework’ or ‘PLE-inspired.’ The goal is alignment and scalable delivery, not SEI compliance."

**Criticism:** "Ephemeral teams will lose knowledge."

**Response:** "Win Engineering Teams can stay on a Customer Solution for up to ~2 years, so they’re not ephemeral in a weeks sense. We preserve knowledge through: (1) solution archetypes (blueprints, cookbooks, playbooks), (2) engagement retrospectives and decision logs, (3) rotation that brings people back to Domain Teams or other engagements, (4) Council-led pattern extraction. Knowledge lives in artifacts and practice, not only in permanent teams."

**Criticism:** "Inner source will hurt platform quality."

**Response:** "We govern it: Definition of Done, Domain Maintainer review, soft gate with tech debt tracking, Council oversight. Maintainers can reject or request changes; tech debt is tagged and remediated. The alternative—only Domain Teams changing platforms—creates an intake bottleneck and underuses Win Engineering expertise. We’re committed to keeping quality bar high."

**When to engage vs. redirect:**
- **Engage** when the person is open to nuance (e.g. "we adapt PLE for our context").
- **Redirect** when the conversation is about labels rather than outcomes (e.g. "Whatever we call it, the important thing is clear ownership and scalable delivery. Let’s focus on that.").

---

## Follow-Through and Trust-Building

- **Under-promise, over-deliver** — Don’t promise what you can’t guarantee (e.g. "we’ll never extend your rotation" unless that’s policy).
- **Document commitments** — If you promise return dates, caps, or process, put it in writing (staffing plan, charter, policy).
- **Close the loop** — When you implement a mitigation (e.g. rotation policy, capacity reservation), communicate it to the affected people.
- **Admit when something isn’t working** — If a mitigation fails or a concern was valid, acknowledge it and adjust. That builds more trust than defensiveness.

---

## References

- [Stakeholder Concerns](stakeholder-concerns.md) — Full matrix of concerns and mitigations
- [PLE Overview](../framework/ple-overview.md) — What we are and aren’t doing; anticipated criticisms and responses
- [Rollout Plan](rollout-plan.md) — Phases and milestones
