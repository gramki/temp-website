
# Persona Twins

Any Collaborator in a Workbench can create any number of Agent Twins for them to delegate their responsibilities to them. They start this journey from a Persona Twin Blueprint. 
Each Agent Twin of a collaborator will have a Scenario in the workbench. The Scenario is labelled as a persona-twin.

The Blueprint provides the common signals a collaborator may be interested in and the collaborator can configure triggers for specific signals filtered using the OPA based filters.

The collaborator can specify skill and behavior prompts in training spec and train the twin in a desired workbench. After he is satisfied, he can promote the agent to different workbenches also as he pleases. Persona Twins can be promoted with authorization from admin by any collaborattor. Need not be a developer.


The agent-lifecycle-manger, trained-agent-lifecycle-manager subsytem recognize persona twins and support their lifecycle. The directories are able to distinguish these agents.

- Persona Twin Scenarios: 
    - Can be triggered by tasks assigned to the delegator
    - Can be triggered by platform notifications scoped to the workbench meant for the delegator
    - Can be triggered by personally configured time schedules
- Persona Twin Scenarios are isolated from Business Scenarios in the Workbench
- The visibility of Persona Twin Scenarios can be set to private - only admin and scenario owner/creator can see them
- Authority Delegation and Accountability model for Twins
* Delegator is the collaborator who creates the NormativeSpec
* Manage is same as Delegator
* At the type of deployment the delegator can give roles, scopes, and group membership of delegation. Can use various policies that can be configured on Trained and Employed agents to fine-tune the scope of delegation and actions.

====
# Persona Twins Implementation - Clarifying Questions

## 1. Persona Twin Blueprint

- Is this a new blueprint type, or a variant of existing blueprints?
> Just a Trained Agent Blueprint

- What does it contain beyond common signals and OPA filters?
> refer to trained agent blueprints
> common singals and opa filter suggestions are supported but additional inclusion to a trained agent blueprint

- Where is it stored/managed (Marketplace, Workbench Studio, etc.)?
> Available in all workbenches, as part of default Hub Platform subscription

## 2. Scenario Labeling

- How should "persona-twin" be represented: a tag, a `scenario_type` field, or a separate category?
> it can just be a metadata label in all relevant resources assocaited
- Should it be a first-class type in the scenario schema?
> no

## 3. Signal Filtering

- What signals should the blueprint include by default?
> invent examples
- Are the OPA filters similar to the COG Sentinel `on_request_update` pattern, or different?
> same
- Should filters be defined in the blueprint or per twin?
> per twin

## 4. Trigger Types

- Tasks assigned to delegator: should this create a task in the delegator's queue that triggers the twin's scenario?
> Yes. 
- Platform notifications: should this use the existing Platform Notifications subsystem, or a new mechanism?
> existing
- Time schedules: are these cron-like schedules, or something else?
> cron-like schedule; check hub native utilties documentation

## 5. Scenario Isolation

- How should Persona Twin Scenarios be isolated from Business Scenarios in the UI and APIs?
> Categorized separately. Visibility config honored.
> API -> support filters
- Should they appear in separate views/sections?
> sections
- Should they be excluded from standard scenario lists by default?
> no; filter support is sufficient

## 6. Visibility and Access Control

- "Private" visibility: only admin and scenario owner/creator can see them — is this similar to marketplace visibility controls, or a new mechanism?
> similar
- Should this be a scenario-level setting, or workbench-level?
> scenario level

## 7. Authority Delegation

- At deployment, the delegator can give roles, scopes, and group membership — is this part of the Employment Spec?
> yes
- Which policies are available for fine-tuning delegation scope?
> read iam extensions documetnation

- Should this use the existing Employment Spec Manager, or a new mechanism?
> yes

## 8. Promotion

- What does "promote the agent to different workbenches" mean — creating new Employed Agents in other workbenches using the same Training Spec?
> yes, check hub documentation for promotion of scenarios
> also check the mechanisms to publish packages to marketplace and using them in various workbenches acorss subscriptions
> both mechanisms are supported.

- Does promotion require admin authorization for each target workbench, or a one-time approval?
> yes, each

- Can a twin exist in multiple workbenches simultaneously?
> Yes. In each WB the identity is different, even though the delegation may be identitical

## 9. Lifecycle Recognition

- How should directories distinguish Persona Twins from other agents — a tag/metadata field, or a separate agent type?
> tag/metadata field

- Should this be tracked in Training Spec metadata, Employment Spec, or both?
> both

## 10. Training

- When training a twin in a workbench, is this creating a Trained Agent from a Raw Agent, or customizing an existing Trained Agent?
> creating trained from raw agent or creating one from blueprint

- Can collaborators without Developer persona create and train twins?
> yes
