---
clients:
- Netflix
- Amazon
- AWS
date: 2025-12-07
description: From storing media content to machine learning training data, Netflix
  relies on Amazon S3 to support a wide range of use cases. As data grows exponentially,
  organizations need tools to understand and optimize their storage footprint. S3
  Storage Lens provides organization-wide visibility into storage usage and activity,
  enabling companies to optimize costs, improve performance, and strengthen data protection.
  In this session, discover how Netflix uses S3 Storage Lens alongside S3 Inventory
  and se
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- s3
- storage
- netflix
- cloud
- data-analytics
- reinvent
thematic: media
title: AWS re:Invent 2025 - How Netflix uses Amazon S3 Storage Lens to track exabytes
  of data (STG214)
url: https://www.youtube.com/watch?v=Q2YoHfhFuI8
video_id: Q2YoHfhFuI8
year: 2025
---

# AWS re:Invent 2025 - How Netflix uses Amazon S3 Storage Lens to track exabytes of data (STG214)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=Q2YoHfhFuI8)
> 📅 2025-12-07 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[Amazon]] [[AWS]]

# How Netflix Uses Amazon S3 Storage Lens to Track Exabytes of Data

## Session Overview

This AWS re:Invent 2025 session (STG214) explores how Netflix manages and optimizes one of the largest data estates in the world using Amazon S3 Storage Lens in conjunction with complementary tools such as S3 Inventory and server access logs. As Netflix's data footprint has grown to encompass exabytes spanning media content, machine learning training datasets, and operational workloads, the company has had to adopt sophisticated tooling to maintain visibility, control costs, and ensure performance at scale. The presentation positions S3 Storage Lens as a foundational capability for organizations facing similar exponential data growth challenges.

## Netflix's Storage Challenges and Approach

### The Scale of Netflix's S3 Footprint

Netflix relies on Amazon S3 for an exceptionally broad range of workloads, from storing the streaming media that powers its global service to housing the training data that fuels its machine learning initiatives. At exabyte scale, traditional approaches to storage analysis quickly break down, and even small inefficiencies translate into significant cost and performance implications. The session emphasizes that as data volumes grow exponentially, organizations cannot rely on intuition or sampling alone — they need tooling capable of providing comprehensive, organization-wide visibility into how storage is being used and accessed.

### Combining Storage Lens with Inventory and Access Logs

Rather than treating S3 Storage Lens as a standalone solution, Netflix uses it alongside S3 Inventory and S3 server access logs to build a complete picture of its storage estate. Storage Lens delivers aggregated metrics and trends across the organization, S3 Inventory provides object-level detail for deep analysis, and server access logs surface granular request patterns. Together, these data sources enable Netflix to identify optimization opportunities, diagnose performance bottlenecks, and make informed decisions about data lifecycle management across billions of prefixes.

### Optimization, Performance, and Data Protection Outcomes

By applying these tools systematically, Netflix is able to optimize costs by identifying underutilized or improperly tiered data, improve performance by spotting hot prefixes and request patterns that could benefit from redistribution, and strengthen data protection by ensuring policies are consistently applied across the entire estate. The combined visibility allows the team to act proactively rather than reactively when issues arise at scale.

## Key Takeaways for AWS Customers

### S3 Storage Lens Capabilities Highlighted

The session showcases several capabilities of S3 Storage Lens that are particularly valuable for large-scale customers, including organization-wide dashboards, visibility into performance bottlenecks, and simplified analysis across billions of prefixes. These features remove much of the operational burden traditionally associated with understanding very large S3 footprints, making it feasible to derive actionable insights without building extensive custom tooling.

### Lessons from Netflix's Practices

The broader lesson presented is that effective storage management at scale requires layering multiple visibility tools, each providing a different lens on the same underlying data. Customers operating at significantly smaller scales than Netflix can still apply the same principles — using Storage Lens for high-level trends, Inventory for detailed object analysis, and access logs for request-level investigation — to drive cost savings, performance improvements, and stronger governance over their own S3 environments.