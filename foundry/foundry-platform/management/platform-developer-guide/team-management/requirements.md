# Team Management Requirements

This document specifies detailed implementation requirements for the Team Management subsystem.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Team Management                                     │
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │  User Sync      │  │  Team/Role      │  │  Authorization  │             │
│  │  Service        │  │  CRUD APIs      │  │  Service        │             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│           │                    │                    │                       │
│           └────────────────────┼────────────────────┘                       │
│                                │                                            │
│                                ▼                                            │
│                     ┌─────────────────────┐                                │
│                     │  PostgreSQL         │                                │
│                     │  (Foundry-scoped)   │                                │
│                     └─────────────────────┘                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. User Sync Service

**Responsibilities:**
- Handle JIT user provisioning on Olympus Cipher callback
- Process SCIM push requests from Olympus Cipher
- Map Cipher attributes to Foundry user profile
- Detect and handle user deprovisioning

**Interfaces:**
- OAuth 2.0 callback endpoint (for JIT)
- SCIM 2.0 API (for push sync)
- Internal event bus (user created/updated/deleted events)

### 2. Team/Role CRUD APIs

**Responsibilities:**
- Manage team lifecycle (create, update, delete)
- Manage team membership
- Manage role definitions (built-in + custom)
- Manage role assignments (user/team to scope)

**Interfaces:**
- REST API for all CRUD operations
- Audit logging for all changes

### 3. Authorization Service

**Responsibilities:**
- Evaluate permission checks in real-time
- Cache permission lookups for performance
- Provide bulk permission evaluation
- Support permission introspection (list user's permissions)

**Interfaces:**
- Synchronous check API (for inline authorization)
- Bulk check API (for UI rendering)
- Introspection API (for admin UIs)

## Database Schema

### users

```sql
CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    foundry_id VARCHAR(36) NOT NULL REFERENCES foundries(id),
    cipher_user_id VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    display_name VARCHAR(255) NOT NULL,
    avatar_url VARCHAR(500),
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    provisioning_source VARCHAR(20) NOT NULL, -- 'jit', 'scim', 'manual'
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    
    CONSTRAINT uk_foundry_cipher_user UNIQUE (foundry_id, cipher_user_id),
    CONSTRAINT uk_foundry_email UNIQUE (foundry_id, email),
    CONSTRAINT chk_status CHECK (status IN ('active', 'suspended', 'deprovisioned'))
);

CREATE INDEX idx_users_foundry ON users(foundry_id);
CREATE INDEX idx_users_status ON users(foundry_id, status);
```

### teams

```sql
CREATE TABLE teams (
    id VARCHAR(36) PRIMARY KEY,
    foundry_id VARCHAR(36) NOT NULL REFERENCES foundries(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_by VARCHAR(36) REFERENCES users(id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    
    CONSTRAINT uk_foundry_team_name UNIQUE (foundry_id, name)
);

CREATE INDEX idx_teams_foundry ON teams(foundry_id);
```

### team_memberships

```sql
CREATE TABLE team_memberships (
    team_id VARCHAR(36) NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    added_by VARCHAR(36) REFERENCES users(id),
    added_at TIMESTAMP NOT NULL DEFAULT NOW(),
    
    PRIMARY KEY (team_id, user_id)
);

CREATE INDEX idx_team_memberships_user ON team_memberships(user_id);
```

### roles

```sql
CREATE TABLE roles (
    id VARCHAR(36) PRIMARY KEY,
    foundry_id VARCHAR(36) REFERENCES foundries(id), -- NULL for built-in roles
    name VARCHAR(100) NOT NULL,
    display_name VARCHAR(255) NOT NULL,
    description TEXT,
    scope_type VARCHAR(20) NOT NULL, -- 'foundry', 'workshop', 'workbench', 'workspace'
    is_builtin BOOLEAN NOT NULL DEFAULT FALSE,
    base_role_id VARCHAR(36) REFERENCES roles(id), -- For custom roles extending built-in
    permissions JSONB NOT NULL DEFAULT '[]',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    
    CONSTRAINT uk_foundry_role_name UNIQUE (foundry_id, name),
    CONSTRAINT chk_scope_type CHECK (scope_type IN ('foundry', 'workshop', 'workbench', 'workspace'))
);

CREATE INDEX idx_roles_foundry ON roles(foundry_id);
CREATE INDEX idx_roles_scope ON roles(scope_type);
```

### role_assignments

```sql
CREATE TABLE role_assignments (
    id VARCHAR(36) PRIMARY KEY,
    foundry_id VARCHAR(36) NOT NULL REFERENCES foundries(id),
    role_id VARCHAR(36) NOT NULL REFERENCES roles(id),
    
    -- Assignee: either user or team (exactly one must be set)
    user_id VARCHAR(36) REFERENCES users(id) ON DELETE CASCADE,
    team_id VARCHAR(36) REFERENCES teams(id) ON DELETE CASCADE,
    
    -- Scope: the entity this assignment applies to
    scope_type VARCHAR(20) NOT NULL,
    scope_id VARCHAR(36) NOT NULL,
    
    assigned_by VARCHAR(36) REFERENCES users(id),
    assigned_at TIMESTAMP NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMP, -- NULL for permanent assignments
    
    CONSTRAINT chk_assignee CHECK (
        (user_id IS NOT NULL AND team_id IS NULL) OR
        (user_id IS NULL AND team_id IS NOT NULL)
    )
);

CREATE INDEX idx_role_assignments_user ON role_assignments(user_id);
CREATE INDEX idx_role_assignments_team ON role_assignments(team_id);
CREATE INDEX idx_role_assignments_scope ON role_assignments(scope_type, scope_id);
CREATE INDEX idx_role_assignments_foundry ON role_assignments(foundry_id);
```

### permission_cache

```sql
CREATE TABLE permission_cache (
    cache_key VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    scope_type VARCHAR(20) NOT NULL,
    scope_id VARCHAR(36) NOT NULL,
    permissions JSONB NOT NULL,
    computed_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP NOT NULL
);

CREATE INDEX idx_permission_cache_user ON permission_cache(user_id);
CREATE INDEX idx_permission_cache_expires ON permission_cache(expires_at);
```

## Integration Details

### Olympus Cipher Integration

**JIT Provisioning Flow:**
```python
def handle_oauth_callback(oauth_token, foundry_id):
    # 1. Exchange token for user info
    cipher_user = cipher_client.get_userinfo(oauth_token)
    
    # 2. Find or create Foundry user
    user = find_user_by_cipher_id(foundry_id, cipher_user.id)
    if not user:
        user = create_user(
            foundry_id=foundry_id,
            cipher_user_id=cipher_user.id,
            email=cipher_user.email,
            display_name=cipher_user.name,
            provisioning_source='jit'
        )
        
        # 3. Assign default role
        assign_role(user.id, 'foundry-member', scope_type='foundry', scope_id=foundry_id)
        
        # 4. Emit event
        emit_event('user.created', user)
    else:
        # Update profile if changed
        update_user_from_cipher(user, cipher_user)
    
    return user
```

**SCIM Push Endpoint:**
```
POST /scim/v2/Users
PATCH /scim/v2/Users/{id}
DELETE /scim/v2/Users/{id}
GET /scim/v2/Users
```

### Metadata Service Integration

Role assignments reference entities in Metadata Service:
- Workshop IDs validated against Metadata Service
- Workbench IDs validated against Metadata Service
- Workspace IDs validated against Metadata Service

### Audit Integration

All mutations logged to audit service:
```python
def create_team(foundry_id, name, created_by):
    team = Team.create(foundry_id=foundry_id, name=name, created_by=created_by)
    
    audit.log(
        foundry_id=foundry_id,
        action='team.created',
        actor_id=created_by,
        resource_type='team',
        resource_id=team.id,
        details={'name': name}
    )
    
    return team
```

## Processing Logic

### Permission Check Algorithm

```python
def check_permission(user_id: str, permission: str, scope_type: str, scope_id: str) -> bool:
    # 1. Check cache
    cache_key = f"{user_id}:{scope_type}:{scope_id}"
    cached = get_cached_permissions(cache_key)
    if cached and permission in cached:
        return True
    
    # 2. Get user's direct role assignments at this scope
    direct_roles = get_role_assignments(user_id=user_id, scope_type=scope_type, scope_id=scope_id)
    for role in direct_roles:
        if permission in role.permissions:
            return True
    
    # 3. Get user's teams and their role assignments
    teams = get_user_teams(user_id)
    for team in teams:
        team_roles = get_role_assignments(team_id=team.id, scope_type=scope_type, scope_id=scope_id)
        for role in team_roles:
            if permission in role.permissions:
                return True
    
    # 4. Check parent scope (inheritance)
    parent_scope = get_parent_scope(scope_type, scope_id)
    if parent_scope:
        return check_permission(user_id, permission, parent_scope.type, parent_scope.id)
    
    return False

def get_parent_scope(scope_type: str, scope_id: str):
    """Returns parent scope for permission inheritance."""
    if scope_type == 'workspace':
        workspace = metadata_service.get_workspace(scope_id)
        return Scope('workbench', workspace.workbench_id)
    elif scope_type == 'workbench':
        workbench = metadata_service.get_workbench(scope_id)
        return Scope('workshop', workbench.workshop_id)
    elif scope_type == 'workshop':
        workshop = metadata_service.get_workshop(scope_id)
        return Scope('foundry', workshop.foundry_id)
    else:
        return None  # Foundry is the top
```

### Bulk Permission Check

```python
def check_permissions_bulk(user_id: str, checks: list[PermissionCheck]) -> dict[str, bool]:
    """Check multiple permissions efficiently."""
    results = {}
    
    # Group by scope to minimize DB queries
    by_scope = group_by_scope(checks)
    
    for scope_key, permissions in by_scope.items():
        scope_type, scope_id = scope_key
        
        # Get all user permissions at this scope (with inheritance)
        user_permissions = get_all_user_permissions(user_id, scope_type, scope_id)
        
        for permission in permissions:
            check_id = f"{permission}:{scope_type}:{scope_id}"
            results[check_id] = permission in user_permissions
    
    return results
```

### Role Assignment Validation

```python
def assign_role(assignee_id: str, assignee_type: str, role_id: str, 
                scope_type: str, scope_id: str, assigned_by: str) -> RoleAssignment:
    # 1. Validate role exists and matches scope
    role = get_role(role_id)
    if role.scope_type != scope_type:
        raise ValidationError(f"Role {role.name} is for {role.scope_type}, not {scope_type}")
    
    # 2. Validate scope entity exists
    entity = validate_scope_entity(scope_type, scope_id)
    if not entity:
        raise ValidationError(f"{scope_type} {scope_id} not found")
    
    # 3. Validate assigner has permission
    can_assign = check_permission(
        assigned_by, 
        f'{scope_type}.roles.assign',
        scope_type,
        scope_id
    )
    if not can_assign:
        raise AuthorizationError("Cannot assign roles at this scope")
    
    # 4. Create assignment
    assignment = RoleAssignment.create(
        role_id=role_id,
        user_id=assignee_id if assignee_type == 'user' else None,
        team_id=assignee_id if assignee_type == 'team' else None,
        scope_type=scope_type,
        scope_id=scope_id,
        assigned_by=assigned_by
    )
    
    # 5. Invalidate permission cache for affected users
    invalidate_permission_cache(assignee_id, assignee_type)
    
    # 6. Audit log
    audit.log(action='role.assigned', ...)
    
    return assignment
```

## Error Handling

| Error Scenario | Error Code | HTTP Status | Handling |
|----------------|------------|-------------|----------|
| User not found | `USER_NOT_FOUND` | 404 | Return clear error message |
| Team not found | `TEAM_NOT_FOUND` | 404 | Return clear error message |
| Role not found | `ROLE_NOT_FOUND` | 404 | Return clear error message |
| Duplicate team name | `TEAM_EXISTS` | 409 | Suggest alternative name |
| Invalid scope | `INVALID_SCOPE` | 400 | Indicate valid scope types |
| Permission denied | `FORBIDDEN` | 403 | Indicate required permission |
| Cipher sync failure | `CIPHER_SYNC_ERROR` | 502 | Retry with backoff, alert on repeated failure |

## Authorization

### Who can manage teams

| Action | Required Permission |
|--------|---------------------|
| Create team | `foundry.teams.write` |
| Update team | `foundry.teams.write` |
| Delete team | `foundry.teams.write` |
| Add team member | `foundry.teams.write` |
| Remove team member | `foundry.teams.write` |

### Who can manage roles

| Action | Required Permission |
|--------|---------------------|
| Create custom role | `foundry.roles.write` |
| Update custom role | `foundry.roles.write` |
| Delete custom role | `foundry.roles.write` |
| Assign role at scope | `{scope}.roles.assign` |
| Revoke role at scope | `{scope}.roles.assign` |

## API Specification

### User APIs

```yaml
# List users
GET /api/v1/foundries/{foundry_id}/users
Query: status, team_id, search, page, limit
Response: { users: [...], pagination: {...} }

# Get user
GET /api/v1/foundries/{foundry_id}/users/{user_id}
Response: { user: {...} }

# Update user
PATCH /api/v1/foundries/{foundry_id}/users/{user_id}
Body: { status, metadata }
Response: { user: {...} }

# Get user permissions (introspection)
GET /api/v1/foundries/{foundry_id}/users/{user_id}/permissions
Query: scope_type, scope_id
Response: { permissions: [...] }
```

### Team APIs

```yaml
# List teams
GET /api/v1/foundries/{foundry_id}/teams
Query: search, page, limit
Response: { teams: [...], pagination: {...} }

# Create team
POST /api/v1/foundries/{foundry_id}/teams
Body: { name, description }
Response: { team: {...} }

# Get team
GET /api/v1/foundries/{foundry_id}/teams/{team_id}
Response: { team: {...}, members: [...] }

# Update team
PATCH /api/v1/foundries/{foundry_id}/teams/{team_id}
Body: { name, description }
Response: { team: {...} }

# Delete team
DELETE /api/v1/foundries/{foundry_id}/teams/{team_id}
Response: 204 No Content

# Add member
POST /api/v1/foundries/{foundry_id}/teams/{team_id}/members
Body: { user_id }
Response: { team: {...}, members: [...] }

# Remove member
DELETE /api/v1/foundries/{foundry_id}/teams/{team_id}/members/{user_id}
Response: 204 No Content
```

### Role APIs

```yaml
# List roles
GET /api/v1/foundries/{foundry_id}/roles
Query: scope_type, is_builtin
Response: { roles: [...] }

# Create custom role
POST /api/v1/foundries/{foundry_id}/roles
Body: { name, display_name, description, scope_type, base_role_id, additional_permissions }
Response: { role: {...} }

# Get role
GET /api/v1/foundries/{foundry_id}/roles/{role_id}
Response: { role: {...}, permissions: [...] }

# Update custom role
PATCH /api/v1/foundries/{foundry_id}/roles/{role_id}
Body: { display_name, description, additional_permissions }
Response: { role: {...} }

# Delete custom role
DELETE /api/v1/foundries/{foundry_id}/roles/{role_id}
Response: 204 No Content
```

### Role Assignment APIs

```yaml
# List role assignments
GET /api/v1/foundries/{foundry_id}/role-assignments
Query: scope_type, scope_id, user_id, team_id
Response: { assignments: [...] }

# Assign role
POST /api/v1/foundries/{foundry_id}/role-assignments
Body: { role_id, user_id|team_id, scope_type, scope_id, expires_at }
Response: { assignment: {...} }

# Revoke role
DELETE /api/v1/foundries/{foundry_id}/role-assignments/{assignment_id}
Response: 204 No Content
```

### Authorization APIs

```yaml
# Check permission
POST /api/v1/authz/check
Body: { user_id, permission, scope_type, scope_id }
Response: { allowed: true|false, reason: "..." }

# Check permissions bulk
POST /api/v1/authz/check-bulk
Body: { user_id, checks: [{ permission, scope_type, scope_id }] }
Response: { results: { "perm:type:id": true|false, ... } }
```

## Scalability

| Aspect | Approach |
|--------|----------|
| Permission check latency | Cache permissions per user/scope with TTL (5 min) |
| Cache invalidation | Invalidate on role assignment change; fan out by team membership |
| Large teams | Pagination for member lists; batch processing for team role lookups |
| Many scopes | Index on (scope_type, scope_id); partition by foundry if needed |

## Observability

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `team_mgmt.users.total` | Gauge | Total users per foundry |
| `team_mgmt.teams.total` | Gauge | Total teams per foundry |
| `team_mgmt.authz.check.latency_ms` | Histogram | Permission check latency |
| `team_mgmt.authz.cache.hit_rate` | Gauge | Permission cache hit rate |
| `team_mgmt.scim.sync.duration_ms` | Histogram | SCIM sync duration |
| `team_mgmt.scim.sync.errors` | Counter | SCIM sync errors |

### Logs

| Event | Log Level | Content |
|-------|-----------|---------|
| User created | INFO | User ID, provisioning source, foundry |
| Role assigned | INFO | User/team, role, scope |
| Permission denied | WARN | User, permission, scope |
| SCIM sync error | ERROR | Error details, retry info |

### Alerts

| Condition | Severity | Action |
|-----------|----------|--------|
| Permission check p99 > 100ms | Warning | Investigate cache, query performance |
| SCIM sync failing > 5 min | High | Check Cipher connectivity |
| Cache hit rate < 50% | Warning | Review cache TTL, invalidation patterns |

## Open Implementation Questions

- Should we support nested teams (team contains teams)?
- How to handle deprovisioned users with pending Work Orders?
- Should role assignments be audited with before/after diffs?
- How to handle timezone for time-bound role assignments?
- Should we provide a "preview" mode for permission changes?

## Read Next

- [README.md](README.md) — Team Management overview
- [../foundry-management/README.md](../foundry-management/README.md) — Foundry Admin context
- [../../agent-fabric/README.md](../../agent-fabric/README.md) — Agent credentials (separate from user credentials)
