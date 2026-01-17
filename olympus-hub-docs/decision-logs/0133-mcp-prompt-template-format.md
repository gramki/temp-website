# 0133. MCP Prompt Template Format

## Status

Accepted

## Date

2026-01-17

## Context

Prompt templates must be compatible with MCP Router's `prompts/list` response format to enable AI agents to discover and use prompts. Hub needs to store additional metadata (category, scenario reference, task type, template content) while maintaining MCP protocol compatibility.

### Constraints

- Must be semantically and structurally equivalent to MCP Router's list-prompts response
- Must support Mustache/Handlebars template compilation
- Must enable context-rich prompt compilation (request, task, subject data)
- Must support different prompt categories (task solver, guidance, error handling, progress)

### Requirements

- MCP-compatible structure for protocol compliance
- Hub-specific metadata for template management
- Template compilation with full request context
- Support for task solver prompts (essential) and optional guidance prompts

## Decision

We will structure prompt templates for **semantic and structural equivalence** with MCP Router's list-prompts response, with Hub storing additional metadata internally.

### Key Points

- **Hub stores additional metadata**: `category`, `scenario_ref`, `task_type`, `template` (full template content)
- **MCP Router exposes only MCP-compliant fields**: `name`, `description`, `arguments`
- **Template compilation**: Mustache/Handlebars used for template rendering (same as Tool Specifications)
- **Context available**: Full request context available for compilation (request, task, subject, related entities)
- **machine-template does not support prompts**: Only scenario-based templates support prompts

## Alternatives Considered

### Alternative 1: MCP-Only Format

**Description:** Store only MCP-compliant fields, no Hub-specific metadata

**Pros:**
- Simple
- Direct MCP compatibility

**Cons:**
- Cannot link prompts to scenarios/tasks
- Cannot categorize prompts
- Cannot compile with context
- Poor developer experience

**Why rejected:** Need Hub-specific metadata for template management and context compilation

---

### Alternative 2: Hub-Only Format with Translation

**Description:** Store Hub format, translate to MCP format on-the-fly

**Pros:**
- Rich Hub metadata
- Flexible format

**Cons:**
- Translation complexity
- Potential format drift
- Harder to maintain compatibility

**Why rejected:** Semantic/structural equivalence ensures compatibility without translation overhead

---

### Alternative 3: Separate Formats

**Description:** Store Hub format and MCP format separately

**Pros:**
- Clear separation
- No compatibility concerns

**Cons:**
- Data duplication
- Synchronization complexity
- Maintenance overhead

**Why rejected:** Semantic/structural equivalence avoids duplication while maintaining compatibility

## Consequences

### Positive

- **MCP Compatibility**: Direct compatibility with MCP Router
- **Rich Metadata**: Hub can store additional metadata for management
- **Context Compilation**: Full request context available for template compilation
- **Developer Experience**: Clear structure for prompt authoring
- **No Translation**: No need for format translation

### Negative

- **Format Discipline**: Must maintain semantic/structural equivalence
- **Template Engine**: Must use Mustache/Handlebars (same as Tool Specifications)

### Neutral

- **Template Storage**: Hub stores full template, MCP Router exposes subset
- **Compilation Performance**: Template compilation happens server-side

## Implementation Notes

- Prompt template format defined in [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md)
- Mustache/Handlebars used for template rendering (same as Tool Specifications)
- Context variables available: `request`, `task`, `subject`, `scenario`, `related_entities`
- Template compilation happens server-side when client requests prompt

## Related Decisions

- [ADR-0131: MCP Server CRD Design](./0131-mcp-server-crd-design.md) — CRD structure
- [ADR-0132: MCP Template Kinds](./0132-mcp-template-kinds.md) — Template kinds

## References

- [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md)
- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md)
