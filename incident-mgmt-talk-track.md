# Incident Management – Agentic AI Demo Talk Track (5 Minutes)

> **Instructions:** This talk track is designed for a 5-minute screen-recorded demo. Each section has an approximate timestamp. Speak at a natural, confident pace. Pause briefly between sections to let visuals land.

---

## [0:00 – 0:30] Opening — Ticket Creation & Escalation

In today's network operations, incidents come from many directions — automated fault detection picking up syslogs and alarms, or directly from a customer calling in to report a problem.

Here, a ticket has just been created in our ticketing system. You can see the ticket details — the problem description, severity level, and the attached logs.

Now, the NOC Level-1 engineer reviews this ticket and decides it needs deeper investigation. With one click, they escalate it to Cisco AI.

---

## [0:30 – 1:00] IO Agent — Initial Interaction

The IO Agent immediately picks up the ticket. It reviews the full context — the problem statement, attached logs, fault snippets — everything.

If it needs more information, it asks targeted follow-up questions. No guesswork — just precise, relevant questions to fill in the gaps.

Once it has enough context, it automatically triggers the investigation workflow. The engineer doesn't need to decide which tools to run or where to look — the AI handles that.

---

## [1:00 – 1:30] Background Reasoning & MRA Activation

Behind the scenes, the IO Agent is doing something powerful. It's categorizing the problem, understanding the customer's intent, and mapping it to relevant use cases.

It decides to invoke the Master Reasoning Agent — the MRA — which is the brain of our agentic system.

The MRA starts gathering data from multiple sources — our Knowledge Graph, retrieval-augmented generation for relevant documentation, network topology, device states, protocol information, live telemetry, and alternate paths.

You can see the progress logs updating in real time as data flows in.

---

## [1:30 – 2:10] Specialized Agents — Deep Troubleshooting

Now, based on the data it's gathered, the MRA makes a critical decision — which specialized agents to deploy.

In this case, it's activating our BGP, IGP, and MPLS agents. Each of these agents is a domain expert. The BGP agent checks peering sessions, route advertisements, and path selection. The IGP agent examines adjacencies, SPF computations, and metric changes. The MPLS agent verifies label paths and forwarding entries.

They perform deep, domain-specific troubleshooting — the kind that would normally take a senior engineer hours — and send their findings back to the MRA.

---

## [2:10 – 2:50] Root Cause Analysis

This is where the real power of agentic AI shows up.

The MRA correlates all the findings from the specialized agents and identifies the precise root cause — with supporting evidence and a confidence score.

Look at this — it clearly tells us what happened, why it happened, where in the network it happened, and what the business impact is. This is an executive-friendly summary that you can share directly with management or the customer.

The IO Agent has also generated a detailed RCA report as a downloadable PDF — complete with the full timeline, analysis steps, evidence chain, and recommendations. This gets attached to the ticket automatically.

---

## [2:50 – 3:20] Remediation — Feasibility Check

Now, the IO Agent asks us a simple question — do we want to check if this issue can be remediated through a configuration change?

We click yes, and the MRA evaluates the feasibility. It analyzes the root cause against the network's configuration capabilities and determines — yes, this can be fixed with a configuration change. No physical intervention needed.

---

## [3:20 – 4:10] Configuration Generation, Approval & Deployment

The IO Agent now invokes our Intent-Driven Configuration Agent. This agent takes the remediation intent, applies the relevant constraints and policies, and generates the proposed configuration.

You can see the exact changes right here on screen. Nothing is hidden — full transparency.

And this is a critical point — we have a human-in-the-loop checkpoint. Nothing goes to the network without explicit human approval. The engineer reviews the configuration and approves it.

Before we touch the live network, we run a dry run through NSO — that's our Network Services Orchestrator. It validates the configuration against the current network state, checks for conflicts, syntax issues, and policy violations. The dry run passes.

Now we deploy. The configuration is pushed to the network through NSO, and you can see the live status updates — device by device — as it rolls out. Configuration applied successfully.

---

## [4:10 – 4:50] Verification & Ticket Closure

Post-deployment verification kicks in automatically. The system confirms that service metrics are back to normal and all health checks have passed. The fix is working.

And here's the final step — the AI goes back to the ticketing system, updates the ticket with the full RCA summary, attaches the RCA report, and sets the ticket status to "Close Pending" — ready for final review and sign-off by the operations team.

---

## [4:50 – 5:00] Closing

And that's the complete journey — from ticket creation to root cause analysis to remediation to closure. All orchestrated by Cisco's Agentic AI. What used to take hours of manual troubleshooting by senior engineers is now handled in minutes — with full transparency, human oversight, and a complete audit trail.

Thank you.

---

## Timing Summary

| Section | Duration | Cumulative |
|---------|----------|------------|
| Opening — Ticket Creation & Escalation | 30s | 0:30 |
| IO Agent — Initial Interaction | 30s | 1:00 |
| Background Reasoning & MRA Activation | 30s | 1:30 |
| Specialized Agents — Deep Troubleshooting | 40s | 2:10 |
| Root Cause Analysis | 40s | 2:50 |
| Remediation — Feasibility Check | 30s | 3:20 |
| Config Generation, Approval & Deployment | 50s | 4:10 |
| Verification & Ticket Closure | 40s | 4:50 |
| Closing | 10s | 5:00 |
