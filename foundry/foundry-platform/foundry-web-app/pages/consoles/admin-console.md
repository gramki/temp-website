# Admin Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/admin`

**Group:** Settings

**Purpose:** Workbench configuration — settings, integrations, team management.

---

## Page Sections

### 1. Workbench Settings

| Setting | Description |
|---------|-------------|
| **Name** | Workbench display name |
| **Description** | Brief description |
| **Product Code** | From Olympus Weave (read-only) |
| **Workshop** | Parent Workshop (read-only) |
| **Created** | Creation date |

### 2. Team Management

| Element | Description |
|---------|-------------|
| **Members list** | All team members |
| **Invite member** | Add new team member |
| **Remove member** | Remove from Workbench |
| **Change role** | Manager ↔ Member |
| **Pending invites** | Awaiting acceptance |

### 3. Integration Settings

| Integration | Settings |
|-------------|----------|
| **GitHub** | Org connection, App status |
| **Figma** | OAuth connection, linked projects |
| **TestRail** | OAuth connection, linked projects |
| **Jira** | OAuth connection, label filters |
| **Olympus Weave** | OAuth connection, Product Code |

### 4. Repository Settings

| Element | Description |
|---------|-------------|
| **Intent repo** | GitHub URL, access |
| **Design repo** | GitHub URL, access |
| **Code repos** | List, add, remove |
| **Quality automation repo** | GitHub URL |

### 5. Jira Label Configuration

| Repository | Jira Project | Label Filter |
|------------|--------------|--------------|
| Operations | JSM-OPS | `workbench:WB-123` |
| Feedback | JIRA-FB | `workbench:WB-123` |
| Work | JIRA-WORK | `workbench:WB-123` |

### 6. Notification Settings

| Setting | Description |
|---------|-------------|
| **Default channels** | Where notifications go |
| **Alert thresholds** | When to notify |
| **Quiet hours** | Suppress non-critical |
| **Escalation rules** | Who gets escalations |

### 7. Access Control

| Element | Description |
|---------|-------------|
| **Permissions** | What each role can do |
| **API access** | Tokens, keys |
| **Audit log** | Access history |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Update settings | Manager | Change Workbench config |
| Manage team | Manager | Add/remove/role change |
| Connect integration | Manager | OAuth flow for tools |
| Disconnect integration | Manager | Remove tool connection |
| Create code repo | Manager | New repo in GitHub Org |
| Update Jira labels | Manager | Change label filters |
| View audit log | Manager | See access history |

---

## Sections (Tabs)

1. **General** — Name, description, basic info
2. **Team** — Members, roles, invites
3. **Integrations** — External tool connections
4. **Repositories** — Git repo management
5. **Notifications** — Alert settings
6. **Access** — Permissions, API, audit

---

## Related Consoles

- **Repositories & Tools** — Use configured integrations
- **Team Console** — Team analytics (vs. management)
- **Risk Console** — Notification triggers
