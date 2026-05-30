# SDK/Library Module

**Model:** Definition Model
**Dimension:** Ecosystem
**Owner:** Product Management (API/Platform), Developer Relations, Engineering

## Definition

An SDK/Library Module is a language-specific client providing idiomatic access to API Modules. It wraps Ecosystem API Module operations in language-specific abstractions — typed models, error handling patterns, retry logic, and async support. An SDK/Library Module is structurally a Structural Module with a **Client-Distributed** deployment topology (published via package registry, instantiated in the customer's codebase).

## Purpose

Reduces time-to-first-call and integration complexity for developers working in specific languages. Without SDKs, every developer must write raw HTTP/protocol-level code, handle serialization, implement retry logic, and manage authentication — work that is repetitive and error-prone.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Module name (e.g., "Python Payments SDK," "Java Card Issuing Client") |
| Language / Platform | Text | Target language or platform (Python, Java, Node.js, .NET, Go, etc.) |
| Wraps | Reference(s) | API Module(s) this SDK provides access to |
| Generation Strategy | Enum | Auto-generated / Hand-crafted / Hybrid |
| Distribution Channel | Text | Package registry (PyPI, Maven Central, npm, NuGet) |
| Version Tracking | Text | How SDK versions relate to API versions |
| Key Capabilities | List | What the SDK adds beyond raw API access (typed models, retry, pagination, async, mocking) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Is a | Module (Structural) | Structurally a Structural Module (Client-Distributed topology) |
| Wraps | API Module (Ecosystem) | Provides idiomatic access to API surface |
| Serves | Developer Persona (Ecosystem) | Used by developers in this language |
| Versioned with | API Compatibility Contract (Ecosystem) | SDK versions track API versions |
| Assessed by | Win Review (Win) | SDK adoption and developer satisfaction reviewed |

## Example

**"Python Payments SDK"** — Wraps Cross-Border Payments API with typed Pydantic models, automatic retry with exponential backoff, async/await support, and built-in webhook signature verification. Published on PyPI. Hand-crafted (not auto-generated) for ergonomic API design. Version 3.x tracks API v2. Key Capabilities: typed request/response models, configurable retry policy, async client, pagination helpers, test mode with mock responses.

---
