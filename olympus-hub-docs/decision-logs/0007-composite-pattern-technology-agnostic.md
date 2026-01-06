# ADR-0007: Composite Patterns Are Technology Agnostic

## Status

Accepted

## Date

2026-01-06

## Context

The "Scenario as an Agent" composite pattern allows a Scenario to be enrolled as an Agent in another Scenario's task queue. Early documentation implied this pattern required AI capabilities (like Seer) to power the automating Scenario.

This raised concerns:
- Would teams without AI expertise be excluded from using this pattern?
- Are simpler automation approaches (rules, workflows) not viable?
- Does "Agent" imply artificial intelligence?

## Decision

**Composite patterns do NOT require AI or Gen AI capabilities. The "Agent" role refers to the capability to complete tasks, not the underlying technology.**

A Scenario-as-Agent can be powered by any Hub Application type:

| Automation Type | Runtime | Example |
|-----------------|---------|---------|
| Rule-based | Atlantis (Drools/DMN) | Decision rules, validation |
| Workflow | Rhea (BPMN) | Multi-step approval processes |
| Image processing | Atlantis (Custom) | Document classification, OCR |
| Batch processing | Perseus | File parsing and validation |
| Durable workflow | ChronoShift | Long-running integrations |
| AI-powered | Seer | LLM analysis, agentic workflows |

Documentation must:
1. Always emphasize that any automation type works
2. Provide examples for both AI and non-AI approaches
3. Not assume or imply AI is required

## Consequences

### Positive
- **Inclusive**: Teams can use patterns with their existing skills
- **Pragmatic**: Simple problems get simple solutions
- **Clear terminology**: "Agent" means task-completer, not AI
- **Broader adoption**: Lower barrier to entry for composite patterns

### Negative
- **More examples needed**: Documentation must cover multiple approaches
- **Potential confusion**: "Agent" term may still suggest AI to some readers

### Neutral
- AI-powered automations remain a valid and powerful option when appropriate

## Related

- [Scenario as an Agent](../09-composite-systems-and-patterns/scenario-as-an-agent.md)
- [Composite Systems and Patterns](../09-composite-systems-and-patterns/README.md)
- [Composite Patterns Rules](../09-composite-systems-and-patterns/.cursor/rules/composite-patterns-rules.mdc)

