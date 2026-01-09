# Prediction Tools

> **Status:** 🔴 Stub — Placeholder for expansion

Prediction Tools are **stateless ML model inference services** that Hub provides as native capabilities. They enable Hub Applications to invoke trained machine learning models for predictions, scoring, and classification—with automatic CAF compliance.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Provide stateless, auditable ML inference capabilities |
| **Nature** | Pure functions — predictions based solely on input features |
| **CAF Integration** | Automatic — all invocations produce audit artifacts |
| **Invocation** | Via Tool Registry, like any other Tool |
| **Hosting** | Elara (Kserve) on Atlantis |

---

## Elara Integration

**Elara** is the MLOps platform in the Olympus ecosystem. Hub leverages Elara for prediction capabilities:

```
┌─────────────────────────────────────────────────────────────────┐
│                         ELARA                                    │
│                   (Olympus MLOps Platform)                       │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                    EXPLORATION                              ││
│  │  (Notebooks, Experiments, Feature Engineering)              ││
│  └─────────────────────────────────────────────────────────────┘│
│                            ↓                                     │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                MODEL REGISTRY                               ││
│  │  (Versioned models, metadata, lineage)                      ││
│  └─────────────────────────────────────────────────────────────┘│
│                            ↓                                     │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                 MODEL SERVING                               ││
│  │            (Kserve on Atlantis)                             ││
│  │                                                             ││
│  │  ┌────────────────────────────────────────────────────────┐ ││
│  │  │     ← Hub Native Utility Gateway Integration →         │ ││
│  │  └────────────────────────────────────────────────────────┘ ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

**Hub's Integration Point:** Model Serving via Kserve, exposed as Prediction Tools.

> **Note:** Elara's exploration and experimentation capabilities (notebooks, feature engineering, model training) are outside Hub's scope. Hub consumes deployed models.

---

## Supported Model Frameworks

Elara/Kserve supports a wide range of ML frameworks:

| Framework | Format | Use Cases |
|-----------|--------|-----------|
| **Scikit-learn** | Pickle, Joblib | Traditional ML (regression, classification, clustering) |
| **TensorFlow** | SavedModel | Deep learning, neural networks |
| **PyTorch** | TorchScript | Deep learning, NLP models |
| **XGBoost** | XGBoost format | Gradient boosting, tabular data |
| **LightGBM** | LightGBM format | Gradient boosting, large datasets |
| **ONNX** | ONNX format | Cross-framework compatibility |
| **Custom** | Custom serving runtime | Specialized models |

---

## Prediction Tool Registration

Prediction tools are registered in the Tool Registry with model-specific metadata:

```yaml
tool:
  id: "fraud-score-model"
  name: "Fraud Score Model"
  namespace: "fraud-detection"
  
  # Tool type marker
  type: prediction_tool
  
  # Model serving configuration
  prediction_engine:
    type: elara_kserve
    model_ref: string           # Reference in Elara Model Registry
    model_version: string       # Deployed version
    serving_runtime: enum       # sklearn | tensorflow | pytorch | xgboost | custom
  
  # Input/Output schemas
  input_schema:
    type: object
    properties:
      transaction_amount: { type: number }
      merchant_category: { type: string }
      time_since_last_txn: { type: number }
      location_distance: { type: number }
      # ... feature vector
  
  output_schema:
    type: object
    properties:
      fraud_probability: { type: number, minimum: 0, maximum: 1 }
      risk_category: { type: string, enum: [low, medium, high, critical] }
      top_factors: { type: array }
  
  # CAF configuration
  caf_config:
    explanation_level: enum     # minimal | standard | detailed
    capture_feature_importance: boolean
    context_capture: enum       # inputs_only | inputs_and_sources | full
  
  # Model performance metadata
  model_metadata:
    training_date: datetime
    evaluation_metrics:
      auc_roc: number
      precision: number
      recall: number
    feature_count: number
  
  # Access control (standard)
  access_control:
    discoverability: { ... }
    invocation: { ... }
```

---

## Invocation Pattern

```
Hub Application
        │
        │ POST /tools/fraud-score-model/invoke
        │ {
        │   "features": {
        │     "transaction_amount": 5000,
        │     "merchant_category": "electronics",
        │     "time_since_last_txn": 120,
        │     "location_distance": 500
        │   },
        │   "request_id": "REQ-456"
        │ }
        │
        ▼
┌─────────────────────────────────────────┐
│       Native Utility Gateway            │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       Elara / Kserve                    │
│                                         │
│  1. Load model (cached)                 │
│  2. Preprocess features                 │
│  3. Run inference                       │
│  4. Compute feature importance          │
│  5. Return prediction                   │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       CAF Integration Layer             │
│                                         │
│  1. Record invocation                   │
│  2. Capture feature snapshot            │
│  3. Store explanation (SHAP/LIME)       │
│  4. Link to Request                     │
│  5. Generate audit reference            │
└────────────────┬────────────────────────┘
                 │
                 ▼
Response:
{
  "result": {
    "fraud_probability": 0.87,
    "risk_category": "high",
    "top_factors": [
      "unusual_amount",
      "new_merchant_category",
      "distant_location"
    ]
  },
  "caf_audit": {
    "invocation_id": "INV-890",
    "request_id": "REQ-456",
    "model_version": "v2.3.1",
    "explanation": {
      "type": "feature_importance",
      "method": "SHAP",
      "feature_contributions": {
        "transaction_amount": 0.35,
        "location_distance": 0.28,
        "merchant_category": 0.15,
        "time_since_last_txn": 0.09
      }
    },
    "confidence": 0.87,
    "audit_ref": "caf://predictions/INV-890"
  }
}
```

---

## Explanation Types

Prediction tools support various explainability methods:

### Feature Importance (SHAP)

```yaml
explanation:
  type: feature_importance
  method: SHAP
  base_value: 0.12  # Average prediction
  feature_contributions:
    transaction_amount: +0.35
    location_distance: +0.28
    merchant_category: +0.15
    time_since_last_txn: +0.09
    other_features: -0.02
  # Sum of base_value + contributions = final prediction
```

### Local Interpretable Explanations (LIME)

```yaml
explanation:
  type: local_explanation
  method: LIME
  interpreted_model: "linear"
  feature_weights:
    - feature: "transaction_amount > 4000"
      weight: 0.42
    - feature: "location_distance > 400"
      weight: 0.31
    - feature: "merchant_category = electronics"
      weight: 0.18
  fidelity: 0.94  # How well local model approximates actual model
```

### Decision Path (Tree Models)

```yaml
explanation:
  type: decision_path
  method: tree_path
  path:
    - node: 0
      feature: "transaction_amount"
      threshold: 2500
      direction: ">"
    - node: 3
      feature: "location_distance"
      threshold: 300
      direction: ">"
    - node: 7
      feature: "merchant_category"
      value: "electronics"
      match: true
  leaf_node: 15
  leaf_prediction: 0.87
```

---

## Model Deployment Workflow

### 1. Train Model (Elara — outside Hub scope)

Data Scientists use Elara for experimentation, training, and validation.

### 2. Register Model in Elara

```yaml
# In Elara Model Registry
model:
  name: "fraud-detection-v2"
  version: "2.3.1"
  framework: xgboost
  metrics:
    auc_roc: 0.94
    precision: 0.89
    recall: 0.91
  artifacts:
    model_file: s3://models/fraud/v2.3.1/model.xgb
    feature_schema: s3://models/fraud/v2.3.1/features.json
```

### 3. Deploy to Kserve (via Elara)

```yaml
# Kserve InferenceService
inferenceService:
  name: fraud-score-model
  predictor:
    model:
      modelFormat: xgboost
      storageUri: s3://models/fraud/v2.3.1/model.xgb
    resources:
      requests:
        cpu: 100m
        memory: 256Mi
```

### 4. Register as Hub Prediction Tool

```
Hub Console → Native Utilities → Prediction Tools → Register
├── Connect to Elara: [Select deployed model]
├── Model: fraud-detection-v2 (v2.3.1)
├── Tool ID: fraud-score-model
├── Configure CAF: [Explanation level, capture settings]
└── Access Control: [Workbenches, roles]
```

---

## Model Versioning & Governance

| Feature | Description |
|---------|-------------|
| **Version Tracking** | All predictions logged with model version |
| **A/B Testing** | Split traffic between model versions |
| **Canary Deployment** | Gradual rollout with monitoring |
| **Rollback** | Quick rollback to previous version |
| **Audit Trail** | Which model version produced each prediction |

---

## Performance Considerations

| Aspect | Guidance |
|--------|----------|
| **Latency** | Models should respond in <100ms for real-time use |
| **Batching** | Use batch inference for non-real-time scenarios |
| **Caching** | Model weights cached; feature transformations optimized |
| **Scaling** | Kserve auto-scales based on demand |

---

## Related Documentation

- [Hub Native Utilities](./README.md) — Overview
- [Decision Tools](./decision-tools.md) — Rule-based decisions
- [CAF Integration](./caf-integration.md) — Audit requirements
- [Tool Registry](../registry-services/tool-registry.md) — Registration

---

*TODO: Detailed design — Elara integration, feature store integration, model monitoring*

