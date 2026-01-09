# Aritfact Registry and CD
A subsytem of Hub

* All Runtime artifacts must be published to container registry
* All artifacts must be packaged as OCI containers
* Hub Application Specification references the container specification
* Every Subscription receives two registries: snapshot, production
* A Workbench can be tagged for a Devlopment Lifecycle: DEV, STAGING, PRODUCTION are default; Tenant Admin can add additional environments tags.
* Workbenches and Scenarios can be moved promoted to Target Workbenches in same subscription or othe subscriptions. 
* Tenant Admin can define "Promption Destinations" under a subscription. 
* Developers can request promption of a Workbench as whole to another Workbench
* Developers can request promotion of a Scenario to another Workbench (may be in another Promotion Destination)
* Each Workbench Specification under a Subscription can have zero or more Promotion Destinations added by developer and approved by admin for frequent reuse. This promotion path can have configurtions that indicate the approval workflow for promotion.
* For each Scenario promoted, all the artifacts associated with the Scenario are promoted, not just the Hub Application. If the target is a non-dev workbench, then it can only refer to artifacts from production repository of the subscription underwhich that workbench exists.
* If the promotion is destined to a different subscription, containers are cloned to that subscription. All CRDs are cloned to target irrespective of whether the subscription is same or different.
* Subscription is lowest atomic unit that can be promoted. All associated artifacts referenced by Subscription are promoted when a Subscription is Promoted.
* CRDs not associated to any single workbench (subscription scoped artifacts) can be promoted by the admin, using the Subscription-level promotion paths.
* Each Subscription has a corresponding Git Repository to hold all the CRDs under the subscription. The Git repo layout is well-defined.
* There may be no resources outside of the Git repository and the Contianer registry defining the Subscription Resources, Workbenches or the Workbench Constituents. 
* The Data Stores content is local to the subscription. When a Data Store is promoted only the Resource Specification along with any migration CRDs associated with that Resource Specification may be promoted and migrations are executed at destination as part of Deployment of the Promoted artifact.
* Migration Scripts may also refer to OCI Contianers for custom data bundles that are required (DMLs) as part of the migration. 
* The Migration CRD specification Data Store specfic. The Data Store provider module would have defined the contracts for that specification.  

---


# CI
Dedicated Subsystem of Hub

## Runtime-Specific CI infrastructure
Every Application Runtime provides CI
Integrates into artifact-registry-and-ci subsystem


## Test Runner and Test Suites
Scenario Test Runner (subsystem available from the platform)
- Contians tools to invoke requests at the IO Gateway and assert the responses, request updates
- Can be enabled per Subscription and Workbench by the Tenant Admin
- The same subsystem can be used to run tests for the standalone tools in the workbench as well
- The scope of the test runner is always limited to a Workbench
- Tests are CRDs. Test Suites are CRD that may reference Tests.
- The Test Runner is itself a Hub Application built on Atlantis Runtime.

## Practice notes
Stubbing Machines and Tools is left upto developers.
The Machine and Tool Protocols/Specifications (contracts, the normative definitions) can be promoted, the 'Evironment' and the 'Concrete' entities cannot be promoted. They are explicitly configured per subscription by the Tenant Admins.


========
## Registry & Artifacts

1. **Registry Technology**: Abstract (platform-agnostic) or specific provider (Harbor, ECR, ACR)?

> Platform agnostic. Relies on Olympus Weave (https://weave.olympus.tech/getting-started/overview/) for the implementation. One Workbench maps to a Cluster as per Weave. The current repositories are ECR and Jfrog Artifactory. But Hub need not make explicit references to them.

2. **Snapshot → Production Promotion**: What triggers artifact promotion from snapshot to production registry?
   - Manual approval?
   - Automated on test pass?
   - Part of workbench/scenario promotion?

> Manual promotion. Couple with promotion of Scenario under which the artifact is defined.
> The source code for the Hub Applications can reside in git repos outside hub and can be referenced in hub in development workbenches. The Scenario developer iterface supports referencing external repositories.

3. **Container Cloning (Cross-Subscription)**: Physical copy to target registry, or registry federation/pull-through?
> Physical copy

4. **Container Versioning**: Semantic versioning, git-sha tags, or both?
> both

5. **Artifact Types**: Beyond Hub Application containers, are there other artifact types (helm charts, config bundles)?
> Only Hub-defined CRDs. No underlying infra specific CRDs.

---

## Workbench Lifecycle & Environments

6. **Environment Tags**: Are DEV/STAGING/PROD tags on a **single Workbench** (indicating its stage), or do they represent **separate Workbench instances**?
> A Workbench can only have one such tag. They are not fluid (although can be changed by admin). A Workbench cannot be in-place promoted from one dev-lifecycle tag to another. Lets be clear to call Dev-Lifecycle-Stage than 'Environment' to avoid confusion with Hub Envrionment - a business/operations domain entity.

7. **Tag Transitions**: Can a Workbench's tag change (DEV → STAGING), or is promotion always to a different target Workbench?

> always to a different workbench. Changing tag may lead to inconsistencies. the admin should understand consequences.

8. **Custom Environment Tags**: When Tenant Admin adds custom tags (e.g., UAT, PERF), what constraints exist?

> The tag can specificy if it accepts snapshot artifacts or not. Nothing else at the moment.

---

## Promotion Model

9. **Promotion Destination**: Is this a target **subscription**, a target **workbench**, or both options?
> Both options. Some options are not legal for some artifacts. 

10. **Cross-Tenant Promotion**: Allowed, or only within same tenant?
> Allowed. Promotion Destination can be any hub subscription. The credentials to push artifacts and resource definitons to the environment are captured in the Promotion Destination entity. Any correlation/correspondance to existing subscription are irrelevant.

11. **Promotion Target Workbench**: Must it be empty/new, or can you promote into an existing workbench (update)?
> Existing workbench is possible, if that workbench is based on the a pervious version of the currrent workbench specification (normative).

12. **Scenario Promotion Without Workbench**: When promoting just a Scenario, does the target Workbench need to already exist?
> Yes. It should also be based on the current Workbench Specification.

13. **Partial Scenario Promotion**: Can you promote a subset of a Scenario's artifacts, or always all-or-nothing?
> Scenario is an atomic unit and least granular unit that can be promoted.
> The accepting workflow deployment version is mutated when a scenario is updated or a new one is accepted. 

14. **Approval Workflow Engine**: Built-in Hub capability, or integration point (Jira, ServiceNow, custom)?
> Built-in functionality with support for external change management tools. 
> The integrations with external tools are placeholders now. Can be documented later.

15. **Approval Actors**: Who approves promotions — Tenant Admin, Supervisor, or configurable per path?
> This is specific to the tenant context and is specific to each promotion destination. Admin defines the hierarchy.
---

## Git Repository

16. **Git Provider**: Platform-managed internal git, or customer-provided (GitHub, GitLab, Bitbucket)?

> For all Hub-native resources, it is platform provided Git. The platform provdied git can support additional origins to push the changes to, if they tenants want these in their private repos.

17. **Repo-per-Subscription**: One git repo per subscription, confirmed?
> Yes, right now. In future, we can support repos per workbench. But for now, only one per subscritpion.

18. **Repo Layout**: Should I define standard folder structure, or is this configurable?
> Define an enforceable standard structure.

19. **GitOps Sync**: Operators watch git and reconcile, or git is just storage (manual apply)?
> Git is just a storage. Sync triggers are managed by Admins. Right now, these are manual. Sync trigger invocation may be delegated to Developers by admins.

20. **Branching Model**: Main branch only, or environment branches (dev, staging, prod)?
> Main branch only for all promotions
> A Developer need to maintain a dedicated Workbench (instance) for themselves if they want to concurrently develop and improve the specification. So a branch may not be needed even in development. However, not supporting branching is a current limitation. 
---

## CI Subsystem

21. **Runtime CI Scope**: Build only, or build + unit test?
Build + Unit test. Unit test support and approach is defined by runtime.

22. **CI Trigger**: On git push, on-demand, or configurable?
configurable

23. **CI Output**: Where do build logs, test results go? Olympus Watch?
The CI module provides the views. The runtime logs will also go to Watch.

24. **CI Pipeline Definition**: CRD-based, or runtime-specific config files?
CRD-based. But standardized per runtime per subscription. Ideally the system provided defaults should work. Overrides by admin is a future feature.

---

## Test Runner

25. **Test Invocation**: On-demand, scheduled, or triggered by promotion request?
> Manual/on-demand

26. **Test Scope**: Integration tests only (I/O Gateway), or also unit tests?
> Hub Test Runner only support integration tests

27. **Test CRD Schema**: Should I define detailed schema, or leave as placeholder for later?
> placeholder

28. **Test Dependencies**: Can tests depend on other tests (ordered execution)?
> Handled in Test Suite definition. Recommended to run suite for execution depedencies

29. **Test Data Management**: How is test data provisioned/cleaned up?
> Test Runner support pre-flight setup. The test can have a dedicated 'Hub Environment' referencing resources that can be reset by the runner.

30. **Test Results**: Stored where? Affect promotion approval?
> Test Runner provides the storage and reports
---

## Data Store Migrations

31. **Migration Ordering**: How are multiple migration CRDs ordered for execution?
> Semantic-Version-based. Lower versions run first. 

32. **Migration Rollback**: If migration fails at destination, what happens?
> Reported as Deployment failure. Admin and Developer intervene to resolve.

33. **DML Bundles (OCI Containers)**: These contain seed data? Who builds them?
> Yes, could be seed data. Developers

34. **Data Store Specific Contracts**: Should I document placeholder for each data store type (Ganymede, Callisto, Europa)?
> yes, placeholders are welcome.

---

## Operations

35. **Rollback Support**: Supported? To last version only, or any historical version?
> Only last version

36. **Version History**: Explicit versioning (semver per workbench/scenario), or implicit (git history)?
> Semver

37. **Promotion Audit Trail**: Where is promotion history stored?
> This subsystem stores it. Admins and Developers will have dedicated CD console where they can see this.

38. **Promotion Notifications**: Who gets notified on promotion request/approval/completion?
> Admins, Developers by default
> The Subscription and Workbench can have explicitly configured groups to receive notifications.

---

## Relationship to Existing Subsystems

39. **Operator Integration**: New operators for CI/CD, or extensions to existing developer operators?
> Likely new operators. To be decided per operator.

40. **Signal Exchange**: Does promotion trigger signals (e.g., for notification)?
> SX has no role here. There are no Busines Domain operations involved in promotion.

41. **Notification Services**: Integrated for approval requests and promotion status?
> Yes