---
name: provisioning-a-new-cluster-handles-eight-cluster-config-repos-update
description: Standard Operating Procedure for provisioning a new cluster (Handles Eight+ Cluster Config Repos Update)
---

# New Cluster Creation SOP (aws-default-pp-mumbai)

> Standard Operating Procedure for provisioning a new cluster in the Olympus PreProd zone.

Status: v1alpha1
---

## What is a Cluster?

In Olympus, a **cluster** is the **atomic deployment unit** — a Kubernetes namespace containing logically related applications that together deliver a specific business capability.

Think of a cluster as a walled garden: it groups services that work together (functional cohesion), isolates faults so one cluster's failure doesn't cascade to others (fault isolation), separates data owned by different business domains (data isolation), and can serve different tenant sets independently (tenant isolation).

```
Olympus World
 └── Site (regional grouping)
      └── Zone (single cloud region — fully independent)
           └── Space (physical resource group — PCI / Non-PCI / DMZ)
                └── Cluster ← THIS IS WHAT WE ARE CREATING
                     └── Application (K8s Deployment)
                          └── Pod (running instance)
```

Every cluster is:

- **A Kubernetes namespace** — The cluster name IS the namespace name. There is a strict 1:1 mapping.
- **Zone-scoped** — A cluster belongs to exactly one zone. The same ClusterSpec can be deployed to multiple zones, but each zone gets its own independent cluster instance.
- **Atomically deployed** — The entire cluster (all its applications) is deployed, upgraded, and rolled back as one unit from its ClusterSpec (a Helm chart).
- **Uniquely identified** — By its JID (Join ID): `world.site.zone.space.cluster` — e.g., `olympus.india-pp.mumbai-1.standard.agent-nexus`.

### What Makes a Cluster Complete?

A cluster isn't just a namespace. For it to function within the Olympus platform, it must be:

| Concern | Why | Without it... |
|---------|-----|---------------|
| **Provisioned** | Physical namespace + RBAC + resource quotas | Cluster doesn't exist in K8s |
| **Identified** | Registered in the control plane metadata registry | Platform doesn't know the cluster exists |
| **Secured** | Vault secrets access + authentication policies | Applications can't access credentials |
| **Buildable** | Container image registry (ECR) for CI artifacts | CI/CD has nowhere to push images |
| **Deployable** | ArgoCD app + deployment descriptor + Weave train | Code can't reach the cluster |
| **Reachable** | Heracles traffic routing (zone + cluster level) | Users can't send HTTP requests to it |

This SOP walks through each of these concerns in order.

---

## Prerequisites

Before starting, gather all cluster identity and configuration parameters:

| Parameter | What it is | Example |
|-----------|-----------|---------|
| **Cluster name** | Lowercase, hyphen-separated — becomes the K8s namespace | `agent-nexus` |
| **URL-safe name** | Same name but **without hyphens** — used in all hostnames | `agentnexus` |
| **Owning group** | The team that publishes and operates this cluster | `Starlabs` |
| **Admin email groups** | Distribution lists for K8s RBAC + Vault access | `starlabs@zeta.tech` |
| **Git repo URL** | Repository containing the ClusterSpec (Helm chart) | `cluster-spec.agent-nexus` |
| **Description** | One-line purpose statement for the cluster | `"AgentNexus serves reusable agent helpers..."` |
| **Resource quotas** | CPU, memory, pod, and ephemeral-storage hard limits | `cpu: 10, memory: 20Gi, pods: 100` |
| **Path prefix** | Short URL prefix for Heracles traffic routing | `/anx` |
| **ECR repo name** | Container image repository name | `zeta-skills` |

### Naming Rule

The hostname portion before `.internal` or the zone domain **must not contain hyphens**. Always derive the URL-safe name by stripping hyphens:

```
agent-nexus  →  agentnexus
agentic-cde  →  agenticcde
app-infra    →  appinfra
```

---

## How the Pieces Fit Together

```
                                        ┌─────────────────────────────────────┐
                                        │         PHASE 1: EXIST              │
                                        │                                     │
                                        │  ┌───────────────────────────────┐  │
                                        │  │ Step 1: Provision Namespace   │  │
                                        │  │ (RBAC + Quotas + PSPs)        │  │
                                        │  └───────────────────────────────┘  │
                                        │  ┌───────────────────────────────┐  │
                                        │  │ Step 2: Register Identity     │  │
                                        │  │ (Control Plane metadata)      │  │
                                        │  └───────────────────────────────┘  │
                                        └─────────────────────────────────────┘
                                                         │
                                                         ▼
                      ┌──────────────────────────────────────────────────────────────┐
                      │                    PHASE 2: SECURE                            │
                      │                                                              │
                      │  ┌────────────────────────────────────────────────────────┐  │
                      │  │ Step 3: Grant Secrets Access (Vault RBAC)              │  │
                      │  └────────────────────────────────────────────────────────┘  │
                      └──────────────────────────────────────────────────────────────┘
                                                         │
                                                         ▼
          ┌──────────────────────────────────────────────────────────────────────────────────┐
          │                           PHASE 3: DEPLOY                                        │
          │                                                                                  │
          │  ┌──────────────────────────────┐      ┌──────────────────────────────────────┐  │
          │  │ Step 4: Create Image Registry │      │ Step 5: Register ArgoCD Application  │  │
          │  │ (ECR — where images live)     │      │ (GitOps sync engine)                 │  │
          │  └──────────────────────────────┘      └──────────────────────────────────────┘  │
          │  ┌──────────────────────────────┐      ┌──────────────────────────────────────┐  │
          │  │ Step 6: Write Zone Deployment │      │ Step 7: Configure Deployment Train   │  │
          │  │ Descriptor (what to deploy)   │      │ (who can deploy, Weave orchestration)│  │
          │  └──────────────────────────────┘      └──────────────────────────────────────┘  │
          └──────────────────────────────────────────────────────────────────────────────────┘
                                                         │
                                                         ▼
          ┌──────────────────────────────────────────────────────────────────────────────────┐
          │                            PHASE 4: REACH                                        │
          │                                                                                  │
          │     External Client  ──→  Zone Ingress  ──→  Cluster Ingress  ──→  K8s Service   │
          │                                                                                  │
          │  ┌──────────────────────────────────────┐  ┌─────────────────────────────────┐   │
          │  │ Step 8: Zone-Level Traffic Routing    │  │ Step 9: Cluster-Level Routing   │   │
          │  │ (Heracles: domain → cluster proxy)    │  │ (Heracles: path → K8s service)  │   │
          │  └──────────────────────────────────────┘  └─────────────────────────────────┘   │
          └──────────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1 — Bring the Cluster into Existence

A cluster that doesn't exist in the zone cannot be deployed to, secured, or reached. These two steps establish the cluster's physical boundary (K8s namespace) and its logical identity within the Olympus control plane.

### Step 1 — Provision the Namespace

> *"A cluster IS a Kubernetes namespace."*

**Repo**: `olympus-cluster-provisioner`
**File**: `aws-default-pp-mumbai/values.yaml`

**Why this step exists**: In Olympus, the cluster-to-namespace mapping is 1:1. This step creates the namespace and simultaneously establishes three critical boundaries:

- **Resource boundary** — ResourceQuota caps CPU, memory, pods, and ephemeral storage so one cluster can't starve others.
- **Access boundary** — RBAC role bindings control who can view, edit, and deploy to this namespace.
- **Security boundary** — PodSecurityPolicies restrict what containers can do (no host paths, no privilege escalation).

Without this entry, the namespace does not physically exist, and nothing else in this SOP can function.

**What to do**: Add a new entry under the clusters section. Insert alphabetically near sibling clusters.

```yaml
- clusterAccess:
    admin:
    - olympus_sre_access_control_internal@zeta.tech
    - zetafoundrydev@zeta.tech
    - starlabs@zeta.tech
  limits:
  - default:
      cpu: 300m
      ephemeral-storage: 1Gi
      memory: 600Mi
    defaultRequest:
      cpu: 90m
      ephemeral-storage: 250Mi
      memory: 200Mi
    type: Container
  name: <cluster-name>
  podSecurityPolicies:
  - psp.hostpath.restricted
  resourceQuota:
    cpu: "10"
    ephemeral-storage: 100Gi
    memory: 20Gi
    pods: "100"
```

**Key fields**:

| Field | Role |
|-------|------|
| `name` | The cluster name — becomes the K8s namespace |
| `clusterAccess.admin` | Email groups granted admin RBAC in this namespace |
| `resourceQuota` | Hard upper limits — prevents runaway resource consumption |
| `limits` | Default container limits — applied when a pod doesn't specify its own |
| `podSecurityPolicies` | Security constraints for all pods in this namespace |

---

### Step 2 — Register the Cluster Identity

> *"Every cluster has a JID — a globally unique hierarchical path that identifies it across the entire Olympus World."*

**Repo**: `olympus-clusters`
**File**: `templates/aws-default-pp-mumbai/<cluster-name>.yaml`  *(new file)*

**Why this step exists**: Step 1 creates the physical namespace, but the Olympus control plane still doesn't know the cluster exists. This step registers the cluster's **identity** — its owning group, description, ArgoCD application reference, RBAC bindings, and resource limits — as an `OlympusClusterConfig` custom resource. This metadata feeds:

- **Inventory dashboards** — "How many clusters exist in this zone? Who owns them?"
- **ArgoCD application binding** — Links the cluster name to its ArgoCD deployment app.
- **Audit and compliance** — Tracks which group is responsible for what.
- **Platform governance** — Enables automated checks against resource and access policies.

The `metadata.name` follows the `<cluster-name>.<zone-name>` convention, forming part of the cluster's globally unique identity.

**What to do**: Create a new YAML file:

```yaml
apiVersion: "zeta.tech/v1alpha1"
kind: "OlympusClusterConfig"
metadata:
  name: "<cluster-name>.aws-default-pp-mumbai"
  namespace: "owcc"
spec:
  olympusClusterMetadata:
    group: "<owning-group>"
    argocdApp: "<cluster-name>-pp"
    description: "<cluster-description>"
  clusterAccess:
    roleBindings:
      admin:
        - <admin-email-1>
        - <admin-email-2>
  clusterResourceLimits:
    quota:
      memory: "20Gi"
      cpu: "10"
      pods: "100"
      ephemeral-storage: "100Gi"
    limitRange:
    - defaultRequest:
        memory: "200Mi"
        cpu: "90m"
        ephemeral-storage: "250Mi"
      type: "Container"
      default:
        memory: "600Mi"
        cpu: "300m"
        ephemeral-storage: "1Gi"
```

**Key fields**:

| Field | Role |
|-------|------|
| `metadata.name` | `<cluster-name>.<zone-name>` — unique identity in the control plane |
| `group` | The owning business group (e.g., Starlabs, Payments, CoreBanking) |
| `argocdApp` | ArgoCD application name — links identity to deployment (typically `<cluster-name>-<zone-alias>`) |
| `description` | Human-readable purpose — appears in dashboards and search results |

---

## Phase 2 — Secure the Cluster

The cluster now exists and is registered. Before anything is deployed, we establish secrets access. Applications in Olympus never hardcode credentials — they retrieve them at runtime from Vault.

### Step 3 — Grant Secrets Access via Vault

> *"HashiCorp Vault is the centralized secret management solution. Every secret access is logged for compliance."*

**Repo**: `aws-default-pp-mumbai-vault-rbac`
**File**: `values.yaml`

**Why this step exists**: Applications in Olympus retrieve database credentials, API keys, TLS certificates, and encryption keys from Vault at runtime via a sidecar agent pattern. Each cluster gets its own Vault path (`secrets/data/cluster/<cluster-name>/...`), and only authorized user groups can read/write secrets under that path.

This is not just about the applications — it's also about **developers and operators**. When engineers need to add or rotate secrets for this cluster, they need Vault access granted through these RBAC rules.

Without this step: Vault Agent sidecars fail to authenticate → pods crash-loop → the cluster is non-functional even if everything else is configured.

**What to do**: Search for a reference cluster (e.g., `agentic-cde`) in the file and add the new cluster name adjacent to it in every `clusters` list. There may be multiple groups (SRE, DRE, dev teams) that need access.

```yaml
      - <reference-cluster>
      - <new-cluster-name>    # ← Add here
```

**Why multiple lists?** Different user groups (SRE on-call, platform engineers, application developers) have different access scopes. Each group's cluster list independently grants access to the cluster's Vault secrets path.

---

## Phase 3 — Make the Cluster Deployable

The cluster exists, is registered, and is secured. Now we set up the deployment pipeline — the mechanism that takes application code from a Git repository and delivers it as running containers inside the cluster.

The deployment pipeline in Olympus follows this flow:

```
Application Code → Container Image → ClusterSpec (Helm Chart) → ArgoCD Sync → Live Cluster
         ↓               ↓                    ↓                      ↓
       ${git_repo}     ${ecr_repo}         ${zdd_descriptor}      ${weave_train}
       Step 5           Step 4              Step 6               Step 7
```

### Step 4 — Create the Container Image Registry

> *"CI needs somewhere to push built images. Kubernetes needs somewhere to pull them from."*

**Repo**: `ecr-tf`
**File**: `terraform/ecr/tfvars/olympus-world.tfvars`

**Why this step exists**: Every application in the cluster is packaged as a Docker container image. AWS ECR (Elastic Container Registry) stores these images. The CI pipeline builds the app, pushes the image to ECR, and Kubernetes pulls it during deployment.

This step comes early in the deploy phase because **nothing can be deployed without an image repository**. It's a prerequisite for the CI pipeline to succeed and for Kubernetes to pull images.

**What to do**: Add a new entry to the `prod_repo_list` map:

```terraform
  # ${group} - ${cluster_description}
  "<ecr-repo-name>" = {"info:maintainer" ="${group}", "org:cluster" = "<cluster-name>"},
```

**Key fields**:

| Field | Role |
|-------|------|
| Key (repo name) | The ECR repository name — typically matches the application/chart name |
| `info:maintainer` | Owning team tag — used for cost allocation and ownership tracking |
| `org:cluster` | Which cluster this image belongs to — links ECR to the Olympus cluster |

---

### Step 5 — Register the ArgoCD Application

> *"ArgoCD is the GitOps engine. It watches a Git repository and ensures the cluster's actual state matches the declared state."*

**Repo**: `showroom-argocd-apps`
**File**: `values.yaml`

**Why this step exists**: Olympus deploys clusters using GitOps — the desired state is declared in a Git repository (the ClusterSpec), and ArgoCD continuously reconciles the cluster's actual Kubernetes state against it. This step creates the ArgoCD `Application` resource that:

- Points ArgoCD at the correct Git repository containing the ClusterSpec.
- Specifies which Helm values files to use during rendering.
- Controls whether changes auto-sync or require manual approval.

Without this, there is no link between your Git repo and the Kubernetes namespace. Code changes would have no path to the cluster.

**What to do**: Add a new cluster entry under `zones.aws-default-pp-mumbai.clusters`:

```yaml
      <cluster-name>:
        name: <cluster-name>
        valuesFiles:
        - Values.yaml
        autosync: false
        gitRepo: <git-repo-url>
        syncOptions:
        - Validate=false
```

**Key fields**:

| Field | Role |
|-------|------|
| `gitRepo` | The Git repository containing the ClusterSpec (Helm chart) — ArgoCD watches this |
| `autosync` | `false` = manual sync (for PreProd, you control when deployments happen) |
| `valuesFiles` | Which Helm values files ArgoCD uses to render the chart |
| `syncOptions` | ArgoCD behavior flags (e.g., `Validate=false` skips server-side validation) |

---

### Step 6 — Write the Zone Deployment Descriptor

> *"The ZDD is the deployment contract — it tells Weave WHAT to deploy and WHERE."*

**Repo**: `zdd-aws-default-pp-mumbai`
**Directory**: `cluster-deployment-descriptors/aws-default-pp-mumbai/<cluster-name>/`  *(new directory)*

**Why this step exists**: ArgoCD knows WHERE to sync from (the Git repo), but Weave (the CD orchestrator) needs to know the specific deployment contract: which ClusterSpec version, which zone-specific overrides, and what deployment number. The Zone Deployment Descriptor (ZDD) is that contract.

Additionally, the same ClusterSpec may need different configuration per zone (different URLs, scaling policies, environment labels). The `zone-values/values.yaml` file provides those zone-specific overrides without modifying the ClusterSpec itself.

Without this: Weave's deployment train has no instructions — it doesn't know what version to deploy or what values to apply.

**What to do**: Create two files:

#### `descriptor.yaml` — The Deployment Contract

```yaml
cluster: <cluster-name>
clusterSpec:
  name: <cluster-name>
  version: 0.1.0
deploymentNumber: 1
space: aws-default-pp-mumbai
zoneValues:
- values.yaml
```

#### `zone-values/values.yaml` — Zone-Specific Overrides

```yaml
# <cluster-name> configuration for aws-default-pp-mumbai zone

<helm-chart-name>:
  enabled: true

  hpa:
    cpu: 80
    maxReplicas: 5

  olympusLabels:
    olympusZone: aws-default-pp-mumbai
    olympusZoneEnv: preprod

  envs:
  - name: ${app_access_url}
    value: "https://<url-safe-name>.internal.mum1-pp.zetaapps.in"

  additionalPodAnnotations:
    health.check.enable: 'true'
    health.check.module: http_2xx
    health.check.path: /health
```

**Key fields**:

| Field | Role |
|-------|------|
| `clusterSpec.version` | The exact ClusterSpec version to deploy |
| `deploymentNumber` | Monotonically increasing counter — Weave tracks progress by this number |
| `zoneValues` | References to zone-specific values files (list, in order of precedence) |
| `olympusLabels` | Zone and environment tags applied to all pods — used by observability and routing |

---

### Step 7 — Configure the Deployment Train

> *"Weave orchestrates WHO can deploy, WHEN, and through which approval gates."*

**Repo**: `weave-config`
**File**: `showroom.yaml`

**Why this step exists**: In Olympus, deployments are not ad-hoc. Weave's **Deployment Trains** enforce a structured release process: who can submit a deployment, who can approve or stop it, and which zones the deployment flows through. This is critical for:

- **Audit compliance** — Every deployment is traceable to a person, approval, and change request.
- **Blast radius control** — Trains can target specific zones, preventing accidental production deployments.
- **Team governance** — RBAC rules on the train ensure only authorized teams can deploy.

Without this: The cluster cannot be deployed through Weave's controlled pipeline. You'd have to deploy manually (bypassing all audit and approval controls).

**What to do**: Add a new deployment train entry under `deploymentTrains`:

```yaml
    <cluster-name>-showroom:
      cluster: <cluster-name>
      clusterSpec: <cluster-name>
      name: <cluster-name>-showroom
      rbac:
        rules:
        - action: '*'
          groups:
          - weave-oncall-internal@zeta.tech
          - <additional-admin-groups>
          type: dt
        - action: submit
          groups:
          - zeta-dev@zeta.tech
          - <additional-submit-groups>
          type: dt
        - action: stop
          groups:
          - zeta-dev@zeta.tech
          - <additional-stop-groups>
          type: dt
        - action: userInput
          dts: '*'
          dtt: '*'
          groups:
          - <additional-userinput-groups>
          type: dtt
      zones:
      - dtsType: dts-default
        name: aws-default-pp-mumbai
        space: aws-default-pp-mumbai
```

**Key fields**:

| Field | Role |
|-------|------|
| `cluster` / `clusterSpec` | Must exactly match the cluster name — links the train to the module |
| `rbac.rules` | Controls who can submit, stop, and approve — `action: '*'` grants full control |
| `zones` | Which zone(s) this train deploys to |
| `dtsType` | Deployment train stage type (`dts-default` for PreProd, `dts-with-jsm` for production with change management) |

---

## Phase 4 — Make the Cluster Reachable

The cluster exists, is secured, and has a deployment pipeline. But deployed applications are useless if no one can reach them. Heracles — Olympus's full-stack traffic management platform — handles all traffic routing through a **two-tier hierarchical ingress architecture**:

```
External Client
     │
     ▼
┌──────────────────────────────────────────────────────┐
│  Zone Ingress (Step 8)                               │
│  Routes traffic from the zone perimeter TO clusters  │
│  • Domain hostname binding                           │
│  • Domain → cluster proxy mapping                    │
│  • Path-based routing to cluster upstream             │
└──────────────────────┬───────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────┐
│  Cluster Ingress (Step 9)                            │
│  Routes traffic WITHIN the cluster to K8s services   │
│  • Path → backend service mapping                    │
│  • Timeout and retry configuration                   │
│  • Request transformation (host, URI rewriting)      │
└──────────────────────────────────────────────────────┘
```

### Step 8 — Configure Zone-Level Traffic Routing

> *"Zone Ingress accepts ALL traffic for the zone and routes it to the correct cluster based on domain, path, and tenant."*

**Repo**: `aws-default-pp-mumbai-heracles-zone-manifest`
**Directory**: `templates/clusters/<cluster-name>/`  *(new directory)*

**Why this step exists**: Every HTTP request to any Olympus cluster first hits the zone's ingress gateways. The zone manifest tells these gateways: "When traffic arrives for hostname `agentnexus.internal.mum1-pp.zetaapps.in`, forward it to the `agent-nexus` cluster ingress." Specifically, it defines:

1. **Domain hostnames** — What DNS names this cluster responds to (internal + public).
2. **Cluster proxies** — The upstream address of the cluster's own ingress controller.
3. **Domain-cluster mappings** — How Heracles resolves which cluster handles a given domain.
4. **Path routing** — Which URL paths get routed to this cluster, with CORS and security headers.

Without this: The zone gateway has no idea this cluster exists. HTTP requests get a 404 or are routed to the wrong cluster.

**What to do**: Create 8 files (use a reference cluster like `agentic-cde` as template):

| File | Kind | What it does |
|------|------|-------------|
| `<cluster>-domain-spec-hds.yaml` | HeraclesDomainSpecification | Defines the domain config template |
| `<cluster>-zone-ingress-internal-hcp.yaml` | HeraclesClusterProxy | Internal ingress → cluster proxy address |
| `<cluster>-zone-ingress-internal-hdcm.yaml` | HeraclesDomainClusterMapper | Maps internal domain to cluster upstream |
| `<cluster>-zone-ingress-public-hcp.yaml` | HeraclesClusterProxy | Public ingress → cluster proxy address |
| `<cluster>-zone-ingress-public-hdcm.yaml` | HeraclesDomainClusterMapper | Maps public domain to cluster upstream |
| `internal/<cluster>-internal-domain-hd.yaml` | HeraclesDomain | Binds internal hostname to this cluster |
| `internal/<cluster>-internal-route-hpr.yaml` | HeraclesPathRouter | Path routing rules + CORS for internal traffic |
| `public/<cluster>-public-domain-hd.yaml` | HeraclesDomain | Binds public hostname to this cluster |

**Hostname conventions** (derived from the cluster's URL-safe name):

| Purpose | Pattern | Example |
|---------|---------|---------|
| Internal hostname | `<url-safe>.internal.<zone-domain>` | `agentnexus.internal.mum1-pp.zetaapps.in` |
| Public hostname | `<url-safe>.<zone-domain>` | `agentnexus.mum1-pp.zetaapps.in` |
| Cluster infra address | `<url-safe>.cluster.olympus.infra` | `agentnexus.cluster.olympus.infra` |
| Cluster upstream | `0-0-<url-safe>.nonpci.olympus.infra` | `0-0-agentnexus.nonpci.olympus.infra` |

**Key fields**:

| Field | Role |
|-------|------|
| `thirdpart` | The URL-safe cluster name — used in `HeraclesDomainClusterMapper` to map domain → cluster |
| `pathPrefix` | Short URL prefix for routing (e.g., `/anx`) — appears in `HeraclesPathRouter` |
| `domainClass` | `zone-ingress-internal` or `zone-ingress-public` — determines which gateway handles it |

---

### Step 9 — Configure Cluster-Level Backend Routing

> *"Cluster Ingress is the last mile — it routes traffic from the cluster's Heracles proxy to the actual Kubernetes service."*

**Repo**: `aws-default-pp-mumbai-heracles-cluster-manifest`
**Directory**: `templates/clusters/<cluster-name>/internal/`  *(new directory)*

**Why this step exists**: Zone-level routing (Step 8) gets traffic to the cluster's ingress proxy. But *within* the cluster, Heracles still needs to know which Kubernetes service handles which path, with what timeouts and retries. The `HeraclesClusterRoute` resource is that configuration.

This is also where request transformation happens — stripping the path prefix, rewriting the host header, and setting upstream protocol and timeout values. Without this, traffic arrives at the cluster ingress but has no backend to forward to.

**What to do**: Create a `HeraclesClusterRoute` file:

#### `internal/<cluster-name>-internal-route-hcr.yaml`

```yaml
apiVersion: zeta.tech/v1alpha1
kind: HeraclesClusterRoute
metadata:
  name: <cluster-name>-internal-route-v2
  namespace: <cluster-name>
spec:
  backend:
    port: 8080
    service: <backend-service-name>
  cluster: <url-safe-name>
  config:
    request-transformer:
      prefix-trimmer:
        replace:
          headers:
          - host:$(headers["x-heracles-migrate-host"] or headers["x-forwarded-host"])
          uri: /$(uri_captures[1])
    upstream-setting:
      proxy-setting:
        connect_timeout: 60000
        path: /
        protocol: http
        read_timeout: 60000
        retries: 3
        write_timeout: 60000
      route-setting:
        methods: POST,PUT,DELETE,PATCH,GET,OPTIONS
        preserve_host: true
        strip_path: false
  domainClass: cluster-ingress
  ingressType:
  - internal
  paths:
  - /<path-prefix>/(.*)
```

**Key fields**:

| Field | Role |
|-------|------|
| `namespace` | Must match the cluster name — this route lives inside the cluster's namespace |
| `backend.service` | The Kubernetes service name of the primary application (e.g., `zeta-prompt-library`) |
| `cluster` | The URL-safe cluster name — links to the cluster proxy defined in Step 8 |
| `paths` | Regex path pattern — must align with the `pathPrefix` in the zone manifest |
| `prefix-trimmer` | Strips the path prefix before forwarding (e.g., `/anx/foo` → `/foo`) |
| `proxy-setting` | Timeout and retry configuration for the upstream connection |

---

## Post-Creation Checklist

After all configuration changes are committed and merged, verify end-to-end:

### Configuration Verification

- [ ] **Namespace provisioned** — `kubectl get ns <cluster-name>` returns the namespace
- [ ] **RBAC applied** — Admin groups can access the namespace
- [ ] **ResourceQuota active** — `kubectl describe quota -n <cluster-name>` shows limits
- [ ] **Identity registered** — OlympusClusterConfig appears in the control plane
- [ ] **Vault access granted** — Vault Agent can authenticate from the cluster's service account
- [ ] **ECR repo created** — `aws ecr describe-repositories` includes the repo
- [ ] **ArgoCD app syncs** — Application appears in ArgoCD dashboard and syncs without errors

### Deployment Pipeline Verification

- [ ] **ZDD valid** — Weave can read the deployment descriptor
- [ ] **Deployment train visible** — Train appears in Weave console
- [ ] **First deployment succeeds** — Submit a deployment through Weave and verify ArgoCD sync

### Traffic Verification

- [ ] **Internal URL resolves** — `curl https://<url-safe-name>.internal.mum1-pp.zetaapps.in/<path-prefix>/health` returns 200
- [ ] **Public URL resolves** — `curl https://<url-safe-name>.mum1-pp.zetaapps.in/<path-prefix>/health` returns 200
- [ ] **Heracles routes correct** — Zone ingress correctly forwards to cluster ingress

---

## Quick Reference

### Phases and Steps

| Phase | Step | Repository | What it does | Domain Concept |
|-------|------|-----------|-------------|----------------|
| **Exist** | 1 | `olympus-cluster-provisioner` | Creates K8s namespace + RBAC + quotas | Cluster Definition |
| **Exist** | 2 | `olympus-clusters` | Registers cluster in the control plane | Cluster Identity |
| **Secure** | 3 | `aws-default-pp-mumbai-vault-rbac` | Grants Vault secrets access | Secrets Management |
| **Deploy** | 4 | `ecr-tf` | Creates container image repository | Application Image Storage |
| **Deploy** | 5 | `showroom-argocd-apps` | Registers ArgoCD GitOps application | ClusterSpec Sync |
| **Deploy** | 6 | `zdd-aws-default-pp-mumbai` | Defines deployment contract + zone overrides | Zone Deployment Descriptor |
| **Deploy** | 7 | `weave-config` | Configures deployment train (CI/CD pipeline) | Deployment Lifecycle |
| **Reach** | 8 | `aws-default-pp-mumbai-heracles-zone-manifest` | Zone-level domain + path routing | Cluster Interaction (Zone → Cluster) |
| **Reach** | 9 | `aws-default-pp-mumbai-heracles-cluster-manifest` | Cluster-level backend routing | Cluster Interaction (Ingress → Service) |

### Naming Conventions

| Context | Format | Example |
|---------|--------|---------|
| Cluster name | lowercase, hyphen-separated | `agent-nexus` |
| K8s namespace | same as cluster name | `agent-nexus` |
| URL-safe name | no hyphens | `agentnexus` |
| Internal hostname | `<url-safe>.internal.<zone-domain>` | `agentnexus.internal.mum1-pp.zetaapps.in` |
| Public hostname | `<url-safe>.<zone-domain>` | `agentnexus.mum1-pp.zetaapps.in` |
| Cluster infra hostname | `<url-safe>.cluster.olympus.infra` | `agentnexus.cluster.olympus.infra` |
| Upstream | `0-0-<url-safe>.nonpci.olympus.infra` | `0-0-agentnexus.nonpci.olympus.infra` |
| ArgoCD app | `<cluster-name>-<zone-alias>` | `agent-nexus-pp` |
| Deployment train | `<cluster-name>-showroom` | `agent-nexus-showroom` |
| ECR repo | application/chart name | `zeta-prompt-library` |
| OlympusClusterConfig | `<cluster-name>.<zone-name>` | `agent-nexus.aws-default-pp-mumbai` |

---

*This SOP was derived from the provisioning of the `agent-nexus` cluster in the `aws-default-pp-mumbai` zone (February 2026). Domain model concepts referenced from the `zeta-ek-domain-semantics-cluster` knowledge base.*