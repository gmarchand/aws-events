---
clients:
- AWS
- Amazon Route 53
date: 2023-12-02
description: Building highly resilient applications in the cloud requires building
  across multiple Availability Zones, capacity planning for redundancy, and having
  mechanisms in place to ensure that requests are routed away from occasional, temporary
  failures—both hard and gray—in an Availability Zone. Learn how you can design and
  monitor applications to detect and automatically recover from failures within Availability
  Zones using capabilities such as the Amazon Route 53 Application Recovery Controller
  zona
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- cloud
- resilience
- availability-zones
- autoshift
- disaster-recovery
thematic: media
title: AWS re:Invent 2023 - Using zonal autoshift to automatically recover from an
  AZ impairment (ARC309)
url: https://www.youtube.com/watch?v=_0F-wdwiqZo
video_id: _0F-wdwiqZo
year: 2023
---

# AWS re:Invent 2023 - Using zonal autoshift to automatically recover from an AZ impairment (ARC309)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=_0F-wdwiqZo)
> 📅 2023-12-02 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon Route 53]]

# Using Zonal Autoshift to Automatically Recover from an AZ Impairment

## Building Resilience Across Availability Zones

Constructing highly resilient applications in the cloud demands more than simply deploying workloads to AWS — it requires deliberate architectural choices that span multiple Availability Zones (AZs). This session emphasizes that true resilience comes from distributing workloads across AZs, planning capacity to absorb the loss of an entire zone, and instrumenting applications with mechanisms that detect and react to failures before they cascade into customer-facing impact. The discussion frames Availability Zones as physically isolated fault domains within an AWS Region, making them the foundational building block for high availability when paired with thoughtful application design.

A central theme is the distinction between hard failures, which are unambiguous outages that monitoring systems detect quickly, and gray failures, which manifest as subtle degradations such as elevated latency, intermittent errors, or partial impairments that are notoriously difficult to diagnose. Because gray failures often evade traditional health checks, applications must be engineered with the assumption that an AZ may behave incorrectly without ever fully going down, and operators need tooling that can shift traffic away from suspect zones quickly and confidently.

## Zonal Shift and Zonal Autoshift in Route 53 ARC

### How Zonal Shift Works

Amazon Route 53 Application Recovery Controller (ARC) provides zonal shift as a primary mechanism for evacuating traffic from an impaired Availability Zone. With a single API call or console action, customers can temporarily remove an AZ from rotation behind supported load balancers, causing new requests to be routed only to the healthy zones. This approach allows teams to recover from impairments in minutes rather than hours, without requiring code changes, DNS manipulation, or complex failover orchestration. The session highlights that zonal shift is most effective when applications have been pre-scaled across zones so that the remaining AZs can absorb the redirected load — reinforcing the importance of static stability and capacity planning ahead of any failure event.

### Introducing Zonal Autoshift

Building on manual zonal shift, AWS introduced zonal autoshift, which removes the human from the critical path during an AZ impairment. When customers opt in, AWS continuously monitors signals across its infrastructure and, upon detecting an AZ impairment that warrants action, automatically shifts traffic away from the affected zone on the customer's behalf. Once AWS determines the zone is healthy again, traffic is gradually returned. This automation is particularly valuable for gray failures, where AWS internal telemetry can identify problems faster and more accurately than customer-side monitoring alone.

### Practice Runs and Safe Adoption

To help customers adopt autoshift with confidence, the service includes practice runs that periodically simulate a zonal shift on a schedule defined by the customer. These weekly exercises validate that the application truly tolerates the loss of an AZ, that capacity is sufficient in the remaining zones, and that alarms behave as expected. Practice runs are gated by customer-supplied outcome alarms, which automatically cancel or block a shift if the application shows signs of distress, ensuring that the resilience mechanism itself never becomes a source of impact. This continuous testing addresses a common operational pitfall: resilience capabilities that exist on paper but have never been exercised in production.

## Operational Guidance and Outcomes

The session closes with practical guidance for teams adopting these capabilities. Workloads should be architected for static stability, meaning they continue to operate correctly using only resources that are already provisioned, without relying on control-plane actions during a failure. Capacity should be pre-provisioned to handle the loss of one AZ, alarms should be tuned to reflect real customer experience, and dependencies should themselves be zonally aware so that a shift at one layer is not undone by an unaware downstream service. By combining multi-AZ architecture, zonal shift for manual recovery, and zonal autoshift with practice runs for automated protection, customers can dramatically reduce the time to recover from both hard and gray AZ impairments and deliver a markedly more reliable experience to their end users.