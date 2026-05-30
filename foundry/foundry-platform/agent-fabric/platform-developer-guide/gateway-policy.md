# Gateway Policy

The Agent Fabric module provides configuration and policy for an OSS LLM gateway. Foundry does not build the gateway itself — it configures and manages a proven open-source solution.

## Gateway Selection

Recommended OSS LLM gateways:

| Gateway | License | Strengths | Considerations |
|---------|---------|-----------|----------------|
| **LiteLLM Proxy** | MIT | 100+ providers, spend tracking, caching, load balancing | Most feature-complete |
| **Portkey** | Apache 2.0 | Enterprise features, fallback, load balancing | Strong observability |
| **Helicone** | Apache 2.0 | Cost tracking, logging, caching | Focused on observability |
| **OpenRouter** | — | Unified API, automatic routing | Managed service option |

**Recommendation:** Start with LiteLLM Proxy for comprehensive feature coverage.

## What the Agent Fabric Module Provides

| Responsibility | OSS Gateway | Agent Fabric Module |
|----------------|-------------|-------------------|
| **Request routing** | ✓ | — |
| **Provider abstraction** | ✓ | — |
| **Rate limiting** | ✓ | — |
| **Caching** | ✓ | — |
| **Quota policy definition** | — | ✓ |
| **Delegation token validation** | — | ✓ |
| **Credential injection** | — | ✓ |
| **Audit log aggregation** | — | ✓ |
| **Cost attribution** | ✓ (raw data) | ✓ (by WO/Task/User) |

The module sits above the gateway, providing Foundry-specific policy.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  Employed Agent (in Workspace Session)                          │
│                                                                 │
│  All model calls go through gateway URL:                       │
│  FOUNDRY_GATEWAY_URL=https://gateway.foundry.internal          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTPS + Delegation Token
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Foundry Gateway Policy Layer                                   │
│  (Sidecar or middleware on OSS gateway)                        │
│                                                                 │
│  • Validate delegation token                                   │
│  • Enforce quota policy                                        │
│  • Inject provider credentials from Capable Agent registry     │
│  • Tag request with WO/Task metadata for cost attribution      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Provider-agnostic call
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  OSS LLM Gateway (LiteLLM / Portkey / etc.)                    │
│                                                                 │
│  • Route to provider (Anthropic, OpenAI, Google, Azure)        │
│  • Handle retries, fallback, load balancing                    │
│  • Cache responses (if enabled)                                │
│  • Log usage metrics                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Model Providers                                                │
│  Anthropic, OpenAI, Google, Azure, etc.                        │
└─────────────────────────────────────────────────────────────────┘
```

## Quota Policy

### Quota Levels

Quotas are configured at three levels:

| Level | Scope | Example |
|-------|-------|---------|
| **Foundry** | Organization-wide | $50K/month total |
| **Workbench** | Product-specific | $2K/month for Checkout |
| **(Foundry, User)** | User's global limit | Alice: $500/month org-wide |
| **(Workbench, User)** | User's product limit | Alice on Checkout: $200/month |

Effective quota = **minimum** of all applicable limits.

### Quota Policy Schema

```yaml
# quota-policy.yaml (Foundry level)
quota:
  foundry:
    monthly_budget_usd: 50000
    daily_token_limit: 100000000
    
  workbenches:
    checkout:
      monthly_budget_usd: 2000
    payments:
      monthly_budget_usd: 5000
      
  user_defaults:
    monthly_budget_usd: 500
    daily_token_limit: 1000000
    
  user_overrides:
    alice@example.com:
      monthly_budget_usd: 1000
    bob@example.com:
      workbench_limits:
        checkout:
          monthly_budget_usd: 300
```

### Quota Enforcement

```
1. Extract session_owner from Delegation Token
2. Look up all applicable quotas:
   - Foundry quota
   - Workbench quota (from token)
   - (Foundry, User) quota
   - (Workbench, User) quota
3. Effective limit = min(all applicable)
4. Check current usage against effective limit
5. If exceeded → 429 (task enters recoverable failure)
6. If OK → forward to OSS gateway
```

### Quota Exhaustion Behavior

When quota is exhausted:

1. Gateway returns 429 with `X-Quota-Reset: <timestamp>`
2. WO Runtime receives 429
3. Task enters **recoverable failure** state
4. Task metadata records: `blocked_reason: quota_exhausted`
5. Task resumes automatically when quota refreshes

## Delegation Token Handling

### Token Flow

```
WO Runtime
    │
    ├── Generates Delegation Token (JWT, signed)
    │   - session_owner, session_id, workbench_id
    │   - granted_scopes (which models allowed)
    │   - work_order, task (for attribution)
    │
    └── Passes to Employed Agent
            │
            └── Agent includes in Authorization header
                    │
                    └── Gateway Policy Layer validates:
                        - Signature (RS256)
                        - Expiry
                        - Scope match (requested model in granted_scopes)
```

### Token Schema

```json
{
  "session_owner": "alice@example.com",
  "session_id": "ws-dev-12345",
  "workbench_id": "checkout",
  "workspace_type": "development",
  "granted_scopes": ["model:claude-opus", "model:claude-sonnet"],
  "work_order": "WO-567",
  "task": "TASK-890",
  "issued_at": "2026-05-28T02:00:00Z",
  "expires_at": "2026-05-28T14:00:00Z"
}
```

## Credential Injection

Provider credentials are **never exposed** to agents. The Gateway Policy Layer injects them:

```
1. Agent requests model: claude-opus
2. Policy layer looks up Capable Agent registry:
   - Workbench credentials? Use those
   - Else Workshop credentials? Use those
   - Else Foundry credentials? Use those
3. Inject credential into request to OSS gateway
4. OSS gateway forwards with credential to provider
```

## Cost Attribution

### Attribution Dimensions

Costs are attributed along multiple dimensions:

| Dimension | Source |
|-----------|--------|
| **Session Owner** | Delegation Token |
| **Work Order** | Delegation Token |
| **Task** | Delegation Token |
| **Workbench** | Delegation Token |
| **Skilled Agent** | Request metadata |
| **Capable Agent** | Request metadata |
| **Model** | Request/response |

### Attribution Data Flow

```
OSS Gateway logs raw usage
    │
    └── { model, tokens, cost, timestamp }
            │
            └── Agent Fabric module enriches from Delegation Token
                    │
                    └── { ..., session_owner, work_order, task, workbench }
                            │
                            └── Stored in usage analytics
```

### Billing Reports

Available reports:

- **By User** — Monthly cost per session owner
- **By Workbench** — Monthly cost per product
- **By Work Order** — Cost per orchestration item
- **By Model** — Usage distribution across models
- **By Skill** — Usage per skill package

## Audit Logging

### Audit Record

Every model call generates an audit record:

```json
{
  "timestamp": "2026-05-28T02:30:00.123Z",
  "session_owner": "alice@example.com",
  "workbench_id": "checkout",
  "work_order": "WO-567",
  "task": "TASK-890",
  "skilled_agent": "feature-implementation-agent",
  "capable_agent": "cursor-agent",
  "model": "claude-opus",
  "input_tokens": 5234,
  "output_tokens": 2341,
  "cost_usd": 0.254,
  "latency_ms": 3421,
  "status": "success"
}
```

### Retention

| Level | Duration |
|-------|----------|
| Full records | 90 days |
| Aggregated metrics | 1 year |
| Cost summaries | 7 years |

## LiteLLM Configuration Example

If using LiteLLM Proxy:

```yaml
# litellm_config.yaml
model_list:
  - model_name: claude-opus
    litellm_params:
      model: claude-3-opus-20240229
      api_key: os.environ/ANTHROPIC_API_KEY
      
  - model_name: claude-sonnet
    litellm_params:
      model: claude-3-5-sonnet-20241022
      api_key: os.environ/ANTHROPIC_API_KEY

  - model_name: gpt-5
    litellm_params:
      model: gpt-5
      api_key: os.environ/OPENAI_API_KEY

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: os.environ/POSTGRES_URL

litellm_settings:
  drop_params: true
  callbacks: ["langfuse"]  # or custom audit callback
```

The Gateway Policy Layer runs as middleware that:
1. Intercepts requests before LiteLLM
2. Validates Delegation Tokens
3. Checks quota
4. Injects credentials
5. Tags request metadata for audit

## Worked examples: Allow/deny path configurations

These examples show how platform implementers can configure the Gateway Policy Layer for common scenarios.

### Example 1: Allow specific models per Workbench

Restrict the Checkout Workbench to only use Claude models:

```yaml
# gateway-policy.yaml
rules:
  - name: checkout-claude-only
    match:
      workbench_id: checkout
    allow:
      models:
        - claude-opus
        - claude-sonnet
    deny:
      models:
        - gpt-*        # Deny all GPT models
        - gemini-*     # Deny all Gemini models
```

**Request flow:**
```
Agent requests gpt-5 → Gateway matches "checkout" Workbench → Denies (model not in allow list) → 403
Agent requests claude-opus → Gateway matches "checkout" Workbench → Allows → Forward to LiteLLM
```

### Example 2: Deny expensive models for non-production Workspaces

Prevent non-production work from using expensive thinking models:

```yaml
rules:
  - name: deny-thinking-in-dev
    match:
      workspace_type:
        - development
        - qa
    deny:
      models:
        - "*-thinking"  # claude-opus-thinking, gpt-5-thinking, etc.
    message: "Thinking models are restricted to production use"
```

**Request flow:**
```
Dev WO requests claude-opus-thinking → Gateway matches dev Workspace → Denies → 403 with message
Release WO requests claude-opus-thinking → No matching rule → Allows
```

### Example 3: Allow all except specific blocked models

Allow most models but block deprecated or restricted ones:

```yaml
rules:
  - name: block-deprecated
    match:
      scope: foundry  # Apply to entire Foundry
    deny:
      models:
        - gpt-4-turbo  # Deprecated
        - palm-*       # Unsupported provider
    allow:
      models:
        - "*"  # Allow everything else
```

### Example 4: Cost-cap enforcement with model tiers

Define model tiers and enforce per-request cost caps:

```yaml
rules:
  - name: cost-cap-by-tier
    match:
      scope: foundry
    tiers:
      economy:
        models: [claude-sonnet, gpt-4o-mini]
        max_cost_per_request_usd: 0.10
      standard:
        models: [claude-opus, gpt-5]
        max_cost_per_request_usd: 1.00
      premium:
        models: [claude-opus-thinking, gpt-5-thinking]
        max_cost_per_request_usd: 5.00
        require_justification: true
```

**Request flow:**
```
Agent requests claude-opus with estimated 50K tokens → ~$2.50 → Exceeds standard tier cap → 402 Payment Required
Agent adds justification header → Request allowed if premium tier budget available
```

### Example 5: Time-based access control

Restrict expensive models to business hours:

```yaml
rules:
  - name: premium-business-hours
    match:
      models: ["*-thinking"]
    allow:
      time_window:
        days: [monday, tuesday, wednesday, thursday, friday]
        hours: "08:00-18:00"
        timezone: "America/New_York"
    deny:
      outside_window: true
      message: "Premium models available 8am-6pm ET weekdays only"
```

### Example 6: Workspace-specific model routing

Route different Workspaces to different model preferences:

```yaml
rules:
  - name: workspace-model-preferences
    routing:
      - match:
          workspace_type: governance
        prefer:
          models: [claude-opus]  # Strong reasoning for governance
      - match:
          workspace_type: development
        prefer:
          models: [claude-sonnet, gpt-5]  # Fast iteration
      - match:
          workspace_type: qa
        prefer:
          models: [claude-opus]  # Thorough testing
```

### Policy evaluation order

1. Explicit `deny` rules are evaluated first
2. Explicit `allow` rules are evaluated second
3. If no rule matches, default to allow (configurable)
4. Quota checks occur after policy evaluation

### Testing policies

Use the policy simulation endpoint to test rules before deployment:

```bash
curl -X POST /api/v1/gateway/policy/simulate \
  -H "Content-Type: application/json" \
  -d '{
    "workbench_id": "checkout",
    "workspace_type": "development",
    "model": "gpt-5-thinking",
    "user_id": "alice@example.com"
  }'

# Response:
{
  "allowed": false,
  "denied_by": "deny-thinking-in-dev",
  "message": "Thinking models are restricted to production use"
}
```

## Read Next

- [capable-agents.md](capable-agents.md) — Credential resolution hierarchy
- [employed-agents.md](employed-agents.md) — Delegation Token lifecycle
- [skill-registry.md](skill-registry.md) — Skill usage tracking
- [../work-order-runtime/platform-developer-guide/agent-spawning.md](..//work-order-runtime/platform-developer-guide/agent-spawning.md) — Token provisioning
