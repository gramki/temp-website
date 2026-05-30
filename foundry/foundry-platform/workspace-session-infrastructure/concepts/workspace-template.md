# Workspace Template

The Workspace Template is Layer 2 of the workspace layering model — how Workshop and Workbench content from the Workshop Definition Repository is merged into a session pod spec at start time.

## What it is

Each session is provisioned for a specific `(workspace-type, workbench)` pair. The template defines what Workshop-specific content the session receives: devcontainer configuration, Scenario manifests, Skills, and repository bindings.

Session Infrastructure does not store templates independently — it interprets content from the Workshop Definition Repo and materializes it via the `workspace-merge` init container.

Template source layout:

```
workshop-{id}/
└── workbenches/
    └── {product-code}/
        └── .devcontainer/
            ├── development/
            │   └── devcontainer.json
            ├── qa/
            │   └── devcontainer.json
            └── ...
```

Key characteristics:

| Aspect | Detail |
|--------|--------|
| **Scope** | Per (Workspace Type, Workbench) |
| **When applied** | Session start — `workspace-merge` init container |
| **Coder integration** | Template registered with Coder Kubernetes provider |
| **Merge output** | Written to `merged-content` emptyDir, mounted at `/workspace/.foundry/` |

## devcontainer.json interpretation

Session Infrastructure interprets `.devcontainer/devcontainer.json` (per workspace type under the Workbench) to configure the session environment:

| devcontainer field | Session Infrastructure action |
|--------------------|----------------------------|
| `features` | Run feature install scripts during workspace-merge |
| `customizations.vscode.extensions` | Install additional extensions (beyond platform defaults) |
| `postCreateCommand` | Record for execution after main container start |
| `remoteEnv` | Inject as container environment variables |
| `mounts` | Map to additional emptyDir or PVC subpaths where supported |
| `forwardPorts` | Document only — ingress routes to Code Server port 8080 |

The platform base image already satisfies most `image` references — devcontainer `image` fields are ignored in favor of the platform base image with workspace-type activation.

## Coder template composition

Coder's Kubernetes workspace provider receives a template derived from Session Infrastructure's pod spec. Session Infrastructure owns the template definition directly (Kubernetes manifests, not Terraform):

```yaml
# Coder template (simplified) — owned by Session Infrastructure
metadata:
  name: foundry-{workspace-type}
spec:
  # Pod spec with init containers, single workspace container, volumes
  # Parameterized by: session_id, foundry_id, workbench_id, user_id
```

Coder handles:
- Workspace create/stop/resume against the K8s cluster
- Wildcard proxy routing to `{session-id}.sessions.{domain}`
- Dotfiles sync (optional, per-user Coder settings)

Session Management remains the source of truth for session state — Coder is the execution layer, not the lifecycle authority.

## Workspace merge flow

```
workspace-merge init container
    │
    ├── Resolve workbench_id → Workshop Definition Repo path
    │
    ├── Fetch .devcontainer/{workspace_type}/devcontainer.json
    │
    ├── Fetch Scenarios referenced by active Work Catalog
    │
    ├── Fetch Skills from Skill Registry (manifests + packages)
    │
    ├── Apply devcontainer features and customizations
    │
    └── Write merged output to /merged-content/workshop/
            │
            ├── scenarios/          → available to WO Runtime
            ├── skills/               → skill-cache population
            └── devcontainer.env      → environment injection
```

Skills are copied to the `skill-cache` emptyDir for WO Runtime installation at daemon startup.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Session Infrastructure** | Interprets devcontainer, runs merge, registers Coder template |
| **Management** | Workshop Definition Repo structure and validation |
| **Work Order Runtime** | Consumes merged Scenarios and Skills at session start |
| **Agent Fabric** | Skill Registry packages fetched during merge |

## Related concepts

- [Platform Base Image](platform-base-image.md) — Layer 1 runtime stack
- [Admin Layering](admin-layering.md) — Layer 3 Foundry admin overlay
- [Session Pod](session-pod.md) — Pod spec produced from template
- [Workspace Session](../../concepts/workspace-session.md) — Platform-wide session definition

## Further reading

- [../platform-developer-guide/coder-on-kubernetes.md](../platform-developer-guide/coder-on-kubernetes.md) — Coder provider configuration
- [../../management/platform-developer-guide/workshop-repository.md](../../management/platform-developer-guide/workshop-repository.md) — Workshop repo structure
