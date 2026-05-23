---
clients:
- AWS
- Amazon
date: 2023-12-01
description: Discover how you can benefit from fully managed runtime threat detection
  for Amazon ECS, including serverless container workloads running on AWS Fargate.
  Join AWS security and container experts to learn how GuardDuty ECS Runtime Monitoring
  simplifies organization-wide threat detection for Amazon ECS workloads. GuardDuty
  ECS Runtime Monitoring gives you visibility into on-host operating system-level
  activities and provides container-level context to detect and take action on threats
  to your Amazo
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- guardduty
- ecs
- fargate
- security
- containers
- threat-detection
thematic: media
title: AWS re:Invent 2023 - Introducing GuardDuty ECS Runtime Monitoring, including
  AWS Fargate (SEC239)
url: https://www.youtube.com/watch?v=nuMOaQctNgE
video_id: nuMOaQctNgE
year: 2023
---

# AWS re:Invent 2023 - Introducing GuardDuty ECS Runtime Monitoring, including AWS Fargate (SEC239)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=nuMOaQctNgE)
> 📅 2023-12-01 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon]]

# Introducing GuardDuty ECS Runtime Monitoring, Including AWS Fargate

## Session Overview

At AWS re:Invent 2023, AWS security and container experts presented session SEC239, unveiling Amazon GuardDuty's expanded runtime threat detection capabilities for Amazon Elastic Container Service (ECS), including serverless workloads running on AWS Fargate. The session addressed a critical gap in container security by demonstrating how organizations can now achieve fully managed, organization-wide runtime threat detection across their entire ECS estate without sacrificing the operational simplicity that draws teams to serverless containers in the first place.

## Extending Runtime Visibility to Modern Container Workloads

### The Challenge of Securing Serverless Containers

The presenters framed the discussion around a fundamental tension in modern application security: as organizations adopt serverless container platforms like AWS Fargate to reduce operational overhead, they often lose the host-level visibility traditionally used to detect runtime threats. Because Fargate abstracts away the underlying infrastructure, customers cannot install conventional endpoint security agents, leaving runtime activity inside containers as a potential blind spot. The speakers emphasized that compromising on security is not an acceptable trade-off for the agility benefits of serverless, and they positioned GuardDuty ECS Runtime Monitoring as the answer to this dilemma.

### How GuardDuty ECS Runtime Monitoring Works

The experts explained that GuardDuty ECS Runtime Monitoring provides visibility into operating system–level activities occurring on the host, while enriching those signals with container-level context so that security teams can pinpoint exactly which task, service, or workload is involved in suspicious behavior. The capability spans both ECS on EC2 and ECS on Fargate, delivering a consistent detection experience regardless of the underlying compute model. Because the service is fully managed, customers do not need to deploy, patch, or operate sensors themselves, and the integration is designed to scale automatically across accounts and regions through AWS Organizations.

### Container-Aware Threat Detection in Practice

The session highlighted the kinds of threats the new capability is designed to surface, including suspicious process execution, cryptocurrency mining, reverse shells, and other indicators of compromise that only become apparent at runtime. By correlating these behaviors with container metadata, GuardDuty enables responders to move quickly from a finding to a specific container and task definition, shortening investigation time and supporting more precise remediation actions.

## Outcomes and Takeaways

The key outcome of the session was the introduction of a unified, managed approach to runtime security that allows customers to adopt AWS Fargate and ECS confidently without building custom monitoring solutions. The presenters encouraged attendees to enable ECS Runtime Monitoring across their organizations to gain container-aware coverage as part of a defense-in-depth strategy, reinforcing the broader message that modern application architectures and strong runtime security can coexist on AWS.