# Repositories & Tools Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/repositories`

**Group:** Resources

**Purpose:** Access all repositories and external tools linked to the Workbench.

---

## Page Sections

### 1. Git Repositories

| Repository | Storage | Description | Content Actions |
|------------|---------|-------------|-----------------|
| **Intent** | GitHub | Product Intents, PDRs, PSDs | Browse, Add Intent, Add doc |
| **Design** | GitHub | Architecture, API models | Browse, Add doc |
| **Code** | GitHub (multiple) | Source code repos | Browse only (edit in IDE) |
| **Quality Automation** | GitHub | Test automation code | Browse only (edit in IDE) |

| Element | Description |
|---------|-------------|
| **Repo list** | All linked Git repositories |
| **Per-repo info** | Name, URL, recent commits |
| **Quick actions** | Open in GitHub, view commits, browse content |

### Repository Content Management

Some repositories support direct content management from the console:

| Repository | Supported Actions |
|------------|-------------------|
| **Intent** | Create new Intent from PDR (gets PI ID from Metadata Service), add PDR/PSD docs, upload mockups, organize folders |
| **Design** | Create design doc, add architecture diagrams, organize folders |
| **Code** | Browse only — code editing happens in Workspace Sessions (IDE) |
| **Quality Automation** | Browse only — test code editing happens in Workspace Sessions (IDE) |

**Intent Content Actions:**

| Action | Description |
|--------|-------------|
| **Create Intent** | Request PI ID from Metadata Service after Go/Pivot PDR, create folder, add initial README |
| **Add PDR** | Link or upload authorizing PDR under Intent folder |
| **Add PSD** | Create/upload PSD document(s) that refine the Product Intent |
| **Add Mockup** | Upload mockup images or add Figma links |
| **Organize** | Move/rename folders (within Intent repo structure) |

**Design Content Actions:**

| Action | Description |
|--------|-------------|
| **Add Design Doc** | Create new design document |
| **Add Diagram** | Upload architecture/flow diagrams |
| **Organize** | Move/rename folders |

### 2. Code Repositories Detail

| Element | Description |
|---------|-------------|
| **Repository name** | Identity |
| **GitHub URL** | Link to repo |
| **Linked component** | System/Capability this repo serves |
| **Tags** | FoundryID, Workshop, Workbench, Product Code |
| **Recent commits** | Last N commits |
| **Open PRs** | Pull requests awaiting review |
| **Branch info** | Default branch, active branches |

### 3. Workbench Services

| Service | Description |
|---------|-------------|
| **Ontology Service** | Product structure (auto-provisioned) |
| **Metadata Service** | PI IDs, commit tracking |
| **Quality Service** | TestRail + Git wrapper |

### 4. External Tools (Integrated)

| Tool | Integration | Actions |
|------|-------------|---------|
| **Figma** | OAuth | View projects, open in Figma |
| **TestRail** | OAuth | View test projects, open in TestRail |
| **Jira** | OAuth | View linked projects |
| **Olympus Weave** | OAuth | View in Weave console |

### 5. Additional Tool References

Custom tool references (URL-based, no deep integration).

| Element | Description |
|---------|-------------|
| **Tool list** | User-added tool references |
| **Per-tool info** | Name, URL, description, category |
| **Categories** | Documentation, Monitoring, Analytics, Communication, Other |
| **Actions** | Open URL, Edit, Remove |

Example entries:
- Confluence space for architecture docs
- Datadog dashboard for this Product
- Slack channel for the team
- Internal wiki pages

### 6. Jira Projects (Label-filtered)

| Project | Type | Label Filter | Description |
|---------|------|--------------|-------------|
| Operations | JSM | `workbench:{id}` | Problems, incidents |
| Feedback | Jira | `workbench:{id}` | FIRs, bugs |
| Work | Jira | `workbench:{id}` | Work items |

---

## Actions

### Repository Actions

| Action | Who | Description |
|--------|-----|-------------|
| Create code repo | Manager | New repo in GitHub Org |
| Import repository | Manager | Tag existing repo in GitHub Org |
| Repository settings | Manager | Access control, branch protection |
| View in GitHub | All | Open repo in GitHub |
| Browse content | All | View files in repository |

### Content Actions (Intent, Design repos)

| Action | Who | Description |
|--------|-----|-------------|
| Create Intent | Manager, Member | Request PI ID from Go/Pivot PDR, create Intent folder |
| Add PDR/PSD | Manager, Member | Add authorizing PDR or PSD refinement to Intent |
| Add Design Doc | Manager, Member | Create design document |
| Upload file | Manager, Member | Add mockups, diagrams |
| Organize folders | Manager | Move/rename within repo |

### Tool Actions

| Action | Who | Description |
|--------|-----|-------------|
| Link integrated tool | Manager | OAuth connect (Figma, TestRail, Jira, Weave) |
| Add tool reference | Manager, Member | Add custom URL reference |
| Edit tool reference | Manager, Member | Update name, URL, description |
| Remove tool reference | Manager | Delete custom reference |
| Update Jira filter | Manager | Change label filter |
| View in tool | All | Open external tool |

---

## Repository Management

| Element | Description |
|---------|-------------|
| **Add repository** | Manager creates new code repo |
| **Import repository** | Tag existing repo in GitHub Org |
| **Repository settings** | Access control, branch protection |
| **Content browser** | Navigate and manage repo contents (Intent, Design) |

---

## Integrations

- **GitHub** — Via GitHub App (org management)
- **Figma** — OAuth
- **TestRail** — OAuth
- **Jira/JSM** — OAuth
- **Olympus Weave** — OAuth

---

## Related Consoles

- **Components Console** — Which System uses which repo
- **CI Console** — Pipelines for repos
- **Admin Console** — Integration settings
