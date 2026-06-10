# Raw Agents

Raw Agents are OCI containers that package agent systems for deployment in Foundry. This specification covers the OCI manifest format, deployment modes, interface types, and the registry model.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Agent** | Defines Raw Agents as the packaging-layer agent systems (Codex, Cursor Agent, Claude Code) |
| **Delegation** | Credentials resolved hierarchically and injected via Access Gateway |
| **Workspace** | Deployment mode adapts to target (container runtime OR Coder workspace program) |

## Definition

A **Raw Agent** is an OCI container that packages an agent system with its orchestration, tool use, context management, and swarm capabilities. It represents the deployable "engine" — what an agent *can* do structurally.

**Platform-shipped Raw Agents:**
- Codex — `registry.foundry.io/raw-agents/codex:v2.4.1`
- Cursor Agent — `registry.foundry.io/raw-agents/cursor-agent:v1.2.0`
- Claude Code — `registry.foundry.io/raw-agents/claude-code:v1.0.3`
- Gemini CLI — `registry.foundry.io/raw-agents/gemini-cli:v0.8.0`

**Candidate agents under evaluation:**
- OpenHands
- Goose
- Cline
- Aider
- OpenCode

→ See [Raw Agent Candidates](#raw-agent-candidates) for the full evaluation matrix

## Raw Agent vs Model

| Concept | Definition | Examples |
|---------|------------|----------|
| **Raw Agent** | OCI container with orchestration capabilities | `registry.foundry.io/raw-agents/codex:v2.4.1` |
| **Model** | Underlying LLM that powers reasoning | claude-opus, gpt-5-thinking, gemini-pro |

A Raw Agent may support multiple models:

```
Raw Agent: registry.foundry.io/raw-agents/codex:v2.4.1
├── Model: codex-3
├── Model: gpt-5
└── Model: gpt-5-thinking

Raw Agent: registry.foundry.io/raw-agents/cursor-agent:v1.2.0
├── Model: claude-opus
├── Model: claude-sonnet
└── Model: gpt-5

Raw Agent: registry.foundry.io/raw-agents/claude-code:v1.0.3
├── Model: claude-opus
└── Model: claude-sonnet
```

## OCI Packaging

Raw Agents use OCI (Open Container Initiative) as the universal packaging format. The OCI image contains:

| Component | Purpose |
|-----------|---------|
| **Agent runtime** | The executable agent system |
| **Dependencies** | Libraries, tools, and runtime requirements |
| **Manifest** | Declares capabilities, interfaces, models |
| **Configuration** | Default settings and environment templates |

### OCI Manifest Schema

Each Raw Agent OCI image includes a manifest at `/foundry/agent-manifest.yaml`:

```yaml
apiVersion: foundry.io/v1
kind: RawAgent
metadata:
  name: codex
  version: 2.4.1
  provider: openai
  description: OpenAI Codex agent with app-server interface
spec:
  interfaces:
    - type: app-server
      protocol: json-rpc
      port: 8080
      recommended: true
    - type: cli
      protocol: spawn-stdio
  models:
    - name: codex-3
      provider: openai
      default: true
    - name: gpt-5
      provider: openai
    - name: gpt-5-thinking
      provider: openai
  deployment:
    modes:
      - container
      - workspace-program
    resources:
      cpu: 2
      memory: 4Gi
      gpu: optional
  capabilities:
    - code-generation
    - code-review
    - test-writing
    - refactoring
```

## Two-Layer Distribution Model

Raw Agents are distributed through a two-layer registry model:

| Layer | Registry URI | Visibility | Managed By |
|-------|--------------|------------|------------|
| **Platform-shipped** | `registry.foundry.io/raw-agents/{agent}:{version}` | All tenants | Foundry Platform |
| **Tenant-added** | `registry.{tenant}.foundry.io/raw-agents/{agent}:{version}` | Organization only | Tenant Org |

### Discovery Order

When resolving a Raw Agent reference:

1. Check tenant registry (`registry.{tenant}.foundry.io/raw-agents/...`)
2. Fall back to platform registry (`registry.foundry.io/raw-agents/...`)

This allows tenants to:
- Override platform-shipped agents with custom versions
- Add proprietary agents not available in the platform registry
- Pin specific versions for compliance requirements

## Deployment Modes

Raw Agents support two deployment modes, declared in the OCI manifest:

| Mode | Target | Use Case |
|------|--------|----------|
| **container** | Container runtime (Kubernetes, Docker) | Production, CI/CD, serverless |
| **workspace-program** | Coder workspace | Interactive development |

### Container Mode

```yaml
deployment:
  modes:
    - container
  container:
    image: registry.foundry.io/raw-agents/codex:v2.4.1
    command: ["/usr/bin/codex-agent"]
    ports:
      - containerPort: 8080
        protocol: TCP
    env:
      - name: FOUNDRY_WORKSPACE_ID
        valueFrom:
          fieldRef:
            fieldPath: metadata.labels['foundry.io/workspace-id']
```

### Workspace Program Mode

```yaml
deployment:
  modes:
    - workspace-program
  workspace-program:
    install-command: "foundry agent install codex@2.4.1"
    run-command: "codex-agent --workspace ${WORKSPACE_PATH}"
    cleanup-command: "foundry agent uninstall codex"
```

## Raw Agent Properties

| Property | Description |
|----------|-------------|
| `metadata.name` | Agent identifier (lowercase, alphanumeric) |
| `metadata.version` | Semantic version |
| `metadata.provider` | Provider name: `openai`, `anthropic`, `cursor`, `google`, `openhands` |
| `spec.interfaces` | List of supported interfaces (see below) |
| `spec.interfaces[].type` | Interface type: `app-server`, `agent-server`, `sdk`, `api`, `cli` |
| `spec.interfaces[].protocol` | Protocol: `json-rpc`, `rest-websocket`, `embedded`, `rest`, `spawn-stdio` |
| `spec.interfaces[].recommended` | Whether this is the preferred interface |
| `spec.models` | List of supported models |
| `spec.deployment.modes` | Supported deployment modes: `container`, `workspace-program` |
| `spec.deployment.resources` | Resource requirements (cpu, memory, gpu) |
| `spec.capabilities` | Declared capabilities for matching |

## Supported Interfaces

Raw Agents expose different interfaces for WO Runtime integration. Richer interfaces provide more control.

| Interface Type | Protocol | Capabilities | Examples |
|----------------|----------|--------------|----------|
| **app-server** | JSON-RPC, bidirectional | Session lifecycle, events, approvals, tool governance | Codex |
| **agent-server** | REST/WebSocket | Session lifecycle, events, workspace abstraction | OpenHands |
| **sdk** | Embedded library | Lifecycle hooks, callbacks, typed interfaces | Cline |
| **api** | REST calls | Programmatic control, per-call | Goose |
| **cli** | Spawn + stdio | Process-based, env/arg config | Aider, Claude Code |
| **cli-jsonl** | Spawn + JSONL output | Structured output parsing | OpenCode |

### Interface Preference

When a Raw Agent supports multiple interfaces, WO Runtime should prefer richer interfaces:

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

All Raw Agent model calls route through the [Gateway Policy Layer](gateway-policy.md):

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

When a preferred model or Raw Agent is unavailable, the system automatically falls back to alternatives.

### Fallback Order

For a Trained Agent with this configuration:

```yaml
compatible-raw-agents:
  - agent: registry.foundry.io/raw-agents/cursor-agent:v1.2.0
    models:
      - claude-opus      # 1st preference
      - claude-sonnet    # 2nd preference
  - agent: registry.foundry.io/raw-agents/codex:v2.4.1
    models:
      - gpt-5-thinking   # 3rd preference
      - gpt-5            # 4th preference
```

Fallback proceeds:
1. Try `cursor-agent` with `claude-opus`
2. If unavailable, try `cursor-agent` with `claude-sonnet`
3. If Cursor Agent entirely unavailable, try `codex` with `gpt-5-thinking`
4. If unavailable, try `codex` with `gpt-5`
5. If all fail, task enters recoverable failure state

### Unavailability Triggers

| Trigger | Detection | Fallback Behavior |
|---------|-----------|-------------------|
| Model rate-limited | 429 from gateway | Try next model |
| Model unavailable | 503 from provider | Try next model |
| Raw Agent unavailable | OCI pull failure | Try next Raw Agent |
| Spawn failure | Process won't start | Try next Raw Agent |
| Gateway unreachable | Connection timeout | Retry, then fail |

### Fallback Logging

All fallback events are logged:

```json
{
  "event": "agent_fallback",
  "task": "TASK-890",
  "attempted": { "agent": "cursor-agent:v1.2.0", "model": "claude-opus" },
  "reason": "model_rate_limited",
  "fallback_to": { "agent": "cursor-agent:v1.2.0", "model": "claude-sonnet" }
}
```

---

## Unavailable Agent Handling

If a Raw Agent becomes unavailable mid-execution, tasks using it enter a **recoverable failure** state.

### Behavior

```
Task executing with cursor-agent
    │
    ├── Raw Agent becomes unavailable (registry issue, OCI pull failure)
    │
    ├── WO Runtime detects agent unavailable
    │
    ├── If fallback available:
    │   └── Attempt fallback to next Raw Agent
    │
    └── If no fallback:
        └── Task pauses (recoverable failure)
            └── Resumes when agent restored
```

### Recoverable Failure States

| Failure Type | Behavior | Resume Trigger |
|--------------|----------|----------------|
| Raw Agent unavailable | Task pauses | Agent restored in registry |
| Quota exhausted | Task pauses | Quota refreshes or increased |
| All fallbacks exhausted | Task pauses | Any fallback option restored |

### User Notification

When a task enters recoverable failure:

1. Task status in Jira: `Blocked` with reason
2. Notification in IDE Work Orders Panel
3. Alert to session owner
4. Optionally: alert to Workbench admin

---

## Raw Agent Candidates

The following agent systems are candidates for packaging as Raw Agents. This matrix captures their interfaces, provider neutrality, and readiness.

→ For detailed architecture comparison, see [Agent Harness Comparison](../../work-order-runtime/platform-developer-guide/design-discussions/agent-harness-comparison.md)

### Candidate Matrix

| Agent | Provider | Primary Interface | Other Interfaces | Model Neutrality | Open Source | Status |
|-------|----------|-------------------|------------------|------------------|-------------|--------|
| **Codex** | OpenAI | App-server (JSON-RPC) | CLI | OpenAI-only | Partial | Platform-shipped |
| **Cursor Agent** | Cursor | CLI | — | Multi-model | No | Platform-shipped |
| **Claude Code** | Anthropic | CLI | — | Anthropic-only | Yes | Platform-shipped |
| **Gemini CLI** | Google | CLI | — | Google-only | Yes | Platform-shipped |
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
| OCI compatibility | High | Can be packaged as OCI container |
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

## Adding a New Raw Agent

To package and register a new Raw Agent:

### 1. Evaluate Candidate

- Review against [Candidate Evaluation Criteria](#candidate-evaluation-criteria)
- Document interfaces, models, and provider neutrality
- Assess integration complexity with WO Runtime

### 2. Create OCI Package

Build the OCI container image with:

1. Agent runtime and dependencies
2. Foundry agent manifest at `/foundry/agent-manifest.yaml`
3. Entrypoint configured for supported interfaces

```dockerfile
FROM foundry-agent-base:latest

COPY agent-binary /usr/bin/agent
COPY agent-manifest.yaml /foundry/agent-manifest.yaml

ENTRYPOINT ["/usr/bin/agent"]
```

### 3. Implement WO Runtime Adapter

Based on the agent's primary interface:

| Interface | Adapter Implementation |
|-----------|------------------------|
| App-server | Implement JSON-RPC client with session management |
| Agent Server | Implement REST/WebSocket client |
| SDK | Embed library, implement lifecycle callbacks |
| API | Implement REST client |
| CLI | Implement process spawn with env/arg config |
| CLI-JSONL | Implement process spawn with output parsing |

→ See [WO Runtime Design Discussion](../../work-order-runtime/platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md) for adapter architecture options

### 4. Register in Raw Agent Registry

Push to the appropriate registry:

```bash
# Platform-shipped (requires platform admin)
docker push registry.foundry.io/raw-agents/new-agent:v1.0.0

# Tenant-added
docker push registry.acme.foundry.io/raw-agents/new-agent:v1.0.0
```

Register metadata via Registry API — see [raw-agent-registry.md](raw-agent-registry.md).

### 5. Test Integration

- Spawn agent with test harness
- Verify session lifecycle (create, attach, terminate)
- Verify tool execution and governance
- Verify fallback behavior
- Test quota enforcement

### 6. Document

- Add agent to [Candidate Matrix](#candidate-matrix) with appropriate status
- Document any agent-specific configuration
- Update [Agent Spawning](../../work-order-runtime/platform-developer-guide/agent-spawning.md) with spawn config

---

## Read Next

- [trained-agents.md](trained-agents.md) — How Trained Agents reference Raw Agents
- [raw-agent-registry.md](raw-agent-registry.md) — Registry API and discovery
- [gateway-policy.md](gateway-policy.md) — How credentials are used at runtime
- [../../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — How Raw Agents are spawned
- [../../work-order-runtime/platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md](../../work-order-runtime/platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md) — Control plane and adapter architecture options
- [../../work-order-runtime/platform-developer-guide/design-discussions/agent-harness-comparison.md](../../work-order-runtime/platform-developer-guide/design-discussions/agent-harness-comparison.md) — Detailed comparison of agent harnesses
