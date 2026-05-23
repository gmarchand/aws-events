---
clients:
- Netflix
- AWS
- Apache Cassandra
- EVCache
- Memcached
date: 2023-11-30
description: Netflix’s data platform serves tens of millions of requests per second
  at millisecond latency from their online data stores hosted on AWS, such as Apache
  Cassandra and EVCache (Memcached-based). In this session, learn how to use shadow
  traffic and unique capabilities of the cloud to migrate petabytes of data and millions
  of requests per second safely and without any risk of data loss or user-visible
  performance regression. By ensuring all operations are idempotent, using the cloud
  to launch shad
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- database
- migration
- netflix
- cloud
- cassandra
- streaming
thematic: media
title: AWS re:Invent 2023 - Safely migrate databases that serve millions of requests
  per second (NFX307)
url: https://www.youtube.com/watch?v=3bjnm1SXLlo
video_id: 3bjnm1SXLlo
year: 2023
---

# AWS re:Invent 2023 - Safely migrate databases that serve millions of requests per second (NFX307)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=3bjnm1SXLlo)
> 📅 2023-11-30 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]] [[Apache Cassandra]] [[EVCache]] [[Memcached]]

# Safely Migrating Databases at Netflix Scale

## Overview of the Challenge

Netflix operates one of the most demanding data platforms in the industry, serving tens of millions of requests per second at millisecond-level latency. The platform relies heavily on AWS-hosted online data stores, primarily Apache Cassandra for persistent storage and EVCache, a Memcached-based caching layer, for low-latency access. Migrating these systems while they continue to serve production traffic presents substantial engineering challenges, since even minor disruptions could affect the streaming experience for millions of users worldwide. The session explores how Netflix approaches these migrations safely, moving petabytes of data and millions of requests per second without data loss or user-visible performance regressions.

## Core Migration Strategy

### Shadow Traffic and Cloud-Native Capabilities

The foundation of Netflix's safe migration approach centers on shadow traffic, a technique that takes full advantage of cloud elasticity. Engineers provision parallel hardware in AWS that mirrors the existing production environment, then duplicate live traffic to flow through both the original and the new infrastructure simultaneously. This shadow environment allows teams to validate the behavior, performance, and correctness of the new system under real production load before any cutover occurs. Because the cloud makes it economically and operationally feasible to spin up large parallel fleets temporarily, Netflix can de-risk migrations in ways that would be prohibitive in traditional data centers.

### Idempotent Operations and Backfills

A critical design principle underpinning the migration strategy is ensuring that all operations are idempotent, meaning they can be safely retried or replayed without producing incorrect results. This property is essential when duplicating traffic and performing backfills of historical data, because it guarantees that running the same operation multiple times against the new system yields the same outcome as a single execution. By combining idempotent traffic replay with idempotent backfills of existing data, Netflix can populate the new database with both historical state and ongoing writes while preserving consistency. This approach eliminates the risk of data corruption or divergence between the source and target systems during the migration window.

### Validation and Cutover

With shadow infrastructure receiving duplicated traffic and backfills completing the historical data picture, engineers can directly compare responses, latencies, and error rates between the old and new systems. This continuous validation builds confidence that the new platform behaves identically to the existing one under real workloads. Once the new system demonstrates equivalence, traffic can be safely shifted, and the legacy infrastructure can be decommissioned without any user-visible regression.

## Key Takeaways

The session demonstrates that safe migrations of mission-critical, high-throughput databases are achievable when teams combine three reinforcing practices: leveraging the cloud to provision disposable shadow hardware, duplicating production traffic to validate new systems under realistic conditions, and designing all operations to be idempotent so that replays and backfills remain consistent. Together, these techniques allow Netflix to upgrade and migrate the foundational data stores behind its streaming service with confidence, even at a scale of petabytes and millions of requests per second.