# Persona: SRE (Site Reliability Engineer)

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **SRE** deploys and maintains the Olympus Hub platform — ensuring availability, performance, and security. SREs operate at the Hub System scope (Publisher Domain).

| Attribute | Value |
|-----------|-------|
| **Category** | Hub Persona — Hub System (Publisher) |
| **Scope** | Hub System |
| **Domain** | Publisher Identity Domain (Zeta) |
| **Primary Console** | Infrastructure Dashboard |

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Maintain Availability** | Ensure Hub platform uptime and reliability |
| **Ensure Security** | Maintain security posture, handle incidents |
| **Monitor Capacity** | Track usage, plan capacity |
| **Support Tenants** | Assist with technical configuration |

---

## Key Activities

### Operations

1. **Platform Monitoring**
   - Track system health via Olympus Watch
   - Monitor resource utilization
   - Detect and respond to incidents

2. **Deployment**
   - Deploy Hub platform updates
   - Manage infrastructure provisioning
   - Configure platform services

3. **Security**
   - Maintain security configurations
   - Handle security incidents
   - Manage certificates and secrets

### Tenant Support

1. **Technical Assistance**
   - Network configuration
   - Machine connectivity
   - Performance troubleshooting

2. **Capacity Management**
   - Provision tenant resources
   - Scale infrastructure
   - Optimize performance

---

## Hub Capabilities Consumed

### Infrastructure Dashboard (Primary Interface)

| Capability | What It Provides |
|------------|------------------|
| **Platform Health** | Hub system health, component status |
| **Resource Monitoring** | CPU, memory, storage across tenants |
| **Capacity Planning** | Usage trends, growth projections |
| **Incident Management** | Alert handling, incident tracking |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Olympus Watch** | Metrics, logs, traces for Hub platform |
| **Atlantis** | Compute infrastructure management |
| **Atropos** | Event bus health, topic management |
| **Ganymede** | Database health, capacity |
| **Cipher IAM** | Platform security, certificate management |

### What They Manage

| Entity | Actions |
|--------|---------|
| **Hub Platform** | Deploy, upgrade, maintain |
| **Infrastructure** | Provision, scale, optimize |
| **Security** | Certificates, secrets, network policies |
| **Tenant Resources** | Provision on request (via Customer Success) |

---

## Related Documentation

- [05-Infrastructure](../../05-infrastructure/)
- [Olympus Platform Dependencies](../../05-infrastructure/olympus-platform-dependencies.md)
- [Hub Application APM](../../04-subsystems/supporting-systems/hub-application-apm.md)

---

*TODO: Detailed operational runbooks, incident response, capacity planning*

