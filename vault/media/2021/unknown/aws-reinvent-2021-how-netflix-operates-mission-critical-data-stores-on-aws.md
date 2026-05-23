---
clients:
- Netflix
- AWS
date: 2021-12-17
description: Netflix relies heavily on high-performance data stores like EVCache to
  serve its mission of entertaining the world. Trusting in the submillisecond latencies
  served by EVCache poses a wide range of challenges, including operations, debugging,
  and mean time to react. In this session, learn how distributed database engineers
  with over a decade of experience running high-performance data stores at massive
  scale (billions of operations per second) have established tools, techniques, and
  approaches on
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- aws
- netflix
- data-stores
- evcache
- cloud
- streaming
- operations
thematic: media
title: AWS re:Invent 2021 - How Netflix operates mission-critical data stores on AWS
url: https://www.youtube.com/watch?v=MtGYgilaPgo
video_id: MtGYgilaPgo
year: 2021
---

# AWS re:Invent 2021 - How Netflix operates mission-critical data stores on AWS

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=MtGYgilaPgo)
> 📅 2021-12-17 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[Netflix]] [[AWS]]

# How Netflix Operates Mission-Critical Data Stores on AWS

## Introduction

Netflix's mission to entertain the world depends on a complex backend of high-performance data stores capable of supporting billions of operations per second at submillisecond latencies. At the heart of this infrastructure sits EVCache, Netflix's distributed caching solution, alongside other mission-critical databases that power virtually every member-facing experience. This session, delivered by Netflix's distributed database engineers with more than a decade of experience operating data stores at massive scale, explores how the company has built tools, techniques, and operational practices on AWS to maintain reliability, debug issues quickly, and meet stringent service level objectives without compromising engineer well-being.

## Operating Data Stores at Netflix Scale

### The Challenges of Submillisecond Latency

Trusting submillisecond latency commitments creates a uniquely demanding operational environment. When services depend on responses arriving in less than a millisecond, even minor disruptions—a single noisy neighbor, a degraded instance, or a transient network blip—can cascade into user-visible failures. Netflix engineers must therefore design for resilience at every layer, anticipating failures rather than reacting to them. The session highlights how operating EVCache and similar systems requires a deep understanding of AWS infrastructure behavior, careful capacity planning, and constant vigilance over performance signals that change on the order of microseconds.

### Tooling, Debugging, and Mean Time to React

A central theme of the discussion is the importance of reducing mean time to react when incidents occur. Netflix has invested heavily in observability tooling that surfaces anomalies before they escalate, allowing engineers to pinpoint root causes across distributed clusters spanning multiple AWS regions. The team relies on automation to mitigate common failure modes, replacing unhealthy nodes, rebalancing traffic, and isolating problematic components without manual intervention. Debugging at this scale demands rich telemetry, the ability to correlate signals across application and infrastructure layers, and runbooks refined through repeated incident response. By codifying institutional knowledge into tools and automated workflows, Netflix shortens recovery times and limits the operational burden on its on-call engineers.

### Meeting SLOs Without Losing Sleep

The session closes with practical guidance on fulfilling demanding service level objectives sustainably. Netflix's approach combines proactive failure injection, redundancy across availability zones, and a culture that treats reliability as a shared engineering responsibility rather than a reactive firefight. By embracing AWS primitives, designing for graceful degradation, and continuously investing in tooling that compresses detection and remediation timelines, the team ensures that mission-critical data stores remain dependable even as scale and complexity grow.

## Key Takeaways

Netflix's experience demonstrates that operating mission-critical data stores on AWS at billions of operations per second is achievable when engineering teams commit to robust observability, automation-driven mitigation, and disciplined SLO management. The combination of EVCache's submillisecond performance with thoughtful operational practices allows Netflix to deliver a reliable streaming experience globally. For organizations facing similar challenges, the message is clear: invest in tools that accelerate debugging, design systems that absorb failure gracefully, and treat reliability as an ongoing engineering investment rather than an afterthought.