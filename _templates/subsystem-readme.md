# [Subsystem Name]

<!-- 
Template: Subsystem README
Purpose: Overview documentation for a subsystem folder
Instructions: Replace all [bracketed] text and remove these comments
-->

## Overview

<!-- 2-3 sentences describing what this subsystem does and its role in the system -->

[Brief description of the subsystem's purpose and responsibilities]

## Architecture

<!-- Include a diagram showing the high-level architecture -->

```
┌─────────────────────────────────────────────────────────┐
│                    [Subsystem Name]                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   ┌──────────────┐    ┌──────────────┐                  │
│   │ Component A  │───▶│ Component B  │                  │
│   └──────────────┘    └──────────────┘                  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

<!-- Or use Mermaid for more complex diagrams -->

## Key Concepts

<!-- Define the core concepts/entities this subsystem deals with -->

| Concept | Description |
|---------|-------------|
| **[Concept A]** | [Definition] |
| **[Concept B]** | [Definition] |
| **[Concept C]** | [Definition] |

## Components

<!-- List the components in this subsystem with links to detailed docs -->

| Component | Description | Documentation |
|-----------|-------------|---------------|
| [Component A] | [Brief description] | [component-a.md](component-a.md) |
| [Component B] | [Brief description] | [component-b.md](component-b.md) |

## Core Responsibilities

<!-- Bulleted list of what this subsystem is responsible for -->

- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

## Integration Points

<!-- How this subsystem connects to other subsystems -->

### Inbound

| Source | Interface | Description |
|--------|-----------|-------------|
| [Subsystem X] | [API/Event/etc.] | [What data/events come in] |

### Outbound

| Target | Interface | Description |
|--------|-----------|-------------|
| [Subsystem Y] | [API/Event/etc.] | [What data/events go out] |

## Configuration

<!-- Key configuration options, if applicable -->

| Setting | Description | Default |
|---------|-------------|---------|
| [setting_name] | [What it controls] | [Default value] |

## Related Documentation

<!-- Links to related docs, ADRs, guides -->

- [Related Subsystem](../related-subsystem/README.md)
- [ADR: Relevant Decision](../../decision-logs/0000-decision.md)
- [Guide: How to Use This](../../10-guides/relevant-guide.md)

## Open Points

<!-- Link to open points if they exist -->

See [open-points.md](open-points.md) for unresolved questions.

