# AI Canvas + Crosswork AI Demo Scripts

## Script-1

| Frame | Visual | Talk Track | Notes |
|-------|--------|------------|-------|
| **1** | Message from @crossworkAI that network issues have been detected in the network, with a link for more info. | One of the biggest advantages of agentic operations is that you can have persistent agents that constantly scan for issues - compliance, security, performance - you name it. Looks like one of our Crosswork Network Controller AI agents has detected an anomaly on the network. Delay is up <%> compared to baseline values. Let's see what is happening [click on 'more' link] | **Message shown in C3:** "Severity Level: High. An anomaly has been detected for service <service id, service name> with service endpoints <blah>. An increase of <x%> compared to baseline delay values has been detected. To analyze this issue in AI Canvas, go to <link>." |
| **2** | AI Canvas window opens the associated board with the AI Assistant showing the same message ("An anomaly has been detected for service <service id>. An increase of <x%> compared to baseline delay values has been detected"). User clicks to add a card to the canvas with the message details (card-1). | | |
| **3** | AI Assistant responds with thinking process and analysis. The following cards are added to the board: **Card-2:** Line chart with delay of service <service id> over time (e.g., last week) – may also include baseline info. **Card-3:** Expanded service assurance graph showing everything "green" – except for the path SLA node and the PE-A VPN node and respective child nodes reporting symptoms. **Card-4:** Topology view with traversed nodes/links highlighted in another color. | Crosswork AI fetches information to analyze what's happening along the service path. Based on service assurance graph analysis, degradation issues have been identified on the transport level. Furthermore, a path change has been identified around the anomaly detection time. The recommendation is to check for anomalous configuration changes that may have caused this. | **AI Assistant Thinking:** "Checking with Crosswork AI. Fetching information from PCA and CNC. Analyzing service assurance graph from CNC. Checking for health issues on associated devices. Two symptoms causing service health degradation. Both seem to be correlated as they are both reporting latency spikes between the same endpoints (PE-A, PE-B). Checking for delay increases on the links along the service path. The links along the service path have not experienced delay increases. Checking event history for associated SR policy. A path change has been identified for the SR policy within the past hour. Potential reason for path change could be a configuration change. Recommendation: Check for anomalous configuration changes." |
| **4** | User invites additional Operations/Engineering folks to the board – via "Share", "Generate AI Summary", and "Invite". | This isn't the kind of issue you want to troubleshoot alone. Let's share this board with additional folks to work on this together. Now, we'll follow the suggestion and run the configuration drift detection agent to check for anomalous network configurations. | |

---

## Configuration Drift Detection

| Frame | Visual | Talk Track | Notes |
|-------|--------|------------|-------|
| **4 (cont.)** | AI Assistant responds with configuration drift analysis. **Card-6:** Table showing anomaly details. **Card-7:** Network plot view highlighting devices <x,y>. | We can see that configuration anomalies have been detected on two devices which are not along the service path. There is a misconfiguration in device <x> that impacts path computation. Looks like we found the culprit. There is also another anomaly detected on device <y> that is unrelated – but quite suspicious. Even though there doesn't seem to be an immediate impact to the network, let's address this "silent issue" now as well and not wait for the next scheduled configuration drift detection run. Note that we did not have to instruct or pre-train against golden configs. The agent knew what to look for—it analyzed the whole network to determine what "normal" looked like, then looked for deviations where there shouldn't be. | **AI Assistant Thinking:** "Checking with Crosswork AI for configuration drift. Checking for devices with configuration changes since latest scheduled configuration drift detection run. Configuration changes identified for devices <x> and <y>. Fetching configurations. Analyzing configurations against configuration language models. Preparing results. Device <x> has 1 anomaly. Device <y> has 1 anomaly" |

---

## Anomaly Details (Card-6)

| Device | Anomaly Type | Line | Description | Confidence Level | Recommended Change |
|--------|--------------|------|-------------|------------------|-------------------|
| Device <x> | Misconfiguration | interface TenGigE0/0/0/2 | Red affinity configured on the wrong interface - resulting in a path with exclude constraints on red affinities rerouting to avoid this interface, thus causing the delay spike | High | `-interface TenGigE0/0/0/2 affinity flex-algo red blue` → `+interface TenGigE0/0/0/2 affinity flex-algo blue` |
| Device <y> | Salt Typhoon type silent issue | tacacs-server config | Suspicious tacacs-server configuration detected | High | `-tacacs-server login host 10.15.1.12 vrf management seq-num 2 key 7 0x960c890a272610d6aca0 port` |

---

## Remediation

| Frame | Visual | Talk Track | Notes |
|-------|--------|------------|-------|
| **5** | AI Assistant responds with remediation plan. **Card-8:** Info on changes performed and the option to revert the change. **Card-9:** Confirmation that delay is back to normal for service <service id>. | With this information, we can use the Crosswork Network Controller to get the recommended remediation plan to restore normal network operations. From here we have options: we can do a dry-run, export the plan for a separate change process, or deploy it directly. But we'll proceed with deploying the recommended remediation plan. The assistant applies the changes - two new cards appear - one capturing what was changed and another confirming the service has been recovered. | **AI Assistant:** "Proceeding with recommended plan: Applying configuration change to device <x> via CNC. Applying configuration change to device <y> via CNC." Optional: AI Assistant indicates: "Waiting for service recovery." After some time: "Service delay has been restored to baseline levels" |

---

## Report Generation

| Frame | Visual | Talk Track | Notes |
|-------|--------|------------|-------|
| **6** | User requests AI Canvas to generate a detailed report. | Now that we've averted disaster, we can do some sleuthing and figure out who made those changes! Using built-in capabilities of AI Canvas, we can easily generate a detailed report to capture the issue and actions taken. | |

---

## Cards Summary

| Card | Content |
|------|---------|
| Card-1 | Initial anomaly message details |
| Card-2 | Line chart with delay of service over time (last week) with baseline info |
| Card-3 | Expanded service assurance graph (green except path SLA node and PE-A VPN node) |
| Card-4 | Topology view with traversed nodes/links highlighted |
| Card-6 | Anomaly details table (Device, Anomaly Type, Line, Description, Confidence Level, Recommended Change) |
| Card-7 | Network plot view highlighting devices with anomalies and service path |
| Card-8 | Changes performed with revert option |
| Card-9 | Service recovery confirmation - delay back to normal |
