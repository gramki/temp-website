# Agent Fluency for Builders — Rubric

> **v0.1 · last updated 2026-05-18**
> Source-of-truth for the rubric content. Edit here; regenerate the docx/xlsx deliverables from this file.

---

## TL;DR

- A capability rubric for **builders** — anyone whose team ships software. **Four dimensions × five levels (AF1–AF5).**
- Use it for **team capability mapping** and **individual development**. Not for performance review or compensation.
- **Practitioner (AF3) is the expected level for every team member by November 2026** — regardless of role or seniority. Future hires will be assessed at hiring; G1 (intern) and G2 (Apprentice) hires will be trained to Practitioner through the academy program.
- **AF5 fluency** is mastery — rare (5–10% of a team). The **Agent Fluency Architect** role is a separate appointed position that AF5 fluency enables but doesn't entail.
- Pair this rubric with the per-role how-tos under `howto/` and the companion *Agent Fluency for Operators* framework (for non-builder functions, planned).

---

## What this is

A capability rubric describing what it looks like, in observable behavior, when a builder becomes fluent at using and building with AI agents.

Two intended uses:

- **Team capability mapping** — an honest snapshot of where the team is, to plan training, staffing, and tool investment.
- **Individual development** — a clear next step on a real growth path.

Not a performance-review tool. Scores are conversation starters, not verdicts.

## Who this covers

"Builders" means anyone whose team ships software: Product Managers, developers, Engineering Managers, Program Managers, QA, SRE, designers, technical writers, data scientists and ML engineers, security engineers, DevOps and platform engineers, solutions engineers, and support engineers. If you're adjacent to the product and the system is yours to shape, you're a builder.

For Product Marketing, BizOps/RevOps/FinOps, IT, HR/TA, and Legal, see the companion *Agent Fluency for Operators* framework.

---

## Glossary

Terms used throughout the rubric. External links point to authoritative or community-reviewed sources.

- **AF1–AF5.** The five fluency levels of this rubric, from *Aware* (AF1) to *Multiplier* (AF5). Distinct from any career-level (e.g., G3, L4) convention.
- **AGENTS.md.** Open standard for repository-level agent instructions, governed by the [Agentic AI Foundation](https://agentic.ai/) under the Linux Foundation. Read by 30+ agent tools.
- **CLAUDE.md.** Anthropic's project-instruction file for Claude Code. Many teams symlink `CLAUDE.md → AGENTS.md` to maintain a single source.
- **SKILL.md / Agent Skills.** Open standard for packaging agent capabilities — a folder containing `SKILL.md` (YAML frontmatter + Markdown body) and optional supporting files. Created by Anthropic; now supported by Claude Code, OpenAI Codex, Cursor, Google Gemini CLI, GitHub Copilot, and 25+ others.
- **MCP (Model Context Protocol).** Open standard for connecting agents to external tools and data sources. See [modelcontextprotocol.io](https://modelcontextprotocol.io/).
- **MCP connector.** A specific MCP server wrapping a particular tool (e.g., GitHub connector, Atlassian connector).
- **Doer skill.** A skill that performs a task and produces output.
- **Coach skill (Doer + Coach pattern).** A skill that performs the task and surfaces its reasoning to less-experienced users, with memory-aware suppression once a user is proficient. Can operate in **pair-programming mode** — alternating driver/navigator with the user — which works particularly well with approve-each-step autonomy.
- **Governor / Monitor skill.** An agentic check that watches, audits, gates, or alerts on agent-driven work. Inline (e.g., pre-commit) or out-of-band (e.g., nightly audit, cost watchdog).
- **Autonomy modes.** Levels of control given to an agent: *chat-only*, *approve-each-step*, *run-and-report*, *fully autonomous*. The right mode is task-dependent and based on risk plus recoverability.
- **Scoped breadth.** Principle that agents perform best with four kinds of context — local, goal, failure-signal, and idiomatic — rather than one narrow input. Surfaced in detail in the per-role how-tos.
- **Work architecture.** Per-role catalog of recurring tasks. The denominator for any "% of tasks" claim in this rubric. Managers and tech leads own its creation and quarterly refresh.
- **Spec-driven development (SDD).** Workflow where a written spec is the source of truth that drives implementation: *constitution → spec → plan → tasks → implement*. Major frameworks: [GitHub spec-kit](https://github.com/github/spec-kit), [AWS Kiro](https://kiro.dev/), BMAD-METHOD. See [Martin Fowler — Understanding SDD](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
- **Multi-agent orchestration.** Patterns where multiple agents collaborate: separate planner / executor, supervisor with specialists, critic reviewing another agent's output, sub-agent invocation. Expected from AF3 onward (basic patterns) through AF5 (designed systems).
- **Cross-cutting concerns.** PII, security, cost (token / infra spend), and irreversibility — considerations that span every task.
- **Frontier / mid-tier / fast models.** Approximate tiers as of 2026: frontier (Claude Opus, GPT-5) for hard reasoning; mid-tier (Sonnet, GPT-5-mini) for daily work; fast/cheap (Haiku, GPT-5-nano) for high-volume or low-stakes loops.
- **Eval / eval harness / golden dataset.** Test suite for prompts or skills, comparing output against expected results. Frameworks: [promptfoo](https://www.promptfoo.dev/), [inspect](https://inspect.aisi.org.uk/).
- **Named failure modes.**
  - *Hallucination* — confidently wrong output.
  - *Sycophancy* — agreeing with the user's wrong assertion.
  - *Instruction drift* — losing the original constraint mid-task.
  - *Context poisoning* — bad output from contaminated prior context.
  - *Sandbagging* — under-performing relative to capability.
  - *Jailbreak* — bypass of safety constraints.
  - *Prompt injection* — adversarial instructions embedded in untrusted content.
  - *Over-confident wrong answer* — high confidence without justification.
- **Agent Fluency Architect.** Designated org role that owns adoption strategy for a team, function, or the org. Filled from AF4–AF5 fluency; the role is appointed, not earned by fluency.

---

## The four dimensions

Scored independently AF1–AF5. A person can sit at different levels on different dimensions — that's normal and useful.

- **Daily Use** — How effectively the person delegates real work and verifies the output.
- **Building & Customization** — How well they extend agents with reusable assets (saved prompts, skills, plugins, MCPs, connectors, workflows).
- **Judgment & Oversight** — How well they decide when to use an agent, when not to, and how to catch problems before they ship.
- **Org Influence** — How much they raise the fluency of people around them.

## The five levels

| Level | Name | One-line shorthand |
|-------|------|---------------------|
| AF1 | Aware | Heard of it; rarely uses |
| AF2 | Exploring | One-off prompts for low-stakes drafts |
| AF3 | Practitioner | Delegates real work reliably; verifies; uses team-shared practices |
| AF4 | Builder | Authors reusable assets; orchestrates workflows; operates what they ship |
| AF5 | Multiplier | Mastery across all four dimensions; raises team capability |

## Signature behaviors (the gestalt)

Useful as a quick adoption check when full dimension scoring is overkill. About quantifiable progress, not evidence drawn from occasional use.

- **AF1 — Aware.** Hasn't really started. AI is occasional curiosity, not a tool.
- **AF2 — Exploring.** Low-stakes, ad-hoc use; no integration with team practices.
- **AF3 — Practitioner.** Roughly **80% of recurring day-to-day tasks** route through an agent, with proper context and verification. Diligently uses any team-shared assets that exist (AGENTS.md, team skills, prompt cookbook, configured MCPs); doesn't run a parallel private setup. Comfortable with simple multi-agent orchestration patterns.
- **AF4 — Builder.** That same 80% is now backed by reusable, recorded assets the person has authored or contributed to — saved prompts treated as artifacts, SKILL.md skills, plugins, scheduled tasks, custom MCPs — usable by at least one other person on the team.
- **AF5 — Multiplier.** Mastery across all four dimensions. Capable of setting stack and norms for a team's agent surface, building shared infrastructure others depend on, and measurably shifting a team's distribution upward over time.

---

## Calibrating measurable bars

Where this rubric uses concrete thresholds — "roughly 80%" of recurring tasks, "≥N reusable assets per quarter", and similar — the numbers are starting points, not absolutes. Managers and tech leads should arrive at the actual values with the team:

- The denominator depends on the team's **work architecture**. "80% of recurring tasks" only means something once the recurring task set is enumerated for the role.
- Counts (≥N assets, ≥N patterns documented per quarter) vary with team size, codebase, and pace. Pick numbers that reflect a real adoption stretch, not a low bar already met.
- Re-calibrate when the tooling landscape or the role itself shifts substantially. Thresholds that make sense in 2026 will look different in 2027.

The bar is not "did you hit the number." It's **"did you make the adoption progress the number was meant to capture."**

---

## Quick matrix

Compact reference. For full descriptors, see *Dimensions in detail* below.

| Dimension | AF1 — Aware | AF2 — Exploring | AF3 — Practitioner | AF4 — Builder | AF5 — Multiplier |
|-----------|-------------|-----------------|---------------------|----------------|------------------|
| **Daily Use** | Rare use; no context | One-off prompts; no iteration | Multi-step delegation with context and verification; chooses autonomy mode per task; basic multi-agent patterns | Long agentic sessions; operates autonomous flows; calibrates autonomy deliberately; designs multi-agent workflows | Designs agent-as-production-system; team-wide trust calibration |
| **Building & Customization** | None | Saved notes only | Personal Doer skills; uses team-shared assets | Team-shared Doer / Coach / Governor skills; instruments, documents, evals as craft | Curates team stack; sets quality bar; maintains team evals harness |
| **Judgment & Oversight** | Over- or under-trusts | Inconsistent verification | Verifies before acting; recognizes failure modes by name; cross-cutting concerns handled | Risk-scoped per task; cost limits; source-trust scoping; postmortems | Team risk policy; monitoring/control tooling; human-only work articulated |
| **Org Influence** | Practice stays private | Casual mentions | Documents and shares with peers on request | Demos, mentors, builds shared assets | Adoption strategy for the unit (team / function / org-wide) |

*Cells describe capabilities at each fluency level. AF5 cells describe what AF5 fluency enables; when applied at team scale (typically by an Architect), these capabilities become the team's defaults. AF5 fluency without the Architect role still has these capabilities — they just don't carry team-wide authority.*

---

## Dimensions in detail

Full descriptors per level, per dimension.

### Daily Use

How effectively the person delegates real work and verifies the output.

- **AF1 — Aware.** Rarely or never uses agents. Treats agent like web search. No context, no follow-up.
- **AF2 — Exploring.** One-off prompts for low-stakes drafts. Single-turn; no attachments. Often redoes work manually.
- **AF3 — Practitioner.** Delegates multi-step tasks reliably. Provides context (attachments, examples, constraints). Iterates within session; catches obvious errors. Picks the right **autonomy mode** per task — chat-only for exploration, approve-each-step for high-stakes work — rather than defaulting to one mode. Comfortable with simple multi-agent orchestration: separating a planner agent from an executor, invoking sub-agents for sub-tasks, using a critic agent to review another's output.
- **AF4 — Builder.** Runs longer agentic sessions with tools/MCPs. Decomposes ambiguous goals; recovers when agent drifts. Uses artifacts/scheduled tasks to make work repeatable. Operates their autonomous flows — responds to alerts, rolls back bad output, holds on-call for what they ship. Deliberately calibrates autonomy per task — chat, approve-each-step, run-and-report, fully autonomous — based on risk and recoverability. Designs multi-agent workflows (supervisor / critic / pair-programming patterns) where they fit.
- **AF5 — Multiplier.** Designs workflows where agents handle the bulk of recurring jobs. Calibrates trust per task from observed quality. Mentors others on framing and verification. Treats the team's agent surface as a production system — distribution, monitoring rotation, postmortems.

### Building & Customization

How well they extend agents with reusable assets.

- **AF1 — Aware.** No customization. Uses defaults only. Doesn't know what skills/plugins/MCPs are.
- **AF2 — Exploring.** A few favorite prompts saved in notes. Re-types similar prompts each time.
- **AF3 — Practitioner.** Diligently uses any team-shared assets that exist — AGENTS.md, team skills, prompt cookbook, configured MCPs — instead of running a parallel private setup. Authors **personal Doer skills** (saved prompts, personal SKILL.md files) for recurring work specific to them. Connects relevant data sources (Microsoft 365 stack, Atlassian stack, GitHub, and internal productivity tools). Knows when a personal asset deserves to be promoted to a team-shared one.
- **AF4 — Builder.** Authors **team-shared skills, plugins, or scheduled tasks** — in code or no-code. Writes custom MCPs/connectors when needed. Chains tools and agents into reliable multi-step workflows. Picks the right abstraction (prompt, skill, plugin, MCP) per problem. Picks the right model per task (frontier vs. fast/cheap) to balance cost and effectiveness. Designs shared skills with a **Doer + Coach** pattern where appropriate — explaining reasoning to less-experienced users with memory-aware suppression once they're proficient. Builds **Governor/Monitor** skills as the system requires — agentic checks that watch, audit, gate, or alert on agent-driven work, inline or out-of-band. Instruments shared skills and flows for observability — structured logs, named failure modes, decision traces. Documents shared assets for adoption — clear SKILL.md descriptions that trigger reliably, READMEs that teach, versioned so teammates aren't burned by silent changes. Treats evals as a craft — golden datasets, named success criteria, knows when LLM-as-judge is appropriate vs. heuristics.
- **AF5 — Multiplier.** Builds shared internal tooling — skills, plugins, marketplaces, custom MCPs/connectors. Integrates agents into CI/CD or production workflows where it makes sense. Curates the team's stack. Sets the team's **model-selection guidance** — which model for which task class, with cost/quality tradeoffs documented. Sets the **quality bar for shared skills** — Doer + Coach where relevant, clear SKILL.md descriptions, versioning, and eval coverage. Maintains the team's evals harness; calibrates what to measure as the stack evolves.

### Judgment & Oversight

How well they decide when to use an agent, when not to, and how to catch problems before they ship.

- **AF1 — Aware.** Either over-trusts (treats output as truth) or under-trusts (refuses to use). No risk awareness.
- **AF2 — Exploring.** Inconsistent verification. Catches obvious errors; misses subtle ones. May paste sensitive data without thinking.
- **AF3 — Practitioner.** Verifies before acting on outputs. Knows what tasks an agent should not do (legal, financial, irreversible). Handles **cross-cutting concerns** — PII, security, cost — appropriately. **Recognizes common agent failure modes by name** (hallucination, sycophancy, instruction drift, prompt injection, over-confident wrong answers) and watches for them in output. Treats external content (emails, web pages, third-party docs, user-supplied files) as a **prompt-injection risk**; doesn't paste untrusted content into agents without thought. Cites sources.
- **AF4 — Builder.** Scopes risk per task: agentic for low, human-in-loop for medium, manual for high. Catches subtle failure modes — sycophancy, instruction drift, context poisoning, sandbagging, jailbreaks — not just hallucinations. Sets up guardrails — redaction, separate connectors, scoped permissions, **cost limits on autonomous flows**. Scopes which connectors and sources are trusted; doesn't let agents act on data from untrusted sources without human review. Knows when an agent is the **wrong tool** for reasons beyond risk — craft, learning, taste, accountability — and chooses human work deliberately. Writes postmortems on agent failures with the same rigor as production incidents.
- **AF5 — Multiplier.** Defines the team's risk policy (covering security, PII, cost, and irreversibility). Stands up the monitoring and control tooling the team needs — cost dashboards, audit logs, agent-output anomaly detection, drift detection — building or adopting as appropriate. Articulates the team's position on what kinds of work stay human, and why. Reviews peers' agent setups for safety. Ensures every shared autonomous flow has a postmortem culture and a clear rollback path. Calibrates team trust over time using real failure data.

### Org Influence

How much they raise the fluency of people around them.

- **AF1 — Aware.** Doesn't discuss AI use with peers. Practice stays private.
- **AF2 — Exploring.** Mentions AI casually. Doesn't share specific techniques or artifacts.
- **AF3 — Practitioner.** Shares prompts/workflows on request. Answers peer questions. Documents what worked in a place teammates can find. Has a few patterns others reuse.
- **AF4 — Builder.** Runs demos, writes guides, builds shared assets. Mentors peers through the curve. Has a clear, defensible point of view on how the team should work.
- **AF5 — Multiplier.** Owns adoption strategy for the unit they serve — which can be a team, a function, or org-wide depending on scope. Builds shared infrastructure others depend on. Measurably raises the unit's average fluency over time.

---

## Skill role types

Three patterns of skill design that Builders and Architects should know.

- **Doer skills.** Perform the task. Produce the output. Personal scale at AF3 (saved prompts, personal SKILL.md files for recurring work); team-shared scale at AF4+ (distribution, docs, eval coverage).
- **Coach skills (Doer + Coach pattern).** Perform the task and surface reasoning to less-experienced users. The user learns while the work gets done. **Memory-aware suppression** switches to terse Doer mode once the user is proficient. Coach skills can also operate in **pair-programming mode** — alternating driver/navigator with the user, which works especially well with approve-each-step autonomy. Generally only worth designing at team-shared scale (AF4+).
- **Governor / Monitor skills.** Watch, audit, gate, or alert on agent-driven work. Inline (a pre-commit check that critiques the agent's diff) or out-of-band (a nightly audit, a cost watchdog, a PII scanner over agent outputs). First-class skills, not just dashboards. Team-shared by nature (AF4+); the Architect ensures the team's stack has them where needed.

---

## Composite level

After scoring the four dimensions, summarize with a composite level.

**The cap.** Composite cannot exceed the lowest dimension + 1, because weak Judgment caps the value of strong Daily Use. An AF4 (Builder) in Daily Use with an AF1 (Aware) in Judgment is a composite AF2 (Exploring) — moving fast in a direction that may cost the team.

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

- **Practitioner (AF3) is the expected level for every team member by November 2026** — regardless of role or seniority. Senior people don't get a pass; junior people aren't held to a lower bar.
- **All future hires** will be assessed for Practitioner-level agent fluency as part of the hiring process.
- **G1 (intern) and G2 (Apprentice) level hires** will be trained to Practitioner-level fluency through the academy training program.
- **Multiplier (AF5) should be rare** — typically 5–10% of a team. AF5 is a fluency level, not a role. The role that AF5 fluency enables is the **Agent Fluency Architect** (next section).

---

## Agent Fluency Architect (org role)

Separate from the fluency scale (AF1–AF5) is an org role: the **Agent Fluency Architect**.

The Architect is a designated position that owns adoption strategy for a team, function, or the broader org. The role is accountable for outcomes (not actions — the actions live in the AF4 and AF5 cells above):

- A current, documented agent stack with model-selection guidance the team actually follows.
- A current, documented risk policy covering security, PII, cost, and irreversibility.
- A monitoring and control surface where cost, safety, and quality deviations get caught.
- Measurable upward movement in the unit's fluency distribution.
- Peers' agent setups elevated to the team's quality bar.

The Architect role is typically filled by someone at AF4 or AF5 fluency — the depth is the prerequisite — but the role is appointed, not earned by fluency. An organization typically has a small number of Architects who rotate focus across teams and functions where adoption needs the most lift. AF5 fluency without the Architect role is still AF5 fluency; the capability exists without the designation.

---

## Evidence per dimension

Each score should be backed by something concrete you could point to.

**Daily Use**

- Recent chat transcripts or artifacts the agent produced.
- Workflows the person has running regularly (scheduled tasks, recurring summaries).
- Time-on-task reductions on specific recurring jobs vs. the pre-agent baseline.
- Examples of deliberate autonomy-mode choice — when they kept chat-only, ran approve-each-step, or let it run fully autonomous, and why.
- Examples of multi-agent orchestration — separated planning from execution, used a critic, invoked sub-agents.

**Building & Customization**

- Library of Doer skills authored — personal SKILL.md files / saved prompts at AF3, team-shared skills/plugins at AF4+.
- Connectors and MCPs the person has set up and uses.
- Scheduled tasks or autonomous workflows that automate recurring work.
- Governor/Monitor skills authored — agentic checks that audit, gate, or alert on agent-driven work.
- Doer + Coach designs where relevant; documented model-selection choices with cost/quality rationale.
- Instrumentation in shared skills — structured logs, named failure modes, decision traces — plus SKILL.md descriptions, READMEs, and versioning.
- An evals harness with golden datasets and named success criteria; runs on prompt or model changes.

**Judgment & Oversight**

- Specific examples of catching a failure mode by name — hallucination, sycophancy, instruction drift, prompt injection, context poisoning, sandbagging, jailbreak, or over-confident wrong answer.
- Tasks the person explicitly chose not to delegate, with rationale (risk and/or craft, learning, taste, accountability).
- Their approach to cross-cutting concerns — PII and sensitive data, security, cost (agent token / infra spend), and irreversible actions.
- Their stance on which sources and connectors are trusted; examples of refusing to let agents act on data from untrusted sources.
- Postmortems written for agent failures, treated with the same rigor as production incidents.

**Org Influence**

- Docs, guides, or demos they've produced for others.
- Named peers who have leveled up because of their help.
- Shared assets (team skills, plugins, prompt libraries) others actually use.
- Adoption movement they can point to — distribution shifts in the unit they serve (team, function, or org-wide), peers who have moved up a level.

---

## Anti-patterns at each level

If you see these, the person is stuck at the level below where they self-rate.

**Stuck at Aware → Exploring**

- Still does manual work that agents could clearly handle.
- Treats AI as a curiosity, not a tool.

**Stuck at Exploring → Practitioner**

- Blames "AI is bad" when output is poor instead of adjusting framing or context.
- Single-turn prompts only; no iteration.
- No attachments or examples provided to the agent.
- Re-types similar prompts each time instead of saving them as personal Doer skills.
- Defaults to one autonomy mode for every task.

**Stuck at Practitioner → Builder**

- Keeps personal Doer skills private; doesn't promote any to team-shared status even when teammates would benefit.
- Solo workflows only; no use of connectors or scheduled tasks.
- Can't articulate when to reach for a skill vs. a plugin vs. a one-off prompt.
- Ships autonomous flows without alerting, rollback, or cost limits.

**Stuck at Builder → Multiplier**

- Builds tools nobody else can run or understand.
- Hoards workflows rather than sharing them.
- Optimizes own throughput but doesn't move the team average.
- Strong in one dimension, weak elsewhere — heavy authoring, no mentoring; or great judgment, no published work.

---

## How to use this framework

1. **Self-assessment first.** Each team member fills out the self-assessment worksheet, rating themselves AF1–AF5 on each dimension and noting one piece of evidence per dimension.
2. **Manager calibrates.** Manager scores independently, then reviews any 2+ level gaps with the person. The conversation is the deliverable — not the number.
3. **Pick one growth move per quarter.** Each person picks one dimension to advance and commits to a concrete behavior change (not a course).
4. **Re-measure quarterly.** Movement is the signal — track whether team average is rising and where the bottleneck is.

**Cadence**

- Initial baseline: ~45 minutes per person (30 min self + 15 min manager calibration).
- Re-measure quarterly. Don't re-measure more often — movement is slow and noisy at shorter intervals.
- Refresh this rubric annually. Tools change fast.

**Pitfalls to avoid**

- Don't use scores for compensation or performance ratings. The moment people think scores affect pay, self-assessments stop being useful signal.
- Don't aggregate to leaderboards. The point is movement, not ranking.
- Don't conflate "uses AI a lot" with high fluency. Volume without verification is an AF2 anti-pattern.
- Don't grade harder than you grade yourself. Calibrate against your own behavior first.

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

- **v0.1 — 2026-05-18.** Initial framework. Four dimensions (Daily Use, Building & Customization, Judgment & Oversight, Org Influence) × five levels (AF1–AF5). Includes: composite scoring with cap; calibration guidance for measurable bars; Skill role types (Doer / Coach / Governor); Agent Fluency Architect role separated from fluency; multi-agent orchestration as AF3+ skill; named failure-mode literacy; prompt-injection awareness; cross-cutting concerns (PII, security, cost, irreversibility); model selection; autonomy modes; eval craft; instrumentation and observability; asset documentation and versioning; pair-programming via Coach skills; "scoped breadth" principle; Glossary; Further reading.