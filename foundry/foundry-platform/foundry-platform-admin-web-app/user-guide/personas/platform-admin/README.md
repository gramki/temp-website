# Platform Admin Persona

**Role:** foundry-platform-admin

**App:** Foundry Platform Admin Web App (separate from Foundry Web App)

## Description

The Platform Admin is responsible for the overall Foundry Platform — creating and managing Foundries, monitoring infrastructure health, and configuring platform-level settings. This is a highly privileged role with access to all Foundries and platform infrastructure.

Platform Admins are typically:
- Platform operations engineers
- DevOps/SRE team members
- Technical leadership with platform oversight

## Prerequisites

- Olympus Cipher membership in the Platform Admin group
- MFA enabled (required for this role)
- Understanding of platform infrastructure (PostgreSQL, object storage, GitHub App)

## Relationship to Foundry Admin

| Aspect | Platform Admin | Foundry Admin |
|--------|----------------|---------------|
| **Scope** | All Foundries, platform infrastructure | Single Foundry |
| **App** | Platform Admin Web App | Foundry Web App |
| **Creates** | Foundries | Workshops, Workbenches |
| **Manages** | Platform settings, regions, quotas | Foundry settings, teams, agents |
| **Auth group** | `foundry-platform-admin` | `foundry-admin` (per Foundry) |

Platform Admin and Foundry Admin are distinct roles operating at different levels. They are not merged because:
- Separation of concerns (platform ops vs tenant ops)
- Different security boundaries (platform-wide vs single-tenant)
- Different skill sets (infrastructure vs product administration)

## Characteristics

| Attribute | Description |
|-----------|-------------|
| **Technical depth** | Strong understanding of infrastructure, databases, security |
| **Scope** | Platform-wide, all Foundries |
| **Frequency** | Daily for monitoring, occasional for Foundry creation |
| **Criticality** | High — actions affect all tenants |

## Jobs to be Done (JTBD)

### 1. Create and Onboard New Foundries

**When** a new organization needs to use Foundry Platform,  
**I want to** quickly provision their Foundry with appropriate resources,  
**So that** they can start onboarding their teams without delay.

**Tasks:**
- Create Foundry with appropriate quotas
- Specify region based on data residency requirements
- Send invitation to designated Foundry Admin
- Monitor onboarding completion

**Success Metrics:**
- Foundry provisioned in < 2 minutes
- Admin invitation delivered successfully
- Onboarding completed within expected timeframe

### 2. Monitor Platform Health

**When** I start my day or receive an alert,  
**I want to** quickly assess platform health and identify issues,  
**So that** I can address problems before they impact users.

**Tasks:**
- Check dashboard for alerts and metrics
- Review infrastructure health (database, storage)
- Identify Foundries with resource issues
- Investigate and resolve issues

**Success Metrics:**
- No blind spots in monitoring
- Issues identified before user reports
- Clear actionable information

### 3. Manage Foundry Lifecycles

**When** a Foundry needs to be archived or deleted,  
**I want to** safely execute the lifecycle transition,  
**So that** resources are managed and data is handled appropriately.

**Tasks:**
- Archive Foundries that are no longer active
- Delete Foundries after appropriate retention period
- Unarchive Foundries that need to be reactivated
- Track lifecycle transitions in audit log

**Success Metrics:**
- No accidental data loss
- Clear audit trail
- Smooth transitions with minimal support requests

### 4. Adjust Foundry Resources

**When** a Foundry needs more (or less) resources,  
**I want to** adjust their quotas appropriately,  
**So that** they have the resources they need without waste.

**Tasks:**
- Review current usage vs. quotas
- Adjust quotas based on growth patterns
- Communicate changes to Foundry Admin
- Track quota changes in audit log

**Success Metrics:**
- Quotas aligned with actual usage
- No unexpected quota exhaustion
- Proactive adjustments before issues

### 5. Configure Platform Settings

**When** platform-level configuration needs to change,  
**I want to** update settings safely with clear understanding of impact,  
**So that** the platform operates according to requirements.

**Tasks:**
- Update default quotas for new Foundries
- Configure integrations (GitHub, Olympus Cipher)
- Manage regions and infrastructure assignments
- Update audit and compliance settings

**Success Metrics:**
- Settings changes applied correctly
- No unintended side effects
- Clear audit trail

### 6. Troubleshoot Foundry Issues

**When** a Foundry Admin reports an issue,  
**I want to** quickly investigate and resolve the problem,  
**So that** the affected Foundry can continue operations.

**Tasks:**
- Access Foundry details and activity logs
- Check resource utilization and health
- Identify root cause
- Take corrective action or escalate

**Success Metrics:**
- Quick time to resolution
- Root cause identified
- Preventive measures implemented

## Workflows

### Create Foundry Workflow

```
1. Navigate to Foundries page
2. Click "Create Foundry"
3. Fill in details:
   - Name, Slug
   - Admin email, Admin name
   - Region
   - (Optional) PostgreSQL instance
   - (Optional) Adjust quotas from defaults
4. Submit and wait for provisioning
5. Verify Foundry created
6. (Optional) Monitor onboarding progress
```

### Daily Monitoring Workflow

```
1. Open Dashboard
2. Review summary metrics
3. Check alerts panel:
   - Address critical/warning alerts
   - Acknowledge informational items
4. Review infrastructure health
5. Check for pending onboardings
6. Review recent activity for anomalies
```

### Archive Foundry Workflow

```
1. Navigate to Foundry detail page
2. Verify this is the correct Foundry
3. Click "Archive Foundry"
4. Read confirmation dialog
5. Confirm action
6. Verify status changed to "Archived"
7. (Optional) Notify Foundry Admin
```

### Delete Foundry Workflow

```
1. Navigate to Foundry detail page
2. Verify Foundry is archived or should be deleted
3. Click "Delete Foundry"
4. Read warning about permanent deletion
5. Type Foundry slug to confirm
6. Confirm deletion
7. Verify Foundry removed from list
```

## Tools and Access

| Tool | Access Level |
|------|--------------|
| Platform Admin Web App | Full access |
| Foundry Web Apps | Can view (for troubleshooting) |
| Cloud console (AWS/GCP) | Read access for monitoring |
| GitHub (platform org) | Admin access |
| Olympus Cipher | Admin group membership |

## Responsibilities

### Do

- Create Foundries on request
- Monitor platform health daily
- Respond to infrastructure alerts
- Adjust quotas as needed
- Archive/delete Foundries as appropriate
- Maintain platform configuration
- Support Foundry Admins with escalated issues

### Don't

- Access Foundry data without legitimate need
- Make changes without audit trail
- Delete Foundries without confirmation
- Share platform credentials
- Bypass security controls

## Security Considerations

- Platform Admin access is highly privileged
- All actions are logged to audit trail
- Session timeout is shorter than regular users
- MFA required via Olympus Cipher
- Access should be limited to essential personnel
- Regular access reviews recommended

## Related

- [Dashboard page](../../../platform-developer-guide/pages/dashboard.md) — Platform health overview
- [Foundries page](../../../platform-developer-guide/pages/foundries.md) — Foundry listing and management
- [Infrastructure page](../../../platform-developer-guide/pages/infrastructure.md) — PostgreSQL and storage monitoring
- [Platform Settings page](../../../platform-developer-guide/pages/platform-settings.md) — Platform configuration
- [Foundry Detail page](../../../platform-developer-guide/pages/foundry-detail.md) — Individual Foundry management
- [Foundry Admin persona](../../../../foundry-web-app/user-guide/personas/foundry-admins/README.md) — Foundry-level administration (separate role)
- [Foundry onboarding](../../../../management/user-guide/foundry-onboarding.md) — Onboarding journey for new Foundries
