# UPIM Visual Models

> **DR-036 authority note:** Deployment/versioning semantics in DR-036 supersede DR-026–029 for operational use. Diagrams marked historical retain Package/SDD labels for design context; prefer Seeds 16–17 and updated diagrams 1–2, 5.

## Purpose

This file collects visual models (mermaid diagrams) that illustrate cross-entity relationships, cross-track flows, and architectural patterns in the Unified Product Information Model. These diagrams complement the entity definitions (in `entities/`) and narrative seeds (in `narrative-seeds.md`) by providing visual representations of flows that span multiple entities and tracks.

## Maintenance

Each diagram carries:
- **Title** — what the diagram shows
- **Source** — the plan or decision record that produced it
- **Reflects** — which decision record(s) and entities the diagram represents

Diagrams may go stale as the model evolves. When entities, relationships, or flows are modified, check whether existing diagrams need updating. The source and reflects fields help identify staleness: if a referenced DR is superseded or an entity is renamed, the diagram likely needs revision.

This is a working document — add new diagrams as the model evolves rather than leaving them in ephemeral plan files.

---

## 1. Composition Levels and Run Track Flow

**Source:** Plan `composition_levels_and_run_track_3c7f70e2`
**Reflects:** DR-026 (Build Track Detailing), DR-027 (Composition Levels), DR-028 (Deployment Descriptors)

Shows the Build Track producing Component Versions, System Versions, and Product Versions; Run Track produces Deployment Specifications and applies them to environments. Reflects DR-036.

```mermaid
flowchart TD
    subgraph BuildTrack [Build Track]
        PSD["PSD (Dim 1)"] --> Epic["Epic (Module-scoped)"]
        Epic --> Story["Story (Module-scoped)"]
        Story --> TechTask["Technical Task (System-scoped)"]
        TechTask --> CompVer["Component Version (atomic build)"]
        CompVer --> SysVer["System Version (sealed BOM)"]
        SysVer --> ProdVer["Product Version (certified BOM)"]
    end
    subgraph RunTrack [Run Track]
        RunEpic["Run Epic"] --> RunStory["Run Story"]
        RunStory --> RunTask["Technical Task"]
        RunTask --> OpsSysVer["Operational System Version"]
        OpsSysVer --> ProdVer
        SysVer --> SDS["System Deployment Specification"]
        ProdVer --> PDS["Product Deployment Specification"]
        SDS --> PDS
        PDS -->|"deploy via"| Env["Environment(s)"]
    end
```

---

## 2. Change-to-Deployment Workflow

**Source:** Plan `change-to-deployment_workflow_d93f53f7`
**Reflects:** DR-029 (Change-to-Deployment Workflow Redesign), DR-027, DR-028

Shows Dim 5 Product Specification, Dim 7 Deployment Train/Station, and Track 3 deployment workflow per DR-036.

```mermaid
graph TB
  subgraph defModel [Definition Model]
    ProdSpec["Product Specification (Dim 5)"]
    Train[Deployment Train (Dim 7)]
    Station[Station]
    DepEnv[Deployment Environment]

    Train -->|contains| Station
    Station -->|targets| DepEnv
    ProdSpec -->|declares| Systems["Systems (Dim 5)"]
  end

  subgraph workModel [Work Model - Track 3]
    CR[Change Request]
    DP[Deployment Plan]
    DPT[Deployment Planning Task]
    DrillTask[Deployment Drill Task]
    DeployTask[Deployment Task]
    VerifyTask[Verification Task]

    SysVer[System Version]
    ProdVer[Product Version]
    SDS[System Deployment Specification]
    PDS[Product Deployment Specification]
    DeployRecord["Deployment (artifact)"]

    CR -->|"scoped to"| Train
    CR -->|contains| DP
    DP -->|produces| DPT
    DPT -->|"produces"| SDS
    DPT -->|"produces"| PDS
    SysVer --> SDS
    ProdVer --> PDS
    SDS --> PDS
    DrillTask -->|"predecessor to"| DeployTask
    DeployTask -->|"applies"| SDS
    DeployTask -->|"applies"| PDS
    DeployTask -->|"produces"| DeployRecord
  end
```

---

## 3. Incident Management Flow

**Source:** Plan `incident_management_refactor_53441906`
**Reflects:** DR-030 (Incident Management Refactor)

Shows how detection sources produce Incident artifacts, which are handled by work entities (Incident Response Task, Customer Communication Task, Post-Incident Review), producing outputs across multiple tracks, while also informing Run Track planning tasks.

```mermaid
flowchart TD
    subgraph detection [Detection Sources]
        SM["System Monitoring"]
        WC["Win Case (Complaint)"]
        OO["Operator Observation"]
    end

    subgraph artifact [Work Artifact]
        INC["Incident (artifact)"]
    end

    subgraph response [Work Entities]
        IRT["Incident Response Task"]
        CCT["Customer Communication Task"]
        PIR["Post-Incident Review"]
    end

    subgraph outputs [Outputs]
        PIReport["Post-Incident Report"]
        BUG["Bug (Track 2)"]
        SIG["Signal (Track 1)"]
        RE["Run Epic (Track 3)"]
        CR["Change Request (Track 3)"]
        ODR["ODR (Dim 7)"]
        EF["Evolve Finding (Track 5)"]
    end

    subgraph planning [Run Track Planning Consumers]
        DPT["Deployment Planning Task"]
        CPT["Capacity Planning Task"]
        REScope["Run Epic scoping"]
    end

    SM -->|"produces"| INC
    WC -->|"corresponds to"| INC
    OO -->|"produces"| INC

    INC -->|"responded to by"| IRT
    INC -->|"communicated by"| CCT
    INC -->|"reviewed by"| PIR

    IRT -->|"may produce"| BUG
    IRT -->|"may trigger"| CR
    PIR -->|"produces"| PIReport
    PIR -->|"may produce"| SIG
    PIR -->|"may trigger"| RE
    PIR -->|"may produce"| ODR
    PIR -->|"may produce"| EF

    INC -->|"informs"| DPT
    INC -->|"informs"| CPT
    INC -->|"informs"| REScope
```

---

## 4. Track 5: Evolve Flow

**Source:** Plan `track_5_evolve_and_artifact_catalog_abc94030`
**Reflects:** DR-022 (Track 5: Evolve and Artifact Type Catalog)

Shows how Evolve Monitoring triggers Evolve Review, which produces Evolve Findings that feed Evolve Planning, which scopes Evolve Definition Tasks that update both Work Model entities and Operating Model guidance.

```mermaid
flowchart TD
    subgraph Track5 ["Track 5: Evolve"]
        EP["Evolve Planning"]
        ER["Evolve Review"]
        EDT["Evolve Definition Task"]
        EM["Evolve Monitoring"]
    end

    EM -->|triggers| ER
    ER -->|produces| EF["Evolve Findings"]
    EF -->|feeds| EP
    EP -->|scopes| EDT
    EDT -->|updates| WM["Work Model entities"]
    EDT -->|updates| OM["Operating Model guidance"]
```

---

## 5. Emergency Fix Path

**Source:** Plan `hotfix_emergency_fix_path_4084a483`
**Reflects:** DR-031 (Hotfix / Emergency Fix Path), DR-029 (Emergency-Technical CR), DR-030 (Incident Response Task)

Shows the end-to-end hotfix chain spanning Build Track (P0 Bug → Emergency System Version) and Run Track (Emergency-Technical CR → Deployment), with the deferred-gate obligation loop.

```mermaid
flowchart TD
    INC["Incident (SEV-0/SEV-1)"]
    IRT["Incident Response Task"]
    BUG["Bug (P0, Run provenance)"]
    TT["Technical Task (sprint bypass)"]
    SV["System Version (Emergency gate profile)"]
    SDS_node["System Deployment Specification"]
    CR["Change Request (Emergency-Technical)"]
    DT["Deployment Task"]
    DEP["Deployment (artifact)"]
    VT["Verification Task"]
    DEFER["Deferred Gate Obligation"]
    STDSV["Subsequent Standard System Version"]

    INC -->|"responded to by"| IRT
    IRT -->|"produces (provenance: Run)"| BUG
    IRT -->|"triggers"| CR
    BUG -->|"spawns"| TT
    TT -->|"produces"| SV
    SV -->|"described by"| SDS_node
    SDS_node -->|"applied by"| DT
    DT -->|"governed by"| CR
    DT -->|"produces"| DEP
    DEP -->|"verified by"| VT
    SV -->|"carries"| DEFER
    DEFER -->|"resolved by"| STDSV
    BUG -->|"closed when"| STDSV
```

---

## FIR Intake and Routing Flow (DR-032)

```mermaid
flowchart TB
    subgraph Sources ["Feedback Sources"]
        CUST["Customer / Partner<br/>(External)"]
        SRE["SRE / Monitoring<br/>(Run)"]
        QA["QA / Developer<br/>(Build)"]
        PM["PM / Support<br/>(Internal)"]
    end

    FIR["FIR<br/>(First Information Report)<br/>PFR-Win"]

    CUST -->|"reports via portal/email/chat"| FIR
    SRE -->|"monitoring alert or observation"| FIR
    QA -->|"regression observation"| FIR
    PM -->|"proactive observation"| FIR

    subgraph Triage ["Win Team Triage"]
        ASSESS["Categorize + Prioritize"]
        ROUTE["Route to Track(s)"]
        DIRECT["Direct Resolution<br/>(zero sub-items)"]
    end

    FIR --> ASSESS
    ASSESS --> ROUTE
    ASSESS -->|"trivial inquiry"| DIRECT

    subgraph Routed ["Routed Sub-Items"]
        INC["Incident<br/>(Track 3, OPR)"]
        BUG_R["Bug<br/>(Track 2, WR)"]
        SIG["Signal<br/>(Dim 1, PIR)<br/>Problem / Need / Opportunity"]
        WC["Win Case<br/>(Track 4, WR)<br/>Query / Complaint / Escalation"]
        MT["Maintenance Task<br/>(Track 3, WR)"]
    end

    ROUTE -->|"service degradation"| INC
    ROUTE -->|"defect"| BUG_R
    ROUTE -->|"capability gap / opportunity"| SIG
    ROUTE -->|"customer query / complaint"| WC
    ROUTE -->|"operational maintenance"| MT

    INC -.->|"Originating FIR ref"| FIR
    BUG_R -.->|"Originating FIR ref"| FIR
    SIG -.->|"Originating FIR ref"| FIR
    WC -.->|"Originating FIR ref"| FIR
    MT -.->|"Originating FIR ref"| FIR

    RESOLVE["FIR Resolved<br/>(all sub-items resolved)"]
    INC --> RESOLVE
    BUG_R --> RESOLVE
    SIG --> RESOLVE
    WC --> RESOLVE
    MT --> RESOLVE
    DIRECT --> RESOLVE

    CLOSE["FIR Closed<br/>(reporter notified)"]
    RESOLVE --> CLOSE
```

---

## Foundry Repository Landscape — 15-Repository Topology (DR-033)

```mermaid
graph TB
    subgraph Strategy_Definition ["Strategy & Definition (Dim 1, 2, 3, 9)"]
        PIR[("PIR<br/>Product Intent<br/>Dim 1, 2, 3")]
        DKB[("DKB<br/>Domain Knowledge<br/>Dim 9")]
    end

    subgraph Product_Structure ["Product Structure (Dim 5, 6, 7, 8)"]
        DAR[("DAR<br/>Design & Arch<br/>Dim 5, 6, 7")]
        POR[("POR<br/>Product Ontology<br/>Dim 8")]
    end

    subgraph Engineering ["Engineering (Track 2)"]
        CAR[("CAR<br/>Code Artifacts")]
        QVS[("QVS<br/>Quality & Verify<br/>Build-time")]
    end

    subgraph Operations ["Operations (Track 3)"]
        OPR[("OPR<br/>Operations<br/>Run-time")]
    end

    subgraph Feedback ["Feedback (Track 4)"]
        PFR_W[("PFR-Win<br/>FIRs, Win Cases")]
        PFR_R[("PFR-Run<br/>Incident Mirrors")]
        PFR_B[("PFR-Build<br/>Bug Mirrors")]
    end

    subgraph Work_Practices ["Work & Practices"]
        WR[("WR<br/>Work Repository<br/>All 5 Tracks")]
        PPR[("PPR<br/>Practices<br/>Op Model + Track 5")]
    end

    subgraph Workforce_Memory ["Workforce, Stakeholders & Memory"]
        WFR[("WFR<br/>Workforce<br/>Internal Agents")]
        ESR[("ESR<br/>External Stakeholders<br/>Reference Layer")]
        PEIR[("PEIR<br/>Evolution & Lineage<br/>Traceability")]
    end

    %% Main flows
    PIR ==>|"Intent"| DAR
    DAR ==>|"Blueprints"| CAR
    CAR ==>|"Code"| QVS
    CAR ==>|"Deploy specs"| OPR

    %% Feedback loops
    PFR_W -->|"FIR-routed Signals"| PIR
    PFR_W -->|"FIR-routed Bugs"| WR
    PFR_R -.->|"references"| OPR
    PFR_B -.->|"references"| WR

    %% Workforce
    WFR -->|"assigns agents"| WR
    ESR -.->|"stakeholder refs"| PFR_W

    %% Memory
    PIR & DKB & DAR & POR & CAR & QVS & OPR & PFR_W & WR & PPR & WFR & ESR -.->|"lineage"| PEIR

    %% Styling
    classDef strategy fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef engineering fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef operations fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef feedback fill:#fce4ec,stroke:#c62828,stroke-width:2px;
    classDef foundation fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;

    class PIR,DKB strategy;
    class DAR,POR,CAR,QVS engineering;
    class OPR operations;
    class PFR_W,PFR_R,PFR_B feedback;
    class WR,PPR,WFR,ESR,PEIR foundation;
```

---
