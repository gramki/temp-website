# ADR-0010: AI Assistants as First-Class Interaction Channel

## Status

Accepted

## Date

2026-01-06

## Context

AI assistants like ChatGPT, Claude, Gemini, and custom agents are becoming primary interfaces for enterprise users. Organizations want their employees to interact with business systems through these AI assistants.

Options considered:
1. **Plugin/Integration approach**: Add Hub as a plugin to each AI system
2. **API-only approach**: Expose REST APIs, let users figure out AI integration
3. **First-class channel approach**: Treat AI assistants as equal to Web/Mobile

The plugin approach requires per-platform implementation and maintenance. The API-only approach puts burden on users.

## Decision

**Treat AI assistants as first-class interaction channels via MCP (Model Context Protocol).**

This means:
1. **Every persona capability must be accessible via MCP tools** — not just a subset
2. **AI assistants appear alongside traditional channels** (Web, Mobile, MS Teams)
3. **Persona-scoped MCP gateways** provide curated tool sets per role
4. **Standard MCP protocol** enables any compliant AI system to connect

### First-Class Channels
| Category | Channels |
|----------|----------|
| Traditional | Web, Mobile, Email |
| Collaboration | MS Teams, Slack |
| **AI Assistants** | ChatGPT, Claude, Gemini, Custom AI, Seer |
| Programmatic | REST APIs |

### Implications
- MCP tool design is as important as UI design
- Tool descriptions must be clear for AI interpretation
- Authentication and authorization apply to AI sessions
- Audit trails capture AI-initiated actions

## Consequences

### Positive
- **Future-ready**: As AI assistants become more capable, Hub is ready
- **User choice**: Users work with preferred AI assistant
- **Consistent capabilities**: AI gets same power as web UI
- **Innovation-friendly**: New AI systems connect via standard MCP

### Negative
- **Design overhead**: Must design both UI and tool interfaces
- **Testing complexity**: Must test AI interaction patterns
- **Security considerations**: AI actions need same controls as human

### Neutral
- Some interactions may be better in traditional UI (complex forms, visualizations)
- AI and traditional channels can complement each other

## Related

- [MCP Channels](../06-ux-architecture/tenant-domain/mcp-channels.md)
- [MCP Router](../05-infrastructure/mcp-router.md)
- [UX Architecture Overview](../06-ux-architecture/README.md)

