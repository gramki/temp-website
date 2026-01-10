# 5.3 Token Budgeting & Truncation

LLM context windows have finite token limits. The Context Assembly Engine must allocate budget across context sections and apply intelligent truncation when limits are exceeded. Poor budgeting leads to lost information, degraded reasoning, or excessive costs.

## Why Token Budgeting Matters

| Problem | Consequence |
|---------|-------------|
| **No budget** | Context exceeds model limits; request fails |
| **Uniform truncation** | Critical information lost randomly |
| **No prioritization** | Constraints deprioritized vs. verbose facts |
| **No provenance** | Can't explain what was included/excluded |

## Budget Allocation Strategy

### Fixed vs. Flexible Sections

Some sections have fixed allocations; others share flexible budget:

```yaml
budget_strategy:
  total_tokens: 8000
  
  fixed_sections:
    constraints: 500      # Always present, critical
    goal: 200             # Always present, defines task
    
  flexible_sections:      # Share remaining 7300 tokens
    ground_truth_facts:
      priority: 1         # Highest
      min: 1000
      max: 3000
    recent_episodes:
      priority: 2
      min: 500
      max: 2000
    procedures:
      priority: 3
      min: 500
      max: 1500
    preferences:
      priority: 4
      min: 100
      max: 500
    working_state:
      priority: 2
      min: 500
      max: 1500
```

### Allocation Algorithm

1. Allocate fixed sections first
2. Distribute remaining budget by priority
3. Each section gets at least its minimum
4. Higher priority sections get more of the remainder
5. Cap at maximum even if budget remains

```python
def allocate_budget(total, fixed, flexible):
    remaining = total - sum(fixed.values())
    
    # Ensure minimums first
    for section in sorted(flexible, key=lambda s: s.priority):
        allocation[section] = section.min
        remaining -= section.min
    
    # Distribute remainder by priority
    for section in sorted(flexible, key=lambda s: s.priority):
        additional = min(remaining, section.max - section.min)
        allocation[section] += additional
        remaining -= additional
        if remaining <= 0:
            break
            
    return allocation
```

## Truncation Strategies

When content exceeds allocated budget, the engine applies truncation:

### Strategy 1: Relevance-Based

Keep highest relevance content:

```yaml
truncation:
  strategy: relevance
  section: ground_truth_facts
  budget: 2500
  candidates: 15 chunks
  
  result:
    included: 8 chunks (highest relevance scores)
    excluded: 7 chunks (below threshold)
    threshold_applied: 0.75
```

### Strategy 2: Recency-Based

Keep most recent content:

```yaml
truncation:
  strategy: recency
  section: recent_episodes
  budget: 1500
  candidates: 10 episodes
  
  result:
    included: 4 most recent episodes
    excluded: 6 older episodes
```

### Strategy 3: Summarization

Compress content while preserving meaning:

```yaml
truncation:
  strategy: summarization
  section: conversation_history
  original_tokens: 3000
  budget: 1000
  
  result:
    summarized_to: 950 tokens
    summary: "Customer disputed $450 charge at ACME Store. 
              Merchant error confirmed via transaction service.
              Customer requested full refund."
```

### Strategy 4: Hierarchical

Keep structure, truncate details:

```yaml
truncation:
  strategy: hierarchical
  section: procedures
  budget: 1500
  
  result:
    kept: step names and key actions
    truncated: detailed sub-steps and examples
    
    example:
      original: "Step 1: Verify transaction details
                 1.1 Check transaction ID format
                 1.2 Verify merchant code
                 1.3 Confirm settlement status..."
      truncated: "Step 1: Verify transaction details"
```

## Section-Specific Defaults

| Section | Default Strategy | Rationale |
|---------|------------------|-----------|
| **Constraints** | Never truncate | Critical for safety |
| **Goal** | Never truncate | Defines the task |
| **Ground Truth Facts** | Relevance-based | Keep most relevant facts |
| **Recent Episodes** | Recency + relevance | Balance recent and relevant |
| **Preferences** | Importance-based | Keep most impactful preferences |
| **Procedures** | Hierarchical | Keep structure, trim details |
| **Working State** | Recency-based | Keep recent tool results |

## Token Counting

Accurate token counting is essential:

```python
# Token counting per model family
token_count = tokenizer.count(content)

# Model-specific limits
model_limits = {
    "gpt-4o": 128000,
    "claude-3.5-sonnet": 200000,
    "bedrock-claude": 200000
}

# Reserve buffer for output
usable_context = model_limit - output_reservation
```

## Audit Trail

All budget decisions are logged:

```yaml
budget_audit:
  assembly_id: "ctx-assembly-789"
  
  allocation:
    total_available: 8000
    fixed_used: 700
    flexible_allocated:
      ground_truth_facts: 2500
      recent_episodes: 1500
      procedures: 1500
      preferences: 300
      working_state: 1500
    total_used: 8000
    
  truncation_applied:
    - section: ground_truth_facts
      strategy: relevance
      original_items: 15
      included_items: 8
      excluded_items: 7
      
    - section: recent_episodes
      strategy: recency
      original_items: 10
      included_items: 4
      excluded_items: 6
      
  items_excluded:
    - item_id: "kb-chunk-456"
      reason: "Below relevance threshold (0.72 < 0.75)"
    - item_id: "episode-789"
      reason: "Exceeded recency limit (older than 4 most recent)"
```

## Dynamic Budget Adjustment

Budget can be adjusted based on task complexity:

```yaml
dynamic_adjustment:
  base_budget: 8000
  
  adjustments:
    - condition: "high_complexity_decision"
      increase_section: ground_truth_facts
      by: 500
      
    - condition: "conversation_continuation"
      increase_section: working_state
      by: 500
      
    - condition: "simple_query"
      reduce_all_flexible: 50%
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-3-context-compilation.md`
