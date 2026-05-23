---
clients:
- Prime Video
- AWS
- NFL
date: 2024-12-05
description: Streaming live sports at scale is critical to meeting viewer expectations
  in today’s digital age. Prime Video, as the exclusive home of Thursday Night Football,
  ensures a seamless experience during peak NFL game times by leveraging a combination
  of multi-Region traffic routing and elastic compute on AWS. In this session, learn
  how Prime Video uses multiple AWS Regions, scheduled AWS auto scaling to pre-scale
  capacity, and dynamic auto scaling to respond to unanticipated viewership spikes.
  Discov
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- streaming
- live
- sports
- nfl
- aws
- prime-video
- scaling
thematic: media
title: AWS re:Invent 2024 - Scaling Prime Video for peak NFL streaming on AWS (ARC311)
url: https://www.youtube.com/watch?v=jZsoQ4qs1bM
video_id: jZsoQ4qs1bM
year: 2024
---

# AWS re:Invent 2024 - Scaling Prime Video for peak NFL streaming on AWS (ARC311)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=jZsoQ4qs1bM)
> 📅 2024-12-05 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Prime Video]] [[AWS]] [[NFL]]

# Scaling Prime Video for Peak NFL Streaming on AWS

## Overview of the Streaming Challenge

Prime Video serves as the exclusive home of Thursday Night Football, a position that demands flawless delivery of live sports content to millions of concurrent viewers. Live sports streaming represents one of the most demanding workloads in digital media because audience demand spikes dramatically at kickoff, latency expectations are unforgiving, and any disruption directly impacts the fan experience. To meet these expectations, Prime Video has architected a streaming platform on AWS that combines multi-Region resiliency with sophisticated scaling strategies, ensuring uninterrupted coverage even when viewership surges unexpectedly.

## Architectural Foundations on AWS

### Multi-Region Traffic Routing for Resilience

Prime Video distributes its workload across multiple AWS Regions to eliminate single points of failure and provide geographic redundancy. By routing traffic intelligently between Regions, the team can shift load away from any Region experiencing degradation and maintain consistent service quality. This multi-Region posture not only protects against localized issues but also allows engineers to perform maintenance and deployments without affecting the live viewing experience. Traffic management decisions are central to the operating model, since they determine how viewer requests reach the optimal compute capacity in real time.

### Compute and Data Services Powering the Platform

The streaming stack relies on a portfolio of AWS compute and data services, each chosen for the workload characteristics it serves best. Amazon EC2 delivers the raw compute horsepower required for sustained high-throughput services, while AWS Lambda handles event-driven and bursty workloads without operational overhead. Containerized microservices run on Amazon ECS with AWS Fargate, giving teams a serverless container experience that simplifies scaling and deployment. Amazon DynamoDB underpins the data layer, providing single-digit-millisecond performance at the massive request rates generated during peak game moments. Together, these services give Prime Video the elasticity and performance profile that live sports demand.

## Scaling Strategies for Peak Viewership

### Scheduled Pre-Scaling Ahead of Kickoff

Because game start times are known well in advance, Prime Video uses scheduled AWS auto scaling to provision capacity before viewers arrive. By warming up fleets of EC2 instances, Fargate tasks, and supporting infrastructure ahead of kickoff, the platform absorbs the initial wave of concurrent connections without cold-start delays or scaling lag. This proactive approach is essential for live sports, where the opening minutes of a broadcast generate the steepest concurrency curve and where any delay in scaling response would translate directly into viewer-facing errors or buffering.

### Dynamic Auto Scaling for Unanticipated Spikes

Even with careful pre-scaling, live events produce unpredictable surges driven by overtime games, viral moments, or external news. Prime Video layers dynamic auto scaling on top of its scheduled capacity to react to these spikes in real time. The system monitors live demand signals and adjusts capacity across compute services automatically, ensuring headroom is always available. This combination of scheduled and dynamic scaling produces a defense-in-depth approach to capacity management, where predictable demand is met proactively and unexpected demand is absorbed reactively.

## Operational Best Practices and Outcomes

The session distills lessons learned into a set of best practices for teams running large-scale streaming workloads. Engineers are encouraged to design for multi-Region from the beginning rather than retrofitting it later, to validate scaling behavior through realistic load testing, and to choose the right compute primitive for each workload pattern rather than standardizing on a single service. Observability across Regions and services is treated as foundational, since rapid detection and response are what allow the platform to meet its availability targets during high-stakes broadcasts.

The outcome of this architecture is a streaming experience that delivers Thursday Night Football to millions of fans with the reliability and performance expected of premium live sports. By combining multi-Region traffic routing, scheduled pre-scaling, dynamic elasticity, and a thoughtfully selected portfolio of AWS services, Prime Video has built a platform capable of handling the most demanding moments in live entertainment while continuing to evolve as audience expectations grow.