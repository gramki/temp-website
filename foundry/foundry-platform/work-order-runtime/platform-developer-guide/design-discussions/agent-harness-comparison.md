# Comparative Analysis of Agent Harness Projects: Codex, OpenHands, Goose, Cline, and Aider

## 1. Purpose of this document

This document compares popular AI coding / agent harness projects through a **harness architecture** lens rather than a model-quality lens.

The central question is:

> Which agent harnesses share an architecture similar to OpenAI Codex’s `app-server`, and how do they compare in the core agent loop, runtime boundaries, tool execution model, safety model, extensibility, and client interfaces?

The projects covered are:

- **OpenAI Codex / Codex CLI / Codex app-server**
- **OpenHands / OpenHands Software Agent SDK / Agent Server**
- **Goose**
- **Cline / Cline SDK**
- **Aider**

The comparison focuses on:

1. Core agent loop
2. Agent harness capabilities
3. Interfaces exposed to clients and developers
4. App-server-like architecture
5. Tooling, sandboxing, approvals, and remote execution
6. Provider neutrality and extensibility
7. Which project fits which strategic use case

---

## 2. Executive summary

### 2.1 One-line positioning

| Project | Best description |
|---|---|
| **Codex** | Opinionated software-engineering agent harness with the clearest app-server protocol boundary |
| **OpenHands** | Most complete open software-agent platform architecture, with Agent Server, SDK, workspaces, event streams, and remote execution |
| **Goose** | General-purpose local-first AI agent runtime with desktop, CLI, API, model-provider breadth, MCP extensions, recipes, and subagents |
| **Cline** | IDE-originated agent runtime becoming an embeddable TypeScript SDK with plugin, tool, provider, lifecycle-hook, and MCP extension surfaces |
| **Aider** | Terminal-first AI pair programmer with excellent repo-edit workflow and provider neutrality, but without a first-class app-server-like runtime protocol |

### 2.2 Most important conclusion

**Codex and OpenHands are the closest architectural peers if the question is specifically “who has a Codex app-server-like architecture?”**

- **Codex** has the clearest app-server boundary: JSON-RPC-style bidirectional protocol, transports, session lifecycle, approvals, streamed events, and rich-client integration.
- **OpenHands** has the strongest open platform substrate: SDK, Agent Server, REST/WebSocket, workspaces, sandboxed execution, event-sourced architecture, and multiple clients.
- **Goose** is adjacent: it has desktop, CLI, API, MCP extensions, recipes, and subagents, but it is broader and less narrowly software-engineering/app-server-protocol oriented.
- **Cline** is adjacent but in a different shape: it exposes an embeddable runtime / SDK / plugin model rather than a Codex-style app-server contract.
- **Aider** is highly useful as a terminal harness but does not appear to expose a first-class app-server-like interface.

---

## 3. Conceptual model: what is an agent harness?

A useful separation:

```text
Model
  The LLM: GPT, Claude, Gemini, local model, etc.

Harness / runtime
  The software loop around the model:
  - Session lifecycle
  - Prompt/context assembly
  - Tool-calling loop
  - File edit application
  - Shell execution
  - Test execution
  - Diff/patch management
  - Approvals
  - Sandboxing
  - Event streaming
  - Memory/context rules
  - Client interface

Client surface
  The UI or integration:
  - Terminal UI
  - IDE extension
  - Desktop app
  - Web app
  - Remote/mobile control surface
  - CI integration
  - Custom enterprise product

Tool layer
  External capabilities:
  - Filesystem
  - Shell
  - Browser
  - Git
  - Databases
  - APIs
  - MCP servers
  - Internal tools
```

The key shift in modern agent systems is from **model APIs** to **harness APIs**.

A chat-completion API answers:

> “What should the model say next?”

A harness API answers:

> “Create a task session, stream agent events, edit files, run commands, ask for approvals, maintain workspace state, and produce a traceable outcome.”

That is why Codex app-server is architecturally important.

---

## 4. What “Codex app-server-like” means

A Codex app-server-like interface has most of the following characteristics:

1. **Separate runtime from client**
   - The agent runtime can be driven by multiple client surfaces.

2. **Session lifecycle API**
   - Start, continue, inspect, rejoin, and terminate agent sessions.

3. **Bidirectional event streaming**
   - Client sends user messages / approvals.
   - Runtime streams model events, tool calls, diffs, command output, and final results.

4. **Tool execution controlled by runtime**
   - File edits, shell commands, tests, and MCP tools are coordinated by the harness.

5. **Approval and safety model**
   - Sensitive actions require user or policy approval.

6. **Workspace/repo awareness**
   - The runtime understands a working directory, repo, files, diffs, commands, tests.

7. **Client-neutral protocol**
   - The same runtime can power terminal UI, IDE extension, desktop app, or custom clients.

8. **Extensibility**
   - Through config, rules, skills, MCP, plugins, or custom tools.

Under that definition:

| Project | App-server-like? | Why |
|---|---:|---|
| **Codex** | **Yes** | Explicit app-server protocol for rich clients |
| **OpenHands** | **Yes / closest open peer** | Agent Server with REST/WebSocket, workspaces, events |
| **Goose** | **Partly** | Desktop + CLI + API + MCP, but less specifically app-server protocol |
| **Cline** | **Partly** | SDK/plugin runtime, not exactly a client/server app-server |
| **Aider** | **No / weak** | Terminal-first CLI; can be wrapped, but not a first-class server protocol |

---

## 5. Core agent loop comparison

All five systems use variants of the same base loop:

```text
User task
  -> Harness assembles context
  -> Model proposes next step
  -> Harness executes tool/action
  -> Observation returns
  -> Model plans next step
  -> Repeat until done
  -> Final answer / patch / commit / PR / artifact
```

The differences are in what the harness treats as first-class.

### 5.1 Core loop table

| Layer | Codex | OpenHands | Goose | Cline | Aider |
|---|---|---|---|---|---|
| Primary loop orientation | Code-change loop | Software-agent platform loop | General local machine-agent loop | IDE / coding agent runtime loop | Terminal pair-programming loop |
| Main work unit | Agent session in repo/workspace | Conversation + workspace + event stream | Session / recipe / subagent | Agent session / task | Chat session over repo |
| Tool execution | Shell, files, tests, MCP, patching | Tools/actions in workspace; REST/WS event observation | Shell, files, apps, MCP extensions | Files, shell, browser/API/custom tools/MCP | File edits, repo map, shell/test commands |
| State model | Session state, repo context, AGENTS.md, approvals | Strong event/state/workspace abstraction | Session history, recipes, extension state | Session history, persistence, lifecycle hooks | Terminal conversation + repo map + git |
| Safety model | Sandbox + approvals central | Workspace isolation + policies + sandboxing | Tool approvals / local controls | Tool approval + plugin/policy hooks | Git/diff visibility, CLI confirmations |
| Client boundary | Strong app-server | Strong Agent Server / SDK | Desktop/CLI/API | SDK/plugin/runtime | CLI process |

### 5.2 Codex loop

Codex is optimized for:

```text
inspect repo -> plan edit -> modify files -> run tests -> inspect failures -> iterate -> present diff
```

Important loop characteristics:

- The loop is **repo-native**.
- Shell/file actions are coordinated by the harness.
- Approvals and sandboxing are first-class.
- The app-server can stream session events to rich clients.
- The UI is not the harness; the harness can sit behind multiple clients.

Codex is therefore best described as:

```text
opinionated coding-agent runtime
+ safe shell/file sandbox
+ approval workflow
+ app-server protocol
```

### 5.3 OpenHands loop

OpenHands models the loop more explicitly as a platform:

```text
conversation -> agent -> action -> workspace execution -> observation -> event stream -> client
```

Important loop characteristics:

- Strong workspace abstraction.
- Strong event-stream orientation.
- Suitable for local, Docker, or remote execution.
- Designed to be used through SDK, CLI, GUI, REST/WebSocket, and visual workspaces.
- More platform-like than Codex, though arguably less productized for everyday developer flow.

OpenHands is best described as:

```text
software-agent platform
+ SDK
+ Agent Server
+ sandboxed workspace execution
+ event-sourced runtime
+ model/provider portability
```

### 5.4 Goose loop

Goose is less specifically a software-engineering loop and more a general local-agent loop:

```text
task -> local agent session -> model -> MCP extension / shell / file / app action -> observation -> continue
```

Important loop characteristics:

- General-purpose: code, research, writing, automation, data analysis, and workflows.
- Local-first desktop and CLI UX.
- MCP extensions are central.
- Recipes package reusable workflows.
- Subagents allow parallel task decomposition.

Goose is best described as:

```text
local general-purpose agent runtime
+ desktop/CLI/API
+ MCP extensions
+ recipes
+ subagents
+ broad model-provider support
```

### 5.5 Cline loop

Cline began as a VS Code agent and is evolving into a runtime/SDK:

```text
IDE/CLI/product -> Cline runtime -> model -> tools/files/shell/MCP/browser/API -> observations -> edits/final result
```

Important loop characteristics:

- Strong IDE-originated coding agent loop.
- Tool approval is first-class.
- Runtime can be embedded using SDK.
- Plugins can register tools, observe lifecycle events, inject rules/commands, and shape what the agent sees.
- The interface is more SDK/plugin-like than app-server protocol-like.

Cline is best described as:

```text
embeddable agent runtime
+ TypeScript SDK
+ plugins/lifecycle hooks
+ provider neutrality
+ MCP/custom tools
+ IDE/CLI heritage
```

### 5.6 Aider loop

Aider is a terminal pair-programmer:

```text
developer in terminal -> aider reads repo map/context -> model proposes edits -> aider applies patch -> developer reviews/runs tests/commits
```

Important loop characteristics:

- Excellent terminal experience.
- Strong repo-map / coding-context approach.
- Very provider-neutral.
- Good for direct developer productivity.
- Not designed as a multi-client app-server runtime.

Aider is best described as:

```text
terminal-first coding agent
+ repo map
+ patch/edit loop
+ multi-provider support
+ git-oriented workflow
```

---

## 6. Harness capability comparison

### 6.1 High-level capability matrix

| Capability | Codex | OpenHands | Goose | Cline | Aider |
|---|---:|---:|---:|---:|---:|
| Local repo editing | Excellent | Excellent | Good | Excellent | Excellent |
| Shell execution | Excellent | Excellent | Excellent | Excellent | Good/Excellent |
| Test/run loop | Strong | Strong | Good | Strong | Strong |
| Patch/diff workflow | Strong | Strong | Less code-specific | Strong | Strong |
| Sandboxing | Very strong | Strong | Medium | Medium/Strong | Medium |
| Approvals | Very strong | Strong | Medium/Strong | Strong | Medium |
| Event streaming | Strong | Very strong | Medium | Medium | Weak |
| Remote execution | Medium/Strong | Strong | Medium | Medium | Weak |
| App-server-like protocol | Strongest | Strong | Partial | Partial | Weak |
| Embeddable SDK | Medium | Strong | Medium/Strong | Strong | Weak |
| Provider neutrality | Medium | High | Very high | Very high | Very high |
| MCP support | Yes | Yes / compatible | Central | Strong | Not central |
| Workflow packaging | AGENTS.md/config/skills-style | Agent configs/SDK composition | Recipes | Rules/plugins/commands | CLI/config/git |
| Enterprise platform fit | Good if OpenAI-centered | Strongest | Good for local automation | Good for IDE/runtime embedding | Lower |
| Daily terminal productivity | Strong | Medium/Strong | Medium | Medium | Strong |
| IDE-native productivity | Strong | Medium/Strong | Medium | Strong | Lower |

---

## 7. Interfaces exposed

### 7.1 Interface comparison

| Interface | Codex | OpenHands | Goose | Cline | Aider |
|---|---|---|---|---|---|
| CLI | Yes | Yes | Yes | Yes | Yes |
| TUI | Yes | Yes/CLI-oriented | CLI | CLI | Terminal chat |
| IDE extension | Yes | Yes / VS Code style surfaces | Not primary | Yes, core heritage | Not primary |
| Desktop app | Yes / Codex app ecosystem | Not primary | Yes | Not primary | No |
| Web/browser GUI | Codex cloud/app surfaces | Yes | Not primary | Not primary | No |
| App server | Yes | Yes, Agent Server | API, not same shape | SDK/runtime, not same shape | No |
| REST API | Not primary app-server shape | Yes | API exists | SDK API | No |
| WebSocket | Yes/transport support | Yes | Not core public mental model | Not primary | No |
| JSON-RPC | Yes | Not primary | Not primary | Not primary | No |
| SDK | Less central | Strong | API/embedding | Strong TypeScript SDK | No first-class SDK |
| MCP client | Yes | Yes/usable | Central | Strong | Not central |
| MCP server | Experimental / possible | Not the main identity | Extensions are MCP servers | MCP integration | Not central |

### 7.2 Codex interfaces

Codex exposes:

- CLI / TUI
- VS Code extension
- app-server
- JSON-RPC-style bidirectional protocol
- transports such as stdio, WebSocket, and Unix socket
- remote TUI/app-server attachment patterns
- MCP support
- configuration/rules via AGENTS.md and related mechanisms

Codex’s architectural strength is that its app-server is a true **client/runtime boundary**.

### 7.3 OpenHands interfaces

OpenHands exposes:

- SDK
- CLI
- GUI
- Agent Server
- REST API
- WebSocket event streaming
- workspace interfaces
- visual workspaces such as VS Code, browser/VNC-style surfaces
- local and remote execution modes

OpenHands’ architectural strength is that it looks like an **agent platform backend** rather than just a developer tool.

### 7.4 Goose interfaces

Goose exposes:

- desktop app
- CLI
- API
- MCP extensions
- MCP Apps
- recipes
- subagents
- multiple providers

Goose’s architectural strength is being a **local-first agent host** that can connect to many tools and models.

### 7.5 Cline interfaces

Cline exposes:

- IDE extension
- CLI
- TypeScript SDK
- plugins
- custom tools
- lifecycle hooks
- MCP connectors
- broad model providers

Cline’s architectural strength is being an **embeddable coding-agent runtime** with strong plugin and provider extensibility.

### 7.6 Aider interfaces

Aider exposes:

- terminal CLI
- configuration
- model-provider integrations
- repo map
- git-oriented workflows

Aider’s strength is being a **practical terminal coding tool**, not a platform API.

---

## 8. Safety, approvals, and sandboxing

### 8.1 Codex

Codex has the strongest explicit safety model among these projects for everyday repo-agent work.

Key characteristics:

- Sandbox modes are central.
- Routine reads/edits/project-local commands can be allowed.
- Riskier actions escalate to approval.
- Network access and broader side effects can be controlled.
- Approval flow is part of the app-server/client interaction model.

Codex is strongest when the use case is:

> “Allow the agent to work productively, but keep dangerous operations behind an approval boundary.”

### 8.2 OpenHands

OpenHands has a strong platform-level isolation model.

Key characteristics:

- Workspace abstraction.
- Local/remote/containerized execution.
- Event/state boundaries.
- Security policies.
- Agent Server lifecycle control.
- Production deployment orientation.

OpenHands is strongest when the use case is:

> “Run software agents in controlled, reproducible, auditable workspaces across local and remote environments.”

### 8.3 Goose

Goose is local-machine oriented.

Key characteristics:

- Tool/extension control.
- MCP extension boundaries.
- Local execution posture.
- Human-in-the-loop interaction through desktop/CLI.
- Recipes and subagents create more automation power, but also require governance if used in enterprise settings.

Goose is strongest when the use case is:

> “Let an agent operate across my local tools, apps, files, APIs, and workflows.”

### 8.4 Cline

Cline’s safety posture is tied to:

- Tool approvals.
- IDE/CLI control.
- Plugin lifecycle hooks.
- Policy/observability hooks via SDK.
- Custom tools with schemas.

Cline is strongest when the use case is:

> “Embed a coding agent runtime into a product or enterprise workflow and control behavior through plugins, tools, rules, and lifecycle hooks.”

### 8.5 Aider

Aider’s safety model is more developer-mediated:

- Edits are visible.
- Git workflow helps review/rollback.
- The terminal user remains close to the loop.
- It is less of a policy-governed sandbox runtime.

Aider is strongest when the use case is:

> “I am the developer, I am in the terminal, and I want a powerful AI pair-programmer whose changes I can inspect.”

---

## 9. Provider neutrality

### 9.1 Comparison

| Project | Provider posture |
|---|---|
| **Codex** | OpenAI-first; supports customization paths, but not primarily provider-neutral |
| **OpenHands** | Strongly model/provider agnostic |
| **Goose** | Very strong provider neutrality |
| **Cline** | Very strong provider neutrality |
| **Aider** | Very strong provider neutrality |

### 9.2 Practical interpretation

If the goal is to use **OpenAI models with a polished coding harness**, Codex is the natural path.

If the goal is to build a **provider-neutral enterprise agent runtime**, OpenHands, Goose, or Cline are stronger candidates.

If the goal is **developer terminal productivity across many models**, Aider remains highly attractive.

---

## 10. Extensibility models

### 10.1 Codex

Extensibility is through:

- configuration
- AGENTS.md-style project instructions
- MCP tools
- app-server clients
- skills/rules-style behavior
- potentially custom provider settings

Codex extensibility is runtime/client oriented, but still OpenAI-shaped.

### 10.2 OpenHands

Extensibility is through:

- SDK components
- custom agents
- tools
- workspaces
- REST/WebSocket Agent Server
- model routing
- event stream
- deployment interfaces

OpenHands extensibility is platform-oriented.

### 10.3 Goose

Extensibility is through:

- MCP extensions
- MCP Apps
- recipes
- subagents
- API embedding
- provider configuration

Goose extensibility is tool/workflow oriented.

### 10.4 Cline

Extensibility is through:

- TypeScript SDK
- custom tools
- zod-schema tools
- plugins
- lifecycle hooks
- MCP
- rules and commands
- model providers

Cline extensibility is runtime/plugin oriented.

### 10.5 Aider

Extensibility is through:

- CLI configuration
- model providers
- repo map behavior
- commands
- git/editor workflow
- scripting/wrapping the CLI externally

Aider extensibility is developer-tool oriented, not platform-runtime oriented.

---

## 11. Detailed project assessments

## 11.1 Codex

### Positioning

Codex is the most opinionated and integrated coding-agent harness in this comparison.

It is not merely a model. It is an agent harness around the model, with a CLI/TUI, app-server, sandboxing, approval flows, repo context, command execution, and client surfaces.

### Strengths

- Best app-server-like architecture.
- Strong coding loop.
- Strong sandbox and approval semantics.
- Strong rich-client support.
- Good fit for IDE/desktop/remote client surfaces.
- Good fit for teams already committed to OpenAI.

### Weaknesses

- OpenAI-first posture.
- App-server interface may still evolve.
- Less obviously provider-neutral than Goose, Cline, Aider, or OpenHands.
- May be less ideal if you want full control over agent platform internals.

### Best use cases

- Serious repo work with OpenAI models.
- Building Codex-compatible client surfaces.
- Teams wanting a strong default coding harness.
- Controlled local code modification with approvals.
- IDE/terminal/desktop workflows around the same runtime.

### Less ideal use cases

- Vendor-neutral enterprise agent platform.
- Deeply customized provider routing.
- General local automation beyond software engineering.
- Organizations wanting a fully independent agent runtime standard.

---

## 11.2 OpenHands

### Positioning

OpenHands is the strongest open platform candidate.

It is closer to a production software-agent substrate than a single developer productivity tool. Its architecture centers around SDK components, Agent Server, workspaces, events, lifecycle control, and remote execution.

### Strengths

- Strongest open production-agent architecture.
- Agent Server with REST/WebSocket shape.
- Strong workspace abstraction.
- Local-to-remote execution portability.
- Model/provider agnostic.
- Event stream and state model suitable for audit/replay.
- Good for building custom software-agent platforms.

### Weaknesses

- More moving parts than Codex or Aider.
- May be heavier than necessary for individual developer workflows.
- Product polish may vary across interfaces.
- Requires more architectural ownership from adopters.

### Best use cases

- Building an internal software-agent platform.
- Running agents in controlled workspaces.
- Remote/containerized software-agent execution.
- Traceability, event streams, and audit needs.
- Provider-neutral agent infrastructure.
- Enterprise experimentation with custom agents.

### Less ideal use cases

- Simple terminal pair programming.
- Lowest-friction individual productivity.
- Teams wanting one polished vendor-provided UX.

---

## 11.3 Goose

### Positioning

Goose is the strongest general-purpose local-agent harness in this comparison.

It is not just a coding tool. It is a local agent that can use desktop, CLI, API, MCP extensions, recipes, and subagents to perform broad workflows.

### Strengths

- Very broad model-provider support.
- Local-first desktop and CLI experience.
- Strong MCP extension model.
- Recipes are a useful workflow-packaging primitive.
- Subagents allow parallel task decomposition.
- Good for general automation, not just coding.

### Weaknesses

- Less specifically optimized for software-engineering patch/test/diff workflows than Codex/OpenHands.
- API architecture is less obviously a Codex-style app-server protocol.
- Enterprise governance around many local extensions may require additional discipline.
- Broadness can reduce sharpness for serious repo-only work.

### Best use cases

- Local automation.
- Developer + non-developer workflows.
- MCP-heavy environments.
- Provider-neutral desktop/CLI agent usage.
- Reusable workflow automation via recipes.
- Research, writing, data analysis, coding, and app automation from one harness.

### Less ideal use cases

- Strict software-engineering agent platform backend.
- Codex-style rich-client server protocol.
- Highly controlled remote workspace execution.

---

## 11.4 Cline

### Positioning

Cline is evolving from an IDE coding agent into an embeddable agent runtime.

Its SDK/plugin architecture is attractive for teams that want to integrate a coding-agent loop into their own products or workflows.

### Strengths

- Strong IDE heritage.
- Strong SDK/plugin model.
- Good lifecycle hooks for policy, logging, and observability.
- Strong provider neutrality.
- Good support for custom tools and MCP.
- Strong fit for TypeScript ecosystem adopters.

### Weaknesses

- Not the same shape as Codex app-server.
- More embedding/plugin oriented than client/server protocol oriented.
- Runtime maturity as an independent SDK should be evaluated carefully.
- IDE-centric roots may show through in assumptions.

### Best use cases

- Building custom coding-agent applications.
- Embedding agent runtime into internal developer platforms.
- Provider-neutral IDE/CLI agent workflows.
- Teams that want plugin governance and lifecycle hooks.
- TypeScript-first agent infrastructure.

### Less ideal use cases

- Need for a stable Codex-like app-server protocol.
- Remote workspace platform architecture.
- Non-TypeScript-centric backend platforms.

---

## 11.5 Aider

### Positioning

Aider is the best pure terminal pair-programming tool in this comparison.

It is not a platform server. It is a highly practical developer tool focused on repo-aware AI coding from the terminal.

### Strengths

- Excellent terminal flow.
- Very strong provider neutrality.
- Good repo map approach.
- Good patch/edit loop.
- Git-friendly.
- Low ceremony.

### Weaknesses

- No first-class app-server-like runtime interface.
- Less suitable for rich-client, remote-client, or platform embedding.
- Safety/governance is mostly developer-mediated.
- Less platform architecture than Codex/OpenHands/Cline.

### Best use cases

- Individual senior engineer doing serious terminal repo work.
- Provider-neutral coding assistance.
- Lightweight adoption.
- Fast experimentation with many models.
- Teams comfortable with CLI workflows.

### Less ideal use cases

- Building a multi-client agent platform.
- Centralized event streaming and approval orchestration.
- Enterprise runtime governance.
- Remote app-server architecture.

---

## 12. Ranking by use case

### 12.1 If you want a Codex app-server equivalent

1. **Codex**
2. **OpenHands**
3. **Goose**
4. **Cline**
5. **Aider**

### 12.2 If you want an open software-agent platform

1. **OpenHands**
2. **Cline**
3. **Goose**
4. **Codex**
5. **Aider**

### 12.3 If you want daily coding productivity

1. **Codex**
2. **Aider**
3. **Cline**
4. **OpenHands**
5. **Goose**

This ranking depends heavily on preferred UI. For terminal maximalists, Aider may outrank Codex.

### 12.4 If you want provider neutrality

1. **Goose**
2. **Cline**
3. **Aider**
4. **OpenHands**
5. **Codex**

### 12.5 If you want enterprise-grade remote execution / controlled workspaces

1. **OpenHands**
2. **Codex**
3. **Cline**
4. **Goose**
5. **Aider**

### 12.6 If you want MCP-centered automation

1. **Goose**
2. **Cline**
3. **Codex**
4. **OpenHands**
5. **Aider**

### 12.7 If you want embeddable SDK/runtime

1. **Cline**
2. **OpenHands**
3. **Goose**
4. **Codex**
5. **Aider**

### 12.8 If you want lowest-friction terminal use

1. **Aider**
2. **Codex**
3. **Goose**
4. **OpenHands**
5. **Cline**

---

## 13. Strategic interpretation

### 13.1 Codex: the polished opinionated harness

Codex is likely the most polished default if you accept the OpenAI-centric ecosystem.

It has a clean app-server boundary, strong repo-editing flow, safety model, approvals, and client architecture.

Strategically, Codex represents the movement from “coding assistant in a UI” to:

```text
agent runtime as product infrastructure
```

### 13.2 OpenHands: the open agent platform substrate

OpenHands is the strongest candidate if the goal is:

```text
build our own software-agent platform
```

It is less about one polished end-user workflow and more about a composable architecture: SDK, Agent Server, workspaces, event streams, remote execution, and model/provider flexibility.

For an enterprise that wants control and auditability, OpenHands is likely the most important project to study deeply.

### 13.3 Goose: the local agent operating layer

Goose is more like:

```text
local AI automation layer for my machine and tools
```

Its power comes from provider neutrality, MCP extensions, recipes, subagents, desktop/CLI/API surfaces, and general-purpose scope.

It is less code-specialized than Codex or OpenHands, but potentially more general as a personal/enterprise agent host.

### 13.4 Cline: the embeddable agent runtime

Cline is interesting because it is moving from “VS Code extension” toward:

```text
agent runtime SDK
```

The SDK/plugin/lifecycle-hook model is a strong architectural direction for teams that want to embed an agent inside an internal developer platform, CI system, or product.

### 13.5 Aider: the terminal-native practitioner tool

Aider is the least platform-like, but that is also its advantage.

It is simple, direct, terminal-native, model-neutral, and focused on getting coding work done.

It is not a Codex app-server peer. It is a strong practitioner tool.

---

## 14. Recommendation framework

### 14.1 Choose Codex if

Choose **Codex** when:

- You want the strongest Codex-style app-server architecture.
- You are comfortable with an OpenAI-first ecosystem.
- You want polished repo editing, shell execution, approvals, and sandboxing.
- You want IDE/terminal/desktop/remote-client potential around a common harness.
- You value controlled code changes more than provider neutrality.

### 14.2 Choose OpenHands if

Choose **OpenHands** when:

- You want to build a software-agent platform.
- You care about remote/containerized workspaces.
- You need event streams, auditability, reproducibility, and lifecycle control.
- You want provider-neutral infrastructure.
- You want REST/WebSocket APIs for agent execution.
- You are willing to own more platform complexity.

### 14.3 Choose Goose if

Choose **Goose** when:

- You want a local-first general-purpose agent.
- You want desktop + CLI + API.
- You want strong model-provider flexibility.
- You want to build around MCP extensions.
- You want reusable automation through recipes.
- You want subagents and broad task automation beyond code.

### 14.4 Choose Cline if

Choose **Cline** when:

- You want an embeddable TypeScript agent runtime.
- You want plugins, lifecycle hooks, custom tools, and MCP.
- You want provider neutrality.
- You want IDE-like coding workflows but also custom product embedding.
- You want to shape the agent runtime with rules and tools.

### 14.5 Choose Aider if

Choose **Aider** when:

- You are an individual or team of terminal-heavy engineers.
- You want low ceremony and fast productivity.
- You want broad model choice.
- You do not need a rich-client server protocol.
- You are comfortable with git/diff-mediated review.

---

## 15. Architectural decision table

| Enterprise requirement | Best fit | Reason |
|---|---|---|
| Build rich clients over an agent runtime | Codex, OpenHands | App-server / Agent Server boundaries |
| Build internal agent platform | OpenHands | SDK + Agent Server + workspaces |
| Provider-neutral local automation | Goose | Broad providers + MCP + local runtime |
| Embeddable coding agent SDK | Cline | TypeScript SDK + plugins |
| Individual terminal productivity | Aider | Low ceremony, repo-aware terminal flow |
| Strongest sandbox/approval coding loop | Codex | Sandboxing and approvals are core |
| Strongest production workspace abstraction | OpenHands | Local/remote/container workspace model |
| Strongest MCP-centered workflow | Goose | MCP extensions are central |
| Strongest plugin/lifecycle hooks | Cline | SDK plugin model |
| Strongest platform audit/event stream | OpenHands | Event/workspace/server architecture |

---

## 16. Final synthesis

The most important distinction is not “which model do they use?” but:

> What boundary does the harness expose?

### Codex exposes a client/server runtime boundary

```text
Client UI -> Codex app-server -> Codex agent runtime -> repo/shell/tools
```

This is the cleanest app-server architecture.

### OpenHands exposes a platform/server/workspace boundary

```text
Client / SDK / GUI -> Agent Server -> Agent runtime -> Workspace -> tools/actions
```

This is the strongest open production-agent architecture.

### Goose exposes a local-agent host boundary

```text
Desktop / CLI / API -> Goose runtime -> MCP extensions / local tools / apps
```

This is the strongest general local automation architecture.

### Cline exposes an embeddable runtime boundary

```text
Product / IDE / CLI -> Cline SDK runtime -> plugins/tools/MCP/providers
```

This is the strongest plugin/SDK-oriented coding-agent architecture.

### Aider exposes a terminal practitioner loop

```text
Developer terminal -> Aider -> model -> repo edits/git/test loop
```

This is the most direct terminal pair-programming architecture.

## 17. Bottom line

If the evaluation is specifically about **Codex app-server-like architecture**, the answer is:

1. **Codex** is the reference architecture.
2. **OpenHands** is the closest open-source architectural peer.
3. **Goose** is adjacent as a local-first agent runtime with API and MCP.
4. **Cline** is adjacent as an SDK/plugin-based embeddable runtime.
5. **Aider** is not app-server-like; it is a terminal-first coding harness.

If the evaluation is about **which project to study for enterprise agent platform design**, study:

1. **OpenHands** for platform architecture.
2. **Codex** for app-server/client protocol and safety UX.
3. **Goose** for local-first MCP extension patterns and workflow recipes.
4. **Cline** for SDK/plugin/lifecycle-hook extensibility.
5. **Aider** for lightweight terminal-native developer ergonomics.

The frontier is clearly moving from:

```text
LLM API + IDE plugin
```

to:

```text
agent runtime + event stream + workspace + approvals + tool governance + client protocol
```

Codex and OpenHands are the clearest examples of that shift.

---

## 18. Open Discussion Items

This section consolidates unresolved decisions for the Foundry Platform team.

### Harness Selection

1. **Which harness architecture should Foundry adopt for WO Runtime?**
   - Codex-style app-server protocol (OpenAI ecosystem, strongest client/server boundary)
   - OpenHands Agent Server (strongest open platform, provider-neutral)
   - Hybrid approach (best-of-breed components from multiple projects)

2. **Should Foundry maintain a single harness or support multiple harnesses?**
   - Single harness simplifies implementation but limits flexibility
   - Multiple harnesses match different Raw Agent interfaces but add maintenance burden

3. **What is the minimum harness capability tier Foundry will support?**
   - Tier 1 only (app-server / agent-server) for full governance
   - Include Tier 2 (SDK embedding) for Cline-style integration
   - Include Tier 3 (CLI) for maximum agent coverage (Aider, Claude Code)

### Integration Patterns

4. **Should WO Runtime adopt Symphony's Elixir/BEAM supervision model?**
   - Strong fit for polling, retries, and concurrent worker isolation
   - Requires team familiarity with Elixir ecosystem
   - Alternative: implement similar supervision in Python/Go

5. **How should WO Runtime workspace abstraction align with OpenHands?**
   - Adopt OpenHands workspace model directly
   - Build Foundry-specific abstraction with compatibility layer
   - Use Coder-based Workspace Sessions as the sole abstraction

6. **What event stream protocol should WO Runtime standardize on?**
   - OpenHands-style event sourcing
   - Codex app-server streaming events
   - Custom Foundry protocol with adapters to both

### Priority and Timeline

7. **What is the priority order for Raw Agent adapter development?**
   - Suggested P0: Codex (Symphony compatibility), OpenHands (strongest open architecture)
   - Suggested P1: Cline (SDK embedding), Claude Code (Anthropic models)
   - Suggested P2: Goose (MCP-centric), Aider (terminal productivity)

8. **Should Foundry contribute adapters upstream or maintain forks?**
   - Upstream contribution reduces maintenance but requires coordination
   - Forks allow faster iteration but create divergence risk

9. **What is the target timeline for first harness integration?**
   - Phase 1: Single harness proof-of-concept with one Raw Agent
   - Phase 2: Adapter layer for second Raw Agent
   - Phase 3: Full multi-harness support with fallback

### Ecosystem Dependencies

10. **What is the maintenance risk of depending on Symphony or OpenHands?**
    - Both are actively maintained as of this analysis
    - OpenAI's open-source commitment to Symphony should be evaluated
    - OpenHands has broader community contribution model

11. **Should CI agent harness share infrastructure with WO Runtime harness?**
    - CI agents are job-scoped, ephemeral, and pipeline-embedded
    - WO Runtime harness is session-scoped with Jira polling
    - Recommended: independent CI harness; see [ci-agent-architecture.md](../../../release-tools/platform-developer-guide/ci-agent-architecture.md)
