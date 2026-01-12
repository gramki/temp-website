# Operational Tools

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13  
> **Design Level**: C2 (Container)

---

## Overview

Operational Tools provides UI tools for operational tasks in Watch Console. These tools enable SRE personas to perform common operational actions directly from the observability interface.

**Key Principle**: Operational tools are integrated into Watch Console as custom plugins, providing immediate access to common operational tasks without switching contexts.

---

## Tool Categories

### Agent Management Tools

#### Agent Isolator

**Purpose**: Immediately isolate agent from network

**Access**: Watch Console (emergency)

**Functionality**:
- Isolate agent from all network traffic
- Block inbound and outbound connections
- Preserve agent state for investigation
- Log isolation event

**Use Cases**:
- Security incident response
- Agent misbehavior
- Cost runaway scenarios
- Emergency containment

#### Agent Scaler

**Purpose**: Manually scale agent replicas

**Access**: Watch Console + kubectl

**Functionality**:
- Scale agent replicas up or down
- View current replica count
- Set target replica count
- View scaling history

**Use Cases**:
- Manual capacity adjustment
- Load testing
- Emergency scaling

---

### Security Tools

#### Credential Revoker

**Purpose**: Revoke agent credentials

**Access**: Watch Console

**Functionality**:
- Revoke agent SPIFFE credentials
- Revoke tool access credentials
- Revoke model gateway credentials
- Log revocation event

**Use Cases**:
- Security incident response
- Credential compromise
- Agent decommissioning

#### Guardrail Configurator

**Purpose**: Update guardrail rules

**Access**: Workbench Studio

**Functionality**:
- View current guardrail configuration
- Update guardrail rules
- Test guardrail changes
- Deploy guardrail updates

**Use Cases**:
- Guardrail tuning
- Security policy updates
- Guardrail optimization

---

### Audit and Investigation Tools

#### Audit Log Viewer

**Purpose**: Deep-dive audit trail analysis

**Access**: Watch Console

**Functionality**:
- Search audit logs by agent, workbench, time range
- Filter by event type (policy violations, guardrail blocks, tool access)
- View detailed event context
- Export audit logs

**Use Cases**:
- Security investigation
- Compliance auditing
- Incident analysis
- Policy violation investigation

#### Injection Pattern Analyzer

**Purpose**: Analyze injection attempt patterns

**Access**: Watch Console

**Functionality**:
- View prompt injection attempts
- Analyze injection patterns
- Identify attack vectors
- Generate security reports

**Use Cases**:
- Security analysis
- Attack pattern detection
- Guardrail improvement

---

### LLMOps Tools

#### Prompt Version Manager

**Purpose**: Deploy, rollback, A/B test prompts

**Access**: Workbench Studio

**Functionality**:
- View active prompt versions
- Deploy new prompt versions
- Rollback to previous versions
- Configure A/B testing

**Use Cases**:
- Prompt version management
- Prompt rollback
- A/B testing

#### Model Fallback Config

**Purpose**: Configure model fallback chains

**Access**: Watch Console

**Functionality**:
- Configure primary and fallback models
- Set fallback triggers
- Test fallback chains
- View fallback history

**Use Cases**:
- Model availability management
- Fallback configuration
- Model reliability

#### Cost Analyzer

**Purpose**: Drill-down cost by agent, prompt, model

**Access**: Watch Console

**Functionality**:
- View cost by agent
- View cost by prompt version
- View cost by model
- Cost trend analysis
- Budget tracking

**Use Cases**:
- Cost optimization
- Budget management
- Cost anomaly investigation

#### Prompt Playground

**Purpose**: Test prompts before deployment

**Access**: Workbench Studio

**Functionality**:
- Test prompt templates
- Preview prompt outputs
- Validate prompt syntax
- Compare prompt versions

**Use Cases**:
- Prompt development
- Prompt testing
- Prompt validation

#### Rollback Trigger

**Purpose**: Instant rollback to previous prompt version

**Access**: Watch Console (one-click)

**Functionality**:
- View rollback history
- Trigger instant rollback
- Rollback confirmation
- Rollback status tracking

**Use Cases**:
- Emergency rollback
- Prompt issue response
- Quick recovery

---

### Platform Tools

#### Tool Registry Admin

**Purpose**: Deprecate, activate, version tools

**Access**: Workbench Studio

**Functionality**:
- View tool registry
- Deprecate tools
- Activate tools
- Manage tool versions

**Use Cases**:
- Tool lifecycle management
- Tool deprecation
- Tool versioning

#### Policy Simulator

**Purpose**: Test policy changes before deployment

**Access**: Watch Console (Rego Playground)

**Functionality**:
- Test OPA policies
- Simulate policy evaluations
- Validate policy syntax
- Compare policy versions

**Use Cases**:
- Policy development
- Policy testing
- Policy validation

#### Runtime Debugger

**Purpose**: Pod exec, log streaming, resource inspection

**Access**: Watch Console + kubectl

**Functionality**:
- Execute commands in agent pods
- Stream agent logs
- Inspect resource usage
- View pod events

**Use Cases**:
- Debugging
- Troubleshooting
- Performance investigation

#### Tool Access Reviewer

**Purpose**: Review and approve tool access requests

**Access**: Watch Console

**Functionality**:
- View tool access requests
- Approve or deny requests
- Review access history
- Manage access permissions

**Use Cases**:
- Access control
- Security review
- Permission management

---

## Tool Integration

### Plugin Architecture

Operational tools are implemented as Watch plugins:

```yaml
plugin:
  name: "seer-agent-isolator"
  type: "operational-tool"
  ui_component: "AgentIsolator"
  api_endpoints:
    - path: "/api/seer/isolate-agent"
      method: "POST"
      handler: "isolateAgent"
  permissions:
    - "seer:agent:isolate"
```

### Tool Access Control

Tools are protected by permissions:

| Tool | Required Permission |
|------|-------------------|
| **Agent Isolator** | `seer:agent:isolate` |
| **Credential Revoker** | `seer:credential:revoke` |
| **Guardrail Configurator** | `seer:guardrail:configure` |
| **Audit Log Viewer** | `seer:audit:view` |
| **Prompt Version Manager** | `seer:prompt:manage` |
| **Tool Registry Admin** | `seer:tool:admin` |

---

## Related Documentation

- [Watch Extension Layer](./watch-extension-layer.md) — Plugin deployment infrastructure
- [Persona Dashboards](./persona-dashboards.md) — Dashboards for each persona
- [Alert Templates](./alert-templates.md) — Alerts for operational scenarios

---

*Operational Tools provide immediate access to common operational tasks directly from Watch Console.*
