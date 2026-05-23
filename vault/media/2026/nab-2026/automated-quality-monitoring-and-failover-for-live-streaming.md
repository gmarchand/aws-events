---
clients:
- Amazon CloudFront
- AWS Media Services
- AWS
date: 2026-05-13
description: "Live streaming operations teams struggle to detect and respond to quality
  issues before viewers are affected. Manual monitoring across multiple availability
  zones and regions is reactive and resource-intensive, often catching problems too
  late. \n\nThis demonstration shows automated quality monitoring and failover for
  live streaming pipelines powered by Media Quality-Aware Resiliency (MQAR), an integrated
  capability between Amazon CloudFront and AWS Media Services that automatically detects,
  react"
event: nab-2026
has_transcript: true
language: en
playlist: NAB 2026
tags:
- live
- streaming
- monitoring
- failover
- quality
- automation
- operations
thematic: media
title: Automated quality monitoring and failover for live streaming
url: https://www.youtube.com/watch?v=BKMYnxmmCxo
video_id: BKMYnxmmCxo
year: 2026
---

# Automated quality monitoring and failover for live streaming

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=BKMYnxmmCxo)
> 📅 2026-05-13 | 🎤 nab-2026 | 🌐 en
> 🏢 Clients: [[Amazon CloudFront]] [[AWS Media Services]] [[AWS]]

# Automated Quality Monitoring and Failover for Live Streaming

## The Operational Challenge in Live Streaming

Live streaming operations teams face a persistent and costly problem: detecting quality issues before viewers experience them. Traditional monitoring approaches require teams to manually observe streams across multiple availability zones and AWS Regions, creating a reactive posture that often identifies problems only after audiences have already been affected. This approach is not only resource-intensive but fundamentally inadequate for the scale and complexity of modern live streaming workloads, where milliseconds of disruption can translate into significant viewer churn and revenue loss.

The core issue lies in the disconnect between where problems originate—often deep within the streaming pipeline—and where they become visible to operators. By the time a human notices a degraded stream, the damage to viewer experience has already occurred, and remediation becomes a scramble rather than a controlled response.

## Media Quality-Aware Resiliency as a Solution

### Integrated Detection Across CloudFront and AWS Media Services

The demonstration centers on Media Quality-Aware Resiliency, known as MQAR, which is an integrated capability that bridges Amazon CloudFront with AWS Media Services. Rather than treating content delivery and media processing as isolated domains, MQAR establishes a continuous feedback loop between them. CloudFront, sitting at the edge closest to viewers, communicates quality signals back to the upstream media services, allowing the platform itself to recognize when something is wrong with the live pipeline. This integration removes the need for operators to stitch together signals from disparate monitoring tools and instead delivers a unified view of pipeline health.

### Automatic Reaction and Cross-Region Resilience

Beyond detection, MQAR automatically reacts to identified issues, executing failover procedures without requiring human intervention. The demonstration showcases these techniques operating both within a single AWS Region—shifting between availability zones when localized issues emerge—and across AWS Regions when broader disruptions occur. This dual-layer resiliency ensures that upstream errors, whether caused by encoder failures, ingest problems, or regional service degradation, are contained before they propagate to the viewer. The system provides visibility into these events as they happen, giving operations teams the context they need to understand what occurred and why.

### Outcomes for Operations Teams

The practical result of deploying MQAR is a fundamental shift from reactive firefighting to proactive issue management. Quality problems are detected at the moment they begin to manifest, recovery happens automatically and transparently to the viewer, and the operational burden on streaming teams drops significantly. Engineers no longer need to maintain constant vigilance across dashboards spanning multiple regions; instead, they can focus on higher-value work while the platform handles routine resilience tasks. For organizations running live streaming workloads on AWS, this translates to more reliable broadcasts, better viewer retention, and a leaner operational model.

## Strategic Implications for Live Streaming Workloads

The broader significance of this capability lies in how it redefines the boundary between platform responsibility and customer responsibility. By embedding quality awareness directly into the integration between CloudFront and Media Services, AWS is taking on monitoring and failover concerns that customers previously had to engineer themselves. This shift allows live streaming providers to deliver enterprise-grade reliability without building bespoke monitoring stacks, lowering the barrier to operating high-quality live experiences at scale and making sophisticated resilience patterns accessible to a wider range of customers.