# Three-Domain Entity Relationship Diagram

```mermaid
graph LR
    subgraph BANK["Bank Domain (Tachyon)"]
        AH[Account Holder<br/><i>LAH · RAH · HAH</i>]
        CF[Credit Facility]
        LH[Limit Hierarchy]
        AP[Account Product]
        VCP[Virtual Card Product]
        VBO[VBO]
        ACCT[Account]
        VC[Virtual Card]
        TKN[Token]
        BSP[Spend Program<br/><i>bank-enforced</i>]
        PC[Posting Category]
    end

    subgraph ESP["ESP Domain (Electron)"]
        ESPE[ESP]
        EAV[ESP Account<br/>Variant]
        EVCV[ESP Virtual Card<br/>Variant]
        CPP[Corporate Payment<br/>Product]
        CC[Client Contract]
    end

    subgraph CORP["Corporate Domain (Electron Portal)"]
        OU[Organizational Unit]
        PRG[Corporate Payment<br/>Program]
        BDG[Budget Hierarchy]
        SP[Spend Program<br/><i>corporate-defined</i>]
        PCAT[Purchase Category]
        BP[Booking Profile]
        STLP[Settlement Profile]
        SA[Settlement Account]
        MBR[Member]
        ENR[Enrollment]
    end

    %% Within Bank
    AH -->|1 : N per currency| CF
    CF -->|0..1 : N may anchor| LH
    LH -->|self-referencing<br/>hierarchy| LH
    PC -->|identifies| BSP
    BSP -.->|0..1 may refer to| LH
    BSP -->|N : 1| ACCT
    BSP -->|N : 1| VC
    BSP -->|N : 1| TKN
    VC -->|linked 1:1<br/>at creation| ACCT
    VC -->|1 : N| TKN

    %% Bank ↔ ESP
    ESPE -.->|registered as| VBO
    VBO -.->|accesses catalog| AP
    VBO -.->|accesses catalog| VCP
    AP -->|1 : N customized as| EAV
    VCP -->|1 : N customized as| EVCV

    %% Within ESP
    EAV -->|1 : 1| CPP
    EVCV -->|1 : 1| CPP
    CC -->|1 : N governs| CPP

    %% ESP → Corporate
    CPP -->|1 : N instantiated as| PRG

    %% Within Corporate
    BDG -->|self-referencing<br/>hierarchy| BDG
    OU -->|1 : N accessible to| BDG
    OU -->|N : N organizes| PRG
    PRG -->|1 : N from OU's budgets| BDG
    PCAT -->|identifies| SP
    PRG -->|1 : N program-level| SP
    PRG -->|1 : 1| BP
    PRG -->|1 : 1| STLP
    STLP -->|refers to| SA
    PRG -->|1 : N contains| ENR
    ENR -->|N : 1 enrolls| MBR
    ENR -->|1 : N enrollment-level| SP
    ENR -->|1 : N provisions| VC
    PRG -->|1 : N creates| ACCT

    %% Budget detail
    BDG -->|1 : 1 overall<br/>program spend| PRG
    SP -.->|0..1 optional<br/>budget per policy| BDG

    %% Cross-domain mappings
    BDG -.->|optionally<br/>translated to| LH
    SP -.->|maps to| BSP
    PCAT -.->|maps to| PC
```

## Cardinality Notes

**Budget accessibility and assignment:**
- Budgets are hierarchical (mirroring Limit Hierarchy in Bank Domain)
- Budgets are made accessible to OUs
- A Program can only be assigned budgets that belong to the OU it is associated with

**Budget structure per Program:**
- One overall program spend budget (shared across all accounts)
- Optionally, one budget per Spend Program

**Spend Program cascade:**
- Program-level: applies to all enrollments in the program
- Enrollment-level: applies to all virtual cards provisioned for that enrollment
  - Enrollment-level Spend Programs translate to per-Virtual Card Spend Programs in Bank Domain
  - Token-specific rules: expressed as enrollment-level Spend Program with additional token-identifying rule; translates to per-Token Spend Program in Bank Domain

**Token:**
- A Virtual Card can have multiple Tokens
- Spend Programs can be associated with Token (bank-enforced), manifesting from enrollment-level Spend Program with token-specific rules in Corporate Domain

**Purchase Category / Posting Category:**
- Bank provides a set of pre-defined Purchase Categories accessible to corporates
- Corporate and ESP can define additional Purchase Categories using a data dictionary provided by the bank
- Purchase Category (Corporate Domain) maps to Posting Category (Bank Domain) — the bank's grammar may include dimensions not available at the corporate level (e.g., authentication method, authenticating parties)
- At authorization, Posting Category identifies which bank-enforced Spend Programs apply to a transaction
- Each Spend Program has a numeric precedence set by the corporate admin; for booking-limit Spend Programs, highest precedence wins

**Spend Program budget and limit evaluation:**
- Every Spend Program must be associated with a Budget derived from the Credit Facility (bank credit risk protection)
- A Spend Program can additionally reference Spend Program Budgets or static limits for corporate policy enforcement
- For Spend Programs tied to ERP-imported Budgets, the Spend Program can designate that budget as the booking destination (booking-limit Spend Program)
- During authorization, only one booking-limit Spend Program applies per posting (highest precedence wins)
- Non-booking-limit Spend Programs are concurrent usage gates — all applicable ones evaluated together
- Hard constraint: per posting, no more than 3 non-booking, non-CF external limits evaluated; exceeding this declines the transaction (up to 5 limit ledgers updated per posting, excluding ancestor traversal)
