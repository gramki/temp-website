# 5. What CSP Offerings Cannot Address

---

This section identifies **structural gaps** in CSP agentic AI offerings—not missing features that will be added, but fundamental limitations inherent to the CSP business model and platform design. These gaps define where Zeta must invest.

---

## 5.1 Product-Grade Agent Lifecycle Management

### The Gap

CSP agent frameworks treat agents as **configurations**, not **products**. They provide:

- Agent definition APIs
- Deployment to managed runtimes
- Basic versioning (often implicit)

They do **not** provide:

| Lifecycle Concern | CSP Status | Impact |
|-------------------|------------|--------|
| **Semantic versioning** | Not supported | Cannot express breaking changes vs patches |
| **Promotion workflows** | Not built-in | No standard path from dev → staging → prod |
| **Rollback with state consistency** | Not supported | Memory and state may diverge from rolled-back logic |
| **Retirement and sunsetting** | Not supported | No graceful end-of-life for agent versions |
| **Cross-environment consistency** | Not enforced | Same agent may behave differently in test vs prod |
| **Backward compatibility testing** | Not supported | No framework for testing agent version upgrades |

### Why This Matters for Banking

Banks deploy software through **rigorous change management** processes:

1. **Change advisory boards** review changes before production
2. **Parallel run periods** validate new versions against existing behavior
3. **Audit trails** document who approved what, when
4. **Rollback plans** are mandatory for any production change

CSP agent frameworks do not support these workflows. Their design reflects general-purpose use cases, not the rigorous change management requirements of regulated industries.

### What Zeta Must Provide

- **Agent versioning** with semantic version semantics
- **Promotion workflows** with approval gates
- **Rollback capability** that maintains state consistency
- **Parallel run support** for version comparison
- **Retirement workflows** with deprecation warnings and migration paths

---

## 5.2 Bank-Grade Authority and Accountability Models

### The Gap

CSP agent frameworks have no concept of **delegated authority**. Their authorization model is built around:

- Agents inheriting the calling user's permissions
- Application-layer authorization (not agent-layer)
- No platform-level accountability tracking

They do **not** provide:

| Authority Concern | CSP Status | Impact |
|-------------------|------------|--------|
| **Agent identity** | No distinct agent identity | Cannot distinguish agent actions from human actions |
| **Delegation ceilings** | Not supported | No way to limit agent authority below user authority |
| **Dual control** | Not supported | No framework for multi-party approval |
| **Separation of duties** | Not supported | Same agent can propose and approve |
| **Kill switches** | Implicit (disable agent) | No instant, cross-instance revocation |
| **Authority audit trail** | Not provided | No record of who delegated what to which agent |

### Why This Matters for Banking

Banking regulations require:

1. **Clear accountability** — When an agent takes an action, who is responsible?
2. **Delegated authority documentation** — What is the agent authorized to do?
3. **Dual control for high-risk actions** — High-value transactions require multiple approvals
4. **Separation of duties** — The function that initiates a transaction should not be the function that approves it
5. **Instant revocation** — Compromised or malfunctioning agents must be stopped immediately

Without these capabilities, banks cannot deploy agents for any consequential decisions.

### Regulatory Precedent

The [OCC Bulletin 2023-37](https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-37.html) on third-party risk management emphasizes:

> "A bank should ensure that the third party... operates in a manner consistent with the bank's own policies, procedures, and risk appetite."

Agents are third parties in this framing. Banks must be able to demonstrate control.

### What Zeta Must Provide

- **Agent identity management** — Agents have distinct, verifiable identities
- **Authority framework** — Explicit delegation with ceilings and scope
- **Dual control workflows** — Multi-party approval for high-risk actions
- **Separation of duties enforcement** — Policy-based constraints on agent capabilities
- **Kill switch infrastructure** — Instant, global revocation
- **Authority audit trail** — Immutable record of delegation and revocation

---

## 5.3 Cross-Cloud and Customer-Cloud Portability

### The Gap

CSP agent frameworks are architected for:

- Agents running in CSP-managed environments
- State stored in CSP-managed services
- Orchestration via CSP control planes

They do **not** support:

| Portability Concern | CSP Status | Impact |
|---------------------|------------|--------|
| **Customer landing zone deployment** | Not designed for | Cannot deploy in bank's VPC with bank's controls |
| **Portable agent definitions** | CSP-specific | Cannot move agent from AWS to Azure |
| **Portable memory** | CSP-specific | Memory stores are not exportable to other CSPs |
| **Cross-CSP failover** | Not supported | No path to continue operations on different CSP |
| **Hybrid deployment** | Limited | Agents expect CSP services, not on-prem |

### Why This Matters for Banking

Banks have:

1. **Negotiated cloud agreements** — Major banks have enterprise contracts with specific CSPs
2. **Concentration risk policies** — Regulators expect banks not to depend entirely on one provider
3. **Data residency requirements** — Some data cannot leave certain jurisdictions
4. **Landing zone architectures** — Banks deploy vendor software in bank-controlled environments
5. **Multi-cloud strategies** — Many banks explicitly require multi-cloud capability

A platform that only runs on one CSP, in CSP-managed environments, cannot meet these requirements.

### The Landing Zone Reality

When banks say "deploy in our cloud," they mean:

| Expectation | Reality |
|-------------|---------|
| **Network** | Bank-controlled VPCs, firewalls, no public endpoints |
| **Identity** | Bank identity provider, not CSP IAM |
| **Logging** | Bank's SIEM, not just CSP logs |
| **Encryption** | Bank-managed keys, not CSP-managed |
| **Compliance** | Bank's compliance controls, not CSP defaults |

CSP agent frameworks are optimized for **CSP-managed, CSP-controlled** environments—the inverse of bank landing zone requirements.

### What Zeta Must Provide

- **Portable agent definition format** — Independent of CSP
- **Abstraction layer** — Swappable backends for storage, compute, models
- **Customer-cloud deployment model** — Runs in bank landing zones
- **Multi-cloud memory** — State that can replicate across CSPs
- **Cross-CSP failover** — Ability to shift operations between clouds

---

## 5.4 Durable Memory, Audit, and Evidence

### The Gap: CSP Memory ≠ Agent Memory

CSP "memory" is **session-scoped context**. It persists for the duration of a conversation, then disappears.

| What Banks Need | What CSPs Provide |
|-----------------|-------------------|
| **Episodic memory** — What happened with this customer? | Conversation history (session only) |
| **Semantic memory** — What does the agent know? | Knowledge bases (retrieval, not memory) |
| **Preference memory** — What does this customer prefer? | Not supported |
| **Procedural memory** — How did the agent learn to do this? | Not supported |
| **Cross-session continuity** — Remember context from last interaction | Not supported natively |

### The Gap: CSP Logs ≠ Audit Trails

CSP logs are **operational telemetry**. They are designed for debugging and monitoring, not regulatory evidence.

| What Banks Need | What CSPs Provide |
|-----------------|-------------------|
| **Decision record** — What was decided and why? | Model invocation logs (inputs/outputs only) |
| **Evidence chain** — Prove the decision was correct | Not structured for evidence |
| **Immutability** — Logs cannot be altered | Depends on configuration |
| **Long-term retention** — 7+ years | Configurable, but not default |
| **Self-describing format** — Interpretable without vendor tools | CSP-specific formats |

### Why This Matters for Banking

Regulators can ask:

> "Show me how your agent decided to decline this loan application."

The bank must produce:

1. **Context at decision time** — What information was available?
2. **Reasoning trace** — How did the agent process the information?
3. **Decision record** — What was the outcome and why?
4. **Authority chain** — Who authorized the agent to make this decision?
5. **Evidence of controls** — What guardrails were in place?

CSP logs cannot answer these questions. They show **what happened**, not **why it was correct**.

### What Zeta Must Provide

- **Persistent, portable memory** — Survives sessions and CSP changes
- **Memory types** — Episodic, semantic, preference, procedural
- **Audit-grade logging** — Decision records, not just telemetry
- **Evidence generation** — Structured records for regulatory response
- **Immutable storage** — Tamper-evident, long-term retention
- **Self-describing formats** — Interpretable without proprietary tools

---

## 5.5 Business Continuity Across Regions and CSPs

### The Gap

CSP platforms provide high availability **within their environment**. They do not provide:

| BC/DR Concern | CSP Status | Impact |
|---------------|------------|--------|
| **Multi-region agent orchestration** | Not provided | Customer must build |
| **State replication across regions** | Limited (storage only) | Agent state is not replicated |
| **Cross-CSP failover** | Not supported | If CSP is down, agents are down |
| **Model failover** | Not supported | If model is unavailable in region, no automatic failover |
| **Graceful degradation** | Not built-in | Agents fail hard, not soft |

### Failure Scenarios CSPs Do Not Cover

| Scenario | CSP Response | Bank Expectation |
|----------|--------------|------------------|
| **Single region outage** | "Use multi-region" | Automatic failover with minimal data loss |
| **Model unavailable** | Error | Fallback to alternative model or rules |
| **CSP-wide outage** | "Wait" | Continue operations on alternative CSP |
| **Agent runtime failure** | Restart | Stateful recovery without losing context |
| **Memory corruption** | Customer problem | Rollback to known-good state |

### Why This Matters for Banking

Banks have:

1. **RTO/RPO requirements** — Defined recovery time and data loss tolerances
2. **Concentration risk policies** — Cannot depend entirely on single provider
3. **Business continuity plans** — Must document how they survive provider failures
4. **Regulatory expectations** — [DORA (EU)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) explicitly requires ICT third-party risk management

A platform that cannot survive CSP failures is not acceptable for critical banking operations.

### What Zeta Must Provide

- **Active-active multi-region** — Agents run in multiple regions simultaneously
- **State synchronization** — Memory and configuration replicate across regions
- **Multi-cloud capability** — Ability to run on alternative CSP if primary fails
- **Model failover** — Automatic switch to alternative models
- **Graceful degradation** — Fall back to rules or human when AI unavailable
- **Defined RTO/RPO** — Clear, documented recovery objectives

---

## 5.6 Product Distribution and Market Access

### The Gap

CSP agent frameworks are designed for **customers building their own agents**. Zeta's model is different: **Zeta builds agent products and distributes them to multiple banks**.

This creates a structural gap that CSPs cannot address:

| CSP Assumption | Zeta Reality |
|----------------|--------------|
| Customer builds agents on CSP | Zeta builds agents and deploys to customer |
| One agent, one CSP | Same agent, many CSPs (based on customer) |
| Agent tied to CSP account | Agent tied to Zeta product catalog |
| No cross-CSP consistency | Same version = same behavior everywhere |

### Why This Matters for Zeta's Business

| Business Dimension | Impact |
|--------------------|--------|
| **Market access** | If agents only run on AWS, Zeta cannot sell to Azure-first banks |
| **Product economics** | One codebase serves all customers; CSP-specific agents multiply costs |
| **Update management** | Zeta pushes patches to all deployments; CSP-specific requires N×effort |
| **Quality assurance** | One test suite validates all; CSP-specific requires N×testing |
| **Support** | One runbook for all; CSP-specific requires N×expertise |

### What CSPs Cannot Provide

| Requirement | CSP Status |
|-------------|------------|
| **Cross-CSP agent packaging** | Not supported—agents are CSP-specific |
| **Unified deployment pipeline** | Not supported—each CSP has own tooling |
| **Cross-CSP version consistency** | Not supported—no shared registry |
| **Multi-CSP update orchestration** | Not supported—no cross-CSP control plane |

### What Zeta Must Provide

- **CSP-agnostic agent artifacts** — Same package deploys to any CSP
- **Unified product catalog** — Single registry of agent versions
- **Cross-CSP deployment pipeline** — One process, multiple targets
- **Consistent behavior guarantee** — Version X behaves identically everywhere
- **Zeta-managed updates** — Zeta controls patch and upgrade cycle
- **Bank-owned data** — Customer data stays in bank environment regardless of CSP

---

## 5.7 Summary: Structural Gaps

| Gap | Nature | Zeta Responsibility |
|-----|--------|---------------------|
| **Product lifecycle** | CSPs treat agents as configs, not products | Version, promote, retire agents as products |
| **Authority model** | CSPs have no delegation concept | Identity, authority, kill switches, dual control |
| **Portability** | CSPs assume their environment | Portable definitions, multi-cloud, landing zones |
| **Memory** | CSPs provide session context, not memory | Persistent, typed, portable memory |
| **Audit/Evidence** | CSPs provide logs, not evidence | Decision records, evidence generation |
| **Business continuity** | CSPs provide availability, not survivability | Multi-region, multi-cloud, graceful degradation |
| **Product distribution** | CSPs assume customer builds agents | Zeta deploys same agent to banks on any CSP |

---

## The Strategic Implication

These are not gaps that CSPs will fill. They are **structural** to the CSP business model:

1. **CSPs want lock-in.** Portability is against their interest.
2. **CSPs are horizontal.** They serve all industries; banking-specific requirements are not prioritized.
3. **CSPs optimize for scale.** They build for the common case, not regulated edge cases.
4. **CSPs are infrastructure providers.** They do not build product semantics.

**Zeta's opportunity is to build the product layer that sits above CSP infrastructure.**

This is not competing with CSPs. It is building capabilities that lie outside their platform scope and business model.

---

*Previous: [Section 4: State of the World: CSP Offerings](./04-csp-offerings.md)*

*Next: [Section 6: Zeta's Solution Principles →](./06-solution-principles.md)*

