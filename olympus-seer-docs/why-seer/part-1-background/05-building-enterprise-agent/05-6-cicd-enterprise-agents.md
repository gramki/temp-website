# 5.6 CI/CD for Enterprise Agents

Continuous integration and continuous deployment (CI/CD) practices transformed traditional software development by enabling rapid, reliable delivery of changes. Enterprise agents, however, present unique challenges that require CI/CD practices to be fundamentally rethought. The non-deterministic nature of AI systems, the multi-artifact composition of agents, and the high stakes of enterprise deployment combine to create requirements that traditional CI/CD pipelines cannot address.

## Why Agent CI/CD Is Different

| Traditional Software CI/CD | Enterprise Agent CI/CD |
|---------------------------|------------------------|
| Test inputs → deterministic outputs | Test behaviors across stochastic outputs |
| Version code | Version code + prompts + knowledge + guardrails |
| Deploy artifacts | Deploy with delegated authority and context |
| Rollback code | Rollback while preserving audit continuity |
| One approval gate | Multiple persona approval gates |

### The Non-Determinism Challenge

Traditional software produces deterministic outputs: given the same input, the same output is expected. AI agents are inherently non-deterministic—the same input may yield different (but potentially valid) outputs. This fundamentally changes what "testing" means.

**Behavioral testing** replaces output matching:
- Not "what" the agent said, but "how" it said it
- Tone, safety, compliance, and appropriateness
- Response within acceptable behavioral envelopes

### The Multi-Artifact Challenge

An enterprise agent is not a single deployable artifact. It comprises:
- **Raw Agent code:** The orchestration logic and runtime
- **Training Specification:** Prompts, knowledge bindings, guardrails
- **Employment Specification:** Delegation, scope, operational context
- **Knowledge versions:** The specific version of knowledge sources
- **Model versions:** The specific LLM versions used

All of these must be versioned, validated together, and tracked as a coherent configuration.

### The Regression Challenge

In traditional software, regression testing validates that new code does not break existing behavior. For agents, "regression" is more complex:
- Model provider updates can change behavior without any code changes
- Prompt refinements can have non-obvious downstream effects
- Knowledge updates can shift decision patterns
- The same test case may produce validly different outputs

## Unique CI Requirements

### Prompt Versioning

Prompts are as critical as code. Enterprise CI must:
- Track prompt evolution with semantic versioning
- Store prompts in version control (not embedded in code)
- Provide diff and review capabilities for prompt changes
- Link prompts to the agent versions that use them

### Knowledge Binding

An agent version must be tied to specific knowledge snapshots:
- Define which knowledge base versions the agent was trained with
- Ensure reproducibility by locking knowledge versions
- Validate compatibility when knowledge is updated
- Prevent "knowledge drift" where agents silently use newer content

### Guardrail Validation

Automated checks must verify:
- Required guardrails are present in the Training Specification
- Guardrails are effective (tested against adversarial inputs)
- No unintended loosening of constraints between versions
- Security boundaries are maintained

### Behavioral Baselines

Rather than exact output matching, CI should:
- Establish behavioral baselines from approved agent versions
- Compare new versions against baseline behavior patterns
- Flag deviations for human review
- Track behavioral metrics over time

### Security Scanning

Agent-specific security testing must include:
- Prompt injection detection
- Jailbreak resistance testing
- Data exfiltration prevention
- PII leakage detection

## Unique CD Requirements

### Multi-Stage Promotion

Enterprise agents require multiple deployment stages with distinct gates:

| Environment | Purpose | Constraints |
|-------------|---------|-------------|
| **Development** | Build and iterate | Synthetic data, no real authority |
| **Testing** | Validate behavior | Evaluation datasets, mocked integrations |
| **Staging** | Pre-production validation | Production-like, limited authority |
| **Production** | Live operations | Full authority, full audit |

### Autonomy Approval Gates

Before production deployment, specific persona approvals are required:
- **Agent Engineer (AE):** Technical validation and testing sign-off
- **Agent Reliability Engineer (ARE):** Production readiness certification
- **AI Risk & Audit Owner (ARAO):** Autonomy level approval

No agent should enter production without appropriate human accountability established.

### Production Readiness Gate

The ARE must certify:
- Observability: metrics, logs, and traces are configured
- Control: kill switches and override mechanisms are functional
- Alerting: anomaly detection is configured
- Runbooks: incident response procedures are documented

### Canary Deployments

Gradual rollout with behavioral monitoring:
- Deploy to a small percentage of traffic initially
- Monitor behavioral metrics, not just latency and error rates
- Compare canary behavior against stable baseline
- Automated rollback if deviation thresholds are exceeded

### Authority Binding

Deployment is not just about running code—it includes:
- Binding the agent to specific delegated authority
- Configuring the operational environment (credentials, endpoints)
- Establishing resource quotas and budgets
- Recording the delegation chain for audit

## The Rollback Problem

Traditional rollback reverts to a previous version. Agent rollback must consider:

### In-Flight Decisions

Rollback cannot un-make decisions. If the bad version made consequential decisions:
- Those decisions are already recorded in audit
- Customer communications may reference agent behavior
- Downstream systems may have acted on agent outputs

### Accumulated Memory

During the bad version's operation:
- What memory was written?
- Should that memory be invalidated?
- How do we prevent the new version from acting on bad memory?

### Authority Delegations

The bad version may have:
- Acquired new delegations
- Exercised authority in unexpected ways
- Established patterns that influenced other agents

### Audit Continuity

Rollback creates a new version, not a revert. The audit trail must:
- Maintain linkage between versions
- Explain why rollback occurred
- Preserve all records from the bad version (they cannot be deleted)

## Environment Considerations

Development, testing, and production environments require different configurations:

- **Authority isolation:** Development agents cannot have production authority
- **Data isolation:** Development uses synthetic data, not customer data
- **Integration isolation:** Development uses mocked external systems
- **Cost isolation:** Development budgets are separate from production

The same Training Specification should work across environments; Employment Specifications differ to provide appropriate bindings.

---

**References:**
*   `olympus-hub-docs/09-composite-systems-and-patterns/devops-workbench/README.md`
*   `aosm-meta-model/raw-trained-employed-agents.md`
