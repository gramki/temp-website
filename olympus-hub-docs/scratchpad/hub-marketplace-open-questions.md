# Marketplace Subsystem - Open Questions Summary

> **Generated:** 2026-01-XX  
> **Status:** Active design phase  
> **Purpose:** Consolidated list of open questions requiring decisions

---

## High Priority - Core Functionality

### Topic 10: Integration with Existing Subsystems ✅ **RESOLVED**

**Status:** Integration points defined and documented

**Resolved:**
1. **Artifact Registry Integration** ✅
   - Marketplace maintains its own artifact repository (Marketplace Artifact Repository)
   - Clones packages from source subscriptions during publishing
   - Containers referenced by Blueprints cloned lazily into tenant artifact repository (only when first used)
   - Lazy container cloning reduces subscription overhead

2. **Promotion Model Integration** ✅
   - When Blueprint-derived resources promoted to new workbench, target workbench automatically gets package subscription
   - Package subscription created automatically as part of deployment workflow
   - Platform operators create this subscription (not manual user action)
   - Ensures Blueprint reference tracking across workbenches

3. **Workbench Management Integration** ✅
   - BlueprintSpecs become available upon subscription (not directly part of workbench)
   - Workbench Management handles creation of derived resources from BlueprintSpecs
   - Derived resources (regular specs) created from BlueprintSpecs when used
   - Blueprint reference section added to derived resources for update tracking

4. **Registry Services Integration** ✅
   - Blueprints can reference platform-provided resources (e.g., platform Machine Definitions)
   - Registry Services resolves Tool/Machine dependencies when creating derived resources
   - Validates Tool Protocol compatibility
   - Handles Machine Definition dependencies

5. **Notification Services Integration** ✅
   - Publishing notifications (to admin, publisher)
   - Deployment notifications (when Blueprint-derived resources are created)
   - Update notifications (when new Blueprint versions are available)
   - Security issue notifications (vulnerabilities, blacklisting)
   - Subscription status notifications (approval, rejection, availability)

---

### Topic 6: Deployment Model ✅ **RESOLVED**

**Status:** Deployment model fully defined with BlueprintSpec transformation

**Resolved:**
1. **BlueprintSpec Transformation** ✅
   - Export transforms regular specs to BlueprintSpec types (e.g., ScenarioNormativeSpec → ScenarioBlueprintSpec)
   - Subscription makes BlueprintSpecs available/usable in workbench
   - Usage requires creating derived resources from BlueprintSpecs
   - Blueprints never become part of workbench definition directly

2. **Deployment Mechanism** ✅
   - BlueprintSpecs become available upon subscription
   - Derived resources (regular specs) created from BlueprintSpecs when used
   - Containers cloned lazily (only when Scenario Deployment references container)
   - No direct copy - uses BlueprintSpec → derived resource transformation

3. **Blueprint Reference Tracking** ✅
   - Structure includes: Package SHA, Package URI, BlueprintSpec name/type, version
   - Enables update workflow and tracking
   - Modified resources remain derived but become divergent; manual merges can be applied

4. **Container Handling** ✅
   - Containers NOT cloned during subscription
   - Cloned into tenant artifact repository only when Scenario Deployment references container
   - Container updates only when derived resource updated; doesn't impact running pods until rollout

5. **Unsubscription Model** ✅
   - Blueprints become invisible, subscription marked "pending-unsubscription"
   - Manual deletion of derived resources required to complete unsubscription
   - When deployments deleted, containers evicted; runtimes impacted if not scaled down

6. **Cross-Workbench Deployment** ✅
   - When Blueprint-derived resource promoted, target workbench automatically gets package subscription
   - Created by platform operators as part of deployment workflow

---

## Medium Priority - Design Details

### Topic 2: Marketplace Catalog Architecture

**Status:** Metadata schema defined, category structure pending

**Resolved:**
1. **Metadata Schema** ✅
   - **Required Fields**: Package identity (ID, name, version, URI), product info (short description, artifact types), publisher info (ID, name), package contents (blueprints, SHA), visibility controls, system metadata
   - **Optional Fields**: Enhanced product info (long description, release notes, keywords, categories), publisher support info, deployment instructions, documentation/media, compliance info, container details
   - **Validation Rules**: Field format validation, content validation, required field checks
   - **Minimum Viable**: All required fields + at least one discoverability field (long_description, keywords, or categories)
   - Complete schema documented in exploration document

**Resolved:**
2. **Category/Taxonomy Structure** ✅
   - **Flat tag-based categorization** (no hierarchical structure)
   - Publishers can assign multiple free-form tags
   - Tags stored in `categories`, `industry_tags`, and `keywords` fields (all optional)
   - No validation of tag values (publishers have freedom)
   - All tags indexed in OpenSearch for filtering and search
   - Marketplace Console may suggest common tags (UI enhancement, not validation)
   - Future: May evolve to curated suggestions, but v1 is free-form

**Design Decisions Needed:**
- [x] Metadata schema (required vs optional fields) - ✅ **Defined**
- [x] Category/taxonomy structure - ✅ **Flat tag-based** (decided)

---

### Topic 4: Discovery and Search ✅ **RESOLVED** (Implementation Details)

**Status:** UI/UX patterns defined (implementation-level details)

**Resolved:**
1. **Discovery UI Patterns** ✅
   - Browse by Publisher and Category
   - Search functionality
   - (Note: These are implementation details, not core system design)

2. **Search Query Syntax** ✅
   - Simple text search
   - Full-text search via OpenSearch
   - (Note: Implementation detail)

3. **Filtering Capabilities** ✅
   - All suggested filters available
   - Multi-select filters supported
   - Filters include: artifact types, categories, industry_tags, keywords, publisher, etc.
   - (Note: Implementation detail)

4. **Sorting Options** ✅
   - Sort by relevancy
   - Sort by recency
   - (Note: Implementation detail)

5. **Result Display Format** ✅
   - List view format
   - Clicking on listing takes to full listing details page
   - (Note: Implementation detail)

**Note:** These are implementation-level UI/UX details. The core system design (OpenSearch-based catalog with filtering and search capabilities) supports these patterns but doesn't prescribe specific UI implementations.

---

### Topic 7: Cross-Subscription and Cross-Tenant Sharing ✅ **RESOLVED**

**Status:** Security boundaries and credential handling fully defined

**Resolved:**
1. **Security Boundaries** ✅
   - **Federated IAM**: Marketplace accessed through federated IAM
     - All Tenant IAM Domains federate with Marketplace IAM
     - Requests from Tenant Users authenticated and attributed to federated identity
     - Reference to tenant domain identity maintained
   - **PII Protection**: No PII beyond desensitized name used for Marketplace profile
   - **Identity & Authentication**: Publishers and Subscribers always identified and authenticated
   - **Artifact Integrity**:
     - Artifacts are immutable and signed
     - Signatures verified by Marketplace
     - Marketplace distributed containers signed by Marketplace private key
     - Subscribers can verify integrity using Marketplace's public key
     - End-to-end integrity: Publisher signature → Marketplace signature → Subscriber verification

**Resolved:**
2. **Credential Handling Strategy** ✅
   - **Packages must NOT contain any credentials**
   - Packages are validated to ensure no credentials are included
   - **Subscribers provide their own credentials** when deploying/using packages
   - Marketplace does not interfere with any credential-related matters
   - Credential management is entirely the responsibility of subscribers
   - This ensures security and prevents credential leakage through packages

**Design Decisions Needed:**
- [x] Security boundaries (detailed) - ✅ **Federated IAM, artifact signing, integrity verification** (decided)
- [x] Credential handling strategy - ✅ **No credentials in packages; Subscribers provide their own; Marketplace stays out** (decided)

---

### Topic 11: UI/UX and Developer Experience

**Status:** CLI command set defined; workflow design out of scope

**Resolved:**
1. **CLI Command Set** ✅

   **Publisher Commands:**
   - `hub marketplace publish <package-manifest-crd>` - Publish a package to Marketplace
   - `hub marketplace packages list` - List all packages published by current publisher
   - `hub marketplace packages get <package-id>` - Get details of a published package
   - `hub marketplace packages update <package-id> <version>` - Publish new version of a package
   - `hub marketplace packages withdraw <package-id>` - Withdraw a package from Marketplace
   - `hub marketplace packages deprecate <package-id>` - Deprecate a package

   **Subscriber Commands:**
   - `hub marketplace search <query>` - Search packages in Marketplace
   - `hub marketplace browse [--publisher <publisher-id>] [--category <category>]` - Browse packages
   - `hub marketplace packages get <package-id>` - Get details of a package
   - `hub marketplace subscribe <package-id> [--workbench <workbench-id>]` - Subscribe to a package
   - `hub marketplace subscriptions list` - List all package subscriptions for current tenant/workbench
   - `hub marketplace subscriptions get <subscription-id>` - Get details of a subscription
   - `hub marketplace subscriptions update <subscription-id> <version>` - Update subscription to new version
   - `hub marketplace subscriptions unsubscribe <subscription-id>` - Unsubscribe from a package

   **Common Commands:**
   - `hub marketplace publishers list` - List all publishers
   - `hub marketplace publishers get <publisher-id>` - Get publisher details
   - `hub marketplace status` - Show Marketplace connection status and authentication

   **Command Flags:**
   - `--output <format>` - Output format (table, yaml, json, wide)
   - `--workbench <workbench-id>` - Specify workbench context
   - `--version <version>` - Specify package version (semver or range)
   - `--verbose` - Verbose output
   - `--quiet` - Minimal output

   **Note:** Detailed workflow design (step-by-step workflows, error handling, progress indicators) is out of scope at this stage.

**Design Decisions Needed:**
- [x] CLI command set - ✅ **Defined above** (decided)
- [ ] Workflow design (detailed) - ⏸️ **Out of scope at this stage**

---

## Lower Priority - Operational & Compliance

### Topic 12: Audit Trail and Compliance

**Open Questions:**
1. **Audit Event Inventory**
   - Complete list of events to audit?
   - Publishing events (what details)?
   - Deployment events (what details)?
   - Access events (who viewed what)?
   - Security scan events?

2. **Audit Log Schema**
   - What data captured (actor, timestamp, artifact details, target, outcome)?
   - Log format and structure?
   - Retention requirements?

3. **Audit Storage Mechanism**
   - CAF integration?
   - Separate audit store?
   - Queryable by tenant admin?
   - Queryable by platform admin?

4. **Compliance Requirements**
   - Data residency (cross-tenant sharing)?
   - Export controls?
   - Intellectual property tracking?
   - Regulatory compliance (SOX, GDPR, etc.)?

**Design Decisions Needed:**
- [ ] Audit event inventory (complete)
- [ ] Audit log schema
- [ ] Audit storage mechanism
- [ ] Compliance requirements

---

### Topic 13: Operational Concerns

**Open Questions:**
1. **Service Deployment Model**
   - Platform-level service deployment details?
   - Per-tenant instance or shared?
   - Infrastructure requirements?

2. **Scalability Architecture**
   - Expected number of listings?
   - Search performance targets?
   - Deployment concurrency limits?
   - Cross-tenant isolation mechanisms?

3. **Monitoring Strategy**
   - What metrics to track?
   - Publishing metrics?
   - Deployment metrics?
   - Search performance?
   - Error rates?
   - Alerting thresholds?

4. **Data Retention Policies**
   - Listing retention (deprecated/withdrawn)?
   - Installation history retention?
   - Audit log retention?
   - Security scan result retention?

5. **Failure Handling Strategy**
   - Deployment failure handling?
   - Dependency resolution failure handling?
   - Partial deployment rollback?
   - Retry mechanisms?

**Design Decisions Needed:**
- [ ] Service deployment model
- [ ] Scalability architecture
- [ ] Monitoring strategy
- [ ] Data retention policies
- [ ] Failure handling strategy

---

### Topic 14: Future Enhancements

**Open Questions:**
1. **v1 Scope Boundaries**
   - What features explicitly out of scope?
   - Commercial model (licensing, payment)?
   - Ratings and reviews?
   - Usage analytics for publishers?
   - Marketplace APIs for external integrations?
   - Automated dependency updates?
   - Marketplace curation (featured listings)?

2. **Extensibility Points**
   - How to design v1 to enable future features?
   - Extensible metadata schema?
   - Plugin architecture?
   - API design for future extensions?

3. **Future Feature Hooks**
   - What hooks/extension points to include in v1?
   - Plugin interfaces?
   - Event system for future integrations?

**Design Decisions Needed:**
- [ ] v1 scope boundaries (explicit list)
- [ ] Extensibility points
- [ ] Future feature hooks

---

## Additional Resolved Topics

### Topic 8: Version Management and Updates ✅ **RESOLVED**

**Resolved:**
- ✅ Semver semantics for package versions
- ✅ Minor versions must be in-place upgradable (backward compatible)
- ✅ No automatic update propagation; explicit pull required
- ✅ Semver compatibility range references supported
- ✅ New version availability notified to all package-subscribers
- ✅ **Update Workflow: Hybrid** - System suggests, user approves
- ✅ **Derived Resource Modification**: Modified resources become divergent; manual merges can be applied
- ✅ **Partial Updates**: Nothing forced; out-of-sync resources shown in Marketplace Console
- ✅ **Withdrawn Blueprints**: Derived resources continue to work until fully unsubscribed, marked as "Orphaned and unsupported"

### Topic 3: Publishing Workflow ✅ **RESOLVED**
- ✅ Publisher registration required (Hub Win approval)
- ✅ Package Manifest CRD created by developer
- ✅ Publishing via Automation Developer Desk
- ✅ Admin approval required before submission
- ✅ Security scanning and quarantine process
- ✅ Container signing and validation

### Topic 9: Access Control ✅ **RESOLVED**
- ✅ Publisher permissions: Registered publishers only
- ✅ Discovery permissions: Users from Agent Developer Desk, Scenario Design Desk, Automation Product Desk, Admin Desk
- ✅ Deployment permissions: Admin approval required for subscriptions
- ✅ Publisher allow/disallow lists (Apache-style, managed by authorized people)

### Topic 2: Marketplace Catalog Architecture ✅ **RESOLVED**
- ✅ Complete metadata schema defined (required vs optional fields)
- ✅ Flat tag-based categorization (no hierarchical structure)
- ✅ Publishers assign free-form tags (no validation)
- ✅ Tags stored in `categories`, `industry_tags`, and `keywords` fields
- ✅ All tags indexed in OpenSearch for filtering and search
- ✅ Marketplace Console may suggest common tags (UI enhancement)

### Topic 4: Discovery and Search ✅ **RESOLVED** (Implementation Details)
- ✅ Browse by Publisher and Category
- ✅ Simple text search (full-text search via OpenSearch)
- ✅ All suggested filters with multi-select capability
- ✅ Sort by relevancy and recency
- ✅ List view format; clicking takes to full listing details
- **Note:** These are implementation-level UI/UX details, not core system design

### Topic 7: Cross-Subscription and Cross-Tenant Sharing ✅ **RESOLVED**
- ✅ **Federated IAM**: All Tenant IAM Domains federate with Marketplace IAM
- ✅ **Authentication**: Requests authenticated and attributed to federated identity
- ✅ **PII Protection**: No PII beyond desensitized name for Marketplace profile
- ✅ **Identity & Authentication**: Publishers and Subscribers always identified and authenticated
- ✅ **Artifact Integrity**: Artifacts immutable and signed; signatures verified by Marketplace
- ✅ **Marketplace Signing**: Distributed containers signed by Marketplace private key
- ✅ **Subscriber Verification**: Subscribers can verify integrity using Marketplace's public key
- ✅ **End-to-End Integrity**: Publisher signature → Marketplace signature → Subscriber verification
- ✅ **Credential Handling**: Packages must NOT contain credentials; Subscribers provide their own; Marketplace stays out

### Topic 11: UI/UX and Developer Experience ✅ **RESOLVED** (CLI Defined)
- ✅ **CLI Command Set**: Complete command set defined for publishers, subscribers, and common operations
- ✅ **Publisher Commands**: publish, list, get, update, withdraw, deprecate
- ✅ **Subscriber Commands**: search, browse, subscribe, subscriptions list/get/update/unsubscribe
- ✅ **Common Commands**: publishers list/get, status
- ✅ **Command Flags**: --output, --workbench, --version, --verbose, --quiet
- ⏸️ **Workflow Design**: Out of scope at this stage

---

## Summary by Priority

### ✅ Resolved (Core Design Complete)
1. ✅ **Topic 10: Integration with Existing Subsystems** - All integration points defined
2. ✅ **Topic 6: Deployment Model** - BlueprintSpec transformation model fully defined
3. ✅ **Topic 8: Version Management** - Update workflow and Blueprint update mechanism defined
4. ✅ **Topic 3: Publishing Workflow** - Complete workflow with security scanning
5. ✅ **Topic 9: Access Control** - Permissions model defined
6. ✅ **Topic 7: Cross-Subscription and Cross-Tenant Sharing** - Security boundaries and credential handling fully defined
7. ✅ **Topic 11: UI/UX and Developer Experience** - CLI command set defined (workflow design out of scope)

### 🟡 Important (Affects User Experience)
1. **Topic 4: Discovery and Search** - UI/UX details (resolved - implementation details)
2. **Topic 11: CLI Commands** - Developer experience

**Note:** Topic 2 (Metadata Schema & Category Structure) ✅ **FULLY RESOLVED**

### 🟢 Nice to Have (Operational Excellence)
1. **Topic 12: Audit Trail** - Compliance requirements
2. **Topic 13: Operational Concerns** - Scalability and monitoring
3. **Topic 7: Credential Handling** - Credential/secret management strategy (Security boundaries ✅ resolved)
4. **Topic 14: Future Enhancements** - Scope boundaries

**Note:** Topic 7 (Security Boundaries) ✅ **RESOLVED** - Federated IAM, artifact signing, integrity verification defined

---

## Recommended Discussion Order

### ✅ Completed
1. ✅ **Topic 10** (Integration) - All integration points resolved
2. ✅ **Topic 6** (Deployment Model) - BlueprintSpec transformation model complete
3. ✅ **Topic 8** (Version Management) - Update workflow defined
4. ✅ **Topic 3** (Publishing Workflow) - Complete workflow defined
5. ✅ **Topic 9** (Access Control) - Permissions model defined

### Next Priority
1. **Topic 2** (Metadata Schema) - Needed for implementation
2. **Topic 4** (Discovery UI) - User-facing feature
3. **Topic 11** (CLI) - Developer experience
4. **Topic 7** (Security Details) - Basic model defined, details can be refined
5. **Topic 12-14** (Operations & Future) - Can be addressed as implementation progresses

---

---

## Topic 15: Hub Application Blueprints

**Status:** ✅ Resolved

**Question:** Should Hub Applications be publishable as Blueprints with build recipes for DSL runtimes?

**Resolution:**
- Introduced `HubApplicationBlueprintSpec` as new BlueprintSpec type
- Build Recipe mechanism with `copy-only` and `buildpack` types
- Sandboxed build environment in CI
- OCI layer deduplication prevents registry bloat
- Full documentation created (ADR-0102, subsystem docs, guides)

---

## Notes

- **Core design is complete**: BlueprintSpec model, deployment mechanism, integration points all resolved
- **Remaining questions** focus on UI/UX details, metadata schema, and operational concerns
- **Blueprint update mechanism** fully defined: Hybrid workflow with divergent resource handling
- **Container cloning** strategy: Lazy cloning on first Scenario Deployment reference
- **Cross-workbench promotion** automatically creates package subscriptions via platform operators
- **Hub Application Blueprints** added: Enables publishing reusable application containers with build recipes