[1 tool called]

I've reviewed Bifrost. Here's what I understand — now my Seer-specific questions:

---

## Seer Model Gateway — Clarifying Questions

### 1. Bifrost Integration

1.1. **Deployment Model**: Is Bifrost deployed:
   - Per-cluster (shared by all tenants)?
   - Per-tenant (isolated instance)?
   - Per-workbench?

Platform level; One instance for one instance of Hub.

1.2. **Customization**: What Seer/Hub-specific customizations have been made to Bifrost?
   - Hub authentication integration?
   - CAF audit logging?
   - OPA policy integration?
   - Others?

> IAM and Access Control Integrations
> OPA Policies
> No CAF; LLM Calls are not regarded as Enterprise auditable events.
> Olympus Watch

---

### 2. Model Catalog

2.1. **Provider Configuration**: Who configures available providers (OpenAI, Anthropic, etc.)?
   - Platform team (global)?
   - Tenant admin (per-workbench)?
   - Both (platform provides, tenant enables)?

> Tenant Admins
> Each Seer Subscription (associated Hub Subscription) can define their own providers and provide the corresponding access credentials

2.2. **Custom Models**: Can tenants add custom deployed models (e.g., fine-tuned models on SageMaker)?

> Yes; But not in scope for this discussion
---

### 3. Routing and Fallback

3.1. **Model Selection**: How does an agent specify which model to use?
   - By name (e.g., `gpt-4o`)?
   - By capability (e.g., `reasoning`, `code`)?
   - By Training/Employment Spec constraints?

> Raw Agents provide a whitelist of supported models by name
> Training Spec and Employment spec can pick subset of them by name

3.2. **Fallback Configuration**: Is fallback:
   - Automatic (Bifrost decides)?
   - Configured in Employment Spec?
   - Configured by tenant admin?

> Configured by tenant admin
---

### 4. Governance

4.1. **Budgets**: Are budgets enforced at:
   - Agent level (per Employed Agent)?
   - Workbench level?
   - Scenario level?
   - Request level?

> Workbench, (Workbench, Agent)

4.2. **Virtual Keys**: How do virtual keys map to Hub concepts?
   - One key per Employed Agent?
   - One key per Workbench?
   - Dynamic (per-request)?

> One key per Employed Agent

---

### 5. Observability

5.1. **Token Tracking**: Where are token usage metrics exposed?
   - Prometheus (Atlantis)?
   - Olympus Watch?
   - Both?
> Prometheus exporter interface
> Olympus Watch scrapes and provides analtyics and alerts

5.2. **Audit Logging**: Are LLM calls logged to:
   - CAF (Cognitive Audit Fabric)?
   - Separate LLM audit store?
   - Both?
> These are treated as operational logs and managed under Watch

---

### 6. Agent Access

6.1. **SDK/API**: How do agents call Model Gateway?
   - OpenAI-compatible API (just change `base_url`)?
   - Seer SDK wrapper?
   - Both?

> Just use the URL from environment. 

6.2. **Endpoint Discovery**: How does an agent know the Model Gateway URL?
   - Environment variable (injected at deployment)?
   - Service mesh internal routing?
> environment
---

Answer what you can, and I'll document based on your responses.