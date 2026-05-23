---
clients:
- AWS
date: 2023-11-30
description: 'Operating in the cloud allows IT teams to focus on business outcomes
  and accelerate innovation. In this session, learn how to build, manage, and operate
  your mission-critical applications in a secure, automated, reliable, and cost-effective
  way. Discover best practices for establishing a multi-account environment, automating
  operations, and managing your applications. Additionally, learn how to overcome
  operational challenges, achieve efficient management, and enhance resilience for
  workloads.


  '
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- cloud
- best-practices
- operations
- reinvent
- automation
- security
thematic: media
title: AWS re:Invent 2023 - Best practices for operating on AWS (COP321)
url: https://www.youtube.com/watch?v=XBKq2JXWsS4
video_id: XBKq2JXWsS4
year: 2023
---

# AWS re:Invent 2023 - Best practices for operating on AWS (COP321)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=XBKq2JXWsS4)
> 📅 2023-11-30 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]]

# Best Practices for Operating on AWS

## Overview of Cloud Operations Strategy

Operating in the cloud fundamentally shifts the focus of IT teams from managing infrastructure to delivering business outcomes and accelerating innovation. This AWS re:Invent 2023 session, COP321, presents a comprehensive framework for building, managing, and operating mission-critical applications on AWS in a manner that is secure, automated, reliable, and cost-effective. The session emphasizes that successful cloud operations require deliberate planning across multiple dimensions, including account structure, automation strategy, application management, and resilience engineering.

The central premise is that cloud operations should free organizations from undifferentiated heavy lifting so engineering teams can concentrate on creating customer value. By adopting proven patterns and AWS-native tooling, organizations can overcome common operational challenges and establish foundations that scale with their business.

## Building a Strong Operational Foundation

### Establishing a Multi-Account Environment

A well-designed multi-account environment forms the cornerstone of effective AWS operations. Separating workloads, environments, and business units across distinct accounts provides strong isolation boundaries for security, billing, and blast radius containment. AWS Organizations and AWS Control Tower enable teams to provision and govern these accounts at scale, applying guardrails that enforce compliance requirements consistently across the entire estate. By codifying account structures and baseline configurations from the outset, organizations avoid the costly retrofitting that often results from ad-hoc growth.

### Automating Operations

Automation is presented as essential rather than optional for operating at cloud scale. Infrastructure as code, configuration management, and event-driven automation reduce manual toil, eliminate configuration drift, and enable repeatable deployments across environments. Services such as AWS Systems Manager, AWS CloudFormation, and AWS Config allow teams to automate provisioning, patching, compliance checking, and incident response. Embedding automation into operational workflows ensures that routine tasks execute reliably while engineers focus on higher-value work.

### Managing Applications Effectively

Application management on AWS benefits from treating applications as first-class operational entities. By tagging resources consistently, organizing them into logical applications, and using observability tools such as Amazon CloudWatch and AWS X-Ray, teams gain the visibility needed to monitor health, performance, and cost. Centralized dashboards and alerting mechanisms enable proactive identification of issues before they impact customers, while structured operational reviews help teams continuously refine their practices.

## Achieving Resilience and Operational Excellence

### Overcoming Operational Challenges

The session addresses common operational pain points, including managing complexity across distributed systems, maintaining security posture as environments grow, and controlling costs without sacrificing agility. The recommended approach combines strong governance with developer enablement, giving teams the freedom to innovate within well-defined guardrails. Standardizing on shared services for logging, monitoring, identity, and networking reduces duplication and creates consistent operational experiences across the organization.

### Enhancing Workload Resilience

Resilience is engineered through deliberate architectural choices and operational practices. Designing for failure, implementing automated recovery mechanisms, and regularly testing disaster recovery procedures ensure that workloads can withstand and rapidly recover from disruptions. The session highlights the importance of defining recovery objectives, leveraging multi-Region and multi-Availability Zone architectures where appropriate, and using AWS resilience services to validate assumptions through chaos engineering and game days.

### Driving Continuous Improvement

The overarching outcome is an operating model that supports continuous improvement. By combining a robust multi-account foundation, pervasive automation, disciplined application management, and resilience-focused engineering, organizations establish operations that are not only efficient today but adaptable to future demands. This approach allows IT teams to consistently deliver secure, reliable, and cost-effective services while accelerating the pace of innovation across the business.