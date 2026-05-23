---
clients:
- NatWest
- AWS
date: 2024-06-14
description: As organizations move to the cloud, rapid change is the new normal. Safeguarding
  against potential security threats demands continuous monitoring of cloud resources
  and code that are constantly evolving. In this session, NatWest shares best practices
  for monitoring their AWS environment for software and configuration vulnerabilities
  at scale using AWS security services like Amazon Inspector and AWS Security Hub.
  Learn how security teams can automate the identification and prioritization of criti
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- security
- vulnerability-management
- cloud
- monitoring
- fintech
- devsecops
thematic: media
title: AWS re:Inforce 2024 - How NatWest uses AWS services to manage vulnerabilities
  at scale (TDR201)
url: https://www.youtube.com/watch?v=7RacD3j4bc8
video_id: 7RacD3j4bc8
year: 2024
---

# AWS re:Inforce 2024 - How NatWest uses AWS services to manage vulnerabilities at scale (TDR201)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=7RacD3j4bc8)
> 📅 2024-06-14 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[NatWest]] [[AWS]]

# How NatWest Uses AWS Services to Manage Vulnerabilities at Scale

## Overview of the Session

At AWS re:Inforce 2024, NatWest presented its approach to managing security vulnerabilities across a rapidly evolving cloud environment. As enterprises accelerate their migration to AWS, the pace of change introduces new risks that traditional, manual security processes cannot adequately address. NatWest, one of the United Kingdom's largest financial institutions, shared how it has built a scalable vulnerability management program leveraging native AWS security services to maintain continuous visibility over its workloads, code, and configurations. The session emphasized that safeguarding modern cloud estates requires automation, prioritization, and close collaboration between security and application teams.

## Building a Scalable Vulnerability Management Program

### Continuous Monitoring with AWS Security Services

NatWest anchors its vulnerability management strategy on Amazon Inspector and AWS Security Hub, which together provide continuous monitoring of software vulnerabilities and configuration weaknesses across the AWS environment. Amazon Inspector automatically scans EC2 instances, container images, and Lambda functions for known CVEs and unintended network exposure, while AWS Security Hub aggregates findings from multiple security services into a unified view. This integrated approach allows NatWest's security team to maintain real-time awareness of risks as cloud resources are provisioned, modified, and decommissioned at speed, eliminating blind spots that typically emerge in fast-moving DevOps environments.

### Automating Identification and Prioritization

A central theme of NatWest's program is the use of automation to combat alert fatigue. Given the sheer volume of findings generated in a large enterprise estate, the security team has implemented automated workflows that enrich, deduplicate, and prioritize vulnerabilities based on contextual factors such as severity, exploitability, asset criticality, and exposure. By focusing analyst attention on the most consequential issues first, NatWest ensures that limited security resources are directed toward risks that genuinely threaten the business rather than being consumed by noise. This prioritization layer transforms raw findings into actionable insights that can be triaged efficiently.

### Collaboration with Application Teams for Remediation

Identification alone does not reduce risk, so NatWest has invested heavily in mechanisms that route prioritized findings directly to the application teams responsible for remediation. By integrating Security Hub findings into developer-facing ticketing and collaboration tools, the security organization shortens the feedback loop between detection and resolution. This decentralized model places ownership of fixes with the teams closest to the code and infrastructure, while the central security function retains oversight and reporting. The result is faster mean-time-to-remediate and a stronger culture of shared accountability for security across the engineering organization.

## Key Outcomes and Best Practices

NatWest's experience demonstrates that managing vulnerabilities at scale in the cloud depends on three reinforcing pillars: continuous and automated discovery using native AWS services, intelligent prioritization to focus on what matters most, and tight collaboration between security and development teams to drive timely remediation. The session offered practical guidance for other enterprises seeking to mature their cloud security posture, underscoring that combining Amazon Inspector and AWS Security Hub with thoughtful automation enables security teams to keep pace with cloud-scale change while reducing operational burden and improving risk outcomes.