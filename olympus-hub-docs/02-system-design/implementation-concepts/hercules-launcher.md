# Hercules Launcher

> **Category:** Integration

---

## Overview

**Hercules Launcher** is a deep linking service that enables cross-channel navigation within Hub. It generates context-aware URLs that open the appropriate Hub interface for viewing requests, tasks, or other resources. Channels like MS Teams, email, and notifications use Hercules Launcher for seamless navigation.

---

## Ontology Context

### Relationship to Ontology

The ontology describes multi-channel access but doesn't address navigation. Hercules Launcher implements cross-channel linking.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Channel | Link target | Launcher opens appropriate channel |
| (not covered) | Deep linking | Cross-channel navigation |

### Gap This Fills

The ontology focuses on channels independently. Hercules Launcher addresses:
1. **Navigation**: How do users move between channels?
2. **Context preservation**: How is context passed in links?
3. **Channel selection**: How is the right UI chosen?

---

## Definition

**Hercules Launcher** is a deep linking service that:
- Generates URLs that open Hub resources in appropriate UIs
- Preserves context across channel transitions
- Handles authorization for linked resources
- Supports mobile and desktop targets

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-wide service |
| **Lifecycle** | Platform-managed; always available |
| **Ownership** | Platform owns |
| **Multiplicity** | Single service; many link types |

---

## Structure

### Link Format

```
Base URL: https://hub.acme.com/launch

Full format:
https://hub.acme.com/launch/{resource_type}/{resource_id}
  ?tenant={tenant_id}
  &subscription={subscription_id}
  &workbench={workbench_id}
  &channel={preferred_channel}
  &context={encoded_context}
```

### Resource Types

| Type | Target | Example |
|------|--------|---------|
| **request** | Request detail view | `/launch/request/req-001` |
| **task** | Task solver view | `/launch/task/task-001` |
| **workbench** | Workbench dashboard | `/launch/workbench/dispute-ops` |
| **scenario** | Scenario view | `/launch/scenario/standard-dispute` |
| **knowledge** | Knowledge document | `/launch/knowledge/doc-001` |

### Link Generation

```python
# Generating a launch URL
from hub.launcher import HerculesLauncher

launcher = HerculesLauncher(base_url="https://hub.acme.com")

# Request link
url = launcher.create_link(
    resource_type="request",
    resource_id="req-001",
    tenant="acme-bank",
    workbench="dispute-ops-prod",
    context={"source": "notification"}
)

# Result:
# https://hub.acme.com/launch/request/req-001?tenant=acme-bank&workbench=dispute-ops-prod&context=...
```

---

## Behavior

### Link Resolution Flow

```
1. User clicks Hercules link
   └── From email, Teams, notification, etc.

2. Hercules Launcher receives request
   ├── Parse resource type and ID
   ├── Validate tenant and workbench
   └── Check user authorization

3. Determine target channel
   ├── User's default preference
   ├── Link-specified channel
   └── Device type (mobile vs desktop)

4. Redirect to appropriate UI
   ├── Web console
   ├── Mobile app deep link
   └── Teams tab

5. UI opens resource
   └── With preserved context
```

### Channel Selection

| Condition | Target |
|-----------|--------|
| Desktop browser | Web console |
| Mobile browser | Mobile web or app |
| Teams context | Teams tab |
| Link specifies channel | Requested channel |

### Authorization

```
Before redirect:
├── Verify user authenticated
├── Check access to resource
├── Log access attempt
└── If unauthorized: show error, not resource
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Notification Services | ← called by | Links in notifications |
| MS Teams | ← called by | Links in Teams messages |
| Email | ← embedded in | Links in email notifications |
| Web Console | → redirects to | Target UI |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Valid resource** | Resource must exist |
| **Authorization required** | User must have access |
| **Context encoded** | Context URL-safe encoded |
| **Expiring tokens** | Optional link expiration |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Seamless navigation** | One-click to resource |
| ✅ **Context preserved** | Source and state carried |
| ✅ **Channel-aware** | Right UI for context |
| ✅ **Trackable** | Link usage logged |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Requires auth** | Clear auth flow |
| ⚠️ **Link rot possible** | Resource availability checks |

---

## Examples

### Example 1: Notification Link

```
Email notification:

"Your dispute has been resolved.

View details: [View Request]

Link: https://hub.acme.com/launch/request/req-001
      ?tenant=acme-bank
      &workbench=dispute-ops-prod
      &context=eyJzb3VyY2UiOiJlbWFpbCJ9"

User clicks → Opens request in web console
```

### Example 2: Teams Deep Link

```
Teams message:

"New task assigned: Investigate dispute
[View Task]

Link: https://hub.acme.com/launch/task/task-001
      ?channel=teams
      &context=..."

User clicks in Teams → Opens in Teams tab
User clicks in browser → Opens in web console
```

### Example 3: CTA Link

```
SMS with call-to-action:

"Upload documents for dispute case.
Link: https://hub.acme.com/launch/upload/req-001"

Customer clicks → Opens upload interface
```

---

## Implementation Notes

### For Developers

- Use Hercules Launcher for all cross-channel links
- Include meaningful context in links
- Handle link resolution errors gracefully

### For Operators

- Monitor link usage and errors
- Review unauthorized access attempts
- Manage link expiration policies

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Channel](./channel.md) | Launcher links to channels |
| [MS Teams Integration](./ms-teams-integration.md) | Teams uses launcher |
| [Notification Services](./notification-services.md) | Notifications include links |

---

## References

- [Hercules Launcher Service](../../04-subsystems/hercules-launcher/README.md)
- [UX Architecture](../../06-ux-architecture/README.md)

