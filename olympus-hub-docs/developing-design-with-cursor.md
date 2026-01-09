# Developing Design Documentation with Cursor

A practical guide for collaborative design documentation using Cursor AI, based on the workflow used to develop the Olympus Hub architecture.

---

## Table of Contents

1. [Philosophy](#philosophy)
2. [Workspace Setup](#workspace-setup)
3. [Conversation Patterns](#conversation-patterns)
4. [Documentation Structure](#documentation-structure)
5. [Decision Logging](#decision-logging)
6. [Cursor Rules](#cursor-rules)
7. [Iteration Workflow](#iteration-workflow)
8. [Quality Practices](#quality-practices)
9. [Tips and Tricks](#tips-and-tricks)

---

## Philosophy

### Design is a Conversation

Treat Cursor as a **thinking partner**, not just a document generator. The best results come from:

- **Iterative refinement** — Start rough, refine through dialogue
- **Explicit clarification** — Ask Cursor to pause and ask questions before proceeding
- **Context accumulation** — Build on previous conversations; reference past decisions
- **Human judgment preserved** — You make decisions; Cursor helps articulate and organize them

### Separation of Concerns

| Concern | Approach |
|---------|----------|
| **Finished thinking** | Formal documentation in structured folders |
| **Unfinished thinking** | Scratchpad folder with protective rules |
| **Decisions made** | Architecture Decision Records (ADRs) |
| **Future guidance** | Cursor rules files |

---

## Workspace Setup

### Folder Structure

Organize documentation hierarchically by concern:

```
project-docs/
├── 01-overview/
├── 02-concepts/
├── 03-architecture/
├── 04-subsystems/
│   ├── subsystem-a/
│   │   ├── README.md
│   │   ├── component-1.md
│   │   └── open-points.md      # Track unresolved questions
│   └── subsystem-b/
├── 06-ux-architecture/
├── 09-composite-patterns/
├── 10-guides/
├── decision-logs/               # ADRs
│   ├── README.md               # Index
│   ├── 0001-decision-name.md
│   └── ...
├── scratchpad/                  # Unfinished thinking
│   └── .cursor/rules/
├── .cursor/rules/               # Project-wide Cursor rules
└── README.md
```

### Essential Cursor Rules Files

Create these rule files to guide AI behavior:

#### 1. Commit Message Format (`.cursor/rules/git-commits.mdc`)
```markdown
Always use this format for git commit messages:
[ticketID] <type>(<scope>): <subject>

Example: [SPE-2586] feat(auth): add biometric login option
```

#### 2. Decision Logging (`.cursor/rules/decision-logs.mdc`)
Define when and how to capture architectural decisions.

#### 3. Scratchpad Protection (`scratchpad/.cursor/rules/scratchpad-rules.mdc`)
Prevent AI from eagerly consulting draft content.

---

## Conversation Patterns

### Pattern 1: Context Setting

Start sessions by providing context before diving into work:

```
We are working on [project]. I previously asked about [topic].
You replied with [summary]. Let's continue from there.
```

### Pattern 2: Clarification Request

Ask Cursor to pause and ask questions before proceeding:

```
Hold, I need to provide clarifications. Acknowledge that you understood the context.
```

Or:

```
Ask any clarifications you may need. We don't need to go beyond C2-level details.
```

### Pattern 3: Phased Approach

For complex topics, break work into phases:

```
Phase 1: Understand and ask questions
Phase 2: Propose structure (don't write yet)
Phase 3: Write documentation
Phase 4: Review for consistency
```

### Pattern 4: Explicit Decision Making

When making decisions, be explicit:

```
We will go with [option]. Accordingly, revise your understanding
and convey all the changes you are going to do before you make them.
```

### Pattern 5: Review Passes

Request focused reviews:

```
Do one more pass for ambiguities and inconsistencies around [topic].
```

```
Fix whatever you can without creating confusion.
Write any open points in open-points.md.
```

### Pattern 6: Scoped Questions

Provide answers to Cursor's questions in a structured format:

```
1. Question about X?
> Answer to X

2. Question about Y?
> Answer to Y, with additional context
```

---

## Documentation Structure

### Document Templates

#### Subsystem README

```markdown
# [Subsystem Name]

## Overview
Brief description of what this subsystem does.

## Architecture
High-level architecture diagram and explanation.

## Key Concepts
- **Concept A**: Definition
- **Concept B**: Definition

## Components
List of components with links to detailed docs.

## Integration Points
How this subsystem connects to others.

## See Also
- [Related Doc 1](link)
- [Related Doc 2](link)
```

#### Guide Document

```markdown
# [Guide Title]

## Overview
What this guide covers and who it's for.

## Prerequisites
What the reader needs to know/have.

## Step-by-Step Instructions
### Step 1: [Action]
Details...

### Step 2: [Action]
Details...

## Examples
Complete worked examples.

## Troubleshooting
Common issues and solutions.
```

### Open Points Document

Every subsystem should have an `open-points.md` to track unresolved questions:

```markdown
# Open Points

## Resolved
- [x] Question 1 — Resolved by [decision/ADR reference]

## Under Discussion
- [ ] Question 2 — Context and current thinking

## Deferred
- [ ] Question 3 — To be addressed in [future phase]
```

---

## Decision Logging

### When to Capture a Decision

Capture an ADR when:

- Choosing between multiple valid approaches
- Establishing a pattern that should be followed consistently
- Making trade-offs (favoring X over Y for reason Z)
- Defining boundaries (what's in scope vs. out of scope)
- Setting conventions or standards

### ADR Format

```markdown
# [Number]. [Title]

## Status
[Proposed | Accepted | Deprecated | Superseded by [ADR-XXXX]]

## Context
What is the issue? Why does a decision need to be made?

## Decision
What is the decision being made?

## Alternatives Considered
### Alternative 1: [Name]
- Description
- Pros
- Cons

### Alternative 2: [Name]
...

## Consequences
### Positive
- Benefit 1
- Benefit 2

### Negative
- Trade-off 1
- Trade-off 2

## References
- [Related ADR](link)
- [Related Documentation](link)
```

### Numbering Convention

```
0001-0099: Foundational decisions
0100-0199: Subsystem-specific decisions
0200+: Feature-specific decisions
```

### Consistency Verification

When creating new ADRs:
1. Check that new decisions don't contradict existing non-superseded decisions
2. When a decision supersedes another, add references in both places
3. Mark superseded decisions with "Superseded by [ADR-XXXX]" status

---

## Cursor Rules

### Purpose of Rules Files

Rules files (`.cursor/rules/*.mdc`) provide persistent instructions to Cursor:

- **Project conventions** — Naming, formatting, structure
- **Domain knowledge** — Key concepts Cursor should remember
- **Behavioral guidance** — When to ask vs. proceed, what to avoid
- **Quality standards** — Review checklists, documentation standards

### Creating Effective Rules

```markdown
# [Rule Category]

## Purpose
Why this rule exists.

## Instructions

### DO
- Specific action to take
- Another action

### DO NOT
- Specific action to avoid
- Another action

## Examples
Good and bad examples.
```

### Rules We Found Useful

| Rule File | Purpose |
|-----------|---------|
| `decision-logs.mdc` | When and how to capture ADRs |
| `composite-patterns-rules.mdc` | Standards for documenting patterns |
| `scratchpad-rules.mdc` | Don't eagerly read draft content |
| `git-commits.mdc` | Commit message format |

---

## Iteration Workflow

### Daily Session Flow

```
1. Set Context
   - Reference previous work
   - State current goal

2. Collaborate
   - Provide information when asked
   - Course-correct as needed
   - Make decisions explicitly

3. Review
   - Ask for consistency checks
   - Capture open points

4. Commit
   - Meaningful commit messages
   - Push regularly
```

### Multi-Session Projects

For large features spanning multiple sessions:

1. **Start with TODO list** — Break work into trackable items
2. **Complete in order** — Avoid jumping around
3. **Commit after each milestone** — Clear save points
4. **End sessions cleanly** — Document where you stopped

### Backfilling

When you realize past decisions weren't captured:

```
Can you go through [folder/topic] and propose decision records
for relevant decisions?
```

---

## Quality Practices

### Consistency Checks

Periodically request reviews:

```
Review [folder] for inconsistencies and ambiguities.
```

### Cross-References

- Link related documents to each other
- Reference ADRs from documentation that implements them
- Maintain README indexes for each folder

### Technology-Agnostic Examples

When documenting patterns or architectures:

- Don't assume specific technologies (e.g., "AI Agent" vs. "Automation")
- Provide multiple implementation examples
- Focus on the pattern, not the technology

### Diagram Standards

For ASCII diagrams in markdown:

```
┌─────────────┐     ┌─────────────┐
│ Component A │────▶│ Component B │
└─────────────┘     └─────────────┘
        │
        ▼
┌─────────────┐
│ Component C │
└─────────────┘
```

---

## Tips and Tricks

### Effective Prompting

| Instead of... | Try... |
|---------------|--------|
| "Document X" | "Document X, following the structure in [existing doc]" |
| "Fix this" | "Fix this without creating confusion. Document open points." |
| "Create docs" | "Create a TODO list and go one by one" |
| "Make it better" | "Do a pass for [specific concern]" |

### Managing Context

- **Reference by path**: `@path/to/file.md` pulls content into context
- **Reference by line**: `@file.md (27-37)` for specific sections
- **Summary requests**: Ask for context summaries at session start

### Handling Disagreements

When Cursor suggests something you disagree with:

```
No, that's not quite right. [Explanation of correct approach].
Update your understanding.
```

### Deferring Topics

When something is out of scope:

```
We will pick [topic] as a whole chapter later.
[Another topic] should also be discussed later.
Let us examine only [current scope].
```

### Parallel Work

Request parallel actions when possible:

```
Read [file1], [file2], and [file3] and then propose changes.
```

---

## Appendix: Session Starters

### Continuing Previous Work
```
We are working on [project]. Last session we [summary].
Let's continue with [next task].
```

### Starting New Topic
```
Let's document [new topic]. Here is the context:
[Detailed explanation]
Ask any clarifications you need.
```

### Review Session
```
Review [folder] for:
- Inconsistencies with other modules
- Ambiguous statements
- Missing cross-references
Fix what you can. Document open points.
```

### Decision Capture Session
```
Go through our discussions about [topic] and construct
decision records for the key decisions.
```

---

## Summary

The key to effective design documentation with Cursor:

1. **Structure your workspace** — Clear folders, rules, and conventions
2. **Communicate explicitly** — State decisions, provide context, ask for pauses
3. **Iterate systematically** — Review, refine, commit
4. **Capture decisions** — ADRs preserve reasoning for the future
5. **Protect drafts** — Scratchpad for thinking, formal folders for finished work

---

*This guide is based on the collaborative development of Olympus Hub architecture documentation.*

