# Agent Engineer (AE)

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [Role Definitions](./roles.md) | [AE Deliverables to ARE](./needs/ae-deliverables-to-are.md)  
> **Detailed Needs:** [Full Development Lifecycle Coverage](./needs/ae-lifecycle-coverage.md)

---

## The Problem AE Solves

Designs don't run in production. Code does.

The gap between "a well-designed agent" and "an agent that actually works" is filled by engineering. But agent engineering is different from traditional software engineering:

- Prompts are code, but they're probabilistic
- Reasoning is logic, but it's emergent
- Tools are APIs, but they're invoked by judgment
- Errors are failures, but they might look like success
- Tests pass, but behavior might still be wrong

**AE exists because agents need to be built, not just designed.**

---

## The AE Mandate

> **AE owns agent implementation — correctness, completeness, and operability.**

This means:

| AE Owns | AE Does NOT Own |
|---------|------------------|
| Agent code, prompts, and workflows | Why the agent exists (APO) |
| Tool integrations and bindings | How cognition is designed (CSA) |
| Safety hooks and telemetry | Runtime safety enforcement (ARE) |
| Execution bounds and limits | Autonomy approval (ARAO) |
| Testing and validation | Business outcome measurement (APO) |

**The distinction matters.** AE implements what CSA designs to achieve what APO intends. AE doesn't define intent or architecture — AE makes them real.

---

## Why This Role Is Different

### It's Not Traditional Software Engineering

Software engineers write deterministic code. AE writes code that orchestrates probabilistic reasoning.

| Software Engineer | Agent Engineer |
|-------------------|----------------|
| Writes functions that compute | Writes prompts that reason |
| Debugs with stack traces | Debugs with reasoning traces |
| Tests with assertions | Tests with behavioral validation |
| Handles errors with exceptions | Handles errors with escalation |
| Deploys with CI/CD | Deploys with production readiness gates |

### It's Not Prompt Engineering

Prompt engineers optimize prompts. AE builds complete agent systems — prompts are just one component.

### It's Not ML Engineering

ML engineers train and deploy models. AE uses models as reasoning engines inside larger systems.

---

## What AE Cares About

### 1. Does the Implementation Match the Design?

CSA provides the blueprint. AE must:
- Implement reasoning patterns as designed
- Respect cognitive boundaries
- Honor decision points
- Preserve traceability

**If the implementation drifts from the design, behavior becomes unpredictable.**

---

### 2. Are the Prompts Correct?

Prompts are the agent's instructions. AE must:
- Write clear, unambiguous prompts
- Version and track prompt changes
- Test prompts against expected behaviors
- Handle prompt failures gracefully

**If prompts are vague, the model will surprise you.**

---

### 3. Are Tool Integrations Safe?

Agents use tools to act in the world. AE must:
- Implement tool bindings correctly
- Validate inputs before invocation
- Handle tool failures gracefully
- Respect tool access permissions

**If tools are poorly integrated, agents can cause real damage.**

---

### 4. Are Execution Bounds Enforced?

Agents can loop, retry, and consume resources indefinitely. AE must implement:
- Maximum reasoning steps
- Retry limits with backoff
- Execution timeouts
- Token and cost ceilings

**If bounds aren't in the code, ARE can't enforce them.**

---

### 5. Is the Agent Observable?

ARE needs to see what the agent is doing. AE must emit:
- Task lifecycle events
- Action execution traces
- Tool invocation logs
- Decision points with context
- Failure events with classification

**If telemetry isn't implemented, the agent is a black box.**

---

### 6. Is the Agent Testable?

Before production, agents need validation:
- Unit tests for individual components
- Integration tests for tool bindings
- Behavioral tests for reasoning patterns
- Regression tests for prompt changes
- Stress tests for resource bounds

**If testing is an afterthought, bugs are discovered by users.**

---

## What AE Owns

### Implementation Artifacts

| Artifact | Description |
|----------|-------------|
| Agent code | Core logic, workflows, orchestration |
| Prompts | System prompts, task prompts, tool prompts |
| Tool bindings | Integrations with external systems |
| Configuration | Runtime parameters, feature flags |
| Tests | All test suites for the agent |

---

### Operability Contracts

AE delivers these to ARE (see [AE Deliverables to ARE](./ae-deliverables-to-are.md)):

| Contract | Purpose |
|----------|---------|
| Agent contract | Machine-readable operational interface |
| Safety controls | Kill switch, bounds, limits |
| Telemetry | Structured events and traces |
| Cost attribution | Token and tool cost tracking |
| Version manifest | Artifact versions for rollback |

---

### Testing Strategy

| Test Type | Purpose | When |
|-----------|---------|------|
| Unit tests | Component correctness | Every change |
| Integration tests | Tool and API behavior | Every change |
| Behavioral tests | Reasoning correctness | Every change |
| Regression tests | Prompt stability | Every prompt change |
| Stress tests | Bound enforcement | Before release |
| Production readiness | Full validation | Before production |

---

## How AE Works With Others

| Role | AE's Relationship |
|------|-------------------|
| **APO** | APO defines success criteria; AE implements to meet them. |
| **CSA** | CSA provides designs; AE implements them. AE validates feasibility. |
| **ARE** | AE delivers operability contracts; ARE uses them to operate safely. |
| **KMO** | AE integrates knowledge access; KMO ensures knowledge is available. |
| **COS** | COS reports behavior issues; AE investigates implementation bugs. |
| **ARAO** | AE implements controls; ARAO validates they meet requirements. |

---

## The Build-Operate Contract

AE and ARE have a critical handoff. AE must deliver:

| Requirement | AE Responsibility |
|-------------|-------------------|
| Kill switch | Implement and expose |
| Execution bounds | Implement and make configurable |
| Telemetry | Emit all required events |
| Cost tracking | Attribute costs to tasks |
| Failure classification | Emit structured errors |
| Rollback readiness | Maintain version lineage |

ARE cannot operate what AE doesn't provide.

---

## What AE Does NOT Do

| Responsibility | Who Owns It |
|----------------|-------------|
| Define agent purpose | APO |
| Design reasoning patterns | CSA |
| Operate agents in production | ARE |
| Approve autonomy | ARAO |
| Monitor cognitive health | COS |
| Govern knowledge | KMO |

AE builds. Others decide what to build, how to design it, and how to run it.

---

## The AE Skill Profile

### Technical Depth

- Proficiency in agent frameworks (Strands, LangChain, etc.)
- LLM API usage and optimization
- Prompt engineering fundamentals
- Tool integration patterns
- Observability instrumentation

### Engineering Discipline

- Version control and CI/CD
- Testing strategies for non-deterministic systems
- Code review and quality practices
- Documentation as a first-class artifact
- Debugging reasoning traces

### Collaboration

- Translating designs into implementation plans
- Communicating feasibility and trade-offs
- Partnering with ARE on operability
- Supporting incident investigation

### Operational Awareness

- Understanding of production readiness requirements
- Appreciation for why safety controls matter
- Cost consciousness in implementation choices
- Designing for observability, not adding it later

---

## Anti-Patterns

| Pattern | Why It's Dangerous |
|---------|-------------------|
| "The prompt works, ship it" | Working ≠ ready for production |
| "We'll add logging later" | Observability must be built in |
| "The model handles edge cases" | Models need explicit handling |
| "Retry until it works" | Unbounded retries cause incidents |
| "Testing agents is too hard" | Untested agents are time bombs |
| "ARE can figure out the limits" | AE implements limits; ARE enforces them |
| "This is just a prototype" | Prototypes become production systems |

---

## Success Criteria

AE is successful when:

- Implementations match CSA designs
- ARE can operate agents with provided controls
- Tests catch issues before production
- Telemetry enables debugging and monitoring
- Prompts are versioned and traceable
- Tool integrations are safe and resilient
- Production readiness reviews pass on first attempt

---

## Final Word

When someone asks:

> "Does this agent actually work?"

AE's job is to answer:

> "Yes — it implements the design correctly, handles failures gracefully, emits proper telemetry, and can be controlled at runtime."

If an agent is impressive in demos but fails in production, the engineering wasn't complete.

**Designs without implementation are dreams. AE makes agents real.**

---

*End of document*

