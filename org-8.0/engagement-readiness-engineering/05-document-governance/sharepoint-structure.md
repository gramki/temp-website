# SharePoint Structure

[← Back to Document Governance](README.md) · [ERE Guide](../README.md)

Each Customer gets a SharePoint site with folders per Exploration and Engagement. SharePoint serves as the repository for all customer-facing and customer-provided documents.

---

## Folder Structure

```
{Customer Name}/
├── EXP-{CODE}/
│   ├── Customer-Provided/
│   ├── Proposals/
│   └── Contracts/
└── ENG-{CODE}/
    ├── Customer-Provided/
    │   ├── Requirements/
    │   ├── Data/
    │   └── Approvals/
    ├── Deliverables/
    │   ├── Status-Reports/
    │   ├── Presentations/
    │   └── Documentation/
    └── Contracts/
```

---

## Exploration Folders (EXP-{CODE})

| Folder | Content |
|--------|---------|
| `Customer-Provided/` | Documents provided by the customer during Exploration — RFPs, requirements docs, background materials |
| `Proposals/` | Proposals and SOWs shared with the customer |
| `Contracts/` | Commercial agreements and terms |

---

## Engagement Folders (ENG-{CODE})

### Customer-Provided/

Documents provided by the customer during the Engagement:

| Subfolder | Content |
|-----------|---------|
| `Requirements/` | Customer requirements documents, specifications, change requests |
| `Data/` | Customer data files, test data, reference materials |
| `Approvals/` | Signed approvals, UAT sign-offs, go-live authorizations |

### Deliverables/

Documents delivered to the customer:

| Subfolder | Content |
|-----------|---------|
| `Status-Reports/` | Weekly/monthly status reports |
| `Presentations/` | Steering committee decks, review presentations |
| `Documentation/` | Delivered documentation — user guides, architecture docs, runbooks |

### Contracts/

Commercial agreements:

- Master agreements
- SOWs and amendments
- Change order documentation

---

## Relationship to Git Repos

SharePoint and Git serve complementary purposes:

| Aspect | SharePoint | Git |
|--------|------------|-----|
| **Audience** | Customer + internal | Internal only |
| **Format** | Office (Word, Excel, PPT) | Markdown |
| **Version control** | Basic versioning | Full Git history |
| **Content type** | Customer-facing, customer-provided | Analysis, decisions, planning |
| **Collaboration** | Office co-authoring | PR-based review |

### Cross-Reference Pattern

Git documents reference SharePoint content via URLs:

```markdown
## Customer Requirements

- Original requirements: [Link](https://sharepoint.com/sites/CustomerName/ENG-CODE/Customer-Provided/Requirements/...)
- Signed SOW: [Link](https://sharepoint.com/sites/CustomerName/ENG-CODE/Contracts/...)
```

SharePoint folders can include README files with links back to relevant Git repo sections for teams navigating from SharePoint.

---

## Auto-Provisioning

SharePoint folders are automatically created by the Bootstrap Kit when:

1. **Exploration initiated** → `EXP-{CODE}` folder structure created
2. **Engagement initiated** → `ENG-{CODE}` folder structure created

See [Governance Rules](governance-rules.md) for provisioning details.
