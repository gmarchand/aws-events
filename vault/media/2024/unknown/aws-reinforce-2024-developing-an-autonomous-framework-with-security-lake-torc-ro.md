---
clients:
- AWS
- Amazon
- Torc Robotics
date: 2024-06-12
description: Security teams are increasingly seeking autonomy in their security operations.
  Amazon Security Lake is a powerful solution that allows organizations to centralize
  their security data across AWS accounts and Regions. In this session, learn how
  Security Lake simplifies centralizing and operationalizing security data. Then,
  hear from Torc Robotics, a leading autonomous trucking company, as they share their
  experience and best practices for using Security Lake to establish an autonomous
  security fra
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- security
- aws
- cloud
- data-lake
- autonomous
- robotics
- devops
thematic: media
title: AWS re:Inforce 2024 - Developing an autonomous framework with Security Lake
  & Torc Robotics (TDR301)
url: https://www.youtube.com/watch?v=qxOFmqmzAY8
video_id: qxOFmqmzAY8
year: 2024
---

# AWS re:Inforce 2024 - Developing an autonomous framework with Security Lake & Torc Robotics (TDR301)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=qxOFmqmzAY8)
> 📅 2024-06-12 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon]] [[Torc Robotics]]

# Developing an Autonomous Security Framework with Amazon Security Lake and Torc Robotics

## Session Overview

This AWS re:Inforce 2024 session (TDR301) explores how modern security teams can achieve greater autonomy in their operations by centralizing and operationalizing security data at scale. The presentation combines an in-depth look at Amazon Security Lake's capabilities with a real-world implementation story from Torc Robotics, a leading autonomous trucking company. Together, the speakers demonstrate how unified security data architectures empower organizations to detect threats faster, respond more effectively, and build self-sustaining security frameworks aligned with the demands of complex, multi-account AWS environments.

## Centralizing Security Data with Amazon Security Lake

### The Case for a Unified Security Data Architecture

Security teams today face a sprawling landscape of logs, telemetry, and alerts distributed across accounts, regions, and third-party tools. The session emphasizes that this fragmentation slows investigation, complicates compliance, and limits the effectiveness of analytics. Amazon Security Lake addresses these challenges by automatically aggregating security data from AWS environments, SaaS providers, on-premises systems, and custom sources into a purpose-built data lake stored in the customer's account. By normalizing this data into the Open Cybersecurity Schema Framework (OCSF), Security Lake removes the heavy lifting of schema reconciliation and allows teams to query consistent, well-structured data using their preferred analytics tools.

### Operationalizing Security Lake

Beyond simply storing data, Security Lake is positioned as a foundation for operational security. The session highlights how customers can use the service to power detection engineering, threat hunting, incident response, and compliance reporting without rebuilding pipelines for each use case. Subscribers—whether SIEMs, analytics platforms, or custom applications—can consume normalized data directly, enabling security engineers to focus on outcomes rather than data plumbing. This consolidation supports the broader goal of building scalable, repeatable security operations that can keep pace with growing cloud workloads.

## Torc Robotics' Autonomous Security Framework

### Business Context and Security Requirements

Torc Robotics shares its journey of designing a security architecture suited to a company developing autonomous trucking technology, where safety, intellectual property protection, and operational reliability are paramount. The company's environment spans engineering, simulation, vehicle telemetry, and corporate workloads, each generating distinct security signals. Torc's security team needed a framework capable of unifying these diverse data streams while keeping pace with rapid engineering velocity and the regulatory expectations of the autonomous vehicle industry.

### Implementation and Best Practices

Torc describes how Security Lake became the cornerstone of an autonomous security model—one in which detection, enrichment, and response activities are automated wherever possible. The team consolidated logs from across AWS accounts and integrated third-party security sources, leveraging OCSF normalization to simplify analytics and reduce custom parsing work. They emphasize the importance of strong account governance, well-defined data ownership, and clear naming and tagging conventions to make a centralized data lake manageable at scale. The team also discusses pairing Security Lake with downstream analytics and SIEM tools to drive automated detections, while applying lifecycle policies to control storage costs as data volumes grow.

### Outcomes and Lessons Learned

The result is a security operation that requires less manual data wrangling and offers faster, more confident investigations. Torc highlights improvements in mean time to detect and respond, better visibility across previously siloed environments, and the ability to develop reusable detection content against a common schema. Key lessons shared include starting with high-value log sources before expanding coverage, investing early in automation and infrastructure-as-code for the data lake, and building close collaboration between security, platform, and engineering teams to ensure the framework evolves alongside the business.

## Key Takeaways

The session concludes by reinforcing that achieving autonomy in security operations depends on having a centralized, normalized, and accessible foundation of security data. Amazon Security Lake provides the technical capabilities to build that foundation, while Torc Robotics' experience illustrates how disciplined architecture, automation, and cross-team collaboration translate those capabilities into measurable improvements. Organizations looking to mature their cloud security posture are encouraged to begin with clear use cases, prioritize OCSF-aligned data sources, and progressively layer automation on top of a unified security data lake to realize the benefits of an autonomous security framework.