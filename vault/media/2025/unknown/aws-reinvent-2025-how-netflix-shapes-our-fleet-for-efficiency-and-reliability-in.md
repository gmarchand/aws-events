---
clients:
- Netflix
- AWS
date: 2025-12-02
description: Netflix's strategy for optimizing its cloud architecture for efficiency
  and reliability. Placement of workloads on price-optimal hardware by automatically
  modeling capacity requirements and understanding AWS hardware performance and pricing.
  The talk will also cover a continuous optimization loop that monitors and reshapes
  the fleet to maintain business outcomes as load patterns change. Finally, it will
  touch upon managing traffic demand and compute supply to ensure availability during
  unexpecte
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- netflix
- cloud
- optimization
- reliability
- infrastructure
- reinvent
thematic: media
title: AWS re:Invent 2025 - How Netflix Shapes our Fleet for Efficiency and Reliability
  (IND387)
url: https://www.youtube.com/watch?v=K-2u50e0VzA
video_id: K-2u50e0VzA
year: 2025
---

# AWS re:Invent 2025 - How Netflix Shapes our Fleet for Efficiency and Reliability (IND387)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=K-2u50e0VzA)
> 📅 2025-12-02 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]]

# How Netflix Shapes Its Fleet for Efficiency and Reliability

## Overview of Netflix's Cloud Optimization Strategy

Netflix operates one of the largest and most demanding cloud workloads in the world, requiring a deliberate strategy to balance cost efficiency with the reliability that millions of streaming customers expect. In this session, Netflix engineers walked through how the company shapes its AWS fleet to achieve both goals simultaneously, explaining that efficiency and reliability are not opposing forces but rather complementary outcomes of disciplined automation, continuous measurement, and a deep understanding of how workloads behave on different hardware. The central thesis is that Netflix has moved beyond static infrastructure decisions toward a dynamic, data-driven model in which workloads are continuously matched to the most appropriate compute resources available within AWS.

## Matching Workloads to Optimal Hardware

### Modeling Capacity Requirements Automatically

Netflix has invested heavily in automated systems that model the capacity requirements of each workload rather than relying on engineers to manually pick instance types. By profiling how services consume CPU, memory, network, and storage resources under real production traffic, the platform can characterize each workload's resource fingerprint. This profiling forms the foundation for placement decisions, ensuring that capacity sizing reflects actual behavior rather than worst-case guesses or legacy choices that may no longer apply as services evolve.

### Understanding AWS Hardware Performance and Pricing

Equally important to modeling demand is understanding the supply side of the equation. Netflix continuously evaluates the performance characteristics and pricing of the AWS instance portfolio, including newer generations such as Graviton-based instances. By combining performance benchmarks with current pricing signals, the company can identify which hardware delivers the best price-to-performance ratio for each specific workload type. This means that a service which is memory-bound may land on a fundamentally different instance family than one that is CPU-bound or network-intensive, and those decisions are revisited as the AWS hardware landscape changes.

### Placing Workloads on Price-Optimal Hardware

The combination of demand modeling and hardware understanding allows Netflix to place workloads on the price-optimal hardware automatically. Rather than treating instance selection as a one-time architectural decision, Netflix treats it as a continuous optimization problem. As new instance generations become available or as workload characteristics shift, services can be migrated to better-suited hardware without manual intervention from individual application teams.

## Continuous Optimization and Fleet Reshaping

### Monitoring Business Outcomes Over Time

A static optimization is quickly outdated, so Netflix has built a continuous optimization loop that constantly monitors the fleet against business outcomes. Rather than focusing solely on infrastructure metrics, this loop ties resource decisions back to higher-level signals such as service health, latency targets, and cost efficiency. When load patterns change due to seasonal viewing trends, content launches, or evolving user behavior, the system detects drift between current placement and optimal placement.

### Reshaping the Fleet Dynamically

When drift is detected, Netflix reshapes the fleet by adjusting instance counts, swapping instance types, or rebalancing workloads across availability zones and regions. This reshaping happens with guardrails that protect availability, ensuring that optimization activity never compromises the streaming experience. The presenters emphasized that this loop must run continuously because the cost of inaction compounds quickly at Netflix's scale, while the cost of automation, once built, scales gracefully across the entire fleet.

## Managing Traffic Demand and Compute Supply

### Handling Unexpected Load Shifts

The final theme of the talk addressed how Netflix manages the relationship between traffic demand and compute supply during unexpected events. Whether the cause is a viral content release, a regional failover, or an external disruption, demand can shift dramatically in short windows of time. Netflix has invested in mechanisms that scale supply ahead of demand where possible and that shed or reshape demand intelligently when supply cannot keep up, all with the goal of preserving availability for end users.

### Balancing Efficiency and Reliability as a Single Discipline

The session closed by reinforcing that Netflix treats efficiency and reliability as a single engineering discipline. Running lean is what creates the headroom and operational discipline needed to absorb shocks, while reliability practices ensure that aggressive optimization never harms the customer experience. By combining automated workload modeling, hardware-aware placement, continuous fleet reshaping, and proactive demand-supply management, Netflix has built a cloud operating model that delivers strong business outcomes while making efficient use of every dollar spent on AWS.