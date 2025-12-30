
# Agent Roles in the Agentic Ops Fabric  
### **Design Standard for Analysts & Developers**

---

# 1. Overview

This document defines the formal design standards for four categories of agents in the **Agentic Operations Fabric**:

1. **Do Agents** – transactional executors  
2. **Think Agents** – reasoning and analytical processors  
3. **Orchestrator Agents** – process controllers  
4. **Governance (Guardrail) Agents** – policy and risk enforcers  

This standard prescribes **what each agent must do**, **must not do**, and highlights **common modelling pitfalls**.

---

# 2. Do Agents

## 2.1 Purpose  
Do Agents perform **atomic, deterministic, rule-driven tasks** in systems.  
They are the “hands” of the system.

### Responsibilities  
- Execute CRUD operations in core systems  
- Post transactions and adjustments  
- Validate data using deterministic rules  
- Interact with APIs and services  
- Maintain audit trails for every action  

## 2.2 Prohibitions  
Do Agents must **not**:  
- Make policy decisions  
- Perform multi-step workflows  
- Interpret ambiguous rules  
- Override compliance constraints  
- Handle human-facing communication flows  

## 2.3 Common Pitfalls  
- **Overloaded Do Agent**: too many responsibilities  
- **Hidden policy logic** inside Do Agent code  
- **Unlimited retries** causing cascading failures  
- **Silent failures** without escalation  

---

# 3. Think Agents

## 3.1 Purpose  
Think Agents perform **reasoning, interpretation, classification, analysis, and summarisation**.  
They are the “analysts” of the system.

### Responsibilities  
- Interpret documents and unstructured data  
- Classify alerts, cases, exceptions  
- Summarise multi-source evidence  
- Produce recommended actions with explanations  
- Translate policy into contextual understanding  

## 3.2 Prohibitions  
Think Agents must **not**:  
- Execute irreversible system actions  
- Close, modify, or create system-of-record entries  
- Skip or reduce control steps  
- Replace required human approvals  

## 3.3 Common Pitfalls  
- **Judge + executor anti-pattern**  
- **Opaque reasoning** without structured summaries  
- **Hardcoded policies** inside prompts  
- **Acting autonomously** instead of recommending  

---

# 4. Orchestrator Agents

## 4.1 Purpose  
Orchestrator Agents manage **multi-step workflows**, sequencing Do and Think Agents.  
They are the “conductors” of the system.

### Responsibilities  
- Control workflow sequence  
- Handle branching logic and retries  
- Manage SLAs and process timers  
- Trigger human-in-loop steps  
- Delegate tasks to Do and Think Agents  

## 4.2 Prohibitions  
Orchestrator Agents must **not**:  
- Make compliance decisions  
- Execute transactional operations directly  
- Perform analytical reasoning  
- Override Governance Agents  

## 4.3 Common Pitfalls  
- **Merged Orchestrator & Governance**  
- **Direct core system access**  
- **Excessively large workflows** ("God Orchestrator")  
- **Buried workflow logic in Do/Think Agents**  

---

# 5. Governance (Guardrail) Agents

## 5.1 Purpose  
Governance Agents enforce **policies, risk controls, segregation of duties, and regulatory requirements**.  
They are the “control layer” of the system.

### Responsibilities  
- Validate policy compliance  
- Enforce SoD and approval hierarchies  
- Ensure data privacy and access rules  
- Gate risky or irreversible actions  
- Provide audit-grade explanations  
- Approve or escalate exceptions  

## 5.2 Prohibitions  
Governance Agents must **not**:  
- Execute business operations  
- Perform multi-step workflows  
- Be optional or bypassable  
- Optimise processes by relaxing controls  

## 5.3 Common Pitfalls  
- **Self-governing workflows** (agent checks itself)  
- **Control at the end instead of pre-action**  
- **Governance as advisory instead of mandatory**  
- **Missing decision logs**  

---

# 6. Reference Interaction Pattern

A compliant interaction pattern for sensitive operations (e.g., account closure):

1. **Think Agent** — analyses context and recommends action  
2. **Governance Agent** — validates compliance and returns decision  
3. **Orchestrator Agent** — sequences workflow based on decision  
4. **Do Agents** — execute the approved actions  

This structure preserves:  
- Separation of duties  
- Auditability  
- Clarity of responsibility  
- Modularity  
- Regulatory alignment  

---

# 7. Role Comparison Matrix

| Agent Type | Executes Actions | Makes Decisions | Interprets Data | Controls Workflow | Enforces Policy |
|------------|------------------|-----------------|------------------|------------------|------------------|
| **Do Agent** | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No |
| **Think Agent** | ❌ No | ⚠ Recommends | ✅ Yes | ❌ No | ❌ No |
| **Orchestrator** | ❌ No | ❌ No | ❌ No | ✅ Yes | ❌ No |
| **Governance Agent** | ❌ No | ✅ Yes | ⚠ Validates | ❌ No | ✅ Yes |

---

# 8. Summary

Agents must follow **clear, strict separation of concerns**:  
- **Do Agents** → execution  
- **Think Agents** → reasoning  
- **Orchestrators** → sequencing  
- **Governance Agents** → control  

Violating these boundaries introduces **risk, audit issues, system fragility, and uncontrolled behavior**.

This design standard must be followed by all analysts and developers modelling agentic workflows and systems.



# Addendum: Why Do Agents Are Not Tools?

This addendum provides a formal explanation to accompany the **Agent Roles in the Agentic Ops Fabric – Design Standard**.  
It clarifies why **Do Agents**, despite appearing similar to “tools,” must remain modeled as **agents** in a compliant, auditable, agentic operations environment.

---

## 1. Do Agents vs Tools — Core Distinction

Although Do Agents perform atomic, deterministic tasks similar to tools, they differ in four critical dimensions:

### 1.1 Autonomy vs Passivity  
**Tools are passive.** They only act when invoked.  
**Do Agents are autonomous executors** capable of:  
- Validating inputs  
- Retrieving supplemental data  
- Handling retries and backoff  
- Producing structured diagnostics  
- Triggering compensating actions  
- Maintaining execution semantics  

Thus, a Do Agent is not “called” — it *acts* with responsibility.

---

## 2. Governance, Compliance, and Observability

Tools do not carry responsibilities for:  
- Logging every action  
- Being governed under agent SLAs  
- Providing auditable traces  
- Respecting access control policies  
- Participating in agent governance loops  

Do Agents are required to:  
- Log semantic actions (“Posted GL entry X”, “Updated KYC attribute Y”)  
- Expose health, availability, throughput metrics  
- Implement rate limits and operational boundaries  

These are **agent behaviours**, not tool behaviours.

---

## 3. Safety Through Separation of Concerns

If Do Agents become “tools,” developers may incorrectly:  
- Embed execution inside Think Agents  
- Allow Orchestrators to mutate system-of-records directly  
- Bypass Governance Agents  
- Break mandatory segregation of duties  

Using Do Agents as **first-class agents** ensures:  
- Execution is always delegated  
- Analytical reasoning is separated from transactional mutation  
- Governance performs checks before execution  
- Orchestration remains focused on workflow, not execution logic  

Separating roles **is a safety requirement**, not a stylistic choice.

---

## 4. Systems Complexity and Abstraction

A Do Agent abstracts:  
- Multiple backend integration patterns  
- API quirks and idempotency protections  
- Rate limiting & retries  
- Distributed failure semantics  
- Transactional safety boundaries  

A tool is simply:  
- A function or API call  

A Do Agent is a **capability with operational responsibility**.

---

## 5. Agent-to-Agent Contract Semantics

Do Agents can publish:  
- **Capabilities** (e.g., “I can post card settlements”)  
- **Preconditions** (e.g., “Requires valid account state”)  
- **Postconditions**  
- **Error modes**  
- **SLAs & behavioral guarantees**  

Tools do not have:  
- Identity  
- Accountability  
- Capabilities  
- Contracts  

Agents must.

---

## 6. Policy-Aware Execution

Tools cannot:  
- Ask Governance for approval  
- Check compliance boundaries  
- Validate SoD rules  
- Trigger human approvals when needed  

Do Agents always execute **within governance boundaries**.  
Tools cannot enforce, understand, or respect policy.

---

## 7. Clear System Design Mental Model

Using agents gives system designers the following clarity:

- **Think Agents → analyse**  
- **Governance Agents → approve**  
- **Orchestrators → sequence**  
- **Do Agents → execute**  

Tools obscure this architecture, causing role confusion and unsafe design.

---

## 8. Summary Table

| Property | Tools | Do Agents |
|---------|--------|------------|
| Execute tasks | ✔ | ✔ |
| Autonomous | ✘ | ✔ |
| Policy-aware | ✘ | ✔ |
| Auditable | ✘ | ✔ |
| SLA-bound | ✘ | ✔ |
| Has identity | ✘ | ✔ |
| Runs inside agent fabric | ✘ | ✔ |

---

## 9. Conclusion

Do Agents may *sound* like tools because they perform atomic, targeted tasks —  
but they behave like **autonomous, governed, auditable entities** with responsibilities that tools cannot fulfil.

Treating Do Agents as tools would:  
- Break safety  
- Break auditability  
- Break segregation of duties  
- Encourage fragile system design  

This is why Do Agents must remain **agents**, not downgraded utilities.

---


