
Set-1:
* Invoking Scenarios as Tools from Hub Applications
* Using a Workbench as a machine from other Workbenches


* Using Scenarios as Agents in Other Scenarios

The Scenario Developer should go through this following steps while publishing the Scenario/Workbench:
- Registering as an Agent in IAM; Receive Identity and Profile
- Receiving Bot Token and register in scenario environment (security aspects will be detailed later)
- Registering for HTTP Signals for this Scenario
- Registering for Webhook Notifications for the received Agent ID above using the HTTP Signal receiving endpoint received in previous step.
- Mapping the incoming Webhook Signal to this scenario's Hub Application that will automate the agent behavior using a Trigger
- This Hub Application is expected to trigger the Task Update REST API available to the agent using its token.


-----
Create a Hub Application
Need: Step-by-step guide for building applications across different runtimes (Seer, ChronoShift, Rhea, Perseus, Atlantis)
----
Create a Task Solver Component for Supported Channels
Need: Guide for building Task Solver UIs for Agent Desk, MS Teams, MCP channels using Angelos framework