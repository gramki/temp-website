# 1.10 Persona Twins: Personal AI Assistants

Seer extends its agent capabilities to personal productivity through **Persona Twins**—AI agents that collaborators create to handle tasks, notifications, and scheduled activities on their behalf. Unlike Business Scenarios that handle organizational workflows, Persona Twin Scenarios are personal productivity agents that respond to personal triggers and operate within the delegator's authority boundaries.

Persona Twins represent Seer's commitment to democratizing AI agent creation, enabling any collaborator (not just developers) to create personal AI assistants for delegation. This design philosophy recognizes that personal productivity is as important as organizational workflows and that agents can serve both purposes within the same governance framework.

## Design Philosophy

Persona Twins embody several key design principles:

| Principle | Description |
|-----------|-------------|
| **Personal Delegation** | Collaborators create AI agents to delegate their responsibilities |
| **Authority Inheritance** | Twins inherit authority from delegator (same as delegator) |
| **Personal Triggers** | Tasks assigned to delegator, platform notifications, schedules |
| **Privacy** | Private visibility option for personal workflows |
| **Blueprint-Based Creation** | Persona Twin Blueprints enable non-developer creation |

These principles ensure that Persona Twins are accessible, governed, and effective for personal productivity.

## Personal Delegation

Persona Twins enable collaborators to delegate routine work to AI assistants:
*   **Task Delegation**: Twins handle tasks assigned to the delegator
*   **Notification Management**: Twins filter and prioritize notifications
*   **Scheduled Activities**: Twins handle recurring work on behalf of the delegator

Personal delegation extends Seer's agent capabilities to personal productivity, enabling collaborators to focus on high-value work while delegating routine tasks to AI assistants.

## Authority Inheritance

Persona Twins inherit authority from their delegator:
*   **Same Authority**: Twins operate with the same authority as the delegator
*   **Delegator as Accountable Human**: The delegator is both the delegator and the accountable human
*   **No Authority Expansion**: Twins cannot exceed delegator authority

Authority inheritance ensures that Persona Twins operate within appropriate boundaries while maintaining full accountability.

## Blueprint-Based Creation

Persona Twin Blueprints enable non-developer creation:
*   **Signal Suggestions**: Blueprints provide signal suggestions for common triggers
*   **OPA Filter Templates**: Blueprints provide OPA filter templates for event matching
*   **Non-Developer Friendly**: Blueprints enable collaborators to create twins without developer skills

Blueprint-based creation democratizes AI agent creation, enabling any collaborator to create personal AI assistants.

## Relationship to Business Agents

Persona Twins differ from Business Scenarios in several ways:

| Aspect | Business Scenarios | Persona Twins |
|--------|-------------------|---------------|
| **Purpose** | Organizational workflows | Personal productivity |
| **Triggers** | Business events, requests | Personal tasks, notifications, schedules |
| **Visibility** | Workbench-wide | Private or workbench-wide |
| **Creation** | Developer-driven | Collaborator-driven (blueprint-based) |
| **Lifecycle** | Standard (Raw → Trained → Employed) | Standard with special recognition |

Despite these differences, Persona Twins follow the same three-layer agent lifecycle (Raw → Trained → Employed) with special recognition, isolation, and trigger mechanisms.

## Practical Implications

Persona Twins provide:
*   **Democratized AI Creation**: Any collaborator can create personal AI assistants
*   **Personal Productivity**: Twins handle routine tasks, freeing collaborators for high-value work
*   **Governed Delegation**: Twins operate within authority boundaries with full accountability
*   **Privacy Options**: Private visibility enables personal workflows without exposure

Persona Twins extend Seer's agent capabilities to personal productivity while maintaining governance and audit requirements.

## Cross-References

*   **Section 21 (Persona Twins in Seer)**: Detailed coverage of Persona Twins, including lifecycle, use cases, and implementation
*   **Section 7 (Agent Lifecycle)**: Persona Twins follow the standard agent lifecycle with special recognition
*   **Section 8 (Identity & Authority)**: Persona Twins inherit authority from their delegators

---

**References:**

*   `seer-design/implementation-concepts/persona-twins.md` — Persona Twins concept
*   `seer-design/implementation-concepts/persona-twin-blueprint.md` — Persona Twin Blueprint design
