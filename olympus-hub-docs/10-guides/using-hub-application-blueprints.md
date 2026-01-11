# Using Hub Application Blueprints

> **Audience:** Developers using published Hub Application Blueprints in their scenarios

This guide walks through subscribing to and using a `HubApplicationBlueprintSpec` — a reusable application container that you extend with your own DSL or configuration files.

---

## Overview

Hub Application Blueprints provide pre-built application containers (DSL runtimes, interpreters, low-code engines) that you can customize with your own files. Instead of building containers from scratch, you:

1. Subscribe to a Blueprint package
2. Reference the Blueprint in your `HubApplicationSpec`
3. Provide your DSL/configuration files
4. CI builds the final container automatically

---

## Step 1: Discover and Subscribe

### Browse Marketplace

1. Open **Marketplace Console** from Automation Developer Desk
2. Search or filter for Hub Application Blueprints
3. Filter by category (e.g., "integration", "rules-engine")
4. Review Blueprint details:
   - Description and use cases
   - Required and optional inputs
   - Version history
   - Publisher information

### Review Blueprint Requirements

Before subscribing, understand what the Blueprint expects:

```yaml
# Example Blueprint inputs
inputs:
  - name: "routes"
    description: "Camel route definitions"
    required: true
    filePattern: "*.{xml,yaml}"
  - name: "config"
    description: "Optional configuration"
    required: false
```

### Subscribe to Package

**Via Marketplace Console:**
1. Click **Subscribe** on the package
2. Select target workbench
3. Submit subscription request
4. Await admin approval

**Via CLI:**
```bash
hub marketplace subscribe \
  --package camel-integration-suite \
  --version "^1.0.0" \
  --workbench payment-ops-dev
```

---

## Step 2: Create Your Application

Once subscribed, the Blueprint is available in your workbench. Create a `HubApplicationSpec` that references it.

### HubApplicationSpec with Blueprint

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-routes
  namespace: payment-ops-dev

spec:
  # Reference the subscribed Blueprint
  blueprint:
    ref: "camel-dsl-runtime"      # HubApplicationBlueprintSpec name
    version: "^1.0.0"             # Semver version range
  
  # Provide your files for the Blueprint's inputs
  inputs:
    routes:
      path: "./camel-routes/"     # Path in your workbench Git repo
    config:
      path: "./config/"           # Optional input
  
  # Scenario binding
  scenarios:
    - payment-processing
  
  # Resource requirements (optional)
  resources:
    cpu: "500m"
    memory: "512Mi"
```

### Key Fields

| Field | Description |
|-------|-------------|
| `blueprint.ref` | Name of the HubApplicationBlueprintSpec from subscribed package |
| `blueprint.version` | Semver constraint for Blueprint version |
| `inputs.<name>.path` | Path in Git repository for each Blueprint input |
| `scenarios` | Scenarios this application handles |

---

## Step 3: Provide Your Files

Create the files referenced in your `inputs`:

```
your-workbench-repo/
├── camel-routes/
│   ├── payment-inbound.xml
│   ├── payment-processing.yaml
│   └── payment-outbound.xml
├── config/
│   └── app-settings.yaml
└── specs/
    └── payment-routes.yaml  # Your HubApplicationSpec
```

### Example: Camel Route File

```xml
<!-- camel-routes/payment-inbound.xml -->
<routes xmlns="http://camel.apache.org/schema/spring">
  <route id="payment-inbound">
    <from uri="direct:payment-received"/>
    <log message="Processing payment: ${body}"/>
    <to uri="direct:validate-payment"/>
  </route>
  
  <route id="validate-payment">
    <from uri="direct:validate-payment"/>
    <bean ref="paymentValidator"/>
    <to uri="direct:process-payment"/>
  </route>
</routes>
```

---

## Step 4: Build and Deploy

### CI Build Flow

When you push changes (or trigger a build manually):

1. **CI detects Blueprint reference** in your HubApplicationSpec
2. **Resolves Blueprint** from Marketplace
3. **Validates your inputs** against Blueprint requirements
4. **Executes build recipe** (copies your files into container)
5. **Pushes result** to your Artifact Registry

### Trigger Build

**On Git push:**
Changes to your input files automatically trigger a build.

**Manual:**
```bash
hub ci build --application payment-routes
```

### Monitor Build

```bash
# Check build status
hub ci status --application payment-routes

# View build logs
hub ci logs --application payment-routes --build latest
```

### Deploy

Once built, deploy as any Hub Application:

```bash
hub deploy scenario payment-processing \
  --workbench payment-ops-dev \
  --stage DEV
```

---

## Understanding the Build

### What Happens During Build

The CI subsystem:

1. Pulls the Blueprint's base container
2. Creates a new OCI layer
3. Copies your files to the Blueprint-specified destinations
4. Produces a new container with your customizations

```
Blueprint Base Container          Your Container
┌────────────────────────┐        ┌────────────────────────┐
│ Layer 3: Camel Runtime │   →    │ Layer 3: Camel Runtime │
│ Layer 2: Java          │   →    │ Layer 2: Java          │
│ Layer 1: Base OS       │   →    │ Layer 1: Base OS       │
└────────────────────────┘        │ Layer 4: YOUR ROUTES   │ ← New
                                  └────────────────────────┘
```

### OCI Layer Efficiency

- Base layers are shared (not duplicated)
- Only your files are stored as a new layer
- Fast builds and efficient storage

---

## Managing Versions

### Blueprint Version Constraints

| Constraint | Behavior |
|------------|----------|
| `^1.0.0` | Any 1.x.x (recommended for stability) |
| `~1.2.0` | Any 1.2.x only |
| `1.2.3` | Exact version only |
| `>=1.0.0` | Any version 1.0.0 or higher |

### Updating to New Blueprint Version

When a new Blueprint version is available:

1. Review release notes in Marketplace Console
2. Update version constraint if needed:
   ```yaml
   blueprint:
     ref: "camel-dsl-runtime"
     version: "^2.0.0"  # Updated
   ```
3. Test with new version in DEV
4. Promote to higher environments

### Notifications

You'll receive notifications when:
- New Blueprint version is available
- Blueprint is deprecated
- Security issues are detected

---

## Troubleshooting

### Build Failures

| Error | Cause | Solution |
|-------|-------|----------|
| "Blueprint not found" | Blueprint ref typo or not subscribed | Verify subscription and ref name |
| "Required input missing" | Missing required input path | Add the required input to spec |
| "Input path not found" | Git path doesn't exist | Create the directory/files |
| "File pattern mismatch" | Files don't match expected pattern | Check Blueprint's filePattern |

### Checking Input Compatibility

```bash
# Validate your spec against Blueprint requirements
hub marketplace validate-inputs \
  --application payment-routes
```

### Viewing Build Details

```bash
# See what files were included
hub ci build-info --application payment-routes --build latest

# Output:
# Blueprint: camel-dsl-runtime:1.0.0
# Recipe: copy-only
# Inputs:
#   routes: ./camel-routes/ (5 files)
#   config: ./config/ (1 file)
# Build time: 12s
```

---

## Best Practices

### File Organization

```
your-repo/
├── blueprint-inputs/        # Group all Blueprint inputs
│   ├── routes/
│   └── config/
├── specs/                   # Your Hub specs
│   └── payment-routes.yaml
└── tests/                   # Test cases
```

### Version Pinning

For production workbenches, consider tighter version constraints:

```yaml
# DEV: Accept minor updates
blueprint:
  version: "^1.0.0"

# PROD: More conservative
blueprint:
  version: "~1.2.0"  # Only patch updates
```

### Testing

1. Validate inputs before committing
2. Test in DEV with real scenarios
3. Review Blueprint release notes before updating

---

## Example: Complete Workflow

### 1. Subscribe to Package

```bash
hub marketplace subscribe \
  --package camel-integration-suite \
  --version "^1.0.0" \
  --workbench payment-ops-dev
```

### 2. Create Application Spec

```yaml
# specs/payment-routes.yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-routes
spec:
  blueprint:
    ref: "camel-dsl-runtime"
    version: "^1.0.0"
  inputs:
    routes:
      path: "./camel-routes/"
  scenarios:
    - payment-processing
```

### 3. Create Your Routes

```yaml
# camel-routes/payment-route.yaml
- route:
    id: payment-processing
    from:
      uri: direct:payment-received
    steps:
      - to: http://payment-gateway/process
      - to: direct:update-status
```

### 4. Build and Deploy

```bash
# Commit and push triggers build
git add .
git commit -m "Add payment routes"
git push

# Or manual build
hub ci build --application payment-routes

# Deploy
hub deploy scenario payment-processing
```

---

## Related Documentation

- [Hub Application Blueprints](../04-subsystems/marketplace/hub-application-blueprints.md) — Technical reference
- [Blueprint-Based Builds](../04-subsystems/ci-subsystem/blueprint-based-builds.md) — CI details
- [Subscribing to Packages](./subscribing-to-packages.md) — General subscription guide
- [Hub Application](../02-system-design/implementation-concepts/hub-application.md) — HubApplicationSpec reference
