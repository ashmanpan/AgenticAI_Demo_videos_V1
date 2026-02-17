# New Use Case Videos — Narration Scripts & Build Plan

**Created:** 2026-02-17
**Status:** DRAFT — Awaiting approval before building

## Structure (all 3 videos)
- OTAP intro (20s) with Sarah voice
- Narrated demo clips (speed-adjusted to narration)
- White slide with use-case-specific closing text
- Cisco logo ending (7s) from original OTAP video
- Quality: CRF 18, slow preset, 192kbps AAC

## Source Videos
- `other use cases/Usecase8-Intent-Driven-Config-Generation-Demo.mov` (247s, 3456x1966)
- `other use cases/Zerotrust_config_guardian-agent.mov` (189s, 3448x1982)
- `other use cases/audit_agent_demo.mp4` (601s, 1920x1080)

---

## Video 1: Intent-Driven Config Generation (~4 min total)

**Final target:** ~232s (3:52)
**Structure:** OTAP intro (20s) + 8 sections (~200s) + white slide (5s) + Cisco ending (7s)

### OTAP Intro Text (20s)
"Welcome to OTAP — the Open Telco AI Platform. In this demo, we'll see how Cisco's Agentic AI enables intent-driven configuration generation — where engineers describe what they need in natural language, and AI agents handle the rest."

### Narration Sections

| # | Name | Source Clip | Clip Dur | Target Dur | Narration |
|---|------|------------|----------|------------|-----------|
| 1 | uc8_01_request | 0–20s | 20s | 14s | "An engineer needs to configure a loopback interface on an IOS-XR PE router. They simply describe the intent in natural language — and the Cisco AI Assistant takes over." |
| 2 | uc8_02_analysis | 20–55s | 35s | 16s | "The system performs intelligent analysis — classifying this as a Network Transport configuration task. The intent config generation agent is selected with ninety-two percent confidence." |
| 3 | uc8_03_config_questions | 55–100s | 45s | 20s | "The agent asks targeted questions — hostname, interface description, and deployment parameters. This interactive workflow ensures the configuration matches the engineer's exact requirements." |
| 4 | uc8_04_payload_review | 100–145s | 45s | 22s | "A complete JSON configuration payload is generated — specifying the loopback interface, IP address, and all required parameters for device NVMBOTAPAAR002. The engineer can review every detail before proceeding." |
| 5 | uc8_05_modification | 145–185s | 40s | 20s | "The engineer requests a modification — changing the loopback ID to 100. The agent instantly regenerates the payload with the updated configuration, demonstrating real-time adaptability." |
| 6 | uc8_06_pool_selection | 185–210s | 25s | 14s | "The system presents pool selection options. The engineer selects the IPv4 pool and confirms the final configuration for deployment." |
| 7 | uc8_07_deployment | 210–240s | 30s | 14s | "After dry-run validation, the configuration is deployed successfully — one of one devices configured. All configurations applied to NVMBOTAPAAR002." |
| 8 | uc8_08_closing_slide | white slide | — | 5s | "Cisco Agentic AI — Intent-Driven Configuration Generation. From natural language to deployed configuration." |

---

## Video 2: Zero-Trust Config Guardian (~3.5 min total)

**Final target:** ~192s (3:12)
**Structure:** OTAP intro (20s) + 7 sections (~160s) + white slide (5s) + Cisco ending (7s)

### OTAP Intro Text (20s)
"Welcome to OTAP — the Open Telco AI Platform. In this demo, we'll see the Zero-Trust Configuration Guardian in action — an AI agent that continuously monitors network devices for unauthorized configuration changes and ensures compliance."

### Narration Sections

| # | Name | Source Clip | Clip Dur | Target Dur | Narration |
|---|------|------------|----------|------------|-----------|
| 1 | zt_01_dashboard | 0–25s | 25s | 14s | "In the ServiceNow dashboard, a new incident is flagged — unauthorized configuration changes detected on a critical network device." |
| 2 | zt_02_escalation | 25–55s | 30s | 16s | "The engineer escalates the ticket to Cisco's Agentic AI. The system immediately begins analysis — selecting the Zero-Trust Config Guardian agent with eighty-nine percent confidence and ninety-four percent match." |
| 3 | zt_03_device_analysis | 55–85s | 30s | 18s | "The agent connects to router NVMBOTAPAAR002 and begins a comprehensive analysis of all configuration changes — comparing the current state against the authorized baseline." |
| 4 | zt_04_compliance | 85–115s | 30s | 20s | "The Zero-Trust Compliance Analysis reveals a critical finding — the device is NON-COMPLIANT with HIGH risk severity. Unauthorized changes have been detected across multiple configuration sections." |
| 5 | zt_05_findings | 115–150s | 35s | 22s | "The agent identifies specific violations — a BGP VPNv4 Unicast neighbor deletion and unauthorized SNMP configuration modifications. Each change is analyzed for security impact and intent classification." |
| 6 | zt_06_llm_analysis | 150–180s | 30s | 16s | "An LLM-powered intent analysis provides dual comparison results — evaluating whether each change was intentional or potentially malicious. The complete configuration change analysis finishes in thirty-six seconds." |
| 7 | zt_07_closing_slide | white slide | — | 5s | "Cisco Agentic AI — Zero-Trust Configuration Guardian. Continuous compliance monitoring and unauthorized change detection." |

---

## Video 3: Audit Agent (~5.5 min total, condensed from 10 min)

**Final target:** ~322s (5:22)
**Structure:** OTAP intro (20s) + 11 sections (~290s) + white slide (5s) + Cisco ending (7s)

### OTAP Intro Text (20s)
"Welcome to OTAP — the Open Telco AI Platform. In this demo, we'll see the Cisco Audit Agent — an AI-powered tool that performs comprehensive network security audits, generates detailed reports, and can automatically create remediation configurations."

### Narration Sections

| # | Name | Source Clip | Clip Dur | Target Dur | Narration |
|---|------|------------|----------|------------|-----------|
| 1 | audit_01_intro | 0–30s | 30s | 12s | "The Cisco Audit Agent provides comprehensive network security auditing. Engineers can request any audit — from targeted protocol checks to full security assessments." |
| 2 | audit_02_ssh_request | 30–60s | 30s | 14s | "The engineer asks the agent to check if SSH is properly configured and secure. The system immediately begins correlating data points and generating the audit report." |
| 3 | audit_03_ssh_results | 60–110s | 50s | 22s | "The SSH audit is complete — six checks performed, generating a comprehensive thirteen-page PDF report. The executive summary shows a health score of forty-one point seven percent — rated as Poor, indicating significant security gaps." |
| 4 | audit_04_ssh_details | 110–160s | 50s | 20s | "The report details each finding — SSH version compliance, key exchange algorithms, authentication methods, and access control configurations. Each issue includes specific mitigation steps." |
| 5 | audit_05_bgp_request | 160–210s | 50s | 14s | "Next, the engineer requests a BGP neighbor analysis — checking if all peering sessions are stable and properly configured." |
| 6 | audit_06_bgp_results | 210–280s | 70s | 24s | "The BGP audit completes — twelve checks performed, producing a twenty-four page report. The analysis covers neighbor status, session stability, prefix counts, and routing policy compliance for every BGP peering session." |
| 7 | audit_07_full_audit_request | 280–320s | 40s | 14s | "For the most comprehensive assessment, the engineer requests a complete security audit — covering all protocols and security configurations on the device." |
| 8 | audit_08_full_audit_results | 320–400s | 80s | 28s | "The full security audit is complete — fifty-five checks across custom and security categories, generating an eighty-four page report. The results table shows a mix of Pass, Fail, and Warning states across dozens of security controls — from interface hardening to protocol security." |
| 9 | audit_09_mitigation | 400–470s | 70s | 24s | "For each failed check, the agent provides detailed mitigation steps and recommended configurations. The compliance analysis identifies critical items requiring immediate attention — including control plane security, routing protocol hardening, and access management." |
| 10 | audit_10_config_gen | 470–560s | 90s | 26s | "The Audit Agent goes beyond reporting — it offers to generate remediation configurations directly. Using the intent-driven config generation agent, it produces ready-to-deploy JSON configuration payloads that address the identified security gaps." |
| 11 | audit_11_closing_slide | white slide | — | 5s | "Cisco Agentic AI — Comprehensive Network Audit Agent. From security assessment to automated remediation." |

---

## Summary

| Video | Source Duration | Final Duration | Sections |
|-------|----------------|----------------|----------|
| Intent-Driven Config | 247s (4:07) | ~232s (3:52) | 8 + OTAP + Cisco |
| Zero-Trust Guardian | 189s (3:09) | ~192s (3:12) | 7 + OTAP + Cisco |
| Audit Agent | 601s (10:01) | ~322s (5:22) | 11 + OTAP + Cisco |
