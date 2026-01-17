# Scenario-Oriented Thinking: Anti-Patterns

> **Status**: 🟢 Design Complete  
> **Target Audience**: All (APOs, PAs, Developers)  
> **Purpose**: When NOT to use scenario-oriented thinking and common mistakes to avoid

---

## When NOT to Use Scenario-Oriented Thinking

### 1. Truly One-Off Scripts

**When:** A script that will genuinely never change, never be maintained, and never evolve.

**Why not:** The upfront structure (normative specs) is overhead if there's no evolution.

**Reality check:** Most "one-off" scripts become production. Most "simple" processes eventually need to evolve.

**Alternative:** Use scenario-oriented thinking anyway — the structure is investment in sustainability.

### 2. Single Person Owns Everything

**When:** One person owns the entire process end-to-end with no separation of concerns.

**Why not:** The three-specification model (normative, automation, deployment) adds coordination overhead when one person does everything.

**Reality check:** This is usually a temporary state. As processes grow, separation of concerns becomes valuable.

**Alternative:** Start with scenario-oriented thinking — it prepares for growth and separation of concerns.

### 3. Speed to First Deployment Is the Only Goal

**When:** You need something working immediately and long-term evolution doesn't matter.

**Why not:** Scenario-oriented thinking requires upfront structure (normative specs), which takes time.

**Reality check:** This is short-term thinking. Most processes need to evolve eventually.

**Alternative:** Use scenario-oriented thinking but start minimal — one scenario, basic normative spec, iterate.

### 4. No Evolution Pressure

**When:** The process is stable, regulations don't change, business rules don't change, and the team is static.

**Why not:** The value of scenario-oriented thinking is in sustainable evolution. If nothing changes, the structure may be overhead.

**Reality check:** This is rare. Most processes face evolution pressure eventually.

**Alternative:** Consider scenario-oriented thinking as insurance against future change.

---

## Common Mistakes

### Mistake 1: Creating Scenarios Based on Implementation Differences

**Anti-pattern:**
```
Scenario: "Automated Dispute"
Scenario: "Manual Dispute"
```

**Problem:** These are differentiated by HOW they're handled, not WHAT situation they represent.

**Correct approach:**
```
Scenario: "Standard Dispute" (may be automated or manual)
Scenario: "Fraud Dispute" (different situation entirely)
```

**Why it matters:** Scenarios should represent distinct situations, not different automation approaches. The automation approach is specified in the automation spec, not in the scenario name.

### Mistake 2: Treating Decision Rules as Separate Scenarios

**Anti-pattern:**
```
Scenario: "Low-Amount Dispute" (amount < $500)
Scenario: "Medium-Amount Dispute" (amount $500-$1000)
Scenario: "High-Amount Dispute" (amount > $1000)
```

**Problem:** These are decision rules within a scenario, not separate scenarios.

**Correct approach:**
```
Scenario: "Standard Dispute"
  normative:
    decision_criteria:
      - amount < $500: auto_resolve
      - amount $500-$1000: analyst_review
      - amount > $1000: senior_analyst_review
```

**Why it matters:** Scenarios are coarse-grained situations. Decision rules belong in the normative specification.

### Mistake 3: Mixing Normative and Automation Concerns

**Anti-pattern:**
```yaml
scenario: standard-dispute
automation:
  # Business rules mixed with implementation
  if amount < 1000:
    auto_approve()
  else:
    escalate_to_analyst()
```

**Problem:** Business rules (amount threshold, approval logic) are in the automation spec instead of normative spec.

**Correct approach:**
```yaml
# Normative spec
scenario: standard-dispute
normative:
  decision_criteria:
    - amount < $1000: Auto-approve if merchant history clean
    - amount >= $1000: Analyst review required

# Automation spec
scenario: standard-dispute
automation:
  application: dispute-handler
  runtime: chronoshift
  # Implementation derives from normative
```

**Why it matters:** Business rules should be in normative spec (owned by Process Architect). Automation spec should implement those rules (owned by Developer).

### Mistake 4: Skipping Normative Specification

**Anti-pattern:**
```
1. Jump straight to automation spec
2. Write code
3. Maybe document later (usually don't)
```

**Problem:** Without normative spec, there's no authoritative source of truth. Business rules end up in code.

**Correct approach:**
```
1. Design normative spec (Process Architect)
2. Get business validation
3. Derive automation from normative (Developer)
4. Configure deployment (Supervisor)
```

**Why it matters:** Normative is the source of truth. Automation derives from it, not the other way around.

### Mistake 5: Identifying Scenarios by "How We Handle It"

**Anti-pattern:**
```
"What's different about how we handle this?"
→ "We use BPM for this one, rules engine for that one"
→ Creates scenarios based on automation approach
```

**Problem:** Scenarios should be identified by WHAT situation they represent, not HOW they're handled.

**Correct approach:**
```
"What situation are we sensing?"
→ "Fraud indicator vs. standard dispute filing"
→ Creates scenarios based on distinct situations
```

**Why it matters:** Scenario-oriented thinking separates WHAT from HOW. The automation approach (BPM, rules, AI) is specified later in the automation spec.

### Mistake 6: One Scenario for Everything

**Anti-pattern:**
```
Scenario: "Dispute Resolution"
  (handles all disputes regardless of type)
```

**Problem:** Different situations (standard, fraud, high-value) have different roles, goals, and compliance requirements, but are forced into one scenario.

**Correct approach:**
```
Scenario: "Standard Dispute"
Scenario: "High-Value Dispute"
Scenario: "Fraud Dispute"
```

**Why it matters:** Each scenario should represent a distinct situation with its own normative specification. Combining different situations into one scenario loses the benefits of separation.

### Mistake 7: Normative Spec Becomes Stale

**Anti-pattern:**
```
1. Create normative spec
2. Implement automation
3. Business rules change
4. Update code directly
5. Forget to update normative spec
6. Normative and automation drift apart
```

**Problem:** If normative spec becomes stale, you lose the benefits of scenario-oriented thinking.

**Correct approach:**
```
1. Business rules change
2. Update normative spec first
3. Derive/update automation from normative
4. Validate automation matches normative
```

**Why it matters:** Normative is the source of truth. Changes should flow: normative → automation, not the other way around.

### Mistake 8: Over-Granular Scenarios

**Anti-pattern:**
```
Scenario: "Dispute Amount $0-$100"
Scenario: "Dispute Amount $100-$200"
Scenario: "Dispute Amount $200-$300"
...
```

**Problem:** These are parameter differences, not distinct situations.

**Correct approach:**
```
Scenario: "Standard Dispute"
  normative:
    decision_criteria:
      - amount ranges with different handling
```

**Why it matters:** Scenarios should be coarse-grained, recognizable business situations. Parameter differences are decision rules within a scenario.

---

## Decision Rule: When to Use vs. Not Use

### Use Scenario-Oriented Thinking When:

✅ Processes involve multiple roles and responsibilities  
✅ Business rules may change over time  
✅ Different situations require different handling  
✅ Compliance and audit requirements matter  
✅ AI-assisted automation is part of your strategy  
✅ Long-term evolution and maintainability matter  
✅ Business needs direct control over rules  

### Consider Alternatives When:

⚠️ Truly one-off script that will never change (rare)  
⚠️ Single person owns everything end-to-end (temporary state)  
⚠️ Speed to first deployment is the only goal (short-term thinking)  
⚠️ No evolution pressure (uncommon)  

**Even in these cases, consider:** The structure is investment in sustainability. Most processes eventually need to evolve.

---

## Related Documentation

- [Entry Point](./scenario-oriented-thinking.md) — Overview and reading guide
- [Core Concepts](./scenario-oriented-thinking-core.md) — Foundations and specifications
- [Adoption Guide](./scenario-oriented-thinking-adoption.md) — How to get started
- [Examples](./scenario-oriented-thinking-examples.md) — Concrete use cases

---

[← Back to Entry Point](./scenario-oriented-thinking.md)
