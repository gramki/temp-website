# Internal Implementation

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Overview

This document describes the internal implementation of Cipher IAM Extensions, including profile storage, authority delegation storage, and policy attachment mechanisms.

---

## Profile Storage

### Storage Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PROFILE STORAGE ARCHITECTURE                          │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    PRIMARY STORAGE                                   │   │
│   │                    (PostgreSQL)                                      │   │
│   │                                                                       │   │
│   │   • Agent profiles (main table)                                      │   │
│   │   • Delegation records                                               │   │
│   │   • Policy attachments                                               │   │
│   │   • Credential mappings                                              │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                          │                                                   │
│                    Write │ Read                                             │
│                          ▼                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    CACHE LAYER                                       │   │
│   │                    (Redis)                                           │   │
│   │                                                                       │   │
│   │   • Profile lookup cache                                             │   │
│   │   • Delegation chain cache                                           │   │
│   │   • Virtual key mappings                                             │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Database Schema

```sql
-- Agent Profiles
CREATE TABLE agent_profiles (
    id VARCHAR(255) PRIMARY KEY,
    type VARCHAR(50) NOT NULL,  -- 'raw', 'trained', 'employed'
    status VARCHAR(50) NOT NULL,  -- 'active', 'revoked', 'deleted'
    
    -- Identity
    spiffe_id VARCHAR(500),
    subscription VARCHAR(255) NOT NULL,
    workbench VARCHAR(255),
    
    -- Delegation
    delegation_type VARCHAR(50),  -- 'user', 'role', 'bot'
    delegator VARCHAR(255),
    accountable VARCHAR(255) NOT NULL,
    
    -- Metadata
    version INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    
    -- JSON for flexible storage
    tags JSONB,
    metadata JSONB
);

-- Inherited Roles
CREATE TABLE profile_roles (
    profile_id VARCHAR(255) REFERENCES agent_profiles(id),
    role VARCHAR(255) NOT NULL,
    inherited_from VARCHAR(255),  -- delegator or explicit
    PRIMARY KEY (profile_id, role)
);

-- Inherited Groups
CREATE TABLE profile_groups (
    profile_id VARCHAR(255) REFERENCES agent_profiles(id),
    group_name VARCHAR(255) NOT NULL,
    inherited_from VARCHAR(255),
    PRIMARY KEY (profile_id, group_name)
);

-- Policy Attachments
CREATE TABLE profile_policies (
    profile_id VARCHAR(255) REFERENCES agent_profiles(id),
    pep VARCHAR(100) NOT NULL,
    policy_ref VARCHAR(500) NOT NULL,
    status VARCHAR(50) NOT NULL,  -- 'loaded', 'error', 'pending'
    PRIMARY KEY (profile_id, pep)
);

-- Credentials
CREATE TABLE profile_credentials (
    profile_id VARCHAR(255) REFERENCES agent_profiles(id),
    credential_type VARCHAR(50) NOT NULL,
    credential_id VARCHAR(255) NOT NULL,
    vault_path VARCHAR(500),
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP,
    PRIMARY KEY (profile_id, credential_type)
);

-- Indexes
CREATE INDEX idx_profiles_subscription ON agent_profiles(subscription);
CREATE INDEX idx_profiles_workbench ON agent_profiles(workbench);
CREATE INDEX idx_profiles_delegator ON agent_profiles(delegator);
CREATE INDEX idx_profiles_accountable ON agent_profiles(accountable);
CREATE INDEX idx_profiles_status ON agent_profiles(status);
```

### Profile Retrieval

```python
class ProfileStore:
    """Storage layer for agent profiles."""
    
    def __init__(self, db, cache):
        self.db = db
        self.cache = cache
    
    async def get(self, profile_id: str) -> Optional[AgentProfile]:
        """Get profile by ID with caching."""
        
        # Check cache first
        cached = await self.cache.get(f"profile:{profile_id}")
        if cached:
            return AgentProfile.from_dict(cached)
        
        # Query database
        profile = await self._query_profile(profile_id)
        if profile:
            # Cache for 5 minutes
            await self.cache.set(
                f"profile:{profile_id}",
                profile.to_dict(),
                ttl=300
            )
        
        return profile
    
    async def _query_profile(self, profile_id: str) -> Optional[AgentProfile]:
        """Query profile from database."""
        
        # Get main profile
        row = await self.db.fetchone(
            "SELECT * FROM agent_profiles WHERE id = $1",
            profile_id
        )
        if not row:
            return None
        
        # Get roles
        roles = await self.db.fetch(
            "SELECT role FROM profile_roles WHERE profile_id = $1",
            profile_id
        )
        
        # Get groups
        groups = await self.db.fetch(
            "SELECT group_name FROM profile_groups WHERE profile_id = $1",
            profile_id
        )
        
        # Get policies
        policies = await self.db.fetch(
            "SELECT pep, policy_ref, status FROM profile_policies WHERE profile_id = $1",
            profile_id
        )
        
        # Get credentials
        credentials = await self.db.fetch(
            "SELECT * FROM profile_credentials WHERE profile_id = $1",
            profile_id
        )
        
        return AgentProfile.from_rows(row, roles, groups, policies, credentials)
```

---

## Authority Delegation Storage

### Delegation Chain Storage

```sql
-- Delegation Chain for audit and resolution
CREATE TABLE delegation_chains (
    id SERIAL PRIMARY KEY,
    agent_profile_id VARCHAR(255) REFERENCES agent_profiles(id),
    level INTEGER NOT NULL,
    identity VARCHAR(255) NOT NULL,
    identity_type VARCHAR(50) NOT NULL,  -- 'agent', 'delegator', 'accountable'
    created_at TIMESTAMP NOT NULL
);

-- Delegation History (for auditing)
CREATE TABLE delegation_history (
    id SERIAL PRIMARY KEY,
    agent_profile_id VARCHAR(255) REFERENCES agent_profiles(id),
    event_type VARCHAR(50) NOT NULL,  -- 'created', 'updated', 'revoked'
    previous_delegator VARCHAR(255),
    new_delegator VARCHAR(255),
    previous_accountable VARCHAR(255),
    new_accountable VARCHAR(255),
    changed_by VARCHAR(255) NOT NULL,
    reason TEXT,
    created_at TIMESTAMP NOT NULL
);
```

### Delegation Resolution

```python
class DelegationStore:
    """Storage layer for delegation chains."""
    
    async def get_delegation_chain(self, profile_id: str) -> DelegationChain:
        """Get full delegation chain for a profile."""
        
        rows = await self.db.fetch(
            """
            SELECT level, identity, identity_type 
            FROM delegation_chains 
            WHERE agent_profile_id = $1 
            ORDER BY level
            """,
            profile_id
        )
        
        return DelegationChain(
            profile_id=profile_id,
            chain=[
                DelegationLevel(
                    level=row['level'],
                    identity=row['identity'],
                    type=row['identity_type']
                )
                for row in rows
            ]
        )
    
    async def store_delegation_chain(
        self, 
        profile_id: str, 
        delegator: str, 
        accountable: str
    ):
        """Store delegation chain for a profile."""
        
        # Clear existing chain
        await self.db.execute(
            "DELETE FROM delegation_chains WHERE agent_profile_id = $1",
            profile_id
        )
        
        # Insert new chain
        chain = [
            (0, profile_id, 'agent'),
        ]
        if delegator:
            chain.append((1, delegator, 'delegator'))
            chain.append((2, accountable, 'accountable'))
        else:
            chain.append((1, accountable, 'accountable'))
        
        await self.db.executemany(
            """
            INSERT INTO delegation_chains 
            (agent_profile_id, level, identity, identity_type, created_at)
            VALUES ($1, $2, $3, $4, NOW())
            """,
            [(profile_id, level, identity, itype) for level, identity, itype in chain]
        )
```

---

## Policy Attachment Mechanisms

### Policy Storage

```python
class PolicyStore:
    """Storage layer for policy attachments."""
    
    async def attach_policy(
        self, 
        profile_id: str, 
        pep: str, 
        policy_ref: str
    ):
        """Attach policy to profile for a PEP."""
        
        # Check if PEP is registered
        if not await self.pep_registry.is_registered(pep):
            log.warning(f"Unknown PEP '{pep}' - storing but not loading")
            status = 'pending'
        else:
            # Load policy to OPA
            try:
                await self.opa_client.load_policy(
                    path=f"agents/{profile_id}/{pep}",
                    policy_ref=policy_ref
                )
                status = 'loaded'
            except PolicyLoadError as e:
                log.error(f"Failed to load policy: {e}")
                status = 'error'
        
        # Store attachment
        await self.db.execute(
            """
            INSERT INTO profile_policies (profile_id, pep, policy_ref, status)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (profile_id, pep) 
            DO UPDATE SET policy_ref = $3, status = $4
            """,
            profile_id, pep, policy_ref, status
        )
    
    async def detach_policy(self, profile_id: str, pep: str):
        """Detach policy from profile."""
        
        # Remove from OPA
        await self.opa_client.delete_policy(f"agents/{profile_id}/{pep}")
        
        # Remove from database
        await self.db.execute(
            "DELETE FROM profile_policies WHERE profile_id = $1 AND pep = $2",
            profile_id, pep
        )
```

### OPA Bundle Management

```python
class OPABundleManager:
    """Manages OPA policy bundles for agents."""
    
    async def load_policy(self, path: str, policy_ref: str):
        """Load policy into OPA."""
        
        # Fetch policy content
        policy_content = await self.policy_store.fetch(policy_ref)
        
        # Upload to OPA
        await self.opa_client.put_policy(
            path=path,
            content=policy_content
        )
    
    async def create_agent_bundle(self, profile_id: str, policies: list):
        """Create complete policy bundle for agent."""
        
        bundle_path = f"bundles/agents/{profile_id}"
        
        # Create bundle manifest
        manifest = {
            "roots": [f"agents/{profile_id}"],
            "revision": str(uuid.uuid4())
        }
        
        # Upload each policy
        for policy in policies:
            await self.load_policy(
                f"agents/{profile_id}/{policy.pep}",
                policy.policy_ref
            )
        
        # Store manifest
        await self.bundle_store.store(bundle_path, manifest)
```

---

## Integration with Cipher Core IAM

### Extending Core IAM

Cipher IAM Extensions registers with Core IAM:

```python
class CipherIAMExtension:
    """Extension registration with Cipher Core IAM."""
    
    def register(self):
        """Register extension with Core IAM."""
        
        # Register identity type
        core_iam.register_identity_type(
            type_id="agent",
            schema=AgentProfileSchema,
            validator=agent_profile_validator
        )
        
        # Register delegation type
        core_iam.register_delegation_type(
            type_id="agent_delegation",
            resolver=AgentDelegationResolver()
        )
        
        # Register credential type
        core_iam.register_credential_type(
            type_id="virtual_key",
            issuer=VirtualKeyIssuer(),
            validator=virtual_key_validator
        )
```

### Core IAM Hooks

Extensions hook into Core IAM events:

```python
@core_iam.on_identity_deleted
async def handle_delegator_deleted(identity_id: str):
    """Handle when a delegator is deleted."""
    
    # Find agents delegating from this identity
    agents = await profile_store.find_by_delegator(identity_id)
    
    for agent in agents:
        # Mark profile as requiring re-delegation
        await profile_store.update(agent.id, {
            "status": "delegation_invalid",
            "delegation_warning": f"Delegator {identity_id} no longer exists"
        })
        
        # Notify accountable human
        await notifications.send(
            to=agent.delegation.accountable,
            subject=f"Agent {agent.id} requires re-delegation",
            body=f"Delegator {identity_id} has been deleted"
        )
```

---

## Cache Invalidation

### Cache Strategy

```python
class ProfileCacheManager:
    """Manages cache invalidation for profiles."""
    
    async def invalidate_profile(self, profile_id: str):
        """Invalidate all cached data for a profile."""
        
        await self.cache.delete(f"profile:{profile_id}")
        await self.cache.delete(f"delegation:{profile_id}")
        await self.cache.delete(f"credentials:{profile_id}")
    
    async def invalidate_by_delegator(self, delegator_id: str):
        """Invalidate all profiles delegating from an identity."""
        
        # Get all affected profiles
        pattern = f"profile:*:delegator:{delegator_id}"
        keys = await self.cache.scan(pattern)
        
        for key in keys:
            await self.cache.delete(key)
```

---

## Related Documentation

- [Architecture](./architecture.md) — Storage architecture overview
- [Agent Profile API](./agent-profile-api.md) — API layer above storage
- [Integration Patterns](./integration-patterns.md) — How components use storage

---

*Internal Implementation provides the storage and management foundation for Cipher IAM Extensions.*
