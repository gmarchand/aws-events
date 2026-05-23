---
clients:
- AWS
- Amazon CloudFront
- Peacock
date: 2023-12-05
description: Learn how AWS collaborates with streaming providers to deliver live sporting
  events at scale to millions of fans globally. In this session, hear how Peacock
  brings fans the most live sports of any streamer in the United States across a multitude
  of devices. Dive deep into Peacock’s delivery architecture, optimized with Amazon
  CloudFront Origin Shield to reduce load on the origin while delivering at low latency
  and high reliability. Finally, explore their innovative end-to-end workflow with
  AWS E
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- streaming
- live
- sports
- cloudfront
- aws
- peacock
- ott
thematic: media
title: AWS re:Invent 2023 - Live video streaming with Amazon CloudFront and Peacock
  (NET328)
url: https://www.youtube.com/watch?v=mttGiB6AEDg
video_id: mttGiB6AEDg
year: 2023
---

# AWS re:Invent 2023 - Live video streaming with Amazon CloudFront and Peacock (NET328)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=mttGiB6AEDg)
> 📅 2023-12-05 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon CloudFront]] [[Peacock]]

# Live Video Streaming with Amazon CloudFront and Peacock

## Overview of the Session

This AWS re:Invent 2023 session explores how AWS partners with major streaming providers to deliver live sporting events at massive scale to global audiences. The session centers on Peacock, NBCUniversal's streaming platform, which holds the distinction of offering more live sports than any other streamer in the United States. Through this collaboration, viewers can access premium sporting content across an extensive range of devices while maintaining the reliability and low latency that live events demand. The discussion brings together AWS technical experts and Peacock engineering leaders to demonstrate how cloud-native architectures enable streaming services to meet the demanding requirements of live broadcast.

## Architectural Approach to Live Streaming at Scale

### Optimizing Delivery with CloudFront and Origin Shield

Peacock's delivery architecture relies heavily on Amazon CloudFront, with Origin Shield playing a central role in optimizing performance during high-demand live events. By introducing an additional caching layer between CloudFront edge locations and the origin, Origin Shield significantly reduces the load placed on origin infrastructure. This design proves particularly valuable during major sporting events when millions of concurrent viewers request the same content simultaneously, allowing the platform to maintain low latency and high reliability without overwhelming origin servers. The architecture demonstrates how careful use of multi-tier caching can transform the economics and performance of live streaming, ensuring fans receive a consistent experience whether they are watching on smart TVs, mobile devices, or web browsers.

### End-to-End Workflow with AWS Elemental Media Services

Beyond content delivery, Peacock leverages AWS Elemental Media Services to construct a comprehensive end-to-end workflow that handles the full lifecycle of live video. This integrated approach connects ingest, encoding, packaging, and delivery into a cohesive pipeline purpose-built for live event streaming. The combination of Elemental services with CloudFront enables Peacock to scale dynamically as audience size fluctuates throughout an event, supporting the unpredictable demand patterns characteristic of live sports.

### Dynamic Advertising During Live Events

A particularly innovative aspect of Peacock's implementation involves the large-scale delivery of dynamic advertising woven into the live stream. The architecture supports server-side ad insertion that personalizes commercial content for individual viewers without disrupting the viewing experience or compromising stream quality. This capability allows Peacock to monetize live sports effectively while delivering targeted, relevant advertising at the moments when audience engagement peaks, transforming what would traditionally be uniform commercial breaks into personalized opportunities.

## Key Takeaways and Outcomes

The session illustrates how the partnership between AWS and Peacock results in a streaming platform capable of meeting the unique challenges of live sports delivery, where scale, latency, and reliability cannot be compromised. By combining CloudFront with Origin Shield, AWS Elemental Media Services, and dynamic ad insertion technologies, Peacock has built an architecture that not only handles peak concurrent viewership but also creates new business value through personalized advertising. The presentation serves as a practical reference for organizations looking to architect live streaming solutions on AWS, demonstrating that cloud-native approaches can match and exceed the capabilities of traditional broadcast infrastructure while offering the flexibility to innovate on monetization and viewer experience.