# Agent Reliability Engineer (ARE)

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [Role Definitions](./roles.md) | [AE Deliverables to ARE](./needs/ae-deliverables-to-are.md)  
> **Detailed Needs:** [Production Readiness Requirements](./needs/production-readiness.md)

---

## The Problem ARE Solves

Traditional reliability engineering assumes deterministic systems. You deploy code, it runs, it either works or throws an error. Failures are binary. Costs are predictable.

**Agents break all of these assumptions.**

An agent can:
- Make a *correct* decision that costs 100x what it should
- Complete a task successfully while violating three policies
- Run for hours in a reasoning loop without any error
- Invoke tools in ways the developer never anticipated
- Cascade a single bad judgment across an entire workflow

These aren't bugs. They're emergent properties of autonomous systems.

**ARE exists because someone has to answer:** *"Is this agent safe to run right now?"*

Not "Is the agent smart?" Not "Will the business benefit?" Just: *Can we let it operate without losing control?*

---

## The ARE Mandate

> **ARE owns runtime trustworthiness.**

This means:

| ARE Ensures | ARE Does NOT Judge |
|-------------|-------------------|
| The agent can be stopped | Whether the agent is right |
| The agent stays within cost bounds | Whether the agent is valuable |
| The agent's behavior is observable | What the agent should do |
| Failures are contained | Business strategy |
| Recovery is possible | Autonomy policy |

**The distinction matters.** ARE is not a gatekeeper for intelligence. ARE is a gatekeeper for *operability*.

An ARE might approve a mediocre agent that's well-bounded and reject a brilliant agent that's unobservable. That's the job.

---

## Why This Role Is Different

### It's Not DevOps

DevOps ensures infrastructure runs. ARE ensures *autonomous behavior* runs safely. The failure modes are different:

| DevOps Failure | ARE Failure |
|----------------|-------------|
| Server down | Agent in infinite loop |
| Network timeout | Agent spent $500 on a $5 task |
| Deployment failed | Agent violated policy undetected |
| Disk full | Agent cascaded bad decision to 12 workflows |

### It's Not MLOps

MLOps manages model lifecycle — training, versioning, deployment. ARE manages *what happens when the model is reasoning live* in production with real stakes.

### It's Not QA

QA validates that the agent works correctly in test scenarios. ARE ensures the agent *remains controlled* when reality diverges from tests.

---

## What ARE Cares About

### 1. Can We Stop It?

Every agent must have:
- A kill switch that works immediately
- Execution bounds that cannot be exceeded
- Tool access that can be revoked at runtime
- Cost ceilings that halt execution when breached

**If the answer is "we'd have to redeploy to stop it," the agent isn't ready.**

---

### 2. Can We See What It's Doing?

Agents reason internally. That reasoning must be:
- Logged in a structured, queryable format
- Correlated across tasks and workflows
- Attributable to specific decisions and actions
- Available in near-real-time, not batched

**If an agent fails and we can't explain why within 15 minutes, the observability is insufficient.**

---

### 3. Is It Economically Sane?

Agents consume tokens, invoke APIs, and use compute. Unlike traditional software, these costs are:
- Unbounded by default
- Variable per execution
- Compounding across retries and reasoning steps

ARE tracks cost not as a finance function, but as a *safety signal*. A cost spike often indicates:
- Reasoning loops
- Retry storms
- Tool abuse
- Prompt injection attempts

**If an agent can spend unlimited money without triggering an alert, it's not production-ready.**

---

### 4. Does It Fail Gracefully?

When an agent fails, it should:
- Fail to a known state
- Emit a structured error
- Not take other agents down with it
- Allow human takeover

**If an agent failure is silent, ambiguous, or cascading, the design is incomplete.**

---

### 5. Can We Recover?

Recovery means:
- Rollback to previous agent version
- Replay failed tasks with modified context
- Isolate affected workflows
- Restore normal operation within defined RTO

**If recovery requires engineering intervention, the system isn't operationally mature.**

---

## The ARE Control Loop

ARE uses exactly two signals to assess operational health:

### Agent Health Score (AHS)

AHS answers: *"Is the agent functioning properly?"*

> **Note:** AHS is a Seer-defined composite metric. It is not an industry standard, but represents how Seer thinks about agent operational health.

```
AHS = Task Completion Score × Action Quality Multiplier
```

**Task Completion Score (TCS)** — weighted composite:

| Signal | Weight | What It Measures |
|--------|--------|------------------|
| Task Success Rate | 50% | Did tasks complete? |
| SLA Adherence | 30% | Did they complete on time? |
| First-Time Resolution | 20% | Did they complete without rework? |

**Action Quality Multiplier (AQM)** — penalty-based:

| Event | Penalty | Why It Matters |
|-------|---------|----------------|
| Human Override | -0.02 | Agent judgment was wrong |
| Escalation | -0.01 | Agent couldn't handle it |
| Policy Violation | -0.05 | Agent broke rules |
| Tool Failure | -0.01 | Agent misused capabilities |
| Excess Retries (>3) | -0.01 each | Agent is thrashing |

AQM floors at 0.5 to prevent total collapse.

**AHS Interpretation:**

| Score | Status | Action |
|-------|--------|--------|
| 0.90+ | Healthy | Continue |
| 0.75–0.89 | Friction | Monitor |
| 0.60–0.74 | Degraded | Investigate |
| <0.60 | Failing | Intervene |

---

### Cost-to-Health Ratio (CHR)

CHR answers: *"Is the cost proportional to agent health?"*

```
CHR = Total Operational Cost / AHS
```

**CHR is a ratio to stabilize, not minimize.**

| CHR Pattern | Meaning |
|-------------|---------|
| Stable CHR, high AHS | Healthy — cost tracks quality |
| Rising CHR, stable AHS | Inefficiency — investigate cost drivers |
| Rising CHR, falling AHS | Crisis — quality and cost both degrading |
| Falling CHR, stable AHS | Improving — efficiency gains |

A very low CHR with low AHS is *worse* than moderate CHR with high AHS. Cheap failures are still failures.

---

## Metrics ARE Monitors

Beyond AHS and CHR, ARE tracks operational metrics in real-time.

---

### System Health Metrics

| Metric | What It Tells ARE | Alert Threshold |
|--------|-------------------|-----------------|
| **Agent Availability** | Is the agent accepting tasks? | < 99.5% |
| **Task Latency (p50, p95, p99)** | How long are tasks taking? | p95 > 2x baseline |
| **Error Rate** | What fraction of executions fail? | > 1% |
| **Queue Depth** | Are tasks backing up? | > 10x normal |
| **Dependency Health** | Are tools/APIs responding? | Any dependency < 99% |

---

### Agent Behavior Metrics

| Metric | What It Tells ARE | Alert Threshold |
|--------|-------------------|-----------------|
| **Reasoning Steps per Task** | Is the agent overthinking? | > 2x median |
| **Tool Invocations per Task** | Is tool usage reasonable? | > 3x median |
| **Retry Rate** | Is the agent thrashing? | > 10% |
| **Timeout Rate** | Are tasks timing out? | > 2% |
| **Loop Detection Events** | Is the agent stuck? | Any occurrence |

---

### Cost Metrics

| Metric | What It Tells ARE | Alert Threshold |
|--------|-------------------|-----------------|
| **Token Usage per Task** | Is reasoning efficient? | > 2x median |
| **API Cost per Task** | Are tool costs reasonable? | > 3x median |
| **Cost Velocity** | How fast is spend accumulating? | > 150% of budget rate |
| **Cost per Successful Task** | What's the effective cost? | Trending up > 20% |
| **Budget Utilization** | How much runway remains? | > 80% of period budget |

---

### Safety Metrics

| Metric | What It Tells ARE | Alert Threshold |
|--------|-------------------|-----------------|
| **Policy Violation Rate** | Is the agent following rules? | Any increase |
| **Escalation Rate** | Is the agent within capability? | > 5% |
| **Human Override Rate** | Is agent judgment trusted? | > 3% |
| **Kill Switch Activations** | Emergency stops triggered | Any occurrence |
| **Guardrail Block Rate** | How often are guardrails firing? | > 10% (investigate) |

---

### Incident Metrics

| Metric | What It Tells ARE | Target |
|--------|-------------------|--------|
| **MTTD** (Mean Time to Detect) | How fast do we spot issues? | < 5 min |
| **MTTC** (Mean Time to Contain) | How fast do we stop damage? | < 15 min |
| **MTTR** (Mean Time to Recover) | How fast do we restore service? | < 1 hour |
| **Incident Frequency** | How often do things break? | < 1 per agent per month |
| **Blast Radius** | How many tasks/workflows affected? | Decreasing trend |

---

## SLOs ARE Defines

ARE establishes Service Level Objectives for agents and the AOS. These are *commitments*, not aspirations.

---

### Agent-Level SLOs

| SLO | Target | Measurement Window |
|-----|--------|-------------------|
| **Availability** | ≥ 99.5% | Rolling 7 days |
| **Task Latency (p95)** | ≤ defined budget | Rolling 24 hours |
| **Error Rate** | ≤ 1% | Rolling 24 hours |
| **AHS** | ≥ 0.80 | Rolling 7 days |
| **CHR** | ≤ defined ceiling | Rolling 7 days |
| **Unbounded Execution Events** | Zero | Rolling 30 days |
| **Policy Violations** | Zero critical | Rolling 30 days |

---

### AOS-Level SLOs

| SLO | Target | Measurement Window |
|-----|--------|-------------------|
| **System Availability** | ≥ 99.9% | Rolling 30 days |
| **End-to-End Task Success** | ≥ 95% | Rolling 7 days |
| **System AHS** | ≥ 0.85 | Rolling 7 days |
| **System CHR** | ≤ defined ceiling | Rolling 7 days |
| **Cascading Failures** | Zero | Rolling 90 days |
| **Cost Overruns** | Zero | Rolling 30 days |
| **RTO (Recovery Time)** | ≤ 1 hour | Per incident |
| **RPO (Recovery Point)** | ≤ 15 min of work | Per incident |

---

### SLO Burn Rate Alerts

ARE uses burn rate to catch problems before SLOs are breached:

| Alert Level | Burn Rate | Meaning | Response |
|-------------|-----------|---------|----------|
| **Warning** | 2x | On pace to breach in 12 hours | Investigate |
| **Critical** | 5x | On pace to breach in 5 hours | Immediate action |
| **Emergency** | 10x | Breach imminent | Escalate + contain |

---

## What ARE Controls

### Agent-Level Levers

These must be adjustable at runtime without redeployment:

| Lever | Purpose |
|-------|---------|
| Execution enable/disable | Kill switch |
| Max reasoning steps | Bound cognitive loops |
| Max retries | Prevent retry storms |
| Tool enable/disable | Isolate capabilities |
| Confirmation thresholds | Force human approval |
| Token/tool cost ceilings | Halt on budget breach |
| Execution timeouts | Prevent runaway execution |

---

### System-Level Levers

| Lever | Purpose |
|-------|---------|
| System-wide kill switch | Emergency halt all agents |
| Per-agent isolation | Quarantine misbehaving agents |
| Blast-radius containment | Prevent cascade to other workflows |
| Dependency circuit breakers | Isolate failing tools/APIs |
| System cost ceiling | Hard stop on total spend |
| Autonomy degradation | Reduce autonomy across the board |

---

## How ARE Works With Others

| Role | ARE's Relationship |
|------|-------------------|
| **APO** (Agent Product Owner) | APO defines intent; ARE reports operational risk. ARE may request autonomy reduction. |
| **CSA** (Cognitive Systems Architect) | ARE reviews designs for operability. Flags unobservable or unbounded patterns. |
| **AE** (Agent Engineer) | AE delivers the controls ARE needs. ARE defines the contract; AE implements it. |
| **KMO** (Knowledge & Memory Owner) | ARE monitors memory growth; flags retention risks. |
| **COS** (Cognitive Operations Steward) | COS handles cognitive health (drift, confusion); ARE handles system health. They share data. |
| **ARAO** (AI Risk & Audit Owner) | ARE provides runtime evidence; ARAO defines policy. ARE enforces what ARAO approves. |

---

## What ARE Does NOT Do

- **Set autonomy policy** — That's APO + ARAO
- **Design agent cognition** — That's CSA
- **Build agents** — That's AE
- **Judge business outcomes** — That's APO
- **Audit for compliance** — That's ARAO
- **Monitor cognitive quality** — That's COS

ARE operates the engine. ARE does not choose the destination.

---

## Platform Coordination

The platform (Seer, Hub) is managed by the provider. ARE coordinates with the provider for:

| Area | ARE Responsibility |
|------|-------------------|
| Capacity planning | Request based on projected load |
| Capability gaps | Report missing features |
| Platform incidents | Escalate and coordinate response |
| Feature requests | Represent operational needs |

ARE does not own platform infrastructure. ARE owns the operational contract with the platform.

---

## The ARE Skill Profile

### Technical

- Distributed systems fundamentals
- Cloud infrastructure and networking
- Observability stacks (metrics, logs, traces)
- Security basics (isolation, access control)
- Working understanding of LLMs and agent frameworks

### Operational

- Failure-mode thinking: "What could go wrong?"
- Cost-risk tradeoff analysis
- Incident leadership under pressure
- Boundary enforcement: "This cannot ship as-is"

### Cultural

- Bias toward safety over speed
- Comfort saying no to stakeholders
- Systems thinking over feature thinking
- Preference for boring, predictable systems

---

## Anti-Patterns

| Pattern | Why It's Dangerous |
|---------|-------------------|
| "The model usually behaves" | Probability is not control |
| "We can add limits later" | Limits must be designed in |
| "That edge case won't happen" | Edge cases cause incidents |
| "LLMs are inherently unpredictable" | Execution bounds are deterministic |
| Treating ARE as DevOps | Agent failures are semantic, not just technical |
| Measuring only uptime | An agent can be "up" and causing damage |
| Shipping without kill switches | Non-negotiable |

---

## Success Criteria

ARE is successful when:

- Agent incidents are rare, contained, and explainable
- Cost overruns are prevented, not explained afterward
- Autonomy increases only after stability is proven
- Engineers trust the runtime environment
- Escalations happen before damage spreads

---

## Final Word

When the Agent Product Owner asks:

> "Can we let this agent act on its own?"

ARE's job is to answer:

> "Yes — and here's exactly how we stay in control."

If an agent cannot be stopped, observed, bounded, and recovered, it is not ready for production — regardless of how intelligent, accurate, or promising it appears.

**Reliability is not the absence of intelligence. It's the presence of control.**

---

*End of document*
