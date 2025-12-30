# 13. Non-Functional Requirements (NFRs)
NFRs ensure FFOS can operate as a mission-critical platform under regulatory scrutiny. Targets are enforced through SLOs, automated testing, and governance reviews before any capability goes live.

## 13.1 Performance & Latency Targets
Critical workflows (approvals, payment executions, concierge responses) must maintain sub-300ms median latency and <1s p95 across channels. Event ingestion, memory updates, and feature refreshes complete within seconds, and orchestration loops enforce deterministic timeout behaviour. Batch analytics run off-peak or in isolated compute pools so real-time SLAs remain unaffected.

## 13.2 Scalability & Capacity Planning
Design for millions of households with elastic scaling for peak obligation periods (tuition cycles, tax seasons). IPC fabric, workflow engine, feature store, and document service scale horizontally with auto-scaling policies driven by telemetry. Storage tiers support hot/warm/cold data with automated lifecycle transitions and cost governance dashboards.

## 13.3 Availability & Resilience
Target 99.95%+ availability for core services and 99.9% for experience agents. Employ multi-AZ deployments, active-active event pipelines, automated failover for memories and IPC brokers, and circuit breakers for downstream dependencies. Critical workflows include compensation patterns (queue, rollback, RM alert) to handle downstream outages gracefully.

## 13.4 Observability & Monitoring
Unified telemetry stack collects metrics, traces, and logs tagged by household, agent, workflow, and consent ID. Real-time dashboards track SLO adherence, and governance agents raise alerts when thresholds breach. Synthetic transactions validate channels continuously; anomalies and engagement deltas feed into the Household Engagement Insights foundation agent.

## 13.5 Operational Support & SRE Considerations
Runbooks cover deployments, scaling operations, incident response, and regulator communications. SRE teams integrate with guardrail services to enforce change windows, simulate failure modes, validate disaster recovery posture quarterly, and maintain RTO/RPO commitments. Post-incident reviews feed backlog prioritization and policy updates.
