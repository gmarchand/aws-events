---
clients:
- AWS
- Amazon EKS
date: 2024-12-07
description: "A wide range of companies, from the most innovative startups to the
  world’s leading enterprises, are running their internal platforms on Amazon EKS,
  helping them to accelerate developer velocity and increase the pace of innovation.
  In this session, learn about best practices that AWS has developed over years of
  helping thousands of customers build and scale their internal platforms on Amazon
  EKS.\n\nLearn more:\nAWS re:Invent: https://go.aws/reinvent.\nMore AWS events: https://go.aws/3kss9CP
  \n\nSubsc"
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- eks
- kubernetes
- cloud
- platforms
- scalability
- reinvent
thematic: media
title: AWS re:Invent 2024 - How to build scalable platforms with Amazon EKS (KUB301)
url: https://www.youtube.com/watch?v=WkPrmHKZsq4
video_id: WkPrmHKZsq4
year: 2024
---

# AWS re:Invent 2024 - How to build scalable platforms with Amazon EKS (KUB301)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=WkPrmHKZsq4)
> 📅 2024-12-07 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon EKS]]

# Building Scalable Platforms with Amazon EKS

## Overview of the Session

This AWS re:Invent 2024 session, titled "How to build scalable platforms with Amazon EKS" (KUB301), addresses the growing trend of organizations adopting Kubernetes-based internal developer platforms to accelerate innovation. The session draws on AWS's extensive experience working with thousands of customers, ranging from agile startups to global enterprises, who have chosen Amazon Elastic Kubernetes Service (EKS) as the foundation for their internal platforms. The presenters share consolidated best practices that have emerged from these engagements, providing a practical roadmap for architects and platform engineers seeking to scale their own environments effectively.

## Why Internal Platforms Matter

### Accelerating Developer Velocity

A central theme of the session is the strategic importance of internal platforms in modern software organizations. By abstracting away the underlying infrastructure complexity, internal platforms allow application developers to focus on writing business logic rather than managing Kubernetes clusters, networking, or security primitives. This separation of concerns directly translates into faster release cycles, reduced cognitive load on engineering teams, and a higher pace of innovation. The presenters emphasize that platforms built on Amazon EKS provide the elasticity, managed control plane, and deep AWS service integrations needed to serve diverse workloads at scale.

### Standardization and Governance

Beyond speed, internal platforms deliver consistency. Centralized platform teams can codify guardrails, security policies, and compliance requirements once, then propagate them across all tenant workloads. This approach reduces operational risk while still giving developers self-service access to the resources they need. EKS serves as a strong foundation for this model because it integrates natively with AWS Identity and Access Management, VPC networking, and observability services, enabling platform teams to enforce policies without reinventing core capabilities.

## Best Practices for Scaling on Amazon EKS

### Architecting for Multi-Tenancy and Growth

The session highlights architectural patterns that AWS has refined through years of customer engagement, including approaches to multi-tenancy, cluster sizing, and workload isolation. Platform teams must decide between single-cluster multi-tenancy and fleet-based models, balancing operational simplicity against blast-radius containment. The presenters recommend designing for growth from the outset, leveraging EKS features such as managed node groups, Karpenter for intelligent autoscaling, and add-ons that streamline lifecycle management of common platform components.

### Operational Excellence and Developer Experience

Equally important are the operational practices that keep platforms reliable as they scale. The session covers strategies for upgrade management, observability, cost optimization, and incident response, all tailored to the realities of running Kubernetes at significant scale. The presenters also stress the importance of curating a strong developer experience layer on top of EKS, using tools and abstractions that hide Kubernetes complexity while preserving the flexibility power users require.

## Key Takeaways

The session ultimately positions Amazon EKS as a proven foundation for internal platforms that must serve a wide spectrum of workloads and stakeholders. Success depends on combining EKS's managed capabilities with deliberate architectural choices around tenancy, automation, and developer-facing abstractions. Organizations that invest in these practices can expect meaningful gains in developer productivity, operational consistency, and the overall speed at which they deliver value to their customers.