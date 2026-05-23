---
clients:
- Netflix
- AWS
date: 2021-12-17
description: Netflix continues to grow at an astonishing rate. With more subscribers
  and productions than ever, the network must continue to scale to connect it all.
  In this session, follow the Cloud Networking team on a journey to understand the
  scaling challenges that Netflix faces with IPv4 and the drivers for IPv6. Explore
  design patterns and architectural flaws that fundamentally shape the design of most
  VPC networks. Get insight into the close collaboration and co-innovation between
  Netflix and AWS tha
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- ipv6
- networking
- cloud
- aws
- netflix
- scaling
- streaming
thematic: media
title: AWS re:Invent 2021 - How Netflix is using IPv6 to enable hyperscale networking
url: https://www.youtube.com/watch?v=1DF6yIFIx14
video_id: 1DF6yIFIx14
year: 2021
---

# AWS re:Invent 2021 - How Netflix is using IPv6 to enable hyperscale networking

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=1DF6yIFIx14)
> 📅 2021-12-17 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[Netflix]] [[AWS]]

# How Netflix Is Using IPv6 to Enable Hyperscale Networking

## Introduction and Context

Netflix continues to expand at a remarkable pace, adding subscribers, content productions, and supporting infrastructure that all depend on a network capable of connecting an ever-growing footprint. In this AWS re:Invent 2021 session, the Netflix Cloud Networking team shares the journey their organization has taken to confront the scaling limits of IPv4 within AWS, and how adopting IPv6 has fundamentally reshaped the way Netflix designs its cloud network. The session frames IPv6 not as a theoretical future but as a practical, present-day enabler for hyperscale workloads, and it highlights the close partnership between Netflix and AWS engineering teams that helped bring this vision to fruition.

## Scaling Challenges and the Drive Toward IPv6

### Hitting the Limits of IPv4 in the VPC

The core motivation behind Netflix's IPv6 adoption is the address-space scarcity inherent to IPv4. As Netflix's footprint grew across multiple AWS accounts, regions, and workloads, the team repeatedly encountered constraints rooted in the limited supply of RFC 1918 private address space. Allocating sufficiently large CIDR blocks to each VPC became increasingly difficult, and overlapping address space across acquisitions, partner networks, and internal services compounded the problem. These challenges did not just create operational friction — they began shaping architectural decisions in ways the team felt were unhealthy, forcing engineers to design around address scarcity rather than around the needs of the application.

### Architectural Flaws Imposed by IPv4

The presentation walks through how IPv4 scarcity manifests as recurring design patterns: heavy reliance on NAT, complex address-management tooling, careful subnet sizing, and the proliferation of private link and proxy layers to bridge networks with conflicting addresses. Each of these workarounds adds latency, cost, and operational complexity. The team makes the case that many "best practices" in VPC design exist primarily because IPv4 forces them, and that IPv6 dissolves the underlying problem rather than merely managing its symptoms.

### Why IPv6 Changes the Equation

With IPv6, Netflix gains effectively unlimited address space, allowing every workload, container, and ephemeral resource to receive a globally unique address without contention. This eliminates overlap concerns across accounts and regions, removes the need for many NAT layers, and makes connectivity between services dramatically simpler. The team emphasizes that the simplicity IPv6 provides is itself a feature — networks become easier to reason about, and entire categories of operational toil disappear.

## Co-Innovation With AWS and Lessons Learned

### Collaboration That Produced Prefix Delegation

A central thread of the talk is the tight collaboration between Netflix and AWS that drove new capabilities such as prefix delegation for elastic network interfaces. Early implementations of IPv6 on AWS did not always meet Netflix's density and performance requirements, particularly for container workloads where each pod or task needs its own routable address. By working closely with AWS service teams, Netflix helped shape features that allow ENIs to receive contiguous IPv6 prefixes, dramatically increasing the number of addresses available per instance and unlocking high-density container networking. The session illustrates how an unimpressive initial feature evolved, through a tight feedback loop between customer and provider, into a capability that meaningfully changes what is possible at scale.

### Practical Guidance for Adopters

The team offers motivation and practical perspective for organizations considering their own IPv6 journey. They acknowledge that adoption is incremental, that dual-stack designs remain important during transition, and that tooling, observability, and security controls all need to evolve alongside the addressing change. However, they argue that the long-term simplification and the removal of architectural compromises imposed by IPv4 more than justify the investment. The session closes by encouraging attendees to look critically at the constraints shaping their own VPC designs and to consider whether IPv6 could remove those constraints entirely.

## Outcomes and Takeaways

By embracing IPv6, Netflix has positioned its cloud network to scale with the business rather than against it, replacing brittle workarounds with a cleaner, more uniform addressing model. The partnership with AWS demonstrates how hyperscale customers can drive platform improvements that benefit the broader community, with prefix delegation standing out as a concrete example. The overarching message is that IPv6 is ready for serious production use on AWS today, that it offers genuine architectural simplification, and that organizations facing IPv4 scaling pain should treat IPv6 adoption as a strategic enabler rather than a distant aspiration.