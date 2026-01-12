Ref: .cursor/plans/trained_agent_&_test_runner_design_7b63ef40.plan.md

Thank you for pointing to the in-progress plan. I see the Raw Agent Lifecycle Manager design pattern establishes:

1. **Spec Manager** → **Directory** → **Operators** → **Levers** structure
2. Clear separation: Raw Agents are NOT deployable - only Employed Agents are deployable
3. Raw Agents are containers referenced through Training Spec

This helps clarify my questions. Let me refine them:

---

## Updated Clarifying Questions

### 1. Trained Agent Lifecycle Manager

**Pattern Consistency:**
- Should Trained Agent Lifecycle Manager follow the **same sub-component pattern** as Raw Agent Lifecycle Manager?
  - **Training Spec Manager** (spec structure, validation)
  - **Trained Agent Directory** (registry, search by capabilities)
  - **Trained Agent Operators** (lifecycle management - registration, validation, versioning)
  - **Trained Agent Levers** (publication controls, version deprecation, affects all derived Employed Agents)

> Yes

**"Employed Agents Discovery":**
- Is this about finding **which Employed Agents use a specific Trained Agent**? (e.g., "show me all deployments using fraud-analyst-v2")
> Yes

- If so, this seems like a query capability on the Trained Agent Directory, not a separate service.
> Yes

**"Feedback Services":**
- What feedback loop is this capturing?
  - Feedback from Employed Agent production outcomes → Training Spec improvements?
  - Developer feedback during sandbox testing?
  - APO/PA feedback on agent behavior?

> Training Spec improvements (from Cognitive Operations Steward, Developer)
> APO/PA feedback on agent behavior
> Feedback from any team members (other human/ai agents) on required improvements

**Seer Operator Boundary:**
- Is Trained Agent Lifecycle Manager the "business logic layer" that manages Training Specs, while Seer Operator is the "controller layer" that reconciles CRDs to Kubernetes state?

> Yes

### 2. Agent Test Runner

**Three-Layer Model Testing:**
- Since Raw/Trained Agents are NOT deployable (only Employed Agents are), does Agent Test Runner:
  - Deploy **temporary Employed Agents** (from a Training Spec + temporary Employment Spec) for testing?
  - Test in **sandbox workbench instances** specifically?
> Yes

**MVP Scope:**
- What's the boundary between MVP "Validations" and parked "Evaluations"?
  - **Validations** = go/no-go checks (health, safety guardrail enforcement, basic behavior)
  - **Evaluations** = quality scoring, regression testing, benchmarks (parked)?

> Yes

**Hub Test Runner Relationship:**
- Does Agent Test Runner **extend** Hub Test Runner (adds agent-specific test types, assertions) or is it **separate** (uses Hub Test Runner patterns but is independent)?

> Extends

### 3. Dependency Clarification

**Raw Agent Lifecycle Manager (from in-progress plan) → Trained Agent Lifecycle Manager:**
- The Raw Agent plan shows: "Trained Agent Lifecycle Manager (Training Specs reference Raw Agents; Raw Agent capabilities influence Training Spec creation)"
- Should the Trained Agent Lifecycle Manager design explicitly show this integration?

> Yes
---

Once you answer these, I'll create a plan that's consistent with both the completed Seer Sidecar design and the in-progress Raw Agent Subsystems design.