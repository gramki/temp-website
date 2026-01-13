

Sentinels as Employed Agents - 

Scenario Scoped (Employed for observing Scenarios or Observing and Participating in every request of the Scenario)
Workbench Scoped (Employed for observing Workbench or Observing and Participating in every request of the Workbench - filters to whitelist/blacklist scenarios)
Subscription Scoped (Employed for observing Workbench or Observing and Participating in every request of the Subscription - filters to whitelist/blacklist Workbenches and Scenarios)


Cognitive Operations Governance Workbench
----

Every Subscription of Seer comes with COGW. Sentinels defined here can be assigned to all or multiple workbenches.
There can be any number of COGW workbenches in a Subscription. Any Workbench can be defined as a COGW in its specification. All the instances of that Workbench will be COGW instances.


Purpose of COGWs is to handle subscription-wide cognitive operatiosn - multi-domain, 

Subscription Scoped Sentinels are auto entrolled in every Workbench of the Subscription. The Scenario corresponding to the sentinel is represented as a local scenario and is activated for all triggers it is associated in the wokbench. 

Each Sentinel is a Scenario in the Workbench activated by request updates to the eligible requests as signals. If a sentinel is participating in a Request, then the sentinel's request is a child request.




X-Workbench Scenarios as children to the parent request. If the source workbenches allow continuation of context and destination workbench authorizes linking of scenario to parent context of the source workbench scenario, then x-workbench context sharing happen. The Parent request and its full context becomes visible to the child across workbenches.

COGW Sentinels by default have x-workbench context sharing from all other workbenches.

