# Scenario as Tool

> **Category:** Composite Patterns

---

## Overview

**Scenario as Tool** is a composite pattern where a Scenario's HTTP signals are exposed as Tool operations. This allows other Hub Applications or AI agents to invoke the Scenario synchronously as a tool call, receiving structured responses without managing the full request lifecycle.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Tool** as a capability that performs operations and **Scenario** as an operational situation. This pattern bridges them by exposing scenario capabilities as callable tools.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Tool | Scenario as Tool | Scenario exposed as tool |
| Scenario | Source of tool operations | HTTP signals become operations |

### Gap This Fills

The ontology treats tools and scenarios separately. This pattern addresses:
1. **Synchronous access**: How to call scenario logic synchronously?
2. **Tool composition**: How to use scenario as building block?
3. **AI integration**: How can AI agents use scenario capabilities?

---

## Definition

**Scenario as Tool** is a pattern where:
- A Scenario is exposed as a Tool with multiple operations
- Each HTTP signal type becomes a tool operation
- Invocations are synchronous (request-response)
- The Tool is registered in the workbench Tool Registry

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped; can be exposed to other workbenches |
| **Lifecycle** | Created by Developer; available while scenario active |
| **Ownership** | Developer creates; workbench owns |
| **Multiplicity** | One tool per scenario; multiple operations per tool |

---

## Rationale

### Why This Design?

Scenario as Tool enables:
1. **Reuse**: Use scenario logic without duplication
2. **Synchronous calls**: Immediate results for tool consumers
3. **AI agents**: Scenario becomes tool in agent toolbox
4. **Composition**: Build complex logic from scenario tools

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Direct HTTP calls** | No tool registry integration |
| **One tool per signal** | Tool explosion; harder to manage |
| **Full request lifecycle** | Too heavy for sync needs |

---

## Structure

### ScenarioAsTool CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsTool
metadata:
  name: validation-tool
  namespace: acme-bank
spec:
  # Source Scenario
  scenario_ref: validation-scenario
  
  # Tool identity
  tool:
    name: transaction-validator
    display_name: "Transaction Validator"
    description: "Validates transactions against rules"
    version: "1.0.0"
    
  # Operations (from HTTP signals)
  operations:
    - name: validate_amount
      signal_type: validate.amount
      description: "Validate transaction amount"
      parameters:
        - name: amount
          type: number
          required: true
        - name: currency
          type: string
          required: false
          default: "USD"
      returns:
        type: object
        schema:
          valid: boolean
          reason: string
          
    - name: validate_merchant
      signal_type: validate.merchant
      description: "Validate merchant details"
      parameters:
        - name: merchant_id
          type: string
          required: true
          
  # Access control
  access:
    within_workbench: true
    exposed_to:
      - workbench: dispute-ops-prod
```

### Tool in Registry

```
Tool Registry
└── transaction-validator (from Scenario)
    ├── validate_amount
    └── validate_merchant
```

---

## Behavior

### How It Works

```
1. Consumer calls tool operation
   └── tool.validate_amount(amount=500)

2. Tool Registry resolves to ScenarioAsTool
   └── Maps operation to signal_type

3. Creates synchronous signal
   └── POST to scenario HTTP endpoint

4. Scenario processes signal
   └── Hub Application handles

5. Response returned
   └── Structured response per schema

6. Consumer receives result
   └── { valid: true, reason: "Amount within limits" }
```

### Invocation Example

```python
# AI agent using scenario as tool
class InvestigationAgent:
    async def investigate(self, transaction):
        # Call scenario as tool
        validation = await self.tools.invoke(
            tool="transaction-validator",
            operation="validate_amount",
            params={
                "amount": transaction.amount,
                "currency": transaction.currency
            }
        )
        
        if not validation.valid:
            return f"Transaction invalid: {validation.reason}"
```

### Operation Mapping

| Scenario HTTP Signal | Tool Operation |
|---------------------|----------------|
| `POST /validate-amount` | `validate_amount` |
| `POST /validate-merchant` | `validate_merchant` |
| `POST /check-fraud-score` | `check_fraud_score` |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Tool Registry | ← registered in | Tool available in registry |
| Scenario | → routes to | Operations routed to scenario |
| Hub Application | → handled by | Application processes |
| AI Agents | ← used by | Agents invoke tool |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **HTTP signals only** | Only HTTP signals become operations |
| **Synchronous** | Tool calls are request-response |
| **Schema defined** | Parameters and returns specified |
| **One tool per scenario** | Operations grouped under one tool |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Reuse** | Scenario logic as tool |
| ✅ **Synchronous** | Immediate results |
| ✅ **AI-ready** | Tools for AI agents |
| ✅ **Organized** | One tool, many operations |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Sync only** | Use direct SX for async needs |
| ⚠️ **Latency** | Scenario must respond quickly |

---

## Examples

### Example 1: Fraud Scoring Tool

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsTool
metadata:
  name: fraud-scorer-tool
spec:
  scenario_ref: fraud-scoring
  
  tool:
    name: fraud-scorer
    display_name: "Fraud Scorer"
    
  operations:
    - name: score_transaction
      signal_type: fraud.score
      parameters:
        - name: transaction_id
          type: string
          required: true
      returns:
        type: object
        schema:
          score: number
          risk_level: string
          factors: array
```

### Example 2: Tool Consumption

```python
# Hub Application using fraud scorer tool
result = await self.tools.fraud_scorer.score_transaction(
    transaction_id="TXN-12345"
)

if result.risk_level == "HIGH":
    await self.escalate_to_fraud_team()
```

---

## Implementation Notes

### For Developers

- Define clear operation schemas
- Handle errors gracefully (return error responses)
- Keep operations focused and fast
- Document parameters and returns

### For Operators

- Monitor tool invocation latency
- Review access patterns
- Check error rates per operation

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Scenario as Agent](./scenario-as-agent.md) | Different pattern |
| [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md) | Similar but application-level |
| [Direct Tool Dispatcher](./direct-tool-dispatcher.md) | May use dispatcher |

---

## References

- [Scenario as Tool Pattern](../../09-composite-systems-and-patterns/scenario-as-a-tool.md)
- [Developer Operators](../../04-subsystems/operators/developer-operators.md)

