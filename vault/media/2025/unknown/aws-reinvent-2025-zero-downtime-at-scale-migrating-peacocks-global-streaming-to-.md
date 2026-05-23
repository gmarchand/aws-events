---
clients:
- AWS
- Peacock
- Amazon EKS
date: 2025-12-05
description: Journey through the strategic migration of a major streaming platform
  from self-managed Kubernetes to Amazon EKS. Learn how, in less than 12 months, a
  multi-region transition was orchestrated spanning 200+ applications with zero service
  disruption for more than 41M subscribers. We'll explore the technical patterns,
  infrastructure automation, and collaboration strategies that enabled seamless cutover
  while maintaining developer productivity. Discover practical insights for planning
  large-scale EK
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- streaming
- kubernetes
- eks
- aws
- cloud-migration
- peacock
- reinvent
thematic: media
title: 'AWS re:Invent 2025 - Zero-Downtime at Scale: Migrating Peacock''s Global Streaming
  to EKS (IND3325)'
url: https://www.youtube.com/watch?v=Sj9t1LRbV5g
video_id: Sj9t1LRbV5g
year: 2025
---

# AWS re:Invent 2025 - Zero-Downtime at Scale: Migrating Peacock's Global Streaming to EKS (IND3325)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=Sj9t1LRbV5g)
> 📅 2025-12-05 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Peacock]] [[Amazon EKS]]

# Zero-Downtime at Scale: Migrating Peacock's Global Streaming to Amazon EKS

## Overview of the Migration Journey

This session at AWS re:Invent 2025 chronicles the strategic migration of Peacock, a major streaming platform serving more than 41 million subscribers, from a self-managed Kubernetes environment to Amazon Elastic Kubernetes Service (EKS). The migration was executed in under twelve months and spanned multiple AWS regions, encompassing more than 200 applications. Remarkably, the entire transition was completed without any service disruption, ensuring that subscribers experienced uninterrupted streaming throughout the cutover period.

The presentation emphasizes how the engineering organization balanced the demands of large-scale infrastructure modernization with the operational realities of a live, high-traffic consumer platform. By treating the migration as both a technical and organizational challenge, the team was able to deliver measurable improvements in reliability, scalability, and developer experience.

## Technical Strategy and Architectural Patterns

### Infrastructure Automation and Multi-Region Design

A cornerstone of the migration was the heavy investment in infrastructure automation, which allowed engineers to provision and manage EKS clusters consistently across regions. The team adopted reusable patterns for cluster bootstrapping, networking, and workload placement, ensuring that new environments could be created reliably and rapidly. This automation-first approach reduced human error and provided the repeatability necessary to coordinate parallel migrations across geographies.

Multi-region resilience was treated as a first-class design goal. The architecture was structured to tolerate regional disruptions while maintaining a consistent experience for subscribers worldwide. Traffic management strategies, combined with careful state and data synchronization considerations, enabled the team to shift workloads gradually and validate behavior at every step.

### Zero-Downtime Cutover Techniques

To achieve zero downtime, the team employed progressive traffic shifting and parallel-running clusters, allowing both legacy and target environments to operate side by side during transition windows. Application-level health checks, observability instrumentation, and automated rollback mechanisms provided confidence that issues could be detected and reversed before impacting users. By migrating applications in carefully sequenced waves rather than as a single big-bang event, the team contained risk and learned iteratively from each cohort.

## Organizational Collaboration and Lessons Learned

### Enabling Developer Productivity

Beyond the technical execution, the migration succeeded because of strong collaboration between platform engineering, application teams, and AWS partners. The platform team prioritized maintaining—and ultimately improving—the developer experience, ensuring that application owners could continue shipping features while their workloads were being relocated. Tooling, documentation, and self-service capabilities were enhanced so that teams felt supported rather than burdened by the change.

### Practical Insights for Large-Scale EKS Migrations

The session closes with practical guidance for organizations contemplating similar journeys. Key takeaways include the importance of investing early in automation, designing for multi-region resilience from the outset, sequencing migrations to manage risk, and treating cross-team collaboration as equally critical to technical design. The Peacock experience demonstrates that even at the scale of tens of millions of subscribers and hundreds of applications, a disciplined, well-automated approach to EKS adoption can deliver transformative outcomes without compromising service availability.