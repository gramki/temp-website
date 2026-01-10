# 5.2 The Immutability Principle

One of the most critical governance requirements for enterprise agents is the principle that **guardrails defined at training cannot be relaxed at employment**. This principle—the Immutability Principle—creates defensible behavioral boundaries that cannot be circumvented regardless of who is deploying the agent or in what context.

## The Problem: Runtime Authority Creep

Without the Immutability Principle, enterprises face a dangerous pattern: agents that were carefully trained with safety constraints can have those constraints loosened at deployment time. This creates:

- **Audit gaps:** Regulators cannot trust that an agent behaves according to its documented training if employment can override it.
- **Accountability confusion:** When an agent violates a constraint, it becomes unclear whether the issue was in training or employment.
- **Security vulnerabilities:** Malicious or negligent deployment can weaponize otherwise safe agents.
- **Compliance risk:** Regulatory requirements embedded in training can be bypassed by employment overrides.

## The Principle Stated

The Immutability Principle has two components:

### 1. Guardrails Cannot Be Relaxed

Any behavioral constraint, prohibition, or safety rule established during Training is **immutable at Employment**. Employment specifications can narrow what an agent does, but they can never expand beyond Training boundaries.

**Example:** If a Trained Agent has a guardrail prohibiting access to customer financial data, no Employment specification can grant that access. The agent simply cannot be employed with that capability.

### 2. Employment Can Only Specialize

Employment is strictly a **narrowing operation**. It selects a subset of trained capabilities, applies additional constraints, and binds the agent to a specific operational context.

| Training Says | Employment Can Say | Employment Cannot Say |
|---------------|--------------------|-----------------------|
| "May use tools A, B, C" | "Use only tool A" | "Also use tool D" |
| "No customer contact" | "No contact, plus no logging to external systems" | "Customer contact allowed for this project" |
| "Max $100 per decision" | "Max $50 per decision" | "Max $500 per decision" |
| "Escalate high-risk cases" | "Escalate high-risk and medium-risk cases" | "No escalation required" |

## Why Immutability Creates Defensibility

The Immutability Principle enables several critical enterprise capabilities:

### 1. Certifiable Training

Organizations can invest in rigorous training validation—testing, red-teaming, compliance review—with confidence that this investment is not nullified at deployment. A Trained Agent that has passed security certification retains that certification across all valid Employment configurations.

### 2. Clear Accountability

When an agent misbehaves, the investigation can clearly separate:
- **Training failure:** The agent was trained incorrectly (Domain Team accountable).
- **Employment misconfiguration:** The agent was deployed in an inappropriate context (Deployer accountable).
- **Runtime anomaly:** The agent encountered unexpected conditions (operational issue).

Without immutability, these categories blur.

### 3. Regulatory Defensibility

Regulators increasingly require organizations to demonstrate that AI systems operate within documented constraints. The Immutability Principle provides a formal guarantee: the constraints documented in the Training Specification are the constraints enforced at runtime.

### 4. Layered Governance

Different stakeholders govern different layers:
- **Security and Compliance** govern guardrails at Training.
- **Business Operations** govern deployment decisions at Employment.

Neither can override the other's jurisdiction.

## Implementation Considerations

Enforcing the Immutability Principle requires architectural support:

- **Schema enforcement:** Employment specifications must be validated against Training specifications at deployment time.
- **Runtime verification:** The agent runtime must enforce Training constraints regardless of Employment configuration.
- **Audit trail:** Any attempt to deploy with invalid specifications must be logged and rejected.
- **Cryptographic binding:** Advanced implementations may cryptographically sign Training specifications to prevent tampering.

## Common Objections and Responses

**"What if business needs change?"**

If business needs require capabilities beyond current Training, the correct path is to update the Training Specification through the appropriate governance process, then redeploy. This ensures the change is reviewed, validated, and documented.

**"This slows down deployment."**

This is intentional. The friction ensures that capability expansion goes through proper review. The alternative—easy overrides—creates unacceptable risk.

**"Our agents need flexibility."**

Flexibility within trained bounds is fully supported. Employment can configure preferences, select among trained tools, and adapt to context. What is prohibited is expansion beyond trained boundaries.

---

**References:**
*   `aosm-meta-model/raw-trained-employed-agents.md` — Section 3.3 on guardrail immutability
*   `olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md`
