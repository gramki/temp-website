
Exclusive section on testing requirements 
Transaction Product Definition
Gateway as a Channel Provider in Athena 
Egress Proxy as the Connector

Origination Chanel Product
- Authorized Originators
- Originating Payment Account
- - Clearing House Payment Account
- - Account Holder Payment Account
- Destination Payment Account
- - Clearing House Payment Account
- - Account Holder Payment Account
- An Issuer Wallet should also be interepreted as a Payment Account; (Wallet extends Payment Account)
- Orignator message always correspond to an Originating Payment Account
- Originating Channel should always specify the Destination Payment Account using one the supported vector formats in the Originator Message; 
- - If the Destination Payment Account is a wallet, then switch translates it to multiple destination payment accounts based on the policies associated with the wallet

Destination Channel Product 



Payment Account Provider, Authorization Gateway, and Channel

All Authorization Gateways in Athena 2.0 should be called as Destination Channel Providers in the Athena 3.0 terminology
Each Desintation Channel has:
- Clearing House Relationship 
- Clearing House Accounts for Receivables, Payables
- Pending Message Chains
Each Payment Request represents a Message Chain of an Origination Channel and may correspond to one or more Destiantion Messages across one or more Destination Channels


> What is the relationship between Payment Account and a Destination Channel? Does a Payment Account belong to a Destination Channel?
> Payment Intrument corresponds to Destination Payment Account
> Should Originating Channel always use a Payment Instrument?
> Should therefore the word Payment Account always mean a Destination Payment Account?
> When a merchant is pulling funds into a Counter ledger, what is the Payment Instrument, Origination Payment Account, Destination Payment Account?
> Destination Channel Accounting and Origination Channel Account should be segreated. [TBD]



Originator could have initiated a Push or Pull.
Destination could be an interal system of the bank or an external network.
Payment Account vs. Clearing House Account.

Wite a clear document to the Athena team.


Kernel (aka APMS) as an originator {Payer initiated transfers/Giro}
- Payment Accounts registered will recognize public key of the kernel as a credential (payment instrument)
- Payment workflow determines the Clearing House Account as a destination (usually for push of credit to the destination account)

Collection Hub as an Originator {Payee initiated requests/Pull}
- Two cases for the Collection Hub to configure Payment Account:
- - Payment Account is of either of the banking institution itself; This in cases where the bank first wants to collect funds into its account and then push to customer account after due business process.
- - Payment Account is of the customer.
- Destination account is a Clearing House Account or a Payment Account