#!/usr/bin/env python3
"""
Build MWC Demo videos — Production Quality for MWC

  1. FULL version: OTAP intro (Sarah voice) + full demo (adelay) + Cisco ending
  2. 200s version WITH VOICE: OTAP intro + condensed incident mgmt + DC use case highlights + Cisco ending
  3. 200s version WITH CAPTIONS (no voice): same as #2 but with burned-in subtitles
  4. 300s version: OTAP intro + detailed incident mgmt + security guardrails + DC use case + Cisco ending

Sources:
  - MWC-Demo.mov (433s) — Incident management demo (BGP/HDFC)
  - Cisco Jio OTAP 4.47 V5.3.mp4 (287s) — DC/Broadband use case (AirFiber/FTTH Dombivli)

Quality: CRF 18, preset slow, 192kbps AAC
"""

import requests
import subprocess
import os
import sys

# ============================================================
# CONFIG
# ============================================================
API_KEY = "sk_52d77f794842aed90bce399924e980037d15ee87454bd591"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Sarah
MODEL = "eleven_multilingual_v2"
VOICE_SETTINGS = {
    "stability": 0.6,
    "similarity_boost": 0.85,
    "style": 0.3,
    "use_speaker_boost": True
}
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
HEADERS = {"xi-api-key": API_KEY, "Content-Type": "application/json"}

WORK = "/home/kpanse/wsl-myprojects/MWC-story/intermediary"
FINAL = "/home/kpanse/wsl-myprojects/MWC-story/final-videos"
VIDFILE = "/home/kpanse/wsl-myprojects/MWC-story/MWC-Demo.mov"
OTAP_VID = os.path.join(WORK, "Cisco Jio OTAP 4.47 V5.3.mp4")
RESOLUTION = "1920:1080"

# Encoding quality — MWC production
CRF = "18"
PRESET = "slow"
AUDIO_BITRATE = "192k"


# ============================================================
# NARRATION DEFINITIONS
# ============================================================

OTAP_INTRO_TEXT = (
    "Welcome to OTAP — the Open Telco AI Platform. "
    "Cisco's vision for network automation is evolving from traditional rules-based systems "
    "to autonomous, self-learning, multi-agent Agentic AI. "
    "In this demo, we'll walk through a complete Incident Management workflow — "
    "powered by Cisco's Agentic AI — including interactive Q&A and built-in security guardrails."
)

# --- FULL VERSION sections (14 sections, 433s total) ---
FULL_SECTIONS = [
    {"name": "s01_ticket_creation", "start": 0, "end": 8,
     "text": "A BGP Session Instability incident affecting HDFC banking operations is reported. The engineer creates a new ServiceNow ticket."},
    {"name": "s02_escalation", "start": 8, "end": 30,
     "text": "The ticket is visible in the dashboard. With a single click on Escalate to AI, the ticket is handed off to Cisco's Agentic AI. The escalation is confirmed — a new ticket ID is generated, and the engineer navigates to the AI Chat to monitor the investigation."},
    {"name": "s03_io_agent", "start": 30, "end": 55,
     "text": "The Cisco AI Assistant opens. The IO Agent immediately picks up the escalated ticket and begins its analysis — reviewing the customer impact, device context, and problem classification. With a ninety-two percent match score, it identifies this as a critical BGP incident requiring immediate intervention and automatically triggers the Master Reasoning Agent."},
    {"name": "s04_data_acquisition", "start": 55, "end": 80,
     "text": "The system begins automated device lookup and data acquisition. It retrieves the device details for NVMBOTAPAAR002 — a Cisco IOS-XR router running SR-MPLS, I.S.I.S., and MPLS protocols. The interface configuration is pulled, showing three active Gigabit Ethernet interfaces with their protocol states, IP addresses, and utilization metrics."},
    {"name": "s05_topology", "start": 80, "end": 100,
     "text": "The network topology is mapped — revealing four interconnected devices and six connections with three neighboring routers. The investigation reaches eighty-five percent progress. The MRA now has a complete picture of the network environment surrounding the affected device."},
    {"name": "s06_specialist_agents", "start": 100, "end": 155,
     "text": "Based on the data gathered, the MRA deploys three specialist agents — an L2 Agent for BFD analysis, an I.S.I.S. Agent for IGP verification, and a BGP Agent for session-level troubleshooting. Tasks are published to the specialist queues, and the agents begin their deep, domain-specific analysis. Each agent is an expert in its protocol domain — they know exactly what to check, what data to collect, and how to correlate findings. You can see the real-time progress updates as they analyze operational states and configurations across the network."},
    {"name": "s07_bgp_findings", "start": 155, "end": 195,
     "text": "The specialist agents continue their deep analysis — L2 examining BFD sessions, I.S.I.S. verifying routing stability, and BGP running session-level diagnostics. As the results emerge, the BGP Agent identifies the core issue — session instability caused by control-plane keepalive failures on the affected neighbor. The session has been up for eight weeks, receiving only one prefix — a clear sign of flapping. The message count imbalance confirms control-plane packet loss. The agent traces this to misconfigured timers on the neighbor-group — values too aggressive for stable BGP adjacency. Root cause analysis and remediation recommendations are now being prepared."},
    {"name": "s08_rca_pdf", "start": 195, "end": 240,
     "text": "The analysis is complete. The root cause is confirmed — the BGP neighbor-group on the affected device lacks appropriate timer configuration, causing intermittent prefix withdrawal affecting HDFC banking operations. A detailed PDF report has been generated and is ready for download. The engineer can also ask follow-up questions or view the detailed analysis. Now, the IO Agent asks a critical question — shall we proceed with configuration generation to fix the issues, if possible? The engineer clicks Yes, Proceed."},
    {"name": "s09_config_approval", "start": 240, "end": 290,
     "text": "The MRA has analyzed the issues and identified a configuration change that can resolve the problem. The recommendation — CFG-001 for the affected device — is to update the BGP neighbor timer configuration from aggressive to stable values. The engineer selects and approves the configuration. The system generates the complete configuration — updating timers to stable, recommended values for the affected neighbor-groups. The full configuration is displayed for review — every change is transparent. The engineer confirms and approves for deployment."},
    {"name": "s10_deployment", "start": 290, "end": 315,
     "text": "The configuration is pushed to the device. The deployment completes successfully — the status shows SUCCESS. All configurations deployed — one of one applied to device NVMBOTAPAAR002. Post-deployment verification begins immediately."},
    {"name": "s11_verification", "start": 315, "end": 345,
     "text": "Back in ServiceNow, the ticket status is updated — the incident is now marked as Completed. The AI Assistant confirms that the intelligent analysis is complete, with all configurations deployed successfully. The system is ready for the engineer to review the full resolution details and ask follow-up questions directly in the AI Chat."},
    {"name": "s12_qa_interaction", "start": 345, "end": 395,
     "text": "But the AI Assistant doesn't stop at resolution. The engineer can ask follow-up questions directly in the chat. When asked What was the root cause — the system provides a comprehensive response with supporting evidence, a detailed table of indicators and findings, and explains why this matters. It also shows the recommended fix with specific timer values. The engineer then asks about affected components, and the AI provides a structured breakdown — the primary root cause, neighbor-group configuration severity, inter-AS peering link issues, and the direct service impact on HDFC banking operations."},
    {"name": "s13_security_guardrails", "start": 395, "end": 425,
     "text": "Security is built in from the ground up. When the engineer attempts to extract router credentials — the message is immediately blocked by Cisco AI Defence. Similarly, when personally identifiable information like an email address is shared, AI Defence blocks it due to PII protection. These guardrails ensure the AI Assistant remains a secure, trustworthy tool — even when users test its boundaries."},
    {"name": "s14_closing", "start": 425, "end": 433,
     "text": "From ticket creation to verified remediation — powered by Cisco's Agentic AI. This is intelligent network operations."},
]

# ============================================================
# 200s VERSION: Incident Mgmt (condensed) + DC Use Case Highlights
# Structure: OTAP intro (27s) + demo clips (~166s) + Cisco ending (7s) = ~200s
# ============================================================
# "src" = "mwc" for MWC-Demo.mov, "otap" for OTAP video
NARR_200_SECTIONS = [
    # --- Incident Management (BGP/HDFC) condensed ---
    {"name": "n200_01_ticket_escalate", "src": "mwc", "clip_start": 0, "clip_dur": 12, "target_dur": 12,
     "text": "A network incident has been reported — BGP Session Instability affecting HDFC banking operations. The engineer creates a ticket and escalates it to Cisco's Agentic AI."},
    {"name": "n200_02_io_agent", "src": "mwc", "clip_start": 35, "clip_dur": 18, "target_dur": 14,
     "text": "The IO Agent picks up the ticket with a ninety-two percent match score and triggers the Master Reasoning Agent for deep investigation."},
    {"name": "n200_03_data_topology", "src": "mwc", "clip_start": 60, "clip_dur": 35, "target_dur": 16,
     "text": "The system retrieves device details and interface configurations. The network topology is mapped — four devices, three neighboring routers. Investigation at eighty-five percent."},
    {"name": "n200_04_specialists", "src": "mwc", "clip_start": 100, "clip_dur": 25, "target_dur": 14,
     "text": "The MRA deploys three specialist agents — L2, I.S.I.S., and BGP — for deep, domain-specific analysis across the network."},
    {"name": "n200_05_bgp_findings", "src": "mwc", "clip_start": 155, "clip_dur": 35, "target_dur": 20,
     "text": "The BGP Agent identifies session instability on the affected neighbor — keepalive failures with significant message count imbalance. The root cause: misconfigured timers on the neighbor-group, too aggressive for stable adjacency."},
    {"name": "n200_06_rca_config", "src": "mwc", "clip_start": 200, "clip_dur": 55, "target_dur": 18,
     "text": "Root cause confirmed. A PDF report is generated. The engineer approves configuration generation. CFG-001 updates BGP timers to stable, recommended values."},
    {"name": "n200_07_deploy_verify", "src": "mwc", "clip_start": 290, "clip_dur": 50, "target_dur": 16,
     "text": "Configuration deployed successfully. Post-deployment verification confirms — session flapping eliminated, HDFC banking operations restored. All symptoms resolved."},
    # --- DC / Broadband Use Case from OTAP ---
    {"name": "n200_08_dc_intro", "src": "otap", "clip_start": 30, "clip_dur": 35, "target_dur": 14,
     "text": "The platform handles diverse use cases. Here, a broadband service disruption in the Dombivli area is reported — affecting AirFiber-FTTH connectivity for twenty-five hundred users."},
    {"name": "n200_09_dc_topology_agents", "src": "otap", "clip_start": 110, "clip_dur": 45, "target_dur": 16,
     "text": "The Knowledge Graph maps the network topology. The MRA identifies nine relevant technologies and deploys six specialized agents — including BNG, QoS, and L3VPN MPLS agents."},
    {"name": "n200_10_dc_config_results", "src": "otap", "clip_start": 175, "clip_dur": 50, "target_dur": 16,
     "text": "The BNG Agent traces the issue to a VLAN misconfiguration. After approval and deployment, active subscriber count is restored. A comprehensive incident report is generated."},
    # --- Closing ---
    {"name": "n200_11_closing", "src": "mwc", "clip_start": 425, "clip_dur": 8, "target_dur": 6,
     "text": "From ticket creation to verified remediation — Cisco's Agentic AI for intelligent network operations."},
]

# --- 200s CAPTION VERSION ---
CAPTIONS_200 = [
    {"start": 0, "end": 12,
     "text": "Incident: BGP Session Instability\\naffecting HDFC banking operations"},
    {"start": 12, "end": 26,
     "text": "IO Agent: 92% match score\\nMaster Reasoning Agent triggered"},
    {"start": 26, "end": 42,
     "text": "Device: NVMBOTAPAAR002 (IOS-XR)\\nTopology: 4 devices, 3 neighbors"},
    {"start": 42, "end": 56,
     "text": "Specialist Agents deployed: L2 + I.S.I.S. + BGP\\nDomain-specific analysis begins"},
    {"start": 56, "end": 76,
     "text": "BGP Agent: Keepalive failures detected\\nRoot cause: Aggressive timer configuration"},
    {"start": 76, "end": 94,
     "text": "RCA complete | PDF report generated\\nCFG-001: Update BGP timers to stable values"},
    {"start": 94, "end": 110,
     "text": "Configuration deployed successfully\\nVerification: All symptoms resolved"},
    {"start": 110, "end": 124,
     "text": "Use Case 2: Broadband disruption — Dombivli\\nAirFiber-FTTH | 2500 users affected"},
    {"start": 124, "end": 140,
     "text": "Knowledge Graph topology mapped\\n9 technologies | 6 specialist agents deployed"},
    {"start": 140, "end": 156,
     "text": "BNG Agent: VLAN misconfiguration identified\\nSubscriber count restored | Report generated"},
    {"start": 156, "end": 162,
     "text": "Cisco Agentic AI\\nIntelligent Network Operations"},
]

# ============================================================
# 300s VERSION: Detailed Incident Mgmt + Security + DC Use Case
# Structure: OTAP intro (27s) + demo clips (~266s) + Cisco ending (7s) = ~300s
# ============================================================
NARR_300_SECTIONS = [
    # --- Incident Management (BGP/HDFC) — detailed ---
    {"name": "n300_01_ticket", "src": "mwc", "clip_start": 0, "clip_dur": 8, "target_dur": 10,
     "text": "A network incident has been reported — BGP Session Instability affecting HDFC banking operations. The knock engineer creates a new ticket in ServiceNow."},
    {"name": "n300_02_escalation", "src": "mwc", "clip_start": 8, "clip_dur": 22, "target_dur": 18,
     "text": "The ticket is escalated to Cisco's Agentic AI. A new ticket ID is generated and the MRA troubleshooting process begins. The engineer navigates to the AI Chat to monitor the investigation."},
    {"name": "n300_03_io_agent", "src": "mwc", "clip_start": 30, "clip_dur": 25, "target_dur": 20,
     "text": "The IO Agent picks up the ticket and begins analysis — reviewing customer impact, device context, and problem classification. With a ninety-two percent match score, it identifies this as a critical BGP incident and triggers the Master Reasoning Agent."},
    {"name": "n300_04_data", "src": "mwc", "clip_start": 55, "clip_dur": 25, "target_dur": 18,
     "text": "The system retrieves device details for NVMBOTAPAAR002 — a Cisco IOS-XR router running SR-MPLS, I.S.I.S., and MPLS. Three active interfaces are identified with their protocol configurations."},
    {"name": "n300_05_topology", "src": "mwc", "clip_start": 80, "clip_dur": 20, "target_dur": 14,
     "text": "The network topology is mapped — four interconnected devices, six connections, three neighboring routers. The MRA has a complete picture of the network environment."},
    {"name": "n300_06_specialists", "src": "mwc", "clip_start": 100, "clip_dur": 35, "target_dur": 22,
     "text": "The MRA deploys three specialist agents — L2 for BFD analysis, I.S.I.S. for IGP verification, and BGP for session troubleshooting. Each agent is an expert in its protocol domain. You can see the real-time progress as they analyze operational states across the network."},
    {"name": "n300_07_bgp_findings", "src": "mwc", "clip_start": 140, "clip_dur": 55, "target_dur": 28,
     "text": "The BGP Agent identifies session instability caused by keepalive failures on the affected neighbor. A significant message count imbalance confirms control-plane packet loss. The root cause — misconfigured timers on the neighbor-group, too aggressive for stable adjacency."},
    {"name": "n300_08_rca_pdf", "src": "mwc", "clip_start": 195, "clip_dur": 45, "target_dur": 20,
     "text": "Root cause confirmed. A detailed PDF report is generated. The IO Agent asks — shall we proceed with configuration generation to fix the issues? The engineer clicks Yes, Proceed."},
    {"name": "n300_09_config", "src": "mwc", "clip_start": 240, "clip_dur": 50, "target_dur": 20,
     "text": "CFG-001 recommends updating BGP timer configuration to stable values. The engineer approves. The full configuration is displayed — updating timers to stable, recommended values. Every change is transparent."},
    {"name": "n300_10_deploy_verify", "src": "mwc", "clip_start": 290, "clip_dur": 50, "target_dur": 18,
     "text": "Configuration deployed successfully. Post-deployment verification confirms — prefix count stable, session flapping eliminated, HDFC banking operations restored. Remediation complete."},
    # --- Security Guardrails ---
    {"name": "n300_11_security", "src": "mwc", "clip_start": 395, "clip_dur": 30, "target_dur": 26,
     "text": "Security is built in from the ground up. When the engineer attempts to extract router credentials, the message is immediately blocked by Cisco AI Defence. Similarly, personally identifiable information is blocked due to PII protection. These guardrails ensure the AI Assistant remains a secure, trustworthy tool."},
    # --- Use Case Slides (static PNG → video) ---
    {"name": "n300_12_slide_ip", "src": "slide", "slide_path": "slide_ip_transport_usecases.png", "target_dur": 18,
     "text": "The platform extends well beyond incident management. Across IP Transport, eleven use cases are supported — including Agentic AI root cause analysis, customer experience management, predictive maintenance, and intelligent capacity planning. Each use case is powered by specialized agents working together autonomously."},
    {"name": "n300_13_slide_dc", "src": "slide", "slide_path": "slide_dc_usecases.png", "target_dur": 16,
     "text": "For service provider datacenters, nineteen use cases are delivered across three deployment drops — powered by fifty-eight specialized agents covering fabric management, workload optimization, and datacenter incident resolution."},
    {"name": "n300_14_slide_security", "src": "slide", "slide_path": "slide_security_usecases.png", "target_dur": 14,
     "text": "And with the Jio AI SOC, fifteen security use cases are handled by seventy-one dedicated agents — from threat detection and response to compliance monitoring and vulnerability management."},
    # --- Closing ---
    {"name": "n300_15_closing", "src": "mwc", "clip_start": 425, "clip_dur": 8, "target_dur": 8,
     "text": "From ticket creation to verified remediation — powered by Cisco's Agentic AI. This is intelligent network operations."},
]


# ============================================================
# 120s VERSION: Condensed Incident Mgmt + DC Use Case
# Structure: OTAP intro (10s) + demo clips (~103s) + Cisco ending (7s) = ~120s
# ============================================================
CAPTIONS_120 = [
    {"start": 0, "end": 8,
     "text": "Incident: BGP Session Instability\\naffecting HDFC banking operations"},
    {"start": 8, "end": 15,
     "text": "IO Agent: Critical BGP incident detected\\nMaster Reasoning Agent triggered"},
    {"start": 15, "end": 25,
     "text": "Device details retrieved\\nTopology: 4 devices, 3 neighbors"},
    {"start": 25, "end": 40,
     "text": "Specialist Agents: L2 + I.S.I.S. + BGP\\nMisconfigured timers identified"},
    {"start": 40, "end": 50,
     "text": "RCA complete | PDF report generated\\nEngineer approves config generation"},
    {"start": 50, "end": 61,
     "text": "Timers updated to stable values\\nEngineer approves and deploys"},
    {"start": 61, "end": 69,
     "text": "Deployment successful | Ticket completed\\nAI Assistant confirms resolution"},
    {"start": 69, "end": 79,
     "text": "IP Transport: 11 Use Cases\\nAgentic AI RCA | Customer Experience | Predictive Maintenance"},
    {"start": 79, "end": 89,
     "text": "SP Datacenter: 19 Use Cases | 58 Agents\\nAcross 3 deployment drops"},
    {"start": 89, "end": 97,
     "text": "AI SOC: 15 Security Use Cases | 71 Agents\\nComprehensive network protection"},
    {"start": 97, "end": 103,
     "text": "Cisco Agentic AI\\nIntelligent Network Operations"},
]

NARR_120_SECTIONS = [
    # --- Incident Management (BGP/HDFC) condensed ---
    {"name": "n120_01_ticket_escalate", "src": "mwc", "clip_start": 0, "clip_dur": 12, "target_dur": 8,
     "text": "A BGP incident affecting HDFC banking operations is reported. The engineer creates a ticket and escalates to Cisco's Agentic AI."},
    {"name": "n120_02_io_agent", "src": "mwc", "clip_start": 35, "clip_dur": 18, "target_dur": 7,
     "text": "The IO Agent identifies a critical BGP incident and triggers the Master Reasoning Agent."},
    {"name": "n120_03_data_topology", "src": "mwc", "clip_start": 60, "clip_dur": 30, "target_dur": 10,
     "text": "Device details and interface configurations are retrieved. The network topology is mapped — four devices, three neighbors."},
    {"name": "n120_04_specialists_bgp", "src": "mwc", "clip_start": 100, "clip_dur": 40, "target_dur": 14,
     "text": "Three specialist agents — L2, I.S.I.S., and BGP — are deployed. The BGP Agent identifies session instability caused by misconfigured timers, too aggressive for stable adjacency."},
    {"name": "n120_05_rca", "src": "mwc", "clip_start": 200, "clip_dur": 25, "target_dur": 10,
     "text": "Root cause confirmed. A PDF report is generated. The engineer approves configuration generation to fix the issues."},
    {"name": "n120_06_config_deploy", "src": "mwc", "clip_start": 260, "clip_dur": 40, "target_dur": 11,
     "text": "The configuration is reviewed — updating timers to stable, recommended values. The engineer approves and deploys."},
    {"name": "n120_07_verify", "src": "mwc", "clip_start": 315, "clip_dur": 22, "target_dur": 8,
     "text": "Deployment successful. The ticket is marked as Completed. The AI Assistant confirms full resolution."},
    # --- Use Case Slides (static PNG → video) ---
    {"name": "n120_08_slide_ip", "src": "slide", "slide_path": "slide_ip_transport_usecases.png", "target_dur": 10,
     "text": "Beyond incident management, the platform supports eleven IP Transport use cases — from Agentic AI root cause analysis to customer experience management and predictive maintenance."},
    {"name": "n120_09_slide_dc", "src": "slide", "slide_path": "slide_dc_usecases.png", "target_dur": 10,
     "text": "For service provider datacenters, nineteen use cases are supported across three deployment drops — powered by fifty-eight specialized agents."},
    {"name": "n120_10_slide_security", "src": "slide", "slide_path": "slide_security_usecases.png", "target_dur": 8,
     "text": "And for the AI SOC, fifteen security use cases are handled by seventy-one dedicated agents — ensuring comprehensive network protection."},
    # --- Closing ---
    {"name": "n120_11_closing", "src": "mwc", "clip_start": 425, "clip_dur": 8, "target_dur": 6,
     "text": "From ticket creation to verified remediation — Cisco's Agentic AI for intelligent network operations."},
]


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def generate_audio(name, text, outfile):
    """Generate audio via ElevenLabs API."""
    if os.path.exists(outfile):
        dur = get_duration(outfile)
        print(f"  [cached] {name}: {dur:.1f}s")
        return
    print(f"  Generating {name}...")
    payload = {"text": text, "model_id": MODEL, "voice_settings": VOICE_SETTINGS}
    resp = requests.post(URL, json=payload, headers=HEADERS)
    if resp.status_code == 200:
        with open(outfile, "wb") as f:
            f.write(resp.content)
        dur = get_duration(outfile)
        print(f"  Saved: {dur:.1f}s ({len(resp.content)//1024} KB)")
    else:
        print(f"  ERROR {resp.status_code}: {resp.text}")
        raise Exception(f"ElevenLabs API error for {name}")


def get_duration(filepath):
    """Get audio/video duration in seconds."""
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", filepath],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())


def run(cmd, desc=""):
    """Run shell command."""
    if desc:
        print(f"  {desc}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  STDERR: {result.stderr[-500:]}")
        raise Exception(f"Command failed: {cmd[:100]}")
    return result.stdout


def get_source(src_key):
    """Get the re-encoded source file path."""
    if src_key == "mwc":
        return os.path.join(WORK, "mwc_hq_reencoded.mp4")
    elif src_key == "otap":
        return os.path.join(WORK, "otap_hq_reencoded.mp4")
    raise ValueError(f"Unknown source: {src_key}")


def make_clip(src, ss, dur, target_dur, outfile):
    """Extract clip from source video, speed-adjust to target duration."""
    ratio = target_dur / dur
    run(f'ffmpeg -y -ss {ss} -t {dur} -i "{src}" '
        f'-vf "setpts=PTS*{ratio},scale={RESOLUTION}:force_original_aspect_ratio=decrease,'
        f'pad={RESOLUTION}:(ow-iw)/2:(oh-ih)/2:black" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 -an "{outfile}"')
    actual = get_duration(outfile)
    speed = 1/ratio
    print(f"    {os.path.basename(outfile)}: src {ss}-{ss+dur}s -> {actual:.1f}s ({speed:.2f}x)")


def make_slide_clip(slide_path, target_dur, outfile):
    """Create a video clip from a static PNG image."""
    run(f'ffmpeg -y -loop 1 -i "{slide_path}" -t {target_dur} '
        f'-vf "scale={RESOLUTION}:force_original_aspect_ratio=decrease,'
        f'pad={RESOLUTION}:(ow-iw)/2:(oh-ih)/2:black" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 -pix_fmt yuv420p -an "{outfile}"')
    actual = get_duration(outfile)
    print(f"    {os.path.basename(outfile)}: slide -> {actual:.1f}s")


def reencode_source(src, outfile, label="source"):
    """Re-encode source to standard format at high quality."""
    if os.path.exists(outfile):
        dur = get_duration(outfile)
        sz = os.path.getsize(outfile) // (1024 * 1024)
        print(f"  [cached] {os.path.basename(outfile)} ({sz} MB, {dur:.1f}s)")
        return
    run(f'ffmpeg -y -i "{src}" '
        f'-vf "scale={RESOLUTION}:force_original_aspect_ratio=decrease,'
        f'pad={RESOLUTION}:(ow-iw)/2:(oh-ih)/2:black" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 -an "{outfile}"',
        f"Re-encoding {label} at CRF 18 / slow preset...")
    sz = os.path.getsize(outfile) // (1024 * 1024)
    print(f"  Done: {sz} MB")


def make_otap_intro(dur, outfile, audio_file):
    """Create OTAP intro clip with Sarah narration (replacing original audio)."""
    run(f'ffmpeg -y -i "{OTAP_VID}" -i "{audio_file}" -t {dur} '
        f'-vf "scale={RESOLUTION}:force_original_aspect_ratio=decrease,'
        f'pad={RESOLUTION}:(ow-iw)/2:(oh-ih)/2:black" '
        f'-map 0:v:0 -map 1:a:0 '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 -shortest "{outfile}"')
    print(f"    OTAP intro: {get_duration(outfile):.1f}s (Sarah voice)")


def make_cisco_ending(outfile, dur=7):
    """Extract Cisco ending clip as-is (with original audio)."""
    run(f'ffmpeg -y -ss 280 -i "{OTAP_VID}" -t {dur} '
        f'-vf "scale={RESOLUTION}:force_original_aspect_ratio=decrease,'
        f'pad={RESOLUTION}:(ow-iw)/2:(oh-ih)/2:black" '
        f'-af "volume=2dB" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 "{outfile}"')
    print(f"    Cisco ending: {get_duration(outfile):.1f}s (original audio)")


def concat_videos(clip_list, outfile):
    """Concatenate video files."""
    listfile = outfile + ".list.txt"
    with open(listfile, "w") as f:
        for c in clip_list:
            f.write(f"file '{c}'\n")
    run(f'ffmpeg -y -f concat -safe 0 -i "{listfile}" -c copy "{outfile}"')
    return get_duration(outfile)


def generate_srt(captions, outfile):
    """Generate SRT subtitle file from caption definitions."""
    with open(outfile, "w") as f:
        for i, cap in enumerate(captions, 1):
            start_h = int(cap["start"] // 3600)
            start_m = int((cap["start"] % 3600) // 60)
            start_s = int(cap["start"] % 60)
            start_ms = int((cap["start"] % 1) * 1000)
            end_h = int(cap["end"] // 3600)
            end_m = int((cap["end"] % 3600) // 60)
            end_s = int(cap["end"] % 60)
            end_ms = int((cap["end"] % 1) * 1000)
            f.write(f"{i}\n")
            f.write(f"{start_h:02d}:{start_m:02d}:{start_s:02d},{start_ms:03d} --> "
                    f"{end_h:02d}:{end_m:02d}:{end_s:02d},{end_ms:03d}\n")
            f.write(f"{cap['text']}\n\n")
    print(f"    SRT file: {outfile} ({len(captions)} captions)")


def build_short_version(version_name, sections, audio_dir_name, final_filename, otap_dur=27):
    """Build a short version: clips speed-adjusted to target_dur, narration overlaid."""
    print(f"\n{'=' * 70}")
    print(f"  BUILDING {version_name}")
    print(f"{'=' * 70}")

    audio_dir = os.path.join(WORK, audio_dir_name)
    os.makedirs(audio_dir, exist_ok=True)

    # Ensure both sources are re-encoded
    mwc_enc = os.path.join(WORK, "mwc_hq_reencoded.mp4")
    otap_enc = os.path.join(WORK, "otap_hq_reencoded.mp4")

    # Step 1: Generate narration
    print(f"\nStep 1: Generate narration audio")
    for sec in sections:
        raw_file = os.path.join(audio_dir, f"{sec['name']}_raw.mp3")
        generate_audio(sec["name"], sec["text"], raw_file)

    # Step 2: Create video clips (speed-adjusted to target_dur)
    print(f"\nStep 2: Create speed-adjusted demo clips")
    clip_files = []
    narration_files = []
    for sec in sections:
        outf = os.path.join(WORK, f"{audio_dir_name}_{sec['name']}.mp4")
        raw_audio = os.path.join(audio_dir, f"{sec['name']}_raw.mp3")
        narr_dur = get_duration(raw_audio)
        # Use max(target_dur, narr_dur) so clip is never shorter than narration
        clip_target = max(sec["target_dur"], narr_dur)
        if sec.get("src") == "slide":
            # Static PNG slide → video clip
            slide_file = os.path.join(WORK, sec["slide_path"])
            make_slide_clip(slide_file, clip_target, outf)
        else:
            src_file = get_source(sec.get("src", "mwc"))
            make_clip(src_file, sec["clip_start"], sec["clip_dur"], clip_target, outf)
        clip_files.append(outf)
        narration_files.append(raw_audio)

    # Step 3: Concatenate clips into silent demo
    print(f"\nStep 3: Concatenate demo clips")
    demo_silent = os.path.join(WORK, f"{audio_dir_name}_demo_silent.mp4")
    demo_dur = concat_videos(clip_files, demo_silent)

    # Step 4: Pad and concatenate narration audio (to match clip durations)
    print(f"\nStep 4: Pad and concatenate narration")
    padded_files = []
    for i, sec in enumerate(sections):
        raw_audio = narration_files[i]
        narr_dur = get_duration(raw_audio)
        clip_target = max(sec["target_dur"], narr_dur)
        padded_file = os.path.join(audio_dir, f"{sec['name']}_padded.m4a")
        pad_dur = max(0, clip_target - narr_dur + 0.1)
        run(f'ffmpeg -y -i "{raw_audio}" -af "apad=pad_dur={pad_dur}" '
            f'-c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 -t {clip_target} "{padded_file}"')
        padded_files.append(padded_file)

    concat_list = os.path.join(audio_dir, "concat_narration.txt")
    with open(concat_list, "w") as f:
        for pf in padded_files:
            f.write(f"file '{pf}'\n")
    narr_audio = os.path.join(WORK, f"{audio_dir_name}_narration.m4a")
    run(f'ffmpeg -y -f concat -safe 0 -i "{concat_list}" -c copy "{narr_audio}"')
    narr_dur = get_duration(narr_audio)
    print(f"  Demo video: {demo_dur:.1f}s, Narration: {narr_dur:.1f}s")

    # Step 5: Overlay narration on video
    print(f"\nStep 5: Overlay narration")
    demo_narrated = os.path.join(WORK, f"{audio_dir_name}_demo_narrated.mp4")
    run(f'ffmpeg -y -i "{demo_silent}" -i "{narr_audio}" '
        f'-map 0:v -map 1:a -c:v copy -c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 '
        f'-shortest "{demo_narrated}"')

    # Step 6: OTAP intro (Sarah voice) + Cisco ending
    print(f"\nStep 6: OTAP intro ({otap_dur}s) + Cisco ending (7s)")
    otap_raw = os.path.join(os.path.join(WORK, "audio_mwc_full"), "otap_intro_raw.mp3")
    if not os.path.exists(otap_raw):
        otap_raw = os.path.join(audio_dir, "otap_intro_raw.mp3")
        generate_audio("otap_intro", OTAP_INTRO_TEXT, otap_raw)

    otap_out = os.path.join(WORK, f"{audio_dir_name}_otap.mp4")
    make_otap_intro(otap_dur, otap_out, otap_raw)
    cisco_end = os.path.join(WORK, f"{audio_dir_name}_cisco_end.mp4")
    make_cisco_ending(cisco_end)

    # Re-encode narrated for concat
    demo_narrated_enc = os.path.join(WORK, f"{audio_dir_name}_demo_narrated_enc.mp4")
    run(f'ffmpeg -y -i "{demo_narrated}" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 "{demo_narrated_enc}"',
        "Re-encoding narrated demo for concat...")

    # Step 7: Final concat
    print(f"\nStep 7: Final concatenation")
    final_out = os.path.join(FINAL, final_filename)
    final_dur = concat_videos([otap_out, demo_narrated_enc, cisco_end], final_out)
    print(f"\n  {version_name}: {final_out}")
    print(f"  Duration: {int(final_dur//60)}:{int(final_dur%60):02d} ({final_dur:.1f}s)")
    print(f"  Size: {os.path.getsize(final_out)//(1024*1024)} MB")
    return final_out, demo_silent


# ============================================================
# BUILD FULL VERSION — adelay + amix approach
# ============================================================
def build_full():
    """Build full version as ONE unified video — no concat seams.

    Architecture: Create a single combined silent video (OTAP 27s + MWC Demo 433s + Cisco ending 7s)
    then overlay ALL narration + Cisco ending audio via a single adelay+amix filter.
    This eliminates the voice quality change at the 27s mark and ensures perfect sync.
    """
    print("\n" + "=" * 70)
    print("  BUILDING FULL VERSION (unified pipeline, single adelay+amix)")
    print("=" * 70)

    audio_dir = os.path.join(WORK, "audio_mwc_full")
    os.makedirs(audio_dir, exist_ok=True)

    OTAP_DUR = 27  # seconds of OTAP intro video
    CISCO_END_DUR = 7  # seconds of Cisco ending

    # Speed ramps: compress static/wait sections at 4x
    # Ramp 1: s02 escalation — static ServiceNow dashboard (src 15-28)
    RAMP1_SRC_START = 15
    RAMP1_SRC_END = 28
    RAMP1_SPEED = 4
    # Ramp 2: processing wait (agents working, no new info) (src 137-154)
    RAMP2_SRC_START = 137
    RAMP2_SRC_END = 154
    RAMP2_SPEED = 4

    # Step 1: Generate narration audio
    print("\nStep 1: Generate narration audio via ElevenLabs")
    otap_raw = os.path.join(audio_dir, "otap_intro_raw.mp3")
    generate_audio("otap_intro", OTAP_INTRO_TEXT, otap_raw)

    for sec in FULL_SECTIONS:
        raw_file = os.path.join(audio_dir, f"{sec['name']}_raw.mp3")
        generate_audio(sec["name"], sec["text"], raw_file)

    # Step 2: Ensure HQ re-encodes exist
    print("\nStep 2: Ensure HQ source videos")
    mwc_enc = os.path.join(WORK, "mwc_hq_reencoded.mp4")
    reencode_source(VIDFILE, mwc_enc, "MWC-Demo.mov")
    otap_enc = os.path.join(WORK, "otap_hq_reencoded.mp4")
    reencode_source(OTAP_VID, otap_enc, "OTAP video")

    # Step 3: Prepare video clips + Cisco ending audio
    print("\nStep 3: Prepare video clips and Cisco ending audio")

    # Extract OTAP intro (0-27s) from re-encoded OTAP (silent)
    otap_clip = os.path.join(WORK, "mwc_full_otap_silent.mp4")
    run(f'ffmpeg -y -t {OTAP_DUR} -i "{otap_enc}" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 -an "{otap_clip}"',
        f"Extracting OTAP intro (0-{OTAP_DUR}s)...")
    print(f"    OTAP clip: {get_duration(otap_clip):.1f}s")

    # Extract Cisco ending (280-287s) from re-encoded OTAP (silent)
    cisco_clip = os.path.join(WORK, "mwc_full_cisco_silent.mp4")
    run(f'ffmpeg -y -ss 280 -t {CISCO_END_DUR} -i "{otap_enc}" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 -an "{cisco_clip}"',
        f"Extracting Cisco ending (280-287s)...")
    print(f"    Cisco clip: {get_duration(cisco_clip):.1f}s")

    # Extract Cisco ending AUDIO from original OTAP for later mixing
    cisco_audio = os.path.join(WORK, "mwc_full_cisco_audio.m4a")
    run(f'ffmpeg -y -ss 280 -t {CISCO_END_DUR} -i "{OTAP_VID}" '
        f'-vn -af "volume=2dB" -c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 "{cisco_audio}"',
        "Extracting Cisco ending audio...")
    print(f"    Cisco audio: {get_duration(cisco_audio):.1f}s")

    mwc_dur = get_duration(mwc_enc)
    otap_clip_dur = get_duration(otap_clip)
    cisco_clip_dur = get_duration(cisco_clip)

    # Speed ramp time savings
    ramp1_original = RAMP1_SRC_END - RAMP1_SRC_START  # 13s
    ramp1_compressed = ramp1_original / RAMP1_SPEED    # ~3.25s
    ramp1_saved = ramp1_original - ramp1_compressed    # ~9.75s
    ramp2_original = RAMP2_SRC_END - RAMP2_SRC_START   # 17s
    ramp2_compressed = ramp2_original / RAMP2_SPEED    # ~4.25s
    ramp2_saved = ramp2_original - ramp2_compressed    # ~12.75s
    time_saved = ramp1_saved + ramp2_saved             # ~22.5s total
    effective_mwc_dur = mwc_dur - time_saved

    cisco_audio_offset_ms = int((otap_clip_dur + effective_mwc_dur) * 1000)
    total_video_dur = otap_clip_dur + effective_mwc_dur + cisco_clip_dur
    print(f"    MWC source: {mwc_dur:.1f}s -> {effective_mwc_dur:.1f}s (2 speed ramps save {time_saved:.1f}s)")
    print(f"    Total video: {total_video_dur:.1f}s ({otap_clip_dur:.1f} + {effective_mwc_dur:.1f} + {cisco_clip_dur:.1f})")

    # Step 4: Compute adelay offsets for ALL narration
    # Map source timestamps to video timeline accounting for two speed ramps
    def src_to_video(src_t):
        """Convert MWC source timestamp to final video timestamp."""
        if src_t <= RAMP1_SRC_START:
            return src_t + otap_clip_dur
        elif src_t <= RAMP1_SRC_END:
            return RAMP1_SRC_START + otap_clip_dur + (src_t - RAMP1_SRC_START) / RAMP1_SPEED
        elif src_t <= RAMP2_SRC_START:
            return src_t + otap_clip_dur - ramp1_saved
        elif src_t <= RAMP2_SRC_END:
            return RAMP2_SRC_START + otap_clip_dur - ramp1_saved + (src_t - RAMP2_SRC_START) / RAMP2_SPEED
        else:
            return src_t + otap_clip_dur - time_saved

    print(f"\nStep 4: Compute narration placement (OTAP +{otap_clip_dur:.1f}s, 2 ramps save {time_saved:.1f}s)")
    audio_files = []
    delays_ms = []

    # First: OTAP intro narration at 0ms
    otap_dur_audio = get_duration(otap_raw)
    audio_files.append(otap_raw)
    delays_ms.append(0)
    cursor_ms = int(otap_dur_audio * 1000) + 300
    print(f"    otap_intro: {otap_dur_audio:.1f}s @ 0.0s (intro)")

    # Then: all 14 demo sections, mapped through speed ramp
    for sec in FULL_SECTIONS:
        raw_file = os.path.join(audio_dir, f"{sec['name']}_raw.mp3")
        audio_dur = get_duration(raw_file)
        video_t = src_to_video(sec["start"])
        section_start_ms = int(video_t * 1000)
        start_ms = max(section_start_ms, cursor_ms)
        delays_ms.append(start_ms)
        cursor_ms = start_ms + int(audio_dur * 1000) + 300
        audio_files.append(raw_file)
        final_start = start_ms / 1000
        drift = final_start - video_t
        print(f"    {sec['name']}: {audio_dur:.1f}s @ {final_start:.1f}s "
              f"(video {video_t:.1f}s, drift {drift:+.1f}s)")

    # Step 5: Single-pass build — concat filter (with speed ramp) + adelay+amix for audio
    print(f"\nStep 5: Single-pass build (2 speed ramps + adelay+amix)")

    # Input order: [0]=otap_clip, [1]=mwc_enc, [2]=cisco_clip, [3..N+2]=narration audio, [N+3]=cisco_audio
    n_narrations = len(audio_files)
    audio_inputs = " ".join(f'-i "{f}"' for f in audio_files)
    audio_inputs += f' -i "{cisco_audio}"'

    # Build filter_complex
    filter_parts = []

    # Video: Split MWC (input 1) into 5 parts — before ramp1, ramp1, between, ramp2, after ramp2
    filter_parts.append(f"[1:v]trim=end={RAMP1_SRC_START},setpts=PTS-STARTPTS[mwc_a]")
    filter_parts.append(f"[1:v]trim=start={RAMP1_SRC_START}:end={RAMP1_SRC_END},setpts=(PTS-STARTPTS)/{RAMP1_SPEED}[mwc_fast1]")
    filter_parts.append(f"[1:v]trim=start={RAMP1_SRC_END}:end={RAMP2_SRC_START},setpts=PTS-STARTPTS[mwc_b]")
    filter_parts.append(f"[1:v]trim=start={RAMP2_SRC_START}:end={RAMP2_SRC_END},setpts=(PTS-STARTPTS)/{RAMP2_SPEED}[mwc_fast2]")
    filter_parts.append(f"[1:v]trim=start={RAMP2_SRC_END},setpts=PTS-STARTPTS[mwc_c]")
    # Concat: OTAP + MWC_a + fast1 + MWC_b + fast2 + MWC_c + Cisco = 7 segments
    filter_parts.append(f"[0:v][mwc_a][mwc_fast1][mwc_b][mwc_fast2][mwc_c][2:v]concat=n=7:v=1:a=0[vout]")

    # Audio tracks: inputs 3..N+2 are narration, N+3 is cisco audio
    mix_labels = []
    for i, delay_ms in enumerate(delays_ms):
        input_idx = i + 3  # offset by 3 video inputs
        label = f"a{i}"
        filter_parts.append(f"[{input_idx}:a]adelay={delay_ms}|{delay_ms}[{label}]")
        mix_labels.append(f"[{label}]")

    # Cisco ending audio
    cisco_input_idx = n_narrations + 3
    filter_parts.append(f"[{cisco_input_idx}:a]adelay={cisco_audio_offset_ms}|{cisco_audio_offset_ms}[acisco]")
    mix_labels.append("[acisco]")

    total_audio_inputs = n_narrations + 1
    filter_str = ";".join(filter_parts)
    mix_str = "".join(mix_labels)
    filter_str += f";{mix_str}amix=inputs={total_audio_inputs}:duration=longest:dropout_transition=0,volume=8dB[aout]"

    final_out = os.path.join(FINAL, "MWC-Demo-Full-v2.2.mp4")
    cmd = (
        f'ffmpeg -y -i "{otap_clip}" -i "{mwc_enc}" -i "{cisco_clip}" '
        f'{audio_inputs} '
        f'-filter_complex "{filter_str}" '
        f'-map "[vout]" -map "[aout]" '
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 '
        f'"{final_out}"'
    )
    run(cmd, "Building unified video (concat + adelay + amix in single pass)...")
    final_dur = get_duration(final_out)
    print(f"\n  FULL VERSION: {final_out}")
    print(f"  Duration: {int(final_dur//60)}:{int(final_dur%60):02d} ({final_dur:.1f}s)")
    print(f"  Size: {os.path.getsize(final_out)//(1024*1024)} MB")
    return final_out


# ============================================================
# BUILD 200s CAPTIONS VERSION
# ============================================================
def build_200s_captions(demo_silent_from_voice=None):
    print(f"\n{'=' * 70}")
    print(f"  BUILDING 200s VERSION (CAPTIONS, NO VOICE)")
    print(f"{'=' * 70}")

    audio_dir_name = "audio_mwc_200s"

    if demo_silent_from_voice and os.path.exists(demo_silent_from_voice):
        demo_silent = demo_silent_from_voice
        print(f"  Using demo clips from voice version")
    else:
        # Rebuild clips if needed
        audio_dir = os.path.join(WORK, audio_dir_name)
        clip_files = []
        for sec in NARR_200_SECTIONS:
            outf = os.path.join(WORK, f"{audio_dir_name}_{sec['name']}.mp4")
            clip_files.append(outf)
        demo_silent = os.path.join(WORK, f"{audio_dir_name}_demo_silent.mp4")
        if not os.path.exists(demo_silent):
            concat_videos(clip_files, demo_silent)

    # Step 1: Generate SRT subtitles
    print("\nStep 1: Generate subtitles")
    srt_file = os.path.join(WORK, "mwc_200s_captions.srt")
    generate_srt(CAPTIONS_200, srt_file)

    # Step 2: Burn subtitles
    print("\nStep 2: Burn captions onto demo video")
    demo_captioned = os.path.join(WORK, "mwc_200s_demo_captioned.mp4")
    subtitle_style = (
        "FontName=Arial,FontSize=12,PrimaryColour=&H00FFFFFF,"
        "OutlineColour=&H80000000,BorderStyle=4,Outline=1,Shadow=0,"
        "MarginV=20,Alignment=2"
    )
    run(f'ffmpeg -y -i "{demo_silent}" '
        f"-vf \"subtitles='{srt_file}':force_style='{subtitle_style}'\" "
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-an "{demo_captioned}"',
        "Burning captions...")

    # Step 3: Add silent audio track
    demo_captioned_audio = os.path.join(WORK, "mwc_200s_demo_captioned_audio.mp4")
    run(f'ffmpeg -y -i "{demo_captioned}" '
        f'-f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 '
        f'-map 0:v -map 1:a -c:v copy -c:a aac -b:a {AUDIO_BITRATE} -shortest '
        f'"{demo_captioned_audio}"',
        "Adding silent audio track...")

    # Step 4: OTAP intro + Cisco ending
    print("\nStep 4: OTAP intro + Cisco ending")
    otap_raw = os.path.join(os.path.join(WORK, "audio_mwc_full"), "otap_intro_raw.mp3")
    otap_out = os.path.join(WORK, "mwc_200s_cap_otap.mp4")
    make_otap_intro(27, otap_out, otap_raw)
    cisco_end = os.path.join(WORK, "mwc_200s_cap_cisco_end.mp4")
    make_cisco_ending(cisco_end)

    # Step 5: Final concat
    print("\nStep 5: Final concatenation")
    final_out = os.path.join(FINAL, "MWC-Demo-200s-captions-v1.0.mp4")
    final_dur = concat_videos([otap_out, demo_captioned_audio, cisco_end], final_out)
    print(f"\n  200s CAPTIONS VERSION: {final_out}")
    print(f"  Duration: {int(final_dur//60)}:{int(final_dur%60):02d} ({final_dur:.1f}s)")
    print(f"  Size: {os.path.getsize(final_out)//(1024*1024)} MB")
    return final_out


# ============================================================
# BUILD 120s CAPTIONS VERSION
# ============================================================
def build_120s_captions(demo_silent_from_voice=None):
    print(f"\n{'=' * 70}")
    print(f"  BUILDING 120s VERSION (CAPTIONS, NO VOICE)")
    print(f"{'=' * 70}")

    audio_dir_name = "audio_mwc_120s"

    if demo_silent_from_voice and os.path.exists(demo_silent_from_voice):
        demo_silent = demo_silent_from_voice
        print(f"  Using demo clips from voice version")
    else:
        audio_dir = os.path.join(WORK, audio_dir_name)
        clip_files = []
        for sec in NARR_120_SECTIONS:
            outf = os.path.join(WORK, f"{audio_dir_name}_{sec['name']}.mp4")
            clip_files.append(outf)
        demo_silent = os.path.join(WORK, f"{audio_dir_name}_demo_silent.mp4")
        if not os.path.exists(demo_silent):
            concat_videos(clip_files, demo_silent)

    # Step 1: Generate SRT subtitles
    print("\nStep 1: Generate subtitles")
    srt_file = os.path.join(WORK, "mwc_120s_captions.srt")
    generate_srt(CAPTIONS_120, srt_file)

    # Step 2: Burn subtitles
    print("\nStep 2: Burn captions onto demo video")
    demo_captioned = os.path.join(WORK, "mwc_120s_demo_captioned.mp4")
    subtitle_style = (
        "FontName=Arial,FontSize=12,PrimaryColour=&H00FFFFFF,"
        "OutlineColour=&H80000000,BorderStyle=4,Outline=1,Shadow=0,"
        "MarginV=20,Alignment=2"
    )
    run(f'ffmpeg -y -i "{demo_silent}" '
        f"-vf \"subtitles='{srt_file}':force_style='{subtitle_style}'\" "
        f'-c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-an "{demo_captioned}"',
        "Burning captions...")

    # Step 3: Add silent audio track
    demo_captioned_audio = os.path.join(WORK, "mwc_120s_demo_captioned_audio.mp4")
    run(f'ffmpeg -y -i "{demo_captioned}" '
        f'-f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 '
        f'-map 0:v -map 1:a -c:v copy -c:a aac -b:a {AUDIO_BITRATE} -shortest '
        f'"{demo_captioned_audio}"',
        "Adding silent audio track...")

    # Step 4: OTAP intro (SILENT — no voice for captions version) + Cisco ending
    print("\nStep 4: OTAP intro (silent) + Cisco ending")
    otap_out = os.path.join(WORK, "mwc_120s_cap_otap_silent.mp4")
    run(f'ffmpeg -y -i "{OTAP_VID}" -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 '
        f'-t 10 -vf "scale={RESOLUTION}:force_original_aspect_ratio=decrease,'
        f'pad={RESOLUTION}:(ow-iw)/2:(oh-ih)/2:black" '
        f'-map 0:v -map 1:a -c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 -shortest "{otap_out}"',
        "Creating silent OTAP intro...")
    print(f"    OTAP intro: {get_duration(otap_out):.1f}s (silent)")
    cisco_end = os.path.join(WORK, "mwc_120s_cap_cisco_end_silent.mp4")
    run(f'ffmpeg -y -ss 280 -i "{OTAP_VID}" -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 '
        f'-t 7 -vf "scale={RESOLUTION}:force_original_aspect_ratio=decrease,'
        f'pad={RESOLUTION}:(ow-iw)/2:(oh-ih)/2:black" '
        f'-map 0:v -map 1:a -c:v libx264 -preset {PRESET} -crf {CRF} -r 30 '
        f'-c:a aac -b:a {AUDIO_BITRATE} -ar 44100 -ac 2 -shortest "{cisco_end}"',
        "Creating silent Cisco ending...")
    print(f"    Cisco ending: {get_duration(cisco_end):.1f}s (silent)")

    # Step 5: Final concat
    print("\nStep 5: Final concatenation")
    final_out = os.path.join(FINAL, "MWC-Demo-120s-captions-v1.4.mp4")
    final_dur = concat_videos([otap_out, demo_captioned_audio, cisco_end], final_out)
    print(f"\n  120s CAPTIONS VERSION: {final_out}")
    print(f"  Duration: {int(final_dur//60)}:{int(final_dur%60):02d} ({final_dur:.1f}s)")
    print(f"  Size: {os.path.getsize(final_out)//(1024*1024)} MB")
    return final_out


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    os.makedirs(FINAL, exist_ok=True)

    # Parse args
    versions = sys.argv[1:] if len(sys.argv) > 1 else ["full", "200s-voice", "200s-captions", "300s", "120s-voice", "120s-captions"]

    # Ensure both sources are re-encoded
    print("\n" + "=" * 70)
    print("  PREPARING SOURCES")
    print("=" * 70)
    mwc_enc = os.path.join(WORK, "mwc_hq_reencoded.mp4")
    reencode_source(VIDFILE, mwc_enc, "MWC-Demo.mov")
    otap_enc = os.path.join(WORK, "otap_hq_reencoded.mp4")
    reencode_source(OTAP_VID, otap_enc, "OTAP video")

    results = {}

    if "full" in versions:
        results["full"] = build_full()

    demo_silent_200 = None
    if "200s-voice" in versions:
        out, demo_silent_200 = build_short_version(
            "200s VERSION (VOICE)",
            NARR_200_SECTIONS,
            "audio_mwc_200s",
            "MWC-Demo-200s-voice-v1.0.mp4",
            otap_dur=27
        )
        results["200s-voice"] = out

    if "200s-captions" in versions:
        results["200s-captions"] = build_200s_captions(demo_silent_200)

    if "300s" in versions:
        out, _ = build_short_version(
            "300s VERSION",
            NARR_300_SECTIONS,
            "audio_mwc_300s",
            "MWC-Demo-300s-v1.1.mp4",
            otap_dur=27
        )
        results["300s"] = out

    demo_silent_120 = None
    if "120s-voice" in versions:
        out, demo_silent_120 = build_short_version(
            "120s VERSION (VOICE)",
            NARR_120_SECTIONS,
            "audio_mwc_120s",
            "MWC-Demo-120s-voice-v1.2.mp4",
            otap_dur=10
        )
        results["120s-voice"] = out

    if "120s-captions" in versions:
        results["120s-captions"] = build_120s_captions(demo_silent_120)

    # Summary
    print("\n" + "=" * 70)
    print("  ALL VERSIONS COMPLETE")
    print("=" * 70)
    for label, path in results.items():
        dur = get_duration(path)
        sz = os.path.getsize(path) / (1024 * 1024)
        print(f"  [{label:>15}] {int(dur//60)}:{int(dur%60):02d} ({dur:.0f}s) | {sz:.0f} MB | {os.path.basename(path)}")
    print(f"\n  Output directory: {FINAL}")
