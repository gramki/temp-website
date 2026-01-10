# 2.1 Consumer vs. Business vs. Enterprise Agents

> **Part 1, Section 2, Chapter 1**  
> **Outline Reference:** §2.1

---

## Purpose of This Chapter

This chapter establishes the categorical distinctions between consumer, business, and enterprise agents. These distinctions are not matters of scale or sophistication but of fundamental design requirements driven by different contexts, stakeholders, and accountability models.

---

## The Three Agent Categories

AI agents operate in different contexts that impose different requirements:

| Category | Primary Goal | Who Bears Risk |
|----------|--------------|----------------|
| **Consumer Agent** | Delight the user | User accepts risk |
| **Business Agent** | Solve a task | Business accepts risk |
| **Enterprise Agent** | Act with delegated authority | Organization must defend decisions |

These categories are not hierarchy levels—enterprise agents are not "better" consumer agents. They are different categories designed for different purposes.

---

## Dimensional Comparison

The following dimensions distinguish the three categories:

### Primary Goal

| Consumer | Business | Enterprise |
|----------|----------|------------|
| Delight the user | Solve a task | Act with delegated authority |
| Optimize for satisfaction | Optimize for efficiency | Optimize for defensibility |
| Success = user returns | Success = task complete | Success = outcome withstands scrutiny |

**Consumer agents** aim to please. A personal assistant that helps plan a vacation succeeds when the user enjoys the interaction and finds the suggestions helpful.

**Business agents** aim to complete work. An agent that schedules meetings succeeds when meetings are scheduled correctly and efficiently.

**Enterprise agents** aim to act correctly on behalf of the organization. A lending agent that evaluates loan applications succeeds when decisions are correct, defensible, and traceable to the policies and authority that governed them.

### Accountability Model

| Consumer | Business | Enterprise |
|----------|----------|------------|
| User accepts risk | Business accepts risk | Organization must defend decisions |
| Caveat emptor | Business judgment | Regulatory scrutiny |
| Personal consequences | Business consequences | Legal/regulatory consequences |

**Consumer agents** operate with implicit user consent. If a recommendation is wrong, the user bears the consequence.

**Business agents** operate under business judgment. If a task fails, the business absorbs the cost.

**Enterprise agents** operate under organizational accountability. If a decision is challenged, the organization must produce evidence of why it was made, who authorized it, and that appropriate policies were followed.

### Memory Requirements

| Consumer | Business | Enterprise |
|----------|----------|------------|
| Personalization | Session continuity | Institutional learning |
| User preferences | Task context | Organizational knowledge |
| Short-term retention | Session-scoped | Multi-year retention |

**Consumer agents** remember for personalization—favorite topics, communication style, past requests.

**Business agents** remember for session continuity—what was discussed, what decisions were made, what context applies.

**Enterprise agents** remember for institutional purposes—what happened and why, what was learned, how precedent informs future decisions. This memory must be governed for compliance, isolated for privacy, and retained for audit.

### Action Stakes

| Consumer | Business | Enterprise |
|----------|----------|------------|
| Low stakes | Medium stakes | Consequential, often irreversible |
| Undo usually possible | Retry usually possible | Actions may be permanent |
| User tolerance for error | Business tolerance for error | No tolerance for certain errors |

**Consumer agents** operate where stakes are typically low. Wrong restaurant recommendation? User chooses differently next time.

**Business agents** operate where stakes are moderate. Meeting scheduled incorrectly? Reschedule with apology.

**Enterprise agents** operate where stakes may be high. Loan denied? Customer relationship damaged, potential regulatory scrutiny. Account closed? Irreversible action with documentation requirements.

### Oversight Requirements

| Consumer | Business | Enterprise |
|----------|----------|------------|
| Optional | Light | Mandatory, regulatory-driven |
| User may review | Supervisor may review | Auditor will review |
| No formal requirements | Policy compliance | Regulatory compliance |

**Consumer agents** may operate without oversight. Users can choose to review or not.

**Business agents** typically have light oversight—supervisors may spot-check or review exceptions.

**Enterprise agents** face mandatory oversight. Regulators require demonstrable human oversight, documented review processes, and evidence of governance.

### Lifecycle Duration

| Consumer | Business | Enterprise |
|----------|----------|------------|
| Ephemeral | Managed | Multi-year, audited |
| Version when convenient | Version for features | Version for compliance |
| Retire freely | Retire with transition | Retire with evidence |

**Consumer agents** can be updated or retired without formal process.

**Business agents** have managed lifecycles—new versions, deprecation notices, migration support.

**Enterprise agents** have audited lifecycles. Every version that operated in production must be traceable. Retirement requires evidence that no pending obligations depend on the agent.

---

## Summary Matrix

| Dimension | Consumer | Business | Enterprise |
|-----------|----------|----------|------------|
| **Primary Goal** | Delight the user | Solve a task | Act with delegated authority |
| **Accountability** | User accepts risk | Business accepts risk | Organization must defend decisions |
| **Memory** | Personalization | Session continuity | Institutional learning |
| **Actions** | Low stakes | Medium stakes | Consequential, often irreversible |
| **Oversight** | Optional | Light | Mandatory, regulatory-driven |
| **Lifecycle** | Ephemeral | Managed | Multi-year, audited |

---

## Why These Distinctions Matter

### Design Implications

Each category requires different platform capabilities:

| Category | Platform Requirements |
|----------|----------------------|
| **Consumer** | User experience, personalization, responsiveness |
| **Business** | Task completion, efficiency, integration |
| **Enterprise** | Governance, audit, authority, override |

Attempting to operate an enterprise agent on a consumer or business platform creates gaps in accountability, audit, and control.

### Evaluation Implications

When evaluating AI platforms, the first question should be: *What category of agents will we operate?*

- Consumer platforms excel at user experience but lack governance
- Business platforms provide task automation but lack regulatory-grade audit
- Enterprise platforms provide governance at the cost of additional complexity

### Migration Implications

Organizations often begin with consumer or business agents and later need enterprise capabilities. This migration is not incremental—it requires fundamental changes to how agents are designed, deployed, and governed.

---

## Common Misconceptions

### "Enterprise agents are just business agents at scale"

Scale is not the distinguishing factor. A business agent handling 10 million tasks remains a business agent. An enterprise agent handling 100 tasks that require regulatory defensibility is an enterprise agent. The distinction is accountability model, not volume.

### "We can add governance later"

Governance cannot be retrofitted effectively. An agent designed without accountability, authority, and audit considerations cannot have these properties added after deployment. The architecture must be designed from first principles around these requirements.

### "Our agents are low-risk, so we don't need enterprise capabilities"

Risk assessment often underestimates downstream effects. Agents that "only" provide information may inform consequential decisions. Agents that "only" route requests may determine service access. The accountability question applies whenever agents participate in processes with consequential outcomes.

### "Consumer AI platforms are just for consumers"

Consumer AI platforms serve consumer use cases. Many organizations attempt to use consumer-grade platforms for enterprise use cases, creating governance gaps that become apparent only under scrutiny.

---

## Practical Implications

### For New Agent Projects

Begin with the accountability question: *Who is accountable when this agent makes a decision?*

- If the user is accountable → Consumer category
- If the business unit is accountable → Business category
- If the organization must defend the decision → Enterprise category

### For Platform Selection

Match platform capabilities to agent category:

- Consumer agents → Consumer platforms
- Business agents → Business platforms  
- Enterprise agents → Enterprise platforms

Mismatches create risk: enterprise agents on consumer platforms lack necessary governance; consumer agents on enterprise platforms incur unnecessary complexity.

### For Governance Planning

Design governance commensurate with category:

- Consumer: User-facing transparency
- Business: Business process controls
- Enterprise: Regulatory-grade audit and evidence

---

## Cross-References

- **Chapter 2.2** (The Accountability Gap) explores accountability requirements in depth
- **Chapter 2.3** (The Authority Question) addresses how authority flows to agents
- **Section 1** (What Is an Enterprise Agent Platform?) describes the platform requirements for enterprise agents
- **Appendix C** (AOSM Foundations) provides theoretical grounding for agent categorization

---

## Key Takeaways

1. Consumer, business, and enterprise agents are categorically different, not points on a spectrum.

2. The distinguishing factors are accountability model, not scale or sophistication.

3. Enterprise agents require governance, audit, and authority models that consumer and business agents do not.

4. Platform selection must match agent category—mismatches create governance gaps.

5. Governance cannot be retrofitted; it must be designed from first principles.

---

**Reference:** `aosm-meta-model/agent-oriented-system.md`
