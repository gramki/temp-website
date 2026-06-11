# Unverified Claims Register — Account Products and Core Banking

**Date compiled:** March 2026
**Streams reviewed:** S1 through S6
**Purpose:** Every claim flagged `[unverified — needs manual confirmation]` across all 6 research streams, with impact assessment

---

## S1: Market Sizing and Revenue Pools

### Claim 1: Limit management systems are "typically bundled within core banking, risk management, or treasury platform market estimates"

- **Where it appears:** S1, Section 1F (Limit Management and Cross-Product Exposure Systems)
- **The claim:** No standalone market sizing exists for limit management / cross-product exposure systems. The assertion that these are bundled into adjacent market estimates is stated as analyst convention but not sourced to a specific analyst report.
- **Why it couldn't be verified:** No analyst report explicitly confirms or denies bundling. The claim is a reasonable inference from market report scope definitions but lacks a primary citation.
- **Source attempted:** Searched Mordor Intelligence, Grand View Research, Celent for standalone limit management market sizing — none found.
- **Impact if wrong:** **Low.** This claim affects completeness of the market sizing composite, not any structural shift or key finding. Limit management is a niche capability within broader platforms.

### Claim 2: Average deal size for community/regional bank core replacement

- **Where it appears:** S1, Section 6 (Implementation Timelines and Deal Size)
- **The claim:** Average deal size for community/regional bank core replacement is not found in public sources.
- **Why it couldn't be verified:** No public source provides reliable average contract value segmented by bank tier. Analyst firms (Celent, Datos Insights) have this data behind paywalls.
- **Source attempted:** Celent, Datos Insights, IBS Intelligence, Core System Partners — all either paywalled or do not publish per-deal pricing.
- **Impact if wrong:** **Medium.** Deal size affects revenue modeling for the opportunity analysis. Without per-deal sizing, revenue projections rely on top-down TAM allocation rather than bottom-up deal economics.

### Claim 3: Gartner Magic Quadrant for Global Retail Core Banking (2024)

- **Where it appears:** S1, Section 8 (Analyst Report References)
- **The claim:** The 2024 Magic Quadrant exists but is fully paywalled. Vendor positioning is available through vendor marketing materials (Temenos, Oracle, Thought Machine cite inclusion) but is not independently verified.
- **Why it couldn't be verified:** Gartner subscriber access only. No free/public version of the full quadrant.
- **Source attempted:** Gartner.com; vendor press releases confirm inclusion but not positioning.
- **Impact if wrong:** **Low.** The MQ's existence is confirmed by vendor citations. The positioning details affect competitive landscape analysis but are available from vendor-announced summaries in S3.

### Claim 4: Market Guide for Digital Banking Platforms (Gartner, 2024)

- **Where it appears:** S1, Section 8 (Analyst Report References)
- **The claim:** Gartner published a 2024 Market Guide for Digital Banking Platforms, but it is fully paywalled.
- **Why it couldn't be verified:** Same as Claim 3 — Gartner subscriber access only.
- **Source attempted:** Gartner.com public catalog.
- **Impact if wrong:** **Low.** Affects competitive landscape completeness but not structural shift ratings or market sizing.

---

## S2: Regulatory Landscape and Account Mandates

### Claim 5: FinCEN BOI registry operational status

- **Where it appears:** S2, Section on Gaps and Unresolved Questions (Gap #2)
- **The claim:** The Corporate Transparency Act BOI reporting requirements have faced multiple injunctions (2024–2025). Whether banks can rely on the FinCEN BOI registry for CDD verification at account opening remains unresolved.
- **Why it couldn't be verified:** The registry's operational status has been in flux due to court injunctions and reinstatement cycles. Status changes rapidly; no stable source as of March 2026.
- **Source attempted:** FinCEN.gov, National Law Review, Crowell FinTalk — all confirm uncertainty but cannot confirm current operational status.
- **Impact if wrong:** **Medium.** Affects the CDD/KYC infrastructure requirement for account opening. If the registry is operational, banks can verify beneficial ownership against it; if not, alternative verification workflows are required. Does not affect structural shift ratings (CDD/KYC is rated wrappable regardless).

### Claim 6: DORA secondary legislation completeness

- **Where it appears:** S2, Section on Gaps and Unresolved Questions (Gap #5)
- **The claim:** Not all delegated and implementing regulations under DORA are finalized as of the January 2025 effective date. Banks face compliance uncertainty.
- **Why it couldn't be verified:** The European Supervisory Authorities (EBA, EIOPA, ESMA) publish regulatory technical standards on a rolling basis. A comprehensive check of all outstanding RTS/ITS would require manual review of ESA publication registers.
- **Source attempted:** EBA DORA page, compliance news aggregators. Confirmed that some standards were still being finalized in late 2024.
- **Impact if wrong:** **Low.** DORA is rated as a partial forcing function — not a strong core replacement driver. Completeness of secondary legislation affects compliance planning timelines but not the market opportunity assessment.

### Claim 7: Basel III/IV output floor transition mechanics

- **Where it appears:** S2, Section on Gaps and Unresolved Questions (Gap #6)
- **The claim:** The 72.5% output floor is being phased in through 2030. Specific transitional percentages by year, and national discretion on implementation pace, require verification from CRR3 text.
- **Why it couldn't be verified:** The transition schedule is embedded in CRR3 regulatory text. Web search returned the endpoint (72.5% by 2030) but not the annual phase-in percentages or national discretion provisions.
- **Source attempted:** CRR3 text via EUR-Lex, Suade Labs, Deloitte analysis — all confirm the 72.5% floor and 2030 endpoint but do not detail annual steps in publicly available summaries.
- **Impact if wrong:** **Medium.** Basel III/IV is rated as a strong forcing function. The transition timeline affects how urgently European banks must upgrade their risk calculation engines. If the phase-in is more gradual than assumed, it reduces near-term urgency.

### Claim 8: India DPDP cross-border transfer restrictions

- **Where it appears:** S2, Section on Gaps and Unresolved Questions (Gap #9)
- **The claim:** 14 of 40 DPDP obligations remain unnotified, including cross-border data transfer restrictions and Significant Data Fiduciary designations.
- **Why it couldn't be verified:** The MeitY notification schedule is ongoing. The CADP tracker was consulted but the specific count of unnotified obligations could not be independently verified.
- **Source attempted:** CADP tracker (cadp.in), MeitY press releases.
- **Impact if wrong:** **Low.** DPDP is rated as wrappable (consent/privacy middleware). Cross-border restrictions would affect data architecture decisions but not core banking replacement decisions.

---

## S3: Competitive Landscape

### Claim 9: Infosys Finacle estimated revenue ($500–700M)

- **Where it appears:** S3, Competitor Profiles Table (Section A and G)
- **The claim:** Finacle revenue estimated at $500–700M, not separately disclosed by Infosys.
- **Why it couldn't be verified:** Infosys reports as a single entity ($19.28B total, FY2025). Finacle is a product within the Financial Services segment, which itself is not separately disclosed. Revenue estimates come from third-party triangulation (employee count, customer base, deal flow).
- **Source attempted:** Infosys IFRS filings, Infosys investor presentations, CB Insights. None provide Finacle-specific revenue.
- **Impact if wrong:** **Medium.** Finacle is a major competitor. Misestimating its revenue by 2x would change the competitive landscape assessment — a $300M Finacle is a niche player; a $700M Finacle is a scale competitor.

### Claim 10: TCS BaNCS estimated revenue ($400–600M)

- **Where it appears:** S3, Competitor Profiles Table (Section A and G)
- **The claim:** BaNCS revenue estimated at $400–600M, not separately disclosed by TCS.
- **Why it couldn't be verified:** Same dynamics as Finacle — TCS reports total revenue ($29B) and BFSI TCV ($4.0B Q4 FY2025) but does not break out product-level revenue. BaNCS is bundled within TCS's services revenue.
- **Source attempted:** TCS quarterly fact sheets, TCS investor presentations. None provide BaNCS-specific revenue.
- **Impact if wrong:** **Medium.** Same reasoning as Claim 9 — competitive landscape accuracy depends on scale assessment.

### Claim 11: Oracle FLEXCUBE estimated revenue ($300–500M)

- **Where it appears:** S3, Competitor Profiles Table (Section A and G)
- **The claim:** FLEXCUBE revenue estimated at $300–500M within Oracle's $56B total revenue.
- **Why it couldn't be verified:** Oracle does not disclose product-level revenue for financial services. FLEXCUBE is a small fraction of Oracle's total. No analyst provides a clean estimate.
- **Source attempted:** Oracle 10-K, Oracle Financial Services investor materials, CB Insights. None provide FLEXCUBE-specific revenue.
- **Impact if wrong:** **Low.** FLEXCUBE is a secondary competitor (aging architecture, lower Gartner Peer rating). Even at $500M, it is a mid-tier player.

### Claim 12: Finxact pre-acquisition customer count (~12–15 banks)

- **Where it appears:** S3, Competitor Profiles Table (Section B)
- **The claim:** Finxact had approximately 12–15 bank customers before FIS acquisition.
- **Why it couldn't be verified:** Finxact was private pre-acquisition; post-acquisition, FIS does not separately report Finxact customer metrics. CB RADAR credits FIS with 13 implementations but does not confirm these are all Finxact-specific.
- **Source attempted:** FIS 10-K, Finxact press releases, CB RADAR summary.
- **Impact if wrong:** **Medium.** Finxact is FIS's cloud-native core strategy. If the customer count is lower (e.g., 5–8), it suggests FIS's modern banking platform is less proven than claimed.

### Claim 13: Kyriba estimated revenue ($200–300M)

- **Where it appears:** S3, Competitor Profiles Table (Section D)
- **The claim:** Kyriba revenue estimated at $200–300M based on client count (3,400), employee count (501–1,000), and Euromoney recognition.
- **Why it couldn't be verified:** Kyriba is private. Revenue estimates are triangulated from employee count and market positioning.
- **Source attempted:** Kyriba press releases, Owler, Growjo.
- **Impact if wrong:** **Low.** Kyriba is a corporate treasury vendor, not a core banking competitor. Revenue affects the business banking sub-market sizing but not the core banking opportunity.

### Claim 14: ION Group estimated revenue ($2B+ total across divisions)

- **Where it appears:** S3, Competitor Profiles Table (Section D)
- **The claim:** ION Group estimated at $2B+ total revenue across all divisions.
- **Why it couldn't be verified:** ION is PE-owned with a complex multi-acquisition structure. No public financial disclosures.
- **Source attempted:** ION Group website, PE industry databases, Reuters. No revenue confirmed.
- **Impact if wrong:** **Low.** ION is a niche capital markets / treasury vendor. Revenue estimate does not affect structural shift ratings or core banking opportunity sizing.

### Claim 15: Zafin estimated revenue ($50–100M)

- **Where it appears:** S3, Competitor Profiles Table (Section F)
- **The claim:** Zafin revenue estimated at $50–100M based on customer base (~20–40 banks) and employee count.
- **Why it couldn't be verified:** Zafin is private. No public revenue disclosures.
- **Source attempted:** Zafin website, Growjo, Owler.
- **Impact if wrong:** **Medium.** Zafin is cited as a product overlay competitor that can delay core replacement decisions (S6). Its revenue scale affects how seriously to take the overlay-as-alternative thesis. A $100M Zafin is a meaningful competitor; a $30M Zafin is a niche player.

### Claim 16: SunTec estimated revenue ($80–120M)

- **Where it appears:** S3, Competitor Profiles Table (Section F)
- **The claim:** SunTec revenue estimated at $80–120M based on 150–170 clients across 45+ countries and 400M+ end-customers served.
- **Why it couldn't be verified:** SunTec is private. No public revenue disclosures.
- **Source attempted:** SunTec website, Celent recognition, Growjo.
- **Impact if wrong:** **Medium.** Same reasoning as Claim 15 — affects overlay competitor assessment.

### Claim 17: FIS Finxact acquisition price (~$650M)

- **Where it appears:** S3, M&A Activity Summary
- **The claim:** FIS acquired Finxact for approximately $650M in 2022.
- **Why it couldn't be verified:** FIS did not publicly disclose the acquisition price. The $650M figure appeared in one analyst estimate but was not confirmed in FIS's 10-K.
- **Source attempted:** FIS 10-K filings, press releases at time of acquisition.
- **Impact if wrong:** **Low.** The acquisition price does not affect the competitive landscape assessment — the strategic rationale (legacy incumbent buying cloud-native core) is the relevant data point.

### Claim 18: Wells Fargo Vantage won 2025 Celent Model Bank Award

- **Where it appears:** S3, Bank Modernization Signals Table
- **The claim:** Wells Fargo Vantage® won the 2025 Celent Model Bank Award for corporate digital banking.
- **Why it couldn't be verified:** The source URL provided in S3 is marked `[unverified — needs manual confirmation]`. Celent awards are often announced via vendor press releases; the full Celent awards list is paywalled.
- **Source attempted:** Celent public pages, Wells Fargo press releases. Could not locate a direct public confirmation.
- **Impact if wrong:** **Low.** The award validates Wells Fargo's augmentation strategy (integrated 65 systems without core replacement). Even without the award, the Vantage platform deployment is documented.

---

## S4: Structural Shifts and Core Modernization Activity

### Claim 19: Column bank BaaS model specifics

- **Where it appears:** S4, Gaps and Unresolved Questions (Gap #5)
- **The claim:** Column is frequently cited as a "modern BaaS bank" but limited public data exists on platform architecture and deployment specifics.
- **Why it couldn't be verified:** Column Bank is a private bank positioning as BaaS infrastructure. Technical architecture details are not publicly available.
- **Source attempted:** Column.com, fintech press coverage, banking databases.
- **Impact if wrong:** **Low.** Column is one of several BaaS banks. The structural shift assessment for embedded banking (Shift 7) does not depend on Column-specific data — it relies on Synapse collapse, FDIC Synapse Rule, Evolve Bank C&D, and Westpac deployment.

### Claim 20: Chime deposit data

- **Where it appears:** S4, Gaps and Unresolved Questions (Gap #7); also S6
- **The claim:** Despite Chime's IPO filing (May 2025) and subsequent quarterly earnings, specific deposit totals are not available in search results.
- **Why it couldn't be verified:** Chime is not a bank — deposits are held at partner banks (Bancorp and Stride). Chime's S-1 and earnings reports do not separately report total deposits held. The deposits appear in partner banks' FDIC call reports, not Chime's balance sheet.
- **Source attempted:** Chime investor relations (investors.chime.com), SEC EDGAR S-1 filing, FDIC call reports for Bancorp/Stride.
- **Impact if wrong:** **Medium.** Chime is the #1 new checking account acquirer (12.8% share, ahead of Chase and Wells Fargo). Knowing deposit scale would quantify the competitive threat to traditional banks. Without it, the deposit competition narrative relies on member count (9.5M) and transaction volume ($136B), which are less direct measures.

---

## S5: Business Banking, Cash Management, and Treasury

### Claim 21: Goldman Sachs identifies virtual accounts as "1 of 4 pillars of next-gen transaction banking"

- **Where it appears:** S5, Section 4.2 (Virtual Account Adoption Data)
- **The claim:** Goldman Sachs strategically frames virtual accounts as one of four pillars of next-generation transaction banking.
- **Why it couldn't be verified:** The claim is cited from a CashFac report that references Goldman Sachs but the primary Goldman Sachs source (likely a TxB strategy deck or client communication) is not publicly available.
- **Source attempted:** Goldman Sachs press releases, Goldman Sachs investor relations, CashFac report (which cites Goldman but does not provide a direct URL).
- **Impact if wrong:** **Low.** The claim is used to validate virtual account adoption momentum. The more important data point is the 86% bank investment rate (from Datos Insights), which is independently sourced.

### Claim 22: UK FCA virtual IBAN guidance (2025–2026 specifics)

- **Where it appears:** S5, Section 4.5 (Virtual Account Regulatory Status — UK row)
- **The claim:** FCA regulates virtual IBANs issued by e-money institutions under Electronic Money Regulations. The 2025–2026 specifics of FCA guidance may have updated.
- **Why it couldn't be verified:** The FCA consultation on safeguarding reform and virtual IBAN guidance is an evolving area. Web search returned the general framework but not confirmed 2025–2026 updates.
- **Source attempted:** FCA.org.uk consultation papers, PSR publications.
- **Impact if wrong:** **Medium.** Affects the regulatory assessment for UK virtual account structures. If FCA has tightened guidance, banks may face new compliance requirements for virtual IBAN services, which could be an adoption accelerator (regulatory clarity) or brake (new restrictions).

### Claim 23: Thought Machine / 10x Banking business banking specific deployments

- **Where it appears:** S5, Section 10.2 (Cloud-Native Core Vendors for Business Banking)
- **The claim:** Thought Machine and 10x Banking are listed as options for separate business banking core deployments, but specific business banking (vs. retail) deployments need verification.
- **Why it couldn't be verified:** Thought Machine's named deployments (Lloyds, Standard Chartered, Intesa) appear to be retail or mixed-use. Whether any deployment is specifically for business banking products is unclear from public sources.
- **Source attempted:** Thought Machine case studies page, 10x Banking success stories.
- **Impact if wrong:** **Medium.** Affects whether next-gen core vendors have a proven business banking track record. If their deployments are retail-only, the business banking overlay market (iGTB, Finastra) has a stronger competitive position for business banking modernization.

---

## S6: Deposit Innovation, Open Banking, and Account Portability

### Claim 24: Neobank share of all new account openings (~40%, 2025)

- **Where it appears:** S6, Section 1 (Market Share of New Account Openings — row 2)
- **The claim:** Neobanks capture approximately 40% of all new account openings in 2025.
- **Why it couldn't be verified:** Source is ainvest.com (an aggregation site), not a primary analyst or survey. The more rigorous Cornerstone Advisors / Forbes data puts the 2024 figure at 44% for all fintech/neobank checking accounts.
- **Source attempted:** ainvest.com (aggregated estimates), cross-referenced with Cornerstone Advisors.
- **Impact if wrong:** **Low.** The more rigorously sourced 44% (2024) and 12.8% Chime-specific (Q4 2025) figures from Cornerstone/American Banker are verified. The ~40% estimate for 2025 is directionally consistent.

### Claim 25: Americans with online savings accounts (>68M)

- **Where it appears:** S6, Section 2 (Deposit Migration Evidence)
- **The claim:** More than 68 million Americans have online savings accounts.
- **Why it couldn't be verified:** Source is finverium.com, a financial blog. No primary survey or FDIC data cited.
- **Source attempted:** FDIC reports, Federal Reserve SCF data — neither provides a specific count of online-only savings accounts.
- **Impact if wrong:** **Low.** The claim is used directionally (large number of Americans use online savings). The structural point about deposit migration stands regardless of the exact count.

### Claim 26: Deposits flowing to fintech investing platforms (>$3T cumulative)

- **Where it appears:** S6, Section 2 (Deposit Migration Evidence); also S6 Cornerstone Advisors raw notes
- **The claim:** More than $3 trillion in deposits have flowed from traditional institutions to fintech investing platforms.
- **Why it couldn't be verified:** Source is Cornerstone Advisors' "What's Going On in Banking 2026" report, which is paywalled. The $3T figure may conflate different asset classes (deposits, brokerage accounts, crypto holdings) or time periods.
- **Source attempted:** Cornerstone Advisors press releases (public summary data only), FDIC deposit flow data.
- **Impact if wrong:** **High.** This is a headline claim about deposit displacement. If the $3T figure includes non-deposit assets (e.g., Robinhood brokerage, Coinbase crypto), it overstates the deposit competition threat. The actual deposit-specific outflow may be significantly smaller. The claim should not be used without verification against Cornerstone's methodology.

### Claim 27: Legacy core time-to-market — African banks (12–18 months)

- **Where it appears:** S6, Section 3 (Time-to-Market)
- **The claim:** Legacy core banking systems in African banks take 12–18 months to launch a new deposit product.
- **Why it couldn't be verified:** Source is BOS Fintech (bosfintech.com), a vendor blog, not an independent analyst or survey.
- **Source attempted:** BOS Fintech blog post. No independent validation of the 12–18 month claim.
- **Impact if wrong:** **Low.** The 10:1 time-to-market ratio (legacy vs. modern) is supported by multiple data points, including verified vendor case studies (Zafin 8-week CD modernization, Temenos 4-month Next Bank, Mambu 8-month Chetwood). The African-specific claim is one data point in a broader pattern.

### Claim 28: Legacy core time-to-market — US banks (9+ months)

- **Where it appears:** S6, Section 3 (Time-to-Market)
- **The claim:** US banks on legacy cores take 9+ months for basic products like high-yield savings.
- **Why it couldn't be verified:** Source is Q2 Holdings blog (q2.com), a vendor with commercial interest in highlighting legacy limitations.
- **Source attempted:** Q2 blog post. No independent analyst validation.
- **Impact if wrong:** **Low.** Same reasoning as Claim 27 — supported by the broader pattern.

### Claim 29: Legacy core maintenance consumes 64% of IT budgets

- **Where it appears:** S6, Section 3 (Time-to-Market)
- **The claim:** Up to 64% of IT budgets are consumed by legacy core banking maintenance, leaving minimal capacity for innovation.
- **Why it couldn't be verified:** Source is BOS Fintech vendor blog. The more commonly cited figure is 24% (EY UK, verified in S1) or "over 60%" for run-the-bank spending (BCG, cited in S5). The 64% figure may be conflating legacy maintenance specifically with broader run-the-bank spend.
- **Source attempted:** BOS Fintech blog, cross-referenced with EY UK (24% for core banking maintenance specifically) and BCG (>60% for run-the-bank generally).
- **Impact if wrong:** **Medium.** The distinction matters: 24% on core banking maintenance (EY, verified) is a meaningful cost burden; 64% is a dramatic claim that changes the cost calculus. The verified 24% figure (EY UK) and the McKinsey-sourced $57.1B global annual legacy maintenance cost should be used instead.

### Claim 30: Stablecoin transaction volume ($33T in 2025)

- **Where it appears:** S6, Section 6 (Stablecoin and Tokenized Deposit Competition)
- **The claim:** Stablecoin transaction volume reached $33 trillion in 2025, up 72% YoY.
- **Why it couldn't be verified:** Source is blockeden.xyz, a crypto analytics blog. Stablecoin transaction volume figures vary widely depending on methodology (e.g., whether wash trading, self-transfers, and smart contract interactions are included).
- **Source attempted:** blockeden.xyz, CoinLaw, CoinMetrics. Figures range from $27T to $35T depending on source and methodology.
- **Impact if wrong:** **Medium.** The stablecoin competitive threat assessment depends on whether $33T represents genuine economic activity or inflated on-chain metrics. If the actual economic value is $10–15T (after excluding wash trading and internal transfers), the threat to bank deposits is proportionally smaller.

### Claim 31: Tether profit ($13B in 2024)

- **Where it appears:** S6, Section 6 (Stablecoin market data)
- **The claim:** Tether reported $13B in profit in 2024.
- **Why it couldn't be verified:** Tether does not publish audited financial statements. The $13B figure comes from Tether's own attestation reports and crypto news coverage, not from independently audited financials.
- **Source attempted:** Tether attestation reports, blockeden.xyz, CoinDesk.
- **Impact if wrong:** **Low.** Tether's profitability supports the narrative that stablecoin issuance is economically significant, but the core banking opportunity assessment does not depend on Tether's exact profit figure.

### Claim 32: Tether US Treasury holdings ($135B)

- **Where it appears:** S6, Section 6 (Stablecoin market data)
- **The claim:** Tether holds $135B in US Treasury securities as reserve backing.
- **Why it couldn't be verified:** Same as Claim 31 — based on Tether's own attestation reports, not independently audited.
- **Source attempted:** Tether transparency page, blockeden.xyz.
- **Impact if wrong:** **Low.** Same reasoning as Claim 31.

### Claim 33: Stablecoin market could exceed $2T by end of 2026

- **Where it appears:** S6, Section 6 (Market Size table)
- **The claim:** CoinLaw projects the stablecoin market could exceed $2T by end of 2026.
- **Why it couldn't be verified:** This is an aggressive growth projection (from ~$300B to $2T in one year, ~7x growth). No mainstream financial analyst validates this trajectory.
- **Source attempted:** CoinLaw projection page. Cross-referenced with more conservative estimates ($500B–$1T by 2028 from various crypto analysts).
- **Impact if wrong:** **Low.** The projection is flagged as "likely aggressive" in S6. The core banking opportunity assessment uses current market cap ($300B+) rather than forward projections.

### Claim 34: PSD3 compliance transition period (21 months after adoption)

- **Where it appears:** S6, Section 4 (Open Banking Adoption — EU row)
- **The claim:** PSD3 has a 21-month transition period after formal adoption.
- **Why it couldn't be verified:** Source is knowledgelib.io, a secondary compliance information site. Norton Rose Fulbright (verified source) states "H2 2027 to early 2028" for implementation, which is consistent with a ~21-month transition from Q1 2026 adoption — but the exact transition period is not confirmed in the provisional agreement text.
- **Source attempted:** Norton Rose Fulbright PSD3 analysis (confirmed "H2 2027–early 2028"), Wintherlaw, knowledgelib.io.
- **Impact if wrong:** **Low.** The directional timeline (H2 2027–early 2028 for PSD3 enforcement) is confirmed by Norton Rose Fulbright. Whether it is exactly 18 or 21 months does not affect the opportunity assessment.

### Claim 35: Warwick University research on open banking "silent revolution" stalling

- **Where it appears:** S6, Section 5 (Account Portability and Switching — Caveat)
- **The claim:** Warwick University (2025) research suggests open banking's "silent revolution" may be stalling — incumbent banks are slowing implementation and acquiring fintechs rather than competing.
- **Why it couldn't be verified:** The source is an academic working paper (wrap.warwick.ac.uk). Academic papers may have different evidentiary standards from industry data. The paper was not accessible for full review.
- **Source attempted:** Warwick University repository (URL provided in S6). Access was partial — abstract available, full paper not reviewed.
- **Impact if wrong:** **Low.** The claim is used as a caveat, not as a structural finding. The open banking adoption data (UK OBIE 15.1M users, India AA 390.9M consents) provides the primary evidence.

### Claim 36: US neobank customer base (~150M accounts)

- **Where it appears:** S6, Section 1 (Market Share of New Account Openings — last row)
- **The claim:** The US neobank customer base grew from 86M to approximately 150M accounts in 30 months.
- **Why it couldn't be verified:** Source is electroiq.com, aggregating eMarketer data. The "150M accounts" figure likely counts all fintech accounts (including secondary accounts, inactive accounts, and non-bank financial product accounts), not unique neobank customers.
- **Source attempted:** electroiq.com, eMarketer (paywalled), Simon-Kucher (which provides the 86M baseline but uses a different methodology).
- **Impact if wrong:** **Medium.** The distinction between "150M accounts" and "150M customers" matters significantly. If 52% of new accounts are secondary (per J.D. Power verified data), the unique customer count could be substantially lower. This affects the "neobanks are winning" narrative — the reality may be "consumers are multi-banking with neobanks as secondary providers."

---

## Impact Summary

| Impact Level | Count | Key Claims |
|---|---|---|
| **High** | 1 | Claim 26 ($3T deposits to fintech investing platforms — methodology unclear, headline risk) |
| **Medium** | 9 | Claims 2 (deal sizes), 5 (BOI registry), 7 (Basel III transition), 9–10 (Finacle/BaNCS revenue), 12 (Finxact customers), 15–16 (Zafin/SunTec revenue), 22 (UK VAM regulation), 23 (business banking deployments), 29 (64% legacy maintenance), 30 (stablecoin volume), 36 (150M neobank accounts) |
| **Low** | 14 | Claims 1, 3, 4, 6, 8, 11, 13–14, 17–19, 21, 24–25, 27–28, 31–35 |

### Priority for Manual Verification

1. **Claim 26** (>$3T deposits to fintech — HIGH) — verify Cornerstone methodology before using in deliverables
2. **Claims 9–10** (Finacle/BaNCS revenue — MEDIUM) — affects competitive landscape positioning
3. **Claim 12** (Finxact customer count — MEDIUM) — affects FIS competitive assessment
4. **Claim 29** (64% legacy maintenance — MEDIUM) — use EY 24% figure instead unless BOS Fintech methodology is confirmed
5. **Claim 36** (150M neobank accounts — MEDIUM) — clarify accounts vs. customers distinction
6. **Claims 15–16** (Zafin/SunTec revenue — MEDIUM) — affects overlay competitor assessment
7. **Claim 7** (Basel III transition — MEDIUM) — verify annual phase-in schedule from CRR3 text
