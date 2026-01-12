# Knowledge & Memory Owner (KMO)

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [Role Definitions](./roles.md) | [CSA Reference](./csa.md)  
> **Detailed Needs:** [Enterprise Learning and Memory Promotion](./needs/kmo-enterprise-learning.md)

---

## The Problem KMO Solves

Agents don't operate in a vacuum. They need knowledge to reason and memory to learn. Without governance:

- Agents use outdated or incorrect information
- Knowledge conflicts create inconsistent behavior
- Memory grows unbounded and becomes toxic
- Sensitive data leaks into agent context
- No one knows what "truth" the agent believes
- Tool access becomes a free-for-all

Traditional knowledge management focuses on human access. Agent knowledge management must focus on *what machines are allowed to believe and remember*.

**KMO exists because agents need curated truth, not a data dump.**

---

## The KMO Mandate

> **KMO owns what agents know and remember.**

This means:

| KMO Owns | KMO Does NOT Own |
|----------|------------------|
| Domain semantics and ontologies | Agent behavior (CSA, AE) |
| Knowledge sources and grounding | Runtime operations (ARE) |
| Enterprise Memory governance | Agent intent (APO) |
| Tool and Machine Registry curation | Compliance judgments (ARAO) |
| Knowledge quality and freshness | Agent Memory (session state) |

**The distinction matters.** KMO curates the "world model" agents use. KMO doesn't control how agents reason — only what raw material they reason with.

---

## Why This Role Is Different

### It's Not Traditional Knowledge Management

Traditional KM focuses on documents and search. KMO focuses on *machine-consumable truth* that agents can reason with.

| Traditional KM | KMO |
|----------------|-----|
| Organize documents for humans | Curate knowledge for machines |
| Search relevance | Grounding accuracy |
| User experience | Agent correctness |
| Content management | Truth management |

### It's Not Data Engineering

Data engineers build pipelines. KMO ensures the *meaning* and *reliability* of what flows through them.

### It's Not the Agent Engineer

AE implements knowledge access. KMO ensures what's accessed is correct and appropriate.

---

## What KMO Cares About

### 1. Is the Knowledge Correct?

Agents that reason with wrong information produce wrong conclusions. KMO must ensure:

- Sources are validated and authoritative
- Updates propagate correctly
- Conflicts are detected and resolved
- Staleness is monitored and addressed

**If knowledge is wrong, the agent is wrong — confidently.**

---

### 2. Is the Knowledge Grounded?

"Grounding" means the knowledge is connected to reality:

| Ungrounded | Grounded |
|------------|----------|
| "Our return policy is flexible" | "Returns accepted within 30 days with receipt" |
| "We generally offer discounts" | "10% discount for orders over $500" |
| "Contact support for help" | "Support available at support@example.com, 9am-5pm EST" |

KMO ensures agents have grounded facts, not vague statements.

**If knowledge is vague, agent responses are vague — or hallucinated.**

---

### 3. Is the Knowledge Appropriate?

Not all knowledge should be available to all agents:

| Consideration | Example |
|---------------|---------|
| Relevance | Customer service agent doesn't need R&D roadmap |
| Sensitivity | PII requires special handling |
| Scope | Agent for Product A shouldn't see Product B data |
| Freshness | Archived data might mislead |

KMO defines access boundaries.

**If access is unbounded, agents see too much — or the wrong things.**

---

### 4. Is Memory Governed?

Enterprise Memory (via CAF) accumulates over time. KMO governs:

| Memory Concern | Governance Response |
|----------------|---------------------|
| Unbounded growth | Retention policies |
| Stale memories | Decay rules |
| Toxic memories | Override mechanisms |
| Sensitive content | PII policies |
| Conflicting memories | Resolution procedures |

**If memory is ungoverned, agents remember things they shouldn't — forever.**

---

### 5. Are Tools Curated?

Agents use tools to act. KMO curates:

| Tool Concern | Curation Response |
|--------------|-------------------|
| Availability | Which tools exist and are maintained |
| Appropriateness | Which agents can use which tools |
| Documentation | How tools should be used |
| Versioning | Which versions are approved |

**If tools are a free-for-all, agents misuse them.**

---

## What KMO Owns

### Knowledge Sources

| Source Type | KMO Responsibility |
|-------------|-------------------|
| SOPs and policies | Curate, version, validate |
| Product information | Ensure accuracy and freshness |
| Domain ontologies | Define and maintain |
| External data | Validate and integrate |
| Grounding corpora | Prepare for retrieval |

---

### Enterprise Memory Governance (via CAF)

| Memory Type | KMO Role |
|-------------|----------|
| Decision Records | Retention policy, not content |
| Evidence Bundles | Retention policy, not content |
| Outcome Records | Retention policy, not content |
| Override Records | Retention policy, not content |
| Semantic Memory | Curation and quality |

KMO sets *policies*. The system enforces them.

---

### Tool and Machine Registry

| Registry Concern | KMO Responsibility |
|------------------|-------------------|
| Tool catalog | Maintain authoritative list |
| Tool documentation | Ensure accuracy |
| Tool access policies | Define who can use what |
| Tool versioning | Track and communicate changes |

---

### Knowledge Quality Metrics

| Metric | What It Measures |
|--------|------------------|
| Freshness | How recently knowledge was validated |
| Accuracy | Error rate in knowledge-based decisions |
| Coverage | Gaps in domain coverage |
| Consistency | Conflicts between sources |
| Usage | Which knowledge is actually used |

---

## Memory Type Clarification

| Memory Type | Owner | KMO Role |
|-------------|-------|----------|
| **Knowledge** (SOPs, policies, grounding data) | KMO | Full ownership |
| **Enterprise Memory** (episodic via CAF) | CAF | Governance policies |
| **Agent Memory** (session state, context) | AE/ARE | Not owned |

KMO does not manage ephemeral session state. That's AE's responsibility, operated by ARE.

---

## Enterprise Learning: Memory Promotion

Enterprise Learning is the process of promoting learnings from individual agent interactions to higher levels of memory and knowledge. KMO owns this workflow.

### Memory Promotion Levels

```
Agent Observation
      ↓ (automatic, policy-based)
Episodic Memory (CAF)
      ↓ (COS detects patterns → KMO validates)
Semantic Memory
      ↓ (KMO proposes → KMO + ARAO approves)
Enterprise Knowledge
      ↓ (KMO proposes → APO + ARAO approves)
Published SOPs / Policies
```

---

### Promotion Workflow

| Stage | Owner | Activity |
|-------|-------|----------|
| **Detection** | COS | Spots patterns across agents worth promoting |
| **Validation** | KMO | Confirms the learning is correct and useful |
| **Risk Assessment** | KMO + ARAO | Evaluates compliance and business impact |
| **Approval** | Varies | See approval matrix below |
| **Execution** | Platform (CAF) | Automated per KMO-defined policies |
| **Verification** | COS | Confirms promotion had intended effect |

---

### Approval Matrix

| Promotion Type | Approver | Rationale |
|----------------|----------|-----------|
| Observation → Episodic | Automatic (policy) | High volume, low risk |
| Episodic → Semantic | KMO | Curated sharing across agents |
| Semantic → Knowledge | KMO + ARAO | Becomes authoritative truth |
| Knowledge → Published SOP | APO + ARAO | Changes business behavior |

---

### Promotion Criteria

KMO defines policies for when promotion should occur:

| Criterion | Question |
|-----------|----------|
| **Frequency** | Is this pattern recurring? |
| **Consistency** | Is the learning stable across contexts? |
| **Correctness** | Has the learning been validated? |
| **Value** | Does promotion benefit other agents? |
| **Risk** | Does promotion create compliance or security risk? |
| **Scope** | Who should have access to this knowledge? |

---

### Demotion and Correction

Learnings can be wrong. KMO also owns:

| Action | Trigger | Process |
|--------|---------|---------|
| **Correction** | Learning found to be incorrect | KMO updates, COS verifies |
| **Demotion** | Learning no longer valid | KMO demotes, documents reason |
| **Quarantine** | Harmful pattern detected | KMO isolates, ARAO reviews |
| **Expiration** | Time-based decay | Automatic per retention policy |

---

### Enterprise Learning Signals

| Signal | Source | KMO Response |
|--------|--------|--------------|
| Pattern emergence | COS detection | Evaluate for promotion |
| Knowledge gap | Agent failures | Identify missing knowledge |
| Conflicting memories | CAF analysis | Resolve and consolidate |
| User corrections | Override records | Validate and incorporate |
| External changes | Business events | Update affected knowledge |

---

## How KMO Works With Others

| Role | KMO's Relationship |
|------|-------------------|
| **APO** | APO specifies knowledge needs; KMO ensures availability. |
| **CSA** | CSA designs knowledge access patterns; KMO ensures sources exist. |
| **AE** | AE integrates knowledge access; KMO provides reliable sources. |
| **ARE** | ARE monitors memory growth; KMO sets retention policies. |
| **COS** | COS reports knowledge-related issues; KMO investigates and corrects. |
| **ARAO** | ARAO defines compliance requirements; KMO ensures knowledge meets them. |

---

## What KMO Does NOT Do

| Responsibility | Who Owns It |
|----------------|-------------|
| Define agent intent | APO |
| Design reasoning patterns | CSA |
| Implement knowledge access | AE |
| Operate agents | ARE |
| Monitor behavior | COS |
| Approve compliance | ARAO |

KMO curates the raw material. Others decide how to use it.

---

## The KMO Skill Profile

### Domain Expertise

- Deep understanding of the business domain
- Knowledge of authoritative sources
- Ability to distinguish fact from opinion
- Understanding of regulatory requirements for data

### Information Architecture

- Ontology and taxonomy design
- Knowledge graph concepts
- Metadata management
- Search and retrieval understanding

### Governance Mindset

- Policy design and enforcement
- Data lifecycle management
- Quality assurance processes
- Change management discipline

### Technical Literacy

- Understanding of how RAG systems work
- Vector databases and embedding concepts
- API-based knowledge access
- Integration with agent architectures

---

## Anti-Patterns

| Pattern | Why It's Dangerous |
|---------|-------------------|
| "Just give the agent access to everything" | Unbounded access causes confusion and leakage |
| "The model will figure out what's relevant" | Models need curated, grounded knowledge |
| "We'll clean up the data later" | Garbage in = garbage out, confidently |
| "Memory should grow forever" | Unbounded memory becomes toxic |
| "Tools are just APIs" | Tools need curation and access control |
| "Knowledge is someone else's problem" | If no one owns it, it degrades |

---

## Success Criteria

KMO is successful when:

- Agents reason with correct, current information
- Knowledge gaps are identified and filled
- Memory growth is bounded and healthy
- Sensitive data is protected
- Tool access is intentional, not accidental
- ARAO can audit knowledge governance
- COS reports few knowledge-related behavior issues

---

## Final Word

When someone asks:

> "How does the agent know that?"

KMO's job is to answer:

> "Because that information comes from [this validated source], curated for agent use, with [these access controls] and [these retention policies]."

If an agent "knows" something wrong, the knowledge governance failed.

**Agents are only as smart as the knowledge they're given. KMO ensures they're given the right knowledge.**

---

*End of document*

