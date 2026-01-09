# Appendix D: Failure Scenarios & Leading Indicators

---

This appendix catalogs **potential failure scenarios** for AI agent systems in banking, along with **leading indicators** that can detect problems before they become incidents, and **platform responses** that mitigate impact.

---

## D.1 Infrastructure Failure Scenarios

### Scenario D.1.1: Single Region Outage

**Description:** A CSP region becomes unavailable due to infrastructure failure, natural disaster, or network partition.

| Aspect | Detail |
|--------|--------|
| **Probability** | Medium (1-2 incidents per CSP per year) |
| **Impact** | High (all agents in region unavailable) |
| **Blast radius** | All tenants in affected region |

**Leading Indicators:**
- Increased latency to region
- Elevated error rates from region
- CSP status page warnings
- Health check failures from monitoring

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Traffic rerouting** | DNS/load balancer shifts traffic to healthy region |
| **State failover** | Replicated state becomes primary |
| **Alert notification** | Ops team notified; customer dashboards updated |
| **Graceful degradation** | Agents operate with slightly stale memory |

**Recovery:**
- Automatic failback when region recovers
- State reconciliation to resolve conflicts
- Incident postmortem

---

### Scenario D.1.2: CSP-Wide Outage

**Description:** An entire CSP experiences extended outage across multiple regions.

| Aspect | Detail |
|--------|--------|
| **Probability** | Low (rare; major incidents 1-2 per decade) |
| **Impact** | Critical (all agents on that CSP unavailable) |
| **Blast radius** | All tenants using that CSP exclusively |

**Leading Indicators:**
- Multi-region health check failures
- CSP status page major incident
- Industry/news reports

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Multi-cloud activation** | If configured, activate standby on alternate CSP |
| **Manual failover** | If not pre-configured, execute documented DR procedure |
| **Customer communication** | Proactive notification to affected customers |
| **Evidence preservation** | Capture incident timeline for regulatory purposes |

**Recovery:**
- Validate state consistency before failback
- Extended reconciliation period
- Regulatory incident report if required

---

### Scenario D.1.3: Model Inference Service Unavailable

**Description:** CSP model API (Bedrock, Azure OpenAI, Vertex AI) is unavailable or degraded.

| Aspect | Detail |
|--------|--------|
| **Probability** | Medium-High (model services are complex) |
| **Impact** | High (agents cannot reason) |
| **Blast radius** | All agents using affected model |

**Leading Indicators:**
- Model API latency increase (>2x baseline)
- Model API error rate increase
- Model API timeout rate increase
- CSP model service status

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Model failover** | Switch to backup model (e.g., Bedrock → Azure OpenAI) |
| **Model fallback** | Use simpler/faster model if primary unavailable |
| **Rules fallback** | For critical paths, fall back to deterministic rules |
| **Human escalation** | Route to human if no automated fallback |

**Recovery:**
- Automatic switch back when primary model recovers
- Monitor for behavior differences
- Log model transitions for audit

---

## D.2 Agent Behavior Failure Scenarios

### Scenario D.2.1: Model Hallucination Causing Incorrect Action

**Description:** Agent generates plausible but factually incorrect information, leading to wrong decision or action.

| Aspect | Detail |
|--------|--------|
| **Probability** | High (inherent to LLMs) |
| **Impact** | Variable (depends on action type) |
| **Blast radius** | Individual transaction/customer |

**Leading Indicators:**
- Grounding check failures
- Tool validation errors
- Customer complaints
- Anomaly in action patterns

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Grounding checks** | Validate claims against authoritative sources |
| **Fact verification** | Cross-check key facts before action |
| **Confidence thresholds** | Require human review for low-confidence decisions |
| **Action limits** | Ceiling enforcement prevents large-impact errors |

**Recovery:**
- Identify affected transactions
- Initiate remediation workflow
- Update guardrails if pattern detected

---

### Scenario D.2.2: Agent Exceeds Authority

**Description:** Agent attempts action beyond its delegated authority, due to prompt injection, jailbreak, or logic error.

| Aspect | Detail |
|--------|--------|
| **Probability** | Medium (adversarial attempts are common) |
| **Impact** | High (unauthorized action) |
| **Blast radius** | Depends on what was attempted |

**Leading Indicators:**
- Authority check denials
- Unusual action patterns
- Prompt injection detection triggers
- Anomaly detection alerts

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Authority enforcement** | Hard block on unauthorized actions |
| **Alert generation** | Security team notified |
| **Session termination** | Suspicious session ended |
| **Evidence capture** | Full context preserved for investigation |

**Recovery:**
- Investigation of root cause
- Update guardrails if needed
- Customer notification if affected

---

### Scenario D.2.3: Agent Feedback Loop / Runaway Behavior

**Description:** Agent enters loop of repeated actions, consuming resources or causing repeated customer impact.

| Aspect | Detail |
|--------|--------|
| **Probability** | Medium (especially in multi-agent systems) |
| **Impact** | Medium-High (resource consumption, customer annoyance) |
| **Blast radius** | Affected agent/session/customer |

**Leading Indicators:**
- Abnormal action frequency
- Repeated identical actions
- Resource consumption spike
- Session duration anomaly

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Rate limiting** | Limit actions per time period |
| **Loop detection** | Detect repeated patterns |
| **Circuit breaker** | Halt agent after threshold |
| **Session timeout** | Force session end |

**Recovery:**
- Identify loop cause
- Fix agent configuration
- Restore normal operation

---

### Scenario D.2.4: Prompt Injection Attack

**Description:** Adversary injects malicious instructions via user input or retrieved content.

| Aspect | Detail |
|--------|--------|
| **Probability** | High (well-known attack vector) |
| **Impact** | Variable (depends on attack success) |
| **Blast radius** | Targeted session |

**Leading Indicators:**
- Injection pattern detection
- Unusual prompt characteristics
- Unexpected tool calls
- Authority check failures

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Input sanitization** | Filter known injection patterns |
| **Structured prompts** | Separate instructions from user content |
| **Output validation** | Verify outputs match expected format |
| **Authority enforcement** | Block unauthorized actions regardless of prompt |

**Recovery:**
- Log attempt for analysis
- Update injection detection
- No customer impact if blocked

---

## D.3 Data and State Failure Scenarios

### Scenario D.3.1: Memory Corruption

**Description:** Agent memory becomes corrupted due to bug, race condition, or storage failure.

| Aspect | Detail |
|--------|--------|
| **Probability** | Low |
| **Impact** | High (agent behaves incorrectly) |
| **Blast radius** | Affected agent/customer |

**Leading Indicators:**
- Consistency check failures
- Schema validation errors
- Agent behavior anomalies
- Customer complaints about incorrect memory

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Detection** | Periodic consistency checks |
| **Isolation** | Quarantine affected memory |
| **Rollback** | Restore from versioned backup |
| **Alert** | Notify ops team |

**Recovery:**
- Identify corruption scope
- Restore from clean version
- Root cause analysis

---

### Scenario D.3.2: Data Synchronization Failure

**Description:** State replication between regions fails, creating split-brain or stale data.

| Aspect | Detail |
|--------|--------|
| **Probability** | Medium |
| **Impact** | Medium (inconsistent behavior across regions) |
| **Blast radius** | Cross-region sessions |

**Leading Indicators:**
- Replication lag alerts
- Consistency check failures
- Different behavior by region

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Session affinity** | Keep session in one region |
| **Conflict detection** | Identify divergent state |
| **Conflict resolution** | Apply merge rules (last-write-wins, CRDT) |
| **Manual resolution** | Escalate unresolvable conflicts |

**Recovery:**
- Restore replication
- Reconcile state
- Validate consistency

---

### Scenario D.3.3: Audit Log Loss

**Description:** Audit log writes fail, creating gaps in evidence trail.

| Aspect | Detail |
|--------|--------|
| **Probability** | Low (audit path is designed for durability) |
| **Impact** | Critical (regulatory exposure) |
| **Blast radius** | Affected time period |

**Leading Indicators:**
- Audit write failures
- Audit lag metrics
- Audit storage alerts

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Write retry** | Retry with backoff |
| **Local buffer** | Cache locally during outage |
| **Agent pause** | Optionally pause agent if audit unavailable |
| **Alert** | Immediate escalation |

**Recovery:**
- Flush buffered records
- Verify no gaps
- Document any gaps for regulatory purposes

---

## D.4 Security Failure Scenarios

### Scenario D.4.1: Credential Compromise

**Description:** Agent credentials or API keys are compromised.

| Aspect | Detail |
|--------|--------|
| **Probability** | Low-Medium |
| **Impact** | Critical (unauthorized access) |
| **Blast radius** | Affected credentials scope |

**Leading Indicators:**
- Unusual access patterns
- Access from unexpected locations
- Credential use outside normal hours
- Rate limit violations

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Detection** | Anomaly detection on credential use |
| **Revocation** | Immediate credential revocation |
| **Kill switch** | Disable affected agent |
| **Audit** | Review actions taken with compromised creds |

**Recovery:**
- Issue new credentials
- Investigate scope of compromise
- Remediate affected transactions

---

### Scenario D.4.2: Data Exfiltration Attempt

**Description:** Agent is manipulated to expose sensitive data.

| Aspect | Detail |
|--------|--------|
| **Probability** | Medium (common attack goal) |
| **Impact** | Critical (data breach) |
| **Blast radius** | Exposed data scope |

**Leading Indicators:**
- Unusual output patterns
- Data in unexpected places
- PII in agent responses
- Customer data outside authorized scope

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Output filtering** | PII detection and redaction |
| **Scope enforcement** | Only access authorized data |
| **Content analysis** | Detect sensitive data in outputs |
| **Session termination** | End suspicious sessions |

**Recovery:**
- Assess data exposure
- Customer notification if required
- Regulatory notification if required

---

## D.5 Regulatory and Operational Failure Scenarios

### Scenario D.5.1: Regulatory Inquiry

**Description:** Regulator requests evidence of agent decision-making for examination.

| Aspect | Detail |
|--------|--------|
| **Probability** | High (regulatory exams are routine) |
| **Impact** | High if evidence unavailable |
| **Blast radius** | Reputational; potential enforcement |

**Leading Indicators:**
- Examination notification
- Specific decision queries
- Adverse action complaints

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Evidence retrieval** | Query audit fabric for requested records |
| **Evidence packaging** | Generate regulator-friendly format |
| **Context reconstruction** | Retrieve decision context |
| **Explanation retrieval** | Provide stored explanations |

**Recovery:**
- Provide requested evidence
- Address any gaps or deficiencies
- Remediate if findings identified

---

### Scenario D.5.2: Customer Complaint About Agent Decision

**Description:** Customer disputes agent decision and files formal complaint.

| Aspect | Detail |
|--------|--------|
| **Probability** | High (complaints are normal) |
| **Impact** | Low-Medium per complaint; pattern is concerning |
| **Blast radius** | Individual customer; potentially class |

**Leading Indicators:**
- Complaint volume increase
- Complaint pattern (same decision type)
- Social media mentions
- Regulatory referrals

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Case retrieval** | Pull complete decision record |
| **Explanation review** | Examine stored explanation |
| **Override capability** | Allow human to correct if appropriate |
| **Pattern analysis** | Check for systemic issues |

**Recovery:**
- Resolve individual complaint
- If systemic, adjust agent behavior
- Document resolution

---

### Scenario D.5.3: Unauthorized Agent Deployment

**Description:** Agent deployed without proper authorization or with incorrect authority.

| Aspect | Detail |
|--------|--------|
| **Probability** | Low-Medium (depends on controls) |
| **Impact** | Medium-High (unauthorized actions) |
| **Blast radius** | Scope of agent's actions |

**Leading Indicators:**
- Deployment without approval record
- Authority configuration anomalies
- Actions outside expected scope

**Platform Response:**

| Response | Implementation |
|----------|----------------|
| **Deployment controls** | Require approval for production deployment |
| **Authority validation** | Verify authority before activation |
| **Audit trail** | Log all deployment activities |
| **Kill switch** | Ability to immediately deactivate |

**Recovery:**
- Deactivate unauthorized agent
- Review actions taken
- Remediate as needed

---

## D.6 Leading Indicators Dashboard

A comprehensive monitoring approach includes these indicator categories:

### Infrastructure Indicators

| Indicator | Threshold | Action |
|-----------|-----------|--------|
| Region health check failures | >5% in 1 min | Alert |
| Model API latency | >2x baseline | Investigate |
| Model API error rate | >1% | Alert |
| Storage latency | >500ms P99 | Investigate |
| Replication lag | >5s | Alert |

### Agent Behavior Indicators

| Indicator | Threshold | Action |
|-----------|-----------|--------|
| Authority check denials | Any | Log + investigate |
| Grounding check failures | >5% | Investigate |
| Session duration | >3x median | Investigate |
| Action frequency | >10x normal | Circuit breaker |
| Error rate per agent | >5% | Disable agent |

### Security Indicators

| Indicator | Threshold | Action |
|-----------|-----------|--------|
| Prompt injection detections | Any | Log + enhance |
| Unusual access patterns | Anomaly score | Investigate |
| PII in outputs | Any | Block + alert |
| Credential use anomaly | Anomaly score | Investigate |

### Compliance Indicators

| Indicator | Threshold | Action |
|-----------|-----------|--------|
| Audit write failures | Any | Critical alert |
| Explanation generation failures | Any | Investigate |
| Approval workflow bypasses | Any | Critical alert |
| Override without documentation | Any | Alert |

---

## D.7 Incident Response Framework

### Severity Classification

| Severity | Definition | Example | Response Time |
|----------|------------|---------|---------------|
| **P1 - Critical** | Service-wide outage; data breach; regulatory violation | CSP outage; credential compromise | Immediate |
| **P2 - High** | Significant degradation; repeated failures | Model unavailable; memory corruption | 15 minutes |
| **P3 - Medium** | Limited impact; workarounds available | Single agent failure; slow performance | 1 hour |
| **P4 - Low** | Minor issues; no customer impact | Warning alerts; non-critical bugs | 4 hours |

### Response Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    INCIDENT RESPONSE FLOW                           │
│                                                                     │
│  Detection ──► Triage ──► Containment ──► Resolution ──► Postmortem │
│      │           │            │              │              │       │
│      ▼           ▼            ▼              ▼              ▼       │
│  Monitoring   Severity    Stop blast    Fix root      Document     │
│  Alerts       Assign      radius        cause         Improve      │
└─────────────────────────────────────────────────────────────────────┘
```

### Communication Plan

| Stakeholder | When to Notify | Channel |
|-------------|----------------|---------|
| **Ops team** | All incidents | PagerDuty |
| **Engineering** | P1-P2 | Slack + PagerDuty |
| **Management** | P1 | Immediate call |
| **Customers** | P1-P2 with impact | Status page + direct |
| **Regulators** | Material incidents | Per notification requirements |

---

## D.8 Failure Prevention Strategies

### Design for Failure

| Strategy | Implementation |
|----------|----------------|
| **Redundancy** | Multiple regions, multiple models, multiple paths |
| **Isolation** | Tenant isolation, agent sandboxing |
| **Graceful degradation** | Fallback paths at every level |
| **Circuit breakers** | Prevent cascade failures |
| **Timeouts** | Bound all external calls |

### Test for Failure

| Test Type | Frequency | Coverage |
|-----------|-----------|----------|
| **Unit tests** | Every commit | Core logic |
| **Integration tests** | Daily | Component interactions |
| **Chaos engineering** | Weekly | Failure injection |
| **DR drills** | Quarterly | Full failover |
| **Tabletop exercises** | Semi-annually | Incident response |

### Learn from Failure

| Practice | Purpose |
|----------|---------|
| **Blameless postmortems** | Understand root cause without fear |
| **Incident database** | Track patterns over time |
| **Improvement tracking** | Ensure fixes are implemented |
| **Sharing** | Cross-team learning |

---

## D.9 Summary

Failure is inevitable. The platform's job is to:

1. **Detect** failures quickly through comprehensive monitoring
2. **Contain** failures to minimize blast radius
3. **Recover** gracefully with minimal data loss
4. **Learn** from failures to prevent recurrence
5. **Evidence** failures for regulatory transparency

The scenarios in this appendix should inform:

- Platform architecture decisions
- Monitoring and alerting design
- Runbook development
- DR/BC planning
- Regulatory evidence requirements

---

*Previous: [Appendix A: Regulatory & Legal Considerations](./appendix-a-regulatory.md)*

*Return to: [README](./README.md)*

