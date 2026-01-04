# Ontology Guide: Business Stakeholders

**For:** Operations Executives, Product Managers, Compliance Officers, Audit Teams, Business Analysts

**Your goal:** Understand what concepts mean and how they relate, without implementation details.

---

## How to Use This Guide

1. **Start with the glossary below** to understand core terms
2. **Read the [Introduction](./ontology-reference.md#introduction)** for the four-layer framework
3. **Explore specific concepts** based on your focus area

---

## Key Concepts by Focus Area

| Focus Area | Relevant Concepts | Layer |
|------------|-------------------|-------|
| **Understanding Operations** | [Domain](./ontology-1-perception-layer.md#domain), [Workbench](./ontology-1-perception-layer.md#workbench), [Scenario](./ontology-1-perception-layer.md#scenario), [Operation](./ontology-3-execution-layer.md#operation-abstract) | Perception, Execution |
| **Compliance & Governance** | [SOP](./ontology-2-normative-layer.md#sop-standard-operating-procedure), [Knowledge Base](./ontology-2-normative-layer.md#knowledge-base-kb), [Checklist](./ontology-2-normative-layer.md#checklist), [Escalation](./ontology-3-execution-layer.md#escalation) | Normative, Execution |
| **Workforce & AI** | [Agent](./ontology-3-execution-layer.md#agent), [Human](./ontology-3-execution-layer.md#human), [AI Agent](./ontology-3-execution-layer.md#ai-agent), [Role](./ontology-2-normative-layer.md#role), [Responsibility](./ontology-2-normative-layer.md#responsibility) | Normative, Execution |
| **Customer Interaction** | [Request](./ontology-1-perception-layer.md#request) (especially Service Requests), [Task](./ontology-3-execution-layer.md#task) | Perception, Execution |

---

## Quick Reference Glossary

### Core Flow (How Work Happens)

| Term | Plain Language | Banking Example |
|------|----------------|-----------------|
| **Signal** | Something happened that the system noticed | A $50,000 wire transfer was initiated |
| **Trigger** | A rule that decides what to do with what happened | "If wire > $10K to new beneficiary, create review request" |
| **Request** | A formal ask for something to be done | "Review this wire transfer for AML compliance" |
| **Scenario** | The situation we're responding to | "Large wire to new international beneficiary" |
| **Operation** | The work being done to handle the situation | The AML review investigation |
| **Activity** | A step in the work | "Verify beneficiary identity" |
| **Task** | A step assigned to a person or AI | "Analyst: Review transaction history" |
| **Action** | A specific thing done to complete a task | Click "Approve" in the system |

### People and Systems

| Term | Plain Language | Banking Example |
|------|----------------|-----------------|
| **Agent** | Anyone (human or AI) who does work | A fraud analyst or a chatbot |
| **Human** | A person doing operational work | Dispute analyst, branch teller |
| **AI Agent** | Software that does operational work | Fraud scoring model, document classifier |
| **Role** | A job function with defined duties | "Senior Fraud Analyst" |
| **Capability** | What someone can do (skills) | "Trained in AML regulations" |
| **Capacity** | How much someone can handle | "Can process 25 cases per day" |

### Rules and Knowledge

| Term | Plain Language | Banking Example |
|------|----------------|-----------------|
| **SOP** | The official way to handle a situation | "Dispute Resolution Procedure" |
| **Knowledge Base** | Where all the guidance documents live | Policy repository, procedure manuals |
| **Runbook** | Step-by-step guide for a specific task | "How to verify a customer's identity" |
| **Checklist** | Regular reviews that must be done | "Daily cash position review" |
| **Goal** | What we're trying to achieve | "Resolve disputes within 10 days" |
| **Responsibility** | What someone is accountable for | "Ensure AML compliance" |

### Work Organization

| Term | Plain Language | Banking Example |
|------|----------------|-----------------|
| **Domain** | A business area we're managing | Dispute resolution, fraud prevention |
| **Workbench** | Everything needed to run a business area | The Dispute Workbench with all its tools |
| **Business Entity** | The things we're managing | Accounts, transactions, customers |
| **Task Queue** | Where tasks wait to be picked up | "Fraud Analyst Queue" |
| **Escalation** | Moving unfinished work to someone senior | Not resolved in 4 hours → Senior Analyst |

### Types of Work

| Term | Plain Language | When to Use |
|------|----------------|-------------|
| **Procedure** | A defined sequence of steps | Routine, repeatable work |
| **Workflow** | Multiple people's procedures connected | Work passing between roles |
| **Case** | Flexible investigation that evolves | Complex, unpredictable work |

### Request Types

| Type | Who Starts It | Banking Example |
|------|---------------|-----------------|
| **Service Request** | Customer (or agent for customer) | Dispute filing, account closure |
| **Business Request** | Internal staff | Reconciliation adjustment |
| **System Request** | An application | Failed batch, system error |

### Systems and Technology

| Term | Plain Language | Banking Example |
|------|----------------|-----------------|
| **Machine** | An application or system | Core banking system, payment gateway |
| **Sensor** | Something that watches for events | Transaction monitor, fraud detection |
| **Environment** | Where all the systems live | Your bank's IT infrastructure |
| **Command** | An action you can tell a system to do | "Lock this account" |
| **Tool** | Something that helps agents work | Fraud scoring model, decision helper |
| **Automation** | The recipe for how work should flow | The dispute resolution workflow definition |
| **Automation Runtime** | The platform that runs the recipes | Olympus Hub |

---

## Visual Overview

For a visual representation of how these concepts relate, see:
- [Ontology Graph Diagram](./ontology-diagrams.md#appendix-mermaid-ontology-graph)

---

## Next Steps

- [Full Ontology Reference](./ontology-reference.md) — Complete navigation hub
- [Perception Layer](./ontology-1-perception-layer.md) — Domain, Signals, Requests
- [Normative Layer](./ontology-2-normative-layer.md) — Roles, SOPs, Knowledge Base
- [Execution Layer](./ontology-3-execution-layer.md) — Operations, Tasks, Agents

