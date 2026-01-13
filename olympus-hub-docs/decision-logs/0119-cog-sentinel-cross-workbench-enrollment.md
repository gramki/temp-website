# ADR-0119: COG Sentinel Cross-Workbench Enrollment

**Status**: Accepted  
**Date**: 2026-01-14  
**Category**: seer, hub-integration

---

## Context

With the introduction of COGW workbenches (ADR-0118), we need a mechanism for COG Sentinels to:

1. **Target multiple workbenches** — Which workbenches should the sentinel monitor?
2. **Enroll automatically** — How does the sentinel get enrolled in requests?
3. **Sync specifications** — How do target workbenches know about the sentinel?
4. **Control locally** — How do target workbench admins manage the sentinel?

### Requirements

1. Pattern-based workbench targeting (support wildcards)
2. Automatic enrollment in matching workbenches
3. Read-only spec visibility in target workbenches
4. Local enable/disable without spec modification
5. Automatic sync when COG Sentinel changes

---

## Decision

### 1. cogSpec for Pattern-Based Targeting

COG Sentinels define target workbenches via `cogSpec` in `SentinelScenarioDeploymentSpec`:

```yaml
cogSpec:
  workbench_patterns:
    - pattern: "production-*"
      action: allow
    - pattern: "production-dev"
      action: disallow
    - pattern: "*"
      action: allow
```

### 2. Apache-Style Sequential Pattern Matching

Pattern evaluation follows Apache webserver-style sequential evaluation:

1. **Evaluate in order** — Top to bottom
2. **First match wins** — Stop on first matching pattern
3. **Default deny** — If no pattern matches, workbench not targeted
4. **Wildcard support** — `*` matches any sequence of characters

### 3. Read-Only Spec Sync to Target Workbenches

COGW Operator syncs specs to target workbenches:

- **Same CRD types** — Standard SentinelScenarioSpec CRDs
- **Read-only annotation** — `sentinel.olympus.io/read-only: "true"`
- **Source annotation** — `sentinel.olympus.io/cog-sentinel-source: "<cogw>/<sentinel>"`
- **Validation enforcement** — Reject modifications to read-only specs

### 4. Local Enable/Disable Control

Target workbench admins can enable/disable COG Sentinels locally:

| Action | Allowed | Mechanism |
|--------|---------|-----------|
| Enable | ✅ | Sentinel Levers (local) |
| Disable | ✅ | Sentinel Levers (local) |
| Modify | ❌ | Rejected (read-only) |
| Delete | ❌ | Rejected (managed by COGW Operator) |

### 5. Automatic Sync on Changes

When COG Sentinel changes in COGW:

1. COGW Operator detects change
2. Re-evaluates cogSpec patterns
3. Syncs to matching workbenches
4. Removes from non-matching workbenches

---

## Alternatives Considered

### 1. Full Spec Copy (Not Read-Only)

Copy full specs to target workbenches with local modification allowed.

**Rejected because:**
- **Drift risk** — Local modifications create inconsistency
- **Governance violation** — Defeats purpose of centralized governance
- **Sync complexity** — How to handle conflicts on update?
- **Ownership unclear** — Is the spec owned by COGW or target?

### 2. Reference-Only (No Local Specs)

Target workbenches don't have specs; only Signal Exchange registration.

**Rejected because:**
- **No visibility** — Admins can't see what's monitoring them
- **No local control** — Can't disable in specific workbenches
- **Discovery issues** — Hard to audit what sentinels are active
- **Inconsistent UX** — Different from regular sentinels

### 3. Manual Enrollment

COGW admins manually select target workbenches (no patterns).

**Rejected because:**
- **Doesn't scale** — Must update for every new workbench
- **Error-prone** — Easy to miss workbenches
- **Operational burden** — Ongoing maintenance required
- **No automation** — Can't automatically include new workbenches

### 4. Regex Patterns Instead of Wildcards

Use full regex for pattern matching.

**Rejected because:**
- **Complexity** — Regex is powerful but error-prone
- **Familiarity** — Wildcards are more familiar to admins
- **Overkill** — Workbench names don't need regex power
- **Debugging** — Harder to understand matching behavior

---

## Consequences

### Positive

1. **Flexible targeting** — Patterns cover common use cases
2. **Familiar model** — Apache-style matching is well-understood
3. **Visible and auditable** — Target workbenches see what's monitoring them
4. **Local autonomy** — Admins can disable without breaking governance
5. **Automatic sync** — Changes propagate without manual intervention

### Negative

1. **Operator complexity** — COGW Operator must watch and sync across workbenches
2. **Read-only enforcement** — Need validation webhook for enforcement
3. **Pattern ordering matters** — First match wins can be confusing

### Neutral

1. **Two-level status** — Global (COGW) and local (target) status both apply
2. **Same CRD types** — Reuses existing specs, just with annotations

---

## Implementation Notes

### Pattern Matching Function

```python
def evaluate_patterns(workbench_name, patterns):
    """Apache-style sequential pattern evaluation."""
    for rule in patterns:
        if wildcard_match(workbench_name, rule.pattern):
            return rule.action == "allow"
    return False  # Default deny

def wildcard_match(name, pattern):
    """Simple wildcard matching where * matches any sequence."""
    import fnmatch
    return fnmatch.fnmatch(name, pattern)
```

### Read-Only Validation Webhook

```python
def validate_sentinel_spec_update(old_spec, new_spec, user):
    # Check if read-only
    if old_spec.annotations.get("sentinel.olympus.io/read-only") == "true":
        # Allow if update is from COGW Operator
        if user.is_service_account("cogw-operator"):
            return ValidationSuccess()
        
        # Allow status changes via Sentinel Levers
        if only_status_changed(old_spec, new_spec):
            return ValidationSuccess()
        
        # Reject other changes
        return ValidationError("Cannot modify read-only COG Sentinel spec")
    
    return ValidationSuccess()
```

---

## Related

- [ADR-0118: Cognitive Operations Governance Workbench Type](./0118-cognitive-operations-governance-workbench-type.md) — COGW workbench type
- [ADR-0120: COGW Operator Subscription Scope](./0120-cogw-operator-subscription-scope.md) — Operator scope
- [COG Sentinel Specification](../../olympus-seer-docs/seer-design/subsystems/cognitive-operations-governance-workbench/cog-sentinel-specification.md) — Detailed specification
