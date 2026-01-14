# Agent Levers

> **Category:** DevOps and Lifecycle  
> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-15

---

## Overview

Agent Levers provide **runtime control mechanisms** for agents at different lifecycle stages (Raw, Trained, Employed) and for Sentinels. Levers enable enable/disable, suspend/resume, and override operations without modifying agent specifications. They provide operational controls that affect agent execution while maintaining auditability and authorization.

---

## Ontology Context

### Relationship to Ontology

Agent Levers implement the **Directability** principle from AOSM:

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|-------------|
| **Directability** | Levers enable human control over agent behavior | Humans can direct agents via levers |
| **Controlled Autonomy** | Levers enforce autonomy boundaries | Levers can narrow agent capabilities |
| **RASCI Accountability** | Lever operations require authorization | Accountable humans can operate levers |
| **OPD (Observability, Predictability, Directability)** | Directability component implemented via levers | Levers provide runtime directability |

### Gap This Fills

The AOSM ontology defines Directability but doesn't specify how to implement runtime controls that don't require specification changes. Agent Levers fill this gap by providing:

1. **Runtime Controls**: Enable/disable, suspend/resume without spec changes
2. **Override Operations**: Fine-grained control over agent capabilities
3. **Authorization Model**: Role-based authorization for lever operations
4. **Audit Trail**: All lever operations recorded for compliance
5. **Unified Pattern**: Consistent lever model across agent types and sentinels

---

## Definition

**Agent Levers** are runtime control mechanisms that enable operational control over agents and sentinels without modifying their specifications. Levers provide enable/disable, suspend/resume, and override operations with authorization, auditability, and immediate effect.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Per-agent (Raw, Trained, Employed) or per-sentinel |
| **Lifecycle** | Available throughout agent/sentinel lifecycle; operations recorded in audit trail |
| **Ownership** | Agent Reliability Engineer (ARE) for operational levers; supervisors for business levers |
| **Multiplicity** | Multiple levers per agent/sentinel; different levers for different control aspects |

---

## Rationale

### Why This Design?

**Unified Lever Pattern**:
- Consistent lever model across Raw, Trained, Employed agents and Sentinels
- Same authorization and audit patterns
- Reduces cognitive load for operators

**Runtime Control Without Spec Changes**:
- Levers affect execution, not specifications
- Enables rapid response to incidents
- No need to modify and redeploy specs

**Authorization and Audit**:
- All lever operations require authorization
- Complete audit trail for compliance
- Supports regulatory requirements

**Fine-Grained Control**:
- Enable/disable for on/off control
- Suspend/resume for temporary stops
- Override operations for capability adjustments

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Spec Modification Only** | Too slow for operational response; levers provide immediate control |
| **Single Lever Type** | Different control needs require different lever types |
| **No Authorization** | Security risk; authorization required for all lever operations |

### Related ADRs

| ADR | Decision |
|-----|----------|
| *To be added* | *Agent lever architecture decisions* |

---

## Structure

### Key Attributes

```yaml
# Conceptual lever operation structure
lever_operation:
  lever_type: enable | disable | suspend | resume | override
  target:
    type: raw_agent | trained_agent | employed_agent | sentinel
    ref: string  # Agent/sentinel ID
  
  operation:
    action: string  # Specific action (e.g., "reduce-ceiling", "revoke-tool")
    parameters: object  # Action-specific parameters
  
  context:
    reason: string
    initiator: string  # user:...
    timestamp: timestamp
    duration: integer  # Optional: auto-resume after duration
  
  authorization:
    required_roles: [string]
    approved_by: string  # Optional: dual control
  
  audit:
    recorded_in: string  # CAF
    compliance_tags: [string]
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Enabled** | Agent/sentinel active and operating | → Disabled, → Suspended |
| **Disabled** | Agent/sentinel disabled (not operating) | → Enabled |
| **Suspended** | Agent/sentinel temporarily suspended | → Enabled (Resume), → Disabled |
| **Overridden** | Agent capabilities modified via override | → Enabled (Remove override) |

---

## Behavior

### How It Works

#### Enable/Disable Flow

```
1. Lever operation requested (enable/disable)
2. Authorization validated (initiator has required role)
3. Agent/sentinel state updated
4. Execution started/stopped (if applicable)
5. Audit record created
6. Operation complete
```

#### Suspend/Resume Flow

```
1. Suspend operation requested
2. Authorization validated
3. Agent/sentinel execution suspended (pods scaled to zero or network isolated)
4. State updated to Suspended
5. Audit record created
6. (Later) Resume operation requested
7. Execution resumed (pods scaled up or network isolation removed)
8. State updated to Enabled
9. Audit record created
```

#### Override Flow

```
1. Override operation requested (e.g., reduce ceiling, revoke tool)
2. Authorization validated
3. Agent capabilities modified (without spec change)
4. Override applied to runtime
5. State updated to Overridden
6. Audit record created
7. (Later) Override removed
8. Agent capabilities restored
9. State updated to Enabled
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| **Agent Levers Service** | → | Executes lever operations for Employed Agents |
| **Trained Agent Levers** | → | Executes lever operations for Trained Agents |
| **Sentinel Levers** | → | Executes lever operations for Sentinels |
| **Agent Runtime** | → | Suspends/resumes agent execution |
| **Agent Directory** | ↔ | Updates agent/sentinel state |
| **CAF (Cognitive Audit Fabric)** | → | Records lever operations |
| **Cipher IAM** | → | Validates authorization for lever operations |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Authorization Required** | All lever operations require authorization |
| **Audit Required** | All lever operations must be recorded in CAF |
| **Narrowing-Only Overrides** | Override operations can only narrow, never expand capabilities |
| **Reversibility** | Enable/disable and suspend/resume are reversible |
| **State Consistency** | Lever state must be consistent across all systems |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Rapid Response** | Immediate control without spec changes |
| ✅ **Unified Pattern** | Consistent lever model across agent types |
| ✅ **Fine-Grained Control** | Different levers for different control needs |
| ✅ **Authorization** | Role-based authorization ensures security |
| ✅ **Audit Trail** | Complete record of lever operations |
| ✅ **Operational Flexibility** | Enables operational response to incidents |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **State Management** | Lever state must be synchronized across systems |
| ⚠️ **Authorization Complexity** | Clear roles and approval workflows |
| ⚠️ **Override Complexity** | Override operations require careful design |
| ⚠️ **Audit Overhead** | Audit recording adds latency; acceptable for operational controls |

---

## Examples

### Example 1: Enable/Disable Agent

**Use Case**: Temporarily disable agent for maintenance

```yaml
# Lever Operation
apiVersion: seer.olympus.io/v1
kind: AgentLeverAction
metadata:
  name: disable-fraud-analyst-001
spec:
  lever_type: disable
  target:
    type: employed_agent
    ref: "fraud-analyst-acme-retail"
  reason: "Scheduled maintenance window"
  initiator: "user:ops-team@acme.com"
```

**Behavior**: Agent disabled; execution stopped. Can be re-enabled without spec changes.

---

### Example 2: Suspend/Resume Agent

**Use Case**: Temporarily suspend agent for investigation

```yaml
# Suspend Operation
apiVersion: seer.olympus.io/v1
kind: AgentLeverAction
metadata:
  name: suspend-fraud-analyst-001
spec:
  lever_type: suspend
  target:
    type: employed_agent
    ref: "fraud-analyst-acme-retail"
  reason: "Investigating anomalous behavior"
  initiator: "user:security-team@acme.com"
  duration: 3600  # Auto-resume after 1 hour
```

**Behavior**: Agent suspended; pods scaled to zero. Can resume after investigation.

---

### Example 3: Override - Reduce Ceiling

**Use Case**: Reduce agent authority ceiling without spec change

```yaml
# Override Operation
apiVersion: seer.olympus.io/v1
kind: AgentLeverAction
metadata:
  name: reduce-ceiling-fraud-analyst-001
spec:
  lever_type: override
  target:
    type: employed_agent
    ref: "fraud-analyst-acme-retail"
  operation:
    action: reduce-ceiling
    parameters:
      maxSingleTransaction: 1000  # Was: 5000
      maxDailyTotal: 10000        # Was: 50000
  reason: "Reduce authority pending investigation"
  initiator: "user:supervisor@acme.com"
```

**Behavior**: Agent authority ceilings reduced. Override can be removed to restore original ceilings.

---

### Example 4: Sentinel Enable/Disable

**Use Case**: Enable sentinel for monitoring

```yaml
# Sentinel Lever Operation
apiVersion: seer.olympus.io/v1
kind: SentinelLeverAction
metadata:
  name: enable-stuck-agent-detector
spec:
  lever_type: enable
  target:
    type: sentinel
    ref: "stuck-agent-detector"
  reason: "Enable monitoring for agent health"
  initiator: "user:cos@acme.com"
```

**Behavior**: Sentinel enabled; starts monitoring agent sessions.

---

## Implementation Notes

### For Developers

- **Lever Service API**: Use appropriate lever service API (Agent Levers, Trained Agent Levers, Sentinel Levers)
- **Authorization**: Implement role-based authorization for lever operations
- **Audit Integration**: All lever operations must be recorded in CAF
- **State Management**: Ensure lever state is synchronized across systems

### For Operators

- **Lever Authorization**: Understand required roles for different lever operations
- **Lever Types**: Know when to use enable/disable vs. suspend/resume vs. override
- **Audit Review**: Review lever operation audit trail regularly
- **Recovery Procedures**: Document recovery procedures for different lever scenarios

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Kill Switch & Emergency Controls](./kill-switch-emergency-controls.md) | Kill switch is a type of agent lever |
| [Agent Lifecycle](./agent-lifecycle.md) | Levers available throughout agent lifecycle |
| [Agent Runtime](./agent-runtime.md) | Runtime executes suspend/resume operations |
| [Sentinels](./sentinels.md) | Sentinels have their own lever service |

---

## References

- [Agent Levers Service](../subsystems/agent-lifecycle-manager/agent-levers-service.md) — Employed Agent levers
- [Trained Agent Levers](../subsystems/trained-agent-lifecycle-manager/trained-agent-levers.md) — Trained Agent levers
- [Sentinel Levers](../subsystems/seer-sentinels/sentinel-levers.md) — Sentinel levers
- [Kill Switch & Emergency Controls](./kill-switch-emergency-controls.md) — Kill switch as lever type

---

*Agent Levers provide runtime control mechanisms for agents and sentinels, enabling operational response to incidents while maintaining authorization, auditability, and specification integrity.*
