# Publishing Workflow

This guide covers how to publish scenarios and OI workflows from personal experimentation to shared catalogs.

## Publishing Levels

Content can be published to different levels, each with different scope and approval requirements:

| Level | Scope | Approval Required | Who Can Publish |
|-------|-------|-------------------|-----------------|
| User | You only (when activated) | None | You |
| Workbench | Your project team | Workbench Manager | Team members |
| Workshop | Your business unit | Workshop Admin | Workshop members |
| Foundry | Your organization | Foundry Admin | Foundry members |

## Publishing to User Catalog

User catalog is for personal experimentation — no approval needed.

### Direct Publish

```bash
# Publish a scenario
foundry scenario publish ./scenarios/implement-feature.yaml --to user

# Publish an OI workflow
foundry workflow publish ./workflow.yaml --to user
```

This:
1. Creates your user catalog repo if it doesn't exist
2. Copies the file to the appropriate path
3. Triggers sync to Metadata Service

### User Catalog Path

Your user catalog is a dedicated repository provisioned on first publish:
```
user-work-catalog-{userId}/
```

Content follows the same layout as other catalogs:
```
user-work-catalog-{userId}/
└── work-catalog/
    └── build/
        └── product-intent/
            └── development/
                └── scenarios/
                    └── implement-feature.yaml
```

## Publishing to Workbench/Workshop/Foundry

Publishing to shared catalogs requires approval via pull request.

### Step 1: Create a Branch

```bash
# Clone the target catalog repo (if not already)
git clone <workbench-catalog-repo>

# Create a feature branch
git checkout -b add-implement-feature-scenario
```

### Step 2: Add Your Content

Copy your tested scenario to the appropriate location:

```bash
# For Workbench
cp ./implement-feature.yaml \
   workshop-{id}/workbenches/{wb}/work-catalog/build/product-intent/development/scenarios/

# For Workshop
cp ./implement-feature.yaml \
   workshop-{id}/work-catalog/build/product-intent/development/scenarios/

# For Foundry
cp ./implement-feature.yaml \
   foundry-{id}/work-catalog/build/product-intent/development/scenarios/
```

### Step 3: Validate

Run validation to ensure the content is correct:

```bash
foundry scenario validate ./scenarios/implement-feature.yaml
```

### Step 4: Commit and Push

```bash
git add .
git commit -m "Add implement-feature scenario for development workspace"
git push -u origin add-implement-feature-scenario
```

### Step 5: Create Pull Request

```bash
# Using the CLI
foundry pr create \
  --title "Add implement-feature scenario" \
  --description "Adds a custom implementation scenario for the development workspace"

# Or use the Git provider UI
```

### Step 6: Approval and Merge

The appropriate manager reviews the PR:

| Target Level | Reviewer |
|--------------|----------|
| Workbench | Workbench Manager |
| Workshop | Workshop Admin |
| Foundry | Foundry Admin |

Reviewers check:
- Scenario/workflow validity
- Appropriateness for the target level
- Potential conflicts with existing content
- Governance compliance

After approval and merge:
1. Catalog sync service detects the change
2. Metadata Service is updated
3. Content becomes available in effective catalogs

## Publishing via IDE

The IDE streamlines the publishing workflow.

### Publish Command

1. Open the scenario file
2. **Command Palette:** "Scenario: Publish..."
3. Select target level (User, Workbench, Workshop, Foundry)
4. For shared catalogs, the IDE creates a branch and PR automatically

### Publish Panel

**View > Work Catalog Publish Panel**

Shows:
- Content ready to publish (modified scenarios)
- Target level selection
- PR status for pending publishes
- Recent publish history

## Graduation Path

Content typically graduates through levels:

```
User (experiment)
    ↓ works well for me
Workbench (team adoption)
    ↓ works well for team
Workshop (business unit standard)
    ↓ works well for BU
Foundry (organization standard)
```

### Promoting Content

To promote content from one level to the next:

```bash
# Promote from Workbench to Workshop
foundry scenario promote \
  --from workbench/<workbench-id> \
  --to workshop/<workshop-id> \
  --scenario build/product-intent/development/scenarios/implement-feature.yaml
```

This creates a PR in the Workshop catalog with the content from Workbench.

### Handling Overrides

When promoting, consider:
- Does the Workshop already have this scenario? (You're replacing it)
- Does Foundry have a default? (You're overriding it)
- Are there Workbench-specific customizations that should remain? (Document them)

## Version Management

Scenarios and OI Workflows are not versioned in the catalog — they're named references. However, the Git repository provides version history.

### Viewing History

```bash
# See change history for a scenario
git log -- scenarios/implement-feature.yaml
```

### Rolling Back

```bash
# Revert to a previous version
git revert <commit-hash>
git push
```

The catalog sync will update to reflect the reverted state.

## Pre-Publish Checklist

Before publishing to shared catalogs:

- [ ] **Validated** — All schema and reference checks pass
- [ ] **Tested** — Dry-run and/or user catalog testing complete
- [ ] **Documented** — Description field explains what the scenario does
- [ ] **Scoped correctly** — `workspace-ingress` vs `workspace-internal` is intentional
- [ ] **Skills available** — All required skills exist in the target environment
- [ ] **No conflicts** — Understand what this overrides (if anything)

## Handling Rejections

If a PR is rejected:

1. **Review feedback** — Understand why it was rejected
2. **Make changes** — Update the scenario to address concerns
3. **Re-test** — Validate and dry-run again
4. **Update PR** — Push new commits to the same branch
5. **Request re-review** — Notify the reviewer

Common rejection reasons:
- Scenario duplicates existing functionality
- Required skills not approved for this level
- Scope too broad for target level
- Missing documentation/description
- Validation module errors on the PR

## Monitoring Published Content

After publishing, monitor adoption:

**Web App:** Resources > Work Catalogs > [your scenario] > Usage

Shows:
- Work Orders created using this scenario
- Success/failure rates
- Which Workbenches are using it
- Override status at lower levels

**CLI:**
```bash
foundry scenario stats build/product-intent/development/scenarios/implement-feature
```
