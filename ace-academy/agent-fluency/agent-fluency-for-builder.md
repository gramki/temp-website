# Agent Fluency for Builders — Rubric

> **v0.1 · last updated 2026-05-18**
> Source-of-truth for the rubric content. Edit here; regenerate the docx/xlsx deliverables from this file.

---

## TL;DR

- A capability rubric for **builders** — anyone whose team ships software. It measures **four dimensions** across **five levels (AF1–AF5).**
- Use it for **team capability mapping** and **individual development**. Do not use it for performance review or compensation.
- **Practitioner (AF3) is the expected level for every team member by November 2026** — regardless of role or seniority. Future hires will be assessed at hiring. G1 (intern) and G2 (Apprentice) hires will be trained to Practitioner through the academy program.
- **AF5 fluency** is mastery — rare (5–10% of a team). The **Agent Fluency Architect** role is a separate appointed position that AF5 fluency enables but doesn't entail.
- Pair this rubric with the per-role how-tos under `howto/` and the companion *Agent Fluency for Operators* framework (for non-builder functions, planned).

---

## What this is

A capability rubric describing what it looks like — in observable behavior — when you become fluent at using and building with AI agents.

Two intended uses:

- **Team capability mapping** — an honest snapshot of where the team is, to plan training, staffing, and tool investment.
- **Individual development** — a clear next step on a real growth path.

This is not a performance-review tool. Scores are conversation starters, not verdicts.

## Who this covers

"Builders" means anyone whose team ships software: Product Managers, developers, Engineering Managers, Program Managers, QA, SRE, designers, technical writers, data scientists and ML engineers, security engineers, DevOps and platform engineers, solutions engineers, and support engineers. If you're adjacent to the product and the system is yours to shape, you're a builder.

For Product Marketing, BizOps/RevOps/FinOps, IT, HR/TA, and Legal, see the companion *Agent Fluency for Operators* framework.

---

## Glossary

Terms used throughout the rubric. Each entry starts with a plain-English explanation, followed by the technical definition. External links point to authoritative or community-reviewed sources.

- **AF1–AF5.** The five levels on this rubric, from beginner to expert. They run from *Aware* (AF1) to *Multiplier* (AF5). These are distinct from any career-level convention (e.g., G3, L4).
- **AGENTS.md.** A file you put in your repository so that AI agents know how to work in your codebase. It's an open standard governed by the [Agentic AI Foundation](https://agentic.ai/) under the Linux Foundation. Over 30 agent tools read it.
- **CLAUDE.md.** Anthropic's version of a project-instruction file for Claude Code. Many teams symlink `CLAUDE.md → AGENTS.md` to maintain a single source.
- **SKILL.md / Agent Skills.** A packaged set of instructions that teaches an agent a specific capability. The open standard uses a folder containing `SKILL.md` (YAML frontmatter + Markdown body) and optional supporting files. Created by Anthropic; now supported by Claude Code, OpenAI Codex, Cursor, Google Gemini CLI, GitHub Copilot, and 25+ others.
- **MCP (Model Context Protocol).** A way to plug agents into external tools and data sources, like connecting a power strip to different appliances. It's an open standard. See [modelcontextprotocol.io](https://modelcontextprotocol.io/).
- **MCP connector.** A specific MCP server that wraps a particular tool. For example, a GitHub connector or an Atlassian connector.
- **Doer skill.** A skill that performs a task and produces output — the workhorse of agent skills.
- **Coach skill (Doer + Coach pattern).** A skill that does the task *and* explains its reasoning to you as it works. It helps less-experienced users learn while the work gets done. Once you're proficient, it has memory-aware suppression that switches to terse mode. It can also operate in **pair-programming mode**, alternating driver/navigator with you. This works especially well with approve-each-step autonomy.
- **Governor / Monitor skill.** An automated check that watches, audits, gates, or alerts on agent-driven work. It can run inline (e.g., a pre-commit hook) or out-of-band (e.g., a nightly audit or a cost watchdog).
- **Autonomy modes.** How much freedom you give an agent. The four levels are: *chat-only*, *approve-each-step*, *run-and-report*, and *fully autonomous*. The right mode depends on the task's risk and how easy it is to undo.
- **Scoped breadth.** The idea that agents work best when you give them four kinds of context: local, goal, failure-signal, and idiomatic. A single narrow input isn't enough. The per-role how-tos cover this in detail.
- **Work architecture.** A list of your recurring tasks for your role. It's the denominator for any "% of tasks" claim in this rubric. Managers and tech leads own its creation and quarterly refresh.
- **Spec-driven development (SDD).** A workflow where a written spec drives implementation, step by step: *constitution → spec → plan → tasks → implement*. Major frameworks: [GitHub spec-kit](https://github.com/github/spec-kit), [AWS Kiro](https://kiro.dev/), BMAD-METHOD. See [Martin Fowler — Understanding SDD](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
- **Multi-agent orchestration.** Patterns where multiple agents work together. Examples: a separate planner and executor, a supervisor with specialists, a critic reviewing another agent's output, or sub-agent invocation. You start using basic patterns at AF3 and design full systems by AF5.
- **Cross-cutting concerns.** Issues that span every task: PII, security, cost (token and infra spend), and irreversibility. You need to think about these no matter what you're building.
- **Frontier / mid-tier / fast models.** Approximate tiers as of 2026. Frontier models (Claude Opus, GPT-5) handle hard reasoning. Mid-tier models (Sonnet, GPT-5-mini) handle daily work. Fast/cheap models (Haiku, GPT-5-nano) handle high-volume or low-stakes loops.
- **Eval / eval harness / golden dataset.** A test suite for your prompts or skills. You compare output against expected results. Frameworks include [promptfoo](https://www.promptfoo.dev/) and [inspect](https://inspect.aisi.org.uk/).
- **Named failure modes.** Common ways agents go wrong. Learn these names so you can spot and discuss them:
  - *Hallucination* — the agent confidently states something wrong.
  - *Sycophancy* — the agent agrees with you even when you're wrong.
  - *Instruction drift* — the agent loses your original constraint partway through.
  - *Context poisoning* — bad output caused by contaminated prior context.
  - *Sandbagging* — the agent under-performs relative to what it can actually do.
  - *Jailbreak* — someone bypasses the agent's safety constraints.
  - *Prompt injection* — adversarial instructions hidden in untrusted content.
  - *Over-confident wrong answer* — the agent expresses high confidence with no justification.
- **Agent Fluency Architect.** A designated org role responsible for adoption strategy for a team, function, or the org. You need AF4–AF5 fluency to fill it, but the role is appointed, not earned by fluency alone.

---

## The four dimensions

Each dimension is scored independently from AF1 to AF5. You can sit at different levels on different dimensions — that's normal and useful.

- **Daily Use** — How effectively you delegate real work to agents and verify the output.
- **Building & Customization** — How well you extend agents with reusable assets. These include saved prompts, skills, plugins, MCPs, connectors, and workflows.
- **Judgment & Oversight** — How well you decide when to use an agent, when not to, and how to catch problems before they ship.
- **Org Influence** — How much you raise the fluency of people around you.

## The five levels

| Level | Name | One-line shorthand |
|-------|------|---------------------|
| AF1 | Aware | Heard of it; rarely uses |
| AF2 | Exploring | One-off prompts for low-stakes drafts |
| AF3 | Practitioner | Delegates real work reliably; verifies; uses team-shared practices |
| AF4 | Builder | Authors reusable assets; orchestrates workflows; operates what they ship |
| AF5 | Multiplier | Mastery across all four dimensions; raises team capability |

## Signature behaviors (the gestalt)

Use these as a quick self-check when full dimension scoring is overkill. The focus is on consistent, quantifiable progress — not occasional use.

- **AF1 — Aware.** You haven't really started. AI is an occasional curiosity for you, not a tool.
- **AF2 — Exploring.** You use agents for low-stakes, ad-hoc tasks. You haven't integrated them with your team's practices yet.
- **AF3 — Practitioner.** You route roughly **80% of your recurring day-to-day tasks** through an agent, with proper context and verification. You diligently use any team-shared assets that exist (AGENTS.md, team skills, prompt cookbook, configured MCPs). You don't run a parallel private setup. You're comfortable with simple multi-agent orchestration patterns.
- **AF4 — Builder.** That same 80% is now backed by reusable, recorded assets you've authored or contributed to. These include saved prompts treated as artifacts, SKILL.md skills, plugins, scheduled tasks, and custom MCPs. At least one other person on your team can use what you've built.
- **AF5 — Multiplier.** You have mastery across all four dimensions. You can set the stack and norms for your team's agent surface. You build shared infrastructure others depend on. You measurably shift your team's distribution upward over time.

---

## Setting measurable bars

Where this rubric uses concrete thresholds — "roughly 80%" of recurring tasks, "≥N reusable assets per quarter," and similar — the numbers are starting points, not absolutes. Managers and tech leads should arrive at the actual values with the team:

- The denominator depends on the team's **work architecture** (that is, the list of recurring tasks for each role). "80% of recurring tasks" only means something once you've listed what those tasks are.
- Counts (≥N assets, ≥N patterns documented per quarter) vary with team size, codebase, and pace. Pick numbers that reflect a real adoption stretch, not a low bar you've already met.
- Revisit these when the tooling landscape or the role itself shifts substantially. Thresholds that make sense in 2026 will look different in 2027.

The bar is not "did you hit the number." It's **"did you make the adoption progress the number was meant to capture."**

---

## Quick matrix

Compact reference. Each cell is a short summary. **For the full description of each level, see the *Dimensions in detail* section below.**

| Dimension | AF1 — Aware | AF2 — Exploring | AF3 — Practitioner | AF4 — Builder | AF5 — Multiplier |
|-----------|-------------|-----------------|---------------------|----------------|------------------|
| **Daily Use** | Rare use; no context | One-off prompts; no iteration | Multi-step delegation with context and verification; chooses autonomy mode per task; basic multi-agent patterns | Long agentic sessions; operates autonomous flows; sets autonomy deliberately; designs multi-agent workflows | Designs agent-as-production-system; team-wide trust adjustment |
| **Building & Customization** | None | Saved notes only | Personal Doer skills; uses team-shared assets | Team-shared Doer / Coach / Governor skills; instruments, documents, evals as craft | Curates team stack; sets quality bar; maintains team evals harness |
| **Judgment & Oversight** | Over- or under-trusts | Inconsistent verification | Verifies before acting; recognizes failure modes by name; cross-cutting concerns handled | Risk-scoped per task; cost limits; source-trust scoping; postmortems | Team risk policy; monitoring/control tooling; human-only work articulated |
| **Org Influence** | Practice stays private | Casual mentions | Documents and shares with peers on request | Demos, mentors, builds shared assets | Adoption strategy for the unit (team / function / org-wide) |

*Cells describe capabilities at each fluency level. AF5 cells describe what AF5 fluency enables. When applied at team scale (typically by an Architect), these capabilities become the team's defaults. AF5 fluency without the Architect role still has these capabilities — they just don't carry team-wide authority.*

---

## Dimensions in detail

Full descriptors per level, per dimension.

### Daily Use

How effectively you delegate real work to agents and verify the output.

- **AF1 — Aware.** You rarely or never use agents. When you do, you treat them like a web search — no context, no follow-up.
- **AF2 — Exploring.** You use one-off prompts for low-stakes drafts. Interactions are single-turn with no attachments. You often redo the work manually afterward.
- **AF3 — Practitioner.** You delegate multi-step tasks reliably. You provide context: attachments, examples, and constraints. You iterate within a session and catch obvious errors.

  You pick the right **autonomy mode** per task. For example, you use chat-only for exploration and approve-each-step for high-stakes work, rather than defaulting to one mode for everything.

  You're comfortable with simple multi-agent orchestration. This includes separating a planner agent from an executor, invoking sub-agents for sub-tasks, and using a critic agent to review another agent's output.

- **AF4 — Builder.** You run longer agentic sessions with tools and MCPs. You can decompose ambiguous goals and recover when an agent drifts.

  You use artifacts and scheduled tasks to make your work repeatable. You operate your own autonomous flows — responding to alerts, rolling back bad output, and holding on-call for what you ship.

  You deliberately set the autonomy mode per task (chat, approve-each-step, run-and-report, or fully autonomous) based on risk and recoverability. You design multi-agent workflows using patterns like supervisor, critic, and pair-programming where they fit.

- **AF5 — Multiplier.** You design workflows where agents handle the bulk of recurring jobs. You adjust trust per task based on observed quality.

  You mentor others on framing and verification. You treat the team's agent surface as a production system — with distribution, monitoring rotation, and postmortems.

### Building & Customization

How well you extend agents with reusable assets.

- **AF1 — Aware.** You do no customization. You use defaults only and don't know what skills, plugins, or MCPs are.
- **AF2 — Exploring.** You have a few favorite prompts saved in your notes. You re-type similar prompts each time you need them.
- **AF3 — Practitioner.** You diligently use any team-shared assets that exist — AGENTS.md, team skills, prompt cookbook, configured MCPs — instead of running a parallel private setup.

  You create **personal Doer skills** for your own recurring work. Save your most-used prompts as reusable files (called Doer skills — typically a SKILL.md file or a saved prompt). You connect relevant data sources like the Microsoft 365 stack, Atlassian stack, GitHub, and internal productivity tools. You know when a personal asset deserves to be promoted to a team-shared one.

- **AF4 — Builder.** You author **team-shared skills, plugins, or scheduled tasks** — in code or no-code. You write custom MCPs and connectors when needed. You chain tools and agents into reliable multi-step workflows.

  You pick the right abstraction per problem: a prompt, a skill, a plugin, or an MCP. You pick the right model per task (frontier for hard reasoning vs. fast/cheap for high-volume work) to balance cost and effectiveness.

  You design shared skills using a **Doer + Coach** pattern where appropriate. This means the skill explains its reasoning to less-experienced users and uses memory-aware suppression once they're proficient. You build **Governor/Monitor** skills as the system requires — automated checks that watch, audit, gate, or alert on agent-driven work, whether inline or out-of-band.

  You instrument shared skills and flows for observability: structured logs, named failure modes, and decision traces. You document shared assets for adoption — clear SKILL.md descriptions that trigger reliably, READMEs that teach, and version numbers so teammates aren't burned by silent changes.

  You treat evals as a craft. You maintain golden datasets and named success criteria. You know when LLM-as-judge is appropriate vs. heuristics.

- **AF5 — Multiplier.** You build shared internal tooling: skills, plugins, marketplaces, and custom MCPs/connectors. You integrate agents into CI/CD or production workflows where it makes sense.

  You curate the team's stack. You set the team's **model-selection guidance** — which model for which task class, with cost and quality tradeoffs documented. You set the **quality bar for shared skills**: Doer + Coach where relevant, clear SKILL.md descriptions, versioning, and eval coverage. You maintain the team's evals harness and adjust what to measure as the stack evolves.

### Judgment & Oversight

How well you decide when to use an agent, when not to, and how to catch problems before they ship.

- **AF1 — Aware.** You either over-trust agents (treating output as truth) or under-trust them (refusing to use them at all). You have no risk awareness.
- **AF2 — Exploring.** Your verification is inconsistent. You catch obvious errors but miss subtle ones. You may paste sensitive data into an agent without thinking.
- **AF3 — Practitioner.** You verify before acting on outputs. You know what tasks an agent should not do — for example, anything legal, financial, or irreversible.

  You handle **cross-cutting concerns** appropriately: PII, security, and cost. You **recognize common agent failure modes by name** (hallucination, sycophancy, instruction drift, prompt injection, and over-confident wrong answers) and watch for them in output.

  You treat external content (emails, web pages, third-party docs, user-supplied files) as a **prompt-injection risk**. You don't paste untrusted content into agents without thinking. You cite sources.

- **AF4 — Builder.** You scope risk per task: agentic for low-risk, human-in-the-loop for medium, manual for high.

  You catch subtle failure modes — sycophancy, instruction drift, context poisoning, sandbagging, and jailbreaks — not just hallucinations. You set up guardrails: redaction, separate connectors, scoped permissions, and **cost limits on autonomous flows**.

  You decide which connectors and sources are trusted. You don't let agents act on data from untrusted sources without human review. You know when an agent is the **wrong tool** for reasons beyond risk — craft, learning, taste, or accountability — and you choose human work deliberately. You write postmortems on agent failures with the same rigor as production incidents.

- **AF5 — Multiplier.** You define the team's risk policy, covering security, PII, cost, and irreversibility.

  You stand up the monitoring and control tooling the team needs: cost dashboards, audit logs, agent-output anomaly detection, and drift detection — building or adopting as appropriate. You articulate the team's position on what kinds of work stay human, and why.

  You review peers' agent setups for safety. You ensure every shared autonomous flow has a postmortem culture and a clear rollback path. You adjust team trust over time using real failure data.

### Org Influence

How much you raise the fluency of people around you.

- **AF1 — Aware.** You don't discuss AI use with peers. Your practice stays private.
- **AF2 — Exploring.** You mention AI casually but don't share specific techniques or artifacts.
- **AF3 — Practitioner.** You share prompts and workflows on request. You answer peer questions. You document what worked in a place teammates can find. You have a few patterns others reuse.
- **AF4 — Builder.** You run demos, write guides, and build shared assets. You mentor peers through the learning curve. You have a clear, defensible point of view on how the team should work.
- **AF5 — Multiplier.** You own adoption strategy for the unit you serve — which can be a team, a function, or org-wide depending on scope. You build shared infrastructure others depend on. You measurably raise the unit's average fluency over time.

---

## Skill role types

Three patterns of skill design that Builders and Architects should know.

- **Doer skills.** These perform the task and produce the output. At AF3, you create them at a personal scale (saved prompts and personal SKILL.md files for recurring work). At AF4+, you create them at team-shared scale, with distribution, docs, and eval coverage.
- **Coach skills (Doer + Coach pattern).** These perform the task *and* surface reasoning to less-experienced users. You learn while the work gets done. **Memory-aware suppression** switches to terse Doer mode once you're proficient. Coach skills can also operate in **pair-programming mode**, alternating driver/navigator with you. This works especially well with approve-each-step autonomy. They're generally only worth designing at team-shared scale (AF4+).
- **Governor / Monitor skills.** These watch, audit, gate, or alert on agent-driven work. They can be inline (a pre-commit check that critiques the agent's diff) or out-of-band (a nightly audit, a cost watchdog, or a PII scanner over agent outputs). They are first-class skills, not just dashboards. They're team-shared by nature (AF4+). The Architect ensures the team's stack has them where needed.

---

## Composite level

After scoring the four dimensions, summarize with a composite level.

**The cap.** Your composite cannot exceed your lowest dimension + 1. This is because weak Judgment caps the value of strong Daily Use. For example, if you score AF4 (Builder) in Daily Use but AF1 (Aware) in Judgment, your composite is AF2 (Exploring) — you're moving fast in a direction that may cost the team.

**Formula.** `composite = min(round(average), min(dimensions) + 1)` — only when all four dimensions are scored.

| Composite | How to read it | Manager action |
|-----------|----------------|----------------|
| AF1 — Aware | Mostly AF1s with maybe one AF2. | Has not started; needs orientation and a first win. |
| AF2 — Exploring | Average ~AF2 across dimensions. | Pair with an AF3+ buddy; assign a small recurring task to delegate. |
| AF3 — Practitioner | Average ~AF3, with no dimension below AF2. | Productive default — owns their own workflow. Encourage saving reusable assets. |
| AF4 — Builder | Average ~AF4, with no dimension below AF3. | Multiplies own output. Invest in their built assets; route junior peers to them. |
| AF5 — Multiplier | AF4+ across all dimensions, with at least two AF5s. | Rare. Treat as a force multiplier — fund their adoption work explicitly. |

---

## Level expectations

- **Practitioner (AF3) is the expected level for every team member by November 2026** — regardless of role or seniority. Senior people don't get a pass. Junior people aren't held to a lower bar.
- **All future hires** will be assessed for Practitioner-level agent fluency as part of the hiring process.
- **G1 (intern) and G2 (Apprentice) level hires** will be trained to Practitioner-level fluency through the academy training program.
- **Multiplier (AF5) should be rare** — typically 5–10% of a team. AF5 is a fluency level, not a role. The role that AF5 fluency enables is the **Agent Fluency Architect** (next section).

---

## Agent Fluency Architect (org role)

Separate from the fluency scale (AF1–AF5) is an org role: the **Agent Fluency Architect**.

The Architect is a designated position that owns adoption strategy for a team, function, or the broader org. The role is accountable for outcomes, not actions. The actions live in the AF4 and AF5 cells above. The outcomes are:

- A current, documented agent stack with model-selection guidance the team actually follows.
- A current, documented risk policy covering security, PII, cost, and irreversibility.
- A monitoring and control surface where cost, safety, and quality deviations get caught.
- Measurable upward movement in the unit's fluency distribution.
- Peers' agent setups elevated to the team's quality bar.

The Architect role is typically filled by someone at AF4 or AF5 fluency — the depth is the prerequisite — but the role is appointed, not earned by fluency. An organization typically has a small number of Architects who rotate focus across teams and functions where adoption needs the most lift.

AF5 fluency without the Architect role is still AF5 fluency. The capability exists without the designation.

---

## Evidence per dimension

Each score should be backed by something concrete you could point to.

**Daily Use**

- Recent chat transcripts or artifacts an agent produced for you.
- Workflows you have running regularly (scheduled tasks, recurring summaries).
- Time-on-task reductions on specific recurring jobs vs. the pre-agent baseline.
- Examples of deliberate autonomy-mode choice — when you kept chat-only, ran approve-each-step, or let it run fully autonomous, and why.
- Examples of multi-agent orchestration — separated planning from execution, used a critic, invoked sub-agents.

**Building & Customization**

- Library of Doer skills you've authored — personal SKILL.md files and saved prompts at AF3, team-shared skills and plugins at AF4+.
- Connectors and MCPs you've set up and use.
- Scheduled tasks or autonomous workflows that automate your recurring work.
- Governor/Monitor skills you've authored — automated checks that audit, gate, or alert on agent-driven work.
- Doer + Coach designs where relevant. Documented model-selection choices with cost and quality rationale.
- Instrumentation in shared skills — structured logs, named failure modes, decision traces — plus SKILL.md descriptions, READMEs, and versioning.
- An evals harness with golden datasets and named success criteria that runs on prompt or model changes.

**Judgment & Oversight**

- Specific examples of catching a failure mode by name — hallucination, sycophancy, instruction drift, prompt injection, context poisoning, sandbagging, jailbreak, or over-confident wrong answer.
- Tasks you explicitly chose not to delegate, with rationale (risk, craft, learning, taste, or accountability).
- Your approach to cross-cutting concerns — PII and sensitive data, security, cost (agent token and infra spend), and irreversible actions.
- Your stance on which sources and connectors are trusted. Examples of refusing to let agents act on data from untrusted sources.
- Postmortems you've written for agent failures, treated with the same rigor as production incidents.

**Org Influence**

- Docs, guides, or demos you've produced for others.
- Named peers who have leveled up because of your help.
- Shared assets (team skills, plugins, prompt libraries) others actually use.
- Adoption movement you can point to — distribution shifts in the unit you serve (team, function, or org-wide), and peers who have moved up a level.

---

## Anti-patterns at each level

If you see these patterns in yourself, you're likely stuck at the level below where you self-rate.

**Stuck at Aware → Exploring**

- You still do manual work that agents could clearly handle.
- You treat AI as a curiosity, not a tool.

**Stuck at Exploring → Practitioner**

- You blame "AI is bad" when output is poor, instead of adjusting your framing or context.
- You use single-turn prompts only, with no iteration.
- You don't provide attachments or examples to the agent.
- You re-type similar prompts each time instead of saving them as personal Doer skills.
- You default to one autonomy mode for every task.

**Stuck at Practitioner → Builder**

- You keep your personal Doer skills private. You don't promote any to team-shared status even when teammates would benefit.
- You only build solo workflows. You don't use connectors or scheduled tasks.
- You can't articulate when to reach for a skill vs. a plugin vs. a one-off prompt.
- You ship autonomous flows without alerting, rollback, or cost limits.

**Stuck at Builder → Multiplier**

- You build tools nobody else can run or understand.
- You hoard workflows rather than sharing them.
- You optimize your own throughput but don't move the team average.
- You're strong in one dimension but weak elsewhere. For example, heavy authoring with no mentoring, or great judgment with no published work.

---

## How to use this framework

1. **Self-assessment first.** Rate yourself AF1–AF5 on each dimension using the self-assessment worksheet. Note one piece of evidence per dimension.
2. **Manager reviews.** Your manager scores independently, then reviews any 2+ level gaps with you. The conversation is the deliverable — not the number.
3. **Pick one growth move per quarter.** Pick one dimension to advance and commit to a concrete behavior change (not a course).
4. **Re-measure quarterly.** Movement is the signal — track whether your team average is rising and where the bottleneck is.

**Cadence**

- Initial baseline: ~45 minutes per person (30 min self-assessment + 15 min manager review).
- Re-measure quarterly. Don't re-measure more often — movement is slow and noisy at shorter intervals.
- Refresh this rubric annually. Tools change fast.

**Pitfalls to avoid**

- Don't use scores for compensation or performance ratings. The moment people think scores affect pay, self-assessments stop being useful signal.
- Don't aggregate to leaderboards. The point is movement, not ranking.
- Don't conflate "uses AI a lot" with high fluency. Volume without verification is an AF2 anti-pattern.
- Don't grade others harder than you grade yourself. Assess against your own behavior first.

---

## Further reading

External resources for the concepts in this rubric. List dates quickly — refresh annually.

- **Agent Skills open standard** — Anthropic [Skills documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) and the [Agentic AI Foundation](https://agentic.ai/) (Linux Foundation), governing AGENTS.md and SKILL.md interop.
- **AGENTS.md** — [agents.md](https://agents.md/) for the format spec and adoption guide.
- **MCP (Model Context Protocol)** — [modelcontextprotocol.io](https://modelcontextprotocol.io/) for the spec and SDK references.
- **Spec-driven development** — [GitHub spec-kit](https://github.com/github/spec-kit), [AWS Kiro](https://kiro.dev/), and [Martin Fowler's overview of SDD tools](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
- **ADR (Architecture Decision Records)** — [adr.github.io](https://adr.github.io/) and [AWS Prescriptive Guidance on ADRs](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html).
- **Eval frameworks** — [promptfoo](https://www.promptfoo.dev/), [inspect (UK AI Safety Institute)](https://inspect.aisi.org.uk/), [OpenAI Evals](https://github.com/openai/evals).
- **Failure-mode literature** — Anthropic's [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) and red-team reports; [Apollo Research](https://www.apolloresearch.ai/) on sandbagging and scheming.
- **Multi-agent patterns** — Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) and the [multi-agent research workflows](https://www.anthropic.com/engineering/built-multi-agent-research-system) write-up.
- **Prompt injection** — [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [Simon Willison's prompt-injection corpus](https://simonwillison.net/tags/prompt-injection/).

This list is a starting point. The framework owner should refresh annually and add internal references as they emerge.

---

## Companion artifacts

These derive from this rubric. Keep them in sync via regeneration, not manual editing.

- `../Agent_Fluency_for_Builders_Rubric.docx` — printable rubric document.
- `../Agent_Fluency_for_Builders_Self_Assessment.xlsx` — worksheet for each team member.
- `../Agent_Fluency_for_Builders_Manager_Scorecard.xlsx` — for the manager, with team-level rollup.
- `howto/Developer.md` — practical how-to for software developers.
- *(Operators framework — planned, not yet drafted.)*

---

## Changelog

- **v0.1.1 — 2026-05-28.** Tone revision for junior builder audience. Rewrote to direct address ("you" voice throughout). Broke compound sentences for readability. Added plain-English definitions before technical terms in glossary. Split long level descriptors into lead sentence + supporting details. Introduced inline definition for "work architecture." Made anti-patterns and signature behaviors self-check oriented. No content removed; all substance, sections, AF1–AF5 numbering, level names, and external URLs preserved.
- **v0.1 — 2026-05-18.** Initial framework. Four dimensions (Daily Use, Building & Customization, Judgment & Oversight, Org Influence) × five levels (AF1–AF5). Includes: composite scoring with cap; guidance for setting measurable bars; Skill role types (Doer / Coach / Governor); Agent Fluency Architect role separated from fluency; multi-agent orchestration as AF3+ skill; named failure-mode literacy; prompt-injection awareness; cross-cutting concerns (PII, security, cost, irreversibility); model selection; autonomy modes; eval craft; instrumentation and observability; asset documentation and versioning; pair-programming via Coach skills; "scoped breadth" principle; Glossary; Further reading.
