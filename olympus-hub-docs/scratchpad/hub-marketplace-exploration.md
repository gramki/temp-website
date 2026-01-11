# Marketplace Subsystem - Discussion Plan

> **Purpose:** Break down Marketplace design into focused discussion topics  
> **Approach:** One topic per discussion session  
> **Status:** 🟡 Planning Phase

---

## Quick Reference: Decisions Made

> *As we make decisions, capture them here for quick reference*

| Topic | Key Decision | Status |
|-------|--------------|--------|
| Topic 1: Scope and Artifact Types | Hub Package (collection of Blueprints) is atomic unit; Package manifest with visibility controls | ✅ Decided |
| Topic 2: Marketplace Catalog Architecture | Platform service; OpenSearch-based catalog storage; Tenant-private via visibility controls; Complete metadata schema; Flat tag-based categorization | ✅ Decided |
| Topic 3: Publishing Workflow | Package Manifest CRD; Publish via Automation Developer Desk; Admin approval; Security scanning & quarantine | ✅ Decided |
| Topic 4: Discovery and Search | Store-front accessible from Agent Developer Desk, Scenario Design Desk, Automation Product Desk; UI patterns defined (implementation details) | ✅ Decided |
| Topic 5: Dependency Resolution | Packages can reference platform resources; No cross-package dependencies; Package-subscription isolation | ✅ Decided |
| Topic 6: Deployment Model | Subscription workflow: User initiates, Admin approves, resources added to workbench | ✅ Decided |
| Topic 7: Cross-Subscription and Cross-Tenant Sharing | Platform service; Tenant-private via package visibility controls; Federated IAM; Artifact signing and integrity verification; No credentials in packages | ✅ Decided |
| Topic 8: Version Management and Updates | Semver semantics; Minor versions in-place upgradable; Explicit pull; Notify subscribers; Semver range references | ✅ Decided |
| Topic 9: Access Control and Permissions | Tenant Admin allow/disallow list of publishers (Apache-style); Admin approval for subscriptions | ✅ Decided |
| Topic 11: UI/UX | Marketplace Console (unified console) accessible from Agent Developer Desk, Scenario Design Desk, Automation Product Desk, Admin Desk; CLI command set defined | ✅ Decided |
| Topic 12: Audit Trail and Compliance | Security scanning, quarantine, continuous monitoring, blacklisting | ✅ Decided |
| Topic 13: Operational Concerns | Quarantine infrastructure, continuous scanning, package subscription tracking | ✅ Decided |
| Topic 10: Integration with Existing Subsystems | Artifact Registry (lazy container cloning), Promotion Model (auto-subscription), Workbench Management (derived resources), Registry Services, Notification Services | ✅ Decided |
| Topic 14: Future Enhancements | | ⏳ Pending |

---

## Discussion Structure

Each discussion topic includes:
- **Key Questions** - What needs to be decided
- **Design Decisions** - Specific choices to make
- **Constraints** - Existing Hub patterns to respect
- **Dependencies** - What other topics this affects
- **Related Subsystems** - Integration points to consider

---

## Topic 1: Scope and Artifact Types

### Key Questions
1. Which artifact types should be publishable in v1?
   - Scenarios (complete with all 3 specs)?
   - Hub Applications (standalone)?
   - Tool Protocols?
   - Machine Definitions?
   - Knowledge Bases?
   - Workbench Templates?
   - Notification Templates?
   - Others?

2. What is the atomic unit of publishing?
   - Scenario (as in Promotion Model)?
   - Individual artifact types?
   - Composite bundles?

3. Should there be a hierarchy of publishable units?
   - Scenario → includes Hub Application + Triggers + etc.
   - Workbench Template → includes multiple Scenarios

### Design Decisions Needed
- [ ] Final list of artifact types for v1
- [ ] Atomic publishing unit definition
- [ ] Whether to support composite bundles
- [ ] Versioning strategy per artifact type

### Constraints
- Promotion Model uses Scenario as atomic unit
- Artifact Registry manages OCI containers + CRDs
- Workbench Management defines workbench structure

### Dependencies
- Affects: Publishing workflow, Deployment model, Dependency resolution

### Related Subsystems
- Artifact Registry (artifact storage)
- Promotion Model (atomic units)
- Workbench Management (workbench structure)

### Thoughts and Answers

**Key Decision: Hub Package is the atomic unit of publishing**

A Developer can publish a **"Hub Package"** to the Marketplace. A Hub Package is a collection of **"Blueprints"** - which are Definitions/Specifications that are exported into a package for distribution.

**Why "Blueprint" terminology?**
- Avoids confusion between:
  - **Definition/Specification** (normative resource) that is deployed in a Workbench
  - **Blueprint** (candidate definition) that can be adopted/deployed in a workbench

**Hub Package Content:**
A Hub Package can contain artifacts of these types:
1. **Scenario Blueprints** (includes Trained Agents)
2. **Workbench Blueprints**
3. **Machine Blueprints**
4. **Standalone Tools Blueprints**
5. **Raw Agents Blueprints**
6. **Mixed artifacts** (combination of the above types)

**Publishing Model - Deep Clone:**
- Publishing performs a **deep clone** of all resources to Marketplace
- **Containers**: Published individually to avoid duplication of unchanged containers
  - Each container image is cloned separately
  - Unchanged containers are not duplicated (referenced if already exists)
- **Non-container resources (CRDs)**: Cloned and packaged into a **package-manifest-container**
  - All CRDs for the package are bundled together
  - Package manifest file is included in the same container
  - Single container per package containing all CRDs + manifest
- **Package Dependency Model**: 
  - Package provides specifications (blueprints), not instances
  - Packages can reference platform-provided resources (e.g., platform Machine Definitions)
  - Packages cannot reference resources from other packages
  - Package-subscription isolation: all resources from a package are isolated to that subscription scope
  - No shared resources between packages

**Storage Model:**
- Source resources in the publishing tenant repository remain intact
- Marketplace Artifact Repository maintains cloned containers and package-manifest-containers
- Containers are stored individually (deduplication for unchanged containers)
- CRDs are packaged in package-manifest-container per package

**Container Deduplication:**
- Hash-based deduplication (e.g., SHA-256)
- Unchanged containers are not duplicated (referenced if hash matches existing container)
- Each container image has a unique hash fingerprint
- Hash included in package manifest for verification

**Container Signing and Validation:**
- **All containers must be signed by the publisher**
- Publisher registration process accepts a signing certificate from the publisher
- Signing certificate is stored and associated with the publisher
- All artifacts are validated by Marketplace services before acceptance
- Validation includes:
  - Signature verification
  - Container integrity check (hash verification)
  - Manifest completeness
  - Dependency resolution

**Publisher Registration:**
- Tenant admin must register the Subscription in Marketplace as a "Publisher"
- Registration process includes:
  - Submission of signing certificate (for container signing)
  - Publisher information (name, contact, etc.)
  - Subscription details
- Hub Win (Customer Success) team reviews and authorizes publisher registration requests
- Signing certificate is stored and associated with the publisher
- This is a prerequisite for publishing packages

**Package Manifest CRD:**
- Developer creates **Marketplace Package Manifest CRD** in workbench
- Can have many Package Manifest CRDs in a single workbench
- CRD includes:
  - References to Specification artifacts (Scenarios, Workbenches, Machines, Tools, Raw Agents)
  - Associated children automatically included (don't need explicit references)
  - All package listing manifest information (product info, publisher info, categories, visibility controls, etc.)
- Multi-media content (screenshots, documentation) stored in workbench git repository alongside CRD

**Package Manifest (Final):**
- Extracted from Package Manifest CRD during publishing
- Modeled similar to AWS Marketplace listing manifest
- Contains metadata for discovery, dependencies, versioning, publisher info, visibility controls, etc.
- Stored in package-manifest-container along with all CRDs

**Package Manifest Fields (AWS Marketplace-inspired):**
- **Product Information:**
  - Product name (display name)
  - Short description
  - Long description
  - Version
  - Release notes/changelog
- **Publisher Information:**
  - Publisher name (tenant/subscription)
  - Publisher contact information
  - Support information
- **Categorization:**
  - Categories/tags
  - Artifact types included (Scenario, Workbench, Machine, Tools, Raw Agents)
- **Deployment Information:**
  - System requirements
  - Dependencies (with version constraints)
  - Deployment instructions
- **Visibility Controls:**
  - Allow/disallow list of tenants (private information of publisher)
  - Allow/disallow list of regions (regions published by Hub Win team)
  - Visibility rules (public, restricted, private)
- **Metadata:**
  - Package ID
  - Package version
  - Published date
  - Last updated date
  - Status (published, deprecated, withdrawn)

**Implications:**
- Atomic unit = Hub Package (not individual artifacts)
- Package can contain multiple blueprint types
- Marketplace maintains its own artifact repository (clones)
- Publisher registration is a controlled process (Hub Win approval)

---

## Topic 2: Marketplace Catalog Architecture

### Key Questions
1. Where does the Marketplace catalog live?
   - Platform-level (shared across all tenants)?
   - Tenant-scoped (private marketplaces)?
   - Hybrid (platform + tenant marketplaces)?
   - ✅ **Platform service** (decided)
   - ✅ **Tenant-private marketplace achieved via visibility controls** (allow list of tenants in package manifest)

2. What is the storage model for listings?
   - CRDs in a dedicated namespace?
   - Separate database/index?
   - Git-based (like other Hub artifacts)?
   - ✅ **OpenSearch-based storage** (decided)

3. How is metadata indexed for search?
   - Full-text search engine?
   - Tag-based filtering?
   - Structured queries?
   - ✅ **OpenSearch** (decided - provides full-text search, filtering, structured queries)

4. What metadata is required vs optional?
   - ✅ **Defined below** - Comprehensive schema with required vs optional fields

### Design Decisions Needed
- [x] Marketplace scope (platform vs tenant vs hybrid) - ✅ **Platform service** (decided)
- [x] Listing storage mechanism - ✅ **OpenSearch-based storage** (decided)
- [x] Search/indexing technology - ✅ **OpenSearch** (decided)
- [x] Metadata schema (required vs optional fields) - ✅ **Defined below** (decided)
- [x] Category/taxonomy structure - ✅ **Flat tag-based** (decided)

### Constraints
- Hub uses GitOps for CRDs
- Small teams → simple defaults
- Enterprise → audit trails required

### Dependencies
- Affects: Publishing service, Discovery service, Access control

### Related Subsystems
- Artifact Registry (references source artifacts)
- User Management (publisher identity)
- Subscription Management (tenant boundaries)

### Thoughts and Answers

**Marketplace as Platform Service:**
- Marketplace is a **platform-level service** (shared across all tenants)
- Single Marketplace instance serves all tenants
- Tenant-private marketplace is achieved through **visibility controls** in package manifest
- Packages with tenant allow lists create private marketplaces for those tenants
- No separate tenant-scoped marketplace infrastructure needed

**Marketplace Catalog Services:**
- Uses **OpenSearch-based storage** for listing manifest files
- Each listing manifest is extracted and read from the published package-manifest-container
- Manifests are added to OpenSearch store for all store-front use cases
- Enables search, filtering, and discovery capabilities
- Visibility controls enforced at query time (tenant/region allow/disallow lists)

**Marketplace Artifact Repository:**
- Separate repository from tenant subscriptions
- Stores cloned containers and package-manifest-containers
- Maintains isolation from source tenant repositories

**Storage Model:**
- **Containers**: Stored individually in Marketplace Artifact Repository
  - Deduplication: Unchanged containers are not duplicated (referenced if already exists)
  - Each container image is cloned separately
- **CRDs + Manifest**: Packaged into package-manifest-container
  - One package-manifest-container per package
  - Contains all CRDs for the package + package manifest file
- **Catalog Index**: OpenSearch-based storage
  - Listing manifests extracted from package-manifest-containers
  - Indexed in OpenSearch for store-front use cases
  - Enables search, filtering, and discovery
- This is separate from the Git-based CRD storage in tenant subscriptions
- Marketplace needs its own artifact storage mechanism (container registry)

**Store-Front/Catalog Capabilities:**
- Provides information about all artifacts included in the package
- Search and discovery based on OpenSearch index
- **Tag-based filtering**: Filter by artifact types, categories, industry_tags, keywords, publisher, etc.
- Flat tag structure enables flexible filtering without hierarchical navigation
- Visibility controls enforced (tenant/region allow/disallow lists)
- Package details including all blueprints (Scenario, Workbench, Machine, Tools, Raw Agents)

**Discovery Mechanisms (Implementation Details - UI/UX):**
- **Browse**: Browse by Publisher and Category
- **Search**: Simple text search (full-text search via OpenSearch)
- **Filtering**: All suggested filters with multi-select capability
  - Filters include: artifact types, categories, industry_tags, keywords, publisher, etc.
- **Sorting**: Sort by relevancy and recency
- **Result Display**: List view format; clicking on a listing takes user to full listing details page
- **Listing Details**: Shows all artifacts included in the package, dependencies, publisher information, version information, etc.

**Note:** These UI/UX patterns are implementation details. The core system design provides OpenSearch-based catalog with filtering and search capabilities that support these patterns, but doesn't prescribe specific UI implementations.

**Implications:**
- Marketplace operates at platform level (has its own artifact repository + catalog)
- Single platform service serves all tenants
- Tenant-private marketplace achieved via package visibility controls (not separate infrastructure)
- Deep clone ensures source artifacts remain intact
- Marketplace can serve packages even if source subscription is modified/deleted
- Container deduplication optimizes storage
- Package-manifest-container provides atomic unit for CRDs + manifest
- OpenSearch enables fast search and discovery
- Catalog services extract and index manifests from published containers
- Visibility controls enforced at query time (tenant/region filtering)

---

## Topic 3: Publishing Workflow and Validation

### Key Questions
1. Who can publish?
   - Any developer with workbench access?
   - Requires approval from tenant admin?
   - Self-service vs moderated?

2. What validation happens before publishing?
   - Artifact completeness check?
   - Dependency declaration validation?
   - Security/compliance scanning?
   - Documentation completeness?

3. What happens to the source artifact after publishing?
   - Listing references source (live link)?
   - Listing contains snapshot (immutable copy)?
   - Hybrid (reference + metadata snapshot)?

4. Can publishers update/withdraw listings?
   - Update metadata only?
   - Publish new versions?
   - Withdraw/deprecate listings?
   - Impact on existing deployments?

### Design Decisions Needed
- [ ] Publisher permissions model
- [ ] Pre-publish validation rules
- [ ] Listing-to-source artifact relationship
- [ ] Listing lifecycle (draft → published → deprecated → withdrawn)
- [ ] Version update mechanism

### Constraints
- Enterprise → approval workflows may be required
- Small teams → minimize friction
- Audit trail → all actions must be logged

### Dependencies
- Affects: Deployment model, Version management, Access control

### Related Subsystems
- Artifact Registry (source artifact validation)
- Workbench Management (publisher permissions)
- Notification Services (publishing notifications)

### Thoughts and Answers

**Publisher Registration (Prerequisite):**
- Tenant admin must register Subscription as "Publisher" in Marketplace
- Hub Win (Customer Success) team reviews and authorizes registration requests
- This is a controlled, approval-based process
- Only registered Publishers can publish packages

**Package Manifest CRD:**
- Developer creates Marketplace Package Manifest CRD in workbench
- Can have many Package Manifest CRDs in a single workbench
- CRD structure:
  - References to Specification artifacts (Scenarios, Workbenches, Machines, Tools, Raw Agents)
  - Associated children automatically included (don't need explicit references)
  - Package listing manifest information (all metadata fields)
- Multi-media content stored in workbench git repository alongside CRD

**Publishing Workflow:**

**Step 1: Create Package Manifest CRD**
- Developer creates **Marketplace Package Manifest CRD** in workbench
- Can have many Package Manifest CRDs in a single workbench
- CRD includes:
  - References to Specification artifacts that should be part of the package
  - Associated children are automatically picked in publishing flow (don't need to be stated explicitly)
  - All package listing manifest information (product info, publisher info, categories, visibility controls, etc.)
- Multi-media content (screenshots, documentation, etc.) can be included in workbench git repository alongside manifest CRD

**Step 2: Publish via Automation Developer Desk**
- Automation Developer Desk has **"Publish to Marketplace"** option
- Lists all Package Manifest CRDs available in the workbench
- Developer picks which CRDs to publish
- Tool packages to build the relevant containers:
  - Extracts all referenced Specification artifacts
  - Includes associated children (automatically picked)
  - Packages CRDs into package-manifest-container
  - Builds/signs container images
- **Notifies Admin** (tenant admin or designated approver)

**Step 3: Admin Approval**
- Admin reviews the package
- Upon approval, admin signs and submits containers to Marketplace
- If rejected, developer is notified

**Step 4: Security Scanning and Quarantine**
- All artifacts are scanned for malware and vulnerabilities
- Artifacts are parked in **quarantined location**
- Artifacts moved to catalog only after all security checks pass

**Step 5: Catalog Indexing** (after security clearance)
- Listing manifest is extracted from package-manifest-container
- Manifest is read and added to OpenSearch store
- Indexed for store-front use cases (search, filtering, discovery)
- Package becomes discoverable in Marketplace

**Package Manifest (Final - in package-manifest-container):**
- Extracted from Package Manifest CRD during publishing
- Modeled like AWS Marketplace listing manifest
- Contains metadata for discovery, dependencies, versioning, publisher info, visibility controls, etc.
- Stored in package-manifest-container along with all CRDs

**Package Manifest Fields (Detailed Schema):**

**REQUIRED FIELDS:**

1. **Package Identity** (Required)
   - `package_id` (string, unique): Unique identifier for the package (immutable)
   - `package_name` (string): Display name of the package
   - `version` (string, semver): Package version (e.g., "1.2.3")
   - `package_uri` (string): Package location/identifier URI

2. **Product Information** (Required)
   - `short_description` (string, max 200 chars): Brief description for listings/search results
   - `artifact_types` (array of strings): Types of artifacts included (Scenario, Workbench, Machine, Tools, Raw Agents)
     - Must include at least one type
     - Valid values: ["scenario", "workbench", "machine", "tools", "raw_agents"]

3. **Publisher Information** (Required)
   - `publisher_id` (string): Publisher subscription/tenant identifier
   - `publisher_name` (string): Display name of publisher

4. **Package Contents** (Required)
   - `blueprints` (array): List of BlueprintSpecs included in package
     - Each entry: `{name, type, version}`
   - `package_sha` (string): SHA-256 hash of the package for integrity verification

5. **Visibility Controls** (Required)
   - `visibility_mode` (enum): "public" | "restricted" | "private"
     - "public": Visible to all tenants (subject to tenant allow/disallow lists)
     - "restricted": Visible only to tenants in allow list
     - "private": Visible only to specific tenants (requires allow list)
   - `tenant_allow_list` (array of strings, optional): List of tenant IDs allowed to see package
     - Required if visibility_mode is "restricted" or "private"
   - `tenant_disallow_list` (array of strings, optional): List of tenant IDs explicitly blocked
   - `region_allow_list` (array of strings, optional): List of regions where package is available
   - `region_disallow_list` (array of strings, optional): List of regions where package is blocked

6. **System Metadata** (Required - Auto-generated)
   - `published_date` (timestamp): When package was published
   - `status` (enum): "published" | "deprecated" | "withdrawn"
   - `publisher_signature` (string): Publisher's signature for container validation

**OPTIONAL FIELDS:**

1. **Product Information** (Optional - Enhanced Discovery)
   - `long_description` (string, max 5000 chars): Detailed description
   - `release_notes` (string): What's new in this version
   - `changelog` (string): Full changelog for this version
   - `keywords` (array of strings): Search keywords/tags
   - `categories` (array of strings): Category classifications
   - `industry_tags` (array of strings): Industry-specific tags (e.g., "financial_services", "healthcare")
   - `use_cases` (array of strings): Common use cases for this package

2. **Publisher Information** (Optional - Support)
   - `publisher_contact_email` (string): Contact email for support
   - `publisher_website` (string): Publisher website URL
   - `support_information` (string): Support details/instructions
   - `publisher_logo_uri` (string): URI to publisher logo image

3. **Deployment Information** (Optional - User Guidance)
   - `deployment_instructions` (string): Step-by-step deployment guide
   - `system_requirements` (object): System requirements
     - `min_hub_version` (string): Minimum Hub version required
     - `required_capabilities` (array of strings): Required Hub capabilities
   - `prerequisites` (array of strings): Prerequisites before deployment
   - `estimated_setup_time` (string): Estimated time to set up (e.g., "30 minutes")

4. **Dependencies** (Optional - Platform Resources)
   - `platform_dependencies` (array of objects): Platform-provided resources referenced
     - Each entry: `{type, name, version_constraint}`
     - Example: `{type: "machine", name: "core-banking-system", version_constraint: "^1.0.0"}`

5. **Documentation & Media** (Optional - Enhanced Experience)
   - `documentation_uri` (string): Link to full documentation
   - `screenshot_uris` (array of strings): URIs to screenshot images
   - `video_uri` (string): Link to demo video
   - `icon_uri` (string): Package icon image URI
   - `readme_uri` (string): Link to README file

6. **Compliance & Security** (Optional - Enterprise)
   - `compliance_certifications` (array of strings): Compliance certifications (e.g., ["SOC2", "ISO27001"])
   - `security_notes` (string): Security considerations or notes
   - `license_type` (string): License type (e.g., "MIT", "Apache-2.0", "Proprietary")
   - `license_uri` (string): Link to full license text

7. **Container Information** (Optional - Technical Details)
   - `container_hashes` (array of objects): Hash fingerprints for all containers
     - Each entry: `{container_name, hash_algorithm, hash_value}`
   - `container_count` (integer): Number of containers in package

8. **Metadata** (Optional - Tracking)
   - `last_updated_date` (timestamp): Last update timestamp
   - `deprecation_date` (timestamp): When package was deprecated (if applicable)
   - `deprecation_reason` (string): Reason for deprecation
   - `replacement_package_id` (string): ID of replacement package (if deprecated)

**Validation Rules:**

1. **Required Field Validation:**
   - All required fields must be present and non-empty
   - `package_id` must be unique across all packages
   - `version` must follow semver format
   - `artifact_types` must include at least one valid type
   - `visibility_mode` must be valid enum value
   - If `visibility_mode` is "restricted" or "private", `tenant_allow_list` must be provided

2. **Format Validation:**
   - `short_description`: 10-200 characters
   - `long_description`: Max 5000 characters (if provided)
   - `package_name`: 3-100 characters, alphanumeric + hyphens/underscores
   - `version`: Valid semver (e.g., "1.2.3", "2.0.0-beta.1")
   - Email addresses must be valid format
   - URIs must be valid URL format

3. **Content Validation:**
   - `blueprints` array must not be empty
   - `package_sha` must be valid SHA-256 hash (64 hex characters)
   - `container_hashes` must match actual containers in package
   - Region names must be from Hub Win team's published region list

**Minimum Viable Metadata (v1):**
For v1, packages must include:
- All REQUIRED fields
- At least one of: `long_description`, `keywords`, or `categories` (for discoverability)
- `deployment_instructions` recommended but optional

**Indexing Strategy:**
- OpenSearch indexes all text fields for full-text search
- Structured fields (artifact_types, categories, visibility_mode) indexed for filtering
- Date fields indexed for sorting
- Package ID and version indexed for exact matching

**Category/Taxonomy Structure:**
- **Flat tag-based categorization** (no hierarchical structure)
- Publishers can assign multiple tags to their packages
- Tags are free-form strings (no predefined taxonomy)
- Common tag types:
  - **Categories**: General classification (e.g., "customer-service", "fraud-detection", "compliance")
  - **Industry tags**: Industry-specific (e.g., "financial-services", "healthcare", "retail")
  - **Keywords**: Search keywords for discoverability
  - **Use case tags**: Specific use cases (e.g., "dispute-resolution", "loan-processing")
- Tags stored in `categories`, `industry_tags`, and `keywords` fields (all optional)
- All tags indexed in OpenSearch for filtering and search
- No validation of tag values (publishers have freedom to choose)
- Marketplace Console may suggest common tags based on existing packages (UI enhancement, not validation)
- Future: May evolve to curated tag suggestions or tag validation, but v1 is completely free-form

**Container Storage:**
- Containers are published individually
- **Hash-based deduplication**: Unchanged containers are not duplicated (hash match = reference existing)
- Each container image has a unique hash fingerprint (e.g., SHA-256)
- Hash included in package manifest for verification
- Each container image is stored separately in Marketplace Artifact Repository

**Container Signing:**
- All containers must be signed by the publisher
- Publisher's signing certificate accepted during registration
- **Admin signs and submits containers** upon approval
- Marketplace services validate all artifacts before acceptance
- Validation includes signature verification and integrity checks
- **Marketplace re-signs distributed containers with Marketplace private key**
- Subscribers can verify integrity using Marketplace's public key
- Ensures end-to-end integrity: Publisher signature → Marketplace signature → Subscriber verification

**Package-Manifest-Container:**
- OCI container format
- Contains all CRDs for the package
- Contains the package manifest file
- Single container per package
- Provides atomic unit for non-container resources
- Must be signed by publisher (like all containers)

**Source Artifact Relationship:**
- Source artifacts in publishing tenant repository remain intact
- Marketplace stores clones in Marketplace Artifact Repository
- No live link - packages are self-contained clones
- Deep clone ensures complete independence

**Validation (Marketplace Services):**
- **Publisher authorization**: Must be registered Publisher
- **Admin approval**: Admin must approve before submission
- **Container signing verification**: All containers must be signed (admin signs upon approval)
- **Container integrity**: Hash verification for all containers
- **Package completeness**: All referenced artifacts and associated children included
- **Package manifest completeness**: All required fields present
- **Container cloning verification**: Containers cloned successfully
- **Package-manifest-container creation**: CRDs + manifest packaged correctly
- **Visibility rules validation**: Tenant/region lists are valid
- **Credential validation**: Packages must NOT contain any credentials (validated during security scanning)

**Security Scanning:**
- **Pre-acceptance scanning**: All artifacts scanned for malware and vulnerabilities before acceptance
- **Quarantine process**: Artifacts parked in quarantined location
- **Security clearance**: Artifacts moved to catalog only after all checks pass
- **Continuous scanning**: Periodic scans for vulnerabilities and malware after publication
- **Issue notification**: Publishers and tenants informed about identified issues
- **Blacklisting**: Publishers and Marketplace admin (Hub Win team) can blacklist packages
  - Block new package-subscriptions
  - Block usage of existing package-subscriptions

**Implications:**
- Two-step process: Publisher registration → Package publishing
- Hub Win team controls who can publish
- Packages are self-contained (no runtime dependencies on source)
- Security scanning adds delay to publishing (quarantine until cleared)
- Continuous security monitoring after publication
- Blacklisting enables rapid response to security issues

---

## Topic 4: Discovery and Search

### Key Questions
1. What discovery mechanisms are needed?
   - Full-text search?
   - Category browsing?
   - Tag filtering?
   - Publisher collections?
   - Popular/featured listings?

2. What search capabilities are required?
   - Search by artifact name/description?
   - Filter by artifact type?
   - Filter by publisher (tenant/subscription)?
   - Filter by tags/categories?
   - Sort by relevance/popularity/recency?

3. How is "popularity" determined?
   - Number of deployments?
   - User ratings (future)?
   - Usage metrics (future)?

4. What information is shown in search results?
   - Listing card with key metadata?
   - Preview of dependencies?
   - Publisher information?
   - Version information?

### Design Decisions Needed
- [x] Discovery UI patterns - ✅ **Browse by Publisher and Category; Search** (decided - implementation detail)
- [x] Search query syntax - ✅ **Simple text search** (decided - implementation detail)
- [x] Filtering capabilities - ✅ **All suggested filters, multi-select** (decided - implementation detail)
- [x] Sorting options - ✅ **Relevancy and recency** (decided - implementation detail)
- [x] Result display format - ✅ **List view, clicking takes to full listing details** (decided - implementation detail)

**Note:** These are implementation-level UI/UX details. Core system design focuses on OpenSearch-based catalog and filtering capabilities.

### Constraints
- Small teams → simple, intuitive interface
- Enterprise → may need advanced filtering for compliance

### Dependencies
- Affects: Metadata schema, Indexing strategy, UI design

### Related Subsystems
- UX Architecture (Marketplace Browser UI)
- Hub Analytics (usage metrics, if tracked)

### Thoughts and Answers

**Marketplace Console:**
- Unified console for all marketplace operations
- Accessible from:
  - **Agent Developer Desk** (same as Automation Development Desk)
  - **Scenario Design Desk**
  - **Automation Product Desk**
  - **Admin Desk**
- Provides unified experience across different personas
- Houses all marketplace functionality in one place

**Store-Front Access Points:**
- Marketplace Console provides store-front functionality
- Discovery section within Marketplace Console
- Accessible from Agent Developer Desk, Scenario Design Desk, Automation Product Desk, and Admin Desk
- Any of these users can initiate subscription to packages visible in the marketplace

**Store-Front/Catalog Capabilities:**
- Provides information about **all artifacts included in the package**
- Can show details of all blueprints (Scenario, Workbench, Machine, Tools, Raw Agents)
- Search and discovery based on OpenSearch index
- Filtering by artifact types, categories, tags, publisher, etc.
- Visibility controls enforced (tenant/region allow/disallow lists)
- Full-text search across package metadata
- Structured queries for advanced filtering

**Discovery Mechanisms (Implementation Details - UI/UX):**
- **Browse**: Browse by Publisher and Category
- **Search**: Simple text search (full-text search via OpenSearch)
- **Filtering**: All suggested filters with multi-select capability
  - Filters include: artifact types, categories, industry_tags, keywords, publisher, etc.
- **Sorting**: Sort by relevancy and recency
- **Result Display**: List view format; clicking on a listing takes user to full listing details page
- **Listing Details**: Shows all artifacts included in the package, dependencies, publisher information, version information, etc.

**Note:** These UI/UX patterns are implementation details. The core system design provides OpenSearch-based catalog with filtering and search capabilities that support these patterns, but doesn't prescribe specific UI implementations.

**Catalog Indexing Process:**
- When package is published, catalog services extract manifest from package-manifest-container
- Manifest is read and parsed
- All artifact information is indexed in OpenSearch
- Index includes all blueprints and their metadata
- Enables fast search and discovery

**OpenSearch Benefits:**
- Full-text search capabilities
- Tag-based filtering
- Structured queries
- Fast retrieval for store-front use cases
- Scalable for large number of packages

**Search Result Information:**
- Package listing card with key metadata
- **All artifacts included in the package** (Scenario, Workbench, Machine, Tools, Raw Agents)
- Preview of dependencies
- Publisher information
- Version information
- Visibility status (based on tenant/region filters)

---

## Topic 5: Dependency Resolution

### Key Questions
1. How are dependencies declared?
   - In listing metadata?
   - Extracted from artifact specs?
   - Both?
   - ✅ **Packages can refer to platform-provided resources** (decided)
   - ✅ **Packages cannot refer to resources from other packages** (decided)

2. What dependency types are supported?
   - Tool Protocols (required/optional)?
   - Machine Definitions (required/optional)?
   - Knowledge Bases (required/optional)?
   - Other Scenarios (required/optional)?
   - Hub Applications (required/optional)?
   - ✅ **Platform-provided resources only** (e.g., platform Machine Definitions) (decided)
   - ✅ **No dependencies on other packages** (decided)

3. How is dependency resolution handled during deployment?
   - Automatic resolution from Marketplace?
   - Prompt subscriber to install dependencies?
   - Allow subscriber to provide existing dependencies?
   - Block deployment if dependencies missing?
   - ✅ **Platform resources available automatically** (decided)
   - ✅ **No cross-package dependency resolution needed** (decided)

4. How are version constraints handled?
   - Semantic version ranges (>=1.0.0, <2.0.0)?
   - Exact version matching?
   - Latest compatible version?
   - ✅ **N/A - no external dependencies** (decided)

5. What about transitive dependencies?
   - Resolve recursively?
   - Show dependency tree to subscriber?
   - Handle dependency conflicts?
   - ✅ **No cross-package dependencies - no conflicts between packages** (decided)
   - ✅ **Package-subscription isolation prevents conflicts** (decided)

### Design Decisions Needed
- [x] Dependency declaration format - ✅ **Platform-provided resources only** (decided)
- [x] Supported dependency types - ✅ **Platform resources (e.g., Machine Definitions)** (decided)
- [x] Resolution strategy (automatic vs manual) - ✅ **Platform resources available automatically** (decided)
- [x] Version constraint syntax - ✅ **N/A - no cross-package dependencies** (decided)
- [x] Transitive dependency handling - ✅ **N/A - no cross-package dependencies** (decided)
- [x] Conflict resolution strategy - ✅ **Package-subscription isolation prevents conflicts** (decided)

### Constraints
- Promotion Model doesn't handle dependencies
- Artifact Registry manages versions
- Small teams → simple dependency model

### Dependencies
- Affects: Deployment workflow, Listing schema, UI design

### Related Subsystems
- Artifact Registry (version management)
- Registry Services (Tool/Machine registries)
- Workbench Management (workbench resource dependencies)

### Thoughts and Answers

**Package Dependency Model:**
- Packages can refer to **platform-provided resources** (e.g., platform Machine Definitions)
- Packages **cannot refer to resources from other packages**
- A Package provides **specifications (blueprints)**, not instances
- Specifications can be instantiated in a workbench instance
- All deployments/resources from a package are **isolated to that package-subscription scope**
- **No shared resources between packages**

**Package Structure:**
- Package contains all required artifacts (Scenarios, Workbenches, Machines, Tools, Raw Agents) as specifications
- Package can reference platform-provided resources (e.g., platform Machine Definitions)
- Package cannot reference resources from other packages
- Package is atomic and self-contained (except for platform references)

**Package-Subscription Isolation:**
- Each package-subscription is isolated
- Resources from one package cannot reference resources from another package
- All deployments/resources from a package are scoped to that package-subscription
- No cross-package resource sharing

**Implications:**
- No dependency resolution between packages
- No dependency conflict resolution between packages
- No transitive dependency handling between packages
- Platform-provided resources are available to all packages
- Package-subscription scope provides isolation
- Simpler deployment model (subscribe and use, with platform resource access)
- Packages are portable and independent (except for platform dependencies)

---

## Topic 6: Deployment Model

### Key Questions
1. How does deployment work?
   - Uses Promotion Model mechanics?
   - Direct copy to target subscription?
   - Creates Promotion Request?
   - Hybrid approach?

2. What is the deployment target?
   - Specific workbench?
   - Subscription (subscriber chooses workbench)?
   - New workbench (for Workbench Templates)?

3. What happens during deployment?
   - Copy container images to target registry?
   - Copy CRDs to target Git repository?
   - Resolve and copy dependencies?
   - Deploy to workbench (sync)?
   - Track installation?

4. Who can deploy?
   - Any subscriber with workbench access?
   - Requires approval?
   - Self-service vs moderated?

5. How are deployments tracked?
   - Installation record per workbench?
   - Link back to source listing?
   - Track deployed version?
   - Enable update notifications?

### Design Decisions Needed
- [ ] Deployment mechanism (Promotion vs direct copy)
- [ ] Deployment target model
- [ ] Deployment workflow steps
- [ ] Deployment permissions
- [ ] Installation tracking model

### Constraints
- Promotion Model handles cross-subscription artifact movement
- Artifact Registry manages physical artifact storage
- Workbench Management handles workbench deployment

### Dependencies
- Affects: Integration with Promotion Model, Artifact Registry usage

### Related Subsystems
- Artifact Registry (artifact copying)
- Promotion Model (deployment mechanics)
- Workbench Management (workbench deployment)

### Thoughts and Answers

**Package Subscription Model:**
- **Package-subscription** is a composite of:
  - Published-package-listing
  - Subscribing-tenant
  - Subscribing-tenant-workbench-id
- Package subscription is tracked to a **workbench of a tenant**, not just to a tenant
- When a Package is subscribed to from a Workbench:
  - All Specification resources under that package become **available** in the Workbench as **BlueprintSpecs**
  - BlueprintSpecs are **usable** but not directly part of the Workbench definition
  - They are **not used** until a Workbench Deployment or Scenario Deployment references them
  - They become available for use, that's all

**BlueprintSpec Transformation:**
- **Export to Package**: When Specifications are exported to a Package, all relevant CRDs change type to corresponding BlueprintSpec types
  - Example: `ScenarioNormativeSpec` → `ScenarioBlueprintSpec`
  - Example: `WorkbenchSpec` → `WorkbenchBlueprintSpec`
  - Example: `MachineSpec` → `MachineBlueprintSpec`
- **Subscription**: When a package is subscribed to, all BlueprintSpecs become **usable** in the Workbench
- **Usage**: To make any BlueprintSpec part of the Workbench, a corresponding resource specification must be created from the BlueprintSpec
  - Example: `ScenarioBlueprintSpec` → `ScenarioNormativeSpec` + `ScenarioAutomationSpec` (and potentially `ScenarioDeploymentSpec`)
  - This ensures that Blueprints **never become part of the Workbench definition**
  - Resources that are considered part of a workbench do not undergo any change
- **Blueprint Reference Tracking**: Resources created with a reference from Blueprint have an additional section referencing the BlueprintSpec
  - Structure includes:
    - Package SHA (hash of the package)
    - Package URI (location/identifier of the package)
    - BlueprintSpec name and type
    - Package version
  - This helps in applying updates from later versions of the Blueprint to the Workbench resources
  - Enables version update workflow and tracking

**Container Handling:**
- Containers referenced by Blueprints are **NOT cloned into Workbench** during subscription
- Containers are cloned into tenant's artifact repository **only when first used** in a Scenario Deployment
  - Trigger: When a Scenario Deployment references a container for the first time
  - Cloned at deployment time, not at subscription time
- Lazy container cloning optimizes storage and reduces subscription overhead
- **Container Updates**: Containers are updated only when a derived resource is updated
  - Update doesn't impact running pods/containers until the derived resources are rolled out
  - Ensures no disruption to active deployments during update

**Unsubscription Model:**
- When a package is unsubscribed:
  - Blueprints cease to be visible in the Workbench
  - Package subscription is marked as **"pending-unsubscription"**
  - Package subscription will **not move to "unsubscribed"** until all derived resources cease to exist under the workbench
  - **Cleanup Process**: Derived resources must be manually deleted to complete unsubscription
  - When deployments are deleted, corresponding containers are also evicted
  - Runtimes will be impacted if containers were not evicted/scaled down to zero
  - This ensures no orphaned resources and proper cleanup

**Cross-Workbench Deployment:**
- When any Blueprint-derived resource is deployed to a new workbench (via Promotion Model or other mechanism):
  - That Workbench instance will automatically have a **package subscription** to the package of the corresponding Blueprint
  - Package subscription is created automatically as part of the deployment workflow
  - **Platform operators create this subscription** (not manual user action)
  - Ensures Blueprint reference tracking across workbenches
  - Enables update propagation across workbenches using the same Blueprint

**Package Subscription Tracking:**
- Marketplace service maintains an up-to-date list of all package-subscriptions
- Tracks all packages across all tenant-subscriptions
- Information available for:
  - Publishers (can see who subscribed to their packages)
  - Hub Win team (can see all subscriptions)
- Enables:
  - Security incident response (notify affected subscribers)
  - Blacklisting (block new or existing subscriptions)
  - Usage analytics

**Subscription Workflow:**
1. User (from Agent Developer Desk, Scenario Design Desk, Automation Product Desk, or Admin Desk) opens Marketplace Console
2. User navigates to Discovery section
3. User selects package from marketplace
4. User initiates subscription (selects target workbench)
5. **Admin approval required** (tenant admin or designated approver)
   - Admin uses Authorization section in Marketplace Console (or Admin Desk)
6. If approved, package subscription is created
7. Package resources are added to the respective workbench
8. Resources become available (not used until referenced in deployments)
9. User receives notification (via Notifications section in Marketplace Console)

**Deployment vs Subscription:**
- **Subscription**: Package resources become available in workbench (not yet used)
  - Requires admin approval
  - Resources added to workbench after approval
- **Deployment**: Workbench Deployment or Scenario Deployment references the subscribed resources
- Subscription is prerequisite for deployment
- Resources from subscribed packages are treated same as locally created resources once deployed

---

## Topic 7: Cross-Subscription and Cross-Tenant Sharing

### Key Questions
1. Can artifacts be shared across subscriptions?
   - Same tenant, different subscriptions?
   - Different tenants?
   - Platform-wide (all tenants)?
   - ✅ **Yes - Marketplace is platform service, supports all sharing scenarios** (decided)

2. How are subscription boundaries handled?
   - Marketplace operates at platform level?
   - Marketplace operates at tenant level?
   - Hybrid (tenant can opt into platform marketplace)?
   - ✅ **Marketplace is platform service** (decided)
   - ✅ **Tenant-private marketplace via visibility controls** (allow list of tenants in package manifest)

3. What about security and isolation?
   - Artifact access control?
   - Publisher identity verification?
   - Subscriber identity verification?
   - Audit trail for cross-tenant deployments?

4. How are credentials/secrets handled?
   - Never included in published artifacts?
   - Subscriber provides their own?
   - Marketplace manages credential templates?

### Design Decisions Needed
- [x] Marketplace scope (platform vs tenant) - ✅ **Platform service** (decided)
- [x] Cross-tenant sharing model - ✅ **Via visibility controls in package manifest** (decided)
- [x] Security boundaries - ✅ **Federated IAM, artifact signing, integrity verification** (decided)
- [ ] Credential handling strategy

### Constraints
- Subscription isolation (Artifact Registry)
- Tenant isolation (User Management)
- Enterprise security requirements

### Dependencies
- Affects: Catalog architecture, Access control, Deployment model

### Related Subsystems
- Subscription Management (subscription boundaries)
- User Management (tenant boundaries)
- Artifact Registry (subscription isolation)

### Thoughts and Answers

**Marketplace as Platform Service:**
- Marketplace is a **platform-level service** (shared across all tenants)
- Single Marketplace instance serves all tenants
- No separate tenant-scoped marketplace infrastructure

**Tenant-Private Marketplace:**
- Achieved through **visibility controls** in package manifest
- Packages with tenant allow lists create private marketplaces for those tenants
- Publisher specifies allow/disallow list of tenants in package manifest
- Marketplace enforces visibility controls at query time
- Supports:
  - Large enterprise sharing packages with related tenants
  - Close partnerships between organizations
  - Exclusion of sanctioned organizations

**Cross-Tenant Sharing:**
- Marketplace supports sharing across:
  - Same tenant, different subscriptions
  - Different tenants
  - Platform-wide (all tenants)
- Controlled via package manifest visibility settings
- No separate infrastructure needed for different sharing scenarios

**Security Boundaries:**

**Federated IAM:**
- Marketplace is accessed through **federated IAM**
- All Tenant IAM Domains federate with the Marketplace IAM
- Any request from Tenant Users to Marketplace are:
  - Duly authenticated
  - Attributed to federated identity in the Marketplace domain
  - Reference to tenant domain identity is maintained
- **PII Protection**: No PII of users beyond a desensitized name is taken to create the Marketplace profile
- Publishers and Subscribers are **always identified and authenticated**

**Artifact Integrity:**
- Artifacts are **immutable and signed**
- Signatures are verified by Marketplace
- **Marketplace distributed containers are signed by Marketplace private key**
- Any subscriber can verify the integrity of distributed containers using Marketplace's public key
- Ensures end-to-end integrity from publisher → Marketplace → subscriber

**Access Control:**
- Platform-level Marketplace with tenant isolation via visibility controls
- Publisher controls who can see their packages
- Marketplace enforces visibility rules at query/discovery time
- Federated authentication ensures proper identity attribution

**Credential Handling Strategy:**
- **Packages must NOT contain any credentials**
- Packages are validated to ensure no credentials are included
- **Subscribers provide their own credentials** when deploying/using packages
- Marketplace does not interfere with any credential-related matters
- Credential management is entirely the responsibility of subscribers
- This ensures security and prevents credential leakage through packages

---

## Topic 8: Version Management and Updates

### Key Questions
1. How are versions managed in Marketplace?
   - Each listing has version history?
   - New version = new listing or update existing?
   - Semantic versioning alignment with Artifact Registry?

2. How are updates communicated to subscribers?
   - Notification when new version published?
   - Notification when update available for installed artifact?
   - Opt-in vs opt-out notifications?

3. How do subscribers update deployed artifacts?
   - Manual update process?
   - Automatic update option?
   - Update approval workflow?

4. What about breaking changes?
   - Version compatibility tracking?
   - Breaking change indicators?
   - Migration guidance?

5. Can subscribers stay on old versions?
   - Version pinning?
   - Multiple versions deployed simultaneously?

### Design Decisions Needed
- [x] Version management model - ✅ **Semver semantics** (decided)
- [x] Update notification mechanism - ✅ **Notify all package-subscribers** (decided)
- [x] Update workflow - ✅ **Explicit pull, no automatic propagation** (decided)
- [x] Breaking change handling - ✅ **Minor versions backward compatible, major may require migration** (decided)
- [x] Version pinning support - ✅ **Explicit version references, semver ranges supported** (decided)

### Constraints
- Artifact Registry uses semantic versioning
- Promotion Model tracks versions
- Small teams → simple update process

### Dependencies
- Affects: Listing schema, Deployment model, Notification integration

### Related Subsystems
- Artifact Registry (version tracking)
- Notification Services (update notifications)
- Workbench Management (version deployment)

### Thoughts and Answers

**Version Management Model:**
- Publishers can publish new updates to packages following **semver semantics**
- Version format: MAJOR.MINOR.PATCH (e.g., 1.2.3)
- **Minor versions must be in-place upgradable** (backward compatible)
- Major versions may require migration/breaking changes

**Update Propagation:**
- **No automatic update propagation**
- Tenant admins and/or developers must **pull new versions explicitly**
- Subscribers must explicitly refer to new version artifacts in their deployments
- Updates are opt-in, not automatic

**Version References:**
- References can use **semver compatibility range references** to reduce toil of dependency updates
- Examples:
  - `^1.2.3` (compatible with 1.x.x, >=1.2.3, <2.0.0)
  - `~1.2.3` (compatible with 1.2.x, >=1.2.3, <1.3.0)
  - `>=1.2.3 <2.0.0` (explicit range)
  - `1.2.3` (exact version)
- Range references allow automatic compatibility with minor/patch updates

**New Version Notifications:**
- New version availability is **notified to all package-subscribers**
- Notification sent when publisher publishes new version
- Subscribers can then decide to pull and deploy new version
- Notification includes version number, release notes, compatibility information

**In-Place Upgrade Requirements:**
- Minor versions must support in-place upgrades
- No breaking changes in minor versions
- Patch versions are always in-place upgradable
- Major versions may require explicit migration

**Update Workflow:**
1. Publisher publishes new version (following semver)
2. Marketplace validates version compatibility
3. Notification sent to all package-subscribers
4. Subscribers review new version
5. Subscribers explicitly pull new version (if desired)
6. New BlueprintSpec version becomes available in workbench
7. Subscribers can update Blueprint-derived resources using the Blueprint reference section
8. Update process uses Blueprint reference to apply changes from new BlueprintSpec version
9. Deployment uses updated resources

**Blueprint Update Mechanism:**
- Blueprint reference section in derived resources enables update workflow
- When Blueprint is updated, subscribers can update derived resources
- **Update Workflow: Hybrid Approach**
  - System suggests updates from new BlueprintSpec version
  - User reviews and approves updates
  - Manual merge can be applied for divergent resources
- **Derived Resource Modification:**
  - If a user modifies a derived resource after creation, it remains a derived spec
  - Modified resources become **divergent** from the Blueprint
  - Manual merges can be applied to reconcile divergent resources with Blueprint updates
- **Partial Updates:**
  - Nothing is forced - updates are opt-in
  - Resources that don't take updates from Blueprint are deemed **out-of-sync** with the Blueprint
  - Marketplace Console shows out-of-sync resources
  - Example: Only ScenarioNormativeSpec updated, ScenarioAutomationSpec remains out-of-sync
- Maintains link between Blueprint and derived resources for update propagation

**Implications:**
- Subscribers have control over when to update
- Semver range references reduce manual update toil
- Minor versions can be updated automatically if range allows
- Major versions require explicit action
- All updates are auditable (who updated, when, to what version)

---

## Topic 9: Access Control and Permissions

### Key Questions
1. Who can publish?
   - Developer role in source workbench?
   - Tenant admin approval required?
   - Platform admin approval for platform marketplace?

2. Who can discover/browse?
   - Any Hub subscriber?
   - Tenant-scoped visibility?
   - Platform-wide visibility?

3. Who can deploy?
   - Developer role in target workbench?
   - Tenant admin approval required?
   - Self-service vs approval workflow?

4. Who can withdraw/update listings?
   - Original publisher only?
   - Tenant admin?
   - Platform admin?

5. What about private listings?
   - Tenant-only visibility?
   - Subscription-only visibility?
   - Explicit sharing with specific tenants?

### Design Decisions Needed
- [ ] Publisher permissions
- [ ] Discovery permissions
- [ ] Deployment permissions
- [ ] Listing management permissions
- [ ] Private listing model

### Constraints
- Hub IAM model (Cipher integration)
- Enterprise → approval workflows
- Small teams → sensible defaults

### Dependencies
- Affects: Publishing workflow, Discovery service, Deployment workflow

### Related Subsystems
- User Management (IAM integration)
- Workbench Management (workbench permissions)
- Cipher IAM (identity and access)

### Thoughts and Answers

**Publisher Allow/Disallow Lists:**
- **Authorized people can maintain allow/disallow list of publishers** under the subscription
- Accessible via Marketplace Console or Admin Desk
- Works like Apache domain config allow/disallow list
- Controls which publishers' packages are visible/accessible to the tenant
- Applied at subscription level (per subscription)
- Enables tenant-level control over package sources
- Permission-based access (not limited to Tenant Admin, but requires authorization)

**Subscription Permissions:**
- Users from Agent Developer Desk, Scenario Design Desk, Automation Product Desk, Admin Desk can:
  - Access Marketplace Console
  - Browse and discover packages (Discovery section)
  - Initiate subscription requests (Subscription section)
- **Admin approval required** for subscription creation
  - Admin uses Authorization section in Marketplace Console or Admin Desk
- After approval, package resources added to workbench
- Users receive notifications (Notifications section in Marketplace Console)

**Publisher Management Permissions:**
- **Authorized people** can manage publisher allow/disallow lists
- Accessible via Marketplace Console (Publisher Management section) or Admin Desk
- Permission-based (not limited to Tenant Admin, but requires authorization)
- Controls which publishers' packages are visible to the tenant

**Access Control Model:**
- **Publisher-level**: Package manifest can specify tenant allow/disallow lists
- **Tenant-level**: Tenant Admin can specify publisher allow/disallow lists
- **Subscription-level**: Admin approval required for subscriptions
- Multi-layer access control for security and governance

**Implications:**
- Authorized people (permission-based) have control over which publishers are trusted
- Publisher allow/disallow list works like Apache config (order matters, first match wins)
- Subscription requires admin approval (governance)
- Marketplace Console provides unified access from multiple desks (including Admin Desk)
- All marketplace operations consolidated in one console
- Consistent UX across personas
- Publisher management available in both Marketplace Console and Admin Desk

---

## Topic 10: Integration with Existing Subsystems

### Key Questions
1. How does Marketplace integrate with Artifact Registry?
   - Reads artifacts from source subscriptions?
   - Uses Artifact Registry copy mechanisms?
   - Aligns with versioning model?

2. How does Marketplace integrate with Promotion Model?
   - Uses Promotion Request for deployments?
   - Extends Promotion Destinations?
   - Separate deployment mechanism?

3. How does Marketplace integrate with Workbench Management?
   - Creates/updates workbench resources?
   - Validates workbench compatibility?
   - Handles workbench templates?

4. How does Marketplace integrate with Registry Services?
   - Resolves Tool/Machine dependencies?
   - Validates Tool Protocol compatibility?
   - Handles Machine Definition dependencies?

5. How does Marketplace integrate with Notification Services?
   - Publishing notifications?
   - Deployment notifications?
   - Update notifications?

### Design Decisions Needed
- [ ] Artifact Registry integration points
- [ ] Promotion Model integration approach
- [ ] Workbench Management integration
- [ ] Registry Services integration
- [ ] Notification Services integration

### Constraints
- Existing subsystem APIs and contracts
- Cannot break existing functionality
- Should leverage existing capabilities

### Dependencies
- Affects: All Marketplace workflows

### Related Subsystems
- All Hub subsystems (integration points)

### Thoughts and Answers
> *Capture answers and thoughts here as we discuss*

---

## Topic 11: UI/UX and Developer Experience

### Key Questions
1. What UI components are needed?
   - Marketplace Browser (discovery)?
   - Publishing Wizard?
   - Deployment Wizard?
   - My Listings (publisher view)?
   - My Installations (subscriber view)?
   - ✅ **Marketplace Console** (unified console for all marketplace operations) (decided)
   - ✅ **Package Manifest CRD editor** (decided)
   - ✅ **"Publish to Marketplace" option in Automation Developer Desk** (decided)

2. What workflows need UI support?
   - Publish artifact from workbench?
   - Discover and deploy artifact?
   - Manage published listings?
   - Track installations?
   - Handle updates?
   - ✅ **Create Package Manifest CRD** (decided)
   - ✅ **Publish via Automation Developer Desk** (decided)
   - ✅ **Admin approval workflow** (decided)

3. What CLI commands are needed?
   - `hub marketplace publish`?
   - `hub marketplace search`?
   - `hub marketplace deploy`?
   - `hub marketplace list` (my listings)?
   - `hub marketplace installs` (my installations)?

4. How does Marketplace integrate with Hub Studio?
   - New Marketplace section?
   - Publishing from Scenario/Application views?
   - Deployment from Marketplace view?
   - ✅ **Marketplace Console accessible from Agent Developer Desk, Scenario Design Desk, Automation Product Desk** (decided)
   - ✅ **Integration with Automation Developer Desk** (decided)

### Design Decisions Needed
- [x] UI component inventory - ✅ **Marketplace Console with 7 sections** (decided)
- [ ] Workflow design - ⏸️ **Out of scope at this stage**
- [x] CLI command set - ✅ **Defined below** (decided)
- [x] Hub Studio integration points - ✅ **Marketplace Console accessible from multiple desks** (decided)

### Constraints
- Hub Studio UX patterns
- CLI consistency with existing commands
- Small teams → simple, intuitive UX

### Dependencies
- Affects: All user-facing workflows

### Related Subsystems
- UX Architecture (Hub Studio integration)
- CLI Channels (CLI design)

### Thoughts and Answers

**Publishing via Marketplace Console:**
- Marketplace Console accessible from Automation Developer Desk (Agent Developer Desk)
- **Creating Package Section**: Package Manifest CRD editor
- **Publishing Section**: 
  - Lists all Package Manifest CRDs available in the workbench
  - Developer picks which CRDs to publish
  - Tool packages to build relevant containers:
    - Extracts all referenced Specification artifacts
    - Includes associated children (automatically picked)
    - Packages CRDs into package-manifest-container
    - Builds/signs container images
  - Notifies Admin for approval
  - Upon admin approval, signs and submits containers to Marketplace
  - Publishing status tracking

**Package Manifest CRD:**
- Created by developer in workbench
- Can have many Package Manifest CRDs in a single workbench
- Contains:
  - References to Specification artifacts
  - Package listing manifest information
  - Multi-media content references (stored in git repo)

**Marketplace Console:**
- **Unified console for all marketplace operations**
- Accessible from:
  - **Agent Developer Desk** (same as Automation Development Desk)
  - **Scenario Design Desk**
  - **Automation Product Desk**
  - **Admin Desk**
- Provides consistent UX across different personas
- Houses all marketplace functionality in one place

**Marketplace Console Sections:**
1. **Discovery**: Browse and search packages
   - Full-text search
   - Filtering by artifact types, categories, tags, publisher
   - Package details view (all artifacts included)
   
2. **Subscription**: Initiate package subscriptions
   - Select package and target workbench
   - View subscription status
   - Manage subscriptions
   
3. **Authorization of Subscription**: Admin approval interface
   - Review subscription requests
   - Approve/reject subscriptions
   - Track approval history
   
4. **Creating Package**: Package Manifest CRD editor
   - Create/edit Package Manifest CRDs
   - Reference Specification artifacts
   - Configure package listing information
   - Manage multi-media content
   
5. **Publishing**: Publish workflow and status
   - List available Package Manifest CRDs
   - Select CRDs to publish
   - Track publishing status
   - View publishing history
   
6. **Notifications**: Updates and issues
   - Version updates (new package versions available)
   - Security issues (vulnerabilities, blacklisting)
   - Subscription status (approval/rejection, resource availability)
   - Publishing status (progress, approval status)
   - Out-of-sync resources (resources not updated from Blueprint)
   - Orphaned resources (from withdrawn Blueprints)
   - Unified notification center for all marketplace events
   
7. **Publisher Management**: Publisher allow/disallow list management
   - Accessible to authorized people (permission-based, not limited to Tenant Admin)
   - Configure publisher allow/disallow lists (Apache-style)
   - Manage trusted publishers
   - Available in both Marketplace Console and Admin Desk

**Store-Front Access:**
- Marketplace Console provides store-front functionality
- Users from multiple desks can access unified console
- Consistent experience across personas

**Subscription Workflow:**
- User initiates subscription from Marketplace Console
- User selects package and target workbench
- Admin approval required (via Marketplace Console)
- If approved, package subscription created
- Package resources added to workbench

**UI Components in Marketplace Console:**
- **Discovery Section**: Browse, search, filter packages
- **Subscription Section**: Initiate subscriptions, view subscription status
- **Authorization Section**: Admin approval interface for subscriptions
- **Package Creation Section**: Package Manifest CRD editor
- **Publishing Section**: Publish workflow, status tracking
- **Notifications Section**: Version updates, security issues, subscription status
- **Publisher Management**: Publisher allow/disallow list management (accessible to authorized people)

**Publisher Management Access:**
- Available in Marketplace Console (Publisher Management section)
- Also available in Admin Desk
- Permission-based access (authorized people, not limited to Tenant Admin)
- Manages publisher allow/disallow lists (Apache-style)

**CLI Command Set:**

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

**Note:** Detailed workflow design (step-by-step workflows, error handling, progress indicators) is out of scope at this stage. CLI commands follow Hub CLI patterns and integrate with existing Hub authentication and workspace context.

---

## Topic 12: Audit Trail and Compliance

### Key Questions
1. What events need to be audited?
   - Publishing events?
   - Deployment events?
   - Update events?
   - Withdrawal events?
   - Access events (who viewed what)?

2. What data is captured in audit logs?
   - Actor identity?
   - Timestamp?
   - Artifact details?
   - Target details?
   - Outcome (success/failure)?

3. How are audit logs stored and accessed?
   - CAF integration?
   - Separate audit store?
   - Queryable by tenant admin?
   - Queryable by platform admin?

4. What compliance requirements apply?
   - Data residency (cross-tenant sharing)?
   - Export controls?
   - Intellectual property tracking?

### Design Decisions Needed
- [ ] Audit event inventory
- [ ] Audit log schema
- [ ] Audit storage mechanism
- [ ] Compliance requirements

### Constraints
- Enterprise → comprehensive audit trails
- CAF integration for cognitive audit
- Regulatory compliance requirements

### Dependencies
- Affects: All Marketplace operations

### Related Subsystems
- Cognitive Audit Fabric (CAF)
- Hub Analytics (if used for audit)

### Thoughts and Answers

**Security Scanning and Compliance:**
- **Pre-acceptance scanning**: All artifacts scanned for malware and vulnerabilities before acceptance
- **Quarantine process**: Artifacts parked in quarantined location until security checks pass
- **Continuous scanning**: Periodic scans for vulnerabilities and malware after publication
- **Issue notification**: Publishers and tenants informed about identified security issues
- **Blacklisting mechanism**: 
  - Publishers can blacklist their own packages
  - Marketplace admin (Hub Win team) can blacklist any packages
  - Can block new package-subscriptions
  - Can block usage of existing package-subscriptions

**Package Subscription Tracking:**
- Marketplace service maintains up-to-date list of all package-subscriptions
- Tracks: (published-package-listing, subscribing-tenant, subscribing-tenant-workbench-id)
- Information available for publishers and Hub Win team
- Enables security incident response and blacklisting

**Audit Events:**
- Publishing events (with security scan results)
- Security scan results (pre-acceptance and continuous)
- Blacklisting events (who, when, why, which packages)
- Package subscription events (subscribe, unsubscribe)
- Security issue notifications (to publishers and tenants)

---

## Topic 13: Operational Concerns

### Key Questions
1. How is Marketplace service deployed?
   - Platform-level service?
   - Per-tenant instance?
   - Shared infrastructure?

2. What are the scalability considerations?
   - Number of listings?
   - Search performance?
   - Deployment concurrency?
   - Cross-tenant isolation?

3. What monitoring and observability is needed?
   - Publishing metrics?
   - Deployment metrics?
   - Search performance?
   - Error rates?

4. What about data retention?
   - Listing retention (deprecated/withdrawn)?
   - Installation history retention?
   - Audit log retention?

5. How are failures handled?
   - Deployment failures?
   - Dependency resolution failures?
   - Partial deployment rollback?

### Design Decisions Needed
- [ ] Service deployment model
- [ ] Scalability architecture
- [ ] Monitoring strategy
- [ ] Data retention policies
- [ ] Failure handling strategy

### Constraints
- Hub infrastructure patterns
- Enterprise → high availability
- Small teams → simple operations

### Dependencies
- Affects: Service architecture, Integration design

### Related Subsystems
- Infrastructure (deployment)
- Hub Analytics (monitoring)

### Thoughts and Answers

**Security Operations:**
- **Quarantine infrastructure**: Separate quarantined location for artifacts pending security clearance
- **Continuous scanning**: Periodic vulnerability and malware scans
- **Incident response**: 
  - Notify publishers and tenants about security issues
  - Blacklist packages (block new/existing subscriptions)
  - Track all package-subscriptions for rapid response

**Package Subscription Management:**
- Marketplace maintains up-to-date list of all package-subscriptions
- Subscription tracking: (published-package-listing, subscribing-tenant, subscribing-tenant-workbench-id)
- Enables:
  - Security incident response (notify affected workbenches)
  - Blacklisting enforcement (block subscriptions)
  - Usage analytics
  - Version update notifications (notify all subscribers of new versions)

**Monitoring and Observability:**
- Security scan metrics (pass/fail rates, scan duration)
- Quarantine metrics (artifacts pending clearance)
- Package subscription metrics (subscriptions per package, per tenant)
- Blacklisting events and impact
- Security issue notifications

**Data Retention:**
- Security scan results (historical vulnerability data)
- Quarantine records (artifacts that failed security checks)
- Package subscription history (for security incident response)
- Blacklisting history (audit trail)

---

## Topic 14: Future Enhancements (Out of Scope for v1)

### Key Questions
1. What features are explicitly out of scope for v1?
   - Commercial model (licensing, payment)?
   - Ratings and reviews?
   - Usage analytics for publishers?
   - ~~Private marketplaces (tenant-scoped)?~~ ✅ **Already supported via visibility controls** (not a future feature)
   - Marketplace APIs for external integrations?
   - Automated dependency updates?
   - Marketplace curation (featured listings)?

2. How do we design v1 to enable future features?
   - Extensible metadata schema?
   - Plugin architecture?
   - API design for future extensions?

### Design Decisions Needed
- [ ] v1 scope boundaries
- [ ] Extensibility points
- [ ] Future feature hooks

### Constraints
- v1 must be complete and useful
- Should not over-engineer for future
- Should not block future enhancements

### Dependencies
- Affects: Overall architecture decisions

### Thoughts and Answers
> *Capture answers and thoughts here as we discuss*

---

## Discussion Order Recommendation

**Phase 1: Foundation (Topics 1-3)**
- Topic 1: Scope and Artifact Types
- Topic 2: Marketplace Catalog Architecture
- Topic 3: Publishing Workflow and Validation

**Phase 2: Core Functionality (Topics 4-6)**
- Topic 4: Discovery and Search
- Topic 5: Dependency Resolution
- Topic 6: Deployment Model

**Phase 3: Integration (Topics 7-10)**
- Topic 7: Cross-Subscription and Cross-Tenant Sharing
- Topic 8: Version Management and Updates
- Topic 9: Access Control and Permissions
- Topic 10: Integration with Existing Subsystems

**Phase 4: Experience and Operations (Topics 11-13)**
- Topic 11: UI/UX and Developer Experience
- Topic 12: Audit Trail and Compliance
- Topic 13: Operational Concerns

**Phase 5: Scope Definition (Topic 14)**
- Topic 14: Future Enhancements (Out of Scope for v1)

---

## Decision Log Template

For each topic, document:
- **Decision:** What was decided
- **Rationale:** Why this decision
- **Alternatives Considered:** What else was discussed
- **Impact:** What this affects
- **Date:** When decided
- **Participants:** Who was involved

---

## Synthesis: Cohesive Design Picture

> *As we complete topics, synthesize the answers into a cohesive design*

### Design Principles (Emerging)

1. **Blueprint Terminology**
   - "Blueprint" distinguishes exportable/distributable definitions from deployed definitions
   - Blueprints are candidates for adoption/deployment in workbenches

2. **Package as Atomic Unit**
   - Hub Package is the atomic unit of publishing (not individual artifacts)
   - Packages can contain artifacts of six types (Scenario, Workbench, Machine, Tools, Raw Agents, or mixed)
   - Packages provide specifications (blueprints), not instances
   - Packages can reference platform-provided resources (e.g., platform Machine Definitions)
   - Packages cannot reference resources from other packages
   - Package-subscription isolation: all resources from a package are isolated to that subscription scope
   - No shared resources between packages

3. **Deep Clone Model**
   - Publishing performs deep clone of all resources to Marketplace
   - Containers: Published individually with hash-based deduplication (unchanged containers not duplicated)
   - CRDs: Cloned and packaged into package-manifest-container (OCI format, along with manifest)
   - Source artifacts remain intact in publishing tenant repository
   - Packages are independent of source subscription lifecycle
   - All containers must be signed by publisher (signing certificate from registration)
   - Marketplace services validate all artifacts before acceptance

4. **Controlled Publishing**
   - Publisher registration required (tenant admin action)
   - Hub Win team approval for publisher registration
   - Ensures quality and governance

### Architecture Decisions (Emerging)

1. **Marketplace as Platform Service**
   - Platform-level service (shared across all tenants)
   - Single Marketplace instance serves all tenants
   - Tenant-private marketplace achieved via visibility controls (not separate infrastructure)
   - Packages with tenant allow lists create private marketplaces

2. **Marketplace Artifact Repository**
   - Separate repository from tenant subscriptions
   - Stores cloned containers individually (with deduplication)
   - Stores package-manifest-containers (one per package, containing CRDs + manifest)
   - Platform-level storage

3. **Marketplace Catalog Services (OpenSearch)**
   - OpenSearch-based storage for listing manifest files
   - Manifests extracted from published package-manifest-containers
   - Indexed in OpenSearch for store-front use cases
   - Enables search, filtering, and discovery
   - Provides information about all artifacts included in packages
   - Visibility controls enforced at query time (tenant/region filtering)

4. **Package-Manifest-Container**
   - Single container per package
   - Contains all CRDs for the package
   - Contains package manifest file
   - Provides atomic unit for non-container resources
   - Manifest extracted by catalog services for indexing

5. **Container Storage Strategy**
   - Containers published individually (OCI format)
   - Hash-based deduplication: Unchanged containers are not duplicated (hash match = reference existing)
   - Each container has unique hash fingerprint (e.g., SHA-256)
   - Optimizes storage for shared/common containers
   - All containers must be signed by publisher
   - Marketplace validates signatures and integrity before acceptance

6. **Package Manifest**
   - Every package has a manifest (like AWS Marketplace)
   - Stored in package-manifest-container along with CRDs
   - Contains listing metadata, dependencies, versioning info, visibility controls
   - **Visibility Controls:**
     - Allow/disallow list of tenants (private to publisher)
     - Allow/disallow list of regions (published by Hub Win team)
     - Supports enterprise sharing, partnerships, sanctions compliance
   - Enables discovery and deployment
   - Fields include: product info, publisher info, categories, deployment instructions, system requirements

7. **Publisher Model**
   - Subscription-level registration (not individual developer)
   - Tenant admin initiates registration
   - Registration includes signing certificate submission
   - Hub Win team approves registration
   - Signing certificate stored and associated with publisher
   - Required for all package publishing

8. **Security and Safety Model**
   - Pre-acceptance scanning: All artifacts scanned for malware and vulnerabilities
   - Quarantine process: Artifacts parked in quarantined location until cleared
   - Continuous scanning: Periodic vulnerability and malware scans after publication
   - Issue notification: Publishers and tenants informed about security issues
   - Blacklisting: Publishers and Hub Win team can blacklist packages
   - Package subscription tracking: Marketplace maintains list of all subscriptions

9. **Package Subscription Model**
   - Subscription tracked to workbench level: (package-listing, tenant, workbench-id)
   - Subscribed resources become available in workbench as **BlueprintSpecs** (not directly part of workbench definition)
   - BlueprintSpecs are usable but must be converted to regular specs to be part of workbench
   - Derived resources created from BlueprintSpecs have Blueprint reference section for updates
   - Marketplace maintains up-to-date subscription list for security response

10. **BlueprintSpec Model**
    - Export transforms regular specs to BlueprintSpec types (e.g., ScenarioNormativeSpec → ScenarioBlueprintSpec)
    - Subscription makes BlueprintSpecs available/usable in workbench
    - Usage requires creating derived resources from BlueprintSpecs (e.g., ScenarioBlueprintSpec → ScenarioNormativeSpec + ScenarioAutomationSpec)
    - Blueprints never become part of workbench definition directly
    - Derived resources have Blueprint reference section (Package SHA, Package URI, BlueprintSpec name/type, version) for update tracking
    - **Derived Resource Modification**: Modified resources remain derived but become divergent; manual merges can be applied
    - **Update Workflow**: Hybrid (system suggests, user approves); nothing forced
    - **Out-of-Sync Resources**: Resources that don't take updates are marked out-of-sync; Marketplace Console shows them
    - Containers referenced by Blueprints cloned lazily (only when Scenario Deployment references container)
    - Container updates only when derived resource updated; doesn't impact running pods until rollout
    - Unsubscription: Blueprints become invisible, subscription marked "pending-unsubscription" until all derived resources manually deleted
    - Unsubscription cleanup: When deployments deleted, containers evicted; runtimes impacted if not scaled down
    - **Withdrawn Blueprints**: Derived resources continue to work until fully unsubscribed, but marked as "Orphaned and unsupported"
    - Cross-workbench deployment: When Blueprint-derived resource promoted, target workbench automatically gets package subscription (created by platform operators)

11. **Version Management Model**
   - Semver semantics for package versions
   - Minor versions must be in-place upgradable (backward compatible)
   - No automatic update propagation
   - Subscribers must explicitly pull new versions
   - Semver compatibility range references supported (reduce update toil)
   - New version availability notified to all package-subscribers
   - Major versions may require explicit migration

### Integration Patterns (Emerging)

1. **Artifact Registry Integration**
   - Marketplace has its own artifact repository (Marketplace Artifact Repository)
   - Clones packages from source subscriptions during publishing
   - Containers referenced by Blueprints cloned lazily into tenant artifact repository (only when first used)
   - Maintains isolation from source

2. **Promotion Model Integration**
   - When Blueprint-derived resources promoted to new workbench, target workbench gets package subscription
   - Ensures Blueprint reference tracking across workbenches
   - Enables update propagation across workbenches

3. **Workbench Management Integration**
   - BlueprintSpecs become available upon subscription (not directly part of workbench)
   - Workbench Management handles creation of derived resources from BlueprintSpecs
   - Derived resources (regular specs) created from BlueprintSpecs when used
   - Blueprint reference section added to derived resources for update tracking

4. **Publisher Registration**
   - Integration with Hub Win (Customer Success) workflow
   - Approval-based registration process

5. **Marketplace Console Integration**
   - Unified console accessible from multiple desks
   - Integrates with Agent Developer Desk, Scenario Design Desk, Automation Product Desk, Admin Desk
   - Provides consistent UX across personas
   - Houses all marketplace operations in one place

### Open Questions (Remaining)

**Resolved:**
- ✅ Blueprint reference structure: Package SHA, Package URI, BlueprintSpec name/type, version
- ✅ Derived resource modification: Remains derived, becomes divergent, manual merges can be applied
- ✅ Partial updates: Nothing forced, out-of-sync resources shown in Marketplace Console
- ✅ Update workflow: Hybrid (system suggests, user approves)
- ✅ Container cloning trigger: When Scenario Deployment references container
- ✅ Container updates: Only when derived resource updated, doesn't impact running pods until rollout
- ✅ Unsubscription cleanup: Manual deletion, containers evicted when deployments deleted
- ✅ Withdrawn Blueprints: Continue to work until fully unsubscribed, marked as "Orphaned and unsupported"
- ✅ Cross-workbench promotion: Automatic subscription created by platform operators

**Remaining Questions:**
- How are version conflicts handled when updating Blueprint-derived resources? (e.g., if Blueprint version incompatible with existing derived resource)
- What happens if target workbench already has subscription to same package (different version) during promotion?
- How is version alignment handled across workbenches using same Blueprint?

---

## Next Steps

1. ✅ Review this discussion plan
2. ✅ Prioritize topics (may want to adjust order)
3. ✅ Document decisions as we go
4. ✅ Create detailed design docs after decisions are made

---

## Topic 15: Hub Application Blueprints

**Status:** ✅ Resolved

### Question

Should Hub Applications be publishable as Blueprints, enabling publishers to share reusable application containers (DSL runtimes, interpreters) that subscribers can extend?

### Background

Raw Agents can be published as Blueprints. A similar pattern exists for Hub Applications where:
- Publisher provides a base runtime container (e.g., Camel DSL interpreter)
- Subscriber provides lightweight configuration/DSL files
- Subscriber's `HubApplicationSpec` references the Blueprint instead of building from source

### Discussion

**Use Cases:**
- Apache Camel DSL runtimes
- GraphQL mashup engines
- Rule engine runtimes (Drools)
- Workflow DSL interpreters

**Key Challenge:** How does CI know how to combine the base container with subscriber files?

**Solution: Build Recipe**

Introduce a `buildRecipe` field in `HubApplicationBlueprintSpec` that defines how CI should combine the Blueprint container with subscriber inputs.

**Recipe Types:**
1. **copy-only** — Safest option; simply copies files to specified destinations
2. **buildpack** — Uses platform-approved Cloud Native Buildpacks for compilation scenarios

**Security Considerations:**
- Constrained recipe types (no arbitrary Dockerfiles)
- Sandboxed build environment (no network access)
- Resource limits (CPU, memory, time)
- Only platform-vetted buildpacks allowed

### Resolved

**CRD Structure:**
```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: camel-dsl-runtime
spec:
  container:
    image: "camel-dsl-runtime"
    tag: "3.0.0"
    runtime: "rhea"
  
  buildRecipe:
    type: "copy-only"  # or "buildpack"
    copyTargets:
      - source: "dsl"
        destination: "/app/routes"
  
  inputs:
    - name: "dsl"
      description: "DSL route definitions"
      required: true
      filePattern: "*.xml"
```

**Subscriber Usage:**
```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-routes
spec:
  blueprint:
    ref: "camel-dsl-runtime"
    version: "^3.0.0"
  inputs:
    dsl:
      path: "./routes/"
```

**Registry Bloat Concern:** Resolved — OCI layer deduplication means base container layers are shared; only subscriber-specific layer is stored.

**CI Integration:**
- CI detects Blueprint reference in HubApplicationSpec
- Resolves Blueprint from Marketplace
- Executes build recipe in sandboxed environment
- Pushes result to subscriber's Artifact Registry

**Documentation Created:**
- ADR-0102: Hub Application Blueprints with Build Recipes
- Marketplace subsystem: hub-application-blueprints.md
- CI subsystem: blueprint-based-builds.md
- Guide: publishing-hub-application-blueprints.md
- Guide: using-hub-application-blueprints.md