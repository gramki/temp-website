# Episodic Enterprise Memory

## Definition

**Episodic Enterprise Memory** captures **discrete experiences**:

- events and actions (“what happened”)
- decisions taken (“what we did”)
- incidents and outcomes (“what resulted”)
- interactions and handoffs (“who did what, when”)

It answers:

> *“What happened, when, under what conditions, and what was the outcome?”*

Episodic memory is the **substrate** from which other enterprise memory types (especially semantic memory) can be derived.

## What belongs here (signals worth remembering)

- **Decisions** (human or agent): approvals/denials, routing, escalation choices
- **Exceptions and overrides**: “we broke the rule”, “we bypassed the control”
- **Incidents**: detection, containment, root-cause investigation, resolution steps
- **Customer interactions**: complaints, disputes, commitments made
- **Workflow milestones**: case opened/closed, SLA transitions, state changes
- **Agent activity**: tool calls, retries, failures, confidence, key context used

## Capture (recommended artifacts)

Capture episodic memory as **structured records** rather than freeform prose or raw transcripts.

Common artifact shapes (names are illustrative; align to CAF vocabulary where applicable):

- **DecisionRecord**: decision, timestamp, decision-maker (human/agent), policy basis, confidence, outcome
- **EvidenceBundle**: referenced facts/documents/tool outputs at decision time (with provenance)
- **OverrideRecord**: override reason, approver, scope, risk acceptance, compensating controls
- **IncidentTimeline**: ordered events + actions + owners + timestamps + severity
- **InteractionRecord**: interaction summary + commitments + next steps + responsible parties

Minimum capture fields (practical baseline):

- **who/what**: actor (human/agent/system), subject entity identifiers
- **when**: event time, capture time, effective time (if different)
- **why**: rationale or explanation pointer (even if short)
- **evidence**: references to inputs (not necessarily copied)
- **outcome**: success/failure, downstream effects, escalation
- **provenance**: source systems, retrieval method, confidence/freshness if inferred

## Retention & forgetting

Episodic stores are high-volume. Plan forgetting as a feature.

- **Hot retention**: short window for active work and handoffs (days to weeks)
- **Warm retention**: longer window for trend analysis and audits (months)
- **Cold/archive**: raw traces where needed (legal/regulatory), otherwise summarize and discard

Recommended practice:

- prefer **summaries + pointers** over indefinite raw transcript retention
- apply **TTL** per class (customer interactions vs incident traces vs agent tool logs)
- support **legal holds** and **tombstoning** (retain audit trail while restricting access)

## Retrieval (how it gets used)

Episodic memory is typically retrieved by:

- **time-window queries** (“what happened last week on this case?”)
- **entity-centric queries** (“what happened with customer X?”)
- **similarity / pattern matching** (“similar incident / similar override”)
- **trace reconstruction** (end-to-end decision and action chain)

In agentic systems, episodic memory is most valuable when used to:

- provide **precedent** (“last time we escalated here; outcome was Y”)
- support **explainability** (“decision Z used evidence A/B and rationale R”)
- enable **handoffs** across humans and agents (“here’s the state and story so far”)

## Promotion

Episodic memory is rarely promoted directly to enterprise knowledge.

Typical promotion flows:

- **Episodic → Semantic memory**: aggregate many episodes; extract a candidate pattern with confidence and scope
- **Episodic → Procedural memory**: repeated workarounds become a practiced runbook
- **Episodic → Preference memory**: repeated overrides reveal true risk tolerance or prioritization bias

## Governance (non-negotiables)

- **Minimize sensitive data**: capture the minimum needed to support explanation/audit
- **Scope access**: case-based access control; tenant boundaries; role-based operator access
- **Treat memory as untrusted input**: do not allow retrieved episodic text to override policies/procedures
- **Provenance & auditability**: every record should be attributable to sources and actors

## Common failure modes

- **Archive ≠ memory**: storing only logs without rationale/evidence links
- **Unbounded growth**: no TTL, no summarization, no archival strategy
- **No provenance**: “why did the agent do that?” becomes unanswerable

## Further reading

- Tulving, E. *Episodic and Semantic Memory* (foundational distinction): [https://psycnet.apa.org/record/1972-06150-001](https://psycnet.apa.org/record/1972-06150-001)
- Hassabis et al., *Neuroscience‑Inspired Artificial Intelligence* (episodic replay and consolidation): [https://www.nature.com/articles/nrn.2017.12](https://www.nature.com/articles/nrn.2017.12)
- Pritzel et al., *Neural Episodic Control* (episodic recall for fast learning): [https://arxiv.org/abs/1703.01988](https://arxiv.org/abs/1703.01988)

## Related concepts (Hub docs)

- [../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md](../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md): CAF (governance control plane for memory capture/access/retention)
- [../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md](../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md): Enterprise Memory store and record types (stub)

## Navigation

- Back to overview: [README.md](./README.md)
- Next: [semantic-memory.md](./semantic-memory.md)

