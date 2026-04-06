| Topic | Deep Dive Follow Up Topics |
|---|---|
| Architecture | Review architectural diagrams of your system including multi-region/zone cloud configuration |
| Reliability and Replication | Table top exercises to walk through the series of events in the case of a region outage. How would services be recovered automatically, or manually, and how is data replicated to prevent data loss? |
| Reliability and Replication | Walk through metrics for scaling services. When and what services get scaled? |
| Reliability and Replication | What automated or manual safeguards are in place to quickly detect and remediate issues? |
| CI/CD | Explain your deployment strategy. Do you operate parallel environments in a blue/green model? |
| Compliance | What controls and processes do you use to ensure PCI‑compliant handling of data at rest and in transit? |
| Locations | Do you have multiple locations for the Cloud for failover? |
| Streaming | Do you stream from the processor datalake/cloud connection for transactions? |


Architecture, Reliability, Security, Compliance
1. World and Estate Architecture
2. SRE Home, Topology, Multi-region Setup, B-G-B Process
4. Show the even distribution of workload across all available Zones
5. Workload segregation by spaces; PCI compliance 
6. Data Storage
7. Messaging and Message Brokers
8. Network, Overlay Network, Service Mesh, CNI 
9. Overview of SRE Home in the US Zone to explain the World, Site, Zone Hierarchy

Multi-Region Switchover
0. HDFC Beta Topology
1. B-G Setup across Regions Active-Active
2. Routine Deployments as B-G-B
3. Switchover
4. (Start Demo)
5. Table-top for Region Failover


Observability, Operations, and Incident Management
1. Customer-Impact centric observability
2. MTTA, MTTD, MTTR focus
3. MTTD: Diagnostic Views (Flows and Components)
3. Alerts and Auto-healing
4. Incident Management with Agents

Multi-Region Switchover (continued)
1. Show that the Cipher Cluster moved to different region and the traffic being served successfully 


Application Performance and Scaling
1. Payment Authorization Request
2. End to End latency
3. Trace depth and components involved
4. Scaling - HPA
5. Scaling - VPA (Jeeves) {Will also be referenced in Alerts}
6. Performance Center



CI, CD

Publisher Home

Configuration Management
1. Launch Control Center from Olympus Home
2. Make Changes in Kernel SaaS and Create a Change Request
3. Get the Change Request Approved
4. Deploy Changes
5. Promote Changes

API Standards and Developer Guides
1. Getting Started
2. API References
3. 



| Observability | What tools are available for us to monitor and support the system? (i.e. dashboard for API status, event mgmt, file delivery, etc.) |
| Observability | What logging is performed (i.e. request receipt to request complete, etc.)? Related to observability above, describe/demo what tools would be available to track lineage of an API request start to finish if a problem gets reported. |
| Alerts | Do you provide alerts and controls and what are they? |

(Foundry, Weave Store, Weave CDM, Deployment Train, )



| API Connectivity | Demonstrate your Developer Portal from the perspective of connecting to an API for the first time. |
| API Standards | How do you ensure consistency, versioning discipline, and backward compatibility across your API ecosystem? |
| API Standards | What logging is performed (i.e. request receipt to request complete, etc.)? Related to observability above, describe/demo what tools would be available to track lineage of an API request start to finish if a problem gets reported. |
| API Versioning | How do you version your APIs, including how breaking vs non‑breaking changes are handled, how long prior versions are supported, and what notice and migration support is provided when |



| Configuration | Show what features can be configured low code/no code and how the configuration is maintained. |
| US Bank configuration | Who is responsible for the initial set up and on-going changes – are changes at the USB level made via a UI or an API |

| Hierarchies | Deep dive with demo on the structure and how it is propagated throughout the entire system. |
| Migration | Deep dive with demo on the structure and how it is propagated throughout the entire system. |
