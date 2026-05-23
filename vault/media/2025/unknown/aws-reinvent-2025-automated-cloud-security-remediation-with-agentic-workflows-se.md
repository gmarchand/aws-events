---
clients:
- AWS
- Dynatrace
date: 2025-12-09
description: Today’s platform teams and SREs need to shift from a reactive operations
  approach to autonomous, agent-based cloud ops. In this session, you’ll learn how
  to build an automated, agent-driven remediation workflow by combining AWS Security
  Hub findings with Dynatrace Davis® AI and the MCP server. We’ll walk through a step-by-step
  pipeline, from detection to automated fix, where automation handles the heavy lifting
  and only minor steps require human interaction. Additionally, discover how AI-generat
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- security
- ai
- cloud
- automation
- agentic-workflows
- devops
thematic: media
title: AWS re:Invent 2025 - Automated cloud security remediation with agentic workflows
  (SEC217)
url: https://www.youtube.com/watch?v=CBlaw7KQwT0
video_id: CBlaw7KQwT0
year: 2025
---

# AWS re:Invent 2025 - Automated cloud security remediation with agentic workflows (SEC217)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=CBlaw7KQwT0)
> 📅 2025-12-09 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Dynatrace]]

# Automated Cloud Security Remediation with Agentic Workflows

## Session Overview

This AWS re:Invent 2025 session, presented by Dynatrace as an AWS Partner, addresses a fundamental shift required for modern platform teams and Site Reliability Engineers (SREs). The presentation argues that traditional reactive operational models can no longer keep pace with the scale, velocity, and complexity of cloud environments. Instead, organizations must embrace autonomous, agent-based cloud operations that detect issues, reason about context, and execute fixes with minimal human intervention. The session demonstrates how this transformation can be achieved by combining AWS Security Hub findings with Dynatrace Davis AI and a Model Context Protocol (MCP) server to orchestrate end-to-end remediation pipelines.

## Building the Agentic Remediation Pipeline

### From Detection to Automated Fix

The core of the session walks through a step-by-step pipeline that transforms raw security findings into resolved issues without burdening engineering teams with manual triage. AWS Security Hub serves as the detection layer, continuously surfacing misconfigurations, vulnerabilities, and compliance violations across the AWS environment. These findings are then enriched and analyzed by Dynatrace Davis AI, which applies causal reasoning and observability context to determine the true impact, affected entities, and the most appropriate remediation path. The MCP server acts as the connective tissue between AI agents and operational tooling, allowing the workflow to invoke targeted actions such as generating infrastructure-as-code patches, opening tickets, and applying fixes through established change management channels.

### AI-Generated Remediation Assets and Context-Aware Ticketing

A central theme of the demonstration is how generative and agentic AI capabilities produce remediation assets directly rather than simply alerting humans to act. The agents create context-aware tickets that include the underlying cause, affected resources, business impact, and proposed code or configuration changes, giving responders everything they need in one place. This eliminates the back-and-forth typically required to gather diagnostic data and dramatically shortens the path from detection to decision. Human interaction is preserved only for the minor approval or validation steps where judgment is genuinely required, while the heavy lifting of investigation, correlation, and asset generation is handled autonomously.

### Post-Fix Validation and Closing the Loop

The pipeline does not end once a fix is applied. The workflow incorporates post-fix validation, in which the agentic system verifies that the remediation actually resolved the underlying finding, that no regressions were introduced, and that the security posture has measurably improved. This closed-loop design ensures that automated actions are trustworthy and auditable, which is essential for adopting autonomous operations in regulated and production-critical environments.

## Outcomes and Strategic Implications

The session concludes by framing the business and operational benefits of this agentic approach. By offloading detection, analysis, remediation generation, and validation to coordinated AI agents, organizations significantly reduce mean time to resolution (MTTR) for security findings and free their platform and security engineers from repetitive toil. The integration of AWS Security Hub, Dynatrace Davis AI, and MCP-driven automation streamlines DevSecOps by embedding security remediation directly into the operational fabric rather than treating it as a separate, manual workstream. The overarching message is that agentic workflows represent the next stage of cloud operations, where teams move from reacting to incidents to supervising autonomous systems that keep environments secure and compliant by default.