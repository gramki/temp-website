# Capable Agents

Capable Agents are whitelisted frontier models and agent systems that provide the core capabilities for agentic work in Foundry.

## Definition

A **Capable Agent** is an agent system with orchestration, tool use, context management, and swarm capabilities. It represents the "engine" — what an agent *can* do structurally.

**Examples:**
- Cursor Agent
- GitHub Copilot
- Claude Code
- Codex CLI
- Gemini CLI

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
    type: ide-agent
    provider: cursor
    enabled: true
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
    type: ide-agent
    provider: github
    enabled: true
    models:
      gpt-5:
        enabled: true
      gpt-5-thinking:
        enabled: true
        
  claude-code:
    type: cli-agent
    provider: anthropic
    enabled: true
    models:
      claude-opus:
        enabled: true
        credentials:
          api-key: ${ANTHROPIC_API_KEY}
          
  codex-cli:
    type: cli-agent
    provider: openai
    enabled: true
    models:
      codex-3:
        enabled: true
        credentials:
          api-key: ${OPENAI_API_KEY}
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
| `type` | Agent type: `ide-agent`, `cli-agent` |
| `provider` | Provider name: `cursor`, `github`, `anthropic`, `openai` |
| `enabled` | Whether this agent is available at this level |
| `models` | Map of model configurations |
| `models.{model}.enabled` | Whether this model is available |
| `models.{model}.credentials` | Credential configuration |

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

## Adding a New Capable Agent

To whitelist a new Capable Agent:

1. **Foundry Admin** adds the agent to Foundry-level `capable-agents.yaml`
2. Define supported models and default credentials
3. Implement spawn adapter in WO Runtime (agent-specific)
4. Workshops and Workbenches can then enable/disable and override credentials

## Read Next

- [skilled-agents.md](skilled-agents.md) — How Skilled Agents use Capable Agents
- [gateway-policy.md](gateway-policy.md) — How credentials are used at runtime
- [../work-order-runtime/agent-spawning.md](../work-order-runtime/agent-spawning.md) — How Capable Agents are spawned
