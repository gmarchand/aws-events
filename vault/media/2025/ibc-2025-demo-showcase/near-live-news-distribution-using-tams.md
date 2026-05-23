---
clients:
- Reuters
- AWS
- UK Parliamentary Broadcasting Unit
date: 2025-09-29
description: Distributing near-live news and sports content to partners remains inefficient,
  relying on costly, point-to-point delivery methods that create delays. We demonstrate
  how a news agency - Reuters - solves this by leveraging the open-source Time-Addressable
  Media Store (TAMS) API on AWS. In this live demonstration, Reuters publishes feeds
  of content from the UK Parliamentary Broadcasting Unit into TAMS, allowing its customers
  to immediately access, clip, and pull the segments they need on demand. T
event: ibc-2025-demo-showcase
has_transcript: true
language: en
playlist: IBC 2025 Demo Showcase
tags:
- news
- live
- sports
- tams
- aws
- distribution
- api
thematic: media
title: Near-live news distribution using TAMS
url: https://www.youtube.com/watch?v=9v3xAXfsVh4
video_id: 9v3xAXfsVh4
year: 2025
---

# Near-live news distribution using TAMS

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=9v3xAXfsVh4)
> 📅 2025-09-29 | 🎤 ibc-2025-demo-showcase | 🌐 en
> 🏢 Clients: [[Reuters]] [[AWS]] [[UK Parliamentary Broadcasting Unit]]

# Near-Live News Distribution Using TAMS

## Rethinking the News Supply Chain

Distributing near-live news and sports content has long been one of the most inefficient processes in the broadcast industry. Traditional workflows depend on costly, point-to-point delivery methods such as dedicated satellite links, fiber circuits, and bespoke file transfers between agencies and their customers. These approaches introduce delays, limit flexibility, and force broadcasters to receive entire feeds when they often need only short clips. As newsrooms shift toward digital-first publishing and faster turnaround times, the limitations of this legacy supply chain have become increasingly difficult to justify.

This session demonstrates how Reuters, one of the world's largest news agencies, is addressing these challenges by adopting the Time-Addressable Media Store (TAMS) API running on AWS. By moving away from rigid distribution pipes toward a cloud-native, interoperable model, Reuters is reshaping how content reaches its global customer base.

## How TAMS Transforms Content Distribution

### The Time-Addressable Media Store Approach

TAMS is an open-source API specification that treats media as time-addressable segments stored in object storage rather than as monolithic files or continuous streams. Each piece of content is broken into small, individually retrievable segments indexed by time, allowing consumers to request precisely the portion of a feed they need. Because the specification is open, it enables true interoperability between vendors, agencies, and customers, removing the lock-in associated with proprietary distribution systems. Running TAMS on AWS provides the scalability, durability, and global reach required to serve an international customer base without provisioning dedicated infrastructure for each partner.

### Live Demonstration with Reuters and UK Parliamentary Broadcasting

In the live demonstration, Reuters ingests feeds from the UK Parliamentary Broadcasting Unit directly into TAMS. As the content is written into the store, it becomes immediately available to Reuters customers, who can browse the timeline, identify the moments relevant to their editorial needs, and clip or pull only those segments on demand. This eliminates the need to deliver full feeds to every customer and removes the latency associated with traditional handoffs. The same source material can serve many downstream consumers simultaneously, each extracting different segments based on their own requirements.

### Efficiency and Flexibility Gains

The outcome is a contribution and distribution supply chain that is dramatically more efficient than point-to-point alternatives. Customers gain near-live access to content with the flexibility to retrieve exactly what they need, while Reuters reduces the operational overhead of managing multiple bespoke delivery paths. The interoperable nature of TAMS also positions both the agency and its partners to integrate additional tools — such as automated metadata enrichment, AI-driven highlight detection, and cloud-based editing — directly against the same media store. The result is a faster, more cost-effective, and more adaptable model for distributing live news and sports content at scale.