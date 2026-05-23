---
clients:
- AWS
- Vanguard Group
date: 2023-12-04
description: 'In systems engineering, resilience refers to the ability of a system
  to withstand and recover from disruptions while maintaining its essential functions
  and operations. To achieve this, organizations need to take a holistic approach
  to embed resilience principles in each stage of systems development: designing,
  building, deploying, testing, and operating. In this session, learn about the AWS
  resilience lifecycle and see how you can implement it in your organization. Hear
  from the Vanguard Group’'
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- resilience
- aws
- cloud
- systems-engineering
- reinvent
- architecture
thematic: media
title: 'AWS re:Invent 2023 - Resilience lifecycle: A mental model for resilience on
  AWS (ARC312)'
url: https://www.youtube.com/watch?v=i-0XJZLvq6U
video_id: i-0XJZLvq6U
year: 2023
---

# AWS re:Invent 2023 - Resilience lifecycle: A mental model for resilience on AWS (ARC312)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=i-0XJZLvq6U)
> 📅 2023-12-04 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Vanguard Group]]

# Resilience Lifecycle: A Mental Model for Resilience on AWS

## Introduction to Resilience as a Holistic Discipline

In modern systems engineering, resilience represents far more than simply keeping applications online. It encompasses a system's ability to withstand disruptions, recover gracefully from failures, and continue delivering essential business functions even when components break down. This AWS re:Invent 2023 session introduces the AWS resilience lifecycle as a mental model that helps organizations embed resilience principles throughout every phase of software development and operations, rather than treating it as an afterthought bolted onto finished systems. The session combines AWS guidance with real-world insights from the Vanguard Group's Resilience Office, demonstrating how a major financial institution operationalizes these principles at scale.

## The AWS Resilience Lifecycle Framework

### Designing and Building for Failure

The lifecycle begins with deliberate architectural choices that anticipate failure rather than hope to avoid it. Teams must define clear resilience objectives tied to business outcomes, establishing recovery time objectives and recovery point objectives that reflect the actual cost of downtime. From there, architects apply patterns such as multi-Availability Zone deployments, redundancy across fault-isolated boundaries, loose coupling between components, and graceful degradation strategies so that partial failures do not cascade into total outages. AWS services like Elastic Load Balancing, Auto Scaling, Amazon Route 53, and managed databases with cross-region replication provide the building blocks, but the discipline lies in choosing the right primitives for each workload's criticality tier.

### Testing, Deploying, and Operating Resilient Systems

Resilience claims remain theoretical until validated through testing. The lifecycle emphasizes continuous verification using chaos engineering tools such as AWS Fault Injection Simulator to inject controlled failures and confirm that systems behave as designed. Deployment practices including blue/green releases, canary rollouts, and automated rollback mechanisms reduce the blast radius of changes, which historically cause the majority of incidents. Once in production, operating resilient systems requires robust observability through Amazon CloudWatch, structured incident response runbooks, and post-incident reviews that feed lessons back into design. AWS Resilience Hub plays a central role by continuously assessing applications against defined targets and surfacing gaps before they become outages.

### Responding to and Learning from Disruption

The final stages of the lifecycle close the loop by treating every disruption as a learning opportunity. Mature organizations practice game days, validate runbooks under realistic conditions, and ensure that operational knowledge is shared across teams rather than locked in individual heroes. Continuous improvement transforms resilience from a one-time architectural exercise into an organizational capability that strengthens over time.

## Vanguard's Implementation of the Resilience Lifecycle

### Establishing a Centralized Resilience Office

Vanguard shared how it operationalized the lifecycle by creating a dedicated Resilience Office that sets standards, provides tooling, and partners with application teams rather than acting as a gatekeeper. This central function classifies applications by business criticality, defines tiered resilience requirements for each class, and ensures that engineering teams have clear, measurable targets aligned with the firm's obligations to investors. The office champions a cultural shift in which resilience is owned by every team that builds software, not delegated to a separate operations group.

### Embedding Practices into Engineering Workflows

Vanguard adopted concrete practices drawn from each stage of the lifecycle, including architecture reviews focused on failure modes, automated resilience testing integrated into delivery pipelines, and regular chaos experiments against production-like environments. By leveraging AWS Resilience Hub and complementary internal tooling, Vanguard converts abstract resilience goals into measurable signals that engineers can act on during day-to-day development. The result is a repeatable approach that scales resilience expertise across hundreds of applications without creating bottlenecks.

## Key Takeaways

The session's central message is that resilience is a continuous lifecycle rather than a project milestone. Organizations succeed when they translate business expectations into concrete technical objectives, apply proven AWS architectural patterns, validate behavior through deliberate failure injection, and learn systematically from every event. Vanguard's experience demonstrates that pairing this lifecycle with a dedicated resilience function and the right AWS services enables even highly regulated enterprises to build systems that remain dependable in the face of inevitable disruption.