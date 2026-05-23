---
clients:
- New York Times
- Amazon
- NetApp
- AWS
date: 2025-12-03
description: Learn and benefit from the New York Times successful FSx for ONTAP migration
  while understanding how to optimize the cost and performance of FSx for ONTAP for
  your workload. A New York Times storage architect will discuss best practices and
  field proven techniques for migrating your data to Amazon FSx for NetApp ONTAP.
  Discover time saving tips on how to increase scale, performance, and resilience
  by migrating to Amazon FSx for ONTAP. You’ll learn how to configure and optimize
  your FSx for NetAp
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- migration
- storage
- fsx
- ontap
- cloud-migration
- best-practices
thematic: media
title: 'AWS re:Invent 2025 - New York Times: Best practices for migration to Amazon
  FSx for ONTAP (STG212)'
url: https://www.youtube.com/watch?v=x0VDgkyaVyE
video_id: x0VDgkyaVyE
year: 2025
---

# AWS re:Invent 2025 - New York Times: Best practices for migration to Amazon FSx for ONTAP (STG212)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=x0VDgkyaVyE)
> 📅 2025-12-03 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[New York Times]] [[Amazon]] [[NetApp]] [[AWS]]

# Best Practices for Migrating to Amazon FSx for NetApp ONTAP: Lessons from The New York Times

## Overview of the Migration Journey

The New York Times undertook a significant storage modernization initiative by migrating its workloads to Amazon FSx for NetApp ONTAP, and a storage architect from the organization shared the lessons learned throughout this transformation. The session combined real-world migration experience with prescriptive guidance from AWS, offering attendees a practical blueprint for moving enterprise storage workloads to a fully managed cloud-native ONTAP service. The discussion centered on how the publication achieved greater scale, stronger resilience, and improved performance while simultaneously controlling costs through deliberate architectural choices.

## Migration Strategy and Field-Proven Techniques

### Planning and Executing the Move

The migration approach emphasized careful workload assessment, capacity planning, and the use of native NetApp data mobility tools such as SnapMirror to transfer data efficiently from on-premises ONTAP environments into FSx for ONTAP. By leveraging block-level replication and incremental synchronization, The New York Times minimized cutover windows and reduced disruption to production systems. The architect highlighted the importance of validating performance characteristics in advance, sizing file systems appropriately, and aligning throughput capacity with actual workload demand rather than overprovisioning from the outset.

### Time-Saving Practices for Enterprise Workloads

Throughout the migration, the team identified techniques that accelerated delivery while preserving data integrity. These included staging migrations in waves, automating repetitive provisioning tasks, and using multi-AZ deployments to ensure that failover behavior was tested before production cutover. The narrative made clear that treating the migration as an opportunity to reassess legacy storage practices, rather than simply lifting and shifting, yielded the strongest long-term outcomes.

## Optimizing Cost, Performance, and Resilience

### Configuration Best Practices

A substantial portion of the session focused on tuning FSx for ONTAP deployments for both performance and economics. The speakers walked through configuration choices such as selecting appropriate SSD capacity, enabling intelligent tiering to move infrequently accessed data to lower-cost capacity pools, and right-sizing throughput to match workload patterns. Auto-tiering emerged as a particularly impactful feature, allowing The New York Times to retain hot data on high-performance storage while transparently offloading cold data, thereby reducing overall storage spend without sacrificing accessibility.

### Resilience, Protection, and Operational Maturity

High availability, ransomware protection, and snapshot strategies formed the resilience pillar of the discussion. Multi-AZ file systems were recommended for production workloads requiring continuous availability, while frequent snapshots and SnapMirror-based replication provided defense in depth against data loss and ransomware events. The session reinforced that enabling these capabilities from day one, rather than retrofitting them later, simplifies operations and aligns with enterprise data protection requirements.

## Key Outcomes and Takeaways

The New York Times migration demonstrated that FSx for ONTAP can support demanding enterprise media workloads at scale while delivering the familiar ONTAP feature set in a fully managed form. The principal takeaways centered on disciplined planning, leveraging native replication tools for low-risk cutovers, embracing tiering and snapshot features for cost and resilience benefits, and treating cloud migration as a chance to modernize operational practices. Attendees left with a clear, field-tested framework for replicating this success in their own environments.