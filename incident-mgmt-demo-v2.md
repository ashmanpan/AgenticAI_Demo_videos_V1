# Incident Management – Agentic AI Demo Story (v2)

## 1. Ticket creation and escalation to Cisco AI
A ticket is created in the ticketing system either by automated fault detection (syslogs, alarms) or by a call from an end customer. The ticket is now visible in the ticketing system. The NOC L1 engineer reviews the ticket and escalates it to Cisco AI for investigation.

## 2. Initial interaction by IO Agent
The IO Agent reviews the ticket context and asks targeted follow-up questions if additional details are required.

## 3. Triggering investigation workflow
Once sufficient information is collected, the IO Agent triggers the investigation workflow automatically.

## 4. Background reasoning and orchestration
The IO Agent categorizes the problem, understands customer intent, maps it to relevant use cases, and decides to invoke the Master Reasoning Agent (MRA). Only high-level logs are visible.

## 5. MRA activation and data acquisition
The MRA gathers data from Knowledge Graph, RAG, topology, device states, protocols, telemetry, and alternate paths. Progress logs are shown on UI.

## 6. Decision on specialized agents
MRA decides which specialized agents (BGP, IGP, MPLS, SR, L2/L3, etc.) are required and deploys them. Deployment logs are visible.

## 7. Specialized troubleshooting
Specialized agents perform domain-specific troubleshooting and send findings back to MRA.

## 8. Root cause synthesis
MRA correlates all inputs and identifies the precise root cause with evidence.

## 9. Result handoff to IO Agent
MRA hands over findings including root cause, affected components, evidence, and confidence score to IO Agent.

## 10. Executive-friendly UI summary
IO Agent displays a clear summary: what happened, why, where, and business impact.

## 11. Downloadable RCA report
IO Agent generates a detailed PDF report for download and attachment to the ticketing system.

## 12. Remediation feasibility prompt
IO Agent asks the user if they want to check feasibility for remediation via configuration changes.

## 13. Feasibility analysis by MRA
MRA evaluates whether the issue can be remediated via configuration or requires physical intervention.

## 14. Feasibility decision
MRA communicates a clear decision (configurable or physical fix required) back to IO Agent.

## 15. Intent-driven agent invocation
If configurable, IO Agent invokes the Intent-Driven Configuration Agent with intent, constraints, and policies.

## 16. Configuration generation
Intent-Driven Agent generates the proposed configuration and displays it on IO Agent UI.

## 17. Human approval checkpoint
User reviews the generated configuration and approves or rejects it.

## 18. Dry-run execution
Upon approval, a dry run is executed using NSO and results are shown on UI.

## 19. Final configuration deployment
If dry run is successful, the configuration is pushed to the network using NSO with live status updates.

## 20. Verification and ticket closure
Post-deployment verification is completed. The AI updates the ticketing system ticket with the RCA summary, attaches the RCA report, and sets the ticket status to **close pending** for final review and sign-off.
