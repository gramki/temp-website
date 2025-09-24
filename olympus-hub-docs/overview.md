# Olympus Hub - Everything is Ops

Olympus Hub is a operations management platform designed for large and medium enterprises to model, manage, and optimize business operations across any business domain. The platform provides a unified framework where enterprises can define domain-specific workbenches, model business entities, and manage operations through AI-powered agents, regardless of the underlying enterprise systems.

## What is Operations? 
An operation is a task to be performed by the Operations Team or the relevant information systems or a combination of both. It could range from simple request to a very complex workflow involving multiple steps and turns between people and systems.
The Operations could refer to operations as in the ITSM realm where people are operating and managing an IT System or it could refer to handling operations of a business domain like HR Operations, Finance Operations, Payment Operations, etc, using systems. An "Operations Domain" determines what the operations are about.   

## Why is Everything Ops?
If we can view an Operation domain as a domain of collaboration between people and systems either to operate the systems or to operate a business function through this collaboration, then a vast majority of business activities can be seen as "Operations". The team of people can also be seen as a team of Human Agents and AI Agents.


Refer to the following model of a system of Human and AI collaboration

![Human-AI Collaboration Model](human-ai-collab.png)

Each Workbench in Olympus Hub should be seen as such a 'System' of Agents and Machines in an Environmemt. The Machine in the model above map to one or more information systems relevant for the specific business domain.

![Foundation Model for Hub](ontology_combined_reference.md)

Requires Systems Thinking. Modeling of effective and optimal collaboration betweens Systems and People. 


# Operations Domain – Workbench
Business Entities
Operations
Scenarios

Consoles
Utilities - Files, Reports, Documents
Operations Team
Operations Executives
Tasks and Task Queues
Checklists & Schleps
Signals
SOPs
Automations
Command Registry
Automation Runtimes
Environment

# Signals
Information from the environment or from the systems managing the entities representing some change or event of relevance for the operations team. These are organized in the following types:

* Events: Events of change published by message oriented systems
* Exceptions: Errors or failures in the applications that deserve attention of Operations team.
* Observations: Information of entities or the system that doesn't yet represent a problem in the system or entities but an operations team may be interested in knowing about.

* Requests: A requests from various users of the applications to draw attention of the operations team.

**  Service Requests: Specialized forms of requests that can be initiated by users of the sytems either in a self-served manner or in an assisted-manner through a contact center, IVR, or such other channel. Service request forms are hosted by hub and can be embedded in various user-interaction channels.

**  Business Requests: Specialized forms for generating requests that can be initaited by the operations teams or internal users of the enterprise in a self-serve manner. Business request froms are hosted by hub and can be embedded in various apps and user-interaction channels meant for the teams and executives internal to the enterprise.

** System Requests: These specialized requests form (REST+JSON interface) that can be integrated into applications of the enterprise that can be invoked directly by the applications. That is, there is no human to initiate these requests. These are auto-initiated by various applications and systems of the enterprise.


* Files: represent a batch of events or requests

Hub natively provides mechanisms to deliver signals to any Workbench. Each such signal could potentially initiate an operation to be performed by the operations team.

## Triggers
* A mechanism to translate a Siganl to invoke an Automation in a Scenario. 
* These are the filters and binders. That is, they filter out unnecesary signals and bind the relevant subset of signals to invoke automation or simply create a task for operations team to work on. 

All signals of type Requests serve as implicit triggers
Singals like Events, Exceptions, and Observations are integrated to Scenarios and Automation using System Requests as Triggers.



# Workbench Studio


# Task Managemewnt Platform
* Task Creation and Status synchronization Automation
* 


# Agent Application - Definition
Capable Agent Application
Skilful Agent Application
Enrolled Agent – Environment, Scope, Role
Creating a Skilful Agent Application from Workbench
Creating an Enrolled Agent from Workbench

# Agent Platform Capabilities

LLM and SLM Gateways
Channel-neutral Sessions
Channel-specific Orchestration Agents (Coordinators; May be these are not agents, they are just applications; The coordination here is technical and mostly routing)
Memory Management
MCP Gateway
MCP Knowledge/Resource Management Systems
Skill Repository (Prompts)
Tool Repository


# IAM
* Human Agent IAM
* AI Agent IAM
* SSO for Human Agents