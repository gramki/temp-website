# Hub Operators Subsystem:

Hub supports and advocate use of GitOps practices for provisioning and manging all the resources, configurations, and meta data. Various personas in publisher realm and the Admin, Architect, Developer, and Supervisor personas in the Tenant realm can accomplish many of their tasks using various form of CRDs in a declarative fashion. To translate the intent expect in these CRDs to desired state in the Hub Deployment or Hub Subscription, Hub ships with various operators. This module details the collection of these operators.  


Operators are grouped by the persona whose operations they intend to operator.

Publisher Domain:
- SRE Operator
-- Hub Cluster Deployment Specifications
-- Resource Specifications for resources required for Hub System Scoped Resources

- Win Operator
-- Tenant Subscription Specification

Tenant Domain:
    - Admin Opertors:
    -- Various Resource Operators (Specifications for Data Stores, Knowledge Stores, Memory Stores, etc.,)
    -- workbench-admin-operator:
        -- Environment Specification
        -- Machine Definition Specification
        -- Machine (Concrete) Instance Specification
        -- Tool Definition Specification
        -- Tool (Concrete) Instance Specification    

    - Process Architect Operator:
    -- workbench-architect-operator
        -- Workbench Normative Specification
        -- Scenario Normative Specification

    - Developer Operators:
    -- workbench-developer-operator
        -- Workbench Deployment Specification
    -- scenario-developer-operator
        -- Scenario Automation Specification
        -- Scenario Deployment Specification
    -- Hub Application Specification
    -- workbench-as-a-machine-operator
    -- scenario-as-a-tool-operator 
    -- scenario-as-an-agent-operator
    -- workbench-ms-teams-operator 
    

    - Supervisor Operators:
    -- workbench-supervisor-operator
        -- task-queue-specification
        -- workbench-supervision-specification

=====

Phase 2:
    - Developer Operators:
    -- workbench-as-a-machine-operator
    -- scenario-as-a-tool-operator 
    -- scenario-as-an-agent-operator
    -- workbench-ms-teams-operator 
    -- workbench-apm-operator


    - Workbench Operator
    - Registries (various) Operator
    - Task Queues Operator
    - Hub Application Operator
    - Hub Storage Operator
    - Hub Application Monitoring Operator
    - Hub Scenario Monitoring Operator
