# Governance Rules

[← Back to Document Governance](README.md) · [ERE Guide](../README.md)

Governance rules ensure consistent provisioning, access control, and lifecycle management of documentation infrastructure.

---

## Core Governance Rules

| Rule | Policy |
|------|--------|
| **Auto-provisioning** | Bootstrap Kit creates repos + SharePoint folders from templates (validated by Engagement Registry) |
| **Cross-references** | Git docs reference SharePoint via URLs |
| **Archival** | Repos become **read-only** on Engagement completion |
| **Access control** | Exploration repos: access per Exploration team; Engagement repos: role-based access |

---

## Auto-Provisioning

The **Bootstrap Kit** automatically provisions infrastructure when Explorations or Engagements are initiated (after validation by the **Engagement Registry**):

### Exploration Provisioning

When an Exploration is created:

1. Git repo `EXP-{CODE}-exploration` created from template
2. SharePoint folder `{Customer}/EXP-{CODE}` created with standard structure
3. Team access configured based on assigned Exploration team
4. Initial README.md populated with Exploration metadata

### Engagement Provisioning

When an Engagement is initiated:

1. Git repos created:
   - `ENG-{CODE}-requirements` from requirements template
   - `ENG-{CODE}-project` from project template
2. SharePoint folder `{Customer}/ENG-{CODE}` created with standard structure
3. Role-based access configured based on Engagement role assignments
4. Engagement charter template pre-populated from Exploration artifacts
5. Outlook Plugin configured with Engagement tags for email categorization

---

## Access Control

### Exploration Repos

| Scope | Access |
|-------|--------|
| Exploration team members | Read + Write |
| Sales / Account Management | Read |
| ERC | Read |
| Other teams | No access (until Engagement initiated) |

### Engagement Repos

| Role | Requirements Repo | Project Repo |
|------|-------------------|--------------|
| EPM, EA, ELs | Read + Write | Read + Write |
| EPO | Read + Write | Read |
| EO, Client Partner | Read | Read |
| Squad members | Read (limited) | Read (limited) |
| ERC | Read | Read |
| Customer | No direct access | No direct access |

Customer-facing content is shared via SharePoint, not Git repos.

---

## Archival

When an Engagement reaches **Complete**:

1. Both Git repos become **read-only**
2. Archive flag added to repo metadata
3. SharePoint folders remain accessible (read-only for historical reference)
4. Knowledge artifacts extracted to Pattern Library / Case Study repository
5. Reusable components tagged for discovery

Archived repos can be referenced but not modified. Any corrections require a documented exception process.

---

## Cross-Reference Standards

### Git → SharePoint

```markdown
## Customer Documents

- Original RFP: [Link](https://sharepoint.com/sites/CustomerName/EXP-CODE/Customer-Provided/...)
- Signed SOW: [Link](https://sharepoint.com/sites/CustomerName/ENG-CODE/Contracts/...)
```

### SharePoint → Git

SharePoint README files can include links to relevant Git repo sections:

```
Analysis and decisions: https://github.com/org/ENG-CODE-requirements
Planning and updates: https://github.com/org/ENG-CODE-project
```

---

## PI Artifacts (SAFe)

Program Increment artifacts follow SAFe terminology and are stored in `ENG-{CODE}-project/pi/PI-{N}/`:

| Artifact | SAFe Concept | Content |
|----------|--------------|---------|
| `pi-objectives.md` | PI Objectives | Committed business and technical objectives; SMART format |
| `pi-backlog.md` | Program Backlog (PI slice) | Features, enablers, stories planned |
| `program-board.md` | Program Board | Delivery timeline, dependencies, milestones |
| `pi-risks.md` | ROAM Board | Risks: Resolved, Owned, Accepted, Mitigated |
| `confidence-vote.md` | Confidence Vote | Squad-by-squad confidence (1-5) |
| `iterations/` | Iteration Plans | Per-sprint stories, capacity, goals |
| `pi-retrospective.md` | Inspect & Adapt | What worked, what didn't, improvements |

See [PI Artifacts Reference](../reference/pi-artifacts.md) for detailed definitions of each artifact.

---

## Compliance Verification

Governance compliance is verified at lifecycle gates:

| Gate | Verification |
|------|--------------|
| Exploration → Initiate | Required Exploration artifacts exist; qualification documented |
| Initiate | Charter exists; operating model documented; roles assigned |
| Discover → Build | Gap analysis complete; architecture decisions recorded |
| Build → Transfer | Variability documentation complete; inner source contributions documented |
| Complete | Retrospective captured; case study drafted; repos marked for archival |

See [Gates and Checkpoints](../06-governance-enforcement/gates-checkpoints.md) for the complete gate framework.
