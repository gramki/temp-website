
Istio, SLIME, Aeraki
Ensure agent traffic is distributed to specific hosts of the agents. This will not be a problem if we adopt MCP as the interfacing protocol for all Agents and using Streaming HTTP transport for MCP. This will at least ensure that a session will mostly remain sticky. However, even in that scenario, if we have to direct all agents of a User or a specific Session to the same agent application after a session is disconnected (stateful sessions), then we will need sticky routing.

https://tetrate.io/blog/introducing-slime-and-aeraki-in-the-evolution-of-istio-open-source-ecosystem


SLIM RPC - https://docs.agntcy.org/messaging/slim-rpc/
There is no open source project yet that implements this on top of Istio.
For the time being we should stick to Istio based agent to agent communication. Leverage the Istio enhancements for all the workload in the k8s environment, not just the agentic workload.

Streamable HTTP Transport
------------------------

* Tracing support by events or MCP session
* MCP Endpoint Access Control


* Session Authentication and Access Control