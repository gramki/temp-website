# Scenario as an Agent

> **Status:** 🟡 Draft — Composite pattern documentation
> **Audience:** Process Architects, Developers

## Overview

The **Scenario as an Agent** pattern allows a Scenario to be published and enrolled as an Agent in another Scenario's Task Queue. This enables automated task completion within pre-existing Scenarios without modifying their original automation.

---

## The Premise

In Hub, **Agents** complete **Tasks** that are created by **Hub Applications** within **Scenarios**. Traditionally, agents are:

- **Human agents** working through Agent Desk, MS Teams, or MCP interfaces
- **AI agents** working through MCP interfaces

But what if you have **any form of automation** — rule-based, workflow, image processing, AI, or otherwise — that could perform the work an agent does? Rather than embedding that automation within the original Scenario, you can **publish it as an Agent** and enroll it in the original Scenario's task queue.

> **Important:** The "Agent" role here refers to the **capability to complete tasks**, not the underlying technology. A Scenario-as-Agent can be powered by simple rule engines, image processors, workflow automations, or AI models — any Hub Application that can receive a task and return a result.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  TRADITIONAL: Tasks Completed by Human/AI Agents             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   Workbench: Dispute Operations                                              │
│   Scenario: Dispute Resolution                                               │
│                                                                              │
│   ┌─────────────────┐     Task: "Review Evidence"    ┌─────────────────┐    │
│   │ Hub Application │ ──────────────────────────────▶│   Task Queue    │    │
│   │                 │                                │                 │    │
│   └─────────────────┘                                └───────┬─────────┘    │
│                                                              │              │
│                                          ┌───────────────────┼───────┐      │
│                                          ▼                   ▼       ▼      │
│                                     ┌────────┐         ┌────────┐ ┌────────┐│
│                                     │ Human  │         │ Human  │ │   AI   ││
│                                     │ Agent  │         │ Agent  │ │ Agent  ││
│                                     └────────┘         └────────┘ └────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

                                    ▼ ▼ ▼

┌─────────────────────────────────────────────────────────────────────────────┐
│                  NEW: Scenario Acting as an Agent                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   Workbench: Dispute Operations                                              │
│   Scenario: Dispute Resolution                                               │
│                                                                              │
│   ┌─────────────────┐     Task: "Review Evidence"    ┌─────────────────┐    │
│   │ Hub Application │ ──────────────────────────────▶│   Task Queue    │    │
│   │                 │                                │                 │    │
│   └─────────────────┘                                └───────┬─────────┘    │
│                                                              │              │
│                                ┌─────────────────────────────┼───────┐      │
│                                ▼                             ▼       ▼      │
│                           ┌────────┐                   ┌────────┐ ┌────────┐│
│                           │SCENARIO│                   │ Human  │ │ Human  ││
│                           │ AGENT  │                   │ Agent  │ │ Agent  ││
│                           └───┬────┘                   └────────┘ └────────┘│
│                               │                                             │
│                               │ (Is actually another Scenario)              │
│                               ▼                                             │
│   ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐  │
│   │                                                                       │  │
│   │  Workbench: Evidence Automation                                       │  │
│   │  Scenario: Evidence Review Automation                                │  │
│   │                                                                       │  │
│   │   ┌─────────────────┐                          ┌─────────────────┐   │  │
│   │   │ HTTP Signal     │────▶ Trigger ────▶       │ Hub Application │   │  │
│   │   │ (Task Assigned) │                          │ (Reviews Docs)  │   │  │
│   │   └─────────────────┘                          └─────────────────┘   │  │
│   │                                                                       │  │
│   └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Automation Types

A Scenario-as-Agent can be powered by **any Hub Application type**. The pattern is technology-agnostic:

### Non-AI Automation Examples

| Automation Type | Runtime | Example Use Case |
|-----------------|---------|------------------|
| **Rule-Based** | Atlantis (Drools/DMN) | Decision rules for loan eligibility checks |
| **Image Processing** | Atlantis (Custom Container) | Document classification, signature verification |
| **Workflow** | Rhea (BPMN) | Multi-step approval processes |
| **Data Validation** | Atlantis (Procedure) | Form validation against business rules |
| **File Processing** | Perseus (Batch) | Parsing and validating uploaded documents |
| **Integration** | ChronoShift (Durable Workflow) | Calling external APIs and aggregating results |

### AI-Powered Automation Examples

| Automation Type | Runtime | Example Use Case |
|-----------------|---------|------------------|
| **LLM Analysis** | Seer | Natural language document analysis |
| **ML Classification** | Atlantis (KServe) | Fraud probability scoring |
| **OCR + Extraction** | Atlantis (Custom) | Extracting data from scanned documents |
| **Agentic Workflow** | Seer | Complex multi-step reasoning with tools |

### Choosing the Right Automation

| When to Use | Automation Approach |
|-------------|---------------------|
| **Deterministic logic, clear rules** | Rule-based (Drools/DMN) |
| **Structured document processing** | Image processing, OCR |
| **Multi-step with human checkpoints** | Workflow (Rhea) |
| **Long-running with retries** | Durable workflow (ChronoShift) |
| **Unstructured content analysis** | LLM/AI (Seer) |
| **High-volume file processing** | Batch processing (Perseus) |

---

## Why Use This Pattern?

### 1. Automate Tasks in Pre-Existing Scenarios

You have a mature Scenario with established workflows. Modifying it is risky or requires extensive testing. Instead, you create a new Scenario that automates a specific task type and enroll it as an agent.

**Example:** A "Dispute Resolution" Scenario has been in production for years. You want to automate the "Evidence Review" task but don't want to modify the proven workflow. You create an "Evidence Review Automation" Scenario and enroll it as an agent.

### 2. Flexibility: Humans + Automation Side-by-Side

When a Scenario-as-Agent is enrolled alongside human agents in a task queue, you gain:

| Capability | Description |
|------------|-------------|
| **Load Balancing** | Scenario agents can handle overflow when humans are busy |
| **24/7 Coverage** | Scenario agents work nights and weekends |
| **A/B Testing** | Route percentage of tasks to automation for comparison |
| **Graceful Rollout** | Gradually increase automation's share of tasks |
| **Fallback** | If automation fails, task can be reassigned to humans |

### 3. Separation of Ownership

Different teams can own different parts of the process:

- **Team A** owns the main "Dispute Resolution" Scenario
- **Team B** owns the "Evidence Review Automation" Scenario-as-Agent
- Each team can iterate independently

### 4. Reusable Automation

The same Scenario-as-Agent can be enrolled in multiple task queues across different Scenarios:

```
Evidence Review Automation (Scenario-as-Agent)
                │
    ┌───────────┼───────────────────────┐
    ▼           ▼                       ▼
Dispute      Fraud                  Compliance
Resolution   Investigation          Review
(Task Queue) (Task Queue)           (Task Queue)
```

---

## How It Works

### Understanding the Interaction Model

When a Scenario is published as an Agent, it participates in the standard agent lifecycle:

1. **Task Assignment** — Task Management assigns a task to the Scenario-Agent
2. **Notification** — Scenario-Agent receives task notification via webhook
3. **Signal Intake** — Notification triggers a new Request in the automating Scenario
4. **Processing** — Hub Application in automating Scenario performs the work
5. **Task Update** — Hub Application calls Agent REST API to update/complete the task
6. **Request Update** — Original Scenario receives the task completion

### Detailed Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SCENARIO-AS-AGENT INTERACTION FLOW                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CONSUMING CONTEXT: Workbench-A / Scenario-Alpha                             │
│  ════════════════════════════════════════════════                            │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     Hub Application (Alpha)                          │    │
│  │                                                                      │    │
│  │   1. Creates Task: "Review document evidence"                       │    │
│  │      → Task Type: EVIDENCE_REVIEW                                   │    │
│  │      → Task Queue: evidence-review-queue                            │    │
│  │      → Task Payload: { document_ids, request_context }              │    │
│  │                                                                      │    │
│  └─────────────────────────────┬────────────────────────────────────────┘    │
│                                │                                             │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     Task Management                                  │    │
│  │                                                                      │    │
│  │   2. Allocation Engine selects assignee from task queue            │    │
│  │      → Queue has: [Human-Agent-1, Human-Agent-2, Scenario-Agent-X]  │    │
│  │      → Selected: Scenario-Agent-X (based on algorithm)             │    │
│  │                                                                      │    │
│  │   3. Sends TASK_ASSIGNED notification via Agent's webhook          │    │
│  │                                                                      │    │
│  └─────────────────────────────┬────────────────────────────────────────┘    │
│                                │                                             │
│ ═══════════════════════════════│═════════════════════════════════════════════│
│                                │                                             │
│  PROVIDING CONTEXT: Workbench-B / Scenario-Beta (as Agent)                   │
│  ══════════════════════════════════════════════════════════                  │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     HTTP Signal Endpoint                             │    │
│  │                     (Heracles Gateway)                               │    │
│  │                                                                      │    │
│  │   4. Receives webhook POST with TASK_ASSIGNED payload               │    │
│  │      → Converts to Normalized Signal DTO                            │    │
│  │      → Forwards to Signal Exchange                                  │    │
│  │                                                                      │    │
│  └─────────────────────────────┬────────────────────────────────────────┘    │
│                                │                                             │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     Signal Exchange                                  │    │
│  │                                                                      │    │
│  │   5. Matches Signal against Trigger                                 │    │
│  │      → Signal Type: agent.task.assigned                             │    │
│  │      → Trigger: trg-task-assigned-evidence-review                   │    │
│  │                                                                      │    │
│  │   6. Creates Request for Scenario-Beta                              │    │
│  │      → Request payload includes task context                        │    │
│  │                                                                      │    │
│  └─────────────────────────────┬────────────────────────────────────────┘    │
│                                │                                             │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     Hub Application (Beta)                           │    │
│  │                     "Evidence Review Automation"                     │    │
│  │                                                                      │    │
│  │   7. Processes the task:                                            │    │
│  │      a. Retrieves documents from context                            │    │
│  │      b. Analyzes documents (AI, rules, etc.)                        │    │
│  │      c. Makes determination                                         │    │
│  │      d. Prepares response                                           │    │
│  │                                                                      │    │
│  │   8. Calls Agent REST API to update task:                           │    │
│  │      POST /agent/tasks/{task_id}/complete                           │    │
│  │      → Uses Bot Token for authentication                            │    │
│  │      → Includes determination and evidence                          │    │
│  │                                                                      │    │
│  └─────────────────────────────┬────────────────────────────────────────┘    │
│                                │                                             │
│ ═══════════════════════════════│═════════════════════════════════════════════│
│                                │                                             │
│  BACK TO CONSUMING CONTEXT                                                   │
│  ═════════════════════════════                                               │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     Task Management                                  │    │
│  │                                                                      │    │
│  │   9. Receives task completion                                       │    │
│  │      → Updates task state to COMPLETED                              │    │
│  │      → Records outcome and evidence                                 │    │
│  │                                                                      │    │
│  └─────────────────────────────┬────────────────────────────────────────┘    │
│                                │                                             │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     Hub Application (Alpha)                          │    │
│  │                                                                      │    │
│  │  10. Receives REQUEST_UPDATE with task completion                   │    │
│  │      → Continues workflow with determination                        │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Architecture Components

A Scenario published as an Agent requires these architectural components:

### 1. IAM Identity

The Scenario-Agent needs an identity in Cipher IAM:

```yaml
agent_identity:
  type: "bot"
  id: "scenario-agent-evidence-review"
  display_name: "Evidence Review Automation"
  
  # Agent profile attributes
  profile:
    agent_type: "scenario"
    source_workbench: "evidence-automation"
    source_scenario: "evidence-review-automation"
    
  # Skills (for skill-based routing)
  skills:
    - document_analysis
    - evidence_review
    - fraud_detection
    
  # Bot token for API access
  credentials:
    type: "bot_token"
    token_ref: "vault://scenario-agents/evidence-review/token"
```

### 2. HTTP Signal Endpoint

A dedicated HTTP endpoint to receive task notifications:

```yaml
signal_endpoint:
  path: "/signals/agent/{agent_id}/notifications"
  method: "POST"
  
  authentication:
    type: "hmac_signature"
    secret_ref: "vault://scenario-agents/evidence-review/webhook-secret"
    
  payload_schema:
    type: "agent_notification"
    version: "1.0"
```

### 3. Webhook Notification Subscription

Registered in the target Workbench to receive task notifications:

```yaml
webhook_subscription:
  subscriber_id: "scenario-agent-evidence-review"
  subscriber_type: "agent"
  
  target_workbench: "dispute-operations"
  
  events:
    - "task.assigned"
    - "task.escalated"
    - "task.cancelled"
    - "request.cancelled"
    
  delivery:
    endpoint: "https://hub.example.com/signals/agent/scenario-agent-evidence-review/notifications"
    method: "POST"
    headers:
      X-Webhook-Source: "dispute-operations"
    authentication:
      type: "hmac_signature"
      secret_ref: "vault://scenario-agents/evidence-review/webhook-secret"
```

### 4. Trigger Configuration

Maps incoming task notifications to the automating Scenario:

```yaml
signal_definition:
  id: "sig-def-task-assigned"
  signal_type: "agent_notification"
  
  filter:
    payload:
      event_type: "task.assigned"
      task_type: "EVIDENCE_REVIEW"

trigger:
  id: "trg-task-assigned-evidence-review"
  signal_definition_id: "sig-def-task-assigned"
  scenario_id: "evidence-review-automation"
  action: "create_new"
  
  transformation:
    type: "low_code"
    mapping:
      request_type: "AgentTaskRequest"
      
      # Preserve source context
      source_context:
        workbench_id: "$.payload.source_workbench_id"
        scenario_id: "$.payload.source_scenario_id"
        request_id: "$.payload.source_request_id"
        task_id: "$.payload.task_id"
        
      payload_mapping:
        task_id: "$.payload.task_id"
        task_type: "$.payload.task_type"
        task_payload: "$.payload.task_payload"
        deadline: "$.payload.sla.deadline"
```

### 5. Hub Application with Agent Capabilities

The Hub Application that performs the work and reports back:

```yaml
hub_application:
  id: "evidence-review-automation-app"
  runtime: "seer"  # or rhea, chronoshift, etc.
  
  # Configuration for agent behavior
  agent_behavior:
    # Token for calling Agent REST API
    agent_token_ref: "vault://scenario-agents/evidence-review/token"
    
    # Target workbench for API calls
    target_api_base: "${source_context.workbench_id}"
    
    # Supported task operations
    operations:
      - "start_work"
      - "add_memo"
      - "add_thought"
      - "complete"
      - "abandon"
```

---

## Value Proposition

### For Operations Leaders

| Benefit | Description |
|---------|-------------|
| **Zero-Disruption Automation** | Automate tasks without modifying proven Scenarios |
| **Gradual Rollout** | Start with 10% automation, increase over time |
| **Easy Rollback** | Simply remove agent from queue to revert to humans |
| **Metrics Comparison** | Compare human vs automation performance |

### For Process Architects

| Benefit | Description |
|---------|-------------|
| **Modular Design** | Each automation is self-contained |
| **Clear Boundaries** | Well-defined interface (task in, result out) |
| **Independent Evolution** | Teams iterate on their components independently |
| **Reuse Across Scenarios** | Same agent serves multiple task queues |

### For Developers

| Benefit | Description |
|---------|-------------|
| **Standard Interfaces** | Use existing Agent REST APIs |
| **Familiar Patterns** | Build with standard Hub Application patterns |
| **Full Hub Capabilities** | Access tools, knowledge, memory within automating Scenario |
| **Observable** | Standard Hub observability for debugging |

---

## Step-by-Step Implementation Guide

### Prerequisites

Before implementing this pattern:

- ✅ Target Workbench and Scenario exist and are operational
- ✅ Task types that will be automated are identified
- ✅ Task queues where the Scenario-Agent will be enrolled are identified
- ✅ Required tools and knowledge for automation are available

### Phase 1: Create the Automating Scenario

#### Step 1.1: Create Workbench for Automation

```
Hub Console → Workbench Studio → Create Workbench
├── Name: "Evidence Automation"
├── ID: evidence-automation
├── Domain: task-automation
└── Description: "Automated agents for task completion"
```

#### Step 1.2: Define the Automating Scenario

```yaml
# Scenario Normative Specification
scenario:
  id: "evidence-review-automation"
  name: "Evidence Review Automation"
  description: "Automated review of evidence documents for dispute tasks"
  
  type: "AgentAutomation"
  
  goals:
    - id: "complete-evidence-review"
      description: "Analyze documents and provide determination"
      sla: "PT30M"  # 30 minutes
      
  roles:
    - id: "automation-operator"
      description: "Monitors automation performance"
```

#### Step 1.3: Build the Hub Application

Create the Hub Application that will process tasks. The implementation depends on your automation approach:

#### Option A: Rule-Based Automation (Atlantis/Drools)

```java
// Example: Drools-based Document Validation
// Runtime: Atlantis (DMN/Drools)

public class DocumentValidationHandler implements TaskHandler {
    
    private final DroolsEngine rulesEngine;
    private final AgentClient agentClient;
    
    @Override
    public TaskResult handle(TaskContext context) {
        // 1. Start work
        agentClient.startWork(context.getTaskId(), 
            "Beginning rule-based document validation");
        
        // 2. Load documents
        List<Document> documents = documentService.retrieve(
            context.getPayload().getDocumentIds());
        
        // 3. Apply validation rules to each document
        List<ValidationResult> results = new ArrayList<>();
        for (Document doc : documents) {
            // Execute Drools rules against document
            ValidationResult result = rulesEngine.execute(
                "document-validation-rules", 
                new DocumentFacts(doc)
            );
            results.add(result);
            
            agentClient.addMemo(context.getTaskId(),
                String.format("Validated %s: %s", 
                    doc.getName(), result.getStatus()));
        }
        
        // 4. Aggregate results using decision table
        Determination determination = rulesEngine.execute(
            "evidence-determination-dmn",
            new EvidenceFacts(results)
        );
        
        // 5. Complete task
        return agentClient.completeTask(context.getTaskId(), 
            Map.of(
                "determination", determination.getResult(),
                "validation_passed", determination.isValid(),
                "documents_validated", documents.size(),
                "issues_found", determination.getIssues()
            ));
    }
}
```

#### Option B: Image Processing Automation (Atlantis/Custom)

```python
# Example: Document Classification via Image Processing
# Runtime: Atlantis (Custom Container with OpenCV/Tesseract)

class DocumentClassificationHandler:
    """
    Classifies documents using image processing and OCR.
    No AI/ML models - uses template matching and rule-based classification.
    """
    
    def __init__(self, agent_client, ocr_engine, template_matcher):
        self.agent_client = agent_client
        self.ocr = ocr_engine  # Tesseract
        self.matcher = template_matcher  # OpenCV
    
    async def handle_task(self, context):
        task_id = context.source_context.task_id
        
        # 1. Start work
        await self.agent_client.start_work(task_id,
            "Beginning document classification")
        
        # 2. Process each document
        classifications = []
        for doc_id in context.payload.document_ids:
            # Download document image
            image = await self.download_document(doc_id)
            
            # Template matching for document type
            doc_type = self.matcher.match_template(image, [
                "bank_statement", "id_card", "utility_bill", "receipt"
            ])
            
            # OCR for text extraction
            extracted_text = self.ocr.extract_text(image)
            
            # Rule-based field extraction
            fields = self.extract_fields_by_rules(doc_type, extracted_text)
            
            classifications.append({
                "doc_id": doc_id,
                "type": doc_type,
                "confidence": self.matcher.last_confidence,
                "extracted_fields": fields
            })
            
            await self.agent_client.add_memo(task_id,
                f"Classified {doc_id} as {doc_type}")
        
        # 3. Validate completeness
        required_types = context.payload.required_document_types
        missing = set(required_types) - {c["type"] for c in classifications}
        
        # 4. Complete task
        return await self.agent_client.complete_task(task_id, {
            "classifications": classifications,
            "all_required_present": len(missing) == 0,
            "missing_types": list(missing),
            "documents_processed": len(classifications)
        })
```

#### Option C: AI-Powered Automation (Seer)

```python
# Example: LLM-based Evidence Analysis
# Runtime: Seer (Case Orchestration Agent)

class EvidenceAnalysisAgent:
    """
    Uses LLM to analyze unstructured evidence documents.
    Best for nuanced analysis requiring reasoning.
    """
    
    async def handle_task_assigned(self, request):
        task_context = request.payload.task_payload
        source_context = request.payload.source_context
        
        # 1. Start work
        await self.agent_client.start_work(
            task_id=source_context.task_id,
            memo="Beginning AI-assisted evidence analysis"
        )
        
        # 2. Retrieve documents
        documents = await self.retrieve_documents(task_context.document_ids)
        
        # 3. Analyze using LLM
        analysis_results = []
        for doc in documents:
            # Use Seer's reasoning capabilities
            result = await self.reason_about_document(
                document=doc,
                context=task_context.dispute_context,
                guidelines=await self.get_sop("evidence-analysis-guidelines")
            )
            analysis_results.append(result)
            
            await self.agent_client.add_thought(
                task_id=source_context.task_id,
                thought=f"Analysis of {doc.name}: {result.summary}"
            )
        
        # 4. Synthesize findings
        determination = await self.synthesize_evidence(
            analysis_results,
            decision_criteria=task_context.decision_criteria
        )
        
        # 5. Complete task
        await self.agent_client.complete_task(
            task_id=source_context.task_id,
            outcome={
                "determination": determination.result,
                "reasoning": determination.explanation,
                "confidence": determination.confidence,
                "documents_reviewed": len(documents)
            }
        )
        
        return RequestCompletion(status="COMPLETED")
```

#### Option D: Workflow Automation (Rhea/BPMN)

```yaml
# Example: Multi-Step Approval Workflow
# Runtime: Rhea (BPMN Workflow)

# BPMN Process Definition
process:
  id: evidence-verification-workflow
  name: "Evidence Verification Workflow"
  
  start_event:
    id: task_received
    type: message
    
  tasks:
    - id: start_work
      type: service_task
      implementation: agent-client.start-work
      
    - id: download_documents
      type: service_task
      implementation: document-service.download-batch
      
    - id: validate_format
      type: service_task
      implementation: validator.check-file-formats
      
    - id: format_valid_gateway
      type: exclusive_gateway
      
    - id: check_completeness
      type: service_task
      implementation: validator.check-required-documents
      
    - id: verify_signatures
      type: service_task
      implementation: signature-verifier.verify-batch
      
    - id: complete_task
      type: service_task
      implementation: agent-client.complete-task
      
  sequence_flows:
    - from: task_received
      to: start_work
    - from: start_work
      to: download_documents
    - from: download_documents
      to: validate_format
    - from: validate_format
      to: format_valid_gateway
    - from: format_valid_gateway
      to: check_completeness
      condition: "allValid == true"
    - from: format_valid_gateway
      to: complete_task
      condition: "allValid == false"
      # Complete with "invalid_format" outcome
    - from: check_completeness
      to: verify_signatures
    - from: verify_signatures
      to: complete_task
```

### Phase 2: Register as an Agent

#### Step 2.1: Create Agent Identity in IAM

```
Cipher IAM Console → Service Accounts → Create Bot
├── ID: scenario-agent-evidence-review
├── Display Name: "Evidence Review Automation"
├── Type: Bot / Service Account
├── Profile:
│   ├── agent_type: scenario
│   ├── source_workbench: evidence-automation
│   └── source_scenario: evidence-review-automation
└── Generate Token → Store in Vault
```

#### Step 2.2: Register HTTP Signal Endpoint

```
Workbench Studio → Evidence Automation → Signals → HTTP Endpoints
├── Path: /signals/agent/scenario-agent-evidence-review/notifications
├── Method: POST
├── Authentication: HMAC Signature
└── Webhook Secret: [Generate and store in Vault]
```

#### Step 2.3: Configure Trigger for Task Notifications

```yaml
# Signal Definition
signal_definition:
  id: "sig-def-task-notification"
  signal_type: "agent_notification"
  filter:
    payload:
      event_type:
        $in: ["task.assigned", "task.escalated"]

# Trigger
trigger:
  id: "trg-task-notification"
  signal_definition_id: "sig-def-task-notification"
  scenario_id: "evidence-review-automation"
  action: "create_new"
  
  transformation:
    type: "low_code"
    mapping:
      request_type: "AgentTaskRequest"
      
      source_context:
        workbench_id: "$.payload.source_workbench_id"
        request_id: "$.payload.source_request_id"
        task_id: "$.payload.task_id"
        
      payload_mapping:
        task_id: "$.payload.task_id"
        task_type: "$.payload.task_type"
        task_payload: "$.payload.task_payload"
```

### Phase 3: Deploy to Target Workbench

#### Step 3.1: Register Webhook Subscription

In the **target** Workbench (where tasks will be assigned):

```
Workbench Studio → Dispute Operations → Notifications → Webhooks → Create
├── Subscriber: scenario-agent-evidence-review
├── Events:
│   ├── task.assigned
│   ├── task.escalated
│   ├── task.cancelled
│   └── request.cancelled
├── Endpoint: https://hub.example.com/signals/agent/scenario-agent-evidence-review/notifications
├── Authentication: HMAC Signature
└── Secret: [Shared secret from Step 2.2]
```

#### Step 3.2: Enroll Agent in Task Queue

```
Workbench Studio → Dispute Operations → Task Queues → evidence-review-queue → Agents
├── Add Agent
│   ├── Agent ID: scenario-agent-evidence-review
│   ├── Type: Bot/Scenario
│   ├── Skills: [document_analysis, evidence_review]
│   └── Capacity: 10 concurrent tasks
└── Enrollment Settings
    ├── Escalation Level: 0 (primary)
    ├── Allocation Weight: 50%
    └── Enabled: true
```

### Phase 4: Test and Validate

#### Step 4.1: Test with Simulated Task

```
Workbench Studio → Dispute Operations → Testing → Simulate Task
├── Task Type: EVIDENCE_REVIEW
├── Task Queue: evidence-review-queue
├── Force Assignment: scenario-agent-evidence-review
├── Test Payload:
│   └── document_ids: ["doc-001", "doc-002"]
└── Execute Simulation
```

#### Step 4.2: Verify End-to-End Flow

Check that:
- ✅ Webhook received by automating Scenario
- ✅ Request created in automating Scenario
- ✅ Hub Application processed the task
- ✅ Task completed via Agent REST API
- ✅ Original Scenario received task completion

### Phase 5: Gradual Rollout

#### Step 5.1: Configure Allocation Weight

Start with low allocation to Scenario-Agent:

```yaml
task_queue:
  id: "evidence-review-queue"
  
  agents:
    - id: "scenario-agent-evidence-review"
      allocation_weight: 10  # 10% of tasks
      
    - id: "human-agent-pool"
      allocation_weight: 90  # 90% of tasks
```

#### Step 5.2: Monitor and Adjust

```
Supervisor Desk → Dispute Operations → Queue Metrics
├── Compare completion rates
├── Compare completion times
├── Review quality metrics
└── Adjust allocation weights based on performance
```

---

## Operator Support

Hub provides operators to automate the Scenario-as-Agent deployment:

### scenario-as-an-agent-operator

Translates a `ScenarioAsAgent` specification into all required components:

```yaml
apiVersion: hub.olympus.tech/v1
kind: ScenarioAsAgent
metadata:
  name: evidence-review-agent
  namespace: evidence-automation
spec:
  # Source Scenario
  source:
    workbench: evidence-automation
    scenario: evidence-review-automation
    
  # Agent Identity
  agent:
    id: scenario-agent-evidence-review
    display_name: "Evidence Review Automation"
    skills:
      - document_analysis
      - evidence_review
    capacity:
      max_concurrent_tasks: 10
      
  # Signal Configuration
  signals:
    webhook_path: "/signals/agent/scenario-agent-evidence-review/notifications"
    trigger:
      scenario_id: evidence-review-automation
      transformation:
        type: low_code
        
  # Deployments (where this agent will be enrolled)
  deployments:
    - target_workbench: dispute-operations
      task_queues:
        - queue_id: evidence-review-queue
          escalation_level: 0
          allocation_weight: 10
          
    - target_workbench: fraud-investigation
      task_queues:
        - queue_id: document-review-queue
          escalation_level: 1
          allocation_weight: 50
```

The operator automatically:
1. Creates IAM identity and bot token
2. Configures HTTP signal endpoint
3. Creates trigger for task notifications
4. Registers webhook subscriptions in target workbenches
5. Enrolls agent in specified task queues

---

## Best Practices

### Do's

| Practice | Rationale |
|----------|-----------|
| **Idempotent task handling** | Same task notification may arrive multiple times |
| **Preserve source context** | Always track original workbench, request, task for callbacks |
| **Add thoughts/memos** | Provide transparency into automation reasoning |
| **Graceful degradation** | If automation fails, allow task to be reassigned |
| **Comprehensive logging** | Enable debugging across workbench boundaries |

### Don'ts

| Anti-Pattern | Why to Avoid |
|--------------|--------------|
| **Ignoring cancellations** | Task or request may be cancelled while processing |
| **Long-running without updates** | Add progress updates for visibility |
| **Hardcoded endpoints** | Use discovered endpoints from source context |
| **Skipping error handling** | Automation failures should be graceful |

---

## Troubleshooting

### Common Issues

| Issue | Possible Cause | Resolution |
|-------|----------------|------------|
| Webhook not received | Incorrect endpoint or auth | Verify webhook registration and secrets |
| Task not updating | Invalid token or expired | Check bot token validity |
| Duplicate processing | Missing idempotency | Add idempotency handling in Hub Application |
| Task stuck ASSIGNED | Automation crashed | Implement timeouts and abandon handling |

### Debug Checklist

1. ✅ Webhook endpoint accessible and authenticated
2. ✅ Trigger matching incoming signal type
3. ✅ Request created in automating Scenario
4. ✅ Hub Application executing
5. ✅ Bot token valid for Agent REST API
6. ✅ Task ID correctly passed through flow

---

## Related Documentation

- [Task Management](../04-subsystems/task-management/README.md) — Task queues and allocation
- [Agent Task Operations](../04-subsystems/task-management/agent-task-operations.md) — Agent operations
- [REST Channels](../06-ux-architecture/tenant-domain/rest-channels.md) — Agent REST API
- [Signal Configuration Guide](../10-guides/signal-configuration-guide.md) — Signal and trigger setup
- [Developer Operators](../04-subsystems/operators/developer-operators.md) — scenario-as-an-agent-operator


