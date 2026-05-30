# {Module display name} — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **{module display name}** components of the Foundry Platform.

## Implementation overview

{2–3 paragraphs: subsystems in this folder, runtime boundaries, and how the module interacts with Management, Orchestrator, Work Order Runtime, or other platform modules.}

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [{Concept}](../../ace/concepts.md) | {Brief mapping} |
| [{Governance or repository topic}](../../ace/governance.md) | {If applicable} |

## UPIM alignment

| UPIM layer / entity | Role in this module |
|---------------------|---------------------|
| {Entity} | {Stored / mutated / exposed via API} |

Full schema: [Product Information Model](../../product-information-model/README.md).

## Specification index

| Document | Scope |
|----------|-------|
| [requirements.md](requirements.md) | Module-level functional and non-functional requirements |
| [{subsystem}/README.md]({subsystem}/README.md) | {Subsystem scope} |
| [{spec}.md]({spec}.md) | {API, schema, or behavior} |
| [design-discussions/](design-discussions/) | Exploratory notes *(non-normative until promoted)* |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [{Module}](../{module}/platform-developer-guide/) | {Contract or event flow} |
| [Propeller](../../propeller/README.md) | {Frameworks used, if any} |
| [Engagement Engineering](../../engagement-engineering/extension-to-ace.md) | {Variance in engagement context, if any} |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [{Module} user guide](../user-guide/) — operator and builder tasks
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
