# A2A Channel in Hub

## Hub Agents should be able to provide services to Non-Hub Agents A2A
- The external agent musth connect with a Access Token that the A2A Channel can recognize
- The External Agent could represent a business user or a collaborator
- Business User
-- The A2A Channel acts as an A2A Client Adapter Agent to the client. 
-- An A2A Client Adapter agent is defined and published in a workbench. There can multiple A2A Adapter Agents in a Workbench. 
-- A2A Client Adapter Agent uses a LLM with the tools it is configured with to participate in A2A protocol.
-- The Client Adapter agent maps the incoming messages from the client agent to the tools it has or gives a suitable error response
-- The Client Adapter Agent forwards any request updates meant for the user (identity in the access token) to the client as A2A task updates
-- Each Hub Request corresponds to a A2A Task Request 

## Hub Agents should be able to consume services from Non-Hub Agents using A2A
This means External A2A Agents as collaborators

Two Scopes:
a. Task Assignees -- Interaction through a A2A Task Adapter Channel
b. Request Assignees -- Interaction through a A2A Request Adapter Channel

The external agent must be registered in IAM and be available as an assignable agent.
The Task Adapter and Request Adapter channels are registered as observers. The IAM Profiles created by them are know to them and they act as recepients of all the notifications meant to those agents.
They forward the notifications to the external Agents using A2A semantics. 
Any updates received from them translated to request updates and posted by the channel using the IAM creds corresponding to the external agent.

