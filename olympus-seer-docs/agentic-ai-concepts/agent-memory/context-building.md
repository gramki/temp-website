# Context Building (Context Compiler) for Agents

## What “context building” is

Context building is the process of assembling the **ephemeral working set** an agent will “think with” for a single step/turn.

It answers:

> *“Given the goal and constraints, what information and procedures should be present in the model’s context right now?”*

Key principle:

> Context should be **compiled**, not concatenated.

## Inputs to context

Context should be built from clearly separated sources:

- **System constraints**: safety rules, tool allowlists, policy gates
- **Task goal + plan**: the intent for this step
- **Knowledge**: authoritative external info (RAG, APIs, databases)
- **Agent memory**:
  - **semantic**: stable facts and entity models
  - **episodic**: recent relevant traces and outcomes
  - **preference**: behavior/tone/format/risk preferences
  - **procedural**: applicable workflows and playbooks
- **Tool outputs**: latest results, errors, partial progress

## Context compiler pipeline (recommended)

1. **Clarify the query/goal**
   - identify the decision to be made and the required output shape
2. **Select retrievers by type**
   - semantic retriever, episodic retriever, preference retriever, procedure selector
3. **Retrieve candidates**
   - hybrid (symbolic filters + vector similarity) where appropriate
4. **Filter and dedupe**
   - remove irrelevant, duplicate, or unsafe content
5. **Conflict resolution**
   - resolve contradictions via precedence and freshness:
     - system policy > procedural allowlist > verified knowledge > semantic memory > episodic hints > preferences
6. **Rank and budget**
   - allocate token budget per section (e.g., constraints, facts, episodes, procedures)
7. **Assemble a structured frame**
   - compile into a predictable layout (see below)
8. **Log provenance**
   - record which items were included and why (for debugging/audit)

## Structured context frame (example)

Recommended frame sections (order matters):

- **Constraints**
  - safety rules, tool allowlists, policy requirements
- **Goal**
  - current objective and “definition of done”
- **Ground truth facts**
  - key semantic facts + retrieved knowledge with citations/provenance
- **Recent relevant episodes**
  - short summaries with pointers to full traces
- **Preferences**
  - user/app/tenant preferences relevant to this response
- **Applicable procedures**
  - selected workflow/playbook steps + checks
- **Working state**
  - tool outputs and intermediate variables for this step

## Token budgeting guidance

- Keep **constraints** and **goal** always present (small but mandatory).
- Keep **semantic facts** concise (prefer normalized facts over paragraphs).
- Keep **episodes** summarized; include only the parts that change the decision.
- Keep **procedures** as structured steps; avoid long prose.

## Safety and robustness

- Treat retrieved text (from memory or RAG) as **untrusted input**.
- Separate **data** from **instructions**: do not allow retrieved content to override system constraints.
- Apply **PII minimization** and consent rules before any memory write or retrieval.

## Common failure modes

- **“Top‑K chunks = memory”**: unstable, high token cost, no provenance
- **No promotion path**: repeated rediscovery because semantic facts aren’t consolidated
- **No conflict handling**: oscillation between contradictory “truths”
- **No observability**: can’t answer “why did you do that?”

## Navigation

- Back: [`README.md`](./README.md)
- Prev: [`procedural-memory.md`](./procedural-memory.md)

