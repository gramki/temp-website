# 11.4 Handoff Context

When agents transfer work to other agents, context must transfer with it. Seer provides structured handoff context mechanisms that preserve state, maintain auditability, and ensure the receiving agent has what it needs to continue.

## The Handoff Problem

When Agent A transfers work to Agent B:

| Challenge | Consequence if Unaddressed |
|-----------|---------------------------|
| **Lost context** | Agent B starts from scratch |
| **Incomplete state** | Agent B makes decisions without full picture |
| **No audit trail** | Transfer is invisible to auditors |
| **Implicit assumptions** | Agent B inherits unstated assumptions |

## Handoff Context Records

Seer uses structured **HandoffContext** records (part of CAF Episodic Memory) to capture transfers:

```yaml
handoff_context:
  id: "hc-12345"
  case_id: "req-001"
  
  # Who is handing off
  source:
    agent_id: "dispute-triage-bot"
    agent_type: "employed_agent"
    scenario_id: "dispute-triage"
    
  # Who is receiving
  target:
    agent_id: "dispute-analyst-bot"
    agent_type: "employed_agent"
    scenario_id: "dispute-resolution"
    
  # What is being transferred
  context:
    # State summary
    summary: "Dispute pre-qualified for standard processing"
    
    # Key decisions made
    decisions_made:
      - decision_id: "dec-001"
        summary: "Dispute categorized as unauthorized transaction"
        
    # Open items
    open_items:
      - "Document verification pending"
      - "Customer callback scheduled"
      
    # Recommendations
    recommendations:
      - "Priority handling due to customer tier"
      
  # Metadata
  timestamp: "2026-01-10T14:30:00Z"
  reason: "Triage complete, escalating to analyst"
```

## Context Components

### Mandatory Elements

Every handoff must include:

| Element | Purpose |
|---------|---------|
| **Source agent** | Who is handing off |
| **Target agent** | Who is receiving |
| **Case binding** | Which case this relates to |
| **Timestamp** | When the handoff occurred |
| **Reason** | Why the handoff is happening |

### Recommended Elements

For complete context:

| Element | Purpose |
|---------|---------|
| **Summary** | Human-readable summary of state |
| **Decisions made** | What has been decided |
| **Open items** | What remains to be done |
| **Recommendations** | Suggestions for the receiver |
| **Entity references** | Key entities involved |

### Optional Elements

Depending on context:

| Element | Purpose |
|---------|---------|
| **Document references** | Relevant documents |
| **Conversation history** | Key conversation points |
| **Tool outputs** | Results of tool invocations |
| **Working hypotheses** | Current thinking (not yet decided) |

## Handoff Patterns

### Sequential Handoff

Linear transfer from one agent to the next:

```
Agent A → Agent B → Agent C
         ↓         ↓
      HandoffContext records
```

Each transition creates a new HandoffContext record.

### Parallel Handoff

One agent hands off to multiple:

```
Agent A → Agent B (document review)
       → Agent C (customer contact)
       → Agent D (policy check)
```

Separate HandoffContext for each receiver.

### Escalation Handoff

Agent escalates to human or senior agent:

```
Agent A (AI)
    ↓ cannot resolve
Agent B (Human Supervisor)
```

HandoffContext includes:
- Why escalation is needed
- What was tried
- Confidence levels

### Return Handoff

Work returns after specialized processing:

```
Agent A → Agent B (specialist) → Agent A
              ↓                    ↓
        HandoffContext      ReturnContext
```

Return includes specialist findings.

## Governance

### Immutability

Handoff records are immutable:
- Once created, cannot be modified
- Content-hashed for integrity
- Part of CAF audit trail

### Access Control

Handoff records follow access policies:

```yaml
access_policy:
  handoff_context:
    read:
      - source_agent
      - target_agent
      - supervisors
      - auditors
    write:
      - source_agent  # Only creator can write
```

### Retention

Handoff records retained per enterprise policy:
- Minimum 7 years for regulatory compliance
- Part of case evidence bundle

## Context Assembly Integration

The Context Assembly Engine uses handoff records:

```
Context Assembly
    ↓
Retrieves HandoffContext for current case
    ↓
Includes relevant handoff summaries in agent context
    ↓
Agent has full handoff history available
```

### Priority Handling

Multiple handoff records are prioritized:

| Source | Priority |
|--------|----------|
| Most recent handoff | Highest |
| Earlier handoffs | Context/history |
| Cross-workbench handoffs | Explicit inclusion required |

## Best Practices

### For Handing-Off Agents

| Practice | Rationale |
|----------|-----------|
| **Include summary** | Receiving agent may not read all details |
| **List open items** | Clear what remains |
| **State what was tried** | Avoid redundant work |
| **Reference decisions** | Don't repeat rationale |

### For Receiving Agents

| Practice | Rationale |
|----------|-----------|
| **Acknowledge receipt** | Auditable acceptance |
| **Review handoff context** | Understand prior state |
| **Continue audit trail** | Link new records to handoff |
| **Don't duplicate** | Reference prior decisions |

---

**References:**
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/episodic-memory-store/handoff-context.md`
*   `olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md`
