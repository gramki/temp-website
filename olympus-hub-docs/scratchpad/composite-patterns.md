
Set-1:
* Invoking Scenarios as Tools from Hub Applications
* Using a Workbench as a machine from other Workbenches


# Scenario as an Agent
* Using Scenarios as Agents in Other Scenarios

## Why would anyone want to treat a Scenario as an Agent
* Fundamentally this make Scenarios invocable against Tasks in other Scenarios.
* Pre-existing Scenarios where certain activities are modeled as Taks for Agents and you have an automation of such a task. You don't yet want to change or can't change the pre-existing Scenario automation. Then you can deliver such a task automation as an Agent and enroll that agent in the pre-existing Scenario's task queue.
* Flexibility to employ humans as well as applications to complete a task. If modeled as an agent, the scenario agent can participate along side other humans in task queues. This allows for load sharing, experimentation, etc.,

<Show Diagram of interactions between (WB-1, Pre-Existing-Scenario-1, Task-Queue-1) to (WB-2, New-Scenario-2[as-an-Agent])>


## Interpretatiton of a Scenario
A Scenario is initiated based on a Signal. However, while addressing a specific occurance of a Scenario there are multiple signals captured as updates to the context of that instance and encapsulated under 'Request'. 

## Architecture of Scenario Publishable as an Agent
1. Identity in IAM
2. HTTP Signals and corresponding Triggers
3. Webhook Notification Subscriptions in the target Workbench (Agent Deployment/Employment Time)
4. Uses the Agent REST Interface to send Signals (updates) to the target Workbench (Endpoints discovered at the time of employment)

## Publishing Scneario as an Agent
The Scenario Developer should go through this following steps while publishing the Scenario as an Agent:
- Registering as an Agent in IAM; Receive Identity and Profile
- Receiving Bot Token and register in scenario environment (security aspects will be detailed later)
- Registering for HTTP Signals for this Scenario
- Registering for Webhook Notifications for the received Agent ID above using the HTTP Signal receiving endpoint received in previous step.
- Mapping the incoming Webhook Signal to this scenario's Hub Application that will automate the agent behavior using a Trigger
- This Hub Application is expected to trigger the Task Update REST API available to the agent using its token.

====

-----
Create a Hub Application
Need: Step-by-step guide for building applications across different runtimes (Seer, ChronoShift, Rhea, Perseus, Atlantis)
----
Create a Task Solver Component for Supported Channels
Need: Guide for building Task Solver UIs for Agent Desk, MS Teams, MCP channels using Angelos framework