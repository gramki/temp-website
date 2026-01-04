# Bank Technology Decision Makers by Segment: Buyers & Appetite Analysis

This document profiles key technology decision makers organized by bank segment, recognizing that organizational structures, roles, and buying patterns vary significantly across different types and sizes of financial institutions.

---

# Segment Overview

| Segment | Asset Range | # of Institutions (US) | Annual Tech Spend | IT Staff Size |
|---------|-------------|------------------------|-------------------|---------------|
| Money Center / Global | >$1T | 4-6 | $10B - $15B+ | 30,000 - 60,000+ |
| Super Regional | $100B - $1T | 15-20 | $1B - $5B | 5,000 - 20,000 |
| Regional | $10B - $100B | 100-150 | $100M - $1B | 500 - 5,000 |
| Community | $1B - $10B | ~700 | $10M - $100M | 50 - 500 |
| Small Community | <$1B | ~4,000 | $1M - $10M | 5 - 50 |
| Credit Unions | $500M - $50B+ | ~5,000 | $2M - $200M | 10 - 1,000 |
| Digital Banks / Neobanks | Varies | 50-100 | $20M - $500M | 50 - 1,000 |
| BaaS / Embedded Finance | N/A | 20-50 | $10M - $200M | 100 - 1,500 |

---

# 1. Money Center / Global Banks

**Examples:** JPMorgan Chase, Bank of America, Citibank, Wells Fargo, Goldman Sachs

**Characteristics:**
- Highly matrixed organization with specialized roles
- Dedicated technology units (sometimes separate subsidiaries)
- Build vs. buy preference (often build custom)
- Long procurement cycles (12-36 months)
- Enterprise-wide standards and architecture review boards

## Key Decision Makers

### CIO / Group CIO
**Typical Title:** Chief Information Officer, Group Head of Technology  
**Reports To:** CEO  
**Team Size:** 5,000 - 30,000+  
**Annual Budget:** $5B - $12B

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Cloud Infrastructure | AWS, Azure, GCP, Private Cloud | 5-7 year strategic deals | $500M - $2B/year |
| Enterprise Cybersecurity | CrowdStrike, Palo Alto, Splunk, Tanium | 3-5 years | $100M - $500M/year |
| Mainframe Infrastructure | IBM, Kyndryl, BMC | 5-10 years | $200M - $800M/year |
| Enterprise Data Platform | Snowflake, Databricks, Cloudera | 3-5 years | $50M - $300M/year |
| DevOps/Platform Engineering | GitHub Enterprise, GitLab, Backstage | 2-3 years | $20M - $100M/year |
| API Gateway/Management | Apigee, MuleSoft, Kong, AWS API Gateway | 3-5 years | $20M - $80M/year |
| IT Service Management | ServiceNow, BMC Helix | 3-5 years | $30M - $100M/year |
| Identity & Access Management | SailPoint, Okta, CyberArk, Ping | 3-5 years | $30M - $100M/year |
| Observability/APM | Datadog, Dynatrace, Splunk | 2-3 years | $20M - $80M/year |
| Enterprise Integration | IBM, MuleSoft, TIBCO | 5-7 years | $50M - $200M |
| Disaster Recovery/BCP | IBM, Kyndryl, Zerto | 5-7 years | $50M - $200M |
| Consulting/SI Partners | Accenture, Deloitte, TCS, Infosys | Annual | $200M - $1B+/year |

**Buying Behavior:** Highly selective; prefers proven enterprise vendors. Heavy POC/pilot requirements. Often negotiates custom SLAs.

---

### CTO / Chief Technology Officer
**Typical Title:** Chief Technology Officer, Head of Engineering  
**Reports To:** CIO or CEO  
**Team Size:** 2,000 - 10,000  
**Annual Budget:** $500M - $2B (engineering/innovation)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| AI/ML Platform | AWS SageMaker, Google Vertex, Databricks, Azure ML | 2-3 years | $30M - $150M/year |
| LLM/GenAI Infrastructure | OpenAI, Anthropic, Cohere, AWS Bedrock | Annual | $10M - $100M/year |
| Container/Kubernetes | Red Hat OpenShift, Rancher, EKS, GKE | 2-3 years | $20M - $80M/year |
| Event Streaming | Confluent Kafka, AWS Kinesis, Pulsar | 3-5 years | $15M - $60M/year |
| Graph Database | Neo4j, TigerGraph, AWS Neptune | 3-5 years | $5M - $30M |
| Low-Code Platforms | Appian, Pega, OutSystems | 3-5 years | $10M - $50M/year |
| Developer Experience | Backstage, Port, Humanitec, Spotify plugins | 2-3 years | $5M - $25M/year |
| Code Security/SAST | Snyk, Veracode, Checkmarx, SonarQube | 2-3 years | $10M - $50M/year |
| Feature Flagging | LaunchDarkly, Split, Optimizely | Annual-2 years | $2M - $10M/year |
| Blockchain/DLT | R3 Corda, ConsenSys, Hyperledger | Project-based | $10M - $100M |
| Quantum Computing R&D | IBM Quantum, Google, IonQ | Project-based | $5M - $50M/year |
| Innovation Labs/Sandbox | AWS/Azure/GCP sandbox accounts | Annual | $10M - $50M/year |

**Buying Behavior:** Tech-forward; willing to pilot emerging tech. Runs innovation labs. Heavy internal build culture but looks for accelerators.

---

### CDO / Chief Digital Officer
**Typical Title:** Chief Digital Officer, Head of Digital Banking  
**Reports To:** CEO or Consumer Banking Head  
**Team Size:** 500 - 3,000  
**Annual Budget:** $300M - $1.5B

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Digital Banking Platform | Usually custom-built, some Backbase, Temenos | 7-10 years | $100M - $500M |
| Mobile Banking Framework | Custom (React Native, Flutter), Kony | 3-5 years | $30M - $150M |
| Personalization Engine | Adobe Target, Salesforce, Dynamic Yield | 2-3 years | $20M - $80M/year |
| Customer Experience (CX) | Medallia, Qualtrics, InMoment | 2-3 years | $10M - $50M/year |
| Conversational AI | Custom, Kasisto, Google CCAI, Amazon Lex | 2-3 years | $20M - $80M/year |
| Digital Onboarding | Jumio, Onfido, Alloy, custom | 2-3 years | $15M - $60M/year |
| Omnichannel Orchestration | Custom, Pega CDH, Salesforce | 3-5 years | $20M - $100M |
| A/B Testing/Experimentation | Optimizely, custom, Split | 2-3 years | $5M - $25M/year |
| UX Research/Analytics | UserTesting, FullStory, Quantum Metric | Annual-2 years | $3M - $15M/year |
| Video Banking | Glia, Pexip, custom | 2-3 years | $5M - $25M |
| Digital Wallet | Custom, Apple/Google integration | 3-5 years | $20M - $100M |
| Voice/Biometrics | Nuance, Pindrop, Daon | 3-5 years | $10M - $50M |

**Buying Behavior:** Focused on customer experience differentiation. Heavy on custom builds with vendor components. Rapid iteration mindset.

---

### Chief Data Officer / Chief Analytics Officer
**Typical Title:** Chief Data Officer, Chief Analytics Officer, Head of Enterprise Data  
**Reports To:** CIO, CFO, or CEO  
**Team Size:** 500 - 2,500  
**Annual Budget:** $200M - $800M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Data Governance Platform | Collibra, Alation, Informatica | 3-5 years | $20M - $80M |
| Enterprise BI/Visualization | Tableau, Power BI, Looker, ThoughtSpot | 2-3 years | $15M - $60M/year |
| Data Catalog/Discovery | Atlan, Alation, AWS Glue, custom | 2-3 years | $5M - $30M/year |
| Master Data Management | Informatica MDM, Reltio, Stibo | 5-7 years | $30M - $120M |
| Data Quality | Informatica DQ, Talend, Monte Carlo | 2-3 years | $10M - $50M/year |
| Customer Data Platform | Segment, Tealium, Treasure Data | 2-3 years | $10M - $50M/year |
| Real-Time Analytics | Druid, ClickHouse, Rockset, custom | 2-3 years | $10M - $40M/year |
| Data Privacy/Compliance | BigID, OneTrust, Privacera | 2-3 years | $10M - $40M/year |
| ML Feature Store | Tecton, Feast, Databricks Feature Store | 2-3 years | $5M - $25M/year |
| ETL/Data Integration | Fivetran, dbt, Informatica, Matillion | 2-3 years | $10M - $50M/year |
| Data Marketplace | Snowflake Marketplace, custom | Annual | $5M - $25M/year |
| Graph Analytics | Neo4j, TigerGraph | 3-5 years | $5M - $25M |

**Buying Behavior:** Heavily invested in enterprise-wide data strategy. Regulatory pressure (BCBS 239) drives urgency. AI/ML demand accelerating investments.

---

### CRO / Chief Risk Officer
**Typical Title:** Chief Risk Officer, Head of Enterprise Risk  
**Reports To:** CEO and Board Risk Committee  
**Team Size:** 1,000 - 5,000  
**Annual Budget:** $300M - $1B

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Enterprise Risk Management | SAS Risk, Moody's Analytics, Archer | 5-7 years | $50M - $200M |
| Credit Risk Platform | FICO, Moody's, S&P Global, custom | 5-7 years | $50M - $200M |
| Anti-Money Laundering | NICE Actimize, Featurespace, Quantexa | 3-5 years | $50M - $200M |
| Fraud Detection | Feedzai, BioCatch, FICO Falcon, LexisNexis | 2-3 years | $30M - $120M/year |
| Stress Testing/CCAR | Moody's, S&P Global, custom | 3-5 years | $20M - $80M/year |
| Model Risk Management | Custom, SAS, CRISIL | 3-5 years | $10M - $50M |
| Sanctions Screening | Dow Jones, Refinitiv, LexisNexis | Annual-2 years | $15M - $60M/year |
| Transaction Monitoring | Actimize, SAS, Featurespace | 3-5 years | $30M - $120M |
| KYC/Identity Verification | Trulioo, LexisNexis, Refinitiv | 2-3 years | $15M - $60M/year |
| RegTech Reporting | AxiomSL, Wolters Kluwer, Vermeg | 3-5 years | $20M - $80M |
| Third-Party Risk | Prevalent, ProcessUnity, Aravo | 2-3 years | $5M - $25M/year |
| Climate Risk | Moody's, MSCI, custom | 2-3 years | $10M - $40M |

**Buying Behavior:** Budget is resilient—regulatory mandates drive spending. Requires extensive vendor due diligence. Prefers proven, auditable solutions.

---

### Other Key Buyers at Money Center Banks

| Role | Focus Area | Top Software Categories | Annual Budget |
|------|-----------|------------------------|---------------|
| **CFO** | Finance transformation, Treasury | Oracle/SAP Financials, Kyriba, Anaplan, BlackLine | $100M - $400M |
| **CMO** | Brand, acquisition, martech | Salesforce, Adobe, Braze, The Trade Desk | $200M - $800M |
| **COO** | Operations, automation | UiPath, Pega, ABBYY, nCino, Genesys | $300M - $1B |
| **CHRO** | Talent, employee experience | Workday, Cornerstone, ServiceNow HR | $50M - $200M |
| **Head of Cards/Payments** | Card issuing, payments | FIS, Fiserv, TSYS, custom builds | $200M - $800M |
| **Head of Wealth/Private Banking** | Wealth platforms | Aladdin, Temenos WealthSuite, SEI | $100M - $500M |
| **Head of Commercial Banking** | Commercial lending, treasury | nCino, Finastra, AvidXchange | $100M - $400M |
| **CISO** | Security operations | CrowdStrike, Palo Alto, Splunk, Recorded Future | $100M - $400M |

---

# 2. Super Regional Banks

**Examples:** PNC, U.S. Bank, Truist, Capital One, Fifth Third, Citizens, M&T Bank

**Characteristics:**
- Full C-suite but less matrix complexity than money centers
- Mix of build and buy (increasingly buy-focused)
- Strong vendor relationships with major providers
- Procurement cycles: 9-18 months
- Technology investment catching up to money centers

## Key Decision Makers

### CIO
**Typical Title:** Chief Information Officer, EVP Technology  
**Reports To:** CEO  
**Team Size:** 2,000 - 8,000  
**Annual Budget:** $500M - $3B

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Cloud Infrastructure | AWS, Azure, GCP | 3-5 year strategic deals | $50M - $300M/year |
| Core Banking Platform | FIS, Fiserv, Temenos, TCS BaNCS | 10-15 years | $100M - $500M |
| Cybersecurity Suite | CrowdStrike, Palo Alto, Splunk | 3-5 years | $15M - $80M/year |
| IT Service Management | ServiceNow, BMC | 3-5 years | $5M - $30M/year |
| Data Platform | Snowflake, Databricks, Cloudera | 3-5 years | $10M - $60M/year |
| API Management | Apigee, MuleSoft, Kong | 3-5 years | $3M - $20M/year |
| Identity & Access | Okta, SailPoint, CyberArk | 3-5 years | $5M - $25M/year |
| DevOps Toolchain | GitHub Enterprise, GitLab, Jenkins | 2-3 years | $2M - $15M/year |
| Disaster Recovery | Zerto, Veeam, IBM | 3-5 years | $5M - $30M |
| Enterprise Integration | MuleSoft, Boomi, IBM | 3-5 years | $5M - $30M |
| Observability | Datadog, Dynatrace, Splunk | 2-3 years | $3M - $20M/year |
| Consulting Partners | Accenture, Deloitte, TCS, Infosys | Annual | $50M - $300M/year |

**Buying Behavior:** Strategic vendor partnerships. Increasingly cloud-first. Looking to leapfrog legacy with modern platforms.

---

### CTO (if separate from CIO)
**Typical Title:** Chief Technology Officer, Head of Technology Innovation  
**Reports To:** CIO or CEO  
**Team Size:** 500 - 2,000  
**Annual Budget:** $100M - $500M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| AI/ML Platform | AWS SageMaker, Databricks, Azure ML | 2-3 years | $5M - $40M/year |
| GenAI/LLM Services | OpenAI, AWS Bedrock, Google Vertex | Annual | $2M - $25M/year |
| Low-Code/No-Code | Appian, OutSystems, Mendix | 3-5 years | $2M - $15M/year |
| Container Platform | Red Hat OpenShift, EKS, AKS | 2-3 years | $2M - $15M/year |
| Event Streaming | Confluent Kafka, AWS MSK | 3-5 years | $2M - $12M/year |
| Developer Experience | Backstage, GitHub, GitLab | 2-3 years | $1M - $8M/year |
| Code Security | Snyk, SonarQube, Veracode | 2-3 years | $1M - $10M/year |
| Feature Management | LaunchDarkly, Split | Annual-2 years | $500K - $3M/year |
| Graph Database | Neo4j, AWS Neptune | 3-5 years | $1M - $8M |
| Innovation Lab Tools | AWS/Azure sandbox environments | Annual | $2M - $15M/year |
| Modern Databases | MongoDB, CockroachDB | 3-5 years | $2M - $15M/year |
| Blockchain POC | R3 Corda, Hyperledger | Project-based | $1M - $10M |

**Buying Behavior:** Eager to adopt modern tech. Innovation-focused but budget-conscious. Pilots are standard before enterprise rollout.

---

### Head of Digital Banking / CDO
**Typical Title:** Chief Digital Officer, EVP Digital Banking, Head of Digital Experience  
**Reports To:** CEO, Consumer Banking Head  
**Team Size:** 200 - 1,000  
**Annual Budget:** $50M - $300M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Digital Banking Platform | Backbase, Q2, Temenos Infinity, NCR Digital | 5-7 years | $20M - $100M |
| Mobile Banking SDK | Q2, Backbase, NCR, custom | 3-5 years | $5M - $30M |
| Personalization Engine | Salesforce, Adobe Target, Dynamic Yield | 2-3 years | $3M - $20M/year |
| Conversational AI/Chatbot | Kasisto, Google CCAI, Clinc | 2-3 years | $2M - $15M/year |
| Digital Onboarding | Alloy, Jumio, Onfido | 2-3 years | $2M - $12M/year |
| Customer Experience | Medallia, Qualtrics | 2-3 years | $1M - $10M/year |
| Video Banking | Glia, POPio, Ameyo | 2-3 years | $1M - $8M/year |
| A/B Testing | Optimizely, VWO | Annual-2 years | $500K - $3M/year |
| UX Analytics | FullStory, Quantum Metric, Heap | Annual-2 years | $500K - $4M/year |
| Omnichannel Orchestration | Twilio, Braze, Salesforce | 2-3 years | $3M - $20M/year |
| Digital Wallet | Apple/Google integration, custom | 3-5 years | $3M - $20M |
| Voice/Biometrics | Nuance, Pindrop | 3-5 years | $2M - $12M |

**Buying Behavior:** Strong appetite for vendor solutions. Digital experience is top competitive priority. Looking for rapid deployment.

---

### CRO / Chief Risk Officer
**Typical Title:** Chief Risk Officer, EVP Risk Management  
**Reports To:** CEO, Board Risk Committee  
**Team Size:** 300 - 1,500  
**Annual Budget:** $50M - $250M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Enterprise Risk | SAS Risk, Moody's Analytics, Archer | 5-7 years | $10M - $50M |
| Credit Risk | FICO, Experian PowerCurve, Zest AI | 3-5 years | $5M - $40M |
| Anti-Money Laundering | Actimize, Featurespace, Verafin | 3-5 years | $8M - $50M |
| Fraud Detection | Feedzai, BioCatch, FICO Falcon | 2-3 years | $5M - $30M/year |
| KYC/Identity | Trulioo, LexisNexis, Onfido | 2-3 years | $2M - $15M/year |
| Transaction Monitoring | Actimize, SAS, Napier | 3-5 years | $5M - $30M |
| Sanctions Screening | Dow Jones, Refinitiv | Annual-2 years | $2M - $12M/year |
| RegTech Reporting | AxiomSL, Wolters Kluwer | 3-5 years | $3M - $20M |
| Model Risk Management | SAS, CRISIL | 3-5 years | $2M - $12M |
| Third-Party Risk | Prevalent, ProcessUnity | 2-3 years | $1M - $6M/year |
| Stress Testing | Moody's, S&P Global | 3-5 years | $3M - $18M/year |
| Climate/ESG Risk | Moody's, MSCI | 2-3 years | $1M - $8M |

**Buying Behavior:** Regulatory-driven. Budget stable. Prefers integrated suites over point solutions.

---

### Other Key Buyers at Super Regional Banks

| Role | Focus Area | Top Software Categories | Annual Budget |
|------|-----------|------------------------|---------------|
| **CFO** | Finance, Treasury | Kyriba, Anaplan, BlackLine, Oracle/SAP | $20M - $100M |
| **CMO** | Marketing, Acquisition | Salesforce Marketing Cloud, Adobe, Braze | $30M - $150M |
| **COO** | Operations, Automation | UiPath, Pega, nCino, Genesys | $40M - $200M |
| **Chief Data Officer** | Data, Analytics | Collibra, Tableau, Informatica | $30M - $150M |
| **Head of Cards/Payments** | Cards, Payments | FIS, Fiserv, Zeta, Marqeta | $30M - $150M |
| **Head of Wealth** | Wealth Management | Orion, eMoney, Envestnet, SEI | $20M - $100M |
| **Head of Commercial** | Commercial Banking | nCino, Finastra | $20M - $100M |
| **CISO** | Security | CrowdStrike, Palo Alto, Recorded Future | $20M - $80M |

---

# 3. Regional Banks

**Examples:** Huntington, Regions, KeyBank, Zions, Comerica, First Horizon, Synovus

**Characteristics:**
- Leaner C-suite; roles often combined
- Predominantly buy (limited custom development)
- Partner heavily with core providers (FIS, Fiserv, Jack Henry)
- Procurement cycles: 6-12 months
- Cost-conscious but investing in digital

## Key Decision Makers

### CIO (Often combined CIO/CTO)
**Typical Title:** Chief Information Officer, SVP Technology, EVP IT  
**Reports To:** CEO or COO  
**Team Size:** 200 - 1,500  
**Annual Budget:** $100M - $600M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Core Banking Platform | FIS, Fiserv, Jack Henry, Temenos | 10-15 years | $30M - $150M |
| Cloud Infrastructure | AWS, Azure (often via core provider) | 3-5 years | $5M - $40M/year |
| Cybersecurity | CrowdStrike, SentinelOne, Palo Alto | 3-5 years | $3M - $20M/year |
| IT Service Management | ServiceNow, Freshservice | 3-5 years | $500K - $5M/year |
| Data Platform/Warehouse | Snowflake, AWS Redshift, Databricks | 3-5 years | $2M - $15M/year |
| API Management | Kong, Apigee, core provider APIs | 3-5 years | $500K - $5M/year |
| Identity & Access | Okta, SailPoint | 3-5 years | $1M - $8M/year |
| Disaster Recovery | Zerto, Veeam, cloud-based | 3-5 years | $1M - $8M |
| DevOps Tools | GitHub, GitLab, Azure DevOps | 2-3 years | $200K - $2M/year |
| Endpoint Management | Microsoft Intune, VMware Workspace ONE | 3-5 years | $500K - $4M/year |
| Network/Infrastructure | Cisco, Arista, VMware | 5-7 years | $5M - $30M |
| Managed Services | Cognizant, TCS, Wipro | Annual | $10M - $80M/year |

**Buying Behavior:** Core provider ecosystem is central. Cloud adoption accelerating. Looking for integrated, lower-TCO solutions.

---

### Head of Digital / VP Digital Banking
**Typical Title:** SVP Digital Banking, VP Digital Channels, Head of Digital Experience  
**Reports To:** CIO, CMO, or Consumer Banking Head  
**Team Size:** 20 - 150  
**Annual Budget:** $10M - $80M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Digital Banking Platform | Q2, NCR Digital Banking, Alkami | 5-7 years | $5M - $40M |
| Mobile Banking | Q2, NCR, Alkami (via core) | 3-5 years | $2M - $15M |
| Digital Onboarding | Alloy, Mantl, core provider add-ons | 2-3 years | $500K - $5M/year |
| Chatbot/Virtual Assistant | Kasisto, Clinc, core provider bots | 2-3 years | $300K - $3M/year |
| Personalization | Personetics, MX, core add-ons | 2-3 years | $500K - $4M/year |
| Customer Experience | Medallia, Qualtrics | 2-3 years | $300K - $2M/year |
| A/B Testing | Optimizely, VWO | Annual-2 years | $100K - $800K/year |
| Video Banking | Glia, POPio | 2-3 years | $200K - $2M/year |
| PFM/Money Management | MX, Personetics, Yodlee | 2-3 years | $500K - $4M/year |
| Digital Account Opening | Mantl, Narmi, core providers | 2-3 years | $500K - $4M |
| Push Notifications | Braze, OneSignal, core add-ons | Annual-2 years | $100K - $1M/year |
| Digital Marketing | Salesforce, HubSpot | 2-3 years | $500K - $4M/year |

**Buying Behavior:** Relies heavily on core provider digital suites. Increasingly open to fintech partnerships. Speed to market is priority.

---

### CFO (Often oversees technology spend approval)
**Typical Title:** Chief Financial Officer, EVP Finance  
**Reports To:** CEO  
**Team Size:** 50 - 300  
**Annual Budget:** $5M - $40M (finance technology)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| ERP/Financials | Oracle, SAP, Workday Financials | 7-10 years | $3M - $20M |
| FP&A/Planning | Anaplan, Workday Adaptive, Planful | 3-5 years | $300K - $3M/year |
| Treasury Management | Kyriba, GTreasury, FIS | 5-7 years | $500K - $5M |
| Expense Management | Concur, Expensify | 2-3 years | $100K - $1M/year |
| Financial Close | BlackLine, FloQast | 3-5 years | $200K - $2M/year |
| AP Automation | Coupa, AvidXchange, Tipalti | 3-5 years | $200K - $2M |
| Contract Management | Icertis, DocuSign CLM | 3-5 years | $100K - $1M |
| Tax Management | Thomson Reuters, Vertex | 3-5 years | $100K - $800K/year |
| Reporting/Consolidation | OneStream, Workiva | 3-5 years | $200K - $2M/year |
| Cost Management | Apptio, CloudZero | 2-3 years | $100K - $800K/year |
| Vendor Management | Coupa, SAP Ariba | 3-5 years | $200K - $2M |
| Audit Management | AuditBoard, Workiva | 3-5 years | $100K - $800K/year |

**Buying Behavior:** TCO-focused. Approves major tech investments. Values demonstrable ROI and cost reduction.

---

### CRO / Head of Risk
**Typical Title:** Chief Risk Officer, SVP Risk, Chief Credit Officer  
**Reports To:** CEO, Board  
**Team Size:** 100 - 500  
**Annual Budget:** $15M - $80M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Credit Risk/Decisioning | FICO, Experian PowerCurve, Zest AI | 3-5 years | $2M - $15M |
| AML/BSA | Verafin (now Nasdaq), Actimize, Abrigo | 3-5 years | $2M - $15M |
| Fraud Detection | Feedzai, FICO Falcon, core provider | 2-3 years | $1M - $10M/year |
| KYC/Identity | Trulioo, LexisNexis, Alloy | 2-3 years | $500K - $4M/year |
| Enterprise Risk | Archer, LogicManager | 5-7 years | $500K - $4M |
| Compliance Management | NICE Actimize, core providers | 3-5 years | $1M - $8M |
| Sanctions Screening | Dow Jones, Refinitiv | Annual-2 years | $300K - $2M/year |
| Loan Review/Stress Test | Moody's, S&P, Abrigo | 3-5 years | $500K - $4M/year |
| Vendor Risk | Prevalent, ProcessUnity | 2-3 years | $100K - $1M/year |
| Document/Audit Trail | OpenText, Box | 3-5 years | $200K - $2M |
| RegTech Reporting | Wolters Kluwer, AxiomSL | 3-5 years | $500K - $3M |
| GRC Platform | ServiceNow GRC, MetricStream | 3-5 years | $500K - $4M |

**Buying Behavior:** Regulatory-driven. Strong preference for proven solutions. Abrigo and Verafin are popular all-in-one choices.

---

### Other Key Buyers at Regional Banks

| Role | Focus Area | Top Software Categories | Annual Budget |
|------|-----------|------------------------|---------------|
| **CMO** | Marketing | Salesforce, HubSpot, Braze | $5M - $30M |
| **COO** | Operations | nCino, UiPath, ABBYY | $10M - $60M |
| **Head of Retail Banking** | Branch, Retail | NCR, Diebold Nixdorf, Verint | $10M - $50M |
| **Head of Cards** | Cards | FIS, Fiserv, via core provider | $5M - $30M |
| **Head of Lending** | Mortgage, Consumer | Blend, Encompass, nCino | $10M - $50M |
| **Head of Commercial** | Commercial Banking | nCino, Finastra, AvidXchange | $5M - $30M |
| **Head of HR** | HRIS, Talent | Workday, ADP, UKG | $3M - $15M |

---

# 4. Community Banks ($1B - $10B Assets)

**Examples:** Glacier Bancorp, Banner Bank, Columbia Banking System, Independent Bank Group

**Characteristics:**
- Smaller executive teams; roles often combined
- 100% buy approach; no custom development
- Heavy reliance on core provider (FIS, Fiserv, Jack Henry)
- Procurement cycles: 3-9 months
- Budget-constrained but modernizing

## Key Decision Makers

### President/CEO (Often involved in major tech decisions)
**Typical Title:** President & CEO  
**Direct Reports:** CFO, COO, CIO (if exists)  
**Approval Threshold:** $50K+ purchases

**Buying Behavior:** Personally involved in major platform decisions. Values relationships with vendors. Community impact considerations.

---

### CIO / IT Director (Sometimes combined with COO)
**Typical Title:** CIO, VP Technology, IT Director, SVP Operations & Technology  
**Reports To:** CEO or COO  
**Team Size:** 10 - 80  
**Annual Budget:** $10M - $60M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Core Banking Platform | Jack Henry, Fiserv, FIS | 10-15 years | $5M - $40M |
| Digital Banking Platform | Q2, Alkami, NCR, core provider | 5-7 years | $1M - $10M |
| Cybersecurity | CrowdStrike, SentinelOne, managed service | 2-3 years | $200K - $2M/year |
| Cloud/Infrastructure | AWS, Azure (via core), managed hosting | 3-5 years | $500K - $4M/year |
| IT Service Desk | Freshservice, Zendesk, ConnectWise | 2-3 years | $50K - $300K/year |
| Backup/DR | Veeam, Datto, cloud backup | 2-3 years | $100K - $800K |
| Email/Productivity | Microsoft 365, Google Workspace | Annual | $100K - $500K/year |
| Endpoint Security | CrowdStrike, Carbon Black | 2-3 years | $100K - $600K/year |
| Network Management | Cisco Meraki, Fortinet | 3-5 years | $200K - $1.5M |
| Patch/Vulnerability Mgmt | Qualys, Tenable, managed | 2-3 years | $50K - $300K/year |
| Help Desk/Remote Support | ConnectWise, TeamViewer | Annual-2 years | $30K - $150K/year |
| Managed IT Services | CSI, Lumen, regional MSPs | Annual | $500K - $5M/year |

**Buying Behavior:** Core provider is the hub. Limited IT staff means managed services are common. Values simplicity and support.

---

### CFO (Major financial/technology decision maker)
**Typical Title:** Chief Financial Officer, EVP Finance, SVP Finance  
**Reports To:** CEO  
**Team Size:** 20 - 100  
**Annual Budget:** $2M - $15M (finance technology)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| General Ledger/Accounting | FIS/Fiserv (via core), Sage | 7-10 years | $200K - $2M |
| FP&A/Budgeting | Planful, Prophix, Excel-based | 3-5 years | $50K - $400K/year |
| AP Automation | AvidXchange, Bill.com, Stampli | 2-3 years | $50K - $300K/year |
| Expense Management | Concur, Expensify, Certify | 2-3 years | $20K - $100K/year |
| Financial Reporting | Wolters Kluwer, Jack Henry | 3-5 years | $50K - $400K/year |
| Loan Accounting | Baker Hill, Abrigo, core add-on | 5-7 years | $100K - $800K |
| Board Reporting | Diligent, BoardEffect | 2-3 years | $30K - $150K/year |
| Tax Preparation | Thomson Reuters, CCH | Annual-2 years | $30K - $150K/year |
| Audit Support | CaseWare, TeamMate | 2-3 years | $30K - $150K/year |
| Treasury/ALM | Empyrean, ZM Financial, QwickRate | 3-5 years | $50K - $400K/year |
| CECL/Allowance | Abrigo, MST, Moody's | 3-5 years | $50K - $400K/year |
| Vendor Management | Venminder, Ncontracts | 2-3 years | $30K - $150K/year |

**Buying Behavior:** Approves all significant tech spend. ROI and cost savings are key. Prefers bundled solutions from core provider.

---

### COO / Head of Operations (Often owns technology and risk)
**Typical Title:** Chief Operating Officer, EVP Operations, SVP Ops  
**Reports To:** CEO  
**Team Size:** 100 - 500  
**Annual Budget:** $5M - $30M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Loan Origination System | Abrigo, Baker Hill, Finastra (LaserPro) | 5-7 years | $200K - $2M |
| Document Management | Laserfiche, DocuWare, Hyland | 5-7 years | $100K - $800K |
| Workflow/BPM | Laserfiche, ProcessMaker | 3-5 years | $50K - $400K |
| eSignature | DocuSign, Adobe Sign | 2-3 years | $30K - $200K/year |
| Check/Item Processing | Core provider, NCR | 5-7 years | $100K - $1M |
| Call Center/IVR | Talkdesk, Five9, RingCentral | 3-5 years | $100K - $800K/year |
| Queue Management | Qmatic, QLess | 5-7 years | $50K - $300K |
| Branch Capture | NCR, Digital Check, Panini | 5-7 years | $100K - $600K |
| Courier/Cash Management | Loomis, Brinks, Dunbar | Annual | $200K - $1M/year |
| Training/LMS | BVS, FIS/Fiserv training | Annual-2 years | $30K - $200K/year |
| Process Mining | Limited adoption | - | - |
| RPA | UiPath (limited), manual processes | 3-5 years | $50K - $300K |

**Buying Behavior:** Focused on operational efficiency. Paper-to-digital transformation is ongoing. Cautious on automation investments.

---

### Chief Credit Officer / CRO (Often combined role)
**Typical Title:** Chief Credit Officer, SVP Lending, Chief Risk Officer  
**Reports To:** CEO  
**Team Size:** 20 - 100  
**Annual Budget:** $3M - $20M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Credit Analysis/Spreading | Moody's, Abrigo, Sageworks | 3-5 years | $100K - $800K/year |
| Loan Review | Abrigo, CRA Wiz, core add-ons | 3-5 years | $50K - $400K/year |
| AML/BSA | Verafin, Abrigo, core provider | 3-5 years | $200K - $2M |
| Fraud Detection | Fiserv/FIS/JH add-ons, NICE Actimize | 2-3 years | $100K - $800K/year |
| KYC/CIP | LexisNexis, core provider | 2-3 years | $50K - $400K/year |
| Compliance Management | Ncontracts, Banker's Toolbox, Wolters Kluwer | 2-3 years | $50K - $400K/year |
| CECL/Allowance | Abrigo, MST, Moody's | 3-5 years | $50K - $400K/year |
| Risk Rating | Abrigo, internal models | 3-5 years | $30K - $200K |
| CRA Management | CRA Wiz, QuestSoft | 2-3 years | $30K - $200K/year |
| Vendor Management | Venminder, Ncontracts | 2-3 years | $30K - $150K/year |
| Policy Management | PolicyStat, Ncontracts | 3-5 years | $20K - $100K/year |
| Exam Management | Continuity, internal | 3-5 years | $20K - $100K |

**Buying Behavior:** Regulatory compliance drives most purchases. Abrigo, Ncontracts, and Verafin are popular integrated options.

---

# 5. Small Community Banks (<$1B Assets)

**Examples:** Thousands of local community banks across the US

**Characteristics:**
- Very small teams; generalist roles
- 100% buy; completely dependent on core provider
- Limited IT resources; often outsourced
- Procurement cycles: 1-6 months
- Extremely budget-sensitive

## Key Decision Makers

### President/CEO
**Typical Title:** President & CEO  
**Role in Tech:** Final approval on all significant purchases (>$10K-$25K)

| Key Purchasing Decisions | Typical Approach |
|-------------------------|-----------------|
| Core banking | 15-20 year relationships; rarely switches |
| Digital banking | Core provider add-on module |
| Major compliance tools | Bundled with core or AML provider |

---

### CFO / Controller (Often primary tech decision maker)
**Typical Title:** CFO, VP Finance, Controller  
**Reports To:** CEO  
**Team Size:** 5 - 25  
**Annual Budget:** $1M - $8M (total technology)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Core Banking | Jack Henry (Symitar, SilverLake), Fiserv, FIS | 15-20 years | $500K - $5M |
| Digital/Mobile Banking | Core provider module, Alkami, Q2 | 5-7 years | $100K - $1M |
| Internet Banking | Core provider | 5-7 years | Bundled |
| Accounting/GL | Core integrated, QuickBooks | 7-10 years | $20K - $150K |
| Budgeting | Excel, Planful (rarely) | Ongoing | $0 - $50K |
| Loan Origination | Abrigo, core module, Finastra | 5-7 years | $50K - $400K |
| AML/BSA | Verafin, Abrigo, core module | 3-5 years | $50K - $500K |
| Fraud Detection | Core provider module | 2-3 years | $20K - $200K |
| Compliance | Ncontracts, Wolters Kluwer, ICBA tools | 2-3 years | $30K - $200K |
| IT Managed Services | Jack Henry, CSI, regional MSPs | Annual | $200K - $1.5M/year |
| Cybersecurity | Managed service, SentinelOne | 2-3 years | $50K - $300K/year |
| Microsoft 365 | Microsoft | Annual | $20K - $100K/year |

**Buying Behavior:** Core provider bundle is primary approach. Values relationships and service. Trade associations (ICBA, state associations) influence.

---

### IT Manager / IT Director (If position exists)
**Typical Title:** IT Manager, IT Director, Network Administrator  
**Reports To:** CFO, COO, or CEO  
**Team Size:** 1 - 10  
**Annual Budget:** $500K - $3M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Server/Infrastructure | Dell, HPE, managed hosting | 5-7 years | $50K - $400K |
| Network Equipment | Cisco, Fortinet, Meraki | 5-7 years | $30K - $250K |
| Backup/Recovery | Veeam, Datto, Carbonite | 2-3 years | $20K - $150K |
| Antivirus/Endpoint | CrowdStrike, SentinelOne, Symantec | 2-3 years | $20K - $150K/year |
| Email Security | Proofpoint, Mimecast, Barracuda | 2-3 years | $10K - $80K/year |
| Firewall/Security | Fortinet, Palo Alto, SonicWall | 5-7 years | $20K - $150K |
| Help Desk Tools | ConnectWise, Zendesk, Freshdesk | 2-3 years | $10K - $50K/year |
| Remote Access/VPN | Cisco AnyConnect, Fortinet | 3-5 years | $10K - $60K/year |
| Patch Management | Managed, Qualys, Automox | 2-3 years | $10K - $50K/year |
| Vulnerability Scanning | Managed, Tenable | Annual | $10K - $50K/year |
| Security Awareness | KnowBe4, Proofpoint | Annual | $5K - $30K/year |
| IT Documentation | IT Glue, Hudu | Annual | $5K - $20K/year |

**Buying Behavior:** Heavily influenced by managed service provider. Limited time for vendor evaluation. Security is growing concern.

---

# 6. Credit Unions

**Examples:** Navy Federal, BECU, State Employees' CU, PenFed, Alliant

**Characteristics:**
- Member-focused; different governance (board of volunteers)
- Range from very large ($50B+) to very small (<$50M)
- Cooperative model; shared resources via CUSOs and leagues
- Heavy reliance on credit union-focused vendors (Symitar, Corelation, CUNA)
- Budget-sensitive but investing in digital

## Key Decision Makers (Large Credit Unions >$5B)

### CEO
**Typical Title:** President & CEO  
**Role:** Strategic direction; approves major investments  
**Board Involvement:** Technology committee common

---

### CIO / VP Technology
**Typical Title:** CIO, VP Information Technology, Chief Technology Officer  
**Reports To:** CEO  
**Team Size:** 50 - 500  
**Annual Budget:** $20M - $150M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Core Processing | Symitar (Jack Henry), Corelation, Fiserv | 10-15 years | $5M - $50M |
| Digital Banking | Q2, Alkami, NCR, MeridianLink | 5-7 years | $2M - $20M |
| Mobile Banking | Q2, Alkami, Narmi | 3-5 years | $1M - $10M |
| Cloud Infrastructure | AWS, Azure, Jack Henry Cloud | 3-5 years | $1M - $10M/year |
| Cybersecurity | CrowdStrike, Palo Alto, managed | 2-3 years | $500K - $5M/year |
| IT Service Management | ServiceNow, Freshservice | 3-5 years | $200K - $2M/year |
| Data Warehouse | Snowflake, AWS, core provider | 3-5 years | $500K - $5M/year |
| API/Integration | MuleSoft, core APIs, custom | 3-5 years | $300K - $3M |
| Identity & Access | Okta, Azure AD, SailPoint | 3-5 years | $200K - $2M/year |
| DevOps/CICD | GitHub, Azure DevOps | 2-3 years | $100K - $1M/year |
| Disaster Recovery | Cloud-based, Zerto | 3-5 years | $200K - $2M |
| Managed Services | Jack Henry, CSI | Annual | $2M - $15M/year |

**Buying Behavior:** Credit union-focused vendors preferred. CUSOs provide shared services. Member experience is key driver.

---

### VP Digital / Member Experience
**Typical Title:** VP Digital, VP Member Experience, Chief Digital Officer  
**Reports To:** CEO or COO  
**Team Size:** 10 - 100  
**Annual Budget:** $5M - $40M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Digital Banking Platform | Q2, Alkami, Narmi | 5-7 years | $1M - $15M |
| Mobile App | Q2, Alkami, MeridianLink | 3-5 years | $500K - $8M |
| Digital Account Opening | MeridianLink, Mantl, Narmi | 2-3 years | $200K - $3M |
| Chatbot | Kasisto, interface.ai, Glia | 2-3 years | $100K - $2M/year |
| Personalization | Personetics, MX | 2-3 years | $100K - $2M/year |
| Member CX | Medallia, Qualtrics | 2-3 years | $100K - $1M/year |
| Video Banking | Glia, POPio | 2-3 years | $50K - $800K/year |
| PFM/Financial Wellness | MX, Personetics | 2-3 years | $100K - $1.5M/year |
| Bill Pay | Fiserv CheckFree, ACI | 5-7 years | $200K - $2M |
| P2P Payments | Zelle, core integration | 3-5 years | $100K - $1M |
| Card Management App | Card Valet, core provider | 3-5 years | $50K - $500K |
| Digital Marketing | Salesforce, HubSpot | 2-3 years | $100K - $1.5M/year |

**Buying Behavior:** Member experience is paramount. Willing to invest in digital differentiation. Often early adopters of fintech partnerships.

---

### CFO / VP Finance
**Typical Title:** Chief Financial Officer, VP Finance  
**Reports To:** CEO  
**Team Size:** 20 - 100  
**Annual Budget:** $3M - $20M (finance technology)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| General Ledger | Core integrated, Oracle (large CUs) | 7-10 years | $100K - $2M |
| ALM/Interest Rate Risk | QRM, ZM Financial, Empyrean | 3-5 years | $50K - $500K/year |
| Budgeting/FP&A | Planful, Prophix, Excel | 3-5 years | $30K - $300K/year |
| CECL/Allowance | Abrigo, Visible Equity, QRM | 3-5 years | $30K - $300K |
| Financial Reporting | Wolters Kluwer, core reports | 3-5 years | $30K - $250K/year |
| AP Automation | Bill.com, AvidXchange | 2-3 years | $20K - $200K/year |
| Board Reporting | Diligent, BoardEffect | 2-3 years | $20K - $150K/year |
| Strategic Planning | Credit Union specific consultants | Project-based | $50K - $300K |
| Investment Management | Callahan, CU Strategic Planning | Annual | $20K - $150K |
| Audit/Exam Prep | CaseWare, Wolters Kluwer | Annual | $20K - $100K |
| Call Report | Wolters Kluwer, Visible Equity | Annual | $20K - $100K |
| Vendor Management | Venminder, Ncontracts | 2-3 years | $20K - $150K/year |

**Buying Behavior:** Fiscally conservative. Values proven ROI. Credit union league resources are influential.

---

### CRO / VP Risk & Compliance
**Typical Title:** Chief Risk Officer, VP Risk, Compliance Officer  
**Reports To:** CEO  
**Team Size:** 10 - 80  
**Annual Budget:** $3M - $20M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| AML/BSA | Verafin, Abrigo, core module | 3-5 years | $100K - $2M |
| Fraud Detection | Fiserv, Verafin, FICO | 2-3 years | $100K - $1.5M/year |
| Compliance Management | Ncontracts, Compli, Wolters Kluwer | 2-3 years | $30K - $300K/year |
| KYC/Identity | LexisNexis, core provider | 2-3 years | $30K - $300K/year |
| Enterprise Risk | LogicManager, Ncontracts | 3-5 years | $30K - $250K |
| Vendor Management | Venminder, Ncontracts | 2-3 years | $20K - $150K/year |
| Loan Review | Abrigo, credit union-focused | 3-5 years | $30K - $200K |
| NCUA Exam Prep | Internal, Wolters Kluwer | Annual | $20K - $100K |
| Collections | FICO, Latitude, core module | 3-5 years | $50K - $500K |
| Fair Lending | ComplianceTech, Wolters Kluwer | 2-3 years | $20K - $150K/year |
| Policy Management | Ncontracts, PolicyStat | 3-5 years | $10K - $80K/year |
| Training/Compliance | BVS, Credit Union National Association | Annual | $20K - $150K |

**Buying Behavior:** NCUA exam-focused. Credit union service organizations (CUSOs) provide shared compliance resources.

---

## Key Decision Makers (Small/Medium Credit Unions <$1B)

| Role | Typical Title | Key Software Purchases | Annual Tech Budget |
|------|--------------|----------------------|-------------------|
| **CEO** | President/CEO | Final approval; strategic decisions | Approves >$10K |
| **CFO/Controller** | CFO, VP Finance | Core, GL, compliance, most tech | $500K - $5M total |
| **IT Manager** | IT Manager, VP IT | Infrastructure, cybersecurity | $200K - $2M |
| **VP Operations** | VP/SVP Operations | Lending, workflow, branch | $300K - $2M |
| **Compliance Officer** | VP Compliance | AML, risk, regulatory tools | $100K - $500K |

**Key Vendors for Small CUs:** Symitar (Jack Henry), Corelation, Q2, Alkami, Abrigo, Verafin, Ncontracts, Venminder

---

# 7. Digital Banks / Neobanks

**Examples:** Chime, SoFi, Current, Varo, Dave, MoneyLion, Upgrade

**Characteristics:**
- Tech-native organization; engineering is core competency
- Cloud-first, API-first architecture
- Build significant components; buy commodity/compliance
- Fast procurement cycles: 2-8 weeks
- Growth-focused; willing to spend for competitive advantage

## Key Decision Makers

### CEO / Founder
**Typical Title:** CEO & Co-Founder, CEO  
**Role:** Strategic technology direction; major vendor decisions  
**Buying Behavior:** Personally involved in platform decisions. Values speed and innovation.

---

### CTO / VP Engineering
**Typical Title:** CTO, VP Engineering, Head of Engineering  
**Reports To:** CEO  
**Team Size:** 50 - 500  
**Annual Budget:** $20M - $200M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Cloud Infrastructure | AWS, GCP (primary choice) | Annual (multi-year) | $5M - $50M/year |
| Banking-as-a-Service/Core | Zeta, Galileo, Synapse, Unit | 3-5 years | $2M - $30M+/year |
| Card Issuing/Processing | Zeta, Marqeta, Galileo, i2c | 3-5 years | $1M - $20M + per-txn |
| Payment Rails | Tabapay, Plaid, Cross River | 2-3 years | $1M - $10M + per-txn |
| Fraud/Risk | Sardine, Unit21, Alloy, Socure | 2-3 years | $500K - $8M/year |
| Identity/KYC | Alloy, Plaid Identity, Socure | 2-3 years | $500K - $5M/year |
| Container/Kubernetes | GKE, EKS, self-managed K8s | 2-3 years | $500K - $5M/year |
| Observability | Datadog, Grafana, PagerDuty | Annual-2 years | $300K - $3M/year |
| CI/CD | GitHub Actions, CircleCI, GitLab | Annual | $100K - $1M/year |
| Feature Flags | LaunchDarkly, Split, Statsig | Annual | $100K - $500K/year |
| Database | PostgreSQL (RDS/Cloud SQL), MongoDB | Included in cloud | - |
| Event Streaming | Kafka (managed), AWS Kinesis | 2-3 years | $200K - $2M/year |

**Buying Behavior:** Engineering-led decisions. Values developer experience and API quality. Fast pilots; faster decisions.

---

### CPO / Head of Product
**Typical Title:** Chief Product Officer, VP Product, Head of Product  
**Reports To:** CEO  
**Team Size:** 20 - 100  
**Annual Budget:** $5M - $40M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Product Analytics | Amplitude, Mixpanel, Heap | Annual-2 years | $200K - $2M/year |
| Feature Management | LaunchDarkly, Statsig | Annual | $100K - $500K/year |
| Session Recording | FullStory, LogRocket | Annual-2 years | $100K - $800K/year |
| A/B Testing | Statsig, Optimizely, Eppo | Annual | $100K - $500K/year |
| Product Management | Linear, Productboard, Jira | Annual | $50K - $300K/year |
| Customer Feedback | Canny, UserVoice, Productboard | Annual | $30K - $200K/year |
| User Research | UserTesting, Maze | Annual | $50K - $300K/year |
| Push/In-App | Braze, Iterable, OneSignal | Annual-2 years | $200K - $2M/year |
| PFM/Insights | Plaid, MX, custom | 2-3 years | $200K - $2M/year |
| Credit Building | Credit-focused partnerships | 2-3 years | Revenue share |
| Design Tools | Figma, Framer | Annual | $30K - $200K/year |
| Roadmapping | Linear, Notion, ProductPlan | Annual | $20K - $100K/year |

**Buying Behavior:** Data-obsessed. Values rapid experimentation. Product-led growth is core strategy.

---

### Head of Risk & Compliance
**Typical Title:** Head of Risk, Chief Compliance Officer, VP Compliance  
**Reports To:** CEO  
**Team Size:** 10 - 50  
**Annual Budget:** $3M - $20M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Fraud Detection | Sardine, Unit21, Socure, Sift | 2-3 years | $500K - $5M/year |
| Identity/KYC | Alloy, Socure, Persona, Plaid Identity | 2-3 years | $500K - $5M/year |
| AML/Transaction Monitoring | Unit21, Alloy, Sardine | 2-3 years | $300K - $3M/year |
| Sanctions Screening | Alloy, ComplyAdvantage | Annual-2 years | $100K - $800K/year |
| Dispute Management | Chargebacks911, custom | 2-3 years | $100K - $800K/year |
| Compliance Workflow | Alloy, Riskified | 2-3 years | $100K - $500K/year |
| Device/Behavioral | Sardine, BioCatch | 2-3 years | $200K - $2M/year |
| Case Management | Unit21, custom | 2-3 years | $100K - $500K/year |
| Regtech Reporting | Custom, RegTech APIs | 2-3 years | $100K - $500K |
| Risk Analytics | Custom, Databricks | Ongoing | Built internal |
| Vendor Risk | Vanta, Secureframe | Annual | $50K - $200K/year |
| SOC 2/Compliance | Vanta, Secureframe, Drata | Annual | $50K - $300K/year |

**Buying Behavior:** API-first compliance tools. Values automation over manual review. Partner bank relationships are critical.

---

### CFO / Head of Finance
**Typical Title:** CFO, VP Finance, Head of Finance  
**Reports To:** CEO  
**Team Size:** 10 - 50  
**Annual Budget:** $2M - $15M (finance technology)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Accounting/GL | NetSuite, QuickBooks, Sage Intacct | 3-5 years | $100K - $1M/year |
| FP&A/Planning | Mosaic, Jirav, Cube | 2-3 years | $50K - $300K/year |
| Spend Management | Ramp, Brex, Airbase | 2-3 years | $30K - $200K + card spend |
| AP Automation | Bill.com, Ramp, Tipalti | 2-3 years | $30K - $200K/year |
| Payroll | Rippling, Gusto, Deel | 2-3 years | $50K - $500K/year |
| Cap Table | Carta, Pulley | Annual | $10K - $50K/year |
| Revenue Recognition | RevPro, Softrax, custom | 3-5 years | $50K - $300K |
| Financial Close | FloQast, Numeric | 2-3 years | $30K - $200K/year |
| Metrics/Reporting | Mosaic, custom dashboards | Ongoing | $30K - $200K |
| Bank Reconciliation | FloQast, Modern Treasury | 2-3 years | $30K - $200K/year |
| Investor Reporting | Carta, Visible | Annual | $10K - $50K/year |
| Audit | Big 4 / regional firms | Annual | $200K - $2M |

**Buying Behavior:** Modern finance stack. Values automation and real-time visibility. Growth-stage finance is distinct from bank finance.

---

### CMO / Head of Growth
**Typical Title:** CMO, VP Growth, Head of Marketing  
**Reports To:** CEO  
**Team Size:** 20 - 100  
**Annual Budget:** $20M - $150M (including paid acquisition)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Paid Acquisition | Facebook/Meta, Google, TikTok, affiliate | Ongoing | $10M - $100M+/year |
| Attribution | Appsflyer, Branch, Singular | Annual-2 years | $200K - $2M/year |
| CRM/Marketing Auto | Braze, Iterable, Customer.io | 2-3 years | $200K - $3M/year |
| Email/SMS | Braze, Iterable, Attentive | 2-3 years | $100K - $1M/year |
| Push Notifications | Braze, OneSignal | 2-3 years | $100K - $500K/year |
| Referral Program | Friendbuy, ReferralCandy, custom | 2-3 years | $50K - $500K + rewards |
| Marketing Analytics | Amplitude, Mixpanel, Looker | 2-3 years | $100K - $500K/year |
| Influencer Platform | Impact, Grin | Annual-2 years | $50K - $500K + payments |
| Landing Pages | Webflow, Unbounce | Annual | $20K - $100K/year |
| ASO Tools | App Annie, Sensor Tower | Annual | $50K - $200K/year |
| Social Media | Sprout Social, Hootsuite | Annual | $20K - $100K/year |
| Content/SEO | Clearscope, Semrush | Annual | $20K - $100K/year |

**Buying Behavior:** Aggressive growth spending. CAC optimization is obsession. Tests rapidly; scales winners.

---

# 8. BaaS / Embedded Finance Providers

**Examples:** Zeta, Marqeta, Galileo, Unit, Synapse, Treasury Prime, Bond

**Characteristics:**
- B2B2C model; platforms serving fintechs and brands
- Core technology is the product
- Heavy engineering investment
- API-first; developer experience is competitive advantage
- Rapid growth; scaling infrastructure is critical

## Key Decision Makers

### CTO / Head of Engineering
**Typical Title:** CTO, Co-Founder & CTO, VP Engineering  
**Reports To:** CEO  
**Team Size:** 100 - 800  
**Annual Budget:** $30M - $200M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Cloud Infrastructure | AWS, GCP (primary) | Multi-year | $10M - $80M/year |
| Kubernetes/Container | GKE, EKS, self-managed | 2-3 years | $1M - $10M/year |
| Database | PostgreSQL, MongoDB, CockroachDB, Spanner | Ongoing | $2M - $15M/year |
| Event Streaming | Kafka (Confluent), Pulsar, AWS Kinesis | 3-5 years | $1M - $8M/year |
| Observability | Datadog, Grafana, Honeycomb | Annual-2 years | $1M - $8M/year |
| CI/CD | GitHub Actions, CircleCI, Buildkite | Annual | $200K - $2M/year |
| Security/SAST | Snyk, Checkmarx, Veracode | 2-3 years | $300K - $3M/year |
| API Documentation | Readme, Stoplight, Redoc | Annual | $50K - $300K/year |
| Load Testing | k6, Gatling | Annual | $50K - $200K/year |
| Developer Portal | Custom, Readme | Ongoing | $100K - $500K/year |
| Network Connectivity | Visa Direct, Mastercard Send, FedNow | 3-5 years | Network fees |
| Card Network | Visa, Mastercard licensing | Multi-year | Licensing + per-txn |

**Buying Behavior:** Build core differentiators; buy commodity. Obsessed with scale, latency, reliability.

---

### CPO / Head of Product
**Typical Title:** Chief Product Officer, VP Product  
**Reports To:** CEO  
**Team Size:** 30 - 150  
**Annual Budget:** $5M - $30M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Product Analytics | Amplitude, Mixpanel | Annual-2 years | $100K - $800K/year |
| Feature Flags | LaunchDarkly, Split | Annual | $100K - $500K/year |
| Product Management | Linear, Jira, Productboard | Annual | $50K - $300K/year |
| API Analytics | Custom, Moesif | Annual | $50K - $300K/year |
| Documentation | Readme, GitBook, custom | Annual | $30K - $200K/year |
| Sandbox/Testing | Custom environments | Ongoing | Included in cloud |
| Customer Feedback | Productboard, Canny | Annual | $30K - $150K/year |
| Roadmapping | ProductPlan, Linear | Annual | $20K - $100K/year |
| Design Tools | Figma | Annual | $30K - $150K/year |
| User Research | UserTesting, Maze | Annual | $30K - $150K/year |
| Partner Portal | Custom, Salesforce PRM | 2-3 years | $100K - $500K/year |
| Developer Relations | DevRel tools, community | Ongoing | $200K - $1M/year |

**Buying Behavior:** Developer experience is product. API quality and documentation are competitive advantages.

---

### CRO / Head of Risk
**Typical Title:** Chief Risk Officer, Head of Risk & Compliance  
**Reports To:** CEO  
**Team Size:** 20 - 100  
**Annual Budget:** $5M - $30M

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| Fraud Detection | Custom, Sardine, Feedzai | 2-3 years | $1M - $10M/year |
| Transaction Monitoring | Custom, Unit21 | 2-3 years | $500K - $5M/year |
| KYC/Identity | Alloy, Socure, Persona | 2-3 years | $500K - $5M/year |
| AML Platform | Custom, Actimize components | 3-5 years | $1M - $8M/year |
| Sanctions Screening | Dow Jones, Refinitiv API | Annual | $200K - $2M/year |
| Dispute Management | Custom, Chargebacks911 | 2-3 years | $200K - $2M/year |
| Card Network Compliance | Network tools, consultants | Ongoing | $200K - $1M/year |
| Regulatory Reporting | Custom | Ongoing | Built internal |
| Case Management | Custom, Unit21 | 2-3 years | $200K - $1M/year |
| Audit/SOC | Big 4, specialized auditors | Annual | $500K - $3M/year |
| PCI Compliance | QSA, tools | Annual | $200K - $1M/year |
| Model Validation | Consultants, internal | Ongoing | $200K - $800K/year |

**Buying Behavior:** Risk is product differentiator. Custom builds for core fraud/AML; vendor APIs for identity/verification.

---

### CFO
**Typical Title:** Chief Financial Officer  
**Reports To:** CEO  
**Team Size:** 20 - 80  
**Annual Budget:** $3M - $20M (finance technology)

| Software/SaaS Category | Example Vendors | Purchase Frequency | Budget Range |
|------------------------|-----------------|-------------------|--------------|
| ERP/Accounting | NetSuite, Sage Intacct | 3-5 years | $200K - $2M/year |
| Billing/Revenue | Stripe Billing, Chargebee, Zuora | 2-3 years | $100K - $1M/year |
| Revenue Recognition | RevPro, Softrax, custom | 3-5 years | $100K - $800K |
| FP&A/Planning | Anaplan, Pigment, Mosaic | 2-3 years | $100K - $800K/year |
| Spend Management | Ramp, Brex | 2-3 years | $50K - $300K/year |
| Procure-to-Pay | Zip, Airbase | 2-3 years | $50K - $300K/year |
| Financial Close | FloQast, Numeric | 2-3 years | $50K - $300K/year |
| Treasury/Banking | Modern Treasury, SVB, Mercury | Ongoing | Transaction fees |
| Investor Relations | Carta, Visible | Annual | $30K - $150K/year |
| Audit | Big 4 | Annual | $500K - $3M/year |
| Tax | Tax consultants, Avalara | Annual | $100K - $500K/year |
| Cap Table | Carta | Annual | $20K - $100K/year |

**Buying Behavior:** Scale-ready systems. Preparing for growth and potential IPO. Modern finance stack.

---

# Summary: Segment Comparison Matrix

| Segment | Top Decision Maker(s) | Primary Vendors | Avg Deal Size | Sales Cycle | Key Buying Criteria |
|---------|----------------------|-----------------|---------------|-------------|---------------------|
| **Money Center** | CIO, CTO, CDO | Custom + Enterprise | $10M - $500M+ | 12-36 months | Scale, Security, Integration |
| **Super Regional** | CIO, CTO, CDO | Enterprise + Platform | $5M - $100M | 9-18 months | Modernization, Experience |
| **Regional** | CIO, Head of Digital | Platform + Core | $1M - $30M | 6-12 months | TCO, Integration, Speed |
| **Community** | CFO, CIO/IT Director | Core Ecosystem | $100K - $5M | 3-9 months | Simplicity, Support, Price |
| **Small Community** | CEO, CFO | Core Provider Bundle | $20K - $500K | 1-6 months | Relationship, Bundle, Price |
| **Credit Unions** | CIO, VP Digital, CFO | CU-Focused Vendors | $100K - $20M | 3-12 months | Member Experience, Cost |
| **Digital Banks** | CTO, CPO, Head of Risk | Modern/API-First | $500K - $30M | 2-8 weeks | API Quality, Speed, Scale |
| **BaaS Providers** | CTO, CPO, CRO | Build + Modern Infra | $1M - $80M | 4-12 weeks | Scale, Reliability, Latency |

---

# Key Insights by Segment

## Money Center & Super Regional Banks
- **Longest sales cycles** (12-36 months for enterprise deals)
- **Highest budgets** but also highest scrutiny
- **Build vs. buy** tension; often custom-build core components
- **Multiple stakeholders** require consensus selling
- **Proof of concepts** are standard before procurement

## Regional & Community Banks  
- **Core provider ecosystem** is central to all decisions
- **Bundled solutions** preferred over point solutions
- **Relationship-driven** sales; trust is essential
- **Budget-sensitive** but investing in digital
- **Trade associations** (ABA, ICBA, state associations) are influential

## Credit Unions
- **Member-first** culture; different from bank profit motive
- **CUSOs and leagues** provide shared resources
- **Credit union-focused** vendors (Symitar, Corelation, Verafin) dominate
- **Volunteer boards** sometimes involved in major decisions
- **Cooperative model** means shared learnings

## Digital Banks & Neobanks
- **Engineering-led** decisions; API quality is paramount
- **Fastest procurement** (weeks, not months)
- **Modern stack** expectations; cloud-native is assumed
- **Growth-focused** spending; willing to pay for competitive advantage
- **Partner bank** relationships influence compliance tooling

## BaaS Providers
- **Technology is the product**; infrastructure must be world-class
- **Developer experience** is competitive differentiation
- **Build core**, buy commodity
- **Scale and reliability** are existential; downtime means customer loss
- **Rapid evaluation** cycles; willing to switch vendors quickly
