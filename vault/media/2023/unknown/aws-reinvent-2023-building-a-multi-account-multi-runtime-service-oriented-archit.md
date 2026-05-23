---
clients:
- AWS
- Amazon
- HashiCorp
date: 2023-12-01
description: As organizations scale their applications and teams, adopting a service-oriented
  architecture (SOA) can improve scalability, flexibility, and agility. In this session,
  walk through a journey from zero to scale and explore when and how an organization
  should implement SOA. Learn how to set up a multi-account, multi-runtime microservices
  architecture using Amazon ECS, Amazon EKS, and Amazon EC2 along with HashiCorp Terraform,
  Consul, Boundary, and Vault. This presentation is brought to you by Hash
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- soa
- multi-account
- architecture
- scalability
- cloud
- reinvent
thematic: media
title: AWS re:Invent 2023 - Building a multi-account, multi-runtime service-oriented
  architecture (DOP316)
url: https://www.youtube.com/watch?v=nSFHlcWj8TY
video_id: nSFHlcWj8TY
year: 2023
---

# AWS re:Invent 2023 - Building a multi-account, multi-runtime service-oriented architecture (DOP316)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=nSFHlcWj8TY)
> 📅 2023-12-01 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon]] [[HashiCorp]]

# Building a Multi-Account, Multi-Runtime Service-Oriented Architecture

## Introduction and Session Context

This AWS re:Invent 2023 session, presented in partnership with HashiCorp, addresses one of the most pressing architectural challenges facing growing organizations: how to evolve from monolithic beginnings to a scalable, distributed system. As applications expand and engineering teams multiply, the friction of shared codebases and tightly coupled deployments begins to outweigh the simplicity that monoliths once provided. The presenters guide attendees through a journey from zero to scale, framing service-oriented architecture (SOA) not as an inevitable destination but as a deliberate response to specific organizational and technical pressures.

The session emphasizes that adopting SOA is fundamentally about improving scalability, flexibility, and agility, allowing independent teams to ship software at their own cadence while maintaining the operational discipline necessary to keep a distributed system reliable and secure.

## Architectural Approach and Decision Framework

### When and Why to Adopt SOA

The presenters argue that the decision to move toward service-oriented architecture should be driven by clear signals such as deployment bottlenecks, team coordination overhead, and the need for differentiated scaling and runtime requirements across components. Rather than prescribing SOA from day one, they advocate for a measured progression in which organizations recognize the inflection point where the cost of remaining monolithic exceeds the complexity introduced by distributing services. This framing ensures that teams adopt distributed patterns to solve real problems instead of pursuing architectural fashion.

### Multi-Account, Multi-Runtime Design

A central theme of the session is that mature SOA implementations rarely live within a single AWS account or rely on a single compute runtime. Instead, the recommended pattern distributes workloads across multiple AWS accounts to achieve strong isolation boundaries, blast radius containment, and clearer cost and security ownership per team or domain. Within this multi-account structure, services run on the runtime best suited to their characteristics: Amazon ECS for container workloads that benefit from deep AWS integration, Amazon EKS for teams standardizing on Kubernetes, and Amazon EC2 for workloads with specialized requirements that do not fit cleanly into either container platform. The architecture is designed so that services on different runtimes can still communicate, share identity, and be governed consistently.

### HashiCorp Tooling Across the Stack

The session demonstrates how HashiCorp's product suite stitches this heterogeneous environment together. Terraform provides the infrastructure-as-code foundation for provisioning accounts, networks, clusters, and services in a repeatable way across environments. Consul serves as the service networking layer, delivering service discovery and a service mesh that spans ECS, EKS, and EC2 so that workloads can communicate securely regardless of where they run. Vault centralizes secrets management and dynamic credential issuance, ensuring that databases, APIs, and inter-service authentication rely on short-lived, auditable secrets rather than static credentials. Boundary addresses secure human access to infrastructure, replacing traditional bastion hosts and broad network access with identity-based, just-in-time sessions to specific targets.

## Outcomes and Key Takeaways

The combined architecture delivers a pragmatic blueprint for organizations that need to scale beyond a single team and a single runtime without sacrificing security or operational coherence. By aligning AWS account boundaries with service ownership, choosing runtimes based on workload fit, and using a consistent set of HashiCorp tools for provisioning, networking, secrets, and access, organizations can give individual teams autonomy while preserving enterprise-wide guardrails.

The overarching message is that successful SOA adoption is as much about disciplined platform engineering as it is about decomposing services. Treating infrastructure, identity, networking, and access as cross-cutting platform concerns enables service teams to focus on business logic, while a unified tooling layer keeps the distributed system observable, secure, and manageable as it grows.