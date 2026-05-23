---
clients:
- Amazon CloudFront
- AWS Media Services
- Amazon
- AWS
date: 2025-09-29
description: 'Deploying infrastructure across multiple availability zones and regions
  is an effective approach to achieve higher levels of resiliency and deliver a high
  quality of experience to viewers. Media Quality-Aware Resiliency (MQAR) is an integrated
  capability between Amazon CloudFront and AWS Media Services that automatically detects,
  reacts to, and provides visibility into potential issues within live streaming pipelines.
  This demonstration explores three different architectures, including MQAR, to '
event: ibc-2025-demo-showcase
has_transcript: true
language: en
playlist: IBC 2025 Demo Showcase
tags:
- live-streaming
- resiliency
- cloudfront
- aws
- media-services
- multi-region
- quality-of-experience
thematic: media
title: Media Quality-Aware Resiliency (MQAR) for live streaming
url: https://www.youtube.com/watch?v=fS509FxDbQE
video_id: fS509FxDbQE
year: 2025
---

# Media Quality-Aware Resiliency (MQAR) for live streaming

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=fS509FxDbQE)
> 📅 2025-09-29 | 🎤 ibc-2025-demo-showcase | 🌐 en
> 🏢 Clients: [[Amazon CloudFront]] [[AWS Media Services]] [[Amazon]] [[AWS]]

# Media Quality-Aware Resiliency (MQAR) for Live Streaming

## Overview and Purpose

Live streaming workloads demand exceptional levels of resiliency to maintain a high quality of experience for viewers, particularly during high-stakes broadcasts where any disruption can directly impact audience engagement and revenue. Deploying infrastructure across multiple Availability Zones and AWS Regions has long been recognized as a foundational strategy for achieving this resiliency, but operating such distributed pipelines introduces significant complexity. Operators must continuously monitor video quality, detect upstream issues, and respond rapidly when something goes wrong. To address these operational challenges, AWS has introduced Media Quality-Aware Resiliency, known as MQAR, which is an integrated capability that spans Amazon CloudFront and the AWS Media Services portfolio. MQAR is designed to automatically detect, react to, and provide visibility into potential issues within live streaming pipelines, reducing the manual burden on broadcast operations teams.

## Architectural Approaches to Resiliency

### Comparing Three Pipeline Designs

The demonstration explores three distinct architectures for delivering live streams on AWS, each representing a progression in resiliency sophistication. The first approach relies on a more traditional multi-AZ or multi-Region setup where redundancy is built into the encoding and packaging layers, but failover decisions and quality assessments depend heavily on operator intervention or basic health checks. While effective at handling infrastructure-level failures, this approach can be slow to react to subtle media quality issues that do not manifest as outright service outages.

The second architecture introduces additional monitoring and automation, improving the speed at which problems are detected and isolated, yet still requires considerable configuration and operational oversight to interpret signals correctly and trigger appropriate responses. The third architecture incorporates MQAR directly, leveraging the native integration between CloudFront and AWS Media Services such as MediaLive and MediaPackage. In this design, the platform itself becomes aware of media quality, allowing CloudFront to make intelligent routing decisions based on the actual health of the upstream pipelines rather than relying solely on infrastructure metrics.

### How MQAR Detects and Responds to Issues

MQAR works by continuously evaluating signals from the encoding and packaging stages of the workflow, identifying upstream errors that might otherwise go unnoticed until they affect viewers. When a degradation is detected, the integration enables CloudFront to automatically shift traffic toward healthy pipelines, providing seamless failover without requiring operators to manually intervene. This automated responsiveness substantially shortens the time between problem occurrence and resolution, which is especially valuable for live events where even brief disruptions are highly visible.

## Operational Benefits and Outcomes

By embedding media quality awareness into the delivery layer, MQAR reduces the operational burden traditionally associated with running resilient live streaming workloads. Teams gain improved visibility into the health of their pipelines, faster reaction times to upstream errors, and a more reliable viewer experience overall. The demonstration ultimately illustrates that while multi-AZ and multi-Region deployments remain essential building blocks, integrating MQAR represents a meaningful step forward in simplifying resilient architectures and ensuring that quality issues are identified and mitigated automatically. For broadcasters and streaming providers running live workloads on AWS, adopting MQAR offers a practical path to higher availability, lower operational complexity, and a consistently high quality of experience for their audiences.