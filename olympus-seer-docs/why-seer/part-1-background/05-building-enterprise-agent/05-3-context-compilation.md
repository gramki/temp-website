# 5.3 Context Compilation

The effectiveness of an AI agent depends fundamentally on the information available to it during reasoning. Unlike human experts who draw on years of accumulated experience and tacit knowledge, AI agents must have their reasoning context explicitly assembled for each step. This process—**context compilation**—is one of the most critical and least understood aspects of enterprise agent design.

## What Context Compilation Is

Context compilation is the process of assembling the **ephemeral working set** an agent will reason with for a single step or turn. It answers a fundamental question:

> *Given the goal and constraints, what information should be present in the model's context right now?*

The key principle is that context should be **compiled, not concatenated**. Simply appending information to a prompt—conversation history, retrieved documents, memory fragments—produces unpredictable, inefficient, and often unsafe results. Compilation implies a deliberate process of selection, filtering, ordering, and formatting.

## The Context Compilation Pipeline

A systematic approach to context compilation follows these stages:

### 1. Clarify the Goal

Before assembling context, the system must identify:
- The decision to be made or action to be taken
- The required output shape (format, structure, constraints)
- The cognitive task type (reasoning, retrieval, classification, generation)

### 2. Select Sources by Type

Different cognitive tasks require different information sources. The context compiler must determine which source types are relevant:
- **System constraints:** Safety rules, tool allowlists, policy gates
- **Task goal and plan:** The intent for this step
- **Knowledge:** Authoritative external information (policies, SOPs, reference data)
- **Memory:** Agent and enterprise memory (episodic, semantic, procedural, preference)
- **Tool outputs:** Latest results, errors, partial progress

### 3. Retrieve Candidates

For each relevant source type, the system retrieves candidate information:
- Hybrid retrieval (symbolic filters + vector similarity) where appropriate
- Recency and relevance ranking
- Confidence scoring for uncertain information

### 4. Filter and Deduplicate

Not all retrieved candidates belong in context:
- Remove irrelevant or marginally relevant content
- Eliminate duplicates and near-duplicates
- Apply safety filters for inappropriate content
- Enforce access control (agent should only see authorized information)

### 5. Resolve Conflicts

When retrieved information contains contradictions, the compiler must apply precedence rules:

**Recommended precedence (baseline):**
```
system policy > procedural allowlist > verified knowledge > 
enterprise memory > agent memory > preferences
```

Freshness also matters: recent authoritative information typically supersedes older information of the same type.

### 6. Rank and Budget

Context windows have token limits. The compiler must allocate budget across sections:
- **Constraints and goal:** Always present (small but mandatory)
- **Ground truth facts:** Concise, normalized (prefer facts over paragraphs)
- **Relevant episodes:** Summarized, only parts that change the decision
- **Applicable procedures:** Structured steps, not prose
- **Working state:** Tool outputs and intermediate variables

### 7. Assemble a Structured Frame

The compiled context should follow a predictable structure:

| Section | Contents |
|---------|----------|
| **Constraints** | Safety rules, tool allowlists, policy requirements |
| **Goal** | Current objective and "definition of done" |
| **Ground Truth Facts** | Key semantic facts + retrieved knowledge with citations |
| **Recent Relevant Episodes** | Short summaries with pointers to full traces |
| **Preferences** | User/app/tenant preferences relevant to this response |
| **Applicable Procedures** | Selected workflow/playbook steps and checks |
| **Working State** | Tool outputs and intermediate variables for this step |

### 8. Log Provenance

For audit and debugging, the compiler must record:
- Which items were included and why
- Which items were excluded and why
- The versions of sources consulted
- The token budget allocation applied

## Why Compilation Matters for Enterprise

Context compilation is not merely a performance optimization. It has fundamental implications for enterprise agent governance:

### Reproducibility

A well-designed compilation process enables reconstruction of the exact context an agent used for any historical decision. This is essential for audit, dispute resolution, and incident investigation.

### Safety

By treating retrieved text as **untrusted input** and separating data from instructions, context compilation prevents prompt injection attacks where retrieved content attempts to override system constraints.

### Efficiency

Systematic compilation reduces token usage (and therefore cost) while improving reasoning quality by presenting only relevant, well-organized information.

### Explainability

Provenance logging enables the system to explain not just what the agent decided, but what information it considered and how that information was prioritized.

## Common Failure Modes

Several patterns lead to poor context compilation:

- **"Top-K chunks = memory":** Simply retrieving the K most similar chunks produces unstable prompts with no provenance and high token cost.
- **No promotion path:** Repeated rediscovery of the same facts because semantic memory is not consolidated.
- **No conflict handling:** Oscillation between contradictory "truths" when sources disagree.
- **No observability:** Inability to answer "why did the agent do that?" because context assembly was not logged.

---

**References:**
*   `olympus-seer-docs/agentic-ai-concepts/agent-memory/context-building.md`
*   `olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md`
