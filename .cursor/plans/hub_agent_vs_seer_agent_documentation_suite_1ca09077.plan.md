---
name: Hub Agent vs Seer Agent Documentation Suite
overview: Create a comprehensive documentation suite for Hub Agents vs Seer Agents at C2 (Container) level with C3 (Component) level detail only when absolutely needed. Focus on architectural understanding, decision frameworks, and examples. Reference existing documentation for implementation details rather than creating protocol-level content.
todos:
  - id: envelope-doc
    content: Create main envelope document (hub-agent-vs-seer-agent.md) with executive summary, confusion statement, quick reference table, reading guide by audience, document map, and key takeaways
    status: completed
  - id: core-understanding
    content: "Create Part 1 (Understanding) of core document: core distinction, relationship diagram, Hub Agent criteria, identity models, protocol interfaces, common misconceptions - all with citations"
    status: completed
  - id: core-building
    content: "Create Part 2 (Building) of core document: Hub Agent creation process (ScenarioAsAgent CRD, IAM registration, enrollment), Seer Agent creation process (lifecycle, binding, deployment), identity flow diagrams"
    status: completed
  - id: core-decision
    content: "Create Part 3 (Decision Framework) of core document: decision tree, decision matrix, runtime selection guide, identity model decisions, task queue requirements"
    status: completed
  - id: examples-rhea
    content: "Create Example 1 in examples document: Rhea Workflow as Hub Agent with complete Scenario definition, Hub Application config, ScenarioAsAgent CRD, task queue enrollment, runtime behavior"
    status: completed
  - id: examples-seer
    content: "Create Example 2 in examples document: Seer Agent as Hub Agent with Raw Agent development, Training Spec, Employment Spec, Scenario binding, Hub Agent participation"
    status: completed
  - id: examples-composite
    content: "Create Example 3 in examples document: Composite Application with multiple agent types, sub-personas, coordination patterns"
    status: completed
  - id: examples-customer
    content: "Create Example 4 in examples document: Customer-facing scenarios showing when to use Hub Agent (non-Seer) vs Seer Agent vs hybrid"
    status: completed
  - id: anti-patterns-migrate
    content: Migrate all 10 anti-patterns from critique document to anti-patterns document, expand with context, add alternatives guide
    status: completed
  - id: architectural-crd
    content: "Create ScenarioAsAgent CRD section: explain architectural role (C2 level) and relationship to Hub Agent creation, reference existing CRD documentation for YAML details"
    status: completed
  - id: architectural-identity
    content: "Create identity management section: explain token structure at architectural level (what identities are included, not how to parse), reference ADR-0129, link to Cipher IAM docs"
    status: completed
  - id: architectural-protocols
    content: "Create protocol interfaces section: list available protocols (HTTP, MCP, A2A) at C2 level, explain when each is used architecturally, reference existing protocol docs for implementation"
    status: completed
  - id: architectural-references
    content: "Add references section: compile links to existing guides for testing, troubleshooting, code examples, and operational concerns"
    status: completed
  - id: customer-analogies
    content: Create customer guide document with simple analogies, conversation guide, decision matrix for CSAs
    status: completed
  - id: customer-use-cases
    content: Add use case scenarios with business value to customer guide document
    status: completed
  - id: cross-references
    content: Add cross-references between all documents, ensure all citations use correct inline markdown link format
    status: completed
  - id: update-readme
    content: Update decision-frameworks README.md to include all new documents in the index
    status: completed
  - id: verify-citations
    content: Verify all architectural claims have citations, all design decisions reference ADRs, all technical details reference implementation docs
    status: completed
  - id: cleanup-scratchpad
    content: Remove or archive scratchpad documents (0WIP-hub-agent-vs-seer-agent.md, CRITIQUE-hub-agent-vs-seer-agent.md) after content migration verified
    status: completed
---

# Hub Agent vs Seer Agent Documentation Suite

## Structure Overview

Create a hybrid documentation structure with:

1. **Main Envelope Document** - Overview, reading guide, quick reference
2. **Core Comprehensive Document** - Understanding, building basics, decision framework
3. **Focused Deep-Dive Documents** - Examples, anti-patterns, implementation details

## Document Structure

### 1. Main Envelope: `hub-agent-vs-seer-agent.md`

**Location**: `olympus-hub-docs/11-decision-frameworks/hub-agent-vs-seer-agent.md`

**Purpose**: Entry point with overview, reading guidance, and quick reference

**Contents**:

- Executive summary (2-3 paragraphs)
- The confusion (why this document exists)
- Quick reference table (Hub Agent vs Seer Agent at a glance)
- Reading guide by audience:
  - Process Architects: Start with Core Concepts → Decision Framework
  - CSAs: Start with Core Concepts → Use Cases → Customer-Facing Guide
  - Developers: Start with Core Concepts → Building Guide → Implementation Details
  - Agent Engineers: Start with Core Concepts → Seer-Specific Details → Implementation Details
- Document map (links to all related documents)
- Key takeaways (bullet points)

### 2. Core Document: `hub-agent-vs-seer-agent-core.md`

**Location**: `olympus-hub-docs/11-decision-frameworks/hub-agent-vs-seer-agent-core.md`

**Purpose**: Comprehensive understanding, building basics, and decision framework

**Contents**:

#### Part 1: Understanding (What They Are)

- Core distinction (pattern vs technology)
- Relationship diagram (Seer Agent ⊆ Hub Agent)
- What makes something a Hub Agent (5 criteria)
- Hub Agent identity model (Agent Persona + optional Deployment Identity)
- Seer Agent identity model (two-layer: Persona + SPIFFE)
- Identity composition when Seer Agent is Hub Agent
- Protocol interfaces (HTTP, MCP, A2A)
- Common misconceptions (table format)

#### Part 2: Building (How They Are Created)

- Hub Agent creation process (C2 level):
  - ScenarioAsAgent CRD role and relationship to Scenario
  - Agent Persona registration process (what happens, not how)
  - Task queue enrollment mechanism
  - Identity flow diagram (container-level interactions)
  - Reference to existing CRD documentation for YAML details
- Seer Agent creation process (C2 level):
  - Raw → Trained → Employed lifecycle (architectural stages)
  - Scenario binding mechanism
  - Employment Spec role in deployment
  - SPIFFE ID provisioning (what it provides, not how)
  - Hub Application deployment relationship
  - Reference to Seer documentation for lifecycle details
- Key clarification: Hub Agent is a configuration of Scenario, not a property of Hub Application
- ScenarioAsAgent is the only way to create Hub Agents

#### Part 3: Decision Framework (When to Use What)

- Decision tree: "Do you need AI reasoning?" → Yes/No paths
- Decision matrix:
  - Use Hub Agent (non-Seer) when...
  - Use Seer Agent when...
  - Use both (Composite Application) when...
- Runtime selection guide (Rhea, Perseus, Seer, Atlantis)
- Identity model decisions (when SPIFFE is needed)
- Task queue participation requirements

### 3. Deep-Dive: `hub-agent-vs-seer-agent-examples.md`

**Location**: `olympus-hub-docs/11-decision-frameworks/hub-agent-vs-seer-agent-examples.md`

**Purpose**: Concrete examples and use cases

**Contents**:

- Example 1: Rhea Workflow as Hub Agent (non-Seer)
  - Scenario definition (architectural level)
  - Hub Application type and runtime
  - ScenarioAsAgent CRD role
  - Task queue enrollment relationship
  - Runtime behavior (what happens, not implementation)
- Example 2: Seer Agent as Hub Agent
  - Raw Agent lifecycle stage
  - Training Spec role
  - Employment Spec role
  - Scenario binding mechanism
  - Hub Agent participation (architectural relationship)
- Example 3: Composite Application (multiple agent types)
  - Multiple Hub Applications in one Scenario
  - Sub-personas for each agent
  - Coordination through shared Request state
- Example 4: Customer-facing scenarios
  - When customer needs Hub Agent (non-Seer)
  - When customer needs Seer Agent
  - Hybrid scenarios
- Example 5: Migration scenario (if applicable)
  - Evolving from rule-based to AI-based

### 4. Deep-Dive: `hub-agent-vs-seer-agent-anti-patterns.md`

**Location**: `olympus-hub-docs/11-decision-frameworks/hub-agent-vs-seer-agent-anti-patterns.md`

**Purpose**: When NOT to use Hub Agent pattern

**Contents**:

- All 10 anti-patterns from critique (already documented)
- Each with: When, Why Wrong, Use Instead, Example
- Summary decision rule (5 criteria)
- Alternatives guide (Standalone Tool, Regular Hub Application, Direct Integration)

### 5. Deep-Dive: `hub-agent-vs-seer-agent-architectural-details.md`

**Location**: `olympus-hub-docs/11-decision-frameworks/hub-agent-vs-seer-agent-architectural-details.md`

**Purpose**: C2-level architectural details and references to implementation documentation for Developers and Agent Engineers

**Contents**:

- ScenarioAsAgent CRD architectural role:
  - Relationship to Hub Agent creation
  - Reference to existing CRD documentation
  - Link to detailed CRD specifications
- Agent Persona registration (architectural process):
  - What happens (C2 level)
  - Reference to Cipher IAM documentation for details
- Task queue enrollment (architectural process):
  - Enrollment mechanism at container level
  - Reference to Task Management subsystem docs
- Identity management (architectural overview):
  - Token structure (what identities are included, not how to parse)
  - Reference to ADR-0129 for identity model details
  - Reference to Cipher IAM for implementation
- Protocol interfaces (architectural overview):
  - Available protocols (HTTP, MCP, A2A)
  - When each protocol is used
  - Reference to protocol documentation for implementation details
- References to existing guides:
  - Testing: Link to existing testing documentation
  - Troubleshooting: Link to operational runbooks
  - Code examples: Reference runtime-specific documentation

### 6. Deep-Dive: `hub-agent-vs-seer-agent-customer-guide.md`

**Location**: `olympus-hub-docs/11-decision-frameworks/hub-agent-vs-seer-agent-customer-guide.md`

**Purpose**: Customer-facing explanations for CSAs

**Contents**:

- Simple analogies (Hub Agent = participation model, Seer Agent = AI technology)
- Customer conversation guide
- Decision matrix for recommendations
- Use case scenarios with business value
- Operational considerations (monitoring, scaling)
- Cost/complexity considerations (deferred per critique)

## Implementation Plan

### Phase 1: Core Documents (Foundation)

1. Create main envelope document (`hub-agent-vs-seer-agent.md`)

   - Extract and refine overview from scratchpad
   - Add reading guide by audience
   - Add quick reference table
   - Add document map

2. Create core document (`hub-agent-vs-seer-agent-core.md`)

   - Part 1: Understanding (from scratchpad, refined)
   - Part 2: Building (new content addressing critique gaps)
   - Part 3: Decision Framework (new content with decision trees)

### Phase 2: Deep-Dive Documents (Addressing Critique)

3. Create examples document (`hub-agent-vs-seer-agent-examples.md`)

   - Address Gap 5 (Process Architects): Examples of non-AI Hub Agents
   - Address Gap 6 (CSAs): Customer use cases
   - Address Gap 1 (Cross-audience): Concrete examples throughout

4. Create anti-patterns document (`hub-agent-vs-seer-agent-anti-patterns.md`)

   - Move anti-patterns from critique document
   - Expand with more context
   - Add alternatives guide

5. Create architectural details document (`hub-agent-vs-seer-agent-architectural-details.md`)

   - Address Gap 1 (Agent Engineers): Architectural relationship of Seer Agent to Hub Agent
   - Address Gap 1 (Developers): Hub Application vs Hub Agent relationship (C2 level)
   - Address Gap 3 (Developers): ScenarioAsAgent CRD architectural role (reference existing docs)
   - Address Gap 4 (Developers): Protocol interfaces overview (reference existing docs)
   - Reference existing documentation for testing, troubleshooting, and code examples

6. Create customer guide (`hub-agent-vs-seer-agent-customer-guide.md`)

   - Address Gap 1 (CSAs): Customer-facing explanation
   - Address Gap 2 (CSAs): Decision matrix for recommendations
   - Address Gap 6 (CSAs): Customer use cases

### Phase 3: Integration and Refinement

7. Update main envelope with links to all documents
8. Add cross-references between documents
9. Update decision-frameworks README to include new documents
10. Remove scratchpad documents (after content is migrated)

## Key Content Additions (Addressing Critique Gaps)

### From Scratchpad to Core Document:

- Identity model differences (already refined)
- Relationship diagrams (already refined)
- Common misconceptions (already refined)

### New Content Needed:

1. **Building Section** (addresses Gap 2, Gap 3 from Process Architects):

   - Clear explanation: Hub Agent is configuration of Scenario via ScenarioAsAgent CRD
   - Step-by-step: Scenario → ScenarioAsAgent CRD → IAM Registration → Enrollment
   - YAML examples for ScenarioAsAgent CRD
   - Identity flow diagrams

2. **Decision Framework** (addresses Gap 2 from CSAs, Gap 2 from Cross-audience):

   - Decision tree: "Do you need AI?" → "Do you need task queue participation?"
   - Decision matrix with criteria
   - Runtime selection guide

3. **Examples** (addresses Gap 5 from Process Architects, Gap 6 from CSAs):

   - Rhea workflow as Hub Agent (concrete example)
   - Seer Agent as Hub Agent (concrete example)
   - Composite Application example
   - Customer scenarios

4. **Implementation References** (addresses Developer/Agent Engineer gaps at C2 level):

   - ScenarioAsAgent CRD architectural role (reference existing docs for schema)
   - Protocol interfaces overview (reference existing docs for API details)
   - Identity token structure (architectural overview, reference ADR-0129 for details)
   - References to existing testing and troubleshooting documentation

5. **Customer Guide** (addresses CSA gaps):

   - Simple analogies
   - Conversation guide
   - Business value examples

## Document Relationships

```
hub-agent-vs-seer-agent.md (Envelope)
├── hub-agent-vs-seer-agent-core.md (Main content)
│   ├── Understanding
│   ├── Building
│   └── Decision Framework
├── hub-agent-vs-seer-agent-examples.md (Use cases)
├── hub-agent-vs-seer-agent-anti-patterns.md (When NOT to use)
├── hub-agent-vs-seer-agent-architectural-details.md (C2-level details and references)
└── hub-agent-vs-seer-agent-customer-guide.md (For CSAs)
```

## Success Criteria

1. Process Architects can answer: "When should I design a Scenario as a Hub Agent?"
2. CSAs can explain to customers: "Hub Agent vs Seer Agent - which do you need?"
3. Developers can understand: "What is the architectural relationship between Hub Application and Hub Agent, and where do I find implementation details?"
4. Agent Engineers can understand: "How does my Seer Agent become a Hub Agent?"
5. All audiences can avoid: Anti-patterns are clearly documented

## Writing Style Requirements

### Technical Textbook Style

All documents must follow a technical textbook narrative style:

- **Factual and direct**: State facts without embellishment
- **No flowery language**: Avoid marketing language, superlatives, or emotional appeals
- **Precise terminology**: Use exact technical terms consistently
- **Structured presentation**: Use clear hierarchies, tables, and diagrams
- **Objective tone**: Present information neutrally without persuasion

### Citation and Reference Requirements

- **Inline markdown links**: Use [`Document Name`](../path/to/doc.md) format for all internal references
- **Reference all claims**: Every architectural statement, design decision, or technical claim must have a reference
- **Link to source documents**: 
  - ADRs for design decisions (e.g., [ADR-0129](../decision-logs/0129-agent-identity-model.md))
  - Implementation concepts for technical details
  - Subsystem documentation for operational details
  - Related patterns for composition approaches
- **External references**: If citing external sources, use standard academic citation format

### Diagram Style

- **Mermaid diagrams**: Use Mermaid for all flow diagrams, relationship diagrams, and process flows
- **ASCII art**: Use for simple structural representations where appropriate
- **Reference existing diagrams**: Link to diagrams in other documentation when relevant

### Content Organization

- **Hierarchical structure**: Clear section numbering and nesting
- **Tables for comparisons**: Use tables for side-by-side comparisons
- **YAML/JSON examples**: Only include if they exist in source documentation, otherwise reference source docs
- **Architectural diagrams**: Focus on container-level (C2) interactions, use component-level (C3) only when necessary

### C4 Architecture Level Constraints

- **Primary level: C2 (Container)**: Document containers (Hub Agent, Seer Agent, Scenario, Hub Application) and their interactions
- **Secondary level: C3 (Component)**: Use only when necessary to explain internal structure of containers
- **Avoid C4 (Code) level**: Do not include code implementation details, API call examples, or protocol-level specifics
- **Reference existing docs**: For implementation details, testing, troubleshooting, link to existing documentation rather than creating new content

## Notes

- **C4 Architecture Level**: Primary focus is C2 (Container) level. Use C3 (Component) level only when absolutely needed to explain container internals. Avoid C4 (Code) level details.
- **Implementation details**: Reference existing documentation rather than creating new protocol-level or code-level content
- Cost/complexity differences: Deferred per critique (question 8)
- Migration guide: Deferred per critique (question 9)
- Operational considerations: Reference existing operational documentation rather than creating new content
- Terminology: Ensure consistent use of "Hub Agent" vs "Agent" throughout
- Writing style: Technical textbook narrative - factual, direct, no flowery language
- Citations: All claims must reference source documentation via inline markdown links