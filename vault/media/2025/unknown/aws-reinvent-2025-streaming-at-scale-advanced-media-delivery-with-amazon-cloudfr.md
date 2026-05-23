---
clients:
- Amazon CloudFront
- AWS
- Amazon
- AWS Elemental
date: 2025-12-04
description: Learn how Amazon CloudFront powers high-profile streaming events with
  low-latency, scalable delivery. Discover how to optimize caching using embedded
  POPs, reduce origin load with Origin Shield, and fine-tune streaming performance.
  We will dive into Common Media Server Data (CMSD) techniques that dynamically adjust
  to network conditions, maintaining high-quality viewing experiences for global audiences.
  We’ll also explore integrations with AWS Elemental Media services for personalized
  ad deliver
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- streaming
- cloudfront
- cdn
- low-latency
- caching
- media-delivery
- aws
thematic: media
title: 'AWS re:Invent 2025 - Streaming at Scale: Advanced Media Delivery with Amazon
  CloudFront (NET307)'
url: https://www.youtube.com/watch?v=fdEizoLj5tU
video_id: fdEizoLj5tU
year: 2025
---

# AWS re:Invent 2025 - Streaming at Scale: Advanced Media Delivery with Amazon CloudFront (NET307)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=fdEizoLj5tU)
> 📅 2025-12-04 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Amazon CloudFront]] [[AWS]] [[Amazon]] [[AWS Elemental]]

# Streaming at Scale: Advanced Media Delivery with Amazon CloudFront

## Session Overview

This AWS re:Invent 2025 session (NET307) explores how Amazon CloudFront delivers high-profile streaming events at scale, combining low-latency performance with the flexibility to handle massive, geographically distributed audiences. The presentation focuses on the architectural patterns and optimization techniques that allow broadcasters and streaming providers to maintain consistent quality of experience even during peak demand moments such as live sporting events. The discussion is grounded in real-world practice, featuring insights from the New England Sports Network (NESN) on how it applies these capabilities to power its live sports streaming workflows.

## Optimizing Delivery Through CloudFront's Edge Architecture

### Caching Strategies and Origin Protection

A central theme of the session is how CloudFront's distributed infrastructure reduces latency and protects origins under heavy load. Embedded Points of Presence (POPs) extend the CloudFront network deeper into last-mile networks, placing cached content closer to viewers and improving startup times for video segments and manifests. To complement this edge tier, Origin Shield adds an intermediate caching layer that consolidates requests before they reach the origin, dramatically reducing origin load during traffic spikes typical of live streaming events. Together, these capabilities create a layered caching architecture that maximizes offload while keeping content fresh.

### Adapting to Network Conditions with CMSD

The session dives into Common Media Server Data (CMSD), an emerging standard that allows servers and CDNs to communicate metadata about cached content, network conditions, and delivery performance back to clients. By exposing signals such as cache status, estimated throughput, and round-trip times, CMSD enables adaptive bitrate players to make smarter decisions about which renditions to request, helping maintain a high-quality viewing experience even as network conditions fluctuate. This dynamic feedback loop is particularly valuable for live streams where buffer margins are tight and rebuffering events are highly visible to viewers.

### Integrations with AWS Elemental Media Services

Beyond pure delivery, the session examines how CloudFront integrates with AWS Elemental Media services to enable advanced workflows including personalized ad delivery and multi-region origin configurations. These integrations support server-side ad insertion at scale, allowing each viewer to receive tailored advertising while still benefiting from the cache efficiency of shared video segments. Multi-region origins improve resilience and provide failover paths so that streams remain available even if a regional component experiences disruption.

## Customer Perspective: NESN's Live Sports Streaming

NESN shares its operational experience using CloudFront and AWS media services to broadcast popular sporting events to its regional audience. The network describes how it leverages the discussed capabilities — edge caching, Origin Shield, CMSD-driven adaptive delivery, and Elemental integrations — to deliver reliable, low-latency streams for time-sensitive live content. Their experience illustrates how the architectural patterns presented translate into measurable improvements in viewer quality of experience and operational stability during high-stakes broadcasts.

## Key Takeaways

The session ultimately demonstrates that delivering streaming media at scale requires more than raw CDN capacity; it depends on a coordinated set of optimizations spanning the edge network, the origin tier, and the player itself. By combining embedded POPs, Origin Shield, CMSD-based intelligence, and tight integration with AWS Elemental Media services, organizations can build streaming architectures that are simultaneously performant, resilient, and capable of supporting personalized experiences. The NESN case study reinforces that these techniques are not theoretical but are actively powering live broadcasts today, providing a practical blueprint for other media organizations seeking to elevate their streaming delivery on AWS.