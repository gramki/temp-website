# Build Track — Scenarios

**Track:** Build — turning specs into verified artifacts.

## Workspaces in this Track

| Workspace | Folder | Example Scenarios |
|-----------|--------|-------------------|
| Product Specification | [product-specification/](product-specification/) | Refine spec from design feedback, Clarify requirements |
| UX Design | [ux-design/](ux-design/) | Design system component, Prototype interaction |
| Development | [development/](development/) | Implement feature from spec, Fix bug from report, Code review |
| QA | [qa/](qa/) | Write test cases, Execute test suite, Report defects |
| Release | [release/](release/) | Build artifact, Run CI pipeline, Publish to distribution store |
| Governance | [governance/](governance/) | Validate build evidence, Enforce quality gate |

## Core Build Scenarios

The following scenarios are referenced by the [PI workflow](../../orchestrator/sample-pi-workflow.yaml) and are executed as the Product Intent moves through the Build Track.

### Product Specification Workspace

#### `create-product-specification`

Creates a Product Specification Document (PSD) from a Product Intent.

| Aspect | Detail |
|--------|--------|
| **Trigger** | Release Intent milestone `product-specification-development-start` |
| **Inputs** | PI README, PDR (if exists), stakeholder requirements |
| **Outputs** | PSD committed to Intent Repository |
| **Skills** | `product-specification-authoring`, `requirements-analysis` |
| **Knowledge** | Product domain docs, existing PSDs, API contracts |
| **Tools** | Intent Repository (Git), Documentation generators |
| **Success criteria** | PSD passes schema validation; all required sections complete |
| **Typical actor** | Product Manager |

Key activities:
1. Analyze PI problem statement and proposed solution
2. Gather detailed requirements from stakeholders
3. Define user stories with acceptance criteria
4. Specify API contracts and data models
5. Document non-functional requirements
6. Delegate UX tasks (mockups, visual design) as needed
7. Commit PSD to `PI-{id}/psd/` folder

---

### Development Workspace

#### `implement-product-specification`

Implements a feature based on the Product Specification Document.

| Aspect | Detail |
|--------|--------|
| **Trigger** | PI enters `specified` stage |
| **Inputs** | PSD, UI mockups, API contracts |
| **Outputs** | Feature branch, PRs, passing CI |
| **Skills** | `code-implementation`, `test-writing`, `pr-authoring` |
| **Knowledge** | Codebase architecture, coding standards, API docs |
| **Tools** | Git, IDE, CI/CD pipeline, code review tools |
| **Success criteria** | All PRs merged; CI passes; code coverage meets threshold |
| **Typical actor** | Developer |

Key activities:
1. Create feature branch
2. Implement backend logic per API contracts
3. Implement frontend per UI mockups
4. Write unit and integration tests
5. Create PRs with descriptive summaries
6. Address code review feedback
7. Merge to main branch

---

### QA Workspace

#### `prepare-test-suite-for-product-specification`

Creates a test plan and automated test cases based on the PSD.

| Aspect | Detail |
|--------|--------|
| **Trigger** | PI enters `specified` stage (parallel with development) |
| **Inputs** | PSD, user stories, acceptance criteria |
| **Outputs** | Test plan, automated test cases |
| **Skills** | `test-planning`, `test-automation`, `requirements-mapping` |
| **Knowledge** | Testing frameworks, product domain, existing test suites |
| **Tools** | Test management system, test automation framework |
| **Success criteria** | Test plan reviewed; all acceptance criteria have test coverage |
| **Typical actor** | QA Engineer |

Key activities:
1. Analyze PSD for testable requirements
2. Create test plan with coverage matrix
3. Define test cases for each user story
4. Implement automated test scripts
5. Set up test data and fixtures
6. Document manual test procedures (if any)

#### `test-developed-feature`

Executes test suite against the implemented feature.

| Aspect | Detail |
|--------|--------|
| **Trigger** | Development and test prep WO Group completes |
| **Inputs** | Deployed feature, test suite, test data |
| **Outputs** | Test results, defect reports |
| **Skills** | `test-execution`, `defect-reporting`, `root-cause-analysis` |
| **Knowledge** | Test suite, product behavior, defect tracking |
| **Tools** | Test automation runner, defect tracker, CI/CD |
| **Success criteria** | All tests pass; coverage threshold met; no critical defects |
| **Typical actor** | QA Engineer |

Key activities:
1. Deploy feature to test environment
2. Execute automated test suite
3. Perform exploratory testing
4. Document defects with reproduction steps
5. Verify defect fixes
6. Sign off on test completion

---

### Release Workspace

#### `accept-completed-product-intent`

Reviews and accepts a PI that has passed QA for release.

| Aspect | Detail |
|--------|--------|
| **Trigger** | PI enters `ready-for-release` stage |
| **Inputs** | PI, PSD, test results, code changes |
| **Outputs** | Acceptance record |
| **Skills** | `release-review`, `compliance-verification` |
| **Knowledge** | Release criteria, compliance requirements |
| **Tools** | Release dashboard, artifact repository |
| **Success criteria** | All release criteria met; acceptance signed |
| **Typical actor** | Release Manager |

Key activities:
1. Verify all tests passed
2. Review code changes and PR history
3. Confirm documentation complete
4. Check compliance requirements
5. Sign off on acceptance

#### `prepare-customer-release`

Prepares the PI for customer deployment.

| Aspect | Detail |
|--------|--------|
| **Trigger** | Acceptance WO completes |
| **Inputs** | Accepted PI, build artifacts |
| **Outputs** | Release package, release notes, deployment artifacts |
| **Skills** | `release-packaging`, `documentation`, `deployment-prep` |
| **Knowledge** | Release process, deployment targets, customer communication |
| **Tools** | Artifact repository, release notes generator, deployment pipeline |
| **Success criteria** | Release package validated; release notes complete; deployment ready |
| **Typical actor** | Release Manager |

Key activities:
1. Gather build artifacts
2. Generate release notes from PI and PSD
3. Create deployment package
4. Validate package integrity
5. Stage for deployment
6. Notify stakeholders

---

## Adding Scenarios

Each Workspace folder will contain scenario definitions as they are authored. A scenario definition includes:

- Scenario name and description
- Inputs and outputs
- Skills required
- Knowledge required
- Tools required
- Success criteria
- Agent recommendations

## Read Next

- [../README.md](../README.md) — Scenario Authoring module overview
- [../../orchestrator/pi-journey.md](../../orchestrator/pi-journey.md) — End-to-end PI walkthrough
- [../../orchestrator/sample-pi-workflow.yaml](../../orchestrator/sample-pi-workflow.yaml) — PI workflow referencing these scenarios
- [../../../ace/workspaces/](../../../ace/workspaces/README.md) — Workspace definitions
