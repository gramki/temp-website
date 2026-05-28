# ACE Academy — Overview

> **Agent Centric Engineering Academy**  
> A learning program to help everyone who builds software at Zeta work effectively with AI agents — not just use them casually, but rely on them as everyday collaborators with proper judgment and verification.

---

## What ACE Academy is

ACE Academy teaches you how to work **with** AI agents across the full software development lifecycle — writing code, testing, tracking work, collaborating, and communicating. It is not a single tool training. It is a structured path that covers **what good looks like** at each stage of adoption.

The academy is organized into **capability areas** (listed in the curriculum map below). Each area will have rubrics that describe expected behaviors, how-to guides with practical steps, and evidence you can show your manager. Today, **Agent Fluency** is the only area with complete materials; the rest are planned.

---

## Who it is for

Anyone whose work touches software delivery:

| Audience | What's available today | Coming next |
|----------|----------------------|-------------|
| Developers, QA, SRE, platform engineers | [Agent Fluency Rubric](./agent-fluency/agent-fluency-for-builder.md) + [Developer How-To](./agent-fluency/developer-howto.md) | More role-specific how-tos |
| Engineering managers, tech leads | Same rubric and how-to — managers reach AF3 first | Manager scorecard, team rollout playbooks |
| Product managers, designers, technical writers | Same rubric (if your team ships software, you're a "builder") | Role-specific how-tos |
| Product Marketing, BizOps, IT, HR/TA, Legal | — | *Agent Fluency for Operators* (separate framework, planned) |

### The AF3 target

**Practitioner (AF3)** is the organization-wide expectation for **all builders — including engineering managers and tech leads — by November 2026.** Future hires will be assessed at hiring. G1 (intern) and G2 (apprentice) hires will be trained to Practitioner through the academy program.

**Managers are not exempt.** You cannot credibly evaluate someone's agent fluency if you haven't built the same habits yourself. Complete the rubric and the developer how-to, and reach AF3 on your own day-to-day work, before you use the rubric to assess others.

---

## What should I do first?

1. **Read the rubric** — [Agent Fluency for Builders](./agent-fluency/agent-fluency-for-builder.md). Skim the five levels (AF1–AF5) and find yourself honestly.
2. **Work through the how-to** — [Developer How-To](./agent-fluency/developer-howto.md). Start with the section that matches your current level (most people start at *Reaching Practitioner*).
3. **Practice on real work** — the how-to gives you specific habits to try this quarter and evidence to collect.

---

## Curriculum map

| Area | Status | What it covers |
|------|--------|----------------|
| **Agent Fluency** | **Available** | How well you use agents, build reusable assets, exercise judgment, and help others improve |
| Building artifacts | Planned | Using agents to produce code, specs, tests, release notes, and other deliverables |
| Testing and verifying artifacts | Planned | Verification habits, evaluation harnesses, catching agent-specific mistakes |
| Project tracking and rituals | Planned | Agents in planning, standups, retros, and work tracking |
| Collaboration | Planned | Shared team practices — AGENTS.md files, team prompt libraries, tool connectors |
| Communication | Planned | Demos, documentation, and handoffs when work is agent-assisted |
| Learning | Planned | Academy rituals, progress measurement, and continuous improvement |

Supporting layers (for academy designers — will cut across all areas):

- **People** — roles and expectations, including the optional **Agent Fluency Architect** role.
- **Tools** — coding agents, spec-writing agents, test-authoring agents, task-planning agents, governing agents.
- **Processes** — how teams adopt and refresh practices without turning rubric scores into performance ratings.

---

## Agent Fluency (available now)

Agent Fluency answers one question: **what does good look like when a builder uses and builds with AI agents?** It defines five levels of fluency, from occasional use to team-wide mastery, measured across four independent dimensions.

### Documents

| Document | Read it for… |
|----------|-------------|
| [Agent Fluency for Builders — Rubric](./agent-fluency/agent-fluency-for-builder.md) | The levels (AF1–AF5), what each one looks like, how to score yourself |
| [Developer How-To: Agent Fluency](./agent-fluency/developer-howto.md) | Concrete habits, tool suggestions, evidence to collect, anti-patterns to avoid |

Read the **rubric first** for definitions. Read the **how-to second** for what to actually do.

### The four dimensions

You are scored on four independent dimensions. It is normal to be at different levels on different dimensions.

| Dimension | What it measures |
|-----------|-----------------|
| **Daily Use** | How effectively you delegate real work to agents and verify the output |
| **Building & Customization** | Whether you create reusable assets (saved prompts, skills, plugins, connectors) that others can use |
| **Judgment & Oversight** | Whether you know when to use an agent, when not to, and how to catch problems before they ship |
| **Org Influence** | Whether you help the people around you get better at working with agents |

### The five levels

| Level | Name | What it means |
|-------|------|---------------|
| AF1 | Aware | You've heard of AI agents but rarely use them |
| AF2 | Exploring | You use agents for one-off, low-stakes tasks — drafting a message, generating a snippet |
| AF3 | Practitioner | ~80% of your recurring tasks go through agents with proper context and verification. You use team-shared practices and basic multi-agent patterns. |
| AF4 | Builder | You create reusable tools (skills, plugins, connectors) that your team depends on. You design multi-agent workflows and operate what you ship. |
| AF5 | Multiplier | Mastery across all dimensions. You raise your team's capability. Rare — roughly 5–10% of a team. |

*AF3 is the target for all builders and people managers by November 2026.*

### How teams should use the rubric

1. **Managers first** — complete the learning and reach AF3 on your own work before mapping or scoring your team. You can only recognize AF3 behaviors if you practice them.
2. **Team capability mapping** — take an honest snapshot of where each person sits on each dimension. Use it to plan training and tool investment.
3. **Individual development** — use scores as conversation starters, **not** as performance-review or compensation inputs.
4. **Setting the bar** — managers define what "80% of recurring tasks" means for each role by listing the recurring tasks (called a "work architecture" in the rubric). The percentages in the rubric are starting points; adjust them with your team.

### Key concepts

These ideas come up repeatedly in the rubric and how-to. One-line teasers here; full definitions in the [rubric glossary](./agent-fluency/agent-fluency-for-builder.md#glossary).

- **Scoped breadth** — give agents four kinds of context (local, goal, failure signal, idiomatic), not just the symptom.
- **Autonomy modes** — how much freedom you give the agent, from chat-only to fully autonomous. Pick based on risk.
- **Multi-agent orchestration** — using multiple agents together. Basic patterns (plan/execute/review) expected at AF3.
- **Skill types** — Doer (performs a task), Coach (performs and explains), Governor (watches and gates).
- **Standards** — AGENTS.md, SKILL.md, and MCP — the open formats agents and tools converge on.
- **Named failure modes** — hallucination, sycophancy, instruction drift, prompt injection, and others. Verification is a distinct skill.

### Planned additions

- More role-specific how-tos (beyond developers)
- *Agent Fluency for Operators* (non-builder functions)
- Printable rubric and self-assessment worksheets

---

## How to navigate

```
ace-academy/
├── overview.md          ← you are here
├── README.md            ← quick index
└── agent-fluency/
    ├── agent-fluency-for-builder.md   ← rubric (read first)
    └── developer-howto.md             ← practical guide (read second)
```

**If you are a developer** aiming for AF3: start with the rubric's *Practitioner* row, then work through the [Developer How-To](./agent-fluency/developer-howto.md) section *Reaching Practitioner (AF3)*.

**If you are a manager**: follow the same developer path, then use the rubric for team conversations.

**If you are exploring other academy areas**: check back as new tracks are added. Agent Fluency is the foundation everything else builds on.

---

## Principles

- **Agents are production collaborators**, not magic autocomplete — context, verification, and shared practices matter.
- **Team-shared assets beat private setups** — when good prompts and skills exist for the team, use them instead of reinventing your own.
- **Fluency is multidimensional** — you can be AF4 on Daily Use and AF2 on Building. That's useful signal, not a single grade.
- **Adoption is measured by progress**, not checkbox compliance with rubric numbers.
- **Managers assess from fluency, not from slides** — reach AF3 yourself before scoring or coaching others.
- **Safety and judgment scale with autonomy** — the more freedom you give an agent, the more oversight, cost limits, and rollback paths you need.

---

## Document status

| Item | Version | Last updated |
|------|---------|--------------|
| Agent Fluency rubric | v0.1 | 2026-05-18 |
| Developer how-to | v0.1 | 2026-05-18 |
| This overview | v0.1 | 2026-05-28 |

Feedback and gaps: raise with academy maintainers or your team's Agent Fluency Architect when one is appointed.
