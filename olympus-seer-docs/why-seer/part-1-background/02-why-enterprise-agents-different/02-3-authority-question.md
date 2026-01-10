# 2.3 The Authority Question

> **Part 1, Section 2, Chapter 3**  
> **Outline Reference:** §2.3

---

## Purpose of This Chapter

This chapter addresses the fundamental question of agent authority: not whether an agent *can* act, but who authorized it to act and within what bounds. It introduces the concepts of authority ceilings, delegation models, and controlled autonomy.

---

## The Fundamental Distinction

The question for enterprise agents is not:

> *Can the agent perform this action?*

The question is:

> *Who authorized the agent to perform this action?*

This distinction separates **capability** from **authority**:

| Concept | Definition | Example |
|---------|------------|---------|
| **Capability** | What the agent can do | The agent can call the account closure API |
| **Authority** | What the agent is permitted to do | The agent is authorized to close accounts under $10,000 with documented reason |

An agent may have the capability to perform actions it lacks the authority to perform. Enterprise governance ensures that capability does not imply permission.

---

## Authority vs. Access Control

Traditional access control answers: *Can this service call this API?*

Authority control answers: *Is this agent permitted to make this business decision?*

| Access Control | Authority Control |
|----------------|-------------------|
| Binary: allowed/denied | Graduated: full/limited/none |
| Technical boundary | Business boundary |
| Permission to invoke | Permission to decide |
| Static configuration | Context-dependent |
| Service-level | Agent-level, decision-level |

Access control protects resources. Authority control governs decisions.

---

## The Four Components of Autonomy

For an agent to act autonomously, it requires all four components (Stevenson et al., 2023):

| Component | Definition | Enterprise Implication |
|-----------|------------|------------------------|
| **Authority** | The right to select or perform an action free from external control | Must be explicitly delegated |
| **Availability** | Being present and able to perform the activities | Must be operationally reliable |
| **Capability** | Having the knowledge, skills, and abilities to perform | Must be trained and equipped |
| **Capacity** | Having resources available under specific circumstances | Must have budget, compute, access |

**Autonomy = Authority + Availability + Capability + Capacity**

If any component is missing, the agent cannot act autonomously. Enterprise platforms must manage all four, but Authority is the governance concern—the others are operational concerns.

---

## Controlled Autonomy

Enterprise agents operate under **controlled autonomy**:

> The agent should act autonomously only to the extent that it is beneficial to the physical entity (e.g., human) who is responsible for controlling it.

This principle has several implications:

### Autonomy Is Bounded

Agents operate within explicit boundaries set by accountable humans. They do not acquire authority through capability alone.

### Authority Is Delegated, Not Assumed

Authority flows from humans to agents through explicit delegation, not through implicit capability.

### Humans Remain Accountable

Even when agents act autonomously, humans remain accountable for the outcomes. Controlled autonomy means the human's control is delegated, not abdicated.

### Authority Can Be Revoked

Delegated authority can be revoked at any time. Kill switches and authority revocation are not optional features—they are essential to controlled autonomy.

---

## Authority Ceilings

**Authority ceilings** define what an agent may NOT do, regardless of capability or request:

| Ceiling Type | Example | Enforcement |
|--------------|---------|-------------|
| **Value limits** | Cannot approve transactions over $10,000 | Hard limit, no exceptions |
| **Action prohibitions** | Cannot close accounts | Action blocked |
| **Scope limits** | Cannot operate outside assigned workbench | Context enforcement |
| **Temporal limits** | Cannot operate outside business hours | Time-based enforcement |

Authority ceilings are:
- **Immutable** at the enforcement level (cannot be overridden by the agent)
- **Layered** (policy → agent class → agent instance → request context)
- **Audited** (all ceiling checks are recorded)

### Ceiling Layers

Authority is constrained at multiple layers:

```
┌──────────────────────────────────────────────┐
│           ORGANIZATIONAL POLICY              │
│   "No AI agent may approve loans > $100K"    │
└──────────────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│              AGENT CLASS                     │
│   "Lending agents limited to $50K"           │
└──────────────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│           AGENT INSTANCE                     │
│   "This agent limited to $25K"               │
└──────────────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│          REQUEST CONTEXT                     │
│   "This request limited to $10K"             │
└──────────────────────────────────────────────┘
```

Each layer can narrow authority but never expand it. If organizational policy limits to $100K, no agent instance can exceed that limit regardless of its configuration.

---

## Delegation Models

Authority flows from humans to agents through delegation:

### Explicit Delegation

Authority is granted through formal specification:

```yaml
employmentSpec:
  delegatedBy: "chief-credit-officer"
  delegatedOn: "2024-03-15"
  authority:
    actions:
      - type: "loan-decision"
        ceiling: 25000
        conditions:
          - "credit-score >= 680"
          - "debt-ratio < 0.40"
    prohibited:
      - "modify-credit-policy"
      - "override-denial"
```

This specification:
- Names the delegating authority
- Records when delegation occurred
- Specifies what authority is granted
- Specifies what is prohibited
- Defines conditions on authority

### Chain of Delegation

Delegation chains trace authority back to its source:

```
Agent Authority
    ↑ delegated by
Employment Specification
    ↑ approved by
Chief Credit Officer
    ↑ authority granted by
Board Credit Policy
    ↑ approved by
Board of Directors
```

Every link in this chain is auditable.

### Delegation Constraints

Delegation is subject to constraints:

| Constraint | Description |
|------------|-------------|
| **Non-expansion** | Cannot delegate more authority than you have |
| **Traceability** | All delegations must be recorded |
| **Revocability** | All delegations can be revoked |
| **Temporal bounds** | Delegations may have expiration |

---

## The Immutability Principle

Enterprise agent platforms enforce an immutability principle for authority:

> **Guardrails defined at training cannot be relaxed at employment.**

This means:

- If a trained agent is restricted from an action, employment cannot enable it
- Employment can add restrictions but never remove them
- Authority ceilings are cumulative, never subtractive

This principle creates defensible boundaries:

| Layer | Can Restrict | Can Enable |
|-------|--------------|------------|
| **Training** | Yes | Yes (base capability) |
| **Employment** | Yes | No (cannot override training) |
| **Request Context** | Yes | No (cannot override employment) |

---

## Kill Switches

Authority must be revocable instantly:

### What Kill Switches Do

| Action | Description |
|--------|-------------|
| **Authority revocation** | Agent loses permission to act (not just process termination) |
| **Immediate effect** | No pending actions complete after revocation |
| **Platform-controlled** | Independent of the agent's own code or state |
| **Audited** | All revocations are recorded with reason |

### When Kill Switches Are Used

| Scenario | Response |
|----------|----------|
| **Unexpected behavior** | Revoke authority pending investigation |
| **Policy violation** | Revoke authority, escalate for review |
| **Security incident** | Revoke authority, preserve evidence |
| **Regulatory request** | Revoke authority, produce records |

Kill switches are not punishment—they are control mechanisms that preserve human oversight.

---

## Common Misconceptions

### "Access control is sufficient"

Access control prevents unauthorized API calls. Authority control prevents unauthorized decisions. An agent may have access to an API but lack authority to make the business decision that would trigger that API call.

### "We can trust the agent to stay within bounds"

Trust is not a governance mechanism. Agents may produce unexpected outputs due to prompt injection, model drift, or edge cases. Authority ceilings enforce bounds regardless of agent behavior.

### "Authority limits reduce agent usefulness"

Authority limits define the agent's scope—within that scope, the agent operates with full capability. Limits create clarity about what the agent can and cannot do, enabling trust within bounds.

### "Kill switches are emergency measures"

Kill switches may be used for routine authority management—not just emergencies. Revoking authority pending investigation, adjusting authority based on performance, or transitioning authority during upgrades are all normal uses.

---

## Cross-References

- **Chapter 2.2** (The Accountability Gap) establishes why authority must trace to accountable humans
- **Chapter 2.4** (The Irreversibility Problem) explains why authority limits matter for consequential actions
- **Section 5.1** (The Agent Lifecycle) describes how authority is configured through Training and Employment specs
- **Part 2, Section 3** (Identity & Authority in Seer) shows how Seer implements authority models

---

## Key Takeaways

1. The authority question is not "can the agent act?" but "who authorized the agent to act?"

2. Authority is distinct from capability—capability enables action; authority permits it.

3. Controlled autonomy means agents act within explicit bounds set by accountable humans.

4. Authority ceilings define what agents may never do, regardless of capability.

5. Authority is delegated through explicit specification, creating auditable chains.

6. The immutability principle ensures training guardrails cannot be relaxed at employment.

7. Kill switches enable instant authority revocation—an essential control mechanism.

---

**Reference:** `aosm-meta-model/agent-oriented-system.md` (Authority and Autonomy sections), `aosm-meta-model/raw-trained-employed-agents.md`
