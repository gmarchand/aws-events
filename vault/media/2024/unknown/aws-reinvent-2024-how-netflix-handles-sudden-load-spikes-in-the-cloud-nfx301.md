---
clients:
- Netflix
- AWS
date: 2024-12-10
description: Netflix operates at full active across four AWS Regions, serving their
  global traffic by intelligently steering users and managing costs via thousands
  of auto scaling compute server groups. At various times, traffic surges hit their
  service that could exceed capacity. In this session, walk through how Netflix solves
  these problems by pairing predictive automated pre-scaling with fast reactive auto
  scaling in combination with advanced resilience techniques like prioritized load
  shedding, cross-Re
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- streaming
- cloud
- aws
- auto-scaling
- netflix
- load-balancing
- reinvent
thematic: media
title: AWS re:Invent 2024 - How Netflix handles sudden load spikes in the cloud (NFX301)
url: https://www.youtube.com/watch?v=TkFyZyxFRBM
video_id: TkFyZyxFRBM
year: 2024
---

# AWS re:Invent 2024 - How Netflix handles sudden load spikes in the cloud (NFX301)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=TkFyZyxFRBM)
> 📅 2024-12-10 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]]

# How Netflix Handles Sudden Load Spikes in the Cloud

## Operating at Global Scale Across Multiple AWS Regions

Netflix runs its streaming service in a fully active configuration across four AWS Regions, simultaneously serving global traffic from each. This architecture allows the company to intelligently steer users between Regions based on proximity, capacity, and operational health, while managing infrastructure costs through thousands of auto scaling compute server groups. The complexity of this footprint creates a constant balancing act: Netflix must remain ready to absorb unexpected traffic surges without overprovisioning resources that would inflate cloud spend.

The challenge intensifies when sudden load spikes—driven by major content launches, live events, regional failovers, or unexpected viewer behavior—threaten to exceed the capacity that has been carefully sized for normal demand patterns. To address this, Netflix has developed a layered strategy that combines proactive forecasting with reactive defenses, ensuring the service stays available even when traffic patterns deviate sharply from expectations.

## Combining Predictive Pre-Scaling with Reactive Auto Scaling

The foundation of Netflix's approach pairs predictive automated pre-scaling with fast reactive auto scaling. Predictive pre-scaling uses historical traffic patterns and forecasted demand to warm up capacity ahead of anticipated peaks, ensuring instances are ready before users arrive rather than scrambling to launch them mid-spike. This eliminates the cold-start latency that pure reactive scaling would impose during the most critical moments.

Reactive auto scaling complements this by responding quickly to demand signals that the predictive layer did not anticipate. By tuning scaling policies aggressively and choosing the right metrics, Netflix ensures that unforecasted surges trigger rapid capacity additions. The combination keeps steady-state costs low while preserving the agility needed to react when reality diverges from the forecast.

## Advanced Resilience Techniques for Unexpected Surges

### Prioritized Load Shedding

When demand still threatens to overwhelm available capacity, Netflix applies prioritized load shedding to protect the most important user experiences. Requests are classified by criticality, allowing the system to drop or delay lower-priority traffic—such as background tasks or non-essential calls—while preserving core playback and discovery flows. This graceful degradation keeps the service usable during the seconds or minutes it takes for additional capacity to come online.

### Cross-Region Traffic Shifting

Because Netflix operates active in four Regions, it can shift traffic across Regions when a single Region experiences pressure. This evacuation pattern redistributes users to healthier Regions with available headroom, buying time for the impacted Region to recover or scale up. The same mechanism also handles full Regional failures, turning a global footprint into a global safety net.

### Targeted Capacity Injection by Service Criticality

Rather than scaling every service uniformly during a spike, Netflix injects capacity in a targeted way based on service criticality. The most important services in the request path receive priority access to additional instances, while less critical components scale more conservatively. This nuanced approach prevents capacity contention and ensures that scarce resources flow first to the parts of the system that matter most for keeping members streaming.

## Balancing Cost Efficiency with Readiness

The overall outcome of these layered techniques is a system that maintains low baseline spend while remaining prepared for sudden load spikes. By avoiding broad overprovisioning and instead investing in intelligent automation, traffic management, and resilience patterns, Netflix demonstrates that cost efficiency and reliability at massive scale are complementary rather than conflicting goals. The session offers a blueprint for any organization running latency-sensitive workloads on AWS that must absorb unpredictable demand without abandoning financial discipline.