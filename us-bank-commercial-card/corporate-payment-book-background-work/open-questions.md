# Open Questions for Corporate Payments Concepts

> **Terminology note (for the rewrite into `corporate-payments-concepts.md`):**
> - "Spend Lane" in questions and answers below maps to **Spend Archetype** in the rewrite — a conceptual workflow pattern, not a system entity. Realized as a classification attribute of Corporate Payment Product.
> - "Spend Mandate" remains the same term but is repositioned as a conceptual tool only — realized as the composition of Budget, Spend Policy, Booking Profile, and Card Profile sub-sections within a Corporate Payment Program. Not a standalone entity.
> - See `suggested-outline-draft.md` for the full outline with the "From Concepts to Entities" bridge.

---

## Corporate → Legal Entity → OU model

1. Is a Corporate itself an entity in the system, or is it just the set of its Legal Entities? If a corporate acquires a new legal entity mid-program, what happens?

> Yes, it is. But it is not a legal enity. It is a logical entity that can host rest of the structure. This entity itself is associated to a Client Contract (and thus to a Legal entity) for legal provenance.  

2. Can an OU span multiple Legal Entities? If a "Global Engineering" OU contains employees from three Legal Entities, and a Program is pinned to one Credit Facility (and thus one Legal Entity), how does that work?

> Yes. There can be any number of trees of OUs under a corporate. All legal entities are by default a OU hierarchy with just one flat list of OUs, one OU per entity under the "Legal Entities" OU root node.
> "how does that work" that work for what? There are multiple dimensions by which how it works should be assessed.

3. Who creates and maintains the OU hierarchy — the corporate alone, the ESP, or both? If the corporate restructures, what downstream impact does that have on Budgets, Programs, and card assignments?

> Corporate with or without ESP's assistance or ESP creates on behalf of Corporate.
> Progarm's Credit Facility cannot move across Legal Entities, but the Budgets can change and the OUs can change. All subsequent transactions are governed by the new Budget and reported to the new OU as required. Should have no impact on cards. Cards are associated to program which inturn carries OU association.

## Account as the bridging entity

4. Is there always one account per Program, or can a Program have multiple accounts?
> Depends on the Spend Lane. Employee spends like travel, reimbursements, will have one account per employee.
> P-Card like programs where cards are issued to suppliers may only have one account per program. The corporate could create programs as per their billing/booking requriements.

5. If a card is always tied to one account, and an account is always tied to one Program, does that mean a card can never be used across programs? For an employee who participates in both a travel program and a department spend program, does the employee carry two separate cards?
> Yes, he will get two cards.

6. What is the relationship between Account and Budget — is it 1:1, many:1, or configurable? If an account is assigned one Budget, but the corporate later wants to split spend within that account across two Budgets, what happens?
> A budget of a program can be shared by n accounts in the program.

## Budget hierarchy

7. If Budget is hierarchical and a Budget can have sub-Budgets, how does limit enforcement cascade? If a parent Budget has a $2M limit and two sub-Budgets of $1.2M and $1M, is the parent over-allocated? Is over-allocation allowed?
> Over-allocation is allowed. Budget is enforced through the hierarchy. All ancestors in the heirarchy will be consulted for authorizing a spend and overuse is not allowed.

8. Can a Budget be shared across Programs, or is it 1:1 with a Program? If one Budget funds two Programs, how is contention resolved?
> Yes, it can be shared across programs.
> There is no contention. Collectively the programs cannot exceed the budget.


## Spend Mandate vs. platform-enforceable controls

9. What parts of the Spend Mandate are enforceable by the issuer at authorization time, and what parts are corporate-side governance only? "Business purpose" and "accountability" cannot be enforced at swipe. Should the Mandate distinguish between its issuer-enforceable half and its corporate-governance half?

> Yes. The Purpose and Accountability are auditable not enforceable. However, the restrictions placed on the card may accomplish certainly controls pertraining to Purpose, like the places, merchants the cards can be used at.

10. What is the enforcement boundary between Mandate and card-level controls? Does the Mandate translate into card-level controls at issuance time, or does the Mandate exist as a separate policy layer evaluated at authorization?
> Both. Relevant controls are enforced at appropriate time.

## ESP

11. Can a corporate work with multiple ESPs under the same bank? If so, who owns the corporate relationship — the bank, the ESP, or both?
> This is a business arrangement question. Out of the product and system realm. System supports a Legal Entity to be customer of multiple ESPs.

12. Does the ESP have its own entity model, or does it operate purely within the bank's entity model? When the ESP "creates a Corporate Payment Product," is that product registered in the bank's system or does the ESP maintain its own product catalog?
> ESP has its own entity model and database. It is an independent perosna with an independent product called "Electron" providing the required capabilities to ESP and Corporates. Tachyon provides capabilities to the Bank to support ESPs and Corporates for 'pure' bank scope - Payments, Accounts, KYB, KYC, Credit Facilities, etc.,

13. What happens when an ESP is replaced? If a corporate switches ESPs but stays with the same bank, do the Credit Facilities, Accounts, and Programs survive?
> Credit Facilities - Yes. 
> Programs - No.


## Supplier / Merchant duality

14. How does the corporate map its Supplier (OU member) to the bank's Merchant (AMC)? Is there an explicit mapping entity, or is this a reconciliation-time matching problem?
> These are not mappable. They represent different concepts and their use in respective domains for different purpose. 
> Corporate should reconcile Supplier assocaition using the Card Data or Data from Posting including L2 Data from the merchnt like:
	•	tax amount
	•	tax indicator / tax rate if supported
	•	PO number
	•	invoice number
	•	customer code / corporate reference
	•	sometimes order/reference IDs passed by the merchant or gateway

> Whereas, L1 Data provides:
	•	transaction amount
	•	MCC
	•	date/time
	•	merchant name / merchant identifier
	•	currency

15. When a card is issued to a supplier (in the Supplier Payments lane), who is the cardholder? Is the supplier the cardholder, or is the Program Admin the cardholder and the supplier the authorized user?
> Program Admin is the card holder, with Card Profile carrying specific-tags about the Supplier the card is issued to.
> If the Card is enabled for ACS and 2-factor authentication for transaction, then an authorized user from the Supplier should be the card holder so that they can respond to the second-factor challenge. 
> In both cases, the Supplier information is tagged to the Card, irrespective of what goes in Cardholder Profile.


## Booking Profile and Settlement Profile

16. Is a Booking Profile always static per Program, or can it vary per transaction? The employee-spend case suggests it can vary (employee adds project codes post-transaction). Is it really a "profile" or more of a "template with runtime resolution"?

> The profile can have rules. Based on the rules, the booking can be attributed to respective Cost Centers and Cost Heads.

17. Can a single Program have multiple Settlement Profiles? For example, a global travel program where settlement happens through different regional treasury accounts depending on the Legal Entity of the traveler.
> No. The system supports only one Settlement Account in a Settlement Profile of a program.

## Transaction lifecycle

18. Where do disputes and chargebacks live in this model? Does the dispute flow back through the Booking Profile (to reverse the GL entry) and the Settlement Profile (to adjust the repayment)?
> Disputes are settled by bank against the Account associated with the Program. The reversal/credits issued are attributed to original postings. So the reconciliation and adjustments can be handled without ambiguity.

19. What happens between authorization and clearing? Is there a concept of "pending spend" against a Budget? If so, is that the Budget's concern or the Account's concern?
> Budget is utilized at the time of authorization. Adjustments are made at the time of clearing. Thus there is no 'Pening Spend' at Budget. "Uncleared" transactions are only a concern at an Account.

20. How are refunds modeled? Does a refund inherit the Booking Profile and Settlement Profile of the original transaction, or does it need its own treatment?
> Yes, it inherits original transaction profile. Settlement profile is scoped to account. So, unmatched refunds are not a problem for settlement. Booking Profile may have default allocation for unmatched credits.

## The five Lanes

21. Is the list of five Lanes exhaustive and closed, or is it extensible? If a corporate has a spend workflow that does not fit any of the five, can a new Lane be defined? Who defines it — the ESP, the bank, or Zeta?
> ESP defines it with help from Zeta.  
> Bank need not be involved.

22. Is "Embedded / ERP-native Payments" really a Lane, or is it a delivery mechanism that applies to any Lane? The "embedded" quality describes how the card is generated, not the nature of the spend workflow. Should it be an attribute of a Program rather than a Lane?
> It is a delivery mecahnism. We can drop that and ensure that every lane has relevant embedding capabilities through APIs and events.

## Commercial terms

23. Should the commercial terms model distinguish between pass-through economics (set by network/regulator), bank economics (set by the bank), and ESP economics (set by the ESP)?

> In Corporate Payment Product, what's relevant is  the ESP terms extended to Corporate.
> The terms extended by the Bank to ESP are not modeled in the current scope.

24. Are commercial terms per Product or per Program? Large corporates negotiate deal-specific pricing that may vary by program volume, geography, or lane. If a corporate runs three programs on the same Product, can each have different commercial terms?
> From ESP to Corporate, they are per Corporate Payment Product. The Program represents a operational requirement in the corporate realm and not a commercial contract between ESP and Corporate.

## Configuration authority and state models

25. Should the document define what is and is not configurable by each actor (Bank, ESP, Corporate)? For each entity — who creates it, who can modify it, who can view it?
> The document should focus only on ESP and Corporate.

26. Should there be an explicit state model for each entity? A Program can be draft, active, suspended, closed. A Budget can be open, exhausted, frozen. A Credit Facility can be active, under review, terminated. Are these states needed for PMs building the platform?
> That would help understand the entity better. go for it.


## Entities referenced but not yet defined

27. Card Profile is mentioned as carrying supplier tags and corporate-set attributes. Is Card Profile a defined entity in Electron? What attributes does it hold beyond supplier tags? Does it carry the control parameters (MCC restrictions, amount limits, validity), or are those separate?
> Card Profile:
- Cardholder Profile: Name on Card, Address, (Email, Phone Number) for ACS Second-factor authentication and Notifications delivery. Custom Attributes to map the Cardholder to the Corporate domain (CorporateMemberType, CorporateMemberID) 
- Spend Policy/Payment Usage Policy: Velocity, Volume limits (using tumbling windows of daily, weekly, monhtly, quarterly, annually) across merchant category, AMC, time-slices, Life-to-date limits, and restrictions of allowed, disallowed transactions based on various attributes in the authorization request. 
- Fee Overrides: For various fees assessed
- Tags: Structured object extensions to capture data at card (serialized as URI format for each tag type); Use-cases: Corporate Program Inforamtion (Corporate ID, Program ID, Member ID, Membership ID), Intended Supplier Information, Reconciliation Tracking Information, etc., Tag data can be referenced in the Payment Usage Policy rules also.
   

28. Member is used throughout — "member of an OU," "eligible members," "enrolled members," member types. Is Member a first-class entity? What are the recognized member types (employee, supplier, contractor, etc.)? What attributes does a Member carry?
> Member is a first-class entity of a Corporate with member-of affiliation to zero or more OUs.
> Default Member Types: Employee, Supplier, Contractor, Client
> A Corporate can define custom attributes for every member type as they may need for mapping them to their enterprise systems
> A Member is eligible for enrollment into a Payment Program based on the program's elegibility rules. 
> An eligible Member can be enrolled by the Program Admin using various tools - UI, Files, APIs.
> An enrolled member receives a virtual card and optionally account based program constructs (lane)
> An eligible member can have multiple enrollments into the same program and each such enrollment represent a new v-card (support one-time use cards, ad-hoc/short-lived cards, etc.,)   

29. Client Contract — the Corporate entity is associated to a Client Contract for legal provenance. What is the Client Contract entity? Is it the contractual relationship between ESP and Corporate? Between Bank and Corporate? Does it govern commercial terms, or is that separate?
> Client Contract is an Entity in ESP Domain that represents a commercial relationship between ESP and real-world Corporate. (Ex: Walmart could be a corporate. But it may have multiple legal entities through which its business is conducted. The ESP initiates a Corporate onboarding for Walmart using a Client Contract signed by one or more of the legal entities)
> A Corporate comes into existence through a Contract. The Contract may have been signed by one or legal entities corresponding to that corporate. 
> A Client Contract may have extensions and renewals. But the system may not model all of that.

30. Spend Policy is referenced as part of Mandate enforcement ("Budget limits, Spend Policies are enforced inline"). Is Spend Policy a separate configurable entity, or is it an attribute of the Mandate? Who configures it — the ESP, the corporate, or both?
> Spend Policy is a Sub-enity of the Mandate.
> Spend Policy can be overriden per Card as well.
> ESP Configure Spend Policy in Corporate Payment Product. 
> Corporate configures Spend Policy in Payment Program. However, this Corporate-defined policy can only be more-restrictive but cannot expand the restrictions or controls enforced by ESP. 
> Corporate may also define a Spend Policy per Card. This can also be only more restrictive than the policy define at the Program.

## Spend Mandate as a system entity

31. Is the Spend Mandate a first-class entity in Electron, or is it a conceptual envelope? Is there literally a "Mandate" object that the corporate creates and attaches to a Program? Or is it realized as a composition of Budget assignment + Policy configuration + Card controls + Booking Profile rules — with no single "Mandate" record?

> There is no single Mandate entity. All relevant aspects are sub-sections of Corporate Payment Program entity. 
> Credit Facility, Budget, Settlement Accounts, OUs, Members, and Users are entities references in the Payment Program 
> Users are people entitle to create and operate the Payment Programs in the Corporate with relevant authorization controls limiting their scope specific programs, products, budgets, and OUs.
> Budgets are associated with OUs.
> Program is always owned by a OU irrespective of the members who may be eligible. Budgets of the OU are visible during the program setup.

## Per-lane control archetypes

32. For each of the four lanes, what is the normative control archetype? For example:
   - Supplier Payments: single-use, one card per invoice, locked to a specific merchant?
> Yes; With a single Account per program
> Each enrollment is typically for an invoice or PO. If for a PO, it could be multi-use card.

   - Employee Spend: multi-use, per-employee, MCC-restricted?
> Yes, with an Account per each Employee
> With optional data capture form for each spend
> With an optional Approval workflow involving an approving authority per employee as defined in the enrollment and optionally a group of users nominated by program admin.

   - Travel: single-use per booking, or lodge-style persistent per agency?
> Both are possible
> Mostly peristent per agency 

   - Central Recurring: multi-use, merchant-locked, persistent?
> One card per Project or Cost Head. Could be used at various merchants/suppliers (whitelist or blacklist based restrictions). Persistent.

33. For reconciliation per lane, what does the corporate match against what? For example:
   - Supplier Payments: card (supplier-tagged) + posting (invoice number from L2) matched against AP invoice in ERP?
> Yes. There are other L2 attributes described earlier.
   - Employee Spend: posting + employee-provided expense code matched against budget/cost center?
> If the program setup requires employee to provide the expense code, then that is used
> If the program is for only one cost head and expense code, that information is available at the program level itself.
   - Travel: posting matched against itinerary/booking reference?
> Yes, provided by the agency in L2 data

## Card issuance and enrollment

34. What does enrollment look like operationally? The doc says "enrollment is always explicit." Does the Program Admin manually enroll each member? Is there a bulk enrollment mechanism? Does enrollment trigger card issuance, or are those separate steps?

> An eligible Member can be enrolled by the Program Admin using various tools - UI, Files, APIs.
> Each enrollment results in a card
> In-specific cases an enrollment require steps to be fulfilled by the card-holder for KYC purposes. And this may be conditional.  

35. Physical cards vs virtual cards — the entity model (Account, Card, Program) seems to support both. Is that correct? Are physical cards in scope for this document, or should it be explicitly scoped to virtual cards? Do any lanes predominantly use physical cards (e.g., employee spend)?

> Yes, Virtual Card can be both Physical or Digital. It can be initiated as Digital card but can be converted to a Physical card. The "virtual" in the phrase doesn't reflect the physical form-factor but indicates that the card in itself doesn't have a financial obligation and the obligation is coming from an Account. Per se, that's an industry term (to distinguish the majority of card system's behavior wherein a card and account are tightly coupled) and has no real relevance in the system.

## Approval and workflow layer

36. Is there an in-platform approval engine, or is approval external? The Mandate has an "approver" and the Program Admin "approves enrollments." Does Electron provide an approval workflow engine (request → approve → issue), or does the corporate handle approvals in its own systems and Electron only enforces the outcome?

> Yes. At the time of program setup this can be configured.


## Cross-border and FX mechanics

37. When a card is used cross-border in a different currency from the account base currency, where does FX conversion happen? At the network level? At the issuer level? Who bears the FX risk — the corporate or the bank?

> Network level
> Corporate


## Statement and billing mechanics

38. In an employee-spend program with hundreds of accounts (one per employee), how does billing work? Is there a consolidated bill at the Program level, or does the corporate receive hundreds of individual account-level statements? Is there a concept of a "master statement" or "consolidated billing view"?

> Yes, a master statement for a program is provided for programs that have multiple accounts under it.
> ESP System (Electron) generates this master statement by compiling the individual account statements received.

## Document scope

39. Should the document cover the network model (issuer, acquirer, network, merchant) briefly? Even a short paragraph establishing the four-party model would help PMs new to payments. Or is that assumed knowledge for the audience?
> It is assumed knowledge
> The Programs can work on Private Label cards as well, where the acquirer and issuer is likely the same

40. Is Level 3 data (line-item detail) relevant for any lane? Some supplier payment programs use L3 for tax compliance and detailed reconciliation. Should it be mentioned?
> yes. if provided by the merchant, it is made available to the corporate through data extracts.

41. Is there anything the document should explicitly declare out of scope? Candidates: bank-to-ESP P&L, card network protocol internals, regulatory specifics per jurisdiction, fraud management, AML/sanctions screening, dispute resolution procedures.

> You can call these as out of scope


## Product-Lane cardinality

42. Can a single Corporate Payment Product support multiple Spend Lanes? For example, could an ESP create one "Enterprise Card Product" that supports both Employee Spend and Travel lanes, and the Corporate then creates separate Programs under it — one for each lane? Or is the design intent that each Product maps to one Lane, and multi-lane coverage requires multiple Products?
> No. Corporate Payment Product is tagged to a spend line to a simplify operations both at Corporate and ESP end
> Treat Lanes as archetype of a workflow. The labels are indicative, but the description should specify what they are meant for.
> Multiple lane coverage requires multiple products. However, new lanes can be introduced representing such hybrid requirements if they are essentail and valuable.


## Users vs Members

43. Can a User also be a Member? For instance, a department head who operates a Program (User role) and is also enrolled as a spender in another Program (Member role). Or are Users and Members strictly separate populations? Are Users modeled as Members with a particular role, or are they an independent entity?

> Yes, they are entities in different domains. User Entity is relevant only for administration and operational use cases. Members are the participants in programs.

## AMC in Spend Policy

44. AMCs are described as the bank-side grouping for commercial terms. Are AMCs also usable in Spend Policy rules at the card level? For example, can a Spend Policy say "allow transactions only at merchants in AMC-Travel" or "block all merchants in AMC-Entertainment"?
> Yes, they can be used by the Corporates and ESPs as well.
> ESPs and Corporates may request for custom AMCs as well


## Data-capture form in Employee Spend

45. The Employee Spend lane has an "optional data-capture form for each spend." Is this form a configurable construct within the Program (defined at program setup)? Does the employee fill it out in Electron's UI after each transaction? Does the data captured flow into the Booking Profile rules for cost-center attribution?

> Yes to all. The form is expected to capture sufficient information to meet the data needs of the booking profile
> "Form" is a metaphor. The actually UI could be anywhere, including the default provided by electron. APIs are provided to add this additional info against each Posting.

## Settlement timing

46. The Settlement Profile defines which account is used for repayment. Does it also govern when and how settlement happens — billing cycle (monthly, weekly), auto-debit vs manual payment, payment due date? Or are those properties of the Credit Facility or the commercial terms rather than the Settlement Profile?

> The Billing is performed by ESP. 
> The Billing configuration at the ESP end determines the Billing Cycle, Payment Due Date, Interest-free period, and subsequent penalities.
> Settlement is performed against the bills/invoices received from ESP as per the Settlement Profile in the Payment Program created by the corporate. This profile indicates how the invoices from the program are settled. This include auto-pay, payment date related config.

## Document tone

47. Should the final `corporate-payments-concepts.md` be written as: (a) a reference manual — precise definitions, structured for lookup, (b) a teaching document — narrative arc, building concepts progressively, or (c) a hybrid — progressive narrative for first read, structured for subsequent reference?

Hybrid. Consider this as a book, rather than a single document. Have authoritative reference sections independents of the narrative sections.  

---

## Bank's Role — Account Products, Virtual Card Products, and ESP Variants

48. **Account Product scope** — Does an Account Product determine the currency of accounts created under it, or is currency inherited from the Credit Facility? What is the relationship between an Account Product and a Credit Facility — can a single Account Product be used across multiple Credit Facilities?

> Yes; Currency should be same between Account Product and Credit Facility
> Account Product doesn't recognize Credit Facility. Credit Facility is associated per Account


49. **Virtual Card Product scope** — Does a Virtual Card Product define the card network (Visa, Mastercard, private label)? Does it define physical vs virtual form factor, or is that a separate concern?
> The Card Product could support multi-network and multi-clearing-houses. A Bank chooses which card schemes to make available and which card scheme card to issue when a card is requested. Irrespective of the scheme to which a card belongs to the transactions may be presented through multiple payment networks if the bank has such relationships. 
> A Card Product provides all the details for a specific product arrangement.
> Settlement to various networks' is bank's obligation
> Dispute resolution is also bank's obligation

50. **ESP Account Variant composition** — When the ESP creates an Account Variant (Fee Programs, Interest Programs, Statement Program, Reward Programs, Rebate Programs), are these overrides on top of the bank's base programs, or does the ESP define them from scratch within bank-defined constraints? For example, can the bank's Account Product define a base fee schedule that the ESP can only reduce but not exceed?

> ESP can make all commercial choices in the scope of the programs accessible to the ESP
> Bank's base programs are fallback for cases an ESP may not have overriden.
> ESP can reduce fees and charges as they may need. 
> The charges made to Bank may or may not represent revenue to bank. It is based on the arrangement between Bank and ESP
> Bank will not let ESP control Credit Risk, AML, and other compliance related parameters. They are exclusively managed by the bank.

51. **ESP Virtual Card Variant composition** — Same question for Virtual Card Variants. Are the component programs (Embossing, Spend/Payment Usage, Authentication, Tokenisation, 3DS, Card Fee) bank-defined with ESP overrides, or ESP-defined within bank constraints?

> Same as above. All commercial and operational parameters are available for the ESP.
> Compliance, Fraud Risk params are not accessible. They are exclusively managed by Bank
> However, for a limited scope Bank provides User-Managed-Risk parameters to ESP and the Cardholder as well. They are discussed in the FRM documentation


52. **Corporate Payment Product assembly** — Does a Corporate Payment Product reference exactly one ESP Account Variant and one ESP Virtual Card Variant? Or can a CPP combine multiple variants?
> Only one

53. **Variant reuse** — Can multiple Corporate Payment Products share the same ESP Account Variant or ESP Virtual Card Variant? For example, could Apex's Supplier Payments Product and Employee Spend Product both use the same Account Variant but different Virtual Card Variants?
> Yes
> But it the ESP is free to create dedicated variants for customer as they may need for large customers
> The variants can give branding options for card, statements, notifications, etc.,

54. **Redistributable** — You described the bank's products as "redistributable." Does this mean a single Account Product or Virtual Card Product can be used by multiple ESPs? Or is each product created specifically for one ESP?
> Can be used by multiple ESPs.


55. **Rewards and Rebates computation** — The bank provides account-level Rewards and Rebate computations. Is this the mechanism by which the ESP's rebate/reward programs (defined in the ESP Account Variant) are computed? Or is this a separate bank-side computation independent of the ESP's commercial terms?
> Yes, this is what ESP relies on.
> ESP system (Electron) provides its own mechanism for Relationship-level Rewards and Rebates

56. **Authorization enforcement** — You said "all processing should honour all the policies applicable to card and account." Does the bank enforce all Spend Policies (including ESP-level and Corporate-level policies) at authorization time? Or does the ESP also participate in the authorization decision (e.g., via a webhook or co-processing step)?
> Yes, bank enforces
> ESP and Corporate both have an option to participate in authorization processing. they can use it if the controls provided by bank are inadequate to meet their needs.

57. **Bank's journey in the book** — Should the Bank part cover the bank's journey from onboarding an ESP to making products available, similar to how Part III covers the ESP's journey and Part IV covers the Corporate's? Or should it be purely a reference section defining what the bank provides?
> It can cover the ESP Onboarding and Corporate's Legale Entities' onboarding journeys as well

58. **Account Product and Virtual Card Product catalogs** — Does the bank maintain a catalog of Account Products and Virtual Card Products that the ESP browses and selects from? Or is it more of a negotiation/request process where the ESP specifies requirements and the bank creates products to match?
>  Both

59. **State models** — Are there state models (e.g., Active, Deprecated, Retired) for Account Products, Virtual Card Products, ESP Account Variants, and ESP Virtual Card Variants?
> Yes. The state for Account Product and Virtual Card Product from the bank are out of scope for this document. The Variants' state modle can be discussed in this document.

60. **Bank-side controls beyond Spend Policy** — Beyond the Spend Policy cascade (Product → Program → Card), does the bank enforce any controls at the Account Product level that the ESP cannot override? For example, regulatory limits, network-mandated restrictions, or risk thresholds?
> Yes. All regulatory checks, bank-defined fraud checks, credit facility related restrictions, delinquency related controls, NPA tracking, complainces wrt. customer servicing are all handled and enforced by the bank.

---

## Notification Program

61. **Notification Program in ESP Account Variant** — What does the Notification Program at the Account Variant level configure? Is this about account-level notifications to the corporate (e.g., billing alerts, credit utilization thresholds, delinquency warnings, statement availability)? Who are the recipients — the Corporate's Program Admin, the Legal Entity contact, or configurable?
> yes. The recepients are typically the Corporate Users configured as Program Admins for the Corporate Payment Program to which the Account is mapped to.
> The Credit Facility related notifications are delivered to the configured contacts for the legal entity over and above the program level contacts.

62. **Notification Program in ESP Virtual Card Variant** — What does the Notification Program at the Virtual Card Variant level configure? Is this about card-level notifications (e.g., transaction alerts to the cardholder, authorization declines, card expiry reminders)? Are these delivered to the cardholder specified in the Card Profile, or are there additional notification recipients (e.g., Program Admin copied on decline alerts)?
> Yes. These are delivered based on the Cardholder Profile Information.
> These include SMS, Email OTP notification for second-factor authentication


63. **Notification channel and customization** — What notification channels are supported (email, SMS, push, webhook/API callback)? Can the ESP customize notification templates per Variant (branding, language, content)? Can the Corporate further customize at the Program or card level?
> Yes to all
> All notification template changes go through review from the bank execs

64. **Bank vs ESP notification boundary** — Are there bank-originated notifications (e.g., regulatory disclosures, fraud alerts) that the ESP cannot override or suppress? If so, how do these interact with the ESP's Notification Program?
> ESP cannot supress but suggest templates.
