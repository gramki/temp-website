# Developer How-To: Agent Fluency

> **v0.1 · last updated 2026-05-18**
> A practical guide for software developers moving up the Agent Fluency for Builders rubric. This pairs with [../Agent_Fluency_for_Builders_Rubric.md](../Agent_Fluency_for_Builders_Rubric.md). Read the rubric for the level definitions; this guide tells you what to *do* about them.
>
> Tool references reflect the landscape as of mid-2026. Refresh annually.

---

## TL;DR

- This guide has three growth sections: **Practitioner (AF3)**, **Builder (AF4)**, and **AF5 fluency** (mastery; rare).
- A fourth section covers **taking on the Agent Fluency Architect role** — a separate org role that AF5 fluency enables but doesn't require.
- **Practitioner is the expected level by November 2026.** Future hires are assessed at hiring. G1/G2 hires are trained to Practitioner through the academy program. The rubric's *Level expectations* section has the full details.
- This guide is for **developers**. If you're in Product Marketing, BizOps, IT, HR/TA, or Legal, a companion guide (*Agent Fluency for Operators*) is planned.
- Numbers in this guide ("≥5 PRs", "ten-case eval") are starting points. Your tech lead will adjust them based on the rubric's *Calibrating measurable bars* section.
- For term definitions and external references (AGENTS.md, SKILL.md, MCP, spec-kit, eval frameworks, multi-agent patterns, prompt-injection literature), check the rubric's **Glossary** and **Further reading**.

---

## Reaching Practitioner (AF3)

> **Goal:** roughly 80% of your recurring day-to-day tasks route through an agent — with proper context and verification — and you use any team-shared practices that exist (AGENTS.md, saved skills, prompt cookbook, configured MCPs) rather than running a private setup.

**You're here when you can say…**

- I shipped at least five PRs last month where an agent did the bulk of the work and I reviewed and refined.
- I provide the file, the test, the error, and a similar example from elsewhere in the codebase — not just the symptom.
- I review agent-generated code with eyes tuned to *agent* failure modes (made-up imports, plausible-but-wrong APIs, missed edge cases, sycophantic confirmation of my framing), not just human review eyes.
- I catch hallucinated imports, wrong APIs, and off-by-one errors before commit. I can name common failure modes — hallucination, sycophancy, instruction drift, prompt injection, over-confident wrong answers — and I watch for them.
- I have a small library of personal Doer skills — your saved prompts and reusable SKILL.md files — for work that's specific to me. I know which ones might be worth promoting to team-shared.
- I pick the right autonomy mode per task. Chat-only for exploration. Approve-each-step for changes I want to vet. Run-and-report for cheap, recoverable jobs.
- I'm comfortable with basic multi-agent orchestration — separating planning from execution, invoking sub-agents, using a critic agent to review another's output.
- When agents read external content (emails, web pages, third-party docs, user-supplied files), I treat it as a prompt-injection risk and verify before acting.
- I share what works with peers — saved prompts they can copy, demos of workflows that landed, written notes on what failed and why.

**Habits to build this quarter**

> **Give the agent scoped breadth, not narrow depth.**
>
> Agents perform best with four kinds of context, not just one: **local context** (the file — imports, surrounding patterns, scope), **goal context** (the failing test, the spec, or the desired outcome), **failure signal** (the actual error message or symptom, verbatim, not paraphrased), and **idiomatic context** (a comparable function from elsewhere in the repo).
>
> The "elsewhere" is what most developers skip — and it makes the biggest difference. The function you're editing doesn't teach the agent your team's vocabulary: naming conventions, helper-utility patterns, error-handling style, logging idioms. A similar function from another module does. Without idiomatic context, the agent produces generic textbook-quality code. With it, you get code that matches the codebase.
>
> That's the difference between "right but I have to rewrite half of it" and "right and merges as-is."

- For one week, refuse to write boilerplate by hand. Test fixtures, mock data, type definitions, doc comments, README updates, migration scaffolding — agent first, edit second. Notice how often you accept versus rewrite.
- Treat agent-generated code review as a distinct skill. Build a personal checklist: imports that don't exist, APIs that don't match the version in `package.json` / `requirements.txt`, edge cases the test didn't cover, sycophantic agreement with a wrong framing in your prompt.
- After each AI-assisted commit, jot one line — what worked, what didn't. After a month you have a personal style guide.
- Save any prompt you've re-typed twice. That's a personal Doer skill candidate. Park it in a personal SKILL.md or a snippets file.
- Try a multi-agent move on one task this month. Have one agent draft a plan, another execute, you act as final reviewer. Or have a critic agent review another's diff. Notice what changes.
- Run an agent on a task with PII or sensitive context. Notice the redaction, scoping, and verification steps you take. Make them habits.
- Share one thing per week with the team — a prompt that worked, a failure to watch for, a connector you set up.

**Tools and patterns**

The tool landscape moves fast and the lines between tools blur. Most modern AI coding tools support most activities. What matters is the habit of using them on real work, with proper context. Treat the list below as *activities and where they tend to happen*, not as tool prescriptions.

- **In-flow editing.** Making changes inside your editor while you work. Most teams use IDE-integrated agents here (Cursor, VS Code + GitHub Copilot, JetBrains AI Assistant, Windsurf).
- **Operating across the repo.** Refactors, sweeps, scripted runs touching many files. Most teams use a CLI agent (Claude Code, Aider, OpenAI Codex CLI, Gemini CLI) or an IDE agent's Composer/Agent mode.
- **Reasoning with project context** (without editing yet). Planning a change, design discussion, reviewing a large diff before opening the IDE. Use a surface that has the project context attached — Claude Projects, ChatGPT Projects, Cursor chat with repo open, Claude Code in ask/plan mode. Pure web chat without project context is mostly useful for greenfield brainstorming before any code exists. Don't default to it.

Cross-cutting:

- **MCP connectors: GitHub, Atlassian (Jira / Confluence), Microsoft 365.** Wire them up so any of the above can read the ticket, design doc, or PR. Open standard, governed by the Agentic AI Foundation. Add internal connectors as your team builds them — wrappers for Foundry CI, Weave CD, Delta, Nalanda, Olympus Watch.
- **Personal SKILL.md files.** A portable open standard for your reusable assets, supported across 30+ tools.

**Evidence to show your manager**

- A list of 5+ recent PRs where the agent carried the bulk of the work.
- Your personal prompt notes / personal Doer skills (saved prompts or SKILL.md files).
- Your agent-code review checklist (even informal).
- One concrete example where the first answer was wrong and you guided the agent to the right one.
- A specific case where you spotted a failure mode by name (hallucination, instruction drift, prompt injection, etc.) and stopped acting on the output.
- An example of an external-content task you handled carefully (or chose not to delegate).
- One example of a multi-agent setup you used and what changed.
- A short list of patterns or prompts you've shared with the team (1:1s, demos, docs).

**Anti-patterns that keep you stuck at Exploring (AF2)**

- "Copilot suggested it, so it's right." Verification absent.
- Reviewing agent-generated code the same way you review human-generated code. You miss the agent-specific failure modes.
- Single-turn prompts — you ask once, the answer's off, you give up and write it yourself.
- Pasting just the symptom, never the surrounding code.
- Re-typing similar prompts each time instead of saving them as personal Doer skills.
- Defaulting to one autonomy mode — chat-only for everything, or auto-run for everything. Mode-blind.
- Never trying multi-agent patterns because they sound complicated. The simplest version is just "have a separate plan-only chat before you start coding."
- Practice stays private. Nothing shared with the team, even in passing.
- Blaming the codebase. "AI is bad at our codebase" is sometimes true. At AF3 it's a problem to solve, not an excuse.

---

## Reaching Builder (AF4)

> **Goal:** that same 80% of your recurring work is now backed by reusable, recorded assets you've authored or contributed to — saved prompts treated as artifacts, SKILL.md skills, plugins, MCPs, scheduled tasks — usable by at least one teammate.

**You're here when you can say…**

- I've authored team-shared assets — Cursor rules, `CLAUDE.md` / `AGENTS.md` project files, SKILL.md skills — that at least one other person on the team uses.
- I've written or extended at least one MCP server that integrates an internal tool.
- I have at least one scheduled or event-driven agentic workflow running. I own its operational side (alerts, rollback, on-call).
- I've built at least one Governor/Monitor skill — an agentic check that watches, audits, or gates agent-driven work.
- I've designed multi-agent workflows (supervisor / critic / pair-programming with a Coach skill) for non-trivial tasks.
- I pick the right abstraction per problem (prompt, skill, plugin, MCP) and the right model per task (frontier vs. fast/cheap) to balance cost and effectiveness. I document the choice.
- I've written postmortems on agent failures with the same rigor as production incidents.

AF4 is wide. The three sub-sections below group the work: **Authoring** (building things), **Quality & Operations** (running them), **Judgment** (knowing when not to and catching what goes wrong).

### Authoring

This sub-section covers the things you build and ship for your team: shared skills, MCP servers, AGENTS.md files, and spec-driven workflows. If it's a reusable artifact that other people run, it lives here.

**Habits this quarter**

- Pick three of your most-repeated workflows and turn each into a team-shared asset. Examples: "Generate a migration from this schema change," "Triage this Sentry issue and propose a fix," "Draft the changelog from the last release's PRs."
- Build one custom MCP server (or Cursor/Claude plugin) that wraps an internal tool — Weave CD, Delta, Nalanda (or Confluence / Academy sites), Olympus Watch. Fifty lines is fine. Usefulness beats polish.
- Build one Governor/Monitor skill — a pre-commit check that critiques the agent's diff, a nightly audit of agent-generated PRs, a cost watchdog on autonomous flows. These are first-class skills, not dashboards.
- When you author a shared skill, decide explicitly: Doer-only, Doer + Coach (with memory-aware suppression), or pair-programming style (alternates driver/navigator with the user). The Doer + Coach pattern is what teaches the team while the work gets done.
- Encode **"scoped breadth"** into your shared skills. When you author a skill for a recurring task, have it auto-pull 2–3 comparable assets from the repo — similar functions, related test files, relevant ADRs. The team shouldn't have to remember to bring this context. That's the whole point of skill-as-asset over prompt-as-instruction.
- Document model choice in your skills. If a skill defaults to Claude Sonnet, state why. If it falls back to Haiku for cheap retries, state that too.

#### Authoring a good AGENTS.md / CLAUDE.md

The AGENTS.md (and Claude Code's CLAUDE.md, typically a symlink) is the most leveraged single artifact in a builder team. Quality varies enormously. Most teams' first attempt is a wall of unstructured rules the agent doesn't actually follow.

What good looks like (the [AGENTS.md spec](https://agents.md/) and community guidance converge on this):

- **Under ~300 lines.** Frontier LLMs follow ~150–200 instructions reliably. Claude Code's own system prompt uses ~50. Leave headroom.
- **Sections the agent can find.** Setup commands, test commands, code conventions, architectural constraints, security/PII rules, what to skip, what to never touch. Headings matter — agents scan.
- **Imperative, specific.** "Use `pnpm`, not `npm`" beats "we tend to prefer pnpm." "Tests live in `__tests__/`, mirror the source path" beats "test conventions are in the repo."
- **What to leave out.** Anything the agent can infer from the codebase (e.g., language, framework choice). Anything that changes weekly (delete instead of bloat). Aspirational rules nobody enforces.
- **Splitting.** For large monorepos, put an `AGENTS.md` at the root plus per-area `AGENTS.md` files in sub-directories. Agents read the nearest one. Don't try to put everything at root.

When you author or revise the team's AGENTS.md, treat it like an ADR: explain *why* a convention exists, not just what it is. The agent (and the next teammate) will thank you.

#### Spec-driven development workflow

Spec-driven development (SDD) means writing a structured spec before you start coding, then letting the agent implement against that spec. Instead of describing a feature verbally in a chat window, you produce a series of short documents that define what to build, how to build it, and what tasks to tackle. For non-trivial features, agents work much better this way.

The community has converged on a four-stage flow: **constitution → spec → plan → tasks → implement**.

- **Constitution** (`.specify/memory/constitution.md`): project-wide foundational guidelines the agent always reads. Lives once.
- **Spec** (`specs/<feature>/spec.md`): requirements, acceptance criteria (often in EARS notation), non-goals. The source of truth for what to build.
- **Plan** (`specs/<feature>/plan.md`): architecture and approach. How the spec will be realized.
- **Tasks** (`specs/<feature>/tasks.md`): decomposed implementation steps with completion tracking.
- **Implement**: the agent executes the tasks, and you review each one.

Use [GitHub spec-kit](https://github.com/github/spec-kit) (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement` slash commands) or AWS Kiro's built-in flow. Spec-kit has the broadest cross-tool support (works with Claude Code, Codex, Cursor, Gemini CLI, and 30+ others).

Spec-driven dev is a craft. At AF4, you've used it on at least one real feature and have an opinion on when it helps versus when it's overkill. Rule of thumb: anything that would otherwise warrant a design doc.

**Tools and patterns**

- **Cursor Rules / `CLAUDE.md` / `AGENTS.md` / Copilot custom instructions.** Encode team conventions so the agent stops re-asking — framework idioms, code style, what to test, what to skip.
- **Custom MCP servers.** Use the MCP SDK. Expose your internal API. The right size is "smaller than you think."
- **`.specify/` + `specs/<feature>/{spec, plan, tasks}.md`.** GitHub spec-kit conventions for spec-driven agentic work.
- **Distribution.** Make your assets easy for teammates to run — `uvx`, `npx`, internal package registry, or a one-step install README. Tools that only run on your laptop don't count.
- **Model selection patterns.** Frontier (Claude Opus, GPT-5) for hard reasoning and high-stakes outputs. Mid-tier (Sonnet, GPT-5-mini) for most daily work. Fast/cheap (Haiku, GPT-5-nano) for high-volume or low-stakes loops.
- **Multi-agent design patterns.** Supervisor + specialists, critic-pattern review, plan-then-execute, pair-programming with a Coach skill. Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) is a solid reference for the canonical patterns.

### Quality & Operations

This sub-section covers what happens after you build something: keeping it running, making it observable, and knowing when it breaks. If you ship a skill or workflow, you own how it behaves in the wild.

**Habits this quarter**

- Instrument your shared skills and flows for observability. Structured logs, named failure modes, decision traces — so someone else can debug them when they break.
- Write a ten-case eval suite for your most-used shared skill. Run it on every prompt edit and model bump. Treat regressions as bugs.
- Version your shared assets. When you change a skill's behavior in a meaningful way, bump a version and note what changed in a CHANGELOG. Teammates shouldn't be burned by silent changes.
- Set up at least one autonomous workflow with proper guardrails. Examples: nightly dependency-update PRs, on-call summary from yesterday's incidents, weekly PR-review digest. Define rollback, alerting, and cost limits *before* turning it on.
- Operate what you ship. When an autonomous flow fails, you respond. When it surfaces noise, you investigate. When it costs more than expected, you trim.
- Set autonomy per task deliberately. Chat for exploration. Approve-each-step for medium risk. Run-and-report for low-risk recoverable jobs. Fully autonomous only when the blast radius is bounded.

**Tools and patterns**

- **CI-integrated agentic workflows.** Foundry CI running an agent (Claude Code, Copilot Workspace, Codex CLI, or similar) for PR generation, automated code review, scheduled triage runs.
- **Eval frameworks.** [promptfoo](https://www.promptfoo.dev/), [inspect](https://inspect.aisi.org.uk/), or roll your own — pick one. Wire it into Foundry CI.
- **Observability for skills.** Structured logs into Olympus Watch (or similar) beat nothing. Decision traces matter when the agent did something surprising.
- **Asset versioning.** SemVer your shared skills/plugins. Keep a short CHANGELOG.
- **Cost dashboards / token-spend logs.** A per-flow spend log in Olympus Watch catches runaways early.

### Judgment

This sub-section covers knowing when *not* to use an agent, how to scope trust, and how to catch things that go wrong. It's the hardest part of AF4 because it requires you to slow down and think critically about outputs you'd otherwise just ship.

**Habits this quarter**

- Build a personal failure-mode checklist. When you review agent output, scan for: hallucination, sycophancy, instruction drift, context poisoning, sandbagging, jailbreaks, prompt injection, over-confident wrong answers. Name what you saw.
- Scope which connectors and sources you trust. Treat user-supplied files, web content, and third-party docs as untrusted by default. Don't let agents act on them without a human in the loop.
- Set cost limits on every autonomous flow. A scheduled job with no spend cap is an outage waiting to happen.
- Practice not delegating. Some tasks are yours because of craft (architecture choices), learning (you're growing into them), taste (the team's voice), or accountability (someone has to own the call). Do these by hand on purpose.
- After every agent-related failure, write a postmortem. What happened, why, what you'd change. Five paragraphs beats nothing.

**Tools and patterns**

- **Pre-commit Governor skills.** Before code goes into a PR, a skill checks it for common failure modes specific to your codebase.
- **Connector trust scopes.** When configuring MCPs, scope each connector to what it actually needs. Default-deny is the right starting point.
- **Risk-tagged autonomy.** Encode in a skill's metadata: autonomous-safe, needs-approval, or never-unattended. Make the policy explicit in the artifact.
- **Postmortem templates.** Use whatever the team uses for production postmortems — same template, same rigor.

**Evidence to show your manager**

- A repo of skills / rules / MCP servers you've authored — with usage from at least one other person, a CHANGELOG, and instrumentation.
- A well-crafted AGENTS.md (under ~300 lines, sectioned, imperative) that the team actually follows.
- A spec-driven dev workflow you've run on a real feature (`.specify/`, `specs/<feature>/*` artifacts).
- A Governor/Monitor skill running in production or Foundry CI.
- One end-to-end agentic workflow in your team's tools, with documented rollback and on-call.
- An evals harness with golden datasets covering at least one critical skill.
- A multi-agent setup (e.g., plan-then-execute, supervisor + specialists) you've designed and run.
- A postmortem you wrote for an agent failure, and what changed because of it.

**Anti-patterns that keep you stuck at Practitioner (AF3)**

- Keeping your personal Doer skills private. Not promoting any to team-shared even when teammates would benefit.
- AGENTS.md that's a wall of unstructured rules nobody (agent or human) actually reads.
- Tools only you can run — uncommitted config, env-specific paths, no README.
- Treating every problem as a one-shot prompt even when the same task recurs.
- Refusing scheduled or autonomous flows because "agents can't be trusted." That's an AF2 stance. At AF4 you scope risk per task and instrument what you ship.
- Shipping autonomous flows without alerting, rollback, or cost limits.
- Building shared skills nobody uses because the SKILL.md description doesn't trigger reliably or the README doesn't teach.
- Never reaching for multi-agent patterns even when the task structure (plan / execute / review) clearly fits.

---

## Reaching AF5 fluency (mastery)

> **Goal:** mastery across all four dimensions — depth and breadth that takes years of deliberate practice. AF5 fluency is rare (5–10% of a team). It enables the Agent Fluency Architect role (next section) but the role itself is appointed.

AF5 isn't a sprint. It's where you start to teach the patterns, adjust trust across many contexts, and recognize failure modes the rest of the team won't see for another year. Most strong builders stay at AF4. That's healthy.

**You're here when you can say…**

- I operate fluently across Daily Use, Building, Judgment, and Org Influence — not strong in two and weak in the others.
- I can recognize and explain failure modes by name, including the subtler ones (sycophancy, instruction drift, context poisoning, sandbagging) that less-experienced builders miss.
- I've designed multiple shared skills, including Governor/Monitor patterns, that are still in use a year later.
- I've designed multi-agent systems for non-trivial team workflows.
- I've mentored at least two developers from AF2/AF3 to AF3/AF4. I can describe what unlocked them.
- I've written and run evals against the team's critical skills. I know what fails and why.
- I can articulate when the team should and shouldn't trust an agent, with examples drawn from real failures the team has lived through.

**Habits to build over time**

- Treat your craft as a discipline. Read postmortems from other teams. Follow what shifts in the model landscape. Refresh your mental model quarterly.
- Mentor deliberately. Pair on agent setup with a less-experienced teammate. Pair-program a Doer + Coach skill with a Practitioner so they see how reasoning gets surfaced.
- Run your own evals against models you don't usually use. Build confidence across the stack, not just the model you default to.
- Write down your judgment heuristics. The implicit calls you make about when to verify, when to delegate, when to do it by hand — get them on paper. They're the substance of mastery.
- Build at least one Governor/Monitor skill that catches a class of failure the team hadn't seen coming. That's the AF5 move.

**Evidence to show your manager**

- A track record across all four dimensions — daily delegation, authored shared assets, postmortems written and incidents prevented, peers leveled up by name.
- Shared infrastructure (skills, MCP servers, Foundry CI integrations) you've authored that the team still depends on a year later.
- A document or talk articulating your judgment heuristics — when to use, when not to, why.
- Named peers who have moved up a level because of your help, with their own description of what changed.

**Anti-patterns that keep you stuck at Builder (AF4)**

- Strong in one dimension, weak elsewhere — heavy authoring, no mentoring; or great judgment, no published work.
- Building tools nobody else can run or understand. Personal mastery, no transfer.
- Hoarding workflows rather than sharing them.
- Optimizing your own throughput without raising the team's. AF5 fluency is recognizable from outside, not just from inside.
- Skipping the harder failure-mode work — only catching hallucinations, not the subtler stuff.

---

## Taking on the Agent Fluency Architect role (org role)

> The Architect is a designated org role — not a fluency level. It's typically appointed from someone at AF4 or AF5 fluency, with depth as the prerequisite. The role is about scope and authority over a team's agent surface. See the rubric's *Agent Fluency Architect* section for the canonical responsibilities and outcomes.

This section is for you if you're being considered for, stepping into, or already in the Architect role. If you're not in the role, the AF5 fluency section above is where to focus.

**Outcomes you'd own** (from the rubric)

- A current, documented agent stack with model-selection guidance the team actually follows.
- A current, documented risk policy covering security, PII, cost, and irreversibility.
- A monitoring and control surface where cost, safety, and quality deviations get caught.
- Measurable upward movement in the unit's fluency distribution.
- Peers' agent setups elevated to the team's quality bar.

**What changes when you step into it**

- **Time mix.** Expect 30–50% of your week on Architect work: stack decisions, policy writing, peer review, mentoring, postmortem facilitation. The remainder goes to your own IC work, which is now proof-by-example of the team's standard.
- **Scope.** You make calls that bind the team — which models, which skills, which MCPs, which connectors are trusted. Lightweight written rationale beats verbal calls.
- **Accountability.** Failures of the team's agent surface land with you. Successes spread across the team. That asymmetry is the role.
- **Rotation.** Architects rotate focus across teams or functions where adoption needs the most lift. Don't get attached to permanence in one team.

**How to step into it from AF4 or AF5**

- Write the team's first `AGENTS.md` if it doesn't exist (or rewrite a bad one). Then publish the first model-selection note and the first risk policy. The artifacts are the role.
- Stand up the team's evals harness in Foundry CI for the top three shared skills. Make passing evals a precondition for skill changes.
- Run a quarterly internal demo. Show one workflow that's saving the team 5+ hours per week and walk through how it works.
- Mentor at least two developers from AF2/AF3 to AF3/AF4 in the first six months. Track who and what unlocked them.
- Define the team's autonomy/risk grid — which kinds of tasks can run autonomously, which need human-in-loop, which stay manual. Get the team to agree to it.

**Anti-patterns in the Architect role**

- Defining policy that doesn't get followed. The artifact without adoption is theater.
- Hoarding the work. Architect does not mean sole builder. If you're authoring everything yourself, you're not stewarding, you're soloing.
- Stack decisions made by preference rather than by eval data. "I like Cursor better" is not a stack rationale.
- Skipping postmortems on agent failures. The team's trust depends on them.
- Holding the role indefinitely. Architect rotation is healthy — it spreads the depth across the org.

---

## Quick-reference table

| Move | Core habit | Signature artifact | Biggest stuck-point |
|------|-----------|-------------------|---------------------|
| Exploring → Practitioner | Delegate real work, iterate in-thread, save personal Doer skills, share with peers | A month of AI-assisted PRs + personal SKILL.md library | Giving up after one bad response |
| Practitioner → Builder | Promote personal skills to team-shared; build Governor/Monitor skills; write a real AGENTS.md; run spec-driven dev | Used team skill, custom MCP, scheduled workflow with rollback, well-crafted AGENTS.md | Solo, undocumented tools |
| Builder → AF5 fluency | Develop breadth across all four dimensions; mentor others; write down your judgment heuristics | Peers leveled up by name + judgment-heuristics doc + multi-agent system in production | Personal output instead of team-wide depth |

> The Architect role is appointed, not earned by fluency alone. See the section above for what stepping into it looks like.

---

## Further reading

Developer-relevant references. For the broader list, see the rubric's *Further reading*.

- **AGENTS.md authoring** — [agents.md](https://agents.md/) for the format spec; cross-tool adoption notes from the Agentic AI Foundation.
- **SKILL.md authoring** — [Anthropic Skills documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview); community skill libraries on GitHub.
- **Spec-driven development** — [GitHub spec-kit](https://github.com/github/spec-kit), [AWS Kiro](https://kiro.dev/), [Martin Fowler — Understanding SDD](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
- **MCP** — [modelcontextprotocol.io](https://modelcontextprotocol.io/) for the spec; Anthropic and OpenAI SDK references for building servers.
- **Multi-agent patterns** — Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) and the [multi-agent research-system write-up](https://www.anthropic.com/engineering/built-multi-agent-research-system).
- **Eval frameworks** — [promptfoo](https://www.promptfoo.dev/), [inspect](https://inspect.aisi.org.uk/), [OpenAI Evals](https://github.com/openai/evals).
- **Prompt injection** — [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [Simon Willison's prompt-injection corpus](https://simonwillison.net/tags/prompt-injection/).
- **ADRs** — [adr.github.io](https://adr.github.io/) and [AWS Prescriptive Guidance on ADRs](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html).

---

## Changelog

- **v0.1.1 — 2026-05-28.** Tone revision for junior builder audience. Shorter paragraphs, split compound sentences, "you" voice, plain-English definitions on first use, sub-section openers explain what they cover. All substance, links, tool names, and structure preserved.
- **v0.1 — 2026-05-18.** Initial developer how-to. Four sections (Practitioner / Builder / AF5 fluency / Architect role). Builder section structured by Authoring / Quality & Operations / Judgment with named principles (scoped breadth, encoded into skills), AGENTS.md authoring depth, spec-driven development workflow, multi-agent patterns, Governor/Monitor skills, pair-programming via Coach, eval craft, instrumentation, and code review of agent-generated code as an explicit AF3 habit. Internal stack named (Foundry CI, Weave CD, Delta, Nalanda, Olympus Watch). Cross-references to the rubric's Glossary, Level expectations, Calibrating measurable bars, and Further reading.
