---
clients:
- iHeart
- iHeartMedia
- AWS
- Amazon Bedrock
- NewRelic
- PagerDuty
- CloudWatch
date: 2025-12-06
description: When performance incidents strike entertainment businesses, downtime
  affects reputation and revenue. Traditional troubleshooting consumes time gathering
  logs and coordinating remediation. Discover how iHeartMedia transformed incident
  response using Amazon Bedrock to build an intelligent agent monitoring alerts from
  NewRelic, PagerDuty, and CloudWatch, automatically collecting diagnostics and initiating
  EKS remediation with minimal human intervention. We'll cover implementation approaches,
  remedi
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aiops
- bedrock
- aws
- incident-response
- ai
- cloud
- monitoring
thematic: media
title: 'AWS re:Invent 2025 - AIOps Revolution: How iHeart slashed incident response
  time by 60% with Bedrock'
url: https://www.youtube.com/watch?v=qvhmFAvG_QI
video_id: qvhmFAvG_QI
year: 2025
---

# AWS re:Invent 2025 - AIOps Revolution: How iHeart slashed incident response time by 60% with Bedrock

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=qvhmFAvG_QI)
> 📅 2025-12-06 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[iHeart]] [[iHeartMedia]] [[AWS]] [[Amazon Bedrock]] [[NewRelic]] [[PagerDuty]] [[CloudWatch]]

# AIOps Revolution: How iHeartMedia Slashed Incident Response Time by 60% with Amazon Bedrock

## Transforming Incident Response in the Entertainment Industry

For entertainment businesses like iHeartMedia, performance incidents carry consequences that extend far beyond technical disruptions. Every minute of downtime erodes audience trust, damages brand reputation, and directly impacts revenue streams tied to advertising and listener engagement. Traditional incident response workflows have long compounded these challenges by requiring engineers to manually gather logs from disparate systems, coordinate across teams, and execute remediation steps under intense pressure. Recognizing that this reactive model could no longer keep pace with the demands of a 24/7 media operation, iHeartMedia turned to generative AI to fundamentally rethink how incidents are detected, diagnosed, and resolved.

## Building an Intelligent Agent on Amazon Bedrock

### Unifying Observability Signals Through Agentic AI

At the heart of iHeartMedia's transformation is an intelligent agent built on Amazon Bedrock that continuously monitors alerts streaming in from NewRelic, PagerDuty, and Amazon CloudWatch. Rather than relying on human responders to triage signals from each tool independently, the agent ingests these alerts in real time, correlates them against operational context, and determines the most likely root cause. By acting as a unified layer above the observability stack, the agent eliminates the fragmented investigation process that traditionally consumed the early minutes of every incident. The Bedrock-powered reasoning capabilities allow the system to interpret unstructured log data, identify patterns across services, and make informed decisions about which diagnostic paths to pursue.

### Automating Diagnostics and EKS Remediation

Once the agent identifies a probable cause, it automatically collects the diagnostics needed to confirm its hypothesis and initiates remediation actions against the underlying Amazon EKS infrastructure with minimal human intervention. This closed-loop approach handles common failure modes—such as pod restarts, scaling adjustments, and configuration corrections—without waking on-call engineers for routine issues. Human operators remain in the loop for higher-risk decisions, but the agent shoulders the repetitive investigative work that previously dominated response timelines. The result is a 60% reduction in incident response time, freeing engineering teams to focus on strategic improvements rather than firefighting.

### Engineering AI Memory for Continuous Learning

A critical element of the implementation is the construction of an AI memory system that allows the agent to learn from every incident it handles. By persisting context about past failures, successful remediations, and environmental nuances, the agent becomes progressively more accurate and efficient over time. This memory layer transforms the system from a stateless responder into an institutional knowledge base that captures operational wisdom and applies it autonomously. Over successive incidents, the agent refines its decision-making, recognizes recurring patterns more quickly, and proposes increasingly sophisticated remediation strategies.

## Advancing Toward Self-Healing Infrastructure

iHeartMedia's experience demonstrates that agentic AI on Amazon Bedrock can move organizations meaningfully closer to the long-standing goal of self-healing infrastructure. The combination of unified alert ingestion, automated diagnostics, autonomous EKS remediation, and a learning memory system establishes a blueprint that other enterprises can adapt to their own environments. Beyond the immediate operational gains, this approach signals a broader shift in how reliability engineering will be practiced—one in which AI agents handle the mechanical aspects of incident response while human engineers concentrate on architectural resilience and innovation. The 60% improvement in response time is significant on its own, but the more durable outcome is the foundation it lays for infrastructure that detects, diagnoses, and repairs itself with ever-decreasing human involvement.