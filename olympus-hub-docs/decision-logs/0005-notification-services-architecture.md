# ADR-0005: Single Notification Service with Persona-Specific Handlers

## Status

Accepted

## Date

2026-01-05

## Context

Hub needs to notify various personas (Agents, Supervisors, Business Users, Tenant Admins) about Request updates. Options considered:

1. **Separate services per persona**: Agent Notification Service, Supervisor Notification Service, etc.
2. **Single service with multiple handlers**: One service with persona-specific internal handlers
3. **Distributed in Hub Applications**: Each Application handles its own notifications

Key requirements:
- Translate Request Updates into persona-appropriate notifications
- Support multiple mechanisms (email, SMS, push, webhook)
- Respect user preferences and Scenario specifications
- Integrate with Cipher Notification Services (CNS) for delivery

## Decision

**Implement a single Notification Service with persona-specific handlers.**

Architecture:
1. **Notification Service** is a single service that observes Signal Exchange
2. **Persona-specific handlers** (Agent, Supervisor, Business User, Tenant Admin) are internal components
3. **CNS integration** handles actual delivery, retries, and callbacks
4. **User preferences** are stored in Notification Service's own store (tenant-scoped)

Flow:
1. Notification Service receives all Request Updates from SX
2. Determines recipients based on Scenario Notification Specification
3. Resolves user preferences for each recipient
4. Routes to appropriate persona handler
5. Handler formats notification and dispatches to CNS
6. CNS delivers via configured mechanisms

## Consequences

### Positive
- **Centralized logic**: All notification rules in one place
- **Consistent behavior**: Same preference handling across personas
- **Single SX integration**: One observer registration, not multiple
- **Easier maintenance**: One service to update, deploy, monitor

### Negative
- **Single point of failure**: If Notification Service fails, all notifications fail
- **Scaling complexity**: Must scale to handle all personas' load

### Neutral
- Persona handlers can be independently developed but are deployed together

## Related

- [Notification Services](../04-subsystems/notification-services/README.md)
- [Observer Notifications](../04-subsystems/signal-exchange/observer-notifications.md)

