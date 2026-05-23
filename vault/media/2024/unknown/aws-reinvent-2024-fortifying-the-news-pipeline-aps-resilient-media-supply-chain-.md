---
clients:
- AWS
- Associated Press
- AP
date: 2024-12-04
description: The Associated Press modernized its mission-critical publishing platform
  using serverless patterns across multiple AWS regions. This cutting-edge platform
  helps the AP in its mission to produce fast, accurate journalism seen by over half
  the world’s population every day. Learn how the AP worked with AWS to review and
  strengthen the fault tolerance of their media supply chain platform. Explore the
  strategies and architectural patterns implemented to ensure uninterrupted news delivery,
  even in the
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- serverless
- multi-region
- media-supply-chain
- resilience
- publishing
- cloud
thematic: media
title: 'AWS re:Invent 2024 - Fortifying the news pipeline: AP''s resilient media supply
  chain on AWS (IMP204)'
url: https://www.youtube.com/watch?v=OUVoXwlXnP0
video_id: OUVoXwlXnP0
year: 2024
---

# AWS re:Invent 2024 - Fortifying the news pipeline: AP's resilient media supply chain on AWS (IMP204)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=OUVoXwlXnP0)
> 📅 2024-12-04 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Associated Press]] [[AP]]

# Fortifying the News Pipeline: AP's Resilient Media Supply Chain on AWS

## Overview of the Modernization Initiative

The Associated Press, one of the world's most trusted news organizations, undertook a comprehensive modernization of its mission-critical publishing platform in collaboration with AWS. This platform serves as the backbone of AP's journalistic mission, delivering fast and accurate news content that reaches more than half of the global population every day. Given the scale and visibility of AP's reporting, even brief disruptions to the publishing pipeline carry significant consequences for both the organization and the broader media ecosystem that depends on its feeds. To meet these demands, AP rearchitected its media supply chain using serverless patterns deployed across multiple AWS regions, prioritizing resilience, fault tolerance, and uninterrupted news delivery.

## Architectural Strategy and Resilience Patterns

### Multi-Region Serverless Foundations

At the core of the redesigned platform is a serverless architecture that spans multiple AWS regions. By adopting managed services rather than maintaining traditional server infrastructure, AP reduced operational overhead while gaining the elasticity needed to handle the unpredictable surges that accompany breaking news events. The multi-region deployment model ensures that if one region experiences degradation or a complete outage, traffic and processing seamlessly continue from another region, preserving the continuous flow of stories, photos, and video to AP's worldwide subscribers.

### Strengthening Fault Tolerance Across the Supply Chain

Working closely with AWS, AP conducted a thorough review of its media supply chain to identify single points of failure and weak links in fault tolerance. The teams implemented architectural patterns designed to isolate failures, gracefully degrade non-critical functionality, and recover automatically from regional disruptions. These patterns were applied end-to-end across the publishing pipeline—from content ingestion and editorial workflows through transformation, enrichment, and final distribution—ensuring that resilience is a property of the entire system rather than just isolated components.

### Operational Continuity and Uptime Assurance

The session emphasized how the redesigned platform meets the rigorous uptime requirements expected of a global news wire. Through careful workload placement, automated failover mechanisms, and continuous validation of recovery procedures, AP gained confidence that its systems can withstand the kinds of regional events that historically threaten cloud-based services. The result is a publishing platform engineered to keep delivering journalism without interruption, even under adverse conditions.

## Key Takeaways for Building Resilient Workloads

The collaboration between AP and AWS offers a practical blueprint for organizations seeking to build highly available and resilient workloads on AWS. The discussion underscored that resilience is achieved not by any single technology choice but through deliberate architectural decisions, disciplined use of serverless and multi-region patterns, and ongoing investment in fault tolerance reviews. For enterprises with demanding operational continuity requirements, AP's experience demonstrates that mission-critical platforms can be modernized to meet stringent reliability standards while simultaneously gaining the agility and scalability advantages of cloud-native design.