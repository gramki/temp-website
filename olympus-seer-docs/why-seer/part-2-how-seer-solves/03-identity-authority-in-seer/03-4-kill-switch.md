# 3.4 Kill Switch

The kill switch is a critical safety mechanism that provides instant authority revocation for enterprise agents. Unlike process termination, which merely stops execution, the kill switch revokes the agent's authority to act—a semantic-level intervention that is independent of infrastructure.

## Kill Switch vs. Process Termination

| Aspect | Process Termination | Kill Switch |
|--------|---------------------|-------------|
| **What it does** | Stops the running container | Revokes agent's authority |
| **Scope** | Single instance | All instances of the agent |
| **Effect** | Process restarts with same authority | Agent cannot act even if restarted |
| **Control** | Infrastructure team | Platform/Security team |
| **Speed** | Depends on orchestrator | Immediate (policy-level) |

A killed process with unchanged authority will resume acting when restarted. A kill switch ensures the agent cannot act regardless of infrastructure state.

## How the Kill Switch Works

### Authority Revocation

When the kill switch is activated:

1. **Immediate Policy Update:** Agent's authority is revoked in Cipher IAM
2. **PEP Enforcement:** All Policy Enforcement Points immediately reject the agent's requests
3. **Token Invalidation:** All outstanding tokens for the agent are invalidated
4. **Audit Recording:** Kill switch activation is recorded in CAF

### Propagation

Authority revocation propagates through all channels:

```
Kill Switch Activated
    ↓
Cipher IAM: Agent marked as revoked
    ↓ (seconds)
All PEPs: Reject agent's requests
    ↓ (seconds)
External Systems (via Cipher SDK): Reject agent's credentials
    ↓
Audit: Full record of revocation
```

### In-Flight Operations

When the kill switch is activated, in-flight operations are handled:

| Operation State | Handling |
|-----------------|----------|
| **Not yet started** | Rejected immediately |
| **In progress (read-only)** | May complete; no further actions |
| **In progress (mutating)** | Blocked at next PEP check |
| **Committed** | Already complete; recorded in audit |

## Kill Switch Controls

### Who Can Activate

Kill switch activation requires appropriate authority:

| Role | Scope |
|------|-------|
| **ARE (Agent Reliability Engineer)** | Agents in their operational domain |
| **Security Team** | All agents |
| **Manager (Accountable)** | Agents they manage |
| **Platform Admin** | Emergency override for all |

### Activation Channels

The kill switch can be activated through multiple channels:

- **Agent Operations Desk:** UI button for operators
- **CLI:** `seer kill-switch activate --agent <agent-id>`
- **API:** REST endpoint for automation
- **Watch Alert:** Automated response to critical alerts

### Confirmation Requirements

For non-emergency situations, kill switch requires confirmation:

```yaml
killSwitchPolicy:
  requireConfirmation: true
  confirmationTimeout: 30s  # Auto-cancel if not confirmed
  emergencyBypass:
    roles: [security-incident-responder]
```

## Kill Switch Governance

### Audit Trail

All kill switch operations are fully audited:

```json
{
  "event": "kill_switch_activated",
  "agent": "dispute-analyst-bot",
  "activatedBy": "are@acme.com",
  "reason": "Anomalous behavior detected",
  "timestamp": "2026-01-10T15:30:00Z",
  "scope": "all_instances",
  "inFlightOperations": 3,
  "inFlightHandling": "blocked"
}
```

### Recovery

After investigation, agents can be restored:

```yaml
# Recovery request
apiVersion: seer.olympus.io/v1
kind: KillSwitchRecovery
metadata:
  name: dispute-analyst-recovery
spec:
  agent: dispute-analyst-bot
  requestedBy: are@acme.com
  reason: "Investigation complete, root cause addressed"
  approvals:
    - role: security
      required: true
    - role: manager
      required: true
```

### Post-Mortem

Kill switch activations trigger post-mortem processes:

- Why was activation necessary?
- What was the agent doing?
- How can prevention be improved?
- Should guardrails be strengthened?

## Platform Independence

### CSP Independence

The kill switch operates at the Seer platform level, independent of cloud infrastructure:

- Works the same on AWS, Azure, GCP
- Does not depend on CSP-specific features
- Remains effective across infrastructure failures

### Agent Framework Independence

The kill switch works regardless of agent implementation:

- Raw Agent framework (LangChain, CrewAI, etc.)
- Deployment model (container, serverless)
- Runtime environment

Authority revocation happens at the policy layer, above implementation details.

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/agent-identity-authority.md`
*   `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md`
