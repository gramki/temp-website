# Capable Agents

Capable Agents are whitelisted frontier models and agent systems that provide the core capabilities for agentic work in Foundry.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Agent** | Defines Capable Agents as the platform-layer agent systems (Cursor, Copilot, Claude Code, Codex CLI) |
| **Delegation** | Credentials resolved hierarchically (Foundry → Workshop → Workbench) and injected via Access Gateway |
| **Workspace** | Enable/disable cascade respects Workspace hierarchy |

## Definition

A **Capable Agent** is an agent system with orchestration, tool use, context management, and swarm capabilities. It represents the "engine" — what an agent *can* do structurally.

**Current examples:**
- Cursor Agent
- GitHub Copilot
- Claude Code
- Codex CLI
- Gemini CLI

**Candidate agents under evaluation:**
- OpenHands
- Goose
- Cline
- Aider
- OpenCode

→ See [Capable Agent Candidates](#capable-agent-candidates) for the full evaluation matrix

## Capable Agent vs Model

| Concept | Definition | Examples |
|---------|------------|----------|
| **Capable Agent** | Agent system with orchestration capabilities | Cursor Agent, Copilot, Claude Code |
| **Model** | Underlying LLM that powers reasoning | claude-opus, gpt-5-thinking, gemini-pro |

A Capable Agent may support multiple models:

```
Capable Agent: Cursor Agent
├── Model: claude-opus
├── Model: claude-sonnet
└── Model: gpt-5

Capable Agent: Copilot
├── Model: gpt-5
├── Model: gpt-5-thinking
└── Model: claude-sonnet

Capable Agent: Claude Code
├── Model: claude-opus
└── Model: claude-sonnet
```

## Hierarchy and Scope

Capable Agents can be defined at three levels:

```
Foundry (org-level)
    │
    └── Workshop (team-level)
            │
            └── Workbench (product-level)
```

### Enable/Disable Cascade

- **Disabling at a level cascades down** — If a Capable Agent is disabled at Workshop level, it is disabled for all Workbenches in that Workshop
- **Enabling requires parent enabled** — A Capable Agent cannot be enabled at Workbench level if it is disabled at Workshop level

### Credential Resolution

Credentials are resolved **from lowest level up** (child overrides parent):

1. Check Workbench-level credentials
2. If not found, check Workshop-level credentials
3. If not found, check Foundry-level credentials

This allows:
- Foundry-wide API keys for org-level billing
- Workshop-specific keys for team-level billing
- Workbench-specific keys for project-level isolation

## Registry Schema

### Foundry Level

```yaml
# foundry.yaml or capable-agents.yaml at Foundry level
capable-agents:
  cursor-agent:
    provider: cursor
    enabled: true
    interfaces:
      - type: cli
        protocol: spawn-stdio
        recommended: true
    models:
      claude-opus:
        enabled: true
        credentials:
          api-key: ${ANTHROPIC_API_KEY}
      claude-sonnet:
        enabled: true
        credentials:
          api-key: ${ANTHROPIC_API_KEY}
          
  copilot:
    provider: github
    enabled: true
    interfaces:
      - type: cli
        protocol: spawn-stdio
        recommended: true
    models:
      gpt-5:
        enabled: true
      gpt-5-thinking:
        enabled: true
        
  claude-code:
    provider: anthropic
    enabled: true
    interfaces:
      - type: cli
        protocol: spawn-stdio
        recommended: true
    models:
      claude-opus:
        enabled: true
        credentials:
          api-key: ${ANTHROPIC_API_KEY}
          
  codex-cli:
    provider: openai
    enabled: true
    interfaces:
      - type: app-server
        protocol: json-rpc
        recommended: true
      - type: cli
        protocol: spawn-stdio
    models:
      codex-3:
        enabled: true
        credentials:
          api-key: ${OPENAI_API_KEY}
          
  # Candidate agents (when approved)
  openhands:
    provider: openhands
    enabled: false  # Enable when ready
    interfaces:
      - type: agent-server
        protocol: rest-websocket
        recommended: true
      - type: sdk
        protocol: embedded
      - type: cli
        protocol: spawn-stdio
    models:
      claude-opus:
        enabled: true
      gpt-5:
        enabled: true
      # Provider-neutral: supports many models
      
  cline:
    provider: cline
    enabled: false
    interfaces:
      - type: sdk
        protocol: embedded
        recommended: true
      - type: cli
        protocol: spawn-stdio
    models:
      claude-opus:
        enabled: true
      gpt-5:
        enabled: true
      # Provider-neutral
```

### Workshop Level (Override)

```yaml
# workshop.yaml capable-agents section
capable-agents:
  cursor-agent:
    enabled: true  # Inherits Foundry config
    models:
      claude-opus:
        credentials:
          api-key: ${WORKSHOP_ANTHROPIC_API_KEY}  # Workshop-specific key
          
  copilot:
    enabled: false  # Disabled for this Workshop
```

### Workbench Level (Override)

```yaml
# workbench.yaml capable-agents section
capable-agents:
  cursor-agent:
    models:
      claude-opus:
        credentials:
          api-key: ${PROJECT_ANTHROPIC_API_KEY}  # Project-specific key
```

## Capable Agent Properties

| Property | Description |
|----------|-------------|
| `provider` | Provider name: `cursor`, `github`, `anthropic`, `openai`, `openhands`, `block`, `cline`, `aider` |
| `enabled` | Whether this agent is available at this level |
| `interfaces` | List of supported interfaces (see below) |
| `interfaces.{}.type` | Interface type: `app-server`, `agent-server`, `sdk`, `api`, `cli` |
| `interfaces.{}.protocol` | Protocol: `json-rpc`, `rest-websocket`, `embedded`, `rest`, `spawn-stdio`, `jsonl` |
| `interfaces.{}.recommended` | Whether this is the preferred interface |
| `models` | Map of model configurations |
| `models.{model}.enabled` | Whether this model is available |
| `models.{model}.credentials` | Credential configuration |

## Supported Interfaces

Capable Agents expose different interfaces for WO Runtime integration. Richer interfaces provide more control.

| Interface Type | Protocol | Capabilities | Examples |
|----------------|----------|--------------|----------|
| **app-server** | JSON-RPC, bidirectional | Session lifecycle, events, approvals, tool governance | Codex |
| **agent-server** | REST/WebSocket | Session lifecycle, events, workspace abstraction | OpenHands |
| **sdk** | Embedded library | Lifecycle hooks, callbacks, typed interfaces | Cline |
| **api** | REST calls | Programmatic control, per-call | Goose |
| **cli** | Spawn + stdio | Process-based, env/arg config | Aider, Claude Code |
| **cli-jsonl** | Spawn + JSONL output | Structured output parsing | OpenCode |

### Interface Preference

When a Capable Agent supports multiple interfaces, WO Runtime should prefer richer interfaces:

1. **app-server / agent-server** — richest control
2. **sdk** — embedded integration
3. **api** — programmatic
4. **cli-jsonl** — structured output
5. **cli** — fallback

## Credential Management

### Environment Variable Resolution

Credentials reference environment variables that are resolved at runtime:

```yaml
credentials:
  api-key: ${ANTHROPIC_API_KEY}
```

### Credential Sources

| Level | Source | Example |
|-------|--------|---------|
| Foundry | Foundry secrets store | Org-wide API keys |
| Workshop | Workshop secrets | Team billing keys |
| Workbench | Workbench secrets | Project-specific keys |
| Session | Session environment | User-provided keys (rare) |

### Security Considerations

- Credentials are never stored in Workshop Definition Repository
- Environment variable references point to secure storage
- Access Gateway validates credentials before use
- Credential exposure is limited to the Access Gateway

## Access Gateway Integration

All Capable Agent model calls route through the [Gateway Policy Layer](gateway-policy.md):

```
Employed Agent
    │
    │ Model call + Delegation Token
    ▼
Access Gateway
    │
    │ Resolves credentials from hierarchy
    │ Validates delegation token
    │ Enforces quota
    ▼
Model Provider (Anthropic, OpenAI, etc.)
```

## Auto-Fallback

When a preferred model or capable agent is unavailable, the system automatically falls back to alternatives.

### Fallback Order

For a Skilled Agent with this configuration:

```yaml
compatible-capable-agents:
  - agent: cursor-agent
    models:
      - claude-opus      # 1st preference
      - claude-sonnet    # 2nd preference
  - agent: copilot
    models:
      - gpt-5-thinking   # 3rd preference
      - gpt-5            # 4th preference
```

Fallback proceeds:
1. Try `cursor-agent` with `claude-opus`
2. If unavailable, try `cursor-agent` with `claude-sonnet`
3. If Cursor Agent entirely unavailable, try `copilot` with `gpt-5-thinking`
4. If unavailable, try `copilot` with `gpt-5`
5. If all fail, task enters recoverable failure state

### Unavailability Triggers

| Trigger | Detection | Fallback Behavior |
|---------|-----------|-------------------|
| Model rate-limited | 429 from gateway | Try next model |
| Model unavailable | 503 from provider | Try next model |
| Capable Agent disabled | Config check | Try next capable agent |
| Spawn failure | Process won't start | Try next capable agent |
| Gateway unreachable | Connection timeout | Retry, then fail |

### Fallback Logging

All fallback events are logged:

```json
{
  "event": "agent_fallback",
  "task": "TASK-890",
  "attempted": { "agent": "cursor-agent", "model": "claude-opus" },
  "reason": "model_rate_limited",
  "fallback_to": { "agent": "cursor-agent", "model": "claude-sonnet" }
}
```

---

## Disabled Agent Handling

If a Capable Agent is disabled mid-execution, tasks using it enter a **recoverable failure** state.

### Behavior

```
Task executing with cursor-agent
    │
    ├── Admin disables cursor-agent at Workbench level
    │
    ├── WO Runtime detects agent disabled
    │
    ├── If fallback available:
    │   └── Attempt fallback to next capable agent
    │
    └── If no fallback:
        └── Task pauses (recoverable failure)
            └── Resumes when agent re-enabled
```

### Recoverable Failure States

| Failure Type | Behavior | Resume Trigger |
|--------------|----------|----------------|
| Capable Agent disabled | Task pauses | Agent re-enabled |
| Quota exhausted | Task pauses | Quota refreshes or increased |
| All fallbacks exhausted | Task pauses | Any fallback option restored |

### User Notification

When a task enters recoverable failure:

1. Task status in Jira: `Blocked` with reason
2. Notification in IDE Work Orders Panel
3. Alert to session owner
4. Optionally: alert to Workbench admin

---

## Capable Agent Candidates

The following agent systems are candidates for inclusion in the Capable Agent registry. This matrix captures their interfaces, provider neutrality, and readiness.

→ For detailed architecture comparison, see [Agent Harness Comparison](..//work-order-runtime/platform-developer-guide/design-discussions/agent-harness-comparison.md)

### Candidate Matrix

| Agent | Provider | Primary Interface | Other Interfaces | Model Neutrality | Open Source | Status |
|-------|----------|-------------------|------------------|------------------|-------------|--------|
| **Cursor Agent** | Cursor | CLI | — | Multi-model | No | Current |
| **GitHub Copilot** | GitHub | CLI | — | Multi-model | No | Current |
| **Claude Code** | Anthropic | CLI | — | Anthropic-only | Yes | Current |
| **Codex CLI** | OpenAI | App-server (JSON-RPC) | CLI | OpenAI-only | Partial | Current |
| **Gemini CLI** | Google | CLI | — | Google-only | Yes | Current |
| **OpenHands** | OpenHands | Agent Server (REST/WS) | SDK, CLI | High | Yes | Candidate |
| **Goose** | Block | API | CLI, Desktop | Very High | Yes | Candidate |
| **Cline** | Cline | SDK (TypeScript) | CLI | Very High | Yes | Candidate |
| **Aider** | Aider | CLI | — | Very High | Yes | Candidate |
| **OpenCode** | OpenCode | CLI (JSONL) | — | Very High | Yes | Candidate |

### Model Neutrality Levels

| Level | Description |
|-------|-------------|
| **Very High** | Works with any OpenAI-compatible API; trivial to add providers |
| **High** | Supports multiple providers with configuration |
| **Multi-model** | Supports multiple models from limited providers |
| **Provider-only** | Locked to single provider (Anthropic, OpenAI, Google) |

### Candidate Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Interface richness | High | App-server/Agent Server preferred over CLI |
| Model neutrality | High | Provider flexibility for fallback |
| Production readiness | High | Used in production by originating org |
| Open source | Medium | Source available for extension/debugging |
| Community activity | Medium | Active development and support |
| Foundry alignment | Medium | Fits WO Runtime architecture |

### Candidate Notes

**OpenHands**
- Strongest open platform architecture
- REST/WebSocket Agent Server aligns with WO Runtime needs
- Event-sourced architecture good for audit/replay
- Already provider-neutral
- Recommended for: Production agent platform

**Goose**
- Very broad model provider support
- MCP extensions central to architecture
- Recipes for workflow packaging
- Local-first orientation
- Recommended for: General automation beyond coding

**Cline**
- TypeScript SDK allows embedding
- Strong lifecycle hooks for policy/observability
- IDE heritage may assume VS Code
- Recommended for: TypeScript-based runtime embedding

**Aider**
- Excellent terminal experience
- Very provider-neutral
- No app-server protocol (CLI-only)
- Recommended for: Terminal-first workflows

**OpenCode**
- JSONL output mode for structured parsing
- Provider-neutral
- Emerging; evaluate maturity
- Recommended for: Model-flexible CLI integration

---

## Adding a New Capable Agent

To whitelist a new Capable Agent:

### 1. Evaluate Candidate

- Review against [Candidate Evaluation Criteria](#candidate-evaluation-criteria)
- Document interfaces, models, and provider neutrality
- Assess integration complexity with WO Runtime

### 2. Implement WO Runtime Adapter

Based on the agent's primary interface:

| Interface | Adapter Implementation |
|-----------|------------------------|
| App-server | Implement JSON-RPC client with session management |
| Agent Server | Implement REST/WebSocket client |
| SDK | Embed library, implement lifecycle callbacks |
| API | Implement REST client |
| CLI | Implement process spawn with env/arg config |
| CLI-JSONL | Implement process spawn with output parsing |

→ See [WO Runtime Design Discussion](..//work-order-runtime/platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md) for adapter architecture options

### 3. Register in Capable Agent Registry

**Foundry Admin** adds the agent to Foundry-level `capable-agents.yaml`:

```yaml
capable-agents:
  new-agent:
    provider: provider-name
    enabled: true
    interfaces:
      - type: app-server  # or agent-server, sdk, api, cli
        protocol: json-rpc
        recommended: true
    models:
      model-a:
        enabled: true
        credentials:
          api-key: ${API_KEY}
```

### 4. Test Integration

- Spawn agent with test harness
- Verify session lifecycle (create, attach, terminate)
- Verify tool execution and governance
- Verify fallback behavior
- Test quota enforcement

### 5. Document

- Add agent to [Candidate Matrix](#candidate-matrix) with "Current" status
- Document any agent-specific configuration
- Update [Agent Spawning](..//work-order-runtime/platform-developer-guide/agent-spawning.md) with spawn config

---

## Read Next

- [skilled-agents.md](skilled-agents.md) — How Skilled Agents use Capable Agents
- [gateway-policy.md](gateway-policy.md) — How credentials are used at runtime
- [../work-order-runtime/platform-developer-guide/agent-spawning.md](..//work-order-runtime/platform-developer-guide/agent-spawning.md) — How Capable Agents are spawned
- [../work-order-runtime/platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md](..//work-order-runtime/platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md) — Control plane and adapter architecture options
- [../work-order-runtime/platform-developer-guide/design-discussions/agent-harness-comparison.md](..//work-order-runtime/platform-developer-guide/design-discussions/agent-harness-comparison.md) — Detailed comparison of agent harnesses
