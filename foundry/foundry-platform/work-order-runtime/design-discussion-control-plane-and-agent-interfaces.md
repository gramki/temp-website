# Design Discussion: Control Plane and Agent Interfaces

This document presents design options for WO Runtime's control plane architecture and Capable Agent integration patterns. It does not prescribe solutions — it calls for decisions.

## Context

WO Runtime must orchestrate Capable Agents to execute Work Orders. This requires:

1. **A control plane** — manages Jira polling, workspace lifecycle, tool governance, agent spawning, and completion reporting
2. **Agent interfaces** — protocols for communicating with diverse Capable Agents (Codex, OpenHands, Goose, Cline, Aider, etc.)

Multiple open-source projects solve parts of this problem. The question is whether to build, adopt, or extend.

## Problem Statement

| Requirement | Challenge |
|-------------|-----------|
| Jira integration | Poll for WOs, manage task state, report completion |
| Workspace lifecycle | Create/manage Coder-based Workspace Sessions |
| Agent spawning | Start Capable Agents with harness (env, tools, skills, knowledge, delegation) |
| Tool governance | Bound what agents can do; approval workflows |
| Multi-agent support | Different agents have different interfaces (app-server, SDK, API, CLI) |
| Fallback | When preferred agent unavailable, try alternatives |
| Event streaming | Surface agent activity to IDE and observability systems |

Building all of this from scratch is significant. Existing projects (Symphony, OpenHands) have production-tested implementations of subsets.

---

## Control Plane Options

### Option A: Build Custom WO Runtime

Build the control plane as documented in the current [WO Runtime architecture](README.md).

**What Foundry builds:**
- Jira MCP integration
- Workspace Session management
- Task Manager (scheduling, dependencies)
- Agent Spawner with per-agent adapters
- Completion Reporter
- IDE plugin integration

**Advantages:**
- Full control over architecture
- Matches Foundry's exact requirements
- No external dependencies
- Can evolve independently

**Disadvantages:**
- Significant engineering investment
- Must solve problems others have already solved
- Risk of reinventing wheels (polling, retries, supervision)

**Recommended if:**
- Foundry's requirements diverge significantly from existing solutions
- Team has capacity and wants full ownership
- Long-term strategic value in owning the control plane

---

### Option B: Adopt/Extend Symphony

Symphony is OpenAI's open-source orchestration layer for Codex. It provides a production-tested Jira-to-PR workflow.

Reference: [Symphony Overview](https://openai.com/index/open-source-codex-orchestration-symphony/)

**What Symphony provides:**
- Jira polling and eligibility checks
- Per-issue workspace materialization
- Bounded tool execution
- PR creation and review handoff
- Review/rework loop
- Elixir/BEAM supervision (polling, retries, concurrency)

**What Foundry would need to add/adapt:**
- Agent adapter layer (Symphony is Codex-specific)
- Integration with Foundry Orchestrator (replace Symphony's Jira polling with Orchestrator events, or run both)
- Integration with Agent Fabric (credential resolution, quota enforcement)
- Scenario-driven tool placement (Symphony uses static config)

**Advantages:**
- Production-tested at OpenAI scale
- Elixir/BEAM fits the supervision model (polling, retries, isolated workers)
- Jira integration is mature
- Review/rework loop already implemented

**Disadvantages:**
- Elixir ecosystem (team familiarity?)
- Currently Codex-specific; needs adapter work
- Symphony's architecture may not match Foundry's module boundaries exactly
- External dependency on OpenAI's open-source maintenance

**Key question:** Can Symphony's session/tool/event contracts be generalized to other Capable Agents?

The Symphony documentation suggests this is expected:
> "OpenCode or Claude Code would need an adapter that preserves the same session, tool, sandbox, and event contracts."

**Recommended if:**
- Team is comfortable with Elixir
- Jira-to-PR workflow matches Foundry's primary use case
- Willing to contribute agent adapters upstream or maintain a fork

---

### Option C: Adopt/Extend OpenHands Agent Server

OpenHands is the strongest open software-agent platform architecture.

Reference: [Agent Harness Comparison](agent_harness_comparison_codex_openhands_goose_cline_aider.md)

**What OpenHands provides:**
- Agent Server with REST/WebSocket APIs
- Strong workspace abstraction
- Event-sourced architecture
- Local/remote/containerized execution
- SDK for custom agents
- Already provider-neutral

**What Foundry would need to add/adapt:**
- Jira integration (OpenHands doesn't have native Jira support)
- Integration with Foundry Orchestrator
- Integration with Agent Fabric (credentials, quotas)
- Foundry-specific tool governance

**Advantages:**
- Strongest open platform architecture
- Already provider/model neutral
- Event streams and workspace abstraction align with Foundry needs
- Python ecosystem (broader team familiarity?)

**Disadvantages:**
- No native Jira integration (must build)
- More moving parts than Symphony
- May be heavier than needed for Foundry's specific workflow

**Recommended if:**
- Team prefers Python ecosystem
- Foundry needs strong workspace/sandbox abstractions
- Plan to support diverse agent backends beyond coding workflows

---

### Option D: Hybrid Approach

Combine elements from multiple sources:

**Example hybrid:**
- Use Symphony's Jira integration and workflow loop (Elixir)
- Use OpenHands-style workspace abstraction
- Build Foundry-specific agent adapter layer
- Use Foundry's existing IDE plugin architecture

**Advantages:**
- Pick best-of-breed components
- Avoid full build-from-scratch

**Disadvantages:**
- Integration complexity
- Multiple codebases/ecosystems to maintain
- Risk of impedance mismatch between components

---

## Agent Interface Patterns

Capable Agents expose different interfaces. WO Runtime must support multiple patterns.

### Interface Types

| Interface Type | Protocol | Session Lifecycle | Event Streaming | Tool Governance | Examples |
|----------------|----------|-------------------|-----------------|-----------------|----------|
| **App-server** | JSON-RPC, bidirectional | Rich | Yes | Yes | Codex |
| **Agent Server** | REST/WebSocket | Rich | Yes | Yes | OpenHands |
| **SDK** | Embedded library | Embedded | Via callbacks | Via SDK | Cline |
| **API** | REST calls | Per-call | Polling | Per-call | Goose |
| **CLI (structured)** | JSONL output | Process | Stdout parsing | Args/env | OpenCode |
| **CLI (plain)** | Spawn + stdio | Process | Stdout | Args/env | Aider, Claude Code |

### Interface Preference

When a Capable Agent supports multiple interfaces, which should WO Runtime use?

**Preference order (richest control first):**

1. **App-server / Agent Server** — bidirectional, session lifecycle, events
2. **SDK** — direct integration, lifecycle hooks
3. **API** — programmatic, less coupling than SDK
4. **CLI (structured)** — parseable output
5. **CLI (plain)** — fallback

**Decision needed:** Should WO Runtime mandate a minimum interface capability, or support all?

---

## Integration Architecture Options

### Option 1: Per-Agent Adapter Pattern

Each Capable Agent gets a dedicated adapter implementing a common interface:

```
WO Runtime Control Plane
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│                    Agent Adapter Interface                   │
│                                                              │
│   spawn(task, harness) -> AgentHandle                       │
│   send_message(handle, message) -> Response                 │
│   get_events(handle) -> Stream[Event]                       │
│   terminate(handle) -> Result                               │
│   get_status(handle) -> Status                              │
└─────────────────────────────────────────────────────────────┘
        │
        ├── CodexAdapter
        │   └── JSON-RPC app-server protocol
        │
        ├── OpenHandsAdapter
        │   └── REST/WebSocket Agent Server
        │
        ├── ClineAdapter
        │   └── TypeScript SDK embedding
        │
        ├── GooseAdapter
        │   └── REST API calls
        │
        └── CLIAdapter
            └── Process spawn + stdio
            └── Used by: Aider, Claude Code, OpenCode, Gemini CLI
```

**Advantages:**
- Each adapter can use native protocol optimally
- Preserves rich capabilities of app-server agents
- Graceful degradation for CLI-only agents

**Disadvantages:**
- N adapters to build and maintain
- Behavior differences across adapters
- Testing matrix grows with each agent

---

### Option 2: Unified Foundry Agent Protocol

Define a Foundry-specific protocol that all agents must implement or be wrapped to support:

```
Foundry Agent Protocol (FAP)
├── Session lifecycle: create, attach, terminate
├── Message passing: user → agent, agent → user
├── Tool calls: agent requests, runtime approves/executes
├── Events: streaming activity, progress, completion
└── Status: health, progress, errors
```

Each Capable Agent gets a "FAP wrapper" that translates:

```
WO Runtime
    │
    │ speaks FAP
    ▼
┌─────────────────────────────────────────────────────────────┐
│                    FAP Gateway                               │
│                                                              │
│   Routes FAP messages to appropriate agent wrapper          │
└─────────────────────────────────────────────────────────────┘
        │
        ├── Codex FAP Wrapper (FAP ↔ JSON-RPC)
        ├── OpenHands FAP Wrapper (FAP ↔ REST/WS)
        ├── Cline FAP Wrapper (FAP ↔ SDK)
        └── CLI FAP Wrapper (FAP ↔ process stdio)
```

**Advantages:**
- Consistent behavior across all agents
- WO Runtime only speaks one protocol
- Easier to add new agents (implement wrapper)

**Disadvantages:**
- Lowest common denominator problem
- May lose rich capabilities of app-server agents
- Overhead of translation layer
- Must define and maintain the protocol spec

---

### Option 3: Tiered Interface Support

Support different integration tiers based on agent capabilities:

**Tier 1: Full Integration (App-server / Agent Server)**
- Rich session lifecycle
- Bidirectional events
- Interactive approvals
- Full tool governance

**Tier 2: SDK Integration**
- Embedded execution
- Callback-based events
- Programmatic tool governance

**Tier 3: CLI Integration**
- Process-based execution
- Stdout event parsing
- Env/arg-based configuration

WO Runtime adapts behavior based on tier:

```
if agent.tier == 1:
    use_bidirectional_session()
elif agent.tier == 2:
    use_embedded_sdk()
else:
    use_cli_process()
```

**Advantages:**
- Preserves rich capabilities where available
- Graceful degradation
- Clear expectations per tier

**Disadvantages:**
- User experience varies by agent
- Fallback across tiers may be jarring

---

## Capable Agent Candidate Matrix

| Capable Agent | Provider | Primary Interface | Other Interfaces | Model Neutrality | Open Source | Production Ready |
|---------------|----------|-------------------|------------------|------------------|-------------|------------------|
| **Codex** | OpenAI | App-server (JSON-RPC) | CLI | OpenAI-only | Partial (CLI) | Yes |
| **OpenHands** | OpenHands | Agent Server (REST/WS) | SDK, CLI | High | Yes | Yes |
| **Goose** | Block | API | CLI, Desktop | Very High | Yes | Yes |
| **Cline** | Cline | TypeScript SDK | CLI | Very High | Yes | Yes |
| **OpenCode** | OpenCode | CLI (JSONL) | — | Very High | Yes | Emerging |
| **Claude Code** | Anthropic | CLI | — | Anthropic-only | Yes | Yes |
| **Aider** | Aider | CLI | — | Very High | Yes | Yes |
| **Gemini CLI** | Google | CLI | — | Google-only | Yes | Yes |
| **Cursor Agent** | Cursor | CLI | — | Multi-model | No | Yes |
| **GitHub Copilot** | GitHub | CLI | — | Multi-model | No | Yes |

**Notes:**
- "Model Neutrality" = Can use models from multiple providers
- "Open Source" = Source code available for extension/forking
- "Production Ready" = Used in production by originating org

---

## Fallback Considerations

When the preferred Capable Agent is unavailable, WO Runtime falls back to alternatives. With heterogeneous interfaces, fallback has additional complexity:

### Same-Interface Fallback

```
Preferred: Codex (app-server)
Fallback 1: OpenHands (agent-server) — similar capabilities
Fallback 2: Cline (SDK) — reduced capabilities
Fallback 3: Aider (CLI) — minimal capabilities
```

**Question:** Should fallback preserve interface tier, or prioritize availability?

### Interface-Preserving Fallback

Only fall back to agents with similar interface capabilities:

```
App-server agents: Codex → OpenHands (closest peer)
CLI agents: Claude Code → Aider → OpenCode
```

**Advantage:** Consistent user experience within fallback chain  
**Disadvantage:** May exhaust options faster

### Capability-Degrading Fallback

Fall back to any available agent, accepting reduced capabilities:

```
Codex (unavailable) → Aider (available, CLI-only)
```

**Advantage:** Work continues  
**Disadvantage:** User experience degrades; some features unavailable

**Decision needed:** What is the fallback strategy?

---

## Decisions Required

### Decision 1: Control Plane Strategy

| Option | Build Effort | Maintenance | Fit with Foundry |
|--------|--------------|-------------|------------------|
| A: Build custom | High | Foundry-owned | Exact fit |
| B: Extend Symphony | Medium | Shared/forked | Good (Jira workflow) |
| C: Extend OpenHands | Medium | Shared/forked | Good (workspace abstraction) |
| D: Hybrid | Medium-High | Complex | Depends on choices |

**Question:** Which control plane strategy should Foundry pursue?

---

### Decision 2: Agent Adapter Architecture

| Option | Flexibility | Complexity | Capability Preservation |
|--------|-------------|------------|-------------------------|
| Per-agent adapters | High | N adapters | Full |
| Unified protocol (FAP) | Medium | 1 protocol + N wrappers | Lowest common denominator |
| Tiered interface support | High | 3 tiers + adapters | Per-tier |

**Question:** Which adapter architecture should WO Runtime implement?

---

### Decision 3: Priority Capable Agents

Given limited engineering capacity, which Capable Agents should be supported first?

**Candidates by strategic value:**

| Priority | Agent | Rationale |
|----------|-------|-----------|
| P0 | Codex | Symphony compatibility, OpenAI relationship |
| P0 | OpenHands | Open platform, provider-neutral, strongest architecture |
| P1 | Cline | SDK embedding, TypeScript, provider-neutral |
| P1 | Claude Code | Anthropic models, production-ready |
| P2 | Goose | MCP-centric, general automation |
| P2 | Aider | Terminal productivity, provider-neutral |
| P3 | OpenCode | Emerging, JSONL output |

**Question:** What is the priority order for Capable Agent support?

---

### Decision 4: Interface Preference

When a Capable Agent supports multiple interfaces (e.g., Codex has app-server and CLI), which should WO Runtime use?

**Options:**
- Always use richest interface available
- Allow configuration per Foundry/Workbench
- Match interface to Scenario requirements

**Question:** How should WO Runtime select interface when multiple are available?

---

### Decision 5: Fallback Strategy

**Options:**
- Interface-preserving: Only fall back within same interface tier
- Capability-degrading: Fall back to any available agent
- Configurable: Let Skilled Agent manifest specify fallback rules

**Question:** What fallback strategy should WO Runtime implement?

---

## References

- [WO Runtime Architecture](README.md)
- [Agent Harness Comparison](agent_harness_comparison_codex_openhands_goose_cline_aider.md)
- [Symphony Overview](https://openai.com/index/open-source-codex-orchestration-symphony/)
- [OpenHands Documentation](https://docs.all-hands.dev/)
- [Codex CLI](https://github.com/openai/codex)
- [Cline SDK](https://github.com/cline/cline)
- [Goose](https://github.com/block/goose)
- [Aider](https://github.com/paul-gauthier/aider)
- [OpenCode](https://opencode.ai/)

## Read Next

- [capable-agents.md](../agent-fabric/capable-agents.md) — Capable Agent registry and expanded candidate set
- [agent-spawning.md](agent-spawning.md) — Current spawning architecture
- [requirements.md](requirements.md) — WO Runtime implementation requirements
