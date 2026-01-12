
AOS is a Olympus Hub Workbench
* Workbench as AOS
    - Operation as a collaboration session for the HAT

* Seer Agent Engine as an Automation System for ‘Seer Case’ Automation; [Requires contract between Hub Request to Automation System integration - Signals/Updates]
* Seer Agent Engine as an Employed Agent provider for ‘Rhea Workflow’ Automation; 
* Seer uses Cipher as the Workforce, Customer IAM and all Employed Agents exist in one of the domains and sandboxes of the tenant
* Cipher shall support enrolment of Raw, Trained, and Employed Agents and should also serve as a Agent Registry
* Hub Task Allocation refers to Groups and Agents (Auth Profiles) from the Cipher Sandboxes associated with workbench

===========
Required subsystems in Entrprise Agent Platform

Olympus Seer:
- Agent Definition & Lifecycle Service :: Seer owned and defined; includes policy/guardrail DEFINITIONS in Training Specs, authority GRANTS in Employment Specs, state management (active/suspended/retired), kill switch COMMANDS, approval workflow definitions
- Agent Identity & Authority Framework :: Seer defined but relies on Cipher 
- Context Assembly Engine :: SDKs provided for use in building raw agents
- Runtime & Deployment Abstraction :: For Raw Agents, Trained Agents, and Employed Agents; includes policy/guardrail ENFORCEMENT, authority CHECKS, override/kill switch EXECUTION, graceful degradation paths
- Agent Observability Service :: Runtime metrics, traces, health; relies on Olympus Estate & Watch for infrastructure observability
- Agent Test Runner :: Development-time testing, behavior/health/safety validations, CI/CD quality gates; entirely owned by Seer
- Model Abstraction Layer :: Owned by Seer

Note: Governance, Policy & Override functions are distributed between:
  - Lifecycle Service (control plane): definitions, commands, state changes
  - Runtime Service (data plane): enforcement, execution, real-time checks 


Olympus Hub:
- Memory System (Episodic, Semantic, Preference, Procedural) :: memory storage and access layer is defined by Seer; Memory management SDKs are provided for use in raw agents; raw agents can have their own frameworks and libraries for memory management. However, all agents *should* use storage from seer memory storage services. 
- Knowledge Integration Layer (RAG) :: Seer provides 'knowledge bank'; Provides ingress pipelines, content organization semantics, content retrieval semantics, that support the multi-tenancy, multi-layer, multi-scope aspects of the knowledge in enterprise memory 
- Tool & Action Framework :: Tool Registry of Hub
- Audit, Explanation & Evidence Fabric :: Olympus Hub CAF
- Secrets & Credential Management (integration with Olympus Hub Workbench & Environment)
- Cognitive Audit Fabric integration :: through Hub Workbench infra
- Enterprise Memory System Integration :: thorugh Hub Workbench infra


- Seer as an Enterprise Decision Layer with ability to publish and host Decision Services (ML Models); This kserve + the model garden/gateway for LLMs and externals models

-- 

CAF, Hub Agent Memory System, Hub Enterprise Memory System are all subsystems of Hub
