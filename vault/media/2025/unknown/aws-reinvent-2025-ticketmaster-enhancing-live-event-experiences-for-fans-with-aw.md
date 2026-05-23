---
clients:
- Ticketmaster
- AWS
date: 2025-12-07
description: 'Discover how Ticketmaster, the world''s largest ticket marketplace,
  delivers superior live event experiences by bringing its online ticket sales and
  distribution platform closer to fans with AWS Local Zones. Learn how Ticketmaster
  overcame technical challenges by reducing latency while using AWS native compute,
  storage, and other services. We''ll examine the architectural evolution, critical
  decisions, and the transformative impact of onboarding latency-sensitive applications
  to Local Zones. This '
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- cloud
- ticketmaster
- live-events
- local-zones
- latency
- ticketing
thematic: media
title: 'AWS re:Invent 2025 - Ticketmaster: Enhancing live event experiences for fans
  with AWS (SPF206)'
url: https://www.youtube.com/watch?v=NfWAAW8MiCM
video_id: NfWAAW8MiCM
year: 2025
---

# AWS re:Invent 2025 - Ticketmaster: Enhancing live event experiences for fans with AWS (SPF206)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=NfWAAW8MiCM)
> 📅 2025-12-07 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Ticketmaster]] [[AWS]]

# Ticketmaster: Enhancing Live Event Experiences for Fans with AWS

## Overview of the Session

At AWS re:Invent 2025, Ticketmaster, the world's largest ticket marketplace, presented how it leverages AWS Local Zones to deliver superior live event experiences to fans around the globe. The session detailed the company's journey to bring its online ticket sales and distribution platform closer to its end users, addressing the demanding performance requirements that come with selling tickets to high-profile concerts, sporting events, and shows where every millisecond of latency can affect a fan's chance to secure a seat.

## Architectural Evolution and Technical Challenges

### Reducing Latency Through Distributed Cloud

Ticketmaster's central challenge has always been managing extreme traffic spikes when popular events go on sale, while maintaining a consistently fast and reliable purchasing experience. The company adopted AWS Local Zones to extend its infrastructure into geographies closer to its fan base, significantly reducing round-trip latency for time-sensitive transactions. By placing latency-sensitive workloads at the edge, Ticketmaster ensures that fans experience faster page loads, quicker queue processing, and more responsive checkout flows during peak demand moments.

The session walked through the architectural evolution of the platform, showing how Ticketmaster transitioned from a more centralized cloud footprint to a distributed model. This shift required rethinking how compute, storage, and supporting services are deployed and orchestrated across multiple Local Zones, while preserving consistency, security, and operational simplicity.

### Leveraging AWS Native Services

To achieve this transformation, Ticketmaster relied on AWS native compute and storage services running within Local Zones, complemented by services in parent AWS Regions for workloads that did not require ultra-low latency. The team made deliberate decisions about which components of the ticketing stack belonged at the edge versus in the core, balancing performance gains against operational complexity. This hybrid distribution model allowed the company to onboard latency-sensitive applications to Local Zones without rearchitecting the entire platform.

## Critical Decisions and Transformative Impact

### Balancing Innovation with Fan Experience

The presenters emphasized the critical decisions that shaped the migration, including how to identify candidate workloads for Local Zones, how to test latency improvements meaningfully, and how to roll out changes safely in a business where downtime during a major on-sale event is not an option. Operational practices, observability, and capacity planning all evolved to match the distributed footprint.

### Setting New Standards for Distributed Cloud

The transformative impact of this implementation extends beyond performance metrics. By measurably reducing latency for fans, Ticketmaster has improved conversion rates, reduced abandonment during high-demand on-sales, and elevated overall satisfaction with the live event purchasing experience. The session positioned Ticketmaster's approach as a benchmark for how large-scale, traffic-intensive consumer platforms can adopt distributed cloud architectures, demonstrating that innovation at the edge and a superior end-user experience are complementary rather than competing goals.

## Key Takeaways

Ticketmaster's collaboration with AWS illustrates how AWS Local Zones enable global consumer platforms to deliver responsive, reliable experiences at scale. The session offered practical insights for organizations considering similar moves: start by identifying genuinely latency-sensitive workloads, leverage AWS native services to minimize integration overhead, and treat distributed deployment as an evolution rather than a rewrite. For Ticketmaster, the outcome is a platform better equipped to serve fans the moment tickets go on sale, reinforcing its leadership in the live event marketplace.