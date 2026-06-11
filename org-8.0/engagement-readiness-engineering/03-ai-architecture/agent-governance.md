# AI Agent Governance

[← Back to AI-Native Architecture](README.md) | [← Back to ERE](../README.md)

AI agents operate under explicit governance controls that ensure reliability, accountability, and progressive trust-building.

---

## Governance Controls

| Control | Description |
|---------|-------------|
| **Autonomy levels** | Each agent has a defined autonomy level (Assistive, Automative) that determines what actions require human approval |
| **Escalation triggers** | Agents escalate to humans when confidence is low, request is out-of-scope, or stakes are high (e.g., customer-facing commitments) |
| **Audit trail** | All agent actions are logged with context, decision rationale, and outcome |
| **Feedback loop** | Human corrections feed back into agent training; systematic errors trigger autonomy review |
| **Periodic review** | ERC reviews agent performance quarterly; autonomy levels adjusted based on accuracy and adoption metrics |

---

## Autonomy Levels

### Assistive (Initial State)

- Agent drafts, suggests, or flags
- Human reviews and approves before action
- Agent learns from human corrections

### Automative (Target State)

- Agent executes routine actions autonomously
- Human reviews exceptions and edge cases
- Audit trail maintained for all actions

---

## Agent Autonomy Progression

Agents advance from Assistive to Automative based on measurable criteria:

| Agent | Initial State | Progression Criteria | Target State |
|-------|---------------|---------------------|--------------|
| **Engagement Concierge** | Answers questions; routes requests to humans | 90%+ accuracy on Q&A; <5% escalation rate on routine requests | Processes routine requests autonomously |
| **Proposal Agent** | Drafts sections for human review | 80%+ acceptance rate on drafts; positive user feedback | Generates complete first drafts |
| **Governance Agent** | Flags missing artifacts | 95%+ accuracy on completeness checks | Auto-generates gate review summaries |

### Progression Process

1. **Baseline metrics established** — Agent deployed in Assistive mode; accuracy and acceptance rates tracked
2. **Threshold achieved** — Agent meets progression criteria over sustained period (typically one quarter)
3. **ERC review** — Performance presented to ERC with recommendation for autonomy advancement
4. **Pilot expansion** — Automative mode enabled for subset of use cases
5. **Full rollout** — Automative mode enabled broadly after successful pilot

---

## Escalation Triggers

Agents escalate to humans when:

| Trigger | Example |
|---------|---------|
| **Low confidence** | Agent uncertain about answer; multiple valid interpretations |
| **Out-of-scope** | Request falls outside agent's trained domain |
| **High stakes** | Customer-facing commitments, financial implications, contractual obligations |
| **Policy uncertainty** | Request touches governance boundaries or requires judgment |
| **Explicit request** | User requests human review |

---

## Audit Trail Requirements

All agent actions are logged with:

| Field | Description |
|-------|-------------|
| **Timestamp** | When the action occurred |
| **Agent** | Which agent performed the action |
| **Action type** | What the agent did (draft, route, answer, approve, etc.) |
| **Input context** | What information the agent used |
| **Decision rationale** | Why the agent made this decision (explainability) |
| **Outcome** | Result of the action |
| **Human review** | Whether human reviewed; any corrections made |

Audit logs are:
- Retained for compliance period (minimum 2 years)
- Searchable by Engagement, agent, user, or time range
- Available for ERC governance reviews

---

## Feedback Loop

### Continuous Learning

```
User request → Agent response → Human review → Correction (if needed)
                                      ↓
                              Feedback captured
                                      ↓
                              Agent improvement
```

### Systematic Error Detection

| Pattern | Response |
|---------|----------|
| **Single error** | Logged; agent continues at current autonomy |
| **Repeated error (same type)** | Flagged for engineering review; training data updated |
| **Systematic error (pattern)** | Autonomy review triggered; may downgrade to Assistive |
| **Customer-impacting error** | Immediate escalation; incident review; autonomy paused |

---

## ERC Oversight

### Quarterly Review

ERC reviews agent performance quarterly, examining:

| Metric | What It Measures |
|--------|------------------|
| **Accuracy rate** | % of agent outputs accepted without modification |
| **Escalation rate** | % of requests escalated to humans |
| **Autonomy utilization** | % of automative capacity actually used |
| **User satisfaction** | Feedback scores from agent users |
| **Error patterns** | Types and frequency of errors |

### Review Outcomes

| Outcome | Action |
|---------|--------|
| **Advance** | Agent moves from Assistive to Automative (or expands Automative scope) |
| **Maintain** | Agent continues at current autonomy level |
| **Regress** | Agent returns to Assistive mode (or reduces Automative scope) |
| **Retire** | Agent decommissioned (not providing value) |

---

## Compliance Dashboard Metrics

AI agent compliance is tracked alongside delivery and knowledge compliance:

| Metric | Description | Target |
|--------|-------------|--------|
| **Agent accuracy** | % of agent outputs accepted without modification | >85% |
| **Escalation rate** | % of requests escalated to humans | <10% (varies by agent) |
| **Autonomy utilization** | % of automative capacity actually used | >70% |
| **Autonomy progression** | # of agents advanced from Assistive to Automative | Increasing trend |

See [Compliance Dashboards](../06-governance-enforcement/compliance-dashboards.md) for full dashboard specification.

---

*See also: [Agents](agents.md) | [Progressive Enforcement Model](../06-governance-enforcement/README.md) | [Compliance Dashboards](../06-governance-enforcement/compliance-dashboards.md)*
