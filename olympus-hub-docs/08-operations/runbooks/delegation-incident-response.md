# Runbook: Delegation Incident Response

> **Status**: 🟢 Complete  
> **Last Updated**: 2026-01-17  
> **Owner**: Security Operations

---

## Purpose

This runbook provides procedures for responding to incidents involving Request-Scoped Authority Delegation. It covers token compromise, unauthorized delegation, and certificate revocation scenarios.

---

## 1. Token Compromise

### Symptoms
- Unusual delegation token usage patterns
- Token used from unexpected network/location
- Alerts from PEP anomaly detection
- User reports unauthorized activity

### Severity: P1 (Critical)

### Response Steps

1. **Immediate Containment** (0-5 minutes)
   ```bash
   # Revoke the specific Delegation Certificate
   curl -X PUT "https://cipher-iam.hub.internal/v1/delegation-certificates/{cert-id}/revoke" \
     -H "Authorization: Bearer $ADMIN_TOKEN" \
     -d '{"reason": "suspected_compromise", "revokedBy": "security-ops"}'
   ```

2. **Token Invalidation** (Automatic)
   - All tokens derived from revoked certificate are immediately invalid
   - PEPs will reject any further usage

3. **Scope Assessment** (5-15 minutes)
   ```bash
   # Query actions performed with the compromised token
   curl "https://caf.hub.internal/v1/audit?filter=token_id:{token-id}" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
   ```

4. **User Notification** (15-30 minutes)
   - Notify affected business user via their registered Channel
   - Provide summary of actions taken
   - Recommend password reset if external IdP compromise suspected

5. **Agent Inspection** (30-60 minutes)
   - Review agent's recent behavior logs
   - Check for other anomalous patterns
   - Consider suspending agent if compromise confirmed

6. **Post-Incident** (1-24 hours)
   - Generate incident report
   - Review detection timeline
   - Update detection rules if needed

---

## 2. Unauthorized Delegation

### Symptoms
- User reports delegation they did not authorize
- Delegation Certificate created without corresponding consent event
- Anomalous delegation patterns detected

### Severity: P1 (Critical)

### Response Steps

1. **Verify Claim** (0-10 minutes)
   ```bash
   # Get delegation certificate details
   curl "https://cipher-iam.hub.internal/v1/delegation-certificates/{cert-id}" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
   
   # Check corresponding consent audit event
   curl "https://caf.hub.internal/v1/audit?filter=event_type:DELEGATION_CERTIFICATE_ISSUED,certificate_id:{cert-id}" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
   ```

2. **Immediate Revocation** (10-15 minutes)
   ```bash
   curl -X PUT "https://cipher-iam.hub.internal/v1/delegation-certificates/{cert-id}/revoke" \
     -H "Authorization: Bearer $ADMIN_TOKEN" \
     -d '{"reason": "unauthorized_delegation", "revokedBy": "security-ops"}'
   ```

3. **Channel Investigation** (15-60 minutes)
   - Identify which Channel issued the certificate
   - Review Channel logs for consent flow
   - Check for session hijacking indicators

4. **User Communication** (30-60 minutes)
   - Confirm revocation with user
   - Provide guidance on reviewing other delegations
   - Recommend session refresh across all Channels

5. **Root Cause Analysis** (1-7 days)
   - Was consent flow bypassed?
   - Was user session compromised?
   - Was Channel compromised?

---

## 3. Mass Certificate Revocation

### Trigger
- Template vulnerability discovered
- Tenant-wide security incident
- Regulatory requirement

### Severity: P2 (High)

### Response Steps

1. **Scope Definition** (0-15 minutes)
   ```bash
   # Count affected certificates
   curl "https://cipher-iam.hub.internal/v1/delegation-certificates?filter=template_ref:{template-name}&status=Active&count=true" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
   ```

2. **Communication Preparation** (15-30 minutes)
   - Draft user notification message
   - Identify affected user count
   - Prepare support resources

3. **Bulk Revocation** (30-45 minutes)
   ```bash
   # Bulk revoke by template
   curl -X POST "https://cipher-iam.hub.internal/v1/delegation-certificates/bulk-revoke" \
     -H "Authorization: Bearer $ADMIN_TOKEN" \
     -d '{
       "filter": {"template_ref": "{template-name}"},
       "reason": "template_vulnerability",
       "revokedBy": "security-ops"
     }'
   ```

4. **Propagation Verification** (45-60 minutes)
   ```bash
   # Verify revocation reached all PEPs
   curl "https://pep-monitor.hub.internal/v1/revocation-status?batch_id={batch-id}" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
   ```

5. **User Notification** (60-120 minutes)
   - Send notifications via Channels
   - Explain reason and next steps
   - Provide re-delegation instructions if applicable

6. **Template Remediation** (Parallel)
   - Deprecate vulnerable template
   - Create corrected replacement template
   - Update tenant admin on new template availability

---

## 4. Authority Request Abuse

### Symptoms
- User reports excessive Authority Request prompts
- Agent sending high volume of requests
- Rate limit alerts triggered

### Severity: P3 (Medium)

### Response Steps

1. **Rate Limit Review** (0-5 minutes)
   ```bash
   # Check agent's Authority Request rate
   curl "https://signal-exchange.hub.internal/v1/metrics?agent_id={agent-id}&metric=authority_request_rate" \
     -H "Authorization: Bearer $ADMIN_TOKEN"
   ```

2. **Agent Throttling** (5-15 minutes)
   ```bash
   # Increase rate limit strictness for specific agent
   curl -X PUT "https://signal-exchange.hub.internal/v1/rate-limits/{agent-id}" \
     -H "Authorization: Bearer $ADMIN_TOKEN" \
     -d '{"authority_requests_per_hour": 5}'
   ```

3. **User Relief** (15-30 minutes)
   - Allow user to block further requests from agent
   - Clear pending Authority Requests

4. **Agent Review** (30-60 minutes)
   - Review agent configuration
   - Check for programming errors causing excessive requests
   - Consider agent suspension if malicious

---

## 5. Monitoring and Alerts

### Key Metrics to Monitor

| Metric | Threshold | Alert Severity |
|--------|-----------|----------------|
| Token usage anomaly score | > 0.8 | P1 |
| Certificate revocations/hour | > 100 | P2 |
| Authority Request denials/hour | > 50 | P3 |
| Token validation failures/min | > 10 | P2 |
| PEP policy violations/hour | > 20 | P2 |

### Dashboards

- **Delegation Health**: Real-time delegation activity
- **Token Lifecycle**: Token issuance, usage, expiry, revocation
- **PEP Enforcement**: Policy evaluations and violations
- **User Consent**: Consent rates, denials, revocations

---

## Related Documentation

- [Request-Scoped Delegation Security](../../../olympus-seer-docs/seer-design/security/request-scoped-delegation-security.md)
- [Cipher IAM Extensions Operations](./cipher-iam-operations.md)
- [Signal Exchange Operations](./signal-exchange-operations.md)
